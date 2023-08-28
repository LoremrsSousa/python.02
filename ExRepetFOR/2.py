nmaior = 0
nmenor = 0
for num in range (1,11):
     n = int(input('digite um número inteiro: '))
     if num == 1:
         nmaior = n
         nmenor = n

else:
    if n > nmaior:
        nmaior = n
    elif n < nmenor:
         nmenor = n
print('O maior é: ', nmaior)
print('O menor é: ', nmenor)