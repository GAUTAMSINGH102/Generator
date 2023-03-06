from flask import Flask, render_template, jsonify, request
from CodeGenerator import code_generate_function
from GenerateDocument import doc_generate_function
from ConvertCode import code_converter_function

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/CODEGEN', methods=["POST"])
def CODEGEN():
    textInput = request.json['textInput']
    codeOutput = code_generate_function(textInput)
    return jsonify(codeOutput)

@app.route('/DOCGEN', methods=["POST"])
def DOCGEN():
    codeInput = request.json['codeInput']
    textOutput = doc_generate_function(codeInput)
    return jsonify(textOutput)

@app.route('/CODECONV', methods=["POST"])
def CODECONV():
    pythonCodeInput = request.json['codeInput']
    codeOutput = code_converter_function(pythonCodeInput)
    return jsonify(codeOutput)


@app.route('/codeGenerator')
def codeGenerator():
    return render_template("codeGenerator.html")

@app.route('/docGenerator')
def docGenerator():
    return render_template("docGenerator.html")

@app.route('/codeConvertor')
def codeConvertor():
    return render_template("codeConvertor.html")

@app.route('/contactUs')
def contactUs():
    return render_template("contactUs.html")


if __name__ == '__main__':
    app.run(debug=True)