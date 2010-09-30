from selenium.remote import connect
from selenium import FIREFOX
from selenium.common.exceptions import NoSuchElementException
from time import sleep

def test_open_google():
    browser = connect(FIREFOX) # Get local session of firefox
    browser.get("http://www.google.com/") # Load page
    assert browser.get_title() == "Google"
    print browser.get_cookies()
    elem = browser.find_element_by_name("q") # Find the query box
    elem.send_keys("teste 123\n")
    sleep(0.2) # Let the page load, will be added to the API
#     try:
#         browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
#     except NoSuchElementException:
#         assert 0, "can't find seleniumhq"
    browser.close()
