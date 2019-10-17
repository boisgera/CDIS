% Calcul Intégral III

<!-- LaTeX Macros -->
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}

Intégrales Multiples
================================================================================

Définitions
--------------------------------------------------------------------------------

### {.remark .ante}
Les pavés joueront dans $\R^n$ le rôle dévolu aux intervalles dans $\R$ :

### Pavés {.definition}
On appelle *pavé* de $[-\infty,+\infty]^n$ tout ensemble $I$ de la forme
$$
I = I_1 \times \dots \times I_n
$$
où les $I_i$ sont des intervalles de $[-\infty,+\infty]$.

### Volume d'un pavé
On appelle *volume* du pavé $I = I_1 \times \dots \times I_n$ de $[-\infty,+\infty]^n$
la valeur
$$
v(I)  = \ell(I_1) \times \dots \times \ell(I_n) \in \left[0, +\infty \right],
$$
en adoptant la convention que $0 \times \infty = 0$.

### Longeur, aire, volume {.remark}
On pourra continuer à appeler cette grandeur
*longueur* plutôt que *volume* si l'on travaille dans $\R$ 
(ou $[-\infty,+\infty]$) ; 
dans $\R^2$ (ou $[-\infty,+\infty]^2$) il est approprié 
de la désigner sous le terme d'*aire*. 
Si l'on souhaite distinguer le cas du
volume "classique" dans $\R^3$ (ou $[-\infty,+\infty]^3$) et les autres dimensions, 
on pourra utiliser le terme d'*hypervolume* comme terme générique
et réserver le terme de *volume* au cas tri-dimensionnel.

### Subdivision pointée
Une *subdivision pointée* du pavé fermé $I$ de 
$[-\infty,+\infty]^n$ est 
une famille finie 
$$
\{(t_i, J_i) \; | \; \; 0 \leq i \leq k-1\}
$$
où les $J_i$ sont des pavés fermés de $I$ sans chevauchement
-- les intersections deux à deux de leurs intérieurs sont vides --
qui recouvrent $I$ et tels que 
$t_i \in J_i$ pour tout $i \in \{0, \dots, k-1\}.$


### Somme de Riemman {.definition}
La somme de Riemann associée à la fonction $f:I \to \mathbb{R}$,
où $I$ est un pavé fermé de $[-\infty,+\infty]^n$ 
et à la subdivision pointée $\mathcal{D}$ 
de $I$ est la grandeur
$$
S(f, \mathcal{D}) = \sum f(t) v(J), \; (t, J) \in \mathcal{D}, \, v(J) < + \infty.
$$

### Jauge {.definition}
Une jauge $\gamma$ sur un pavé fermé $I$ de $[-\infty,+\infty]^n$ est une 
fonction qui associe à tout $t \in I$ un 
pavé ouvert $\gamma(t)$ de $[-\infty,+\infty]^n$ contenant $t$. 

### Subdivision pointée subordonnée à une jauge {.definition}
Une subdivision $\mathcal{D}$ du pavé fermé $I$ de $[-\infty,+\infty]^n$
est *subordonnée à une jauge* $\gamma$ sur $I$ si pour tout 
$(t, J) \in \mathcal{D}$, $J \subset \gamma(t).$

### Intégrale dans $\mathbb{R}^n$ {.definition}
Une fonction $f:\R^n \to \R$ est dite *intégrable 
(au sens de Henstock-Kurzweil)* s'il existe un réel $A$ tel
que pour tout $\varepsilon > 0$ il existe une jauge $\gamma$ de 
$[-\infty,+\infty]^n$ telle que pour 
toute subdivision pointée $\mathcal{D}$ de $[-\infty,+\infty]^n$
subordonnée à $\gamma$, on ait
$|S(f, \mathcal{D}) - A| \leq \varepsilon$.
Le réel $A$ quand il existe est unique ; 
il est appelé *intégrale de $f$ sur $\R^n$* et noté
$$
\int f \; \mbox{ ou } \;
\int_{\R^n} f(x) \, dx \; \mbox{ ou } \; \int_{\R^n} f(x_1,\dots, x_n) \, dx_1\dots dx_n.
$$

### {.post}
Comme dans le cas réel, la définition supposerait que $f$ soit a priori
définie sur $[-\infty,+\infty]^n$ plutôt que sur $\R^n$ ; 
mais on peut étendre $f$ pour des arguments à l'infini 
(dont au moins l'une des composantes est infinie) 
sans que l'intégrabilité de cette extension ou la valeur de son intégrale
ne soient affectés par le choix de ces valeurs.

Propriétés élémentaires
--------------------------------------------------------------------------------

Nous évoquons rapidement dans cette section la façon dont les propriétés 
de l'intégrale dans $\R$ se transposent à $\R^n$.

L'intégrale dans $\R^n$ est toujours linéaire et positive ;
l'intégrabilité peut être testée par un critère de Cauchy analogue au cas réel.
La notion d'ensemble négligeable est similaire au cas réel, à ceci près
qu'on utilise des pavés au lieu d'intervalles et le volume au lieu de la
longueur ; comme dans le cas réel, des fonctions égales presque partout
sont intégrables simultanément et ont la même intégrale.

Un théorème de changement de variable existe, mais il diffère quelque peu
du résultat élémentaire déjà traité dans $\R$
(par certains aspects, il est plus général) ; 
il possède dans sa propre sous-section dans ce chapitre.
L'équivalent dans $\R^n$ du théorème fondamental du calcul est le théorème
de la divergence[^pe] auquel une section entière de ce chapitre est consacrée.

[^pe]: même si cela ne saute pas forcément aux yeux !

Les théorème de convergence (dominée, monotone) et le critère d'intégrabilité
dominée se transposent directement.
La notion d'ensemble mesurable est inchangée (modulo le remplacement des
intervalles compact de $\R$ par les pavés compacts de $\R^n$) ; les trois
propriétés élémentaires de la collection des ensembles mesurables de $\R^n$
sont toujours vérifiées (la collection est une tribu), cette famille contient
tous les fermés (et tous les ouverts) et "négligeable" et 
"(mesurable et) de volume nul" sont toujours synonymes.

Les fonctions mesurables ont la même definition (limite simple de fonctions
intégrables) ; le critère de mesurabilité par l'image réciproque est toujours
valide. L'intégrabilité (et les intégrales) des fonctions définies sur des 
sous-ensembles de $\R^n$ (ou $[-\infty, +\infty]^n$) sont toujours définies
à partir de l'extension de la fonction par zéro. Les fonctions absolument 
et conditionnellement intégrables sont définies de manière identique.

Théorème de Fubini
--------------------------------------------------------------------------------

### Théorème de Fubini {.theorem #Fubini}
Soit $f: \mathbb{R}^m\times \mathbb{R}^n \to \mathbb{R}$ 
une fonction intégrable.
Alors la fonction partielle $x \in \mathbb{R}^n \mapsto f(x, y)$ est intégrable 
pour presque tout $y \in \mathbb{R}^n$, la fonction définie presque partout
$$
y \in \R^n \mapsto \int_{\R^m} f(x, y) \, dx
$$
est intégrable et
$$
\int_{\mathbb{R}^{m+n}} f(z) \, dz = \int_{\mathbb{R}^m} \left[ \int_{\mathbb{R}^n} f(x, y) \, dx\right] dy.
$$
De même, la fonction partielle $y \in \mathbb{R}^n \mapsto f(x, y)$ est intégrable 
pour presque tout $x \in \mathbb{R}^m$, la fonction définie presque partout
$$
x \in \R^m \mapsto \int_{\R^n} f(x, y) \, dy
$$
est intégrable et
$$
\int_{\mathbb{R}^{m+n}} f(z) \, dz =
\int_{\mathbb{R}^n} \left[ \int_{\mathbb{R}^m} f(x, y) \, dy\right] dx.
$$

### Démonstration {.proof}
Se reporter à @Swa01.

### {.ante .post .remark}
On peut noter que pour appliquer le théorème de Fubini, il faut savoir 
a priori que $f$ est intégrable, or fréquemment on souhaiterait pouvoir
déduire l'intégrabilité de l'examen des intégrales itérées. Le théorème
de Fubini peut alors être complété utilement par le théorème de Tonelli :

### Théorème de Tonelli {.theorem #Tonelli}
Soit $f: \mathbb{R}^m\times \mathbb{R}^n \to \mathbb{R}$ une fonction
mesurable. Si pour presque tout $y \in \R^m$ la fonction
$x \in \R^n \mapsto |f(x, y)|$ est intégrable et que la fonction
définie presque partout
$$
y \in \R^m \mapsto \int_{\mathbb{R}^n} |f(x, y)| \, dx
$$
est intégrable, alors la fonction $f$ est (absolument) intégrable.

### Démonstration {.proof}
Se reporter à @Swa01.

Changement de variables
--------------------------------------------------------------------------------

