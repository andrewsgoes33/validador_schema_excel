from pydantic import BaseModel, Field
from datetime import datetime


class Vendas(BaseModel):
    ID_Pedido: str = Field(alias="ID Pedido")
    Data_Pedido: datetime = Field(alias="Data Pedido")
    Data_Envio: datetime = Field(alias="Data Envio")
    Modo_Envio: str = Field(alias="Modo Envio")
    Prioridade_Pedido: str = Field(alias="Prioridade Pedido")