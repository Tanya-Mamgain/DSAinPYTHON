#BASIC SETS OPERATIONS: diff. b/w remove() and discard()

#what if try to remove an elememt that is not present in the set??
my_set={1,2,3,4,5,6}
# my_set.remove(10)   =>10 SET me hai hi nhi...to remove() error dega
# print(my_set)       => no output as error occurs for this purpose we use discard()
my_set.discard(10)
print(my_set)