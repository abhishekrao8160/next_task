import pandas as pd
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

Email=0
Password=1
Repeat_Password=2
driver = webdriver.Chrome(ChromeDriverManager().install())
data = pd.read_csv('data.csv', header=None)
def registration_form(row):
        driver.get("https://www.w3schools.com/howto/howto_css_register_form.asp")
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,"//input[@placeholder='Enter email']").send_keys(row[Email])
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").send_keys(row[Password])
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@placeholder='Repeat Password']").send_keys(row[Repeat_Password])
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[text()='Register']").click()
        time.sleep(2)

data.apply(registration_form, axis=1)

driver.quit()

