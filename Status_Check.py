#!/usr/bin/env python
# coding: utf-8

# In[9]:


from selenium import webdriver
from selenium.webdriver.common.by import By

universities = [
    {
        "name": "ASU",
        "link": 'https://webapp4.asu.edu/myasu/',
        "username_path": '//*[@id="username"]',
        "username": 'YOUR-USERNAME',
        "password_path": '//*[@id="password"]',
        "password": 'YOUR-PASSWORD',
        "button_path": '//*[@id="login"]/section[2]/div[1]/input',
        "to_print": ['//*[@id="app-drawer-container-1"]/div/div/div/div/div[2]', '//*[@id="my-tasks-box"]/div']
    },
    {
        "name": "Buffalo",
        "link": 'https://ubseasconnect.buffalo.edu/account/login?r=https%3a%2f%2fubseasconnect.buffalo.edu%2fapply%2ffrm%3ff453c1c3-fa30-459d-9acb-9b540c975a39',
        "username_path": '//*[@id="email"]',
        "username": 'YOUR-USERNAME',
        "password_path": '//*[@id="password"]',
        "password": 'YOUR-PASSWORD',
        "button_path": '//*[@id="content"]/form/table/tbody/tr/td[1]/div/button',
        "to_print": ['//*[@id="part_979bffaf-dfc5-4dd5-b7d6-7a5460265f55"]/span']
    },
    {
        "name": "San Jose",
        "link": 'https://calstate.liaisoncas.com/applicant-ux/#/login',
        "username_path": '//*[@id="cas-login-field-username"]',
        "username": 'YOUR-USERNAME',
        "password_path": '//*[@id="cas-login-field-password"]',
        "password": 'YOUR-PASSWORD',
        "button_path": '//*[@id="cas-content-wrapper"]/div/div[3]/div[2]/form/button',
        "to_print": ['//*[@id="cas-content-wrapper"]/section/div[1]/header/p']
    },
    {
        "name": "NorthEastern",
        "link": 'https://enroll.northeastern.edu/account/login?r=https%3a%2f%2fenroll.northeastern.edu%2fapply%2ffrm%3f41abe722-a6b1-47b5-9b3d-ae68bfc86b93',
        "username_path": '//*[@id="email"]',
        "username": 'YOUR-USERNAME',
        "password_path": '//*[@id="password"]',
        "password": 'YOUR-PASSWORD',
        "button_path": '//*[@id="content"]/form/table/tbody/tr/td[1]/div/button',
        "to_print": ['//*[@id="appdetails"]/li[6]']
    },
    {
        "name": "Stony Brook",
        "link": 'https://graduateadmissions.stonybrook.edu/account/login?r=https%3a%2f%2fgraduateadmissions.stonybrook.edu%2fapply%2ffrm%3f51637bcf-92c3-47dd-8670-ebc294e98402',
        "username_path": '//*[@id="email"]',
        "username": 'YOUR-USERNAME',
        "password_path": '//*[@id="password"]',
        "password": 'YOUR-PASSWORD',
        "button_path": '//*[@id="content"]/form/table/tbody/tr/td[1]/div/button',
        "to_print": ['//*[@id="part_1e32e933-d355-46a8-bd96-4b140b429298"]/h3/span']
    }
]



# In[10]:


def getInfo(universities):
    browser = webdriver.Chrome()
    for i in universities:
        print(i['name'], ':')
        try:
            browser.get(i['link'])
            browser.find_element(By.XPATH, i['username_path']).send_keys(i['username'])
            browser.find_element(By.XPATH, i['password_path']).send_keys(i['password'])
            browser.find_element(By.XPATH, i['button_path']).click()
            browser.implicitly_wait(5)
            for r in i['to_print']:
                print((browser.find_element(By.XPATH, r).text))
        except:
            print('Something unholy happened!')
                
        print('\n\n')
    
    
    
getInfo(universities)


# In[ ]:




