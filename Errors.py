# while True print('Hello world')
# Syntax error as its missing semicolon Python compiler gives error at word which is after error

try:
    x = 3 / 0
except ArithmeticError:
    print("CAN'T DIVIDE BY ZERO")
finally:
    print("WHATEVER EXCEPTION OCCUR THIS WILL PRINT")

# HANDLING MULTIPLE EXCEPTIONS
try:
    x = 3 / 0
except (RuntimeError, TypeError, NameError):
    print("CAN'T DIVIDE BY ZERO")
finally:
    print("WHATEVER EXCEPTION OCCUR THIS WILL PRINT")
