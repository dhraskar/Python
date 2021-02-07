# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 12:55:31 2021

@author: Danilo P.
"""

''' Cria a classe ponto '''
class ponto:
        ''' Construtor'''
        def __init__(self, initX, initY, initZ): #recebe coordenadas X e Y
                self.x = initX  #coordenada x
                self.y = initY  #coordenada y
                self.z = initZ  #coordenada y
        

        ''' Métodos'''
        #Distância do ponto até a origem
        def returnDistFromOrigin(self):
                distOrigem = ((self.x-0)**2+(self.y-0)**2+(self.z-0)**2)**(1/2)
                return distOrigem

''' Cria a classe reta '''
class reta:
        ''' Construtor'''
        def __init__(self, initPontoInicial, initPontoFinal):
                #Guarda os objetos pontos (objetivando ver se é possível trabalhar com um objeto dentro de outro)
                self.pontoInicial = initPontoInicial
                self.pontoFinal = initPontoFinal

                #Determina os deltas pra que fique mais fácil de entender o cálculo de comprimento
                self.deltaX = initPontoFinal.x-initPontoInicial.x
                self.deltaY = initPontoFinal.y-initPontoInicial.y
                self.deltaZ = initPontoFinal.z-initPontoInicial.z

                #Cálculo do comprimento
                self.comprimento = ((self.deltaX)**2+(self.deltaY)**2+(self.deltaZ)**2)**(1/2)

        ''' Métodos'''
        #Alarga o comprimento da reta
        def alargar(self, incremento):
                self.comprimento = self.comprimento + incremento

        #Diminui o comprimento da reta
        def diminuir(self, decremento):
                self.comprimento = self.comprimento - decremento
          
        
''''''''''''
'''Testes'''
''''''''''''
#Criação dos objetos--------------
p0 = ponto(25, 1, 33) #ponto
p1 = ponto(1, 1, 1) #ponto
r0 = reta(p0, p1) #reta

#Prints de controle---------------
print(p0.returnDistFromOrigin(), " = dist p0 para (0,0,0)") #Verifica o que o método de cálculo da distancia até origem para "p0" retorna
print(p1.returnDistFromOrigin(), " = dist p1 para (0,0,0)") #Verifica o que o método de cálculo da distancia até origem para "p1" retorna
print(r0.comprimento, " = comprimento da reta(p0,p1)") #Verifica se o atributo "comprimento" retorna 

#Averigando o que os métodos "alargar" e "diminuir" retornam 
r0.alargar(25) #chamando método "alargar"
print(r0.comprimento, " alarga(25)") #print de controle

r0.diminuir(5) #chamando método "diminuir"
print(r0.comprimento, " diminui(5)") #print de controle