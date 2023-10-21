from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os

from engine.colors import get_colors
from engine.fonts import get_font_set
from engine.products import get_products
from template.template import open_template

class Scrapper:
    def __init__(self, url, dataset_op = True):
        self.url = url
        self.dataset_op = dataset_op

    def execute(self):
        self.set_browser()

        if not self.dataset_op:
            image_path = os.path.abspath('temp/screenshot.png')
            open_template(self.colors(), self.fonts(), self.products(), image_path)
    
        self.driver.quit()
        
        return {
            'colors': self.colors(),
            'fonts': self.fonts(),
            'products': self.products(),
            'url': self.url
        }

    def set_browser(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chrome_options)
        self.driver = driver.get(self.url)

    def colors(self):
        self.colors = get_colors(self.driver)
        if not self.dataset_op: return self.colors
        
        return {
            item['name']: {
                item['rbg'],
                item['percentage']
            } for item in self.colors
        }

    def fonts(self):
        self.fonts = get_font_set(self.driver)
        if not self.dataset_op: return self.fonts

        return {
            item['tag']: ''.join(item['fonts']) for item in self.fonts
        }

    def products(self):
        self.products = get_products(self.driver)
        if not self.dataset_op: return self.products

        return ''.join(self.products)