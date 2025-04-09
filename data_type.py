# int
x = 29
#float
y= 30.35

# complex
z= 10+10j

#string

name= "Lamia Sultana"

"""
list
square bracket
mutable
"""

foods= ["apple", 2 , 2.50 , "navle"]
print(foods[2])

#tuple 1.first bracket 2.immutable

cities = ("japan", 3.98, "bangladesh")
print(cities[1])

#range

numbers= range(1,10)
print(*numbers)

#inside range (start number,before last number)

number1 = range(0,10,2)
print(*number1)

#inside range(start num, before last num, how many num)


#dic

person={
    'name': 'Lamia Sultana',
    'age': 25,
    'isBangladeshi':True,

}
print(person['name'])

#set unique value,--mutable
# not duplicate value, second bracket{}, no index, unordered

unique_num={1,2,3,4}

#frozen set--immutable

unique_number=frozenset([1,2,3,4])
print(unique_number)

#check data_type

check = type(person)
print(check)











