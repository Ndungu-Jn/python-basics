#Error handling
try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    z = int(input("Enter third number: "))


    print(x * y  * z)
except:
    print("Error! Enter valid numbers")