from turtle import *
import time
t=Turtle()
t.speed(0)
l=["purple","red","orange","blue","green"]
for i in range(2500):
    t.color(l[i%5])
    t.pensize(i//10+1)
    t.forward(i)
    t.left(59)
#t.circle(50,steps=10)
getscreen().getcanvas().postscript(file='outputname.ps')
print("done")
time.sleep(10000)