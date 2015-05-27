#Understanding Predicate logic

Predicate logic is used to determine the validity of a given statement via logic.  The notion was to treat statements as components that were either true or false
and then to evaluate these atomic elements in the context of their larger complex grammatical structures.

Below is an example:

The dog is red and I am named Eric.  

For the purposes of this exercise, assume the dog is indeed red.  

Thus we have a true statement and a true statement (since my name is indeed Eric).  The combination of these two statements, via an and, results in a true statement.

Therefore true AND true => true.

There are many logical operators, all of which can be understood through truth tables.  I leave it as an exercise to
prove the truth tables for AND, OR, NOT, (not OR) NOR, (exclusive OR) XOR, (not AND) NAND.  These are the primary operators you'll make use of in computer
science.  There are other logical operators, but we need to not concern ourselves with them.

Once you have convinced yourself of each operator, please do refer to this [cheat sheet](https://a5d4fed1fa89428299f0deb8efb006eb2b9d148d.googledrive.com/host/0B05rsAAJoYVMR1R4ZEtDaTAwbWs/English/Teaching/CSI30-materials/Chapter1-cheat-sheet.pdf)
Until you are comfortable.  

Now that we have the foundation, let's look at some examples of boolean statements in python:

```
print 1 and 0
print True and False
print 1 and ''
print False and ''
print 1 or 0
print [] or 1
print True or False
print True or True
print True and True
print not(False and True)
print None and None
print None and False
print None and True
print None and []
print None and ''
print False and None
print True and None
print [] and None
print '' and None
print True ^ False
print True ^ True
print False ^ False
```

