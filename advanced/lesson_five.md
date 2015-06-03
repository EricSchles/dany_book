#Iteration - the power of computation

Up until now we've learned mostly basic ways of dealing with computation, understanding simple programs like this:

```
x = 5
x = x + 7
if x < 4:
	print "what happened here?"
else:
	print "everything worked, phew"
print x
```

In this lecture we'll learn the true difference between computational thinking and mathematical thinking - iteration.  Thinking computationally, means being able to do something millions or trillions of times and making use of asymptotic behavior to meet some condition, because a computer's time is cheap.  No one cares if a computer runs for 4 days without stopping, working on one problem.  In mathematics, humans solve computational problems, and thus getting there as fast and as elegantly as possible is paramount.  This has lead to some of the most beautiful and precise mathematical writing ever.  But now that we can simply make use of asymptotic behavior, we really don't care how long solutions take to be found, or how precise our equations are.  As long as they get there "eventually" where "eventually" is a relative term.  It is relative in the sense of how powerful the computational engines you have available take to accomplish a task.  

So let's say you have a mathematical problem and a solution that will take trillions of mathematical operations to find a solution and let's say you have a computer (mostly likely a cluster) that can do half a trillion operations a second.  Then you need not find the more elegant, efficient solution, because what do you care if a computer has to think for 12 seconds on your problem?  If the problem needs to be solved every second, yes, you still need to find a more elegant solution, but only in the case of performance essential tasks do you care about being efficient.  And you can always just add resources, assuming they are sufficiently cheap.  Therefore you'll never need to do better computationally, than you do mathematically, and it is rare you'll need to do as well.  

So, how do we run a calculation many, many times?

##The For-Loop

```
for i in range(10000):
	print i
```

This program creates a temporary variable i and set's it equal to each of the values in range(10000) in order, from index 0, to index 10000-1.  

So the for loop more or less says the following in english: 

for each element, named i, in the list range(10000) print i to the screen.

You should try running the above code, just to see what it's doing.  


```
summation = 0
for i in range(10000):
	summation += i
print summation

```

This code is slightly more interesting, here, we see a summation of the elements of range(10000), which is also known as an accumulator pattern.  There are many design patterns in computer science and software development.  This is just a simple example of one.

Another new thing here is summation += i, which is equivalent to summation = summation + i.  Notice the order.  While this doesn't matter for addition, since addition is communiative, however for operators like subtraction this is not the case.  

##Lists

In the previous section we haphazardly mentioned lists via the range function.  Now let's be a bit more precise about them.

A list is a series of elements that can be accessed via an index.  So you can think of them as a group of variables that are associated programmatically.  Whether or not they are associated semantically is a matter of choice by the programmer (since computers don't understand semantics easily), however they need not be associated semantically to be associated programmatically.  The association is simply one of memory.  In a sense, a list is actually just one giant variable that takes on many smaller container elements for it's individual part.

One way to think about this, is a list is like the forrest, and each element is a tree.

Enough talk, let's look at what a list looks like in detail.

```
x = [1,2,3]
print x
print dir(x)
``` 

You should run the above code.  

As it shows, x is comprised of the elements, 1, 2, and 3.  All notice that we print all the methods associated with x.  These methods are functions that will act on the elements of the list, x.

Since the dir funtion itself returns a list, let's look at it's output from a for-loop:

```
x = []
for method in dir(x):
	print method
```



