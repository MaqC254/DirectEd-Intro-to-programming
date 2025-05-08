#This is the main fuction
def main():
#Here we call the function print_square and pass the parameter 3 as the size
    print_square(3)

#This is the print_square function
def print_square(size):
#The for loop will run for the number in the variable size and in each iteration, the function print_row will be called
    for i in range(size):
        print_row(size)

#When print_row is called it prints the character # the number of times equal to size
def print_row(width):
    print("#" * width)


main()