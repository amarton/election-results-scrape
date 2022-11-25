from selenium import webdriver

from selenium.webdriver.firefox.service import Service as FirefoxService
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


# In[96]:


#####################
#GOV RACE
#####################


#call the webdriver browser

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)


#open the gov results webpage
driver.get('https://results.elections.maryland.gov/elections/2022/general_results/gen_results_2022_1.html')

# Wait a few seconds for load
WebDriverWait(driver, 20)


# find element
results = driver.find_elements(by=By.CSS_SELECTOR, value="#primary_right_col")



# In[97]:


# create empty array to store data for first gov candidate
data = []

for result in results:
    #find the headline from the alert
    name = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[2]/td[1]").text
    #find the description from the alert
    votes = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[2]/td[7]").text
    # append dict to array
    data.append({"name" : name, "total-votes" : votes})


# In[98]:


# create empty array to store data for second gov candidate
data2 = []

for result in results:
    #find the headline from the alert
    name = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[3]/td[1]").text
    #find the description from the alert
    votes = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[3]/td[7]").text
    # append dict to array
    data2.append({"name" : name, "total-votes" : votes})


# In[99]:


# create empty array to store data for 3rd gov candidate
data3 = []

for result in results:
    #find the headline from the alert
    name = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[4]/td[1]").text
    #find the description from the alert
    votes = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[4]/td[7]").text
    # append dict to array
    data3.append({"name" : name, "total-votes" : votes})


# In[100]:


# create empty array to store data for 4th gov candidate
data4 = []

for result in results:
    #find the headline from the alert
    name = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[5]/td[1]").text
    #find the description from the alert
    votes = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[5]/td[7]").text
    # append dict to array
    data4.append({"name" : name, "total-votes" : votes})


# In[101]:


# create empty array to store data for 5th gov candidate
data5 = []

for result in results:
    #find the headline from the alert
    name = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[6]/td[1]").text
    #find the description from the alert
    votes = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[6]/td[7]").text
    # append dict to array
    data5.append({"name" : name, "total-votes" : votes})


# In[102]:


# create empty array to store data for 6th gov candidate
data6 = []

for result in results:
    #find the headline from the alert
    name = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[7]/td[1]").text
    #find the description from the alert
    votes = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[7]/td[7]").text
    # append dict to array
    data6.append({"name" : name, "total-votes" : votes})


# In[103]:


# create empty array to store data for 7th gov candidate
data7 = []

for result in results:
    #find the headline from the alert
    name = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[8]/td[1]").text
    #find the description from the alert
    votes = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[8]/td[7]").text
    # append dict to array
    data7.append({"name" : name, "total-votes" : votes})


# In[104]:


# close driver 
driver.quit()

# save to pandas dataframe for first candidate
df = pd.DataFrame(data)
print(df)

# for second candidate
df2 = pd.DataFrame(data2)
print(df2)

# for 3rd candidate
df3 = pd.DataFrame(data3)
print(df3)

# for 4th candidate
df4 = pd.DataFrame(data4)
print(df4)

# for 5th candidate
df5 = pd.DataFrame(data5)
print(df5)

# for 6th candidate
df6 = pd.DataFrame(data6)
print(df6)

# for 7th candidate
df7 = pd.DataFrame(data7)
print(df7)


# In[105]:


# write first candidate to csv
df.to_csv('csv-results/gov-results2022.csv')

# append second candidate to csv
df2.to_csv('csv-results/gov-results2022.csv', mode='a', header=False)

# append 3rd candidate to csv
df3.to_csv('csv-results/gov-results2022.csv', mode='a', header=False)

# append 4th candidate to csv
df4.to_csv('csv-results/gov-results2022.csv', mode='a', header=False)

# append 5th candidate to csv
df5.to_csv('csv-results/gov-results2022.csv', mode='a', header=False)

# append 6th candidate to csv
df6.to_csv('csv-results/gov-results2022.csv', mode='a', header=False)

# append 7th candidate to csv
df7.to_csv('csv-results/gov-results2022.csv', mode='a', header=False)


# In[106]:


#####################
#COMPTROLLER RACE
#####################


#call the webdriver browser

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)


#open the gov results webpage
driver.get('https://results.elections.maryland.gov/elections/2022/general_results/gen_results_2022_2.html')

# Wait a few seconds for load
WebDriverWait(driver, 20)


# find element
results = driver.find_elements(by=By.CSS_SELECTOR, value="#primary_right_col")


# In[107]:


# create empty array to store data for first comptroller candidate
dataComp = []

for result in results:
    #find the headline from the alert
    name = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[2]/td[1]").text
    #find the description from the alert
    votes = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[2]/td[7]").text
    # append dict to array
    dataComp.append({"name" : name, "total-votes" : votes})


# In[108]:


# create empty array to store data for 2nd comptroller candidate
dataComp2 = []

for result in results:
    #find the headline from the alert
    name = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[3]/td[1]").text
    #find the description from the alert
    votes = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[3]/td[7]").text
    # append dict to array
    dataComp2.append({"name" : name, "total-votes" : votes})


# In[109]:


# create empty array to store data for 3rd comptroller candidate
dataComp3 = []

for result in results:
    #find the headline from the alert
    name = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[4]/td[1]").text
    #find the description from the alert
    votes = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[4]/td[7]").text
    # append dict to array
    dataComp3.append({"name" : name, "total-votes" : votes})


# In[110]:


# close driver 
driver.quit()

# save to pandas dataframe for first candidate
dfComp1 = pd.DataFrame(dataComp)
print(dfComp1)

# for second candidate
dfComp2 = pd.DataFrame(dataComp2)
print(dfComp2)

# for 3rd candidate
dfComp3 = pd.DataFrame(dataComp3)
print(dfComp3)


