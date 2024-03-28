"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

'''td_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1


print('Acabou')'''

import random

# Parâmetros do Biorreator
num_lotes = 5
tempo_fermentacao = 48  # horas

# Função para simular a produção de etanol
def simulate_producao_etanol(concentracao_acucar, temperatura, ph):
    # Modelo simplificado de produção de etanol
    eficiencia_fermentacao = random.uniform(0.8, 1.0)
    producao_etanol = eficiencia_fermentacao * concentracao_acucar * (1 + 0.1 * (temperatura - 30)) / (1 + 0.2 * abs(ph - 6.5))
    return producao_etanol

# Loop externo: Lotes (Fermentações)
for lote in range(1, num_lotes + 1):
    print(f"Iniciando lote {lote}")

    # Parâmetros iniciais do lote
    concentracao_acucar_inicial = random.uniform(50, 100)  # g/L
    temperatura_inicial = random.uniform(28, 32)  # °C
    ph_inicial = random.uniform(6.2, 6.8)

    # Loop interno: Tempo de fermentação
    for hora in range(1, tempo_fermentacao + 1):
        # Simulação do processo de fermentação
        producao_etanol = simulate_producao_etanol(concentracao_acucar_inicial, temperatura_inicial, ph_inicial)

        # Atualização dos parâmetros para a próxima iteração
        concentracao_acucar_inicial -= 0.5  # Consumo de açúcar
        temperatura_inicial += random.uniform(-0.5, 0.5)  # Variação aleatória de temperatura
        ph_inicial += random.uniform(-0.05, 0.05)  # Variação aleatória de pH

        # Exibindo informações
        print(f"Lote {lote}, Hora {hora}: Produção de Etanol={producao_etanol:.2f} g")

    print(f"Finalizando lote {lote}")

print("Processo de fermentação concluído.")