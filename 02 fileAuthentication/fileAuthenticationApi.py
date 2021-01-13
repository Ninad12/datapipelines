import fileAuthentication
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/readFile', methods=['POST'])
def readFile():
    fileDetail = request.get_json()
    fileName = fileDetail['fileName']
    is_valid, extension = fileAuthentication.is_authenticate(fileName)
    if is_valid:
        return 'valid file' + ' ' + fileName
    else:
        return 'Invalid file' + ' ' + fileName

app.run(host='0.0.0.0',port=int(8080))


if __name__ == '__main__':
    app.run()
