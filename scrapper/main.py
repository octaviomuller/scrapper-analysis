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
            template.open_template(self.colors(), self.font(), self.context(), image_path)
            
            return
    
        dataset_info = {
            **self.colors(),
            'font': self.font(),
            'context': self.context(),
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
        
        if not self.url.startswith("https://"):
            self.url = "https://" + self.url
            
        driver.get(self.url)

    def colors(self):
        colors = engine.get_colors(self.driver, self.dataset_op)
        
        return colors

    def font(self):
        font = engine.get_most_common_font(self.driver)
        
        return font

    def context(self):
        context =  engine.get_context(self.driver)

        return context