from flask import Flask, request, render_template
import math

from timeit import default_timer as timer

app = Flask(__name__)

@app.route("/factorial/<n>")
def factorial(n=None):
        n = int(n)
        start = timer()

        factorial = math.factorial(n) # uses a c funcion, faster

        end = timer()

        time = end-start

        return render_template('a.html', n=factorial, t = time)

@app.route("/fibonacci/<n>")
def fibonacci(n=None):
        n = int(n)
        start = timer()
        
        # binet formula
        fibonacci =  round((math.pow(1.618033988749895, n) - math.pow(-0.6180339887498949, n)) / 2.23606797749979, 5)
                
        

        end = timer()

        time = end-start

        return render_template('b.html', n=fibonacci, t = time)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)