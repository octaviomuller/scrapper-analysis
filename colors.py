# TODO: Corrigir comentários
# TODO: Trocar método para temp file
from selenium import webdriver
import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def get_colors(driver):
    driver.execute_script("""
var elements = document.querySelectorAll('img');
elements.forEach(e => e.parentNode.removeChild(e))
""")
    driver.save_screenshot('temp/screenshot.png')

    img = cv2.imread('temp/screenshot.png') # Leia a imagem com OpenCV
    img = cv2.resize(img, (128, 128)) # Redimensionar imagem para aumentar a velocidade da análise de cores
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Mude para RGB (OpenCV usa BGR)

    pixels = img.reshape(-1, 3) # Redimensione a imagem para ser uma lista de pixels

    kmeans = KMeans(n_clusters=5) # Execute o algoritmo de agrupamento KMeans
    kmeans.fit(pixels)

    colors = kmeans.cluster_centers_ # Mostre as cores predominantes
    labels = kmeans.labels_

    _, counts = np.unique(labels, return_counts=True) # Calcule as porcentagens
    percentages = counts / len(labels)

    color_set = list()
    for color, percentage in zip(colors, percentages):
        r, g, b = color.astype(int)
        color_set.append({
            'rgb': f'rgb({r}, {g}, {b})',
            'percentage': percentage
        })

    def color_percentage(color):
        return color['percentage']

    color_set.sort(reverse=True, key=color_percentage)

    colors_names = ['primary-color', 'secondary-color', 'accent-color']
    for i in range(len(colors_names)):
        color_set[i]['name'] = colors_names[i]
        color_set[i]['percentage'] = round(color_set[i]['percentage'] * 100, 1)

    return color_set[:3]