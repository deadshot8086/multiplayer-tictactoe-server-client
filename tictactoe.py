# Main game file, contains all logic, state, players, rules ... of game.
from helper import *
from state import GameState


class TicTacToe:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.state = GameState(N)
        send(self.player1.conn, State.PLAYER_CONNECTED)
        send(self.player2.conn, State.PLAYER_CONNECTED)
        while self.state.isRunning:
            self.listen_for_move()

    def listen_for_move(self):  # Function for receiving and making moves
        if self.state.turn == 0:  # If player X turn
            # Inform players about their turns
            send(self.player1.conn, State.YOUR_TURN)
            send(self.player2.conn, State.NOT_YOUR_TURN)
            # Get move from player
            msg = recv(self.player1.conn)
            # if msg == State.DISCONNECT:
            #     self.stop()
            #     return
            msg = [int(x) for x in msg.split(' ')]
            # Make move from GameState class
            ret = self.state.move(self.player1, msg[0], msg[1])
            if ret != 0:  # If not unsuccessful send and update client state
                send(self.player1.conn, (msg[0], msg[1], self.player1.mark))
                send(self.player2.conn, (msg[0], msg[1], self.player1.mark))
            if ret == State.WIN:  # Winning state
                self.win(self.player1, self.player2)
            if ret == State.DRAW:  # Draw state
                self.draw()
        else:  # If player Y turn
            send(self.player2.conn, State.YOUR_TURN)
            send(self.player1.conn, State.NOT_YOUR_TURN)
            msg = recv(self.player2.conn)
            # if msg == State.DISCONNECT:
            #     self.stop()
            #     return
            msg = [int(x) for x in msg.split(' ')]
            ret = self.state.move(self.player2, msg[0], msg[1])
            if ret != 0:
                send(self.player1.conn, (msg[0], msg[1], self.player2.mark))
                send(self.player2.conn, (msg[0], msg[1], self.player2.mark))
            if ret == State.WIN:
                self.win(self.player2, self.player1)
            if ret == State.DRAW:
                self.draw()

    def win(self, win, lose):  # Function to send win/lose message
        send(win.conn, State.WIN)
        send(lose.conn, State.LOSE)
        self.stop()

    def draw(self):  # Function to send draw message
        send(self.player1.conn, State.DRAW)
        send(self.player2.conn, State.DRAW)
        self.stop()

    def stop(self):  # Function to stop and close connection
        self.state.isRunning = False
        # send(self.player1.conn, State.DISCONNECT)
        # send(self.player2.conn, State.DISCONNECT)
        self.player1.conn.close()
        self.player2.conn.close()
