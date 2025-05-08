#This is the main function
def main():
    #It calls the function get_int as the prompt "What's x? as the parameter"
    x = get_int("What's x? ")
    #This statement prints the value of x that was got from the called function
    print(f"x is {x}")

#This is the get_int function
def get_int(prompt):
    #This statement initializes a while loop that always runs if True
    while True:
        #The code in try is run. If there is an exception, then the code under except is run
        try:
            return int(input(prompt))
        #This is the piece of code that is run if there is a ValueError exception
        except ValueError:
            #The line below indicates that no further processing of the code is required. 
            pass


main()