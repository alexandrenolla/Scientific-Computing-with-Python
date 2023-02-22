counts = {'chuck': 1, 'fred': 42, 'jan': 100}
print('with a determined loop:')
for key in counts:
    print(key, counts[key])

print('with a list:')
print(list(counts))

print('with the .keys method:')
print(counts.keys())

print('with the .values method:')
print(counts.values())

print('with the .items method:')
print(counts.items())

print('with a determined loop with two iteration variables + .items:')
for aaa,bbb in counts.items():
    print(aaa,bbb)