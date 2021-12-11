from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

ser = Service("/Users/ashique/projects/python/selenium/chromedriver")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.get(
    "https://bmvs.onlineappointmentscheduling.net.au/oasis/ModifyAppointment2.aspx"
)

elem = driver.find_element(by=By.ID, value="ContentPlaceHolder1_txtHAPID")
elem.clear()
elem.send_keys("26696764")

first_name = driver.find_element(by=By.ID, value="ContentPlaceHolder1_txtFirstName")
first_name.clear()
first_name.send_keys("Sajani")

last_name = driver.find_element(by=By.ID, value="ContentPlaceHolder1_txtSurname")
last_name.clear()
last_name.send_keys("Narayanankutty")

dob = driver.find_element(by=By.ID, value="ContentPlaceHolder1_txtDOB")
dob.clear()
dob.send_keys("3/03/1993")

elem.send_keys(Keys.RETURN)

modify_dates = driver.find_element(
    by=By.ID, value="ContentPlaceHolder1_repAppointments_lnkChangeAppointment_0"
)

modify_dates.send_keys(Keys.RETURN)

flag = True
while flag:
    next_page = driver.find_element(by=By.ID, value="ContentPlaceHolder1_btnCont")
    next_page.send_keys(Keys.RETURN)

    data_selector = driver.find_element(
        by=By.ID, value="ContentPlaceHolder1_SelectTime1_txtAppDate"
    )

    time.sleep(0.5)

    date = data_selector.get_property("value")
    print(date)
    month = date.split("/")[1]
    day = date.split("/")[0]
    year = date.split("/")[2]

    if int(month) == 12 and int(year) == 2021 and int(day) < 19:
        flag = False
        print("Click Fast!!!!")
    else:
        elem = driver.find_element(
            by=By.XPATH,
            value='//*[@id="form1"]/div[3]/div[2]/div/div[2]/div[7]/button[2]',
        )

        # scroll down functionality
        # elem2 = driver.find_element(by=By.ID,value='ContentPlaceHolder1_SelectTime1_rblResults')
        # # identify element
        # driver.execute_script("arguments[0].scrollIntoView(true);",elem2)
        elem.click()
        time.sleep(0.5)






