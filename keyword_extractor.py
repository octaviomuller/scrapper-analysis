import spacy

def keyword_extractor(input):
    nlp = spacy.load('pt_core_news_sm')
    doc = nlp(input)
    keywords = [token.text for token in doc if token.pos_ in ['NOUN', 'ADJ']]

    return keywords