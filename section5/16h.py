#Iterating over dictionaries
#you can use loops to iterate over dictionaries
student = {'name':'Tanya','Batch of:':2025, 'Grade':'A', 'roll':111}

#iterating over keys
for keys in student.keys():
    print(keys)

#iterate over values 
for val in student.values():
 print(val)

print('\n')  #to give space for neatness 
for key,value in student.items():
   print(f"{key}:{value}") 