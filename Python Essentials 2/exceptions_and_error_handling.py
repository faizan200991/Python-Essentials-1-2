"""PE2 Topic 3: Exceptions & Error Handling"""


def divide(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b


try:
    x = int(input("Enter numerator: "))
    y = int(input("Enter denominator: "))
    print("Result:", divide(x, y))
except ValueError as err:
    print("ValueError:", err)
except Exception as err:
    print("Unexpected error:", err)
finally:
    print("Execution finished.")
