#Autor: Pablo gullith
#Bibliotecas
from numpy import *
from scipy.optimize import *
from pylab import *

dados = loadtxt("scattering.data")
x = dados[:,0]
y = dados[:,1]
erro = dados[:,2]

def funcao(e,fr,er,g):
    return fr/((e - er)**2 + g**2/4)

param,pcov = curve_fit(funcao,x,y)

fr = param[0]
er = param[1]
g = param[2]
en = linspace(0,200,1000)
f = funcao(en,fr,er,g)

#Plots
plot(x,y,"ko")
plot(en,f,"m")
xlabel("Energia (MeV)")
ylabel("Seção Transversal")
show()
clf()
print("")
print("VALOR DE ER:",er)
print("")
print("VALOR DE GAMA:",g)

param,pcov = curve_fit(funcao,x,y,sigma=erro)

fr = param[0]
er = param[1]
g = param[2]
f = funcao(en,fr,er,g)

#Plots
plot(x,y,"ko")
plot(en,f,"m")
xlabel("Energia (MeV)")
ylabel("Seção Transversal")
show()
print("")
print("NOVO VALOR DE ER:",er)
print("")
print("NOVO VALOR DE GAMA:",g)

#Prints e Plots
errorbar(x,y,yerr=erro,fmt="ko",capsize=5)
plot(en,f,"m")
plot(x,y,"ko")
xlabel("Energia (MeV)")
ylabel("Seção Transversal")
show()
clf()

#Alguns comentários
"""
- Não obtemos uma informação tão importante com o gráfico das barras de erro, isso por causa do ajuste atual que
não possue tanta significância estatística. Se olharmos direito, iremos perceber que as barras de erro não são
proporcionais, elas estão maiores que os dados que nos foi fornecido. Agora é importante lembrar que as barras de erro
no final do intervalo não são maiores se tu comparas com as do centro. sabemos que o experimento de neutrons não permite
ti ter valores próximos de zero, sendo assim a lorentziana ajustada dá uma certa credibilidade. 

- Se olharmos bem, iremos ver que no ajuste sem erros os valores dados para Er e gamma estão pouco mais distantes
do valor real. Sabemos que o gamma na lorentziana está ao quadrado, o código feito encontrou o fitting mais plausível
levando em consideração os valores negativos do parametro. Quando adicionamos uma barra de erros, o python achou um fitting
que acertou o sinal do parametro gamma e achou um valor mais plausível para Er.

"""


