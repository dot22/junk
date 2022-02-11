def mykey(adict): return adict['name']
x = [{'name': 'Homer', 'age': 39}, {'name': 'Bart', 'age':10}]
print(sorted(x, key=mykey))
print(x)