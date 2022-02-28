# a dictionary is an unordered collection of mutable name:value pairs
d1 = {"name":"Timnit", 'age':42,  'member':True}
d2 = {"name":"Grace",  'age':82,  'member':True}
d3 = {"name":"Ada",    'age':142, 'member':False}

members_d = {'a':d1, 'b':d2, 'c':d3, 'li':[5,4,3]}

d1['age'] = 43
d1['wibble'] = 'wobble' # new members MUST use square-bracket notation
d1['wibble'] = False # mutating member must also use bracket notation for dict

print(d1.keys(), d1.values())

# alternative creational techniques
w = dict() # an empty dict
x = list( (4,3,2) ) # make a list out of a tuple
y = tuple(x) # make a tuple from a list

# what is this...
z = (7,) # I'm after a single-member tuple

# there is also a data-type known as a 'set' - like a dict but no keys
s = {7,6,5,4,7,3,2,5} # only unique members survive
s.add(0)
print(s)
