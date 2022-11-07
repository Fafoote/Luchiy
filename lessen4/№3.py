a=int(input('Введите число   '))
b=int(input('Введите максимальное число   '))
c=int(input('шаг   '))
i=a
print(f'{a}:{b}:{c}')
if a<b:
    if c>0:
        while i<b:
            print(i)
            i=i + c
    else:
        print('ERROR  404')
else:
    if c<0:
        
        while i>b:
            print(i)
            i=i + c
    else:
        print('ОШИБКААААААААААААААААА')