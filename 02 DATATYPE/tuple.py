


#if we have list then why tuple because tuple is a collection which is ordered and unchangeable. Allows duplicate members. Tuple is faster than list because it is immutable and it takes less memory than list because it is immutable.

my_tuple = (1, 2, 3, 4, 5) #this is a tuple of integers
my_tuple2 = ("apple", "banana", "cherry") #this is a tuple

my_tuple3 = (1, "apple", 3.14, True) #this is a tuple of mixed data types

#we can also have a tuple of tuples which is called a nested tuple
my_tuple4 = (1, 2, (3, 4), 5)
#we can access the elements of a tuple using indexing and slicing
tea_tuple =("Black tea", "Green tea", "Oolong tea", "White tea", "Herbal tea")

print(tea_tuple)
first_tea = tea_tuple[0]  #we can also use negstive indexing
print(first_tea) #Black tea because when we use indexing on a tuple it will return the element at the specified index which in this case is index 0 which is "Black tea"
my_tuple[0]=10 #we cannot change the elements of a tuple using indexing because tuples are immutable and we cannot change the value of an element in a tuple once it is created so this will give an error because we are trying to change the value of the element at index 0 which is 1 to 10 which is not allowed in a tuple because tuples are immutable
tea =("herbal","Matcha","Chai") #we can also create a tuple without using parentheses but it is recommended to use parentheses to create a tuple because it makes the code more readable and it also helps to avoid confusion with other data types like lists and dictionaries which also use square brackets and curly braces respectively to create their own data types so it is better to use parentheses to create a tuple to avoid confusion and make the code more readable
alL_tea = tea + tea_tuple #we can also concatenate two tuples using the + operator which will create a new tuple that contains all the elements of both tuples which in this case is ('herbal', 'Matcha', 'Chai', 'Black tea', 'Green tea', 'Oolong tea', 'White tea', 'Herbal tea') because when we use the + operator to concatenate two tuples it will create a new tuple that contains all the elements of both tuples in the order they are concatenated which in this case is first the elements of the tuple tea and then the elements of the tuple tea_tuple so the new tuple will be ('herbal', 'Matcha', 'Chai', 'Black tea', 'Green tea', 'Oolong tea', 'White tea', 'Herbal tea')
print(alL_tea)

if "Matcha" in tea_tuple:
    print("Matcha is in the tuple") #Matcha is in the tuple because when we use the in operator to check if an element is in a tuple it will return true if the element is in the tuple and false if the element is not in the tuple which in this case is true because "Matcha" is in the tuple tea_tuple
    

tea=("herbal","earl grey","chai") #we can also create a tuple without using parentheses but it is recommended to use parentheses to create a tuple because it makes the code more readable and it also helps to avoid confusion with other data types like lists and dictionaries which also use square brackets and curly braces respectively to create their own data types so it is better to use parentheses to create a tuple to avoid confusion and make the code more readable
print(tea) #('herbal', 'earl grey', 'chai') because when we create a tuple without using parentheses it will still create a tuple but it is recommended to use parentheses to create a tuple because it makes the code more readable and it also helps to avoid confusion with other data types like lists and dictionaries which also use square brackets and curly braces respectively to create their own data types so it is better to use parentheses to create a tuple to avoid confusion and make the code more readable

tea.count()
tea.index("chai") #2 because when we use the index() method on a tuple it will return the index of the first occurrence of the specified value in the tuple which in this case is "chai" and it is at index 2 in the tuple tea so the result will be 2
# we can use tuple to undrwaple the values of a tuple into separate variables
tea1, tea2, tea3 = tea #we are using tuple unpacking to unpack the values of the tuple tea into separate variables tea1, tea2, tea3 so the value of tea1 will be "herbal", the value of tea2 will be "earl grey" and the value of tea3 will be "chai" because when we use tuple unpacking it will assign the values of the tuple to the variables in the order they are defined in the tuple so the first value of the tuple will be assigned to the first variable, the second value of the tuple will be assigned to the second variable and so on so in this case the first value of the tuple which is "herbal" will be assigned to tea1, the second value of the tuple which is "earl grey" will be assigned to tea2 and the third value of the tuple which is "chai" will be assigned to tea3 so the result will be tea1 = "herbal", tea2 = "earl grey", tea3 = "chai"
print(tea1) #herbal because when we use tuple unpacking to unpack the values of a tuple into separate variables it will assign the values of the tuple to the variables in the order they are defined in the tuple so the first value of the tuple which is "herbal" will be assigned to tea1 so the result will be tea1 = "herbal"

type(tea) #<class 'tuple'> because when we use the type() function on a tuple it will return the type of the object which in this case is a tuple so the result will be <class 'tuple'>
