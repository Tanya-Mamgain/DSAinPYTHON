#List comprehension with function calls
words=['hello','world','list','comprehension']
lengths = [ len(words) for words in words]
print(lengths)