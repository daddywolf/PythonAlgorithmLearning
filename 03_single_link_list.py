class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None


# node=Node(100)

class SingleLinkList(object):

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self.__head
        while cur is not None:
            print(cur.elem, end="  ")
            cur = cur.next
        print("")

    def add(self, item):
        '''链表头部添加元素，头插法'''
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        '''链表尾部添加元素，尾插法'''
        cur = self.__head
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        '''
        :param pos: 从0开始
        :param item:
        :return:
        '''
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)
            cur = self.__head
            for i in range(pos - 1):
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        pass

    def search(self, item):
        pass


if __name__ == "__main__":
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())
    ll.append(1)
    print(ll.is_empty())
    print(ll.length())
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.travel()
    ll.insert(3, 9)
    ll.travel()
