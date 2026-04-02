"""PE2 Topic 1: Modules & Packages"""

import math
from datetime import date

print("Square root of 49:", math.sqrt(49))
print("Today is:", date.today())


def area_of_circle(radius):
    return math.pi * radius ** 2


if __name__ == "__main__":
    print("This file is being run directly.")
    print("Area with r=3:", area_of_circle(3))