### Changement de variables {.theorem}
Soient $D_1$ et $D_2$ des ouverts de $\mathbb{R}^n$ et 
$h: D_1 \to D_2$ un $C^1$-difféomorphisme de $D_1$ sur $D_2$ :
une fonction continûment différentiable et bijective
dont l'inverse $h^{-1}: D_2 \to D_1$ également continûment différentiable. 
La matrice de Jacobi associée à la différentielle de $h$ étant notée $J_h$,
la fonction $f: D_2 \to \mathbb{R}$ est absolument intégrable
si et seulement si la fonction $(f \circ h) |\det J_h| : D_1 \to \mathbb{R}$ 
est absolument intégrable et dans ce cas,
$$
\int_{D_2} f(y) \, dy = \int_{D_1} f(h(x)) |\det J_h(x)| \, dx.
$$


### Démonstration {.proof}
Se reporter à [@Swa01, annexe 5].

### {.post .remark}
L'absolue intégrabilité -- et pas simplement l'intégrabilité -- de la fonction
est une hypothèse cruciale de ce théorème de changement de variables. 
On peut en effet exhiber une fonction $f:\R^2 \to \R$ qui soit intégrable,
mais telle que quand $h$ désigne la rotation centrée à l'origine d'angle
$\pi/4$, la fonction $f \circ h$ ne soit pas intégrable[^ref-ai].
Comme dans ce cas on a $|\det J_h| = 1$ sur tout $\R^2$, cela contredit
la conclusion du théorème de changement de variables.

[^ref-ai]: cf. [@Swa01, ex. 29, p. 98].

### {.post .remark}
La situation est assez similaire à celles des séries réelles. 
On sait en effet que si la série $\sum_k a_k$ est absolue
convergente, un réordonnancement des termes de la série n'a pas d'effet,
ni sur la convergence de la série ni sur la valeur de la somme ;
pour toute bijection $\sigma: \N \to \N$,
$$
\sum_{k=0}^{+\infty} a_{\sigma(k)} = \sum_{k=0}^{+\infty} a_{k}.
$$
Par contre, si $\sum_k a_k$ est conditionnellement convergente 
(c'est-à-dire convergente, mais telle que $\sum_k |a_k|$ soit divergente ; 
par exemple, $a_k = (-1)^k / (k+1)$), il existe un réordonnancement 
$\sigma$ tel que $\sum_k a_{\sigma(k)}$ n'ait pas de limite 
(ni finie ni infinie).
Pour toute valeur limite 
$\ell \in [-\infty, +\infty]$ souhaitée de la somme, 
on peut aussi construire un réordonnancement $\sigma$ tel que
$$
\sum_{k=0}^{+\infty} a_{\sigma(k)} = \ell.
$$

<!--
### TODO
Mention du fait qu'il est vraiment nécessaire de chercher l'absolue
intégrabilité. Retrouver la référence qui cite qu'avec une simple
rotation et l'intégrabilité conditionnelle ça ne marche pas.
C'est dans le Bullen -- Non-Absolute Integrale, mais pas détaillé
(Q: le texte utilise une rotation de $\pi/4$ pour le contre-exemple.
Avec une rotation de $\pi/2$ ça marcherait ?).
Un exemple détaillé est donné dans 
"Petit traité d'intégration: Riemann, Lebesgue et Kurzweil-Henstock" 
(Jean-Yves Briend). L'exemple est compréhensible et intéressant;
peut faire l'objet d'un exercice technique semble faisable.
(note: aussi exercice similaire dans le Swarz)
-->

<!--

Tracer un parralèle avec les séries, ou il est connu que les séries
conditionnellement convergentes ne gardent pas cette propriété par
réordonnancement (exemple mono-dim ou bi-dim) ?

-->

Théorème de la divergence
================================================================================

<!--
### TODO:
Deux façon raisonnables de définir un compact à bord sont données;
la troisème (localement demi-espace après transfo par difféo) peut trouver
sa place en exo ?
-->

### Compact à bord régulier {.definition #cbr}
Un sous-ensemble $K$ de $\mathbb{R}^n$ est *un compact à bord $C^1$*
s'il est compact et peut être caractérisé au voisinage de tout point de
sa frontière $\partial K$, 
et après un éventuel changement de repère,
comme l'*hypographe* -- l'ensemble des points en-dessous du graphe -- 
d'une fonction continûment différentiable.
Autrement dit, pour tout point $x_0 \in \partial K$, 
il existe une application affine inversible $T: \R^n \to \R^n$ et
un voisinage ouvert $V$ de $x_0$ de la forme $V = T(U \times I)$,
où $U$ est un ouvert de $\mathbb{R}^{n-1}$ et $I$ 
est un intervalle ouvert de $\mathbb{R}$, et une fonction 
$f: U \to I$ continûment différentiable tels que
$$
K \cap V = T\left(\{(y_1,\dots, y_n) \in U \times I \; | \;  y_n \leq f(y_1, \dots, y_{n-1})\}\right).
$$

