from flask import Flask

app = Flask(__name__)

@app.route('/delreq', methods=['DELETE'])
def delreq():
    return "This is DELETE reqest";

@app.route('/postreq', methods=['POST'])
def postreq():
    return "This POST request";

@app.route('/getreq', methods=['GET'])
def getreq():
    return "This is GET request"

@app.route('/putreq', methods=['PUT'])
def putreq():
    return "This is PUT request"

if __name__ == '__main__':
    app.run(debug=True)
