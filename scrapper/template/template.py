from jinja2 import Environment, FileSystemLoader
import webbrowser
import tempfile

# # Criar o ambiente Jinja2
# env = Environment(loader=FileSystemLoader('.'))
# # Carregar o template HTML
# template = env.get_template('template.html')

# # Renderizar o template com as variáveis
# output = template.render(teste=teste)

# # Escrever o conteúdo renderizado em um arquivo HTML temporário
# with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.html') as temp_file:
#     temp_file.write(output)
#     temp_file_path = temp_file.name

# # Abrir o arquivo HTML no navegador padrão
# webbrowser.open('file://' + temp_file_path)

def open_template(colors, fonts, products, image_path):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')
    output = template.render(colors=colors, fonts=fonts, products=products, image_path=image_path)

    # Escrever o conteúdo renderizado em um arquivo HTML temporário
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.html') as temp_file:
        temp_file.write(output)
        temp_file_path = temp_file.name

    # Abrir o arquivo HTML no navegador padrão
    webbrowser.open('file://' + temp_file_path)

