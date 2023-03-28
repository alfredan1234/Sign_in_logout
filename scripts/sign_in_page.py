import time
from pytest import fail
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class isSignInException(Exception):
    fail


def isSignIn(self):
    '''
    Determine whether elements exist
    Usage:
    isElement(By.XPATH,"//a")
    '''
    # SignIn_id = ''
    time.sleep(1)

    # notSignIn_len = self.find_element_by_android_uiautomator('new UiSelector().text("糟糕")')
    try:
        # self.find_element_by_android_uiautomator('new UiSelector().text("登录Mattel Login")')
        #显示等待
        WebDriverWait(self, 10, 1).until(EC.presence_of_element_located((By.XPATH, "//android.view.View[@text='登录Mattel Login']")))
            # self.driver.implicitly_wait(60)
        print("Enter Sign In page successfully!")
            # self.save_screenshot('login.png')
    except isSignInException as e:
        print(e)
        self.save_screenshot('login.png')
        print("network is bad")
