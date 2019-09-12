//-------------------------------------------------------------------------------
//
//               Etude de l'ordre des schemas d'integration 
//
//-------------------------------------------------------------------------------

//           Trace des resultats sous scilab : 
//r=fscanfMat('order_EDO/erreur.txt');plot2d(r(:,1),r(:,2),logflag='ll');plot2d(r(:,1),r(:,2),style=-1,logflag='ll')

#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <fstream>

using namespace std;

const double T        = 1.;
const int    Nb_dt    = 22;
//-- parametres pour methodes implicites implementees avec point fixe --
const double tol      = 1e-10;
const int    max_iter = 100;
//-- choix de la reference ---
double CI = 0.99;
// si f(y) = y   : CI*exp(T);  --> solution theorique y(t) = exp(t); 
// si f(y) = y^2 : CI/(1-CI*T); avec CI un peu en dessous de 1  --> solution y(t) = y^0/(1-t y^0) 
const double ref      = CI/(1-CI*T);


//--- choix de la methode ------
// 0 = Euler explicite
// 1 = Euler implicite
// 2 = Heun
// 3 = trapezes (Cranck-Nicholson)
// 4 = Runge Kutta ordre 4
int method = 4; 

//--- force -------
double force (double z)
{
  double f = 0.;
  f = pow(z,2);
  return f;
}

//----  boucle generale -----
int main () 
{ 
  double y, y_proposed, y_old, y_new, y_intermediate, y2, y3, y4, error; 
  int iter;
  cout << endl;
  ofstream ERREUR ("erreur.txt"); 
  
  //---- boucle sur les pas de temps ----
  ifstream DT ("time_steps.txt");
  double dt = 1.;
  int N = 1;
  for (int nb_dt = 0; nb_dt < Nb_dt; nb_dt++)
    {
      //--- lecture du pas de temps --
      DT >> dt >> ws;
      //--- nombre de pas d'integration ---
      N  = (int)rint(T/dt);
      //--- condition initiale ---
      y = CI;

      //--- iterations en temps ---
      //    EDO : \dot{y} = y(t), solution exacte y(t) = exp(t)
      
      switch (method) {
      case 0:
	cout << "------ EULER EXPLICITE -------" << endl;
	for (int pas = 0; pas < N; pas++)
	  y += dt*force(y); 
	break;
      case 1:
	cout << "------ EULER IMPLICITE -------" << endl;
	for (int pas = 0; pas < N; pas++)
	  {
	    y_proposed = y+dt*force(y);  
	    // premiere proposition par Euler explicite
	    error = 1;
	    iter = 0;
	    while ( (error > tol) && (iter < max_iter))
	      {
		iter++;
		y_old = y_proposed;
		y_proposed = y + dt*force(y_proposed); 
		error = fabs(y_old-y_proposed);
	      }
	    if (iter > max_iter)
	      cout << " Probleme dans les iterations de point fixe ! dt = " << dt << endl;
	    y = y_proposed;
	  }
	break;
      case 2:
	cout << "------ METHODE DE HEUN -------" << endl;
	for (int pas = 0; pas < N; pas++)
	  {
	    y_intermediate = y + dt*force(y);
	    y += 0.5*dt*( force(y) + force(y_intermediate) ); 
	  }
	break;
	case 3:
	cout << "------ TRAPEZES -------" << endl;
	for (int pas = 0; pas < N; pas++)
	  {
	    y_proposed = y+dt*force(y);  // premiere proposition par Euler explicite
	    error = 1;
	    iter = 0;
	    while ( (error > tol) && (iter < max_iter))
	      {
		iter++;
		y_old = y_proposed;
		y_proposed = y + 0.5*dt*( force(y)+force(y_proposed) ); 
		error = fabs(y_old-y_proposed);
	      }
	    if (iter > max_iter)
	      cout << " Probleme dans les iterations de point fixe ! dt = " << dt << endl;
	    y = y_proposed;
	  }
	break;
      case 4:
	cout << "------ METHODE DE RUNGE KUTTA D'ORDRE 4 -------" << endl;
	for (int pas = 0; pas < N; pas++)
	  {
	    y2 = y + 0.5*dt*force(y);
	    y3 = y + 0.5*dt*force(y2);
	    y4 = y +     dt*force(y3);
	    y += dt/6*( force(y) + 2*force(y2) + 2*force(y3) + force(y4)); 
	  }
	break;
      }
      
      //------ fin du programme -------
      cout << " Pas de temps : " << dt << ",  erreur = " << fabs(y-ref) << endl;
      ERREUR << dt << " " << fabs(y-ref) << endl;
    }
  
  cout << endl;
  
  return 1;
  
}
