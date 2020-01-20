from textblob import TextBlob
from flask import Flask, request, jsonify
import time

app = Flask(__name__)


@app.route("/analyse/sentiment", methods=['POST'])
def obtener_lista():
    lista = request.get_json()['lista']


    n = int(lista)
    t1=time.time()
    # Array booleano de tamano "prime[0..n]" inicializado como True
    prime = [True for i in range(n + 1)]
    primos = []
    p = 2
    while (p * p <= n):
        # Si es un numero primo, eliminamos todos sus multiplos
        if prime[p]:
            # Actualizamos todos los multiplos que tiene
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    # Guardamos todos los primos en una lista que vamos a retornar
    for p in range(n + 1):
        if prime[p]:
            primos.append(p)
    # Calculamos el tiempo utilizado para esto
    tiempo=t1-time.time()

    str1 = " ".join(str(e) for e in primos)

    return jsonify(
        lista=str1,
        tiempo=tiempo
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
