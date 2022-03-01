# we can write our own custom generator functions

def normalFn():
    return 'normal functions can only return ONCE'

# a custom generator will generate values on demand
def genSquares(n=0, stop=10, step=1):
    '''
    Generate a sequence of squares of numbers
    '''
    number = n
    stop_before = stop
    while number < stop_before:
        number += step
        yield number**2 # yield instead of return

if __name__ == '__main__':
    normalFn()
    # create an instance of our generator
    g = genSquares(stop=15)
    print(g) # it is a generator - because it has a yield statement
    print( g.__next__() )
    print( g.__next__() )
    print( g.__next__() )
    for x in g:
        print(x, end=', ')