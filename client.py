import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("Connected to server.")

@sio.event
def disconnect():
    print("Disconnected from server.")

@sio.on('move')
def on_move(data):
    print(f"Received move: {data['move']}")
    # Update game state in GameController

def connect_to_server(url="http://localhost:5000"):
    sio.connect(url)

def create_room(room):
    sio.emit('create_room', {'room': room})

def join_room(room):
    sio.emit('join_room', {'room': room})

def send_move(room, move):
    sio.emit('move', {'room': room, 'move': move})

if __name__ == "__main__":
    connect_to_server()

