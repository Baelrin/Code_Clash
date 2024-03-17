import contextlib
import pickle
import socket
from typing import Optional


class Network:
    """
    A class to manage network connections and communication for a client.
    """

    def __init__(self):
        """
        Initializes a new Network client, connecting it to a predefined IP and port.
        """
        self.client = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM
        )  # TCP connection
        self.server = "Your IP"  # Server IP address
        self.port = 5555  # Server port
        self.addr = (self.server, self.port)  # Tuple for IP and port
        self.p = self.connect()  # Store connection result

    def getP(self) -> Optional[str]:
        """
        Returns the initial data received from the server upon connecting.

        :return: Optionally returns a string received from the server.
        """
        return self.p

    def connect(self):
        """
        Establishes a connection to the server, suppressing all exceptions.

        :return: Decoded message received from the server if connection is successful, None otherwise.
        """
        with contextlib.suppress(Exception):
            self.client.connect(self.addr)
            return self.client.recv(
                2048
            ).decode()  # Decodes the received message from bytes to str

    def send(self, data):
        """
        Sends data to the server and waits for a response.

        :param data: The string data to send to the server.
        :return: The response from the server, deserialized from pickle format.
        """
        try:
            self.client.send(
                str.encode(data)
            )  # Sends the encoded string data to the server
            return pickle.loads(
                self.client.recv(2048 * 2)
            )  # Returns the deserialized server response
        except socket.error as e:
            print(e)  # Prints the socket error if any occurs during communication
