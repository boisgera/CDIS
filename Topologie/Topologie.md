% Topologie

\newcommand{\R}{\mathbb{R}}


Complétude
================================================================================

### TODO:

  - evn, espace métrique (comme sous-ensemble d'un e.v.n.), 
    suite de Cauchy, complétude

  - application lipschitzienne, (et lip est cont) contractante, 
    $\kappa$-contractante

### Théorème de Point Fixe de Banach {.definition .theorem}

Soit $f: E \to E$ une application contractante dans un espace métrique $E$.
Si l'espace $E$ est complet, l'application $f$ admet un unique *point fixe* $x$,
c'est-à-dire une unique solution $x \in E$ à l'équation
  $$
  x = f(x).
  $$

### Démonstration {.proof}

L'unicité du point fixe (l'existence d'au plus une solution à $x=f(x)$) est
simple à établir: si $x$ et $y$ sont deux points fixes de $f$, c'est-à-dire 
si $x=f(x)$ et $y=f(y)$, alors $\|x - y\| = \|f(x) - f(y)\|$. 
L'application $f$ étant $\kappa$-contractante, on a donc
$$
\|x - y\| = \|f(x) - f(y)\| \leq \kappa \|x - y\|;
$$
et puisque $0\leq \kappa < 1$, cette inégalité entraîne $\|x - y\| = 0$, 
soit $x=y$.

Quant à l'existence du point fixe, sa preuve est constructive: 
nous allons établir que quel que soit le choix de $x_0 \in E$, 
la suite de valeurs définie par
$$
x_{n+1} = f(x_n)
$$
converge vers le point fixe. 
Le point crucial est d'établir que cette suite
admet une limite $x_{\infty}$; en effet, si ce résultat est acquis, 
en passant à la limite sur $n$ dans la relation de récurrence, 
et exploitant la continuité de l'application $f$, on obtient
$$
x_{\infty} = \lim_{n \to +\infty} x_{n+1} = \lim_{n \to +\infty}f(x_n) = f(x_{\infty}).
$$
A cette fin, nous allons prouver que la suite des $x_n$ est de Cauchy; 
l'existence d'une limite se déduira alors de la complétude de $E$. 
On remarque tout d'abord que pour tout entier $n$, 
$$
\|x_{n+2} - x_{n+1}\| = \|f(x_{n+1}) - f(x_n)\| \leq \kappa \|x_{n+1} - x_n\|,
$$
ce qui par récurrence fournit pour tout $n$
$$
\|x_{n+1} - x_n\| \leq \kappa^n \|x_1 - x_0\|.
$$
Par conséquent, pour tout couple d'entiers $n$ et $p$, on a
$$
\|x_{n+p} - x_n\| 
\leq \sum_{k=0}^{p-1} \|x_{n+k+1} - x_{n+k}\|
\leq \sum_{k=0}^{p-1} \kappa^{n+k} \|x_{1} - x_{0}\|.
$$
Dans le second membre apparaît une somme de termes d'une suite géométrique:
$$
\sum_{k=0}^{p-1} \kappa^{n+k} = \kappa^n \frac{1 - \kappa^{p}}{1 - \kappa}
\leq \frac{\kappa^n}{1 - \kappa};
$$
on en déduit
$$
\|x_{n+p} - x_n\| 
\leq  
\frac{\kappa^n}{1 - \kappa} \|x_{1} - x_{0}\|.
$$
Le second membre de cette inégalité tendant vers $0$ indépendamment de $p$
quand $n$ tend vers $+\infty$, la suite des $x_n$ est bien de Cauchy, ce
qui conclut la preuve.


### TODO

Applis, exemples, par exemple dans le cas matriciel, 
pour la résolution des systèmes linéaires, lien avec la norme d'opérateur.

Compacité
================================================================================

### Compacité séquentielle {.definition}
Un ensemble $E$ est *(séquentiellement) compact* si toute suite de valeurs de 
$E$ admet une sous-suite convergeant dans $E$.

### Image d'un compact {.theorem}
L'image d'un ensemble compact par une application continue est un ensemble
compact.

### Existence d'un minimum {.corollary #T-EM}
Une fonction continue $f: K \to \mathbb{R}$ définie sur un ensemble compact 
$K$ admet un minimum global.

### Théorème de Heine-Borel {.theorem}
Un ensemble $E$ de $\R^n$ est compact 
si et seulement si il est fermé et borné.

Exercices
================================================================================

Comparaison des normes
--------------------------------------------------------------------------------

TODO: comparaison manuelle, meilleure bornes

Normes d'opérateurs
--------------------------------------------------------------------------------

Changer les normes au départ et à l'arrivée, calculer les normes d'opérateurs
associées sur la base d'une représentation matricielle (ex: norme sup au 
départ et à l'arrivée)

Fonctions définies par un recouvrement
--------------------------------------------------------------------------------

Soit une fonction définie par la donnée de 
ses restrictions $f_A$ aux ensembles $A \in \mathcal{A}$.
Ce procédé permet de définir uniquement la fonction $f$ sur l'ensemble
$$
\mbox{dom}(f) = \bigcup_{A \in \mathcal{A}} A
$$
à condition que les restrictions soient compatibles
$$
x\in A \cap B, \, A \in \mathcal{A}, \, B \in \mathcal{A}
\, \Rightarrow \, 
f_A(x) = f_B(x).
$$

  1. On suppose que les fonctions $f_A$, $A \in \mathcal{A}$ sont continues.
     Est-ce que la fonction $f$ est nécessairement continue ?
     Dans le cas contraire, quelle condition "raisonnable" portant sur
     la collection $\mathcal{A}$ faut-il ajouter pour s'assurer du résultat ?

  2. Application angle sur l'hélice et $\arctan$ ...

### Réponse {.answer}

**TODO**

Equations Linéaires et Point Fixes
--------------------------------------------------------------------------------

Préparer et résoudre numériquement des systèmes de la forme $A x = b$ dans
des cas simples (ex: Jacobi, Gauss-Seidel, cas diagonally dominant ?).

Exemples concrets (ex: Poisson Image editing) et exemples ou "ça ne marche pas"
en itérant sans s'assurer du caractère contractant. 

Lien norme d'opérateur et rayon spectral ???



Nombres Réels de Bishop ?
--------------------------------------------------------------------------------

(illustration des suites de Cauchy ?)

Compacité et Continuité
--------------------------------------------------------------------------------

Montrer la réciproque du [résultat d'existence d'un minimum pour une fonction
numérique continue définie sur un compact](#T-EM), à savoir:

Si l'ensemble $E \subset \mathbb{R}^n$ n'est pas compact, 
il existe une fonction continue $f: E \to \mathbb{R}$ 
n'ayant pas de minimum.

### Réponse {.answer}

**TODO**

Fonctions propres
--------------------------------------------------------------------------------

Soit $f: \mathbb{R}^n \to \mathbb{R}$ une fonction continue et propre,
c'est-à-dire telle que
$$
f(x) \to +\infty \mbox{ quand } \|x\| \to +\infty.
$$

Montrer que les ensembles de sous-niveaux de $f$, de la forme
$$
\{x \in \mathbb{R}^n \, | \, f(x) \leq c\}, \, c \in \mathbb{R}
$$
sont compacts.