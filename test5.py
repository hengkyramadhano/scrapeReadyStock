from selenium import webdriver
from selenium.webdriver.common.by import By


# Initialize the web driver
driver = webdriver.Chrome('/Users/fdn-hengky/Learn/001 - Open Browser/chromedriver')

# Navigate to the website
driver.get("https://femaledaily.com/about")

# Find the specific p tag and get its text
p_tag = driver.find_elements(By.XPATH, '//p')
print(p_tag.text)

# Close the browser window
driver.quit()