"""
Created on Wed Mar 19 14:55:02 2025

@author: Jules Malavieille
"""
import numpy as np
import matplotlib.pyplot as plt

P1 = 0.0    # model value = 0.0
G1 = 0.6747  # 0.6447
P2 = 0.7476  # model value : 0.7476
G2 = 0.0381  #0.0381
P3 = 0.6619  # model value : 0.6619
G3 = 0.0137  # 0.0137
P4 = 0.7006  # model value : 0.7006
G4 = 0.0452  # 0.0452
P5 = 0.0   # model value : 0.0
G5 = 0.8091   # 0.8091
P6 = 0.0   # model value : 0.0
G6 = 0.8091   # 0.8091
P7 = 0.8084   # model value : 0.8084
F5 = 127
F6 = 4
F7 = 80

# The Leslie matrix
L = np.array([[0,0,0,0,F5,F6,F7],
              [G1,P2,0,0,0,0,0],
              [0,G2,P3,0,0,0,0],
              [0,0,G3,P4,0,0,0],
              [0,0,0,G4,P5,0,0],
              [0,0,0,0,G5,P6,0],
              [0,0,0,0,0,G6,P7]])

val, vec = np.linalg.eig(L)
val_max = max(np.real(val))

# Growth rate of turtle
r = np.log(val_max)
print(r)

a = np.argmax(val)  # index of max value of eigenvalues
vec_d = vec[:,a]
som = np.sum(vec_d)
prop = (vec_d/som)*100

classe = ("Oeufs", "petit juvénile", "gros juvénile", "préadulte", "jeune reproducteur", "remigrante", "adulte")

plt.figure(1)
plt.grid()
plt.bar(classe, prop)
plt.ylabel("Abondance en %")
plt.title("Abondances de chaque classe en pourcentage de la population totale")

val_g, vec_g = np.linalg.eig(L.T)

b = np.argmax(val_g)  # recurpere indice de la valeur max de val_g
vec_mg = vec_g[:,b]
repro = vec_mg/[vec_mg[0]]

plt.figure(2)
plt.grid()
plt.bar(classe, repro)
plt.ylabel("Impact relatif de la reproduction")
plt.title("Impact de chaque classe sur la reproduction relativement a la classe 1")

S = np.zeros([len(vec_d), len(vec_d)])
for i in range(len(vec_d)):
    for j in range(len(vec_d)):
        S[i,j] = (vec_mg[i] * vec_d[j])/(np.dot(vec_mg.T, vec_d))
  
P = []
G = []
F = []
for i in range(len(vec_d)):
    for j in range(len(vec_d)):
        if i == j:
            P.append(S[i,j])
        if i == j+1:
            G.append(S[i,j])
        if i == 0 and (j == 4 or j == 5 or j == 6):
            F.append(S[i,j])
            

plt.figure(3)
plt.grid()
plt.plot(classe, P,"*-", label="Taux de survie")
plt.plot(classe[0:6], G,"*-", label="Taux de vieillissement")
plt.plot(classe[4:7], F,"*-", label="Fécondité")
plt.legend()
plt.xlabel("Classes")
plt.ylabel("Valeur d'élasticité")
plt.title("Elasticité de chaque classe en fonctions des paramètres du modèle")

# plt.figure(4)
# TS = [1, 6, 7, 5, 1, 1, 30]
# plt.scatter(TS, P)

""" Valeur d'origine"""
# lam_max = 0.9288
# r = -0.0738

"""Stade 2 à 4 Pi = 0.8 """
# lam_max = 0.9899
# r = -0.0101

"""Stade 5,6,7 à Pi = 0.85"""
# lam_max = 0.9421
# r = -0.05696

"""Stade 3 et 4 Pi = 0.8 et stade 5 et 6 Pi = 0.85"""
# lam_max = 0.9787
# r = -0.0214

"""Stade 1 Pi/2, stade 3 et 4 Pi = 0.8 et stade 5 6 et 7 Pi = 0.85"""
# lam_max = 0.9874
# r = -0.01263

"""Interprétation : 
    On voit que lorsque les classes 2 à 4 survivent plus le r augmente 
    On voit que si les classes 3 à 6 survivent plus r augmente mais moins que si la classe 2 augmente aussi
    Si les classes 5 à 7 survivent plus, r augmente mais beaucoup moins que si les classes de jeunes augmente
    Si les classes 3 à 6 augmente, r augmente mais pas autant que les classes 2 à 4
    On voit que si la classe 1 survie moins et les classes 3 à 7 survivent plus r augmente encore plus 
    
    Conclusion : l'impact le plus fort sur r est donnée par le groupe des juveniles.
    Augmenter la survie des oeufs ne change rien et la survie des reproducteur augmente r 
    mais pas autant que les jeunes individus"""

















