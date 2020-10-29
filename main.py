#===========================
# Imports
#===========================

import time

from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options as FirefoxOptions

#===========================
# Main Script
#===========================

class App:
    # ==========================================
    def firefox_driver(self, driverpath):
        self.__browser = wd.Firefox(executable_path=driverpath)

    def chrome_driver(self, driverpath):
        self.__browser = wd.Chrome(executable_path=driverpath)

    def ie_driver(self, driverpath):
        self.__browser = wd.Ie(executable_path=driverpath)

    def safari_driver(self, driverpath):
        self.__browser = wd.Safari(executable_path=driverpath)

    def load_site(self, sitename):
        self.__browser.get(sitename)

    def headless_firefox_driver(self, driverpath):
        options = FirefoxOptions()
        options.add_argument('--headless')
        self.__browser = wd.Firefox(executable_path=driverpath, options=options)

    # ==========================================
    def show_site_title(self):
        return self.__browser.title

    def show_site_url(self):
        return self.__browser.current_url

    def show_site_content(self):
        return self.__browser.page_source

    def identify_open_window(self):
        return self.__browser.window_handles

    def close_browser(self):
        self.__browser.close()

    def maximize_browser(self):
        self.__browser.maximize_window()

    def delete_cookies(self):
        self.__browser.delete_all_cookies()

    def implicit_wait(self, time=0):
        self.__browser.implicitly_wait(time)

    # ==========================================
    def switch_window(self, name):
        self.__browser.switch_to_window(name)

    def primary_window(self):
        self.__browser.switch_to_default_content()

    # ==========================================
    def select_name(self, name):
        self.__selector = self.__browser.find_element_by_name(name)
        return self

    def select_all_name(self, name):
        self.__selector = self.__browser.find_elements_by_name(name)
        return self

    def select_tag_name(self, name):
        self.__selector = self.__browser.find_element_by_tag_name(name)
        return self

    def select_all_tag_name(self, name):
        self.__selector = self.__browser.find_elements_by_tag_name(name)
        return self

    def select_id(self, name):
        self.__selector = self.__browser.find_element_by_id(name)
        return self

    def select_all_id(self, name):
        self.__selector = self.__browser.find_elements_by_id(name)
        return self

    def select_class(self, name):
        self.__selector = self.__browser.find_element_by_class_name(name)
        return self

    def select_all_class(self, name):
        self.__selector = self.__browser.find_elements_by_class_name(name)
        return self

    def select_xpath(self, name):
        self.__selector = self.__browser.find_element_by_xpath(name)
        return self

    def select_link_text(self, name):
        self.__selector = self.__browser.find_element_by_link_text(name)
        return self

    def select_all_link_text(self, name):
        self.__selector = self.__browser.find_elements_by_link_text(name)
        return self

    def select_partial_link_text(self, name):
        self.__selector = self.__browser.find_element_by_partial_link_text(name)
        return self

    def select_all_partial_link_text(self, name):
        self.__selector = self.__browser.find_elements_by_partial_link_text(name)
        return self

    # ==========================================
    def text(self):
        return self.__selector.text

    def attribute_value(self, attribute):
        return self.__selector.get_attribute(attribute)

    def selector_location(self):
        return self.__selector.selector_location

    def is_selector_visible(self):
        return self.__selector.is_displayed()

    def is_input_enabled(self):
        return self.__selector.is_enabled()

    def is_inputbox_selected(self):
        return self.__selector.is_selected()

    def clear_text(self):
        self.__selector.clear()
        return self

    def set_text(self, text):
        self.__selector.send_keys(text)
        return self

    def press_button(self):
        self.__selector.click()
        return self

    def press_refresh_button(self):
        self.__browser.refresh()

    def press_close_button(self):
        self.__browser.quit()

    def press_back_button(self):
        self.__browser.back()

    def press_forward_button(self):
        self.__browser.forward()

    def press_returnkey(self):
        self.__selector.send_keys(Keys.RETURN)
        return self

    def press_enterkey(self):
        self.__selector.send_keys(Keys.ENTER)
        return self

    def press_deletekey(self):
        self.__selector.send_keys(Keys.DELETE)
        return self

    def press_backspacekey(self):
        self.__selector.send_keys(Keys.BACK_SPACE)
        return self

    def press_escapekey(self):
        self.__selector.send_keys(Keys.ESCAPE)
        return self

    def press_tabkey(self):
        self.__selector.send_keys(Keys.TAB)
        return self

    def press_up_arrowkey(self):
        self.__selector.send_keys(Keys.UP)
        return self

    def press_down_arrowkey(self):
        self.__selector.send_keys(Keys.DOWN)
        return self

    def press_left_arrowkey(self):
        self.__selector.send_keys(Keys.LEFT)
        return self

    def press_right_arrowkey(self):
        self.__selector.send_keys(Keys.RIGHT)
        return self

    def press_pagedownkey(self):
        self.__selector.send_keys(Keys.PAGE_DOWN)
        return self

    def press_pageupkey(self):
        self.__selector.send_keys(Keys.PAGE_UP)
        return self

    def press_homekey(self):
        self.__selector.send_keys(Keys.HOME)
        return self

    def press_endkey(self):
        self.__selector.send_keys(Keys.END)
        return self

    def press_f1key(self):
        self.__selector.send_keys(Keys.F1)
        return self

    def press_f2key(self):
        self.__selector.send_keys(Keys.F2)
        return self

    def press_f3key(self):
        self.__selector.send_keys(Keys.F3)
        return self

    def press_f4key(self):
        self.__selector.send_keys(Keys.F4)
        return self

    def press_f5key(self):
        self.__selector.send_keys(Keys.F5)
        return self

    def press_f6key(self):
        self.__selector.send_keys(Keys.F6)
        return self

    def press_f7key(self):
        self.__selector.send_keys(Keys.F7)
        return self

    def press_f8key(self):
        self.__selector.send_keys(Keys.F8)
        return self

    def press_f9key(self):
        self.__selector.send_keys(Keys.F9)
        return self

    def press_f10key(self):
        self.__selector.send_keys(Keys.F10)
        return self

    def press_f11key(self):
        self.__selector.send_keys(Keys.F11)
        return self

    def press_f12key(self):
        self.__selector.send_keys(Keys.F12)
        return self

