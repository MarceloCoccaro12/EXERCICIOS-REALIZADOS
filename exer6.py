a = float(input('Primeiro lado: '))
b = float(input('Segundo lado: '))
c = float(input('Terceiro lado: '))
    
    
if (a == b) and (a == c) :
        print('Isósceles')
elif (a==b) or (a==c) or (b==c):
        print('Equilatero')
else:
        print('Escaleno')