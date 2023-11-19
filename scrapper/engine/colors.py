import cv2
import numpy as np
from sklearn.cluster import KMeans
from matplotlib.colors import rgb2hex

def get_colors(driver):
    driver.execute_script("""
var elements = document.querySelectorAll('img');
elements.forEach(e => e.parentNode.removeChild(e))
""")
    driver.save_screenshot('temp/screenshot.png')

    img = cv2.imread('temp/screenshot.png')
    img = cv2.resize(img, (128, 128))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    pixels = img.reshape(-1, 3)

    kmeans = KMeans(n_clusters=5)
    kmeans.fit(pixels)

    colors = kmeans.cluster_centers_
    labels = kmeans.labels_

    _, counts = np.unique(labels, return_counts=True)
    percentages = counts / len(labels)

    color_set = list()
    for color, percentage in zip(colors, percentages):
        r, g, b = color.astype(int)
        hex_color = rgb2hex([r/255, g/255, b/255])
        color_set.append({
            'rgb': hex_color,
            'percentage': percentage
        })

    def color_percentage(color):
        return color['percentage']

    color_set.sort(reverse=True, key=color_percentage)

    colors = {
        'primary-color': None,
        'secondary-color': None,
        'accent-color': None
    }

    for i, [key, _] in enumerate(list(colors.items())):
        colors[key] = color_set[i]['rgb']

    return colors