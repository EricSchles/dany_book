#Understanding lists

Python has much more than just basic variables.  You can actually create groupings of variables, often referred to as data structures.  The term data structure refers to a structure for your data.  Pretty simple right?  In fact, data structures are one of the most complex and interesting parts of computer science.

##Seeing the list in action

A list is a very simple data structure, where the data structured in a sequential order.  

```
x = [1,2,3]
print x
```

So the list stores the elements indexed by the natural numbers.  

```
x = [1,2,3]
print x[0]
print x[1]
print x[2]
``` 

This is known as referencing elements in a list by index.  

##Introduction to functions

A function is a piece of code that is referenced by a name and called by name.  Then the code in the function is executed and a result is returned.

```
def f(name):
	print "Hello there "+name

f("Eric")
f("Billy")
f("Jim Bo Jangles")
print f
print f("Eric") 
```

If you run this code, you'll see a bunch of greetings and then the memory address of the function f, and finally you should see None.  This is because the function f doesn't actually return anything.  

```
def g(x):
	return x*x
print g(5)
print g(8)
print g(49)
```

Here we see the use of the return statement, which will pass whatever value is being returned back.  If the function hits a return statement, the function will end, no matter how much code is left.  So we could have a function like:

```
def f():
	return "hi"
	print "things"
f()
```

If you try this code, you'll notice that things is never printed to the screen, this is because the statement simply returns `"hi"` before it has a chance to execute the print statement.

##Introduction to Methods

Now that we understand functions, let's understand methods.  A method is a function associated with a data structure - like a list.  The list data structure has several methods associated with it which will manipulate the elements in the list.  This makes list extremely powerful.

Let's took a look at a few methods presently:

```
x = [1,2,3]
print x
x.append(4)
print x
```

The append method will add an element to the end of the list.  We can also remove elements with the following method:

```
x = [1,2,3,1]
print x
x.remove(1)
print x
```

Notice the remove method only removes the first occurrence of the number 1, which is actually best.  

If you are interested in any of the methods associated with a specific data structure you can use the dir function, which is built into python. 

```
x = []
print dir(x)
```

If you run the following code, you may have noticed that dir returns a list of methods.  The dir function will work with anything in python, so feel free to use whatever.

##Introduction to iteration



