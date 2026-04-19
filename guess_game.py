
i = 0

while i < 3:
    guess = int(input("Enter a number: "))
    i += 1
    if guess == 9:
        print("success!")
        break
else:
    print("Game over")
