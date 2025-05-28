#MATHEMATICAL OPERATIONS (SETS cont.)
set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}

#DIFFERENCE
   #NOTE set difference is not commutative
print('Set1 diff. Set2=> ',set1.difference(set2))  #means: elements in set1 but NOT in set2
print('Set2 diff. Set1=> ',set2.difference(set1))  #means: elements in set2 but NOT in set1

#DIFFERENCE_UPDATE
  #NOTE .difference_update() method works similarly to .difference(),
  #      but it modifies the original set in place instead of returning a new one.
set1.difference_update(set2)
print('\nAfter performing difference_update()=> ',set1) #set1 modify hojayega & diff stored

#SYMETRIC DIFFERENCE =>both the unique elements from both the sets are combined
set1={1,2,3,4,5,6} #set1 wapas phle jaisa krdia kyuki difference_update se change hogya tha
sym_diff=set1.symmetric_difference(set2)  #common elements are removed
print('\nSymmetric difference=> ',sym_diff) #o/p me 4,5,6 nhi aayega cause it's common

