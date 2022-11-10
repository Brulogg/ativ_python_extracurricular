n = int(input("Insira um número: "))
i = 2

while i < n:
    if n%i != 0:
        i += 1
    else:
        print("\nO número {} não é primo.".format(n))
        quit()

print("\nO número {} é primo".format(n))