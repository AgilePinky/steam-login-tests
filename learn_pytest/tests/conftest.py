import pytest
from tests.driver_singleton import Driver

@pytest.fixture(scope="function")
def driver():
    driver = Driver()
    yield driver
    Driver.quit()