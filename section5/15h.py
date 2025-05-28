#MATHEMATICAL OPERATIONS (SETS)
set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}


#UNION 
union_set= set1.union(set2)  #union operation is commutative for sets
print('After performing set1 union set2 ',union_set)
union_sett= set2.union(set1)  # set1 U set2 = set2 U set1 => same o/p
print('After performing set2 union set1 ',union_sett)


#INTERSECTION
  #It gives common elements from both the sets, it's commutative
intersection_set= set1.intersection(set2)
print('\nAfter performing intersection=> ', intersection_set)

#INTERSECTION UPDATE
  #we get the intersection of set1 and set2
  #then that intersection value get's updated to set1
set1.intersection_update(set2)
print('\nAfter performing intersection update set1 becomes=> ',set1)