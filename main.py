from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from captchaProcess import captchaCrack
# Set the path to your webdriver (e.g., chromedriver.exe)
webdriver_path = 'chromedriver.exe'

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()





while True:
    url = 'https://game.mnd.gov.tw/gameplay.aspx'
    driver.get(url)
    while True:
        
            # 找到Ans1到Ans4按钮
        try:
            buttons = driver.find_elements(
                By.XPATH, "//button[starts-with(@id, 'Ans')]")
            # 随机点击一个按钮
            random.choice(buttons).click()

            # 等待页面加载完成
            time.sleep(5)
        except:
            print('break')
            break
        try:
            img_back_element = driver.find_element("xpath",'//*[@id="imgBack"]')
            #print(img_back_element)
            # 检查元素是否存在
            if img_back_element:
                #print('backBtnclick')
                img_back_element.click()
        except:
            pass

    password_input = driver.find_element(By.XPATH, '//input[@name="PID" and @type="password"]')
    password_input.clear()  # 清空输入框内容
    password_input.send_keys("F130740737")

    # Captcha
    res = captchaCrack(driver)
    captcha_input = driver.find_element(By.XPATH, '//input[@name="txtValidateCode" and @type="text"]')
    captcha_input.send_keys(res)
    submit_button = driver.find_element(By.XPATH, '//input[@type="submit" and @name="ImgBtn"]')
    submit_button.click()
    time.sleep(3)
# Close the browser window
driver.quit()
