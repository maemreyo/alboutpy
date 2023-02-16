# Concatenate list
list_a = ['foo', 'bar']
list_b = ['foo-foo', 'barbar']
result = list_a + list_b

# Check 'in'
this_list = ['foo', 'bar', 'foobar', 'barfoo', 'baz']
if 'foo' in this_list:
    print('YES')

# sorted()
sorted(this_list)
sorted(this_list, reverse=True)

# sort
this_list.sort()

# for
for item in this_list:
    print(item)

# append
this_list.append('foo-foo-bar-baz')

# index
this_list.index('foo')

# copy
list_copy = this_list.copy()
list_copy.append('foo-baz')

# remove
this_list.remove('foo')

# pop
this_list.pop()

# del
del this_list
