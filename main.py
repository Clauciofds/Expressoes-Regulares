import requests

from Telefones import TelefoneBr
from datasb_br import DataBr
from acesso_cep import BuscaEndereco
import re


telefone = '2019942585500'

telefone_objeto = TelefoneBr(telefone)
print(telefone_objeto)

cadastro = DataBr()

print(cadastro.format_data())

hoje = DataBr()
print(hoje.tempo_cadastro())

cep = "13843204"
objeto_cep = BuscaEndereco(cep)


r = requests.get('https://viacep.com.br/ws/13843204/json/')
print(r.text)

a = objeto_cep.acessa_via_cep()
# print(type(a.text))
# print(type(a.json()))
# print(a.json()['cep'])
# print(a.json()['bairro'])

bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro,cidade,uf)