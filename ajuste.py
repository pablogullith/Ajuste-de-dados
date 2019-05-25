"""Se analisarmos, o gráfico exponencial serve muito bem para o decaimento de 
pions. Quando linearizamos, tornamos o valor de vida média bem abrupta em relação
ao achado teoricamente"""
#Bibliotecas
#Autor: Pablo Gullith
from scipy.optimize import curve_fit
from numpy import arange, exp, loadtxt, mean, log
from pylab import plot, show, xlabel, ylabel


dados = loadtxt("decay.data", float)
x = dados[:,0]
y = dados[:,1]

def f(x, a, b):
    return a*exp(-b*x)

param, pcov = curve_fit(f, x, y)
x_axis = []
y_axis = []

#Laço
for i in arange(0, 120, 1):

    x_axis.append(i)
    y_axis.append(f(i, param[0], param[1]))

z = log(y)

def g(x,x1,z):
   
    zm = mean(z)
    xm = mean(x)
    
    s1 = 0.0
    s2 = 0.0
    n = x1.size
    
    
    for i in range(n):
        
        s1 = s1 + x1[i]*(z[i] - zm)
        s2 = s2 + x1[i]*(x1[i] - xm)
    
    m = s1/s2
    a = zm - m*xm
    h = m*x + a,m
    return h

L,b = g(x,x,z)
t = -1/b

#Plots e prints
print('VALOR DE VIDA MÉDIA:',1/param[1],'ns')
print("\nVALOR DE VIDA MÉDIA:",t,"ns")
xlabel("Tempo(ns)")
ylabel("Número")
plot(x, y, "ko")
plot(x_axis, y_axis,'m')
show()
plot(x,L,'m')
plot(x,z,"ko")
xlabel("Tempo(ns)")
ylabel("Log(número)")
show()