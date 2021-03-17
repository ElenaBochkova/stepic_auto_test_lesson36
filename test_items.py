import pytest
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def element_is_present(browser, classname):
    try:
        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, classname))
        )
    except TimeoutException:
        return False
    return True

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"]
                         )
def test_add_button_is_present(browser, link):
    browser.get(link)
    assert element_is_present(browser, "btn-add-to-basket") == True, "There is no your button"