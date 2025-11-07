"""
Flask Web Application for Calculator
Provides a web interface for the calculator operations
"""

from flask import Flask, render_template, request, jsonify
from calculator import Calculator
import os

app = Flask(__name__)
calc = Calculator()

@app.route('/')
def index():
    """Main calculator page"""
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    """API endpoint for calculator operations"""
    try:
        data = request.get_json()
        operation = data.get('operation')
        num1 = float(data.get('num1', 0))
        num2 = float(data.get('num2', 0))
        
        if operation == 'add':
            result = calc.add(num1, num2)
        elif operation == 'subtract':
            result = calc.subtract(num1, num2)
        elif operation == 'multiply':
            result = calc.multiply(num1, num2)
        elif operation == 'divide':
            result = calc.divide(num1, num2)
        elif operation == 'power':
            result = calc.power(num1, num2)
        else:
            return jsonify({'error': 'Invalid operation'}), 400
        
        return jsonify({
            'result': result,
            'operation': operation,
            'num1': num1,
            'num2': num2
        })
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'calculator-web-app',
        'version': '1.0.0'
    })

@app.route('/api/operations')
def operations():
    """Get available operations"""
    return jsonify({
        'operations': [
            {'key': 'add', 'symbol': '+', 'name': 'Addition'},
            {'key': 'subtract', 'symbol': '-', 'name': 'Subtraction'},
            {'key': 'multiply', 'symbol': '×', 'name': 'Multiplication'},
            {'key': 'divide', 'symbol': '÷', 'name': 'Division'},
            {'key': 'power', 'symbol': '^', 'name': 'Power'}
        ]
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=True)
