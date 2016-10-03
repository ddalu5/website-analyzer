from bs4 import BeautifulSoup
from mechanize import Browser


def get_browser(user_agent='Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
                handle_robots=True, handle_referer=False, handle_refresh=False):
    br = Browser()
    br.set_handle_robots(handle_robots)
    br.set_handle_referer(handle_referer)
    br.set_handle_refresh(handle_refresh)
    br.addheaders = [('User-agent', user_agent), ('Content-type', 'text/html; charset=utf-8')]
    return br


def get_html(browser, url):
    response = browser.open(url)
    if response.code == 200:
        return response.read().lower()
    return None


def get_web_soup(browser, url, l_type="lxml"):
    response = browser.open(url)
    if response.code == 200:
        return BeautifulSoup(response.read().lower(), l_type)
    return None

