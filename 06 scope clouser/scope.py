#scope


username= "chai or code"

def test():
    pass

#we majorly concern about the function scope not the conditional scope
#function scope means the variables defined inside a function are only accessible within that function and cannot be accessed outside of it. This is known as local scope. Variables defined outside of any function are in the global scope and can be accessed from anywhere in the code.
#when we create a function it create a new scope for each varible like think like 
# when we create a py file we have a memory and when we create function it 
# create a new memory for that function and when we define a variable inside that function it will be stored in that memory and when we call that function it will access the variable from that memory and when we exit the function that memory will be destroyed and the variable will no longer be accessible
#so the variable defined inside the function is only accessible within that function and cannot be accessed outside



def func():
    username="chai"
    print(username)
print(username)

func()


x=99

def func2(y):
    z=x+y
    return z

func2(100)


def func3():
    global x   # this keyword help us to make refrence to global varible
    
    x=12





func()
print(x)


def f1():   # in this case  we  have clouser  
    x=88
    def f2():
        print(x)
    
    f2()
   
    
f1()
def f1():   # in this case  we  have clouser  
    x=88
    def f2():
        print(x)
    
     
    return f2
   
















