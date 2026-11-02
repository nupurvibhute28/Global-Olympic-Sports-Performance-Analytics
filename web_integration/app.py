from flask import Flask, render_template
import webbrowser
from threading import Timer

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    Timer(1, lambda: webbrowser.open('http://127.0.0.1:8000')).start()
    app.run(host='127.0.0.1', port=8000, debug=False)
