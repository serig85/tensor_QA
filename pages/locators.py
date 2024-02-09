from selenium.webdriver.common.by import By


class BasePageLocation:
    block_mes_cookies_sbis = (By.XPATH, '//div[@class = "sbis_ru-CookieAgreement sbis_ru-CookieAgreement--show"]')
    close_mes_cookies_sbis = (By.XPATH, '//div[@class = "sbis_ru-CookieAgreement__close"]')
    block_mes_cookies_tensor = (By.XPATH, '//div[@class = "tensor_ru-messages-container"]')
    close_mes_cookies_tensor = \
        (By.XPATH, '//div[@class = "tensor_ru-CookieAgreement__close'
                   ' icon-Close ws-flex-shrink-0 ws-flexbox ws-align-items-center"]')


class MainPageLocators:
    contact_link = (By.XPATH,
                    '//li[@class = "sbisru-Header__menu-item sbisru-Header__menu-item-1 mh-8  s-Grid--hide-sm"]')
    tensor_icon = (By.XPATH, '//a[@class = "sbisru-Contacts__logo-tensor mb-12"]')
    block_sila_v_ludah = (By.XPATH, '//div[@class="tensor_ru-Index__block4-bg"]')
    text_sila_v_ludah = \
        (By.XPATH, '//div[@class="tensor_ru-Index__block4-bg"]'
                   '//p[@class = "tensor_ru-Index__card-title tensor_ru-pb-16"]')
    sila_details = \
        (By.XPATH, '//div[@class="tensor_ru-Index__block4-bg"]//a[@class="tensor_ru-link tensor_ru-Index__link"]')
    download_sbis_link = (By.XPATH, '//a[@href="/download?tab=ereport&innerTab=ereport25"]')


class AboutPageLocators:
    imgs_block = (By.XPATH,
                  '//div[@class = "tensor_ru-container tensor_ru-section tensor_ru-About__block3"]')
    imgs = (By.XPATH,
            '//div[@class = "tensor_ru-container tensor_ru-section tensor_ru-About__block3"]//img')


class ContactPageLocators:
    region_label_link = (By.XPATH,
                         '//span[@class = "sbis_ru-Region-Chooser ml-16 ml-xm-0"]//span')
    list_of_partners = (By.XPATH,
                        '//div[@class = "sbisru-Contacts-List__col ws-flex-shrink-1 ws-flex-grow-1"]')
    label_list_of_partners = (By.XPATH, '//div[@id = "city-id-2"]')
    pop_up_window = (By.XPATH, '//ul[@class = "sbis_ru-Region-Panel__list"]//li')
    title = (By.XPATH, '//title[@class = "state-1"]')


class DownloadPageLocator:
    change_download_plagin = (By.XPATH,
                              '//div[@class = "controls-TabButton__caption"][text() = "СБИС Плагин"]')
    web_install_link = (By.XPATH, '//h3[text()= "Веб-установщик "]/parent::div/parent::div//a')
