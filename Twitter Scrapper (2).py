#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install selenium')
#You need to download the chrome driver at https://chromedriver.storage.googleapis.com/index.html?path=73.0.3683.20/


# In[123]:


import selenium
from selenium.webdriver.common.keys import Keys


# In[124]:


#Open a Browser
chrome_path = "C:/Users/phili/OneDrive/Desktop/chromedriver.exe"
driver = webdriver.Chrome(chrome_path)


# In[125]:


#Go to Twitter
driver.get("http://www.twitter.com")
driver.find_element_by_xpath("""//*[@id="doc"]/div/div[1]/div[1]/div[2]/div[2]/div/a[2]""").click()


# In[126]:


#Log in to Twitter
userName = driver.find_element_by_class_name("js-username-field")
userName.send_keys("HealthAnalytic4")
passWord = driver.find_element_by_class_name("js-password-field")
passWord.send_keys("""%^TYGHBN56tyghbn""")

driver.find_element_by_xpath("""//*[@id="page-container"]/div/div[1]/form/div[2]/button""").click()


# In[127]:


#Type into search box using searchWord
searchWord = "Vaccines" #Change this to Scrape Different Word Searches
searchBox = driver.find_element_by_xpath("""//*[@id="search-query"]""")
searchBox.send_keys(searchWord)
searchBox.submit()

#View all
driver.find_element_by_xpath("""//*[@id="page-container"]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/h3/a""").click()


# In[128]:


#Scroll all the way down to collect more.
body = driver.find_element_by_xpath("""/html/body""")

for x in range(1000):
    body.send_keys(Keys.PAGE_DOWN)


# In[129]:


#Collect the tweets on page 1 of your searchWord...
tweets = driver.find_elements_by_class_name("js-tweet-text")
len(tweets)
#for tweet in tweets: #Prints all the tweets on page 1
    #print(tweet.text)
#print(tweets[1].text) #Prints the first tweet on the page


# In[162]:


file = open("Vaccines.txt", "w", encoding="utf-8")
for tweet in tweets:
    file.write(tweet.text)
    file.write("\n")
file.close()


# In[163]:


file = open("Vaccines.txt", "r", encoding="utf-8")


# In[164]:


for line in file:
    print (line)


# In[ ]:




