# TODO: Corrigir comentários
# TODO: 
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag
import re

def get_products(driver):
    soup = BeautifulSoup(driver.page_source, 'html.parser') # Capturando a página HTML
    text_tags = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'span']) # Buscando todas as tags de texto na página
    product_titles = set() # Inicializando um conjunto para guardar os títulos dos produtos

    # nltk.download('averaged_perceptron_tagger')

    # Analisando cada tag
    for tag in text_tags:
        text = tag.get_text().strip().lower() # Remove strings that look like prices
        text = re.sub(r'\$\d+(\.\d{2})?', '', text)
        tokens = word_tokenize(text) # Remove strings that look like prices
        
        # Verificando o comprimento do texto e a diversidade de palavras
        if len(tokens) > 5 and len(set(tokens)) > 4:
            product_titles.add(text)

    return product_titles
