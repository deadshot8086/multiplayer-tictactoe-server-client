# Contains constant variables and methods.
from pickle import dumps, loads
import enum
import select

FORMAT = 'utf-8'
HEADERSIZE = 10
# DISCONNECT_MSG = "!DISCONNECT"
# PLAYER_CONNECTED = "!PLAYER_CONNECTED"
MARK = ('X', 'O')
N = 3


# common used enum words/states
class State(enum.Enum):
    PLAYER_CONNECTED = 0
    DISCONNECT = 1
    YOUR_TURN = 2
    NOT_YOUR_TURN = 3
    WIN = 4
    LOSE = 5
    DRAW = 6


# for sending msg to socket
def send(socket, msg):
    msg = dumps(msg)
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', FORMAT) + msg
    socket.sendall(msg)


# for receiving msg from socket
def recv(socket):
    full_msg = b''
    new_msg = True
    while True:
        msg = socket.recv(4096)
        if new_msg:
            msglen = int(msg[:HEADERSIZE])
            new_msg = False
        full_msg += msg
        if len(full_msg) - HEADERSIZE >= msglen:
            d = loads(full_msg[HEADERSIZE:])
            break
    return d
