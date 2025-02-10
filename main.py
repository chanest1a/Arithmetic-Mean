print("Welcome! Please choose one of the options. Option 1: for 2 numbers. Option 2: calculates the arithmetic mean of 3 numbers.")


option = int(input("Please choose an option (1 or 2): "))

if option == 1: 
    number = float(input("Enter the 1st number: "))
    number1 = float(input("Enter the 2nd number: "))
    conclusion = (number + number1) / 2 
    print("Arithmetic Mean:", conclusion)

elif option == 2:
    number3 = float(input("Enter the 1st number: "))
    number4 = float(input("Enter the 2nd number: "))
    number5 = float(input("Enter the 3rd number: "))
    conclusion = (number3 + number4 + number5) / 3 
    print("Arithmetic Mean:", conclusion)

else:
    print("Invalid option! Please choose 1 or 2.")
