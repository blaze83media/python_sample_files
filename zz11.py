from bs4 import BeautifulSoup
import requests
import csv
import urllib.request as urllib2

# get page source and create a BeautifulSoup object based on it
#print "Reading page..."

#pg = urllib2.urlopen("https://www.blaze83media.com/postpage/55/5/new-iphone-se-worth-399-release-for-2020.html", data=None)
#soup = BeautifulSoup(pg, "html.parse")

#URL = 'https://www.blaze83media.com/postpage/55/5/new-iphone-se-worth-399-release-for-2020.html'
URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)

r1 = soup.find(id='tit')
r2 = soup.find(class_='caption')

print(r1.prettify())
print(r2)

elmt = r1.find_all('div', class_='col-sm-12')
print(elmt)

###############################################################################
ptg = soup.find_all("p")

for yi in ptg:
    print(yi, end='\n'*3)

###############################################################################

ptg1 = r1.find_all("p")

for zs in ptg1:
#q1 =  zs.find('h2', class_='title')    
    q1 = zs.find('a')
    q2 = zs.find('a')
    q3 = zs.find('a')
    if None in (q1,q2,q3):
        continue
    print(q1)
    print(q2)
    print(q3)
    print()


########### NOT YET COMPLETED ####################################################################
print(soup.head)

metaData = soup.find_all("b")
print(metaData)

# likewise the post data is stored
# under <dd ...>
postData = soup.find_all("p")
print(soup.find_all("p"))

# define where we will store info
titles = []
authors = []
times = []
posts = []


for p in postData:
    txt = BeautifulSoup(str(p).strip()).get_text()   #now we iterate through the metaData and parse it
# into titles, authors, and dates
#print "Parsing data..."
    titles.append(txt.split("title:")[1].strip())
    
#for html in metaData:
#    text = BeautifulSoup(str(html).strip()).get_text().encode("utf-8").replace("\n", "") # convert the html to text
    
#    titles.append(text.split("Title:")[1].split("Post by:")[0].strip()) # get Title:
#    authors.append(text.split("Post by:")[1].split(" on ")[0].strip()) # get Post by:
#    times.append(text.split(" on ")[1].strip()) # get date

# now we go through the actual post data and extract it
for post in postData:
    posts.append(BeautifulSoup(str(post)).get_text().encode("utf-8").strip())

# now we write data to csv file
# ***csv files MUST be opened with the 'b' flag***
csvfile = open('silkroad.csv', 'wb')
writer = csv.writer(csvfile)

# create template
writer.writerow(["Time", "Author", "Title", "Post"])

# iterate through and write all the data
for time, author, title, post in zip(times, authors, titles, posts):
    writer.writerow([time, author, title, post])


# close file
csvfile.close()

# done
#print "Operation completed successfully."