# In[111]:


# write first candidate to csv
dfComp1.to_csv('csv-results/comp-results2022.csv')

# append second candidate to csv
dfComp2.to_csv('csv-results/comp-results2022.csv', mode='a', header=False)

# append 3rd candidate to csv
dfComp3.to_csv('csv-results/comp-results2022.csv', mode='a', header=False)


# In[112]:


#####################
#AG RACE
#####################


#call the webdriver browser

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)


#open the gov results webpage
driver.get('https://results.elections.maryland.gov/elections/2022/general_results/gen_results_2022_3.html')

# Wait a few seconds for load
WebDriverWait(driver, 20)


# find element
results = driver.find_elements(by=By.CSS_SELECTOR, value="#primary_right_col")


# In[113]:


# create empty array to store data for first AG candidate
dataAG = []

for result in results:
    #find the headline from the alert
    name = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[2]/td[1]").text
    #find the description from the alert
    votes = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[2]/td[7]").text
    # append dict to array
    dataAG.append({"name" : name, "total-votes" : votes})


# In[114]:


# create empty array to store data for 2nd AG candidate
dataAG2 = []

for result in results:
    #find the headline from the alert
    name = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[3]/td[1]").text
    #find the description from the alert
    votes = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[3]/td[7]").text
    # append dict to array
    dataAG2.append({"name" : name, "total-votes" : votes})


# In[115]:


# create empty array to store data for 3rd AG candidate
dataAG3 = []

for result in results:
    #find the headline from the alert
    name = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[4]/td[1]").text
    #find the description from the alert
    votes = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[4]/td[7]").text
    # append dict to array
    dataAG3.append({"name" : name, "total-votes" : votes})


# In[116]:


# close driver 
driver.quit()

# save to pandas dataframe for first candidate
dfAG1 = pd.DataFrame(dataAG)
print(dfAG1)

# for second candidate
dfAG2 = pd.DataFrame(dataAG2)
print(dfAG2)

# for 3rd candidate
dfAG3 = pd.DataFrame(dataAG3)
print(dfAG3)


# In[117]:


# write first candidate to csv
dfAG1.to_csv('csv-results/ag-results2022.csv')

# append second candidate to csv
dfAG2.to_csv('csv-results/ag-results2022.csv', mode='a', header=False)

# append 3rd candidate to csv
dfAG3.to_csv('csv-results/ag-results2022.csv', mode='a', header=False)


# In[118]:


#####################
#SENATE
#####################


#call the webdriver browser

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)


#open the gov results webpage
driver.get('https://results.elections.maryland.gov/elections/2022/general_results/gen_results_2022_4.html')

# Wait a few seconds for load
WebDriverWait(driver, 20)


# find element
results = driver.find_elements(by=By.CSS_SELECTOR, value="#primary_right_col")


# In[119]:


# create empty array to store data for first senate candidate
dataSen = []

for result in results:
    #find the headline from the alert
    name = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[2]/td[1]").text
    #find the description from the alert
    votes = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[2]/td[7]").text
    # append dict to array
    dataSen.append({"name" : name, "total-votes" : votes})


# In[120]:


# create empty array to store data for 2nd senate candidate
dataSen2 = []

for result in results:
    #find the headline from the alert
    name = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[3]/td[1]").text
    #find the description from the alert
    votes = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[3]/td[7]").text
    # append dict to array
    dataSen2.append({"name" : name, "total-votes" : votes})


# In[121]:


# create empty array to store data for 3rd senate candidate
dataSen3 = []

for result in results:
    #find the headline from the alert
    name = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[4]/td[1]").text
    #find the description from the alert
    votes = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[4]/td[7]").text
    # append dict to array
    dataSen3.append({"name" : name, "total-votes" : votes})


# In[122]:


# create empty array to store data for 4th senate candidate
dataSen4 = []

for result in results:
    #find the headline from the alert
    name = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[5]/td[1]").text
    #find the description from the alert
    votes = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[5]/td[7]").text
    # append dict to array
    dataSen4.append({"name" : name, "total-votes" : votes})


# In[123]:


# create empty array to store data for 5th senate candidate
dataSen5 = []

for result in results:
    #find the headline from the alert
    name = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[6]/td[1]").text
    #find the description from the alert
    votes = result.find_element(By.XPATH, "/html/body/div/div[2]/div[4]/div/div[2]/div/div[8]/table/tbody/tr[6]/td[7]").text
    # append dict to array
    dataSen5.append({"name" : name, "total-votes" : votes})


# In[124]:


# close driver 
driver.quit()

# save to pandas dataframe for first candidate
dfSen1 = pd.DataFrame(dataSen)
print(dfSen1)

# for second candidate
dfSen2 = pd.DataFrame(dataSen2)
print(dfSen2)

# for 3rd candidate
dfSen3 = pd.DataFrame(dataSen3)
print(dfSen3)

# for 4th candidate
dfSen4 = pd.DataFrame(dataSen4)
print(dfSen4)

# for 5th candidate
dfSen5 = pd.DataFrame(dataSen5)
print(dfSen5)


# In[125]:


# write first candidate to csv
dfSen1.to_csv('csv-results/sen-results2022.csv')

# append second candidate to csv
dfSen2.to_csv('csv-results/sen-results2022.csv', mode='a', header=False)

# append 3rd candidate to csv
dfSen3.to_csv('csv-results/sen-results2022.csv', mode='a', header=False)

# append 4th candidate to csv
dfSen4.to_csv('csv-results/sen-results2022.csv', mode='a', header=False)

# append 5th candidate to csv
dfSen5.to_csv('csv-results/sen-results2022.csv', mode='a', header=False)


# In[ ]:




