N = int(input("Введите число N : "))

list_2 = [i for i in range(1, N + 1)]
print(*list_2)

X = int(input("Введите число X : "))

for i in list_2:
    if i == X + 1:
        print("-> {}".format(i))
        break
    elif i == X - 1:
        print("-> {}".format(i))
        break          