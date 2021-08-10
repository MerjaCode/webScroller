from selenium import webdriver
import json
from time import sleep

print("Starting Web Scroller")

driver = webdriver.Chrome()
file = open("./urlList.json")
jsnFile = json.load(file)
url_List = [url for url in jsnFile["url_list"]]

driver.maximize_window() # maximize the browser window

# Open all urls in the json file

for i in range(len(url_List)):
    print(f"Window Index: {i}")
    driver.get(url_List[i])
    if i != len(url_List)-1:
        print("Opening a new window...")
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[-1])
    
# Custom code for each window

  # weather radar
driver.switch_to.window(driver.window_handles[1])
fullscreen_btn  = "/html/body/div/div[5]/div[1]/div[1]/div[1]/div[2]/div[2]"
zoom_btn        = "/html/body/div/div[5]/div[1]/div[1]/div[1]/div[2]/div[4]/div[3]/div[1]/div/button[1]"
play_btn        = "/html/body/div/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]"
driver.find_element_by_xpath(fullscreen_btn).click()
for i in range(6): driver.find_element_by_xpath(zoom_btn).click()
driver.find_element_by_xpath(play_btn).click()

  # Wheat prices 
driver.switch_to.window(driver.window_handles[2])
cookie_btn      = "//*[@id=\"pardotCookieButton\"]"
driver.find_element_by_xpath(cookie_btn).click()

  # Wheat graph
driver.switch_to.window(driver.window_handles[3])
driver.find_element_by_xpath(cookie_btn).click()

  # Farm weather station
driver.switch_to.window(driver.window_handles[4])
user_input      = "//*[@id=\"username\"]"
pass_input      = "//*[@id=\"password\"]"
login_btn       = "//*[@id=\"submit\"]"
uname           = "chuckmerja"
passwd          = "soilmoisture"
driver.find_element_by_xpath(user_input).send_keys(uname)
driver.find_element_by_xpath(pass_input).send_keys(passwd)
driver.find_element_by_xpath(login_btn).click()



# Cycle through tabs

wait_time = 15  # seconds
count = 1
refresh = False
while True:
    try:
        if count == 10:
            refresh = True 
            count = -1
        for i in range(len(url_List)):
            if refresh:
                driver.refresh()
            driver.switch_to.window(driver.window_handles[i])
            sleep(wait_time)
        count += 1
    except Exception as e:
        print(e)
        break

