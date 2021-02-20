class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.next = None


# node=Node(100)

class SingleLinkList(object):

    def __init__(self, node=None):
        self._head = node

    def is_empty(self):
        return self._head is None

    def length(self):
        cur = self._head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self._head
        while cur is not None:
            print(cur.elem)
            cur = cur.next

    def add(self, item):
        pass

    def append(self, item):
        cur = self._head
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        pass

    def remove(self, item):
        pass

    def search(self, item):
        pass


if __name__ == "__main__":
    ll = SingleLinkList()
    print(ll.is_empty())
    ll.append(1)
    print(ll.is_empty())
    print(ll.length())
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.travel()

# 该看P20了
