#accessing elements using get()
student={1:'Tanya',2:'Gulshan',3:'bullet'}
print(student.get(1))
print(student.get(3))
print(student.get(5)) #gives op none
#following provides default value
print(student.get(5,"Not Available"))