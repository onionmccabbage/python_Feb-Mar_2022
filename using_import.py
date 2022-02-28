import using_input as wibblywoo # everything is imported from that module

# we can declare functions whenever we like
def boo(b):
    if type(b) == bool:
        # the None operator is useful for setting to nothing
        print( None == b ) # is an empty list equivalent to a boolean True

# Python has a 'range' object
def use_r():
    for i in range(10,-3,-2): # start, stop-before, step
        print(i)

if __name__ == '__main__':
    print('this is the main module')
    wibblywoo.main()
    # invoke our functions
    boo(False)
    use_r()
    # using 'in'
    t = (3,5,7,9)
    x = 4 in t # True or False
    print(x)