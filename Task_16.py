N = int(input("Введите число N : "))
list_1 = [i for i in range(1, N + 1)]

print(*list_1)

X = int(input("Введите число X : "))
count = 0

for i in list_1:
    if i == X:
        count += 1

print("-> {}".format(count))
