people = 30
cars = 40
trucks = 15
#checks if the value stored in the variable cars is greater than people. If True it prints "We should take the cars"
if cars > people:
    print("We should take the cars.")
#else if the number of cars is less than the number of people then it prints "We should not take the cars"
elif cars < people:
    print("We should not take the cars.")
#for any case other than the two above, the statement "We can't decide" is printed
else:
    print("We can't decide.")
#checks if the value stored in the variable trucks is greater than cars. If True it prints "That's too many trucks"
if trucks > cars:
    print("That's too many trucks.")
#else if the number of trucks is less than the number of cars then it prints "Maybe we could take the cars."
elif trucks < cars:
    print("Maybe we could take the cars.")
#for any case other than the two above, the statement "We still can't decide" is printed
else:
    print("We still can't decide.")
#if the value of the variable people is greater than trucks "Fine, let's stay home then." is printed
if people > trucks:
    print("Fine, let's stay home then.")
#for any case other than the above, the statement "Alright, let's just take the trucks" is printed
else:
    print("Alright, let's just take the trucks.")