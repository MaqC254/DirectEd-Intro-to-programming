#Try to get input from user. We use try in cases where errors arelikely to occur
try:
    x = int(input("What's x?"))
#incase there is a value error then the message is printed and the program is terminated
except ValueError:
    print("x is not an integer")
# The statement below is printed to the console
print(f"x is {x}")