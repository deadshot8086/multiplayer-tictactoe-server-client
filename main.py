# Main server starting file.
import socket
import threading
from collections import deque
from helper import recv, MARK
from player import Player
from tictactoe import TicTacToe

IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDR = (IP, PORT)


# this function runs in separate thread, creates game between two socket
def handle_client(conn1, addr1, conn2, addr2):
    name1 = recv(conn1)
    name2 = recv(conn2)
    player1 = Player(conn1, addr1, name1, MARK[0])
    player2 = Player(conn2, addr2, name2, MARK[1])
    print(f"[GAME STARTED] {name1} vs {name2}")
    print(f"[ACTIVE GAMES] {threading.activeCount() - 1}")
    TicTacToe(player1, player2)
    # game = TicTacToe(player1, player2)
    # del game
    print(f"[GAME ENDED] {name1} vs {name2}")
    print(f"[ACTIVE GAMES] {threading.activeCount() - 2}")


def main():
    print("[STARTING] Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}:{PORT}")
    queue = deque()
    while True:
        # listens for sockets, if found, add in queue
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected")
        queue.append((conn, addr))
        # if len(queue) >= 2 then we can make game with a pair of 2
        while len(queue) >= 2:
            (conn1, addr1) = queue.popleft()
            (conn2, addr2) = queue.popleft()
            thread = threading.Thread(target=handle_client, args=(conn1, addr1, conn2, addr2))
            thread.start()


if __name__ == "__main__":
    main()
