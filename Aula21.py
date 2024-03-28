# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições 
# precisam ser verdadeiras
# Se qualquer valor for 
# considerado falso a expressão inteira será avaliada naquele valor
# São coniderados falsy (vc já viu
# 0 0.0 '' false
# Também existe o tipo None que é
# usado para representar um não valor

Entrada = input('[E]ntrar [S]air:  ')
Senha_digitada = input("Senha: ")

Senha_permitida = "123456"
# if True:
if Entrada == "E" and Senha_digitada == Senha_permitida:
    print("Entrar")
else:
    print("Sair")


# Avaliação de curto circuito
print (True and False and True)
# Ele para na condição 


