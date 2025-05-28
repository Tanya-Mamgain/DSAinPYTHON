fruits=["apple",'orange','strawberry','kiwi','cranberry']
for i in fruits:
    print(i , end=' ')

print('\n')
print(fruits[1:])
print('\n')
print(fruits[2:3])
print('\n')

fruits[2:] = "watermelon"
print(fruits)