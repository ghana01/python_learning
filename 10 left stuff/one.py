x =('Masala','lemon','salt')

y=enumerate(x)  # this function is used to get the index of the element in the list 
#and the element itself as a tuple    

print(list(y))   # this will print the list of tuples with index and element
#[(0, 'Masala'), (1, 'lemon'), (2, 'salt')]



file =open('test.py')  # this will open the file in read mode by default
print(file.read())  # this will read the content of the file and print it
file.close()  # this will close the file after reading it


# we can aslo give the mode to the file like in ehich mode we want to open the file like
# 'r' for read, 'w' for write, 'a' for append etc.
file = open('test.py', 'r')  # 'r' for read mode  if the file is not preset
#it will make a new file with the name test.py

file=open('youtube.txt'),'w'  # this will open the file in write mode if the file is not present it will create a new file with the name youtube.txt
file.write('This is a youtube channel')  # this will write the string in the file
file.close()  # this will close the file after writing in it


# try catch error handeling in python

try:
    file = open('test.py', 'r')  # this will open the file in read mode
    print(file.read())  # this will read the content of the file and print it
except FileNotFoundError:  # this will catch the error if the file is not found
    print('File not found')  # this will print the message if the file is not found
finally:
    try:
        file.close()  # this will close the file if it is opened
    except NameError:  # this will catch the error if the file is not opened
        print('File is not opened')  # this will print the message if the file is not opened
        
        
# but now day in python we  have better way to handel the  file usi withe statement which will automatically close the file after the block of code is executed

with open('test.py', 'r') as file:  # this will open the file in read mode and assign it to the variable file
    print(file.read())  # this will read the content of the file and print it
    

