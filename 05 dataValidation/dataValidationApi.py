from flask import Flask, render_template, request
import dataValidation as dv

app = Flask(__name__)

@app.route('/file_validation', methods=['POST'])
def fileValidation():
    
    #file = open("HSBC_Volumes_monthly_121212.csv", "rb")
    #data = file.read()
    
    file = request.files['file']
    data = file.read()
    
    data_validated, message = dv.data_check(data, 'csv')
    
    if data_validated:
        return 'File is valid'
    else:
        return message

app.run(host='0.0.0.0',port=int(8080))


if __name__ == '__main__':
    app.run()
