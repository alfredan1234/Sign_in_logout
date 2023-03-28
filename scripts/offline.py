def isElement(self, identifyBy,elementWay):
    '''
    Determine whether elements exist
    Usage:
    isElement(By.XPATH,"//a")
    '''
    time.sleep(1)
    try:
        if self.driver.find_elements(*a) == []:
        return False
        else:
        return True