n=int(input("Сколько рядов?"))
r=0
while r < n:
    if r%2==0:
        print(r*5+0)
        print(r*5+1)
        print(r*5+3)
        print(r*5+4)
    else:
        print(r*5+2)
    r=r+1