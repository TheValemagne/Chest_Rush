import socket
import threading
import time

class Client :

    def __init__ (self,name,ip,port,buffer_size = 1024,push = None) : # Default parameters

        """Initialisation of the client class"""

        self.Username = name # Username

        self.IP = ip # IP of the server

        self.Port = port # Port of the server

        self.Push = push # Function to update the message

        self.Buffer_Size = buffer_size # Buffer size
        
        self.Address = (self.IP, self.Port) # Server address

        self.Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creation of the client

    def connect (self) :

        """Establish the server connection"""

        try : # Try to do the next lines

            self.Client.connect(self.Address) # Create the connection

            self.Receiver = threading.Thread(target = self.receive_Msg) # Create the client listener

            self.Receiver.start() # Start the server listener

            self.send(self.Username) # Send the username to the server

        except Exception as e: # If try failed

            self.Push("no data")

    def receive_Msg (self): # Receive message from the server

        """Server listener"""

        while True : # Loop

            msg = self.Client.recv(1024).decode("utf-8") # Receive message from the server

            if msg != "" :

                self.Push(msg)

            else :

                self.Push("no data")

            if msg == "{quit}" :

                self.Push("offline")

                break

        self.Client.close()

    def leave (self) :

        """Leave the server"""

        self.send("{quit}")

    def send(self,msg):

        """Send message to the server"""

        try :

            self.Client.send(bytes(msg, "utf-8"))

        except :

            pass
