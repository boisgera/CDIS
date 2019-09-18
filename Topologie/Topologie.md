% Topologie

<!-- LaTeX Macros -->
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}

<!--
TODO / acquis {.meta}
--------------------------------------------------------------------------------

  - intro: ensembles "nus" (théorie des ensembles sans structure additionnelle)
   ne disposent que de la notion d'appartence et d'aucun notion de proximité.
   Structure topologiques sur les ensembles comblent ce manque. 
   "dualité" structure / morphismes, ie topologie peut être vue comme
   l'étude des fcts continues (on peut tout ramener à ça: limites, etc.).

  - "hiérarchie" des structures topologiques, justification
    (généralité et/ou "abstraction"), positionnement utile.
    Evocation dim finie et infinie (partiellement ici, 
    principalement les choses qui ne posent pas de pb
    supplémentaire par rapport au cas dim finie).
    Exemple définition fonction continue de façon abstraite ... 
    pas plus compliqué !

  - point fixe, appli contractante, complétude

  - lister "use cases" compacité,
    transition locale vers le (semi-)global (dim. finie),
    extraction recouvrement fini (ex compacts à bords),
    optimisation, etc. Compacité substitut à fini dans le cas des
    fonctions continues, etc.

  - warning: pptés définies *relativement à un espace de référence* 
    (ex: fermé dans quoi ?). Topologie "trace" / induite, sous-espace ...

### TODO

    >>> from numpy import *

-->

Structures topologiques
================================================================================

