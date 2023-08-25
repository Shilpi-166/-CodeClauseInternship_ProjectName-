import pyshorteners
link=input("enter the link : ")

shortener=pyshorteners.Shortener()

shorted_link=shortener.tinyurl.short(link)

print("shorten link is" )

print (shorted_link)