from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

#import beautiful soup plus
import requests # allow you to send HTTP requests
from bs4 import BeautifulSoup # allows you to parse
import time  # allows you to do things with dates
import csv #allows you to save csv
import pandas as pd


# In[12]:


#call the webdriver browser 

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)


#open a webpage
driver.get('https://elections.maryland.gov/elections/2022/primary_results/gen_results_2022_1.html')

# Wait a few seconds for load
WebDriverWait(driver, 20)


# find element
results = driver.find_elements(by=By.CSS_SELECTOR, value="#primary_right_col")



# In[13]:


# create empty array to store data for first candidate
data = []

for result in results:
    #find the headline from the alert
    name = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr/td[1]").text
    #find the description from the alert
    votes = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr/td[6]").text
    # append dict to array
    data.append({"name" : name, "total-votes" : votes})


# In[14]:


# create empty array to store data for second candidate
data2 = []

for result in results:
    #find the headline from the alert
    name = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[10]/table/tbody/tr[9]/td[1]").text
    #find the description from the alert
    votes = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[10]/table/tbody/tr[9]/td[6]").text
    # append dict to array
    data2.append({"alert" : name, "description" : votes})


# In[15]:


# close driver 
driver.quit()

# save to pandas dataframe for first candidate
df = pd.DataFrame(data)
print(df)

# for second candidate
df2 = pd.DataFrame(data2)
print(df2)


# In[16]:


# write first candidate to csv
df.to_csv('csv-results/election-test.csv')

# append second candidate to csv
df2.to_csv('csv-results/election-test.csv', mode='a', header=False)


# In[ ]:




