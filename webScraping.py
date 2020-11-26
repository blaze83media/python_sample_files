from bs4 import BeautifulSoup
import csv
import urllib.request as urllib2
#import pandas as pd

# get page source and create a BeautifulSoup object based on it
#print "Reading page..."

#http=urllib3.PoolManager()
#page=http.request('GET','https://silkroad5v7dywlc.onion.to/index.php?action=printpage;topic=28536.0')




#############################################
sample="<p class='pad1'> My name is this </p><b class='col-sm-12'>me name is ddsdff</b><br><a href='https://www.blaze83media.com/postpage/55/5/new-iphone-se-worth-399-release-for-2020.html'>We are welcoming them</a>"
soup = BeautifulSoup(sample, "lxml")

soup1 = BeautifulSoup(sample, "html.parser")
soup2 = BeautifulSoup(sample, "lxml-xml")
soup3 = BeautifulSoup(sample, "xml")

soup4 = BeautifulSoup(sample, "html5lib")


print(soup.prettify())
print(soup1.prettify())
print(soup2.prettify())
print(soup3.prettify())
print(soup4.prettify())


print(soup.find_all("p"))
print(soup.find_all("a"))

print(soup.p['class']) 

######################################################
s1=BeautifulSoup("<document><content/> My name is this </document>","xml")
s2=BeautifulSoup("<footer> When will the time be?</footer>","xml")

#s1.find(text="name is")
#s1.find(text="My name is this").replace_with(s2)   #not working yet
print(s2)
#print(s1)


##### working request method ########################
pg = urllib2.urlopen("https://www.blaze83media.com/postpage/55/5/new-iphone-se-worth-399-release-for-2020.html", data=None)
sp = BeautifulSoup(pg, "lxml")
#sp = BeautifulSoup(pg, "html.parse")
#print(sp.prettify())
print(len(sp.contents))    #prints everth in the url or file, len is for its length
print(sp.contents[1].name)    #prints html as name

sd=sp.head    #select head tag
print(sd)               #print head tag
print(sd.contents)        # print head tag content

child=' '
for child in sd.contents:
    print(child)

print(sd.contents[1])   #select parts of the array content
print(sd.contents[3])
print(sd.contents[5])        
print(sd.contents[9])

print(sp.body)
print(sp.div)
print(sp.div.p)
#print(sp.div.h1)    #if h1 tag is not in the html u will get 'none'
print(sp.a)
#print(sp.find_all('p'))   #find all <p>
#print(sp.find_all('b'))   #find all <b>

print(len(sp.body.contents)) 
print(len(sp.div.contents)) 

print(sp.body.children)
print(sp.div.children)



