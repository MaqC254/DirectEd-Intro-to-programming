print("""You enter a dark room with two doors.
Do you go through door #1 door #2  door #3 or door #4?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off.  Good job!")
    elif bear == "2":
        print("The bear eats your legs off.  Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

elif door == "3":
    print("Medusa stands on the other side of the door.")
    print("1. Look into her eyes using a mirror.\n2. Look directly at her and scream.\n3. Look away.")
    choice = input('>')

    if choice == "1":
        print("You look through the mirror and slice her neck open. You defeat her")
    elif choice == "2":
        print("You immediately turn into stone")
    elif choice == "3":
        print("Her guards stab your back as you look away")
    else:print("You just stand there as the door closes and smashes your face killing you") 

if door == "4":
    print("It is a dark room. You have no flashlight but something is shining at the corner")
    print("What do you do?")
    print("1. Head to the light.")
    print("2. Ask if anyone is there.")

    dark_choice = input("> ")

    if dark_choice == "1":
        print("You find a chest full of gold")
    elif dark_choice == "2":
        print("You bother an evil spirit in its sleep. It eats your face off.  Good job!")
    else:
        print("This did not end well. You stumble in the dark and die")

else:
    print("You stumble around and fall on a knife and die.  Good job!")