#Lesson eight - python as a scripting interface

Now that we know something about how python works and we've seen a little bit of computer science, we are ready for some serious developer tools.  In this lesson we'll learn how to script the command line, creating a powerful interface into the machine.  Later we'll learn how to use make files to get our programs to do even more for us (with extremely efficient parallelization).  

##Enter subprocess

Today we'll start learning how to use python libraries to take advantage of all the hard work of people much smarter than us.  

```
from subprocess import call
from sys import platform

if 'win' in platform:
	call(["dir"])
if "linux" in platform or "darwin" in platform:
	call(["ls","-al"])
```

In the above code, you printed out the current working directory by calling the command line.  Notice that call takes a list of strings.  Each string represents a single word and words are seperated by commas.  Notice this is used for linux systems in the above example.

##PDF to Text

Now that we have a way of accessing the computers resources, let's make use of that to turn pdfs into text files!  For a full explanation of how this works, please go read my friend [Thomas Levine's blog post](https://thomaslevine.com/!/parsing-pdfs/).  In fact, go read everything Tom writes, because he is awesome and knows a TON about computers.  (Way more than I do).

We are now ready for the following small piece of code that will make your life a million times easier:

```
from subprocess import call
from sys import argv

call(["pdftotext","-layout", argv[1]])
```
Okay - so before you can start using this we need to install poppler utils, but don't worry, that's easy:

For linux:

* Simply head to the [poppler site](http://poppler.freedesktop.org/)
* Save the folder to some place reasonable like `~`.  
* Extract the contents
* Open a terminal navigate to the poppler folder (via cd)
* `./configure`
* `make`
* `sudo make install`

After that you are done!

For Windows:

You simply need to download the [windows binary](http://www.outsch.org/wp-content/uploads/2010/09/poppler-utils.zip)

For this you'll need to add the folder to your system variables on windows.  

To check try typing pdftotext in the command line (you'll need to close all open terminals on windows before you can use pdftotext).  If it prints a whole bunch of options then you've succeeded!  After that, just try running the above script with any pdf.  Note: the pdf will need to be processed with optical character recognition (OCR).  You can use, adobe's OCR solution (most offices have this at the very least) or use [google's tesseract project](https://code.google.com/p/tesseract-ocr/).  

Or you could implement your own solution!  For that I'd recommend a deep belief network, neural network, or something hierarchical.  You can see a full list of possible algorithms and implementations at [this kaggle competition](https://www.kaggle.com/c/digit-recognizer).

##Parsing PDFs  

Now that we can translate pdfs to text files, we are finally in a position to pull information from them.  Remember when we covered file IO?  Well we are going to make use of that here.  

We are going to pull out data from [this report](https://github.com/EricSchles/dany_book/blob/master/basic/trafficking_report.pdf).  The report is from the state department and has a table (on page 45 about trafficking convictions).  Wouldn't it be nice if we had a spreadsheet of that data?  We'll now we can make it ourselves!

So what you'll do is download the pdf and then run the following script:







