from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "/home/ed/Documents/python/chromedriver" # location of the webdriver - amend as requried

url = "https://ebn.eu/?p=members"

driver = webdriver.Chrome(PATH)
driver.get(url)

member_list = []

# Flow to open page and click on link to extract href

members = driver.find_elements_by_xpath('//*[@class="projectImageOuter"]') # Looking for the required class - the image which on click bring up the info


for member in members:
    print(member.text) # to see that loop went to next iteration
    member.find_element_by_xpath('//*[@class="projectImage"]').click()
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'VIEW FULL PROFILE')))
    links = driver.find_element_by_partial_link_text("VIEW FULL PROFILE")
    href = links.get_attribute("href")
    member_list.append(href)
    member.find_element_by_xpath("/html/body/div[5]/div[1]/button").click()

    print(member_list)
driver.quit()
