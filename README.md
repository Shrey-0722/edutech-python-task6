# Edutech Solution Python Internship

# Task 6: Exception Handling & Debugging


## code: 

```python
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
```

## Output
```
Enter the first number: 10
Enter the second number: 5
Result: 2.0
Program Execution completed.
```

### Division by Zero
```
Enter the first number: 10
Enter the second number: 0
Error: Cannot divide by zero.
Program Execution completed.
```

### Invalid Input
```
Enter the first number: abc
Invalid input. Please enter a valid integer.
Program Execution completed.
```

### Error Log File (`error_log.txt`)
```
2026-06-02 18:58:20 | ERROR | ZeroDivisionError: User attempted division by zero.
2026-06-02 18:58:27 | ERROR | ValueError: User entered a non-integer value.
```

---

## 📖 Deliverables

## 1. What is an Exception?
An exception is an event that occurs during program execution which disrupts the normal flow of instructions. In Python, exceptions are objects that are raised when errors or unexpected conditions happen — such as dividing by zero (`ZeroDivisionError`), providing invalid input (`ValueError`), or trying to access a missing file (`FileNotFoundError`).

If not handled properly, exceptions cause the program to crash. Python provides a structured mechanism (`try-except-finally`) to catch and handle these exceptions gracefully.

## 2. Try vs Except Blocks

| Block     | Purpose                                                                 |
|-----------|-------------------------------------------------------------------------|
| `try`     | Contains the code that may raise an exception during execution.     |
| `except`  | Catches and handles specific exceptions, preventing a program crash.|
| `finally` | Always executes after try/except, regardless of whether an exception occurred. Useful for cleanup tasks. |

**How they work together:**
- The try block is executed first.
- If an exception occurs, Python skips the remaining try code and jumps to the matching except block.
- If no exception occurs, the except block is skipped entirely.
- The finally block runs no matter what — whether the code succeeded or an exception was caught.

---

## Interview Questions: Building Robust Applications

### Q1: How does exception handling make an application robust?
**A:** Exception handling prevents the application from crashing when unexpected errors occur. Instead of terminating abruptly, the program catches errors, provides user-friendly messages, logs the issue for debugging, and continues running. This ensures a smooth experience even when things go wrong.

### Q2: What is the difference between `try`, `except`, and `finally`?
**A:**
- `try` — Contains code that might fail at runtime.
- `except` — Catches specific errors and handles them gracefully.
- `finally` — Always runs, whether or not an error occurred. Used for cleanup tasks like closing files or database connections.
---

## Final Outcome

| Deliverable             | Status      |
|-------------------------|-------------|
| Debugged Python script  | ✅ Complete |
| try-except-finally demo | ✅ Complete |
| Interview Q&A           | ✅ Complete |
| README documentation    | ✅ Complete |

---
