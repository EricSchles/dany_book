#Lesson One

Welcome to your introduction to Programming!!  Thanks so much for checking this tutorial and I hope you learn a lot!

lesson plan:

* Installation
* First Program
* Running the program

##Preamble/Requirements gathering

Before we can get started with programming, we'll need to install a few things.  In truth, programming is really just a form of writing, where the words you write have power.  If you write words in the correct way, they can do almost anything.  So in a sense, programming is magic (in a true sense).  After all, you are controlling electricity at the end of the day :)

So what does any form of writing on a device need?  (the answer is two things)

1) A text editor to write with,
2) An idea to write down.

For programming, we'll add a third thing:

3) A way to run the written text.

##Installation

So now that we know sort of what we need, we'll be specific.  We will need 

0) You - our idea generator
1) Emacs - our text editor
2) A Python Interpretter - our way to run our code

###Installing Emacs

There are various operating systems that have you can program on.  I'll cover the major ones here.

Linux: Standard installation from your favorite package manager :)

Ubuntu: `sudo apt-get install emacs` (from the terminal)

(Mac OSX package)[http://emacsformacosx.com/]

(Windows 7 & 8 package)[https://ftp.gnu.org/gnu/emacs/windows/emacs-24.5-bin-i686-mingw32.zip]

###Adding Python to your path (windows only)

Once you have successfully downloaded the emacs folder you'll need to unzip it and then copy it to your c drive (or whatever you've named your hard drive).  From there the instructions vary slightly.

####On Windows 7

Click the start button (lower left) and right click on computer>properties

This will open a new window.  Find Advanced system settings (third option on the left hand side of the window).  From there, click on environment variables.  

In the new window, under system variables, select the variable named Path. (You'll need to scroll to see this).  Then click edit and append the following to the path: C:\emacs-24.5-bin-i686-mingw32/bin; to the text.  Now click OK and then exit out of all the other windows.

####On Windows 8

On the search in windows 8 type in System Environment variables.  From there the steps are the same as with windows 7.


###Installing Python

If you are Ubuntu or Mac OSX you already have a Python interpretter.  If you are on windows keep reading:

You'll need to head to the (python download page)[https://www.python.org/downloads/] and then download Python 2.7.9  From there you'll simply need to copy the installer and next through the steps.  

The final thing you'll need to do is add Python to your path.  To do this go to your system environment variables and add C:\Python27; to your Path variable.  

Now you are ready to start programming!

##Our first example

Now that you are done installing things, let's make use of what we've just installed!  So you'll need to find your terminal.  For Mac OSX and Ubuntu this program is just called terminal.  For Windows we are going to download (git bash)[https://git-scm.com/download/win].  Now launch your terminal (or git bash) and type the following command:

`python`

You should see a bunch of text like this:

```
Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

If you didn't it means something went wrong, get Eric, he'll fix it :).  If you are running this tutorial remote, Eric's email address is ericschles@gmail.com.  Don't abuse that he's giving this out!

Okay, now that you have python type `exit()` into the window (after the `>>>`).  

Now we'll open a text editor from the command line.  To do this type:

`emacs hello.py`

This opens the fille hello.py for editting.  

We are now ready to write our first program!

Type:

`print "Hello World"`

Into the emacs window that should have popped up.  If nothing popped up, again, get Eric and he'll fix it.

Now close emacs and type:

`python hello.py`

This should print `Hello World` to the screen.  Congradulations, you've written your first program!  

##Where we will go from here

Now that you've written your first program, we'll go through the primitives of the python language.  These include:

* If/Else statements
* Variables
* For loops, While loops (known as iteration more generally)
* Functions
* Objects
* Writing to Files / Reading from Files (known as File I/O)

From there will move onto more advanced topics:

* Object Oriented Programming
* Web Development
* Functional Programming
* Statistics in Python
* Data Visualization in Python
* Web scraping
* Machine Learning
* High Performance Computing
  * Multi-threading / parallel processing
  * GPU programming
  * Spark
* Using Databases







