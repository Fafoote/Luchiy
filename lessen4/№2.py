n=int(input("Сколько рядов? ")  )
r=0
while r<n:
    if r%3==0:
        print(r*6+0)
        print(r*6+1)
        print(r*6+5)
    elif r%3==1:
        print(r*6+1)
        print(r*6+2)
        print(r*6+5)
    else:
        print(r*6+2)
        print(r*6+3)
        print(r*6+5)
    r=r+1
