##Lesson 7 - Understanding Objects (continued)

Now that we've made use of some objects other people have written, it's time to write our own!  The first object everyone creates is typically the linked list.

This simple object is called a data structure and it will simply store the data you add to it.  The reason such an object is useful is it will begin our journey to understanding the complexity of computers and teach us a lot about how to write code in an efficient way.  

##Writing an object

Objects are a little different than the code you've seen so far.  Now you'll need to declare a specification, called a class for how your object should behave, store data, or interact with the world.  

```
class Node:
	def __init__(self,data,next=None):
		self.data = data
		self.next = next
	def __str__(self):
		return repr(self.data)

if __name__ == '__main__':
	head = Node(0)
	print head

	#list generation
	cur = head
	for i in xrange(100):
		new_node = Node(i)
		cur.next = new_node
		cur = cur.next
	
	#list observation
	cur = head
	while cur:
		print cur
		cur = cur.next
```

This shows us how to create a linked list.  Notice that we have a few things here.  

The way an object's blueprint is created, is with class [Name of class].  To create a new instance of the object we set a variable equal to the name of the class, like we do in the main - `head = Node(0)`.  Such a construction instiates the class, storing any state related data.  The state of an object is defined in the __init__ function, in this case - `data` and `next` are the state variables.  

These two types of variables - `data` and `next` represent to major types of data that can be stored - a classical variable (like the ones we've interacted with thus far) and a new type of variable, called a pointer.  

Pointers are a very interesting topic and making use of them we can do all sorts of things 'in memory'.  A pointer doesn't store data the way a typical variable does.  Instead, it stores meta-data about another variable or object.  Typically this meta-data is the address of the variable.  Why would you want to store such a thing?  Well because then you can create structures for your data 'in-memory'.  

This is powerful because the way in which your data is organized determines how efficiently it can be accessed.  In some cases it can mean the difference between a computation taking miliseconds and days.  

One more thing to note - because python is weakly typed (which means we don't need to specify the type of a variable when we create it) we don't need to do anything special to create a pointer in python.  We simply need to "decide" a variable is a pointer and use it accordingly.  So there is nothing special about next (in this context) and there is nothing special about initializing it to `None`.  `None` is an important keyword - it represents a non-type and means there is no value in the variable.  None is also similar in behavior to False (in python).  In other languages this might be called the null pointer (which is distinct from False) or it might be called nil.  
Now that we understand the __init__ and the types of data it can hold.  Let's move onto __str__ which is known as the "to string" method - a term popularized by Java.  (Which you should all learn by the way).  The to string method defines what data should be shown when you try to print the instance of the object.  In this case, we should print data.  We have to wrap our data in the repr function to ensure we get the canonical string representation of the object, instead of the object representation.  

Now that we understand our object blueprint, let's see how to use this object in practice.


###Understanding the linked list
```
if __name__ == '__main__':
	head = Node(0)
	print head

	#list generation
	cur = head
	for i in xrange(100):
		new_node = Node(i)
		cur.next = new_node
		cur = cur.next
	
	#list observation
	cur = head
	while cur:
		print cur
		cur = cur.next

```

The object - called Node that we created is the main piece of something called a linked list.  The reason the data structure is named as such is because the list is created by linking nodes together, via pointers.  The pointer stores the address to the next object in the series, creating a chain.  

Notice the use of standard conventions here - creating a variable cur (which stands for current) that references the head of the list and is updated throughout the list generation process.  Notice that to iterate the cur node to the next, we simply set the cur node's next variable - via cur.next = new_node and then set cur equal to the next node.  It is through this reference and indirection scheme that we are able to play with the semantics of memory in our program.

Notice also we make use of this same paradigm - cur = cur.next when printing out all the elements in our linked list.

##More Objects

Now that we understand what happens when we have one pointer, what would happen if we had two?

```
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
	
```

The linked list is a data structure that motivates iteration.  The tree data structure motivates a different type of iteration called recursion.  A recursive function is one that typically increments or decrements a counter (for a finality condition) and does computation on successive subproblems of a problem.  Examples of uses of recursive functions are:

* Calculating sequences
* Recursing web pages
* much, much more!

The major difference here is that we call a function within a function.  Doing so allows us to create a recursive call stack "in memory".  Notice that we've now learned how to play with memory in two ways - via function calls and via variable assignments.  There are many more ways to play with memory and this is the essence of computer science.  






