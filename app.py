from flask import Flask, render_template, request
from calculator import add, sub, mul, div

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            if operation == "add":
                result = add(num1, num2)
            elif operation == "sub":
                result = sub(num1, num2)
            elif operation == "mul":
                result = mul(num1, num2)
            elif operation == "div":
                result = div(num1, num2)
        except Exception as e:
            result = f"Error: {e}"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
