from enum import Enum
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)

def access_website(url:str)->None:
    try:
        driver.get(url)
    except Exception as e:
        print(f'Fail to access website(${url}) : ')
        print(e)

class Attribute(Enum):
    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"

def get_element(attribute:Attribute, value:str)-> object:
    try:
        target = driver.find_element(by=attribute.value,value=value)
        return target
    except Exception as e:
        print(f'Fail to find element(${value}):e')
        return None

def click_element(element:object):
    element.click()
