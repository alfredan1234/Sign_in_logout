# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time
import json
import pytest
import allure
import os
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from scripts import sign_in_page

class TestDemo_1:
#     @allure.story("sign in and then sign out")
#     @allure.title("Title_one")
    def test_a(self):
        caps = json.load(open('settings.json'))
        print(caps)
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # with allure.step('正在启动smart connect app'):
        print("正在启动smart connect app")
        time.sleep(10)
        signIn = driver.find_element_by_id("com.fisher_price.android:id/tvSignIn")
        signIn.click()
        print("正在进入登陆页面...")
        time.sleep(10)
        sign_in_page.isSignIn(driver)
        print("正在输入用户名")
        email = driver.find_element_by_xpath("//android.widget.EditText[@text='邮箱地址']")
        email.click()
        email.send_keys('zxcv@qq.com')
        time.sleep(3)
        closeKeyboard = driver.find_element_by_xpath("//android.widget.Image[contains(@index,1)]")
        closeKeyboard.click()
        time.sleep(3)
        print("正在输入密码")
        password = driver.find_element_by_xpath("//android.widget.EditText[@text='密码']")
        password.click()
        password.send_keys("password")
        closeKeyboard.click()
        time.sleep(3)
        print("正在登陆账号...")
        loginButton = driver.find_element_by_xpath("//android.widget.Button[@text='下一步']")
        loginButton.click()
        time.sleep(10)
        print("进入Account Settings页面")
        settings = driver.find_element_by_xpath('//android.widget.TextView[@content-desc="设置"]')
        settings.click()
        time.sleep(3)
        print("滑动页面以找到logout 按钮")
        TouchAction(driver).press(x=508, y=1183).move_to(x=513, y=753).release().perform()
        TouchAction(driver).press(x=508, y=1183).move_to(x=513, y=753).release().perform()
        time.sleep(3)
        print("正在退出账号...")
        logoutButton = driver.find_element_by_id("com.fisher_price.android:id/logout")
        logoutButton.click()
        time.sleep(3)
        confirmButton = driver.find_element_by_id("com.fisher_price.android:id/ok")
        confirmButton.click()
        print("测试用例运行正确")
        time.sleep(5)
        driver.quit()
if __name__ == "__main__":
    # pytest.main(['sign_in_logout.py'])
    pytest.main(['-s', '-q', '--alluredir', './report/allure'])
    time.sleep(5)
# os.system("allure generate ../report/Json -o ../report/html --clean")