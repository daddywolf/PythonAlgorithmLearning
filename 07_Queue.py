class Queue(object):
    """队列"""

    def __init__(self):
        self.__list = []

    def is_empty(self):
        return self.__list == []

    def enqueue(self, item):
        """进队列"""
        self.__list.insert(0, item)
        # self.__list.append(item)
        # 必有一个O(n)必有一个O(1)

    def dequeue(self):
        """出队列"""
        return self.__list.pop()
        # return self.pop()

    def size(self):
        """返回大小"""
        return len(self.__list)


if __name__ == "__main__":
    q = Queue()
    q.enqueue("hello")
    q.enqueue("world")
    q.enqueue("itcast")
    print(q.size())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
