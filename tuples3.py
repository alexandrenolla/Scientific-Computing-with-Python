# The top 3 most common words

fhand = open('text')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:3]:
    print(key, val)

# List Comprehension
c = {'a':10, 'b':1, 'c':22}
print(sorted([(v, k) for k, v in c.items()]))