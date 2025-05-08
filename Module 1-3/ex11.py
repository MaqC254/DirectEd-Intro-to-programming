#Example for the or operator
x = int(input("What's x? "))
y = int(input("What's y? "))
#if x is not equal to y, then x is not equal to y is printed else x is equal to y is printed
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

#Example for the and operator
#initializes the value of score to the user input aand converts it to an integer
score = int(input("Score: "))
#if the value of the score is from 90 to 100, it will output Grade: A
if score >= 90 and score <= 100:
    print("Grade: A")
#if the value of the score is from 80 to 89, it will output Grade: B
elif score >=80 and score < 90:
    print("Grade: B")
#if the value of the score is from 70 to 79, it will output Grade: C
elif score >=70 and score < 80:
    print("Grade: C")
#if the value of the score is from 60 to 69, it will output Grade: D
elif score >=60 and score < 70:
    print("Grade: D")
#if the grade is not in any of the above ranges, then Grade: F will be printed
else:
    print("Grade: F")

#Example for the not operator.
isStudent=int(input("Are you a student ?: press 1 for yes 2 for no "))
#if the statement in the brackets evaluates to False, meaning that the value of isStudent is neither 1 nor 2 then I don't understand is printed in the console
#not will change the evaluation of the statement in the brackets to the opposite
if not (isStudent==1 or isStudent==2):
    print("I don't understand")
#If the value of student is 1, then Aha! You are a student will be printed to the console
elif isStudent==1:
    print("Aha! You are a Student!")
#if the value of student is none of the above (value is 2), then the statement below will be printed
else:
    print("Only Students can use this program, Bye!")