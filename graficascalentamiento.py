to=20
tf=1000
m=1.77
al=0.0039
ce=385#1.7*pow(10, -8)
I=387
ro=0.309
DTr=0
DT=1
n=0
while n<80:
    rf=ro*(1+al*DTr)
    t=(m*ce*DT)/(pow(I, 2)*rf)
    n=n+1
    DT=DT+1
    print('Temp: '+ str(DT) + '/ tiempo: '+ str(t) + ' Resist: '+ str(rf))
    
#for i in range(0, 10, 2):
#    l=m*i   
#    print(l)