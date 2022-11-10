n = int(input("Insira um número: "))
i = 1
x = 0
y = 1

while i <= n:
    if i == 1:
        print(x)
    elif i == 2:
        print(y)
    else:
        resp = x+y
        print(resp)
        x=y
        y=resp
    i += 1