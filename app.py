from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App!"

@app.route('/about')
def about():
    return "This is a simple Flask app."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=500)