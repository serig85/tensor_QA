from .pages.main_page import MainPage


def test_scenario_one(browser):
    url = 'https://sbis.ru/'
    page = MainPage(browser, url)
    page.open()
    page.scenario_one()


def test_scenario_two(browser):
    url = 'https://sbis.ru/'
    page = MainPage(browser, url)
    page.open()
    page.scenario_two()


def test_scenario_three(browser):
    url = 'https://sbis.ru/'
    page = MainPage(browser, url)
    page.open()
    page.scenario_three()
