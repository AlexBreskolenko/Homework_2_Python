dictionary = {'AEIOULNSTRАВЕИНОРСТ' : 1, 'DGДКЛМПУ' : 2, 'BCMPБГЁЬЯ': 3, 'FHVWYЙЫ' : 4, 'KЖЗХЦЧ' : 5, 'JXШЭЮ' : 8, 'QZФЩЪ' : 10}

word = input("Введите слово : ")

sum = 0

for i in word.upper():
    for j in dictionary.keys():
        if i in j:
            sum += dictionary.get(j)

print("{} -> {}".format(word, sum))