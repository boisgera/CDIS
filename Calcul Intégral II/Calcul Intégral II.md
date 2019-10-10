% Calcul Intégral II

<!-- LaTeX Macros -->
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}

<!--

Perspective {.notes}
--------------------------------------------------------------------------------

Scope: (ensembles mesurables,) fonctions mesurables, absolue intégrabilité.

La perspective est commune dans une large mesure: avec les outils dont on
dispose à ce moment, il est souvent difficile de savoir dans un calcul,
une expression composée si une fonction va être intégrable.

Exemples (à améliorer, distiller): 

  - Hypothèses sous lesquelles $\max(f, g)$ ou $fg$ intégrables pas claires
    (et quand c'est le cas, manque de théorème simple à ce stade pour 
    l'affirme)

  - produit de deux fonction intégrales n'est pas intégrable
    (ex: $f(x) = g(x) = 1/\sqrt{x}$ sur $[0,1]$), ok, car
    le produit est "trop grand", moralement l'intégrale est $+\infty$.
    Mais s'il n'était pas "trop grand", est-ce que ça marcherait ?

  - Si $f$ est intégrable sur l'intervalle $[a,b]$ de $\R$, 
    elle est aussi intégrable sur toute union finie $E$ d'intervalles de 
    $\R$, ce que l'on peut définir comme l'intégrabilité de 
    $f 1_{E}$. Et si $E$ est plus général ? On "voit bien" qu'il est
    nécessaire de requérir que $1_E$ soit intégrable (sinon ça ne 
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

  - Mener toute la présentation dans $\R$.
   
-->

Introduction
================================================================================

L'intégrale de Henstock-Kurzweil, introduite dans "Calcul Intégral I", 
présente l'avantage de pouvoir intégrer une plus grande gamme de fonctions
que l'intégrale de Riemann : moins régulières, non bornées et/ou définies
sur des intervalles non-bornés[^ii].

Il faut néanmoins reconnaître qu'à ce stade de notre exposé l'intégrale
de Riemann est parfois plus pratique. 
Par exemple : si avec l'intégrale de Henstock-Kurzweil,
on sait que $\lambda f$ et $f + g$ sont intégrables quand
$f$ et $g$ le sont, 
il n'est pas certain que le produit $f g$ soit intégrable ;
et nous ne disposons pas encore des outils adaptés pour étudier cette 
intégrabilité.
Or dans le cadre Riemannien, rien de plus simple : si $f$ et $g$ sont
des fonctions intégrables au sens de Riemann sur un segment, le produit 
$fg$ est systématiquement intégrable au sens de Riemannn sur ce segment[^cocpp]. 

[^ii]: Sans nécessiter de construction supplémentaire ; dans le cadre
de l'intégrale de Riemann, certaines de ces intégrales peuvent être
calculées comme des intégrales *impropres*, par un passage à la limite
d'intégrales de Riemann de fonctions définies sur un sous-ensemble.
Mais l'intégrale qui en résulte 
-- on parle parfois d'intégrale de *Cauchy-Riemann* -- 
perd une bonne partie des propriétés de l'intégrale de Riemann.

[^cocpp]: En première approche on pourra rapidement s'en convaincre 
en remplaçant "intégrables au sens de Riemann" par "continues". 
Dans le cas général, 
supposons que $f$ et $g$ sont intégrables au sens de Riemann 
sur un segment $[a, b]$ de $\R$, 
c'est-à-dire bornées et continues presque partout.
De toute évidence, leur produit est borné. Si $f$ est continue en tout point
de $[a, b]$ à l'exception de l'ensemble négligeable $A$ et $g$ en tout point
de $[a, b]$ à l'exception de l'ensemble négligeable $B$, l'ensemble
$C$ des points de discontinuité de $fg$ est nécessairement dans $A\cup B$,
donc négligeable. Le produit $fg$ est donc intégrable au sens de Riemann.

Cette remarque ne souligne pas à proprement parler un défaut de l'intégrale de 
Henstock-Kurzweil, mais plutôt une conséquence de sa généralité : en permettant
d'intégrer des fonctions telles que $x \in [0, 1] \mapsto 1/\sqrt{x}$ 
(presque partout), on s'expose à devoir refuser d'intégrer le produit d'une 
fonction par elle-même, ici $x \in [0,1] \mapsto 1/x$ (presque partout).
Il est donc normal de devoir imposer des conditions supplémentaires
pour garantir l'intégrabilité d'un produit.

Heureusement, comme dans le cas de l'intégrale de Riemann, 
un critère d'intégrabilité des fonctions -- nécessaire et suffisant -- 
existe pour établir ce type de résultat (et bien d'autres).
Comme dans le cas de l'intégrale de Riemann, il se décompose en deux tests
indépendants : pour être intégrable une fonction doit être "encadrée par des
fonctions intégrables" et "suffisamment régulière". Bien sûr ici les 
fonctions qui jouent le rôle de bornes devront être intégrables au sens
de Henstock-Kurzweil (et non plus de Riemann) ; 
quant à la régularité, il ne s'agira plus de tester la continuité presque
partout, mais de vérifier la *mesurabilité* de la fonction considérée,
une propriété que possèdent presque toutes les fonctions "imaginables".

Bien que n'étant un cas particulier, 
l'intégrabilité d'un produit revêt une importance particulière. 
En effet dans ce chapitre pour des raisons de simplicité, 
nous mettrons l'accent sur les fonctions définies sur $\R$ ; 
par défaut le symbole intégrale sans bornes désignera donc 
l'intégrale entre $-\infty$ et $+\infty$:
$$
\int := \int_{-\infty}^{+\infty}.
$$
Si une fonction n'est définie que sur un sous-ensemble $A$ de $\R$
-- qui pourra être un intervalle ou un ensemble plus complexe --
il est naturel de l'étendre en une fonction définie sur $\R$ prenant
la valeur $0$ en dehors de $A$ puisque dans le cas des intervalles,
cette opération ne change pas la valeur de l'intégrale.
Le mouvement inverse -- restreindre une fonction définie sur $\R$ à un 
sous-ensemble nécessite de considérer le produit $1_A f$ 
de $f$ par la fonction caractéristique de $A$, ce qui soulève la question
de l'étude de l'intégrabilité de ces fonctions caractéristiques.

Mais notre première étape dans ce chapitre sera de nous doter d'un
théorème de convergence dominée, qui permettra -- sous certaines
conditions qui sont plus simples que dans le cadre Riemannien classique
-- de calculer l'intégrale d'une fonction $f$ à partir
des intégrales d'une suite de fonctions convergeant vers $f$.

<!--
Finalement, l'intégrale de Henstock-Kurzweil possède comme l'intégrale de
Riemann un théorème de convergence dominée, qui permet d'évaluer 
l'intégrale d'une fonction $f$ en calculant les intégrales d'une suite 
de fonctions convergeant simplement vers $f$. Contrairement au cadre de 
l'intégrale de Riemann, il ne sera pas nécessaire de supposer que la
limite des fonctions considérées soit intégrable -- les hypothèses
du théorème fourniront automatiquement ce résultat.
-->

<!--
--------------------------------------------------------------------------------

Dans la suite de ce document, nous mettons l'accent sur les fonctions définies
sur $\R$ (ou $\R \cup \{-\infty, +\infty\}$) ; par défaut le symbole intégrale 
sans bornes désignera donc l'intégrale entre $-\infty$ et $+\infty$:

$$
\int := \int_{-\infty}^{+\infty}
$$

L'essentiel des notions et résultats qui sont introduits peuvent être 
généralisés sans difficulté à des fonctions définies sur des intervalles
(voire des ensembles plus complexes), en considérant le prolongement 
de ces fonctions par zéro.

-->

Théorèmes de Convergence
================================================================================

### Théorème de convergence dominée {#TCD .theorem}
Si une suite de fonctions intégrables $f_k:\R \to \R$
converge simplement vers la fonction $f$, c'est-à-dire si pour tout
$x \in \R$,
$$
\lim_{k \to +\infty} f_k(x) = f(x)
$$
et qu'il existe deux fonctions intégrables $g$ et $h$ encadrant la suite $f_k$,
c'est-à-dire telles que pour tout $k \in \mathbb{N}$ et pour tout 
$x \in \R$,
$$
g(x) \leq f_k(x) \leq h(x)
$$
alors la fonction $f$ est intégrable et 
$$
\int f(t) \, dt 
=
\int \lim_{k \to +\infty} f_k(t) \, dt
= 
\lim_{k \to +\infty} \int f_k(t) \, dt.
$$

### Démonstration {.proof}
Se reporter à @Dem11.

### Dérivation sous le signe somme {.theorem #DSS}
Soit $I$ un intervalle de $\R$ et $f: I \times \R \to \R$ une fonction
telle que :

 1. pour tout $\lambda \in I$, 
    la fonction $t \in \R \mapsto f(\lambda, t)$ est intégrable,

 2. pour tout $t \in \R$, la fonction
    $\lambda \in I \mapsto f(\lambda, t)$
    est dérivable et 
    $$|\partial_{\lambda} f(\lambda, t)| \leq g(t)$$
    où $g: \R \to \left[0, +\infty\right[$ est une fonction intégrable.

Alors la fonction $S: I \to \R$ définie par
$$
S(\lambda) := \int f(\lambda, t) \, dt
$$
est dérivable pour tout $\lambda$ et 
$$
S'(\lambda) = \int \partial_{\lambda} f(\lambda, t) \, dt.
$$

### Démonstration {.proof}
Par linéarité de l'intégrale, 
pour tout $\lambda \in I$ et tout $h \in \R$ tel que $\lambda + h \in I$, 
on a
$$
\frac{S(\lambda + h) - S(\lambda)}{h}
= \int \frac{f(\lambda + h, t) - f(\lambda, t)}{h} \, dt.
$$
Soit $h_k$ une suite de réels non nuls tels que $\lambda + h_k \in I$ et $h_k \to 0$
quand $k \to +\infty$. En raison de la dérivabilité de $f$ par rapport
à son premier argument, pour tout $t \in \R$,
$$
\lim_{k \to +\infty} \frac{f(\lambda + h_k, t) - f(\lambda, t)}{h_k}
= \partial_{\lambda} f(\lambda, t).
$$
De plus, par l'inégalité des accroissement finis, pour tout $k \in \N$,
$$
\left|\frac{f(\lambda + h_k, t) - f(\lambda, t)}{h_k} \right|
\leq \sup_{\mu \in I} |\partial_{\lambda} f(\mu, t)| \leq g(t),
$$
et donc
$$
-g(t) \leq \frac{f(\lambda + h_k, t) - f(\lambda, t)}{h_k} \leq g(t).
$$
Les taux d'accroissements de $f$ sont donc encadrés par deux fonctions intégrables.
Par [le théorème de convergence dominée](#TCD), on conclut que
$$
\lim_{k \to +\infty} \frac{S(\lambda + h_k) - S(\lambda)}{h_k}
=
\int \partial_{\lambda} f(\lambda, t) \, dt,
$$
ce qui achève la démonstration.


### Théorème de convergence monotone {#TCM .theorem}
Si une suite de fonctions intégrables $f_k:\R \to \R$
est croissante et majorée en tout point, c'est-à-dire si pour tout
$x$ de $\R$ 
$$
\mbox{pour tout } \, k \in \mathbb{N}, \, f_k(x) \leq f_{k+1}(x) 
\; \mbox{ et } \;
\sup_k f_k(x) < + \infty,
$$
alors la limite simple $f$ des $f_k$ est intégrable si et seulement si 
$$
\sup_k \int f_k(t) \, dt < +\infty.
$$
et dans ce cas,
$$
\int f(t) \, dt 
=
\int \lim_{k \to +\infty} f_k(t) \, dt
= 
\lim_{k \to +\infty} \int  f(t) \, dt.
$$

### Démonstration {.proof}
Se reporter à @Dem11.

Ensembles mesurables
================================================================================

Il existe un lien étroit entre la notion de longueur d'un ensemble de réels
et le calcul intégral. Nous savons par exemple que pour tout intervalle 
compact $E = [a, b]$, la longueur $b-a$ de l'intervalle peut être calculée
par l'intégrale de la fonction caractéristique de $E$ :
$$
\ell(E) = \ell([a, b]):=  b - a  = \int_a^b \, dt = 
\int 1_{[a, b]}(t) \, dt =
\int 1_{E}(t) \, dt.
$$
Si $E$ est une collection finie d'intervalles disjoints $[a_i, b_i]$,
l'intégrale de $1_E$ vaut cette fois-ci $\sum_i b_i - a_i$, 
ce qui correspond toujours à la valeur "intuitive" de la longueur 
de l'ensemble. 

Il apparait donc légitime pour définir la longueur d'un sous-ensemble $E$
de $\R$ aussi général que possible[^loop] de $\R$ de prendre cette 
égalité comme une définition, ce qui suppose toutefois que la fonction 
caractéristique soit intégrable ; on parle alors d'*ensemble intégrable*
ou *de longueur finie*. 
Cette définition laisse toutefois de coté les ensembles "trop grands" 
pour être intégrables, mais par ailleurs parfaitement inoffensifs, 
comme $\R$ tout entier ou l'ensemble des réels positifs. 
Nous préférons donc mettre l'accent sur la notion d'ensemble *mesurable* :

<!--
### TODO
Insérer référence ens Vitali en annexe
-->

[^loop]: Il existe des ensembles dont on ne peut pas définir raisonnablement
la longueur, sauf à accepter un concept de longueur aux propriétés
très étranges. Cette situation ne résulte pas de la méthode de définition
de la longueur par l'intégrale ; c'est au contraire une limitation intrinsèque
de la théorie de la mesure que nous étudierons plus en détail par la suite.
Malheureusement pour la didactique, il n'existe aucun exemple explicite 
(élaboré par un procédé constructif) d'ensemble qui ne soit pas 
mesurable (et c'est une chose que l'on peut prouver !).
On peut se consoler en apprenant que, du point de vue logique, 
si l'on suppose que tous les ensembles sont
mesurables -- ce qui peut sembler relativement anodin -- 
on peut alors prouver des propositions beaucoup plus perturbantes,
comme l'existence de partitions de $\R$ "strictement
plus grandes" que $\R$ lui-même. 

### Ensemble mesurable {.definition}
Un ensemble $E$ de $\R$ est *de longueur finie* si sa fonction 
caractéristique $1_E$ est intégrable sur $\R$ ; 
il est *mesurable* si sa fonction caractéristique est intégrable 
sur tout intervalle compact $[a, b]$ de $\R$.
La (mesure de) *longueur* d'un ensemble $E$ mesurable est définie par
$$
\ell(E) := \int 1_E(t) \, dt
$$
si $E$ est de longueur finie et
$$
\ell(E) := +\infty
$$
dans le cas contraire (si $E$ mesurable mais pas de longueur finie).

### Interprétation {.remark}
Il faut comprendre le terme "mesurable" littéralement, 
comme signifiant "dont on peut définir la mesure (de longueur)", 
qui est un nombre fini ou infini. 
Cette interprétation  est cohérente, puisque tous les ensembles 
$E$ de longueur finie 
sont bien mesurables ;
en effet si la fonction caractéristique $1_E$ est intégrable,
sa restriction à tout intervalle compact $[a, b]$ également.

<!--
### TODO:

intégrale de fct carac sur $[a, b]$ dominé par une borne finie commune,
conclure que l'ensemble est de longueur finie?

### TODO en exercice

Structure de $\delta$-ring pour les ensembles intégrables ?
-->

### {.definition .post}
Un ensemble est *dénombrable* s'il est fini ou bien en bijection avec 
$\mathbb{N}$.

### Propriétés élémentaires {.theorem #pptés-tribu}

 1. L'ensemble vide est mesurable.

 2. Le complémentaire d'un ensemble mesurable est mesurable.

 3. L'union d'une collection dénombrable d'ensembles mesurables
    est mesurable.

### Complémentaire absolu et relatif {.notation .definition}
Le complémentaire (absolu) d'un ensemble $A$, relativement au
sur-ensemble $X=\R$ dans ce chapitre
-- mais le concept peut facilement être généralisé --
désigne l'ensemble des points de $X$ qui ne sont pas dans $A$.
Quand le choix de $X$ est clair dans le contexte, on pourra le noter
$$
A^c = \{x \in X \, | \, x \not \in A\}.
$$
Pour être plus explicite, on peut utiliser la notation du complémentaire 
relatif : le complémentaire de $A$ dans $B$ est l'ensemble des points de 
$B$ qui n'appartiennent pas à $A$ :
$$
B \setminus A = \{x \in B \, | \, x \not \in A\}.
$$
Cette notation ne suppose pas a priori que $A$ soit inclus dans $B$ ; 
on a bien sûr
$$
A^c = X \setminus A.
$$

### Démonstration des [propriétés élémentaires](#pptés-tribu) {.proof}
 1. La fonction caractéristique $1_{\varnothing}$ est identiquement nulle ; 
    l'ensemble vide $\varnothing$ est donc de longueur finie et par conséquent 
    mesurable.

 2. Si l'ensemble $A$ est mesurable et $B = \R \setminus A$,
    pour tout $[a, b]$, l'ensemble $A \cap [a, b]$ est de longueur finie.
    Par ailleurs, l'ensemble $[a, b]$ est de longueur finie. 
    Donc, comme
    $$
    1_{B \cap [a, b]} = 1_{[a, b]} - 1_{A \cap [a, b]},
    $$
    l'ensemble $B \cap [a, b]$ est de longueur finie ;
    l'ensemble $B$ est donc mesurable.

 3. Montrons tout d'abord que l'union d'une collection finie d'ensembles 
    mesurables est mesurable ;
    il suffit d'établir que si $A$ et $B$ sont mesurables,
    alors leur union $A \cup B$ l'est également. 
    Or, pour tout intervalle compact $[a, b]$, on a 
    $$
    (A \cup B) \cap [a, b]
    = (A \cap [a, b]) \cup (B \cap [a, b]),
    $$
    ce qui se traduit au moyen des fonctions caractéristiques par la relation
    $$
    1_{(A \cup B) \cap [a, b]}  = \max \left(1_{A \cap [a, b]}, 1_{B \cap [a, b]} \right).
    $$
    La fonction caractéristique de $(A \cup B) \cap [a, b]$ est donc intégrable
    comme [maximum de deux fonctions positives intégrables (cf. annexe)](#max).
    L'union $A \cup B$ est donc mesurable.
 
    Considérons désormais une suite d'ensembles mesurables
    $A_k$, pour $k \in \N$. 
    Quitte à remplacer $A_k$ par $\cup_{j=0}^k A_j$
    --
    ce qui ne change pas le caractère mesurable des $A_k$ ou leur union 
    jusqu'à l'ordre $k$
    --
    on peut supposer que $A_k \subset A_{k+1}$.
    Pour tout intervalle compact $[a, b]$, 
    $$
    \left(\bigcup_{k=0}^{+\infty} A_k\right) \cap [a, b] = 
    \bigcup_{k=0}^{+\infty} \left(A_k \cap [a, b]\right);$$
    les ensembles $A_k \cap [a, b]$ sont de longueur finie, 
    c'est-à-dire que $1_{A_k \cap [a, b]}$ est intégrable.
    Pour tout $k\in \N$, on a $0 \leq 1_{A_k \cap [a, b]} \leq 1_{[a, b]}$ ;
    les ensembles $A_k \cap [a, b]$ formant une suite croissante pour l'inclusion,
    la suite des fonctions caractéristiques $1_{A_k \cap [a, b]}$ est croissante 
    et majorée par $1_{[a, b]}$ ; pour tout réel $x$ on a donc
    $$
    1_{\left(\cup_{k=0}^{+\infty} A_k\right) \cap [a, b]}(x)
    = \lim_{k\to +\infty} 1_{A_k \cap [a, b]}(x)
    $$
    Par [le théorème de convergence dominée](#TCD),
    la fonction caractéristique de $\left(\cup_{k=1}^{+\infty} A_k\right) \cap [a, b]$ 
    est intégrable ; 
    cet ensemble est donc mesurable.

<!--
### Tribu {.definition .remark}
Une collection de sous-ensembles contenant l'ensemble vide,
stable par passage au complémentaire et par union dénombrable 
est appelée *tribu* (ou *$\sigma$-algèbre*).
Les ensembles mesurables dans $\R$ forment donc une tribu.
-->


### Intersection d'ensemble mesurables {.proposition #IEM}
L'intersection d'une collection dénombrable d'ensembles mesurables est mesurable.

### Démonstration {.proof}
Notons que pour toute collection $\mathcal{A}$ d'ensembles de $\R$,
$$
\bigcap \mathcal{A} =
\bigcap_{A \in \mathcal{A}} A= \left(\bigcup_{A \in \mathcal{A}} A^c\right)^c.
$$
La conclusion quand $\mathcal{A}$ est dénombrable résulte alors 
des [propriétés élémentaires des ensembles mesurables](#pptés-tribu).

### Complémentaire relatif {.proposition #CR}
Si les ensembles $A$ et $B$ sont mesurables, le complémentaire 
$B \setminus A$ de $A$ dans $B$ est mesurable.

### Démonstration {.proof}
Les ensembles $A$ et $B$ appartenant à $\R$, on a 
$B \setminus A = B \cap A^c$ ; 
le complément de $A$ dans $B$ est donc mesurable comme intersection
d'ensembles mesurables.

### Topologie et ensembles mesurables {.theorem #OSM}
Tout ensemble fermé (ou ouvert) est mesurable.

### Démonstration {.proof}
Les ensembles fermés et ouverts étant complémentaires les uns des autres
et le [complémentaire d'un ensemble mesurable étant mesurable](#pptés-tribu),
on peut se contenter de démontrer le résultat soit pour les ouverts 
soit pour les fermés ; la preuve s'avère plus simple dans le cas des ouverts.

Tout intervalle ouvert $I$ est mesurable : en effet, 
son intersection avec un intervalle compact $[a, b]$ 
est un intervalle inclus dans $[a, b]$.
La fonction caractéristique associée est de la forme $1_{[c, d]}$,
ou en diffère au plus en deux points ; 
dans tous les cas, elle est intégrable.

Si maintenant $U$ est un ensemble ouvert, pour chaque point $x$ de $U$ 
on peut construire le plus grand intervalle ouvert $I_x$ contenant $x$ et inclus
dans $U$ (c'est l'union de tous les intervalles ouvert vérifiant ces
deux propriétés). Pour un couple $x$ et $y$ dans $U$, soit $I_x = I_y$,
soit $I_x$ et $I_y$ sont disjoints et l'union de tous les intervalles
$I_x$ est égale à $U$. Comme dans chaque $I_x$ on peut choisir
un nombre rationnel $y$ tel que $I_x = I_y$, la collection de $I_x$
est dénombrable.
L'ouvert $U$ est donc une union dénombrable d'intervalles ouverts[^pf], 
qui sont tous mesurables, il est donc mesurable.

[^pf]: le résultat correspondant est faux pour les intervalles fermés.

### Ensembles négligeables {.theorem #négligeable-longueur-nulle}

Un ensemble est de longueur nulle si et seulement s'il est négligeable.

### Démonstration {.proof}

Si l'ensemble $A$ est négligeable, sa fonction caractéristique est
égale presque partout à la fonction identiquement nulle, qui est
intégrable et d'intégrale nulle. 
Par conséquent, $1_A$ est intégrable et d'intégrale nulle, 
donc l'ensemble $A$ est intégrable et de longueur nulle.

Réciproquement, supposons l'ensemble $A$ de longueur nulle ; 
nous cherchons à montrer que pour tout $\varepsilon >0$, 
il existe une famille dénombrable d'intervalles
$I_i$ de $\R$ qui recouvre $A$ et telle que
$$
\sum_i \ell(I_i) \leq \varepsilon.
$$

Supposons temporairement que $A$ soit inclus dans un intervalle compact 
$[a, b]$ de $\R$. 
La fonction caractéristique $1_A$ de $A$ est intégrable, 
donc pour tout $\varepsilon > 0$ il existe une jauge $\gamma$ sur
$[a, b]$ telle que, si la subdivision pointée (totale ou partielle) <!--[^todo-hens]--> 
$\mathcal{D} =\{(t_i, I_i)\}_i$ est
subordonnée à $\gamma$, on a
$$
S(1_A, \mathcal{D})
=
\left|S(1_A, \mathcal{D}) - \sum_i \int_{I_i}  1_A (t) \, dt \right| 
\leq 
\varepsilon.
$$
Pour conclure, nous allons construire une famille dénombrable $\{(t_i, I_i)\}_i$ 
où les $I_i$ sont des intervalles compacts de $[a, b]$ sans chevauchement, 
tels que pour tout $i$, $t_i \in A$, $I_i \subset \gamma(t_i)$ et tels que la famille des
$I_i$ recouvre $A$. Si cette construction est acquise et que $\mathcal{D}_k$
désigne la collection des $\{(t_i, I_i)\}$ pour $0 \leq i \leq k-1$, alors c'est
une subdivision pointée partielle de $[a, b]$ subordonnée à $\gamma$ et donc
$$
S(1_A, \mathcal{D}_k) 
=
\sum_{i=0}^{k-1} 1_A(t_i) \ell(I_i)
=
\sum_{i=0}^{k-1} \ell(I_i) \leq \varepsilon.
$$
En passant à la limite sur $k$, cette inégalité fournit comme souhaité
$$
\sum_{i=0}^{+\infty} \ell(I_i) \leq \varepsilon.
$$


<!--
[^todo-hens]: cette formulation est intéressante. C'est un peu moins fort
que le lemme de Henstock stricto sensu, mais ça peut peut-être suffire 
à tous nos besoins: le lemme de Henstock permet de revisiter la définition
d'intégrabilité (de façon équivalente) en rajoutant à la définition le
qualificatif "(totale ou partielle)" à la subdivision (modulo aussi
un mini-patch dans la formule inégalité ou l'on n'intègre plus nécessairement
sur tout $[a, b]$, mais on somme sur les confettis ... Mmmm; on aurait
peut-être intérêt à écrire ça comme
$$
\int_{\cup_i I_i} f(t) \, dt := \sum_i \int_{I_i} f(t) \, dt
$$
en définissant l'intégrale sur une union (finie) d'intervalles qui sont
sans chevauchement).
Et c'est un raccourci très intéressant pour la présentation orale.
Il faudrait voir si ce "corollaire" du lemme de Henstock couvre l'ensemble
des usage que l'on a en aval ...
-->

Procédons à la construction de la collection de $(t_i, I_i)$,
par dichotomie.
S'il existe un 
$t \in [a, b]$ tel que $t \in A$ et $[a, b] \subset \gamma(t)$,
alors on prend pour collection le singleton $\{(t, [a, b])\}$.
Dans le cas contraire, on considère la décomposition de $[a, b]$ en
$[a, (a+b)/2]$ et $[(a+b)/2, b]$. On examine chacun de ces intervalles $J$
et s'il existe un $t \in A \cap J$ tel que $J \subset \gamma(t)$, 
on inclut la paire $(t, J)$ dans la collection ; dans le cas contraire,
on poursuit la dichotomie. Cette procédure définit par construction
une famille dénombrable $\{(t_i, I_i)\}_i$ où $t_i \in A$ et 
les $I_i$ sont des intervalles compacts de $[a, b]$ sans chevauchement 
tels que pour tout $t_i$, $I_i \subset \gamma(t_i)$. 
De plus, les $I_i$ recouvrent $A$ : en effet si l'on considère $t \in A$,
il existe nécessairement un entier $k$ tel que tout intervalle compact
$I$ de longueur inférieure ou égale à $(b-a)/2^k$ contenant $t$ 
vérifie $I \subset \gamma(t)$.
Par conséquent, $t$ appartient à l'un des intervalles inclus par le procédé
au plus tard à l'étape $k$ de la dichotomie.

Finalement, supposons $A$ de longueur nulle mais plus nécessairement borné.
Soit $\varepsilon > 0$.
Pour tout $k \in \N$, l'ensemble $A \cap [-k, k]$ est de longueur nulle et borné ; 
il peut donc être recouvert par une famille dénombrable d'intervalles dont
la somme des longueurs est inférieure $\varepsilon / 2^{k+1}$. 
Comme $A = \cup_{k=0}^{+\infty} (A \cap [-k, k])$, la collection 
de tous ces intervalles recouvre $A$ ; la somme de leur 
longueur est majorée par 
$\sum_{k=0}^{+\infty} \varepsilon/2^{k+1} = \varepsilon.$
L'ensemble $A$ est donc négligeable.

### Complétude de la longueur {.corollary}

Un sous-ensemble d'un ensemble de longueur nulle est de longueur nulle.

### Démonstration {.proof}
Un sous-ensemble $A$ d'un ensemble négligeable $B$ est négligeable car
pour tout $\varepsilon > 0$, il existe une famille dénombrable 
d'intervalles $I_i$ recouvrant $B$ et tels que 
$\sum_i \ell(I_i) \leq \varepsilon$ ; or cette famille recouvre aussi $A$. 
Comme [un ensemble est négligeable si et seulement si il est de longueur
nulle](#négligeable-longueur-nulle), cet argument conclut la démonstration.

Fonctions mesurables
================================================================================

### Fonction mesurable {.definition}
Une fonction $f:\R \to \R$ est *mesurable* 
si elle est la limite simple d'une suite de fonctions intégrables,
c'est-à-dire s'il existe une suite de fonctions intégrables 
$f_k:\R \to \R$ telle que 
pour tout $x\in \R$, 
$f_k(x) \to f(x)$ quand $k \to +\infty$.
Une fonction $f:\R \to \R^n$ est mesurable 
si chacune de ses composantes est mesurable.

### Mesurabilité sur un intervalle {.remark}
Nous nous limitons dans ce chapitre à l'étude des fonctions mesurables
définies sur $\R$. La notion peut être très facilement étendue
à une fonction $f$ définie sur un intervalle fermé $I$ de $\R$ de la
façon suivante : on dira que $f$ est mesurable si son prolongement par $0$
dans le complémentaire de $I$ est mesurable. Nous vous laissons le soin
de généraliser en conséquence les énoncés qui vont suivre.

### Critère d'intégrabilité dominée {.theorem #CID}
Une fonction $f: \R \to \R$ est intégrable si et seulement
si $f$ est mesurable et il existe deux fonctions intégrables 
$g: \R \to \R$ et $h: \R \to \R$ telles que
$g \leq f \leq h$.


### Interprétation {.post .remark}
Souvenons-nous qu'une fonction définie sur un intervalle fermé et borné 
est intégrable au sens de Riemann si et seulement si elle est encadrée 
par deux fonctions intégrables au sens de Riemann et continue presque partout.

Dans le cas de l'intégrale de Riemann comme de Henstock-Kurzweil, 
l'intégrabilité est donc caractérisée par une structure analogue qui
repose sur deux propriétés distinctes :
être encadrée par deux fonctions intégrables (pour la notion d'intégrale
considérée) et être "suffisamment régulière". 
La différence est que dans le cas de l'intégrale de Riemann
l'exigence de régularité est forte -- être continue presque partout --
alors que dans le cas de l'intégrale de Henstock-Kurzweil, 
la régularité demandée -- la mesurabilité -- s'avère être une 
condition très peu contraignante[^note].

[^note]: A tel point que s'il l'on peut prouver l'existence d'une fonction
non-mesurable, sa "construction explicite" est impossible. Les fonctions
non-mesurables font partie des objets "intangibles" (cf. @Sch96) dont
l'existence est prédite par la théorie mais que l'on ne rencontre jamais 
en pratique ...

### {.ante}
Plusieurs propriétés des fonctions mesurables se déduisent directement de
leur définition :

### Les fonctions intégrables sont mesurables {.proposition}

### Démonstration {.proof}
Si $f$ est une fonction intégrable, elle est la limite simple de la suite
constante égale à $f$.

### Les fonctions mesurables forment un espace vectoriel  {.proposition}

### Démonstration {.proof}
Si $f$ et $g$ sont mesurables et $\lambda$ est un nombre réel, 
il existe des suites $f_k$ et $g_k$ de fonctions intégrables
convergeant simplement vers $f$ et $g$ respectivement.
Les fonctions $f_k + g_k$ et $\lambda f_k$ sont intégrables
et convergent alors simplement vers $f+g$ et $\lambda f$ 
respectivement.

<!--
### TODO ?

Evoquer fct localement intégrable ? Quand on regarde la preuve ci-dessous,
on n'utilise pas autre chose ...
-->

### Les fonctions continues (presque partout) sont mesurables

### Démonstration {.proof}

Soit $f:\R \to \R$ une fonction continue presque partout. 
Soit $k \in \N$ ; on note $\sigma_k:\R \to \R$ la fonction
définie par
$$
\sigma_k(x)
=
\left|
\begin{array}{rl}
-k & \mbox{si $x \in \left]-\infty, -k\right]$,} \\
x  & \mbox{si $x \in \left]-k, k\right[$,} \\
k & \mbox{si $x \in \left[k, +\infty\right[$.} \\
\end{array}
\right.
$$

Comme $\sigma_k$ est continue et bornée, 
la fonction $g_k : [-k, k] \to \R$ définie par 
$$
x \in [-k, k] \mapsto (\sigma_k \circ f)(x)
$$
est continue presque partout sur $[-k, k]$ et bornée.
Par conséquent, elle est intégrable au sens de Riemann -- 
et donc de Henstock-Kurzweil -- sur $[-k, k]$. Son extension
$f_k$ par zéro au reste de $\R$ est donc intégrable au sens de
Henstock-Kurzweil. De plus, la suite des $f_k$ converge simplement vers $f$ ;
la fonction $f$ est donc mesurable. 

### Critère de l'image réciproque {.theorem #CIR}
Une fonction $f:\R \to \R^n$ est mesurable si et seulement
l'image réciproque de tout fermé (ou de tout ouvert) de $\R^n$
par $f$ est mesurable.

### {.post .remark}

--------------------------------------------------------------------------------

Ce critère ressemble beaucoup à la caractérisation abstraite des fonctions
continues, qui exige que l'image de tout fermé (ou de tout ouvert)
soit un fermé (ou un ouvert). Comme [tout fermé (et tout ouvert) est
mesurable](#OSM), ce critère montre de façon particulièrement simple
que toute fonction continue est mesurable.


<!--
**NOTA:** l'énonce ici est donné dans le cas des fonctions scalaires,
mais on a rapidement besoin du cadre vectoriel (pour composer avec
des opérateurs binaires), ce qui renforce encore l'attrait de la 
formulation "abstraite" (qui "tient" dans le cas vectoriel, mais
pas les autres). donc **TODO:** nettoyer, ne garder que le cas 3.,
et rajouter le bout de démo qui finit la preuve dans le cas vectoriel
(dans les deux sens).

**TODO:** update: énoncé patché, adapter la preuve en fonction.

**TODO:** remarque très rapidement sur la forme abstraite et lien avec la
continuité.
-->

### {.ante}
En se basant exclusivement sur ce critère de mesurabilité par 
les images réciproques (donc en comprenant temporairement 
"mesurable" comme "satisfaisant le critère de l'image réciproque"
en attendant la preuve de l'équivalence des deux propriétés), 
on peut montrer les résultats suivants:

### Stabilité par passage à la limite {#SPL}
Les limites simples de fonctions mesurables sont mesurables.

### Démonstration {.proof}
Soit  $f_k: \R \to \R$ des fonctions vérifiant 
[le critère de l'image réciproque](#CIR), 
telles que pour tout $x \in \R$, $f_k(x) \to f(x)$ quand $k \to +\infty$.
Montrons que $f$ vérifie également ce critère.
Il suffit pour cela de remarquer que comme $U$ est ouvert et que
$f_k(x) \to f(x)$, $f(x) \in U$ si et seulement si $f_k(x) \in U$
pour $k$ assez grand. Cette déclaration se traduit par la formule
$$
f^{-1}(U) = \bigcup_{j=0}^{+\infty} \bigcap_{k = j}^{+\infty} f_k^{-1}(U)
$$
qui établit que $f^{-1}(U)$ est un ensemble mesurable, comme union 
(dénombrable) d'intersections (dénombrable) d'ensembles mesurables.

### Fonctions égales presque partout {.theorem #FPPE}
Toute fonction égale presque partout à une fonction mesurable est
mesurable.

### Démonstration {.proof}
Toute fonction $f$ égale presque partout à une fonction $g$ qui vérifie 
[le critère de l'image réciproque](#CIR) vérifie également 
[le critère de l'image réciproque](#CIR). 
En effet, si pour tout ouvert $U$ l'ensemble $g^{-1}(U)$ est mesurable, 
alors
$$
f^{-1}(U) = (g^{-1}(U) \setminus E) \cup F
$$
où $E$ et $F$ sont négligeables (et donc mesurables puisque la mesure
de Lebesgue est complète) ;
par conséquent, $f^{-1}(U)$ est mesurable.

### Démonstration du [critère de l'image réciproque](#CIR) {.proof #pCIR}
Il suffit de démontrer le critère pour les ensembles ouverts : 
si une fonction satisfait le critère de d'image réciproque pour
tout ouvert de $\R^n$, alors si $F$ est un fermé de $\R^n$, 
en utilisant l'égalité $f^{-1}(F) = \R \setminus f^{-1}(\R^n \setminus F)$,
le fait que le complémentaire d'un fermé soit un ouvert et 
que [le complémentaire d'un ensemble mesurable soit mesurable](#pptés-tribus),
on établit le critère pour les fermés.

Montrons tout d'abord le résultat pour les fonctions scalaires ($n=1$).
Supposons [le critère de l'image réciproque](#CIR) satisfait. 
La démonstration repose sur la construction explicite d'une suite $f_k(x)$ 
de fonctions intégrables qui soient étagées, c'est-à-dire ne prenant qu'un
nombre fini de valeurs possibles.

Définissons $f_0(x) = 0$ et $f_k(x)$ par la relation de récurrence
$$
f_{k+1}(x) = f_k(x) + 
\left|
\begin{array}{rl}
-1/k & \mbox{si } \, f(x) \leq f_k(x) -1/k \, \mbox{ et } \, |x| \leq k,\\
+1/k  & \mbox{si } \, f_k(x) + 1/k \leq f(x)  \, \mbox{ et } \, |x| \leq k, \\
0 & \mbox{sinon.}
\end{array}
\right.
$$
Par construction, si $f(x)=0$, $f_k(x)= 0$. Si $f(x) \geq 0$, les $f_k(x)$
forment une suite croissante convergeant vers $f(x)$, car la suite des
$1/k$ tend vers $0$ quand $k$ tend vers $+\infty$, mais leur somme est 
divergente. La situation est similaire si $f(x) \leq 0$, mais avec une
suite $f_k(x)$ décroissante.

Montrons que la suite des $f_k$ est intégrable, ce qui concluera cette 
section de la preuve.
L'ensemble des valeurs $\{y_j\}$ que prend chaque $f_k$ est bien fini ;
il comprend la valeur $y_0 = 0$ et la fonction 
peut s'écrire sous la forme
$$
f_k = \sum_{j} y_j 1_{A_j}
$$
où les $A_j = f_k^{-1}(y_j)$ sont en nombre fini et disjoints.
A part $A_0$, les $A_j$ sont également bornés, 
car $f_k$ est nulle en dehors de $[-k, k]$.
Montrons qu'à tout rang $k$, les ensembles $A_j$ sont mesurables, 
ce qui prouvera que chaque $f_k$ est intégrable par le critère d'intégrabilité
dominé.
C'est évident au rang $0$ où 
$\{y_j\} = \{0\}$ et la collection des $A_j$ se réduit à 
$\{A_0\} = \{\R\}$.
Supposons cette propriété valable au rang $k$ ;
l'ensemble $E$ des
réels $x$ tels que $f_k(x) + 1/k \leq f(x)$ et $|x| \leq k$
peut être écrit comme
$$
E = \left(\bigcup_j \{x \in \R \, | \, y_j + 1/k \leq f(x)\} \cap A_j\right) \cap [-k, k],
$$
qui est mesurable. 
De même, on peut montrer que l'ensemble $F$ des
réels $x$ tels que $f(x) \leq f_k(x) - 1/k$ et $|x| \leq k$ est mesurable.
On a alors par construction: 
$$
f_{k+1} = \sum_{j} y_j 1_{A_j} + \frac{1}{k} 1_E - \frac{1}{k} 1_F
$$
qui est sous la forme souhaitée, à ceci près que les ensembles intervenant
ne sont pas nécessairement disjoints. Mais pour toute valeur $y$ dans l'image
de $f_{k+1}$, l'image réciproque de $\{y\}$ par $f$ est nécessairement une
union (finie) d'intersections (finies) d'ensembles dans la collection 
$\{\dots, A_j, \dots, E, F\}$ et donc un ensemble mesurable. La fonction 
$f_{k+1}$ peut donc être mise sous la forme souhaitée.

Réciproquement, considérons désormais une fonction intégrable $f:\R \to \R$.
Par le [théorème de dérivation des intégrales indéterminées](#DII),
si l'on définit la fonction $f_k(x)$ comme le taux d'accroissement
$$
f_k(x) :=  \frac{F(x + 2^{-k}) - F(x)}{2^{-k}}
\; \mbox{ où } \;
F: x \in \R \mapsto \int_0^x f(t) \, dt,
$$
alors $f_k(x) \to f(x)$ presque partout quand $k \to +\infty$.
Or chaque $f_k$ est continue, donc l'image réciproque de tout ouvert
par $f_k$ est un ouvert [et donc un ensemble mesurable](#OSM) ;
c'est encore le cas des fonctions qui sont égales presque partout aux 
$f_k$ mais valent $0$ aux points ou les $f_k$ ne convergent pas,
car [elles sont égales presque partout aux fonctions $f_k$](#FPPE).
L'ensemble des fonctions satisfaisant le critère de l'image réciproque 
étant [stable par passage à la limite](#SPM), 
[une fonction égale à $f$ presque partout satisfait le critère de l'image réciproque](#FPPE) ;
la fonction intégrable $f$ satisfait donc 
elle-même le critère de l'image réciproque.

Finalement, une fonction mesurable étant limite simple
d'une suite de fonctions intégrables et les fonctions intégrables 
vérifient le critère de l'image réciproque, 
par une nouvelle application du résultat de 
[stabilité par passage à la limite](#SPL), 
ce critère est également satisfait pour toute fonction mesurable.

Pour établir le résultat dans le cas où $n>1$, il suffit de montrer qu'une
fonction $f:\R \to \R^n$ satisfait le critère de l'image réciproque si et
seulement si toutes ses composantes le satisfont. Pour le sens direct,
il suffit de constater que 
$$
f_k^{-1}(U) = f^{-1}(\R \times \cdots \times U \times \cdots \R)
$$
et que si $U$ est ouvert, $\R \times \cdots \times U \times \cdots \R$ également.
Pour la réciproque, nous exploitons le fait[^demo] que tout ouvert de $\R^n$ peut être
décomposé comme l'union d'une collection dénombrable $\mathcal{P}$ 
de pavés ouverts de la forme
$$
P = \left]a_1,b_1\right[ \times \dots \times \left]a_n,b_n\right[.
$$
Il nous suffit alors de noter que pour tout pavé $P$,
$$
f^{-1}(P) = f_1^{-1}(\left]a_1,b_1\right[) \times \dots \times f_n^{-1}(\left]a_n,b_n\right[)
$$
et donc $f^{-1}(P)$ est mesurable. 
Comme $f^{-1}(U) = \cup_{P \in \mathcal{P}} f^{-1}(P)$ et que $\mathcal{P}$
est dénombrable, l'image réciproque de $U$ par $f$ est bien mesurable.

[^demo]: la démonstration est similaire à la décomposition d'un ouvert de
$\R$ en une collection d'intervalle ouvert : pour chaque point $x$ de 
$U \subset \R^n$ ouvert dont les coordonnées sont rationnelles, 
on considère le plus grand pavé ouvert $P_x$ qui contienne $x$ ; 
ces pavés forment une collection dénombrable et leur union 
est égale à $U$ par construction.

### Composition par une fonction continue {.theorem #CFC}

Soit $f:\R \to \R^n$ une fonction mesurable et 
$g:\R^n \to \R^m$ une fonction continue.
La composée $g \circ f$ de ces deux fonctions est mesurable.

### {.remark .post}
Dans le cas d'une fonction $g: \R \to \R$, il suffit de supposer que
$g$ soit continue par morceaux pour pouvoir conclure (cf. exercice
["Composition de fonctions et mesurabilité"](#cfm)).
En général, les fonctions $g$ qui assurent que 
$g \circ f$ soit mesurable pour toutes les fonctions mesurables
$f$ sont appelées fonction *boréliennes* ; elles seront étudiées plus
en détail par la suite.

### Démonstration {.proof}
Si $F$ est un fermé de $\R^m$.
Par continuité de $g$, l'ensemble $g^{-1}(F)$ est un fermé de $\R^n$ 
et par conséquent, par [le critère de mesurabilité par les images réciproques](#CIR)
$$
(g\circ f)^{-1}(F) = f^{-1}(g^{-1}(F))
$$
est un ensemble mesurable. Par le même critère, 
la composée $g\circ f$ est donc mesurable.

### {.remark}
Les corollaires de ce résultat sont nombreux et immédiats. 
Citons les deux instances les plus directement utiles.

### Mesurabilité du produit {.corollary #prod}

Le produit de deux fonctions scalaires mesurables est mesurable.

### Démonstration {.proof}

Par continuité de l'application produit 
$\times: \R \times \R \to \R$.

### Mesurabilité de la valeur absolue {.corollary #abs}

La valeur absolue d'une fonction scalaire mesurable est mesurable.

### Démonstration {.proof}

Par continuité de l'application valeur absolue
$|\, \cdot \,|: \R \to \R$.

### Démonstration du critère d'intégrabilité dominée {.proof}
Le sens direct est évident :
si la fonction $f$ est intégrable, elle est mesurable et satisfait
les inégalités $f \leq f \leq f$. 

Nous notons que pour établir la réciproque, il suffit de se limiter au cas
où $g=0$. En effet si le résultat est établi dans ce cas précis, sous
les hypothèses plus générales on a $0 \leq f - g \leq h -g$ où $f-g$
est mesurable et $h - g$ est intégrable ; $f -g$ est alors intégrable,
et donc $f$ est intégrable.

Pour montrer la réciproque dans ce cas, nous approchons 
la fonction mesurable $f$ par la suite de fonctions étagées $f_k$ 
définie par le procédé de [la démonstration du critère de l'image réciproque](#pCIR). 
La fonction $f$ apparaît comme une limite simple des
fonctions $f_k$, qui sont intégrables et
encadrées par les fonctions intégrables $0$ et $h$. 
Par le théorème de convergence dominée, $f$ est intégrable.


Fonctions absolument intégrables
================================================================================

### {.ante}
Un grand nombre de résultats d'intégration 
-- dont [le critère d'intégrabilité dominée](#CID) -- 
sont plus faciles à exploiter quand les fonctions
que l'on considère sont intégrables ainsi que leur valeur absolue.

### Fonction absolument/conditionnellement intégrable {.definition} 
Une fonction $f:\R \to \R$ est *absolument intégrable*
si $f$ et $|f|$ sont intégrables. 
Si $f$ est intégrable mais pas $|f|$, 
elle est *conditionnellement intégrable*.

### {.post .remark .definition}
Une intégrale (l'intégrale de Newton, Riemann, Henstock-Kurzweil, etc.)
est dite *conditionnelle* si elle admet des fonctions
conditionnellement intégrables ; dans le cas contraire -- si le fait que
$f$ soit intégrable implique que $|f|$ le soit également, 
elle est dite *absolue*.

### Produit de fonctions absolument intégrable et bornée {.corollary}
Si $f: \R \to \R$ est une fonction absolument intégrable 
et $g: \R \to \R$ est une fonction mesurable et bornée,
alors le produit $fg$ est (absolument) intégrable.

### Preuve {.proof}
Par hypothèse $f$ est intégrable donc mesurable ; $g$ étant mesurable,
le produit $fg$ est mesurable. Par ailleurs, si $|g| \leq M$, on a
$$
- M |f| \leq f g \leq M |f|
$$
et comme les fonctions $-M|f|$ comme $M |f|$ sont intégrables, 
par [le critère d'intégrabilité dominée](#CID), $fg$ est intégrable. 
La valeur absolue $|fg|$ de $fg$ est mesurable
et vérifie également $- M |f| \leq f g \leq M |f|$, 
elle est donc également intégrable par le même critère.

### Fonctions absolument intégrables {.theorem}
L'ensemble des fonctions absolument intégrables 
<!-- de $\R$ dans $\R$ --> est un espace vectoriel.

### Démonstration {.proof}
Si $f$ et $g$ sont absolument intégrables et $\lambda \in \R$,
alors $\lambda f$ est mesurable et $\lambda f$ comme $|\lambda f|$
sont encadrées par les fonctions intégrables $-|\lambda||f|$ et
$|\lambda||f|$ ; $f$ est donc absolument intégrable par le critère
d'intégrabilité dominée. La somme $f + g$ est également mesurable
et $f+g$ comme $|f+g|$ sont encadrées par $-|f| - |g|$ et $|f| + |g|$ qui
sont intégrables ; la somme est donc intégrable par le même critère.

### Inégalité triangulaire {.theorem}
Si $f: \R \to \R$ est absolument intégrable, alors
$$
\left|\int f(t)\, dt \right| 
\leq 
\int |f(t)| \,dt.
$$

### Démonstration {.proof}
Les fonctions $f$ et $|f|$ étant intégrables, pour tout $\varepsilon > 0$,
il existe une jauge commune $\gamma$ sur $\R$ telle que pour toute 
subdivision pointée $\mathcal{D}$ de $\R$ qui soit subordonnée à $\gamma$, 
on ait
$$
\left| S(f, \mathcal{D}) - \int f(t) \, dt \right| \leq \varepsilon/2
\; \mbox{ et } \;
\left| S(|f|, \mathcal{D}) - \int |f(t)| \, dt \right| \leq \varepsilon/2.
$$
Par l'inégalité triangulaire appliquée à la somme finie $S(f, \mathcal{D})$, on
obtient donc
$$
\left|
\int f(t) \, dt
\right| 
\leq |S(f, \mathcal{D})| + \varepsilon /2
\leq S(|f|, \mathcal{D}) + \varepsilon /2
\leq \int |f(t)| \, dt + \varepsilon,
$$
et en passant à la limite sur $\varepsilon$, l'inégalité cherchée.

### Une fonction conditionnellement intégrable {.example}

La fonction $f:[0, 1] \to \R$ définie par
$$
f(x) = \frac{1}{x} \cos \frac{1}{x^2} \, \mbox{ si }\,  x > 0 \, \mbox{ et } \, f(0) = 0
$$
est conditionnellement intégrable. 

![](images/f.py)\

Pour montrer qu'elle est intégrable, 
nous exploitons [le théorème fondamental du calcul](Calcul Intégral I.pdf/#TFC), 
appliqué à la fonction $g:[0, 1] \to \R$ définie par 
$$
g(x) = -\frac{x^2}{2} \sin \frac{1}{x^2} \, \mbox{ si }\,  x > 0 \, \mbox{ et } \, g(0) = 0.
$$
Cette fonction est dérivable en tout point de $[0,1]$ ; en $0$, sa dérivée est 
nulle[^dn] et quand $x>0$,
$$
\left[-\frac{x^2}{2} \sin \frac{1}{x^2} \right]' +
x \sin \frac{1}{x^2} 
= \frac{1}{x} \cos \frac{1}{x^2}.
$$
Par [le critère d'intégrabilité dominée](#CID), la fonction $h(x)$ égale à
$x \sin (1/x^2)$ si $x>0$ et nulle en zéro est absolument intégrable
car continue sur $[0, 1]$.
<!--[^details]-->
La fonction $g'$ étant également intégrable, $f = g' + h$ est intégrable comme
somme de deux fonctions intégrables.

[^dn]: En effet,
$$
\left| \frac{g(h) - g(0)}{h} \right| \leq \frac{|h|}{2} \to 0 \, \mbox{ quand } \, h \to 0.
$$

<!--
[^details]: La  fonction $h$ est mesurable comme limite des 
suite des fonctions continues $h_k$ -- et donc intégrables -- définies par 
$h_k(x) = 0$ si 
$x \in [0, 1/\sqrt{2k\pi}]$ et $h_k(x) = h(x)$ sinon. De la même façon,
$|h|$ est limite des fonctions intégrables $|h_k|$.
Par ailleurs, $h$ comme $|h|$ sont encadrées par les deux fonctions intégrables
$x\in [0,1] \mapsto -x$ et $x\in [0,1] \mapsto x$.
-->

La fonction $f$ n'est pourtant pas absolument intégrable, 
car $h$ est absolument intégrable mais pas $g'$.
En effet, si c'était le cas, toute fonction absolument intégrable
dont la valeur absolue est majorée par $|g'|$ aurait par l'inégalité
triangulaire son intégrale majorée par celle de $|g'|$. 
Or nous allons exhiber une suite de telles fonctions dont l'intégrale
tend vers $+\infty$, ce qui établira la contradiction.

Soit $k\geq 1$ un entier ; on définit la function $\phi_k:[0,1] \to \R$ 
par
$$
\phi_k(x) = 
\left|
\begin{array}{rl} 
g'(x) & \mbox{si } \, \alpha_j \leq x \leq \beta_j, \, 1 \leq j \leq k\\
0 & \mbox{sinon.}
\end{array}
\right.
$$
où
$$
\alpha_j = \frac{1}{\sqrt{2\pi (j + 1/4)}}
\; \mbox{ et } \;
\beta_j = \frac{1}{\sqrt{2\pi(j - 1/4)}},
$$

L'idée sous-jacente est la suivante :
les fonctions $\phi_k$ sont faites pour coïncider avec $g'$ dans les 
plages de valeurs où $\cos 1/x^2$ est positif ; comme 
$g'(x) = - x \sin {1}/{x^2} + (1/x)\cos {1} / {x^2}$,
et que pour $x$ petit, $1/x$ est grand devant $x$, cela correspond 
approximativement aux plages où $g'(x)$ est positif.

![...](images/g-prime.py)\

Par construction, $\phi_k$ est continue par morceaux et donc absolument 
intégrable, et bien telle que $|\phi_k| \leq |g'|$.
Par ailleurs,
$$
\begin{split}
\int_0^1 \phi_k(t) \, dt &= \sum_{j=0}^k \int_{\alpha_j}^{\beta_k} \phi_k(t) \, dt \\
&=\sum_{j=0}^k \left[-\frac{x^2}{2} \sin \frac{1}{x^2} \right]_{\alpha_j}^{\beta_j} \\
&=\sum_{j=0}^k \left[-\frac{1}{4\pi(j-1/4)} \sin (2\pi(j-1/4)) \right. \\
&\phantom{=\sum_{j=0}^k \left[\right.} \left. +\frac{1}{4\pi(j+1/4)} \sin (2\pi(j+1/4)) \right] \\
&=\sum_{j=0}^k \frac{1}{4\pi}\left[\frac{1}{j-1/4} + \frac{1}{j+1/4}\right] \\
&= \frac{1}{2 \pi}\sum_{j=0}^k \frac{j}{j^2 + 1/16}. \\
\end{split}
$$
Comme la série associée à cette équation est divergente, 
on peut rendre l'intégrale arbitrairement grande en choisissant
un $k$ suffisamment grand, ce qui permet de conclure.

### Intégrabilité sur un sous-ensemble {.definition}
Une fonction $f: \R \to \R$ est dite *intégrable (resp. absolument intégrable) 
sur un sous-ensemble $E$ de $\R$* si la fonction $f 1_E$ est intégrable
(resp. absolument intégrable). On note alors
$$
\int_E f(x) \, dx = \int 1_E(x) f(x) \, dx.
$$

### {.remark .post}
Cette définition est cohérente avec la définition existant déjà dans le cas
où $E$ est un intervalle de $\R$ (cf. ["Extension à la droite réelle achevée"
dans Calcul Intégral I](Calcul Intégral I.pdf/#EDRA)).

### Restriction à des ensembles mesurables {.corollary}
Une fonction $f:\R \to \R$ est absolument intégrable
si et seulement si $f$ est (absolument) intégrable sur $E$
pour tout ensemble mesurable $E$. 

### Démonstration {.proof}
Si $f$ est absolument intégrable, elle est mesurable ; si l'ensemble
$E$ est mesurable, sa fonction caractéristique $1_E$ est également
mesurable. Par conséquent, le produit $f 1_E$ est mesurable, 
comme sa valeur absolue $|f 1_E|$.
Par ailleurs, comme $|1_E| \leq 1$, on a 
$-|f| \leq f1_E \leq |f|$ et donc $-|f| \leq |f1_E| \leq |f|$.
Par [le critère d'intégrabilité dominée](#CID), 
$f 1_E$ est (absolument) intégrable.

Réciproquement, supposons $f 1_E$ intégrable pour tout ensemble mesurable 
$E$. En prenant $E = \R$, on constate que $f$ est intégrable,
et donc mesurable.
Notons $E_+ = \{x \in \R \, | \, f(x) \geq 0 \}$ et 
$E_- = \{x \in \R \, | \, f(x) \leq 0 \}$ ; ces deux ensembles sont
mesurables [comme images réciproques de fermés par une fonction mesurable](#CIR).
La fonction $|f|$ satisfaisant
$$
|f| = 1_{E_+} f - 1_{E_-} f,
$$
elle est intégrable comme somme de fonctions intégrables.
La fonction $f$ est donc absolument intégrable.


Annexes
================================================================================

<!-- suppression temporaire, cf <https://github.com/boisgera/CDIS/issues/29>

Ensembles non mesurables
--------------------------------------------------------------------------------

L'ensemble $\R / \Q$ 
-- la droite des réels quotientée par l'ensemble des rationnels -- 
désigne une partition de $\R$ construite de la façon suivante:
les éléments $A$ de $\R / \Q$ sont de la forme
$$
A = \{r + q \, | \, q \in \Q \}, \; r \in \R.
$$
Par exemple, l'ensemble $A$ associée à $r=0$ est $\Q$ ; c'est le même que
celui associé à $1/2$ ou $1$ car la différence entre ces valeurs est 
rationnelle. Tout élément $A$ de $\R / \Q$ est d'intersection non vide avec
$[0, 1]$. Nous avons donc une famille d'ensembles non vides indexées par
$A \in \R / \Q$ définie par
$$
A \in \R / \Q \mapsto A \cap [0, 1].
$$
L'axiome du choix nous garantit donc l'existence d'une fonction de choix
$f$ définie sur $\R / \Q$ telle que pour tout $A \in \R / \Q$,
$f(A) \in A \cap [0, 1]$. On appelle alors *ensemble de Vitali* l'ensemble
$$
V := \{f(A) \, | \, A \in \R / \Q \}.
$$
(sa définition dépend de la fonction de choix considérée).

### Existence d'un ensemble non-mesurable 
Tout ensemble de Vitali est non-mesurable.

### TODO -- Démonstration {.proof}

-->

Maximum de fonctions intégrables
--------------------------------------------------------------------------------

### Maximum de fonctions intégrables et positives {.lemma #max}
Si les fonctions $f: \R \to \left[0, +\infty\right[$ et $g: \R \to \left[0, +\infty\right[$ 
sont intégrables, la fonction $\max(f, g)$ est également intégrable.

### Démonstration {.proof}
Pour simplifier le problème, on remarque tout d'abord que 
$$\max(f, g) = f + \max(g - f, 0) = f + (g-f)_+$$ 
où $x _+ = \max(x, 0)$ désigne la partie positive de $x$.
Par linéarité, la fonction $g-f$ est intégrable et 
$(g-f)_+ \leq g + f$ ; la fonction $g+f$ est également intégrable.
Pour démontrer le lemme, il nous suffit donc de prouver que 
toute fonction intégrable dont la partie positive est dominée
par une fonction intégrable est de partie positive intégrable.

Soit $f$ une telle fonction et $g$ une fonction intégrable telle que 
$f_+ \leq g$. Nous allons montrer que
$$
\int f_+(t) \, dt 
= S :=
\sup_{\mathcal{D}} 
\sum_{(t, I) \in \mathcal{D}} \left( \int_I f(t) \, dt\right)_{\!\!+}
$$
où le supremum est calculé sur toutes les subdivisions pointées de $\R$.
Tout d'abord, ce supremum est fini ; en effet pour toute subdivision
$\mathcal{D}$, on a
$$
\begin{split}
\sum_{(t, I) \in \mathcal{D}} \left( \int_I f(t) \, dt\right)_{\!\!+}
&\leq
\sum_{(t, I) \in \mathcal{D}} \left( \int_I g(t) \, dt\right)_{\!\!+} \\
&=
\sum_{(t, I) \in \mathcal{D}} \int_I g(t) \, dt \\
&=
\int g(t) \, dt.
\end{split}
$$
Soit $\varepsilon > 0$ et $\mathcal{D}_{0}$ une subdivision pointée
de $\R$ telle que
$$
S - \frac{\varepsilon}{2} 
\leq \sum_{(t, I) \in \mathcal{D}_0} \left( \int_I f(t) \, dt\right)_{\!\!+} 
\leq S.
$$
Soit $\lambda$ une jauge sur $\R$ assurant une précision $\varepsilon/2$
dans l'estimation de l'intégrale de $f$ par les sommes de Riemann.
Soit $\nu$ une jauge sur $\R$ telle que si $(t, [a, b]) \in \mathcal{D}_0$
et $t \in \left]a,b\right[$ alors $\nu(t) \subset \left]a,b\right[$ ;
on note $\gamma$ la jauge définie par $\gamma(t) = \lambda(t) \cap \nu(t)$.
Si $\mathcal{D}$ est subordonnée à $\gamma$, quitte à découper des intervalles
en deux si $(t, I) \subset \mathcal{D}$ et $t$ appartient à la frontière
d'un intervalle composant $\mathcal{D}_0$ -- ce qui ne change pas la somme
de Riemann associée -- les éléments $(t, J) \in \mathcal{D}$ tels que
$J \subset I$, où $(x, I) \subset \mathcal{D}_0$ forment une subdivision
pointée de $I$. Par conséquent, comme 
$$
\left( \int_I f(t) \, dt\right)_{\!\!+} 
=
\left( \sum_{(t, J) \in \mathcal{D}, J \subset I}\int_J f(t) \, dt\right)_{\!\!+} 
\leq 
\sum_{(t, J) \in \mathcal{D}, J \subset I} \left(\int_J f(t) \, dt\right)_{\!\!+} 
$$
et donc
$$
S - \frac{\varepsilon}{2} \leq 
\sum_{(t, I) \in \mathcal{D}_0} \left( \int_I f(t) \, dt\right)_{\!\!+} 
\leq 
\sum_{(t, I) \in \mathcal{D}} \left( \int_I f(t) \, dt\right)_{\!\!+}
\leq S, 
$$
on obtient
$$
\left|
\sum_{(t, I) \in \mathcal{D}} \left( \int_I f(t) \, dt\right)_{\!\!+}
- S \right| \leq \frac{\varepsilon}{2}.
$$
Par ailleurs, si l'on considère la subdivision (partielle) pointée 
$\mathcal{D}_+$ extraite de $\mathcal{D}$ composée des paires
$(t, I) \in \mathcal{D}$ et telles que
$$
f(t) \ell(I) \geq \int_I f(x) \, dx,
$$
alors le [lemme de Henstock](Calcul Intégral I.pdf/#henstock-lemma) fournit
$$
\sum_{(t, I) \in \mathcal{D}} 
\left( f(t) \ell(I) - \int_I f(x) \, dx \right)_{\!\!+}
\leq \frac{\varepsilon}{2}.
$$
Comme $(x+y)_+ \leq x_+ + y_+$, on en déduit
$$
\sum_{(t, I) \in \mathcal{D}} 
f_+(t) \ell(I) - 
\sum_{(t, I) \in \mathcal{D}} 
\left(\int_I f(x) \, dx \right)_{\!\!+}
\leq \frac{\varepsilon}{2}.
$$
De façon similaire, en raisonnant sur la subdivision partielle complémentaire
à $\mathcal{D}_+$ dans $\mathcal{D}$, on peut montrer que
$$
\sum_{(t, I) \in \mathcal{D}} 
\left(\int_I f(x) \, dx \right)_{\!\!+} - 
\sum_{(t, I) \in \mathcal{D}} 
f_+(t) \ell(I)
\leq \frac{\varepsilon}{2}.
$$
On obtient donc au final
$$
\left|
\sum_{(t, I) \in \mathcal{D}} f_+(t) \ell(I) 
- 
S
\right| 
\leq 
\frac{\varepsilon}{2};
$$
la fonction $f_+$ est donc intégrable, d'intégrale égale à $S$.

Dérivabilité des intégrales indéterminées
--------------------------------------------------------------------------------

### Une intégrale indéterminée est dérivable presque partout {.theorem #DII}
Soit $I$ un intervalle fermé de $\R$, 
$f: I \to \R$ une fonction intégrable et un point 
$a$ de $I$.
La dérivée de la fonction
$$
F: x\in I \mapsto \int_a^x f(t) \, dt
$$
existe et est égale à $f$ presque partout.

### Démonstration {.proof}
Voir [@Swa01, pp. 135-136].

Exercices
================================================================================

Théorème de convergence dominée {.question #exo-TCD}
--------------------------------------------------------------------------------

Montrer que la conclusion [du théorème de convergence dominée](#TCD)
est toujours valide si les fonctions $f_k$ ne satisfont 
les hypothèses de convergence et d'encadrement que presque partout.

Ensembles de longueur finie {.question #lf}
--------------------------------------------------------------------------------

Soit $A$ un ensemble mesurable de $\R$ pour lequel il existe une
constante $L$ (finie) telle que pour tout intervalle compact
$[a, b]$, on ait
$$
\int_a^b 1_A(t) \, dt \leq L.
$$

Montrer que $A$ est de longueur finie et que $\ell(A) \leq L$.

Intégrabilité locale
--------------------------------------------------------------------------------

Une fonction $f: \R \to  \R$ est dite *localement intégrable* 
si tout point $x$ de $\R$, il existe un $\varepsilon > 0$ 
et un intervalle $[x+\varepsilon, x+\varepsilon]$ 
où la fonction $f$ soit intégrable.

### Question 0 {.question #il-0}
Montrer que $f$ est localement intégrable si et seulement si
pour tout intervalle compact $[a, b]$ de $\R$, $f$ est intégrable
sur $[a, b]$.

### Question 1  {.question #il-1}
Montrer que toute fonction localement intégrable est mesurable.

### Question 2  {.question #il-2}
La réciproque est-elle vraie ?
 
Fonctions mesurables 
--------------------------------------------------------------------------------

### Question 1 {.question #fm-1}
Montrer qu'une fonction $f: \R \to \R$ est mesurable si et
seulement si pour tout nombre réel $a$, l'ensemble
$$
f^{-1}(\left]-\infty, a\right]) = \{x \in \R \, | \, f(x) \leq a\}
$$
est mesurable.

### Question 2 {.question #fm-2}
En déduire qu'une fonction croissante $f: \R \to \R$ est intégrable 
sur tout intervalle compact.

Composition de fonctions et mesurabilité {.question #cfm}
--------------------------------------------------------------------------------
Montrer que si la fonction $f:\R \to \R$ est mesurable et que la
fonction $g: \R \to \R$ est continue par morceaux, 
alors la fonction composée $g \circ f$ est mesurable.

Composition par une fonction lipschitzienne 
--------------------------------------------------------------------------------

Soit $f:[0,1] \to \R$ et $g:\R \to \R$.
On suppose que $g$ est nulle en $0$ et lipschitzienne, 
c'est-à-dire qu'il existe un $K\geq0$ tel que pour toute paire de réels 
$x$ et $y$  on ait
$|g(x) - g(y)| \leq K |x - y|$.

### Question 1 {.question #cfl-1}
Si $f$ est mesurable est-ce que $g \circ f$ est mesurable ?

### Question 2 {.question #cfl-2}
Si $f$ est intégrable, est-ce que $g \circ f$ est intégrable ?

### Question 3 {.question #cfl-3}
Si $f$ est absolument intégrable, est-ce que $g \circ f$ est 
  absolument intégrable ?

Caractérisation des ensembles mesurables {.question #cer}
--------------------------------------------------------------------------------

Montrer qu'un ensemble $E \subset \R$ est mesurable si et seulement si
sa fonction caractéristique $1_E$ est mesurable.


Formule de la moyenne 
--------------------------------------------------------------------------------

Soit $f: U \subset \R^2 \to \R^2$ une fonction définie sur un
ensemble $U$ ouvert et supposée continûment différentiable. 
On considère $c \in U$ et $R > 0$ tel 
que le disque fermé centré en $c$ 
et de rayon $R$ soit inclus dans $U$; on définit alors la grandeur 
$I(r)$ pour tout $r \in [0, R] \to \R^2$ comme la valeur moyenne
du vecteur $f$ sur le cercle de rayon $c$ et de rayon $r$:
$$
I(r) = \frac{1}{2\pi}\int_0^{2\pi} f(z_{\alpha, r}) \, d\alpha
\, \mbox{ où } \, 
z_{\alpha, r} = c + r (\cos \alpha, \sin \alpha).
$$

### Question 1 {.question #fmoy-1}
Que vaut $I(0)$ ?

### Question 2 {.question #fmoy-2}
Montrer que l'application $r \in [0, R] \mapsto I(r)$ est dérivable et
calculer $I'(r)$ pour tout $r \in [0, R]$.

### Question 3 {.question #fmoy-3}
On suppose désormais que $f$ vérifie les conditions de Cauchy-Riemann
en tout point $(x, y)$ de $U$, c'est-à-dire que
    $$
    \partial_y f(x, y) = R(\pi/2) \cdot \partial_x f(x, y)
    $$
    où $R(\alpha)$ désigne la rotation d'angle $\alpha$ centrée sur l'origine.
    Simplifier l'expression de $I'(r)$ et conclure.
    Indication: on pourra évaluer $\partial_{\alpha} (f(z_{\alpha, r}))$.

<!--
Mesurabilité de $\|f\|$
--------------------------------------------------------------------------------

**TODO**
-->

Intégrabilité du produit {.question #ip}
--------------------------------------------------------------------------------

Soient $f:\R \to \R$ et $g:\R \to \R$ deux
fonctions mesurables dont les carrés sont intégrables. 
Montrer que le produit $fg$ est (absolument) intégrable.

Intégrabilité du maximum {.question #im}
--------------------------------------------------------------------------------

Soient $f:\R \to \R$ et $g:\R \to \R$ deux fonctions absolument intégrables. 
Montrer que la fonction $\max(f, g)$ est (absolument) intégrable.

Solutions
================================================================================

Théorème de convergence dominée {.answer #answer-exo-TCD}
--------------------------------------------------------------------------------

Imaginons que les fonctions mesurables $f_k$ convergent vers la fonction
$f$ sur $\R \setminus A$ où $A$ est négligeable, et satisfont 
$g \leq f_k \leq h$ sur l'ensemble $\R \setminus B_k$ où $B_k$ est
négligeable.

Alors l'ensemble $C := A \cup (\cup_{k=1}^{+\infty} B_k)$ est négligeable. 
En effet, $A$ et chaque $B_k$ [est négligeable donc mesurable et de longueur nulle](#négligeable-longueur-nulle) ;
la suite des $C_j := A \cup (\cup_{k=1}^{j} B_k)$ est composée d'ensemble mesurables,
croissante et comme
$$
1_{C_j} = 1_{A \cup (\cup_{k=1}^j B_k)} \leq 1_A + \sum_{k=1}^j 1_{B_k},
$$
on a 
$$
\int 1_{C_j}(x) \,dx \leq \int 1_A(x) \, dx + \sum_{k=1}^j \int 1_{B_k}(x) \,dx = 
\ell(A) + \sum_{k=1}^j \ell(B_k) = 0. 
$$
Par [le théorème de convergence monotone](#TCM), 
$$
\ell(C) = \int 1_{C}(x) \,dx = \lim_{j\to +\infty} \int 1_{C_j}(x) \,dx = 0.
$$
Alternativement, il suffit de recouvrir $A$ puis chaque $B_k$ par des intervalles
sont la somme de longueurs soit inférieure à $\varepsilon/2$, puis $\varepsilon/2^{k+2}$.
La collection de l'intégralité de ces intervalle est dénombrable, recouvre
l'ensemble $C$, et la somme des longueurs des intervalles est inférieure à 
$$
\frac{\varepsilon}{2} + \sum_{k=0}^{+\infty} \frac{\varepsilon}{2^{k+1}} = \varepsilon.
$$
L'ensemble $C$ est donc négligeable.

Sachant que $C$ est négligeable, c'est-à-dire mesurable et de longueur nulle,
il suffit alors de rédéfinir chaque fonction $f_k$, $f$, $g$ et $h$ pour leur
assigner la valeur $0$ en tout $x \in C$ ; cette opération ne change pas leur
caractère mesurable ou intégrable, ni la valeur des intégrales associées.
Et les nouvelles fonctions satisfont partout les hypothèses de convergence
et d'encadrement du [théorème de convergence dominée](#TCD). On peut donc
conclure sous les hypothèse plus faibles considérées dans cet exercice.

Ensembles de longueur finie {.answer #answer-lf}
--------------------------------------------------------------------------------

La suite des fonctions $f_k:\R \to \R$ définie par 
$$
f_k(t) = \left|
\begin{array}{rl}
1_A(t) & \mbox{si } \, t \in [-k, k], \\
0      & \mbox{sinon.}
\end{array}
\right.
$$
est croissante, de limite simple $1_A$. A tout rang $k$, on a 
$$
\int f_k(t) \, dt 
=
\int_{-k}^k 1_A(t) \, dt
\leq L,
$$
donc
$$
\sup_k \int f_k(t) \, dt 
\leq 
L < +\infty. 
$$
Le théorème de convergence monotone nous garantit l'intégrabilité de
$1_A$ -- c'est-à-dire le fait que $A$ est de longueur finie -- et 
fournit
$$
\ell(A) = \int 1_A(t) \, dt = 
\lim_{k\to +\infty} \int f_k(t) \, dt
\leq L.
$$

Intégrabilité locale
--------------------------------------------------------------------------------

### Question 0 {.answer #answer-il-0}
De toute évidence, si $f$ est intégrable sur tout intervalle compact,
elle est intégrable sur tous les intervalles de la forme 
$[x - \varepsilon, x+\varepsilon]$.

Réciproquement, supposons que pour tout $x$ il existe un $\varepsilon > 0$
tel que $f$ soit intégrable sur $[x - \varepsilon, x + \varepsilon]$.
Si la fonction $f$ n'est pas intégrable sur $[a, b]$, par additivité c'est
qu'elle n'est pas intégrable sur $[a, (a+b)/2]$ ou sur $[(a+b)/2, b]$
(voire sur les deux sous-ensembles). En procédant par récurrence, on
construit ainsi une suite d'intervalles fermés emboités $[a_k, b_k]$,
indexés par l'entier $k$, avec $[a_0, b_0] = [a, b]$, 
de longueur $(b-a)/2^k$ où la fonction $f$ n'est pas intégrable.
Par compacité de $[a, b]$, 
il existe un (unique) point $x$ appartenant à tous ces intervalles fermés ;
pour $k$ assez grand, on a $I_k \subset [x -\varepsilon, x+\varepsilon]$.
Par restriction, $f$ devrait donc être intégrable sur $I_k$, d'où une
contradiction ; $f$ est donc intégrable sur $[a, b]$.

### Question 1 {.answer #answer-il-1}
Une fonction $f$ localement intégrable est intégrable sur tout intervalle
de la forme $[-k, k]$ où $k \in \N$ par [le résultat de la question 0](#il-0).
La fonction $f$ étant la limite simple des fonctions $f_k = 1_{[-k, k]} f$, 
elle est mesurable.

### Question 2 {.answer #answer-il-2}
La réciproque est fausse. Par exemple, la fonction $f$ définie par 
$$
f(x) = 
\left|
\begin{array}{cc}
1/x^2 & \mbox{si } x \neq 0, \\
0     & \mbox{si } x = 0
\end{array}
\right.
$$
est mesurable ; c'est par exemple la limite des fonctions intégrables
$$
f_k(x) = 
\left|
\begin{array}{cl}
1/x^2     & \mbox{si } |x| \geq 2^{-k}, \\
0 & \mbox{si } |x| < 2^{-k}, \\
\end{array}
\right.
$$
Mais elle n'est intégrable sur $[-\varepsilon, \varepsilon]$ 
pour aucun $\varepsilon > 0$. 
En effet, si elle l'était, on pourrait appliquer 
[le théorème de convergence dominée](#DCT) aux fonctions
$0 \leq f_k 1_{[-\varepsilon, \varepsilon]} 
\leq f 1_{[-\varepsilon, \varepsilon]}$
et conclure que
$$
\int_{-\varepsilon}^{\varepsilon} f(x) \, dx 
= 
\lim_{k \to +\infty} \int_{-\varepsilon}^{\varepsilon} f_k(x) \, dx
$$
Or, quand $2^{-k} \leq \varepsilon$, on a
$$
\begin{split}
\int_{-\varepsilon}^{\varepsilon} f_k(x) \, dx 
&= \int_{-\varepsilon}^{-2^{-k}} \frac{dx}{x^2} + \int_{2^{-k}}^{\varepsilon} \frac{dx}{x^2} \\
&= \left[ -\frac{1}{x} \right]_{-\varepsilon}^{-2^{-k}} + \left[ -\frac{1}{x}\right]_{2^{-k}}^{\varepsilon} \\
&= (2^k - 1/\varepsilon) + (2^k - 1/\varepsilon) = 2^{k+1} - 2/\varepsilon.
\end{split}
$$
Cette grandeur tendant vers $+\infty$ quand $k \to +\infty$, on aurait une
contradiction. La fonction $f$ n'est donc pas intégrable.

Fonction mesurables
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-fm-1}

Compte tenu du [critère de l'image réciproque](#CIR),
comme tous les ensembles $\left]-\infty, a\right]$ sont fermés, 
le critère de l'énoncé est bien vérifié pour toute fonction mesurable.

Montrons désormais la réciproque. Supposons le critère de l'énoncé vérifié et 
soit $U$ un ouvert de $\R$; l'ensemble $U$ peut être décomposé comme
union d'un nombre dénombrables d'intervalles ouverts bornés $I_k$
de $\R$.
Par conséquent, comme
$$
f^{-1}(U) = f^{-1} \left(\cup_k I_k \right) = \bigcup_{k} f^{-1}(I_k),
$$
il nous suffit de montrer que l'image réciproque de tout intervalle
ouvert borné $\left]a, b\right[$ par $f$ est mesurable, pour conclure
que $f^{-1}(U)$ est mesurable, comme union dénombrable d'ensembles
mesurables.

Or, un point $x$ vérifie $a < f(x) < b$ si et seulement
il ne vérifie pas $f(x) \leq a$ et vérifie $f(x) \leq b - 2^{-k}$ 
pour au moins un entier $k$, ce qui se traduit par la relation ensembliste
$$
f^{-1}(\left]a, b\right[) 
= 
\left(\R \setminus
f^{-1}(\left]-\infty,a \right]) \right) 
\cap 
\left( \bigcup_{k=0}^{+\infty} f^{-1}(\left]-\infty, b -2^{-k}\right])\right).
$$
Les images réciproques au second membre sont mesurables par hypothèse,
et sont combinées par complément, union dénombrable et intersection,
par conséquent $f^{-1}(\left]a, b\right[)$ est également mesurable.
Le [critère de l'image réciproque](#CIR)
pour la mesurabilité de $f$ est donc bien vérifié.

### Question 2 {.answer #answer-fm-2}
Si la fonction $f: \R \to \R$ est croissante, les images réciproques
des ensembles de la forme $\left]-\infty,a \right]$ sont des intervalles.
En effet, si $f(x) \leq a$ et $f(y) \leq a$, pour tout point intermédiaire
$x \leq z \leq y$, $f(z) \leq a$. Par conséquent, $f$ est mesurable.

De plus, $f$ étant croissante, pour tout intervalle compact $[a, b]$ et tout
$x \in [a, b]$, on a $f(a) \leq f(x) \leq f(b)$.
Par le [critère d'intégrabilité dominée](#CID), $f$ est intégrable sur
$[a, b]$.


Composition de fonctions et mesurabilité {.answer #answer-cfm}
--------------------------------------------------------------------------------

Soient $a_0 \leq a_1 \leq \dots \leq a_k$ des nombres réels 
tels que la fonction $g$ soit continue sur
chaque intervalle ouvert $\left]a_j, a_{j+1} \right[$. Soit $U$ un ouvert
de $\R$ ; alors pour tout $j \in \{0,\dots,k-1\}$ si $g_j$ désigné la
restriction de $g$ à $\left]a_j, a_{j+1} \right[$, par continuité de $g_j$, 
l'image réciproque $V_j = g_j^{-1}(U)$ est ouverte dans $\left]a_j, a_{j+1} \right[$
et donc dans $\R$. L'image réciproque de $U$ par $g$ est donc la réunion $V$
de ces ouverts, c'est-à-dire un ouvert, 
et éventuellement d'un sous-ensemble $F$ (nécessairement fini, donc fermé) 
de $\{a_0, \dots, a_k\}$.

L'image réciproque de $U$ par $g\circ f$ est donc l'image réciproque de 
$V \cap F$ par $f$. La fonction $f$ étant mesurables, $f^{-1}(V)$ et
$f^{-1}(F)$ sont mesurables, 
ainsi que $f^{-1}(V \cap F) = f^{-1}(V) \cap f^{-1}(F)$.
La fonction composée $g \circ f$ est donc mesurable.


Composition par une fonction lipschitzienne 
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-cfl-1}
Oui, car toute fonction lipschitzienne est continue ; 
$g \circ f$ est donc mesurable 
comme [composée d'une fonction mesurable et d'une fonction continue](#CFC).

### Question 2 {.answer #answer-cfl-2}
Pas nécessairement; si $f$ est une fonction conditionnellement
intégrable sur $[0,1]$, la fonction $|f|$ n'est pas intégrable ; 
or, l'application $t \mapsto |t|$ est lipschitzienne (avec $K=1$).

### Question 3 {.answer #answer-cfl-3}
Oui. D'une part, $f$ étant absolument intégrable, elle est mesurable et
donc par la question 1., la composée $g \circ f$ est mesurable.
D'autre part, pour tout $x \in [0,1]$, on a
$$
|g \circ f(x) - g \circ f(0)| \leq K |f(x) - f(0)|
$$
et donc
$$
|g \circ f(x)| \leq K |f(x)| + (K |f(0)| + |g \circ f(0)|)
$$
Le membre de droite de cette inégalité est une fonction (absolument)
intégrable sur $[0, 1]$, donc par le critère d'intégrabilité dominée,
la fonction $g \circ f$ est (absolument) intégrable.

Caractérisation des ensembles mesurables {.answer #answer-cer}
--------------------------------------------------------------------------------

Si l'ensemble $E$ est mesurable, pour tout $k\in \N$, l'ensemble 
$E_k := E \cap [-k,k]$
est intégrable, c'est-à-dire que la fonction $1_{E_k}$ est intégrable.
La fonction $1_{E}$ est donc mesurable car limite simple de fonctions intégrables.

Réciproquement, si une fonction caratéristique $1_E$ est mesurable, 
par [le critère de l'image réciproque](#CIR), comme
$E = 1_{E}^{-1}(\{1\})$ et que le singleton $\{1\}$ est fermé,
$E$ est mesurable.

Alternativement, si $1_E$ est une limite simple de fonctions intégrables
$f_k$ et $\sigma:\R \to \R$ est la fonction définie par
$$
\sigma(x) = \left|
\begin{array}{cl}
0 & \mbox{si } x \leq 1/2, \\
1 & \mbox{si } x > 1/2, 
\end{array}
\right.
$$
alors les fonctions $g_k = \sigma \circ f_k$ sont à valeurs dans $\{0,1\}$, 
convergent simplement vers $1_E$ et de plus sont mesurables: en effet si $F$
est un fermé de $\R$, $\sigma^{-1}(F)$ est un ouvert ou un 
fermé de $\R$ (4 possibilités uniquement, que l'on peut énumérer, selon
que $F$ contienne ou non $0$ et $1$), et donc $g_k^{-1} (F) = f_k^{-1} (\sigma^{-1}(F))$
est un ensemble mesurable.   
Par conséquent, pour tout intervalle compact $[a, b]$ de $\R$, 
$1_{E \cap [a, b]}$ est la limite simple des fonctions mesurables 
$g_k 1_{[a, b]}$, qui sont dominées par $1_{[a, b]}$ et donc intégrable.
L'ensemble $E$ est donc mesurable.

Formule de la moyenne
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-fmoy-1}
On a 
$$
I(0) = \frac{1}{2\pi}\int_0^{2\pi} f(c_1, c_2) \, d\alpha = f(c_1, c_2) = f(c).
$$

### Question 2 {.answer #answer-fmoy-2}
Formons le taux d'accroissement de $I$ en $r$, pour une variation de
l'argument $h$ telle que $r + h \in [0, R]$. On a
$$
\begin{split}
\frac{I(r+h) - I(r)}{h}
&=
\frac{1}{2\pi h}
\left(
\int_0^{2\pi} f(c_1 + (r+h) \cos \alpha, c_2 + (r+h) \sin \alpha) \, d\alpha\right. \\
&\phantom{=} \left. - \int_0^{2\pi} f(c_1 + r \cos \alpha, c_2 + r \sin \alpha) \, d\alpha \right) \\
&= \frac{1}{2\pi}\int_0^{2\pi} 
\frac{f(z_{r+h, \alpha}) - f(z_{\alpha, r})}{h} \, d\alpha.
\end{split}
$$
La fonction $g_{\alpha}: r \mapsto f(z_{\alpha, r})$ étant différentiable 
pour tout $\alpha$, on a 
$$
\begin{split}
\lim_{h \to 0} \frac{f(z_{r+h, \alpha}) - f(z_{\alpha, r})}{h}
&= \frac{d}{dr} f(z_{\alpha, r}) \\ 
&= df(z_{r, \alpha}) \cdot (\cos \alpha, \sin \alpha) \\
&= \partial_x f (z_{r, \alpha}) \cos \alpha 
+ \partial_y f (z_{r, \alpha}) \sin \alpha.
\end{split}.
$$
De plus, par le théorème des accroissements finis,
$$
\left\| \frac{g_{\alpha}(r+h) - g_{\alpha}(r)}{h} \right\|
\leq
\sup_{r \in [0, R]} \left\| \frac{d}{dr} g_{\alpha}(r) \right\|
$$
où le sup du membre de droite est bien fini puisque 
$dg_{\alpha}(r)/dr$
est une fonction continue du couple $(\alpha, r)$ qui appartient 
à l'ensemble compact $[0, 2\pi] \times [0, R]$.
Par conséquent, 
pour toute suite $h_k$ tendant vers $0$ et 
telle que $r+h_k \in [0, R]$, la suite des
$$
\frac{g_{\alpha}(r+h_k) - g_{\alpha}(r)}{h_k}
$$
associée converge simplement vers 
$$
\partial_x f (z_{r, \alpha}) \cos \alpha 
+ \partial_y f (z_{r, \alpha}) \sin \alpha
$$
et chacune des composantes de ce vecteur de $\R^2$ 
est bornée par la fonction absolument intégrable (constante)
$$
\alpha \in [0, 2\pi] \mapsto \sup_{r \in [0, R]} \left\| \frac{d}{dr} g_{\alpha}(r) \right\|.
$$
Par conséquent, par le théorème de convergence dominée,
la dérivée de $I$ est définie en tout point $r$ et est donnée par
$$
I'(r)
= \frac{1}{2\pi}\int_{0}^{2\pi} 
  \left(
  \partial_x f (z_{r, \alpha}) \cos \alpha 
  + \partial_y f (z_{r, \alpha}) \sin \alpha
  \right) \, d\alpha.
$$

### Question 3 {.answer #answer-fmoy-3}
Evaluons la dérivée par rapport à $\alpha$ de $f(z_{\alpha, r})$. On a
$$
\begin{split}
\partial_{\alpha} (f(z_{\alpha, r}))
&=
\partial_{\alpha} (f(c_1 + r \cos \alpha, c_2 + r \sin \alpha)) \\
&= \partial_x f(z_{\alpha, r}) (- r\sin \alpha)
+ \partial_y f(z_{\alpha, r}) (r\cos \alpha).
\end{split}
$$
Comme $\partial_y f(z_{\alpha, r}) = R(\pi/2) \partial_x f(z_{\alpha, r})$,
on en déduit que
$$
\begin{split}
\partial_{\alpha} (f(z_{\alpha, r}))
&= r(- \sin \alpha \times I + \cos \alpha  \times R(\pi/2)) \cdot \partial_x f(z_{\alpha, r}) \\
& = r R(\pi/2 + \alpha) \cdot \partial_x f(z_{\alpha, r}) \\
& = r R(\pi/2) R(\alpha) \cdot \partial_x f(z_{\alpha, r})
\end{split}
$$
D'un autre coté, l'intégrande dans l'expression de $I'(r)$
s'écrit
$$
\begin{split}
\partial_x f (z_{r, \alpha}) \cos \alpha 
+ 
\partial_y f (z_{r, \alpha}) \sin \alpha
&= 
(\cos \alpha \times I + \sin \alpha \times R(\pi/2)) \cdot \partial_x f(z_{r, \alpha}) \\
&=
R(\alpha) \cdot \partial_x f(z_{r, \alpha}).
\end{split}
$$
Par conséquent lorsque $r$ est non nul
$$
\partial_x f (z_{r, \alpha}) \cos \alpha 
+ 
\partial_y f (z_{r, \alpha}) \sin \alpha
= \frac{1}{r} R(-\pi/2) \cdot \partial_{\alpha} (f(z_{\alpha, r}))
$$
et donc
$$
\begin{split}
I'(r)
&= \frac{1}{2\pi}\int_{0}^{2\pi} 
  \left(
  \partial_x f (z_{r, \alpha}) \cos \alpha 
  + \partial_y f (z_{r, \alpha}) \sin \alpha
  \right) \, d\alpha \\
  &= \frac{1}{2\pi r} 
  \left(
  \int_0^{2\pi}
  R(-\pi/2) \cdot
  \partial_{\alpha} (f(z_{\alpha, r}))
  \, d\alpha \right) \\
&= \frac{1}{2\pi r} 
    R(-\pi/2) \cdot
  \left(
  \int_0^{2\pi} \partial_{\alpha} (f(z_{\alpha, r}))
  \, d\alpha \right)  \\
& = \frac{1}{2\pi r} 
    R(-\pi/2) \cdot 
    \left[f(z_{\alpha, r})\right]_0^{2\pi} \\
& = 0
  \end{split}.
$$
Par ailleurs, un calcul direct montre que $I'(0) = 0$.
La dérivée de $I$ est donc identiquement nulle ; on en conclut
que pour tout $r$,
$$
I(r) = \frac{1}{2\pi}\int_0^{2\pi} f(z_{\alpha, r}) \, d\alpha
= I(0) = f(c).
$$

Intégrabilité du produit {.answer #answer-ip}
--------------------------------------------------------------------------------

Les produits $fg$ est mesurable comme [produit de fonctions mesurables](#prod) ;
[la fonction $|fg|$ est donc également mesurable](#abs).
De plus, pour tout $x \in \R$, comme $(|f(x)| + |g(x)|)^2 \geq 0,$
$$
0 \leq |fg|(x) \leq \frac{1}{2} f(x)^2 + \frac{1}{2} g(x)^2.
$$
et donc
$$
- \frac{1}{2} f(x)^2 - \frac{1}{2} g(x)^2
\leq fg(x)
\leq \frac{1}{2} f(x)^2 + \frac{1}{2} g(x)^2.
$$
Par le [critère d'intégrabilité dominée](#CID), 
$fg$ et $|fg|$ sont donc intégrables.

Intégrabilité du maximum {.answer #answer-im}
--------------------------------------------------------------------------------

Les fonctions $f$ et $g$ étant absolument intégrables, elles sont mesurables.
Par [composition avec une fonctions continue](#CFC), 
$\max(f, g)$ est également mesurable.

De plus, on a $-|f|-|g| \leq |\max(f, g)| \leq |f| + |g|$. 
Les fonctions $\max(f, g)$ et sa valeur absolue sont donc encadrées
par deux fonctions intégrables ; $\max(f, g)$ est donc absolument intégrable.

Références
================================================================================
