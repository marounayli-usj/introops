from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def indexget():
    return 'najib'

@app.route('/', methods=['POST'])
def index():
    data = request.json  # Assume the incoming request has JSON data
    print("Data received:", data)
    
    # Perform your logic here.
    
    return jsonify({"message": "Data received"}), 200

if __name__ == '__main__':
    app.run(debug=True,port=4500)
#added comment