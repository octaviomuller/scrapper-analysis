from bs4 import BeautifulSoup
import re

def get_products(driver):
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    text_tags = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'span'])
    product_titles = set()


    for tag in text_tags:
        text = tag.get_text().strip().lower()
        text = re.sub(r'\$\d+(\.\d{2})?', '', text)
        
        if len(text.split()) > 5 and len(set(text.split())) > 4:
            product_titles.add(text)

    return list(product_titles)
