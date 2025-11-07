from flask import Flask, render_template, request
from calculator import add, subtract, multiply, divide

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    num1 = num2 = ''
    operation = 'add'

    if request.method == 'POST':
        try:
            num1 = request.form['num1']
            num2 = request.form['num2']
            operation = request.form['operation']

            n1 = float(num1)
            n2 = float(num2)

            if operation == 'add':
                result = add(n1, n2)
            elif operation == 'subtract':
                result = subtract(n1, n2)
            elif operation == 'multiply':
                result = multiply(n1, n2)
            elif operation == 'divide':
                result = divide(n1, n2)
        except ValueError:
            result = "Invalid input"
    return render_template('index.html', result=result, num1=num1, num2=num2, operation=operation)

if __name__ == '__main__':
    app.run(debug=True)
