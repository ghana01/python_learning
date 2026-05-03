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
    
