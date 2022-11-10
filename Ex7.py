n=1
soma = 0
cont = 0
verificador = 0

while n > 0:
    n = int(input("Insira um número: "))

    if verificador == 0:
        maior = n
        menor = n
        verificador += 1
    if n != 0:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        soma = soma + n
        cont = cont + 1

print("\n\nMaior: {}\nMenor: {}\nQuantidade de valores informados: {}".format(maior, menor, cont))
print("Soma: {}\nMédia: {}\n".format(soma, soma/cont))