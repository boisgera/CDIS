% Calcul Intégral III
%
% [today](https://www.youtube.com/watch?v=Te7DR4iuJj8)

Intégrales Multiples
================================================================================

### TODO

rappel résultats analogues (du chap I et II) au cas réel.

### Pavés {.definition}
On appelle *pavé* tout sous-ensemble $I$ de $\mathbb{R}^n$ de la forme
$$
I = I_1 \times \dots \times I_n
$$
où les $I_i$ sont de intervalles de $\mathbb{R}$.

### Remarque {.reamrk .anonymous}
La notion de pavé généralise la notion d'intervalle de 
$\mathbb{R}$ à $\mathbb{R}^n$; le terme intervalle est d'ailleurs
parfois utilisé au lieu du terme pavé. 

### Subdivision pointée
Une *subdivision pointée* du pavé fermé $I$ de $\mathbb{R}^n$ est 
une famille finie 
$$
\{(t_i, I_i) \; | \; \; 0 \leq i \leq k-1\}
$$
où les $I_i$ sont des pavés fermés de $I$ sans chevauchement, 
qui recouvrent $I$, et tels que 
$t_i \in I_i$ pour tout $i \in \{0, \dots, k-1\}.$

### Volume d'un pavé
On appelle *volume* du pavé $I = I_1 \times \dots \times I_n$
la valeur
$$
v(I)  = \ell(I_1) \times \dots \times \ell(I_n) \in \left[0, +\infty \right],
$$
en adoptant la convention que $0 \times \infty = 0$.

### Longeur, aire, volume {.remark}
Dans $\mathbb{R}$, on pourra continuer à appeler cette grandeur
la longueur ; dans $\mathbb{R}^2$ il est approprié de la désigner
sous le terme d'aire. Si l'on souhaite distinguer le cas du
volume "classique" dans $\mathbb{R}^3$ et les autres dimensions, 
on pourra utiliser le terme d'*hypervolume* comme terme générique
et réserver le terme de volume au cas de $\mathbb{R}^3$.

### Somme de Riemman {.definition}

La somme de Riemann associée à la fonction $f:I \to \mathbb{R}$,
où $I$ est un pavé compact de $\mathbb{R}^n$,
et à la subdivision pointée $\mathcal{D}$ de $I$ est la grandeur
$$
S(f, \mathcal{D}) = \sum_{(t, I) \in \mathcal{D}} f(t) v(I)
$$

### Jauge {.definition}
Une jauge $\gamma$ sur un pavé $I$ de $\mathbb{R}^n$ est une 
fonction qui associe à tout $t \in I$ un 
intervalle ouvert $\gamma(t)$ de $\mathbb{R}^n$ contenant $t$. 

### Subdivision pointée subordonnée à une jauge {.definition}
Une subdivision $\mathcal{D}$ du pavé compact $I$ 
est *subordonnée à une jauge* $\gamma$ sur $I$ si pour tout 
$(t, J) \in \mathcal{D}$, $J \subset \gamma(t).$

### Intégrale dans $\mathbb{R}^n$ {.definition}
Soit $I$ un pavé de $\mathbb{R}^n$.
Une fonction $f:I \to \mathbb{R}$ est dite *intégrable 
(au sens de Henstock-Kurzweil)* s'il existe un réel $A$ tel
que pour tout $\varepsilon > 0$ il existe une jauge $\gamma$ de $\mathbb{R}^n$ 
et un pavé compact $K$ de $I$
tels que pour tout pavé compact $P$ vérifiant $K \subset P \subset I$
et pour toute subdivision pointée $\mathcal{D}$ de $P$ 
subordonnée à $\gamma$, on ait
$|S(f, \mathcal{D}) - A| \leq \varepsilon$.
Le réel $A$ quand il existe est unique; il est appelé
*intégrale de $f$ sur $\mathbb{R}^n$* et noté
$$
\int_{\mathbb{R}^n} f(t) \, dt.
$$

### Théorème de Fubini {.theorem}
Soit $f: \mathbb{R}^m\times \mathbb{R}^n \to \mathbb{R}$ 
une fonction intégrable.
Alors la fonction partielle $x \in \mathbb{R}^n \mapsto f(x, y)$ est intégrable 
pour presque tout $y \in \mathbb{R}^m$ et
$$
\int_{\mathbb{R}^{m+n}} f(t) \, dt = \int_{\mathbb{R}^m} \left[ \int_{\mathbb{R}^n} f(x, y) \, dx\right] dy
$$

### Démonstration {.proof}
Se reporter à @Swa01.

### TODO
Résultat en intervertissant $x$ et $y$, la réciproque ne marche pas
(donc la définition d'intégrale directement dans $\mathbb{R}^n$ est
"nécessaire", l'intégrale multiple "ne marche pas".)

### Changement de variables {.theorem}
Soient $D_1$ et $D_2$ des ouverts de $\mathbb{R}^n$ et 
$h: D_1 \to D_2$ une fonction continûment différentiable
ayant une fonction inverse $h^{-1}: D_2 \to D_1$ également 
continûment différentiable. Si $Dh$ désigne la matrice de Jacobi
associée à la différentielle de $h$,
la fonction $f: D_2 \to \mathbb{R}$ est absolument intégrable
si et seulement si la fonction $(f \circ h) |\det Dh| : D_1 \to \mathbb{R}$ 
est absolument intégrable et dans ce cas,
$$
\int_{D_2} f(y) \, dy = \int_{D_1} f(h(x)) |\det Dh(x)| \, dx.
$$


### Démonstration {.proof}
Se reporter à [@Swa01, annexe 5].

Théorème de Stokes
================================================================================

### TODO

Définition par une équation implicite (équivalent).
Que doit-on adopter comme définition ? Et quoi comme propriété ?
La définition par l'épigraphe est sans doute plus intuitive, 
mais sa formalisation plus lourde ... Je serais tenté dans le cours
oral de partir de la définition par l'épigraphe, informellement,
pour l'intuition (et de toute façon on a besoin de cette construction
pour la suite) puis d'énoncer rigoureusement la version
implicite, équivalente.

### Compact à bord régulier {.definition}

Un sous-ensemble $K$ de $\mathbb{R}^n$ est *un compact à bord $C^1$*
s'il est compact et peut être caractérisé au voisinage de tout point de
sa frontière $\partial K$, 
et après un éventuel changement de repère orthonormé direct,
comme l'épigraphe -- l'ensemble des points "au-dessus du graphe" -- 
d'une fonction de classe $C^1$.
Autrement dit, pour tout point $x \in \partial K$, 
il existe un ouvert non vide $V_x \subset \mathbb{R}^n$ de la forme
$V_x = U_x \times I_x$ où $U_x \subset \mathbb{R}^{n-1}$ et $I_x$ 
est un intervalle ouvert non vide de $\mathbb{R}$, 
une isométrie directe $T_x$ telle que $T_x(x) \in V_x$ 
et une fonction 
$f_x: y \in U_x \to I_x$ continûment différentiable tels que
$$
T_x(K) \cap V_x = \{(y_1,\dots, y_n) \in V_x \; | \;  f_x(y_1, \dots, y_{n-1}) \leq y_n\}
$$

### TODO

Vérifier qu'il n'est pas nécessaire (?) de spécifier indépendamment 
intérieur et frontière comme dans [@DZ11, p. 87].

Lister qq conséquences du fait d'être compact à bord (tq: adhérence de 
l'intérieur est l'ensemble, etc.), etc.
Notation $\Omega$, $\Gamma$, etc.

