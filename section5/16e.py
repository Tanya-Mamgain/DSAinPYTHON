#Modifying dictionary elements 
#dictionaries are mutable so you can add,
# update or delete elements
car={'model':'eco-sport','company':'Ford',
     'ID':2222,'state':'delhi'}
car["state"] = "Harayana" #updated val for a key
car['country']='India' #added new key
print('After changes\n',car)
print('\n\nDeleting key')
del car['model'] #deleted existing key
print(car)