##The if-statement

The if statement is an essential part of programming, it allows us to automate logic and have more control about how we execute code.

If you'll recall from the last lecture we learned about booleans and how to get boolean values.

Here we'll see how to use an if statement to make use of such a statement.

```
x = 5
if x < 4:
	print "Something crazy happened"
print "end of program"
```

You should copy/paste and then run the following piece of code.  

What does it print out?  It should have printed end of program, this is because x was assigned the value of 5.  So when we run x < 4, this will return false.

You can check this by openning a python REPL and typing: (You get to the python repl by openning a terminal and typing python)

```
>>> x = 5
>>> print x < 4
```

Now that we understand the if statement, let's start understanding more advanced boolean patterns, so that we can start applying if statements in a meaningful way.

##Checking for value in a string

One of the most important uses of the if statement is checking if a word or phrase is in a string.  In fact, this is the most pattern in the code I often write. 

So, enough talk, let's see this in action!

```
greeting = "Hello there, I'm Eric, how are you?"
if "Eric" in greeting:
	print "Eric must have said this"
else:
	print "Eric didn't say this"
```

So there is a lot new going on here.  The first thing is the use of double quoted and single quoted strings.  In the line, `greeting = "Hello there, I'm Eric, how are you?"` I make use of both.  A string can either be enclosed in two single quotes `'like this'` or two double quotes `"like this"`, however when you use both single quotes and double quotes in a string, the other pair will be treated as a literal, rather than ending the quoting.  Thus `'this is a valid string"'` and `"so' is this"`, but `'this is not"` and `"nor is this'`.  Many programming languages make use of this paradigm, so please do try to keep it in mind.  

The next thing that's happening is the `if "Eric" in greeting:` line.  So, what's happening here is pretty simple.  We can actually just look at an english translation - if the string "Eric" is in the string represented by greeting, then the value is true otherwise the value of the statement is false.  This may seem obvious, but let's say you had to check a million lines, having such a tool is extremely powerful.

The print statements should be obvious :)  Do let Eric know if you need a refresher here.  

The final thing is the `else:` line.  This says, first check the if statement and if that statement is false, then do the else statement.  Why this is different the following lines of code:

```
greeting = "Hello there, I'm Eric, how are you?"
if "Eric" in greeting:
	print "Eric must have said this"
print "Eric didn't say this"
```

Is simple.  In the version without the else statement the line `print "Eric didn't say this"` will always execute, the code with the else statement will only execute the line, `print "Eric didn't say this"` if the if-statement is false.  

So say we had two greetings -

`greeting_one = "Hello there, I'm Eric, how are you?"` and `greeting_two = "Hello there, I'm Sam, how are you?"`.  In the situation where the 


So looking at these two flow of control statements:

```
greeting_one = "Hello there, I'm Eric, how are you?"
greeting_two = "Hello there, I'm Sam, how are you?"
if "Eric" in greeting_one:
	print "Eric must have said this"
print "Eric didn't say this"
if "Eric" in greeting_two:
	print "Eric must have said this"
print "Eric didn't say this"
```

And

```
greeting_one = "Hello there, I'm Eric, how are you?"
greeting_two = "Hello there, I'm Sam, how are you?"
if "Eric" in greeting_one:
	print "Eric must have said this"
else:
	print "Eric didn't say this"
if "Eric" in greeting_two:
	print "Eric must have said this"
else:
	print "Eric didn't say this"
```

If you run these two lines of code, one with the greeting as it was originally and the greeting that is false.  

