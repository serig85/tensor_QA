import os
import time
import urllib.request
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from .base_page import BasePage
from .locators import MainPageLocators, AboutPageLocators, ContactPageLocators, DownloadPageLocator
from .logger import Logger


log = Logger().loggen()


class MainPage(BasePage):

    list_partners_text_before = ""

    def scenario_one(self):
        self.click_contact_link()
        self.click_tensor_icon()
        self.switch_to_window()
        self.checking_for_block_availability_sila_v_ludah()
        self.click_details_in_sila_v_ludah()
        self.checking_the_size_of_images()

    def click_contact_link(self):
        WebDriverWait(self.browser, 10).until(ec.element_to_be_clickable(MainPageLocators.contact_link)).click()

    def click_tensor_icon(self):
        time.sleep(1)
        icon = WebDriverWait(self.browser, 10).until(ec.presence_of_element_located(MainPageLocators.tensor_icon))
        icon.click()

    def switch_to_window(self):
        tensor_window = self.browser.window_handles[1]
        self.browser.switch_to.window(tensor_window)

    def checking_for_block_availability_sila_v_ludah(self):
        self.close_cookies_mess_tensor()
        element = WebDriverWait(self.browser, 10).until(ec.presence_of_element_located(MainPageLocators.
                                                                                       block_sila_v_ludah))
        ActionChains(self.browser).move_to_element(element).perform()
        text = WebDriverWait(self.browser, 10).until(ec.presence_of_element_located(
            MainPageLocators.text_sila_v_ludah)).text
        excepted_text = 'Сила в людях'
        assert text == excepted_text, \
            (f"Текущий текст соответствует ожидаемому. "
             f"\nActual: '{str(text)}' Expected: {str(excepted_text)}")

    def click_details_in_sila_v_ludah(self):
        self.browser.find_element(*MainPageLocators.sila_details).click()
        url = self.browser.current_url
        expected_url = 'https://tensor.ru/about'
        assert url == expected_url, \
            (f"URL сайта не соответствует ожидаемому. "
             f"\nActual: '{str(url)}' Expected: {str(expected_url)}")

    def checking_the_size_of_images(self):
        images_block = self.browser.find_element(*AboutPageLocators.imgs_block)
        ActionChains(self.browser).move_to_element(images_block).perform()
        image_sizes = set()
        images = self.browser.find_elements(*AboutPageLocators.imgs)
        for image in images:
            image_sizes.add(image.get_attribute('width') + image.get_attribute('height'))
        assert len(image_sizes) == 1, \
            "Есть отличающиеся картинки"

    def scenario_two(self):
        self.click_contact_link()
        self.check_display_text_on_region_link()
        self.check_list_of_partners()
        self.check_region_list_of_partners()
        self.take_list_partners_text_before()
        self.change_the_region(region='41 Камчатский край')
        self.check_region_text_after_region_select()
        self.check_city_in_contacts_changes()
        self.check_list_of_partners_in_contacts_changes()
        self.check_url_changes()
        self.check_browser_title_changes()

    def check_display_text_on_region_link(self):
        region_label = self.browser.find_element(*ContactPageLocators.region_label_link)
        expected_label = 'Нижегородская обл.'
        assert region_label.text == expected_label, \
            (f"Регион не соответствует ожидаемому. "
             f"\nActual: '{str(region_label.text)}' Expected: {str(expected_label)}")

    def check_list_of_partners(self):
        list_of_partners = self.browser.find_element(*ContactPageLocators.list_of_partners)
        assert list_of_partners

    def check_region_list_of_partners(self):
        label_list_of_partners = (self.browser.find_element
                                  (*ContactPageLocators.label_list_of_partners)).text
        expected_label = 'Нижний Новгород'
        assert label_list_of_partners == expected_label, \
            (f"Регион в списке контактов не соответствует ожидаемому. "
             f"\nActual: '{str(label_list_of_partners)}' Expected: {str(expected_label)}")

    def take_list_partners_text_before(self):
        self.list_partners_text_before = self.browser.find_element(*ContactPageLocators.list_of_partners).text

    def change_the_region(self, region: str):
        region_label = self.browser.find_element(*ContactPageLocators.region_label_link)
        region_label.click()
        pop_up_window = self.browser.find_elements(*ContactPageLocators.pop_up_window)
        for element in pop_up_window:
            if element.text == region:
                element.click()
                break
        else:
            log.info(f"Регион '{region}' не найден")

    def check_region_text_after_region_select(self):
        expected_text_value = 'Камчатский край'
        WebDriverWait(self.browser, 10).until(
            ec.text_to_be_present_in_element(ContactPageLocators.region_label_link, expected_text_value),
            "Ожидаемый текст элемента не найден в течение заданного промежутка времени"
        )
        region_label = self.browser.find_element(*ContactPageLocators.region_label_link)
        assert region_label.text == expected_text_value, \
            f"Region does not match. \nActual: '{region_label.text}' Expected: {expected_text_value}"

    def check_city_in_contacts_changes(self):
        label_list_of_partners = self.browser.find_element(*ContactPageLocators.label_list_of_partners)
        except_label = 'Петропавловск-Камчатский'
        assert label_list_of_partners.text == except_label, \
            (f"Регион  не соответствует ожидаемому. "
             f"\nActual: '{str(label_list_of_partners)}' Expected: {str(except_label)}")

    def check_list_of_partners_in_contacts_changes(self):
        list_partners_text = self.browser.find_element(*ContactPageLocators.list_of_partners).text
        assert list_partners_text != self.list_partners_text_before, \
            'Лист партнёров не изменился'

    def check_url_changes(self):
        actual_url = self.browser.current_url
        except_url = 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'
        assert actual_url == except_url, \
            (f"URL сайта не соответствует ожидаемому. "
             f"\nActual: '{str(actual_url)}' Expected: {str(except_url)}")

    def check_browser_title_changes(self):
        actual_title = self.browser.title
        except_title = 'СБИС Контакты — Камчатский край'
        assert actual_title == except_title, \
            (f"Название сайта не соответствует ожидаемому. "
             f"\nActual: '{str(actual_title)}' Expected: {str(except_title)}")

    def scenario_three(self):
        self.close_cookies_mess_sbis()
        download = self.browser.find_element(*MainPageLocators.download_sbis_link)
        ActionChains(self.browser).move_to_element(download).perform()
        download.click()
        time.sleep(3)
        download = WebDriverWait(self.browser, 10).until(
            ec.element_to_be_clickable(DownloadPageLocator.change_download_plagin))
        ActionChains(self.browser).click(download).perform()
        download = WebDriverWait(self.browser, 10).until(ec.presence_of_element_located(
            DownloadPageLocator.web_install_link))
        href = download.get_dom_attribute('href')
        filedir = os.path.join(os.getcwd(), "downloads")
        filename = href.split('/')[-1]
        if not os.path.exists(filedir):
            os.mkdir(filedir)
        filepath = os.path.join(filedir, filename)
        urllib.request.urlretrieve(href, filepath)
        size = os.path.getsize(filepath)
        actual_size_mb = round(size / 1024 ** 2, 2)
        expected_value = float(download.text.split(" ")[-2])
        time.sleep(3)
        os.remove(filepath)
        assert expected_value == actual_size_mb, \
            (f"Размер файла в МБ не соответствует ожидаемому. "
             f"\nActual: '{str(actual_size_mb)}' Expected: {str(expected_value)}")
