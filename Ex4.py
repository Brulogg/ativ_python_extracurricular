N = int(input("Insira a quantidade N: "))
i=1

while i<=N:
    n = float(input("Insira os números reais: "))
    if n > 0:
        if i == 1:
            maior = n
            menor = n
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        i = i + 1
    else:
        print("Número inválido")

print("Maior: {}\nMenor: {}".format(maior,menor))