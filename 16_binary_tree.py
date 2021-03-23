class Node(object):
    '''树的节点'''

    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        '''广度优先遍历'''
        if self.root is None:
            return
        quque = [self.root]
        while quque:
            cur_node = quque.pop(0)
            print(cur_node.elem)
            if cur_node.lchild is not None:
                quque.append(cur_node.lchild)
            if cur_node.rchild is not None:
                quque.append(cur_node.rchild)


if __name__ == "__main__":
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.breadth_travel()
