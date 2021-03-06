from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import csv
import time

PATH = "/home/ed/Documents/python/chromedriver" # location of the webdriver - amend as requried

url = "https://ebn.eu/?p=members"

driver = webdriver.Chrome(PATH)
driver.get(url)

member_list = []

# Flow to open page and click on link to extract href

members = driver.find_elements_by_class_name("projectImage") # Looking for the required class - the image which on click bring up the info

for member in members:
    print(member.text) # to see that loop went to next iteration

#they have the onclick script which basically triggers the JS and renders the pop-up. You can make use of it. You can find the onclick script in the child element img. So your logic should be like (1)Get the child element (2)go to first child element (which is img always for your case) (3)Get the onclick script text (4)execute the script#
    
    # member.find_element_by_xpath('//*[@class="projectImage"]').click()
    child_elems = member.find_elements_by_css_selector("*") #Get the child elems
    onclick_script = child_elems[0].get_attribute('onclick')#Get the img's onclick value
    driver.execute_script(onclick_script)                   #Execute the JS
    time.sleep(1)                                           #Wait for some time
    
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'VIEW FULL PROFILE'))) #wait for the element to appear before moving on to avoid crash
    links = driver.find_element_by_partial_link_text("VIEW FULL PROFILE")
    href = links.get_attribute("href")
    member_list.append(href)
    member.find_element_by_xpath("/html/body/div[5]/div[1]/button").click()

driver.quit()

# Loop through the links to extract the sought information
df_list = []

for member in member_list:
    table = pd.read_html(member, index_col = None, header=None)
    df = table[0]
    df = df.T # Transposes the data
    df_list.append(df)
    print("ok " + member)

dfmaster = pd.concat(df_list, sort=False)
dfmaster = dfmaster.drop_duplicates()
dfmaster.to_csv('member_data.csv')
print(dfmaster)