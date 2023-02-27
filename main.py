from Telefones import TelefoneBr
from datasb_br import DataBr
import re


telefone = '2019942585500'

telefone_objeto = TelefoneBr(telefone)
print(telefone_objeto)

cadastro = DataBr()

print(cadastro.format_data())