# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time
import pytest
import allure
import json

# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
from scripts import sign_in_page
from appium import webdriver

caps = json.load(open('settings.json'))
print(caps)
class TestDemo:
    @allure.story("story one")
    @allure.title("Title_one")
    def test_a(self):
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # driver.implicitly_wait(10)
        # WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.ID, "com.fisher_price.android:id/tv_account_ques")))
        # wait = WebDriverWait(driver, 10, 1)
        # wait.until(lambda driver:driver.find_element_by_id('com.fisher_price.android:id/tv_account_ques'))
        with allure.step('正在启动smart connect app'):
            print("\n正在启动smart connect app")
            time.sleep(10)
        # WebDriverWait(driver, 10, 1).until(lambda driver: driver.find_element_by_id("com.fisher_price.android:id/tv_account_ques"))
        signIn = driver.find_element_by_id("com.fisher_price.android:id/tvSignIn")
        signIn.click()
        driver.implicitly_wait(10)
        with allure.step("正在进入登陆页面..."):
            print("正在进入登陆页面...")
            # driver.implicitly_wait(10)
            # time.sleep(10)
        sign_in_page.isSignIn(driver)
        print("输入用户名")
        # email = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[3]/android.view.View[1]/android.widget.EditText")
        email = driver.find_element_by_xpath("//android.widget.EditText[@text='邮箱地址']")
        # //input[@name="phone" and @datatype="m"]
        email.click()
        email.send_keys('zxcv@qq.com')
        time.sleep(3)
        # driver.find_element_by_android_uiautomator('new UiSelector().text("登录Mattel Login")')
        # self.driver.implicitly_wait(60)
        # print("Enter Sign In page successfully!")
        # prompt = 'com.fisher_price.android:id/tvErrorTitle'
        # offline_exception.isSignIn(driver)
        driver.quit()
        time.sleep(3)


if __name__ == "__main__":
    # result_dir = "../report/Json"
    pytest.main(['-x', 'smart_connect_1.py'])
    # pytest.main(["-vs", '--alluredir', './report', 'smart_connect_1.py'])
    # pytest.main(["-sv", "--alluredir="%result_dir, "smart_connect_1.py"])
    # time.sleep(5)
# if ret:
#     print("生成测试报告失败")
# else:
#     print("生成测试报告成功")
