#How do we access nested dictionaries ??
student ={
    'student 1:': {'name':'Tanya' , 'roll':1 },
    'student 2:':{'name':'Gulshan' , 'roll':2},
    'student 3:': {'name':'Ravi', 'roll':3}
}
#suppose we wanna access roll of gulshan ?
print(student['student 2:'] ['name'])  # KEY NAME = "student 2:" 
print(student['student 2:'] ['roll'])  #access roll 