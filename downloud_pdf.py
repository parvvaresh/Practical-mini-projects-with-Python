import urllib.request
url = input("enter link to downloud : ")
name = input("enter name of book")
name += "pdf"
urllib.request.urlretrieve(url, name)