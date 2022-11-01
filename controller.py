from flask import Flask, jsonify
from model import Calc

app = Flask(__name__)

@app.route('/somar', methods=["GET"])
def consultar():
    return jsonify(Calc.somar(1, 2))

if __name__ == '__main__':
  app.run(debug=True)