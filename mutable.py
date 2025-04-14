"""
mutable data..
sets, lists , dict
-can be modified
-does not create new location
"""

l = [1, 3,7,6]
first_local = id(l)
print(first_local)

l[2] = 9

new_local = id(l)
print(new_local)
