# in modern python we can use decorator syntax
# we will encapsulate an 'Todo' class with id, title and completed properties

class Todo(object):
    def __init__(self, id, title,completed):
        self.id        = id # use our setter methods
        self.title     = title
        self.completed = completed
    def __str__(self):
        return '{} {} {}'.format(self.__id, self.__title, self.__completed)
    # use decorators for get/set methods
    @property # this is a getter-method
    def id(self):
        return self.__id #name mangling avoids direct access to this property
    @id.setter # this is a seter method
    def id(self, new_id): # if we leave the 'setter' out, we have a read-only property
        if int(float(new_id)) > 0:
            self.__id = new_id
        else:
            raise Exception # throw an exception to be handled elsewhere
    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, new_title):
        if new_title !='':
            self.__title = new_title
        else:
            raise Exception
    @property
    def completed(self):
        return self.__completed
    @completed.setter
    def completed(self, completed):
        if type(completed) == bool:
            self.__completed = completed
        else:
            raise Exception

if __name__ == '__main__':
    t1 = Todo(1, 'have coffee', False)
    t1.completed = True
    t1.id = 2 # access the id as if it was a proeprty, but actually via the setter method
    print(t1)