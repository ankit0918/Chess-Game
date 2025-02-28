from flask import Flask, request
from flask_socketio import SocketIO, emit, join_room, leave_room
import os

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

rooms = {}  # Store game state for each room

@app.route('/')
def index():
    return "Chess server is running!"

@socketio.on('connect')
def handle_connect():
    print(f"Client connected: {request.sid}")

@socketio.on('disconnect')
def handle_disconnect():
    print(f"Client disconnected: {request.sid}")

@socketio.on('create_room')
def create_room(data):
    room = data['room']
    if room not in rooms:
        rooms[room] = {'players': [], 'moves': []}
    join_room(room)
    rooms[room]['players'].append(request.sid)
    emit('room_created', {'message': f'Joined room {room}'}, room=room)

@socketio.on('join_room')
def join_room_event(data):
    room = data['room']
    if room in rooms and len(rooms[room]['players']) < 2:
        join_room(room)
        rooms[room]['players'].append(request.sid)
        emit('room_joined', {'message': f'Joined room {room}'}, room=room)
    else:
        emit('error', {'message': 'Room full or does not exist'})

@socketio.on('move')
def handle_move(data):
    room = data['room']
    move = data['move']
    if room in rooms:
        rooms[room]['moves'].append(move)
        emit('move', {'move': move}, room=room, include_self=False)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use environment variable or default to 5000
    socketio.run(app, host="0.0.0.0", port=port)
