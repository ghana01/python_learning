from one import chai


chai("ginger tea")


h1=[1,2,3,4,5]
h2=h1[:]   #copy of h1 list we are  using the slice operator to copy the list h1 and assign it to h2
#using slicing we can also copy the list and create a new list h2 which is independent of h1 and also we do indexing and slicing on h2 list it will not affect the h1 list because they are two different lists in memory
print(h2)  


n=[1,2,3]
m=n

m==n  #true because both m and n are pointing to the same list in memory but in == we just compare the value of it
m is n  #true because both m and n are pointing to the same list in memory

n=[1,2,3]
m=n
m==n  #true because both m and n are pointing to the same list in memory

m=[1,2,3]

m==n  #true because both m and n have the same elements in the list
m is n  #false because m and n are pointing to different lists in memory