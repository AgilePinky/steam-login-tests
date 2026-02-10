from selenium import webdriver

class Driver:
    _instance = None
    _driver = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Driver, cls).__new__(cls)
        return cls._instance

    def get_driver(self):
        if self._driver is None:
            self._driver = webdriver.Chrome()
        return self._driver

    def restart(self):
        if self._driver:
            self._driver.quit()
        self._driver = webdriver.Chrome()

    def quit(self):
        if self._driver:
            self._driver.quit()
            self._driver = None



