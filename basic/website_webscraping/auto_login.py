import requests

payload = {"username":"Eric","password":"1234"}
print requests.post("http://localhost:5000",data=payload).text
