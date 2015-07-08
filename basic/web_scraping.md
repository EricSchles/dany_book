#Web Scraping

Web scraping is the ability to take content from the web and store it and manipulate it locally.  There are many reasons someone might scrape the web, but at it's core, web scraping is about taking in unstructured or poorly structured data and structuring it to learn something.  

Web scraping can be used for a few obvious tasks:

* Social Network Analysis
* Financial/Economic Analysis
* In conjunction with Natural Language Processing
 * Sentiment/Psychological Analysis
 * Political Analysis

##Understanding the web

In order to understand web scraping, we need to understand the web.  This means understanding the various networking layers (in some detail), understanding html (well) and understanding the client/server model (in some detail).  

###The OSI Model (Open Systems Interconnect)

The [OSI model of the internet](link to wikipedia article) (while somewhat dated) shows the granularity of concerns within the internet.  As you can see (if you clicked the link), there are seven layers.  We care about the presentation layer (which is where HTML lives), the HTTP layer, and the TCP/IP layer.  Since we'll talk about HTML indetail we'll avoid it for now.  

###HTTP - Hypertext Transport Protocol

HTTP defines a few methods that are language agonostic and will be used to send information from the server computer to the client computer.  The server computer is where the data is saved (like the html,CSS,javascript,server code, and database of the website).  The way a client computer asks for information from the server is via a request called a `GET` request.  The client can also send data to the server via a `POST` request.  There are a few other request types that can be sent to and from the client and server but these are the ones we primarily care about.  

When scraping the web, we'll be making use of the `GET` request to get information from a specific website (rather than a specific server) but we'll be sending that request to one of a cluster of computers all serving the same content.

First we'll need to install the requests library with the following command:

`sudo pip install requests`

If you are on linux or mac

For windows users, open powershell with admin privileges and type:

`pip install requests`

In python we make a get request as follows:

```
import requests

req = requests.get("https://www.google.com")
print req.text
```

Here I've made a get request to google.com and saved the result of the request in an object called req.  After I get the object back I can use one of many methods to interact with the content locally.  If you try running this code, you should see a whole bunch of html fly by your terminal, that's the html information that google.com servers.  The text object stores the html from the given request.  

Now let's say you wanted to send some data to the server - say login credentials?  To do that you'd need to send a post request

```
import requests

payload = {"username":"Eric","password":"1234"}
r = requests.post("http://localhost:5000",data=payload)
print r.text
```

(We'll be skipping TCP/IP until we do dynamic web scraping in another lecture).

###HTML

Now that we understand how to get a bunch of html, let's learn how to structure it.  A very common task is finding all the links on the page.  With python and lxml this is easy, however it's going to require some upfront understanding of how an html document is structured.  

###Understanding HTML

HTML is structured as a tree, where the tags inform the hierarchy of the structure.  

A typical HTML document will look like this:

```
<html>
<head></head>
<body>
  <p>Hello there</p>
</body>
</html> 
```

Within the html document the `html` tag is the root of the tree.  Since the `html` tag wraps around the `head` tag, it is considered a child of the `head` tag.  Note that the p tag is at the deepest level in the tree because it is encased in other tags but does not enclose any other tags.  

###Traversing HTML

Now that we have a rudimentary understanding of html, we can begin to traverse the html via python and lxml.html

installation:

`sudo pip install lxml.html`

on windows open powershell with admin rights (please make sure you have a c++ compiler installed)

`pip install lxml.html`

```
import lxml.html
import requests

r = requests.get("https://www.google.com")
html = lxml.html.fromstring(r.text)
print html.xpath("//a/@href")
```
