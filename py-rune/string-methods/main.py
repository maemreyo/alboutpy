# String Useful Methods

# replace()
sen = 'this is my home'
sen.replace(' ', '_')

# split()
sen.split()

# join()
sen = 'this is my company'
my_sen = sen.split()
'_'.join(my_sen)

# in
sen = 'this is my company'

if 'is' in sen:
    print('YES')

# strip()
sen = '           this is my company              '
sen.strip()

# isdigit()
sen = '313'
sen.isdigit()

sen = '313a'
sen.isdigit()

# concatenate strings
sen1 = 'Trung'
sen2 = 'Thanh'

sen1 + sen2
' '.join((sen1, sen2))

# formatted strings
var = 25
sen = "Hello"

f'Okay {var} {sen}'

# startswith endswith
url = 'https://foo.com/'

url.startswith('https')
url.endswith('/')

# count()
url.count('foo')

# splitlines
sen = '''
Okay
Let's
go
'''

sen.splitlines()
