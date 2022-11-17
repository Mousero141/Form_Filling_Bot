import time
from selenium import webdriver
import pandas as pd


df = pd.read_excel('C:\\webdrivers\\Data.xlsx')
print(df.iloc[0])

PATH = "C:\\webdrivers\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get('https://230914.9e.cz/form.php')

driver.implicitly_wait(5)

for index in df.index:
    entry = df.loc[index]

    time.sleep(3)
    name_input = driver.find_element_by_name('fjmeno')
    name_input.send_keys(entry['Name'])

    time.sleep(3)

    email_input = driver.find_element_by_name('fpredmet')
    email_input.send_keys(entry['Subject'])

    time.sleep(3)

    temp = entry['Grades']
    grades_input = driver.find_element_by_name('fprumer')
    grades_input.send_keys(int(temp))

    time.sleep(3)

    temp = entry['Date1']
    date_input = driver.find_element_by_name('fdatum')
    date_input.send_keys(temp.strftime("%d/%m/%Y"))

    time.sleep(3)

    submit_btn = driver.find_element_by_name('submit')
    submit_btn.click()

    time.sleep(3)
    refresh_btn = driver.find_element_by_partial_link_text("Zpět")
    refresh_btn.click()

time.sleep(5)
driver.close()