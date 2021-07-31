from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/')
def hello_world():

@app.route('/page/<int:pg_num>')
def content(pg_num):
    return f'<h1>Display results for page {pg_num}</h1>'

if __name__ == "__main__":
    app.run(debug = True)
