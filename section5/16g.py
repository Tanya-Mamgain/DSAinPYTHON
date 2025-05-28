#SHALLOW COPY
student={'name':'Tanya','Semester':8,'Grade':'A','CGPA':9.5}
student_copy=student
print(student_copy)
student['name']='Mamgain'
print(student) #changes
print(student_copy) #copy also changed