# coding: utf-8

#Import das bibliotecas e import do arquivo a08.txt para a pasta
import numpy as np
import matplotlib.pyplot as plt
#get_ipython().magic('cat a08.txt') #-->Disponível somente no ambiente python do IAG

#Pega as linhas e colunas com valores numéricos do arquivo a08.txt
#  e transforma as linhas em variáveis
mes,Rio_de_Janeiro,Fortaleza=np.loadtxt("a08.txt", usecols=range(1,13))

#Declaração das variáveis fixas
P=365 #(Período total em dias)
Dias=30.5*mes-30.5/2. #(Vetor com o dia de cada ponto)
z_sup=0 #(Profundidade em metros)
D=5.73  #(Dumping depth em metros)
A_Rio=2.69 #(Amplitude da curva para Rio de Janeiro)
A_Fortaleza=0.87 #(Amplitude da curva para Fortaleza)
Phi_Rio=-(np.pi/0.595) #(Fator de deslocamento da curva para Rio de Janeiro)
Phi_Fortaleza=-(np.pi/.700)  #(Fator de deslocamento da curva para Fortaleza)
To_Rio=(np.sum(Rio_de_Janeiro)/len(Rio_de_Janeiro))+0.15 #(Temperatura média do Rio de Janeiro)
To_Fortaleza=(np.sum(Fortaleza)/len(Fortaleza))-0.05 #(Temperatura média de Fortalezza)

#Fórmulas da temperatura em função da profundidade e periodo do ano para cada cidade
T_Rio=(To_Rio+A_Rio*np.sin(2*np.pi*Dias/P+Phi_Rio-z_sup/D)*np.exp(-z_sup/D)) 
T_Fortaleza=(To_Fortaleza+A_Fortaleza*np.sin(2*np.pi*Dias/P+Phi_Fortaleza-z_sup/D)*np.exp(-z_sup/D))

#Construção do gráfico
plt.plot(Dias,T_Rio,'k-',label='Rio de Janeiro') #(Curva da Temperatura calculada do Rio de Janeiro)
#plt.plot(Dias,Rio_de_Janeiro,'k:',label='Pontos RJ')  #(Curva dos pontos inicias para ajuste de curva do Rio de Janeiro)
plt.plot(Dias,T_Fortaleza,'k--',label='Fortaleza') #(Curva da Temperatura calculada de Fortaleza)
#plt.plot(Dias,Fortaleza,'k:',label=' Pontos Fortaleza') #(Curva dos pontos inicias para ajuste de curva de Fortaleza)
plt.legend() #(Legenda)
plt.xlabel("Tempo (dias)") #(Nomeação do eixo X)
plt.ylabel("Temperatura (°C)") #(Nomeação do eixo Y)
plt.grid(True) #(Coloca o grid)
plt.title('Temperatura x Tempo, para Superfície') #(Título)
plt.show() #(Plota)

#Avalia as diferenças de temperatura para diferentes profundidades
n_p=100 #numero de profundidades que você pode avaliar (Utilizei algo em torno de 51 a 201 pontos para cada análise)
z_p=np.linspace(0,20,n_p) #vetor contendo as prfundidades que vão de 0 a 20 (No caso eu usei do 0 a 10, e de 10 a 20)
for h in z_p: #Laço que possibilita a análise para cada profundidade do vetor
    print("--------------------")
    print(h, "Metros") #Indica a profundidade analisada
    h_T_Rio=(To_Rio+A_Rio*np.sin(2*np.pi*Dias/P+Phi_Rio-h/D)*np.exp(-h/D)) #Temperatura do RJ na profundidade analisada
    h_T_Fortaleza=(To_Fortaleza+A_Fortaleza*np.sin(2*np.pi*Dias/P+Phi_Fortaleza-h/D)*np.exp(-h/D)) #Temperatura de Fortaleza na profundidade analisada
    Delta_T_Rio=h_T_Rio-T_Rio #Diferença de Temperatura entre a superfície e a profundidade para RJ
    Delta_T_Fortaleza=h_T_Fortaleza-T_Fortaleza #Diferença de Temperatura entre a superfície e a profundidade para Fortaleza
    #OBS: Valores positivos de Delta_T significa que a profundidade esta mais quente que a superfície e vice-versa
    print(Delta_T_Rio, "Graus Rio") #Printa os valores de Delta_T do RJ
    print("....  .....    ....")
    print(Delta_T_Fortaleza,"Graus Fortaleza") #Printa os valores de Delta_T do RJ

    np.savetxt('testfile.txt', Delta_T_Rio)   
    np.savetxt('testfile.txt', Delta_T_Fortaleza)  
 
#Código por Danilo de Paula, N°USP 10314732.
