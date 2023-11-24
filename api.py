import os
import shutil
from zipfile import ZipFile
from flask import Flask, request, send_file
from association import associate_keywords_with_colors_and_font
from builder import edit_tailwind, build_project
from keyword_extractor import keyword_extractor
from screenshot import capture_screenshot
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/project', methods=["POST"])
def project():
    data = request.json['text']
    keywords = keyword_extractor(data)
    result = associate_keywords_with_colors_and_font(keywords, similarity_threshold=0.01)

    edit_tailwind(
        primary=result['primary-color'],
        secondary=result['secondary-color'],
        accent=result['accent-color'],
    )
    build_project()

    zip_project()

    response = send_file('temp/arquivo.zip', download_name='projeto.zip', as_attachment=True, mimetype='application/zip')

    response.headers['Cache-Control'] = 'no-store'

    return response

@app.route('/image', methods=["POST"])
def image():
    data = request.json['text']
    keywords = keyword_extractor(data)
    result = associate_keywords_with_colors_and_font(keywords, similarity_threshold=0.01)

    edit_tailwind(
        primary=result['primary-color'],
        secondary=result['secondary-color'],
        accent=result['accent-color'],
    )
    build_project()
    capture_screenshot()

    response = send_file('temp/teste.png')

    response.headers['Cache-Control'] = 'no-store'

    return response

def zip_project():
    # Caminho para a pasta dist
    folder_path = 'web-template-engine/dist'
    abs_path = os.path.abspath(folder_path)

    destination_path = os.path.abspath('temp/arquivo')

    swagger_path = 'swagger.yaml'

    # Cria um arquivo ZIP em memória
    shutil.make_archive(destination_path, 'zip', abs_path)

    myzipfile = ZipFile("temp/arquivo.zip", mode='a')
    myzipfile.write(swagger_path)
    myzipfile.close()

app.run(debug=True)
