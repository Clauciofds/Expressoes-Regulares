import re

padrao = '[0-9][a-z][0-9]'
texto = '123 1a2 1cc aal'
resposta = re.search(padrao,texto)
print(resposta.group())

padrao = "[0-9][a-z]{2}[0-9]"
texto = "123 1ac2 1cc aa1"
resposta = re.search(padrao, texto)
print(resposta.group())

padrao = '\w{5,50}@\w{3,10}.\w{2,3}'
texto = 'aaabbbcc clauciofds@gamil.com.br ccbbbbaaa'
resposta = re.search(padrao, texto)
print(resposta.group())

padrao = '\w{5,50}@[a-z]{2,10}.com.br'
resposta = re.search(padrao, texto)
print(resposta.group())

