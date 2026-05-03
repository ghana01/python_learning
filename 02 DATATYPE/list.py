

#LIST 

#List is a collection which is ordered and changeable. Allows duplicate members.

my_list = [1, 2, 3, 4, 5] #this is a list of integers
my_list2 = ["apple", "banana", "cherry"] #this is a list of strings
my_list3 = [1, "apple", 3.14, True] #this is a list of mixed data types

#we can also have a list of lists which is called a nested list
my_list4 = [1, 2, [3, 4], 5]

#we can access the elements of a list using indexing and slicing

tea_list =["Black tea", "Green tea", "Oolong tea", "White tea", "Herbal tea"]

print(tea_list)
first_tea = tea_list[0]  #we can also use negstive indexing to access the elements of a list
print(first_tea) #Black tea because when we use indexing on a list it will return

print(tea_list[:2]) #['Black tea', 'Green tea'] because when we use slicing on a list it will return a new list that contains the elements from the specified start index to the specified end index (exclusive) which in this case is from index 0 to index 2 (exclusive) of the list tea_list which is ['Black tea', 'Green tea']
print(tea_list[2:]) #['Oolong tea', 'White tea', 'Herbal tea'] because when we use slicing on a list it will return a new list that contains the elements from the specified start index to the end of the list which in this case is from index 2 to the end of the list tea_list which is ['Oolong tea', 'White tea', 'Herbal tea']
print(tea_list[1:4]) #['Green tea', 'Oolong tea',
 #   'White tea'] because when we use slicing on a list it will return a new list that contains the elements from the specified start index to the specified end index (exclusive) which in this case is from index 1 to index 4 (exclusive) of the list tea_list which is ['Green tea', 'Oolong tea', 'White tea']


tea_list[2]="Earl Grey tea" #we can also change the elements of a list using indexing
print(tea_list) #['Black tea', 'Green tea', 'Earl Grey tea', 'White tea', 'Herbal tea'] because when we use indexing on a list to change the value of an element it will change the value of the element at the specified index which in this case is index 2 which is "Oolong tea" and we are changing it to "Earl Grey tea" so the new list will be ['Black tea', 'Green tea', 'Earl Grey tea', 'White tea', 'Herbal tea']


#slicing/dicing a list is also mutable because we can change the elements of a list using slicing
tea_list[1:3] = ["Matcha tea", "Chai tea"] #
#we are using slicing to change the value of the elements from index 1 to index 3 (exclusive) of the list tea_list which is ['Green tea', 'Earl Grey tea'] and we are changing it to ['Matcha tea', 'Chai tea'] so the new list will be ['Black tea', 'Matcha tea', 'Chai tea', 'White tea', 'Herbal tea']       


#can we replace using the slicing with a different number of elements in the list
tea_list[1:3] = ["Matcha tea"] #yes we can replace using the slicing with a different number of elements in the list because when we use slicing to change the value of the elements from index 1 to index 3 (exclusive) of the list tea_list which is ['Matcha tea', 'Chai tea'] and we are changing it to ['Matcha tea'] so the new list will be ['Black tea', 'Matcha tea', 'White tea', 'Herbal tea']

print(tea_list[1:1]) #[] because when we use slicing on a list with the same start and end index it will return an empty list which in this case is from index 1 to index 1 (exclusive) of the list tea_list which is []


for tea in tea_list:
    print(tea) #Black tea
              #Matcha tea
              #White tea
              #Herbal tea because when we use a for loop to iterate over a list it will return each element of the list one by one which in this case is 'Black tea', 'Matcha tea', 'White tea', 'Herbal tea'


for tea in teaL_list:
    print(tea,end="-") #`Black tea-Matcha tea-White tea-Herbal tea- because when we use a for loop to iterate over a list and we use the end parameter in the print function it will print each element of the list one by one with the specified end character which in this case is "-" so the output will be 'Black tea-Matcha tea-White tea-Herbal tea-'
    
if "Matcha tea" in tea_list:
    print("Matcha tea is in the list") #Matcha tea is in the list because when we use the in operator to check if an element is in a list it will return true if the element is in the list and false if the element is not in the list which in this case is true because "Matcha tea" is in the list tea_list
    
tea_list.append("Lemon tea") #we can also add elements to a list using the append() method

tea_list.pop() #we can also remove the last element of a list using the pop() method
tea_list.pop(1) #we can also remove an element from a list using the pop() method with the index of the element we want to remove which in this case is index 1 which is "Matcha tea" so the new list will be ['Black tea', 'White tea', 'Herbal tea']  
tea_list.remove("White tea") #we can also remove an element from a list using the remove() method with the value of the element we want to remove which in this case is "White tea" so the new list will be ['Black tea', 'Herbal tea']
#in remove methods it doe not return the removed element it just removes the element from the list and it does not return anything so if we try to print the result of the remove() method it will return None because it does not return anything
#inserting an element in a list at a specific index using the insert() method
tea_list.insert(1,"Green tea") #we can also insert an element in a list at a specific index using the insert() method with the index of the element we want to insert and the value of the element we want to insert which in this case is index 1 which is "Green tea" so the new list will be ['Black tea', 'Green tea', 'Herbal tea']

squared_nums =[x**2 for x in range(10)] #we can also use list comprehension to create a new list by applying an expression to each element of an iterable which in this case is the range of numbers from 1 to 10 and we are applying the expression x**2 to each element of the range so the new list will be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

squared_nums

cubed_nums =[x**3 for x in range(10)] #we can also use list comprehension to create a new list by applying an expression to each element of an iterable which in this case is the range of numbers from 1 to 10 and we are applying the expression x**3 to each element of the range so the new list will be [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]