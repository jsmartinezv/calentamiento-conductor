import matplotlib.pyplot as plt
import numpy as np
m=1.77    # masa
al=0.0039 # coeficiente termico de resistividad cobre 
ce=385    # calor especifico cobre
I=387     # I_cc
rf=0      
ro=0.309  # resistencia conductor a temperatura ambiente   
DTr=0     # Delta de temperatura     
tiempo=[] ### inicializacion arrays usados para graficar
temper=[]
resist=[]
while DTr<1000: # bucle de iteración
    rf=ro*(1 + al*DTr)  # calculo de la resistencia variable
    t=(m*ce*DTr)/(pow(I, 2)*rf) # calculo del tiempo de calentamiento
    DTr=DTr+1
    print('Temp: '+ str(DTr+19) + '/ tiempo: '+ str(t) + ' Resist: '+ str(rf))
    Temp=DTr+19
    tiempo.append(t)  ### agregar datos a los arreglos
    temper.append(Temp)
    resist.append(rf)
# grafico 1 temperatura - resistencia
plt.title("Efecto de la temperatura sobre la resistencia")
plt.xlabel("Temperatura [^oC]")
plt.ylabel("Resistencia [Ohms]")
plt.plot(temper, resist)
plt.show()
# grafico 2 temperatura - tiempo
plt.title("Curva caracteristica: tiempo de calentamiento de línea de tx \n Cu, 60 m , 12 AWG, 387 A ")
plt.ylabel("Temperatura [^oC]")
plt.xlabel("Tiempo [s]")
plt.plot(tiempo, temper)
plt.show()