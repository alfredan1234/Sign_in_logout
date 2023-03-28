import time

from pytest import fail


class NoSuchElementException(Exception):
    fail


def isElement(self, elementWay):
    '''
    Determine whether elements exist
    Usage:
    isElement(By.XPATH,"//a")
    '''
    time.sleep(1)
    try:
        self.find_element_by_id(elementWay)
        # self.driver.implicitly_wait(60)
        print("network is offline")
        # elif identifyBy == "xpath":
        #     # self.driver.implicitly_wait(60)
        #     self.find_element_by_xpath(elementWay)
        # elif identifyBy == "class":
        #     self.find_element_by_class_name(elementWay)
        #
        # elif identifyBy == "name":
        #     self.find_element_by_name(elementWay)
        # elif identifyBy == "tag name":
        #     self.driver.find_element_by_tag_name(c)
        # elif identifyBy == "css selector":
        #     self.driver.find_element_by_css_selector(c)
        # print("network is offline")
    except NoSuchElementException as e:
        print(e)
