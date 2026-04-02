"""PE2 Topic 8: Lambda Functions & Functional Tools"""

numbers = [1, 2, 3, 4, 5, 6]

square = lambda n: n * n
print("Square of 4:", square(4))

squared = list(map(lambda n: n * n, numbers))
print("map() squared:", squared)

evens = list(filter(lambda n: n % 2 == 0, numbers))
print("filter() evens:", evens)
