from selenium import webdriver
from PIL import Image
import os,sys
import pytesseract
username = ' '
password = ' '

driver = webdriver.Chrome()
driver.get(url='https://www.umjicanvas.com/login/openid_connect')
driver.maximize_window()
driver.find_elements_by_id('user')[0].send_keys(username)
driver.find_elements_by_id('pass')[0].send_keys(password)

driver.save_screenshot(r".\aa.png")
rangle = (1300,350,1400,380)#全屏条件下截图
i = Image.open(r".\aa.png")
frame4 = i.crop(rangle)
frame4.save(r".\frame8.png")
qq = Image.open(r".\frame8.png")
test = pytesseract.image_to_string(qq).strip()
driver.find_elements_by_id('captcha')[0].send_keys(test)
driver.find_elements_by_id('submit-button')[0].click()

os.remove(r".\frame8.png")
os.remove(r".\aa.png")
