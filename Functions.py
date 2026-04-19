'''def count_events(n, m):
    count = 0
    for i in range(n, m + 1):
        if i % 2 != 0:
            print(i)
            count += 1
    return count
        
count_events(1, 10)

'''

'''
# return if positive or negative
def is_positive(n):
    if n > 0:
        return True
    else:
        return False
    
print(is_positive(5))
print(is_positive(-5))
'''

'''def reverse_number(n):
    number = str(n)
    number = number[::-1]
    return int(number)

print(reverse_number(543))'''

def get_bigger(m, n):
    p = max(m, n)
    return p

print(get_bigger(81, 9))

