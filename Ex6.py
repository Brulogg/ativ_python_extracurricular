N = int(input("Insira um número: "))

if N < 100:
    print("Mínimo é 100!!")
    quit()
i=1
soma=0
while i < N:
    if i%2==0:
        soma = soma + i
    i = i + 1

print("A somatória dos números pares de 1 a {} é de {}".format(N,soma))