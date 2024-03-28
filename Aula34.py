'''
Repetições 
while (Enquanto)
Executa uma ação uma condição verdadeira
Loop infinito -> Quando um código não tem fim
'''

condicao = True

while condicao:
    nome = input("Qual o seu nome: ")
    print(f'Seu nome é {nome}')

    if nome == "sair":
        break

print("Acabou")