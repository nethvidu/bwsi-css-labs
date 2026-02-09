"""
lab_1b.py

This is a script that implements a simple calculator. It takes two numbers and an operation,
then performs the operation and returns the result. 

The script asks the user to input the numbers and the operation to be performed,
and prints the result to the terminal window.

"""

def simple_calculator(num1: float, num2: float) -> float:
    """
    Function that takes in two numbers,
    then prompts for an operation and performs the operation on the two numbers, returning the result.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The result of the operation.
    """

    while True:
        try:
            operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
            if operation == "add":
                print(f"The result of adding", end=" ")
                return num1 + num2
            elif operation == "subtract":
                print(f"The result of subtracting", end=" ")
                return num1 - num2
            elif operation == "multiply":
                print(f"The result of multiplying", end=" ")
                return num1 * num2
            elif operation == "divide":
                if num2 != 0:
                    print(f"The result of dividing", end=" ")
                    return num1 / num2
                else:
                    raise ValueError("Cannot divide by zero.")
            else:
                raise ValueError("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'.")
        except ValueError as v:
            print(str(v))
def ask_input_sanitized(strInput: str) -> float:
    while True:
        try:
            number = float(input("Enter the " + strInput + ": "))
            return number
        except ValueError:
            print("Invalid " + strInput + ". Please enter valid input")

def main():
    
    print(f"===== Simple Calculator =====")

    # Ask the user for sample input    
    num1 = ask_input_sanitized("first number")
    num2 = ask_input_sanitized("second number")

    # Perform the calculation and display the result
    result = simple_calculator(num1, num2)
    print(f"{num1} and {num2} is {result}")



if __name__ == "__main__":
    main()
