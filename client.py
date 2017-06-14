import socket, sys, argparse, threading
 
# Create the socket AF_INET the internet family of protocols IPv4
# SOCK_STEAM TCP PROTOCOL
 
host = 'localhost'
port = 9999
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
 
# Function to send data
def send():
    global my_nickname
    while True:
        message = raw_input(my_nickname + ' :')
        sock.sendall(message)
        if message == 'quit':
            break
            sock.close()
            sys.flush()
            #sys.exit
            thread_send.stop()
            thread_receive.stop()
 
# Function to receive data
def receive():
    while True:
        data = sock.recv(4096)
        # New line for when receiving data from other clients
        print('\n' + data)
        if not data:
            break
 
 
#thread_connect = threading.Thread(target=connect, args=(args.host, args.p))
 
# A thread for send and receive
thread_send = threading.Thread(target = send)
thread_send.start()
thread_receive =  threading.Thread(target = receive)
thread_receive.start()
