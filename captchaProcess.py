from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import ddddocr




def captchaCrack(driver: webdriver) -> str:
    ocr = ddddocr.DdddOcr() 
    wait = WebDriverWait(driver, 10)
    # 找驗證碼圖片
    captcha_image = driver.find_element(By.ID, 'CAPTCHAImage')
    captcha_image.screenshot('code.png')
    with open("code.png", "rb") as fp:
        image = fp.read()
    return ocr.classification(image)
    '''
    # 截圖存成PIL的Image
    img = Image.open(io.BytesIO(captcha_image.screenshot_as_png))
    # 灰階處理
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    # 雜訊處理
    noise = np.random.normal(0, 15, threshold.shape)
    noise = np.clip(threshold +noise, 0, 255).astype('uint8')
    guassian = cv2.blur(noise, (3, 3))
    # 最後存回 PIL Image
    img = Image.fromarray(guassian)
    # 回傳辨識結果
    return ocr.classification(img)
    '''
