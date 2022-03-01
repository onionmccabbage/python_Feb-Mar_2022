# typical conventions found in languages

ALL_CAPS = ('used', 'for', 'constants')

class InitialCaps(): # by convention indicates a class (Python doesn't care)
    pass # we can name-mangle using _item (i.e. leading underscore)

lower_snake_case = 'identifiers, functions etc'

camelCase = 'also identifiers'

something_d = {'d for dict l for list t for tuple etc'}

# there are some rules
print = 'oops' # this overrides the built in print!!! - avoid doing this with keywords
rules = 'start with a letter or underscore. Can include digits in names'
__internal__ = 'tend to belong to python internal things'