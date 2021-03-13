import time

from selenium import webdriver
from bs4 import BeautifulSoup

# Defines constants to be used
BASE_URL = 'https://www.leafly.com/strains'
SLEEP_TIME = 5

def get_strains_list(page_id):
    """Gets a list of strain URLs based on the page's identifier.

    Args:
        page_id (int): Page identifier.

    Returns:
        List containing the strains' URLs.

    """

    # Creates the URL to be scrapped
    url = f'{BASE_URL}?page={page_id}'

    print(f'Fetching data from: {url}')

    # Gathers an instance of the Firefox driver, gets the URL and sleeps
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(SLEEP_TIME)

    # Performs the age-approval validation
    driver.find_element_by_xpath('//*[@id="tou-continue"]').click()
    time.sleep(SLEEP_TIME)

    # Gets the HTML list of strains
    strains_list_html = driver.find_element_by_xpath('/html/body/main/div/div[2]/ul').get_attribute('outerHTML')

    # Parses the HTML and find their individual items
    soup = BeautifulSoup(strains_list_html, features='html.parser')
    strains_list = soup.find_all('li')

    # Creates a list holding the URLs themselves
    strains_url = [BASE_URL + strain.find('a')['href'] for strain in strains_list]

    # Closes the driver
    driver.close()

    return strains_url
