def bank(x, y):
    for i in range(1, y):
        x = x + x * 0.1
        print("Сумма в ", i + 1, " год = ", x)
    print("Сумма на конец вклада = ", x)

x = int(input("Введите сумму = "))
y = int(input("Введите срок = "))

bank(x,y)
