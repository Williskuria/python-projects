def my_sum(n):
    if n == 0:
        return 0
    else:
        return n + my_sum(n -1)
    
print(my_sum(5))

def power(m, n):
    if n == 0:
        return 1
    else:
        return m * power(m, n - 1)
    
print(power(2, 3))


def countdownn(n):
    if n == 0:
        print("Blast off!")
    else:
        print(n)
        countdownn(n-1)
    
countdownn(5)