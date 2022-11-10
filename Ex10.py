n = int(input("Insira um número: "))
Prim = int(input("Insira o número Prim: "))
i = 1
x = 0
y = 1
soma = 0

while soma <= Prim:
    soma = x+y
    x=y
    y=soma

while i <= n:
    if i == 1:
        print(soma)
    else:
        resp = x+y
        print(resp)
        x=y
        y=resp
    i += 1