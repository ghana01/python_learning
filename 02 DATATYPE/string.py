#we have string in '' or " " or ''' ''' or """ """   in python

'chai'
chai='masala chai'
print(chai) #masala chai because we have assigned the value 'masala chai' to the variable chai and when we print the variable chai it will print the value of the variable which is 'masala chai'

firsr_char =chai[0]
print(firsr_char) #m because when we use indexing on a string it will return the character at the specified index and in this case we are using index 0 which is the first character of the string 'masala chai' which is 'm'

#now we want to remove the msala fron the string 'masala chai' and we want to get only the 'chai' part of the string we can use slicing to get the desired result

slice_chai =chai[6:10]
print(slice_chai) #chai because we are using slicing to get the substring from index 6 to index 10 (exclusive) of the string 'masala chai' which is 'chai'
#we can also use negative indexing to get the desired result
slice_chai =chai[-4:]
print(slice_chai) #chai because we are using negative indexing to get the substring from index -4 to the end of the string 'masala chai' which is 'chai'

num_List= "0123456789"

nums_list[3:]

num_list[:5]

num_list[0:7:2] #02468 because we are using slicing to get the substring from index 0 to index 7 (exclusive) of the string '0123456789' with a step of 2 which means we will get every second character starting from index 0 which is '0' then '2' then '4' then '6' and finally '8'

"ginger chai"

#string methods
"ginger chai".upper() #GINGER CHAI because when we use the upper() method on a string it will return a new string with all the characters in uppercase
"GINGER CHAI".lower() #ginger chai because when we use the lower() method on a string it will return a new string with all the characters in lowercase
"ginger chai".title() #Ginger Chai because when we use the title()

chai="  ginger chai"
chai.strip() #ginger chai because when we use the strip() method on a string it will return a new string with all the leading and trailing whitespace removed

print(chai.replace('ginger',"kemon"))

chai ="lemon ,ginger,masala ,mint"

#convert this into list
chai_list =chai.split(", ") #['lemon', 'ginger', 'masala', 'mint'] because when we use the split() method on a string it will return a list of substrings that are separated by the specified separator which in this case is ", "


print(chai.find("ginger")) #8 because when we use the find() method on a string it will return the index of the first occurrence of the specified substring which in this case is "ginger" and it is found at index 8 in the string "lemon ,ginger,masala ,mint"

chai_type ="masalaa"
quantity=5

order ="i ordered {} cups of {} "  #{} is a placeholder for the value that we want to insert in the string
print(order.format(quantity,chai_type)) #i ordered 5 cups of masalaa because when we use the format() method on a string it will replace the placeholders {} with the values that we pass as arguments to the format() method in the order they are passed


#list to string
chai_list =['lemon', 'ginger', 'masala', 'mint']
chai_string = ", ".join(chai_list) #lemon, ginger, masala, mint because when we use the join() method on a string it will return a new string that is the concatenation of the strings in the list with the specified separator which in this case is ", "


chai ="lemon  chai"
print(len(chai)) #11 because when we use the len() function on a string it will return the number of characters in the string including whitespace which in this case is 11 characters in the string "lemon  chai"

for letter in chai:
    print(letter)

chai="he said,"Masala chai is best"" #SyntaxError because when we use double quotes to define a string and we want to include double quotes inside the string we need to escape the double quotes using a backslash \ or we can use single quotes to define the string instead of double quotes

chai='he said,\"Masala chai is best\ "' #he said,"Masala chai is best" because when we use single quotes to define a string we can include double quotes inside the string without any issues



print(chai)
