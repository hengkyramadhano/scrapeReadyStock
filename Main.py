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


service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def test_driver_manager_chrome():

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

    # Button Mengerti
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='headlessui-popover-panel-6']/div/div[2]/button"))).click()

    # -----------------------------------------------------------------------------------------------------------

    SKU_Store = {}
    copy_mylist = mylist.copy()
    carry = []

    bagi_bulat = len(mylist) // 100
    bagi_sisa = len(mylist) % 100

    # Berapa kali hit search per-100 SKU
    for item in range(bagi_bulat+1):

        for i in range(len(copy_mylist)):
            
            carry.append(copy_mylist[i])

            if (len(copy_mylist) == (i+1)):
                search_sku(carry, copy_mylist, SKU_Store)

                print("call Break")
                break

            if (i == 99):
                search_sku(carry, copy_mylist, SKU_Store)

                break

    return SKU_Store

def search_sku(carry, copy_mylist, SKU_Store) :
    # Enter SKU for 100 SKU
    # print(f"Isi dari SKU Field: {carry}")
    search_field = driver.find_element(by=By.NAME, value="key")
    search_field.clear()
    search_field.send_keys(f"{carry}")
    search_field.send_keys(Keys.RETURN)

    for item2 in carry:
        copy_mylist.remove(item2)
    
    carry.clear()

    driver.get(driver.current_url + "&show=100")

    total_sku = driver.find_elements(by=By.XPATH, value="//div[@class='product-list-wrapper']/div/div[1]")
    print(f"Total SKU result: {len(total_sku)}")

    for j in range(len(total_sku)):

        sku = driver.find_element(by=By.XPATH, value=f"//div[@class='product-list-wrapper']/div[{j+1}]/div[1]").get_attribute("textContent")
        # print(f"getSKU: {sku}")

        harga = driver.find_element(by=By.XPATH, value=f"//*[@class='product-list-wrapper']/div[{j+1}]/div[4]/div/*[@class='product-list__price']").text

        jakpus_stock = driver.find_element(by=By.XPATH, value=f"//*[@class='product-list-wrapper']/div[{j+1}]/div[4]/div[2]/div/div[2]/div[2]/span[1]").text
        jakut_stock = driver.find_element(by=By.XPATH, value=f"//*[@class='product-list-wrapper']/div[{j+1}]/div[4]/div[2]/div/div[4]/div[2]/span[1]").text
        tangerang_stock = driver.find_element(by=By.XPATH, value=f"//*[@class='product-list-wrapper']/div[{j+1}]/div[4]/div[2]/div/div[5]/div[2]/span[1]").text
        cikupa_stock = driver.find_element(by=By.XPATH, value=f"//*[@class='product-list-wrapper']/div[{j+1}]/div[4]/div[2]/div/div[6]/div[2]/span[1]").text


        store_dict = {
            "Harga" : harga.replace("Rp. ","").replace(".",""),
            "Jakarta Pusat" : jakpus_stock.replace("Tersedia","Aktif").replace("Habis","Nonaktif").replace("On Restock","Nonaktif"),
            "Jakarta Utara" : jakut_stock.replace("Tersedia","Aktif").replace("Habis","Nonaktif").replace("On Restock","Nonaktif"),
            "Tangerang" : tangerang_stock.replace("Tersedia","Aktif").replace("Habis","Nonaktif").replace("On Restock","Nonaktif"),
            "Cikupa" : cikupa_stock.replace("Tersedia","Aktif").replace("Habis","Nonaktif").replace("On Restock","Nonaktif")
        }

        SKU_Store[sku] = store_dict


        # print(f"Status dari Jakarta Pusat: {jakpus_stock}")


def convert_to_excel() :
    
    # convert into dataframe
    df = pd.DataFrame.from_dict(test_driver_manager_chrome(), orient='index')

    #convert into excel
    df.to_excel('data.xlsx')
    print("Dictionary converted into excel...")

    sleep(5)

    driver.quit()

convert_to_excel()