import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
import random

#cmap = ListedColormap([[0, 0, 0], [1, 1, 1], [1, 0, 0]])
#matrix = [[0,0,0],[0,7000,0],[0,0,10000]]
mapa = []
max_x = 50
max_y = 50
#grama = [4300,5000,5500]
#deserto = [7200,7600,7400]
#oceano = [1400,2200,2300]
grama = []
deserto = []
oceano = []
ultimo = 10000
cont = 0
#maps_list = ['flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
#            'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg',
#            'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar']
maps_list = ['nipy_spectral']
map_used = random.choice(maps_list)
for i in range (0,1):
    al_grama = random.randint(0,500)
    grama.append(al_grama)
    grama.append(random.randint(al_grama,al_grama+500))
    grama.append(random.randint(al_grama-500,al_grama))

    al_deserto = random.randint(7500,8000)
    deserto.append(al_deserto)
    deserto.append(random.randint(al_deserto,500+al_deserto))
    deserto.append(random.randint(al_deserto-500,al_deserto))

    al_oceano = random.randint(500,800)
    oceano.append(al_oceano)
    oceano.append(random.randint(al_oceano,500+al_oceano))
    oceano.append(random.randint(al_oceano-500,al_oceano))
#for i in range (0,10000):
#    matrix.append(i)

#countour = np.reshape(matrix, (100,100))

for i in range (0,max_x*max_y):
    mapa.append(10)
    
countour = np.reshape(mapa, (max_y,max_x))
verif = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1],[0,0]]
proporcao = [grama, deserto, oceano, grama, deserto, oceano]
f_g = False
f_d = False
f_o = False

for i in range (1,max_y-1):
    for j in range (1,max_x-1):
        g = 0
        d = 0
        o = 0
        prop_atual = proporcao
        for k in range (0,8):
            if (countour[i+verif[k][0]][j+verif[k][1]] in grama):
                g+=1
                prop_atual.append(grama)
                if (f_g == True):
                    #prop_atual.append(grama)
                    #prop_atual.append(grama)
                    #prop_atual.append(grama)
                    #prop_atual.append(grama)
                    #prop_atual.append(grama)
                    #prop_atual.append(grama)
                    #prop_atual.append(grama)
                    #prop_atual.append(grama)
                    #prop_atual.append(grama)
                    #prop_atual.append(grama)
                    #prop_atual.append(grama)
                    #prop_atual.append(grama)
                    #prop_atual.append(grama)
                    f_g = False
                
            elif (countour[i+verif[k][0]][j+verif[k][1]] in deserto):
                d+=1
                prop_atual.append(deserto)
                if (f_d == True):
                    #prop_atual.append(deserto)
                    #prop_atual.append(deserto)
                    #prop_atual.append(deserto)
                    #prop_atual.append(deserto)
                    #prop_atual.append(deserto)
                    #prop_atual.append(deserto)
                    #prop_atual.append(deserto)
                    #prop_atual.append(deserto)
                    #prop_atual.append(deserto)
                    #prop_atual.append(deserto)
                    #prop_atual.append(deserto)
                    #prop_atual.append(deserto)
                    #prop_atual.append(deserto)
                    
                    f_d = False
                
            elif (countour[i+verif[k][0]][j+verif[k][1]] in oceano):
                o+=1
                prop_atual.append(oceano)
                if (f_o == True):
                    #prop_atual.append(oceano)
                    f_o = False
                
        gerado = random.choice(prop_atual)
        if (gerado == grama):
            countour[i][j] = random.choice(grama)
        elif (gerado == deserto):
            countour[i][j] = random.choice(deserto)
        elif (gerado == oceano):
            countour[i][j] = random.choice(oceano)
        if (countour[i][j] in grama):
            f_g = True
        elif (countour[i][j] in deserto):
            f_d = True
        elif (countour[i][j] in oceano):
            f_o = True

