#Dictionary methods
student={'name':'Tanya','Semester':8,'Grade':'A','CGPA':9.5}
keys=student.keys()#gets all the keys 
print(keys)
values=student.values()
print(values) #gets all values
items=student.items()
print(items)# gets all key value pairs 

# Why Use .items() Instead of Just print(student)?
# print(student) will print the entire dictionary as a whole:
# {'name': 'Tanya', 'Semester': 8, 'Grade': 'A', 'CGPA': 9.5}
# rint(student.items()) returns a special view object that contains all the (key, value) pairs:
# dict_items([('name', 'Tanya'), ('Semester', 8), ('Grade', 'A'), ('CGPA', 9.5)])
# You can just use print(student), but .items() is used when you want more control over
# the (key, value) pairs—especially useful for loops, transformations, or when building
# logic from dictionary data.




