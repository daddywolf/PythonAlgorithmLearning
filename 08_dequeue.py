class Dequeue(object):
    '''双端队列'''

    def __init__(self):
        self.__list = []

    def is_empty(self):
        return self.__list == []

    def add_front(self, item):
        """进队列"""
        self.__list.insert(0, item)

    def add_rear(self, item):
        """进队列"""
        self.__list.append(item)

    def pop_front(self):
        return self.__list.pop(0)

    def pop_rear(self):
        return self.__list.pop()

    def dequeue(self):
        """出队列"""
        return self.__list.pop()
        # return self.pop()

    def size(self):
        """返回大小"""
        return len(self.__list)
