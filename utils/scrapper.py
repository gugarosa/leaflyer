import os
import re
import time

from selenium import webdriver
from bs4 import BeautifulSoup

#
BASE_URL = 'https://www.leafly.com/strains'

def get_strains_list(page_id):
    """
    """

    #
    url = f'{BASE_URL}?page={page_id}'

    #
    driver = webdriver.Chrome('C:\\Users\\Gustavo\\Documents\\GitHub\\pixel_character_generator\\notebooks\\chromedriver.exe')
    driver.get(url)
    time.sleep(5)

    #
    driver.find_element_by_xpath('//*[@id="tou-continue"]').click()
    time.sleep(5)

    #
    strains_list_html = driver.find_element_by_xpath('/html/body/main/div/div[2]/ul').get_attribute('outerHTML')

    #
    soup = BeautifulSoup(strains_list_html, features='html.parser')

    #
    strains_list = soup.find_all('li')

    #
    strains_url = []

    for strain in strains_list:
        strains_url.append(BASE_URL + strain.find('a')['href'])

    return strains_url


if __name__ == "__main__":
    urls = get_strains_list(1)
    print(urls)