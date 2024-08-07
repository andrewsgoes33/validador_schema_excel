from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.service import Service
from time import sleep
import pytest
import subprocess

@pytest.fixture

def driver():
    # Iniciar o Streamlit em background
    process = subprocess.Popen(["streamlit", "run", "src/app.py"])

    # Iniciar o WebDriver usando GeckoDriver
    driver = webdriver.Firefox()
    driver.set_page_load_timeout(5)
    yield driver

    # Fechar o WebDriver e o Streamlit após o teste
    driver.quit()
    process.kill()

def test_app_opens(driver):
    # Verificar se a página abre
    driver.get("http://localhost:8501")
    sleep(5)

def test_check_title_is(driver):
    # Verificar se a página abre
    driver.get("http://localhost:8501")
    # Verifica se o titulo de página é
    sleep(5)
    # Capturar o título da página
    page_title = driver.title

    # Verificar se o título da página é o esperado
    expected_title = "Validador de schema excel"  # Substitua com o título real esperado
    assert page_title == expected_title, f"O título da página era '{page_title}', mas esperava-se '{expected_title}'"
    
from selenium.webdriver.common.by import By

def test_check_streamlit_h1(driver):
    # Acessar a página do Streamlit
    driver.get("http://localhost:8501")

    # Aguardar para garantir que a página foi carregada
    sleep(5)  # Espera 5 segundos

    # Capturar o primeiro elemento <h1> da página
    h1_element = driver.find_element(By.TAG_NAME, "h1")

    # Verificar se o texto do elemento <h1> é o esperado
    expected_text = "Insira o seu excel para validação"
    assert h1_element.text == expected_text


# # Precisamos definir qual driver vamos utilizar
# service = Service('C:/geckodriver/geckodriver.exe')
# driver = webdriver.Firefox(service=service)

# # Define um timeout implícito
# driver.set_page_load_timeout(5)  # 5 segundos

# # Vamos fazer uma tratativa de try-except de entrar na nossa página
# try:
#     driver.get("http://localhost:8501")
#     sleep(5)
#     print("Acessou a página com sucesso")
# except TimeoutException:
#     print("Tempo de carregamento da página excedeu o limite.")
# finally:
#     driver.quit()