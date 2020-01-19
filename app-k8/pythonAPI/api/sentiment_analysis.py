from textblob import TextBlob
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/primos/calculo", methods=['POST'])
def analyse_sentiment():
    primos = request.get_json()['primos']
    tiempo = TextBlob(primos).primoss[0].tiempo
    return jsonify(
        primos=primos,
        tiempo=tiempo
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
