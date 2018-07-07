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
listing = []
dates = []

def job_title(soup):
    jobs = []
    ##Div class list-group-item contains information about jobs.
    ##Will append respective information to correct variable and compile each variable at the end.

    for date in soup.find_all(name = "div", attrs = {"class" : "col-sm-1 col-xs-2"}):
        new_date = ''
        date = date.contents[1].text
        print ("date: ", date)
        if "Jan" in date:
            new_date = date.replace("Jan", "1")
        elif "Feb" in date:
            new_date = date.replace("Feb", "2")
        elif "Mar" in date:
            new_date = date.replace("Mar", "3")
        elif "Apr" in date:
            new_date = date.replace("Apr", "4")
        elif "May" in date:
            new_date = date.replace("May", "5")
        elif "Jun" in date:
            new_date = date.replace("Jun", "6")
        elif "Jul" in date:
            new_date = date.replace("Jul", "7")
        elif "Aug" in date:
            new_date = date.replace("Aug", "8")
        elif "Sep" in date:
            new_date = date.replace('Sep', "9")
        elif "Oct" in date:
            new_date = date.replace("Oct", "10")
        elif "Nov" in date:
            new_date = date.replace("Nov", "11")
        elif "Dec" in date:
            new_date = date.replace("Dec", "12")
        print ("new_date: ", new_date)

    for desc in soup.find_all(name = "p", attrs = {"class" : "job-description"}):
        summary.append(desc.text)

    for div in soup.find_all(name = "li", attrs = {"class" : "list-group-item"}):

        ##locating h5 and then anchor will give job-title. Append job-title to list of titles.
        for h in div.find_all(name = "h5"):
            for a in h.find_all(name = "a"):
                job_list.append(a.contents[0])

        ##Span with class text-danger is job description. Append job description to list of descriptions.
        for span in div.find_all(name = "span", attrs = {"class" : "text-danger"}):
            description.append(span.contents[0])

        ##By using 1st index of p tag, we'll be able to find location of each job. Will append location to list.
        for p in div.find_all(name = "p", attrs = {"class" : "job-type-info"}):
            if p.contents[1] == ' ':
                location.append("No location given")
            else:
                location.append(p.contents[1])

        ##Find all Dates attributed with each job posting. Will use to sort scraped data into chronilogical order
        for date in div.find_all(attrs = {"class" : "col-sm-1 col-xs-2"}):
            print ('date:', date.text)


def contract(soup):
    return

job_title(soup)
# print("job_list: ", len(job_list))
# print ("description: ", len(description))
# print("location: ", len(location))
# print("summary: ", len(summary))
print ("dates: ", dates)
#
# def compile():
#     for x in range (0, len(job_list)):
#         listing.append((job_list[x], description[x], location[x], summary[x]))
#
# compile()
# print ("listing: ", listing)
