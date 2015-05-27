#Understanding logic

The basic tentants of logic are pretty simple - statements can either be true or false.  

So let's say you had the statement:

My name is Sam (and say my name was infact sam).  Then the statement would be true.

It's important to be aware that not all statements will be true or false.

##Understanding composite statements

Now that we understand that a statement can be true or false, let's understand how to combine simple logical statements to form larger logical statements.  This is done via connector words such as AND, OR, NOT, XOR, and a few others.  The ones of primary concern for us will be AND, OR, and NOT.  

###Understanding the AND statement

The AND statement looks at the left hand side and right hand side of a statement and evaluates the composite statement as either true or false.  

So say we had the two following statements:

```
x = 4
print x < 5 and x == 4
```

In the above example, we'd have a true statement.  

```
x = 3
print x < 5 and x == 4
```

Now the statement should evaluate to false.  

The take away is with and statements, both the left and right hand side of the and must be true, in order for the statement to evaluate to true.

###Understanding the OR statement

The OR statement looks at the right hand side and the left hand side and evaulates the composite statement as well.  However the condition for the statement being true, is of course, different.

Example 1:

```
x = 7
print x%7==0 or x < 4
```

In the above example, the statement will evaulate to true, because the left hand side boolean is true, x%7==0.  Therefore the statement simply evaulates to true and we don't care that x < 4 is false.  

Example 2:

```
x = 4
print x%4==1 or x < 3
```

In this statement, the answer will be false, because both x%4==1 is false AND x < 3 is false, when x is equal to 4.

###Understanding the NOT statement

Unlike the AND and OR statements, the NOT statement only takes a single boolean statement, and changes it's truth value.

thus `not True` -> `False`.

So for example:

```
x = 7
print not(x ==7)
```

