# static methods and class methods

class Duck():
    count = 0 # this property belongs to the class, not to any particular instance
    def __init__(self):
        Duck.count += 1 # every time a Duck is instantiated, the count will increase
    @classmethod
    def numDucks(cls): # we don't use 'self' but by convention we use 'cls'
        return cls.count
    @staticmethod
    def promo(): # no self, no cls...
        return 'this promotional content will encourage you to buy ducks'

if __name__ == '__main__':
    # call static metods on the class - they have NO DEPENDANCE on ANY instances
    print( Duck.promo() ) # works even if there are no instances
    donald = Duck()
    howard = Duck()
    ella   = Duck()
    n = Duck.numDucks() # call the method on the class itself
    print(n)