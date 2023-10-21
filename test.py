import pandas as pd
import json

# Lendo o JSON do arquivo "dataset.json"
with open('dataset.json', 'r') as json_file:
    data = json.load(json_file)

# Convertendo cores em um DataFrame
colors_data = data[0]["colors"]
colors_df = pd.DataFrame(colors_data)

# Convertendo fonts em um DataFrame
fonts_data = data[0]["fonts"]
fonts_list = []
for item in fonts_data:
    fonts_list.extend(item["fonts"])
fonts_df = pd.DataFrame({"tag": [item["tag"] for item in fonts_data], "fonts": fonts_list})

# Convertendo produtos em um DataFrame
products_data = data[0]["products"]
products_df = pd.DataFrame({"product": products_data})

# Adicionando a URL como metadados
url = data[0]["url"]
metadata_df = pd.DataFrame({"url": [url]})

# Concatenando os DataFrames em um único DataFrame
merged_df = pd.concat([colors_df, fonts_df, products_df, metadata_df], axis=1)

# Salvando o DataFrame em um arquivo CSV chamado "output.csv"
merged_df.to_csv('output.csv', index=False)