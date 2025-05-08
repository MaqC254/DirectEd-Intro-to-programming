#This is the main function
def main():
#This line sets x to be the value returned by the function get_int() that has been called
    x = get_int()
#The value is then printed here
    print(f"x is {x}")

#This is the get_int function
def get_int():
#Initializes a while loop
    while True:
#The code under try is ran
        try:
            return int(input("What's x?"))
#The code under except is run if there is an exception of ValueError
        except ValueError:
        #The error message below is printed to the console
            print("x is not an integer")

#This statement will run the main function
main()