#===========================
# Test Site
#===========================

def main():
    ## login to fb 1
    # email = 'mercado.joshua.web@gmail.com'
    # password = 'xxxxxxxxx'
    # a = App()
    # a.firefox_driver(r'C:\\Python\\Selenium\\Firefox\\geckodriver.exe')
    # a.maximize_browser()
    # a.load_site('https://www.facebook.com')

    # a.select_id('email').clear_text().set_text(email)
    # a.select_id('pass').clear_text().set_text(password)
    # a.press_returnkey()

    ## login to fb 2
    # email = 'mercado.joshua.web@gmail.com'
    # password = 'xxxxxxxxxxxxx'
    # b = App()
    # b.firefox_driver(r'C:\\Python\\Selenium\\Firefox\\geckodriver.exe')
    # b.maximize_browser()
    # b.load_site('https://www.facebook.com')

    # b.select_id('email').clear_text().set_text(email)
    # b.select_id('pass').clear_text().set_text(password)
    # b.select_name('login').press_button()

    # search something to google
    # c = App()
    # c.firefox_driver(r'C:\\Python\\Selenium\\Firefox\\geckodriver.exe')
    # c.maximize_browser()
    # c.load_site('https://www.google.com/')
    # c.select_name('q').clear_text().set_text('javatpoint').press_enterkey()

    ## login to gmail
    # email = 'mercado.joshua.web@gmail.com'
    # password = 'xxxxxxxxxxx'
    # d = App()
    # d.firefox_driver(r'C:\\Python\\Selenium\\Firefox\\geckodriver.exe')
    # d.delete_cookies()
    # d.maximize_browser()
    # d.load_site('https://www.gmail.com')

    # d.select_id('identifierId').clear_text().set_text(email)
    # d.select_xpath("//span[@class='RveJvd snByac'][1]").press_button()

    # d.select_name('password').clear_text().set_text(password)
    # d.select_xpath("//span[contains(text(),'Next')][1]").press_button()

    ## headless
    # e = App()
    # e.headless_firefox_driver(r'C:\\Python\\Selenium\\Firefox\\geckodriver.exe')
    # e.load_site('http://webcode.me')
    # print(e.show_site_title)
    # print(e.show_site_url)

    # print(e.show_site_content)

    # f = App()
    # f.firefox_driver(r'C:\\Python\\Selenium\\Firefox\\geckodriver.exe')
    # f.maximize_browser()

    # f.load_site('http://zetcode.com/python/logging/')
    # f.select_tag_name('html')
    # f.press_endkey()
    # f.press_homekey()
    pass

if __name__ == '__main__':
    main()