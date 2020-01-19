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

# Python program to print all primes smaller than or equal to
# n using Sieve of Eratosthenes
@app.route("/primos/calculo", methods=['POST'])
def primos():
    n = int(request.get_json()['primos'])
    t1=time.time()
    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n + 1)]
    primos = []
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    # Print all prime numbers
    for p in range(n + 1):
        if prime[p]:
            primos.append(p)

    tiempo=t1-time.time()

    return jsonify(
        primos=primos,
        tiempo=tiempo
                    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
