from bs4 import BeautifulSoup
import urllib2
from urllib2 import HTTPError
import csv
import re

statesJobsUrls = ["https://www.indeed.com/jobs?q=&l=pierre%2C+sd","https://www.indeed.com/jobs?q=&l=austin%2C+TX","https://www.indeed.com/jobs?q=&l=Houston%2C+TX","https://www.indeed.com/jobs?q=&l=San+Francisco%2C+CA","https://www.indeed.com/jobs?q=&l=Denver%2C+CO","https://www.indeed.com/jobs?q=&l=New+York%2C+NY","https://www.indeed.com/jobs?q&l=Little%20Rock%2C%20AR"]

i = 0

with open('jobData.csv','wb') as jobFile:
   csv_writer = csv.writer(jobFile)
   for stateJobs in statesJobsUrls:
        page = urllib2.urlopen(stateJobs).read()
        soup = BeautifulSoup(page)
        jobs = soup.find(id="searchCount").getText()
        csv_writer.writerow([stateJobs,jobs])
        print(i)
        i += 1
        
    
    
#https://www.indeed.com/jobs?q=&l=austin%2C+TX
#https://www.indeed.com/jobs?q=&l=Houston%2C+TX
#https://www.indeed.com/jobs?q=&l=San+Francisco%2C+CA
#https://www.indeed.com/jobs?q=&l=Denver%2C+CO

#have soup go through a list
#find elements
#write list to csv of job data append


#soup = BeautifulSoup(html_doc, 'html.parser')
#html_doc = """
#<html><head><title>The Dormouse's story</title></head>
#<body>
#<p class="title"><b>The Dormouse's story</b></p>
#
#<p class="story">Once upon a time there were three little sisters; and their names were
#<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
#<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
#<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
#and they lived at the bottom of a well.</p>
#
#<p class="story">...</p>
#"""

#print(soup.prettify())
#print(soup.title.string) good code
#print(soup.title.parent.name)
#
#print(soup.p['class'])
#
#print(soup.find(id="link3"))

#for link in soup.find_all('a'):
 #   print(link.get('href'))
    
#print(soup.get_text())    