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

### Remarque {.remark .anonymous}
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

### TODO

Mention du fait qu'il est vraiment nécessaire de chercher l'absolue
intégrabilité. Retrouver la référence qui cite qu'avec une simple
rotation et l'intégrabilité conditionnelle ça ne marche pas.
C'est dans le Bullen -- Non-Absolute Integrale, mais pas détaillé
(Q: le texte utilise une rotation de $pi/4$ pour le contre-exemple.
Avec une rotation de $\pi/2$ ça marcherait ?).
Un exemple détaillé est donné dans 
"Petit traité d'intégration: Riemann, Lebesgue et Kurzweil-Henstock" 
(Jean-Yves Briend). L'exemple est compréhensible et intéressant;
peut faire l'objet d'un exercice technique semble faisable.

Tracer un parralèle avec les séries, ou il est connu que les séries
conditionnellement convergentes ne gardent pas cette propriété par
réordonnancement (exemple mono-dim ou bi-dim) ?

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

### TODO

Remplacer épigraphe par hypographe ? Ca me semble graphiquement plus
intuitif et ça colle sans doute mieux avec les exemples usuels 
(fonction distance orientée, conventions KKT, etc.), mais bien sûr pas
toujours (ex: carac convexité). OK, oui

### TODO
Minimiser le cadre "reprère orthonormé direct", par simplement 
"changement de repère"; cela simplifie l'enoncé, la preuve, etc.
et la contrainte "orthonormé direct" peut venir plus tard, 
en exercice? Pas évident, rédiger la preuve associé au passage
de l'hypographe à l'inégalité implicite et voir ce qui vient.
OK, ça devrait passer.

### Compact à bord régulier {.definition}

Un sous-ensemble $K$ de $\mathbb{R}^n$ est *un compact à bord $C^1$*
s'il est compact et peut être caractérisé au voisinage de tout point de
sa frontière $\partial K$, 
et après un éventuel changement de repère,
comme l'*hypographe* -- l'ensemble des points en-dessous du graphe -- 
d'une fonction de classe $C^1$.
Autrement dit, pour tout point $x_0 \in \partial K$, 
il existe un ouvert non vide $V \subset \mathbb{R}^n$ de la forme
$V = U \times I$ où $U \subset \mathbb{R}^{n-1}$ et $I$ 
est un intervalle ouvert non vide de $\mathbb{R}$, 
une application affine inversible $T$ telle que $T(x_0) \in V$ 
et une fonction 
$f: U \to I$ continûment différentiable tels que
$$
T(K) \cap V = \{(y_1,\dots, y_n) \in V \; | \;  y_n \leq f(y_1, \dots, y_{n-1})\}
$$


### TODO

Faire passer l'idée d'un ensemble borné délimité par une surface
$n-1$-dimensionelle (une "hypersurface"), "suffisamment régulière"
et qu'il n'y a plus qu'à trouver une façon de mesurer cette régularité.

### TODO

Vérifier qu'il n'est pas nécessaire (?) de spécifier indépendamment 
intérieur et frontière comme dans [@DZ11, p. 87].

Lister qq conséquences du fait d'être compact à bord (tq: adhérence de 
l'intérieur est l'ensemble, etc.), etc.
Notation $\Omega$, $\Gamma$, etc.
Caractériser la frontière de $K$ comme étant localement 
les points tels que $y_n = f(y_1, \dots, y_{n-1})$.

Evoquer "localement d'un seul coté" de la frontière ?

Définir normale (extérieure). Carac intrinsèque ?

### Caractérisation implicite des compacts à bord régulier {.theorem}
Un sous-ensemble compact $K$ de $\mathbb{R}^n$ est un compact à bord $C^1$ 
si pour tout point $x_0$ de sa frontière $\partial K$ il existe un voisinage 
ouvert $V$ de $x_0$ et une fonction continûment différentiable 
$g: V \to \mathbb{R}$ dont la différentielle est non-nulle en $x_0$, 
telle que pour tout point $x$ de $V$, $x$ appartient à $K$ 
si et seulement si $g(x) \leq 0$.

