
import time
import signal

import g
from Area import AREA_LOBBY, AREA_TOWN, AREA_DUNGEON, AREA_ARENA, Area
from Player import Player

CHANNEL_ADD_PLAYER = -1
CHANNEL_REMOVE_PLAYER = -2

def handle_message_no_1(conn_id, req_msg_type, req_msg_body):
    return (conn_id, 1, b'handle_message_no_1:' + req_msg_body, True)

HANDLERS = {}
HANDLERS[1] = handle_message_no_1

class Channel:
    def __init__(self):
        signal.signal(signal.SIGINT, self.stop)
        signal.signal(signal.SIGTERM, self.stop)

        self.is_running = True
        self.max = 100
        self.players = {}
        self.area_id = 0
        self.areas = {}
        self.areas[self.area_id] = Area(AREA_LOBBY)
        self.area_id += 1

    def run(self, incoming, outgoing):
        while self.is_running:
            i = 0
            while i < self.max and not incoming.empty():
                i += 1

                print('incoming_get')
                (conn_id, req_msg_type, req_msg_body) = incoming.get()
                print(conn_id)
                print(req_msg_type)
                print(req_msg_body)
                if req_msg_type == CHANNEL_ADD_PLAYER:
                    print('add_player')
                    area_id = 0
                    self.players[conn_id] = Player(area_id)
                    self.areas[area_id].player_conn_ids.append(conn_id)

                elif req_msg_type == CHANNEL_REMOVE_PLAYER:
                    print('remove_player')
                    area_id = self.players[conn_id].area_id
                    self.areas[area_id].player_conn_ids.remove(conn_id)
                    del self.players[conn_id]

                else:
                    print(req_msg_type)
                    print('else')
                    if HANDLERS[req_msg_type] is not None:
                        (conn_id, ack_msg_type, ack_msg_body, broadcast) = HANDLERS[req_msg_type](
                            conn_id, req_msg_type, req_msg_body)

                    if broadcast:
                        area_id = self.players[conn_id].area_id
                        for player_conn_id in self.areas[area_id].player_conn_ids:
                            outgoing.put([player_conn_id, ack_msg_type, ack_msg_body])

                    else:
                        outgoing.put([conn_id, ack_msg_type, ack_msg_body])

            for area in self.areas.values():
                area.run()

            time.sleep(3.0 / 1000.0)

    def stop(self, signal_num, frame_obj):
        self.is_running = False

