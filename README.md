
# Tic-Tac-Toe

Multiplayer TicTacToe game with *Sockets & MultiThreading*
Server can host multiple games each on different Threads

# Internal Working

## Model
*ConnectionListener* is in Main thread, when two or more client connects, it calls *GameHandler* in serepate thread.
*GameHandler* then creates seperate instance of class *TicTacToe* which takes two *Player* class object, when game ends, resulting winning/losing/draw state is stored in *state* class object, which can be then retrived by *GameHandler* and it calls *increase_score* method which updates and print global *score_board* via mutex lock.

![Model](https://github.com/adityabadhiye/multiplayer-tictactoe-server-client/blob/master/images/model.png)

## Use of Mutex
Since we are creating seperate objects for different game which are *threadsafe* so we don't need to worry about mutex in case of client-to-client communication.

But in the case of server-client communication eg updating *global scoreboard*, we need to use *Mutex Locks*, so that each thread/client updates score_board one at a time.

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

# Demo Video



https://user-images.githubusercontent.com/76732801/174389937-16122633-8d46-4cf3-9a64-9ae50af9059f.mp4



# Learnings
- Learned creating code with OOPS concepts
- Learned working of multithreading, thread synchronization and use of mutex
- Learned concepts of sockets, and blocking functions

# References
- https://www.tutorialspoint.com/python/python_multithreading.htm#:~:text=The%20threading%20module%20provided%20with,force%20threads%20to%20run%20synchronously.
- https://superfastpython.com/thread-mutex-lock/
- https://realpython.com/python-sockets/
- https://docs.python.org/3/library/socket.html
