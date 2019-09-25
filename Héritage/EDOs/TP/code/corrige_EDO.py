#-------------------------------------------------
#   (G. Stoltz, Paris, 13 juillet 2017)
#   Sous Linux, executer avec 'python EDO.py'
#------------------------------------------------- 

import matplotlib.pyplot as plt
import numpy as np

#------------ parametres d'integration ----------
x = 1.;           # condition initiale
Time = 0.99;      # temps d'integration
dt = 1e-3;        # pas de temps
tol = 1e-10;      # tolerance dans convergence des methodes implicites
max_iter = 100;   # nb maximal d'iterations pour point fixe methodes implicites

#------------ choix du champs de force ----------

def force(x):
  ff = x**2;
  return ff

#------------- constantes derivees et variables locales ----------
nb_steps = int(np.round(Time*1./dt));  # nb pas d'integration, tronques a la partie entiere ---> IL FAUT FAIRE ROUND PEX HEUN PAS DE TEMPS 10^{-5}... SINON PBM ARRONDI PAS DE TEMPSx
time = 0.;
mean_iter = 0.;

#---------- trace de la trajectoire de reference (quand elle existe) --------
fig, ax = plt.subplots()
Nref = 100;
y = np.linspace(0,Time,nb_steps);
z = np.zeros(nb_steps);
for i in range(0,nb_steps):
  z[i] = 1./(1-y[i]); 
ax.plot(y,z)

#------- boucle d'integration ---------------
t = np.linspace(0,Time,nb_steps+1);
sol = np.zeros(nb_steps+1);

t[0] = 0.;
sol[0] = x;

for i in range(1,nb_steps+1):
  # incrementation du temps
  time = time + dt; 
  #--- schema numerique choisi ---
  # Euler explicite
  #x  = x + dt*force(x);
  # Heun
  #xi  = x + dt*force(x);
  #x = x + dt/2*( force(xi) + force(x));
  # Euler implicite
  x_new = x + dt*force(x);
  diff = 1;
  iter = 0;
  while ( (diff > tol) & (iter < max_iter)):
    iter = iter + 1; 
    x_old = x_new; 
    x_new = x + dt*force(x_old);
    diff = abs(x_new-x_old);
  x = x_new;
  mean_iter = mean_iter + iter;

  # aquisition pour graphique
  sol[i] = x;
  t[i] = time; 

#---- verification temps d'integration ; l'instruction **"0.3f" % number** permet d'afficher seulement 3 decimales ----
print('Temps integration:',Time,"%0.3f" % (dt*nb_steps),"%0.3f" % time)

#------ erreur ---------
xref = 1./(1-Time); 
print('Erreur au temps final',abs(x-xref))

#------ implicit Euler -------
print('Average number of fixed-point loops', "%0.2f" % (mean_iter*1./nb_steps) )

#--- trace solution numerique ---
ax.plot(t,sol,'ro')
ax.set_xticks([0,0.5,0.99])
ax.set_title('pas de temps = '+str(dt))
ax.set_xlabel('temps')
ax.set_ylabel('valeur')
plt.show()


