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
	cur = head
	for i in xrange(100):
		new_node = Node(i)
		cur.next = new_node
		cur = cur.next
	cur = head
	while cur:
		print cur
		cur = cur.next
```

This shows us how to create a linked list.  Notice that we have a few things here.  

##More Objects







