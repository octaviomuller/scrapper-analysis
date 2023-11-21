from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from collections import Counter

def get_most_common(font_list):
    if len(font_list) == 0:
        return
    
    counter = Counter(font_list)
    most_common = counter.most_common(1)[0][0]

    return most_common

def get_font(elements):
    font_set = set()

    for element in elements:
        try:
            font = element.value_of_css_property("font-family")
            font_set.add(font)
        except StaleElementReferenceException:
            print('Error getting font')

    return list(font_set)

def get_most_common_font(driver):
    tags = ['span', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a']

    fonts = list()
    for tag in tags:
        target_tags = driver.find_elements(By.TAG_NAME, tag)
        fonts = get_font(target_tags)
        most_common = get_most_common(fonts)
        fonts.append(most_common)

    return get_most_common(fonts)