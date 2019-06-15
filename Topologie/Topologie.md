% Topologie

\newcommand{\R}{\mathbb{R}}

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

### TODO

Remarque scalaires réels, extension plus tard au cas complexe.

### Norme {.definition}
Une *norme* sur un espace vectoriel $E$ est une application
$$\| \cdot \|: E \to \left[0, +\infty\right[$$
qui vérifie les trois axiomes suivants:

  - Séparation: $\|x\| = 0$ si et seulement si $x=0$,

  - Homogénéité: $\|\lambda x\| = |\lambda| \|x\|$ pour tous $\lambda \in \mathbb{R}$ et $x \in E$,

  - Inégalité triangulaire (subadditivité): $\|x+y\| \leq \|x\| + \|y\|$ pour tous $x \in E$ et $y \in E$.

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

### Sous-ensembles d'espaces vectoriels normés

Si $X$ est un sous-ensemble d'espace vectoriel normé $E$, 
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

 1. $d(x,y) = d(y,x)$ (symétrie).

 2. $d(x,y) = 0$ si et seulement si $x = y$ (séparation).

 3. $d(x,z) \leq d(x,y) + d(y,z)$ (inégalité triangulaire).


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

### Espace Métrique  {.definition}
Un *espace métrique* est un ensemble $X$ muni d'une *distance*.

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

### Test d'adhérence {.definition}

Un *test d'adhérence* sur l'ensemble *X* est une relation 
entre éléments de $X$ et sous-ensembles de $X$ telle que:

 1. Aucun point n'adhère à de l'ensemble vide,

 2. Tout point d'un ensemble adhère à cet ensemble,

 3. Un point adhère à l'union de deux ensembles 
    si et seulement s'il adhère à l'un ou l'autre 
    des deux ensembles,

 4. Un point qui adhère à l'ensemble des points adhérents 
    à un ensemble adhère à cet ensemble.

### Espace Topologique
Un *espace topologique* est un ensemble muni d'un test d'adhérence.
Les éléments de l'ensemble sont appelés des *points*, 
ses sous-ensembles des *ensembles de points*.

### Application Continue

Une application continue $f: X \to Y$ est une fonction définie entre deux espaces
topologique telle que lorsque $x$ adhère à $A$ dans $X$, $f(x)$ adhère à $f(A)$
dans $Y$.

### {.post}
Les applications sont les *morphismes* des espaces topologiques:
elle préservent la structure des espaces topologiques.

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
type limite quand on tend vers un point est intéressante.)

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

### Définitions séquentielles

  - Un ensemble $F$ est *fermé* si la limite de toute suite convergente de $F$
    appartient à $F$.

  - Un ensemble $V$ est un *voisinage* d'un point $x$ de $X$ si toute
    suite convergeant vers $x$ appartient à $V$ à partir d'un certain rang.

  - Un ensemble $O$ est *ouvert* si tout suite convergeant vers une
    limite appartenant à $O$ appartient à $O$ à partir d'un certain rang.

  - Un ensemble $K$ est *compact* si toute suite de $K$ admet une sous-suite
    convergente.

  

Complétude
================================================================================

### TODO:

  - point fixe, lien avec la résolution d'équations implicites, etc.
    Example nombre d'or

  - evn, espace métrique (comme sous-ensemble d'un e.v.n.), 
    suite de Cauchy, complétude

  - application lipschitzienne, (et lip est cont) contractante, 
    $\kappa$-contractante

### Points fixes et zéros
Etre un point fixe d'une fonction $f: X \to X$, c'est être déterminé 
implicitement par l'équation $x = f(x)$. Si $X$ est un sous-espace
d'un espace vectoriel,
cela équivaut à dire que $x$ est une solution de l'équation $x - f(x) = 0$,
soit un *zéro* (appelé également une *racine*) de la fonction $x \in X \mapsto x - f(x)$.

La démarche inverse 
-- qui consiste à caractériser les solutions d'une équation 
comme des point fixes -- peut être utile pour établir des résultats
d'existence et d'unicité des solution ou obtenir des méthodes numériques 
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


### Suite de Cauchy {.definition}
Une suite de points $x_k$ est *de Cauchy* si pour tout
$\varepsilon > 0$, 
il existe un rang $m$ tel que pour tous les entiers $n \geq m$ et $p \geq m$, 
$\|x_n - x_p\| \leq \varepsilon$. 

### Diamètre {.definition}
Le diamètre d'un sous-ensemble $A$ d'un espace vectoriel normé est donné par:
$$
\mbox{diam}(A) = \sup \, \{\|x - y \| \, | \, x \in A, \, y \in A\}
$$

### Suite de Cauchy et diamètre {.proposition}
Une suite de points $x_k$ est de Cauchy si et seulement si
$$
\lim_{k \to + \infty} \mbox{diam}(\{x_n \, | \, n \geq k \}) = 0.
$$

### Complétude {.definition}
Un espace métrique $X$ est *complet* si et seulement si tout suite de Cauchy
est convergente.

### Application contractante {.definition}
Une fonction $f: X \to X$ est *$\kappa$-contractante*, 
où $\kappa \in \left[0, 1\right[$,
si pour tout couple de points $x$ et $y$ de $X$, on a 
$$
\|f(x) - f(y)\| \leq \kappa \|x - y\|.
$$
Une telle application est *contractante* si elle est 
$\kappa$-contractante pour un $\kappa \in \left[0, 1\right[$.

### Théorème de Point Fixe de Banach {.definition .theorem #T-TPFB}

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

Compacité
================================================================================

### Compacité {.definition}
Un ensemble $E$ est *compact* si toute suite de valeurs de 
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

 1. Pouvez-vous donner une interprétation géométrique simple à la grandeur
    calculée par la fonction $f$ ?

    ![Construction d'une métrique pour la droite réelle achevée.](images/extended-real-numbers.tex)

 2. Montrer que $f$ est une bijection.

 3. En déduire qu'il existe une et une seule fonction distance sur
    $\mathbb{R} \cup \{-\infty, +\infty\}$ qui fasse de $f$ une isométrie;
    on note $d^{\pm \infty}$ cette distance. 

 4. (Optionnel) Calculer $d^{\pm \infty}(0, +\infty)$, $d^{\pm \infty}(-\infty, +\infty)$, 
    $d^{\pm \infty}(-1, 1)$.

 5. Montrer que l'injection canonique
    $x \in \mathbb{R} \mapsto x \in \mathbb{R} \cup \{-\infty, +\infty\}$
    est une fonction continue.

 6. Yoda a dit "deux façons d'interpréter $x_k \to +\infty$ désormais il y a".
    Qu'est-ce qu'il a voulu dire ? Est-ce que c'est un problème ?

 7. (Optionnel) Suggérer une variante de la construction précédente pour
   doter l'ensemble $\mathbb{R} \cup \{\infty\}$ ($\infty$ sans signe:
    ni $+$, ni $-$) d'une métrique $d^{\infty}$ 
    telle que $d^{\infty}(x_k, \infty) \to 0$ si et seulement si
    $|x_k| \to +\infty$.
    

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

 1. Est-ce que la distance entre ensembles classique
    $$
    d(A, B) = \inf_{a \in A} d(a, B) = \inf_{a\in A}\inf_{b \in B} d(a, b)
    $$
    fait l'affaire ?

On définit la grandeur
  $$
  d[A, B] = \max \left\{ \sup_{a \in A} d(a, B), \, \sup_{b \in B} d(b, A) \right\}.
  $$
appelée *distance de Hausdorff* entre $A$ et $B$.

  2. Calculer $d[A, B]$ lorsque $A = [-1,1] \times [-1, 1]$ et
     $B = [0, 2] \times [0,2]$.

![Ensembles $A = [-1,1] \times [-1, 1]$ et $B = [0, 2] \times [0,2]$.](images/hausdorff.tex){#A-et-B}

  3. Cette terminologie de "distance" de Hausdorff est-elle légitime ?


---------------------------

  $$
  \begin{split}
  d[A, B] &= \inf \, \{\|T - I\|_{\infty} \, | \, T \in A \to B \}.
  \end{split}
  $$

 1. Montrer que dans la définition de $d[A, B]$, l'infimum est un minimum, 
    c'est-à-dire qu'il existe une fonction $T^{\star}: A \to B$
    telle que $d[A, B] = \|T^{\star} - I\|_{\infty}$.

 2. Est-ce que $d[\cdot, \cdot]$ est une distance sur l'ensemble des
    sous-ensembles compacts de $\mathbb{R}^n$ ? Dans le cas contraire,
    suggérer une modification simple de $d[\cdot, \cdot]$ qui en soit
    une (on parle alors de *distance de Hausdorff* entre ensembles).

 3. La somme de Minkowksi de deux ensembles $A$ et $B$ est définie
    comme
    $$
    A + B = \{a + b \, | \, a \in A, \, b \in B \}.
    $$
    Est-ce que la somme de Minkowski, appliquée aux ensembles
    compacts de $\mathbb{R}^n$, est continue pour la distance 
    introduite à la question précédente ?



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

 1. Montrer que la fonction $x \mapsto f_x$ est injective.

 2. Montrer que pour tout point $x$ la fonction $f_x$ est bornée.

 3. Montrer que l'espace vectoriel $E$ des fonctions bornées de $X$ dans 
    $\mathbb{R}$ est un espace vectoriel qui peut être muni de la norme 
    $\| \cdot \|_{\infty}$ définie par
    $$
    \|f\|_{\infty} = \sup \, \{|f(y)| \, | \, y \in X\}.
    $$

 4. Montrer que $x \mapsto f_x$ est une isométrie, 
    c'est-à-dire que pour tout $x$ et
    $y$ dans $X$, on a 
    $$
    d(x, y) = \|f_x - f_y\|_{\infty}.
    $$

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

 1. Montrer que tout point fixe éventuel de $f$ est également 
    un point fixe de $f^n$.

 2. Montrer que $f^n$ admet un unique point fixe et qu'il est également
    un point fixe de $f$.

 3. Montrer que le procédé habituel pour construire un point 
    fixe de $f$ est toujours valable quand $f^n$ est contractante.


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


Nombres Réels de Bishop ?
--------------------------------------------------------------------------------

(illustration des suites de Cauchy ?)

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

Solution -- [Droite réelle achevée]
--------------------------------------------------------------------------------

 1. **TODO**

 2. **TODO**

 3. **TODO**

 4. **TODO**

 5. **TODO**

 6. **TODO**

 7. **TODO**

 
Solution -- [Distance entre ensembles]
--------------------------------------------------------------------------------

 1. Non, la distance usuelle $d(A,B)$ en convient pas.
    En effet, cette distance est nulle dès que l'intersection de $A$ et $B$
    est non vide, même si des points de $A$ sont être très éloignés de $B$.

 2. Lorsque $A = [-1,1] \times [-1, 1]$ comme l'abscisse et l'ordonnée de 
    tout point $a$ de $A$ sont de valeur absolue inférieure ou égale à $1$,
    on a $d(a, 0) \leq \sqrt{2}$ et donc
    $$
    \inf_{a \in A} d(a, 0) \leq \sqrt{2}
    $$
    L'origine $0$ appartenant $B = [0, 2] \times [0,2]$.
    Or $(0,0)$ appartient à $B$ donc pour tout point $(x, y)$ de $A$,
    $d((x, y), B) \leq \sqrt{2}$. Par ailleurs, ... **TODO**


 3. 

Solution -- [Plongement de Kuratowski]
--------------------------------------------------------------------------------

 1. Soit $x$, $x'$ deux points de $X$. Pour tout $y$ dans $X$ on a:
    $$
    \begin{split}
    f_x(y) - f_{x'}(y) &= d(x, y) - d(x_0, y) - (d(x', y) - d(x', x_0))\\
    &= d(x, y) - d(x', y),
    \end{split}
    $$
    par conséquent, si $f_x = f_{x'}$, on a en particulier
    $f_x(x') = f_{x'}(x')$, soit $d(x, x') - d(x', x') = d(x, x') = 0$, 
    c'est-à-dire $x = x'$.

 2. **TODO** Montrer que pour tout point $x$ la fonction $f_x$ est bornée.

 3. **TODO** Montrer que l'espace vectoriel $E$ des fonctions bornées de $X$ dans 
    $\mathbb{R}$ est un espace vectoriel qui peut être muni de la norme 
    $\| \cdot \|_{\infty}$ définie par
    $$
    \|f\|_{\infty} = \sup \, \{|f(y)| \, | \, y \in X\}.
    $$

 4. **TODO** Montrer que $x \mapsto f_x$ est une isométrie, 
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

 1. Si $x$ est un point fixe de $f$, $f(x) = x$, par conséquent
    $$
    f^2(x) = f(f(x)) = f(x) = x, 
    $$
    puis
    $$
    f^3(x) = f(f^2(x)) = f(x) = x,
    $$
    etc. Par récurrence, il est clair que l'on peut établir que pour tout
    $n \geq 1$, on a $f^n(x) = x$: $x$ est un point fixe de $f^n$.

 2. La fonction itérée $f^n$ satisfait les hypothèses du 
    [théorème du point fixe de Banach](#T-TPFB), par conséquent elle
    admet un point fixe $x$. Comme $f^n(x) = x$, en applicant $f$ aux
    deux membres de cette équation, on obtient 
    $$
    f(f^n(x)) = f^n(f(x)) = f(x).
    $$
    Par conséquent, $f(x)$ est un point fixe de $f^n$. 
    C'est donc l'unique point fixe $x$ de $f^n$; on a donc $f(x) = x$,
    c'est-à-dire que $x$ est un point fixe de $f$. 

 3. Le "procédé habituel pour construire un point fixe de $f$" 
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