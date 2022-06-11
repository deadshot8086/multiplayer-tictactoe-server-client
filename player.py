# Player class contains basic properties of player like its name, socket ...
from helper import send, recv


class Player:
    def __init__(self, conn, addr, name, mark):
        self.conn = conn
        self.addr = addr
        self.name = name
        self.mark = mark