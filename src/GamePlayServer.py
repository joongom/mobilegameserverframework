
import logging, logging.handlers
import json
import multiprocessing
import asyncio
import struct
import sys
import signal
import time

import google.protobuf
'''
import msg_type_play_pb2
import msg_enum_pb2
import msg_struct_pb2
import msg_packet_play_pb2

import AESCrypto
'''

from GameChannel import GameChannel
from Session import Session

'''
struct
{
	int32_t msg_type; // 4 bytes
	int32_t msg_size; // 4 bytes
}
// totally 8 bytes
'''
msg_head_size = 8

log = logging.getLogger()
cfg = {}
mst = {}
connections = []

@asyncio.coroutine
def handle_message_no_1(req_msg_type, req_msg_body):
	print('message_no_1')
	return req_msg_body

handlers = {
	1:handle_message_no_1,
}

def init_pool():
	signal.signal(signal.SIGINT, signal.SIG_IGN)

channel = GameChannel()
channel_service = multiprocessing.Pool(1, init_pool)

class GamePlayServer(asyncio.Protocol):
	def __init__(self):
		self.timeout_sec = 1800.0
		self.msg_buffer = b''

	@asyncio.coroutine
	def handle_received(self, req_msg_type, req_msg_body):
		print('handle_received')
		if handlers[req_msg_type] is None:
			return

		(ack_msg_type, ack_msg_body) = yield from handlers[req_msg_type](req_msg_type, req_msg_body)
		ack = struct.pack('ii', ack_msg_type, msg_head_size + len(ack_msg_body)) + ack_msg_body

		self.transport.write(ack)

	def connection_made(self, transport):
		self.transport = transport
		self.h_timeout = asyncio.get_event_loop().call_later(self.timeout_sec, self.connection_timed_out)
		connections.append(self)
		session = Session(self)

	def data_received(self, data):
		self.h_timeout.cancel()
		self.h_timeout = asyncio.get_event_loop().call_later(self.timeout_sec, self.connection_timed_out)

		print(data)
		return
		if len(data) > 8192:
			return

		self.msg_buffer += data
		msg_head_offset = 0

		while len(self.msg_buffer) >= (msg_head_offset + msg_head_size):
			msg_body_offset = msg_head_offset + msg_head_size
			(msg_type, msg_size) = struct.unpack('ii', self.msg_buffer[msg_head_offset:msg_body_offset])

			msg_end_offset = msg_head_offset + msg_size
			if len(self.msg_buffer) < msg_end_offset:
				break

			msg_body = self.msg_buffer[msg_body_offset:msg_end_offset]
			msg_head_offset = msg_end_offset

			asyncio.Task(self.handle_received(msg_type, msg_body))

		self.msg_buffer = self.msg_buffer[msg_head_offset:]

		#print(data)
		#for conn in connections:
			#if conn is not self:
				#conn.transport.write(ack)

	def eof_received(self):
		pass

	def connection_lost(self, ex):
		self.h_timeout.cancel()
		connections.remove(self)

	def connection_timed_out(self):
		self.transport.close()

	def set_session(self, sess):
		self.sess = sess

def main():
	if len(sys.argv) < 3:
		print('Usage: sudo python3 ./GamePlayServer.py develop 00')
		sys.exit()

	phase = sys.argv[1]
	server_seq = sys.argv[2]

	# cfg
	with open('../cfg/' + phase + '.json', encoding='utf-8') as cfg_file:
		cfg = json.loads(cfg_file.read())

	# log
	log_level = None
	log_rotation = None

	if cfg['log']['level'] == 'debug':
		log_level = logging.DEBUG
	elif cfg['log']['level'] == 'info':
		log_level = logging.INFO
	elif cfg['log']['level'] == 'warn':
		log_level = logging.WARNING
	elif cfg['log']['level'] == 'error':
		log_level = logging.ERROR
	else:
		log_level = logging.DEBUG

	if cfg['log']['rotation'] == 'every_minute':
		log_rotation = 'M'
	elif cfg['log']['rotation'] == 'hourly':
		log_rotation = 'H'
	elif cfg['log']['rotation'] == 'daily':
		log_rotation = 'D'
	else:
		log_rotation = 'M'

	log_formatter = logging.Formatter('%(asctime)s,%(levelname)s,%(message)s')
	log_handler = logging.handlers.TimedRotatingFileHandler('../log/game_play_server_' + server_seq + '.csv', when=log_rotation, interval=1)
	log_handler.setFormatter(log_formatter)

	log.setLevel(log_level)
	log.addHandler(log_handler)

	# channel_service
	channel_service.apply_async(channel.run)

	# server
	server_id = 'server' + server_seq

	# play_server
	loop = asyncio.get_event_loop()
	loop.add_signal_handler(signal.SIGINT, loop.stop)
	loop.add_signal_handler(signal.SIGTERM, loop.stop)

	f = loop.create_server(GamePlayServer, port=cfg[server_id]['play_port'])
	play_server = loop.run_until_complete(f)

	for s in play_server.sockets:
		print('game_play_server_{} starting.. {}'.format(server_seq, s.getsockname()))

	try:
		log.info('game_play_server_%s starting.. port %s', server_seq, cfg[server_id]['play_port'])
		loop.run_forever()

	except KeyboardInterrupt:
		log.info('keyboard interrupt..')
		play_server.close()
		loop.run_until_complete(play_server.wait_closed())
		loop.close()

		channel_service.apply_async(channel.stop)

	else:
		play_server.close()
		loop.run_until_complete(play_server.wait_closed())
		loop.close()

		channel_service.apply_async(channel.stop)

if __name__ == '__main__':
	main()

