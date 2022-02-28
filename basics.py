# here is a Python comment
a = 3 # integer
b = 7

# Py 2 integers result in integer
print(b//a) # method (use brackets)
print(b%a) # show remainder
print(b**a) # raise to the power
print(b/a) # integers result in a floating point answer

c = 4.0
d = 5.0
c = 'Hi' # replace string with something else
c = 'hello and welcome to Python' # python strings are immutable
print( c+str(d) ) # float is preserved
e = '42'
print( float(e) - d )

# accessing members of a collection
print(c[4:13:2]) # o to l start:stop-before:step
# c[0] = 'H' # nope - strings are immutable
# big numbers
# Python is only restricted by system resources
# g = 10**1000000 # will fauil only due to lack of resourses
# print(g)

# other data types
h = True # or False
# collections: lists and tuples
l = [6, 5.2, 4, True, 'nearly coffee', c, b, a] # a list is a mutable collection of indexed members of any data type
l.append([8,7,6]) # append new members to the list
l[4] = 'soon lunch'
print(l[2:5:2], l.__len__() )
t = (8,7,6,l) # a tuple is an immutable indexed collection of any data types
print(t[3][4])



# quotes
j = "double \nquotes"
k = 'single \tquotes'
l = """tripple \"double quotes\" allow
multiple lines without needing special escape characters"""
m = '''tripple \'single\' quotes'''
# print(j,k,l,m)

# documeting code
def someFn(): # NB indentation is essential....
    ''' this is a docstring
    tripple quotes are often used
    tp document blocks of code
    such as functions, classes etc.
    '''