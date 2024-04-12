altura=float(input("Digite a altura (em metros): "))
largura=float(input("Digite a largura (em metros): "))
comprimento=float(input("Digite o comprimento (em metros): "))
consumo_medio=float(input("Digite o nível de consumo médio (em litros): "))

volume= (altura * largura * comprimento) * 1000000
capaci_litros= volume / 1000 

autonomia_dias= volume / consumo_medio

if (autonomia_dias < 2):
    classificacao="Consumo elevado"

elif (2 <= autonomia_dias <= 7):
    classificacao="Consumo moderedo"

else:
    classificacao="Consumo reduzido"

print("Capacitade total do reservatório:", capaci_litros, "litros")
print("Autonomia do reservatório:", autonomia_dias, "dias")
print("Classificação do consumo:", classificacao)
