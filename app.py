import os
from flask import Flask

system_name = os.environ.get("SYSNAME", "localhost")
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerized this from %s' % system_name

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
