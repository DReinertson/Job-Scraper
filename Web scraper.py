import requests
import bs4
from bs4 import BeautifulSoup

import pandas as pd
import time


##URL for page. Would like to have maybe a list or dict sites (since I search multiple sections of sites for jobs

URL = "https://www.flexjobs.com/search?accolade=&category%5B%5D=38&category%5B%5D=165&country=&exclude=&location=&search=developer"

URL_page = requests.get(URL)

##parsing HTML into wanted format
soup = BeautifulSoup(URL_page.text, "html.parser")
job_list = []
description = []
summary = []
location = []
listing = {}

def job_title(soup):
    jobs = []
    ##Div class list-group-item contains information about jobs.
    ##Will append respective information to correct variable and compile each variable at the end.

    for desc in soup.find_all(name = "p", attrs = {"class" : "job-description"}):
        summary.append(desc.text)
    
    for div in soup.find_all(name = "li", attrs = {"class" : "list-group-item"}):

        ##locating h5 and then anchor will give job-title
        for h in div.find_all(name = "h5"):
            for a in h.find_all(name = "a"):
                job_list.append(a.contents[0])

        ##Span with class text-danger is job description
        for span in div.find_all(name = "span", attrs = {"class" : "text-danger"}):
            description.append(span.contents[0])

        ##By using 1st index of p tag, we'll be able to find location of each job. 
        for p in div.find_all(name = "p", attrs = {"class" : "job-type-info"}):
            if p.contents[1] == ' ':
                location.append("No location given")
            else:
                location.append(p.contents[1])

        
def contract(soup):
    return
    
job_title(soup)
print("job_list: ", len(job_list))
print ("description: ", len(description))
print("location: ", len(location))
print("summary: ", len(summary))

