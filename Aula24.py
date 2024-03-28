# Operadores in e not in
# String são iteráveis
# 0 1 2 3 4 5 6
# f a m i l i a
#-7-6-5-4-3-2-1

nome = "familia"
print(nome [2])
print(nome[-7])
print("vio" in nome)
print("ia" in nome)

nome_n = input("Digite seu nome:  ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in nome_n:
    print(f"{encontrar} está em {nome_n}")
else:
    print(f"{encontrar} não está em {nome_n}")