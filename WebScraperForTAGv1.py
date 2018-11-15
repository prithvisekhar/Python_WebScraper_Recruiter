# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 07:48:17 2018

@author: prithvisekhp
"""

import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

def jobsiteIndeed(skill, location, resultLinks):
    BaseURL = "https://www.indeed.com/resumes?q=&l=&cb=jt&cb=skills&cb=fos"
  # print(BaseURL)
    indexSkill = BaseURL.find("?q=")

    SearchURLIndeed = BaseURL[:indexSkill+3] + skill + BaseURL[indexSkill+3:]
  #print(SearchURLIndeed)
    indexLocation = SearchURLIndeed.find("&l=")
    SearchURLIndeed = SearchURLIndeed[:indexLocation+3] + location + SearchURLIndeed[indexLocation+3:]
  #print(SearchURLIndeed)
  
    #conducting a request of the stated URL above:
    page = requests.get(SearchURLIndeed)
    #specifying a desired format of “page” using the html parser - this allows python to read the various components of the page, rather than treating it as one long string.
    #soup = BeautifulSoup(html_doc, 'html.parser')
    soup = BeautifulSoup(page.text, 'html.parser')
    #printing soup in a more structured tree format that makes for easier reading
    #print(soup.prettify())
    #Runnning the function to extract links
    extract_links_from_result(soup, resultLinks)
    return 1


def extract_links_from_result(soup, resultLinks):

    Links = []
    for div in soup.find_all(name='div', attrs={"class": "app_name"}):

        for link in soup.findAll('a', attrs={'href': re.compile("/r/")}):
            Links.append(link.get('href'))
    #print(Links)
    MaxLinks = 10
    resultLinks = Links[:MaxLinks] # to extract MaxLinks only
    WebRef = "https://www.indeed.com"
    resultLinks = [WebRef+ s for s in resultLinks] # to append the website reference
    print(resultLinks)
    return resultLinks

#need to append https://www.indeed.com/ befor the below list


#Inserting the sillk and location
skill = "embedded+systems"
location = "Bengaluru%2C+Karnataka"
resultLinks = []
jobsiteIndeed(skill, location, resultLinks)
#print(resultLinks)


# extract 10 links
#Links get append
# Results into file -
# mail merge
