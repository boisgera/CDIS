//-------------------------------  trace  ------------------------------------------- 
//
//  POUR f(y) = -0.5*y^3 :
//  - comparer la solution exacte (1+t)^(-1/2) et la solution numerique
//     r=fscanfMat('adaptatif_EDO/res.txt'); plot(r(:,1),r(:,3)); plot(r(:,1),(1+r(:,1)).^(-0.5),'r')  
//  - voir l'evolution des pas de temps : 
//      r=fscanfMat('adaptatif_EDO/res.txt'); plot2d(1:size(r,1),r(:,2),logflag='nl')
//
//-----------------------------------------------------------------------------------


#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <fstream>

using namespace std;

const double T       = 1000.;
const double dt_min  = 1e-5;
const double dt_max  = 1000;
const double dt_init = 1e-2;
const double tol     = 1e-5;
const double y_init  = 1.;

double force (double z)
{
  double f = 0.;
  f = -0.5*pow(z,3);
  return f;
}

int main () 
{ 
  double y    = y_init; 
  double time = 0;
  double dt   = dt_init;
  double f_old, f_new, error;
  ofstream RES ("res.txt"); 
  
  //-- calcul de la premiere force --
  f_old = force(y);
  f_new = force(y+dt*f_old);
  error = 0.5*fabs(f_new-f_old);
  RES << time << "  " << dt_init << "  " << y << "  " << error << endl;
  
  while (time < T)
    {
      //--- mise a jour du temps ---
      time += dt;
      //--- garder force en memoire ---
      f_old = f_new;
      f_new = force(y);
      //--- mise a jour du pas de temps ---
      error = 0.5*fabs(f_new-f_old);
      if (error < tol/3)
	{
	  dt *= 1.5;
	  if (dt > dt_max)
	    dt = dt_max;
	}
      if (error > tol)
	{
	  dt *= 0.75;
	  if (dt < dt_min)
	    {
	      dt = dt_min;
	      cout << " Attention : dt est au minimum ! Singularite ?" << endl;
	    }
	}
      //--- calcul du nouveau point ---
      y += dt*f_new;
      
      //--- on sort les resultats ---
      RES << time << "  " << dt << "  " << y << "  " << error << endl;
    }
  
  cout << endl;
  
  return 1;
  
}
