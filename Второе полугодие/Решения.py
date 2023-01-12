#5
for i in range(1,100):
    chislo=''
    num=(bin(i)[2:])
    if num.count('1')%2==0:
        chislo='10'+num[2:]+'0'

    if num.count('1')%2!=0:
        chislo='11'+num[2:]+'1'
    if int(chislo,2)>40:
        print (i, int(chislo,2))
        break
#6        
from turtle import *
left(90)
for i in range(7):
forward(300)
right(120)
pu()
for x in range(1,9):
for y in range(1,10):
goto(x*30,y*30)
dot(5)
done()
