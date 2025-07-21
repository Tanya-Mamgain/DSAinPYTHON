#ITERATING OVER NESTED DICTIONARIES 
student ={
    'student 1:': {'name':'Tanya' , 'roll':1 },
    'student 2:':{'name':'Gulshan' , 'roll':2},
    'student 3:': {'name':'Ravi', 'roll':3}
}

for student_id, details in student.items():
    print(f"\n{student_id}:")  # student1, student2, etc.
    for key, value in details.items():
        print(f"  {key}: {value}")

