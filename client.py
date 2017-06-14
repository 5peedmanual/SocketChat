import socket, sys, argparse, threading

# Function to send data
def send():
	global my_nickname
	while True:
		message = raw_input(my_nickname + ' :')
		sock.sendall(message)
		if message == 'quit':
			#break
			sock.close()
			sys.stdout.flush()
			sys.exiti(0)

# Function to receive data
def receive():
	while True:
		data = sock.recv(4096)
		# New line for when receiving data from other clients
		print('\n' + data)
		if not data:
			break



if __name__ == '__main__':

	 # Args for host and port
	parser = argparse.ArgumentParser(description='My TCP server')
	parser.add_argument('host',  help='server to connect to')
	parser.add_argument('-p', metavar='PORT', type=int, help='TCP PORT (default 9999)')      
	args = parser.parse_args()
	host = args.host
	port = args.p

	 # Create the socket AF_INET the internet family of protocols IPv4
	 # SOCK_STEAM TCP PROTOCOL
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
	sock.connect((host,port))
	except:
	print('Can\'t connect')
	sock.close()
	sys.exit()

	# Sends nickname to server
	my_nickname = raw_input('Choose nick: ')    
	sock.sendall(my_nickname)

	# A thread for send and receive
	thread_send = threading.Thread(target = send)
	thread_send.start()
	thread_receive =  threading.Thread(target = receive)
	thread_receive.start()
	
