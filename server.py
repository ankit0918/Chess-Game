from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, leave_room, emit
from GameController import GameController

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

rooms = {}  # Dictionary to track active rooms and players
game_controllers = {}  # Dictionary to track game controllers for each room

@app.route('/')
def index():
    return "Chess Game Server Running"

@socketio.on('join')
def handle_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    
    if room not in rooms:
        rooms[room] = []
        game_controllers[room] = GameController()
    rooms[room].append(username)

    emit('status', {'message': f"{username} joined the room."}, room=room)
    print(f"{username} joined room: {room}")

@socketio.on('leave')
def handle_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    
    if room in rooms and username in rooms[room]:
        rooms[room].remove(username)
        if not rooms[room]:
            del rooms[room]
            del game_controllers[room]
    emit('status', {'message': f"{username} left the room."}, room=room)
    print(f"{username} left room: {room}")

@socketio.on('move')
def handle_move(data):
    room = data['room']
    move = data['move']  
    if room in game_controllers:
        try:
            game_controllers[room].make_move(move)
            emit('opponent_move', {'move': move}, room=room, include_self=False)
            print(f"Move in room {room}: {move}")
        except Exception as e:
            emit('error', {'message': f'Invalid move: {str(e)}'}, room=room)
    else:
        emit('error', {'message': 'Game controller not found for this room'}, room=room)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
