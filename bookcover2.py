#! /usr/bin/env python3

from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')

link_elem = browser.find_element_by_link_text('Read Online for Free')
link_elem.click()

