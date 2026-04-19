# upper method
def shout(name):
    u = name.upper()
    return u

print(shout("willis"))
print(shout("nganga"))

# number of words in a sentence
def counts(string):
    s = string.split()
    return len(s)

print(counts("I love Python"))

# remove spaces in a string

def remove_spaces(string):
    r = string.replace(" ", "")
    return r

print(remove_spaces("hello world"))

# capitalize first word
def capitalize(string):
    cap = string.title()
    return cap

print(capitalize(" i love python"))

#join two strings

def join_strings(string1, string2):
    join = string1 + " " + string2
    return join

print(join_strings("Hello", "World"))

# bigger number

def bigger(m, n):
    b = max(m, n)
    return b

print(bigger(5, 8))

