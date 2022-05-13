from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\WebDriver\chromedriver.exe"
DELAY = 0.5

def ClickIDToNextPageAndPause(ID_to_click):
    toClick = driver.find_element_by_id(ID_to_click)
    toClick.click()
    time.sleep(DELAY)
    

print("Application Loading...")

driver = webdriver.Chrome(PATH)
driver.get("http://clonetexas.local/")

searchUserNameLogin = driver.find_element_by_id("user_login")
searchUserNameLogin.send_keys("Graham.Pearl@gmail.com")
searchUserPassword = driver.find_element_by_id("user_pass")
searchUserPassword.send_keys("12345")
searchUserButton = driver.find_element_by_id("wp-submit")
searchUserButton.click()

clickOrderList = [
    "menu-item-1486",
    "menu-item-1486",
    "gform_next_button_1_64",
    "gform_next_button_1_65",
    "gform_next_button_1_66",
    "gform_next_button_1_67",
    "gform_next_button_1_69",
    "gform_next_button_1_71",
    "gform_next_button_1_24",
    "gform_next_button_1_57",
    "gform_next_button_1_15",
    "gform_next_button_1_14",
    "gform_next_button_1_12",
    "gform_next_button_1_16",
    "gform_next_button_1_9",
    "gform_next_button_1_48",
    "gform_next_button_1_11",
    "gform_next_button_1_93",
    "gform_next_button_1_113",
    "gform_next_button_1_91",
    "gform_next_button_1_13",
    "gform_next_button_1_114",
    "gform_next_button_1_26",
    "gform_next_button_1_96",
    "gform_next_button_1_37",
    "gform_next_button_1_10",
    "gform_next_button_1_97"
    #"menu-item-2108"    
]

for item in clickOrderList:
    ClickIDToNextPageAndPause(item)

print("Application Closing...")
#driver.quit()