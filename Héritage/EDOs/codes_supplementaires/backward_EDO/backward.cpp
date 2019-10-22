//-------------------------------------------------------------------------------
//
//               Etude de l'ordre des schemas d'integration 
//
//-------------------------------------------------------------------------------

//           Trace des resultats sous scilab (solution exacte y(t) = y^0/(1-t y^0) )
//y=fscanfMat('backward_EDO/num.txt');z=fscanfMat('backward_EDO/mod.txt');plot(y(:,1),y(:,2),'r+');plot(z(:,1),z(:,2),'k');plot(z(:,1),(1-z(:,1)).^(-1))

#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <fstream>

using namespace std;

const double T        = 0.99;
const double dt       = 0.01;
const double dt_mod   = 1e-5;
const double tol      = 1e-10;
const int    max_iter = 100;

//---- method ----
int method = 0; // 0 = Euler explicite, 1 = Euler implicite

//-- choix de la condition initiale ---
double CI = 1.;

//--- force -------
double force (double z)
{
  double f = 0.;
  f = pow(z,2);
  return f;
}

//--- forces modifiee -------
double force_mod_EulerExplicite (double z)
{
  double f = 0.;
  f = pow(z,2) - dt*pow(z,3);
  return f;
}

double force_mod_EulerImplicite (double z)
{
  double f = 0.;
  f = pow(z,2) + dt*pow(z,3);
  return f;
}

//------------------------  boucle generale ---------------------
int main () 
{ 
  double y, y_proposed, y_old, z, time, time_mod, error; 
  int iter;
  int N     = (int)rint(T/dt);
  int N_mod = (int)rint(T/dt_mod);
  cout << endl;
  ofstream NUM ("num.txt");   // solution numerique usuelle 
  ofstream MOD ("mod.txt");   // resolution tres precise de la dynamique modifiee
  
  //--- conditions initiales ---
  y = CI;
  z = CI;
  time = 0;
  time_mod = 0;
  NUM << time     << "  " << y << endl;
  MOD << time_mod << "  " << z << endl;

  //--- iterations en temps ---
  cout << "------ SOLUTION NUMERIQUE USUELLE -------" << endl;
  for (int pas = 0; pas < N; pas++)
    {
      time += dt;
      //-- integration de la dynamique --
      switch (method) {
      case 0:
	//--- Euler explicite ---
	y += dt*force(y); 
	break;
      case 1:
	//--- Euler implicite ---
	y_proposed = y+dt*force(y);  
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
	break;
      }
      //-- acquisition du nouveau point --
      NUM << time << "  " << y << endl;
    }
  
  //--- iterations en temps ---
  cout << "------ SOLUTION DE LA DYNAMIQUE MODIFIEE -------" << endl;
  for (int pas = 0; pas < N_mod; pas++)
    {
      time_mod += dt_mod;
      switch (method) {
      case 0:
  	z += dt_mod*force_mod_EulerExplicite(z); 
  	break;
      case 1:
  	z += dt_mod*force_mod_EulerImplicite(z); 
  	break;
      }
      MOD << time_mod << "  " << z << endl;
    }
    
  cout << endl;
  
  return 1;
  
}
