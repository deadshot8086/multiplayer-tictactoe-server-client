
# Tic-Tac-Toe

Multiplayer TicTacToe game with *Sockets & MultiThreading*
Server can host multiple games each on different Threads

# Model
*ConnectionListener* is in Main thread, when two or more client connects, it creates *GameHandler* in serepate thread

![Model](https://github.com/adityabadhiye/multiplayer-tictactoe-server-client/blob/master/images/model.png)

# How to Play?
- Start the Server
```bash
python3 main.py
```
![Server](https://github.com/adityabadhiye/multiplayer-tictactoe-server-client/blob/master/images/server.png)

- Start the client
```bash
python3 server.py <PlayerName>
```
![Client](https://github.com/adityabadhiye/multiplayer-tictactoe-server-client/blob/master/images/client.png)