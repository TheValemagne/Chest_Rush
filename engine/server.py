
import socket
import threading

class Server : # Server listener

	def __init__ (self,name,welcome,ip,port,max_connections,time_var,locations,buffer_size = 1024) : # Default parameters

		"""Initialisation of the server class"""

		# Default variables setup

		self.Format = {"Server" : "[Server] : ","Users" : "<%> : "} # Message format

		self.Messages_In_Chat = [""] * 10

		self.Messages_In_Chat[len(self.Messages_In_Chat) - 1] = "ANCIENT"
		self.Messages_In_Chat[len(self.Messages_In_Chat) - 2] = "TESTER"

		self.IP = ip # IP of the server
		self.Port = port # Port of the server
		self.Max = max_connections # Max users
		self.Name = name # Name of the server
		self.Welcome = self.Format["Server"] + welcome # Welcome message on user join
		self.Buffer = buffer_size # Buffer size

		self.Timer = time_var # Time ingame

		self.Locations = locations # Spawn coords for player

		self.Players_In_Game = {} # All players in game

		########################################

		self.Address = (self.IP, self.Port) # Server address
		self.Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creation of the socket
		self.Server.bind(self.Address) # Create the server with the address

		self.Clients = {} # Dict for the clients

		self.Server.listen(max_connections) # Listen up to max connections

	def start_Server (self) : # Start the connection thread

		"""Create the server connection"""

		self.Incomers = threading.Thread(target = self.accept_Connections) # Create the accepting loop

		self.Incomers.start() # Start the thread

	def stop_Server (self) : # Stop the server

		"""Close the server connection"""

		self.Incomers.join() # Join the thread

		self.Server.close() # Close the server

	def accept_Connections(self): # Loop for accepting the client connections

		"""Accept the incoming connections"""

		while True: # Loop

			Client, Address = self.Server.accept() # Accept the entering connection

			Client.send(bytes(self.Welcome, "utf-8")) # Send the welcome message

			threading.Thread(target = self.handle_client, args=(Client,)).start() # Create the client listener

	def server_Broadcast(self,msg,command = False): # Send the incoming message to all users

		"""Distribute the message to all users"""

		if command == False :

			self.Messages_In_Chat = self.Messages_In_Chat[1:]

			self.Messages_In_Chat.append(msg)

		for user in self.Clients: # For the user in the dict

			user.send(bytes(msg, "utf-8")) # Send the message to the user

	def handle_client(self,client): # Receive message from the client

		"""Receive message from client"""

		Username = client.recv(self.Buffer).decode("utf-8").upper() # Receive the client username

		print(Username,"just joined !")

		for iteration in range (len(self.Locations)) :

			if self.Locations[iteration][0] == True :

				Coords = self.Locations[iteration][1:]

				self.Locations[iteration][0] = False

				break

		if self.Messages_In_Chat[len(self.Messages_In_Chat) - 1] == "" :

			Infos = "_" + self.Timer.get() + "/" + str(Coords) + "/" + Username + "/" + str(self.Players_In_Game)  # Incoming message with format : _time/coords/Username/{Players}

		else :

			Infos = "_" + self.Timer.get() + "/" + str(Coords) + "/" + Username + "/" + str(self.Players_In_Game) + "/" + str(self.Messages_In_Chat) # Incoming message with format : _time/coords/Username/{Players}

		client.send(bytes(Infos,"utf-8")) # Send session info

		self.server_Broadcast(Infos,command = True) # Broadcast the message

		Msg = self.Format["Server"] + Username + " has joined the chat !" # Format of the message

		self.server_Broadcast(Msg) # Broadcast the message

		self.Clients[client] = Username # Attribute the username to the client

		self.Players_In_Game[Username] = Coords # Updating dict when user joined

		while True: # Loop

			try : # Try the next lines

				msg = client.recv(self.Buffer) # Receive message from the user

				if msg != bytes("{quit}", "utf-8") : # If message != quit

					if msg.decode("utf-8").startswith(".") or msg.decode("utf-8").startswith("_") :

						if msg.decode("utf-8").count(".") > 1 :

							Reformater = [0,0]

							for inner_message in msg.decode("utf-8").split(".")[1:] :

								inner_message = inner_message.split("/")

								Coords = eval(inner_message[0])

								Reformater = [Reformater[0] + Coords[0], Reformater[1] + Coords[1]]

								Name = inner_message[1]

							New_Message = "." + str(Reformater) + "/" + Name

							self.server_Broadcast(New_Message,command = True)

						else :

							if msg.decode("utf-8").startswith(".") :

								Infos = msg.decode("utf-8")[1:]

								Infos = Infos.split("/")

								self.Players_In_Game[Infos[1]] = self.Players_In_Game[Infos[1]][0] + eval(Infos[0])[0], self.Players_In_Game[Infos[1]][1] + eval(Infos[0])[1]	

							self.server_Broadcast(msg.decode("utf-8"),command = True)

					elif msg.decode("utf-8")[0:2] == "//" :

						self.server_Broadcast(msg.decode("utf-8"),command = True)

					elif msg.decode("utf-8").startswith("/") :

						Msg = "|COMMAND| : " + msg.decode("utf-8") + " executed"

						self.server_Broadcast(Msg)

					else :

						Msg = self.Format["Users"].replace("%",Username) + msg.decode("utf-8") # Create the message with the format

						self.server_Broadcast(Msg) # Broadcast the message

				else : # Closing the client connection

					client.send(bytes("{quit}", "utf8")) # Send confirmation to client

					client.close() # Close the connection

					del self.Clients[client] # Removing client from dict

					Msg = self.Format["Server"] + Username + " has left the chat." # Alerting the users

					self.server_Broadcast(Msg) # Broadcast the message

					break # Breaking the loop

			except Exception as e : # If message receive failed

				print("EXCEPTION :",e)

				client.close() # Close the connection

				del self.Clients[client] # Removing client from dict

				Msg = self.Format["Server"] + Username + " has left the chat." # Alerting the users

				self.server_Broadcast(Msg) # Broadcast the message

				break # Exiting the loop



