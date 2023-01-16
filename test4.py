from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('/Users/fdn-hengky/Learn/001 - Open Browser/chromedriver') 

driver.get("https://www.jakartanotebook.com/p/taffstudio-wireless-uhf-call-center-mic-with-transmitter-hx-w002-black")

judul = driver.find_element(by=By.XPATH, value=f"//h1[@class='bHQSTV']").text

print(judul)