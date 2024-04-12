temp=float(input("Digite o valor de temperatura que deseja:"))
print("Qual qual conversão prefere fazer?")
print("Celsius para Fahrenheit(F) ou Fahrenheit para Celsius(C)")
opcao=input()

if (opcao=='F'):
    conta= (temp*9/5)+32
elif (opcao=='C'):
    conta= (temp-32)/(9/5)

print("A temperatura é de:{:.1f}".format(conta))
