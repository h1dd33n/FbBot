from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import time
import os

# from files import hunter
from bot import Hunter

if __name__ == '__main__':
    print('|---- Welcome, please enter group url to start gathering facebook data ----|')
    print('|---- ', end='')
    url = input()
    bot = Hunter()
    bot.login()
    title = bot.get_group_title(url)
    # title = bot.get_group_title('https://www.facebook.com/groups/117547242139482')
    bot.make_directory(title)
    bot.get_new_members(title)
