#SET() METHODS SUBSET & SUPERSET egs. (cont.)

set1 = {1, 2}
set2 = {1, 2, 3, 4}

print(set1.issubset(set2))     # True
#set1 is a subset of set2 because all elements of set1 are present in set2.
print(set2.issuperset(set1))   # True 
#set2 is a superset of set1 because it contains all elements of set1.

#NOTE: In this case, set2 is a strict superset of set1. [SET2>SET1]
# A strict superset (or proper superset) means that the set contains all 
# elements of the other set, but it also has additional elements.

#NOTE set1 is a strict subset of set2
#A set A is a strict subset (also called a proper subset) of set B if:
    # Every element of A is also in B (A ⊂ B), and  [B>A]
    # A and B are not equal — meaning B has at least one extra element.

# set1 = {1, 2}
# set2 = {1, 2, 3, 4}
    # All elements of set1 are in set2
    # set2 has extra elements (3, 4) => SET2>SET1
    #So, set1 is a strict subset of set2.


