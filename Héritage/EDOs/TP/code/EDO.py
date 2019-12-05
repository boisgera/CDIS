#-------------------------------------------------
#   (G. Stoltz, Paris, 13 juillet 2017)
#   Sous Linux, executer avec 'python EDO.py'
#------------------------------------------------- 

import matplotlib.pyplot as plt
import numpy as np

#------------ parametres d'integration ----------
x = 1.           # condition initiale
Time = 0.99      # temps d'integration
dt = 0.01        # pas de temps
tol = 1e-10      # tolerance dans convergence des methodes implicites
max_iter = 100   # nb maximal d'iterations pour point fixe methodes implicites

#------------ choix du champs de force ----------

def force(x):
  ff = x**2
  return ff

#------------- constantes derivees et variables locales ----------
nb_steps = int(np.floor(Time*1./dt))  # nb pas d'integration, tronques a la partie entiere
time = 0.
mean_iter = 0.

#---------- trace de la trajectoire de reference (quand elle existe) --------
fig, ax = plt.subplots()
Nref = 100
y = np.linspace(0,Time,nb_steps)
z = np.zeros(nb_steps)
for i in range(0,nb_steps):
  z[i] = 1./(1-y[i]) 
ax.plot(y,z)

#------- boucle d'integration ---------------
t = np.linspace(0,Time,nb_steps+1)
sol = np.zeros(nb_steps+1)

t[0] = 0.
sol[0] = x

for i in range(1,nb_steps+1):

  # incrementation du temps
  time = time + dt 

  #--- schema numerique choisi ---
  # Euler explicite
  x  = x + dt*force(x)
  # Heun
  # x = ...
  # Euler implicite
  # x = ... 

  # aquisition pour graphique
  sol[i] = x
  t[i] = time 

#---- verification temps d'integration ; l'instruction **"0.3f" % number** permet d'afficher seulement 3 decimales ----
print('Temps integration:',Time,"%0.3f" % (dt*nb_steps),"%0.3f" % time)

#------ erreur ---------
xref = 1./(1-Time) 
print('Erreur au temps final',abs(x-xref))

#--- trace solution numerique ---
ax.plot(t,sol,'ro')
ax.set_xticks([0,0.5,0.99])
ax.set_title('pas de temps = '+str(dt))
ax.set_xlabel('temps')
ax.set_ylabel('valeur')
plt.show()


