# -*- coding: utf-8 -*-
import bs4, requests, re, sys, math, os
import datetime
import time
import socket
import json
import urllib.parse
import random, string

from pyvirtualdisplay import Display
from selenium import webdriver


BASE_URL = 'https://pastebin.com/archive'

_headers_get = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
}



def getPastebin():
    display = Display(visible=0, size=(800, 600))
    display.start()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')

    chrome_options.add_experimental_option('prefs', {
        'download.default_directory': os.getcwd(),
        'download.prompt_for_download': False,
    })

    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get(BASE_URL)

    # Loop through transactions and count
    links = browser.find_elements_by_tag_name('.page table.maintable td a')
    link_urls = [link.get_attribute('href') for link in links]

    for url in link_urls:
        if not "archive" in url:
            ref = str(url).split('/')[-1]
            url = "https://pastebin.com/%s" % (ref)
            print(ref)
            print(url)
            print("Opening : %s" % url)
            # Open a new window
            browser.execute_script("window.open('');")
            # Switch to the new window and open URL B
            browser.switch_to.window(browser.window_handles[1])

            url_raw = "https://pastebin.com/raw/%s" % (ref)
            browser.get(url_raw)


            # …Do something here
            print("Current Page Title is : %s" % browser.title)
            html = browser.find_element_by_xpath('/HTML/Body')
            html = html.text

            print(html)

            # Close the tab with URL B
            browser.close()
            # Switch back to the first tab with URL A
            browser.switch_to.window(browser.window_handles[0])
            print("Closing: %s" % url)

    browser.quit()
    display.stop()


def main():
    getPastebin()


if __name__ == "__main__":
    main()
