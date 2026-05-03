#dictinary

#creating a dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"} #we can also use dict keyword to create a dictionary
my_dict2 = dict(name="John", age=30, city="New York") #both my_dict and my_dict2 are the same dictionary because they have the same keys and values
print(my_dict)
#accessing the values of a dictionary using the keys
name = my_dict["name"]  = "RohanZ" #we are trying to access the value of the key "name" which is "John" and we are trying to change the value of the key "name" to "RohanZ" so the new value of the key "name" will be "RohanZ"
age = my_dict["age"]
city = my_dict["city"]
print(name, age, city)

#we can also use the get() method to access the values of a dictionary using the keys
name = my_dict.get("name")
age = my_dict.get("age")

print(name, age)
#we can also use the get() method to access the values of a dictionary using the keys and we can also specify a default value to return if the key is not found in the dictionary
country = my_dict.get("country", "USA") #we are trying to access the value of the key "country" which is not present in the dictionary my_dict so it will return the default value "USA"
print(country) #USA because when we use the get() method to access the value of a key that is not present in the dictionary it will return the default value that we have specified which in this case is "USA"

for key in my_dict:
    print(key, my_dict[key])

for key, value in my_dict.items():# we need items() method to get the key-value pairs of the dictionary
    print(key, value) #this will give an error because when we use a for loop to iterate over a dictionary it will return the keys of the dictionary and not the values so we need to use the items() method to get the key-value pairs of the dictionary

if "name" in my_dict:
    print("name is in the dictionary") #name is in the dictionary because when we use the in operator to check if a key is in a dictionary it will return true if the key is in the dictionary and false if the key is not in the dictionary which in this case is true because "name" is in the dictionary my_dict 

print(my_dict.__len__()) #3 because when we use the __len__() method on a dictionary it will return the number of key-value pairs in the dictionary which in this case is 3 key-value pairs in the dictionary my_dict


my_dict.pop("age") #we can also remove a key-value pair from a dictionary using the pop() method with the key of the key-value pair we want to remove which in this case is "age" so the new dictionary will be {"name": "RohanZ", "city": "New York"}



my_dict_copy = my_dict.copy() #we can also create a copy of a dictionary using the copy() method which will create a new dictionary that is a copy of the original dictionary my_dict so the new dictionary my_dict_copy will be {"name": "RohanZ", "city": "New York"}


{{},{},{}}

tea_shop ={
    "name": "Tea Time",
    "location": "New York",
    "menu": {
        "tea": ["Black tea", "Green tea", "Oolong tea", "White tea", "Herbal tea"],
        "snacks": ["Samosa", "Kachori", "Vada pav"]
    },
    "ratings": [4.5, 4.0, 5.0, 3.5, 4.0]
    
}

squared_nums ={x: x**2 for x in range(10)} #we can also use dictionary comprehension to create a new dictionary by applying an expression to each element of an iterable whi

keys =["masala", "ginger", "lemon"]
default_value = "tea"
tea_dict =dict.fromkeys(keys,default_value) #we can also use the fromkeys() method to create a new dictionary with the specified keys and a default value for all the keys which in this case is "tea" so the new dictionary tea_dict will be {"masala": "tea", "ginger": "tea", "lemon": "tea"}
print(tea_dict)
tea_dict =dict.fromkeys(keys,keys) #we can also use the fromkeys() method to create a new dictionary with the specified keys and a default value for all the keys which in this case is the list of keys itself so the new dictionary tea_dict will be {"masala": ["masala", "ginger", "lemon"], "ginger": ["masala", "ginger", "lemon"], "lemon": ["masala", "ginger", "lemon"]} because when we use the fromkeys() method to create a new dictionary with a default value that is a mutable object like a list it will create a new dictionary with the same mutable object as the default value for all the keys which in this case is the list of keys itself so all the keys will have the same list as their default value which is ["masala", "ginger", "lemon"]
print(tea_dict)


