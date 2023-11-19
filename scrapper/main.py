import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import engine
import template

class Scrapper:
    def __init__(self, url: str, dataset_op = True):
        self.url = url
        self.dataset_op = dataset_op
        self.set_browser()

    def execute(self):
        if not self.dataset_op:
            image_path = os.path.abspath('temp/screenshot.png')
            template.open_template(self.colors(), self.fonts(), self.products(), image_path)
    
        dataset_info = {
            'colors': self.colors(),
            'fonts': self.fonts(),
            'products': self.products(),
            'url': self.url
        }

        self.driver.quit()

        return dataset_info

    def set_browser(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chrome_options)
        self.driver = driver
        
        driver.get(self.url)

    def colors(self):
        colors = engine.get_colors(self.driver)
        if not self.dataset_op: return colors
        
        return {
            item['name']: {
                item['rgb'],
                item['percentage']
            } for item in colors
        }

    def fonts(self):
        fonts = engine.get_font_set(self.driver)
        
        if not self.dataset_op: return fonts

        return {
            item['tag']: ''.join(item['fonts']) for item in fonts
        }

    def products(self):
        products = engine.get_products(self.driver)

        if not self.dataset_op: return products

        return ''.join(products)