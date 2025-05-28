#SET METHODS
set1={1,2,3}
set2={3,4,5}

#IS SUBSET()
print(set1.issubset(set2)) 
#means all the elements that is available in set1 is also available in set2?
#result FALSE as 1,2 is not available in set2

#IS SUPERSET
print(set1.issuperset(set2)) #result=FALSE
#  checks if all elements of set2 are also in set1.