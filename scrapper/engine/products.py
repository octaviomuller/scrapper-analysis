import spacy
from bs4 import BeautifulSoup

def get_context(driver):
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    text_tags = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'span'])

    nlp = spacy.load("pt_core_news_sm")

    texts = list()
    for tag in text_tags:
        text = tag.get_text().strip().lower()
        doc = nlp(text)

        filtered_tokens = [token.text for token in doc if token.pos_ in ['NOUN', 'ADJ']]
        filtered_text = ' '.join(filtered_tokens)

        if filtered_text:
            texts.append(filtered_text)

    context = ' '.join(texts)

    return context