num = {0: 568, 1: 283, 2: 944, 3: 427, 4: 722, 5: 801, 6: 222, 7: 956
, 8: 335, 9: 510, 10: 105, 11: 921, 12: 595, 13: 416, 14: 264, 15: 231, 16: 653,
17: 641, 18: 891, 19: 297, 20: 784, 21: 122, 22: 379, 23: 179,
 24: 706, 25: 725, 26: 367, 27: 824, 28: 752}
maior = 0
menor = 9999
i = 0
while len(num) > i:
    print(num[i])
    if num[i] > maior:
        maior = num[i]
    elif num[i] < menor:
        maior = num[i]
    i += 1
print(maior, 'é o maior valor desta lista')
print(menor, 'é o menor valor desta lista')