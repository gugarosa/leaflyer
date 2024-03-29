"""Module used to scrap data from Leafly."""

import time

from bs4 import BeautifulSoup
from selenium import webdriver

# Defines constants to be used
BASE_URL = 'https://www.leafly.com'
SLEEP_TIME = 5


def _attempt_find_element(element, *args, **kwargs):
    """Attempts to find an element with try-except clause.

    Args:
        element (BeautifulSoup): An element to be searched.

    """

    # Attempts to find the element
    try:
        # Returns the result
        return element.find(*args, **kwargs)

    # If element has not been found
    except:
        # Returns an empty string
        return ''


def get_strains_list(page_id):
    """Gets a list of strain URLs based on the page's identifier.

    Args:
        page_id (int): Page identifier.

    Returns:
        List containing the strains' URLs.

    """

    # Creates the URL to be scrapped
    url = f'{BASE_URL}/strains?page={page_id}'

    print(f'Fetching data from: {url}')

    # Gathers an instance of the Firefox driver, gets the URL and sleeps
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(SLEEP_TIME)

    # Performs the age-approval validation
    driver.find_element_by_xpath('//*[@id="tou-continue"]').click()
    time.sleep(SLEEP_TIME)

    # Performs a check if the element is really available
    try:
        # Gets the HTML list of strains
        strains_list_html = driver.find_element_by_xpath('/html/body/main/div/div[1]/div[2]/ul').get_attribute('outerHTML')

    # If the element is not available
    except:
        print(f'Missed up page: {page_id}')

        # Closes the driver
        driver.close()

        return None

    # Parses the HTML and find its individual items
    soup = BeautifulSoup(strains_list_html, features='html.parser')
    strains_list = soup.find_all('li')

    # Creates a list holding the URLs themselves
    strains_url = [BASE_URL + strain.find('a')['href'] for strain in strains_list]

    # Closes the driver
    driver.close()

    return strains_url


def get_strain_data(url):
    """Gets meta-information regarding a specific strain.

    Args:
        url (str): URL to gather the meta-information.

    Returns:
        A dictionary containing the meta-data of the desired strain.

    """

    print(f'Fetching data from: {url}')

    # Gathers an instance of the Firefox driver, gets the URL and sleeps
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(SLEEP_TIME)

    # Performs the age-approval validation
    driver.find_element_by_xpath('//*[@id="tou-continue"]').click()
    time.sleep(SLEEP_TIME)

    # Creates an empty dictionary
    data = {}

    # Performs a check if the element is really available
    try:
        # Gets the HTML that holds the strain's data
        strain_data_html = driver.find_element_by_xpath('/html/body/main/div/div').get_attribute('outerHTML')

    # If the element is not available
    except:
        print(f'Missed up url: {url}')

        # Closes the driver
        driver.close()

        return None

    # Parses the HTML and find its individual sections
    soup = BeautifulSoup(strain_data_html, features='html.parser')

    # Finds the `strain-card` element and gathers its information
    strain_data_card = soup.find(id='strain-card')
    strain_data_card_level = strain_data_card.find_all(class_='jsx-1012626707 text-xs rounded flex items-center mr-xl')

    data['name'] = _attempt_find_element(strain_data_card, 'h1').getText()
    data['img_url'] = _attempt_find_element(strain_data_card, 'img')['srcset'].split('?')[0]        
    data['type'] = _attempt_find_element(strain_data_card, class_='bg-leafly-white').getText()
    data['thc_level'] = strain_data_card_level[0].getText().split(' ')[-1]
    data['cbd_level'] = strain_data_card_level[1].getText().split(' ')[-1]
    data['most_common_terpene'] = _attempt_find_element(strain_data_card, class_='jsx-1012626707 flex items-center').getText()
    data['description'] = _attempt_find_element(strain_data_card, class_='strain__description').find('p').getText()

    # Finds the `strain-effects-section` element and gathers its information
    strain_effects_card = soup.find(id='strain-effects-section').find(class_='react-tabs__tab-panel-container')
    strain_effects_card_divs = strain_effects_card.find_all('div')

    # Instantiates the `effects` list from the `data` dictionary
    data['effects'] = {}

    # Iterates through every div
    for div in strain_effects_card_divs:
        # Finds all the div tags inside current tag
        items_div = div.find_all(class_='mb-lg')

        # Iterates through every item
        for item in items_div:
            # Gathers the name and description of the effect
            item_name = _attempt_find_element(item, class_='mb-xs').getText()[:-1]
            item_desc = _attempt_find_element(item, class_='font-mono').getText().split('%')[0] + '%'

            # Changes the item's name to a key-like string
            item_name = item_name.replace(" ", "_").lower()

            # Appends the data
            data['effects'][item_name] = item_desc

    # Closes the driver
    driver.close()

    return data
