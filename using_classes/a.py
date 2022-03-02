# declare stuff
p = {'n':'Ada', 'a':42} # if a built-in structure suits your purpose no need for a class

def fn():
    return 'hi'
fn.oooo = 'wow' # an arbitrary property
print(fn.oooo)

# ...but when the built-ins don't meet your need, then make a class
class Person(): # 'self' refers to the class itself
    '''
    explain your class in a docstring
    This class encapsulates a 'Person'
    Paramaters: name, age and email
    'age' must be a positive integer
    '''
    def __init__(self, n, a, e): # all functions in the class MUST take self as a parameter
        self.__name  = n
        self.__age   = a # this is name-mangling - makes it very hard to access this property directly
        self.email = e
    def setAge(self, new_age):
        if int(float(new_age)) >0:
            self.__age = new_age
        else:
            self.__age = 42
    def getAge(self):
        return self.__age
    def setName(self, new_name): # name must be a non-empty string
        if type(new_name)==str and len(str)>0:
            self.__name == new_name
        else:
            self.__name = 'default'
    def getName(self): # we write getter and setter methods (accessor and mutator)
        return self.__name
    def __str__(self): # the built-in __str__ is always used by the print statement
        return '{} age {} email {}'.format(self.__name, self.__age, self.email)

if __name__ == '__main__':
    # we can create an instance of the class
    t = Person('Timnit', 38, 'timnit@babbage.ie')
    # we can access properties using dot-notation
    t.wibble = False # we can always add arbitrary properties to any object
    # we can mutate properties of the instance
    t.setAge(-3) # problem - we can still directly access the age
    t.__age = 13 # this does NOT access the built-in property, it adds another arbitrary property
    print(t, t.getName(), t.__age, t.getAge(), t.wibble)
    # is remains possible to directly access members even if they have been name-mangled
    t._Person__name = 'altered' # not a good use of Python
    print(t) # we have made a change to a name-mangled property

