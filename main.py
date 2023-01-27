import re

from Browser import *

with open('auth.txt') as f:
    for text in f.readlines():
        if 'username' in text:
            username = re.findall(r"'.[A-z].*|[А-я].*'", text)[0][1:][:-1]
        else:
            password = re.findall(r"'.[A-z].*|[А-я].*'", text)[0][1:][:-1]

with open('text.txt') as f:
    browser = Startbrowser()
    browser.auth(username, password)
    while True:
        browser.get_main_page()
        browser.make_a_coment(browser.main_page_pub(), f.readlines())
        time.sleep(300)
