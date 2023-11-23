import subprocess
import time
from selenium import webdriver
from nturl2path import pathname2url
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os


def capture_screenshot():
    # Iniciar o servidor HTTP com http-server
    http_server_process = subprocess.Popen(['http-server', 'web-template-engine/dist'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Aguardar alguns segundos para garantir que o servidor está pronto
    time.sleep(5)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Navegar para o arquivo local
    driver.get('http://localhost:8081')

    # Executar um script JavaScript para ocultar a barra de rolagem
    script = "document.documentElement.style.overflow='hidden';"
    driver.execute_script(script)

    # Aguarde um tempo para garantir que a página foi totalmente carregada (pode ser ajustado conforme necessário)
    time.sleep(5)

    # Tirar uma captura de tela
    driver.save_screenshot('temp/teste.png')

    # Encerrar o servidor HTTP
    http_server_process.terminate()
    http_server_process.wait()

    # Fechar o navegador
    driver.quit()

capture_screenshot()