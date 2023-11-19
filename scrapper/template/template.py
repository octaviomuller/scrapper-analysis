import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from jinja2 import Environment, FileSystemLoader, Template
import webbrowser
import tempfile

def open_template(colors, fonts, products, image_path):
    with open(f'{os.path.abspath(os.path.join(os.path.dirname(__file__)))}/template.html.jinja2') as file_:
        template = Template(file_.read())
    output = template.render(colors=colors, fonts=fonts, products=products, image_path=image_path)

    # Escrever o conteúdo renderizado em um arquivo HTML temporário
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.html') as temp_file:
        temp_file.write(output)
        temp_file_path = temp_file.name

    # Abrir o arquivo HTML no navegador padrão
    webbrowser.open('file://' + temp_file_path)

