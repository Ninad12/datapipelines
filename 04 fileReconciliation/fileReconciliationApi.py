from flask import Flask, render_template, request
import fileReconciliation as recon

app = Flask(__name__)

@app.route('/recon', methods=['POST'])
def fileRecon():
    
    fileDetail = request.get_json()
    fileName = fileDetail['fileName']
    data_validated, message = recon.recon(fileName)
    
    if data_validated:
        return message
    else:
        return message

app.run(host='0.0.0.0',port=int(8080))


if __name__ == '__main__':
    app.run()
