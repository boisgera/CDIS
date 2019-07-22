% Calcul Intégral V

<!-- LaTeX Macros -->
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}

Common thread
================================================================================

Analyse et proba, étude de 
$$
g(t) = c + \int^t f(x) \,dx
$$
et notion de dérivée faible associée ? Avec deux motivations différentes ?

Bagage en commun ?

Proba / Fct répartition
================================================================================

Généralisation cas discret et à densité; dans les deux cas, fcts croissante
$\mathbb{R} \to \mathbb{R}$, nulle en $-\infty$, de variation 1, etc.

Montrer comment définir une mesure (extérieure) associée,
notation $(\mu =) df$ (Lebesgue-Stieltjes) ?
Lien notation avec somme de Riemman-Stieltjes pour l'intégration de fcts
continues ?

Ext. Calcul Diff
================================================================================

Si $f$ dérivable partout,
$$
f(x) = \int^x f'(t) \, dt,
$$
mais l'hypothèse de dérivabilité partout est parfois un peu (trop) forte ...
Exemple $\dot{x} = u$ avec $u$ discontinue (ex: chauffage ...) ... 
interprétation en "recollant les morceaux diff" par continuité ? 
Plus simple ?

Autre approche: si $g$ définie **presque partout** et localement 
intégrable, et vérifie
$$
f(x) = \int^x g(t) \, dt,
$$
tentation de considérer $g$ comme une dérivée généralisée de $f$.
En pratique on se limite à des $g$ localement **absolument** intégrables.

Pptés (quid liste raisonnables ppté dérivées faible ?):

  - $g$ si elle existe est unique (cf dériv / borne)

  - si $f$ dérivable partout et dérivée abs int, les deux notions sont
    identiques

Carac directes fcts $f$ ayant une dérivée faible (*absolument continues*).

Exemples:

  - valeur absolue, puis   
  
  - dérivée abs int par morceaux + cont (retour ex ODE)

  - qui ne marche pas: dérivée p.p. abs int, mais avec saut

  - attention: dérivée existe pp et abs int + continue ne suffit pas
    (devil's staircase). Ouch ...

-----

Equivalence $g$ dérivée faible de $f$ et
$$
\int g \phi = - \int f \phi'
$$
pour $\phi$ $C^1$ à support compact. Mq membre de gauche cont par rapport
à $\phi$ et que $g$ définie par la fonctionnelle
$$
\phi \mapsto \int g \phi
$$
(TCD pour se ramener à des intervalles, puis dérivation / borne).
Etudier cet objet de façon plus générale, lien avec mesure (signée) de Radon
(via Riesz, complexe); définir dérivée de fct (localt abs int) comme mesure
de Radon. Formule des sauts.

Idée plus générale: peut-on dériver une mesure de Radon ? 
Définition distribution d'ordre fini, etc.
Extension au cas vectoriel.

Probab $\Omega \neq \R^n$
================================================================================