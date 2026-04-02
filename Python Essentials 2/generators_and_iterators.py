"""PE2 Topic 9: Generators & Iterators"""

numbers = [10, 20, 30]
iterator = iter(numbers)

print("Iterator values:")
print(next(iterator))
print(next(iterator))
print(next(iterator))


def count_up_to(limit):
    current = 1
    while current <= limit:
        yield current
        current += 1


print("Generator values:")
for value in count_up_to(5):
    print(value)

# Generator expression
gen_expr = (n * 2 for n in range(1, 4))
print("Generator expression:", list(gen_expr))
