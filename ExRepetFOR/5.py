quantidade = 0
for num in range(5,101):

    if (num % 7 == 0 and num % 5 != 0):
        print(num)
        quantidade +=1

print('essa é a quantidade',quantidade)
