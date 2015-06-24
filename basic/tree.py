class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return repr(self.data)

class Tree:
    def __init__(self,data=None):
        self.head = Node(data)
    def append(self,data):
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            if data <= cur.data:
                cur.left = Node(data)
            elif data > cur.next:
                cur.right = Node(data)
    def pretty_print(self):
        cur = self.head
        self.pprint(self,cur)

    def pprint(self,cur):
        pprint(cur.left)
        print cur
        pprint(cur.right)

if __name__ == '__main__':
    tree = Tree(1)
    for i in xrange(100000):
        tree.append(i)
    tree.pretty_print()	
