class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return repr(self.data)

    def has_next(self):
        if self.left != None or self.right != None:
            return True
        else:
            return False
        
class Tree:
    def __init__(self,data=None):
        self.head = Node(data)

    def append(self,data):
        if not self.head:
            self.head = Node(data)
        else:
            self._append(self.head,data)

    def _append(self,cur,data):
        if cur.data > data and cur.left == None:
            cur.left = Node(data)
        elif cur.data < data and cur.right == None:
            cur.right = Node(data)
        else:
            if cur.data < data:
                self._append(cur.right,data)
            else:
                self._append(cur.left,data)
                        
    def pretty_print(self):
        cur = self.head
        self.pprint(cur)

    def pprint(self,cur):
        if cur.left:
            self.pprint(cur.left)
        print cur
        if cur.right:
            self.pprint(cur.right)

if __name__ == '__main__':
    tree = Tree(1)
    for i in xrange(100):
        tree.append(i)
    tree.pretty_print()	
