def addition (number1, number2):
    result = number1 + number2
    return result

def subtraction (number1, number2):
    result = number1 - number2
    return result

def multiplication (number1, number2):
    result = number1 * number2
    return result

def division (number1, number2):
    result = number1 / number2
    return result

def remainder (number1, number2):
    result = number1 % number2
    return result

def exponent (number1, number2):
    result = number1 ** number2
    return result

def gcd (number1, number2):
    number1, number2 = number2, number1 % number2
    return number1

def lcm (number1, number2):
    return abs(number1 * number2) // gcd (number1, number2)

while True:
    print("1. Addition \n2.Subtraction \n3. Multiplication \n4. Division \n5. Remainder"
          "\n6. Exponent \n7. HCF \n8. LCM")

    try:
        user_input = int(input("Enter operation to perform (1-8): "))
    except ValueError:
        print("Invalid Option! Please enter a number")
        continue

    if user_input > 8 or user_input < 1:
        print("Invalid Option! Please enter a number")

    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    match user_input:
        case 1:
            value = addition(num1, num2)
        case 2:
            value = subtraction(num1, num2)
        case 3:
            value = multiplication(num1, num2)
        case 4:
            if num2 != 0:
                print("Division by 0 not possible.")
                continue
            else:
                value = division(num1, num2)
        case 5:
            if num2 != 0:
                print("Division by 0 not possible.")
                continue
            else:
                value = remainder(num1, num2)
        case 6:
            value = exponent(num1, num2)
        case 7:
            value = gcd(num1, num2)
        case 8:
            value = lcm(num1, num2)
        case _:
            print("Invalid Option! Please try again!")
            continue


    print("Result:",value)

    repeat = input("Do you wish to continue? (enter 'no' or 'n'): ")
    if repeat.lower() == "no" or repeat.lower() == "n":
        print("Have a good day! Calculator closed")
        break

print("Program Terminated")
