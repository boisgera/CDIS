% Calcul Intégral III

### TODO

  - MCT, DCT. **NON**, transférer au chapitre précédent

  - Intervalle (ou "pavé") dans $\mathbb{R}^n$, par analogie avec le cas
    réel (via les points intermédiaires) ou comme produit d'intervalles
    réels.

  - Intégrale dans $\mathbb{R}^n$, Fubini, formule de changement de variable

  - Compact à bord régulier (par épigraphe et comme solution d'une
    inégalité (avec équivalence par IFT)), normale, intégrale de surface, 
    formule de Stokes.

Théorèmes de Convergence
================================================================================

Intégrales Multiples
================================================================================

Théorème de Stokes
================================================================================

### TODO



### Compact à bord régulier {.definition}

Un sous-ensemble $K$ de $\mathbb{R}^n$ est *un compact à bord $C^1$*
s'il est compact et peut être caractérisé au voisinage de tout point de
sa frontière $\partial K$, 
et après un éventuel changement de repère orthonormé direct,
comme l'épigraphe d'une fonction de classe $C^1$.
Autrement dit, pour tout point $x \in \partial K$, 
il existe un ouvert non vide $V_x \subset \mathbb{R}^n$ de la forme
$V_x = U_x \times I_x$ où $U_x \subset \mathbb{R}^{n-1}$ et $I_x$ 
est un intervalle ouvert non vide de $\mathbb{R}$, 
une isométrie directe $T_x$ telle que $T_x(x) \in V_x$ 
et une fonction 
$f_x: y \in U_x \to I_x$ continûment différentiable tels que
$$
T_x(K) \cap V_x = \{(y_1,\dots, y_n) \in V_x \; | \; y_n \leq f_x(y_1, \dots, y_{n-1})\}
$$



### TODO

Vérifier qu'il n'est pas nécessaire (?) de spécifier indépendamment 
intérieur et frontière comme dans [@DZ11, p. 87].

Exercices
================================================================================

Déformations
--------------------------------------------------------------------------------

$\Omega$ dans $U$ paramétrisé par une déformation $T = I + u$ avec $u$ petit
et une base $\Omega_0$ qui est un compact à bords $C^1$. Montrer que
si la base est un compact à bord $C^1$, les déformés aussi.

Réferences
================================================================================