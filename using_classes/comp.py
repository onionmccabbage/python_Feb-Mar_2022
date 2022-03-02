# we can use classes to compose other classes
# lets build a duck

class Bill():
    def __init__(self, description):
        self.description = description

class Tail():
    def __init__(self, length):
        self.length = length

class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def __str__(self):
        return 'This duck has a {0} bill and a {1} tail'.format(self.bill.description, self.tail.length)

if __name__ == '__main__':
    b = Bill('long orange')
    t = Tail('medium')
    d = Duck(b, t)
    print(d)