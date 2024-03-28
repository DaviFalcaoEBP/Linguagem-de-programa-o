"""
Iterável -> str, range, etc (__iter___)
iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador

"""
# fot letra in texto
texto = iter("Luiz") # iterável
ITERADOR = iter (texto) # iterador (Automático)

while True:
    try:
        letra = next(ITERADOR)
        print(letra)
    except StopIteration:
        break
        ...