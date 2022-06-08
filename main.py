from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/factorial/<n>", methods = ['POST'])
def factorial(n=None):
    if request.method == 'POST':
        n = request.args.get() 
        factorial = 1    
        if n < 0:    
            print(" Factorial does not exist for negative numbers")    
        elif n == 0:    
            print("The factorial of 0 is 1")    
        else:    
            for i in range(1,n + 1):    
                factorial = factorial*i    
        return make_response(factorial)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)