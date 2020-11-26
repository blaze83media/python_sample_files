from bs4 import BeautifulSoup
import requests
import csv
import urllib.request as urllib2

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)

results = soup.find(id='ResultsContainer')
print(results.prettify())      # beautify the result for readability

job_elems = results.find_all('section', class_='card-content')

for job_elem in job_elems:
    print(job_elem, end='\n'*3)
    
    
print('#####################################################################')
          
for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()


#select only text needed
#python_jobs = results.find_all('h2', string='Python Developer')

##find a word in the search then convert to lowercase
    python_jobs = results.find_all('h2',
                               string=lambda text: 'python' in text.lower())

#find how much of the word is there    
print(len(python_jobs))

print('#####################################################################')
      
for p_job in python_jobs:
    link = p_job.find('a')['href']
    print(p_job.text.strip())
    print(f"Apply here: {link}\n")




#further practice
#http://pythonjobs.github.io/
#https://remote.co/remote-jobs/developer/
#https://au.indeed.com/?sq=1