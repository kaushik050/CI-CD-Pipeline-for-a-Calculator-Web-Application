"""
Simple Calculator Application
Provides basic arithmetic operations: add, subtract, multiply, divide
"""

class Calculator:
    """Calculator class with basic arithmetic operations"""
    
    def add(self, a, b):
        """Add two numbers"""
        return a + b
    
    def subtract(self, a, b):
        """Subtract second number from first"""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers"""
        return a * b
    
    def divide(self, a, b):
        """Divide first number by second"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, a, b):
        """Raise first number to the power of second"""
        return a ** b


def main():
    """Main function to run calculator as CLI application"""
    calc = Calculator()
    
    print("Welcome to Calculator!")
    print("Available operations: +, -, *, /, ^")
    print("Enter 'quit' to exit")
    
    while True:
        try:
            operation = input("\nEnter operation (+, -, *, /, ^): ").strip()
            
            if operation.lower() == 'quit':
                print("Goodbye!")
                break
            
            if operation not in ['+', '-', '*', '/', '^']:
                print("Invalid operation. Please use +, -, *, /, or ^")
                continue
            
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if operation == '+':
                result = calc.add(num1, num2)
            elif operation == '-':
                result = calc.subtract(num1, num2)
            elif operation == '*':
                result = calc.multiply(num1, num2)
            elif operation == '/':
                result = calc.divide(num1, num2)
            elif operation == '^':
                result = calc.power(num1, num2)
            
            print(f"Result: {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
