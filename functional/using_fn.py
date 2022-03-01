import doctest # this is a library provided by the standard Python instalation

def cube(x): # these are positional arguments
    '''
    This function takes on numeric arguments and returns the cube of that value
    >>> cube(3)
    27
    >>> cube(-3)
    -27
    >>> cube(-7)
    -343
    '''
    return x**3

def pythag(x=3, y=4): # these are keyword arguments (with default values)
    '''
    >>> pythag(3, 4)
    5.0
    >>> pythag()
    5.0
    '''
    return (x*x + y*y)**0.5

# reading the set of arguments
def myArgs( *args ): # the asterisk gathers all the positional arguments into a tuple
    if len(args) == 0:
        # we have the no-args version of the fn
        print('called with no positional arguments')
    elif len(args) == 1:
        print('the single positional argument is {}'.format(args[0]))
    else:
        for arg in args:
            print('positional argument {}'.format(arg))
    print(args)

# reading the set of keyword arguments
def myKwargs(**kwargs): # the double asterisk gathers all the keyword arguments into a dict
    print(kwargs)

if __name__ == '__main__':
    doctest.testmod(verbose=True) # run any docstring tests in this module
    cube(3) # 27
    pythag() # uses the ddfaults for the parameters
    pythag(y=-3, x=-4) # override the default values
    myArgs()
    myArgs(42)
    myArgs(pythag, True, [], {})
    myKwargs(x = 1)
    myKwargs(x = 1, y=2)
    myKwargs(x = 1, y=2, z=True)