#Lesson Two

Now that we have python installed, the next thing is to understand python as a computational engine.  To do this, we'll explore the basic mathematical operators: 

+ : plus,
- : subtraction,
* : multiplication,
/ : division,
** : exponentiation,
% : modulus,

In addition to the primitive computational tools, we can easily build more advanced algorithms like the square root function:

[source](http://interactivepython.org/runestone/static/gmu-cs100-F2014/MoreAboutIteration/Newton'sMethod.html)
```
def newtonSqrt(n,howmany):
	approx = 0.5 * n
	for i in xrange(howmany):
		better_approx = 0.5 * (approx + n/approx)
		approx = better_approx
	return better_approx

print newtonSqrt(10,3)
print newtonSqrt(10,5)
print newtonSqrt(10,10)

```

Don't worry if that code doesn't make sense, yet.  The notion is, you can use an algorithm to write your own square root function.  

Now that we understand that computation can be done, and with a few lines.  Let's begin to understand Python as a computational engine:

simple_math.py

copy/paste the below code into a file named simple_math.py and run it.

```
print 5+5
print 7+4
print 20*5
print 14*6
print 2**5
print 3**3
print 3/1
print 3%2
print 5%3
print 5 - 7
print 5 - 3
print 3/2 #what's going on here?!
```

As you should have seen the last answer doesn't give you what you expect.  This is because Python does integer division by default.  It can easily fixed by coercising the type of the 3 or 2 in 3/2 to a float - which allows us to carry out floating point mathematics:

`print 3.0/2`

In addition to being able to use python like a calculator, you can also use it for string manipulation, to evaluate true or false statements and to manipulate native programmatic objects.  At the end of the day, all languages only really have a few types: Numbers, Booleans, and Strings.  But the way these types are interacted with, via objects can be extremely powerful, and python is great for object orientation.

Now that we understand how to do computation, how do we save our results for further processing?  Python makes this extremely easy.

storing_data.py

Save and run this file as well, as storing_data.py

```
x = 5+4
print x
x = x - 1
print x
x = x % 2
print x
x = x + 17
print x
x = x**4
print x
```

As you can see, x's value has been changed multiple times.  Also, x appears both on the left hand side (LHS) and right hand side (RHS) of the equal sign.  This is because the `=` is an assignment operator in python, instead of an equality operator.  Unlike mathematics, it's best that operators not have side effects, and so python forces you to differentiate between assignment `=` and equality `==`.  In standard mathematics equality and assignment are defined with `=` because if two quantities are equal, by definition, they must be the same.  Therefore to claim, mathematically, that two values are equal, implies that they are the same thing.  In computer science, we aren't as strict.  In fact, when we are saying `==` we are asking the question, "are the things on both sides equal?".  This is because we allow for the possibility of being wrong, which allows us a great deal of flexibility.

So when we are talking about things like,

```
x = 5
x = x +2
print x
```

We are saying add the value of x (in this case 5) to the value 2 and then store the result in a variable called 'x'.

This behavior extends to any type.  So:

```
x = "Hello there"
x = x + ", Eric"
print x
```

What did we just do?  We added two strings, weird right?  Try this small piece of code out.  You can either copy/paste it into a text editor or you can open a terminal and type python.  This will load the shell, where you can enter the above three lines 1 by 1.  
It's good practice :)

So what this did is concatenate the strings, which I find very, very powerful.  In fact, strings in python are really well designed.  They come with a ton of built in functions (something we'll get to soon) and a lot of great little tricks, like using the `+` operator.

The final thing is to understand is how create booleans:

```
sometimes = True
sometimes = sometimes and False
print sometimes

```

Here we are making use of the boolean operator and, which is true only if both the left hand side of and and the right hand side of and are true.




