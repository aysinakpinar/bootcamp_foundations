from flask import Flask, request # NOTE: we must import `request` too

app = Flask(__name__)

# Request:
# GET /hello?name=David

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args['name'] # The value is 'David'

    # Send back a friendly greeting with the name
    return f"Hello {name}!"

# To make a request, run:
# curl "http://localhost:5001/hello?name=David"
