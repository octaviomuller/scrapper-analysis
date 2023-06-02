# TODO: Gerar rotina pra scrapping dos dados
# TODO: Montar estrutura para salvar no csv
# TODO: Adicionar extração de palavra chave (Tensor Flow?)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from jinja2 import Environment, FileSystemLoader
import os

from colors import get_colors
from fonts import get_font_set
from products import get_products
from template import open_template


chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=chrome_options)
driver.get('https://www.kabum.com.br/ofertas/megamaio')

colors = get_colors(driver)
fonts = get_font_set(driver)
products = get_products(driver)
image_path = os.path.abspath('temp/screenshot.png')

# driver.quit()

open_template(colors, fonts, products, image_path)