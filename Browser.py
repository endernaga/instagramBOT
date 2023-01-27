import random
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver


class Startbrowser:
    def __init__(self):
        self.browser = webdriver.Edge('edgedriver')

    def auth(self, username, password):
        self.browser.get('https://www.instagram.com')
        time.sleep(3)

        username_input = self.browser.find_element(by='name', value='username')
        username_input.clear()
        username_input.send_keys(username)

        password_input = self.browser.find_element(by='name', value='password')
        password_input.clear()
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

    def get_main_page(self):
        self.browser.get('https://www.instagram.com')
        time.sleep(5)
        try:
            close_button = self.browser.find_element(by=By.XPATH,
value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
            close_button.click()
        except:
            pass
        time.sleep(3)

    def main_page_pub(self):
        all_post = self.browser.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/section/div/div[3]/div[1]/div')
        posts = all_post.find_elements(by=By.TAG_NAME, value='article')
        is_avable = 0
        for post in posts:
            if post.find_elements(by=By.CSS_SELECTOR, value='div._aar2'):
                is_avable += 1

        return_list = []
        for post in posts:
            pre_href = post.find_element(by=By.CSS_SELECTOR, value='div._ae2s._aggd')
            hrefs = pre_href.find_elements(by=By.TAG_NAME, value='a')
            href = [href.get_attribute('href') for href in hrefs if '/p/' in href.get_attribute('href') and 'liked_by' not in href.get_attribute('href')]
            return_list += href

        if not is_avable:
            self.browser.execute_script("window.scrollBy(0, 3000);")
            return return_list + self.main_page_pub()

        else:
            return return_list

    def make_a_coment(self, hrefs, text):
        already_checked = []
        for href in hrefs:
            self.browser.get(href)
            time.sleep(3)
            is_folow = self.browser.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div[2]/button/div/div').text
            if is_folow == 'Відстежується' and href not in already_checked:
                already_checked.append(href)
                comment_input = self.browser.find_element(By.CSS_SELECTOR, value='form._aidk')
                comment_click = comment_input.find_element(by=By.TAG_NAME, value='textarea')
                comment_click.click()
                comment_input = self.browser.find_element(by=By.TAG_NAME, value='textarea')
                comment_input.send_keys(random.choice(text))
                time.sleep(2)
            elif href in already_checked:
                pass
            else:
                time.sleep(2)
                break
