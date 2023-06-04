#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install selenium')
get_ipython().system('pip install wget')
get_ipython().system('pip install webdriver_manger')


# In[23]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sklearn
from sklearn import preprocessing, linear_model, model_selection
from sklearn.preprocessing import StandardScaler , MinMaxScaler
from sklearn.model_selection import train_test_split
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import os
import matplotlib as mpl
import math
from collections import Counter
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import bs4
from bs4 import BeautifulSoup
import scipy as sc
import requests
import csv


# In[24]:


import requests
 
# Lat-Lon of New York
URL = "https://weather.com/weather/today/l/40.75,-73.98"
resp = requests.get(URL)
print(resp.status_code)
print(resp.text)


# In[25]:


driver = webdriver.Chrome()
check = driver.get("https://www.zillow.com/homes/")
print (check)


# In[26]:


import requests
import io
import pandas as pd

URL = "https://www.zillow.com/homes/.txt"
page = requests.get(URL)
df = pd.read_csv(io.StringIO(page.text), sep="\t")
df.to_excel(r'i_data.xlsx', index = False)


# In[27]:


import csv
from urllib.request import urlopen
html = urlopen("http://www.google.com/").read()
print(html)
import urllib2

url = 'https://www.zillow.com/homes/medals.csv'
response = urllib2.urlopen(url)
cr = csv.reader(response)

for row in cr:
    print (row)



url = 'https://www.zillow.com/homes/medals.csv'
r = requests.get(url)
text = r.iter_lines()
reader = csv.reader(text, delimiter=',')


# In[33]:


from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Chrome(
    executable_path='/usr/lib/chromium-browser/chromedriver')

driver.get('https://www.zillow.com/homes/')
driver.implicitly_wait(10)
driver.maximize_window()
r = 1
templist = []

while(1):
	try:
		method = driver.find_element(By.XPATH, '//*[@id="post-427949"]		/div[3]/table[2]/tbody/tr['+str(r)+']/td[1]').text
		Desc = driver.find_element(By.XPATH, '//*[@id="post-427949"]/		div[3]/table[2]/tbody/tr['+str(r)+']/td[2]').text
        
		method = driver.find_element(By.XPATH, '//*[@id="post-427949"]		/div[3]/table[2]/tbody/tr['+str(r)+']/td[1]').text
		Desc = driver.find_element(By.XPATH, '//*[@id="post-427949"]/		div[3]/table[2]/tbody/tr['+str(r)+']/td[2]').text

		Table_dict = {'Method': method,
					'Description': Desc}

		templist.append(Table_dict)
		df = pd.DataFrame(templist)

		r =r +  1

	# if there are no more table data to scrape
	except NoSuchElementException:
		break

# saving the dataframe to a csv
df.to_csv('table.csv')
driver.close()


# In[38]:


# Python program to demonstrate
# selenium

# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Chrome()

# enter keyword to search
keyword = "zillow"

driver.get("https://www.zillow.com/homes/")

# get element
element = driver.find_element(By.XPATH, "//*[@id="wrapper"]/div[5]")

# print complete element
print(element)


# In[ ]:





# In[ ]:





# In[ ]:




