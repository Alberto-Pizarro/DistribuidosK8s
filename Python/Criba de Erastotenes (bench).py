from textblob import TextBlob
from flask import Flask, request, jsonify
import time

app = Flask(__name__)


'''@app.route("/analyse/sentiment", methods=['POST'])
def analyse_sentiment():
    sentence = request.get_json()['sentence']
    polarity = TextBlob(sentence).sentences[0].polarity
    return jsonify(
        sentence=sentence,
        polarity=polarity
    )
'''

# Progrma en python que calcula todos los primos menores a N
# Basado en la Criba de Erastótenes
# Entrega cuantos primos encontró y cuanto se demoró en ello
@app.route("/analyse/sentiment", methods=['POST'])
def SieveOfEratosthenes():
    n = int(request.get_json()['sentence'])
    t1=time.time()
    # Array booleano de tamaño "prime[0..n]" inicializado como True
    prime = [True for i in range(n + 1)]
    primos = 0
    p = 2
    while (p * p <= n):
        # Si es un número primo, eliminamos todos sus múltiplos
        if prime[p]:
            # Contabilizamos el primo encontrado
            primos+=1
            # Actualizamos todos los múltiplos que tiene
            for i in range(p * 2, n + 1, p):
                prime[i] = False
            
        p += 1
    prime[0] = False
    prime[1] = False
    # Calculamos el tiempo utilizado para esto
    tiempo=t1-time.time()

    return jsonify(
        primos=primos,
        tiempo=tiempo
                    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)