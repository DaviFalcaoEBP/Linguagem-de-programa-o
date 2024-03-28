'''
Cuidados com dados mutáveis
= - copiando o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
'''

lista_a = ["Luiz", "Maria"]
lista_b = lista_a.copy()

lista_a[0]= "Qualquer coisa"

print (lista_b)