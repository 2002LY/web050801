from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
@app.route('/a')
def 你好():
    return '你好Hello, World'
if __name__ =="__main__":
    app.run()