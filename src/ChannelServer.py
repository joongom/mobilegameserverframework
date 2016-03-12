
import sys
import multiprocessing
import asyncio
import concurrent.futures
import signal

import g
from ChannelConnection import handle_internal, handle_outgoing
from ChannelConnection import ChannelConnection
from Channel import Channel

import config
import logger

def main():
    if len(sys.argv) < 3:
        print('Usage: sudo python3 ./ChannelServer.py develop 00')
        sys.exit()

    phase = sys.argv[1]
    server_seq = sys.argv[2]
    server_id = 'server' + server_seq

    config.load(phase)
    logger.init('channel', server_seq)
    #master.load(phase)

    # queues and pool
    g.INCOMING = multiprocessing.Queue()
    g.INTERNAL = multiprocessing.Queue()
    g.OUTGOING = multiprocessing.Queue()
    g.PROCPOOL = concurrent.futures.ProcessPoolExecutor(g.CFG[server_id]['channel_process_pool_size'])

    # channel
    channel = Channel()
    process = multiprocessing.Process(target=channel.run, args=())
    process.start()

    # channel_server
    loop = asyncio.get_event_loop()
    loop.add_signal_handler(signal.SIGINT, loop.stop)
    loop.add_signal_handler(signal.SIGTERM, loop.stop)

    loop.create_task(handle_internal())
    loop.create_task(handle_outgoing())

    coro = loop.create_server(ChannelConnection, port=g.CFG[server_id]['channel_port'])
    channel_server = loop.run_until_complete(coro)

    for sock in channel_server.sockets:
        print('channel_server_{} starting.. {}'.format(server_seq, sock.getsockname()))

    try:
        g.LOG.info('channel_server_%s starting.. port %s',
                   server_seq, g.CFG[server_id]['channel_port'])
        loop.run_forever()

    except KeyboardInterrupt:
        g.LOG.info('keyboard interrupt..')

    channel_server.close()
    loop.run_until_complete(channel_server.wait_closed())
    loop.close()

    g.INCOMING.close()
    g.INTERNAL.close()
    g.OUTGOING.close()
    g.PROCPOOL.shutdown()

    process.join()

if __name__ == '__main__':
    main()