Définir normale (extérieure).

### Caractérisation implicite des compacts à bord régulier {.theorem}
Un sous-ensemble compact $K$ de $\mathbb{R}^n$ est un compact à bord $C^1$ 
si pour tout point $x$ de sa frontière $\partial K$ il existe un voisinage 
ouvert $V_x$ et une fonction continûment différentiable $f_x: V_x \to \mathbb{R}$ 
dont la différentielle est inversible en tout point, 
telle que pour tout point $y$ de $V_x$, $y$ appartient à $K$ 
si et seulement si $f_x(y) \leq 0$.

### TODO

Rendre explicite la normale extérieure dans ce cas et comment trouver
un axe orthonormé qui permet de se ramener au cadre de l'épigraphe.

Evoquer en remarque la notion de sous-variété de $\mathbb{R}^n$ ?


### TODO

Intégrale de surface, partition de l'unité, etc.

Preuve de Stokes (dans un patch, puis en général)
Enoncer version différentielle partielle de Stokes
(directement analogie à l'IPP en dimension 1, 
permet de se limiter à l'intégration de fcts scalaires en 
1ere approche et pas de perte de généralité; permet ensuite
d'étudier les "applications" (théorème de la divergence, etc.))

$$
\int_{\Omega} \partial_i f(x) \, dx
= 
\int_{\Gamma} f(x) n_i(x) \, S(dx)
$$

Exercices
================================================================================

Déformations
--------------------------------------------------------------------------------

$\Omega$ dans $U$ paramétrisé par une déformation $T = I + u$ avec $u$ petit
et une base $\Omega_0$ qui est un compact à bords $C^1$. Montrer que
si la base est un compact à bord $C^1$, les déformés aussi.

Exemples de compacts à bord (déterminés implicitement)
--------------------------------------------------------------------------------

... par la fonction distance orientée par exemple ?

Calcul
--------------------------------------------------------------------------------

Un calcul réalisable par Fubini et/ou Stokes ? Dans le disque unité ?
Avec un champ de vecteurs


Réferences
================================================================================