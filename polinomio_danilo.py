#-*-coding:cp1252-*-
import numpy as np 
import matplotlib.pyplot as plt

#Intro: apresenta o programa
print("Este programa, uma atividades de Problemas Integrados")
print("calcula o valor do X que você decidir, de um polinôomio qualquer,")
print("e depois gera seu gráfico")
print("------------------------------------------------------------")


#1a parte: Lista de N
#Gera o vetor  dos numeros inteiros (que vão de 0 à N, indo de 1 em 1) que X será elevado
#e guarda os coeficientes pra cada um deles
n_g=int(input("Por favor, diga qual o grau do polinômio: "))
n=n_g+1
lista_pol=np.linspace(0,n_g,n)
coef=np.linspace(0,0,n)
ini=list(range(n))
print("Favor digite o coeficiente de")
for indice in ini:
  print("X elevado à %i:"%(indice))
  coef[indice]=float(input("--> "))

#2a parte: Calculo pedido de f(x)
#Gera um vetor com todos os valores iguais a X, depois os eleva ao numero respectivo e multiplica pelo coeficiente
#somando todos os valores do vetor resultante no final, obtendo assim f(x)
x_i=float(input("Diga o valor do x que quer calcular: "))
x=np.linspace(0,0,n)
for indice in ini:
  x[indice]=x_i
pol=np.sum(coef*x**(lista_pol))
print("O valor obtido para o seu x foi: %f"%(pol))
print("------------------------------------------------------------")

#3a parte: Plot do gráfico
#Gera um vetor crescente com grande numero de elementos, e calcula(em outro vetor com range igual) o f(x) pra cada um deles
#depois plota  o gráfico de X em função de Y
x_graf=np.linspace(-10*n,10*n,100*n)
y_graf=np.linspace(0,0,100*n)
ini2=list(range(100*n))
for indice in ini2:
  y_graf[indice]=np.sum(coef*(x_graf[indice]**(lista_pol)))
plt.plot(x_graf,y_graf)
plt.title("O gráfico da sua função é: ")
plt.xlabel("Valores de X")
plt.ylabel("Valores de f(x)")
plt.show()
#***Programa por Danilo de Paula***
