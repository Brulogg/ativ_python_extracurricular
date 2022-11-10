x=1
while x != 0:
    x = int(input("Insira o número: "))
    if x == 0:
        quit()
    elif x%2==0 and x%3==0:
        print("O número {} é divisível por 2 e 3.".format(x))
    else:
        print("O múmero {} não é divisível por 2 e 3.".format(x))