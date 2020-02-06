# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 18:19:21 2020

@author: samou
"""
import requests #request webpage HTML information
from bs4 import BeautifulSoup #beautifulsoup fundamental in working with page HTML data
import pandas as pd #I want to use beautifulsoup to create a pandas dataframe

#get URL and store as page variable
URL = 'http://www.bom.gov.au/jsp/ncc/cdio/weatherData/av?p_nccObsCode=136&p_display_type=dailyDataFile&p_startYear=2019&p_c=-898522497&p_stn_num=067027'
page = requests.get(URL)

#pass page variable through beautifulsoup html parser
soup = BeautifulSoup(page.content, 'html.parser')

#find the table on the page, which in this case is still quite dense with HTML
#then use prettify to make it more readable, this is just to help me look at it
table = soup.find(id='dataTable')
print(table.prettify())

#using the inspect page element we can easily see all of the rows of data are contained under the <tr> tags
#so find and store them in tableRows
tableRows = table.find_all('tr')

#setup variable to fill with column data, found under <td class> tags
#strip to remove extraneous characters from strings
dtb = []
for tr in tableRows:
    td = tr.find_all('td')
    row = [tr.text.strip() for tr in td if tr.text.strip()]
    if row:
        dtb.append(row)

#now the easy part, pass our list through pandas and bang we have a dataframe
df = pd.DataFrame(dtb, columns=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"])
print(df)