### Changement de repère orthonormé {.remark #cbr-isom}
Il est possible d'imposer dans [la définition des compacts à bord $C^1$](#cbr)
que $T$ soit une isométrie directe (qui conserve la distance et l'orientation) ; 
cela revient à n'autoriser que les changements de repère orthonormés directs. 
La caractérisation des compacts
à bord $C^1$ qui en résulte est inchangée.

<!--
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

-->

### Caractérisation implicite des compacts à bord régulier {.theorem #cbr-implicit}
Un sous-ensemble compact $K$ de $\mathbb{R}^n$ est un compact à bord $C^1$ 
si pour tout point $x_0$ de sa frontière $\partial K$ il existe un voisinage 
ouvert $V$ de $x_0$ et une fonction continûment différentiable 
$g: V \to \mathbb{R}$ dont la différentielle est non nulle en $x_0$, 
telle que pour tout point $x$ de $V$, $x$ appartient à $K$ 
si et seulement si $g(x) \leq 0$.

### Démonstration {.proof}
Si $K$ est un compact à bord $C^1$, il existe 
une application affine inversible $T: \R^n \to \R^n$ et
un voisinage ouvert $V$ de $x_0$ de la forme $V = T(U \times I)$,
où $U$ est un ouvert de $\mathbb{R}^{n-1}$ et $I$ 
est un intervalle ouvert de $\mathbb{R}$, et une fonction 
$f: U \to I$ continûment différentiable tels que
$$
K \cap V = T\left(\{(y_1,\dots, y_n) \in U \times I \; | \;  y_n \leq f(y_1, \dots, y_{n-1})\}\right).
$$
Par conséquent, si l'on définit la fonction $g: V \to \mathbb{R}$ par
$$
g(x) = y_n - f(y_1, \dots, y_{n-1}) \, \mbox{ où } \,
(y_1, \dots, y_n) = T^{-1}(x),
$$
on obtient la caractérisation implicite souhaitée.
La seule vérification qui n'est pas évidente par construction 
est le caractère non-nul de la différentielle $dg$ en $x_0$. 
Si $T(x) =  A \cdot x + b$ où $A$ est une application linéaire 
(nécessairement inversible) et $b \in \mathbb{R}^n$, 
en posant $\phi(y) = y_n - f(y_1, \dots, y_{n-1})$, on
obtient 
$$
dg(x) = d (\phi \circ T^{-1})(x) = d\phi(T^{-1}(x)) \cdot dT^{-1}(x) 
= d\phi(T^{-1}(x)) \cdot A^{-1}.
$$
Or, $\partial_n \phi(y) = 1$ en tout point $y$ de $U \times I$. 
L'application $A^{-1}$ étant inversible, 
il existe un vecteur $h$ de $\mathbb{R}^n$ tel que
$A^{-1} \cdot h = (0, \dots, 0, 1)$ ; 
pour un tel vecteur on a donc
$$
dg(x) \cdot h = d\phi(T^{-1}(x)) \cdot A^{-1} \cdot h = 
\sum_{i=1}^n \partial_i \phi(T^{-1}(x)) (A^{-1} \cdot h)_i = 1.
$$
La différentielle de $g$ est donc bien non-nulle en tout point de $V$
(et donc a fortiori en $x_0$).

Réciproquement, considérons un $x_0 \in \partial K$ et supposons qu'il existe 
une fonction $g: V \to \mathbb{R}$ satisfaisant les propriétés de l'énoncé. 
La différentielle de $g$ étant non nulle en $x_0$, par continuité de
l'application $x \mapsto dg(x) \cdot u$ pour tout $u \in \R^n$, 
il existe un vecteur de $u$ de $\R^n$ tel que 
$$
dg(x) \cdot u > 0
$$
dans un voisinage $V'$ de $x_0$ contenu dans $V$. 
Soit $T$ une application affine inversible de la forme 
$T(x) = A \cdot x + b$ telle que $A \cdot e_n = u$.
La fonction $g \circ T$ définie sur de $T^{-1}(V')$
satisfait alors
$$
\begin{split}
\partial_n (g \circ T)(y) &= dg(T(y)) \cdot dT(y) \cdot e_n \\
&= dg(T(y)) \cdot A \cdot e_n  \\
&= dg(T(y)) \cdot u > 0. \\
\end{split}
$$
L'application du théorème des fonctions implicites fournit
un ouvert non vide $U \times I$ inclus dans $T^{-1}(V')$ 
où $U \subset \mathbb{R}^{n-1}$ et
$I$ est un intervalle ouvert de $\mathbb{R}$, 
ainsi qu'une fonction $f: U \to I$ continûment différentiable telle que
dans $U \times I$,
$$
g \circ T(y_1,\dots,y_n) = 0 
\, \Leftrightarrow \, 
y_n = f(y_1,\dots, y_{n-1}).
$$
Par le théorème fondamental du calcul,
$$
\begin{split}
g \circ T(y_1,\dots,y_n) &= 
g \circ T(y_1,\dots,f(y_1, \dots, y_{n-1})) \\
& \phantom{=}+
\int_{f(y_1, \dots, y_{n-1})}^{y_n}
\partial_n  (g\circ T)(y_1,\dots,y_{n-1}, t) \, dt \\
&=
\int_{f(y_1, \dots, y_{n-1})}^{y_n}
\partial_n  (g\circ T)(y_1,\dots,y_{n-1}, t) \, dt, \\
\end{split}
$$
ce qui garantit que dans $T(U \times I)$, $g(x) \leq 0$
-- c'est-à-dire $x \in K$ --
si et seulement si $x = T(y)$ et $y_n \leq f(y_1, \dots, y_{n-1})$.

### Normale extérieure {.definition}
Une *normale* à un compact à bord $C^1$ $K$ de $\R^n$
en un point $x \in \partial K$ de sa frontière est un vecteur 
$n(x) \in \R^n$ unitaire (de norme $1$) tel que
$$
\lim_{\substack{y \to x \\ y \in \partial K}} \left<n(x), \frac{y-x}{\|y-x\|}\right> = 0.
$$
Cette normale $n(x)$ est *extérieure* si pour $\varepsilon>0$ assez petit, 
$x + \varepsilon n(x) \not \in K$.

### {.post .ante}
On admettra l'unicité de la normale extérieure ainsi définie ; 
son expression peut être calculée simplement dans le cas d'une représentation
implicite ou explicite (comme hypographe) du compact à bord.


### Normale extérieure et caractérisation implicite {.proposition #neci}
Si $K$ est un compact à bord $C^1$ caractérisé au voisinage de 
$x_0 \in \partial K$ par l'inégalité $g(x) \leq 0$, 
où $V$ est un voisinage ouvert de $x$ et $g: V \to \mathbb{R}$
est continûment différentiable de différentielle non nulle sur $V$, 
alors la *normale extérieure* de $K$ en $x \in \partial K \cap V$ 
est le vecteur de $\mathbb{R}^n$ donné par
$$
n(x) = \frac{\nabla g(x)}{\|\nabla g(x)\|}.
$$

### Démonstration {.proof}
La fonction $g$ étant différentiable en $x \in \partial K$, 
on a localement
$$
g(y) = g(x) + dg(x) \cdot (y - x) + o(\|y - x\|)
=\left<\nabla g(x), y-x \right> + o(\|y-x\|).
$$
Si $y \in \partial K$, $g(y) = 0$, donc 
$$
\left<\nabla g(x), \frac{y-x}{\|y-x\|} \right> = o(1)
\to 0 \, \mbox{ quand } \, y \to x.
$$
Si $y = x + \varepsilon \nabla g(x) /\|\nabla g(x)\|$, avec $\varepsilon >0$,
$$
g(y) = \left<\nabla g(x), y-x \right> + o(\|y-x\|)
= \varepsilon \|\nabla g(x)\| + o(\varepsilon),
$$
et donc $g(y) > 0$ -- soit $y \not \in K$ -- 
pour $\varepsilon$ suffisamment petit.

### Normale extérieure et hypographe {.proposition #neh}
Si $K$ est un compact à bord $C^1$ caractérisé au voisinage de 
$x_0 \in \partial K$ comme l'hypographe de la fonction 
$f: U \to I$ où $U$ est un ouvert de $\mathbb{R}^{n-1}$ et $I$ 
un intervalle ouvert de $\mathbb{R}$, alors
la normale extérieure de $K$ en $x \in \partial K \cap V$ 
est le vecteur de $\mathbb{R}^n$ donné par
$$
n(x_1, \dots, x_n) = \frac{(-\partial_1 f(x_1,\dots, x_{n-1}), \dots, -\partial_{n-1} f(x_1,\dots, x_{n-1}),1)}{\sqrt{1 +\|\nabla f(x_1, \dots, x_{n-1})\|^2}}.
$$

<!--
### Remarque {.remark .note}
Il suffit de retenir que la normale extérieure
est colinéaire et de même sens que le vecteur
$$
(-\partial_1 f, \dots, -\partial_{n-1} f, 1),
$$
puis de retrouver la formule de la normale extérieure en utilisant le fait que
sa norme vaut 1.
-->

### Démonstration {.proof}
Il suffit de constater qu'on peut associer à l'hypographe de $f$ la
description implicite $g(x) \leq 0$ avec
$$
g(x_1,\dots, x_{n-1}, x_n) = x_n - f(x_1, \dots, x_{n-1})
$$
puis d'exploiter [la caractérisation de la normale dans ce cas](#neci).
Comme
$$
\nabla g(x_1, \dots, x_n)
= (-\partial_1 f(x_1,\dots, x_{n-1}), \dots, -\partial_{n-1} f(x_1,\dots, x_{n-1}),1)
$$
et que par conséquent
$$
\|\nabla g(x_1, \dots,  x_n)\| = \sqrt{1 +\|\nabla f(x_1, \dots, x_{n-1})\|^2},
$$
le résultat s'en déduit.


<!--
### TODO

Evoquer indépendance du choix dans la définition


### TODO

Rendre explicite la normale extérieure dans ce cas et 
un peu plus explicitement (sur un exemple ?) comment trouver
un axe (orthonormé ?) qui permet de se ramener au cadre de 
l'hypographe. Sur $x^2 + y^2 - 1 \leq 0$ par exemple.

-->

### {.ante}
Nous allons maintenant définir l'intégrale de surface d'une fonction continue
sur la frontière d'un compact à bord. Pour arriver à nos fins, nous allons
tout d'abord définir l'intégrale de surface pour des fonctions continues
nulles en dehors d'un voisinage -- arbitrairement petit -- d'un point du 
compact.
Le résultat suivant de partition de l'unité nous permettra de 
"recoller" ces contributions à l'intégrale globale.

### Partition de l'unité {.definition .proposition #pu}
Pour toute famille finie d'ouverts $V_i$ de $\R^n$ recouvrant un ensemble
compact $K$, il existe une famille $\rho_i: \R^n \to \left[0, +\infty\right[$ 
de fonctions continûment différentiables dont le *support*
$$
\mbox{supp}(\rho_i) 
=
\overline{\{x \in \mbox{dom}(\rho_i)\, | \, \rho_i(x) \neq 0\}}.
$$ 
est compact et inclus dans $V_i$ et telles que
$$
\sum_{i} \rho_i(x) = 1 \mbox{ pour tout } x \in K.
$$

### {.post}
La démonstration est donnée [en annexe](#proof-pu).

<!--
### TODO
Préciser hypothèse sur $f$ (ouch, $C^1(\overline{U})$ va être nécessaire).
OK, pas besoin dans l'usage qu'on a, si l'on accepte que la contribution
de $V$ peut être indéfinie (ce qui n'arrive pas dès qu'on pondère par les
fcts à support compact.)

-->

### Intégrale de surface {.definition}
Soit $\phi: \partial K \to \mathbb{R}^m$ une fonction continue.
Si $K$ est caractérisé dans un voisinage ouvert $V$ de $x_0 \in \partial K$
comme l'hypographe de la fonction $f: U \to I$ après une
transformation $T$ qui soit une isométrie directe, 
la *contribution de $V = T(U \times I)$ à l'intégrale de surface
de $\phi$* est définie par la relation
$$
\int_{\partial K \cap V} \phi(x) \sigma(dx) 
:= 
\int_{U}
\phi(z, f(z)) \sqrt{1 + \|\nabla f(z)\|^2}\, dz. 
$$
Si les $V_i$ sont de tels ouverts consituant un recouvrement fini de $\partial K$
et les $\rho_i$ [une partition de l'unité associée](#lrl),
alors *l'intégrale de surface de $\phi$ sur $\partial K$* 
est définie par
$$
\int_{\partial K} \phi(x) \sigma(dx) 
:= \sum_i \int_{\partial K \cap V_i} \rho_i(x) \phi(x) \sigma(dx) 
$$

### {.post}
On admettra que cette définition est indépendante du choix de la 
décomposition de $\partial K$.


### Définition {.definition}
Soit $V$ un ouvert de $\R^n$. 
On appelle *divergence* d'une fonction différentiable 
$$
v: V \to \mathbb{R}^n,
\;
v=(v_1, \dots, v_n)
$$
la fonction $\mbox{div} \, v: V \to \mathbb{R}$ définie par
$$
\mbox{div} \, v(x) = \sum_{i=1}^n \partial_i v_i(x)
$$


### Lemme de la divergence {.lemma #div-lemma}
Soit $f: U \to \mathbb{R}$ une fonction de classe $C^1$
où $U$ est un pavé ouvert borné de $\mathbb{R}^{n-1}$. 
Soit $v: U \times \mathbb{R} \to \mathbb{R}^n$ une fonction
de classe $C^1$ de support compact dans $U \times \R^{n-1}$([^sc]). 
L'ensemble $\Omega$ désignant l'hypographe strict de $f$
-- soit $\Omega = \{(y, z) \, | \, y \in U, \, z \in \R, \, z < f(y)\}$ --
et $\Gamma$ le graphe de $f$
-- soit $\Gamma = \{(y, f(y)) \, | \, y \in U\}$ --
et $n$ la normale extérieure associée,
on a la relation
$$
\int_{\Omega} \mbox{div} \, v(x) \, dx
=
\int_{\Gamma} \left<v(x), n(x) \right> \, \sigma(dx).
$$

[^sc]: La fonction $v$ étant continue et définie dans un ouvert 
($U \times \R^{n-1}$), 
son support est compact dans cet ensemble
si et seulement si l'ensemble $\{x \, | \, v(x) \neq 0\}$ 
est borné et sa distance au complémentaire de $U\times \mathbb{R}$ 
dans $\mathbb{R}^n$ est strictement positive.

### Démonstration {.proof}
On remarque que si $v = w e_i$ où $w: U \times \mathbb{R} \to \mathbb{R}$ est
de classe $C^1$ et $i \in \{1,\dots, n\}$, 
comme $\mbox{div}\, v = \partial_i w$ et 
$\left<v(x), n(x) \right> = w(x) n_i(x)$, 
le résultat du lemme devient
$$
\int_{\Omega} \partial_i w(x) \, dx
=
\int_{\Gamma} w(x) n_i(x) \, \sigma(dx).
$$
Réciproquement, que si cette relation est valable pour tout 
$i \in \{1,\dots, n\}$, la conclusion du lemme de Stokes s'en déduit
facilement. Démontrer la relation ci-dessus suffit donc à prouver le lemme.

La transformation $h: U \times \left]-\infty, 0\right[ 
\to \mathbb{R}^n$ définie par
$$
h(x_1, \dots, x_{n-1}, x_n) = (x_1, \dots, x_{n-1}, x_n + f(x_1, \dots, x_{n-1}))
$$
est une application de classe $C^1$. Par construction,
$$
h(U \times \left]-\infty, 0\right[) = \Omega
$$
et admet une inverse, donnée par 
$$
h^{-1}(x_1, \dots, x_{n-1}, x_n) = (x_1, \dots, x_{n-1}, x_n - f(x_1, \dots, x_{n-1}))
$$
qui est également de classe $C^1$. La matrice jacobienne associée à $h$ vaut
$$
J_h(x)
=
\left[
\begin{array}{c|c}
I & 0 \\
\hline
J_f(x) & 1
\end{array}
\right]
$$
et par conséquent son déterminant jacobien satisfait
$$
\mbox{det} \, J_h(x) = 1.
$$
Par conséquent, le changement de variable associé à $h$ fournit
$$
\begin{split}
\int_{\Omega} \partial_i w(x) \, dx
&= \int_{h(U \times \left]-\infty, 0\right[)} \partial_i w(x) \, dx \\
&= \int_{U \times \left]-\infty, 0\right[} \partial_i w(h(x)) |\det J_h(x)| \, dx \\
&= \int_{U \times \left]-\infty, 0\right[} \partial_i w(x_1, \dots, x_{n-1}, x_n + f(x_1, \dots, x_{n-1})) 
\, dx
\end{split}
$$
ou encore, en notant $\pi(x) = (x_1,\dots, x_{n-1})$,
$$
\int_{\Omega} \partial_i w(x) \, dx
=
\int_{U \times \left]-\infty, 0\right[} 
\partial_i w(\pi(x), x_n + f(\pi(x))) 
\, dx.
$$
Nous allons évaluer cette expression en comparant l'intégrande dans le
membre de droite de cette équation avec la dérivée partielle 
de $w(\pi(x), x_n + f(\pi(x)))$ par rapport à $x_i$.


Si $i \in \{1,\dots, n-1\}$, la règle de dérivation en chaîne fournit
$$
\begin{split}
\partial_i \left( w(\pi(x), x_n + f(\pi(x)) \right)
&= 
\partial_i w(\pi(x), x_n + f(\pi(x)) \\
&\phantom{=}
+ \partial_n w(\pi(x), x_n + f(\pi(x)) \times 
\partial_i f (\pi(x))
\end{split}
$$
et dans le cas contraire,
$$
\partial_n \left( w(\pi(x), x_n + f(\pi(x)) \right)
= 
\partial_n w(\pi(x), x_n + f(\pi(x))).
$$

Si $U = I_1 \times \dots \times I_{n-1}$ et si pour $i \in \{1,\dots, n-1\}$, 
on a $I_i = \left]a_i, b_i\right[$, alors par le théorème fondamental du 
calcul,
$$
\begin{split}
\int_{I_i} 
\partial_i (w(\pi(x), x_n + f(\pi(x))) 
\, dx_i
&=
\lim_{\varepsilon \to 0}
\int_{a_i+\varepsilon}^{b_i-\varepsilon}
\partial_i (w(\pi(x), x_n + f(\pi(x))) 
\, dx_i \\
&=
\lim_{\varepsilon \to 0}
\left[
w(\pi(x), x_n + f(\pi(x)))
\right]_{a_i + \varepsilon}^{b_i - \varepsilon}
\end{split}
$$
Comme $w$ est de support compact, pour toute valeur de 
$x_1$, $x_2$, $\dots$, $x_{i-1}$, $x_{i+1}$, $\dots$, $x_n$, 
la fonction partielle
$$
x_i \in \left]a_i, b_i \right[ \to w(\pi(x), x_n + f(\pi(x)))
$$
est également de support compact.
Par conséquent,
$$
S_i(x_1, \dots, x_{i-1}, x_{i+1}, \dots) :=
\int_{I_i} 
\partial_i (w(\pi(x), x_n + f(\pi(x)))) 
\, dx_i
=
0.
$$
Par le théorème de Fubini, on peut alors déduire que
\begin{multline*}
\int_{U \times \left]-\infty, 0\right[} 
\partial_i (w(\pi(x), x_n + f(\pi(x)))) 
\, dx
=  \\
\int_{I_1\times\dots I_{i-1} \times I_{i+1} \times \dots \times \left]-\infty, 0\right[}
\!\!\!\!\!
S_i(x_1, \dots, x_{i-1}, x_{i+1}, \dots)  \, d(x_1,\dots,x_{i-1}, x_{i+1},\dots)
= 0.
\end{multline*}
Si $i \in \{1,\dots, n-1\}$, on a donc
$$
\int_{\Omega} 
\partial_i w(x) 
\, dx
= 
\int_{U \times \left]-\infty, 0\right[} 
\partial_n w(\pi(x), x_n + f(\pi(x)) \times 
(- \partial_i f (\pi(x))) \, dx
$$
et pour $i=n$,
$$
\int_{\Omega} 
\partial_n w(x) 
\, dx
= 
\int_{U \times \left]-\infty, 0\right[} 
\partial_n w(\pi(x), x_n + f(\pi(x)) \, dx.
$$
Dans ce second cas, en raison de la compacité du support $w$, 
le théorème fondamental du calcul fournit
$$
\begin{split}
\int_{-\infty}^0 
\partial_n w(\pi(x), x_n + f(\pi(x)) \, dx_n
&= 
\lim_{z \to -\infty}\left[
x_n \mapsto 
w(\pi(x), x_n + f(\pi(x)))
\right]^0_{z} \\
&= 
w(\pi(x), f(\pi(x)),
\end{split}
$$
et donc par le théorème de Fubini,
$$
\int_{\Omega} 
\partial_n w(x) 
\, dx
= 
\int_U w(y, f(y)) \, dy.
$$
Quand $i \in \{1, \dots, n-1\}$, un calcul analogue fournit
$$
\int_{\Omega} 
\partial_n w(x) 
\, dx
= 
\int_U w(y, f(y)) \times (- \partial_i f(y)) \, dy.
$$

Quel que soit la valeur de $i \in \{1, \dots, n\}$, comme la normale
extérieure $n$ est donnée par
$$
n(y, f(y)) = \frac{(-\partial_1 f(y), \dots, -\partial_{n-1} f(y), 1)}{\sqrt{1 +\|\nabla f(y)\|^2}}, 
$$
on constate que l'on a
$$
\int_{\Omega} 
\partial_i w(x) 
\, dx
= 
\int_U w(y, f(y)) n_i(y, f(y)) \sqrt{1 +\|\nabla f(y)\|^2} \, dy,
$$
et par conséquent
$$
\int_{\Omega} 
\partial_i w(x) 
\, dx
= 
\int_{\Gamma} w(x) n_i(x)\, d\sigma(x).
$$

### Théorème de la divergence {.theorem #div-theorem}
Soit $U$ un ouvert de $\R^n$ et $K$ un ensemble compact 
$K$ à bord $C^1$ inclus dans $U$. 
Pour toute fonction $v: U \to \mathbb{R}^n$ continûment différentiable,
$$
\int_{K} \mbox{div} \, v(x) \, dx
=
\int_{\partial K} \left<v(x), n(x) \right> \, \sigma(dx).
$$
Pour toute fonction $f: U \to \mathbb{R}$ continûment différentiable
et tout $i \in \{1,\dots, n\}$,
$$
\int_{K} \partial_i f(x) \, dx
=
\int_{\partial K} n_i(x) f(x) \, \sigma(dx).
$$

### Démonstration {.proof}
Comme dans la démonstration du [lemme de la divergence](#div-lemma), 
il suffit d'établir une version du résultat, par exemple la première,
et la seconde version s'en déduit.

Pour tout $x \in \partial K$, il existe un pavé ouvert borné $U_x$ de $\R^{n-1}$,
un intervalle ouvert $I_x$ de $\R$, une isométrie affine directe $T_x$ et une
fonction continûment différentiable $f_x:U_x \to I_x$ telle que 
$T_x(U_x \times I_x)$ soit un voisinage de $x$ et 
$K \cap T_x(U_x \times I_x)$ soit l'image de l'hypographe de $f_x$ par $T_x$.
Si $x \in \mathring{K}$, il existe un pavé ouvert borné $U_x$ de $\R^{n-1}$ et
un intervalle ouvert $I_x$ de $\R$ tels que $U_x \times I_x \subset \mathring{K}$ ;
on prendra ici $T_x=I$ (l'identité) et pour $f_x: U_x \to \R$ une fonction constante dont
la valeur soit un majorant de $I_x$.

Par compacité, $K$ peut être recouvert par un nombre fini des
ensembles $V_x := T_x(U_x \times I_x)$, associés au points $x_1, \dots, x_k$.
Soit $\rho_j$, $j \in \{1,\dots, k\}$ une [partition de l'unité](#pu) associée.
On a alors
$$
\begin{split}
\int_{K} \mathrm{div}\, v(x) \, dx
&= \int_{K} \mathrm{div}\, \left({\textstyle \sum}_{j=1}^k  \rho_j(x) v(x) \right) \, dx \\
&= \sum_{j=1}^k \int_{K \cap V_{x_j}} \mathrm{div}\, (\rho_j(x) v(x)) \, dx.
\end{split}
$$
L'application du [lemme de la divergence](#div-lemma) quand $x_j$ est un point
intérieur à $K$ fournit
$$
\int_{K \cap V_{x_j}} \mathrm{div}\, (\rho_j(x) v(x)) \, dx = 0,
$$
car $v$ est nulle sur le graphe de $f_{x_j}$,
et quand $x_j$ est un point frontière
$$
\begin{split}
\int_{K \cap V_{x_j}} \mathrm{div}\, (\rho_j(x) v(x)) \, dx &= 
\int_{\partial K \cap V_{x_j}}  \left<\rho_j(x) v(x), n(x)\right> \, d\sigma(x) \\
&=\int_{\partial K \cap V_{x_j}}  \rho_j(x) \left< v(x), n(x)\right> \, d\sigma(x).
\end{split}
$$
Par conséquent,
$$
\begin{split}
\int_{K} \mathrm{div}\, v(x) \, dx
&= \sum_{j=1}^{k} \int_{\partial K \cap V_{x_j}}  \rho_j(x) \left< v(x), n(x)\right> \, d\sigma(x) \\
&= \int_{\partial K} \left< v(x), n(x)\right> \, d\sigma(x).
\end{split}
$$

<!--
### TODO
Perspective sur les versions plus "relaxées" du théorème de Stokes,
qu'il s'agisse du bord Lipschitz ou des travaux (Mawhin, Pfeffer, etc.)
pour demander moins que $C^1$ sur l'intégrande ?
-->

Annexes
================================================================================

Partition de l'unité {#proof-pu}
--------------------------------------------------------------------------------

La preuve de l'existence d'une partition de l'unité repose sur le lemme suivant :

### Lemme de recouvrement de Lebesgue {.lemma #lrl}
Soit $K$ un compact de $\R^n$ et une famille arbitraire d'ouverts $V_i$ recouvrant
$K$. Alors il existe un rayon $r>0$ tel que pour tout $x \in K$, il existe un
indice $i$ telle que la boule ouverte $B(x, r)$ de rayon $r$ centrée en $x$
soit incluse dans $V_i$.

### Démonstration {.proof}
Supposons au contraire que pour tout $r>0$ il existe un $x \in K$ tel que 
pour tout indice $i$, la distance entre $x$ et le complémentaire de $V_i$
soit (strictement) inférieure à $r$.
Soit $x_k$ une suite de points de $K$ tels que pour tout $i$,
$d(x_k, \R^n \setminus V_i) \leq 2^{-k}$ ; par compacité de $K$,
il existe une suite extraite des $x_k$ qui converge vers un $\ell \in K$.
En passant à la limite sur cette suite, on établit que pour tout 
indice $i$ on a $d(\ell, \R^n \setminus V_i) = 0$, 
soit $x \in \R^n \setminus V_i$ puisque $\R^n \setminus V_i$ est fermé.
Par conséquent, pour tout $i$, $x \not \in V_i$, ce qui contredit l'hypothèse
que les $V_i$ forment un recouvrement de $K$.

### Démonstration de l'existence d'une partition de l'unité {.proof}

Nous allons initialement établir l'existence
d'une suite de fonctions $\rho_i:\R^n \to \R$ 
continues, nulles en dehors de $V_i$ dont la somme vaut $1$ sur un voisinage
ouvert $V$ de $K$, 
puis déduire de cette construction l'existence de fonctions
continûment différentiables $\rho'_i$ satisfaisant satisfaisant le théorème.

Notons $V=\cup_i V_i$ ; l'ensemble $V_i$ étant ouvert, la fonction 
$x \in V \mapsto d(x, \R^n \setminus V_i)$, qui est continue, 
est strictement positive sur $V_i$ et nulle ailleurs. 
La somme $x \in \R^n \mapsto \sum_j d(x, \R^n \setminus V_j)$, également
continue, est donc strictement positive sur $V$.
Les fonctions $\rho_i$ définies par
$$
\rho_i(x) = \frac{d(x, \R^n \setminus V_i)}{\sum_j d(x, \R^n \setminus V_j)}
$$
satisfont donc les propriétés requises pour l'étape 1.

[Le lemme de recouvrement de Lebesgue](#lrl) établit l'existence d'un $r>0$ 
tel que pour tout $x \in K$, il existe au moins un indice $i$ tel que
$B(x, r) \subset V_i$. Notons $V'_i$ l'union des boules ouverts $B(x,r)$
pour lequel l'incide $i$ convient quand $x$ décrit $K$. Par construction,
les $V'_i$ sont ouverts et recouvrent $K$ ; de plus, les adhérences
$\overline{V'_i}$ sont bornées
(ce sont des sous-ensembles de $\{x \in K \, | \, d(x, K) \leq r\}$)
et vérifient $d(\overline{V'}_i, \R^n \setminus V_i) \geq r$.

Considérons les fonctions $\rho_i$ de l'étape initiale 
associées à la famille des $V'_i$ et prolongées par
$0$ en dehors de $\bigcup_i V'_i$. Définissons alors
les fonctions $\rho'_i:\R^n \to \left[0, +\infty \right[$ par
$$
\rho'_i(x) = \int_{\R^n} \rho_i(y) \phi(x-y) \, dy
$$
où $\phi:\R^n \to \left[0, +\infty\right[$ est une fonction continûment 
différentiable, de support inclus dans $\overline{B}(0, r/2)$ et 
telle que 
$$
\int_{\R^n} \phi(x) \, dx = 1.
$$
Le théorème de dérivation sous le signe somme établit que les
$\rho'_i$ sont continûment différentiables. Par construction,
le support de $\rho'_i$ est inclus dans $V'_i + \overline{B}(x, r/2)$,
ce qui garantit que $\mathrm{supp}(\rho'_i) \subset V_i$. Finalement,
pour tout $x \in K$,
$$
\begin{split}
\sum_{i} \rho'_i(x) &= 
\sum_i \int_{\R^n} \rho_i(y) \phi(x-y) \, dy \\
&= 
\int_{\R^n} \sum_i \rho_i(y) \phi(x-y) \, dy \\
&= 
\int_{\R^n} \phi(x-y) \, dy \\ &= 1. \\
\end{split}
$$

Exercices
================================================================================

Changement de variables linéaire
--------------------------------------------------------------------------------

### Question 1 {.question #cvl-1}
Soit $f:\R \to \R$ une fonction intégrable. Montrer que pour tout
réel $\lambda$ non nul, $x \in \R \mapsto f(\lambda x)$ est intégrable
et calculer
$$
\int_{-\infty}^{+\infty} f(\lambda x) \, dx.
$$
Même question pour 
$$
\int_{-\infty}^{+\infty} f(x + h) \, dx
$$
où $h \in \R$.

### Question 2 {.question #cvl-2}
Soit $f:\R^n \to \R$ une fonction absolument intégrable.
Soient $i, j \in \{1,\dots, n\}$, $i\neq j$ et $\lambda$ un réel non nul.
Montrer que les intégrales suivantes existent et les calculer en fonction
de l'intégrale de $f$ :
$$
S_1 = \int_{\R^n} f(x_1, \dots, x_{i-1}, \lambda x_i, x_{i+1}, \dots, x_n) \, dx,
$$
$$
S_2 = \int_{\R^n} f(x_1, \dots, x_i, x_i + \lambda x_j, x_{i+2},\dots, x_j, \dots, x_n) \, dx,
$$
$$
S_3 = \int_{\R^n} f(x_1, \dots, x_i, x_j, x_{i+2},\dots, x_{j-1}, x_i, x_{j+1} \dots, x_n) \, dx.
$$

### Question 3 {.question #cvl-3}
Soit $A: \R^n \to \R^n$ une application linéaire inversible. 
Montrer que la fonction $x \in \R^n \mapsto  f(A \cdot x) |\det [A]|$ 
est intégrable et que
$$
\int_{\R^n} f(y) \, dy = \int_{\R^n} f(A \cdot x) |\det [A]| \, dx.
$$

Déformations d'un compact à bord régulier {.question #dcbr}
--------------------------------------------------------------------------------

Soit $K$ un compact à bord $C^1$ de $\R^n$ et $T:\R^n \to \R^n$ une application
continûment différentiable telle que $T = I + H$, où l'application
continûment différentiable $H:\R^n \to \R^n$ satisfait $\sup_{x \in \R^n} \|dH(x)\| < 1$.

Montrer que l'ensemble
$$
T(K) = \{x + T(x) \, | \, x \in K\}
$$
est un compact à bord $C^1$ de $\R^n$.

Ovales de Cassini {.question #oc}
--------------------------------------------------------------------------------

Soit $a$ et $b$ deux nombres réels strictements positifs. 
On désigne par $K$ l'ensemble du plan délimité par les *ovales de Cassini*
$$
K = \{(x,y) \in \R^2 \, | \, (x^2+y^2)^2 - 2a^2 (x^2 - y^2) + a^4 \leq b^4\}.
$$

Montrer que si $a \neq b$, l'ensemble $K$ est un compact à bord $C^1$.

![Compact à bord $C^1$ délimité par les ovales de Cassini.](images/cassini-ovals.py)


![Ensemble délimité par les ovales de Cassini quand $a=b=1$.](images/cassini-ovals-limite.py)



Aire du disque unité {.question #adu}
--------------------------------------------------------------------------------
Soit $B = \overline{B}(0,1)$ le disque unité fermé de $\R^2$.
Calculer l'aire de $B$
$$
A := \int_B \, dx
$$


Intégrales de surface {.question #is}
--------------------------------------------------------------------------------

Soit $B = \overline{B}(0,1)$ le disque unité fermé de $\R^2$.
Calculer
$$
\int_{\partial B} \sigma(dx)
\; \mbox{ et } \;
\int_{\partial B} x_1^2 \, \sigma(dx).
$$

Rétraction
--------------------------------------------------------------------------------

Soit $B = \overline{B}(0,1)$ le disque unité fermé de $\R^2$ et 
$f: B \to B$ une fonction de classe $C^2$
(c'est-à-dire admettant un prolongement de classe $C^2$ sur un ouvert $U$ 
contenant $B$). Une telle fonction $f$ est une *rétraction* de $B$
sur $\partial B$ si $f(B) = \partial B$ et pour tout $x\in \partial B$,
$f(x) = x$.

<!--
### Question 1 {.question #pfb-1}
Montrer que si $f$ n'admet pas de point fixe, il existe une 
*rétraction* de $D$ dans $\partial D$ de classe $C^2$, 
c'est-à-dire une fonction 
$g: D \to \partial D$ telle que $g(x) = x$ si $x \in \partial D$.
-->

### Question 1  {.question #pfb-1}
Montrer que pour une telle rétraction $f$, on a 
$$
\int_B \det J_f(x) \, dx = 0.
$$

### Question 2  {.question #pfb-2}
En déduire l'impossibilité d'une telle rétraction.
 
Intégration par parties {.question #IPP-n}
--------------------------------------------------------------------------------

Si l'équivalent dans $\R^n$ du théorème fondamental du calcul 
est le théorème de la divergence, quel résultat est l'équivalent
dans $\R^n$ de l'intégration par parties ?

Solutions
================================================================================

Changement de variables linéaire
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-cvl-1}
Supposons tout d'abord que $\lambda > 0$ ;
si la fonction $f$ est intégrable, pour tout $\varepsilon > 0$ il existe
une jauge $\gamma$ sur $[-\infty, +\infty]$ telle que pour toute 
subdvision pointée $\mathcal{D}$ de $[-\infty, +\infty]$ subordonnée 
à $\gamma$ on ait
$$
\left|S(f,\mathcal{D}) - \int_{-\infty}^{+\infty} f(x) \,dx \right| \leq \varepsilon.
$$
Soit $\mathcal{C}$ une subdivision pointée de $[-\infty, +\infty]$ ;
la somme de Riemann associée à $\mathcal{C}$ et la fonction 
$x \mapsto f(\lambda x)$ s'écrit
$$
S(x \mapsto f(\lambda x), \mathcal{C}) 
= 
\sum f(\lambda t) \ell(J), \; (t, J) \in \mathcal{C}, \, \ell(J) < +\infty.
$$
L'ensemble 
$$
\mathcal{D} = \{(\lambda t, \lambda J) \, | \, (t, J) \in \mathcal{C}\}
$$
est une subdivision pointée de $[-\infty, +\infty]$, surbordonné à la jauge
$\gamma$ -- tel que $\gamma(\lambda t) \subset \lambda J$ -- 
si et seulement si $\mathcal{C}$ est subordonné à la jauge définie par
$\nu(t) = \gamma(\lambda t) / \lambda$. Comme $f(\lambda t) \ell(J)
= f(\lambda t)\ell(\lambda J) / \lambda$, on a
$$
S(x \mapsto f(\lambda x), \mathcal{C}) 
= 
\frac{1}{\lambda} S(f, \mathcal{D}).
$$
Si $\mathcal{C}$ est subordonnée $\nu$, on a donc
$$
\left|S(x \mapsto f(\lambda x),\mathcal{C}) - \frac{1}{\lambda}\int_{-\infty}^{+\infty} f(x) \,dx \right| \leq \frac{\varepsilon}{\lambda}.
$$
La fonction $x \mapsto f(\lambda x)$ est donc intégrable, d'intégrale
$$
\int_{-\infty}^{+\infty} f(\lambda x) \,dx = \frac{1}{\lambda}\int_{-\infty}^{+\infty} f(x) \,dx.
$$
On montrerait de manière similaire que si $\lambda < 0$, on a 
$$
\int_{-\infty}^{+\infty} f(\lambda x) \,dx = -\frac{1}{\lambda}\int_{-\infty}^{+\infty} f(x) \,dx
$$
et la validité de
$$
\int_{-\infty}^{+\infty} f(x + h) \, dx = \int_{-\infty}^{+\infty} f(x) \, dx.
$$

### Question 2 {.answer #answer-cvl-2}
Par le changement de variable linéaire dans $\R$ de la question 1
et le théorèmes de [Fubini](#Fubini) et [Tonelli](#Tonelli),
$$
\begin{split}
& \phantom{ =. }  \frac{1}{|\lambda|} \int_{\R^n} f(x) \, dx  \\
&= \frac{1}{|\lambda|}
\int_{\R^{n-1}} \left[\int_{\R} f(x_1, \dots, x_{i-1}, x_i, x_{i+1}, \dots, x_n) \, dx_i\right] \, 
dx_1 \dots dx_{i-1}dx_{i+1}\dots dx_n \\
&= 
\int_{\R^{n-1}} \left[\int_{\R} f(x_1, \dots, x_{i-1}, \lambda x_i, x_{i+1}, \dots, x_n) \, dx_i\right] \, 
dx_1 \dots dx_{i-1}dx_{i+1}\dots dx_n \\
& = S_1
\end{split}
$$
De même,
$$
\begin{split}
& \phantom{ =. }  \int_{\R^n} f(x) \, dx  \\
&= 
\int_{\R^{n-1}} \left[\int_{\R} f(x_1, \dots, x_{i-1}, x_i, x_{i+1}, \dots, x_n) \, dx_i\right] \, 
dx_1 \dots dx_{i-1}dx_{i+1}\dots dx_n \\
&= 
\int_{\R^{n-1}} \left[\int_{\R} f(x_1, \dots, x_{i-1}, x_i + \lambda x_j, x_{i+1}, \dots, x_n) \, dx_i\right] \, 
dx_1 \dots dx_{i-1}dx_{i+1}\dots dx_n \\
& = \int_{\R^n} f(x_1, \dots, x_i, x_i + \lambda x_j, x_{i+2},\dots, x_j, \dots, x_n) \, dx \\
& = S_2.
\end{split}
$$
Quant à l'identité
$$
\begin{split}
S_3 &= \int_{\R^n} f(x_1, \dots, x_i, x_j, x_{i+2},\dots, x_{j-1}, x_i, x_{j+1} \dots, x_n) \, dx \\
&= \int_{\R^n} f(x) \, dx,
\end{split}
$$
elle résulte directement du [théorème de Fubini](#Fubini).

### Question 3 {.answer #answer-cvl-3}
Nous avons établi dans la question précédente que pour les 3 types
d'opérations linéaires
$$
A \cdot (x_1, \dots, x_n) = (x_1, \dots, \lambda x_i , \dots, x_n),
$$
$$
A \cdot (x_1, \dots, x_n) = (x_1, \dots, x_{i-1}, x_i + \lambda x_j, x_{i+1}, \dots, x_n)
$$
et
$$
A \cdot (x_1, \dots, x_n) = (x_1, \dots, x_{i-1}, x_{j},x_{i+1}, \dots, x_{j-1}, x_{i},x_{j+1}, \dots, x_n)
$$
nous avions
$$
\int f(A \cdot x) |\det [A]| \, dx 
= \int f(x)  dx.
$$
Mais toute application linéaire inversible $A$ peut être décomposée
-- par le pivot de Gauss -- en la succession d'un nombre fini
de ces opérations. Or si $A = A_1 \cdots A_k$,
comme $|\det [A]| = |\det [A_k] \cdots \det [A_k]|$, on peut
établir par récurrence que
$$
\int f(A \cdot x) |\det [A]| \, dx 
= \int f(A_1 \cdots A_k \cdot x) |\det [A_1] \cdots \det [A_k]| \, dx 
= \int f(x)  dx.
$$



Déformations d'un compact à bord régulier {.answer #answer-dcbr}
--------------------------------------------------------------------------------

Sous les hypothèses de l'énoncé, nous avons établi en exercice de 
"Calcul Différentiel II" que la fonction $T$ est un $C^1$-difféomorphisme
global de $\R^n$ dans l'ouvert $T(\R^n)$.

L'ensemble $T(K)$ est un ensemble compact comme image d'un ensemble compact
par une application continue. Comme $T$ est un difféomorphisme, 
un point $y$ de $\R^n$ est intérieur à $T(K)$ si et seulement si 
$x = T^{-1}(y)$ est intérieur à $K$. Les points de la frontière
$\partial T(K)$ sont donc les images des points de $\partial K$ par
$T$.

Soit $y_0 \in \partial T(K)$ et $x_0 = T^{-1}(y_0) \in \partial K$. 
Dans un voisinage $V$ de $x_0$, il existe une fonction continûment 
différentiable $g:V \to \R$
de différentielle non nulle en $x_0$ telle que $g(x) \leq 0$ équivaut 
à $x \in K$. Par conséquent, $y \in T(V)$ appartient à $T(K)$
si et seulement si $g \circ T^{-1}(y) \leq 0$.
La fonction $g \circ T^{-1}$ est continûment différentiable et
$$
d (g \circ T^{-1})(y_0) = dg (T^{-1}(y_0)) \cdot dT^{-1}(y_0)
= dg(x_0) \cdot (dT(x_0))^{-1}.
$$
Soit $u \in \R^n$ tel que $dg(x_0) \cdot u \neq 0$ ; si 
$v = (dT(x_0)) \cdot u$, $d(g \circ T^{-1})(y_0) \cdot v \neq 0$.
La différentielle de $g \circ T^{-1}$ est donc non nulle en $y_0$.
Par la [caractérisation implicite des compacts à bord $C^1$](#cbr-implicit), 
$T(K)$ est donc un compact à bord $C^1$ de $\R^n$.

Ovales de Cassini {.answer #answer-oc}
--------------------------------------------------------------------------------

Montrons tout d'abord que l'ensemble $K$ est compact. Si les points
$(x_k, y_k)$ de $\R^2$ appartiennent à $K$, ils vérifient 
$(x_k^2+y_k^2)^2 - 2a^2 (x_k^2 - y_k^2) + a^4 \leq b^4$ ; 
si la suite converge vers $(x, y)$, par continuité
$(x^2+y^2)^2 - 2a^2 (x^2 - y^2) + a^4 \leq b^4$ et donc $(x, y) \in K$.
L'ensemble $K$ est donc fermé. De plus pour tout $(x, y) \in K$, 
comme
$$
\|(x, y)\|^4 = (x^2 + y^2)^2 \, \mbox{ et } \, x^2- y^2 \leq \|(x, y)\|^2, 
$$
on a
$\|(x, y)\|^4 \leq b^4 - a^4 + 2a^2 \|(x, y)\|^2,$
donc si 
$$
\frac{\|(x, y)\|^4}{2} \geq b^4 
\, \mbox{ et } \,
\frac{\|(x, y)\|^2}{2} \geq 2a^2,
$$
le point $(x, y)$ n'appartient pas à $K$ ; l'ensemble $K$ est donc borné.
Fermé et borné dans $\R^2$, l'ensemble $K$ est donc compact.

Pour montrer que l'on a affaire à un ensemble compact à bord $C^1$, nous
souhaitons utiliser le résultat sur [la caractérisation implicite de ces
ensembles](#cbr-implicit). La fonction $g$ de ce théorème prend bien
sûr ici la forme
$$
g(x, y) := (x^2+y^2)^2 - 2a^2 (x^2 - y^2) + a^4 - b^4
$$
puisque $x \in K$ si et seulement si $g(x, y) \neq 0$. Il nous suffit donc
de vérifier que $g$ est $C^1$, ce qui est évident, et qu'en tout point de
la frontière de $K$, la différentielle de $g$ -- ou son gradient -- est 
non-nulle. On se convaincra que tout point $(x, y)$ de la frontière de 
$K$ vérifie nécessairement $g(x, y)$ en exploitant la continuité de $g$.
Par conséquent, notre démonstration sera achevée si nous montrons qu'aucun
point $(x, y)$ de $\R^2$ ne satisfait simultanément
$$
g(x, y) = 0, \, \partial_x g(x, y) = 0 \, \mbox{ et } \, \partial_y g(x, y) = 0.
$$
Or $\partial_x g(x, y) = 4(x^2+y^2)x - 4a^2x$ et 
$\partial_x g(x, y) = 4(x^2+y^2)y + 4a^2 y$ ; de la nullité de ces deux dérivées
partielles, on déduit 
$$
(x^2+y^2)x = a^2 x \, \mbox{ et } \, (x^2 + y^2) y = -a^2 y.
$$
Il nous faut désormais envisager les cas possibles selon que 
$x$ et $y$ sont nuls ou non:

  - $x \neq 0$ et $y \neq 0$ est impossible car les deux équations ci-dessus
    entraînent alors $(x^2+y^2) = a^2 = -a^2$ or $a > 0$.

  - $x = y = 0$ est impossible car $g(0, 0) = a^4 - b^4 \neq 0$, car
    $a>0$, $b>0$ et $a\neq b$.

  - $x = 0$ et $y \neq 0$ entraîne $x^2 + y^2 = y^2 = -a^2$, impossible
    car $a>0$.

  - finalement, si $x\neq 0$ et $y = 0$, $x^2 + y^2 = x^2 = a^2$, ce qui
    réinjecté dans $g(x, 0)= 0$ fournit 
    $a^4 -2 a^4 + a^4 - b^4 = 0,$
    soit $b^4=0$, également impossible car $b>0$.

Aucun point $(x, y)$ de $\R^2$ n'annule simulanément $g$ et son gradient ;
l'ensemble $K$ est donc bien un compact à bord $C^1$.


Aire du disque unité {.answer #answer-adu}
--------------------------------------------------------------------------------

La fonction $f: x \in \R^2 \mapsto 1_B(x)$ est intégrable: l'ensemble $B$ est
fermé, donc mesurable, et la fonction $f$ est par exemple dominée par la
fonction caractéristique du pavé fermé $[-1,1]^2$, qui est intégrable.

Le théorème de Fubini nous fournit donc
$$
\int_B dx = \int_{-1}^1 \left[\int_{-\sqrt{1-x^2}}^{\sqrt{1-x^2}} dy\right] dx
= 2 \int_{-1}^1 \sqrt{1 - x^2} \, dx.
$$
Comme
$$
\int_{-1}^1 \sqrt{1 - x^2} \, dx
= \int_{[-1, 1]} \sqrt{1 - x^2} \, dx
= \int_{\left]-1, 1\right[} \sqrt{1 - x^2} \, dx
$$
On peut donc opérer le changement de variable 
$$
\theta \in \left]0, \pi\right[ \mapsto x = -\cos \theta \in \left]-1,1\right[
$$
(bijectif, continûment différentiable ainsi que son inverse).
Comme $(-\cos \theta)' = \sin \theta$, on a
$$
\int_{0}^{\pi} \sqrt{1-(-\cos^2 \theta)} \sin \theta  \, d\theta = \int_{-1}^1 \sqrt{1 - x^2} \, dx
$$
et donc
$$
\int_{-1}^1 \sqrt{1 - x^2} \, dx
=
\int_{0}^{\pi} \sin^2 \theta  \, d\theta
=
\int_{0}^{\pi} \frac{1 - \cos 2\theta}{2} \, d\theta
=
\left[\frac{\theta}{2} - \frac{\sin 2\theta}{4} \right]_0^{\pi}
=\frac{\pi}{2},
$$
et finalement
$$
\int_B \, dx = \pi.
$$

Alternativement, on peut noter que l'union $N$ de $\partial B$ et 
du segment $\{(x, 0) \, | \, x \in [-1, 0]\}$ est négligeable dans $\R^2$ 
et donc que
$$
\int_B \, dx = \int_{B \setminus N} dx,
$$
ce qui nous permet de considérer le changement de variable
$$
\phi: (r, \theta) \in \left]0, 1\right[ \times \left]-\pi ,\pi\right[
\mapsto (x, y) = (r \cos \theta, r \sin \theta) \in B \setminus N
$$
(bijectif, continûment différentiable ainsi que son inverse).
On calcule la matrice jacobienne
$$
J_{\phi}(r, \theta) = 
\left[ 
\begin{array}{cr}
\cos \theta & -r \sin \theta \\
\sin \theta & r \cos \theta
\end{array}
\right],
$$
dont le déterminant vaut
$$
\det J_{\phi}(r, \theta) = (\cos \theta)(r \cos \theta) - (\sin \theta)(-r\sin \theta)
= r.
$$
On a donc
$$
\int_{\left]0, 1\right[ \times \left]-\pi ,\pi\right[} r \, drd\theta
=
\int_B \, dx,
$$
et donc par le théorème de Fubini,
$$
\int_B \, dx
= \int_{-\pi}^{\pi} \left[\int_{0}^1 r \, dr \right] \, d\theta
= \int_{-\pi}^{\pi} \frac{1}{2} \, d\theta
= \pi.
$$

Intégrales de surface {.answer #answer-is}
--------------------------------------------------------------------------------

Comme la normale extérieure à $B$ en $\partial B$ vaut $n(x) = (x_1, x_2)$
et que $x_1^2 + x_2^2 = 1$ sur $\partial B$, on a en posant $v(x) = (x_1, x_2)$ 
sur $B$ l'égalité
$$
\int_{\partial B} \sigma(dx) = \int_{\partial B} (x_1^2 + x_2^2) \, \sigma(dx)
= 
\int_{\partial B} \left<v(x), n(x)\right> \sigma(dx)
$$
et donc par le théorème de la divergence
$$
\int_{\partial B} \sigma(dx)
= \int_{B} \mathrm{div} \, v(x) \, dx
= \int_{B} (\partial_1 x_1 + \partial_2 x_2) \, dx
= 2 \int_{B} \, dx.
$$
L'intégrale initiale est donc égale au double de l'aire du disque unité, 
soit $2\pi$.
Concernant la seconde intégrale, on à l'égalité
$$
\int_{\partial B} x_1^2 \sigma(dx) = \int_{\partial B} \left<v(x), n(x)\right> \sigma(dx)
\, \mbox{ avec } \, v(x) = (x_1, 0)
$$
et donc par le théorème de la divergence
$$
\int_{\partial B} x_1^2 \sigma(dx)
= \int_{B} \mathrm{div} \, v(x) \, dx
= \int_{B} (\partial_1 x_1 + \partial_2 0) \, dx
= \int_{B} \, dx.
$$
L'intégrale initiale est donc égale à l'aire du disque unité, soit $\pi$.

Rétraction
--------------------------------------------------------------------------------

<!--
### Question 1 {.answer #answer-pfb-1}
Comme par hypothèse pour tout $x\in B$, $f(x) \neq x$, on peut associer à
$x$ l'unique point de la demi-droite ouverte d'origine $f(x)$ et
de direction $x - f(x)$ appartenant à $\partial B$. 
Par construction, cette fonction est une rétraction.

Elle est également de classe $C^2$.
-->

Source: [@Kan81]

### Question 1  {.answer #answer-pfb-1}
On déduit de l'identité $\|f(x)\|^2=\left<f(x), f(x)\right> =1$ valable sur $B$
que pour tout $h \in \R^2$,
$$
\left<df(x) \cdot h, f(x) \right> + \left<f(x), df(x) \cdot h \right>=
2 \left<df(x)^* \cdot f(x), h \right> = 0
$$
et donc la relation $J_f(x)^t f(x) = 0$. La valeur $f(x)$ étant non nulle, cela
entraîne la non-inversibilité de la matrice jacobienne $J_f(x)$,
ou ce qui est équivalent, la nullité du déterminant jacobien
$\det J_f(x)$. En conséquence,
$$
\int_B \det J_f(x) \, dx = 0.
$$

### Question 2  {.answer #answer-pfb-2}
La fonction $f$ étant de classe $C^2$, on a
$$
\begin{split}
\det J_f 
&= (\partial_1 f_1) (\partial_2 f_2) - (\partial_1 f_2) (\partial_2 f_1) \\
&= \partial_1 (f_1 \partial_2 f_2) - f_1 \partial^2_{12} f_2
   -\partial_2 (f_1 \partial_1 f_2) + f_1 \partial^2_{21} f_2 \\
&= \partial_1 (f_1 \partial_2 f_2) 
   -\partial_2 (f_1 \partial_1 f_2)
\end{split}
$$
Par le théorème de la divergence, on a donc
$$
\begin{split}
\int_B \det J_f(x) \, dx &=
\int_{\partial B} (n_1 (f_1 \partial_2 f_2) 
   -n_2 (f_1 \partial_1 f_2)) \sigma \\
&=\int_{\partial B} f_1 \left<\nabla f_2, t\right> \sigma
\end{split}
$$
où $t(x)$ désigne le vecteur tangent à $\partial B$ en $x$ :
$$
t(x) = (-n_2(x), n_1(x)).
$$
Comme la normale extérieure à $B$ en $x=(x_1, x_2) \in \partial B$ est donnée
par $n(x) = (x_1, x_2)$, on a $t(x) = (-x_2, -x_1)$. Par ailleurs, comme
$f(x)$ vaut identiquement $x$ sur $\partial B$, $f_2(x)$ vaut $x_2$ et
par conséquent 
$$
\left<\nabla f_2(x), t(x)\right>  = \left<\nabla (x_2), t(x)\right>= x_1,
$$
soit, puisque $f_1(x) = x_1$ sur $\partial B$,
$$
\int_B \det J_f(x) \, dx = \int_{\partial B} x_1^2 \, \sigma(dx) > 0.
$$
Si une telle rétraction existait, on aurait donc une contradiction.

Intégration par parties {.answer #answer-IPP-n}
--------------------------------------------------------------------------------

On obtient le théorème d'intégration par parties en appliquant le théorème
fondamental du calcul à la dérivée du produit $fg$.

Supposons de façon analogue que $U$ est un ouvert de $\R^n$,
$K$ un ensemble compact à bord $C^1$ de $U$ et que $f, g: U \to \mathbb{R}$ 
sont deux fonctions de classe $C^1$. Le produit $fg$ est également de classe 
$C^1$ et pour tout $i \in \{1,\dots, n\}$, 
$$
\int_{K} \partial_i (fg) (x) \, dx
=
\int_{\partial K} n_i(x) f(x)g(x) \, \sigma(dx),
$$
soit
$$
\int_{K} (\partial_i f(x))g(x) \, dx
=
\int_{\partial K} n_i(x) f(x)g(x) \, \sigma(dx) 
- \int_{K} f(x)(\partial_i g(x)) \, dx.
$$
Alternativement, si
$f:U \to \R$ et $v: U \to \mathbb{R}^n$ sont deux
fonctions de classe $C^1$, comme $fv$ est de classe $C^1$ et que
 $\mathrm{div} \, fv = f \mathrm{div} \, v + \left<\nabla f, v\right>$,
par le théorème de la divergence appliqué à $fv$ on obtient
$$
\int_{K} \left<\nabla f(x), v(x)\right> \, dx
=
\int_{\partial K} f(x) \left<v(x), n(x) \right> \, \sigma(dx)
-\int_{K} f(x) \mathrm{div} \, v(x) \, dx.
$$

Réferences
================================================================================