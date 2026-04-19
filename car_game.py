while True:

    value = input("> ")
    if value == "start":
        print("Car started...Ready to go!")
    elif value == "stop":
        print("Car stopped.")
    elif value == "quit":
        break
    else:
        print("I don't understand that.....")
