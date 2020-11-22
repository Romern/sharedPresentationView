from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, send, emit
#from flask_basicauth import BasicAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

curPage = 1

#app.config['BASIC_AUTH_USERNAME'] = 'roman'
#app.config['BASIC_AUTH_PASSWORD'] = 'test'
#basic_auth = BasicAuth(app)

@app.route('/', methods=["GET"])
def main():
	return render_template('index.html')

@socketio.on('welcome')
def welcome():
	emit("welcome", curPage)
	print("welcome received")

@socketio.on("newslide")
#@basic_auth.required
def newslide(slide):
	curPage = slide
	emit('newslide', curPage, broadcast=True)
	print(f"newslide received: {slide}")

if __name__ == '__main__':
	socketio.run(app, debug=True)
