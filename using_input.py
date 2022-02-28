# we can ask the user to enter values
def main(): # here we define a function (nb functions are objects)
    a = input('please enter a number ') # ALWAYS takes a string
    # we can validate
    if(a.isalpha()):
        print('{} is not numeric'.format(a))
    elif(a.isdecimal):
        print('it is a decimal value')
        # now cast it as an actual number
        n = int(float(a)) # always safest to make it a float then an int just in case
        print('{} squared is {}'.format(n, n*n)) # the curly-braces are positional members
    else:
        print('The value {} is a number'.format(a))

# when indentation stops, that is the end of the code block
# NB we try to avoid pollution of the global namespace
print(__name__) # Python ALWAYS provides a value for __name__

# we commonly do the following:
if __name__ == '__main__': # will NOT run if this module is imported elsewhere
    main() # must come AFTER we declare 'main'

