#Week 4B 20.9.2019

Type "help", "copyright", "credits" or "license" for more information.
>>> fruits = ['orange', 'apple', 'pear', 'banana','coconut']
>>> fruits.reverse()
>>> fruits

['coconut', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits

['coconut', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.remove('apple')
>>> fruits

['coconut', 'banana', 'pear', 'orange', 'grape']
>>> fruits
['coconut', 'banana', 'pear', 'orange', 'grape']
>>> fruits.insert(1,'cucumber')
>>> fruits
['coconut', 'cucumber', 'banana', 'pear', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['banana', 'coconut', 'cucumber', 'grape', 'orange', 'pear']
>>> fruits.pop()
'pear'
>>> fruits
['banana', 'coconut', 'cucumber', 'grape', 'orange']
>>> fruits.pop(2)
'cucumber'
>>> fruits
['banana', 'coconut', 'grape', 'orange']


from math import pi
[str(round(pi, i)) for i in range(1, 6)]


[[row[i] for row in matrix] for i in range(4)]


transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])