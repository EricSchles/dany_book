#Lesson One

The assumption here is that you already know how to program or are technically proficient.  But you may be new to python.  

Our set up:

Python 2.7.9 && Emacs

##Motivation:

Python:

The reason for Python 2.7.9 is there are a large number of packages that don't have ports yet to Python 3.  Python 3 is a better language, with a lot more functionality.  However, until all of the necessary libraries are ported over, it's not worth it to switch.  The assumption is, eventually this will change and these tutorials will need to be updated.  

Emacs:

The motivation for Emacs over other text editors.  The strongest reason for emacs over other text editors, is simple:  Python tab completion is very good.  This means that you will get to the correct tab completion, in almost every situation, automatically.  I don't know of any other text editor that does this.  

##Installation

Installation for Python and Emacs is very well documented, so I recommend looking on the internet for instructions on how to do this :)

##First Example

Open your text editor and type:

print "Hello World"

name the file hello.py

To run it, navigate to the directory you saved the file in and type:

python hello.py

This should have the following result:

Hello World

The reason no binary was created and no linking is necessary is because Python is an interpretted language, therefore, it is interpretted at run time, rather than being compiled first.  Of course, you can compile python to byte code and simply run the created executable (which is a form of binary code).  

Choosing to make the language interpretted rather than compiled may seem like a clear miss, because of all the speed ups presented by compiled languages.  However in the age of clusters, super computers, and very very fast machines, processing power is cheap.  The goal of python and languages like python is to optimize programmer time, which is significantly more expensive than computer time.  

Of course, if you are running on a very meger budget and still need to get things done, learning a compiled language like C++ or Java is probably in your best interest.  Of course, Python will always be great for prototyping as well as small programs, regardless of whatever languages you decide to learn.  

Other scripting languages worth learning include:

Lua, Haskell, Ruby, Javascript, Groovy, CoffeeScript, Julia

#Where to go from here.

In future lessons we'll cover the language primitives.  From there we'll move onto special topics including web development, data science, high performance computing, cyber security, and networking.   

