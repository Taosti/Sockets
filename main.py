import socket
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

HEADER = 64
PORT = 5050
SERVER = "IP" #INSERT IP
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
	message = msg.encode(FORMAT)
	msg_length = len(message)
	send_length = str(msg_length).encode(FORMAT)
	send_length += b' ' * (HEADER - len(send_length))
	client.send(send_length)
	client.send(message)
	print(client.recv(2048).decode(FORMAT))

class MyGrid(GridLayout):
	def __init__(self, **kwargs):
		super(MyGrid, self).__init__(**kwargs)
		self.cols = 2
		
		self.submit = Button(text="Submit", font_size=40)
		self.submit.bind(on_press=self.pressed)
		self.add_widget(self.submit)
		
	def pressed(self, instance):
		print("Pressed")
		send("Hello")

class MyApp(App):
	def build(self):
		return MyGrid()

if __name__ == '__main__':
	MyApp().run()