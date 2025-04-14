"""
immutable: cannot be modified
1. int
2. float
3. string
4. tuple
5. frozen set

cannot be updated,
takes new location

"""

a= 4
first_location =id(a)
print(first_location)

a= 8
second_location = id(a)
print(second_location)