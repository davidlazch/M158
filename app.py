from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    hello = "Hello, DevOps!\n"
    hello += "Hello, it's David!\n"
    hello += "Hello, it's Lionel now !\n"
    hello += "Hello, it's a me, William !\n"
    hello += "Hello, it's Aaron, Lets go !\n"
    hello += "Hello, it's Lionel, for a third time !\n"
    return hello

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
