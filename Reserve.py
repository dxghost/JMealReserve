from selenium import webdriver
import pytesseract
from PIL import Image
import os
#import Captcha
import time
'''
food_list = ["خوراک کتلت","کوکو سیب زمینی","چلو شنیستل مرغ","شوید پلو با گوشت","استانبولی پلو","کوکو سبزی","چلو کنسرو ماهی تن","کوفته","زرشک پلو با مرغ","کشک بادمجان","جوجه کباب","چلو کباب کوبیده","ماکارونی","سبزی پلو با ماهی","لوبیا پلو","ماهی کبابی","چلو خورش قیمه بادمجان","عدس پلو"]
print("food list : ")
for food in food_list:
    print(food)

print("choose your favourite foods : ")
favourites = []
for i in range(10):
    favourite_foods = input("Enter your food")
    favourites.append(favourite_foods)'''

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
driver = webdriver.Chrome()
driver.set_window_size(1024, 720)
driver.get("http://stu.iust.ac.ir")

Username = driver.find_element_by_name("j_username")
Username.clear()
Username.send_keys('96521128')

Password = driver.find_element_by_name("j_password")
Password.clear()
Password.send_keys("0022028900")

driver.get_screenshot_as_file('tmp.png')
img = Image.open('tmp.png')
img = img.crop((746, 245, 802, 276))
CaptchaText = pytesseract.image_to_string(img)

os.remove('tmp.png')
CaptchaInput = driver.find_element_by_name("captcha_input")
CaptchaInput.clear()
CaptchaInput.send_keys(CaptchaText)

submit = driver.find_element_by_id('login_btn_submit')
submit.click()

reserveKey = driver.find_element_by_class_name('icon_home')
reserveKey.click()

nextWeekButton = driver.find_element_by_id('nextWeekBtn')
nextWeekButton.click()

foods = {}
for i in range(15):
    try:
        foods[i] = (driver.find_element_by_id('foodNameSpan' + str(i)).text,
                    driver.find_element_by_id('userWeekReserves.selected' + str(i)))
    except:
        break

favourites = ['كوفته', 'استانبولی', 'شنیستل مرغ', 'شویدپلو', 'قیمه', 'کباب کوبیده', 'ماهی تن', 'کوکوسبزی']

foods1 = {}
for i in range(0, 8, 2):
    foods1[i] = []
    for j in range(2):
        foods1[i].append(foods[i + j])

for key in foods1.keys():
    flag = False
    for food in favourites:
        print(food)
        if flag:
            break
        for choice in foods1[key]:
            if flag:
                break
            print(food in choice[0])
            if food in choice[0]:
                time.sleep(1)
                choice[1].click()
                flag = True
                break

doReservBtn = driver.find_element_by_id('doReservBtn')
doReservBtn.click()

driver.get('http://stu.iust.ac.ir/accessMgmt/action/logout.rose')
driver.close()
