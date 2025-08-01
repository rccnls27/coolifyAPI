# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Change this message!
    return {"message": "This is a new version deployed automatically!"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
