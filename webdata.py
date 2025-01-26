import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


def setup_driver():
    driver = webdriver.Firefox()
    driver.get('https://www.monitor.co.ug/')
    return driver

def get_classes():
    _driver = setup_driver()
    unorderly_text = _driver.page_source
    soup = BeautifulSoup(unorderly_text, 'html.parser')

    classes = set()
    for tag in soup.find_all(True):
        if 'class' in tag.attrs:
            classes.update(tag['class'])
    
    with open('classes.txt', 'w') as file:
        for cls in classes:
            file.write(cls + '\n')

    time.sleep(2)
    _driver.quit()

get_classes()