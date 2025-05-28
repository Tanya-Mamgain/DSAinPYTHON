#ITERATING OVER LIST
num = [1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99]
print(num)

#iterating with idx
for index, number in enumerate(num): #The enumerate() function in Python 
                                        #lets you loop through a list (or any iterable) 
                                        # and get both the index and the value at the same time.
    print(index,number) 

    #agr yaha number ke jgh print(index,num) hota then baar baar poori list print hoti(prev. error)