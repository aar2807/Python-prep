#Lesson3
#Functions, Conditionals and Loops

#Functions
def motivation():
    print("You’re doing amazing, Aarna.")
    print("Keep learning. Keep winning.")
motivation()

#Parameters
def intro(name, age):
    print("Hello", name + ", you are", age, "years old.")
intro("Aarna", 17)

#Loops
#for loop
for i in range(1, 6):
    print("Day", i, "- Keep coding!")
#while loop
count = 1
while count <= 3:
    print("Try", count)
    count += 1
    
#Conditionals(if, elif, else)    
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Excellent!")
elif marks >= 75:
    print("Very Good!")
elif marks >= 50:
    print("Good.")
else:
    print("Work harder.")
    
#Practice
#1. Make a function square() that prints the square of a number.
def square():
	num=int(input("Enter the number to be squared: "))
	square=num*num
	print("Square of number is: ",square)
square()
#2. Write a for loop that prints all even numbers from 1 to 10.
print("All even numbers between 1 to 10 are: ")
for i in range(11):
	if i%2==0:
		print(i)
#3. Create a while loop that counts down from 5 to 1.
print("Space")
count = 5
while count >= 1:
    print(count)
    count -= 1
#4. Ask user their name and age, and tell them if they are eligible for a driving license (age ≥ 18).
print("Driving licence eligibility test:")
name=input("Enter your name: ")
age=int(input("Enter your age: "))
if age >= 18:
	print("You are eligible for a driving licence.")
else:
	print("Not eligible.")
print("Completed")

#Lesson3: Done	