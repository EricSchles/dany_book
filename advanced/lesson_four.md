#Understanding flow of control

Now that we understand what and how a boolean works, let's begin working through flow of control and making use of booleans in practice.

The fundamental flow of control statement is:

```
if [some condition]:
  [do this]
[do some other stuff]
```

A specific example:

```
x = 5
if x < 5:
  print "something insane happened"
print "hello there"
```

As the above statement shows, we check whether x is indeed less than 5 as we anticipated, or if something crazy happened. In the event that the unexpected, did indeed occur, we note that by printing out "something insane happened".

The specific boolean statement - x < 5 is one of the many standard boolean statements you'll encounter in the world of programming.  Typically a comparison such as:

* val1 < val2 - val1 less than val2
* val1 > val2 - val1 greater than val2
* val1 == val2 - val1 equals val2
* val1 != val2 - val1 not equal val2
* val1 <= val2 - val1 less than or equal to val2
* val1 >= val2 - val1 greater than or equal to val2

###Some specific examples

```
import random
x = random.randint(0,20)
if x < 5:
  if x >= 2:
    print "We think x is 3, but it could be 4"
  elif x <= 2:
    print "We know x is 0, 1, or 2."
else:
  print "x is larger than 5 for sure"
```

Here I introduce two new flow of control paradiagms - elif and else.  

elif (which stands for else if) can only be used after an if statement.  The way it works is similar to if, except the condition is only checked in the event that the if statement is false.  The reason this is different than writing two if statements, one after another, may be none obvious.

Consider the following example:

```
import random
x = random.randint(0,20)
if x%2==0:
  print x
  x = 5
elif x == 5:
  print "x is 5"
```

And,

```
import random
x = random.randint(0,20)
if x%2==0:
  print x
  x = 5
if x ==5:
  print "x is 5"
```

In the first example, only the if block is executed, while in the second example, both the first and second if blocks will be executed.  Thus we see the difference - with if, elif the circuit is cut short if the first statement is true and thus, the elif isn't even checked.  Say you had a statement with many possible conditions, like 15 or so.  Being able to use if or elif statements will yield significantly different behavior.  Neither is the right way to go, and in fact it all comes down to the disired functionality.

As far as the else statement goes - it's far easier to explain.

The else statement only executes if the if statement should fail.  So:

```
x = 6
if x%2==0:
  print "x is even"
else:
  print "x is false"
```

