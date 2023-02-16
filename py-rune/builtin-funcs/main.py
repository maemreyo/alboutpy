# Useful builtin functions

# zip()
words = ['as', 'youtube', 'wikipedia', 'google']
counts = [1, 2, 3, 4]

for word, count in zip(words, counts):
    print(word, count)

# type()
type(words)
type(1)
type('youtube')

# sum()
sum(counts)

# set()
nums = [1, 1, 2, 2, 3, 3, 4, 5, 6, 6, 7, 7, 8, 8, 10]
set(nums)

# list()
list(set(nums))

# round()
round(1.234534321234, 2)

# min(), max()
min(nums)
max(nums)


# map()
def map_num(x):
    return 'x' * x


list(map(map_num, [1, 2, 3, 4, 5]))

# isinstance()
items = ['foo', 3, 'bar', 4, 'baz']

[item for item in items if isinstance(item, str)]

# any(), all()
bools = [True, False, False]
any(bools)
all(bools)
