
#how  loop work behing in the  python

iteration tool -> for,comprehensive 
 iterable object -> list,tuple,string,dict,set,file



#when we run a loop in python it creates an iterator object and then it calls the next() function on that iterator object to get the next value in the sequence and it continues to call the next() function until it reaches the end of the sequence and then it raises a StopIteration exception to signal that there are no more items to iterate over.


#file object is also an iterable object and when we run a loop on a file object it creates an iterator object and then it calls the next() function on that iterator object to get the next line in the file and it continues to call the next() function until it reaches the end of the file and then it raises a StopIteration exception to signal that there are no more lines to iterate over.

f=open("loop.py")
f.readline() #it will read the first line of the file and return
'print("hello world")\n'
f.readline()

'print(username)'
f.readline() #it will read the second line of the file and return
