## Sets
print('---------')

a = set()
a.add(1)
a.add(3)
a.add(3)
print(a)

print('---------')

a = list(a)
print(a)

print('---------')

## Lists 

a = ["a", "m", "z"]
print(a[-1])

print('----------')

print(a)
print(a.pop())
print(a)

print('----------')

a = ["hello", "my", "name", "is", "X"]
print(a[:2]) 

'''
a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array
'''

print('-------')
a = ["a", "b", "c", "d", "e"]
print(a[2:3])

print('-------')
a = ["b", "c", "a"]
print(sorted(a))

print('-------')

print(list(range(5)))

print('---------') 

print(list(range(1, 5)))

print('---------')

print(list(range(5, 0, -1)))

print('---------')

print(list(range(1, 5, -1)))

print('---------')
