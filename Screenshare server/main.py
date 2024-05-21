from flask import Flask, render_template, Response
from camera import VideoCamera  # Importing custom VideoCamera class for video streaming
import pyscreenshot # Importing pyscreenshot for taking screenshot
import flask # Importing flask for sending files
from PIL import ImageGrab # Importing ImageGrab for taking screenshot
from io import BytesIO # Importing BytesIO for storing image in memory
import socket 

app = Flask(__name__) # Creating Flask app


@app.route('/')
def index():
    return render_template('index.html') # Rendering index.html


def gen(camera):
    while True:
        frame = camera.get_frame() # Getting frame from camera
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n') # Yielding frame


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()), #frameee catching from camera
                    mimetype='multipart/x-mixed-replace; boundary=frame') # Returning video feed


@app.route('/screen.png') # Route for taking screenshot
def serve_pil_image():
    img_buffer = BytesIO() 
    ImageGrab.grab().save(img_buffer, 'PNG', quality=10) # Taking screenshot
    img_buffer.seek(0)
    return flask.send_file(img_buffer, mimetype='image/png') # Sending screenshot


@app.route('/js/<path:path>')
def send_js(path):
    return flask.send_from_directory('js', path) # Sending js files


@app.route('/css/<path:path>')
def send_css(path):
    return flask.send_from_directory('css', path) # Sending css files


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        
        s.connect(('10.33.22.206', 8000)) # change it accroding to your ip
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


if __name__ == '__main__':
    app.run(host=get_ip(), debug=False) # Running the app
