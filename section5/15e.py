# POP() => removing an elemnt from SET() using POP() 
my_set={1,2,3,4,5}
print('Before popping set is=> ',my_set)
removed_emelent = my_set.pop()
print('Item removed is=> ',removed_emelent)
print('After popping set now becomes=> ', my_set)

# Key points about set.pop():
    # It removes one element from the set.
    # Since sets are unordered, you can’t predict which element will be removed.
    # If the set is empty, pop() will raise a KeyError.