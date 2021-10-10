import matplotlib.pyplot as plt
import numpy as np
to=20
tf=1000
m=1.77
al=0.0039
ce=385#1.7*pow(10, -8)
I=387
rf=0.309
DTr=0
DT=1
n=0
arr = np.array([0])
while n<80:
    rf=rf*(1 + al*DT)
    t=(m*ce*DTr)/(pow(I, 2)*rf)
    n=n+1
    DTr=DTr+1
    print('Temp: '+ str(DT) + '/ tiempo: '+ str(t) + ' Resist: '+ str(rf))
    np.append(arr, t)
    print(arr)
   
#plt.plot(DT, t)
#plt.show()
#for i in range(0, 10, 2):
#    l=m*i   
#    print(l)