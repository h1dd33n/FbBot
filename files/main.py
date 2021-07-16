from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import time
import os


class DataGatherer:

    def __init__(self):
        self.browser = webdriver.Firefox()

    def login(self):
        browser = self.browser
        browser.get('https://www.facebook.com')
        time.sleep(5)
        browser.find_element_by_class_name('_4t2a').find_element_by_css_selector('div>div>div>div:nth-child(3)'
                                                                                 '>button:nth-child(2)').click()
        time.sleep(1)
        browser.find_element_by_tag_name('form').find_element_by_id('email').send_keys('+358418053212')
        time.sleep(3)
        browser.find_element_by_tag_name('form').find_element_by_id('pass').send_keys('N3wP@$$!')
        time.sleep(3)
        browser.find_element_by_tag_name('form').find_element_by_id('email').send_keys(Keys.ENTER)
        time.sleep(10)

    def get_group_title(self, group_url):
        self.browser.get(group_url + '/members')
        time.sleep(10)
        title = self.browser.find_elements_by_tag_name('h1')
        print('[+] Collecting users from group - ' + title[-1].text)
        return title[-1].text

    def make_directory(self, title):
        if not os.path.isdir(title):
            os.mkdir(title)
            comp = os.path.join(f'{title}', f'{title}.json')
            comp2 = os.path.join(f'{title}', 'checks.json')
            f = open(comp, 'a')
            f.close()
            f = open(comp2, 'a')
            f.close()

    def get_new_members(self, title):
        ignore = ['Learn More', "Online ", 'About', 'Discussion', 'Rooms', 'Topics', 'Members', 'Events',
                  'Media', 'Announcements']
        users = list()
        added = list()
        input = self.browser.find_elements_by_tag_name('input')
        input = input[-1]
        added.append('a'.title())
        members_count = int(str(self.browser.find_elements_by_tag_name('strong')[-2].text)
                            .replace('·', '').replace(',', '').strip())
        # Add user input options based on members_count
        print(f'Members count is {members_count}')

        while True:
            for k in added:
                if len(users) >= members_count / 2:
                    break
                print(len(users))
                print(f'----- {len(added)} users in added ------')
                # k = k.split(' ')[0]
                for j in k:
                    input.send_keys(j)
                    time.sleep(3)
                    for i in range(0, 19):
                        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                        time.sleep(3)
                    a = self.browser.find_elements_by_tag_name('a')
                    for i in a[17:]:
                        if i.text:
                            # print(i.get_attribute('href'))
                            # print(i.text)
                            name = str(i.text)
                            user = {name: i.get_attribute('href')}
                            if name not in added:
                                if name not in ignore:
                                    users.append(user)
                                    print(f'[+] Added {name} to users [U]')
                            if name not in added:
                                if name not in ignore:
                                    added.append(name)
                                    print(f'[+] Added {name} to added [A]')
                            else:
                                print(f'[-] {name} already in added [-]')
                for l in range(0, len(k) + 1):
                    input.send_keys(Keys.BACK_SPACE)
                    time.sleep(2)
            break

        with open(f'{title}/checks.json', 'w+') as f:
            json.dump(added, f)
            f.close()
        with open(f'{title}/{title}.json', 'w+') as f:
            json.dump(users, f)
            f.close()


def get_members(self, group_url):
    self.make_directory(self.get_group_title(group_url))


if __name__ == '__main__':
    print('|---- Welcome, Please enter group url to start gathering facebook data ----|')
    url = input()
    bot = DataGatherer()
    bot.login()
    title = bot.get_group_title(url)
    # title = bot.get_group_title('https://www.facebook.com/groups/117547242139482')
    bot.make_directory(title)
    bot.get_new_members(title)
