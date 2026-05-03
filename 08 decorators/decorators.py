
#Timing Function Exection 

#Q1 write a decorator function that measures the time a functon takes to execute
import time
def timera(func):
    def wrapper(*args,**kwargs):
        start_time = time.time() #we are using the time() function from the time module to get the current time in seconds since the epoch
        result = func(*args,**kwargs) #we are calling the original function and passing the arguments to it and storing the result in a variable called result
        end_time = time.time() #we are using the time() function again to get the current time after the function has executed
        execution_time = end_time - start_time #we are calculating the execution time by subtracting the start time from the end time
        print(f"{func.__name__} run in  {execution_time} seconds") #we are printing the execution time in seconds
        return result #we are returning the result of the original function
        
    return wrapper #we are returning the wrapper function which is the decorated version of the original function

@timera #we are using the @ symbol to apply the decorator to the function which is the same as writing exaample_function = timera(exaample_function)
def example_function(n):
    time.sleep(n) #we are using the sleep() function from the time module to pause the execution of the function for n seconds which is the argument passed to the function

example_function(2) #Execution time: 2.002345561981201 seconds because when we call the example_function with an argument of 2 it will pause the execution of the function for 2 seconds and then it will print the execution time which is approximately 2 seconds





#Q2  create a decorater to print the function name and the vlues of its argument every time the function is called

def print_args(func):
    def wrapper(*args,**kwargs):
        #args_values = ", ".join(str(arg) for arg in args) #we are using a generator expression to iterate over the args and convert each argument to a string and then we are joining the string representations of the arguments with a comma and a space in between
        #kwargs_values = ", ".join(f"{key}={value}" for key, value in kwargs.items()) #we are using a generator expression to iterate over the items in the kwargs dictionary and convert each key-value pair to a string in the format key=value and then we are joining the string representations of the keyword arguments with a comma and a space in between
        print(f"{func.__name__} called with  arguments: {args} and {kwargs}") #we are printing the function name and the values of its arguments which is the args and kwargs
        result = func(*args,**kwargs) #we are calling the original function and passing the arguments to it and storing the result in a variable called result
        return result #we are returning the result of the original function
    return wrapper #we are returning the wrapper function which is the decorated version of the original function

@print_args #we are using the @ symbol to apply the decorator to the function which is the same as writing add = print_args(add)
def add(a,b):
    return a+b #we are returning the sum of a and b

add(3,5) #add called with the arguments: (3, 5) and {} because when we call the add function with the arguments 3 and 5 it will print the function name and the values of its arguments which is (3, 5) and {} because we are not passing any keyword arguments to the function and then it will return the sum of 3 and 5 which is 8
@print_args
def multiply(a,b):
    return a*b #we are returning the product of a and b

multiply(4,6) #24 because when we call the multiply function with the arguments 4 and 6 it will return the product of 4 and 6 which is 24


#output
#example_function run in  2.0006790161132812 seconds
#add called with  arguments: (3, 5) and {}
#multiply called with  arguments: (4, 6) and {}





#Q3 implement a decorator that caches the return value of a function ,so that when its called with the same arguments the cached value is returned instead of re-execution the function
def cache(func):
    cached_results = {} #we are creating an empty dictionary to store the cached results of the function
    def wrapper(*args):
        key = args #we are using the args as the key for the cache dictionary
        if key in cached_results: #we are checking if the key is already in the cache dictionary
            print("Returning cached result") #if the key is in the cache dictionary we will print a message indicating that we are returning the cached result
            return cached_results[key] #we will return the cached result from the cache dictionary
        else:
            result = func(*args) #if the key is not in the cache dictionary we will call the original function and pass the arguments to it and store the result in a variable called result
            cached_results[key] = result #we will store the result in the cache dictionary with the key as the key and the result as the value
            return result #we will return the result of the original function
    return wrapper #we will return the wrapper function which is the decorated version of the original function

@cache #we are using the @ symbol to apply the decorator to the function which is the same as writing fibonacci = cache(fibonacci)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2) #we are using recursion to calculate the nth Fibonacci number which is the sum of the (n-1)th and (n-2)th Fibonacci numbers

print(fibonacci(10)) #55 because when we call the fibonacci function with an argument of 10 it will calculate the 10th Fibonacci number which is 55 and it will cache the results of the previous Fibonacci numbers so that when we call the function with the same arguments it will return the cached result instead of re-executing the function