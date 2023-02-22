# Tuples and Assignment
x, y = (4, 'fred')
print(y)
(a, b) = (99, 98)
print(a)

print('----------------')

# Tuples and Dictionaries
d = dict()
d['csev'] = 2
d['cwen'] = 4

for (k,v) in d.items():
    print(k,v)

tups = d.items()
print(tups)

print('------------------')

# Sorting Lists of Tuples
d = {'a':10, 'b':1, 'c':22}
print(d.items())
for k,v in sorted(d.items()):
    print(k,v)