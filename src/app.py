from flask import Flask

app = Flask(__name__)
#app object

@app.route("/")

def index():
    return "Hello, World!"

if __name__ == "__main__":
   app.run()


