#Nested list comprehension
lst1= [1,2,3,4]
lst2= ['a','b','c','d']

#performs all possible pairings between lst1 and lst2 
pair = [(i,j) for i in lst1 for j in lst2]
print(pair)