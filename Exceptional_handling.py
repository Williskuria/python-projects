while True:
    try:
        number = int(input("Enter a  number: "))
        divide = 100 / number
        print(divide)
        break

    except ZeroDivisionError:
        print("You cant divide by zero!")

    except ValueError:
        print("That's not a number!")

    finally:
        print("program finished!")

