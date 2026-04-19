import random

print(random.randrange(10, 20))

list1 = ['a', 'b', 'c', 'd', 'e']

# get random item from list1
print(random.choice(list1))

# Shuffle list1
random.shuffle(list1)

# Print the shuffled list1
print(list1)

# Print random element
print(random.random())


import math

print(math.pi)
radius = int(input("Enter the radius: "))


solution = math.pi * int(math.pow(radius, 2))
print("The area of the circle is ", solution)