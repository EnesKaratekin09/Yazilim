import random
secimler=[0,1,2]
i = 1
t=0
z=0
y=0
while i <= 10000000:
    i += 1
    a=random.choice(secimler)
    if a ==2:
        t += 1
    elif a ==1:
        z +=1
    elif a ==0:
        y += 1
print(t)
print(z)
print(y)
