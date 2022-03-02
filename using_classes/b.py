from a import Person


# a code is a person
class Coder(Person): # we inherit everything from the Person class
    def __init__(self, n, a, e, l):
        super().__init__(n, a, e) # call the parent
        self.__language = l
    def __str__(self):
        # NB self.__name is NOT available outside the class it was defined in
        return '{} codes in {}'.format(self.getName(), self.__language)


if __name__ == '__main__':
    c = Coder('Grace', 84, 'grace@nasa.com', 'Python')
    print(c)