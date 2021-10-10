import matplotlib.pyplot as plt
import numpy as np
to=20
tf=1000
m=1.77
al=0.0039
ce=385#1.7*pow(10, -8)
I=387
rf=0
ro=0.309
DTr=0
DT=0
n=0
#arr = np.array([1,2,3])
tiempo=[]
temper=[]
while n<1000:
    rf=ro*(1 + al*DTr)
    t=(m*ce*DTr)/(pow(I, 2)*rf)
    n=n+1
    DTr=DTr+1
    print('Temp: '+ str(DTr+19) + '/ tiempo: '+ str(t) + ' Resist: '+ str(rf))
    #np.append(arr, t)
    Temp=DTr+19
    tiempo.append(t)
    temper.append(Temp)

#print(tiempo)
#print(temper)

plt.plot(tiempo, temper)
plt.show()
#for i in range(0, 10, 2):
#    l=m*i   
#    print(l)