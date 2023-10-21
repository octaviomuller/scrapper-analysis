from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

def not_empty_fonts(font):
    return len(font['fonts']) > 0

def get_font(elements):
    font_set = set()

    for element in elements:
        try:
            font = element.value_of_css_property("font-family")
            font_set.add(font)
        except StaleElementReferenceException:
            print('Error getting font')

    return list(font_set)

def get_font_set(driver):
    tags = ['span', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a']

    fonts_set = list()
    for tag in tags:
        target_tags = driver.find_elements(By.TAG_NAME, tag)
        fonts = get_font(target_tags)
        
        if len(fonts) > 0:
            fonts_set.append({
            'tag': tag,
            'fonts': fonts
        })

    return fonts_set