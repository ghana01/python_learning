
#basic function syntax

def square_of_num(x):
    return x**2

result =square_of_num(5)

print("The square of 5 is:", result) #The square of 5 is: 25 because when we define a function with the name square_of_num and we pass a parameter

#function with multiple parameters  -> create a function that takes two number as  paramater and  returns their sum

def sum_of_numbers(a,b):
    return a+b

result =sum_of_numbers(4,8)

print("TThe sum of two numbers is :", result) #The sum of two numbers is : 12 because when we define a function with the name sum_of_numbers and we pass two parameters a and b and we return the sum of a and b which in this case is 4 + 8 = 12


#ploymorphism in function ->write a function   that multiply two numbers but can also accept and multiply string


def multiply(a,b):
    return a*b

result1=multiply(4,5)

print("The product of 4 and 5 is:", result1) #The product of 4 and 5 is: 20 because when we define a function with the name multiply and we pass two parameters a and b and we return the product of a and b which in this case is 4 * 5 = 20

result2=multiply("Hello", 3)

print("The result of multiplying 'Hello' by 3 is:", result2) #The result of multiplying 'Hello' by 3 is: HelloHelloHello because when we pass a string and an integer to the multiply function, it repeats the string the specified number of times


#create a function that return both the area and cicumference of circle given it radius\

import math
from turtle import circle

def circle(r):
    area =math.pi*r**2
    circumference =2*math.pi*r
    return area,circumference


circle(5) #(78.53981633974483, 31.41592653589793) because when we define a function with the name circle and we pass a parameter
  # yes  in python we can return multiple value from a function by seperating them with comma and in return we get tuple value

# we can also handel this like  a.b = circle(5) #a=78.53981633974483 and b=31.41592653589793 because when we return multiple values from a function it will return a tuple and we can unpack the tuple into separate variables which in this case is a and b where a will be the area of the circle and b will be the circumference of the circle


a, b = circle(6)  # function is fisr class object in python which means we can assign the function to a varible
# and then we call the function using the varbile name and passing the argument to it which in this case is 6 to get the area and circumference of the circle with radius 6

#write a function that great user if no name is provide it should greet with defaul name

def greet(name="User"):
    return f"Hello, {name}!"


print(greet())  # Output: Hello, User!
print(greet("Alice"))  # Output: Hello, Alice!



# create a lamda  function to compute the cube of a number

def cube(x):
    return x**3

result = cube(3)
print("The cube of 3 is:", result) #The cube of 3 is: 27 because when we define a function with the
#name cube and we pass a parameter x and we return the cube of x which in this case is 3**3 = 27

cube_lambda = lambda x: x**3    # we can also define a lambda function to compute the cube
#of a number by using the lambda keyword followed by the parameter and the
# #expression which in this case is x**3 and we assign it to a variable cube_lambda 
# #so we can call the lambda function using the variable name and passing the argument 
# #which in this case is 3 to get the cube of 3 which is 27
result_lambda = cube_lambda(3)
print("The cube of 3 is:", result_lambda) #The cube of 3 is: 27 because when we define a lambda function with the name cube_lambda and we pass a parameter x and we return the cube of x which in this case is 3**3 = 27

#lamda function means -> a small anonymous function that can take any number of arguments
# but can only have one expression which is evaluated and returned when 
# the function is called and we can use lambda functions for simple operations
# or as an argument to higher-order functions like map(), filter(), and reduce() 
# to perform operations on iterables without the need to define a separate function 
# using the def keyword.
#purpose of using the lamda function is to create small, one-time,
# anonymous functions that can be used in a concise way without the need to
# define a separate function using the def keyword. Lambda functions are
# often used for simple operations or as an argument to higher-order functions like
# map(), filter(), and reduce() to perform operations on iterables without the need to define
# a separate function. They can help make code more concise and readable when used appropriately.




#function with *args and **kwargs -> these are used to handle variable number of arguments
#*args ->in this when we pass the argument it will be treated as a tuple and we can iterate over the tuple to get the values of the arguments
#**kwargs -> in this when we pass the argument it will be treated as a dictionary and we can iterate over the dictionary to get the key-value pairs of the arguments

# in a function where *args is used to handle non-keyworded variable length arguments and
# **kwargs is used to handle keyworded variable length arguments
#write a function that varible number of argument and return their sum
# in this **kwarg we can give the name of the paramater as  we want and we can also
# give the value of the parameter as we want and we can also use the items() method
# to iterate over the key-value pairs of the kwargs dictionary and
# we can print each key and value in a formatted string which in this
# case is name: Alice, age: 30, city: New York

def sum_of_numbers(*args):   
    return sum(args)

result =sum_of_numbers(1,2,3,4,5)

def sum(*args):
    total=0
    for i in args:
        total +=i
    
    return total

print("The sum of the numbers is:", result) #The sum of the numbers is: 15 because when we define a function with the name sum_of_numbers and we use *args to handle variable number of arguments and we return the sum of the arguments using the built-in sum() function which in this case is 1 + 2 + 3 + 4 + 5 = 15

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Alice", age=30, city="New York") #name: Alice
                                                     #age: 30
                                                     #city: New York because when we define a function with the name print_info and we use **kwargs to handle keyworded variable length arguments and we iterate over the key-value pairs of the kwargs dictionary using the items() method and we print each key and value in a formatted string which in this case is name: Alice, age: 30, city: New York    
                                                     



#write a generoter function that yeild even number up to speficied limit

#yeild means -> it is used in a function to make it a generator function 
# which is a special type of function that can be paused and resumed and
# it allows us to iterate over a sequence of values without the need to store
# the entire sequence in memory at once. When a generator function is called,
# it returns an iterator object that can be used to iterate over the values produced by the generator.
# The yield statement is used to produce a value and pause the execution of the generator function
# until the next value is requested.


def even_generator(limit): 
    li=[]
    for num in range(2,limit+1,2):
        li.append(num)
    return li

#in above even_generator  function we are using a for loop to itirate over the range of number from 2 to limit
# and we are appending it to the list and we are returning the list which will give us the even number up to the specified limit but in this case we are storing the entire sequence of even numbers in memory at once which is not efficient if the limit is very large
# but the problem is we dont want list we want the number directly without storing it into memory so 
#we can use the yield statement to produce a value and pause the execution of the generator function
# until the next value is requested which will allow us to iterate over a sequence
# of even numbers without the need to store the entire sequence in memory at once

def even_generator(limit):       
    for num in range(2,limit+1,2):
        yield num
            

for even in even_generator(10):
    print(even) #2
                #4
                #6
                #8
                #10 because when we define a generator function with the name even_generator and we use the yield statement to produce a value and pause the execution of the generator function until the next value is requested and we iterate over the generator using a for loop we will get the even numbers up to the specified limit which in this case is 2, 4, 6, 8, 10 because we are iterating over the range of numbers from 2 to limit with a step of 2 which will give us only even numbers
            




#recursive  function -> a function that calls itself in order to solve a problem by breaking
# it down into smaller, more manageable subproblems. A recursive function typically has
# a base case that stops the recursion and a recursive case that continues to call
# the function until the base case is reached.


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)





print(factorial(5))  # Output: 120
