from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("/Users/ashique/projects/python/selenium/chromedriver")
driver.get(
    "https://bmvs.onlineappointmentscheduling.net.au/oasis/ModifyAppointment2.aspx"
)

elem = driver.find_element_by_id("ContentPlaceHolder1_txtHAPID")
elem.clear()
elem.send_keys("26696764")

first_name = driver.find_element_by_id("ContentPlaceHolder1_txtFirstName")
first_name.clear()
first_name.send_keys("Sajani")

last_name = driver.find_element_by_id("ContentPlaceHolder1_txtSurname")
last_name.clear()
last_name.send_keys("Narayanankutty")

dob = driver.find_element_by_id("ContentPlaceHolder1_txtDOB")
dob.clear()
dob.send_keys("3/03/1993")

elem.send_keys(Keys.RETURN)

modify_dates = driver.find_element_by_id(
    "ContentPlaceHolder1_repAppointments_lnkChangeAppointment_0"
)

modify_dates.send_keys(Keys.RETURN)

flag = True
while flag:
    next_page = driver.find_element_by_id("ContentPlaceHolder1_btnCont")
    next_page.send_keys(Keys.RETURN)

    data_selector = driver.find_element_by_id(
        "ContentPlaceHolder1_SelectTime1_txtAppDate"
    )

    time.sleep(7)

    date = data_selector.get_property("value")
    print(date)
    month = date.split("/")[1]
    day = date.split("/")[0]
    year = date.split("/")[2]

    if int(month) < 4 and int(day) < 31 and int(year) <=2022:
        flag = False
    else:
        elem = driver.find_element_by_xpath(
            '//*[@id="form1"]/div[3]/div[2]/div/div[2]/div[7]/button[2]'
        )

        elem2 = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_SelectTime1_divSearchResults"]/div[1]/h2')
        # identify element
        driver.execute_script("arguments[0].scrollIntoView(true);",elem2)

        time.sleep(4)
        elem.click()
        time.sleep(5)
