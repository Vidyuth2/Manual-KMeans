from matplotlib import pyplot as blt
import numpy as np
import random

x2 = 1+np.random.rand(40)
x1 = np.random.rand(50)-1
y2 = 1+np.random.rand(40)
y1 = np.random.rand(50)-1
main = list(map(lambda e,f: [e,f], x1,y1))
main2 = list(map(lambda e,f:[e,f], x2,y2))
for i in main2:
    main.append(i)



blt.scatter(x1,y1)
blt.scatter(x2,y2)

class line:
    def __init__(self, p1, p2):
        self.m = (p1[0]-p2[0])/(p2[1]-p1[1])
        self.p = np.array([(p1[0]+p2[0])/2, (p2[1]+p1[1])/2])
        self.b = self.p[1]-(self.p[0]*self.m)
       
    def return_val(self, x):
        return (self.m*x)+self.b

p1, p2 = np.array([random.random(), random.random()*2]), np.array([random.random()*2, random.random()])
blt.scatter(p1[0], p1[1], c = "b")
blt.scatter(p2[0], p2[1], c = "g")


tu = True
def iterate(p1, p2):
    test = line(p1.astype(float), p2.astype(float))
    blt.plot(p1[0], p1[1])
    blt.plot(p2[0], p2[1])
    for i in main:
        blt.scatter(i[0], test.return_val(i[0]), c = "r")
        
    above = [i for i in main if i[1]>test.return_val(i[0])]
    below = [i for i in main if i[1]<test.return_val(i[0])]
    
    t = 0
    for i in main:
        if test.return_val(i[0])<i[1]+0.1 and test.return_val(i[0])>i[1]-0.1:
            t+=1
    if t == 0:
        global tu
        tu = not tu
        if tu == True:
            temp = [i[0] for i in main]
            blt.plot(temp, [test.return_val(i) for i in temp])
            for i in(p1,p2):
                blt.scatter(i[0],i[1], c = "m")
                
            return
           
    px1 = 0
    py1 = 0
    for i in above:
        px1+=i[0]
        py1+=i[1]
    point1 = np.array([px1/len(above),py1/len(above)])
    px2, py2 = 0,0
    for i in below:
        px2+=i[0]
        py2+=i[1]
    point2 = np.array([px2/len(below),py2/len(below)])
    iterate(point1,point2)
iterate(p1,p2)
blt.show()
