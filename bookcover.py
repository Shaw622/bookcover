#! /usr/bin/env python3

from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')

try:
    elem = browser.find_element_by_class_name('bookcover')
    print('そのクラス名を持つ要素 <{}>を見つけた！'.format(elem.tag_name))
except:
    print('そのクラス名を持つ要素は見つからなかった。')
