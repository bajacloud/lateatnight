# Sample Python Application
# This script uses Flask to create a basic web server and Pillow for image processing (not actually used but imported)

from flask import Flask
from PIL import Image

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)