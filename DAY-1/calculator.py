choice = int(input("Please pick a choice from the below options: \n"
             " 1.Addition \n 2.Subtraction \n 3.SquareRoot \n"
             " 4.Multiplication \n 5.Power \n 6.Division \n 7.Exit The Program "))

def my_calculator(choice):
    if choice == 3:
        square = int(input("Please insert number:"))
        root = square ** 0.5
        print(f"The square root is {root}")
    elif choice == 7:
            print("See you again next time")
            return
    else:
        number_One = int(input("Please insert first number:"))
        number_Two = int(input("Please insert the second number:"))
        if choice == 1:
            sum = number_One + number_Two
            print(f"The sum of the two numbers is {sum}")
        elif choice == 2:
            diff = number_One - number_Two
            print(f"The difference of the two numbers is {diff}")
        elif choice == 4:
            multiple = number_One * number_Two
            print(f"The multiple of the two numbers is {multiple}")
        elif choice == 5:
            power = number_One ** number_Two
            print(f"{number_One} raised to the power of {number_Two} is {power}")
        elif choice == 6:
            division = number_One / number_Two
            print(f"{number_One} divided by {number_Two} is {division}")
        else:
            print("Incorrect choice")
    

my_calculator(choice)



