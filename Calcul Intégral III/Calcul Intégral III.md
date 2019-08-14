% Calcul Intégral III

<!-- LaTeX Macros -->
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}

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
(Q: le texte utilise une rotation de $\pi/4$ pour le contre-exemple.
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


### TODO:

Deux façon raisonnables de définir un compact à bord sont données;
la troisème (localement demi-espace après transfo par difféo) peut trouver
sa place en exo ?

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
est le caractère non-nul de la différentielle $dg$. 
Si $T(x) =  A \cdot x + b$ où $A$ est une application linéaire 
(nécessairement inversible) et $b \in \mathbb{R}^n$, 
en posant $\phi(y) = y_n - f(y_1, \dots, y_{n-1})$, on
obtient 
$$
dg(x) = d (\phi \circ T^{-1})(x) = d\phi(T^{-1}(x)) \cdot dT^{-1}(x) 
= d\phi(T^{-1}(x)) \cdot A^{-1}.
$$
Or, $\partial_n \phi(y) = 1$ en tout point $y$ de $V$. 
L'application $A^{-1}$ étant inversible, 
il existe un vecteur $h$ de $\mathbb{R}^n$ tel que
$A^{-1} \cdot h = (0, \dots, 0, 1)$ ; 
pour un tel vecteur on a donc
$$
dg(x) \cdot h = d\phi(T^{-1}(x)) \cdot A^{-1} \cdot h = 
\sum_{i} \partial_i \phi(T^{-1}(x)) (A^{-1} \cdot h)_i = 1.
$$
La différentielle de $g$ est donc bien non-nulle.

Réciproquement, considérons un $x_0 \in \partial K$ et supposons qu'il existe 
une fonction $g: V \to \mathbb{R}$ satisfaisant les propriétés de l'énoncé. 
La différentielle de $g$ étant non nulle en $x_0$, il exists un vecteur de $u$ 
de $\mathbb{R}^n$ tel que 
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
&= dg(T(y)) \cdot u > 0 \\
\end{split}
$$
L'application du théorème des fonctions implicite fournit
un ouvert non vide $U \times I$ inclus dans $T^{-1}(V')$ 
où $U \subset \mathbb{R}^{n-1}$ 
et $I$ est un intervalle ouvert de $\mathbb{R}$ 
et une fonction $f: U \to I$ continûment différentiable telle que
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
si et seulement si $x = T(y)$ et $f(y_1, \dots, y_{n-1}) \leq y_n$.

### TODO

Définition intrinsèque de la normale extérieure.

### Normale extérieure {.definition .theorem}
Si $K$ est un compact à bord $C^1$ caractérisé au voisinage de 
$x_0 \in \partial K$ par l'inégalité $g(x) \leq 0$, 
où $V$ est un voisinage ouvert de $x$ et $g: V \to \mathbb{R}$
est continûment différentiable de différentielle non nulle, 
alors la *normale extérieure* de $K$ en $x \in \partial K \cap V$ 
est le vecteur de $\mathbb{R}^n$ donné par
$$
n(x) = \frac{\nabla g(x)}{\|\nabla g(x)\|}.
$$

### Normale extérieure et hypographe {.proposition}
Si $K$ est un compact à bord $C^1$ caractérisé au voisinage de 
$x_0 \in \partial K$ comme l'hypographe de la fonction 
$f: U \to I$ où $U$ est un ouvert de $\mathbb{R}^{n-1}$ et $I$ 
un intervalle ouvert de $\mathbb{R}$, alors
la normale extérieure de $K$ en $x \in \partial K \cap V$ 
est le vecteur de $\mathbb{R}^n$ donné par
$$
n(x_1, \dots, x_n) = \frac{(1, -\partial_1 f(x_1,\dots, x_{n-1}), \dots, -\partial_{n-1} f(x_1,\dots, x_{n-1}))}{\sqrt{1 +\|\nabla f(x_1, \dots, x_{n-1})\|^2}}, 
$$

### Remarque TODO

A retenir sous la forme: il existe $\alpha > 0$ tel que
$$
n(x_1, \dots, x_n) = \alpha \times (1, -\partial_1 f(x_1,\dots, x_{n-1}), \dots, -\partial_{n-1} f(x_1,\dots, x_{n-1}))
$$
(colinéarité)

### Démonstration {.proof}

**TODO** (essentiellement trivial)

### Terminologie
La normale est dite *extérieure* car si l'on part de $x \in \partial K$ 
et que l'on considère un déplacement suffisamment petit 
dans la direction de la normale, on se retrouve à l'extérieur de $K$. 
En effet, par la définition du gradient,
$$
g(x + h) = g(x) + \left<\nabla g(x), h \right> + o(h) = \left<\nabla g(x), h \right> + o(h)
$$
et par conséquent, si $h = \varepsilon n(x)$ avec $\varepsilon > 0$,
$$
g(x+h) =
\left<\nabla g(x), \varepsilon \frac{\nabla g(x)}{\|\nabla g(x)\|} \right> + o(\varepsilon)
= \varepsilon \|\nabla g(x)\| + o(\varepsilon)
$$
et le second membre de cette équation est positif si $\varepsilon$ est 
suffisamment petit.

### TODO

Evoquer indépendance du choix dans la définition


### TODO

Rendre explicite la normale extérieure dans ce cas et 
un peu plus explicitement (sur un exemple ?) comment trouver
un axe (orthonormé ?) qui permet de se ramener au cadre de 
l'épigraphe. Sur $x^2 + y^2 - 1 \leq 0$ par exemple.

### Partition de l'unité {.definition .propoosition #pu}
Pour toute famille finie d'ouverts $V_i$ de $\R^n$, il existe une famille
$\rho_i: \R^n \to \left[0, +\infty\right[$ de fonctions continues, telles
que $\rho_i(x) = 0$ si $x \not \in V_i$ et 
$$
\sum_{i} \rho_i(x) = 1 \mbox{ pour tout } x \in \bigcup_i V_i.
$$

**TODO** Définition, énoncé existence



### Intégrale de surface {.definition}
Soit $\phi: \partial K \to \mathbb{R}^m$ une fonction continue.
Quand $K$ est caractérisée au voisinage de $x_0 \in \partial K$
comme l'épigraphe de la fonction $f: U \to I$ après une
transformation $T$ qui soit une isométrie directe, 
la *contribution de $V = T(U \times I)$ à l'intégrale de surface
de $\phi$* est définie par la relation
$$
\int_{\partial K \cap V} \phi(x) S(dx) 
:= 
\int_{U}
\phi(z, f(z)) \sqrt{1 + \|\nabla f(z)\|^2}\, dz. 
$$
Si les ouverts $V_i$ consituent un recouvrement fini de $\partial K$ par de tels
ouverts et les $\rho_i$ une partition de l'unité associée,
alors *l'intégrale de surface de $\phi$ sur $\partial K$* 
est définie par
$$
\int_{\partial K} \phi(x) S(dx) 
:= \sum_i \int_{\partial K \cap V_i} \rho_i(x) \phi(x) S(dx) 
$$

### TODO

Evoquer indépendance du choix dans la définition

### Définition {.definition}
On appelle *divergence* d'une fonction différentiable 
$$
v: V \subset \mathbb{R}^n \to \mathbb{R}^n,
\;
v=(v_1, \dots, v_n)
$$
où $V$ est un ouvert, la fonction $\mbox{div} \, f: V \to \mathbb{R}$
définie par
$$
\mbox{div} \, v(x) = \sum_{i=1}^n \partial_i v_i(x)
$$


### Lemme de Stokes {.lemma}
Soit $f: U \to \mathbb{R}$ une fonction de classe $C^1$
où $U$ est un pavé ouvert borné de $\mathbb{R}^{n-1}$. 
Soit $v: U \times \mathbb{R} \to \mathbb{R}^n$ une fonction
de classe $C^1$ de support compact[^sc]. 
L'ensemble $\Omega$ désignant l'hypographe strict de $f$
-- soit $\Omega = \{(y, z) \, | \, y \in \mathbb{R}^{n-1}, \; z < f(y)\}$ --
et $\Gamma$ le graphe de $f$
-- soit $\Gamma = \{(y, f(y)) \, | \, y \in \mathbb{R}^{n-1}\}$ --
et $n$ la normale extérieure associée,
on a la relation
$$
\int_{\Omega} \mbox{div} \, v(x) \, dx
=
\int_{\Gamma} \left<v(x), n(x) \right> \, S(dx)
$$

[^sc]: le support d'une fonction $v$ est l'adhérence de l'ensemble des
points où elle est non nulle:
$$
\mbox{supp}(v) = \overline{\{x \in \mbox{dom}(v)\, | \, f(x) \neq 0\}}.
$$
Ici, $f$ étant définie dans un ouvert ($\mbox{dom}(f) = U \times \mathbb{R}$), 
son support est compact si et seulement si l'ensemble $\{x \, | \, f(x) \neq 0\}$ 
est borné et sa distance au complémentaire de $U\times \mathbb{R}$ 
dans $\mathbb{R}^n$ est positive.

### Démonstration {.proof}

On remarque que si $v = w e_i$ où $w: U \times \mathbb{R} \to \mathbb{R}$ est
de classe $C^1$ et $i \in \{1,\dots, n\}$, 
comme $\mbox{div}\, v = \partial_i w$ et 
$\left<v(x), n(x) \right> = w(x) n_i(x)$, 
le résultat du lemme devient
$$
\int_{\Omega} \partial_i w(x) \, dx
=
\int_{\Gamma} w(x) n_i(x) \, S(dx).
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
\nabla f(x)^t & 1
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
&= \int_{U \times \left]-\infty, 0\right[} 
\partial_i w(x_1, \dots, x_{n-1}, x_n + f(x_1, \dots, x_{n-1})) 
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
\partial_i w(\pi(x), x_n + f(\pi(x))) 
\, dx_i
=
0.
$$
Par le théorème de Fubini, on peut alors déduire que
\begin{multline*}
\int_{U \times \left]-\infty, 0\right[} 
\partial_i w(\pi(x), x_n + f(\pi(x))) 
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
w(\pi(x), x_n + f(\pi(x)) \, dx
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
n(y, f(y)) = \frac{(1, -\partial_1 f(y), \dots, -\partial_{n-1} f(y))}{\sqrt{1 +\|\nabla f(y)\|^2}}, 
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
\int_{\Gamma} w(x) n_i(x)\, dS(x).
$$

### TODO

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

### TODO
Préfiguration intégrale de surface "intrinsèque".


Exercices
================================================================================

Déformations
--------------------------------------------------------------------------------

$\Omega$ dans $U$ paramétrisé par une déformation $T = I + u$ avec $u$ petit
et une base $\Omega_0$ qui est un compact à bords $C^1$. Montrer que
si la base est un compact à bord $C^1$, les déformés aussi.

Compact à Bords
--------------------------------------------------------------------------------

Caractérisation par "applatissement" local en un demi-espace fermé.

Exemples de compacts à bord (déterminés implicitement)
--------------------------------------------------------------------------------

... par la fonction distance orientée par exemple ?

Calcul
--------------------------------------------------------------------------------

Un calcul réalisable par Fubini et/ou Stokes ? Dans le disque unité ?
Avec un champ de vecteurs


Réferences
================================================================================