### Démonstration {.proof}
Si $K$ est un compact à bord $C^1$, il existe un ouvert non vide 
$V \subset \mathbb{R}^n$ de la forme
$V = U \times I$ où $U \subset \mathbb{R}^{n-1}$ et $I$ 
est un intervalle ouvert non vide de $\mathbb{R}$, 
une application affine inversible $T$ telle que $T(x_0) \in V$ 
et une fonction 
$f: U \to I$ continûment différentiable tels que
$$
T(K) \cap V = \{(y_1,\dots, y_n) \in V \; | \;  y_n \leq f(y_1, \dots, y_{n-1})\}.
$$
Par conséquent, si l'on définit la fonction $g: V \to \mathbb{R}$ par
$$
g(x) = y_n - f(y_1, \dots, y_{n-1}) \, \mbox{ où } \,
(y_1, \dots, y_n) = T^{-1}(x),
$$
on obtient la caractérisation implicite souhaitée.
La seule vérification qui n'est pas évidente par construction 
est le caractère non-nul de la différentielle $dg$. 
Si $T(x) =  A \cdot x + b$ où $A$ est une application linéaire 
(nécessairement inversible) et $b \in \mathbb{R}^n$, 
en posant $\phi(y) = y_n - f(y_1, \dots, y_{n-1})$, on
obtient 
$$
dg(x) = d\phi(T(x)) \cdot dT^{-1}(x) = d\phi(T(x)) \cdot A^{-1}.
$$
Or, $\partial_n \phi(y) = 1$ en tout point $y$ de $V$. 
L'application $A^{-1}$ étant inversible, 
il existe un vecteur $h$ de $\mathbb{R}^n$ tel que
$A^{-1} \cdot h = (0, \dots, 0, 1)$; pour un tel vecteur on a donc
$$
dg(x) \cdot h = d\phi(T(x)) \cdot A^{-1} \cdot h = 
\sum_{i} \partial_i \phi(T(x)) (A^{-1} \cdot h)_i = 1.
$$
La différentielle de $g$ est donc bien non nulle.

Réciproquement, considérons un $x_0 \in \partial K$ et supposons qu'il existe 
une fonction $g: V \to \mathbb{R}$ satisfaisant les propriétés de l'énoncé. 
La différentielle de $g$ étant non nulle en $x_0$, il exists un vecteur de $u$ 
de $\mathbb{R}^n$ tel que 
$$
dg(x) \cdot u > 0
$$
dans un voisinage $V'$ de $x_0$ contenu dans $V$. 
Soit $T$ une application affine inversible de la forme 
$T(x) = A \cdot x + b$ telle que $A \cdot u = e_n$.
La fonction $g \circ T^{-1}$ définie sur un voisinage ouvert de $T(x_0)$
satisfait alors
$$
\begin{split}
\partial_n (g \circ T^{-1})(y) &= dg(T^{-1}(y)) \cdot dT^{-1}(y) \cdot e_n \\
&= dg(T^{-1}(y)) \cdot A^{-1} \cdot e_n  \\
&= dg(T^{-1}(y)) \cdot u > 0 \\
\end{split}
$$
L'application du théorème des fonctions implicite fournit
un ouvert non vide $V \subset \mathbb{R}^n$ de la forme
$V = U \times I$ où $U \subset \mathbb{R}^{n-1}$ et $I$ 
est un intervalle ouvert non vide de $\mathbb{R}$ et une fonction 
$f: U \to I$ continûment différentiable telle que
$$
g \circ T^{-1}(y_1,\dots,y_n) = 0 
\, \Leftrightarrow \, 
y_n = f(y_1,\dots, y_{n-1}).
$$
Par le théorème fondamental du calcul,
$$
\begin{split}
g \circ T^{-1}(y_1,\dots,y_n) &= 
g \circ T^{-1}(y_1,\dots,f(y_1, \dots, y_{n-1})) \\
& \phantom{=}+
\int_{f(y_1, \dots, y_{n-1})}^{y_n}
\partial_n  (g\circ T^{-1})(y_1,\dots,y_{n-1}, t) \, dt \\
&=
\int_{f(y_1, \dots, y_{n-1})}^{y_n}
\partial_n  (g\circ T^{-1})(y_1,\dots,y_{n-1}, t) \, dt, \\
\end{split}
$$
ce qui garantit que dans $V$, $(g \circ T^{-1})(y) \leq 0$
-- c'est-à-dire $x = T^{-1}(y) \in K$ --
si et seulement si $f(y_1, \dots, y_{n-1}) \leq y_n$.

### TODO

Rendre explicite la normale extérieure dans ce cas et 
un peu plus explicitement (sur un exemple ?) comment trouver
un axe (orthonormé ?) qui permet de se ramener au cadre de 
l'épigraphe. Sur $x^2 + y^2 - 1 \leq 0$ par exemple.


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

### TODO
Perspective sur les versions plus "relaxées" du théorème de Stokes,
qu'il s'agisse du bord Lipschitz ou des travaux (Mawhin, Pfeffer, etc.)
pour demander moins que $C^1$ sur l'intégrande ?


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