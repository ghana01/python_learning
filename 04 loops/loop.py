#Q1 count Positive Numbers in a give list 

numbers = [1, -2, 3, 4, -5, 6]

positive_count =0
for num in numbers:
    if num >0:
        positive_count +=1

print("Number of positive numbers in the list:", positive_count) #Number of positive numbers in the list: 4 because when we use a for loop to iterate over a list and we use an if statement to check if the number is greater than 0 it will count the number of positive numbers in the list which in this case is 4 because 1, 3, 4, 6 are greater than 0
#Q2 Sum of even number in a given list 
even_sum=0
for num in numbers:    # for i in range(1,10): we can also use a for loop with a range to iterate over a list of numbers which in this case is from 1 to 10
    if num %2 ==0:
        even_sum +=num

print("Sum of even numbers in the list:", even_sum) #Sum of even numbers in the list: 10 because when we use a for loop to iterate over a list and we use an if statement to check if the number is divisible by 2 it will sum the even numbers in the list which in this case is 10 because 2, 4, 6 are even numbers


#Q3 Multiplication table printer -> print the multication table for give number up to 10 but skip the fifth iteration

number =5

for i in range (1,11):
    if i==5:
        continue #we can also use the continue statement to skip the current iteration of the loop and move to the next iteration
    #which in this case is when i is equal to 5 we will skip the current iteration and move to the next iteration
    # which is when i is equal to 6
    else:
        print(f"{number} x {i} = {number*i}") #5 x 1 = 5
                                              #5 x 2 = 10
                                              #5 x 3 = 15
                                              #5 x 4 = 20
                                              #5 x 6 = 30
                                              #5 x 7 = 35
                                              #5 x 8 = 40
                                              #5 x 9 = 45
                                              #5 x 10 = 50 because when we use a for loop to iterate over a range of numbers and we use an if statement to check if the number is equal to 5 we will skip the current iteration and move to the next iteration which is when i is equal to 6 so we will print the multiplication table for the number 5 up to 10 but skip the fifth iteration which is when i is equal to 5




#Q4 reverse the string using loop

string ="hello world"
reverse_string =""

for char in string:
    reverse_string =char + reverse_string #we are adding the current character to the reverse string which is initially an empty string so the new reverse string will be the current character followed by the previous reverse string which in this case will be "h" + "" = "h" then "e" + "h" = "eh" then "l" + "eh" = "leh" and so on until we get the final reverse string which is "dlrow olleh"
  # learn the how this happen like  swaping in the value of reverse_string and char in each iteration of the loop
print("Original string:", string)


#Q5 find the nor repeted char in a string
string ="hello world"

char_count ={}
for char in string:
    char_count[char] = char_count.get(char,0) +1 #we are using the get() method to get the value of
    #the key char in the char_count dictionary if the key is not present in the dictionary 
     #it will return 0 and we are adding 1 to the value of the key char in the 
    # char_count dictionary which will count the number of occurrences of each
    # #character in the string which in this case will be
    # #{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
for char, count in char_count.items():
    if count == 1:
        print(f"Character '{char}' is not repeated.") #Character 'h' is not repeated.
        
# we can solve in different way by usinf the count() method or we can also use a set to find the non-repeated characters in a string

#Q6  factorial calculater using loop
number =8

for i in range(1,number):
    number *=i #we are multiplying the current value of number with the current value of i which is from 1 to number-1 so the new value of number will be the factorial of the original number which in this case will be 40320 because 8! = 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 40320
print(f"Factorial of {number//i} is {number}") #Factorial of 8 is 40320 because when we use a for loop to iterate over a range of numbers from 1 to number-1 and we multiply the current value of number with the current value of i which is from 1 to number-1 we will get the factorial of the original number which in this case is 40320 because 8! = 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 40320    


factorial =1

while number >0:
    factorial *=number #we are multiplying the current value of factorial with the current value of number which is from number to 1 so the new value of factorial will be the factorial of the original number which in this case will be 40320 because 8! = 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 40320
    number -=1 #we are decrementing the value of number by 1 in each iteration of the loop until we get to 0 which is when we will stop the loop
print(f"Factorial is {factorial}") #Factorial is 40320 because when we use a while loop to iterate over a range of numbers from number to 1 and we multiply the current value of factorial with the current value of number which is from number to 1 we will get the factorial of the original number which in this case is 40320 because 8! = 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 40320


#Q7 keep asking the user for input until they enter a valid number

valid_number =9

while True: # using for loop ?
    user_input =int(input("Enter  valid number: "))
    if user_input == valid_number:
        print("Your entred a valid number") #Your entred a valid number because when we use a while loop to keep asking the user for input until they enter a valid number and we use an if statement to check if the user input is equal to the valid number we will print a message saying that the user entered a valid number which in this case is true because when the user enters 9 it will print "Your entred a valid number"
        break #we can also use the break statement to exit the loop when the user enters a valid number which in this case is when the user enters 9 we will exit the loop and stop asking for input
    else:
        print("Invalid number, please try again.") #Invalid number, please try again. because when we use a while loop to keep asking the user for input until they enter a valid number and we use an if statement to check if the user input is equal to the valid number we will print a message saying that the user entered a valid number if the user input is equal to the valid number and if the user input is not equal to the valid number we will print a message saying that the user entered an invalid number and ask them to try again which in this case is true because when the user enters a number other than 9 it will print "Invalid number, please try again."


# for file handeling or iterating over a file we can use a for loop to read the file line by line and we can also use a while loop to read the file line by line until we reach the end of the file which is when we will stop the loop

# The 'with' block acts as a Context Manager. 
# It guarantees the file is closed automatically when the loop finishes.
with open("my_data.txt", "r") as file:
    
    for line in file:
        print(line.strip())
        
        
Mylist = [1, 2, 3, 4, 5]
for i in range(len(Mylist)):
    print(Mylist[i]) #1
                    #2
                    #3
                    #4
                    #5 because when we use a for loop to iterate over a range of numbers from 0 to the length of the list-1 and we use the index to access the elements of the list we will print each element of the list which in this case is 1, 2, 3, 4, 5
                    
#iter() -> this help to iterate over a sequence of elements and we can use the next() function
# to get the next element in the sequence which is useful when we want to iterate
# over a file or a large dataset without loading it all into memory at once.

my_iter = iter(Mylist)
my_iter #<list_iterator object at 0x7f8c8c8c8c8c> because when we use the iter() function to create an iterator object from a list we will get a list_iterator object which is an iterator that can be used to iterate over the elements of the list

my_iter.__next__() #1 because when we use the next() function to get the next element in the iterator we will get the first element of the list which is 1
my_iter.__next__() #2 because when we use the next() function again to get the next element in the iterator we will get the second element of the list which is 2

next(my_iter) #3 because when we use the next() function again to get the next element in the iterator we will get the third element of the list which is 3


#dic is also iterable we can use a for loop to iterate over the keys of the dictionary or we can use the items() method to iterate over the key-value pairs of the dictionary
D={"a": 1, "b": 2, "c": 3}

for key in D.Keys():
    print(key) #a
              #b
              #c because when we use a for loop to iterate over the keys of the dictionary we will print each key of the dictionary which in this case is a, b, c
            
I=iter(D) #we can also use the iter() function to create an iterator object from a dictionary which will iterate over the keys of the dictionary by default
I.__next__() #a because when we use the next() function to get the next element in the iterator we will get the first key of the dictionary which is a
I.__next__() #b because when we use the next() function again to get the

