% Calcul Intégral V

<!-- LaTeX Macros -->
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}

Misc.
================================================================================

  - fcts définies dans $\R$, au moins dans un premier temps

Dérivées faibles
================================================================================

**Motivation:** étendre la notion de dérivation pour traiter des uses cases 
comme les équations différentielles avec second membre discontinu en $t$, 
sans "bricolage" (qui serait: résoudre portion par portion et recoller
par continuité, si l'on suppose que l'on est $C^1$ par morceaux).
Motivation analogue pour les probas: variable aléatoire à densité
uniforme sur $[0,1]$: $p$ n'est pas (partout) la dérivée de $F$.

Dans les deux cas néanmoins, on a le même schéma ou la "dérivée" 
permet d'obtenir la fct originale par intégration.
(pour les ODEs, pour travailler sur $\R$, prolonger rhs par $0$
pour $t\neq 0$ et $x(t)$ par $x_0$.)

Idée: dérivation initialement source de définition de l'intégrale (de Newton);
l'intégration est une opération inverse, mais sait aussi intégrer
des fonctions qui ne sont *pas* des dérivées (exemple).
On peut retourner le problème et définir une nouvelle notion,
généralisée de dérivée, à partir de l'intégrale.

### Dérivée faible {.definition}
La fonction $f:\R \to \R$ est *faiblement dérivable*, 
de dérivée (faible) la fonction localement intégrable 
$g: \R \to \R$ s'il existe une constante $c$ telle que
pour tout $x \in \R$, 
$$
f(x) = c + \int_0^x g(t) \, dt.
$$

### TODO -- extension "p.p." ?
Aka fct de départ définie pp ? Bof ... Mmm quand même nécessaire pour la
suite.

### TODO -- Terminologie
Opter pour "généralisée" en 1ere instance ?
dérivée généralisée, dérivable au sens des distributions (cf. + tard)

### TODO -- Dérivable faiblement implique dérivable pp {.proposition}
Corollaire: dérivable faiblement implique dérivée classique existe pp et
est égale à la dérivée faible

### TODO -- Exemples
$x \mapsto |x|$ ?

### TODO -- Warning
attention: dérivée classique définie pp suffit pas à avoir dérivée
faible (ex: fct de Heaviside).
Dérivée faible implique dérivée pp, réciproque pas vraie, même si on ajoute
continue (idée qui vient naturellement quand on construit un contre-exemple).
Exemple avec ensembles de Cantor / devil's staircase.

### TODO -- Continuité absolue {.definition}

### TODO -- Existence de dérivée faible {.proposition}
(équiv abs. cont. si dérivée faible est localement absolument intégrable)

### TODO -- Rk
On peut ne pas se limiter au dérivée loclt abs cont, mais alors la classe
des fcts est $AC^*$ ... Grpmh.

### TODO -- Dérivation faible et IPP
(équivalence)

Mesures signées
================================================================================

Aka section "dérivée est une mesure"

### TODO -- mesure signée {.definition} 
Définir comme différence de deux mesures $\mu_+$ et $\mu_-$ de support disjoint
(introduire $\bot$ et collapser $\pm \infty$ en $\bot$)
et / ou par une intégrale avec fct $\sigma$ mesurable égale à $\pm 1$?
Et /ou par les axiomes habituels ? 

### TODO -- Equivalence
(des 3 cas précédents, à montrer)

### TODO 
$f$ $\mu-$intégrable à valeurs réelles fois $\mu$ défini une mesure signée

### TODO -- mesure de Radon (signée)
+ lien avec 

### TODO -- fct localement intégrable
... définie ("est") une mesure de Radon. Et la mesure détermine

### Dérivée généralisée comme mesure
La fonction $f:\R \to \R$ admet comme *dérivée généralisée* la mesure de
Radon $\mu$ sur $\R$ s'il existe une constante $c$ telle que
pour tout $x \in \R$, 
$$
f(x) = c + \int_0^x d\mu(t).
$$
$$

### TODO -- extension "p.p." ?
Aka fct de départ définie pp ? Là peut-être plus légitime que pour les
fcts, sinon quand il y a un saut, la fct de départ est tjs continue à gauche ?
Grpmh la déf est peut-être pas terrible. On ferait mieux d'intégrer sur
$\left[0, x\right[$ (ne serait-ce que pour avoir la "bonne" constante en 
$0$, et l'additivité) ; nécessaire alors de définir ça comme ça dans
la section sur la théorie de la mesure.

### TODO -- Fonction de variation localement bornée {.definition}

### TODO -- Existence d'une dérivée comme mesure {.proposition}
Fct de variation localement bornée iff dérivée est une mesure de Radon

### TODO -- Exemples

  - Equa diff encore, mais en prologeant $x(t)$ par $0$ pour $t \neq 0$

  - Proba et fct de répartition arbitraire.

### TODO -- Formule des sauts

Distributions
================================================================================

### TODO -- Distribution {.definition}
distribution d'ordre $k$ uniquement. Fonctionnelle définie sur les fcts
$C^k$ telle que si $C^k_0([a, b])$ désigne les fcts nulles
que leurs dérivée au bord, alors (restriction de $T$) 
linéaire bornée de $C^k_0([a, b])$ dans $\R$.

### TODO -- Mesure signée est une distribution

### TODO -- Dérivée d'une distribution

Proba / Fct répartition
================================================================================

Généralisation cas discret et à densité; dans les deux cas, fcts croissante
$\mathbb{R} \to \mathbb{R}$, nulle en $-\infty$, de variation 1, etc.

Montrer comment définir une mesure (extérieure) associée,
notation $\mu (= df)$ (Lebesgue-Stieltjes) ? 


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

Exercices
================================================================================

Fonctions lipschitzienne
--------------------------------------------------------------------------------

(d'une variable). Montrer qu'elles ont une dérivée faible (et donc pp),
en utilisante leur caractère absolument continu (cf. Evans-Gariepy dans
le cas multivariable) et que la dérivée (faible) est de norme plus petite
que la constante de Lipschitz.

Fonctions convexes
--------------------------------------------------------------------------------

Equivalent dérivée seconde est une mesure positive ?

Fonction distance
--------------------------------------------------------------------------------

Dérivées seconde fonction distance, squelette, courbure, etc ?