import contextlib
import pickle
import socket
from _thread import start_new_thread

from .game import Game

server = "Your IP"  # Server's IP address
port = 5555  # Port number for the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object

try:
    s.bind((server, port))  # Bind the socket to the server and port
except Exception as e:
    print(f"Caught an exception: {e}")

s.listen(2)  # Listen for connections, allowing a queue of up to 2
print("Waiting for a connection, Server Started")

connected = set()  # Keep track of connected clients (not used in this snippet)
games = {}  # Dictionary to store games by gameId
idCount = 0  # Counter to keep track of the number of connections


def threaded_client(conn, p, gameId):
    """
    Handle client connections in a separate thread.
    :param conn: The connection object to the client.
    :param p: Player number (0 or 1).
    :param gameId: The ID of the game the player is in.
    """
    global idCount  # Need to modify the global idCount
    conn.send(str.encode(str(p)))  # Send the player number to the client

    while True:
        try:
            data = conn.recv(4096).decode()  # Receive data from the client

            if gameId not in games:  # If the game no longer exists, exit the loop
                break
            game = games[gameId]  # Get the game object

            if not data:  # If no data is received, exit the loop
                break
            if data == "reset":  # If the reset command is received, reset the game
                game.resetWent()
            elif (
                data != "get"
            ):  # If the command is not 'get', process the command as a move
                game.play(p, data)

            conn.sendall(
                pickle.dumps(game)
            )  # Send the updated game object back to the client
        except Exception:  # Catch any exceptions and exit the loop
            break

    print("Lost connection")  # Connection was lost or an exception occurred
    with contextlib.suppress(
        Exception
    ):  # Ignore exceptions when trying to delete the game and decrements the idCount
        del games[gameId]
        print("Closing Game", gameId)
    idCount -= 1  # Decrement the global counter for active connections
    conn.close()  # Close the connection to the client


while True:
    conn, addr = s.accept()  # Accept a new connection
    print("Connected to:", addr)  # Print the address of the connected client

    idCount += 1  # Increment the global counter for active connections
    p = 0  # Default to player 0
    gameId = (
        idCount - 1
    ) // 2  # Calculate the gameId based on the number of connected clients
    if idCount % 2 == 1:  # If this is the first player to connect for a game
        games[gameId] = Game(gameId)  # Create a new game
        print("Creating a new game...")
    else:  # This is the second player for the game
        games[gameId].ready = True
        p = 1  # Set to player 1

    start_new_thread(
        threaded_client, (conn, p, gameId)
    )  # Start a new thread for handling the client
