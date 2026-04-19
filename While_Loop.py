correct_password = "Wkuria@123"
attempts = 3

password = input("Enter password: ")



while password != correct_password and attempts > 1:
    attempts -= 1
    print(f"You have {attempts} attempts left!")
    password = input("Enter password: ")
if password == correct_password:
    print("Success!")
else:
    print("You have no attempts left! ")




