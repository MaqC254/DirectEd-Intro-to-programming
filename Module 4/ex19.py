# Create our own function
def hello(to="world", myName = "Maxwell"):
    print("hello,", to)
    print("hello,", myName)

def main():
# Output using our own function
    name = input("What's your name? ")
    hello(name)

# Output without passing the expected arguments
hello()



main()