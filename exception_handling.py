import logging

# Configure logging to write errors to error_log.txt
logging.basicConfig(
    filename="error_log.txt",
    level=logging.ERROR,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2

    print("Result:", result)

except ValueError:
    print("Invalid input. Please enter a valid integer.")
    logging.error("ValueError: User entered a non-integer value.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
    logging.error("ZeroDivisionError: User attempted division by zero.")

finally:
    print("Program Execution completed.")