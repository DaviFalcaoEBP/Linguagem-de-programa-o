Entrada = input('[E]ntrar [S]air:  ')
Senha_digitada = input("Senha: ")

Senha_permitida = "123456"
# if True:
if (Entrada == "E" or Entrada == "e") and Senha_digitada == Senha_permitida:
    print("Entrar")
else:
    print("Sair")

# Avaliação de curto circuito
print (True or False or 0 or "ABC")
print (0.0 or False or 0 or "ABC")