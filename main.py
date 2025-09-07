def calculator():
    while True:
        print("\n+ , - , / , *")
        choice = input("Choose Your Choice : ")

        number01 = int(input("Enter Number 01 : "))
        number02 = int(input("Enter Number 02 : "))

        match choice:
            case "+":
                result = number01 + number02
            case "-":
                result = number01 - number02
            case "*":
                result = number01 * number02
            case "/":
                if number02 == 0:
                    print("Error: Cannot divide by zero")
                    continue
                result = number01 / number02
            case _:
                print("Invalid Choice")
                continue

        print("Answer is:", result)

        answer = input("Do you want to continue (Y/N) : ")
        if answer.lower() != "y":
            print("Exiting Calculator. Goodbye!")
            break


if __name__ == "__main__":
    calculator()
