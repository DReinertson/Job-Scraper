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

def job_title(soup):
    jobs = []
    ##Div class list-group-item contains title of job. Will locate list-group-item, h5 within and then the anchor tag.
    for div in soup.find_all(name = "li", attrs = {"class" : "list-group-item"}):
        for h in div.find_all(name = "h5"):
            for a in h.find_all(name = "a"):
                jobs.append(a.contents[0])
    return jobs

jobs_list = job_title(soup)
print ("jobs: ", jobs_list)
