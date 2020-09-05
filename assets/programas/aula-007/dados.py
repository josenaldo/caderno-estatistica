import random
from tabulate import tabulate

numero_de_lancamentos = int(input("Informe o número de lançamentos: "))
lancamentos = []
frequencia_absoluta = [0,0,0,0,0,0]
frequencia_absoluta_acumulada = [0,0,0,0,0,0]
frequencia_relativa = [0,0,0,0,0,0]
frequencia_relativa_acumulada = [0,0,0,0,0,0]

# lançamentos e calculo da frequencia absoluta
for i in range(numero_de_lancamentos):
    lancamento = random.randrange(1, 7)
    lancamentos.append(lancamento)

    frequencia_absoluta[lancamento -1] = frequencia_absoluta[lancamento -1] + 1

# calculo da frequencia relativa
faa = 0
fra = 0
for i in range(6):
    faa = faa + frequencia_absoluta[i]
    frequencia_absoluta_acumulada[i] = faa

    frequencia_relativa[i] = frequencia_absoluta[i] / numero_de_lancamentos
    fra = fra + frequencia_relativa[i]
    frequencia_relativa_acumulada[i] = fra

# exibir tabela de frequencias
cabecalho = ["Face","(f)","(fa)","(fr)","(fra)"]
categorias = ["1","2","3","4","5","6"]

# montar tabela
tabela_crua = []

for i in range(6):
    tabela_crua.append([
        categorias[i],
        frequencia_absoluta[i],
        frequencia_absoluta_acumulada[i],
        frequencia_relativa[i],
        frequencia_relativa_acumulada[i]
    ])

tabela_formatada = tabulate(tabela_crua, headers=cabecalho, tablefmt='orgtbl')

print (tabela_formatada)

# lançar dados
# guardar resultados dos dados
# montar tabela de frequencia