from textblob import TextBlob
from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Progrma en python que calcula todos los primos menores a N
# Basado en la Criba de Erastotenes
# Entrega cuantos primos encontro y cuanto se demoro en ello
@app.route("/calculo/criba", methods=['POST'])
def obtener_lista():
    lista = request.get_json()['lista']

    n = int(lista)
    t1=time.time()
    # Array booleano de tamano "prime[0..n]" inicializado como True
    prime = [True for i in range(n + 1)]
    primos = 0
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

    for i in prime:
        if (i):
            primos+=1
    # Calculamos el tiempo utilizado para esto
    tiempo=t1-time.time()

    string = str(primos)

    return jsonify(
        lista=string,
        tiempo=tiempo*(-1)*pow(10,6)
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
