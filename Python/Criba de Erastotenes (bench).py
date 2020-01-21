from textblob import TextBlob
from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Progrma en python que calcula todos los primos menores a N
# Basado en la Criba de Erastótenes
# Entrega cuantos primos encontró y cuanto se demoró en ello
@app.route("/calculo/criba", methods=['POST'])
def SieveOfEratosthenes():
    n = int(request.get_json()['lista'])
    t1=time.time()
    # Array booleano de tamaño "prime[0..n]" inicializado como True
    prime = [True for i in range(n + 1)]
    primos = 0
    p = 2
    while (p * p <= n):
        # Si es un número primo, eliminamos todos sus múltiplos
        if prime[p]:
            # Actualizamos todos los múltiplos que tiene
            for i in range(p * 2, n + 1, p):
                prime[i] = False

        p += 1
    prime[0] = False
    prime[1] = False

    for i in prime:
        if (i):
            primos+=1
    # Calculamos el tiempo utilizado para esto
    tiempo=t1-time.time()

    return jsonify(
        lista=primos,
        tiempo=tiempo
                    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
