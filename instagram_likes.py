from selenium import webdriver
import time

browser=webdriver.Chrome("C:\chromedriver.exe")
browser.get("https://www.instagram.com/")
time.sleep(4)

#login
Username=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
Username.send_keys("tanvi_rawle")
time.sleep(4)

Password=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
Password.send_keys("anatan1995")
Password.submit()
time.sleep(4)

# login=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button/div")
# login.click()
# time.sleep(2)

#NotNow
Notnow=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
Notnow.click()
time.sleep(3)

#Notification
Noti=browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
Noti.click()
time.sleep(3)

#Search
search=browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
search.send_keys("udnevus")
time.sleep(3)
name=browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[2]/div")
name.click()
time.sleep(3)

def likepic():
    time.sleep(2)
    pic=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[4]/article/div[1]/div/div[1]/div[1]/a/div/div[2]")
    pics=pic.find_elements_by_class_name("_9AhH0")

    for p in pics:
        p.click()
        time.sleep(4)
        like=browser.find_element_by_xpath("/html/body/div[6]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span/svg")
        like.click()
        exit=browser.find_element_by_xpath("/html/body/div[6]/div[3]/button/div/svg")
        time.sleep(2)
        exit.click()
    print(pics)

likepic()