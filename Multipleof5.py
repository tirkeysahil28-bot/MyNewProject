#Check given number is multiple of 5
def check_multiple_of_5(number):
    if number % 5 == 0:
        print(number, "is a multiple of 5")
    else:
        print(number, "is not a multiple of 5")

# Take input from user
num = int(input("Enter a number: "))
check_multiple_of_5(num)