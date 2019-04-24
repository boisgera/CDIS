% Calcul Intégral II
% Sébastien Boisgérault

Perspective {.notes}
--------------------------------------------------------------------------------

Scope: (ensembles mesurables,) fonctions mesurables, absolue intégrabilité.

La perspective est commune dans une large mesure: avec les outils dont on
dispose à ce moment, il est souvent difficile de savoir dans un calcul,
une expression composée si une fonction va être intégrable.

Exemples (à améliorer, distiller): 

  - produit de deux fonction intégrales n'est pas intégrable
    (ex: $f(x) = g(x) = 1/\sqrt{x}$ sur $[0,1]$), ok, car
    le produit est "trop grand", moralement l'intégrale est $+\infty$.
    Mais s'il n'était pas "trop grand", est-ce que ça marcherait ?

  - Si $f$ est intégrable sur l'intervalle $[a,b]$ de $\mathbb{R}$, 
    elle est aussi intégrable sur toute union finie $E$ d'intervalles de 
    $\mathbb{R}$, ce que l'on peut définir comme l'intégrabilité de 
    $f \chi_{E}$. Et si $E$ est plus général ? On "voit bien" qu'il est
    nécessaire de requérir que $\chi_E$ soit intégrable (sinon ça ne 
    marche pas avec $f=1$), ce que l'on appelle "ensemble intégrable",
    mais est-ce que ça suffit ? La réponse est non ...   
    (c'est un cas particulier du précédent, le faire avant).
    Pb résolu si la fct est abs int (c'est même un critère ici !).

  - Mais plus surprenant peut-être: le produit de deux fonction intégrables
    avec l'une des deux fonctions bornées n'est pas nécessairement intégrable.
    (cf [@Swa01, p.43, ex. 14] avec $\cos 1/t$ et $t^{-3/2} \cos 1/t$).
    Pb résolu si les fcts sont abs int.

  - Si $f$ est intégrable et $g$ est "sympa" (Lipschitz), 
    est-ce que $g \circ f$ est intégrable ? Non ... cf
    [@HL89, p. 525, ex. 4.2]
    Pb résolu si les fcts sont abs int.

On a deux outils qui se combinent pour analyser et résoudre ces pbs:

  - La notion de fonction mesurable et le critère d'intégrabilité dominée [@PS17],

  - La notion de fonction absolument mesurable.

(nota: autres avantages fcts abs int: chgt de variable robuste et complétude
$L^1$.)

Sinon

  - le théorème de convergence dominé est requis techniquement dans certaines
    preuves et également pour donner une perspective sur la démarche.
    Mais sa preuve, ses conséquences, variantes, etc. non, ce qui peut
    suggérer une "preview" de ce résultat et un développement plus complet
    ultérieurement. On a "besoin" du DCT et de son corollaire qu'une fct
    est intégrable ssi elle est bornée par des fcts intégrables et mesurable.

  - UPDATE: ensemble mesurable objet "secondaire", défini comme limite simple
    de fonction caractéristique ?

    Justifier l'introduction des ensembles mesurables ... par la recherche
    d'une notion de "volume" (longueur/aire/...) suffisamment générale ?
    Oui, en généralisant ce qui se passe pour les intervalles.
    Et les ensembles mesurables sont ceux dont la mesure ne pose pas de pb
    à part qu'ils sont "trop grands".
    Introduire mesure de Lebesgue à ce stade, est possible, 
    $\sigma$-algèbres, etc. Nécessaire dans la manip des fcts mesurables.

    Cross-justifier la notion de fonction absolument mesurable 
    (concept "stable" par multiplication par la fonction caractéristique
    d'un ensemble mesurable.)

    Probablement inclure plus généralement la pbmatique des fcts 
    absoluments continues ici. Deux axes: intégrer sur des sous-ensembles
    "plus généraux" et de façon général, meilleur comportement par rapport
    aux opération usuelles: le produit borné abs int et abs int est abs int;
    ça n'est pas le cas pour les fcts simplement intégrables, ce qui est
    compliqué! Le pb du "multiplier" de fcts intégrable (égal pp à une fct
    de variation bornée), c'est too much ...

  - JTODO: parallèle séries AC ou C pour fct AI (et exemple restriction est
    parlant, très proche, faire le parallèle ?)

  - Mener toute la présentation dans $\mathbb{R}$.
   
Fonctions mesurables
================================================================================

### Meta {.meta}
Dans la présentation, commencer par le théorème d'intégrabilité dominée,
son contraste avec le cas Riemann classique, sans utiliser le mot de
mesurabilité, puis en "extraire" la notion de mesurabilité.

### TODO

Relire/réfléchir sur domain def: travailler sur intervalle fermé général ou
dans $\mathbb{R}$ et si oui faire le lien ?
A l'inverse, focus sur intervalle qui permet de limiter l'exposition au
cas borné pour simplifier ???

### Ante {.ante}

Nous allons nous doter dans ce chapitre d'outils permettant de caractériser
plus facilement l'intégrabilité des fonctions. Au coeur de l'approche,
la notion de fonction mesurable:

### Fonction mesurable {.definition}
Une fonction $f:\mathbb{R} \to \mathbb{R}$ est *mesurable* 
si elle est la limite simple d'une suite de fonctions intégrables,
c'est-à-dire s'il existe une suite de fonctions intégrables 
$f_k:\mathbb{R} \to \mathbb{R}$ telle que 
pour tout $x\in \mathbb{R}$, 
$f_k(x) \to f(x)$ quand $k \to +\infty$.
Une fonction $f:\mathbb{R} \to \mathbb{R}^n$ est mesurable 
si chacune de ses composantes est mesurable.

### Ante {.ante}

Le résultat qui met la notion de fonction mesurable au coeur de l'approche
est le critère d'intégrabilité dominée:

### Critère d'intégrabilité dominée {.theorem}

Une fonction $f: \mathbb{R} \to \mathbb{R}$ est intégrable si et seulement
si $f$ est mesurable et il existe deux fonctions intégrables 
$g: \mathbb{R} \to \mathbb{R}$ et $h: \mathbb{R} \to \mathbb{R}$ telles que
$g \leq f \leq h$.

### Interprétation {.post .remark}

Souvenons-nous qu'une fonction définie sur un intervalle fermé et borné 
est intégrable au sens de Riemann si et seulement si elle est encadrée 
par deux fonctions intégrables au sens de Riemann et continue presque partout.

Dans le cas de l'intégrale de Riemann comme de Henstock-Kurzweil, 
l'intégrabilité est donc caractérisée par une structure analogue qui
repose sur deux propriétés distinctes:
être encadrée par deux fonctions intégrables et être "suffisamment
régulière". La différence est que dans le cas de l'intégrale de Riemann
l'exigence de régularité est forte, alors que dans le cas de l'intégrale
de Henstock-Kurzweil, la régularité demandée -- la mesurabilité -- est 
particulièrement faible.


### Remarque {.remark}

Nous verrons également dans la suite que ce résultat est généralement 
plus facile à exploiter quand on peut faire l'hypothèse que les fonctions
que l'on manipule sont non seulement intégrables, mais également
absolument intégrables.

**TODO: fcts abs int introduites SI TOT ???** Cela retarde assez notablement les résultats élémentaires
sur les fonctions mesurables, bof donc ... Faire une autre section ?

### Fonction absolument/conditionnellement intégrable {.definition} 
Une fonction $f:\mathbb{R} \to \mathbb{R}$ est *absolument intégrable*
si $f$ et $|f|$ sont intégrables. Si $f$ est intégrable mais pas $|f|$,
elle est *conditionnellement intégrable*.

### Fonctions absolument intégrables {.theorem}
L'ensemble des fonctions absolument intégrables de $\mathbb{R}$ dans
$\mathbb{R}$ est un espace vectoriel.

### Démonstration {.proof}
Si $f$ et $g$ sont absolument intégrables et $\lambda \in \mathbb{R}$,
alors $\lambda f$ est mesurable et $\lambda f$ comme $|\lambda f|$
sont encadrées par les fonctions intégrables $-|\lambda||f|$ et
$|\lambda||f|$; elle est donc absolument intégrable par le critère
d'intégrabilité dominée. La somme $f + g$ est également mesurable
et $f+g$ comme $|f+g|$ sont encadrées par $-|f| - |g|$ et $|f| + |g|$ qui
sont intégrables; la somme est donc intégrable par le même critère.

### Inégalité triangulaire {.theorem}
Si $f: \mathbb{R} \to \mathbb{R}$ est absolument intégrable, alors
$$
\left|\int_{\mathbb{R}} f(t)\, dt \right| 
\leq 
\int_{\mathbb{R}} |f(t)| \,dt.
$$

### Démonstration {.proof}
Les fonctions $f$ et $|f|$ étant intégrables, pour tout $\varepsilon > 0$,
il existe une jauge commune $\gamma$ sur $\mathbb{R}$ et un $r>0$ commun, 
tels que pour tout couple $(a,b)$ tel que 
$a \leq -r$ et $r \leq b$ et toute subdivision pointée $\mathcal{D}$ de 
$[a, b]$ qui soit subordonnée à $\gamma$, on ait
$$
\left| S(f, \mathcal{D}) - \int_{\mathbb{R}} f(t) \, dt \right| \leq \varepsilon/2
\; \mbox{ et } \;
\left| S(|f|, \mathcal{D}) - \int_{\mathbb{R}} |f(t)| \, dt \right| \leq \varepsilon/2.
$$
Par l'inégalité triangulaire appliquée à la somme finie $S(f, \mathcal{D})$, on
obtient donc
$$
\int_{\mathbb{R}} f(t) \, dt \leq S(f, \mathcal{D}) + \varepsilon /2
\leq S(|f|, \mathcal{D}) + \varepsilon /2
\leq \int_{\mathbb{R}} |f(t)| \, dt + \varepsilon,
$$
et donc en passant à la limite sur $\varepsilon$,
$$
\int_{\mathbb{R}} f(t) \, dt \leq  \int_{\mathbb{R}} |f(t)| \, dt.
$$
L'inégalité similaire
$$
-\int_{\mathbb{R}} f(t) \, dt \leq \int_{\mathbb{R}} |f(t)| \, dt.
$$
est obtenue en remplaçant $f$ par $-f$.


### TODO

Plus pertinent/simple de construire un exemple basé sur une série de valeurs
qui converge conditionnellement ?

### Une fonction conditionnellement intégrable {.example}

La fonction $f:[0, 1] \to \mathbb{R}$ définie par
$$
f(x) = \frac{1}{x} \cos \frac{1}{x^2} \, \mbox{ si }\,  x > 0 \, \mbox{ et } \, f(0) = 0
$$
est conditionnellement intégrable. Pour montrer qu'elle est intégrable, 
nous exploitons le théorème fondamental du calcul, appliqué à la fonction
$g:[0, 1] \to \mathbb{R}$ définie par 
$$
g(x) = -\frac{x^2}{2} \sin \frac{1}{x^2} \, \mbox{ si }\,  x > 0 \, \mbox{ et } \, g(0) = 0.
$$
Cette fonction est dérivable en tout point de $[0,1]$; en $0$, sa dérivée est 
nulle[^dn] et quand $x>0$,
$$
\left[-\frac{x^2}{2} \sin \frac{1}{x^2} \right]' +
x \sin \frac{1}{x^2} 
= \frac{1}{x} \cos \frac{1}{x^2}
$$
Par le théorème d'intégrabilité dominée, la fonction $h$ égale à
$x \sin (1/x^2)$ si $x>0$ et nulle en zéro est absolument intégrable[^details].
La fonction $g'$ étant également intégrable, $f = g' + h$ est intégrable comme
somme de deux fonctions intégrables.

[^dn]: En effet,
$$
\left| \frac{g(h) - g(0)}{h} \right| \leq \frac{|h|}{2} \to 0 \, \mbox{ quand } \, h \to 0.
$$

[^details]: La  fonction $h$ est mesurable comme limite des 
suite des fonctions continues $h_k$ -- et donc intégrables -- définies par 
$h_k(x) = 0$ si 
$x \in [0, 1/\sqrt{2k\pi}]$ et $h_k(x) = h(x)$ sinon. De la même façon,
$|h|$ est limite des fonctions intégrables $|h_k|$.
Par ailleurs, $h$ comme $|h|$ sont encadrées par les deux fonctions intégrables
$x\in [0,1] \mapsto -x$ et $x\in [0,1] \mapsto x$.

La fonction $f$ n'est pourtant pas absolument intégrable, 
car $h$ est absolument intégrable mais pas $g'$.
En effet, si c'était le cas, toute fonction absolument intégrable
dont la valeur absolue est majorée par $|g'|$ aurait par l'inégalité
triangulaire son intégrale majorée par celle de $|g'|$. 
Or nous allons exhiber une suite de telles fonctions dont l'intégrale
tend vers $+\infty$, ce qui établira la contradiction.

Soit $k\geq 1$ un entier;  on définit la function $\phi_k:[0,1] \to \mathbb{R}$ 
par
$$
\phi_k(x) = 
\left|
\begin{array}{rl} 
g'(x) & \mbox{si } \, \alpha_j \leq x \leq \beta_j, \, 0 \leq j \leq k\\
0 & \mbox{sinon.}
\end{array}
\right.
$$
où
$$
\alpha_j = \frac{1}{\sqrt{2\pi j}}
\; \mbox{ et } \;
\beta_j = \frac{1}{\sqrt{2\pi(j+3/4)}},
$$
Par construction, $\phi_k$ est continue par morceaux et donc absolument 
intégrable, et bien telle que $|\phi_k| \leq |g'|$.
Par ailleurs,
$$
\int_0^1 \phi_k(t) \, dt = \sum_{j=0}^k \int_{\alpha_j}^{\beta_k} \phi_k(t) \, dt
=\sum_{j=0}^k \left[-\frac{x^2}{2} \sin \frac{1}{x^2} \right]_{\alpha_j}^{\beta_j}
= \frac{1}{2}\sum_{j=0}^k \frac{1}{2\pi j + 3\pi/4}.
$$
Comme la série de cette équation est divergente, 
on peut rendre l'intégrale arbitrairement grande en choisissant
un $k$ suffisamment grand, ce qui permet de conclure.

### Les fonctions intégrables sont mesurables

... trivial

### Les limites simples de fonction mesurables sont mesurables.

... facile, en diagonalisant.

### Les fonctions continues sont mesurables

... car elle sont localement intégrables.


### Images réciproques des fonctions mesurables {.theorem}

Une fonction $f:\mathbb{R} \mapsto \mathbb{R}$ est mesurable si et seulement
les conditions équivalentes suivantes sont satisfaites:

 1. Pour tout nombre réel $a$, l'ensemble
    $$
    f^{-1}(\left]a, +\infty\right[) = \{x \in \mathbb{R} \, | \, a < f(x)\}
    $$
    est mesurable.

 2. Pour tout intervalle ouvert $\left]a, b\right[$ de $\mathbb{R}$,
    l'ensemble
    $$
    f^{-1}(\left]a, b\right[) = \{x \in \mathbb{R} \, | \, a < f(x) < b\}
    $$
    est mesurable.

 3. Pour tout ouvert $U$ de $\mathbb{R}$, l'ensemble
    $$
    f^{-1}(U) = \{x \in \mathbb{R} \,  | \, f(x) \in U\}
    $$
    est mesurable.

**TODO:** carac par les boréliens (serait 4.) nécessaire ici ? Non.

A l'inverse, simplifier en ne retenant que la formulation la plus forte ?
Et mettre le reste (et aussi intervalle fermé, etc.) en exercice 
(éventuellement) ?

**NOTA:** l'énonce ici est donné dans le cas des fonctions scalaires,
mais on a rapidement besoin du cadre vectoriel (pour composer avec
des opérateurs binaires), ce qui renforce encore l'attrait de la 
formulation "abstraite" (qui "tient" dans le cas vectoriel, mais
pas les autres). donc **TODO:** nettoyer, ne garder que le cas 3.,
et rajouter le bout de démo qui finit la preuve dans le cas vectoriel
(dans les deux sens).

**TODO:** remarque très rapidement sur la forme abstraite et lien avec la
continuité.

### Démonstration {.proof}

#### 1. $\Leftrightarrow$ 2. $\Leftrightarrow$ 3.

Montrons avant tout l'équivalence des trois relations de l'énoncé.
Supposons la condition 1.\ satisfaite.  Si $a =-\infty$ et $b=+\infty$,
comme
$$
f^{-1}(\left]-\infty, +\infty\right[)
= \bigcup_{k = 0}^{+\infty}  f^{-1}(\left]-2^k, +\infty\right[)
$$
l'image réciproque de $\left]a,b\right[$, est mesurable comme union
dénombrable d'ensembles mesurables. Dans le cas $-\infty < a$ et 
$b = +\infty$, la condition 1. s'applique directement et 
$f^{-1}(\left]a, b \right[)$ est mesurable. 
Si $-\infty < a < b < +\infty$, 
$$
\begin{split}
f^{-1}(\left]a, b\right[)
&= \bigcup_{k=0}^{+\infty} f^{-1}(\left]a, b - 2^{-n}\right]) \\
&= \bigcup_{k=0}^{+\infty} f^{-1}(\left]a, +\infty\right[) \setminus f^{-1}(\left]b - 2^{-n}, +\infty\right[)
\end{split}.
$$
L'image réciproque $f^{-1}(\left]a, b \right[)$ est donc mesurable comme
union dénombrable d'ensembles mesurables, car différences d'ensembles mesurables. 
Le seul intervalle ouvert que nous n'avons pas encore considéré est l'ensemble
vide, mais son image réciproque par $f$ est l'ensemble vide qui est bien 
mesurable.

Si la condition 2. est satisfaite, la condition 3. également, car tout ouvert
$U$ de $\mathbb{R}$ peut-être décomposé comme une union (finie ou) dénombrable 
d'intervalles ouverts (disjoints) $I_k$, par conséquent
$$
f^{-1}(U) = f^{-1} \left(\cup_k I_k \right) = \bigcup_{k} f^{-1}(I_k),
$$
l'image réciproque de $U$ par $f$ est donc mesurable. Finalement,
il est clair que si la condition 3.\ est satisfaite, la condition 1.\ également.

#### 3. $\Rightarrow$ mesurable.

Supposons la condition $3$ satisfaite. Construisons la suite
des $f_k(x)$ par la condition initiale $f_0(x) = 0$ et la relation
de récurrence
$$
f_{k+1}(x) = f_k(x) + 
\left|
\begin{array}{rl}
-1/k & \mbox{si } \, f(x) < f_k(x) -1/k \\
0    & \mbox{si } \, f_k(x) -1/k \leq f(x) \leq f_k(x) + 1/k \\
1/k  & \mbox{si } \, f_k(x) + 1/k < f(x).
\end{array}
\right.
$$
Par construction, si $f(x)=0$, $f_k(x)= 0$. Si $f(x) > 0$, les $f_k(x)$
forment une suite croissante convergeant vers $f(x)$, car la suite des
$1/k$ tend vers $0$ quand $k$ tend vers $+\infty$, mais leur somme est 
divergente. La situation est similaire si $f(x) < 0$, mais avec une
suite $f_k(x)$ décroissante.

Montrons que la suite des $f_k$ est mesurable, ce qui concluera cette 
section de la preuve puisqu'on aura montré que $f$ est une 
limite simple de fonctions mesurables.
Chaque fonction $f_k$ est étagée: l'ensemble des valeurs 
$\{\alpha_j\}$ que prend chaque $f_k$ est fini. 
La fonction peut donc s'écrire sous la forme
$$
f_k = \sum_{j} \alpha_j \chi_{A_j}
$$
où les ensembles $A_j = f_k^{-1}(\alpha_j)$ sont disjoints par construction.
Montrons qu'à tout rang $k$, les ensembles $A_j$ sont mesurables, 
ce qui prouve que chaque $f_k$ est mesurable.
C'est évident au rang $0$ où $\{\alpha_j\} = \{0\}$ et $A_0 = \mathbb{R}$;
supposons cette propriété valable au rang $k$. La fonction $f_k + 1/k$
peut donc mettre sous la forme d'une somme finie $\sum_j (\alpha_j + 1/k) \chi_{A_j}$
où les $A_k$ sont mesurables et disjoints. L'ensemble $E$ des
réels $x$ tels que $f_k(x) + 1/k < f(x)$ peut être écrit comme
$$
E = \bigcup_j \{x \in \mathbb{R} \, | \, \alpha_j + 1/k < f(x)\} \cap A_j,
$$
qui est mesurable. De même, on peut montrer que 
$F = \{x \in \mathbb{R} \, | \, f(x) < f_k(x) -1/k\}$ est mesurable.
On a alors par construction 
$$
f_{k+1} = \sum_{j} \alpha_j \chi_{A_j} + \frac{1}{k} \chi_E - \frac{1}{k} \chi_F
$$
qui est sous la forme souhaitée, à ceci près que les ensembles intervenant
ne sont pas nécessairement disjoints. Mais pour toute valeur $y$ dans l'image
de $f_{k+1}$, l'image réciproque de $\{y\}$ par $f$ est nécessairement une
union (finie) d'intersections (finies) d'ensembles dans la collection 
$\{\dots, A_j, \dots, E, F\}$ et donc un ensemble mesurable. La fonction 
$f_{k+1}$ a donc la forme souhaitée.

#### mesurable $\Rightarrow$ 3.

**TODO:** éviter circonvolution autour de "cette propriété"; 
lui donner un nom.

Montrons tout d'abord que l'ensemble des fonctions telles 
que l'image réciproque de tout ensemble 
ouvert est un ensemble mesurable est stable par passage à la limite simple,
c'est-à-dire que si toutes les fonctions de la suite 
$f_k: \mathbb{R} \to \mathbb{R}$ vérifient cette propriété et que
pour tout $x \in \mathbb{R}$, $f_k(x) \to f(x)$ quand $k \to +\infty$,
alors $f$ vérifie également cette propriété.
Il suffit pour cela de remarquer que comme $U$ est ouvert et que
$f_k(x) \to f(x)$, $f(x) \in U$ si et seulement si $f_k(x) \in U$
pour $k$ assez grand. Cette déclaration se traduit par la formule
$$
f^{-1}(U) = \bigcup_{j=1}^{+\infty} \bigcap_{k = j}^{+\infty} f_k^{-1}(U)
$$
qui établit que $f^{-1}(U)$ est un ensemble mesurable, comme union 
(dénombrable) d'intersections (dénombrable) d'ensembles mesurables.

Toute fonction $f$ égale presque partout à une fonction $g$ qui vérifie 
cette propriété vérifie également cette propriété. En effet, si pour
tout ouvert $U$ l'ensemble $g^{-1}(U)$ est mesurable, alors
$$
f^{-1}(U) = (g^{-1}(U) \setminus E) \cup F
$$
où $E$ et $F$ sont de mesure nulle (et donc mesurables puisque la mesure
de Lebesgue est complète);
par conséquent, $f^{-1}(U)$ est mesurable.

Considérons désormais une fonction intégrable $f:\mathbb{R} \to \mathbb{R}$.
Par le [théorème de dérivation de l'annexe][Une intégrale indéterminée est dérivable presque partout],
si l'on définit la fonction $f_k(x)$ comme le taux d'accroissement
$$
f_k(x) :=  \frac{F(x + 2^{-k}) - F(x)}{2^{-k}}
$$
où
$$
F: x \in \mathbb{R} \mapsto \int_0^x f(t) \, dt,
$$
alors $f_k(x) \to f(x)$ presque partout quand $k \to +\infty$.
Or chaque $f_k$ est continue, donc l'image réciproque de tout ouvert
par $f_k$ est un ensemble mesurable. Par les deux résultats établis dans
cette section, $f$ vérifie également cette propriété.

Pour conclure: par définition, une fonction mesurable est limite simple
d'une suite de fonctions intégrables, qui vérifient donc la propriété. 
Par stabilité de cette classe de fonctions par limite simple, la propriété
est également satisfaite pour toute fonction mesurable.


### Composition par une fonction continue {.theorem}

Soit $f:\mathbb{R} \to \mathbb{R}^n$ une fonction mesurable et 
$g:\mathbb{R}^n \to \mathbb{R}^m$ une fonction continue.
La composée $g \circ f$ de ces deux fonctions est mesurable.

**TODO:** extension composition par les fcts boréliennes ?
En exercice, pas sur le chemin critique ici.

### Démonstration {.proof}

Si $U$ est un ouvert de $\mathbb{R}^m$.
Par continuité de $g$, l'ensemble $g^{-1}(U)$ est un ouvert de $\mathbb{R}^n$ 
et par conséquent, par [le critère de mesurabilité par les images réciproques][Images réciproques des fonctions mesurables],
$$
(g\circ f)^{-1}(U) = f^{-1}(g^{-1}(U))
$$
est un ensemble mesurable. Par le même critère, 
la composée $g\circ f$ est donc mesurable.

### Remarque {.remark}
Les corollaires de ce résultat sont nombreux et immédiat. 
Citons les deux instances les plus directement utiles.

### Mesurabilité du produit {.corollary}

Le produit de deux fonctions scalaires mesurables est mesurable.

### Démonstration {.proof}

Par continuité de l'application produit 
$\times: \mathbb{R} \times \mathbb{R} \to \mathbb{R}$.

### Mesurabilité de la valeur absolue {.corollary}

La valeur absolue d'une fonction scalaire mesurable est mesurable.

### Démonstration {.proof}

Par continuité de l'application valeur absolue
$|\, \cdot \,|: \mathbb{R} \to \mathbb{R}$.


### Démonstration du critère d'intégrabilité dominée {.proof}

Si la fonction $f$ est intégrable, elle est mesurable et satisfait
les inégalités $f \leq f \leq f$. Le sens direct est donc démontré.

Pour établir la réciproque, nous allons exploiter le théorème de convergence
dominée du chapitre suivant.
Nous allons appliquer le procédé d'approximation
par une suite de fonctions étagées déjà utilisé dans [la preuve de la
caractérisation des fonctions mesurables par leurs images réciproques][Images réciproques des fonctions mesurables]. Nous appliquons cette construction à la fonction $f - g$ qui
est mesurable comme différence de fonctions mesurables. Comme $f-g$ vérifie
$0\leq f-g \leq h - g$, la suite $\delta_k$ -- qui converge
simplement vers $f-g$ --
vérifie $0 \leq \delta_k \leq h - g$. En raison de cette inégalité,
et comme $h - g$ est (absolument) intégrable, $\chi_{[-k, k]}\delta_k$ est 
une somme finie de la forme $\sum_j \alpha_j \chi_{A_j}$ où les $A_j$ 
sont mesurables et bornés (dans $[-k, k]$), $A_j$ est intégrable.

La fonction $f-g$ apparaît donc comme une limite simple des
fonction $\chi_{[-k, k]} \delta_k$, qui sont intégrables et
encadrées par les fonctions intégrables $0$ et $h - g$. Par le théorème de
convergence dominée, $f - g$ est intégrable, et par conséquent $f = (f-g) + g$
l'est également.

### TODO

 remarque nécessaire ou exemples montrant que le critère 
d'intégrabilité dominée est en fait pratique quand on manipule des
fonction absolument intégrables et que les calculs manipulant des 
fonctions uniquement conditionnellement intégrables sont "fragiles".

### Produit de fonctions intégrable et bornée {.corollary}

Si $f: \mathbb{R} \to \mathbb{R}$ est une fonction absolument intégrable 
et $g: \mathbb{R} \to \mathbb{R}$ est mesurable et bornée,
alors le produit $fg$ est (absolument) intégrable.

### Preuve {.proof}

Par hypothèse $f$ est intégrable donc mesurable; $g$ étant mesurable,
le produit $fg$ est mesurable. Par ailleurs, si $|g| \leq M$, on a
$$
- M |f| \leq f g \leq M |f|
$$
et comme les fonctions $-M|f|$ comme $M |f|$ sont intégrables, 
par le critère d'intégrabilité dominée, $fg$ est intégrable. 
La valeur absolue $|fg|$ de $fg$ est mesurable
et vérifie également $- M |f| \leq f g \leq M |f|$, elle est donc également
intégrable par le même critère.


Ensembles mesurables
================================================================================

**TODO:** secondaire dans l'approche, introduire plus tard et pas par une
nouvelle définition: fonction caractéristique mesurable suffit.

### Ensemble mesurable {.definition}

Un ensemble $E$ de $\mathbb{R}$ est *mesurable* si pour tout intervalle
$[a, b]$ compact de $\mathbb{R}$, la fonction caractéristique de 
l'intersection de $E$ et de $[a, b]$ 
$$
x \in \mathbb{R} \mapsto \{x \in E \mbox{ et } x \in [a, b]\}
$$
est intégrable.


--------------------------------------------------------------------------------

(expliquer ensembles infinis, problématique de régularité mais pas de taille)


### Propriétés des ensembles mesurables {.theorem}

 1. L'ensemble vide est mesurable.

 2. L'ensemble des points n'appartenant pas à un ensemble mesurable est mesurable.

 3. L'union d'une collection finie ou dénombrable d'ensembles mesurables,
    est mesurable.

 4. Tout ensemble ouvert est mesurable.

### Preuve {.proof}

**TODO.**

**TODO:** corollaires immédiats: difference mesurable, ensemble fermés
mesurables, etc.

--------------------------------------------------------------------------------

### Tribu / $\sigma$-algèbre {.definition}

**TODO:** $\sigma$-algèbre, "calculs"/notations associées, Boréliens, 
perspective par rapport à supra.

**TODO:** mesure, pptés, complétude de la mesure (nécessaire plus tard).


### Restriction à des ensembles mesurables {.corollary}

Une fonction $f:\mathbb{R} \to \mathbb{R}$ est absolument intégrable
si et seulement si $f \chi_E$ est (absolument) intégrable pour 
tout ensemble mesurable $E$. 

### Preuve {.proof}

Si $f$ est absolument intégrable, elle est mesurable; si l'ensemble
$E$ est mesurable, sa fonction caractéristique $\chi_E$ est également
mesurable. Par conséquent, le produit $f \chi_E$ est mesurable, 
comme sa valeur absolue $|f \chi_E|$.
Par ailleurs, comme $|\chi_E| \leq 1$, on a 
$-|f| \leq f\chi_E \leq |f|$ et donc $-|f| \leq |f\chi_E| \leq |f|$.
Par le critère
d'intégrabilité dominée, $f \chi_E$ est (absolument) intégrable.

Réciproquement, supposons $f \chi_E$ intégrable pour tout ensemble mesurable 
$E$. En prenant $E = \mathbb{R}$, on constate que $f$ est intégrable,
et donc mesurable.
Notons $E_+ = \{x \in \mathbb{R} \, | \, f(x) > 0 \}$ et 
$E_- = \{x \in \mathbb{R} \, | \, f(x) < 0 \}$; ces deux ensembles sont
mesurables comme images réciproques d'ouverts par une fonction mesurable.
La fonction $|f|$ satisfaisant
$$
|f| = \chi_{E_+} f - \chi_{E_-} f,
$$
elle est intégrable comme somme de fonctions intégrables.
La fonction $f$ est donc absolument intégrable.


Exercices
================================================================================

Intégrabilité locale
--------------------------------------------------------------------------------

Une fonction $f: \mathbb{R} \to  \mathbb{R}$ est localement intégrable si
pour tout point $x \in \mathbb{R}$, il existe un $\varepsilon > 0$ tel que
la fonction $f$ soit intégrable sur $[x-\varepsilon, x+\varepsilon]$.

 0. Montrer que $f$ est localement intégrable si et seulement si elle
    est intégrable sur tout intervalle fermé et borné.

 1. Montrer que toute fonction localement intégrable est mesurable.

 2. La réciproque est-elle vraie ?

### Réponses

 0. **TODO**

 1. **TODO**

 2. **TODO**
 
Fonctions Mesurables
--------------------------------------------------------------------------------

Alléger le texte principal des 3 caractérisations de mesurable par l'image
réciproque et se contenter de la plus "standard" (image réciproque de
tout ouvert est mesurable). Proposer ici le variantes plus simples, 
fermées et la variante plus "forte" (image réciproque d'un Borélien).

MMmm splitter, cas fct numériques et variantes "plus faibles" d'un coté
et fct Boréliennes et mesurabilité de l'autre (avec appli qui revisite
au passage la composition, en affaiblissant l'hypothèse de continuité).
Au passage, "jouer" avec les fcts Boréliennes ? Mq elles sont aussi 
mesurables ? Question: peut-être exhiber un exemple simple de compo
de fct Lebesgue mesurables qui ne soit pas mesurable?

Mesurabilité de $\|f\|$
--------------------------------------------------------------------------------

**TODO**

Intégrabilité
--------------------------------------------------------------------------------

Soient $f:\mathbb{R} \to \mathbb{R}$ et $g:\mathbb{R} \to \mathbb{R}$ deux
fonctions mesurables dont les carrés sont intégrables. Montrer que 
le produit $fg$ est (absolument) intégrable.

### Réponse

Les produits $fg$ et $|fg|$ sont mesurables comme produit de fonctions mesurables.
De plus, pour tout $x \in \mathbb{R}$, comme $(|f(x)| + |g(x)|)^2 \geq 0,$
on a
$$
0 \leq |fg|(x) \leq \frac{1}{2} f(x)^2 + \frac{1}{2} g(x)^2.
$$
et donc
$$
- \frac{1}{2} f(x)^2 - \frac{1}{2} g(x)^2
\leq fg(x)
\leq \frac{1}{2} f(x)^2 + \frac{1}{2} g(x)^2.
$$
Par le critère d'intégrabilité dominée, 
$fg$ et $|fg|$ sont donc intégrables.



Annexe 
================================================================================

### Une intégrale indéterminée est dérivable presque partout {.theorem}

Soit $I$ un intervalle fermé de $\mathbb{R}$, 
$f: I \to \mathbb{R}$ une fonction intégrable et un point 
$a$ de $I$.
La dérivée de la fonction
$$
F: x\in I \mapsto \int_a^x f(t) \, dt
$$
existe et est égale à $f$ presque partout.

### Démonstration {.proof}

Voir [@Swa01, pp. 135-136].

Références
================================================================================
