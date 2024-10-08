from datetime import datetime
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from enum import Enum

# Enum para os produtos
class ProdutoEnum(str, Enum):
    produto1 = "ZapFlow com Gemini"
    produto2 = "ZapFlow com chatGPT"
    produto3 = "ZapFlow com Llama3.0"

# Classe de vendas
class Vendas(BaseModel):
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum

    


