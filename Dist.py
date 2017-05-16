print("__--------------------------------------------------------__")
nome=raw_input("Olá diga seu nome, por favor: ")
print("-----------------------------------------------------------")
print("Seja bem vindo %s !"%(nome))
print("-----------------------------------------------------------")

print ("Distância")

print("As coordenadas x1 e y1 são as do início, e as x2 e y2 do destino!")

a=input("Diga suas coordenada x1 em metros: ")
b=input("Diga suas coordenada y1 em metros: ")
c=input("Diga suas coordenada x2 em metros: ")
d=input("Diga suas coordenada y2 em metros: ")
print(" ")

h=raw_input("Diga: [a]  se deseja a presença de cota nas contas ou [b] para não: ")

if h=="a":
    h1=input("Diga sua cota h1 em metros: ")
    h2=input("Diga sua cota h2 em metros: ")
    dx=((c-a)**2)
    dy=((d-b)**2)
    dz=((h2-h1)**2)
    metros=(dx+dy+dz)**0.5
elif h=="b":
    dx=((c-a)**2)
    dy=((d-b)**2)
    metros=(dx+dy)**0.5


if metros==0:
    print("Você não saiu do seu lugar!")
    print("--PROGRAM-BY-DHRASKAR-------------------------------BR-PY--")
    exit()
print ("Você está a: %f metros do seu destino." %(metros))
print(" ")
print("-----------------------------------------------------------")


print("Velocidade")
print(" ")

vel=input("Diga o módulo de sua velocidade: ")
if vel==0:
    print "Velocidade Inválida"
    vel=input("Diga o módulo de sua velocidade: ")
    if vel==0:
        print("ERRO!\nREINICIE O PROGRAMA!")
        print("--PROGRAM-BY-DHRASKAR-------------------------------BR-PY--")
        exit()
    
tvel=raw_input("Diga: [a] para metros por segundo ou [b] para kilometros por hora: ")
print(" ")

velf=None

if tvel=="a":
    velf=vel
elif tvel=="b":
    velf=vel/3.6
else:
    print("Você inseriu uma tecla diferente das estipuladas!\n")
    tvel=raw_input("Diga: [a] para metros por segundo ou [b] para kilometros por hora: ")
    print(" ")

    velf=None

    if tvel=="a":
        velf=vel
    elif tvel=="b":
        velf=vel/3.6
    else:
        print("ERRO!\nREINICIE O PROGRAMA!")
        print("--PROGRAM-BY-DHRASKAR-------------------------------BR-PY--")
        exit()


tt=metros/vel
tvh=input("Diga a quantas horas esta viajando: ")
tvm=input("Diga a quantos minutos esta viajando: ")
tvs=input("Diga a quantos segundos esta viajando: ")
tv=(tvh*3600)+(tvm*60)+tvs
tr=tt-tv
a = tt % 60
if tr==tt:
    print("O tempo total de viagem será de: %f segundos\n " %(tt))
    print("Esperamos que sua viagem seja agradável %s!\n" %(nome))
if tr==0:
    print("Você chegou ao seu destino! \n")
    print("Esperamos que sua viagem tenha sido agradável %s!\n" %(nome))
if tr<0:
    print("O TEMPO DE VIAGEM INSERIDO É MAIOR DO QUE TEMPO TOTAL! \nPor favor, se ainda não chegou no seu destino")
    print("Digite novamente os valores! \n ")
    print("-----------------------------------------------------------")
    tvh=input("Diga a quantas horas esta viajando: ")
    tvm=input("Diga a quantos minutos esta viajando: ")
    tvs=input("Diga a quantos segundos esta viajando: ")
    tv=(tvh*3600)+(tvm*60)+tvs
    tr=tt-tv
    if tr==tt:
        print("O tempo total de viagem será de: %f segundos\n " %(tt))
        print("Esperamos que sua viagem seja agradável %s!\n" %(nome))
    if tr==0:
        print("Você chegou ao seu destino! \n")
        print("Esperamos que sua viagem tenha sido agradável %s!\n" %(nome))
    if tr<0:
        print("ERRO!\nO TEMPO DE VIAGEM INSERIDO É MAIOR DO QUE TEMPO TOTAL! \nPor favor reinicie o programa e digite denovo! \n ")
        print("--PROGRAM-BY-DHRASKAR-------------------------------BR-PY--")
        exit()
    else:
        print("O tempo total de viagem é de: %f segundos\nFaltam ainda: %f segundos\n" %(tt,tr))
        print("Esperamos que o restante de sua viagem seja agradável %s!\n" %(nome))
else:
    print("O tempo total de viagem é de: %f segundos\nFaltam ainda: %f segundos\n" %(tt,tr))
    print("Esperamos que o restante de sua viagem seja agradável %s!\n" %(nome))
    

print("--PROGRAM-BY-DHRASKAR-------------------------------BR-PY--")
exit()

