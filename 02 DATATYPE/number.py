#number is strong game in python     ,pythong handel complex,decimal,integer, float, binary, octal, hexadecimal number
#number is immutable data type   , it handel many verity of number like int, float, complex, decimal, binary, octal, hexadecimal number


#number is not a single object it  is a collection of many type of number like int, float, complex, decimal, binary, octal, hexadecimal number

#boolean is also number in python
#boolean is a subclass of int in python   , it is a subclass of int because it can be used in place of int and it can be used in arithmetic operations like int



x=2
y=3
x+y #5
x-y # -1
x*y #6
x/y #0.6666666666666666
x//y #0
x%y #2
x**y #8
z=5

x+y*z #2+3*3=11   using precison table we can see that multiplication has higher precedence than addition so we will do multiplication first and then addition
(x+y)*z #(2+3)*3=15   using precison table we can see that parentheses has higher precedence than multiplication so we will do addition first and then multiplication

40 +2.23 #42.23  because when we add an integer and a float the result is a float


float(40) #40.0  because when we convert an integer to a float the result is a float

'chat'+'code' # 'chatcode' because when we add two strings the result is a string concatenation of the two strings
100**2 #10000 because when we raise a number to the power of another number the result is the first number multiplied by itself the number of times specified by the second number
2**1000

#we can also use the math module to perform mathematical operations on numbers
result =1/3.0
print(result) #0.3333333333333333 because when we divide an integer by a float the result is a float


#comparision operators
x=10
y=20
x>y #false because 10 is not greater than 20
x<y #true because 10 is less than 20
x>=y #false because 10 is not greater than or equal to 20
5.0==5 #true because when we compare a float and an integer the result is true if they are equal in value
5.0 is 5 #false because when we compare a float and an integer the result is false because they are different types in memory

x,y,z=1,2,3
x<y<z #true because 1 is less than 2 and 2 is less than 3
x<y>z #false because 1 is less than 2 but 2 is not greater than 3x
x<Y<z #true because 1 is less than 2 and 2 is less than 3
x<y and y<z #true because 1 is less than 2 and 2 is less than 3   


1==2 <3 #false because 1 is not  equal to 2 and 2 is less than 3 

import math
math.sqrt(16) #4.0 because when we take the square root of a number the result is a float
math.floor(2.9) #2 because when we take the floor of a number the result is the largest integer less than or equal to the number

math.ceil(2.1) #3 because when we take the ceiling of a number the result is the smallest integer greater than or equal to the number
math.trunc(2.9) #2 because when we take the trunc of a number the result is the integer part of the number it give the value towar zero
math.trunc(-5.6) #-5 because when we take the trunc of a number the result is the integer part of the number it give the value towar zero


#pythong give usa precise value if we want to get the precise value of a number we can use the decimal module


2+4j   #this will give an error because we are trying to add a complex number and an integer without using the correct syntax for complex numbers in python. In python,
#we can represent complex numbers using the syntax a+bj where a is the real part and b is the imaginary part. So if we want to add 2 and 3j we can write it as 2+3j which will give us the result (2+3j)


import random  #this will import the random module which contains functions for generating random numbers
# and many function for generating random numbers like random.randint(), random.uniform(), random.choice(), random.shuffle() etc


random.random() #this will give us a random number between 0 and 1

0.1+0.4+0.1 #0.6000000000000001 because of the way floating point numbers are represented in memory, it can lead to precision issues when performing arithmetic operations on them. In this case, the result is not exactly 0.6 but a very close approximation due to the limitations of floating point representation.

0.1+0.1+0.1 -0.3 #5.551115123125783e-17 because of the way floating point numbers are represented in memory, it can lead to precision issues when performing arithmetic operations on them. In this case, the result is not exactly 0 but a very close approximation due to the limitations of floating point representation.
from decimal import Decimal

Decimal(0.1)+Decimal(0.1)+Decimal(0.1) - Decimal(0.3) #Decimal('0.0') because the decimal module provides a way to perform decimal floating point arithmetic with more precision than the built-in float type, so the result is exactly 0 when using Decimal instead of float.

from frctions import Fraction
myFra =Fraction(1,3) #this will create a fraction object with the value 1/3
print(myFra) #1/3 because the fraction module provides a way to represent rational numbers


setone={1,2,3,4,5}
setone & {3,4,5,6,7} # {3, 4, 5} because the & operator is used to find the intersection of two sets, which is the set of elements that are common to both sets. In this case, the common elements between setone and {3,4,5,6,7} are 3, 4, and 5.  

#on set we can perform all the operation of set like subset ,superset, union, intersection, difference, symmetric difference etc

#one thing is remebr  in this setone-{1,2,3,4,5} is a set and {3,4,5,6,7} is also a set but when we use the & operator it will give us the intersection of the two sets which is {3,4,5} because 3,4,5 are common in both sets.


