import pandas as pd
import numpy as np


def abrir_excel(nome_arquivo, aba):
    p_ler=pd.read_excel(nome_arquivo, sheet_name=aba,header=None) #leitura do arquivo excel
    p_t=p_ler.values.T #transforma a coluna em um unico vetor 
    return(p_t)
 

def calculo_azim(azim_dec):
    graus_int=azim_dec.astype(int) #pega so os valores inteiros de azim_dec
    graus_dec=azim_dec-graus_int  #retorna somente os decimos do grau

    minutos=graus_dec*60
    minutos_int=minutos.astype(int)
    minutos_dec=minutos-minutos_int

    segundos_sem_around=minutos_dec*60
    segundos=np.around(segundos_sem_around, decimals=0)
    return(graus_int,minutos_int,segundos)

valores=abrir_excel("excel _decimal to degress_xlsx.xlsx", "aba1")
calculo_azim(valores)
g,m,s=calculo_azim(valores)
gms=np.vstack((g,m,s))
df_gms=pd.DataFrame(gms.T,columns=['g', 'm', 's'])

with pd.ExcelWriter('saida_gleba_B.xlsx') as writer:  
    df_gms.to_excel(writer, sheet_name='aba_1', index=False, header=False)
