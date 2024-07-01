# 12)Leia um numero inteiro e imprima a soma do sucessor de seu triplo com o antecessor de ´
#seu dobro


# resolução 

n = int(input("digite um numero inteiro Qualquer : "))
triplo =int(3*(n+1))
dobro = int(2*(n-1))

soma =int(triplo+dobro)

print(f" A Soma de  {triplo} com {dobro} é {soma} ")