### Norme {.definition}
Une *norme* sur un espace vectoriel $E$ est une application
$$
\| \cdot \|: E \to \left[0, +\infty\right[
$$ 
telle que pour tous les points $x$ et $y$ de $E$ et tous les scalaires
$\lambda$ dans $\R$ on ait

 1. [$\|x\| = 0$ si et seulement si $x=0$ (*séparation*)]{#norme-sep},

 2. [$\|\lambda x\| = |\lambda| \|x\|$ (*homogénéité*)]{#norme-homo},

 3. [$\|x+y\| \leq \|x\| + \|y\|$ (*inégalité triangulaire*).]{#norme-ineg}

### Espace vectoriel normé {.definition}
Un espace vectoriel $E$ muni d'une norme sur $E$ est 
*un espace vectoriel normé*.

<!--
### Remarque
Terminologie evn, espace métriques regroupées après coup ? Et référence
au cas plus général en annexe ?

**TODO:** limitation des evn, sous-ensembles d'evn, nouvelle
structure, et plus tard (?) comment espace métrique n'est pas plus
général (à une isométrie près). Convention (légèrement abusive)
qui consiste à appeler espace métrique sous-ensembles d'un evn.
**Update:** distinguer ici le cours oral du poly; la restriction
"sous-ensemble d'un e.v.n." peut valoir uniquement dans le cours
oral.

### TODO

Espace normés: fonctions bornées à valeurs dans $\mathbb{R}$,
fonctions numériques continues définies sur un compact (à faire
plus tard: nécessite à la fois compacité et complétude; évoquer
aussi Arzela-Ascoli / attendre Calcul Diff 3 / zapper ?)
-->

### Normes sur $\R^n$ {.example}
La norme privilégiée sur $\R^n$ est la *norme euclidienne*
$\|\cdot\|_2$, définie par
$$
\|x\|_2 = \sqrt{x_1^2 + \dots + x_n^2}.
$$
Elle se déduit du *produit scalaire* usuel
$$
\left<x, y\right> = x_1 y_1 + \dots + x_n y_n
$$
par la relation $\|x\|_2 = \sqrt{\left<x, x\right>}$.
On la notera simplement $\|\cdot\|$ s'il n'y a pas d'ambiguité.
Deux autres normes communes dont on peut doter $\R^n$:
la norme $\|\cdot\|_1$, définie par
$$
\|x\|_1 = |x_1| + \dots + |x_n|
$$
et la norme $\|\cdot\|_{\infty}$, définie par
$$
\|x\|_{\infty} = \max_{i=1\dots n} |x_i|.
$$

### Opérateurs linéaires bornés {.proposition}
Si $E$ et $F$ sont deux espaces vectoriels normés muni des normes
$\|\cdot\|_E$ et $\|\cdot\|_{F}$, l'ensemble des applications linéaires
$A: E \to F$ dites *bornées*, telles que *la norme d'opérateur*
$$
\|A\| := \sup_{x \neq 0} \frac{\|A \cdot x\|_F}{\|x\|_E} < +\infty
$$
est un espace vectoriel normé.

### Démonstration {.proof}
Il est clair que si $A$ et $B$ sont des opérateurs linéaires bornés de $E$ dans
$F$ et $\lambda$ est un réel, 
alors $\lambda A$ et $A + B$ sont des opérateurs linéaires bornés de $E$ dans $F$ ; 
les opérateurs linéaires bornés forment donc un espace vectoriel. 
De plus la valeur $\|A\|$ est positive et si $\|A\| = 0$, c'est-à-dire si
$$
\sup_{x \neq 0} \frac{\|A \cdot x\|_F}{\|x\|_E} = 0,
$$
nécessairement $A \cdot x$ est nulle pour tout $x \in E \setminus \{0\}$.
Comme $A \cdot 0 = 0$ par linéarité, l'opérateur $A$ est nul.
On a également
$$
\|\lambda A\| = \sup_{x \neq 0} \frac{\|\lambda A \cdot x\|_F}{\|x\|_E} 
= \sup_{x \neq 0} \frac{|\lambda| \|A \cdot x\|_F}{\|x\|_E} 
= |\lambda|\sup_{x \neq 0} \frac{\|A \cdot x\|_F}{\|x\|_E}
= |\lambda| \|A\| 
$$
et 
$$
\begin{split}
\|A+B\| 
    &= \sup_{x \neq 0} \frac{\|(A+B) \cdot x\|_F}{\|x\|_E} \\
    &= \sup_{x \neq 0} \frac{\|A\cdot x + B \cdot x\|_F}{\|x\|_E} \\
    &\leq \sup_{x \neq 0} \frac{\|A\cdot x\|_F + \|B \cdot x\|_F}{\|x\|_E} \\
    &\leq \sup_{x \neq 0} \frac{\|A\cdot x\|_F}{\|x\|_E} 
        + \sup_{x \neq 0} \frac{\|B\cdot x\|_F}{\|x\|_E} \\
    &= \|A\| + \|B\|
\end{split}
$$
ce qui prouve que la norme d'opérateur est bien une norme sur 
l'espace des opérateurs bornés de $E$ dans $F$.

### Opérateurs linéaires de $\R^n$ dans $\R^m$ {.proposition}
Tout opérateur linéaire de $\R^n$ dans $\R^m$ 
-- munis de leur normes euclidiennes -- est borné.

### Démonstration {.proof}
Soit $e_i$ le $i$-ème vecteur de la base canonique de $\R^n$
et soit $x=(x_1, \dots, x_n) \in \R^n$.
Comme $x = x_1 e_1 + \dots + x_n e_n$, on a 
$$
A \cdot x
= A \cdot (x_1 e_1 + \dots + x_n e_n) = 
\sum_{i=1}^n x_i (A \cdot e_i).
$$
Par [l'inégalité triangulaire](#norme-ineg) 
et par [homogénéité de la norme](#norme-homo),
$$
\|A \cdot x\|_2 \leq \sum_{i=1}^n |x_i| \|A \cdot e_i\|_2
\leq \sum_{i=1}^n \|x\|_2 \|A \cdot e_i\|_2
= \left(\sum_{i=1}^n \|A \cdot e_i\|_2\right) \|x\|_2,
$$
d'où le caractère borné de $A$.


### {.remark .ante}
Si $X$ est un sous-ensemble d'un espace vectoriel normé $E$, 
celui-ci "hérite" de $E$ une mesure de la distance entre 
deux points $x$ et $y$ avec la grandeur 
$$
d(x, y) = \|x - y\|.
$$ 

![Le cercle unité $\{x \in \mathbb{R}^2 \, | \, \|x\|=1\}$.
Bien que $x=(1,0)$ et $y=(0,1)$ appartiennent au cercle unité, 
ni $x+y$ ni $2 x$ ne lui appartiennent. Il hérite néanmoins
d'une distance $d$ de l'espace euclidien $\mathbb{R}^2$
(telle que $d(x,y) = \|x - y\|_2 = \sqrt{2}$
quand $x=(1,0)$ et $y=(0,1)$),
ce qui fait de lui un espace métrique.](images/circle.tex)

Par contre, à moins que $X$ soit un sous-espace vectoriel de $X$
les additions entre élements de $X$ ou la multiplication d'un 
élément de $X$ n'ont plus de sens dans $X$ ;
nous ne pouvons plus définir une norme sur $X$.

La fonction $d$ définie ci-dessus sur $X$ vérifie automatiquement 
les axiomes qui font techniquement d'elle une distance:

### Distance
Une *distance* sur un ensemble $X$ est une fonction 
$$
d: X \times X \to \left[0, +\infty\right[
$$
telle que pour tous points 
$x, y$ et $z$ de $X$, on ait:

 1. [$d(x,y) = 0$ si et seulement si $x = y$ (*séparation*)]{#dist-sep},

 2. [$d(x,y) = d(y,x)$ (*symétrie*)]{#dist-sym},

 3. [$d(x,z) \leq d(x,y) + d(y,z)$ (*inégalité triangulaire*)]{#dist-ineg}.

### Espace métrique  {.definition}
Un *espace métrique* est un ensemble $X$ muni d'une *distance*.

### {.post}
Une fonction distance est également appelée une *métrique*.

### Sous-ensemble d'un espace vectoriel normé {.proposition}
Soit $X$ un sous-ensemble d'un espace vectoriel normé $E$. 
La fonction $d: X \times X \to \left[0, +\infty\right[$ 
définie par
$$
d(x, y) := \|x - y\|
$$
est une distance sur $X$.

### {.post}
Autrement dit, tout sous-ensemble d'un espace vectoriel normé "est" un
espace métrique, c'est-à-dire qu'il existe une fonction distance
"naturelle" dont on peut le doter, induite par l'espace vectoriel normé.
Cela vaut en particulier pour l'espace vectoriel normé lui-même:
tout espace vectoriel normé "est" un espace métrique.

Réciproquement, les espaces métriques ne sont pas plus généraux que les
sous-ensembles d'espace vectoriels normés: tout espace métrique peut en
effet être identifié au moyen d'une isométrie avec un tel sous-ensemble
(cf. l'exercice "[Plongement de Kuratowski]"). Les espaces métriques
n'exhibent donc aucune propriété qui ne soit déjà manifeste dans l'étude
des sous-ensembles d'espaces vectoriel normés.

### Démonstration {.proof}

Par construction, la fonction $d$ est bien positive. 
De plus, pour tous points $x, y$ et $z$ de $X$:

 1. Par l'[axiome de séparation des normes](#norme-sep), 
    $$
    \|x - y\| = 0 \, \Leftrightarrow \, x - y = 0 \, \Leftrightarrow \, x = y.
    $$
    Cela entraîne que $d(x, y) = 0$ si et seulement si $x=y$, 
    soit l'[axiome de séparation pour la distance $d$](#dist-sep).

 2. Par [homogénéité de la norme $\| \cdot \|$](#norme-homo), on a
    $$
    \|x - y\| = \|(-1) \times (y-x)\| = |-1| \times \|y - x\| = \|y - x\|,
    $$
    et donc $d(x, y) = d(y, x)$, 
    d'où la [symétrie de la fonction $d$](#dist-sym).

 3. Par l'[inégalité triangulaire pour les normes](#norme-ineg), on a
    $$
    \|x - z\| = \|x - y - (y - z)\| \leq \|x - y\| + \|y - z\|,
    $$
    ce qui établit l'[inégalité triangulaire pour la distance $d$](#dist-ineg).


### Distance point-ensemble et ensemble-ensemble
Une distance $d$ sur $X$ associe à deux points de $X$ un réel positif.
Cette fonction peut servir de base pour définir une distance entre
un point $x$ de $X$ et un ensemble de points de $A$ de $X$:
$$
d(x, A) := \inf_{a \in A} d(x, A) \in \left[0, +\infty \right]
$$
ou même entre deux ensembles $A$ et $B$ de points de $X$:
$$
d(A, B) = \inf_{a \in A} d(a, B) = \inf_{a \in A} \inf_{b \in B} d(a, b)
\in \left[0, +\infty \right].
$$
Si $A$ est l'ensemble vide, on a $d(x, A) = +\infty$ et si $A$ ou $B$ est
vide on a $d(A, B)= +\infty$ ; ce sont les seuls cas où ces extensions de
la distance entre points peuvent prendre des valeurs infinies.

### Isométries {.definition}
Une application $f: X \to Y$ définie entre deux espaces
métriques $(X, d_X)$ et $(Y, d_Y)$ telle que:
$$
d_Y(f(x), f(y)) = d_X(x, y)
$$
est une *isométrie*.

### {.post}
Les isométries sont les *morphismes* des espaces métriques: 
les applications qui préservent la structure des espaces métriques.
Construire des isométries peut aller de pair avec la construction
d'une métrique sur un ensemble qui en est initialement dépourvu ;
voir à ce propos l'exercice "[Droite réelle achevée]".

### Sous-espace métrique {.definition}
Un sous-ensemble $Y$ d'un espace métrique $X$ est un *sous-espace métrique*
de $X$ lorsqu'il est muni de la distance de $X$, restreinte aux points de
$Y$.

### Structure topologique d'un espace métrique
Il est possible de se livrer à un exercice d'abstraction sur les
espaces métriques en considérant la distance $d(x, A)$ entre un 
point $x$ et un ensemble de points $A$ et en regardant uniquement
si cette grandeur est nulle -- on dira alors que $x$ *adhère* à $A$ -- 
ou strictement positive:
$$
x \mbox{ adhère à } A \, \Leftrightarrow \, d(x, A) = 0.
$$
En faisant de la sorte pour tous les points et ensembles de points
de l'espace métrique et en "oubliant" ensuite la distance qui a permis
cette construction, on remplace une mesure quantitative de proximité
sur l'ensemble par une mesure uniquement qualitative 
(dans ce contexte, "$x$ adhère à $A$" peut être interprété comme 
"$x$ dans $A$ ou infiniment proche de $A$").

### Relation d'adhérence {.definition #ak}

Une *relation d'adhérence* (ou *test d'adhérence*) sur l'ensemble *X* est une 
relation entre éléments de $X$ et sous-ensembles de $X$ telle que:

 1. Aucun point n'adhère à l'ensemble vide,

 2. Tout point d'un ensemble adhère à cet ensemble,

 3. Un point adhère à l'union de deux ensembles 
    si et seulement s'il adhère à l'un des deux ensembles,

 4. Un point qui adhère à l'ensemble des points adhérents 
    à un ensemble adhère à cet ensemble.

### Espace topologique
Un *espace topologique* est un ensemble muni d'[une relation d'adhérence](#ak).
Les éléments de l'ensemble sont appelés des *points*, 
ses sous-ensembles des *ensembles de points*.

### Sous-espace topologique
Un sous-ensemble $Y$ d'un espace topologique $X$ est un *sous-espace topologique*
de $X$ lorsqu'il est muni de la relation d'adhérence de $X$, 
restreinte aux points et sous-ensembles de $Y$.

### Continuité
Une application $f: X \to Y$ définie entre deux espaces topologiques
est *continue en $x \in X$* si, lorsque $x$ adhère à $A$ dans $X$, 
$f(x)$ adhère à $f(A)$ dans $Y$. Une application continue en tout point
$x \in X$  est *continue*.

--------------------------------------------------------------------------------

### {.post}
Les applications continues sont les *morphismes* des espaces topologiques:
elle préservent la structure des espaces topologiques.

### {.post}
Cette caractérisation "abstraite" des fonctions continues se prête
à des preuves particulièrement concises de certains résultats. Ainsi:

### Composée d'applications continues
La composée de fonctions $f:X \to Y$ continue en $x \in X$ 
et $g:Y\to Z$ continue en $f(x) \in Y$ est continue en $x$.

### Démonstration {.proof}
Si $x$ adhère à $A$, par continuité de $f$ en $x$,
$f(x)$ adhère à $f(A)$ ; donc par continuité de $g$ en $y=f(x)$,
$g(y)= (g \circ f)(x)$ adhère à $g(f(A)) = (g \circ f)(A)$.
La composée de $f$ et de $g$ est donc continue en $x$.

### Les espaces métriques sont des espaces topologiques
Soit $X$ un espace métrique muni d'une distance $d$. 
La relation définie par
$$
x \mbox{ adhère à } A \, \Leftrightarrow \, d(x, A) = 0
$$
est une relation d'adhérence sur $X$.

### Démonstration {.proof}

 1. Le point $x$ adhère à l'ensemble vide si et seulement si 
    $d(x, \varnothing) = 0$, mais
    $$
    d(x, \varnothing) = \inf_{y \in \varnothing} d(x, y) = +\infty, 
    $$
    par conséquent aucun point d'adhère à l'ensemble vide.

 2. Si $x \in A$, on a 
    $$
    d(x, A) = \inf_{y \in A} d(x, y) = d(x, x) = 0,
    $$
    donc $x$ adhère à $A$.

 3. Si $x$ adhère à $A$, c'est-à-dire si $d(x,A)=0$, alors
    $$
    0 \leq d(x, A \cup B) = \inf_{y \in A \cup B} d(x, y)
    \leq  \inf_{y \in A} d(x, y) = d(x, A)= 0
    $$
    et donc $x$ adhère à $A \cup B$.
    De la même façon, du fait de la symétrie des rôles des ensembles $A$ et $B$,
    si $x$ adhère à $B$ alors $x$ adhère à $A \cup B$.

    Réciproquement, si $x$ adhère à $A \cup B$, alors il existe une
    suite de points $x_k$ de $A \cup B$ telle que $d(x, x_k) \to 0$
    quand $k \to +\infty$. Cette suite $x_k$ admet une suite extraite
    de points de $A$ et/ou une suite extraite de points de $B$.
    Dans le premier cas on a donc $d(x, A)=0$ et dans le second $d(x, B)=0$,
    c'est-à-dire que $x$ adhère à $A$ et/ou à $B$.

 4. Les points $y$ qui adhèrent à l'ensemble $A$ sont caractérisés par
    $d(y, A) = 0$. Par conséquent, l'ensemble des points $x$ qui adhèrent
    à cet ensemble sont caractérisés par
    $$
    d(x, \{y \in X \, | \, d(y, A) = 0\}) = 0.
    $$
    Pour tout $x$ de ce type et pour tout $\varepsilon > 0$,
    il existe un $y$ tel que $d(y, x) \leq \varepsilon /2$ et $d(y, A)= 0$
    et donc un $z \in A$ tel que $d(y, z) \leq \varepsilon/2$.
    L'[inégalité triangulaire](#dist-ineg) fournit donc
    $$
    d(x, A) = \inf_{a \in A} d(x, a) \leq d(x, z) 
    \leq d(x, y) + d(y, z) \leq \varepsilon
    $$
    et comme $\varepsilon >0$ est arbitraire, $d(x, A)=0$ : $x$ adhère à $A$.

### L'espace topologique généralise l'espace métrique

Les espaces métriques "sont" des espaces topologiques 
(c'est-à-dire héritent automatiquement d'une relation d'adhérence,
définie à partir de leur distance). 
A l'inverse, les espaces topologiques qui peuvent être muni d'une distance
compatible avec leur relation d'adhérence sont dits *métrisables*.
Toutefois, tous les espaces topologiques ne sont pas métrisables[^Sier];
la notion d'espace topologique est donc strictement plus générale que la notion
d'espace métrique.

[^Sier]: Par exemple, l'espace formé de deux points $\{0, 1\}$ 
où $x$ adhère à $A$ si $x$ appartient à $A$ ou $x=0$ et $A=\{1\}$
-- c'est-à-dire l'[espace de Sierpiński](https://en.m.wikipedia.org/wiki/Sierpi%C5%84ski_space) --
est un espace topologique qui n'est pas métrisable. En effet, si $d$ était une
distance sur cet ensemble, telle que $d(x, A)= 0$ si et seulement si $x$
adhère à $A$, alors on aurait $d(0, \{1\}) = d(0, 1) = 0$, ce qui contredirait
[l'axiome de séparation pour les distances](#dist-sep).

### Produit d'espaces vectoriels normés {.definition}
On appelle *produit des espaces vectoriels normés $E_1$, $\dots$, $E_n$*, 
munis des normes $\|\cdot\|_{E_1}$, $\dots$, $\|\cdot\|_{E_n}$, 
l'espace vectoriel $E = E_1 \times \dots \times E_n$, 
muni de la norme
$$
\|(x_1,\dots, x_n)\| = \sqrt{\|x_1\|_{E_1}^2 + \dots + \|x_n\|_{E_n}^2}.
$$

### Produit d'espaces métriques {.definition}
On appelle *produit des espaces métriques $X_1$, $\dots$, $X_n$,* 
munis des distances $d_{X_1}$, $\dots$, $d_{X_n}$ le produit cartésien
$X = X_1 \times \dots \times X_n$, muni de la distance
$$
d((x_1,\dots, x_n), (y_1,\dots, y_n)) 
= \sqrt{d_{X_1}(x_1, y_1)^2 + \dots + d_{X_n}(x_n, y_n)^2}.
$$

<!--

(rk: Quotient ne "marche pas" dans une simple structure métrique.
Arf, si, si les classe d'équivalences sont fermées, via la distance
de Hausdorff. Lol.)
-->

Limite
================================================================================

### Limite d'une suite de points {.definition}
Une suite $x_k$ de valeurs d'un espace métrique $X$ a comme *limite* 
un point $\ell$ de $X$ -- ou *converge vers $\ell$* -- 
si $x_{k}$ est arbitrairement proche de $\ell$
à partir d'un certain rang, c'est-à-dire si 
pour tout $\varepsilon > 0$, il existe un entier $n$ 
tel que pour tout $k \geq n$, $d(x_k, \ell) \leq \varepsilon$,
ou encore si
$$
\lim_{k \to +\infty} d(x_k, \ell) = 0.
$$
On utilisera alors une des deux notations:
$$
\ell = \lim_{k\to +\infty} x_k
\; \mbox{ ou } \;
x_k \to \ell \mbox{ quand } k \to + \infty.
$$
Une suite possédant une limite est dite *convergente*.

### Unicité de la limite d'une suite {.proposition}
Si une suite $x_k$ admet une limite, celle-ci est unique.

### Démonstration {.proof}
Par [l'inégalité triangulaire](#dist-ineg), 
si les points $\ell$ et $\ell'$
sont des limites de la suite des $x_k$, alors pour tout entier $k$ on a
$$
d(\ell, \ell') \leq d(x_k, \ell) + d(x_k, \ell').
$$
Comme il existe des rangs $n$ et $n'$ tels que
lorsque $k \geq n$ et $k\geq n'$, on a $d(x_k, \ell) \leq \varepsilon /2$
et $d(x_k, \ell') \leq \varepsilon /2$, 
pour $k = \max(n, n')$, on a
$d(\ell, \ell') \leq \varepsilon$. 
La valeur $\varepsilon > 0$ étant arbitraire,
on en déduit que $d(\ell, \ell')=0$, 
soit par [l'axiome de séparation](#dist-sep), 
que $\ell = \ell'$. 
Il n'existe donc qu'une limite possible pour la suite des $x_k$.

### Limite d'une fonction en un point {.definition}
Soit $f: X \subset Y \to Z$ une application 
définie sur un sous-ensemble $X$ d'un espace métrique $Y$ 
et à valeurs dans un espace métrique $Z$.
Soit $x$ un point de $Y$ adhérent à $X$. 
Le point $\ell \in Z$ est la *limite* de $f$ en $x$ si pour toute suite
$x_k$ de points de $X$ convergeant vers $x$ mais ne prenant pas la
valeur $x$, on a $\lim_{k \to +\infty} f(x_k) = \ell$.
On utilisera alors une des deux notations:
$$
\ell = \lim_{y \to x} f(y)
\; \mbox{ ou } \;
f(y) \to \ell \mbox{ quand } y \to x.
$$

### Unicité de la limite d'une fonction en un point {.proposition}
Si la fonction $f$ admet une limite en $x$, celle-ci est unique.

### Démonstration {.proof}
Un corollaire de [l'unicité de la limite des suites][Unicité de la limite d'une suite].

### Continuité et limite
Une fonction $f: X \to Y$, où $X$ et $Y$ sont deux espaces métriques, est
continue en $x \in X$ si et seulement si la limite de $f$ existe en
$x$ et
$$
\lim_{y \to x} f(y) = f(x).
$$

### Démonstration {.proof}
Supposons que $f$ soit telle que $f(y) \to f(x)$ quand $y \to x$.
Soit $A$ un sous-ensemble de $X$ tel que $x$ adhère à $A$.
Dans un espace métrique, cela signifie que $d(x, A) = 0$, ou encore
qu'il existe une suite de points $x_k$ de $A$ telle que 
$d(x, x_k) \to 0$ quand $x_k \to x$. 
Par conséquent, $f(x_k) \to f(x)$ quand $k \to +\infty$, 
soit $d(f(x_k), f(x)) \to 0$ quand $k \to +\infty$. 
Comme l'ensemble $\{f(x_k) \, | \, k \in \N\}$ est un sous-ensemble
de $f(A)$, nous en déduisons que $d(f(x), f(A)) = 0$: 
le point $f(x)$ adhère à $f(A)$.
La fonction $f$ est donc continue en $x$.

Réciproquement, si $f(y) \not \to f(x)$ quand $y \to x$, 
il existe une suite $x_k$ tendant vers $x$ telle que $f(x_k)$ ne tende
pas vers $f(x)$ et donc un $\varepsilon > 0$ et une suite $y_k$ extraite
de $x_k$ telle que $y_k \to x$ et pour tout $k \in \N$, 
$d(f(y_k), f(x))  > \varepsilon$. 
Par conséquent, $x$ adhère à $\{y_k \, | \, k \in  \N\}$, mais 
$f(x)$ n'adhère pas à $f(\{y_k \, | \, k \in  \N\}) = 
\{f(y_k) \, | \, k \in  \N\}$ ; 
la fonction $f$ n'est donc pas continue en $x$.

### Continuité de la distance {.proposition}
Soit $X$ un espace métrique. La fonction distance
$d: X \times X \to \left[0, +\infty\right[$ est une application continue.
Si $A$ est un sous-ensemble non vide de $X$, la distance à $A$
$x \in X \mapsto d(x, A) \in \left[0, +\infty\right[$ 
est une application continue.

### Démonstration {.proof}
Soient $(x_0, y_0)$ et $(x, y)$ deux points de l'espace produit $X \times X$.
Par [l'inégalité triangulaire](#dist-ineg), 
$d(x, y) \leq d(x, x_0) + d(x_0, y_0) + d(y_0, y)$
et
$d(x_0, y_0) \leq d(x_0, x) + d(x, y) + d(y, y_0),$
donc
$$
|d(x, y) - d(x_0, y_0)| \leq d(x_0, x) + d(y_0, y).
$$
Or la distance sur le produit $X \times X$ est définie comme
$$
d_{X \times X}((x, y), (x_0, y_0)) = \sqrt{d(x, x_0)^2 + d(y, y_0)^2},
$$
donc
$$
|d(x, y) - d(x_0, y_0)| \leq 2 d_{X \times X}((x, y), (x_0, y_0))
$$
et $d(x, y) \to d(x_0, y_0)$ quand $(x, y) \to (x_0, y_0)$. 

Pour tout $a \in A$, on a $d(x, a) \leq d(x, x_0) + d(x_0, a)$ 
et donc $d(x, A) \leq d(x, x_0) + d(x_0, A)$. 
En intervertissant $x$ et $x_0$, on obtient 
également $d(x_0, A) \leq d(x_0, x) + d(x, A)$. 
Par [symétrie de la distance](#dist-sym), ces deux inégalités entraînent
$$
|d(x, A) - d(x_0, A)| \leq d(x_0, x)
$$
et donc $d(x, A) \to d(x_0, A)$ quand $x \to x_0$.

Bestiaire
================================================================================

### Définitions séquentielles {.definition}

Soit $X$ un espace métrique et $A$ un ensemble de points de $X$.

  - Un point *adhère* à un ensemble $A$ s'il existe une suite de
    points de $A$ qui converge vers ce point.

  - Un ensemble $A$ est *fermé* si la limite de toute suite de points de $A$
    qui est convergente (dans $X$) appartient à $A$.

  - Un point est *frontière* de $A$ s'il existe une suite de points de $A$
    qui converge vers ce point et une suite de points du complémentaire de $A$
    dans $X$ qui converge vers ce point.

  - Un point $x$ est *intérieur* à un ensemble $A$ si toute
    suite convergeant vers $x$ appartient à $A$ à partir d'un certain rang.

  - Un ensemble $V$ est un *voisinage* d'un point $x$ de $X$ si toute
    suite convergeant vers $x$ appartient à $V$ à partir d'un certain rang.

  - Un ensemble $A$ est *ouvert* si toute suite de points de $X$ 
    qui converge vers un point de $A$ appartient à $A$ 
    à partir d'un certain rang.

### Ensembles dérivés {.definition}
Soit $A$ un ensemble de $X$. On note

  -  $\overline{A}$ l'*adhérence* de $A$
     (l'ensemble des points adhérents à $A$),

  - $\partial A$ la *frontière* de $A$ 
    (l'ensemble des points frontières de $A$).

  - $\mathring{A}$ l'*intérieur* de $A$ 
    (l'ensemble des points intérieurs à $A$).

### Définitions métriques {.definition}
Soit $X$ un espace métrique et $A$ un ensemble de points de $X$.

  - Un point $x$ *adhère* à un ensemble $A$ si
    sa distance à l'ensemble $A$ est nulle:
    $$
    x \in \overline{A} \; \Leftrightarrow \; d(x, A) = 0.
    $$

  - Un ensemble $A$ est *fermé* si tous les points à distance nulle de $A$
    appartiennent à $A$:
    $$
    A = \overline{A} \; \Leftrightarrow \; (d(x, A) = 0 \Rightarrow x \in A).
    $$

  - Un point est *frontière* de $A$ si sa distance à $A$ et au complémentaire
    de $A$ est nulle:
    $$
    x \in \partial{A} 
    \; \Leftrightarrow \; 
    (d(x, A) = 0 \mbox{ et } d(x, X \setminus A)=0).
    $$

  - Un point $x$ est *intérieur* à un ensemble $A$ si sa distance au 
    complémentaire de $A$ est strictement positive:
    $$
    x \in \mathring{A}
    \; \Leftrightarrow \; 
    d(x, X \setminus A) > 0.
    $$

  - Un ensemble $V$ est un *voisinage* d'un point $x$ de $X$ si la
    distance de $x$ au complémentaire de $V$ est strictement positive:
    $$
    V \in \mathcal{V}(x)
    \; \Leftrightarrow \; 
    d(x, X \setminus V) > 0.
    $$

  - Un ensemble $A$ est *ouvert* si la distance de tout point de $A$
    au complémentaire de $A$ est strictement positive:
    $$
    A = \mathring{A}
    \; \Leftrightarrow \; 
    (x \in A \Rightarrow d(x, X \setminus A) > 0).
    $$

  - Pour tout $x \in X$ et $r\geq 0$, on définit la *boule ouverte 
    de centre $x$ et de rayon $r$* comme
    $$
    B(x, r) = \{y \in X \, | \, d(x, y) < r\}
    $$
    et la *boule fermée 
    de centre $x$ et de rayon $r$* comme
    $$
    \overline{B}(x, r) = \{y \in X \, | \, d(x, y) \leq r\}.
    $$

### Définitions topologiques {.definition}
Soit $X$ un espace topologique et $A$ un ensemble de points de $X$.

  - L'*adhérence* $\overline{A}$ d'un ensemble $A$ est constituée des points
    qui adhèrent à l'ensemble $A$.
    
  - Un ensemble $A$ est *fermé* s'il est égal à son adhérence:
    $$
    A = \overline{A} \; \mbox{ ou } \; (x \in \overline{A} \Leftrightarrow x \in A)
    $$

  - Un point est *frontière* de $A$ s'il appartient à l'adhérence de $A$ et
    à celle de son complémentaire:
    $$
    x \in \partial{A} 
    \; \Leftrightarrow \; 
    (x \in \overline{A} = 0 \mbox{ et } x \in \overline{X \setminus A}).
    $$

  - Un point $x$ est *intérieur* à un ensemble $A$ s'il n'adhère pas
    au complémentaire de $A$
    $$
    x \in \mathring{A}
    \; \Leftrightarrow \; 
    x \not \in \overline{X \setminus A}.
    $$

  - Un ensemble $V$ est un *voisinage* d'un point $x$ de $X$ si
    $x$ est intérieur à $V$
    $$
    V \in \mathcal{V}(x)
    \; \Leftrightarrow \; 
    x \not \in \overline{X \setminus V}.
    $$

  - Un ensemble $A$ est *ouvert* s'il est un voisinage de chacun de ses points
    $$
    A = \mathring{A}
    \; \Leftrightarrow \; 
    (x \in A \Rightarrow x \not \in \overline{X \setminus A}).
    $$

### Calcul topologique {.ante}
Avec l'opérateur d'adhérence, [les axiomes définissant
une relation d'adhérence](#ak) -- et donc un espace topologique -- 
prennent une forme symbolique simple :

 1. $\overline{\varnothing} = \varnothing$,

 2. $A \subset \overline{A}$,

 3. $\overline{A \cup B} = \overline{A} \cup \overline{B}$,

 4. $\overline{\overline{A}} = \overline{A}$.

### Ouverts et fermés {.theorem}
Un ensemble est ouvert si et seulement si son complémentaire
est fermé ; un ensemble est fermé si et seulement 
si son complémentaire est ouvert.

### Démonstration {.proof}
En raisonnant par équivalence, le complémentaire $F = X \setminus U$
d'un ensemble ouvert $U$ -- qui vérifie aussi $U = X \setminus F$ -- est 
caractérisé par
$$
x \in X \setminus F \Rightarrow x \not \in \overline{X \setminus (X \setminus F)},
$$
soit $x \in X \setminus F \Rightarrow x \not \in \overline{F}$.
La contraposée de cette relation -- qui lui est équivalente -- est
$x \in \overline{F} \Rightarrow x \in F$. Comme $F \subset \overline{F}$,
cela équivaut $\overline{F} =F$, c'est-à-dire au caractère fermé de $F$.

La démonstration de la seconde partie de l'énoncé est immédiate
(le complémentaire du complémentaire d'un ensemble est cet ensemble).

### Continuité {.theorem}
Une fonction $f: X \to Y$ où $X$ et $Y$ sont des espaces topologiques est 
continue si et seulement si l'image réciproque de tout ensemble fermé 
(resp. ouvert) de $Y$ 
par $f$ est un ensemble fermé (resp. ouvert) de $X$.

### Démonstration {.proof}
Supposons $f$ continue. 
Si $B$ est un ensemble fermé de $Y$, par continuité, 
  $$
  f(\overline{f^{-1}(B)}) 
  \subset 
  \overline{f(f^{-1}(B))} 
  \subset \overline{B}
  =
  B.
  $$
Prendre l'image réciproque des deux membre de cette équation fournit
  $$
  \overline{f^{-1}(B)} = f^{-1}(B),
  $$
par conséquent $f^{-1}(B)$ est fermé.

Réciproquement, supposons que l'image réciproque de tout ensemble fermé
est un ensemble fermé. Soit $A$ un sous-ensemble de $X$ ;
l'ensemble $\overline{f(A)}$ étant fermé,
  $$
  \overline{f^{-1}(\overline{f(A)})}
  = 
  f^{-1}(\overline{f(A)}).
  $$
Comme $A \subset f^{-1}(\overline{f(A)})$, on a
$\overline{A} \subset f^{-1}(\overline{f(A)})$, 
donc
  $$
  f(\overline{A}) 
  \subset f(f^{-1}(\overline{f(A)})) 
  \subset \overline{f(A)}.
  $$
Comme $A$ est arbitraire, $f$ est continue.

Montrons la variante avec des ensembles ouverts plutôt que fermés.
Supposons $f$ continue ; si $C$ est un ensemble ouvert de $Y$, 
son complémentaire $B=Y \setminus C$ est un ensemble fermé. Comme
$$
f^{-1}(C) = f^{-1}(Y \setminus B) = X \setminus f^{-1}(B),
$$  
son image réciproque est le complémentaire d'un fermé dans $X$ et donc ouverte.
La réciproque est établie de façon similaire.

Complétude
================================================================================

### Point fixe {.definition}
Soit $f: X \to X$ une application d'un ensemble $X$ dans lui-même.
Un élément $x \in X$ est un *point fixe* de $f$ si $x = f(x)$.
 
### Points fixes et zéros
Être un point fixe d'une fonction $f: X \to X$, c'est donc être déterminé 
**implicitement** par l'équation $x = f(x)$. Si $X$ est un sous-espace
d'un espace vectoriel,
cela équivaut à dire que $x$ est une solution de l'équation $x - f(x) = 0$,
soit un *zéro* (appelé également une *racine*) de la fonction 
$x \in X \mapsto x - f(x)$.

La démarche inverse 
-- qui consiste à caractériser les solutions d'une équation 
comme des point fixes -- peut être utile pour établir des résultats
d'existence et d'unicité de solutions ou obtenir des méthodes numériques 
pour leur calcul. Un exemple élémentaire de ce type de transformation:
le nombre d'or est déterminé comme l'unique solution de l'équation
$$
x^2 = x + 1 , \; x > 0
$$
ou encore comme un zéro de fonction par l'équation
$$
x^2 - x - 1 = 0, \; x > 0;
$$
il peut également être caractérisé comme un point fixe par l'équation
$$
x = 1 + \frac{1}{x}, \; x > 0.
$$
Ce type de transformation n'est toutefois pas unique: un zéro de fonction
peut être caractérisé par une infinité d'équations de type point fixe. 
Parmi cette multitude de choix, il faudra déterminer une reformulation
qui soit utile aux objectifs poursuivis, ce qui n'a rien d'automatique.
On se reportera à l'exercice "[Le nombre d'or](#golden-ratio)" 
pour prolonger l'étude de cet exemple particulier.

![Le nombre d'or comme point fixe de $x \mapsto 1 + 1/x$.](images/fixed-point.tex){#golden-ratio}

### Algorithmes et critères de convergence

Dans un algorithme (idéalisé) de calcul d'une suite de valeurs numériques,
il n'est pas évident d'établir un critère de convergence
qui garantisse exactement que la suite calculée ait une limite,
quand cette limite potentielle est inconnue.

Vérifier que $|x_{k+1} - x_k| \to 0$ par exemple est insuffisant 
pour garantir une limite comme en atteste la suite des $x_k = \sum_{j=0}^k 1 / (j+1).$ 
Vérifier que la série de terme général $|x_{k+1} - x_k|$ est bornée, c'est-à-dire
que
$$
\sum_{k=0}^{+\infty} |x_{k+1} - x_k| < +\infty
$$
va bien garantir la convergence, mais va par contre rejeter des suites convergentes 
telle que $x_k = \sum_{j=0}^{k} (-1)^j / (j+1)$.
Un critère plus adapté serait d'examiner le développement décimal de 
$x_k$ et de vérifier que quel que soit le nombre de décimales souhaité
après la virgule, le développement de $x_k$ finit par se stabiliser au-delà 
d'un certain rang $m$ (qui dépend du nombre de décimales). 
Mais là aussi, il existe des cas pathologiques qui convergent 
sans respecter le critère, comme la suite des $x_k = 1 + (-1)^k 2^{-k}$, 
dont le développement avec 0 décimales  après la virgule 
-- c'est-à-dire la partie entière --
oscille indéfiniment entre $0$ et $1$. 

C'est la notion de suite de Cauchy qui capture le bon critère;
pour une suite numérique (à valeurs réelles ou dans $\R^n$) 
"être de Cauchy" -- ou "passer le test de Cauchy" ou encore 
"vérifier le critère de Cauchy" -- est équivalent à être convergente.

### Suite de Cauchy {.definition}
Une suite de points $x_k$ d'un espace métrique $X$ *est de Cauchy* si pour tout
$\varepsilon > 0$, 
il existe un rang $m$ tel que pour tous les entiers $n \geq m$ et $p \geq m$, 
$d(x_n, x_p) \leq \varepsilon$. 

### Diamètre {.definition}
Le diamètre d'un sous-ensemble $A$ d'un espace métrique $X$ est donné par:
$$
\mbox{diam}(A) = \sup \, \{d(x, y) \, | \, x \in A, \, y \in A\}
$$

### Suite de Cauchy et diamètre {.proposition}
Une suite de points $x_k$ est de Cauchy si et seulement si
$$
\lim_{k \to + \infty} \mbox{diam}(\{x_n \, | \, n \geq k \}) = 0.
$$
  
### Toute suite convergente est de Cauchy
Toute suite de points convergente dans un espace métrique est de Cauchy.

### Démonstration {.proof}
Soit $X$ un espace métrique et $x_k$ une suite convergente, 
de limite $\ell$. Soit $\varepsilon > 0$; il existe un rang
$m$ au-delà duquel on a 
$d(x_k, \ell) \leq \varepsilon / 2.$
Par conséquent, si $n \geq m$ et $p\geq m$, 
$$
d(x_n, x_p) \leq d(x_n, \ell) + d(\ell, x_p) \leq \varepsilon.
$$
La suite $x_k$ est donc de Cauchy.

### Réciproque ?
Il est parfois plus facile de vérifier qu'une suite de points dans un espace
métrique satisfait le critère de Cauchy que de vérifier qu'elle est convergente, 
en particulier quand la limite de la suite est inconnue.
Malheureusement, dans ce cadre très général, il n'est pas possible en général 
de déduire la convergence du fait que la suite vérifie le critère de Cauchy. 
Ainsi, dans $\Q$, considéré en tant que sous-espace métrique de $\R$,
la suite qui définie le développement décimal de $\sqrt{2}$ à l'ordre $k$:
$$
x_k = \frac{a_k}{10^k} \, \mbox{ où } \, a_k = \max \, \{ n \in \N \, | \, n^2 \leq 2(10^k)^2\}
$$
est de Cauchy -- on peut prouver que 
$|x_n - x_p| \leq {1}/{10^m}$ quand $n \geq m$ et $p \geq m$
-- mais n'est pas convergente. 
En effet, la suite converge dans $\R$, mais sa limite $\sqrt{2}$ est 
irrationelle;
cette suite n'a donc pas de limite dans $\Q$ 
(une telle limite serait aussi une limite dans $\R$, 
ce qui contredirait son unicité.)

L'ensemble $\R$ possède une propriété bien utile qui fait défaut à $\Q$:
toute suite de Cauchy y est convergente.

### Espaces complets {.definition}
Un espace métrique $X$ est *complet* si et seulement si toute suite de Cauchy
est convergente. Un espace vectoriel normé $E$ complet est qualifié
d'*espace de Banach[^Banach]*.

[^Banach]: d'après [Stefan Banach](https://en.wikipedia.org/wiki/Stefan_Banach), 
un mathématicien polonais du 20ème siècle d'après lequel sont nommés
[de nombreux concepts et théorèmes](https://en.wikipedia.org/wiki/List_of_things_named_after_Stefan_Banach).

### Complétude de l'espace euclidien {.proposition}

L'espace $\mathbb{R}^n$ est complet.

### Démonstration {.proof}
Dans les cas de $\R$ (c'est-à-dire quand $n=1$), 
le résultat est une conséquence directe de la 
construction de $\R$ comme complété de $\Q$([^ahahah]).
Pour des valeurs de $n > 1$, si $x_k$ est une suite de Cauchy,
ses composantes $x_k^1, \dots, x_k^n$ sont aussi de Cauchy car
pour tout $i \in \{1, \dots, n\}$,
$$
|x_n^i - x_p^i| \leq \left\|x_n - x_p\right\|.
$$
Comme $\mathbb{R}$ est complet, chaque suite $x_k^i$ admet donc une limite,
notée $\ell^i$. 
Si l'on note $\ell = (\ell^1, \dots, \ell^n)$,
on déduit de l'égalité
$$
\|x_k - \ell\| = \sqrt{\sum_{i=1}^n (x_k^i - \ell^i)^2}
$$
la convergence de $x_k$ vers $\ell$. 
Toute suite de Cauchy de $\R^n$ est donc convergente.

[^ahahah]: bien sûr si l'on a utilisé une technique alternative pour
construire $\R$, par exemple par les coupures de Dedekind, 
la complétude de $\R$ n'a rien d'automatique.

### Complétude de l'espace des fonctions bornées {.proposition}
Soit $X$ un ensemble et $Y$ un espace métrique complet.
L'ensemble des fonctions $f$ de $X$ dans $Y$ bornées
-- c'est-à-dire telles que $\sup_{x \in X} d(0, f(x))$ soit fini --
muni de la distance de la convergence uniforme
$$
d(f, g) := \sup_{x \in X} d(f(x), g(x))
$$
est complet.

### Démonstration {.proof}
Soit $f_k$ une suite de Cauchy de fonctions bornées pour la distance
de la convergence uniforme. 
Pour tout $\varepsilon > 0$, il existe un rang $m \in \N$ tel que si 
$n\geq m$ et $p\geq m$, on ait
$$
\sup_{x \in X} d(f_n(x), f_p(x)) \leq \varepsilon.
$$
Par conséquent, pour tout $x \in X$, 
on a $d(f_n(x), f_p(x)) \leq \varepsilon$, donc
la suite des $f_k(x)$ est de Cauchy dans $Y$. 
L'espace $Y$ étant par hypothèse complet, cette suite a une limite,
que nous notons $f_{\infty}(x)$. Par continuité de la distance, 
pour tout $x \in X$ et tout $n \geq m$, on a
$$
d(f_n(x), f_{\infty}(x)) 
= \lim_{p \to +\infty} d(f_n(x), f_p(x)) 
\leq \varepsilon
$$
et donc
$\sup_{x \in X} d(f_n(x), f_{\infty}(x)) \leq \varepsilon$. 
La fonction $f_{\infty}$ est donc bornée, car
$$
d(0, f_{\infty}(x)) \leq d(0, f_n(x)) + \varepsilon,
$$
et la limite uniforme de la suite des $f_k$.

### Application contractante {.definition}
Soit $X$ un espace métrique.
Une fonction $f: X \to X$ est *$\kappa$-contractante*, 
où $\kappa \in \left[0, 1\right[$,
si pour tout couple de points $x$ et $y$ de $X$, on a 
$$
d(f(x), f(y)) \leq \kappa d(x, y).
$$
Une telle application est *contractante* si elle est 
$\kappa$-contractante pour un $\kappa \in \left[0, 1\right[$.

### Théorème de point fixe de Banach {.definition .theorem #T-TPFB}

Soit $f: X \to X$ une application contractante dans un espace métrique $X$ complet.
L'application $f$ admet un unique *point fixe* $x$,
c'est-à-dire une unique solution $x \in X$ à l'équation
  $$
  x = f(x).
  $$

### Démonstration {.proof}

L'unicité du point fixe (l'existence d'au plus une solution à $x=f(x)$) est
simple à établir: si $x$ et $y$ sont deux points fixes de $f$, c'est-à-dire 
si $x=f(x)$ et $y=f(y)$, alors $d(x, y) = d(f(x), f(y))$. 
L'application $f$ étant $\kappa$-contractante, on a donc
$$
d(x, y) = d(f(x), f(y)) \leq \kappa d(x, y);
$$
et puisque $0\leq \kappa < 1$, cette inégalité entraîne $d(x , y) = 0$, 
soit $x=y$.

Quant à l'existence du point fixe, sa preuve est constructive: 
nous allons établir que quel que soit le choix de $x_0 \in E$, 
la suite de valeurs définie par
$$
x_{n+1} = f(x_n)
$$
converge vers un point fixe. 
Le point crucial est d'établir que cette suite
admet une limite $\ell$ ; en effet, si ce résultat est acquis, 
en passant à la limite sur $n$ dans la relation de récurrence
et exploitant la continuité de l'application $f$, on obtient
$$
\ell = \lim_{n \to +\infty} x_{n+1} = \lim_{n \to +\infty}f(x_n) = f(\ell).
$$
À cette fin, nous allons prouver que la suite des $x_n$ est de Cauchy; 
l'existence d'une limite se déduira alors de la complétude de $X$. 
On remarque tout d'abord que pour tout entier $n$, 
$$
d(x_{n+2}, x_{n+1}) = d(f(x_{n+1}), f(x_n)) \leq \kappa d(x_{n+1}, x_n),
$$
ce qui par récurrence fournit pour tout $n$
$$
d(x_{n+1}, x_n) \leq \kappa^n d(x_1, x_0).
$$
Par [l'inégalité triangulaire](#dist-ineg), 
pour tout couple d'entiers $n$ et $p$, on a
$$
d(x_{n+p} , x_n) 
\leq \sum_{k=0}^{p-1} d(x_{n+k+1} , x_{n+k})
\leq \sum_{k=0}^{p-1} \kappa^{n+k} d(x_{1}, x_{0}).
$$
Dans le second membre apparaît une somme de termes d'une suite géométrique:
$$
\sum_{k=0}^{p-1} \kappa^{n+k} = \kappa^n \frac{1 - \kappa^{p}}{1 - \kappa}
\leq \frac{\kappa^n}{1 - \kappa};
$$
on en déduit
$$
d(x_{n+p}, x_n) 
\leq  
\frac{\kappa^n}{1 - \kappa} d(x_{1}, x_{0}).
$$
Le second membre de cette inégalité tend vers $0$ indépendamment de $p$
quand $n$ tend vers $+\infty$; la suite des $x_n$ est bien de Cauchy.

Compacité
================================================================================

### Compacité séquentielle {.definition}
Un ensemble $K$ d'un espace métrique est *compact (séquentiellement)* 
si toute suite de valeurs de $K$ admet une sous-suite qui converge dans $K$.

### Théorème de Heine-Borel {.theorem}
Un ensemble $K$ de l'espace euclidien $\R^n$ est compact 
si et seulement si il est fermé et borné.

### Démonstration {.proof}
Supposons $K$ compact; soit $x_k$ une suite de points de
$K$ qui converge dans $\R^n$, vers une limite notée $\ell$. 
Il existe alors une sous-suite $y_k$ de $x_k$ qui converge dans $K$;
or comme cette sous-suite a la même limite que $x_k$, $\ell$ 
appartient à $K$. L'ensemble $K$ est donc fermé.

Si $K$ est non-borné, il existe une suite $x_k$ non-bornée de points de $K$.
Toute sous-suite de $x_k$ étant également non-bornée, elle ne peut donc converger
et par conséquent $K$ ne peut pas être compact.

Finalement, supposons $K$ fermé et borné. Soit $x_k$ une suite de valeurs
de $K$.
Tout ensemble borné peut être recouvert par un nombre finis d'ensembles 
fermés et bornés de diamètre arbitrairement faible[^cover]. Si l'on 
considère un recouvrement de ce type de $K$ pour un diamètre inférieur
à 1, il existe nécessairement un ensemble du recouvrement qui contient
l'intégralité d'une sous-suite $x^0_k$ de $x_k$; on le note $K_0$.
Il est possible de réitérer le raisonnement à la suite des $x^0_k$ dans $K^0$
en imposant cette fois-ci un diamètre maximale de $1/2$ aux
élements du recouvrement et plus généralement de construire une suite 
$y_k$ extraite de $x_k$ telle que $y_k \in K_m$ si $k\geq m$ et 
$\mathrm{diam}(K_m) \leq 2^{-m}$. 
La suite des $y_k$ est donc de Cauchy; l'espace euclidien $\R^n$ étant
complet, elle est convergente. L'ensemble $K$ étant
fermé par hypothèse, cette limite appartient à $K$ ; 
l'ensemble $K$ est donc compact.

[^cover]: par exemple des pavés de la forme 
$$[i_1 \varepsilon, (i_1+1)\varepsilon] \times \dots \times [i_n \varepsilon, (i_{n}+1) \varepsilon]
\, \mbox{ où } \, (i_1,\dots, i_n) \in \Z^n,$$
dont le diamètre est $\varepsilon \sqrt{n}$.

### Image d'un compact {.theorem}
L'image d'un ensemble compact par une application continue est un ensemble
compact.

### Démonstration {.proof}

Soit $f: K \subset X \to Y$ où $X$ et $Y$ sont deux espaces métriques 
et $K$ un sous-ensemble compact de $X$. 
Soit $y_k$ une suite de points de $f(K)$ ; par construction, 
il existe une suite de points $x_k$ de $K$ tels que $f(x_k) = y_k$. 
Soit $z_k$ une sous-suite de $x_k$ qui converge vers un $\ell \in K$; 
par continuité de $f$ en $\ell$, la suite des $f(z_k)$
-- qui est une suite extraite des $y_k$ -- 
converge vers $f(\ell) \in f(K)$. 
L'ensemble $f(K)$ est donc compact.

### Existence d'un minimum / maximum {.corollary #T-EM}
Une fonction continue $f: K \to \mathbb{R}$ définie sur un ensemble compact 
$K$ admet un minimum global et un maximum global.

### Démonstration {.proof}
Soit $x_k \in K$ une suite minimisante de $f$, c'est-à-dire telle que
$$
\lim_{k \to +\infty} f(x_k) = \inf_{x \in K} f(x).
$$
Il existe une suite $y_k$ extraite de $x_k$ qui converge vers un point
$\ell$ de $K$. Par continuité de $f$ en $\ell$, on a
$$
f(\ell) = \lim_{k \to +\infty} f(y_k) = \inf_{x \in K} f(x).
$$
La fonction $f$ admet donc un minimum en $\ell$.
En appliquant ce résultat à la fonction $-f$, 
on établit que $f$ admet un maximum.


### Complétude de l'espace des fonctions continues {.proposition}
Soit $X$ un espace métrique compact et $Y$ un espace métrique complet.
L'ensemble des fonctions continues de $X$ dans $Y$
muni de la distance de la convergence uniforme
$$
d(f, g) := \sup_{x \in X} d(f(x), g(x))
$$
est complet.

### Démonstration {.proof}
En préambule: pour toute fonction $f$ continue de $X$ dans $Y$,
la fonction $$x \in X \mapsto d(f(x), 0) \in \R,$$ 
continue et définie sur un compact, [admet un maximum](#T-EM); 
la fonction $f$ est donc bornée.
L'espace des fonction continues de $X$ dans $Y$ est donc un
sous-espace métrique de l'espace des fonctions bornées de $X$ dans $Y$.

Soit $f_k$ une suite de Cauchy de fonctions continues de $X$ dans $Y$.
Cette suite est convergente dans l'espace des fonctions bornées en raison
de la complétude de ce dernier. Il nous suffit de montrer que sa limite
(uniforme) est continue pour conclure la preuve. 

Soit $f$ la limite des $f_k$ et soit $\varepsilon > 0$.
Soit $k$ tel que $$\sup_{x \in X}(f_k(x), f(x)) \leq \varepsilon /3.$$
Pour tout $x \in X$, $f_k$ étant continue en $x$, pour $y$ assez proche
de $x$ on a $d(f_k(x), f_k(y)) \leq \varepsilon /3.$ 
Or, par l'inégalité triangulaire,
$$
d(f(x), f(y)) \leq d(f(x), f_k(x))  + d(f_k(x), f_k(y)) + d(f_k(y), f(y))
\leq \varepsilon.
$$
La fonction $f$ est donc continue.

### {.ante}
La notion de compacité peut également être définie dans des espaces topologiques
généraux, sans recourir à une distance ou aux suites de points.

### Propriété de l'intersection finie {.definition}
Une collection d'ensembles vérifie la propriété de l'intersection 
finie si toute sous-collection finie est d'intersection non vide.

### Compacité et propriété de l'intersection finie {.definition}
Un ensemble $K$ d'un espace topologique est *compact* si pour toute collection
de sous-ensembles de $K$ vérifiant la propriété de l'intersection finie, 
il existe un point adhérent à tous les ensembles de la collection.

Autrement dit, si pour tout $A \in \mathcal{A}$, $A$ est un sous-ensemble de
$K$ et si pour toute suite finie $A_1, \dots, A_k \in \mathcal{A}$ 
il existe un $x \in K$ tel que $x \in A_1\cap \dots \cap A_k$, 
alors il existe un $x \in K$ adhérent à tout $A \in \mathcal{A}$.

### Compacité et compacité séquentielle
Dans les espaces métriques, compacité et compacité séquentielle sont 
équivalentes.

### Démonstration {.proof}
Supposons que $K$ est un sous-ensemble compact de l'espace métrique $X$.
Soit $x_k$ une suite de points de $K$. Considerons la collection d'ensembles
$\mathcal{A}$ définie par
$$
\mathcal{A} = \{A_k \, | \, k \in \mathbb{N} \}
\; \mbox{ où } \; A_k = \{x_j \,| \, j \geq k \}.
$$
La collection $\mathcal{A}$ vérifie la propriété d'intersection finie: 
en effet, si $A_{k_1}$, $A_{k_2}$, $\dots$, $A_{k_p} \in \mathcal{A}$, alors
$$
A_{k_1} \cap A_{k_2} \cap \dots \cap A_{k_p} = A_{k} 
\; \mbox{ avec } \; k = \max(k_1, \dots, k_p)
$$
et donc leur intersection est non-vide. 
Par conséquent, il existe un $x \in K$ tel que pour tout rang $k$,
$x$ adhère à $A_k = \{x_j \,| \, j \geq k \}$, c'est-à-dire 
$d(x, \{x_j \,| \, j \geq k \}) = 0$. En particulier, il existe un
$y_0 := x_{k_0} \in A_0$ tel que $d(x, y_0) \leq 2^{-0}$, 
un $y_1 := x_{k_1} \in A_{k_0+1}$ tel que $d(x, y_1) \leq 2^{-1}$, etc.
La suite $y_k$ est extraite de $x_k$ et vérifie $d(x, y_k) \leq 2^{-k}$,
elle converge donc vers $x$. De toute suite de points de $K$ on peut donc
extraire une sous-suite qui converge dans $K$: $K$ est donc séquentiellement
compact.

Réciproquement, supposons $K$ séquentiellement compact.
Nous allons montrer que si $\mathcal{A}$ est une collection d'ensembles
de $K$ telle que 
$$
\bigcap_{A \in \mathcal{A}} \, \overline{A} = \varnothing,
$$
où $\overline{A}$ désigne l'adhérence de $A$ dans $K$, 
alors il existe un nombre fini d'ensemble de $\mathcal{A}$ 
dont l'intersection est vide ; nous aurons alors établi la contraposée
de la propriété qui définit la compacité de $K$ et donc la compacité de $K$. 
Au préalable, nous allons montrer que sous l'hypothèse ci-dessus d'intersection
vide des adhérences, il existe un $\varepsilon > 0$ tel
que pour tout $x\in K$, on peut trouver un $A \in \mathcal{A}$ tel que
$B(x, \varepsilon) \cap \overline{A} = \varnothing$. 
En effet, si cette propriété n'était pas vérifiée, on pourrait construire
une suite $x_k$ de points de $K$ telle que pour tout $A \in \mathcal{A}$,
il existe un $a^A_k \in \overline{A}$ tel que $d(x_k, a^A_k) < 2^{-k}$.
Mais une telle suite aurait alors une sous-suite convergente;
la limite serait dans l'adhérence de chacun des
$A \in \mathcal{A}$, en contradiction avec l'hypothèse initiale.
On utilise ce résultat de la façon suivante: 
on sélectionne un $x_0 \in K$ et un $A_0 \in \mathcal{A}$ 
tel que $\overline{A_0} \cap B(x_0, \varepsilon) = \varnothing$, 
puis un $x_1 \in K \setminus B(x_0, \varepsilon)$ et un
$A_1 \in \mathcal{A}$ tel que $\overline{A_1} \cap B(x_1, \varepsilon) = \varnothing$, 
ce qui induit
$$
(\overline{A_0} \cap \overline{A_1}) \cap (B(x_0, \varepsilon) \cup B(x_1, \varepsilon)) = \varnothing,
$$
puis un $x_2 \in K \setminus (B(x_0, \varepsilon) \cup B(x_1, \varepsilon))$
et un $A_2 \in \mathcal{A}$ tel que 
$\overline{A_2} \cap B(x_2, \varepsilon) = \varnothing$, etc.
Le procédé s'arrête en un nombre fini d'étapes, dès que
$B(x_0,\varepsilon) \cup \dots \cup B(x_k, \varepsilon)$ recouvre $K$.
Cela arrive nécessairement puisque les $x_k$ ainsi construits
vérifient $d(x_i, x_j) \geq \varepsilon$ si $i\neq j$; si cette suite
était infinie, elle ne pourrait admettre de suite extraite convergente,
en contradiction avec l'hypothèse de compacité séquentielle.
Par conséquent, il existe un rang $k$ tel que 
$$
K \subset B(x_0,\varepsilon) \cup \dots \cup B(x_k, \varepsilon)
$$
et comme 
$$
(\overline{A_0} \cap \dots \cap \overline{A_k}) 
\cap (B(x_0, \varepsilon) \cup \dots \cup B(x_k, \varepsilon)) = \varnothing,
$$
on en déduit que 
$\overline{A_0} \cap \dots \cap \overline{A_k} = \varnothing$
et donc que
$A_0 \cap \dots \cap A_k = \varnothing$, ce qui conclut la preuve.

<!--

### Compacité et recouvrement ouvert {.proposition}
Un ensemble $K$ d'un espace topologique est compact si pour tout
recouvrement de $K$ par une collection d'ouverts, on peut extraire un
sous-recouvrement fini.

Autrement dit, si $\mathcal{O}$ est composé d'ouverts $O$ de $X$ tels que
$$K \subset \bigcup \, \{O \, | \,  O \in \mathcal{O}\},$$ 
alors il existe une collection
finie $O_1, \dots, O_k$ de $\mathcal{O}$ telle que 
$$K \subset O_1 \cup \dots \cup O_k.$$

### TODO -- Démonstration {.proof}

-->

<!--
TODO -- Et $\C$ alors ?
--------------------------------------------------------------------------------

TODO -- Structures Euclidiennes & Hermitiennes
--------------------------------------------------------------------------------

### Produit scalaire {.definition}
Un *produit scalaire* sur un espace vectoriel $E$ est une application
$$\left< \cdot , \cdot \right>: E \times E \to \mathbb{R}$$
qui est

  - Bilinéaire symmétrique: pour tous $\lambda \in \mathbb{R}$ et $x, y, z \in E$:
    
      - $\left<x, y\right> = \left<y, x\right>$,

      - $\left<x, \lambda y\right> = \lambda \left<x, y\right>$

      - $\left<x, y + z\right> = \left<x, y\right> + \left<x, z\right>$.


  - Définie positive: pour tout $x \in E$, 
  
    - $\left<x, x \right> \geq 0$,

    - $\left<x, x \right> = 0$ si et seulement si $x=0$.

### TODO

Mq produit scalaire définit une norme.


### TODO

Hors cas euclidien, exemple de produit scalaire ? Trop tôt ? 
(pas les structures adaptées)

### L'espace euclidien $\mathbb{R}^n$ {.remark}
L'ensemble $\mathbb{R}^n$ est un espace vectoriel de dimension finie
qui muni du produit scalaire
$$
\left<x,y\right> = x_1 y_1 + \dots + x_n y_n
$$
devient un *espace euclidien*; la norme associée vérifie
$$
\|x\| = \sqrt{x_1^2 +\dots + x_n^2}.
$$

-->

Exercices
================================================================================

Normes d'opérateurs {#no .question}
--------------------------------------------------------------------------------

[La fonction `norm` du module `numpy.linalg`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.norm.html#numpy-linalg-norm) peut calculer des normes de vecteurs 
de $\R^n$, mais également de matrices carrée de $\R^{n\times n}$. 
Ainsi, on a par exemple:

    >>> from numpy import inf
    >>> from numpy.linalg import norm
    >>> A = [[1.0, 2.0], [3.0, 4.0]]
    >>> norm(A)
    5.477225575051661
    >>> norm(A, 1)
    6.0
    >>> norm(A, 2)
    5.464985704219043
    >>> norm(A, inf)
    7.0

En étudiant [la documentation de cette fonction]((https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.norm.html#numpy-linalg-norm)), déterminer pour les quatres exemples
d'usage ci-dessus s'il existe une norme $\|\cdot\|_?$ de vecteurs de $\R^n$ dont 
la norme d'opérateur associée correspond à cette norme de matrice, 
c'est-à-dire telle que
$$
\|A\| = \sup_{x \neq 0} \frac{\|A\cdot x\|_?}{\|x\|_?}.
$$

Droite réelle achevée {#dra}
--------------------------------------------------------------------------------

La *droite réelle achevée* (ou *droite réelle étendue*) 
est composée des nombres réels et de $-\infty$ et $+\infty$.
Le but de cet exercice est de doter cet ensemble 
$[-\infty, +\infty]$([^nre]) d'une distance aux propriétés
"raisonnables".
A cette fin, on introduit l'espace métrique $X$ des points du cercle unité de 
$\mathbb{R}^2$ d'ordonnée positive:
$$
X = 
\left\{
(x, y) \in \mathbb{R}^2 \, \left| \, \sqrt{x^2+y^2} = 1 \right. \mbox{ et } y \geq 0
\right\},
$$
muni de la distance euclidienne de $\mathbb{R}^2$
et la fonction $f: X \to [-\infty, +\infty]$ définie par
$$
f(x,y) = 
\left|
\begin{array}{rl}
- \infty & \mbox{si } (x, y)=(-1, 0), \\
x/y & \mbox{si } y > 0, \\
+ \infty & \mbox{si } (x, y)=(1, 0). \\
\end{array}
\right.
$$

[^nre]: **Pilule rouge.** Dans le monde réel,
on trouvera fréquemment la notation $\overline{\R}$ 
pour désigner l'ensemble des réels étendus; 
mais cette convention se heurte alors avec la désignation de l'adhérence
de $\mathbb{R}$ dans lui-même, une interprétation selon laquelle 
on aurait $\overline{\mathbb{R}} = \mathbb{R}$. 

### Question 1 {.question #dra-1}
Pouvez-vous donner une interprétation géométrique simple à la grandeur
calculée par la fonction $f$ ?

![Construction d'une métrique pour la droite réelle achevée.](images/extended-real-numbers.tex)

### Question 2 {.question #dra-2}
Montrer que $f$ est une bijection.

### Question 3 {.question #dra-3}
En déduire qu'il existe une et une seule fonction distance sur
$[-\infty, +\infty]$ qui fasse de $f$ une isométrie;
on note $d^{\pm \infty}$ cette distance. 

### Question 4 {.question #dra-4}
Calculer $d^{\pm \infty}(0, +\infty)$, $d^{\pm \infty}(-\infty, +\infty)$, 
$d^{\pm \infty}(-1, 1)$.

### Question 5 {.question #dra-5}
Montrer que l'injection canonique
$x \in \mathbb{R} \mapsto x \in [-\infty, +\infty]$
est une fonction continue.

### Question 6 {.question #dra-6}
Yoda a dit "deux façons d'interpréter $x_k \to +\infty$ désormais il y a".
Qu'est-ce qu'il a voulu dire ? Est-ce que c'est un problème ?

### Question 7 {.question #dra-7}
Suggérer une variante de la construction précédente pour
doter l'ensemble $\mathbb{R} \cup \{\infty\}$ ($\infty$ sans signe:
ni $+$, ni $-$) d'une métrique $d^{\infty}$ 
telle $|x_k| \to +\infty$ si et seulement si 
$d^{\infty}(x_k, \infty) \to 0$. 
En déduire que cet ensemble est compact.
    
Localement fermé
--------------------------------------------------------------------------------

### {.definition}
Dans un espace métrique[^ext] $X$, un ensemble $A$ est *localement fermé* si 
chaque point de $A$ a un voisinage ouvert $V$ tel que $A \cap V$ soit fermé 
dans $V$ [@Sat59].

[^ext]: ou plus généralement dans un espace topologique.

### Question 0 {.question #lf-0}
Expliquer l'expression "fermé dans $V$" dans la définition ci-dessus; 
est-ce que cela fait une différence si l'on remplace cette expression
par "fermé" ? 

### Question 1 {.question #lf-1}
Montrer que dans $\R$, l'intervalle $\left[0, 1\right[$ est localement 
fermé et que l'image de toute suite convergente est localement fermée. 
Donner un exemple de sous-ensemble de $\mathbb{R}$ qui ne soit pas 
localement fermé.

### Question 2 {.question #lf-2} 
Montrer que tout ensemble fermé est localement fermé, mais aussi que tout
ensemble ouvert est localement fermé. 
Montrer que l'intersection de deux ensembles localement fermés est 
localement fermé.

### Question 3 {.question #lf-3}
Montrer qu'un ensemble est localement fermé si et seulement s'il est
l'intersection d'un ensemble fermé et d'un ensemble ouvert.

<!--
TODO -- Comparaison des normes
--------------------------------------------------------------------------------

TODO: comparaison manuelle, meilleure bornes
-->

Distance entre ensembles
--------------------------------------------------------------------------------

Soit $A$ et $B$ deux ensembles compacts non vides de $\mathbb{R}^n$ ; 
on souhaite évaluer à quel point les deux ensembles diffèrent
-- en mesurant à quelle distance les points de $A$ peuvent 
être éloignés de l'ensemble $B$ et réciproquement.

### Question 1 {.question #dh-1}
Est-ce que la distance entre ensembles classique
$$
d(A, B) = \inf_{a \in A} d(a, B) = \inf_{a\in A}\inf_{b \in B} d(a, b)
$$
fait l'affaire ?

### {.definition}
On définit la grandeur
  $$
  d[A, B] = \max \left\{ \sup_{a \in A} d(a, B), \, \sup_{b \in B} d(b, A) \right\}.
  $$
appelée *distance de Hausdorff* entre $A$ et $B$.

### Question 2 {.question #dh-2}
Calculer $d[A, B]$ lorsque $A = [-1,1] \times [-1, 1]$ et
$B = [0, 2] \times [0,2]$.

![Ensembles $A = [-1,1] \times [-1, 1]$ et $B = [0, 2] \times [0,2]$.](images/hausdorff.tex){#A-et-B}

### Question 3 {.question #dh-3}
Cette terminologie de "distance" de Hausdorff est-elle légitime ?

### Question 4 {.question #dh-4}
La somme de Minkowksi de deux ensembles $A$ et $B$ est définie comme
$$
A + B = \{a + b \, | \, a \in A, \, b \in B \}.
$$
Vérifier que la somme de Minkowski de deux ensembles compacts non vides de 
$\R^n$ est un ensemble compact non vide de $\R^n$.
Cette opération est-elle continue pour la distance de Hausdorff ?

Plongement de Kuratowski
--------------------------------------------------------------------------------

Nous souhaitons établir le résulat suivant: tout espace métrique peut être
identifié à un sous-ensemble d'un espace vectoriel normé
d'une façon qui préserve la distance entre points.

Soit $X$ un espace métrique et $x_0$ un point de $X$. 
On associe à l'élément $x$ de $X$ la fonction $f_x: X \to \R$ définie
par
$$
f_x(y) = d(x, y) - d(x_0, y).
$$

### Question 1 {#pk-1 .question}
Montrer que la fonction $x \mapsto f_x$ est injective.

### Question 2 {#pk-2 .question}
Montrer que pour tout point $x$ la fonction $f_x$ est bornée.

### Question 3 {#pk-3 .question}
Montrer que l'espace vectoriel $E$ des fonctions bornées de $X$ dans 
$\mathbb{R}$ est un espace vectoriel qui peut être muni de la norme 
$\| \cdot \|_{\infty}$ définie par
$$
\|f\|_{\infty} = \sup \, \{|f(y)| \, | \, y \in X\}.
$$

### Question 4 {#pk-4 .question}
Montrer que $x \mapsto f_x$ est une isométrie, 
c'est-à-dire que pour tout $x$ et $y$ dans $X$, on a 
$$
d(x, y) = \|f_x - f_y\|_{\infty}.
$$

<!--
Limite approchée {.question #approximate-limit}
--------------------------------------------------------------------------------

Soit $x_k$ une suite de points dans un espace métrique $X$. On dit que 
$\ell \in X$ est une *limite approchée de la suite $x_k$ à la précision
$\varepsilon > 0$* s'il existe un seuil $n \in \N$ tel que pour tout
$k \geq m$, on ait $d(x_k, \ell) \leq \varepsilon$.

Comment désigner une suite qui admet pour tout $\varepsilon$ 
une limite approchée $\ell$ (qui peut dépendre de $\varepsilon$) ?

-->


Le nombre d'or {#golden-ratio}
--------------------------------------------------------------------------------

Le but de cet exercice est de montrer l'existence d'un unique réel 
positif $x$ tel que $x^2 = x + 1$ -- le *nombre d'or* --
et de produire une méthode itérative pour l'évaluer.

### Question 1 {.question #golden-ratio-1}
Montrer l'existence d'un unique point fixe associé à l'application
$$
x \in \left]0, +\infty\right[ \mapsto 1 + \frac{1}{x}
$$
et établir qu'il se situe dans l'intervalle fermé $[4/3, 2]$.

### Question 2 {.question #golden-ratio-2}
Montrer que la suite de réels définie par $x_0 \in [4/3, 2]$
et $x_{n+1} = f(x_n)$ converge vers le nombre d'or.
 
### Question 3 {.question #golden-ratio-3}
Etudier la fonction $f \circ f$ et en exploitant le résultat de 
l'exercice ["Point fixe"](#TPFB2), en déduire que la suite des $x_n$
converge vers le nombre d'or pour toute valeur initial $x_0$ strictement
positive.

Spirale d'Euler 
--------------------------------------------------------------------------------

La spirale d'Euler est la courbe paramétrée du plan déterminée 
pour $t\geq 0$ par les coordonnées
$$
x(t) = \int_0^t \cos s^2 \, ds \, \mbox{ et } \, \, y(t) = \int_0^t \sin s^2 \, ds
$$

![Spirale d'Euler ($0 \leq t \leq 5$)](images/euler.py)

Nous souhaitons établir que cette spirale à un point limite quand 
$t \to +\infty$([^euler]).

### Question 1 {.question #se-1}
Montrer que si pour toute suite de valeurs $t_k$ tendant vers l'infini, 
la suite de points de coordonnées $(x_k, y_k) := (x(t_k), y(t_k))$ 
a une limite dans le plan
-- limite qui peut dépendre a priori de la suite $t_k$ -- 
alors le point de coordonnées $(x(t), y(t))$ a une limite dans le plan 
quand $t$ tend vers $+\infty$.

### Question 2 {.question #se-2}
Montrer que pour tout couple $(a,b)$ de réels tels que $0 < a \leq b$,
les grandeurs
$$
I(a, b) :=
\int_{a}^{b} \cos s^2 \, ds
\mbox{ et }
J(a, b) := \int_{a}^{b} \sin s^2 \, ds
$$
vérifient pour un réel $\alpha > 0$ les inégalités
$$
|I(a, b)| \leq \frac{\alpha}{\sqrt{a}}
\, \mbox{ et } \,
|J(a, b)| \leq \frac{\alpha}{\sqrt{a}}.
$$

### Question 3 {.question #se-3}
Conclure.

[^euler]: cette courbe a été introduite par Euler en 1744. 
Il lui apparait alors manifeste que la courbe est une spirale qui s'enroule 
après un nombre de tours infinis autour d'un centre bien défini, 
mais que ce point est très difficile à déterminer par cette construction. 
Il faudra attendre 1781 pour
qu'Euler puisse calculer analytiquement les coordonnées de ce point 
(cf. @Lev08).

Point fixe {#TPFB2}
--------------------------------------------------------------------------------

<!--
**TODO:** exemple introductif (simple, matriciel $2\times2$)
-->

On souhaite montrer que si $X$ est un espace métrique complet et 
qu'il existe un entier $n \geq 1$ tel que la composée 
$n$ fois d'une application $f: X \to X$ avec elle-même 
-- notée $f^n$ -- est contractante,
alors la conclusion du [théorème de point fixe de Banach](#T-TPFB)
est toujours valable (bien que les hypothèses considérées ici 
soient plus générales).

### Question 1 {.question #pf-1}
Soit $X$ un ensemble et $f: X \to X$.
Montrer que tout point fixe de $f$ est également 
un point fixe de $f^n$ ; montrer que si $f^n$ admet un unique point fixe,
il est également l'unique point fixe de $f$.

### Question 2 {.question #pf-2}
On suppose désormais que $X$ est un espace métrique complet et que 
$f^n$ est contractante.
Montrer que $f$ admet un unique point fixe et que le procédé habituel 
pour calculer ce point fixe comme une limite est toujours valable.

<!--

TODO -- Normes d'opérateurs
--------------------------------------------------------------------------------

Changer les normes au départ et à l'arrivée, calculer les normes d'opérateurs
associées sur la base d'une représentation matricielle (ex: norme sup au 
départ et à l'arrivée)

En lien avec les résolutions itératives de systèmes linéaires,
utiliser / montrer que pour tout $A \in \R^{n\times n}$
et tout $\varepsilon > 0$, il existe une norme matricielle 
$\|\, \cdot \, \|$ telle que $\|A\| \leq \rho(A) + \varepsilon$.

Voir aussi <https://math.stackexchange.com/questions/126460/iteration-convergence>

TODO -- Fonctions définies par un recouvrement
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
     la collection $\mathcal{A}$ peut-on ajouter pour s'assurer du résultat ?

  2. Application angle sur l'hélice et $\arctan$ ...

-->

Résolution itérative de systèmes linéaires
--------------------------------------------------------------------------------
Un opérateur linéaire $A: \R^n \to \R^n$ est *diagonalement dominant* 
si la matrice $[a_{ij}]_{ij} \in \R^{n\times n}$ associée vérifie
pour tout $i \in \{1,\dots, n\}$,
$$
\sum_{\substack{j=1\\j\neq i}}^n |a_{ij}| < |a_{ii}|.
$$
Soit $D$ l'opérateur dont la matrice $[d_{ij}]_{ij}$ est la diagonale de 
$[a_{ij}]_{ij}$:
$$
[d_{ij}]_{ij} = \left[
\begin{array}{cccc}
a_{11} & 0 & \cdots & 0 \\
0 & a_{22} & \cdots & 0 \\
\cdots & \cdots & \cdots & \cdots \\
0 & \cdots & 0 & a_{nn} \\
\end{array}
\right]
$$

### Question 1 {.question #risl-1}
Montrer que deux vecteurs $x$ et $y$ de $\R^n$ vérifient 
$A \cdot x = y$ si et seulement si 
$$x = D^{-1} \cdot (D-A) \cdot x  + D^{-1} \cdot y.$$

### Question 2 {.question #risl-2}
En déduire que $A$ est inversible et une méthode itérative de calcul de $A^{-1}$.

<!--
Préparer et résoudre numériquement des systèmes de la forme $A x = b$ dans
des cas simples (ex: Jacobi, Gauss-Seidel, cas diagonally dominant ?).

Exemples concrets (ex: Poisson Image editing) et exemples ou "ça ne marche pas"
en itérant sans s'assurer du caractère contractant. 

Prendre un exemple de petite dimension associé au PIE; admettre le résultat
que $\|A^k\| \to 0 \Leftrightarrow \rho(A) < 1$ et tester algo de Jacobi
(Au préalable, calculer norme de l'opérateur via la svd ?).

Lien norme d'opérateur et rayon spectral ??? Cf supra sur rayon spectral
et lien avec norme.
-->

Équation différentielle
--------------------------------------------------------------------------------
Soit $A$ un opérateur linéaire de $\R^n$ dans $\R^n$. 
On souhaite montrer que pour tout $x_0 \in \R^n$,
il existe une unique fonction dérivable $x: \left[0, +\infty\right[ \to \R^n$
à l'équation différentielle
$$
\dot{x}(t) = A \cdot x(t) \mbox{ pour tout } t \geq 0,
$$
assortie de la condition initiale $x(0) = x_0$. 

### Question 1 {.question #ed-1}
Montrer que la fonction $x: \left[0, +\infty\right[ \to \R^n$ est solution du 
problème ci-dessus si et seulement si elle est continue et vérifie 
pour tout $t \geq 0$ la relation
$$
x(t) = x_0 + \int_0^t A \cdot x(s) \, ds.
$$

### Question 2 {.question #ed-2}
Soit $T > 0$ ; 
on note $E$ l'espace des fonctions continues de $[0, T]$ dans $\R^n$, 
muni de la norme
$$
\|x\|_{\infty} = \sup_{t \in [0, T]} \|x(t)\|.
$$
A quelle condition simple
l'application $\Phi: E \to E$ définie par
$$
\Phi(x) = \left(t \mapsto x_0 +  \int_0^t A \cdot x(s) \, ds\right)
$$
est-elle contractante ? Quelle conclusion (partielle) quant
au problème initial peut-on en tirer ?

### Question 3 {.question #ed-3}
Soit $\alpha > 0$. On note 
$$
\|x\|_{\infty}^{\alpha} = \sup_{t \in [0, T]} \|e^{-\alpha t}x(t)\|.
$$
Montrer que $\|\cdot\|_{\infty}^{\alpha}$ est une norme sur l'espace
des fonctions continues de $[0, T]$ dans $\R^n$ et que 
muni de cette norme, l'espace $E$ est complet.

### Question 4 {.question #ed-4}
Reprendre la question 2 avec la norme $\|\cdot\|_{\infty}^{\alpha}$
au lieu de $\|\cdot\|_{\infty}$ et conclure quant à l'existence
d'une solution au problème initial.

Localement borné
--------------------------------------------------------------------------------
Soit $f: U \subset \R^n \to \R$ où $U$ est ouvert.
Cette application est dite
*localement bornée* si pour tout point $x \in U$, on peut trouver un
rayon $r>0$ et une borne $M\geq 0$ tels que pour tout point 
$y \in U$ tel que $\|y - x\| \leq r$ on ait $|f(y)| \leq M$.

### Question 1 {.question #lb-1}
Soit $A$ un sous-ensemble borné de $U$ tel que $d(A, \R^n \setminus U) > 0$.
Montrer que $f$ est bornée sur $A$.

### Question 2 {.question #lb-2}
La fonction $f$ est *localement constante*
si pour tout point $x \in U$, on peut trouver un
rayon $r>0$ et une valeur $c \in \R$ tels que pour tout point 
$y \in U$ tel que $\|y - x\| \leq r$ on ait $f(y) = c$.
La fonction $f$ est-elle nécessairement constante sur 
tout sous-ensemble borné $A$ de $U$ tel que $d(A, \R^n \setminus U) > 0$ ?

<!--
TODO -- "Localement"
--------------------------------------------------------------------------------

Etude des pptés "localement X" pour X=bornée, positive (ex: distance), 
coup de la stabilité asympt (localt equi-convergente ?), 
localement unift continue, etc.
et comment elle s'étendent à un ensemble d'adhérence compacte 
("compactement inclus" dans l'espace de référence).

"Contre-exemples" ? Avec "localement constant", "localement polynomial", 
"localement lipschitz", fct "localement définie", etc., opérations 
qui ne sont pas stables par union finie. 
-->
 
<!--
TODO -- Compacité et Continuité
--------------------------------------------------------------------------------

Montrer la réciproque du [résultat d'existence d'un minimum pour une fonction
numérique continue définie sur un compact](#T-EM):
si l'ensemble $E \subset \mathbb{R}^n$ n'est pas compact, 
il existe une fonction continue $f: E \to \mathbb{R}$ 
n'ayant pas de minimum.

TODO -- Fonctions propres
--------------------------------------------------------------------------------

Soit $f: \mathbb{R}^n \to \mathbb{R}$ une fonction continue et propre,
c'est-à-dire telle que
$$
f(x) \to +\infty \mbox{ quand } \|x\| \to +\infty.
$$

Montrer que les ensembles de sous-niveaux de $f$, de la forme
$$
\{x \in \mathbb{R}^n \, | \, f(x) \leq c\} \, \mbox{ où } \, c \in \mathbb{R}
$$
sont compacts.

-->

Solutions
================================================================================

Normes d'opérateurs {#answer-no}
--------------------------------------------------------------------------------

### `norm(A)` {.answer}
En l'absence de second argument, la fonction `norm` calcule 
la norme de Frobenius de l'opérateur $A$, donnée comme
$$
\|A\|_F = \sqrt{\sum_{i=1}^n\sum_{j=1}^n a_{ij}^2}.
$$
Il s'agit bien d'une norme sur les applications linéaires de 
$\R^n$ dans $\R^n$, car on peut la calculer
comme la norme euclidienne de la matrice $[A]$ 
après une ["mise à plat"](Calcul Différentiel I.pdf#flatten) comme vecteur
de $\R^{n^2}$, c'est-à-dire par la formule $\|A\|_F = \|\pi([A])\|_2$. 
Mais elle n'est induite par aucune
norme de vecteur ; en effet, s'il existait une norme $\|\cdot\|_?$ telle que 
$\|A\|_F = \sup \|A \cdot x\|_? / \|x\|_?$, alors on aurait en particulier
$$
\|I\|_F  = \sup_{x \neq 0} \frac{\|I \cdot x\|_?}{\|x\|_?} = 
\sup_{x \neq 0} \frac{\|x\|_?}{\|x\|_?}  = 1.
$$
Or, on peut constater que la norme de Frobenius de la matrice associée
à l'identité dans $\R^n$ est $\sqrt{n}$, qui diffère de $1$ si $n>1$.

### `norm(A, 1)` {.answer}
L'expression `norm(A, 1)` calcule d'après la documentation de `norm` la
grandeur
$$
\|A\|_1 = \max_{j = 1 \dots n} \left(\sum_{i=1}^n |a_{ij}|\right).
$$
Le fait que le second argument de l'appel à `norm` soit $1$ peut laisser
penser que cette norme de matrice est induite par la norme de vecteurs
$$
\|x\|_1 = \sum_{i=1}^n |x_i|.
$$
Vérifions cela ; si $y= A \cdot x$, on a
$$
\begin{split}
\|y\|_1 =
\sum_{i=1}^n |y_i| = \sum_{i=1}^n \left|\sum_{j=1}^n a_{ij} x_j \right|
&\leq \sum_{i=1}^n \sum_{j=1}^n |a_{ij}||x_j|
=\sum_{j=1}^n \left(\sum_{i=1}^n |a_{ij}|\right)|x_j| \\
&\leq 
\max_{j=1\dots n} \left(\sum_{i=1}^n |a_{ij}|\right) \sum_{j=1}^n |x_j| \\
&=
\|A\|_1 \|x\|_1.
\end{split}
$$
Pour conclure, il nous suffit désormais d'exhiber un $x \in \R^n$ tel que 
$\|A \cdot x\| = \|A\|_1 \|x\|_1$. Si le maximum de $\sum_{i=1}^n |a_{ij}|$
est réalisé en $j$, il nous suffit de considérer le $j$-ème vecteur de la
base canonique de $\R^n$, $x = e_j$. En effet, on a alors
$\|e_j\|_1 = 1$ et 
$$
\|A \cdot e_j\|_1 = \left\| (a_{1j}, \dots, a_{nj})\right\|_1
= \sum_{i=1}^n |a_{ij}| = \|A\|_1.
$$


### `norm(A, 2)` {.answer}
La norme en question est définie par NumPy comme $\sigma_1$, 
la plus grande valeur singulière de $A$.
Les valeurs singulières $\sigma_1 \geq \sigma_2 \geq \sigma_n \geq 0$
associées à l'opérateur linéaire $A:\R^n \to \R^n$ sont définies à
travers une décomposition de $A$ de la forme
$$
A = U \cdot \Sigma \cdot V^*
$$
où $\Sigma \cdot (x_1, \dots, x_n) = (\sigma_1 x_1, \dots, \sigma_n x_n)$
et $U \in \R^{n} \to \R^n$ et $V \in \R^n \to \R^n$ sont des applications 
linéaires orthogonales (inversible et dont l'inverse est l'adjoint). 
Pour montrer que $\sigma_1(\cdot)$
constitue la norme d'opérateur $\|\cdot\|_{22}$ induite par la norme euclidienne
$\|\cdot\|_2$ des vecteurs de $\R^n$, on constate au préalable que
pour toute application orthogonale $U$,
$$
\|U \cdot x\| = \sqrt{\left< U \cdot x, U \cdot x \right>}
= \sqrt{\left<U^* \cdot U \cdot x, x \right>}
= \sqrt{\left<x, x\right>} = \|x\|_2,
$$
puis que
$$
\begin{split}
\|A\|_{22} &= \sup_{\|x\|_2 \leq 1} \|(U \cdot \Sigma \cdot V^*) \cdot x\|_2  \\
&= \sup_{\|x\|_2 \leq 1} \|U \cdot (\Sigma \cdot (V^* \cdot x))\|_2 \\
&= \sup_{\|y\|_2 \leq 1} \|\Sigma \cdot y\|_2 \\
&= \sup_{\|y\|_2 \leq 1} \sqrt{\sigma_1^2 y_1^2 + \dots + \sigma_n^2 y_{n}^2} \\
&= \sigma_1.
\end{split}
$$

### `norm(A, inf)` {.answer}
On constate que l'expression donnée dans la documentation de `norm`, 
à savoir
$$
\|A\|_{\infty} = \max_{i = 1 \dots n} \left(\sum_{j=1}^n |a_{ij}|\right)
$$
entretient une troublante ressemblance avec la norme 
$\|\cdot\|_1$ pour les opérateurs. Plus précisément, 
si $A^{*} : \R^n \to \R^n$ désigne l'opérateur adjoint de $A$,
tel que pour tous vecteurs $x$ et $y$ de $\R^n$, 
$\left<y, A x\right> = \left<A^* y,x \right>$,
associé à la matrice transposée de la matrice associée à $A$,
alors on a
$$
\|A\|_{\infty} = \|A^*\|_1.
$$
C'est un peu trop gros pour être une coincidence ...
Pour montrer que $\|\cdot\|_{\infty}$ est la norme d'opérateur 
$\|\cdot\|_{\infty\infty}$ associée à 
la norme de vecteurs $\|\cdot\|_{\infty}$, on peut d'abord constater que 
pour les vecteurs,
$$
\|x\|_{\infty} = \sup_{\|y\|_1 \leq 1} \left<y, x\right>
\; \mbox{ et } \;
\|x\|_{1} = \sup_{\|y\|_{\infty} \leq 1} \left<y, x\right>
$$
puis en déduire que 
$$
\begin{split}
\|A\|_{\infty\infty} = \sup_{\|x\|_{\infty} \leq 1} \|A \cdot x\|_{\infty}
&=\sup_{\|x\|_{\infty} \leq 1} \sup_{\|y\|_1 \leq 1} \left<y, A \cdot x\right> \\
&=
\sup_{\|x\|_{\infty} \leq 1} \sup_{\|y\|_1 \leq 1} \left<A^* \cdot y, x\right> \\
&=
\sup_{\|y\|_1 \leq 1} \sup_{\|x\|_{\infty} \leq 1} \left<x, A^* \cdot y \right> \\
&=
\sup_{\|y\|_1 \leq 1} \|A^* \cdot y \| \\
&=\|A^*\|_1 \\ &= \|A\|_{\infty},
\end{split}
$$
et donc $\|\cdot\|_{\infty\infty} = \|\cdot\|_{\infty}$.

Droite réelle achevée
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-dra-1}
Quand l'ordonnée $y$ du point $p=(x,y)$ est strictement positive,
$f(p)$ représente l'abscisse de l'unique point $q$ de l'intersection
de la demi-droite $D$ issue de l'origine $(0,0)$ et passant par $p$ 
avec la droite horizontale des points d'ordonnée $y=1$.

En effet, les points de $D$ sont de la forme $(\lambda x, \lambda y)$
pour $\lambda \geq 0$. On a donc $\lambda y = 1$ si et seulement si
$\lambda  = 1/y$, auquel cas $\lambda x = x / y$.

Dans les cas limites où $p = (1,0)$ et $p=(-1,0)$, la demi-droite $D$ est
horizontale, partant vers la droite de l'origine ou vers sa gauche selon
le cas. Il n'y a donc pas d'intersection avec la droite horizontale
d'équation $y=1$ dans $\R^2$, mais des intersections "à l'infini".

### Question 2 {.answer #answer-dra-2}
La fonction $f$ peut être décomposée comme $f = \psi \circ \phi$ où
l'application $\phi: (x, y) \in X \to x \in [-1, 1]$ est bijective,
d'inverse $\phi^{-1}(x) = (x, \sqrt{1 - x^2})$ 
et l'application $\psi: [-1, 1] \to [-\infty, +\infty]$
définie par
$$
\psi(x) = 
\left|
\begin{array}{cl}
- \infty & \mbox{si } x=-1, \\
\displaystyle \frac{x}{\sqrt{1-x^2}} & \mbox{si } -1 < x < 1, \\
+ \infty & \mbox{si } x=1. \\
\end{array}
\right.
$$
est également bijective, d'inverse
$$
\psi^{-1}(x) = 
\left|
\begin{array}{cl}
- 1 & \mbox{si } x=-\infty, \\
\displaystyle \frac{y}{\sqrt{1+y^2}} & \mbox{si } -\infty < x < +\infty, \\
+ 1 & \mbox{si } x=+\infty. \\
\end{array}
\right.
$$
La fonction $f$ est donc bijective comme composée de fonctions bijectives.

### Question 3 {.answer #answer-dra-3}
La fonction $f$ sera une isométrie quand $[-\infty, +\infty]$ 
est muni de la distance  $d^{\pm \infty}$ 
-- et $X$ la distance induite par la distance euclidienne de $\R^2$ -- 
si et seulement si pour toute paire de points $p_1$ et $p_2$ dans $X$
$$
d^{\pm \infty}(f(p_1), f(p_2)) = d(p_1, p_2),
$$
ce qui rend nécessaire le choix de
$$
d^{\pm \infty}(x_1, x_2) := d(f^{-1}(x_1), f^{-1}(x_2)).
$$
On vérifiera facilement que ce choix détermine bien une distance sur
la droite réelle achevée.

### Question 4 {.answer #answer-dra-4}
On a $f^{-1}(-\infty) = (-1,0)$, $f^{-1}(-1) = (-\sqrt{2}/2, \sqrt{2}/2)$,
$f^{-1}(0) = (0, 1)$,  $f^{-1}(-1) = (\sqrt{2}/2, \sqrt{2}/2)$ et
$f^{-1}(\infty) = (1,0)$, donc
$d^{\pm \infty}(0, +\infty) = d((0,1), (1,0)) = \sqrt{2},$ 
$d^{\pm \infty}(-\infty, +\infty) = d((-1, 0), (1, 0)) = 2$
et 
$d^{\pm \infty}(-1, 1) = \sqrt{2}.$

### Question 5 {.answer #answer-dra-5}
Soit $i: x \in \R \to x \in [-\infty, +\infty]$. Pour montrer que
$i$ est continue, il nous faut prouver que pour tout $x_1 \in \R$, quand
$d(x_2, x_1) \to 0$, alors $d^{\pm \infty}(i(x_2), i(x_1)) = d^{\pm \infty}(x_2, x_1)\to 0$.
Or, 
$$
\begin{split}
d^{\pm \infty}(x_2, x_1)
&= d \left(\left(\frac{x_1}{\sqrt{1 + x_1^2}}, \frac{1}{\sqrt{1 + x_1^2}} \right), 
\left(\frac{x_2}{\sqrt{1 + x_2^2}}, \frac{1}{\sqrt{1 + x_2^2}} \right)\right) \\
&= 
\sqrt{\left(\frac{x_1}{\sqrt{1 + x_1^2}} - \frac{x_2}{\sqrt{1 + x_2^2}}\right)^2 
+ 
\left(\frac{1}{\sqrt{1 + x_1^2}} -  \frac{1}{\sqrt{1 + x_2^2}}\right)^2},
\end{split}
$$
et cette expression est une fonction continue de ses arguments $x_1$ et $x_2$,
nulle quand $x_1 = x_2$ ; cette propriété est donc bien vérifiée.

### Question 6 {.answer #answer-dra-6}
Quand $x_k$ est une suite de réels, $x_k \to +\infty$ est à interpréter
classiquement comme: pour tout $M \in \R$, il existe un rang $m \in \N$
tel que si $k \geq m$, alors $x_k \geq M$.

Mais il existe maintenant une seconde interprétation si l'on considère 
$x_k \in \R$ comme une suite de points dans l'espace métrique 
$[-\infty, +\infty]$. Cela signifie alors que
$d^{\pm \infty}(x_k, +\infty) \to 0$ quand $k \to +\infty$.
Or, comme
$$
\begin{split}
\left(d^{\pm \infty}(x_k, +\infty) \right)^2
&= \left(\frac{x_k}{\sqrt{1+x_k^2}} - 1\right)^2 + \frac{1}{1+x_k^2} \\
&= \left(\mathrm{sign}(x_k)\sqrt{\frac{x_k^2}{1+x_k^2}} - 1\right)^2 + \frac{1}{1+x_k^2},
\end{split}
$$
ces deux conditions sont équivalentes.

### Question 7 {.answer #answer-dra-7}
On admettra sans preuve (la démarche est très similaire à celle menée
dans les questions précédentes) que la construction graphique ci-dessous

![Construction du compactifié de $\R$.](images/extended-real-numbers-2.tex)

permet de doter $\R \cup \{\infty\}$ d'une métrique telle que 
$|x_k| \to +\infty$ si et seulement si $d^{\infty}(x_k,\infty) \to 0$
et que l'injection canonique associée est continue.
On constate graphiquement que dans cette variante, quand le point
de la droite d'ordonnée $y=2$ s'éloigne vers l'infini vers la droite ou
vers la gauche, le point correspondant du cercle centré en $(0,1)$ et de
rayon $1$ converge vers l'origine $(0,0)$.

Si l'on considère une suite de points $x_k \in \R \cup\{\infty\}$, 
soit il existe une suite de points réels bornée que l'on peut extraire de 
$x_k$ -- auquel cas par compacité des fermés bornés dans $\R$ 
il existe une sous-suite extraite des $x_k$ convergeant dans $\R$ 
(et donc dans $\R \cup\{\infty\}$)
-- soit $|x_k| \to +\infty$ quand $k\to +\infty$ -- auquel cas
$x_k \to \infty$ dans $\R \cup\{\infty\}$. Dans les deux cas,
la suite admet une suite extraite convergente, l'espace est donc
compact.


Localement fermé
--------------------------------------------------------------------------------

### Question 0 {.answer #answer-lf-0}
Un sous-ensemble $B$ d'un ensemble $A$ de points d'un espace topologique $X$
est "fermé dans $A$" s'il est fermé **comme ensemble de points de l'espace
topologique $A$**, muni de la topologie (ou le cas échéant la métrique)
induite par $X$. Et cette propriété peut être différente de être "fermé"
(sous-entendu comme ensemble de points de $X$).

Par exemple, si $X = \R$, $A = \left]0, +\infty\right[$ et 
$B = \left]0, +\infty\right[$, $B$ n'est pas fermé dans $\mathbb{R}$,
car la suite $x_k = 2^{-k}$ appartient à $B$, mais $x_k \to 0 \not \in B$ 
quand $k \to +\infty$. Par contre, toute suite de $B$ convergeant 
dans $A$ converge dans $B$ car les deux ensembles sont identiques.
Par conséquent, $B$ est fermé dans $A$.

### Question 1 {.answer #answer-lf-1}

Soit $x \in A:=\left[0, 1\right[$ ; 
si $x>0$, on peut prendre $V=\left]x/2, 1\right[$.
C'est bien un voisinage ouvert de $x$ et $A\cap V = V$. 
L'ensemble $A \cap V$ est donc fermé dans $V$. 
Si $x=0$, on peut prendre $V = \left]-1, 1/2\right[$; 
c'est un voisinage ouvert de $x$ 
et $A \cap V = \left[0, 1/2\right[$ est bien fermé dans $V$.

Soit $x_k$ une suite de $\mathbb{R}$ qui converge vers $\ell$ et 
$A = \{x_k \, | \, k \in \mathbb{N}\}$. 
Si $a \in A$ et que $a \neq \ell$, 
alors il existe un $\varepsilon > 0$ tel que 
$V = ]a - \varepsilon, a + \varepsilon[$ vérifie $A \cap V = \{a\}$.
$V$ est un voisinage ouvert de $a$ et $A \cap V$ est bien fermé dans $V$.
Si la valeur limite $\ell$ n'est pas atteinte par un $x_k$, cela conclut
la preuve que $A$ est localement fermé. Dans le cas contraire, pour 
$a=\ell$, on peut prendre $V = \R$; en effet, $A$ est alors fermé.

L'ensemble des rationnels $\mathbb{Q}$ n'est pas localement fermé.
En effet si $V$ est un voisinage de $0$ il contient nécessairement un ensemble
de la forme $\left]-\varepsilon, \varepsilon\right[$ pour un $\varepsilon > 0$.
Or cet intervalle contient des irrationels, qui peuvent être obtenus
comme limite de rationnels dans $\left]-\varepsilon, \varepsilon\right[$
et donc de $V$. 
Par conséquent, $\mathbb{Q} \cap V$ ne peut pas être fermé dans $V$,
donc $\mathbb{Q}$ n'est pas localement fermé.


### Question 2 {.answer #answer-lf-2}

Si $A$ est fermé, on peut prendre $V=X$ qui est un voisinage ouvert 
de $A$ (il contient $A$ et est ouvert). On a alors $A \cap V = A$ est donc 
$A \cap V$ est bien fermé dans $V=X$.

Si $A$ est ouvert, on peut prendre $V=A$ qui est un voisinage ouvert 
de $A$ (il contient $A$ et est ouvert). On a alors $A \cap V = A$ est donc 
$A \cap V$ est bien fermé dans $V=A$.

Si $A$ et $B$ sont localement fermés et $x \in A \cap B$, il existe des 
voisinages ouverts $U$ et $V$ de $x$ tels que $A \cap U$ soit fermé 
dans $U$ et $B \cap V$ soit fermé dans $V$. 
Par construction, $U \cap V$ est un voisinage ouvert de $x$;
en effet, d'une part cette intersection contient $x$ et d'autre part
pour tout $y$ dans $U \cap V$, 
$d(y, X \setminus U) > 0$ et $d(y, X \setminus V) > 0$ ; or 
$$
\begin{split}
d(y, X \setminus (U \cap V)) 
&= 
d(y, (X \setminus U) \cup (X \setminus V)) \\
&= \min \left( d(y, X \setminus U), d(y, X \setminus V) \right) \\
&> 0.
\end{split}
$$
donc $U \cap V$ est ouvert.
L'ensemble $A$, qui est fermé dans $U$, est donc fermé dans $U \cap V$
(si une suite de $A$ converge dans $U \cap V$, elle converge dans $U$
et donc sa limite appartient à $A$); de la même façon, $B$ est fermé
dans $U \cap V$. Par conséquent, $A \cap B$ est fermé dans $U \cap V$.

### Question 3 {.answer #answer-lf-3}

Si un ensemble est l'intersection d'un ouvert et d'un fermé dans $X$,
il est l'intersection de deux ensembles localement fermés, donc il
est localement fermé (par les résultats de la [question précédente](#lf-2)).

Réciproquement, supposons que l'ensemble $A$ soit localement fermé.
En tout point $a \in A$, il existe un voisinage ouvert $V_a$ tel que
$A\cap V_a$ soit fermé dans $V_a$. L'ensemble $V_a \setminus (A \cap V_a)
= V_a \setminus A$ est donc ouvert dans $V_a$ et donc dans $X$.
Par construction, la collection des $V_a$ recouvre $A$, c'est-à-dire que
$A \subset \cup_{a \in A} V_a$, donc
$$
A = \bigcup_{a \in A} V_a \setminus \left(\bigcup_{a \in A} V_a \setminus A\right).
$$
Posons $V = \cup_{a \in A} V_a$;
le complémentaire dans $X$ de $\bigcup_{a \in A} V_a \setminus A$ est un
ensemble fermé $F$ ; de l'équation ci-dessus on déduit donc
que $A = V \cap F$ où $V$ est ouvert dans $X$ et $F$ est fermé dans $X$.

Distance entre ensembles
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-dh-1}

Non, la distance usuelle $d(A,B)$ en convient pas.
En effet, cette distance est nulle dès que l'intersection de $A$ et $B$
est non vide, même si des points de $A$ sont très éloignés de $B$.

### Question 2 {.answer #answer-dh-2}

Lorsque $A = [-1,1] \times [-1, 1]$ et $B = [0,2] \times [0,2]$, 
il est possible de calculer $d(a, B)$ pour tout $a \in A$.
Plus précisément, $B$ étant fermé, l'infimum qui définit la
distance est un minimum. Dans ce cas précis, il existe un 
unique projeté $\pi_B(a)$ de $a$ sur $B$, 
qui minimise la distance
$$
d(a, \pi_B(a)) = \inf_{b \in B} d(a, b).
$$
Il est donné quadrant par quadrant par
$$
\pi_B((x, y)) = \left|
\begin{array}{rl}
(0, y) & \mbox{si } (x, y) \in [-1, 0] \times [0,1] \\
(x, y) & \mbox{si } (x, y) \in [0, 1] \times  [0,1] \\
(0, 0) & \mbox{si } (x, y) \in [-1, 0] \times [-1,0] \\
(x, 0) & \mbox{si } (x, y) \in [0, 1] \times [-1,0] \\
\end{array}
\right.
$$
Par conséquent, on a
$$
d((x, y), B) = \left|
\begin{array}{rl}
|x| & \mbox{si } (x, y) \in [-1, 0] \times [0,1] \\
0 & \mbox{si } (x, y) \in [0, 1] \times  [0,1] \\
\sqrt{x^2 + y^2} & \mbox{si } (x, y) \in [-1, 0] \times [-1,0] \\
|y| & \mbox{si } (x, y) \in [0, 1] \times [-1,0] \\
\end{array}
\right.
$$
Cette fonction est minimale sur $A$ pour $(x, y) = (-1, -1)$. 
On a donc
$$
\sup_{a \in A} \inf_{b \in B} d(a, b) = \sqrt{2}.
$$
On montre de la même façon que 
$$
\sup_{b \in B} \inf_{a \in A} d(a, b) = \sqrt{2}.
$$
La distance de Hausdorff entre $A$ et $B$ vaut donc $\sqrt{2}$.

### Question 3 {.answer #answer-dh-3}

Vérifions que la "distance" de Hausdorff est effectivement une distance
sur l'espace des sous-ensembles compacts de $\R^n$.

 1. Axiome de séparation. 
    Si $$d[A, B] = \max(\sup_{a \in A} d(a, B), \sup_{b \in B} d(b, A)) = 0,$$
    alors pour tout $a \in A$, $d(a, B) = 0$ et pour tout $b \in B$, 
    $d(b, A) = 0$, c'est-à-dire $a \in \overline{B}$ et $b \in \overline{A}$.
    Par conséquent, puisque $A$ et $B$ sont fermés, 
    $A \subset \overline{B} = B$ et $B \subset \overline{A} = A$
    et donc $A = B$.

 2. Axiome de symétrie. Il est clair par construction que pour tous les
    ensembles compacts non vides $A$ et $B$ de $\R^n$, on a $d[A, B] = d[B, A]$.

 3. Pour tout $a \in A$, $b \in B$, $c \in C$, l'inégalité triangulaire
    fournit $d(a, c) \leq d(a, b) + d(b, c)$. 
    Par conséquent, 
    $\inf_{c \in C} d(a, c) \leq d(a, b) + \inf_{c \in C}d(b, c)$
    et donc 
    $$
    \begin{split}
    \inf_{c \in C} d(a, c) 
    &\leq \inf_{b \in B} d(a, b) + \inf_{b \in B} \inf_{c \in C}d(b, c) \\
    &\leq
    \inf_{b \in B} d(a, b) + \sup_{b \in B} \inf_{c \in C}d(b, c),
    \end{split}
    $$
    inégalité dont on déduit
    $$
    \sup_{a \in A} \inf_{c \in C} d(a, c) \leq
    \sup_{a \in A} \inf_{b \in B} d(a, b) + \sup_{b \in B} \inf_{c \in C}d(b, c)
    $$
    et par conséquent
    $$
    \sup_{a \in A} \inf_{c \in C} d(a, c) \leq
    d[A, B] + d[B, C].
    $$
    De façon similaire, on a 
    $$
    \sup_{c \in C} \inf_{a \in A} d(a, c) \leq
    \sup_{c \in A} \inf_{b \in B} d(c, b) + \sup_{b \in B} \inf_{a \in A}d(b, a)
    $$
    et par conséquent
    $$
    \sup_{c \in C} \inf_{a \in A} d(a, c) \leq
    d[A, B] + d[B, C]
    $$
    et donc $d[A, C] \leq d[A, B] + d[B, C]$.
    
### Question 4 {.answer #answer-dh-4}

Si $A$ et $B$ sont des ensembles non vides de $\R^n$, $A+B$ est clairement
non vide. Si de plus $A$ et $B$ sont compacts, et que l'on considère une
suite $x_k$ de points de $A+B$, alors il existe des $a_k$ de $A$ 
et $b_k$ de $B$ tels que $x_k = a_k + b_k$. Par compacité de $A$, 
il existe une suite $a_{\sigma(k)}$ 
-- où $\sigma: \N \to \N$ est croissante --
qui converge vers un $a \in A$ ;
par compacité de $B$, il existe une suite $b_{\tau (\sigma(k))}$
-- où $\tau: \N \to \N$ est croissante --
qui converge vers un $b \in B$. 
Par continuité de la somme dans $\R^n$, la suite des
$x_{\tau (\sigma(k))}$, qui est extraite des $x_k$, converge vers $a+b \in A+B$.

Soit $A$, $B$, $C$ et $D$ quatre ensembles compacts non vides de $\R^n$.
Si $a \in A$, $b \in B$, $c \in C$ et $d \in D$, on a
$$
d(a+b, c+d) = \|a+b - c -d\| \leq \|a - c\| + \|b - d\|.
$$
Par conséquent,
$$
\begin{split}
\sup_{x \in A + B} \inf_{y \in C + D} d(x, y)
&=
\sup_{a \in A} \sup_{b \in B} \inf_{c \in C} \inf_{d \in D}
\|a + b - c - d\| \\
&\leq
\sup_{a \in A} \sup_{b \in B} \inf_{c \in C} \inf_{d \in D}
\|a - c\| + \|b - d\| \\
&\leq \sup_{a \in A} \inf_{c \in C} 
\|a - c\| 
+ \sup_{b \in B} \inf_{d \in D}
\|b - d\| \\
&\leq d[A, C] + d[B, D].
\end{split}
$$
De même, on peut montrer que 
$$
\sup_{y \in C+D} \inf_{x \in A + B} d(x, y) \leq d[A, C] + d[B, D]
$$
et par conséquent
$d[A + B, C + D] \leq d[A, C] + d[B, D].$
Si $A_k \to A$ et $C_k \to C$, comme
$d[A_k+C_k, A+C] \leq d[A, A_k] + d[C, C_k]$, on en déduit que
$A_k + C_k \to A + C$. La somme de Minkowski est donc continue.

 [Plongement de Kuratowski]
--------------------------------------------------------------------------------

### Question 1 {#answer-pk-1 .answer}

Soit $x$, $x'$ deux points de $X$. Pour tout $y$ dans $X$ on a:
$$
\begin{split}
f_x(y) - f_{x'}(y) &= d(x, y) - d(x_0, y) - (d(x', y) - d(x', x_0))\\
&= d(x, y) - d(x', y),
\end{split}
$$
par conséquent, si $f_x = f_{x'}$, on a en particulier
$f_x(x') = f_{x'}(x')$, soit $d(x, x') - d(x', x') = d(x, x') = 0$, 
c'est-à-dire $x = x'$ par [l'axiome de séparation](#dist-sep).

### Question 2 {#answer-pk-2 .answer}
Pour tout $x, y \in X$, on a 
$$
|f_x(y)| = |d(x, y) - d(x_0, y)| \leq d(x, x_0)
$$
par [l'inégalité triangulaire](#dist-ineg).

### Question 3 {#answer-pk-3 .answer}
Si $f: E \to \R$ et $g: E \to \R$ sont bornées et $\lambda \in \R$,
il est clair que $f+g$ et $\lambda f$ sont bornées.
De plus,

  1. Si $\|f\|_{\infty} = \sup_{x\in E} \|f(x)\| = 0$, alors 
     $\|f(x)\|=0$ pour tout $x \in E$ ; par conséquent $f=0$,

  2. On a $\|\lambda f\|_{\infty} = \sup_{x\in E} \|\lambda f(x)\| = |\lambda| \sup_{x\in E} \|f(x)\| = |\lambda| \|f\|_{\infty}$.

  3. On a $$\begin{split}\|f+g\|_{\infty} &= \sup_{x\in E} \| f(x) + g(x)\| \\ &\leq \sup_{x\in E} \|\lambda f(x)\| + \sup_{x\in E} \|\lambda g(x)\|\\ &= \|f\|_{\infty} + \|g\|_{\infty}.\end{split}$$

### Question 4 {#answer-pk-4 .answer}
Soient $x, y \in X$ ; on a
$$
f_x(z) - f_y(z) = d(z, x) - d(z, x_0) - (d(z, y) - d(z, y_0)) = d(z, x) - d(z, y).
$$
Par conséquent, par [l'inégalité triangulaire](#dist-ineg),
$$
\|f_x - f_y\|_{\infty}
= \sup_{y \in X} |d(z, x) - d(z, y)| \leq d(x, y)
$$
et d'autre part
$$
\|f_x - f_y\|_{\infty}
= \sup_{y \in X} |d(z, x) - d(z, y)| \geq |d(x, x) - d(x, y)| = d(x, y).
$$
Finalement, on a bien
$$
\|f_x - f_y\|_{\infty} = d(x, y)
$$
et $x \mapsto f_x$ est une isométrie.

Le nombre d'or {#golden-ratio}
--------------------------------------------------------------------------------

### Question 1 {#answer-golden-ratio-1 .answer}
L'existence d'un unique point fixe associé à l'application
$$
f: x \in \left]0, +\infty\right[ \mapsto 1 + \frac{1}{x}
$$
peut être établi par des méthodes classiques d'analyse d'une fonction
d'une variable réelle. 
La fonction $g: x \in \left]0, +\infty\right[ \to x - f(x)$ est dérivable.
Sa dérivée en $x$ vaut $1 + 1/x^2$, qui est strictement positive, donc 
la fonction  $g$ est strictement croissante et 
il existe donc au plus un zéro de $g$. 
De plus, $g(x) \to -\infty$ quand $x\to 0$ et $g(x) \to +\infty$ quand $g(x) \to +\infty$.
Comme $g$ est continue (puisque dérivable), par le théorème des valeurs intermédiaires,
$g$ admet bien un zéro sur $\left]0, +\infty\right[$.
La fonction $f$ admet donc un unique point fixe. 
Comme $g(4/3) = 4/3 - 1 - 3/4 = -5/12 <0$ 
et $g(2) = 2 - 1 - 1/2 = 1/2 > 0$,
le point fixe de $f$ se situe dans l'intervalle $[3/2, 2]$.

<!-- C'est mignon mais c'est faux: la suite extraite n'est pas solution de la
même équation fonctionnelle ...
Alternativement, pour établir l'existence (mais pas l'unicité) du point fixe,
on aurait pu associer à la fonction $f$ la fonction 
$\bar{f}: [0, +\infty] \to [0, +\infty]$ définie par
$$
\bar{f}(x) = \left|
\begin{array}{cl}
+\infty & \mbox{si } x = 0, \\
f(x) & \mbox{si } 0 < x < + \infty, \\
1 & \mbox{si } x = +\infty.
\end{array}
\right.
$$
Si l'on munit $[0, +\infty]$ de la métrique
induite par [la droite réelle achevée](#dra), la fonction $f$
est continue et $[0, +\infty]$ est compact. 
La suite de valeurs
définie par $x_0 = 1$ (par exemple) et $x_{k+1} = \bar{f}(x_k)$
admet donc une sous-suite $y_k$ qui converge vers un $\ell \in [0, +\infty]$.
Par continuité de $\bar{f}$, on en déduit que $\ell = \bar{f}(\ell)$.
Il suffit alors de vérifier que $\bar{f}(0) \neq 0$ et $\bar{f}(+\infty) \neq
+\infty$ pour conclure à l'existence d'un réel $\ell> 0$ tel que
$\ell = f(\ell)$.
-->

### Question 2 {#answer-golden-ratio-2 .answer}
Soit $x_k$ la suite de réels définie par $x_0 \in [4/3, 2]$
et $x_{k+1} = f(x_k)$. La fonction $f$ est continue et décroissante 
croissante ; de plus
$$
f(4/3) = 1 + \frac{1}{4/3} = 1 + \frac{3}{4} = \frac{7}{4} \in \left[\frac{4}{3}, 2\right]
$$
et 
$$
f(2) = 1 + \frac{1}{2} = \frac{3}{2}  \in \left[\frac{4}{3}, 2\right].
$$
Par conséquent, $f([4/3,2]) \subset [4/3,2]$. Comme $f'(x) = - 1/x^2$,
pour tout $x \in [4/3,2]$, $|f'(x)| < 9/16 < 1$. 
Par le théorème des accroissements finis, la restriction de $f$ à $[4/3, 2]$ 
est donc contractante.
L'ensemble $[4/3, 2]$ est un ensemble fermé $\R$ ; il est donc complet.
L'existence et l'unicité du point fixe de $f$ sur $[4/3,2]$ ainsi que son
obtention comme limite de la suite $x_k$ résultent du [théorème de point fixe
de Banach](#T-TPFB).
 
### Question 3 {#answer-golden-ratio-3 .answer}
Compte tenu des résultats de l'exercice ["Point fixe"](#TPFB2),
il suffit d'établir que sur un sous-ensemble complet $X$ de 
$\left]0, +\infty\right[$ tel que $f(X) \subset X$, $f \circ f$ 
est contractante pour conclure que $f$ possède un unique point fixe
sur $X$,  obtenu comme limite de la suite
définie par $x_{k+1} = f(x_k)$ pour tout $x_0 \in X$.

Posons $X = \left[1, +\infty\right[$ ; $X$ est complet car c'est un sous-ensemble
fermé de $\R$ qui est complet (une suite de Cauchy de $X$ converge dans $\R$,
donc dans $X$). 
De plus, comme pour tout $x>0$, $1+1/x > 1$, 
on a bien $f(\left[1, +\infty\right[) \subset \left[1, +\infty\right[$.
Pour tout $x \geq 1$, on a
$$
f(f(x)) = 1+ \frac{1}{(1+1/x)} = 1 + \frac{x}{x+1} = 1+\frac{x+1}{x+1} - \frac{1}{x+1}
=2 - \frac{1}{x+1}
$$
et donc
$$
(f \circ f)'(x) = \frac{1}{(x+1)^2}
$$
ce qui entraîne que $|(f \circ f)'(x)| \leq 1/4 < 1$ si $x\geq 1$.
La restriction de $f \circ f$ à $\left[1, +\infty\right[$ est donc contractante.
Nous avons donc établi toutes les hypothèses garantissant que
la suite $x_{k+1} = f(x_k)$ tend vers le nombre d'or si 
$x_0 \geq 1$.
Notons finalement que si $x_0 \in \left]0,1\right[$, 
$f(x_0) \in \left[1, +\infty\right[$ ; par conséquent le résultat
vaut non seulement pour tout $x_0 \in \left[1, +\infty\right[$ mais
bien pour tout $x_0 \in \left]0, +\infty\right[$.


 [Spirale d'Euler]
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-se-1}

Montrer que $(x(t), y(t))$ à une limite quand $t\to+\infty$ suppose de
montrer qu'il existe un point $T \in \mathbb{R}^2$ tel que pour 
toute suite de valeurs $t_k$ tendant vers $+\infty$, 
la suite $(x(t_k), y(t_k))$ tende vers $T$. 
Compte tenu de l'hypothèse, 
cela revient à montrer que la limite d'une telle suite est indépendante du
choix de la suite des $t_k$. 

Considérons deux suites $s_k$ et $r_k$
de réels positifs tendant vers $+\infty$ et notons $S$ et $R$ les 
limites de $(x(s_k), y(s_k))$ et $(x(r_k), y(r_k))$. La suite 
$t_k$ des réels $s_0$, $r_0$, $s_1$, $r_1, \dots$ est positive 
et tend vers $+\infty$. Les $(x(t_k), y(t_k))$ sont admettent donc
une limite $T$ quand $k \to +\infty$; toute sous-suite étant convergente
et de même limite, on a nécessairement $T = S = R$, ce qui prouve le
résultat cherché.

### Question 2 {.answer #answer-se-2}

Nous traitons le cas de $I(a, b)$, celui de $J(a, b)$ étant similaire.
Pour tout $a$ et $b$ tels que $0 < a \leq b$,
le changement de variable $\tau = s^2$ fournit:
$$
I(a, b) = \int_a^b \cos s^2 \, ds = \int_{\sqrt{a}}^{\sqrt{b}} \frac{\cos \tau}{2\sqrt{\tau}} \, d\tau.
$$
Par intégration par parties, on obtient alors
$$
I(a, b) = \frac{\sin b}{2\sqrt{b}} -  \frac{\sin a}{2\sqrt{a}} 
+ \int_{\sqrt{a}}^{\sqrt{b}} \frac{\sin \tau}{\tau^{3/2}} \, d\tau.
$$
Comme $|\sin \tau| \leq 1$,
$$
\left| \int_{\sqrt{a}}^{\sqrt{b}} \frac{\sin \tau}{\tau^{3/2}} \, d\tau \right|
\leq \int_{\sqrt{a}}^{\sqrt{b}} \frac{d \tau}{\tau^{3/2}}
= - \frac{2}{\sqrt{b}} + \frac{2}{\sqrt{a}}.
$$
On en déduit
$$
\left|I(a, b)\right| 
\leq 
\frac{5}{2 \sqrt{a}} + \frac{5}{2 \sqrt{b}} \leq \frac{5}{\sqrt{a}}.
$$

### Question 3 {.answer #answer-se-3}

Pour établir l'existence d'un point limite à la spirale d'Euler,
compte tenu du résultat de la question 1, il nous suffit de montrer
que pour toute suite de valeurs $t_k$ tendant vers $+\infty$, 
la suite des $(x_k, y_k) = (x(t_k), y(t_k))$ est convergente. 
Comme nous ne connaissons
par la valeur de cette limite, nous allons établir que cette suite est
de Cauchy; l'ensemble $\mathbb{R}^2$ étant complet, cela prouvera la
convergence de la suite.

Or, pour tout couple d'entier $n$ et $p$, on a
$$
\begin{split}
x_n - x_p = x(t_n) - x(t_p) 
&= \int_0^{t_n} \cos s^2 \, ds - \int_0^{t_p} \cos s^2 \, ds \\
&=\int_{t_p}^{t_n} \cos s^2 \, ds \\& = I(t_p, t_n)
\end{split}
$$
et de façon similaire,
$$
y_n - y_p = \int_{t_p}^{t_n} \sin s^2 \, ds  = J(t_p, t_n).
$$
En exploitant le résultat de la question 2, on peut alors en déduire que
$$
\|(x_n, y_n) - (x_p, y_p)\| 
= 
\sqrt{I(t_p, t_n)^2 + J(t_p, t_n)^2}
\leq \frac{2\alpha}{\sqrt{\min(t_p, t_n)}}.
$$
Pour un $\varepsilon > 0$ donné, il suffit de choisir un rang 
$m \in \mathbb{N}$ tel que
$$
t_k \geq \left(\frac{2 \alpha}{\varepsilon}\right)^2, \, k\geq m
$$
pour avoir la garantie que si $p \geq m$ et $n \geq m$, alors
$$
\|(x_n, y_n) - (x_p, y_p)\| 
\leq \frac{2\alpha}{\sqrt{\min(t_p, t_n)}} 
\leq \varepsilon.
$$
La suite des $(x_k, y_k)$ est donc de Cauchy.



 [Point fixe]
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-pf-1}
Si $x$ est un point fixe de $f$, $f(x) = x$, par conséquent
$$
f^2(x) = f(f(x)) = f(x) = x, 
$$
puis
$$
f^3(x) = f(f^2(x)) = f(x) = x,
$$
etc. Par récurrence, il est clair que l'on peut établir que pour tout
$n \geq 1$, on a $f^n(x) = x$: $x$ est un point fixe de $f^n$.

Supposons désormais que la fonction itérée $f^n$ admette un unique point fixe
$x$. Comme tout point fixe de $f$ est un point fixe de $f^n$, $f$ admet au
plus un point fixe.
De plus, comme $f^n(x) = x$, en applicant $f$ aux
deux membres de cette équation, on obtient 
$$
f(f^n(x)) = f^n(f(x)) = f(x).
$$
Par conséquent, $f(x)$ est un point fixe de $f^n$ ; 
c'est donc l'unique point fixe $x$ de $f^n$.
On a donc $f(x) = x$, c'est-à-dire que $x$ est un point fixe de $f$. 

### Question 2 {.answer #answer-pf-2}
Si $X$ est un espace métrique complet et que $f^n$ est contractante, 
par [théorème du point fixe de Banach](#T-TPFB), $f^n$ admet un
unique point fixe $x$, calculable comme limite de toute suite
$y_k$ telle que $y_{k+1} = f^n(y_k)$ et $y_0 \in X$.

Par les résultats de [la question 1](#pf-1), $x$ est l'unique point 
fixe de $f$.
Le "procédé habituel pour construire un point fixe de $f$" 
consiste à prendre un $x_0 \in X$ quelconque et à construire 
par récurrence la suite des $x_{k+1} = f(x_k)$ ; 
on souhaite donc montrer que cette suite converge vers l'unique point fixe 
$x$ de $f$. 
La suite $(x_{kn})_k$ -- extraite des $x_k$ -- converge vers $x$, 
car $x_{(k+1)n} = f^n(x_{kn})$.
Il en est de même pour la suite extraite $(x_{kn+1})_k$, construite
à partir du même procédé mais en initialisant la séquence avec 
la valeur $x_1$, pour la suite $(x_{kn+2})_k$, ..., jusqu'à 
$(x_{kn + (n-1)})_k$. Ces $n$ suites convergent toutes vers $x$,
donc la suite des $(x_k)_k$ converge également vers le point fixe $x$.

Résolution itérative de systèmes linéaires
--------------------------------------------------------------------------------

### Question 1 {#answer-risl-1 .answer}
La relation $A \cdot x = y$ est vérifiée si et seulement si
$D \cdot x + (A - D) \cdot x = y$, soit
$$
D \cdot x = (D - A) \cdot x + y.
$$
L'opérateur $A$ étant diagonalement dominant, $a_{ii} > 0$ pour tout $i$; 
l'opérateur $D$ est donc inversible. 
La relation ci-dessus est donc équivalente à
$$
x = D^{-1} \cdot (D-A) \cdot x + D^{-1} \cdot y.
$$

### Question 2 {#answer-risl-2 .answer}
La question 1 établit que pour tout $y \in \R^n$, 
le vecteur $x \in \R^n$ est solution de $A \cdot x = y$ 
si et seulement s'il est un point fixe de l'application 
$$
\phi: x \in \R^n \mapsto D^{-1} \cdot (D-A) \cdot x + D^{-1} \cdot y \in \R^n.
$$
Cette application est affine: pour tout couple $x_1$ et $x_2$ dans $\R^n$, 
$$
\phi(x_1) - \phi(x_2) = D^{-1} \cdot (D-A) \cdot (x_1 - x_2).
$$
Notons qu'avec $B := D^{-1} \cdot (D-A)$ et $[B]_{ij} = b_{ij}$, 
on a $b_{ii} = 0$ et si $i \neq j$, $b_{ij} = -a_{ij}/a_{ii}$.
Par conséquent, pour tout $i$, 
$\sum_{j=1}^n |b_{ij}| < 1$, soit
$$
\max_{i=1\dots n} \sum_{j=1}^n  |b_{ij}| < 1.
$$
On reconnait au membre de gauche de cette inégalité la norme d'opérateur 
$\|B\|_{\infty}$ de l'exercice "[Normes d'opérateurs]" ;
on a donc pour tout $x \in \R^n$,
$$
\|B \cdot x\|_{\infty} \leq \kappa \|x\|_{\infty}
\; \mbox{ avec } \; \kappa:=\|B\|_{\infty} < 1
$$ 
(on peut aussi établir ce résultat directement).
Si l'on munit $\R^n$ de la norme $\|\cdot\|_{\infty}$
(l'espace est alors complet puisque $\|\cdot\|_{\infty}$ est équivalent à la norme
euclidienne : on a $\|\cdot\|_2 / \sqrt{n} \leq \|\cdot\|_{\infty} \leq \|\cdot\|_2$), 
l'application $\phi$ est contractante. 
Par [le théorème du point fixe de Banach](#T-TPFB), 
elle admet donc un unique point fixe $x$, qui est la solution de $A \cdot x = y$.
L'opérateur $A$ est donc inversible et $A^{-1} \cdot y$ peut être calculé comme
la limite de la suite
$x_{k+1} = B \cdot x_k$ pour un $x_0 \in \R^n$ arbitraire.

Équation différentielle
--------------------------------------------------------------------------------

### Question 1 {#answer-ed-1 .answer}
Si la fonction $x$ est continue et vérifie pour tout $t\geq0$
l'équation intégrale
$$
x(t) = x_0 + \int_0^t A \cdot x(s) \, ds,
$$
alors nécessairement
$$
x(0) =x_0 + \int_0^0 A \cdot x(s) \, ds = x_0,
$$
et sa dérivée satisfait $\dot{x}(t) = A \cdot x(t)$.

Réciproquement, si $x(0) = x_0$ et pour tout $t \geq 0$ on a 
$\dot{x}(t) = A \cdot x(t)$, alors comme le second membre de cette équation
est continue comme composée de fonctions continues, $\dot{x}$ est continue,
et par intégration entre $0$ et $t$ on retrouve l'équation intégrale 
souhaitée.

### Question 2 {#answer-ed-2 .answer}
Par linéarité de l'intégrale et de l'opérateur $A$, pour tout couple
$x$ et $y$ de fonctions continue de $[0, T]$ dans $\R^n$ et tout
$t \in [0, T]$, on a
$$
(\Phi(x) - \Phi(y))(t) = \int_0^t A \cdot (x(s) - y(s)) \, ds,
$$
et donc
$$
\begin{split}
\|(\Phi(x)(t) - \Phi(y)(t)\| &\leq \int_0^t \|A \cdot (x(s) - y(s))\| \, ds \\
&\leq  \int_0^t \|A \| \|x - y\|_{\infty} \, ds \\
&= (\|A\| T) \times \|x - y\|_{\infty}, \\
\end{split}
$$
soit 
$$
\|\Phi(x) - \Phi(y)\|_{\infty} \leq (\|A\| T) \times \|x - y\|_{\infty}.
$$
L'application $\Phi$ est donc contractante si $\|A\| \leq 1/T$.
[Le théorème du point fixe de Banach](#T-TPFB) prouve alors
l'unicité d'une fonction continue telle que 
$$
x(t) = x_0 + \int_0^t A \cdot x(s) \, ds
$$
pour tout $t \in [0, T]$.

### Question 3 {#answer-ed-3 .answer}
Le fait que $\|\cdot\|_{\infty}^{\alpha}$ soit une norme se déduit facilement
du fait que $\|\cdot\|_{\infty}$ en soit une. On peut constater que pour 
toute fonction $x$ continue sur $[0, T]$, on a
$$
\|e^{-\alpha T} x\|_{\infty}^{\alpha} \leq \|x\|_{\infty}^{\alpha} \leq \|x\|_{\infty}.
$$
Les deux normes sont donc équivalentes. En particulier, les notions de 
convergence de suite de points et de suites de Cauchy sont les mêmes dans
les deux espaces. 
L'espace vectoriel $E$ muni de la norme $\|\cdot\|_{\infty}$ étant complet, 
c'est également le cas pour $E$ muni de la norme $\|\cdot\|^{\alpha}_{\infty}$.

### Question 4 {#answer-ed-4 .answer}
Pour tout couple
$x$ et $y$ de fonctions continue de $[0, T]$ dans $\R^n$ et tout
$t \in [0, T]$, on a
$$
e^{-\alpha t} (x-y)(t) 
= e^{-\alpha t} \int_{0}^t A \cdot (x-y)(s) \, ds
= \int_{0}^t A \cdot e^{-\alpha s}(x-y)(s) e^{-\alpha (t-s)} \, ds
$$
et donc
$$
\begin{split}
\left|e^{-\alpha t} (x-y)(t)\right|
&\leq 
\int_{0}^t \|A\| \|e^{-\alpha s}(x-y)(s)\| e^{-\alpha (t-s)} \, ds \\
&\leq 
\left(\|A\| T \int_0^t e^{-\alpha (t-s)} \, ds \right) \|x-y\|_{\infty}^{\alpha}.
\end{split}
$$
Comme
$$
\int_0^t e^{-\alpha (t-s)} \, ds
= \left[\frac{e^{-\alpha (t-s)}}{\alpha} \right]_0^t
=\frac{1 - e^{-\alpha t}}{\alpha} \leq \frac{1}{\alpha},
$$
on en déduit que 
$$
\|x - y\|_{\infty}^{\alpha} \leq \frac{\|A| T}{\alpha} \|x-y\|_{\infty}^{\alpha}.
$$
L'application $\Phi$ est donc contractante dès lors que $\alpha > \|A\| T$.
Pour tout $T > 0$,
[le théorème du point fixe de Banach](#T-TPFB) prouve donc, en sélectionnant
un $\alpha$ adapté, l'unicité d'une fonction continue telle que 
$$
x(t) = x_0 + \int_0^t A \cdot x(s) \, ds
$$
pour tout $t \in [0, T]$. Le problème original admet donc une solution unique.

Localement borné
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-lb-1}
Soit $A$ un sous-ensemble borné de $\R^n$ tel $d(A, \R^n \setminus U) > 0$.
Supposons que $f$ ne soit pas bornée sur $A$ ;
cela signifie qu'on peut trouver une suite de $x_k \in A$ telle que
$|f(x_k)| \to +\infty$ quand $k \to +\infty$. Comme $A$ est borné,
c'est-à-dire si $A \subset K:=\overline{B}(0,r)$ pour un $r > 0$,
par compacité la suite $x_k$ a une sous-suite $y_k$ qui converge vers
un $\ell \in \R^n$.
Comme $d(A, \R^n \setminus U) > 0$ et que 
$d(y_k, \R^n \setminus U) \geq d(A, \R^n \setminus U)$,
en passant à la limite sur $k$ on obtient $d(\ell, \R^n \setminus U)  >0$,
soit $\ell \in U$. Mais $f$ est localement bornée au voisinage de $\ell$,
nous avons donc exhibé une contradiction ; par conséquent, $f$ est bornée
sur $A$.

### Question 2 {.answer #answer-lb-2}
La réponse est non: il suffit de prendre pour $U$ l'ensemble $\R$ privé de $0$
et la fonction $f: U  \to \R$ définie par
$$
f(x) = \left|
\begin{array}{cl}
+1 & \mbox{si } x>0, \\
-1 & \mbox{si } x<0.
\end{array}
\right.
$$
Elle est localement constante, mais pas constante sur l'ensemble 
$A = \{-1, +1\}$ qui est pourtant borné et vérifie
$d(A, \R \setminus U) = d(A, \{0\}) = 1>0$.

Références
============================================================================
