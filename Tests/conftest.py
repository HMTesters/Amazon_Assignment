import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
import configparser
config = configparser.ConfigParser()
config.read("..//Utilities//input_properties")


@pytest.fixture(scope= "class")
def setUp(request):
    # service_obj = Service("C:\\Users\\Admin\\PycharmProjects\\pythonProject2\\Driver\\chromedriver.exe")
    request.cls.driver = webdriver.Chrome()
    request.cls.driver.get(config.get("Url","base_url"))
    # request.cls.driver.get('https://www.amazon.in/')
    request.cls.driver.maximize_window()
    request.cls.driver.implicitly_wait(20)
    yield
    request.cls.driver.quit()