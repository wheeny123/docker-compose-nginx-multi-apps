import os
import socket
from flask import Flask

# flask application object
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World! (Hostname=%s, PID=%s)" % (socket.gethostname(), os.getpid())

if __name__ == "__main__":
    app.run()
