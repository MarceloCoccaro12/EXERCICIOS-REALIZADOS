precot=float(input("Valor da refeição:"))
atendim=input("Nível de serviço recebido (bom, regular ou ruim)")

if (atendim=="bom") or (atendim=="Bom"):
    novopreco= precot*1.20

if (atendim=="regular") or (atendim=="Regular"):
    novopreco= precot*1.15

if (atendim=="ruim") or (atendim=="Ruim"):
    novopreco= precot*1.10

print("Novo preço é: {:.2f}".format(novopreco))