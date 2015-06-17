#Lesson Six - Objects

In this lesson we will be moving forward from people who use computers to computer scientists.  The biggest part of this jump is the introduction the object, as a concept.  

##Files as objects

Technically everything in python is an object - so functions are objects, int's are objects, strings are objects, booleans are objects, and anything else you might encounter.  But we typically don't frame these "things" as objects.  

This is because of the way objects are typically treated.  Objects are typically both data and methods.  

So for instance for a string:

```
hello = "Hello"
print dir(hello) # shows all the methods
print hello #shows the data
```

The reason I made use of the string as the basic example of an object is because file objects are very similar to strings.  The major difference is that the strings are stored after the program ends.  Also this allows us to access the string in another program later or concurrently.  (Don't worry we won't do concurrency today, but it will happen somewhat soon!)

###Writing to a file

The first thing to learn is writing to a file - which is essentially "saving data" like you would with a word document.  

```
f = open("file.txt","w")
f.write("Hello there\n")
f.close()
```

###Reading data from a file

Now that we have the data saved to a file, let's print it to the screen!

```
f = open("file.txt","r")
contents = f.read()
f.close()
print contents
```

###Understanding files as streams

Now that we understand how to read data from a file and send data to a file, let's understand what the file object really is.  A file object is part of a whole class of objects called streams.  The characteristics of a stream are almost completely standard.  There is always a way to get data from the stream, send data to the stream, open the stream, and close the stream.  Notice in the above example that we do all four things.  We always have to open the stream before reading or writing to it, and we always have to close the stream when we are done using it.  The two major examples of streams in modern computing are:

* connection streams - data streaming over an internet/intranet connection
* file streams - data streams from somewhere on your physical computer

##The with statement

Often times having to open and close a connection is a pain.  For this reason the core python programmers have created a keyword called `with`.  The `with` keyword expects an __enter__() and __exit__() method.  For those of you interested in a deeper understand I'd encourage you to read the [PEP for with](https://www.python.org/dev/peps/pep-0343/).  

###Seeing the with statement in action

```
with open("file.txt","r") as f:
	print f.read()

try:
	print f.read()
except:
	print "couldn't read the file!!"
```

By using the with statement, you neither need to close or open the file, `file.txt`, instead it is openned and closed automatically.  Notice that the file object (f) is only openned inside the scope of the `with` statement.  

This is very helpful and safe!  In fact, a very large part of cyber security stemms from the fact that people forget to close files properly when they are done using them.  This creates what's called a memory leak.  Fortunately, the file system is usually smart enough to close a file at the end of the program, whether it's told to or not.  But, if a program exits unexpectedly due to a bug in the program, such a closure may not happen.  

If the file is not closed, then that memory is just around and free for any program to use, under the right conditions.  And is how malicious code finds the space it needs to execute.  By opening and closing streams automatically, we make our code more secure and easier to read! 

##Understanding the try, except statement

Until now we haven't written any code that could actually "fail".  If we write code where a statement could fail, then it will cause the program to exit, unexpectedly (from the computers perspective).  

Below we will write a program that will definitely not work:

```
x = []
print x[0]
```

If you try to run this program, you should get an IndexError print to the screen - because there is nothing stored at index 0 in the list!  A way to get this program to run, without fixing this bug is as follows:

```
try:
	x = []
	print x[0]
except IndexError:
	print "index error encounter but we finished anyway"
```

What the `try` does is try the code in the try block and whenever an exception is encountered, anything in the except block will execute.  In this case we pass in the type of exception we will allow.  If any other except is encountered, the program will still fail.  If you are interested in debugging your code, you'd more than likely just do this:

```
try:
	x = []
	print x[0]
except:
	print "error occurred"
``` 

Since we didn't specify an exception type, all exceptions are caught.  








