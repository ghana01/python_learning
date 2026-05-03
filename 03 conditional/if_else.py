
#1 age grp categorization

input() # it help us to take input from cmd line/terminal
age=int(input("Enter your age: ")) #we are using the int() function to convert the input from a string to an integer because the input() function always returns a string and we want to compare the age with an integer value so we need to convert it to an integer

# age=input("enter your age: ") # in this it take user input but it take it as a string  so before taking define the  datatype of input

if age<13:
    print("you are child")# if the age is less than 18 then it will print "you are minor"

elif  age <20:
    print("your are teenager")

elif  age <60:
    print("you are adult")

elif age>=60:
    print("you are senior citizen")

else:
    print("super human")



# Q2  MOvie ticket price on age 12$ for adult and over ,8$ for children  ,Everyone gets 2$ discount on wednesday

day=input("enter the day of the week: ") # we are taking input from the user for the day of the week and storing it in a variable called day

age=int(input("Enter  your age"))

if day=="Wednesday":
    if age <18:
        print("the ticket price is 6$") # if the day is Wednesday and the age is less than 18 then it will print "the ticket price is 6$" because the original price for children is 8$ and they get a 2$ discount on Wednesday so the new price will be 8$ - 2$ = 6$
    else:
        print("the ticket price is 10$") # if the day is Wednesday and the age is 18 or above then it will print "the ticket price is 10$" because the original price for adults is 12$ and they get a 2$ discount on Wednesday so the new price will be 12$ - 2$ = 10$
else:
    if age <18:
        print("the ticket price is 8$") # if the day is not Wednesday and the age is less than 18 then it will print "the ticket price is 8$" because the original price for children is 8$ and they do not get a discount on other days so the price will remain 8$
    else:
        print("the ticket price is 12$") # if the day is not Wednesday and the age is 18 or above then it will print "the ticket price is 12$" because the original price for adults is 12$ and they do not get a discount on other days so the price will remain 12$  

# price =12 if age >=18 else 8  # this is a ternary operator which is a shorthand for an if-else statement it is used to assign a value to a variable based on a condition in this case we are assigning the value 12 to the variable price if the age is greater than or equal to 18 and we are assigning the value 8 to the variable price if the age is less than 18


#Q3   assign a letter grade based on a student score a(90-100), b(80-89), c(70-79), d(60-69), f(<60)

score =int(input("enter your score: "))

if score >=90 and score <=100:
    print("Grade: A")
elif score >=80 and score <90:
    print("Grade: B")
elif score >=70 and score <80:
    print("Grade:C")
elif score >=60 and score <70:
    print("Grade :D")
elif score <60:
    print("Grade :F")
else:
    print("NA")

#Q4 check which fruit is this according to  their color

fruit="Banana"
color ="Yellow"

if fruit =="Banana":
    if color =="Green":
        print("This is a unripe banana")
    elif color =="Yellow":
        print("This is a ripe banana")
    else:
        print("This is a banana with an unknown ripeness")