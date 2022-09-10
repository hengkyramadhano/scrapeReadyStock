import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from variables import mylist

def test_driver_manager_chrome():
    service = ChromeService(executable_path=ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service)

    driver.get("https://www.jakmall.com/")
    title = driver.title
    print(title + driver.current_url)
    driver.get("https://www.jakartanotebook.com/auth/login")

    imel = driver.find_element(by=By.NAME, value="username")
    imel.send_keys("hengkyramadhano@gmail.com")
    pwd = driver.find_element(by=By.NAME, value="password")
    pwd.send_keys("Jakarta48@")

    submit_button = driver.find_element(by=By.XPATH, value="//*[@id='__next']/div/div[2]/div[1]/div/div[2]/div/form/div[3]/button")
    submit_button.click()

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='headlessui-popover-panel-6']/div/div[2]/button"))).click()

    SKU_Store = {}

    for item in mylist:
        #do something with item
        search_field = driver.find_element(by=By.NAME, value="key")
        search_field.clear()
        search_field.send_keys(item)
        search_field.send_keys(Keys.RETURN)

        jakpus_stock = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[4]/div/div[1]/div/div[4]/div[2]/div/div[2]/div[2]/span"))).text
        jakut_stock = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[4]/div/div[1]/div/div[4]/div[2]/div/div[4]/div[2]/span"))).text
        tangerang_stock = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[4]/div/div[1]/div/div[4]/div[2]/div/div[5]/div[2]/span"))).text
        cikupa_stock = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[4]/div/div[1]/div/div[4]/div[2]/div/div[6]/div[2]/span"))).text

        store_dict = {
            "Jakarta Pusat" : jakpus_stock,
            "Jakarta Utara" : jakut_stock,
            "Tangerang" : tangerang_stock,
            "Cikupa" : cikupa_stock
        }

        SKU_Store[item] = store_dict


        print(f"Status dari Jakarta Pusat: {jakpus_stock}")



    print(SKU_Store)

    # convert into dataframe
    df = pd.DataFrame.from_dict(SKU_Store, orient='index')

    #convert into excel
    df.to_excel('data.xlsx')
    print("Dictionary converted into excel...")

    sleep(5)

    driver.quit()

test_driver_manager_chrome()

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }

# print(myfamily)


# driver.back()
# driver.forward()
# driver.refresh

# driver.quit() 