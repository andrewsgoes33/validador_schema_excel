import pytest
from datetime import datetime
from src.contrato import Vendas
from pydantic import ValidationError

# Testes com dados válidos
def test_vendas_com_dados_validos():
    dados_validos = {
        "ID Pedido": "CA-2012-124891",
        "Data Pedido": datetime.strptime("2012-07-31 00:00:00", "%Y-%m-%d %H:%M:%S"),
        "Data Envio": datetime.strptime("31-07-2012", "%d-%m-%Y"),
        "Modo Envio": "Mesmo Dia",
        "Prioridade Pedido": "Critico",
    }

    # A sintaxe **dados_validos é uma forma de desempacotamento de dicionários em Python. 
    # O que isso faz é passar os pares chave-valor no dicionário dados_validos como argumentos nomeados para o construtor da classe Vendas.

    venda = Vendas(**dados_validos)

    assert venda.ID_Pedido == dados_validos["ID Pedido"]
    assert venda.Data_Pedido == dados_validos["Data Pedido"]
    assert venda.Data_Envio == dados_validos["Data Envio"]
    assert venda.Modo_Envio == dados_validos["Modo Envio"]
    assert venda.Prioridade_Pedido == dados_validos["Prioridade Pedido"]
   

# # Testes com dados inválidos
# def test_vendas_com_dados_invalidos():
#     dados_invalidos = {
#         "email": "comprador",
#         "data": "não é uma data",
#         "valor": -100,
#         "produto": "",
#         "quantidade": -1,
#         "categoria": "categoria3"
#     }

#     with pytest.raises(ValidationError):
#         Vendas(**dados_invalidos)

# # Teste de validação de categoria
# def test_validacao_categoria():
#     dados = {
#         "email": "comprador@example.com",
#         "data": datetime.now(),
#         "valor": 100.50,
#         "produto": "Produto Y",
#         "quantidade": 1,
#         "categoria": "categoria inexistente",
#     }

#     with pytest.raises(ValidationError):
#         Vendas(**dados)