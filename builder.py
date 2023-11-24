import re
import subprocess
import os
import time

def edit_tailwind(caminho_arquivo='web-template-engine/tailwind.config.js', primary='#ff0000', secondary='#00ff00', accent='#0000ff'):
    abs_file_path = os.path.abspath(caminho_arquivo)

    # Lê o conteúdo do arquivo
    with open(abs_file_path, 'r') as arquivo:
        conteudo = arquivo.read()

    # Edita as variáveis primary, secondary e accent
    conteudo = re.sub(r'primary:\s?.*,', f'primary: "{primary}",', conteudo)
    conteudo = re.sub(r'secondary:\s?.*,', f'secondary: "{secondary}",', conteudo)
    conteudo = re.sub(r'accent:\s?.*,', f'accent: "{accent}",', conteudo)

    # Escreve o conteúdo de volta no arquivo
    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.write(conteudo)

def build_project(caminho_pasta="web-template-engine"):
    abs_file_path = os.path.abspath(caminho_pasta)

    # Muda para a pasta do projeto
    os.chdir(abs_file_path)

    # Executa npm run build
    subprocess.run(['npm', 'run', 'build'])

    time.sleep(5)