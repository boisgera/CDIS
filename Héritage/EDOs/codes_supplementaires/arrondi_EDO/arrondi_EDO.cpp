//-------------------------------------------------------------------------------
//
//  Etude de l'influence des erreurs d'arrondi sur l'intégration des EDOs
//
//-------------------------------------------------------------------------------

//   Pas de temps optimal, à la louche :
//      TRAPEZES
//      sigma = 1e-8; T = 1; p = 2; C_T \simeq exp(1)
//      soit dt_opt \sim (1e-8/2/exp(1))^(1/3) \simeq 1e-3
//   EULER EXPLICITE : idem avec p=1 soit dt_opt \sim 1e-4
//   Trace des resultats sous scilab : 
//     r=fscanfMat('arrondi_EDO/erreur.txt');plot2d(r(:,1),r(:,2),logflag='ll');plot2d(r(:,1),r(:,2),style=-1,logflag='ll')

#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <fstream>

using namespace std;

const double T     = 1.;
const int    Nb_dt = 19;

int main () 
{ 
  float y, alpha_trapezes, alpha_EulerExplicite, alpha;  //--------- CHANGER : float ou double ------------
  //float e = (float)(4./3.-1)*3.-1;
  //cout << " précision arithmétique " << e << endl;
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
      y = 1.;

      //--- iterations en temps ---
      //    EDO : \dot{y} = y, solution exacte y(t) = exp(t)
      
      //    schema des trapezes : y^{n+1} = y^n + 0.5*dt*(y^n+y^{n+1})
      //                   soit : y^{n+1} = alpha*y^n avec alpha = (1+0.5*dt)/(1-0.5*dt)
      alpha_trapezes = (1+0.5*dt)/(1-0.5*dt);
      //    schema d'Euler explicite 
      alpha_EulerExplicite = 1 + dt;
      // choix de la methode;
      alpha = alpha_EulerExplicite;
      for (int pas = 0; pas < N; pas++)
	y *= alpha; 
      
      //------ fin du programme -------
      cout << " Pas de temps : " << dt << ",  erreur = " << fabs(y-exp(1)) << "  " << alpha << endl;
      ERREUR << dt << " " << fabs(y-exp(1)) << endl;
    }
  
  cout << endl;
  
  return 1;
  
}
