from flask import Flask, render_template, request

app = Flask(__name__)

def basic_calculator(a, b, operation):
    try:
        a = float(a)
        b = float(b)

        if operation == "add":
            result = a + b
        elif operation == "subtract":
            result = a - b
        elif operation == "divide":
            if b == 0:
                result = "Cannot divide by zero"
            else:
                result = a / b
        elif operation == "multiply":
            result = a * b
        else:
            result = "Operations supported: add, subtract, divide, multiply only"
    except ValueError:
        result = "Please enter valid numbers for a & b"

    return result

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    a = request.form['a']
    b = request.form['b']
    operation = request.form['operation']

    result = basic_calculator(a, b, operation)

    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)