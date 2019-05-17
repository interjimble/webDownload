#A python 3.7.2 program

import webbrowser

siteList = ["linkExample.com/one.html", "linkExample.com/two.html",
"linkExample.com/three.html", "linkExample.com/four.html"]

for x in siteList:
      print(x) #feel free to remove, just to test it works.
      webbrowser.open(x)
