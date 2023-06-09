from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from jinja2 import Environment, FileSystemLoader
import os
import json

from colors import get_colors
from fonts import get_font_set
from products import get_products
from template import open_template
from keyword_extractor import keyword_extractor
from ecommerce_list import ecommerce_list

def save_dataset(dataset, file_name):
    if os.path.isfile(file_name) and os.path.getsize(file_name) > 0:
        with open(file_name, 'r+') as json_file:
            content = json.load(json_file)
            content.extend(dataset)
            json_file.seek(0)
            json.dump(content, json_file, indent=4)
            json_file.truncate()
    else:
        with open(file_name, 'w') as json_file:
            json.dump(dataset, json_file, indent=4)

def url_analysis(url, dataset_op = False):
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chrome_options)
    driver.get(url)

    colors = get_colors(driver)
    fonts = get_font_set(driver)
    products = get_products(driver)

    if dataset_op:
        data = {
            'colors': colors,
            'fonts': fonts,
            'products': products,
            'url': url
        }
        save_dataset([data], 'dataset.json')

    else:
        image_path = os.path.abspath('temp/screenshot.png')
        open_template(colors, fonts, products, image_path)
    
    driver.quit()

def execute_routine():
    # url_analysis('http://www.kabum.com.br', True)
    for ecommerce in ecommerce_list:
        print(ecommerce)
        url_analysis(ecommerce, True)

def execute_keyword_extraction():
    text_input = input("Text to analyze: ")
    result = keyword_extractor(text_input)
    print(result)

def main():
    op = input("[1] - URL Analysis\n[2] - Execute Routine\n[3] - Extract Keywords\n")
    
    if op == '1':
        url = input('URL: ')
        url_analysis(url)
    elif op == '2':
        execute_routine()
    elif op == '3':
        execute_keyword_extraction()
    else:
        print("Opção inválida")

if __name__ == "__main__":
    main()