import socket, argparse, threading

 # Accept a new socket and receive the nickname
def socket_accept():
	
	conn, address = s.accept() # Three-way handshake - This is a TCP connection with the server
	# Receive the nickname
	nickname = conn.recv(1024)
	# Append address in clients list
	if address not in clients:
		#clients.append((address[0]+':'+str(address[1])))
		clients.append(conn)
	print("Connection has been established | " + "IP " + address[0] + \
		" | Port " + str(address[1]) + ' ' + nickname)
	#client(conn)
	#conn.close()
	# Go for data
	# Start a thread to keep receiving client data
	thread_client = threading.Thread(target = data, args=[nickname, conn])
	thread_client.start()

def data(nickname, conn):
	while True:	
		# Reveive the data from client
		data = conn.recv(4096)
		#conn.sendall(data)
		if data:
			print("%s said %s" % (nickname, repr(data)))
			bcast(conn, data, nickname) # Call for broadcast
						    # I tried to put this function here instead of calling it but it don't work because it's
						    # always on the same client socket and we need to change socket to send to other clients
						    # sendto(data, address) also didn't work
		if not data:	
			break

 # Broadcast 
def bcast(client_socket, message, client_nickname):
	# We don't want to receive what we sent	
	for i in clients:
		if i == client_socket:
			pass
		# Sent my message to other clients
		else:
			print(clients)
			#i.sendall(client_nickname)
			#i.sendall()
			# New line on the client side
			i.sendall(client_nickname + ': ' + message)	

if __name__ == '__main__':
	# Args for host and port
	parser = argparse.ArgumentParser(description='My TCP server')
	parser.add_argument('host',  help='Interface the server listens at')
	parser.add_argument('-p', metavar='PORT', type=int,                                                help='TCP PORT (default 9999)')	
	args = parser.parse_args()
	host = args.host
	port = args.p

	 # Client List	
	clients = []

	 # Create socket
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	except socket.error as msg:
		print("Socket creation error: " + str(msg))

	 # Bind the sockets
	try:
		print("Binding socket to port: " + str(port))
		s.bind((host, port))
		s.listen(5) #number of connections
	except socket.error as msg:
		print("Socket binding error: " + str(msg) + "\n" + "Retrying...")


	
	while True:
		socket_accept()
