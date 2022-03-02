# we can override the built in features of Python
# we already saw __str__ - there are plenty more

# here we will override the equality operator
class Word(): # implicitly inherit from 'object'
    '''
    this class compares words regardless of their case
    e.g. hello == Hello should be True
    '''
    def __init__(self,text):
        self.text = text # here we don't use get/set methods
    def __eq__(self, other_word): # __eq__ is the built in == operator
        return self.text.lower() == other_word.text.lower()

# use with great care!!!!!!
# __ne__ not equal
# __gt__ greater than
# __lt__ less than
# __ge__ and __le__ greater-or-equal and less-or-equal

# other 'magic methods'
# __add__( self, other ) self + other
# __sub__( self, other ) self - other
# __mul__( self, other ) self * other
# __floordiv__( self, other ) self // other
# __truediv__( self, other ) self / other
# __mod__( self, other ) self % other
# __pow__( self, other ) self ** other
# __len__ is the length of the object

if __name__ == '__main__':
    str_a = 'hello'
    str_b = 'Hello'
    print(str_a == str_b) # normal equality behaves as expected
    # use our class
    w1 = Word('hello')
    w2 = Word('Hello')
    print(w1.__doc__) # access the docstring
    print(w1 == w2) # True