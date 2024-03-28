"""
split e join com list e str
slit - divide uma string
join - une uma string
"""

frase = "Olha só que, coisa interessante"
lista_palavras_cruas = frase.split(",")

print (lista_palavras_cruas)


lista_palavras = []
for i, frase in enumerate (lista_palavras):
    lista_palavras[i] = lista_palavras[i].strip()
    
print (lista_palavras)