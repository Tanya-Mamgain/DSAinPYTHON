#NOT STRICT SUBSET & NOT STRICT SUPERSET
setA = {1, 2, 3}
setB = {1, 2, 3}

print(setA.issubset(setB))   # True ✅ (because A == B)
print(setA.issuperset(setB)) # True ✅ (because A == B)

print(setA < setB)  # False ❌ (not a strict subset)
print(setA > setB)  # False ❌ (not a strict superset)
