import socket
import threading #Seperates code by thread 
from playsound import playsound

HEADER = 64
PORT = 5050 #Random unavaiable port (Over 4000)
SERVER = socket.gethostbyname(socket.gethostname()) #IPV4 Address on Computer
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #What type of address are we looking for? (INET [IPV4], INET6 [IPV6]
server.bind(ADDR) #Bound the socket to this address

def handle_client(conn, addr):
	print(f"[NEW CONNECTION] {addr} connected.")
	
	connected = True
	while connected:
		msg_length = conn.recv(HEADER).decode(FORMAT) #How long is the message? .decode it in UTF-8
		if msg_length:
			msg_length = int(msg_length) #Turn the length into an int
			msg = conn.recv(msg_length).decode(FORMAT) #Decode the actual message
			if msg == "Hello":
				print("Button Pressed")
				#playsound("sound")
			elif msg == DISCONNECT_MESSAGE:
				connected = False
			
			print(f"[{addr}] {msg}")
			conn.send("Msg received".encode(FORMAT))
			
	conn.close()
		
def start():
	server.listen() #Listen for new connections
	print(f"[LISTENING] Server is listening on {SERVER}")
	while True: #Forever Loop
		conn, addr = server.accept() #Wait for a new connection, and then store the address of where the connection came from in "addr" and "conn" allows to send info back
		thread = threading.Thread(target=handle_client, args=(conn, addr)) #When a new connection occurs, start handle_client() and pass the "conn" and "addr" into it on a serperate thread 
		thread.start() #Start the thread
		
		print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}") #Shows us the amoutn of connections
	
print("[STARTING] server is starting...")
start()