def ilha(max_y,max_x,countour,verif):
    tam_ilha = random.randint(0, max_y//1.5)
    comeco_x = random.randint(0,max_x-1)
    comeco_y = random.randint(0,max_y-1)
    countour[comeco_y][comeco_x] = random.choice(grama)
    prob = [1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,5,5,5,10]
    tam_atual = 0
    #for k in range (0,8):
    #    if (comeco_y+verif[k][0]<max_y and comeco_x+verif[k][1]<max_x):
    #        countour[comeco_y+verif[k][0]][comeco_x+verif[k][1]] = grama
    for i in range (comeco_y, max_y):
        if(tam_pos<tam_ilha//2):
            tam_pos = random.choice(prob)
            tam_neg = random.choice(prob)
        for j in range (comeco_x-tam_neg,comeco_x+tam_pos):
            if (j >= 0 and j < max_x):
                countour[i][j] = random.choice(grama)




def suavLeve (countour,max_y,max_x):
    
    for i in range (1,max_y-1):
        for j in range (1,max_x-1):
            g = 0
            d = 0
            o = 0
            prop_atual = proporcao
            s_n = [0,0,0,0,0,0]
            #print(s_n)
            for k in range (0,8):
                if (countour[i+verif[k][0]][j+verif[k][1]] in grama):
                    g+=1
                    
                elif (countour[i+verif[k][0]][j+verif[k][1]] in deserto):
                    d+=1
                    
                elif (countour[i+verif[k][0]][j+verif[k][1]] in oceano):
                    o+=1
            if (g > 2):
                for p in range (0, g-2):
                    s_n[p] = 1
                if (random.choice(s_n)==1):
                    countour[i][j] = random.choice(grama)
                #print("O s_n eh: ",s_n," ------------ g-4 eh: ", g-4)
            
            if (d > 2):
                for p in range (0, d-2):
                    s_n[p] = 1
                if (random.choice(s_n)==1):
                    countour[i][j] = random.choice(deserto)
            if (o > 2):
                for p in range (0, o-2):
                    s_n[p] = 1
                if (random.choice(s_n)==1):
                    countour[i][j] = random.choice(oceano)

def suavPesada (countour,max_y,max_x):
    
    for i in range (1,max_y-1):
        for j in range (1,max_x-1):
            g0 = 0
            g1 = 0
            g2 = 0
            d0 = 0
            d1 = 0
            d2 = 0
            o0 = 0
            o1 = 0
            o2 = 0
            prop_atual = proporcao
            s_n = [0,0,0,0,0,0]
            #print(s_n)
            for k in range (0,8):
                if (countour[i+verif[k][0]][j+verif[k][1]] == grama[0]):
                    g0+=1
                elif (countour[i+verif[k][0]][j+verif[k][1]] == grama[1]):
                    g1+=1
                elif (countour[i+verif[k][0]][j+verif[k][1]] == grama[2]):
                    g2+=1
                    
                elif (countour[i+verif[k][0]][j+verif[k][1]] == deserto[0]):
                    d0+=1
                elif (countour[i+verif[k][0]][j+verif[k][1]] == deserto[1]):
                    d1+=1
                elif (countour[i+verif[k][0]][j+verif[k][1]] == deserto[2]):
                    d2+=1
                    
                elif (countour[i+verif[k][0]][j+verif[k][1]] == oceano[0]):
                    o0+=1
                elif (countour[i+verif[k][0]][j+verif[k][1]] == oceano[1]):
                    o1+=1
                elif (countour[i+verif[k][0]][j+verif[k][1]] == oceano[2]):
                    o2+=1

            if (g0 > 2):
                for p in range (0, g0-2):
                    s_n[p] = 1
                if (random.choice(s_n)==1):
                    countour[i][j] = grama[0]
                #print("O s_n eh: ",s_n," ------------ g-4 eh: ", g-4)
            if (g1 > 2):
                for p in range (0, g1-2):
                    s_n[p] = 1
                if (random.choice(s_n)==1):
                    countour[i][j] = grama[1]
            if (g2 > 2):
                for p in range (0, g2-2):
                    s_n[p] = 1
                if (random.choice(s_n)==1):
                    countour[i][j] = grama[2]
            
            if (d0 > 2):
                for p in range (0, d0-2):
                    s_n[p] = 1
                if (random.choice(s_n)==1):
                    countour[i][j] = deserto[0]
            if (d1 > 2):
                for p in range (0, d1-2):
                    s_n[p] = 1
                if (random.choice(s_n)==1):
                    countour[i][j] = deserto[1]
            if (d2 > 2):
                for p in range (0, d2-2):
                    s_n[p] = 1
                if (random.choice(s_n)==1):
                    countour[i][j] = deserto[2]
            if (o0 > 2):
                for p in range (0, o0-2):
                    s_n[p] = 1
                if (random.choice(s_n)==1):
                    countour[i][j] = oceano[0]
            if (o1 > 2):
                for p in range (0, o1-2):
                    s_n[p] = 1
                if (random.choice(s_n)==1):
                    countour[i][j] = oceano[1]
            if (o2 > 2):
                for p in range (0, o2-2):
                    s_n[p] = 1
                if (random.choice(s_n)==1):
                    countour[i][j] = oceano[2]

                
def maiorResol (countour,mult):
    
    pinta = [[0,0],[0,1],[1,0],[1,1],[0,2],[1,2],[2,0],[2,1],[2,2],[0,3],[1,3],[2,3],[3,3],[3,0],[3,1],[3,2]]
    mapa_Maior = []
    aumento_x = max_x*mult
    aumento_y = max_y*mult

    for i in range (0,aumento_x*aumento_y):
        mapa_Maior.append(0)
    mapa_Maior = np.resize(mapa_Maior,(aumento_y, aumento_x))

    for i in range (0,aumento_y,2):

        for j in range (0,aumento_x,2):

            for k in range (0,4):
                ind_i = i//2
                ind_j = j//2
                mapa_Maior[i+pinta[k][1]][j+pinta[k][0]] = countour[ind_i][ind_j]
    return (mapa_Maior)




#ilha(max_y,max_x,countour,verif)
countour[max_y-1][max_x-1] = ultimo
print(countour)
plt.figure()
plt.matshow(countour, fignum=0, interpolation='none', cmap = map_used)
#plt.savefig("SohZeros.jpg", bbox_inches='tight', dpi=200)
nome_ini = input("Digite o nome da imagem inicial: ")
plt.savefig(nome_ini+".jpg", bbox_inches='tight', dpi=200)
plt.show()
plt.close()


#file = open("matrix.txt", 'w')
#separador = ";"
#for i in range (1,max_y-1):
#        for j in range (1,max_x-1):
#            file.write("%d%s" %(countour[i][j],separador))
#file.close()

numSuav = 0

def plotar(nome, numSuav, countour, max_x, max_y, leve):
    if(leve == True):
        suavLeve(countour, max_y, max_x)
    else:
        suavPesada(countour, max_y, max_x)
    plt.figure()
    plt.matshow(countour, fignum=0, interpolation='none', cmap = map_used)
    #plt.savefig("SohZeros.jpg", bbox_inches='tight', dpi=200)
    plt.savefig(nome+'.jpg', bbox_inches='tight', dpi=200)
    #plt.show()
    plt.close()


    #rodar_Seg = input("Deseja rodar seg vez a suavizacao? (s/n): ")
    #if (rodar_Seg=="s"):
    #    numSuav += 1
    #    nome = input("Digite o nome da imagem apos a %da suavizacao: " %(numSuav))
    #    plotar(nome,numSuav)
    #else:
    #    return (0)


#rodar_Seg = input("Deseja rodar a suavizacao? (s/n): ")
rodar_Seg = "s"
if (rodar_Seg=="s"):
    numSuav += 1
    #vezes = int(input("num de vezes: "))
    vezes = 2
    for i in range (0, vezes):

        nome = str(i)
        #nome = input("Digite o nome da imagem apos a %da suavizacao: " %(numSuav))
        plotar(nome,numSuav, countour, max_x, max_y, True)
mapa_aumentado = maiorResol(countour,2)
plt.figure()
plt.matshow(mapa_aumentado, fignum=0, interpolation='none', cmap = map_used)
#plt.savefig("SohZeros.jpg", bbox_inches='tight', dpi=200)
plt.savefig("MapaAumentadoAntesSuav.jpg", bbox_inches='tight', dpi=200)
#plt.show()
plt.close()
for i in range (0, 3):

        nome = "aumentado_2x2"
        #nome = input("Digite o nome da imagem apos a %da suavizacao: " %(numSuav))
        plotar(nome,numSuav, mapa_aumentado, max_x*2,max_y*2, True)

mapa_aumentado4 = maiorResol(mapa_aumentado,4)
for i in range (0, 3):

        nome = "aumentado_4x4"
        #nome = input("Digite o nome da imagem apos a %da suavizacao: " %(numSuav))
        plotar(nome,numSuav, mapa_aumentado4, max_x*4,max_y*4,False)

mapa_aumentado8 = maiorResol(mapa_aumentado4,8)
for i in range (0, 3):

        nome = "aumentado_4x4"
        #nome = input("Digite o nome da imagem apos a %da suavizacao: " %(numSuav))
        plotar(nome,numSuav, mapa_aumentado8, max_x*8,max_y*8, False)
