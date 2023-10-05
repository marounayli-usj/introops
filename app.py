from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World from CICD and now we have a full pipeline with no errors!!!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')