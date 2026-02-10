from selenium import webdriver

class Driver:
    _driver = None

    def __new__(cls, *args, **kwargs):
        if not cls._driver:
            cls._driver = webdriver.Chrome()
        return cls._driver

    @classmethod
    def restart(cls):
        cls._driver.quit()
        cls._driver = webdriver.Chrome()

    @classmethod
    def quit(cls):
        if cls._driver:
            cls._driver.quit()
            cls._driver = None



