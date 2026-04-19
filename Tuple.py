# Tuple - A tuple is a collection similar to a Python list. The primary difference is that we cannot modify a tuple once it is created.

numbers = (1, 5, -4)

print(numbers)

Friends = tuple(("Walter", "Maish", "Jim"))

print(Friends)

blank = ()

print(blank)

print(Friends[0])

print(len(Friends))

for friend in Friends:
    print(friend)


colors = ('red', 'orange', 'blue')

print('yellow' in colors)    # False
print('red' in colors)       # True

print("maish" in Friends)
print("Willis" in Friends)