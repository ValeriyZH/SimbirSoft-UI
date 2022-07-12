import time
import requests
from loguru import logger
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class BasePage:

    def check_exists_by_xpath(self, xpath):
        try:
            self.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def assertElementsIsPresentByXpatch(self, xpath_elements):
        try:
            elements = self.find_elements_by_xpath(xpath_elements)
            return [True, len(elements)]
        except NoSuchElementException:
            return [False, 0]

    def assertElementIsPresentByXPath_Click(self, xpath, msg=None):
        try:
            element = self.find_element_by_xpath(xpath).click()
            return True
        except NoSuchElementException:
            return False

    def assertElementIsPresentByXPath_Send(self, xpath_input, send_message):
        try:
            element = self.find_element_by_xpath(xpath_input)
            element.clear()
            length = len(element.get_attribute('value'))
            element.send_keys(length * Keys.BACKSPACE)
            time.sleep(2)
            element.send_keys(send_message)
            return True
        except NoSuchElementException:
            return (False)

    def element_exists_and_click(self, xpath):
        assert BasePage.assertElementIsPresentByXPath_Click(self, xpath), f'Элемента {xpath} на странице нет'

    def element_exists_and_send(self, xpath_input, send_message) -> object:
        assert BasePage.assertElementIsPresentByXPath_Send(self, xpath_input,
                                                           send_message), f'Элемента {xpath_input} на странице нет'

    def element_exists_count(self, xpath_elements):
        elements_array = BasePage.assertElementsIsPresentByXpatch(self, xpath_elements)
        assert elements_array[0], f'Элементов {xpath_elements} на странице нет'
        return elements_array

    def scroll_down_link_click(self, xpath_down_link):

        SCROLL_PAUSE_TIME = 0.5
        # Get scroll height
        last_height = self.execute_script("return document.body.scrollHeight")
        while True:
            # Scroll down to bottom
            self.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        assert BasePage.assertElementIsPresentByXPath_Click(self,
                                                            xpath_down_link), f'Элемент {xpath_down_link} внизу страницы не обнаружен'

    def drop_down_element_click(self, xpath_drop_down_list, element_text):

        element = self.find_element_by_xpath(xpath_drop_down_list)
        element.click()
        all_options = element.find_elements_by_tag_name("option")
        for option in all_options:
            if option.get_attribute("text") == element_text:  # print("Value is: %s" % option.get_attribute("value"))
                option.click()
                break

    def element_exists_and_click_enter(self, xpath_element):
        self.find_element_by_xpath(xpath_element).send_keys(Keys.RETURN)

    def autorization_user(self, url, login, password):
        session = requests.Session()
        session.post(url, {
            'username': login,
            'password': password,
            'remember': 1,
        })

    def uploading_file(self, xpath_input_file, file_path):
        self.find_element(By.XPATH, xpath_input_file).send_keys(file_path)

    def logging_file(log_file):
        logger.remove()
        logger.add(log_file, level='INFO',
                   format="<lvl>[</lvl><c>{time:DD.MM.YYYY HH:mm:ss.SSS}</c><lvl>]</lvl> <lvl>{message}</lvl>",
                   catch='True')

    def element_exists_array(self, xpath_elements):
        elements_array = self.find_elements(By.XPATH, xpath_elements)
        assert elements_array[0], f'Элементов {xpath_elements} на странице нет'
        return elements_array

    def switch_to_current_window(self):
        self.switch_to.active_element
        handles = self.window_handles
        for handle in handles:
            if self.current_window_handle != handle:
                # Закрываем первое окно
                self.close()
                # переключаемся на второе окно', handle
                self.switch_to.window(handle)

    def element_href_return(self, xpath_element):
        element = self.find_element_by_xpath(xpath_element)
        return element.get_attribute('href')

    def drop_down_select_value(self, xpath_drop_down, drop_down_value):
        select = Select(self.find_element_by_xpath(xpath_drop_down))
        # select by value
        select.select_by_value(drop_down_value)

    def drop_down_select_text(self, xpath_drop_down, drop_down_text):
        select = Select(self.find_element_by_xpath(xpath_drop_down))
        # select by visible text
        select.select_by_visible_text(drop_down_text)

    def clear_element_input(self, xpath_element):
        element = self.find_element_by_xpath(xpath_element)
        element.clear()
        length = len(element.get_attribute('value'))
        element.send_keys(length * Keys.BACKSPACE)

    def get_text_of_element(self, xpath_element):
        element = self.find_elements_by_xpath(xpath_element)
        return element.text

    def pressing_down_arrow_key(self, n):
        action = ActionChains(self)
        for _ in range(n):
            action.send_keys(Keys.ARROW_DOWN)
            time.sleep(.1)
        action.perform()

    def pressing_down_enter_key(self, n):
        action = ActionChains(self)
        for _ in range(n):
            action.send_keys(Keys.RETURN)
            time.sleep(.1)
        action.perform()

    def find_text_on_page(self, text):
        try:
            self.find_element_by_partial_link_text(text).click()
            return True
        except NoSuchElementException:
            return False


    def link_search_in_page(self, text):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches()
        main_page.search_text_element = text
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        assert search_results_page.is_results_found(), "No results found."


    def find_href_on_page(self, link):
        message = f'# Ссылки на {link} на странице нет'
        url = ''
        elems = self.find_elements_by_xpath("//a[@href]")
        for elem in elems:
            s = elem.get_attribute("href")
            if link in s:
                message = f'# Ссылка на {link} на странице ЕСТЬ'
                url = s
        m = []
        m.append(message)
        m.append(url)
        return m

    def check_url(url):
        message = "# Адрес существует"
        try:
            response = requests.get(url)
        except ValueError:
            message = "# Адреса НЕ существует"
        return message

    def set_attribute_value(self, xpath, value):
        self.execute_script("arguments[0].setAttribute('value',arguments[1])",xpath, value)

    def open_url_in_new_tab(self, url):
        # open in new tab
        self.execute_script("window.open('%s', '_blank')" % url)
        # Switch to new tab
        self.switch_to.window(self.window_handles[-1])