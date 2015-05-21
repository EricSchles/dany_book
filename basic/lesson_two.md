#Lesson two

Here we'll learn how use python like a calculator and how to save the results of a given computation.

##how to do math

```
print 5+5 #addition
print 5-4 #subtraction
print 4*3 #multiplication
print 2**3 #exponentiation
print 8/4 #integer division
print 4/3.0 #floating point division
```

Here we see that most of the standard mathematical operators you know (and possibly love) are well defined in python.  Something that may seem a little strange is the last two things:

```
print 8/4
print 4/3.0
```

8/4 does yield 2, but try doing 4/3.  The result should be 1.3, but it will be 1, which is definitely wrong.  Unless you are talking about integer division.  Fortunately, we can use floating point numbers.  Those are numbers that have a decimal point, so we can have a more precise answer (like the correct one, when we are doing division).  

##How to save answers

Now that we understand how to manipulate numbers with python, let's learn how to store the answers of the things we've manipulated.

```
x = 5
print x + 4
x = x - 3
print x
```

Here we store the value 5, in a variable x, and then add 4 to it (printing the result).  Then we subtract 3 from x, and store the result in a variable x.  Finally, we inspect the last change.  Notice that the change after x + 4 hasn't been saved.  This is because we didn't tell python we wanted to save the change.  This may feel a little weird at first, but it's a choice someone else made that we just have to live with.  In python and in other languages the `=` means, assignment.  

So the statement x = 5, says assign the value of 5 to x.  And x = x - 3, says subtract 3 from the value of 5 and then store it a variable named x.  


