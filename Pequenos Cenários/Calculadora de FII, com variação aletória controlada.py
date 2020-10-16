import numpy as np
import random 
i0=5000.00 #Investimento inicial
p=170.00 #preço por cota inicial
dvl=9.80 #varição do valor da cota inicial
sd=p-dvl #preço mais baixo cota
sf=p+dvl #preço mais alto cota
n=int(i0/p) #numero de cotas
pm=p #preço cota variação por média inicial
r=0.74*n #rendimento do fundo
c=1000.0 #caixa 
ta=1 #tempo do rendimento em meses
tt=5*12 #tempo total
ct=n*p+c #total bruto
at=0 #Aporte em t0=0
tx=10 #fator de variação de pvar
print ("------------------")
print (n,"Ações")
print (round(c,2), "Caixa")
print (round(r,2), "Rendimento")
print (round(ct,2),"total líquido")
print ("------------------")
while ta<tt:
    r=0.74*n
    #Aporte mensal
    if ta>=0 and ta<12:
        ap=100
    elif ta>=12 and ta<36:
        ap=150
    elif ta>=36 and ta<72:
        ap=200
    else:
        ap=250
    c=c+r+ap
    while c>=pm:
        n=n+1
        c=c-pm
    pvar=(random.uniform(sd, sf)-pm)/tx #variação do valor aleatório entr sd e sf em relação ao valor médio anterior
    pm=pm+pvar #variação média entre a média anterior e a variação aleatória
    at=at+ap #aporte total
    ta=ta+1
    print (ta, " Meses// ",ap," Aporte// ",n," Ações// ",round(r, 2)," Rendimento//", round(pm,2), " Preço Cota// ", round(pvar,4), " Variação Cota// ")
    
ct=n*p+c
print ("------------------")
print (n,"Ações")
print (round(c,2), "Caixa")
print (round(r,2), "Rendimento")
print (round(ct,2),"Total Bruto")
print (round(at+0.00,2),"Aporte total")
print (round(pm,2),"Cota var.Média")
print (round(ct-at,2),"Cota valor bruto-aporte")
print ("------------------")
