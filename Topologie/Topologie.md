% Topologie

<!-- LaTeX Macros -->
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}

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

Structures Topologiques
================================================================================

### Norme {.definition}
Une *norme* sur un espace vectoriel $E$ est une application
$$\| \cdot \|: E \to \left[0, +\infty\right[$$ telle que
pour tous les points $x$ et $y$ de $E$ et tous les scalaires
$\lambda$ dans $\R$ on ait

 1. [$\|x\| = 0$ si et seulement si $x=0$ (*séparation*)]{#norme-sep},

 2. [$\|\lambda x\| = |\lambda| \|x\|$ (*homogénéité*)]{#norme-homo},

 3. [$\|x+y\| \leq \|x\| + \|y\|$ (*inégalité triangulaire*).]{#norme-ineg}



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

### Sous-ensembles d'espaces vectoriels normés

Si $X$ est un sous-ensemble d'un espace vectoriel normé $E$, 
celui-ci "hérite" de $E$ une mesure de la distance entre 
deux points $x$ et $y$ avec la grandeur 
$$
d(x, y) = \|x - y\|.
$$ 

![Le cercle unité $\{x \in \mathbb{R}^2 \, | \, \|x\|=1\}$.
Bien que $x=(1,0)$ et $y=(0,1)$ appartiennent au cercle unité, 
ni $x+y$ ni $2 \times x$ ne lui appartiennent. Il hérite néanmoins
d'une distance $d$ de l'espace euclien $\mathbb{R}^2$
(telle que $d(x,y) = \|x - y\|_2 = \sqrt{2}$
quand $x=(1,0)$ et $y=(0,1)$),
ce qui fait de lui un espace métrique.](images/circle.tex)

Par contre, à moins que $X$ soit un sous-espace vectoriel de $X$
les additions entre élements de $X$ ou la multiplication d'un 
élément de $X$ n'ont plus de sens dans $X$;
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

 1. [$d(x,y) = d(y,x)$ (*symétrie*)]{#dist-sym},

 2. [$d(x,y) = 0$ si et seulement si $x = y$ (*séparation*)]{#dist-sep},

 3. [$d(x,z) \leq d(x,y) + d(y,z)$ (*inégalité triangulaire*)]{#dist-ineg}.

### Espace Métrique  {.definition}
Un *espace métrique* est un ensemble $X$ muni d'une *distance*.

### Sous-ensemble d'un espace vectoriel normé {.proposition}
Soit $X$ un sous-ensemble d'un espace vectoriel normé $E$. 
La fonction $d: X \times X \to \left[0, +\infty\right[$ 
définie par
$$
d(x, y) := \|x - y\|
$$
est une distance sur $X$.

--------------------------------------------------------------------------------

###

Autrement dit, tout sous-ensemble d'un espace vectoriel normé "est" un
espace métrique, c'est-à-dire qu'il existe une fonction distance
"naturelle" dont on peut le doter, induite par l'espace vectoriel normé.
Cela vaut en particulier pour l'espace vectoriel normé lui-même:
tout espace vectoriel normé "est" un espace métrique.

### Démonstration {.proof}

Par construction, la fonction $d$ est bien positive. 
De plus, pour tous points $x, y$ et $z$ de $X$:

 1. Par [homogénéité de la norme $\| \cdot \|$](#norme-homo), on a
    $$
    \|x - y\| = \|(-1) \times (y-x)\| = |-1| \times \|y - x\| = \|y - x\|,
    $$
    et donc $d(x, y) = d(y, x)$, 
    d'où la [symétrie de la fonction $d$](#dist-sym).

 2. Par l'[axiome de séparation des normes](#norme-sep), 
    $$
    \|x - y\| = 0 \, \Leftrightarrow \, x - y = 0 \, \Leftrightarrow \, x = y.
    $$
    Cela entraîne que $d(x, y) = 0$ si et seulement si $x=y$, 
    soit l'[axiome de séparation pour la distance $d$](#dist-sep).

 3. Par l'[inégalité triangulaire pour les normes](#norme-ineg), on a
    $$
    \|x - z\| = \|x - y - (y - z)\| \leq \|x - y\| + \|y - z\|,
    $$
    ce qui établit l'[inégalité triangulaire pour la distance $d$](#dist-ineg).


### Distance point-ensemble et ensemble-ensemble
Une distance $d$ sur $X$ associe à deux point de $X$ un réel positif.
Cette fonction peut servir de base pour définir une distance entre
un point $x$ de $X$ et un ensembles de points de $A$ de $X$:
$$
d(x, A) := \inf_{a \in A} d(x, A) \in \left[0, +\infty \right]
$$
ou même entre deux ensembles $A$ et $B$ de points de $X$:
$$
d(A, B) = \inf_{a \in A} d(a, B) = \inf_{a \in A} \inf_{b \in B} d(a, b)
\in \left[0, +\infty \right].
$$
Si $A$ est l'ensemble vide, on a $d(x, A) = +\infty$ et si $A$ ou $B$ est
vide on a $d(A, B)= +\infty$; ce sont les seuls cas où ces extensions de
la distance entre points peuvent prendre des valeurs infinies.

### {.ante}
On parle aussi de *métrique* pour désigner une fonction
distance, ce qui explique la terminologie ci-dessous:

### Isométrie {.definition}
Une isométrie $f: X \to Y$ est une fonction définie entre deux espaces
métriques $(X, d_X)$ et $(Y, d_Y)$ telle que:
$$
d_Y(f(x), f(y)) = d_X(x, y)
$$

### {.post}
Les isométries sont les *morphismes* des espaces métriques: 
les applications qui préservent la structure des espaces métriques.
Construire des isométries peut aller de pair avec la construction
d'une métrique sur un ensemble qui en est initialement dépourvu;
voir à ce propos l'exercice "[Droite réelle achevée]"

### TODO

Sous-espace (métrique)

### Structure topologique d'un espace métrique
Il est possible de se livrer un à exercice d'abstraction sur les
espaces métriques en considérant la distance $d(x, A)$ entre un 
point $x$ et un ensemble de points $A$ et en regardant uniquement
si cette grandeur est nulle -- on dira alors que $x$ *adhère* à $A$ -- 
ou strictement positive:
$$
x \mbox{ adhère à } A \, \mbox{ ssi } \, d(x, A) = 0
$$
En faisant de la sorte pour tous les points et ensembles de points
de l'espace métrique et en "oubliant" ensuite la distance qui a permis
cette construction, on remplace une mesure quantitative de proximité
sur l'ensemble par une mesure uniquement qualitative 
(dans ce contexte, "$x$ adhérent à $A$" peut être interprété comme 
"$x$ infiniment proche de $A$ (ou dans $A$)").

### Relation d'adhérence {.definition}

Une *relation d'adhérence* sur l'ensemble *X* est une relation 
entre éléments de $X$ et sous-ensembles de $X$ telle que:

 1. Aucun point n'adhère à de l'ensemble vide,

 2. Tout point d'un ensemble adhère à cet ensemble,

 3. Un point adhère à l'union de deux ensembles 
    si et seulement s'il adhère à l'un ou l'autre 
    des deux ensembles,

 4. Un point qui adhère à l'ensemble des points adhérents 
    à un ensemble adhère à cet ensemble.

### Espace Topologique
Un *espace topologique* est un ensemble muni d'une relation d'adhérence.
Les éléments de l'ensemble sont appelés des *points*, 
ses sous-ensembles des *ensembles de points*.

### Application Continue

Une application continue $f: X \to Y$ est une fonction définie entre deux espaces
topologique telle que lorsque $x$ adhère à $A$ dans $X$, $f(x)$ adhère à $f(A)$
dans $Y$.

### {.post}
Les applications sont les *morphismes* des espaces topologiques:
elle préservent la structure des espaces topologiques.

### Les espaces métriques sont des espaces topologiques

Soit $X$ un espace métrique muni d'une distance $d$. 
La relation définie par
$$
x \mbox{ adhère à } A \, \Leftrightarrow \, d(x, A) = 0
$$
est une relation d'adhérence sur $X$.

### Démonstration 

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

 3. Si $x$ est proche de $A$, c'est-à-dire si $d(x,A)=0$, alors
    $$
    0 \leq d(x, A \cup B) = \inf_{y \in A \cup B} d(x, y)
    \leq  \inf_{y \in A} d(x, y) = d(x, A)= 0
    $$
    et donc $x$ est proche de $A \cup B$.
    De la même façon, du fait de la symétrie des rôles des ensembles $A$ et $B$,
    si $x$ est proche de $B$ alors $x$ est proche de $A \cup B$.

    Réciproquement, si $x$ est proche de $A \cup B$, alors il existe une
    suite de points $x_k$ de $A \cup B$ telle que $d(x, x_k) \to 0$
    quand $k \to +\infty$. Cette suite $x_k$ admet une suite extraite
    de points de $A$ et/ou une suite extraite de points de $B$.
    Dans le premier cas on a donc $d(x, A)=0$ et dans le second $d(x, B)=0$,
    c'est-à-dire que $x$ est proche de $A$ et/ou proche de $B$.

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
    et comme $\varepsilon >0$ est arbitraire, $d(x, A)=0$: $x$ adhère à $A$.

### TODO

Rq comme quoi espace métrique et sous-ensemble d'un evn sont 
similaires (métrique n'est "pas plus général"), mais que ça
n'est pas le cas pour les espaces topo (il existe de espace
topologiques non métrisables)

### Calcul Topologique
Une fonction $\overline{\, \cdot \,}: \mathcal{P}(E) \to \mathcal{P}(E)$ est 

 1. $\overline{\varnothing} = \varnothing$,

 2. $A \subset \overline{A}$,

 3. $\overline{A \cup B} = \overline{A} \cup \overline{B}$,

 4. $\overline{\overline{A}} = \overline{A}$.


### TODO

Sous-espace (topologique)

Produit (et Quotient?)
--------------------------------------------------------------------------------

(rk: Quotient ne "marche pas" dans une simple structure métrique)

Continuité et Limite
================================================================================

### TODO 

(que dire sur limite ? Cadre général exclu ici ...
Au minimum, indispensable limite de suite. 
Qui du reste ? fonctions $X \to Y$, etc ? 
Montrer en exercice que des cas "limite en $\infty$" se ramènent à ça ?
L'idée que la notion de limite peut tjs être ramenée à une limite de
type limite vers un point est intéressante.)

### Limite d'une suite {.definition}
Une suite $x_k$ de valeurs d'un espace métrique $X$ est *convergente*
si elle a une *limite*, c'est-à-dire un élement de $x$ de $X$
dont $x_{k}$ soit arbitrairement proche à partir d'un certain rang,
c'est-à-dire vérifiant: pour tout $\varepsilon > 0$, il existe un entier $n$ 
tel que pour tout $k \geq n$, on ait $\|x_k - x\| \leq \varepsilon$.

### Unicité de la limite {.proposition}
Si une suite $x_k$ admet une limite, celle-ci est unique.

### Démonstration {.proof}
Par l'inégalité triangulaire, pour tout entier $k$ on a
$$
\|x - x'\| \leq \|x - x_k\| + \|x' - x_k\|.
$$
Les points $x$ et $x'$ étant deux limites de $x_k$, 
pour tout $\varepsilon > 0$, il existe des rangs $n$ et $n'$ tels que
lorsque $k \geq n$ et $k\geq n'$, on a $\|x - x_k\| \leq \varepsilon /2$
et $\|x' - x_k\| \leq \varepsilon /2$. Par conséquent, pour 
$k = \max(n, n')$, on a
$\|x - x'\| \leq \varepsilon$. La valeur $\varepsilon > 0$ étant arbitraire,
on en déduit que $\|x - x'\|= 0$, soit par séparation, $x=x'$.

### TODO

Pb / pt dans l'adhérence de la fct (cf prg prépa).

### Limite d'une fonction en un point {.definition}

Soit $f:X \subset E \to Y$ une application définie sur un sous-ensemble $X$
d'un espace vectoriel normé $E$ et à valeurs dans un espace métrique $Y$.
Soit $x$ un point de l'adhérence de $X$ dans $E$. 
Le point $\ell \in Y$ est la *limite* de $f$ en $x$ si pour toute suite
$x_k$ de points de $X$ convergeant vers $x$, on a 
$\lim_{k \to +\infty} f(x_k) = \ell$.

Bestiaire
================================================================================

**TODO**

  - ouvert, fermé, voisinage, compact (?), adhérence, intérieur, frontière

  - point isolé, d'accumulation, ensemble dense, etc.

**TODO.** Partir de la notion de limite, définir l'adhérence, et le reste
à partir de ça, puis "découvrir" les définitions "directes"/séquentielles.

### Définitions séquentielles {.definition}

Soit $X$ un espace métrique et $A$ un ensemble de points de $X$.

  - Un point *adhère* à un ensemble $A$ s'il existe une suite de
    points de $A$ qui converge vers ce point.

  - Un ensemble $A$ est *fermé* si la limite de toute suite de points de $A$
    qui est convergente dans $X$ appartient à $A$.

  - Un point est *frontière* de $A$ s'il existe une suite de points de $A$
    qui converge vers ce point et une suite de points du complémentaire de $A$
    qui converge vers ce point.

  - Un point $x$ est *intérieur* à un ensemble $A$ si toute
    suite convergeant vers $x$ appartient à $A$ à partir d'un certain rang.

  - Un ensemble $V$ est un *voisinage* d'un point $x$ de $X$ si toute
    suite convergeant vers $x$ appartient à $V$ à partir d'un certain rang.

  - Un ensemble $A$ est *ouvert* si tout suite de points de $X$ 
    qui converge vers un point de $A$ appartient à $A$ 
    à partir d'un certain rang.

### TODO

Notation $\mathcal{V}(x)$ pour les voisinages de $x$.

### Ensembles dérivés {.definition}

Soit $A$ un ensemble de $X$. On note

  -  $\overline{A}$ l'*adhérence* de $A$ 
     (composée de l'ensemble des points adhérents à $A$).

  - $\partial A$ la *frontière* de $A$ (composée de 
    l'ensemble des points frontières de $A$).

  - $\mathring{A}$ l'*intérieur* de $A$ (composé de
    l'ensemble des points intérieurs à $A$).


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
    d(x, X \setminus A) > 0.
    $$

  - Un ensemble $A$ est *ouvert* si la distance de tout point de $A$
    au complémentaire de $A$ est strictement positive:
    $$
    A = \mathring{A}
    \; \Leftrightarrow \; 
    (x \in A \Rightarrow d(x, X \setminus A)=0).
    $$


  

Complétude
================================================================================

### Point fixe {.definition}
Soit $f: X \to X$ une application d'un ensemble $X$ dans lui-même.
Un élément $x \in X$ est un *point fixe* de $f$ si $x = f(x)$.
 
### Points fixes et zéros
Etre un point fixe d'une fonction $f: X \to X$, c'est donc être déterminé 
**implicitement** par l'équation $x = f(x)$. Si $X$ est un sous-espace
d'un espace vectoriel,
cela équivaut à dire que $x$ est une solution de l'équation $x - f(x) = 0$,
soit un *zéro* (appelé également une *racine*) de la fonction 
$x \in X \mapsto x - f(x)$.

La démarche inverse 
-- qui consiste à caractériser les solutions d'une équation 
comme des point fixes -- peut être utile pour établir des résultats
d'existence et d'unicité des solutions ou obtenir des méthodes numériques 
pour leur calcul. Un exemple élémentaire de ce type de transformation:
le nombre d'or est déterminé comme l'unique solution de l'équation
$$
x^2 = x + 1 = 0, \; x > 0
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
On se reportera à l'exercice "[Le nombre d'or]" pour prolonger l'étude de
cet exemple particulier.

![Le nombre d'or comme point fixe de $x \mapsto 1 + 1/x$.](images/fixed-point.tex){#golden-ratio}

### Algorithmes et critères de convergence

Dans un algorithme (idéalisé) de calcul d'une suite de valeurs numériques,
il n'est pas évident d'établir un critère de convergence
qui garantisse exactement que la suite calculée ait une limite,
quand cette limite potentielle est inconnue.

Vérifier que $|x_{k+1} - x_k| \to 0$ par exemple est insuffisant comme
en atteste la suite des $x_k = 1 / (k+1)$. 
Vérifier que la suite  $\sum_{j=0}^{k} |x_{i+1} - x_i|$ reste bornée 
va bien garantir la convergence, mais va par contrer rejeter des suites convergentes 
telle que  $x_k = \sum_{j=0}^{k} (-1)^j / (j+1)$.
Un critère plus adapté serait d'examiner le développement décimal de 
$x_k$ et de vérifier que quel que soit le nombre de décimales souhaité
après la virgule, le développement de $x_k$ finit par se stabiliser au-delà 
d'un certain rang $m$ (qui dépend du nombre de décimales). 
Mais là aussi, il existe des cas pathologiques qui convergent 
sans respecter le critère, comme la suite des $x_k = 1 + (-1)^k 2^{-k}$, 
dont le développement avec 0 décimales après la virgule oscille indéfiniment 
entre $0$ et $1$. 

C'est la notion de suite de Cauchy qui capture le bon critère;
pour une suite numérique (à valeurs réelles ou dans $\R^n$) 
être de Cauchy -- ou passer le test de Cauchy ou encore 
vérifier le critère de Cauchy -- est équivalent à être convergente.

### Suite de Cauchy {.definition}
Une suite de points $x_k$ d'un espace métrique $X$ est *de Cauchy* si pour tout
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
de limite $x_{\infty}$. Soit $\varepsilon > 0$; il existe un rang
$m$ au-delà duquel on a 
$d(x_k, x_{\infty}) \leq \varepsilon / 2.$
Par conséquent, si $n \geq m$ et $p\geq m$, 
$$
d(x_n, x_p) \leq d(x_n, x_{\infty}) + d(x_{\infty}, x_p) \leq \varepsilon.
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
Un espace métrique $X$ est *complet* si et seulement si tout suite de Cauchy
est convergente. Un espace vectoriel normé $E$ complet est qualifié
d'*espace de Banach[^Banach]*.

[^Banach]: d'après [Stefan Banach](https://en.wikipedia.org/wiki/Stefan_Banach), 
un mathématicien polonais du 20ème siècle d'après lequel sont nommés
[de nombreux concepts et théorèmes](https://en.wikipedia.org/wiki/List_of_things_named_after_Stefan_Banach).

### Complétude de l'espace euclien {.proposition}

L'espace $\mathbb{R}^n$ est complet.

### Démonstration {.proof}

Dans les cas de $\R$ (c'est-à-dire quand $n=1$), 
le résultat est une conséquence directe de la 
construction de $\R$ comme complété de $\Q$[^ahahah].
Pour des valeurs de $n > 1$, si $x_k$ est une suite de Cauchy,
ses composantes $x_k^1, \dots, x_k^n$ sont aussi de Cauchy car
pour tout $i \in \{1, \dots, n\}$,
$$
|x_n^i - x_p^i| \leq \left\|x_n - x_p\right\|.
$$
Comme $\mathbb{R}$ est complet, chaque suite $x_k^i$ admet donc une limite,
notée $x^i_{\infty}$. 
Si l'on note $x_{\infty} = (x_{\infty}^1, \dots, x_{\infty}^n)$,
on déduit de l'égalité
$$
\|x_k - x_{\infty}\| = \sqrt{\sum_{i=1}^n (x_k^i - x_{\infty}^i)^2}
$$
la convergence de $x_k$ vers $x_{\infty}$. 
Toute suite de Cauchy de $\R^n$ est donc convergente.

[^ahahah]: bien sûr si l'on a utilisé une technique alternative pour
construire $\R$, par exemple par les coupures de Dedekind, il faut en
faire la démonstration.

### Complétude de l'espace des fonctions bornées {.proposition}

Soit $X$ un ensemble et $Y$ un espace métrique complet.
L'ensemble des fonctions $f$ de $X$ dans $Y$ bornées
-- c'est-à-dire telles que $\sup_{x \in X} d(0, f(x))$ soit fini --
muni de la distance de la convergence uniforme
$$
d(f, g) := \sup_{x \in X} d(f(x), g(x)))
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
= \lim_{m \to +\infty} d(f_n(x), f_m(x)) 
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
Une fonction $f: X \to X$ est *$\kappa$-contractante*, 
où $\kappa \in \left[0, 1\right[$,
si pour tout couple de points $x$ et $y$ de $X$, on a 
$$
d(f(x), f(y)) \leq \kappa d(x, y).
$$
Une telle application est *contractante* si elle est 
$\kappa$-contractante pour un $\kappa \in \left[0, 1\right[$.

### Théorème de Point Fixe de Banach {.definition .theorem #T-TPFB}

Soit $f: E \to E$ une application contractante dans un espace métrique $E$ complet.
L'application $f$ admet un unique *point fixe* $x$,
c'est-à-dire une unique solution $x \in E$ à l'équation
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
d(x_{n+2}, x_{n+1}) = d(f(x_{n+1}), f(x_n)) \leq \kappa d(x_{n+1}, x_n),
$$
ce qui par récurrence fournit pour tout $n$
$$
d(x_{n+1}, x_n) \leq \kappa^n d(x_1, x_0).
$$
Par conséquent, pour tout couple d'entiers $n$ et $p$, on a
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

### Compacité Séquentielle {.definition}
Un ensemble $K$ d'un espace métrique est *compact (séquentiellement)* 
si toute suite de valeurs de $K$ admet une sous-suite qui converge dans $K$.

### Théorème de Heine-Borel {.theorem}
Un ensemble $K$ de l'espace euclidien $\R^n$ est compact 
si et seulement si il est fermé et borné.

### Démonstration {.proof}

Supposons $K$ compact; soit $x_k$ une suite de points de
$K$ qui converge dans $\R^n$, vers une limite notée $x_{\infty}$. 
Il existe alors une sous-suite $y_k$ de $x_k$ qui converge dans $K$;
or comme cette sous-suite a la même limite que $x_k$, $x_{\infty}$ 
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
complet, elle converge vers un point $y_{\infty}$. L'ensemble $K$ étant
fermé par hypothèse, cette limite appartient à $K$. L'ensemble $K$ est
donc compact.

[^cover]: par exemple des pavés de la forme 
$$[i_1 \varepsilon, (i_1+1)\varepsilon] \times \dots \times [i_n \varepsilon, (i_{n+1} \varepsilon)]
\, \mbox{ où } \, (i_1,\dots, i_n) \in \Z^n,$$
dont le diamètre est $\varepsilon \sqrt{2} n$.


### Image d'un compact {.theorem}
L'image d'un ensemble compact par une application continue est un ensemble
compact.

### Démonstration {.proof}

Soit $f: K \subset X \to Y$ où $X$ et $Y$ sont deux espaces métriques 
et $K$ un sous-ensemble compact de $X$. 
Soit $y_k$ une suite de points de $f(K)$; par construction, 
il existe une suite de points $x_k$ de $K$ tels que $f(x_k) = y_k$. 
Soit $z_k$ une sous-suite de $x_k$ qui converge dans
$K$ vers un $z_{\infty} \in K$; 
par continuité de $f$, la suite des $f(z_k)$
-- qui est une suite extraite des $y_k$ -- 
converge vers $f(z_{k}) \in f(K)$. 
L'ensemble $f(K)$ est donc compact.

### Existence d'un minimum {.corollary #T-EM}
Une fonction continue $f: K \to \mathbb{R}$ définie sur un ensemble compact 
$K$ admet un minimum global.

### Démonstration {.proof}
Soit $x_k \in K$ une suite minimisante de $f$, c'est-à-dire telle que
$$
\lim_{k \to +\infty} f(x_k) = \inf_{x \in K} f(x).
$$
Il existe une suite $y_k$ extraite de $x_k$ qui converge vers un point
$y_{\infty}$ de $K$. Par continuité de $f$ en $y_{\infty}$, on a
$$
f(y_{\infty}) = \lim_{k \to +\infty} f(y_k) = \inf_{x \in K} f(x).
$$
La fonction $f$ admet donc un minimum en $y_{\infty}$.

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

### TODO -- Démonstration {.proof}

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
dont l'intersection est non-vide. 
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
vérifie $d(x_i, x_j) \geq \varepsilon$ si $i\neq j$; si cette suite
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

### TODO

  - distance fermé compact

  - continuité application linéaire $\mathbb{R}^n \to Y$.

  - Fct continue sur compact est uniformément continue.

  - Ens des fcts $C^0$ sur un compact est un espace de Banach.

  - Inclure ici élts dim infinie ?  Non, calcul diff 3


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

Annexe
================================================================================

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
devient un *espace euclien*; la norme associée vérifie
$$
\|x\| = \sqrt{x_1^2 +\dots + x_n^2}.
$$

Exercices
================================================================================

Droite réelle achevée
--------------------------------------------------------------------------------

La droite réelle achevée est composée des nombre réels de $-\infty$ 
et de $+\infty$.
Le but de cet exercice est de doter cet ensemble 
$\mathbb{R} \cup \{-\infty, +\infty\}$[^nre] d'une distance aux propriétés
"raisonnables".
A cette fin, on introduit l'espace métrique $X$ des points du cercle unité de 
$\mathbb{R}^2$ d'ordonnée positive ou nulle:
$$
X = 
\left\{
(x, y) \in \mathbb{R}^2 \, \left| \, \sqrt{x^2+y^2} = 1 \right. \mbox{ et } y \geq 0
\right\},
$$
muni de la distance euclidienne de $\mathbb{R}^2$
et la fonction $f: X \to \mathbb{R} \cup \{-\infty, +\infty\}$ définie par
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
de $\mathbb{R}$ dans lui-même, une autre interprétation selon laquelle 
$\overline{\mathbb{R}} = \mathbb{R}$. 

### Question 1 {.question #dra-1}

Pouvez-vous donner une interprétation géométrique simple à la grandeur
calculée par la fonction $f$ ?

![Construction d'une métrique pour la droite réelle achevée.](images/extended-real-numbers.tex)

$\to$ [Solution](#a-dra-1)

### Question 2 {.question #dra-2}

Montrer que $f$ est une bijection.

$\to$ [Solution](#a-dra-2)

### Question 3 {.question #dra-3}

En déduire qu'il existe une et une seule fonction distance sur
$\mathbb{R} \cup \{-\infty, +\infty\}$ qui fasse de $f$ une isométrie;
on note $d^{\pm \infty}$ cette distance. 

$\to$ [Solution](#a-dra-3)

### Question 4 {.question #dra-4}

(Optionnel) 

Calculer $d^{\pm \infty}(0, +\infty)$, $d^{\pm \infty}(-\infty, +\infty)$, 
$d^{\pm \infty}(-1, 1)$.

$\to$ [Solution](#a-dra-4)

### Question 5 {.question #dra-5}

Montrer que l'injection canonique
$x \in \mathbb{R} \mapsto x \in \mathbb{R} \cup \{-\infty, +\infty\}$
est une fonction continue.

$\to$ [Solution](#a-dra-5)

### Question 6 {.question #dra-6}

Yoda a dit "deux façons d'interpréter $x_k \to +\infty$ désormais il y a".
Qu'est-ce qu'il a voulu dire ? Est-ce que c'est un problème ?

$\to$ [Solution](#a-dra-6)

### Question 7 {.question #dra-7}

(Optionnel) 

Suggérer une variante de la construction précédente pour
doter l'ensemble $\mathbb{R} \cup \{\infty\}$ ($\infty$ sans signe:
ni $+$, ni $-$) d'une métrique $d^{\infty}$ 
telle que $d^{\infty}(x_k, \infty) \to 0$ si et seulement si
$|x_k| \to +\infty$.
    
 $\to$ [Solution](#a-dra-7)
   
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

$\to$ [Solution](#a-lf-0)

### Question 1 {.question #lf-1}
Montrer que dans $\R$, l'intervalle $\left[0, 1\right[$ est localement 
fermé et que l'image de toute suite convergente est localement fermée. 
Donner un exemple de sous-ensemble de $\mathbb{R}$ qui ne soit pas 
localement fermé.

$\to$ [Solution](#a-lf-1)

### Question 2 {.question #lf-2} 
Montrer que tout ensemble fermé est localement fermé, mais aussi que tout
ensemble ouvert est localement fermé. 
Montrer que l'intersection de deux ensembles localement fermés est 
localement fermé.

$\to$ [Solution](#a-lf-2)

### Question 3 {.question #lf-3}
Montrer qu'un ensemble est localement fermé si et seulement s'il est
l'intersection d'un ensemble fermé et d'un ensemble ouvert.

$\to$ [Solution](#a-lf-3)

Comparaison des normes
--------------------------------------------------------------------------------

TODO: comparaison manuelle, meilleure bornes

Distance entre ensembles
--------------------------------------------------------------------------------

Soit $A$ et $B$ deux ensembles compacts non vides de $\mathbb{R}^n$; 
on souhaite évaluer à quel point les deux ensembles diffèrent
-- en mesurant à quelle distance les points de $A$ peuvent 
être éloignés de l'ensemble $B$ et réciproquement.

### Question 1 {.question #dh-1}

Est-ce que la distance entre ensembles classique
$$
d(A, B) = \inf_{a \in A} d(a, B) = \inf_{a\in A}\inf_{b \in B} d(a, b)
$$
fait l'affaire ?

$\to$ [Solution](#a-dh-1)

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

$\to$ [Solution](#a-dh-2)

### Question 3 {.question #dh-3}

Cette terminologie de "distance" de Hausdorff est-elle légitime ?

$\to$ [Solution](#a-dh-3)

### Question 4 {.question #dh-4}

La somme de Minkowksi de deux ensembles $A$ et $B$ est définie comme
$$
A + B = \{a + b \, | \, a \in A, \, b \in B \}.
$$
Vérifier que la somme de Minkowski de deux ensembles compacts non vides de 
$\R^n$ est un ensemble compact non vide de $\R^n$.
Cette opération est-elle continue pour la distance de Hausdorff ?

$\to$ [Solution](#a-dh-4)


Plongement de Kuratowski
--------------------------------------------------------------------------------

Nous souhaitons établir le résulat suivant: tout espace métrique peut être
identifié à un sous-ensemble d'un espace vectoriel normé tout en préservant 
sa distance.

Soit $X$ un espace métrique et $x_0$ un point de $X$. 
On associe à l'élément $x$ de $X$ la fonction $f_x: X \to \R$ définie
par
$$
f_x(y) = d(x, y) - d(x_0, y).
$$

### Question 1 {#pk-1 .question}

Montrer que la fonction $x \mapsto f_x$ est injective.

$\to$ [Solution](#a-pk-1)


### Question 2 {#pk-2 .question}

Montrer que pour tout point $x$ la fonction $f_x$ est bornée.

$\to$ [Solution](#a-pk-2)

### Question 3 {#pk-3 .question}

Montrer que l'espace vectoriel $E$ des fonctions bornées de $X$ dans 
$\mathbb{R}$ est un espace vectoriel qui peut être muni de la norme 
$\| \cdot \|_{\infty}$ définie par
$$
\|f\|_{\infty} = \sup \, \{|f(y)| \, | \, y \in X\}.
$$

$\to$ [Solution](#a-pk-3)

### Question 4 {#pk-4 .question}

Montrer que $x \mapsto f_x$ est une isométrie, 
c'est-à-dire que pour tout $x$ et $y$ dans $X$, on a 
$$
d(x, y) = \|f_x - f_y\|_{\infty}.
$$

$\to$ [Solution](#a-pk-4)

Le nombre d'or
--------------------------------------------------------------------------------

**TODO**

Spirale d'Euler 
--------------------------------------------------------------------------------

La spirale d'Euler est la courbe paramétrée du plan déterminée 
pour $t\geq 0$ par les coordonnées
$$
x(t) = \int_0^t \cos s^2 \, ds \, \mbox{ et } \, \, y(t) = \int_0^t \sin s^2 \, ds
$$


![Spirale d'Euler ($0 \leq t \leq 5$)](images/euler.py)

Nous souhaitons établir que cette spirale à un point limite quand 
$t \to +\infty$[^euler].

### Question 1 {.question #se-1}

Montrer que si pour toute suite de valeurs $t_k$ tendant vers l'infini, 
la suite de points de coordonnées $(x_k, y_k) := (x(t_k), y(t_k))$ 
à une limite dans le plan
-- limite qui peut dépendre a priori de la suite $t_k$ -- 
alors le point de coordonnées $(x(t), y(t))$ a une limite dans le plan 
quand $t$ tend vers $+\infty$.

$\to$ [Solution](#a-se-1)


### Question 2 {.question #se-2}

Montrer que pour tout couple $(a,b)$ de réels strictement positifs,
les grandeurs
$$
I(a, b) :=
\int_{a}^{b} \cos s^2 \, ds
\mbox{ et }
J(a, b) := \int_{a}^{b} \sin s^2 \, ds
$$
vérifient pour un réel $\alpha > 0$ les inégalités
$$
|I(a, b)| \leq \frac{\alpha}{\sqrt{\min(a, b)}}
\, \mbox{ et } \,
|J(a, b)| \leq \frac{\alpha}{\sqrt{\min(a, b)}}.
$$

$\to$ [Solution](#a-se-2)

### Question 3 {.question #se-3}

Conclure.

$\to$ [Solution](#a-se-3)


[^euler]: cette courbe a été introduite par Euler en 1744. 
Il lui apparait alors manifeste que la courbe est une spirale qui s'enroule 
après un nombre de tours infinis autour d'un centre bien défini, 
mais que ce point est très difficile à déterminer par cette construction. 
Il faudra attendre 1781 pour
qu'Euler puisse calculer analytiquement les coordonnées de ce point 
(cf. @Lev08).


Séries Absolument Convergentes
--------------------------------------------------------------------------------

**TODO:** définition "limite dans tous les sens" d'une série double et 
jouer avec Cauchy ?


Point fixe
--------------------------------------------------------------------------------

**TODO:** exemple introductif (simple, matriciel $2\times2$)

Soit $f: E \to E$ une fonction définie et à valeurs dans un espace métrique 
complet $E$ pour laquelle il existe un entier $n \geq 1$ tel que la composée 
$n$ fois de $f$ avec elle-même, notée $f^n$, est contractante. 

On souhaite montrer que sous ces hypothèses 
-- qui généralisent celles du [théorème de point fixe de Banach](#T-TPFB) -- 
$f$ admet encore un unique point fixe.

### Question 1 {.question #pf-1}

Montrer que tout point fixe éventuel de $f$ est également 
un point fixe de $f^n$.

$\to$ [Solution](#a-pf-1)

### Question 2 {.question #pf-2}

Montrer que $f^n$ admet un unique point fixe et qu'il est également
un point fixe de $f$.

$\to$ [Solution](#a-pf-2)

### Question 3 {.question #pf-3}

Montrer que le procédé habituel pour construire un point 
fixe de $f$ est toujours valable quand $f^n$ est contractante.

$\to$ [Solution](#a-pf-3)

Normes d'opérateurs
--------------------------------------------------------------------------------

Changer les normes au départ et à l'arrivée, calculer les normes d'opérateurs
associées sur la base d'une représentation matricielle (ex: norme sup au 
départ et à l'arrivée)

En lien avec les résolutions itératives de systèmes linéaires,
utiliser / montrer que pour tout $A \in \R^{n\times n}$
et tout $\varepsilon > 0$, il existe une norme matricielle 
$\|\, \cdot \, \|$ telle que $\|A\| \leq \rho(A) + \varepsilon$.

Voir aussi <https://math.stackexchange.com/questions/126460/iteration-convergence>

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
     la collection $\mathcal{A}$ peut-on ajouter pour s'assurer du résultat ?

  2. Application angle sur l'hélice et $\arctan$ ...


Equations Linéaires et Point Fixes
--------------------------------------------------------------------------------

Préparer et résoudre numériquement des systèmes de la forme $A x = b$ dans
des cas simples (ex: Jacobi, Gauss-Seidel, cas diagonally dominant ?).

Exemples concrets (ex: Poisson Image editing) et exemples ou "ça ne marche pas"
en itérant sans s'assurer du caractère contractant. 

Prendre un exemple de petite dimension associé au PIE; admettre le résultat
que $\|A^k\| \to 0 \Leftrightarrow \rho(A) < 1$ et tester algo de Jacobi
(Au préalable, calculer norme de l'opérateur via la svd ?).

Lien norme d'opérateur et rayon spectral ??? Cf supra sur rayon spectral
et lien avec norme.

Equa Diff
--------------------------------------------------------------------------------

Pt fixe associé à l'équation différentielle $\dot{x} = A(t) \cdot x$?
Et solution itérative ? Avec norme custom ?

"Localement"
--------------------------------------------------------------------------------

Etude des pptés "localement X" pour X=bornée, positive (ex: distance), 
coup de la stabilité asympt (localt equi-convergente ?), 
localement unift continue, etc.
et comment elle s'étendent à un ensemble d'adhérence compacte 
("compactement inclus" dans l'espace de référence).

"Contre-exemples" ? Avec "localement constant", "localement polynomial", 
"localement lipschitz", fct "localement définie", etc., opérations 
qui ne sont pas stables par union finie. 

Compacité et Continuité
--------------------------------------------------------------------------------

Montrer la réciproque du [résultat d'existence d'un minimum pour une fonction
numérique continue définie sur un compact](#T-EM):
si l'ensemble $E \subset \mathbb{R}^n$ n'est pas compact, 
il existe une fonction continue $f: E \to \mathbb{R}$ 
n'ayant pas de minimum.



Fonctions propres
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

Solutions aux Exercices
================================================================================

Solution -- [Localement fermé]
--------------------------------------------------------------------------------

### Solution à la [question 0](#lf-0) {.answer #a-lf-0}

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

### Solution à la [question 1](#lf-1) {.answer #a-lf-1}

Soit $x \in A:=\left[0, 1\right[$; 
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


### Solution à la [question 2](#lf-2) {.answer #a-lf-2}

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

### Solution à la [question 3](#lf-3) {.answer #a-lf-3}

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
ensemble fermé $F$; de l'équation ci-dessus on déduit donc
que $A = V \cap F$ où $V$ est ouvert dans $X$ et $F$ est fermé dans $X$.

TODO -- Solution -- [Droite réelle achevée]
--------------------------------------------------------------------------------

### TODO -- Solution à la [question 1](#dra-1) {.answer #a-dra-1}

### TODO -- Solution à la [question 2](#dra-2) {.answer #a-dra-2}

### TODO -- Solution à la [question 3](#dra-3) {.answer #a-dra-3}

### TODO -- Solution à la [question 4](#dra-4) {.answer #a-dra-4}

### TODO -- Solution à la [question 5](#dra-5) {.answer #a-dra-5}

### TODO -- Solution à la [question 6](#dra-6) {.answer #a-dra-6}

### TODO -- Solution à la [question 7](#dra-7) {.answer #a-dra-7}

 
Solution -- [Distance entre ensembles]
--------------------------------------------------------------------------------

### Solution à la [question 1](#dh-1) {.answer #a-dh-1}

Non, la distance usuelle $d(A,B)$ en convient pas.
En effet, cette distance est nulle dès que l'intersection de $A$ et $B$
est non vide, même si des points de $A$ sont très éloignés de $B$.

### Solution à la [question 2](#dh-2) {.answer #a-dh-2}

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

### Solution à la [question 3](#dh-3) {.answer #a-dh-3}

Vérifions que la "distance" de Hausdorff est effectivement une distance
sur l'espace des sous-ensembles compacts de $R^n$.

 1. Axiome de symétrie. Il est clair par construction que pour tous les
    ensembles compacts non vide $A$ et $B$ de $\R^n$, on a $d[A, B] = d[B, A]$.

 2. Axiome de séparation. Si $$d[A, B] = \max(\sup_{a \in A} d(a, B), \sup_{b \in B} d(b, A)) = 0,$$
    alors pour tout $a \in A$, $d(a, B) = 0$ et pour tout $b \in B$, 
    $d(b, A) = 0$, c'est-à-dire $a \in \overline{B}$ et $b \in \overline{A}$.
    Par conséquent, puisque $A$ et $B$ sont fermés, 
    $A \subset \overline{B} = B$ et $B \subset \overline{A} = A$
    et donc $A = B$.

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
    
### Solution à la [question 4](#dh-4) {.answer #a-dh-4}

Si $A$ et $B$ sont des ensembles non vides de $\R^n$, $A+B$ est clairement
non vide. Si de plus $A$ et $B$ sont compacts, et que l'on considère une
suite $x_k$ de points de $A+B$, alors il existe des $a_k$ de $A$ 
et $b_k$ de $B$ tels que $x_k = a_k + b_k$. Par compacité de $A$, 
il existe une suite $a_{\sigma(k)}$ 
-- où $\sigma: \N \to \N$ est croissante --
qui converge vers un $a \in A$;
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
&=
\sup_{a \in A} \sup_{b \in B} \inf_{c \in C} \inf_{d \in D}
\|a - c\| + \|b - d\| \\
&= \sup_{a \in A} \inf_{c \in C} 
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

Solution -- [Plongement de Kuratowski]
--------------------------------------------------------------------------------

### Solution à la [question 1](#pk-1) {#a-pk-1}

Soit $x$, $x'$ deux points de $X$. Pour tout $y$ dans $X$ on a:
$$
\begin{split}
f_x(y) - f_{x'}(y) &= d(x, y) - d(x_0, y) - (d(x', y) - d(x', x_0))\\
&= d(x, y) - d(x', y),
\end{split}
$$
par conséquent, si $f_x = f_{x'}$, on a en particulier
$f_x(x') = f_{x'}(x')$, soit $d(x, x') - d(x', x') = d(x, x') = 0$, 
c'est-à-dire $x = x'$.

### Solution à la [question 2](#pk-2) {#a-pk-2}

**TODO** Montrer que pour tout point $x$ la fonction $f_x$ est bornée.

### Solution à la [question 3](#pk-3) {#a-pk-3}

 **TODO** Montrer que l'espace vectoriel $E$ des fonctions bornées de $X$ dans 
$\mathbb{R}$ est un espace vectoriel qui peut être muni de la norme 
$\| \cdot \|_{\infty}$ définie par
$$
\|f\|_{\infty} = \sup \, \{|f(y)| \, | \, y \in X\}.
$$

### Solution à la [question 4](#pk-4) {#a-pk-4}

**TODO** Montrer que $x \mapsto f_x$ est une isométrie, 
c'est-à-dire que pour tout $x$ et
$y$ dans $X$, on a 
$$
d(x, y) = \|f_x - f_y\|_{\infty}.
$$

Solution -- [Spirale d'Euler]
--------------------------------------------------------------------------------

### Solution à la [question 1](#se-1) {.answer #a-se-1}

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

### Solution à la [question 2](#se-2) {.answer #a-se-2}

Nous traitons le cas de $I(a, b)$, celui de $J(a, b)$ étant similaire.
Pour tout $a$ et $b$ strictement positifs,
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
\frac{5}{2 \sqrt{a}} + \frac{5}{2 \sqrt{b}} \leq \frac{5}{\sqrt{\min(a, b)}}.
$$

### Solution à la [question 3](#se-3) {.answer #a-se-3}

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



Solution -- [Point fixe]
--------------------------------------------------------------------------------

### Solution à la [question 1](#pf-1) {.answer #a-pf-1}

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

### Solution à la [question 2](#pf-2) {.answer #a-pf-2}

La fonction itérée $f^n$ satisfait les hypothèses du 
[théorème du point fixe de Banach](#T-TPFB), par conséquent elle
admet un point fixe $x$. Comme $f^n(x) = x$, en applicant $f$ aux
deux membres de cette équation, on obtient 
$$
f(f^n(x)) = f^n(f(x)) = f(x).
$$
Par conséquent, $f(x)$ est un point fixe de $f^n$. 
C'est donc l'unique point fixe $x$ de $f^n$; on a donc $f(x) = x$,
c'est-à-dire que $x$ est un point fixe de $f$. 

### Solution à la [question 3](#pf-3) {.answer #a-pf-3}

Le "procédé habituel pour construire un point fixe de $f$" 
consiste à prendre un $x_0 \in E$ quelconque et à construire 
par récurrence la suite des $x_{k+1} = f(x_k)$. 
On souhaite donc montrer que cette suite converge vers l'unique point fixe 
$x$ de $f$. 
La fonction $f^n$ satisfaisant les hypothèses du
[théorème du point fixe de Banach](#T-TPFB), 
on sait que la suite extraite
$(x_{kn})_k$ converge vers $x$, car $x_{(k+1)n} = f^n(x_{kn})$.
Il en est de même pour la suite extraite $(x_{kn+1})_k$, construite
à partir du même procédé mais en initialisant la séquence avec 
la valeur $x_1$, pour la suite $(x_{kn+2})_k$, ..., jusqu'à 
$(x_{kn + (n-1)})_k$. Ces $n$ suites convergent toutes vers $x$,
donc la suite des $(x_k)_k$ converge également vers le point fixe $x$, 
comme sous les hypothèses du [théorème du point fixe de Banach](#T-TPFB).


Références
============================================================================
