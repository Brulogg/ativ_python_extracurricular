min = int(input("Insita o mínimo: "))
max = int(input("Insira o máximo: "))

if min > max:
    print("Erro")
    quit()

while min <= max:
    if min%5==0:
        print("{}".format(min))
    min = min + 1