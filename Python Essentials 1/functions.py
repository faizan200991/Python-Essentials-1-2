"""PE1 Topic 8: Functions"""

# Global variable
greeting = "Hello"


def greet(name):
    """Return a greeting message."""
    # Local variable
    message = f"{greeting}, {name}!"
    return message


def add_numbers(x, y=0):
    """Return the sum of two numbers."""
    return x + y


print(greet("Student"))
print("Sum:", add_numbers(10, 5))
print("Sum with default:", add_numbers(10))
