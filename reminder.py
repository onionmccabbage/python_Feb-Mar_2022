# using 'in'
from re import A


t = ('posts', 'albums', 'todos', 'photos')
exists = 'users' in t # False since it is not in the tuple
print(exists)

# iterating over a dict
d = {'name':'Grace Hopper', 'admin':False, 'address':[42, 'Primrose Av', 'Becknall']}
for k, v in d.items():
    if(type(v)==list):
        for item in d[k]:
            print('\t{}'.format(item))
    else:
        print('key {} has value {}'.format(k,v))

# by reference and by value
e = d # e and d now reference the same data structure
a = 42
b = a # b is given the value of a - passed by value. b has no further interest in a
a = 24
print(b)
# what happens when we mutate d - does e also mutate?
d['admin'] = True
print(e['admin']) # this is passed by reference not by value) so when d mutates, so does e