#BASIC SETS OPERATIONS: adding & removing elements
#adding and removing elements
my_set= set()  #declare krna zaruri hai vrna error aajayega 
my_set.add(7)
print(my_set)

my_set.update([1, 2, 3, 4, 5])   # sets are unordered, so there is no guaranteed order of elements.
#kyuki hume bht sari values ek bari me add krna tha so we used update().As add() allows only one 
# value at a time to be added
print(my_set)  # sets are unordered so koi specific sequence nhi aayega (7 ke phle ya baad me)
my_set.remove(3)  #remove()
print('After removing 3=> ', my_set)   
