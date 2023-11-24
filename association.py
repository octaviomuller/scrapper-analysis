import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk
import statistics

from keyword_extractor import keyword_extractor

nltk.download('punkt')

def apply_stemming(text):
    stemmer = PorterStemmer()
    words = word_tokenize(text)
    stemmed_words = [stemmer.stem(word) for word in words]
    return ' '.join(stemmed_words)
    
def parse_hex_color(color):
    color = color.lstrip('#')
    return [int(color[i:i+2], 16) for i in (0, 2, 4)]

def weighted_average_color(colors, teste):
    color_tones = list(zip(*colors))

    median_tones = [statistics.median(tone) for tone in color_tones]

    median_tones_int = [int(value) for value in median_tones]

    hex_color = "#{:02x}{:02x}{:02x}".format(*median_tones_int)

    return hex_color


def get_most_frequent_tone(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return max(counts, key=counts.get)

def most_frequent(lst):
    counts = lst.value_counts()
    return counts.idxmax()

def associate_keywords_with_colors_and_font(keywords, similarity_threshold=0.3):
    dataset = pd.read_csv('dataset.csv') 
    
    dataset['context'] = dataset['context'].fillna('')

    dataset['context'] = dataset['context'].apply(apply_stemming)

    docs = list(dataset['context'])
    docs.append(" ".join(keywords))

    vectorizer = TfidfVectorizer()
    
    tfidf_matrix = vectorizer.fit_transform(docs)

    cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

    similarity_df = pd.DataFrame(cosine_sim.T, columns=['similarity'])

    relevant_rows = similarity_df[similarity_df['similarity'] > similarity_threshold]

    if not relevant_rows.empty:
        most_similar_indices = relevant_rows.index

        selected_data = dataset.loc[most_similar_indices, ['primary-color', 'secondary-color', 'accent-color', 'font']]

        selected_data_colors = selected_data[['primary-color', 'secondary-color', 'accent-color']].applymap(parse_hex_color)

        primary_color = weighted_average_color(selected_data_colors['primary-color'], 'primary-color')
        secondary_color = weighted_average_color(selected_data_colors['secondary-color'], 'secondary-color')
        accent_color = weighted_average_color(selected_data_colors['accent-color'], 'accent-color')

        result = {
            'primary-color': primary_color,
            'secondary-color': secondary_color,
            'accent-color': accent_color,
            'font': most_frequent(selected_data['font'])
        }

        return result
    else:
        return None

data = "loja de jogos e vídeo games"
keywords = keyword_extractor(data)
result = associate_keywords_with_colors_and_font(keywords, similarity_threshold=0.01)
print(result)