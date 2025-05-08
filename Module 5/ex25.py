#THe below statement initializes a while loop
while True:
    #The code under try is run. If an error occurs, then the code under except is run
    try:
        x = int(input("What's x?"))
    except ValueError:
        print("x is not an integer")
    #The code under else is run if there is no exception. This will end the loop prematurely and start it again prompting the user to enter a valid value of x
    else:
        break
#The statement below will print the value of x
print(f"x is {x}")