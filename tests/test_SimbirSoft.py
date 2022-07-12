import datetime
import os
import sys
import time

sys.path.append(os.path.abspath('/home/gm/PycharmProjects/SimbirSoft/'))
from lib.base_page import BasePage as Base
from lib.my_selectors import MySelectors as S
from lib.my_data import MyData as D
from loguru import logger
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def __init__(self, browser):
    self.browser = browser


@logger.catch
def test_simbirsoft(browser):
    global new_page
    logger.info('# Записываем дату и время начала теста: ' + str(datetime.datetime.today().strftime('%d.%m.%Y')))
    logger.info('# устанавливаем имя файла для логирования')
    Base.logging_file(D.log_file_name)

    logger.info('# ЗАПУСТИЛИ ТЕСТОВОЕ ЗАДАНИЕ ПО UI ДЛЯ КОМПАНИИ "SIMBIRSOFT"')

    logger.info('# установили максимальный размер окна браузера')
    browser.maximize_window()

    # сначала зайдем на другой сайт, а уже с него перейдем на ЯНдекс
    # это для того, чтобы обойти капчу для роботов от Яндекс
    # потратим дополнительно 15 секунд, зато гарантировано зайдем на Яндекс без капчи
    message_in_log = '# заходим на стартовую страницу ' + D.start_url
    logger.info(message_in_log)
    browser.get(D.start_url)

    message_in_log = '# нажимаем на "Yandex"'
    logger.info(message_in_log)
    Base.element_exists_and_click(browser, S.xpath_enter_Yandex)

    message_in_log = '# ждем 15 секунд для переходя на сайт yandex.ru'
    # 10 + 10 - 15 = 5 секунд на поиск селектора в следующем шаге
    logger.info(message_in_log)
    time.sleep(10)

    message_in_log = '# после перехода на yandex.ru делаем эту страницу активной'
    logger.info(message_in_log)
    Base.switch_to_current_window(browser)

    message_in_log = '# нажимаем кнопку "Войти"'
    logger.info(message_in_log)
    Base.element_exists_and_click(browser, S.xpath_enter_button)

    message_in_log = '# делаем страницу с логином и паролем активной'
    logger.info(message_in_log)
    Base.switch_to_current_window(browser)

    message_in_log = '# выбираем "Почта"'
    logger.info(message_in_log)
    Base.element_exists_and_click(browser, S.xpath_email)

    message_in_log = '# вводим логин'
    logger.info(message_in_log)
    Base.element_exists_and_send(browser, S.xpath_enter_login, D.mail_login)

    message_in_log = '# нажимаем кнопку "Войти"'
    logger.info(message_in_log)
    Base.element_exists_and_click(browser, S.xpath_enter_login_button)

    message_in_log = '# вводим пароль"'
    logger.info(message_in_log)
    Base.element_exists_and_send(browser, S.xpath_enter_password, D.mail_password)

    message_in_log = '# нажимаем кнопку "Войти"'
    logger.info(message_in_log)
    Base.element_exists_and_click(browser, S.xpath_enter_login_button)

    time.sleep(3)
    message_in_log = '# переходим на страницу "Яндекс.Диск"'
    logger.info(message_in_log)
    browser.get(D.url_yandex_disk)

    message_in_log = '# закрываем модальное окно, если оно есть и активно'
    logger.info(message_in_log)
    if Base.assertElementIsPresentByXPath_Click(browser, S.xpath_pop_up_close_button) == True:
        Base.element_exists_and_click(browser, S.xpath_pop_up_close_button)

    message_in_log = '# нажимаем кнопку "Создать"'
    logger.info(message_in_log)
    Base.element_exists_and_click(browser, S.xpath_create_button)

    message_in_log = '# нажимаем создание новой папки'
    logger.info(message_in_log)
    Base.element_exists_and_click(browser, S.xpath_create_Folder)

    message_in_log = '# вносим название новой папки'
    logger.info(message_in_log)
    Base.element_exists_and_send(browser, S.xpath_name_Folder, D.name_Folder)

    message_in_log = '# сохраняем новую папку'
    logger.info(message_in_log)
    Base.element_exists_and_click(browser, S.xpath_save_Folder)

    message_in_log = '# переходим в эту новую папку'
    logger.info(message_in_log)
    browser.get(D.url_new_Folder)

    message_in_log = '# нажимаем кнопку "Создать"'
    logger.info(message_in_log)
    Base.element_exists_and_click(browser, S.xpath_create_button)

    message_in_log = '# нажимаем создание нового текстового документа'
    logger.info(message_in_log)
    Base.element_exists_and_click(browser, S.xpath_new_Document)

    message_in_log = '# вносим название нового документа'
    logger.info(message_in_log)
    Base.element_exists_and_send(browser, S.xpath_name_Document, D.name_Document)

    message_in_log = '# сохраняем новый документ'
    logger.info(message_in_log)
    Base.element_exists_and_click(browser, S.xpath_save_Folder)

    time.sleep(3)
    message_in_log = '# закрываем вкладку документа и переходим на страницу "Яндекс.Диск"'
    logger.info(message_in_log)
    browser.switch_to.window(browser.window_handles[-1])
    browser.close()
    browser.switch_to.window(browser.window_handles[0])

    time.sleep(3)

    message_in_log = '# открываем страницу созданного документа'
    logger.info(message_in_log)
    Base.open_url_in_new_tab(browser, D.url_new_Document)

    time.sleep(7)

    message_in_log = '# опять закрываем вкладку документа и переходим на страницу "Яндекс.Диск"'
    logger.info(message_in_log)
    browser.switch_to.window(browser.window_handles[-1])
    browser.close()
    browser.switch_to.window(browser.window_handles[0])

    message_in_log = '# разлогиниваемся'
    logger.info(message_in_log)
    Base.element_exists_and_click(browser, S.xpath_avatar)
    Base.element_exists_and_click(browser, S.xpath_out)

    logger.info('# ЗАВЕРШИЛИ ТЕСТОВОЕ ЗАДАНИЕ ПО UI ДЛЯ КОМПАНИИ "SIMBIRSOFT"')

    

