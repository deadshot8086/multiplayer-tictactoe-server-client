# Client script.
import socket
import sys
from helper import *


IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDR = (IP, PORT)


def main():
    name = sys.argv[1]
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect(ADDR)
    board = [[' ' for x in range(N)] for y in range(N)]

    def print_board():
        # for _ in board:
        #     print(_)
        print(f'''                   A   B   C

               1   {board[0][0]} ║ {board[0][1]} ║ {board[0][2]}
                  ═══╬═══╬═══
               2   {board[1][0]} ║ {board[1][1]} ║ {board[1][2]}
                  ═══╬═══╬═══
               3   {board[2][0]} ║ {board[2][1]} ║ {board[2][2]}''')

    send(server, name)
    print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")
    print("[WAITING] waiting for player to join")
    msg = recv(server)
    if msg == State.PLAYER_CONNECTED:
        print(f"[SERVER] Player Connected")
        print_board()
    while True:
        msg = recv(server)
        if msg == State.DISCONNECT:
            server.close()
            break
        elif msg == State.YOUR_TURN:
            print("YOUR TURN")
            send(server, input("> "))
        elif msg == State.NOT_YOUR_TURN:
            print("OPPONENT TURN")
        elif msg == State.WIN:
            print_board()
            print("you win!!")
            server.close()
            break
        elif msg == State.LOSE:
            print_board()
            print("you lose!!")
            server.close()
            break
        elif msg == State.DRAW:
            print_board()
            print("game draw!!")
            server.close()
            break
        else:
            board[msg[0]][msg[1]] = msg[2]
            print_board()


if __name__ == "__main__":
    main()
