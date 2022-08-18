from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from datetime import datetime

ser = Service("/Users/ashique/projects/python/selenium/chromedriver")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.get(
    "https://bmvs.onlineappointmentscheduling.net.au/oasis/ModifyAppointment2.aspx"
)

elem = driver.find_element(by=By.ID, value="ContentPlaceHolder1_txtHAPID")
elem.clear()
# Hap Id
elem.send_keys("XXXXXXXXXXX")

first_name = driver.find_element(by=By.ID, value="ContentPlaceHolder1_txtFirstName")
first_name.clear()
# First Name
first_name.send_keys("XXXXXXXXXXXX")

last_name = driver.find_element(by=By.ID, value="ContentPlaceHolder1_txtSurname")
last_name.clear()
# Last Name
last_name.send_keys("XXXXXXXX")

dob = driver.find_element(by=By.ID, value="ContentPlaceHolder1_txtDOB")
dob.clear()
# DOB in DD/MM/YYYY
dob.send_keys("XXXXXXXXXXXX")

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

    picker_date = datetime.strptime(date, "%d/%m/%Y")
    # Date of the last successful appointment
    last_appointment_date = datetime.strptime("10/05/2022", "%d/%m/%Y")
    current_date = datetime.now()

    if current_date < picker_date < last_appointment_date:
        # code will break out of loop when the picker date (date inside the ui) is between the current date and last recieved appointment date
        flag = False
        print("Click Fast!!!!")
        driver.get('https://www.youtube.com/watch?v=hT_nvWreIhg')
    else:
        elem = driver.find_element(
            by=By.XPATH,
            value='/html/body/form/div[3]/div[2]/div/div[2]/div[6]/button[2]',

        )

        # scroll down functionality
        # elem2 = driver.find_element(by=By.ID,value='ContentPlaceHolder1_SelectTime1_rblResults')
        # # identify element
        # driver.execute_script("arguments[0].scrollIntoView(true);",elem2)
        elem.click()
        time.sleep(0.5)
