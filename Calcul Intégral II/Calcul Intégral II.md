% Calcul Intégral II

<!-- LaTeX Macros -->
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}

\newcommand{\zero}{$\mathord{\boldsymbol{\circ}}$}
\newcommand{\one}{$\mathord{\bullet}$}
\newcommand{\two}{$\mathord{\bullet}\mathord{\bullet}$}
\newcommand{\three}{$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$}
\newcommand{\four}{$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$}



<!--{\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}}-->


Introduction
================================================================================

L'intégrale de Lebesgue, introduite dans "Calcul Intégral I", 
présente l'avantage de pouvoir intégrer une plus grande gamme de fonctions
que l'intégrale de Riemann : moins régulières, non bornées et/ou définies
sur des intervalles non-bornés[^ii].

Il faut néanmoins reconnaître qu'à ce stade de notre exposé l'intégrale
de Riemann est parfois plus pratique. 
Par exemple : si avec l'intégrale de Lebesgue,
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
Lebesgue, mais plutôt une conséquence de sa généralité : en permettant
d'intégrer des fonctions telles que $x \in [0, 1] \mapsto 1/\sqrt{x}$ 
(presque partout), on s'expose à devoir refuser d'intégrer le produit d'une 
fonction par elle-même, ici $x \in [0,1] \mapsto 1/x$ (presque partout).
Il est donc normal de devoir imposer des conditions supplémentaires
pour garantir l'intégrabilité d'un produit.


Heureusement, comme dans le cas de l'intégrale de Riemann, 
un critère d'intégrabilité des fonctions -- nécessaire et suffisant -- 
existe pour établir ce type de résultat (et bien d'autres).
Comme dans le cas de l'intégrale de Riemann, il se décompose en deux tests
indépendants : pour être intégrable une fonction doit être "dominée par une
fonction intégrable" et "suffisamment régulière". Bien sûr ici la
fonction qui domine devra être intégrable au sens de Lebesgue 
(et non plus de Riemann) ; 
quant à la régularité, il ne s'agira plus de tester la continuité presque
partout, mais de vérifier la *mesurabilité* de la fonction considérée,
une propriété que possèdent presque toutes les fonctions "non-pathologiques".

Dans ce chapitre pour des raisons de simplicité, 
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

Mais notre première étape dans ce chapitre sera de nous doter de
théorèmes de convergence qui nous permettront -- sous certaines
conditions qui sont plus simples que dans le cadre Riemannien
-- de calculer l'intégrale d'une fonction $f$ comme la limite
d'intégrales de fonctions convergeant vers $f$.

Objectifs d'apprentissage
================================================================================

#### Ensembles mesurables

  - \one savoir qu'un ensemble est mesurable si sa longueur est bien définie,

  - \one connaître la définition formelle d'ensemble mesurable,

  - \one savoir calculer sa longueur comme une intégrale,

  - connaître les propriétés principales des ensembles mesurables :

    - \one les ensembles mesurables forment une tribu,

    - \two ensembles ouverts (et fermés) sont mesurables,

    - \two négligeable = de longueur nulle.

  - connaître quelques propriétés secondaires qui s'en déduisent :

    - \one intersection dénombrable d'ensembles mesurables.

    - \one complémentaire relatif d'ensembles mesurables,

  - savoir les exploiter pour :
  
    - \two montrer qu'un ensemble donné est mesurable,

    - \three déduire de nouvelles propriétés secondaires.

#### Fonctions mesurables

  - \one connaître la définition des fonctions mesurables,

  - \one connaître leur caractérisation par le critère de l'image réciproque,

  - savoir que les fonctions suivantes sont mesurables :
    
    - \one les fonctions intégrables,

    - \one les fonctions caractéristiques d'ensembles mesurables,

    - \one les fonctions égales presque partout à des fonctions mesurables,

    - \two les limites (simples) de fonctions mesurables,

    - \two les compositions de fonctions mesurables et continues.

  - savoir exploiter les éléments précédents pour :
  
    - \two montrer qu'une fonction donnée est mesurable,
      
    - \three déduire de nouvelles classes de fonctions mesurables.


#### Fonctions intégrables

  - \one connaître le critère d'intégrabilité dominée,

  - \one connaître le théorème de convergence dominée,

  - \two connaître le théorème de convergence monotone,

  - savoir mettre en oeuvre ces théorèmes pour :

    - \one montrer qu'une fonction est intégrable,

    - \two calculer l'intégrale d'une fonction comme une limite,

    - \three démontrer qu'une fonction n'est pas intégrable.

  - \one connaître la définition d'intégrale sur un sous-ensemble (mesurable).
  

Théorèmes de convergence
================================================================================

### Théorème de convergence dominée {#TCD .theorem}
Si une suite de fonctions intégrables $f_k:\R \to \R$
converge simplement vers la fonction $f$, c'est-à-dire si pour tout
$x \in \R$,
$$
\lim_{k \to +\infty} f_k(x) = f(x)
$$
et qu'il existe une fonction intégrable $g:\R \to \left[0, +\infty\right[$ 
dominant la suite $f_k$, c'est-à-dire telle que pour tout $k \in \N$ 
et pour tout 
$x \in \R$,
$$
|f_k(x)| \leq g(x)
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

### Défaut de domination {.exercise .question .one #dd}
Comparer
$$
\lim_{k \to +\infty} \int f_k(t) \, dt
\; \mbox{ et } \; 
\int \lim_{k \to +\infty} f_k(t) \, dt\;
$$
pour la suite de fonctions $f_k:\R \to \R$ définie par
$$
f_k(t) = \left|
\begin{array}{rl}
1 & \mbox{si $k\leq t \leq k+1$} \\
0 & \mbox{sinon.}
\end{array}
\right.
$$
Expliquer le résultat.

### Intégrale fonction d'un paramètre {.exercise .question .two #ifp}
Montrer que 
$$
\lim_{x \to 0^+} \int_0^1 \frac{e^{-xt}}{1+t^2} \, dt = \frac{\pi}{4}.
$$

### Théorème fondamental du calcul {.exercise .three #exo-TCD .question}
Déduire de la forme classique du théorème fondamental du calcul 
et du [théorème de convergence dominée](#TCD) 
que si $f: [a, b] \subset [-\infty, +\infty] \to \R$ est continue sur $[a, b]$,
dérivable sur $[a, b]$ et de dérivée $f'$ intégrable, alors
$$
f(b) - f(a) = \int_a^b f'(t) \, dt.
$$
(Indication : considérer une suite d'intervalles fermés bornés $[a_k, b_k]$ de $\R$ tels
que $[a_k, b_k] \subset [a, b]$ et tels que $a_k \to a$ et $b_k \to b$ quand
$k \to +\infty.$)
<!-- (Indication: on pourra étudier la suite des $g_k := f'1_{[-k, k]}$.)-->



### Dérivation sous le signe somme {.theorem #DSS}
Soit $I$ un intervalle de $\R$ et $f: I \times \R \to \R$ une fonction
telle que :

 1. pour tout $\lambda \in I$, 
    la fonction $t \in \R \mapsto f(\lambda, t)$ est intégrable,

 2. pour tout $t \in \R$, la fonction
    $\lambda \in I \mapsto f(\lambda, t)$
    est dérivable et 
    $$\sup_{\lambda \in I} |\partial_{\lambda} f(\lambda, t)| \leq g(t)$$
    où $g: \R \to \left[0, +\infty\right[$ est une fonction intégrable.

Alors, la fonction $S: I \to \R$ définie par
$$
S(\lambda) := \int f(\lambda, t) \, dt
$$
est dérivable ; pour tout $\lambda \in I$,
la fonction $t \in \R \mapsto \partial_{\lambda} f(\lambda, t)$ est intégrable 
et
$$
S'(\lambda) = \int \partial_{\lambda} f(\lambda, t) \, dt.
$$



### Démonstration {.proof}
Par linéarité de l'intégrale, 
pour tout $\lambda \in I$ et tout $h \in \R^*$ tel que $\lambda + h \in I$, 
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
\leq \sup_{\mu \in I} |\partial_{\lambda} f(\mu, t)| \leq g(t).
$$
Les taux d'accroissements de $f$ sont donc bornés par une fonction intégrable.
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
\mbox{pour tout } \, k \in \N, \, f_k(x) \leq f_{k+1}(x) 
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

### Fonctions puissance  {.one .exercise #power .question}
Montrer que la fonction puissance $t \in \left[1, +\infty\right[ \mapsto t^{\alpha}$
est intégrable si et seulement $\alpha < -1$ et que la fonction puissance
$t \in \left]0,1\right] \mapsto t^{\alpha}$ est intégrable si et seulement
si $\alpha > -1$.

### Intégrabilité et intégrales impropres {.two .question .exercise #iii}
Montrer qu'une fonction $f: \R \to \R$ qui est intégrable sur tout intervalle 
fermé borné de $\R$ est intégrable sur $\R$ si et seulement si
$$
\lim_{k \to +\infty} \int_{-k}^k |f(t)| \, dt < +\infty.
$$

<!--
### Fonctions d'ordre exponentielle {.one .exercise #exp}
Montrer que si $f: \left[0, +\infty\right[ \to \R$ satisfait $|f(t)| \leq M e^{at}$
pour des constantes $M$ et $a$ réelles, alors
$$
\int_0^{+\infty} f(t) e^{-xt} \, dt
$$
est définie pour tout $x > a$.
-->

Ensembles mesurables
================================================================================

Il existe un lien étroit entre la notion de longueur d'un ensemble de réels
et le calcul intégral. Nous savons par exemple que pour tout intervalle 
fermé borné $E = [a, b]$, la longueur $b-a$ de l'intervalle peut être calculée
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
Cette définition laisse toutefois de côté les ensembles "trop grands" 
pour être intégrables, mais par ailleurs parfaitement anodins, 
comme $\R$ tout entier ou l'ensemble des réels positifs. 
Nous préférons donc mettre l'accent sur la notion d'ensemble *mesurable* :

[^loop]: Il existe des ensembles dont on ne peut pas définir raisonnablement
la longueur, sauf à accepter un concept de longueur aux propriétés
très étranges. Cette situation ne résulte pas de la méthode de définition
de la longueur par l'intégrale ; c'est au contraire une limitation intrinsèque
de la théorie de la mesure que nous étudierons plus en détail par la suite.
Malheureusement pour la didactique, il n'existe aucun exemple explicite 
(élaboré par un procédé constructif) d'ensemble qui ne soit pas mesurable.
On peut se consoler en apprenant que, du point de vue logique, 
si l'on suppose que tous les ensembles sont
mesurables -- ce qui peut sembler relativement anodin -- 
on peut alors prouver des propositions beaucoup plus perturbantes,
comme l'existence de partitions de $\R$ "contenant strictement plus d'éléments" 
que $\R$ lui-même. 

### Ensemble mesurable {.definition}
Un ensemble $E$ de $\R$ est *de longueur finie* si sa fonction 
caractéristique $1_E$ est intégrable sur $\R$ ; 
il est *mesurable* si sa fonction caractéristique est intégrable 
sur tout intervalle fermé borné $[a, b]$ de $\R$.
La (mesure de) *longueur* d'un ensemble $E$ mesurable est définie par
$$
\ell(E) := \int 1_E(t) \, dt
$$
si $E$ est de longueur finie et
$$
\ell(E) := +\infty
$$
dans le cas contraire (si $E$ est mesurable mais pas de longueur finie).

### Interprétation {.remark}
Il faut comprendre le terme "mesurable" littéralement, 
comme signifiant "dont on peut définir la mesure (de longueur)", 
qui est un nombre fini ou infini. 
Cette interprétation  est cohérente, puisque tous les ensembles 
$E$ de longueur finie 
sont bien mesurables ;
en effet si la fonction caractéristique $1_E$ est intégrable,
sa restriction à tout intervalle fermé borné $[a, b]$ également.

### Ensemble de longueur finie I {.exercise .question .one #elfI}
Montrer que l'ensemble $E = \left[-1, 0\right[ \cup \left]0, 1\right]$ est
de longueur finie et calculer sa longueur.

### Ensemble de longueur finie II {.exercise .question .one #elfII}
Montrer que l'ensemble $\Q$ est de longueur finie et calculer sa longueur.

### Ensemble de longueur finie III {.exercise .question .two #elfIII}
Montrer que l'ensemble 
$E = \cup_{k=0}^{+\infty} \left[k, k+2^{-k}\right[$ 
est de longueur finie et calculer sa longueur.

### La longueur est additive {.exercise .question .three #la}
Montrer que la longueur $\ell$ est additive : si $A$ et $B$ sont deux
ensembles mesurables de $\R$ disjoints, alors $A\cup B$ est mesurable
et $\ell(A \cup B) = \ell(A) + \ell(B)$.



### Propriétés élémentaires (tribu) {.theorem #pptés-tribu}

 1. L'ensemble vide est mesurable.

 2. Le complémentaire d'un ensemble mesurable est mesurable.

 3. L'union d'une collection dénombrable d'ensembles mesurables
    est mesurable.

### {.remark}
(On rappelle qu'un ensemble est *dénombrable* s'il est fini 
ou en bijection avec $\N$.)

### {.remark}
On agrège cet ensemble de propriétés en disant que les ensembles mesurables 
de $\R$ forment une *tribu* -- ou *$\sigma$-algèbre* -- de $\R$.


### Démonstration {.proof}
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
    Or, pour tout intervalle fermé borné $[a, b]$, on a 
    $$
    (A \cup B) \cap [a, b]
    = (A \cap [a, b]) \cup (B \cap [a, b]),
    $$
    ce qui se traduit au moyen des fonctions caractéristiques par la relation
    \begin{align*}
    1_{(A \cup B) \cap [a, b]}  &= \max \left(1_{A \cap [a, b]}, 1_{B \cap [a, b]} \right) \\
    &= 1_{A \cap [a, b]} + (1_{B \cap [a, b]} - 1_{A \cap [a, b]})_+
    \end{align*}
    où $x_+ := \max(x, 0)$. Comme $1_{B \cap [a, b]} - 1_{A \cap [a, b]}$
    est intégrable et sa partie positive majorée par $2 \times 1_{[a, b]}$ qui est également
    intégrable, sa partie positive est intégrable (cf. annexe "Calcul Intégral I").
    La fonction caractéristique de $(A \cup B) \cap [a, b]$ est donc intégrable.
 
    Considérons désormais une suite d'ensembles mesurables
    $A_k$, pour $k \in \N$. 
    Quitte à remplacer $A_k$ par $\cup_{j=0}^k A_j$
    --
    ce qui ne change pas le caractère mesurable des $A_k$ ou leur union 
    jusqu'à l'ordre $k$
    --
    on peut supposer que $A_k \subset A_{k+1}$.
    Pour tout intervalle fermé borné $[a, b]$, 
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

### Suite d'ensembles {.exercise .question .two #sde}
Soit $A_k$, $k \in \N$, une suite d'ensembles mesurables de $\R$,
$$
B = \{x \in \R \;| \; \exists \, k_0 \in \N, \, \forall \, k \geq k_0, \, x \in A_k\}
$$
et
$$
C = \{x \in \R \; | \; \forall \, k_0 \in \N, \, \exists \, k \geq k_0, \, x \in A_k\}.
$$
Montrer que les ensembles $B$ et $C$ sont mesurables.



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
son intersection avec un intervalle fermé borné $[a, b]$ 
est un intervalle inclus dans $[a, b]$.
La fonction caractéristique associée est de la forme $1_{[c, d]}$,
ou en diffère au plus en deux points ; 
dans tous les cas, elle est intégrable.

Si maintenant $U$ est un ensemble ouvert, pour chaque point $x$ de $U$ 
on peut construire le plus grand intervalle ouvert $I_x$ contenant $x$ et inclus
dans $U$ (c'est l'union de tous les intervalles ouverts vérifiant ces
deux propriétés). Pour un couple $x$ et $y$ dans $U$, soit $I_x = I_y$,
soit $I_x$ et $I_y$ sont disjoints et l'union de tous les intervalles
$I_x$ est égale à $U$. Comme dans chaque $I_x$ on peut choisir
un nombre rationnel $y$ tel que $I_x = I_y$, la collection de $I_x$
est dénombrable.
L'ouvert $U$ est donc une union dénombrable d'intervalles ouverts[^pf], 
qui sont tous mesurables, il est donc mesurable.

[^pf]: le résultat correspondant est faux pour les intervalles fermés.

### Ni ouvert ni fermé {.exercise .question .one #nonf}
Exhiber un ensemble mesurable $E$ de $\R$ qui ne soit ni ouvert ni fermé.

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

Supposons temporairement que $A$ soit inclus dans un intervalle fermé borné 
$[a, b]$ de $\R$. 
La fonction caractéristique $1_A$ de $A$ est intégrable, 
donc pour tout $\varepsilon > 0$ il existe une jauge $\gamma$ sur
$[a, b]$ telle que, si la subdivision pointée (totale ou partielle)
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
où les $I_i$ sont des intervalles fermés bornés de $[a, b]$ sans chevauchement, 
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
les $I_i$ sont des intervalles fermés bornés de $[a, b]$ sans chevauchement 
tels que pour tout $t_i$, $I_i \subset \gamma(t_i)$. 
De plus, les $I_i$ recouvrent $A$ : en effet si l'on considère $t \in A$,
il existe nécessairement un entier $k$ tel que tout intervalle fermé borné
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

### Complétude de la longueur {.corollary #complétude}

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
Une fonction $f:\R \to \R^m$ est mesurable 
si chacune de ses composantes est mesurable.

### Mesurabilité sur un intervalle {.remark}
Nous nous limitons dans ce chapitre à l'étude des fonctions mesurables
définies sur $\R$. La notion peut être très facilement étendue
à une fonction $f$ définie sur un intervalle $I$ de $\R$ de la
façon suivante : on dira que $f$ est mesurable si son prolongement par $0$
dans le complémentaire de $I$ est mesurable. Nous vous laissons le soin
de généraliser en conséquence les énoncés qui vont suivre.

### Critère d'intégrabilité dominée {.theorem #CID}
Une fonction $f: \R \to \R$ est intégrable si et seulement
si $f$ est mesurable et il existe une fonction intégrable
$g: \R \to \left[0,+\infty\right[$ telle que $|f| \leq g$.

### {.post}
La démonstration de ce théorème, qui nécessite des résultats intermédiaires, 
est donnée [à la fin de cette section](#proof-CID).

### Interprétation {.post .remark}
Souvenons-nous qu'une fonction définie sur un intervalle fermé et borné 
est intégrable au sens de Riemann si et seulement si elle est encadrée 
par deux fonctions intégrables au sens de Riemann et continue presque partout.

Dans le cas de l'intégrale de Riemann comme de Lebesgue, 
l'intégrabilité est donc caractérisée par une structure analogue qui
repose sur deux propriétés distinctes :
être encadrée par deux fonctions intégrables (pour la notion d'intégrale
considérée) et être "suffisamment régulière". 
La différence est que dans le cas de l'intégrale de Riemann
l'exigence de régularité est forte -- être continue presque partout --
alors que dans le cas de l'intégrale de Lebesgue, 
la régularité demandée -- la mesurabilité -- s'avère être une 
condition très peu contraignante[^note].

[^note]: À tel point que, si l'on peut prouver l'existence d'une fonction
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

### Les fonctions continues presque partout sont mesurables {.proposition}

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
et donc de Lebesgue -- sur $[-k, k]$. Son extension
$f_k$ par zéro au reste de $\R$ est donc intégrable au sens de
Lebesgue. De plus, la suite des $f_k$ converge simplement vers $f$ ;
la fonction $f$ est donc mesurable. 

### Critère de l'image réciproque {.theorem #CIR}
Une fonction $f:\R \to \R^m$ est mesurable si et seulement
l'image réciproque de tout fermé (ou de tout ouvert) de $\R^m$
par $f$ est mesurable.

### Fonctions continues {.exercise .question .one #fcm}
Montrer en utilisant le critère de l'image réciproque que toute fonction
continue est mesurable.

### Image réciproque d'un intervalle {.exercise .question .one #iri}
Montrer que si $f: \R \to \R$ est mesurable, alors l'image réciproque d'un
intervalle arbitraire par $f$ est mesurable.


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
où $E$ et $F$ sont négligeables et donc mesurables puisque 
[la mesure de Lebesgue est complète](#complétude) ;
par conséquent, $f^{-1}(U)$ est mesurable.

### Démonstration du [critère de l'image réciproque](#CIR) {.proof #pCIR}
Il suffit de démontrer le critère pour les ensembles ouverts : 
si une fonction satisfait le critère de d'image réciproque pour
tout ouvert de $\R^m$, alors si $F$ est un fermé de $\R^m$, 
en utilisant l'égalité $f^{-1}(F) = \R \setminus f^{-1}(\R^m \setminus F)$,
le fait que le complémentaire d'un fermé soit un ouvert et 
que [le complémentaire d'un ensemble mesurable soit mesurable](#pptés-tribu),
on établit le critère pour les fermés.

Montrons tout d'abord le résultat pour les fonctions scalaires ($m=1$).
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
ce qui prouvera que chaque $f_k$ est intégrable comme combinaison linéaire
de fonctions intégrables.
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
Par le théorème de dérivation des intégrales indéterminées,
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
étant [stable par passage à la limite](#SPL), 
[une fonction égale à $f$ presque partout satisfait le critère de l'image réciproque](#FPPE) ;
la fonction intégrable $f$ satisfait donc 
elle-même le critère de l'image réciproque.

Finalement, une fonction mesurable est une limite simple
d'une suite de fonctions intégrables et les fonctions intégrables 
vérifient le critère de l'image réciproque, 
par une nouvelle application du résultat de 
[stabilité par passage à la limite](#SPL), 
ce critère est également satisfait pour toute fonction mesurable.

Pour établir le résultat dans le cas où $n>1$, il suffit de montrer qu'une
fonction $f:\R \to \R^m$ satisfait le critère de l'image réciproque si et
seulement si toutes ses composantes le satisfont. Pour le sens direct,
il suffit de constater que 
$$
f_k^{-1}(U) = f^{-1}(\R \times \cdots \times U \times \cdots \R)
$$
et que si $U$ est ouvert, $\R \times \cdots \times U \times \cdots \R$ également.
Pour la réciproque, nous exploitons le fait[^demo] que tout ouvert de $\R^m$ peut être
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

[^demo]: Pour chaque point $x$ de 
$U \subset \R^m$ ouvert dont les coordonnées sont rationnelles, 
on considère le plus grand pavé ouvert de la forme 
$$\left]x_1-h, x_1+h\right[ \times \dots \times \left]x_m-h, x_m+h\right[,
\; h > 0$$ 
qui soit inclus dans $U$ ; 
ces pavés forment une collection dénombrable et leur union 
est égale à $U$ par construction.


### Démonstration du critère d'intégrabilité dominée {.proof #proof-CID}
Le sens direct est évident :
si la fonction $f$ est intégrable, elle est mesurable et est dominée
par la fonction $|f|$ qui est intégrable.

Pour montrer la réciproque dans ce cas, nous approchons 
la fonction mesurable $f$ par la suite de fonctions étagées $f_k$ 
introduites dans [la démonstration du critère de l'image réciproque](#pCIR). 
La fonction $f$ apparaît comme une limite simple des
fonctions $f_k$, qui sont intégrables et dominées par la fonction intégrable $g$. 
Par [le théorème de convergence dominée](#TCD), $f$ est intégrable.

### Composition par une fonction continue {.theorem #CFC}

Soit $f:\R \to \R^m$ une fonction mesurable et 
$g:\R^m \to \R^p$ une fonction continue.
La composée $g \circ f$ de ces deux fonctions est mesurable.

### {.remark .post}
Dans le cas d'une fonction $g: \R \to \R$, il suffit de supposer que
$g$ soit continue par morceaux pour pouvoir conclure (cf. exercice
["Composition de fonctions et mesurabilité"](#cfm)).
(En général, les fonctions $g$ qui assurent que 
$g \circ f$ soit mesurable pour toutes les fonctions mesurables
$f$ sont appelées fonctions *boréliennes*.).

### Démonstration {.proof}
Si $F$ est un fermé de $\R^p$,
par continuité de $g$, l'ensemble $g^{-1}(F)$ est un fermé de $\R^m$ 
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
Par continuité de l'application produit $\times: \R \times \R \to \R$.

### Mesurabilité de la valeur absolue {.corollary #abs}
La valeur absolue d'une fonction scalaire mesurable est mesurable.

### Démonstration {.proof}
Par continuité de l'application valeur absolue $|\, \cdot \,|: \R \to \R$.

### Intégrabilité du produit {.exercise .question .one #ip}
Soient $f:\R \to \R$ et $g:\R \to \R$ deux
fonctions mesurables dont les carrés sont intégrables. 
Montrer que le produit $fg$ est intégrable.

### Intégrabilité du maximum {.exercise .question .one #im}
Soient $f:\R \to \R$ et $g:\R \to \R$ deux fonctions intégrables. 
Montrer que la fonction $\max(f, g)$ est intégrable.

### Fonction d'ordre exponentiel {.exercise .question .one #foe}
Soit $f: \left[0, +\infty\right[ \to \R$ une fonction mesurable 
pour laquelle il existe des constantes réelles $M$ et $\sigma$ telles que 
$|f(t)| \leq M e^{\sigma t}$. Montrer que si $x \geq \sigma$ alors
l'application $t \in \left[0, +\infty\right[ \mapsto f(t)e^{-xt}$ est intégrable.

### Ensemble mesurable {.proposition}
Un sous-ensemble $E$ de $\R$ est mesurable si et seulement si sa fonction
caractéristique $1_E$ est mesurable.

### Démonstration {.proof}
Si l'ensemble $E$ est mesurable, pour tout $k\in \N$, l'ensemble 
$E_k := E \cap [-k,k]$
est de longueur finie, c'est-à-dire que la fonction $1_{E_k}$ est intégrable.
La fonction $1_{E}$ est donc mesurable car limite simple de fonctions 
intégrables.

Réciproquement, si une fonction caractéristique $1_E$ est mesurable, 
par [le critère de l'image réciproque](#CIR), comme
$E = 1_{E}^{-1}(\{1\})$ et que le singleton $\{1\}$ est fermé,
$E$ est mesurable.


### Intégrabilité sur un sous-ensemble {.definition}
Une fonction $f: \R \to \R$ est dite *intégrable 
sur un sous-ensemble $E$ de $\R$* si la fonction $f 1_E$ est intégrable. 
On note alors
$$
\int_E f(t) \, dt := \int 1_E(t) f(t) \, dt.
$$


### {.remark .post}
Cette définition est cohérente avec la définition existant déjà dans le cas
où $E$ est un intervalle de $\R$ (cf. "Calcul Intégral I").

### Restriction à des ensembles mesurables {.corollary}
Une fonction $f:\R \to \R$ est intégrable
si et seulement si $f$ est intégrable sur $E$
pour tout ensemble mesurable $E$. 

### Démonstration {.proof}
Si $f$ est intégrable, elle est mesurable ; si l'ensemble
$E$ est mesurable, sa fonction caractéristique $1_E$ est également
mesurable, comme limite des $1_{E\cap[-k, k]}$ qui sont
intégrables, et donc mesurables. 
Par conséquent, le produit $f 1_E$ est mesurable, 
comme sa valeur absolue $|f 1_E|$.
Par ailleurs, comme $|1_E| \leq 1$, on a 
$|f1_E| \leq |f|$.
Par [le critère d'intégrabilité dominée](#CID), 
$f 1_E$ est donc intégrable.

Réciproquement, supposons $f 1_E$ intégrable pour tout ensemble mesurable 
$E$. En prenant $E = \R$, on constate que $f$ est nécessairement intégrable.

Annexe -- Intégrabilité conditionnelle
================================================================================

On utilise parfois le terme *conditionnellement intégrable* pour qualifier
les fonctions qui intégrables au sens de Henstock-Kurzweil mais pas au sens
de Lebesgue, car leur valeur absolue n'est pas intégrable. Nous fournissons
dans cette section l'exemple d'une telle fonction, en démontrant que
la fonction $f:[0, 1] \to \R$ définie par
$$
f(x) = \frac{1}{x} \cos \frac{1}{x^2} \, \mbox{ si }\,  x > 0 \, \mbox{ et } \, f(0) = 0
$$
est conditionnellement intégrable. 

![](images/f.py)\

Pour montrer qu'elle est intégrable au sens de Henstock-Kurzweil, 
nous exploitons la forme générale du théorème fondamental du calcul
(cf "Calcul Intégral I"), 
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
La fonction $g'$ étant également intégrable au sens de Henstock-Kurzweil, 
$f = g' + h$ est intégrable au sens de Henstock-Kurzweil comme
somme de deux fonctions intégrables au sens de Henstock-Kurzweil.

[^dn]: En effet,
$$
\left| \frac{g(h) - g(0)}{h} \right| \leq \frac{|h|}{2} \to 0 \, \mbox{ quand } \, h \to 0.
$$

La fonction $f$ n'est pourtant pas intégrable au sens de Lebesgue, 
car $h$ est intégrable au sens de Lebesgue mais pas $g'$.
En effet, si c'était le cas, toute fonction intégrable au sens de Lebesgue
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

![](images/g-prime.py)\



Par construction, $\phi_k$ est continue par morceaux et donc 
intégrable au sens de Lebesgue, et bien telle que $|\phi_k| \leq |g'|$.
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


Exercices
================================================================================

Intégrale de Gauss
--------------------------------------------------------------------------------

Source : @Swa01

On s'intéresse à la valeur de l'intégrale
$$
I := \int_0^{+\infty} e^{-t^2} \, dt.
$$
On pose 
$$
g(x) := \int_0^x e^{-t^2} \, dt
\; \mbox{ et } \;
F(x) := \int_0^1 \frac{e^{-x(1+t^2)}}{1+t^2} \, dt.
$$

### Question 1 {.question .two #exp-m2-1}
Montrer que $F$ est continue sur $\left[0, +\infty\right[$.
Calculer $F(0)$ et $\lim_{x \to +\infty} F(x)$.

### Question 2 {.question .two #exp-m2-2}
Montrons que la fonction $F$ est dérivable sur $\left]0, +\infty\right[$
et que
$$
F'(x) 
= -\frac{e^{-x}}{\sqrt{x}} g(\sqrt{x}).
$$

### Question 3 {.question .three #exp-m2-3}
Evaluer de deux façons différentes
$$
\lim_{\varepsilon \to 0^+} F(\varepsilon^{-1}) - F(\varepsilon)
$$
et en conclure que
$$
I =\frac{\sqrt{\pi}}{{2}}.
$$



Théorème de convergence dominée
--------------------------------------------------------------------------------

### Question 1  {.question .three #exo-TCD}
Montrer que la conclusion [du théorème de convergence dominée](#TCD)
est toujours valide si les fonctions $f_k$ ne satisfont 
les hypothèses de convergence et d'encadrement que presque partout.

Ensembles de longueur finie
--------------------------------------------------------------------------------

### Question 1 {.question .one #lf}
Soit $A$ un ensemble mesurable de $\R$ pour lequel il existe une
constante $L$ (finie) telle que pour tout intervalle fermé borné
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

### Question 0 {.question .three #il-0}
Montrer que $f$ est localement intégrable si et seulement si
pour tout intervalle fermé borné $[a, b]$ de $\R$, $f$ est intégrable
sur $[a, b]$.

### Question 1  {.question .one #il-1}
Montrer que toute fonction localement intégrable est mesurable.

### Question 2  {.question .two #il-2}
La réciproque est-elle vraie ?
 
Fonctions mesurables 
--------------------------------------------------------------------------------

### Question 1 {.question .four #fm-1}
Montrer qu'une fonction $f: \R \to \R$ est mesurable si et
seulement si pour tout nombre réel $a$, l'ensemble
$$
f^{-1}(\left]-\infty, a\right]) = \{x \in \R \, | \, f(x) \leq a\}
$$
est mesurable.

### Question 2 {.question .two #fm-2}
En déduire qu'une fonction croissante $f: \R \to \R$ est intégrable 
sur tout intervalle fermé borné.

Composition de fonctions et mesurabilité 
--------------------------------------------------------------------------------

### Question 1 {.question .three #cfm}
Montrer que si la fonction $f:\R \to \R$ est mesurable et que la
fonction $g: \R \to \R$ est continue par morceaux, 
alors la fonction composée $g \circ f$ est mesurable.

Composition par une fonction lipschitzienne 
--------------------------------------------------------------------------------

Soit $f:[0,1] \to \R$ et $g:\R \to \R$.
On suppose que $g$ et lipschitzienne, 
c'est-à-dire qu'il existe un $K\geq0$ tel que pour toute paire de réels 
$x$ et $y$  on ait
$|g(x) - g(y)| \leq K |x - y|$.

### Question 1 {.question .one #cfl-1}
Si $f$ est mesurable est-ce que $g \circ f$ est mesurable ?

<!--
### Question 2 {.question #cfl-2}
Si $f$ est intégrable, est-ce que $g \circ f$ est intégrable ?
-->

### Question 2 {.question .one #cfl-2}
Si $f$ est intégrable, est-ce que $g \circ f$ est 
intégrable ?

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

### Question 1 {.question .one #fmoy-1}
Que vaut $I(0)$ ?

### Question 2 {.question .three #fmoy-2}
Montrer que l'application $r \in [0, R] \mapsto I(r)$ est dérivable et
calculer $I'(r)$ pour tout $r \in [0, R]$.

### Question 3 {.question .three #fmoy-3}
On suppose désormais que $f$ vérifie les conditions de Cauchy-Riemann
en tout point $(x, y)$ de $U$, c'est-à-dire que
    $$
    \partial_y f(x, y) = R(\pi/2) \cdot \partial_x f(x, y)
    $$
    où $R(\alpha)$ désigne la rotation d'angle $\alpha$ centrée sur l'origine.
    Simplifier l'expression de $I'(r)$ et conclure.
    Indication: on pourra évaluer $\partial_{\alpha} (f(z_{\alpha, r}))$.


Solutions
================================================================================

Exercices essentiels
--------------------------------------------------------------------------------


### Défaut de domination {.answer #answer-dd}
On établit sans difficultés que pour tout $k \in \N$,
$$
\int f_k(t)\, dt = \int_k^{k+1} dt = 1, 
$$
et donc
$$
\lim_{k \to +\infty} \int f_k(t) \, dt  =1.
$$
D'autre part, pour tout $t \in \R$, on a $f_k(t) = 0$ si $k > t$, donc
$f_k(t) \to 0$ quand $k \to + \infty$ ; par conséquent,
$$
\int \lim_{k \to +\infty} f_k(t) \, dt = 0.
$$
L'intégrale de la limite des $f_k$ diffère donc de la limite des intégrales
des $f_k$. Cela ne contredit pas  [le théorème de convergence
dominée](#TCD) puisque nous n'avons pas exhibé de fonction intégrable dominant
les $f_k$ ; en l'occurence, une fonction $g$ dominant toutes les $f_k$
vérifie nécessairement $1 \leq g(t)$ pour tout $t \geq 0$, or aucune 
fonction de ce type n'est intégrable. 

### Intégrale fonction d'un paramètre {.answer #answer-ifp}
Au préalable, on note que l'application $\arctan$ est continue et donc 
intégrable sur $[0, 1]$ ; le théorème fondamental du calcul nous garantit
donc l'intégrabilité de sa primitive $t \in [0, 1] \mapsto 1/(1+t^2)$ 
et nous fournit la valeur de son intégrale :
$$
\int_0^1 \frac{dt}{1+t^2}
=
\int_0^1 \arctan'(t) \, dt
=
\arctan(1) - \arctan(0) = \frac{\pi}{4} - 0 = \frac{\pi}{4}.
$$
De plus, pour tout $x \geq 0$ et tout $t\in [0, 1]$, on a
$|e^{-xt}| \leq 1$ ; 
pour toute suite de réels strictement positifs $x_k$ tendant vers $0$, on a donc
$$
\lim_{k\to +\infty} \frac{e^{-x_kt}}{1+t^2} = \frac{1}{1+t^2}  \mbox{ et } \;
\left| \frac{e^{-x_kt}}{1+t^2} \right| \leq 
 \frac{1}{1+t^2}.
$$
Si l'on introduit des prolongements des fonctions considérées 
par zéro en dehors de $[0, 1]$,
[le théorème de convergence dominée](#TCD) nous fournit donc
$$
\lim_{x \to 0^+} \int_0^1 \frac{e^{-xt}}{1+t^2} \, dt = 
\int_0^1 \frac{dt}{1+t^2} = \frac{\pi}{4}.
$$


### Théorème fondamental du calcul {.answer #answer-TCD}
Soit $[a_k, b_k]$ une suite d'intervalles fermés bornés de $\R$ tels
que $[a_k, b_k] \subset [a, b]$ et tels que $a_k \to a$ et $b_k \to b$ quand
$k \to +\infty.$ 
Pour tout $k \in \N$, la fonction $g_k$ définie par
$$
g_k(t) = \left| 
\begin{array}{rl}
f'(t) & \mbox{si $t \in [a_k, b_k]$,} \\
0 & \mbox{sinon.}
\end{array}
\right.
$$
est intégrable car $f'|_{[a_k, b_k]}$ est intégrable par restriction ; 
la suite des $g_k$ est dominée par la fonction valant $|f'|$ sur 
$\left]a, b\right[$ et $0$ en dehors, fonction qui est intégrable par 
additivité. De plus la suite des $g_k$ converge simplement vers la
fonction égale à $f'$ sur $\left]a, b\right[$ et nulle en dehors.
Appliquer le théorème fondamental du calcul à 
$f'|_{[a_k, b_k]}$ donne par ailleurs
$$
\int_{-\infty}^{+\infty} g_k(t) \, dt = \int_{a_k}^{b_k} f'(t) \, dt = f(b_k) - f(a_k).
$$
Par application [du théorème de convergence dominée](#TCD), on obtient donc
$$
\int_a^b f'(t) \, dt = \int g(t)\, dt = \lim_{k \to +\infty}  \int g_k(t) \, dt,
$$
donc
$$
\int_a^b f'(t) \, dt  = \lim_{k\to+\infty} f(b_k) - f(a_k)
=f(b) - f(a).
$$ 

### Fonctions puissance  {.answer #answer-power}
Pour tout $x \in \left[1, +\infty\right[$, si $\alpha \neq {-1}$, 
on a
$$
\int_1^x t^{\alpha} \, dt = \left[\frac{t^{\alpha+1}}{\alpha + 1} \right]_1^x
=\frac{x^{\alpha+1}}{\alpha + 1} - \frac{1}{\alpha + 1},
$$
et pour $\alpha = -1$,
$$
\int_1^x t^{-1} \, dt = [\ln t]_1^x =\ln x.
$$
Si nous définissons les fonctions $f_k :\R \to \R$ pour $k \geq 1$ par
$$
f_k(t) = \left|
\begin{array}{rl}
t^{\alpha} & \mbox{si $t \in [1, k]$,} \\
0 & \mbox{sinon.}
\end{array}
\right.
$$
alors
$$
\lim_{k \to +\infty} \int f_k(t) \, dt = \lim_{k \to +\infty} \int_1^k t^{\alpha} \, dt,
$$
donc cette limite est finie si et seulement si $\alpha < -1$.
Comme la suite des fonctions $f_k$ est croissante et converge simplement
vers la fonction égale à $t \mapsto t^{\alpha}$ sur $\left[1, +\infty \right[$
et nulle ailleurs, nous en déduisons par [le théorème de convergence monotone](#TCM)
que la fonction $t \in \left[1, +\infty\right[ \mapsto t^{\alpha}$ est intégrable
si et seulement si $\alpha < -1$. Le cas de la fonction puissance sur 
l'intervalle $\left]0,1\right]$ peut être analysé de façon similaire, 
ou bien en pratiquant le changement de variable $t \mapsto 1/t$ pour se
ramener à l'intervalle que nous avons déjà étudié.

### Intégrabilité et intégrales impropres {.answer #answer-iii}
Si une fonction $f: \R \to \R$ est intégrable sur tout intervalle fermé
borné de $\R$, alors la suite $|f_k|: \R \to \R$ des restrictions de $|f|$ à 
$[-k, k]$ prolongées par zéro à $\R$ est croissante, composée de fonctions 
intégrables, et sa limite est la fonction $|f|$. 
Par [le théorème de convergence monotone](#TCM), on a donc
$$
\lim_{k \to +\infty} \int_{k}^k |f(t)| \, dt = \int  |f(t)| \, dt
$$
si la limite du membre de gauche est finie. La fonction $|f|$ est alors 
intégrable ; elle domine les fonctions $f_k$ qui convergent simplement vers
$f$, donc $f$ est également intégrable par [le théorème de convergence dominée](#TCD).

Réciproquement, si 
$$
\lim_{k \to +\infty} \int_{-k}^k |f(t)| \, dt = +\infty,
$$
[le théorème de convergence monotone](#TCM) prouve que la
fonction $|f|$ n'est pas intégrable et donc que $f$ n'est pas intégrable.


### Ensemble de longueur finie I {.answer #answer-elfI}
La fonction caractéristique $1_E$ est égale presque partout à la fonction
$1_{[-1, 1]}$ qui est intégrable et satisfait
$$
\int 1_{[-1, 1]}(t) \, dt = \int_{-1}^1 \, dt  =2.
$$
L'ensemble $E$ est donc de longueur finie égale à $2$.

### Ensemble de longueur finie II {.answer #answer-elfII}
La fonction caractéristique $1_{\Q}$ est nulle presque partout puisque
$\Q$ est dénombrable. Elle est donc intégrable d'intégral nulle ; l'ensemble
des rationnels $\Q$ est donc de longueur nulle.

### Ensemble de longueur finie III {.answer #answer-elfIII}
La fonction caractéristique $f = 1_E$ est la limite de la suite croissante de
fonctions $f_j = 1_{\cup_{k=0}^j \left[k, k+2^{-k} \right[}$.
Comme par linéarité de l'intégrale on a 
$$
\int f_j(t) \, dt = \sum_{k=0}^j \int 1_{\left[k, k+2^{-k} \right[}(1) \, dt
= \sum_{k=0}^j \int_k^{k+2^{-k}} \, dt
= \sum_{k=0}^j 2^{-k} = 2 - 2^{-j},
$$ 
par [le théorème de convergence monotone](#TCM), la fonction $1_E$ est intégrable
et
$$
\ell(E) = \int 1_E(t) \, dt = 2.
$$


### La longueur est additive {.answer #answer-la}
Si $A$ et $B$ sont deux ensembles de $\R$ disjoints et de longueur finie, 
alors $1_{A\cup B} = 1_A + 1_B$ donc $A\cup B$ est de longueur finie
par linéarité de l'intégrale et 
$$
\ell(A \cup B) = \int 1_{A \cup B}(t) \, dt =
\int 1_A(t) \, dt + \int 1_B(t) \, dt =
\ell(A) + \ell(B).
$$
Si $A$ et $B$ sont mesurables et disjoints, alors sur tout intervalle fermé
borné $[a, b]$ de $\R$, comme 
$$
1_{(A \cup B) \cap [a, b]} = 1_{A \cap [a, b]} + 1_{B \cap [a, b]},
$$
$A \cup B$ est mesurable. Si l'un des ensembles $A$ et $B$ au moins
a une longueur infinie, disons $A$ par exemple, 
alors par [le théorème de convergence monotone](#TCM), on a 
$$
\int_{-k}^k 1_A(t) \, dt \to +\infty \; \mbox{ quand } \; k \to +\infty.
$$
Par conséquent,
$$
\int_{-k}^k 1_A(t) \, dt \leq \int_{-k}^k 1_{A \cup B}(t) \, dt \to +\infty \; \mbox{ quand } \; k \to +\infty
$$
et donc dans ce cas aussi on a donc $\ell(A \cup B) = \ell(A) + \ell(B)$.

### Suite d'ensembles {.answer #answer-sde}
Il suffit de réaliser que d'après leur définition,
$$
B = \bigcup_{k_0=0}^{+\infty} \bigcap_{k=k_0}^{+\infty} A_k
\; \mbox{ et } \;
C = \bigcap_{k_0=0}^{+\infty} \bigcup_{k=k_0}^{+\infty} A_k
$$
puis d'invoquer la stabilité des ensembles mesurables 
[par union dénombrable](#pptés-tribu) et [intersection dénombrable](#IEM).

### Ni ouvert ni fermé {.answer #answer-nonf}
L'ensemble $E= \left[0, 1\right[$ n'est ni ouvert ni fermé : $0$ est un point
frontière qui appartient à $E$ donc $E$ n'est pas ouvert et $1$ est un point
frontière de $E$ qui n'appartient pas à $E$ donc $E$ n'est pas fermé.
Mais $E = [0, 1] \setminus \{0\}$ donc l'ensemble est le complémentaire
d'un ensemble fermé dans un autre ensemble fermé ; or [les ensembles fermés
sont mesurables](#OSM) et [le complémentaire relatif de deux ensembles mesurables
est mesurable](#CR), donc $E$ est mesurable.

### Fonctions continues {.answer #answer-fcm}
L'image réciproque de tout fermé par une application continue $f:\R \to \R^m$ 
est fermé. Comme [tout fermé est mesurable](#OSM), 
[le critère de l'image réciproque](#CIR)
prouve qu'une telle fonction continue est mesurable.

### Image réciproque d'un intervalle {.answer #answer-iri}
Tout intervalle de $\R$ peut être décomposé comme l'union (disjointe)
d'un ouvert $U$ et d'un ensemble fermé $F$ (composé de 0, 1 ou 2 points) ;
comme [ensembles ouverts ou fermés sont mesurables](#OSM), 
il est donc mesurable et [son image réciproque par $f$ est donc mesurable](#CIR).


### Intégrabilité du produit {.answer #answer-ip}
Les produits $fg$ est mesurable comme [produit de fonctions mesurables](#prod) ;
[la fonction $|fg|$ est donc également mesurable](#abs).
De plus, pour tout $x \in \R$, comme $(|f(x)| + |g(x)|)^2 \geq 0,$
$$
|fg|(x) \leq \frac{1}{2} f(x)^2 + \frac{1}{2} g(x)^2.
$$
Par le [critère d'intégrabilité dominée](#CID), 
$fg$ est donc intégrable.

### Intégrabilité du maximum {.answer #answer-im}
Les fonctions $f$ et $g$ étant intégrables, elles sont mesurables.
Par [composition avec une fonction continue](#CFC), 
$\max(f, g)$ est également mesurable.

De plus, on a $|\max(f, g)| \leq |f| + |g|$. 
La fonction $|\max(f, g)|$ est donc dominée par une fonction intégrable ; 
par le [critère d'intégrabilité dominée](#CID), $\max(f, g)$ est donc intégrable.

### Fonction d'ordre exponentiel {.answer #answer-foe}
La fonction $t \in \left[0, +\infty\right[ \mapsto f(t)e^{-xt}$ est mesurable
comme produit de fonctions mesurables. De plus, 
$$
|f(t)e^{-xt}| \leq M e^{-\varepsilon t} \; \mbox{ avec } \; \varepsilon = x - \sigma > 0,
$$
La fonction $t \mapsto M e^{-\varepsilon t}$ étant intégrable 
(intégrer la fonction sur un intervalle borné, puis passer à la limite par le
[le théorème de convergence monotone](#TCM)), la fonction
$t \in \left[0, +\infty\right[ \mapsto f(t)e^{-xt}$ est intégrable par
[le critère d'intégrabilité dominée](#CID).


Intégrale de Gauss
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-exp-m2-1}

$$
F(x) = \int_0^1 \frac{e^{-x(1+t^2)}}{1+t^2} \, dt
$$

$$
F(0)= \int_0^1 \frac{dt}{1+t^2}  =[\arctan]^1_0 = \frac{\pi}{4}.
$$

La fonction $F$ est continue sur $\left[0, +\infty\right[$. En effet, si 
$x_0 \in \left[0, +\infty\right[$, alors 
$$
\frac{e^{-x(1+t^2)}}{1+t^2} \to \frac{e^{-x_0(1+t^2)}}{1+t^2}
\; \mbox{ quand } \, x \to x_0.
$$
De plus pour tout $x \in \left[0, +\infty\right[$,
$$
\left|\frac{e^{-x(1+t^2)}}{1+t^2}\right| 
\leq 
\frac{1}{1+t^2}
$$
Le second membre de cette équation étant intégrable (il est intégrable sur
tout intervalle fermé borné et 
décroit quand $t\to +\infty$ comme $1/t^2$), par [le théorème de 
convergence dominée](#TCD),
$$
F(x) \to F(x_0) \; \mbox{ quand } \; x \to x_0.
$$
De plus, toujours par le théorème de convergence dominée
(avec la même domination), on obtient
$$
\lim_{x \to +\infty} F(x) =  \int_0^1 \lim_{x \to +\infty} \frac{e^{-x(1+t^2)}}{1+t^2}\, dt =
\int_0^1 0 \, dt =0.
$$

### Question 2 {.answer #answer-exp-m2-2}
Montrons que la fonction $F$ est dérivable sur $\left]0, +\infty\right[$.
Soit $\varepsilon > 0$ ; la fonction
$$
x \in \left]\varepsilon ,+\infty\right[ \mapsto \frac{e^{-x(1+t^2)}}{1+t^2}
$$
est dérivable en tout $x$, de dérivée égale à
$-e^{-x(1+t^2)}$, qui est dominée par $e^{-\varepsilon/(1+t^2)}$.
La fonction $t \in [0, 1] \mapsto e^{-\varepsilon/(1+t^2)}$ est intégrable car
continue. Par [le théorème de dérivation sous le signe somme](#DSS), on a
donc
$$
F'(x) = -\int_0^1 e^{-x(1+t^2)} \, dt 
$$
quand $x > \varepsilon$ et donc quand $x > 0$ puisque $\varepsilon > 0$ est 
arbitraire.
Avec $g : \left[0, +\infty\right[ \mapsto \R$ définie par
$$
g(x) = \int_0^x e^{-t^2} \, dt,
$$
pour tout $x > 0$, on a donc
$$
F'(x) = -\int_0^1 e^{-x} e^{-x t^2} \, dt
= -e^{-x} \int_0^1  e^{-x t^2} \, dt,
$$
soit avec le changement de variable $u = \sqrt{x} t$, 
$$
F'(x) 
= -\frac{e^{-x}}{\sqrt{x}} \int_0^{\sqrt{x}}  e^{-u^2} \, du
= -\frac{e^{-x}}{\sqrt{x}} g(\sqrt{x}).
$$

### Question 3 {.answer #answer-exp-m2-3}
On a d'une part par le théorème fondamental du calcul et les résultats de la
question 1
$$
\int_{\varepsilon}^{\varepsilon^{-1}} F'(x) \, dx
= F(\varepsilon^{-1}) - F(\varepsilon) \to - \frac{\pi}{4}
\; \mbox{ quand }  \; \varepsilon \to 0^+,
$$
et d'autre part avec l'expression de la question 2 de $F'$ et le changement
de variable $x=\sqrt{t}$, on obtient
\begin{align*}
\int_{\varepsilon}^{\varepsilon^{-1}} F'(x) \, dx
&= - \int_{\varepsilon}^{\varepsilon^{-1}} \frac{e^{-x}}{\sqrt{x}} g(\sqrt{x}) \, dx \\
&= - 2 \int_{\varepsilon}^{\varepsilon^{-1}} e^{-\sqrt{x}^2}g(\sqrt{x}) \, \frac{dx}{2\sqrt{x}} \\
&=- 2 \int_{\sqrt{\varepsilon}}^{1/\sqrt{\varepsilon}} {e^{-u^2}} g(u) \, du \\
&= - \int_{\sqrt{\varepsilon}}^{1/\sqrt{\varepsilon}} 2g'(u) g(u) \, du \\
&= - \int_{\sqrt{\varepsilon}}^{1/\sqrt{\varepsilon}} ((g(u))^2)' \, du \\
&= - \left[(g(u))^2\right]_{\sqrt{\varepsilon}}^{1/\sqrt{\varepsilon}} \\
&= -\left(g\left(1/\sqrt{\varepsilon}\right)\right)^2 + \left(g\left(\sqrt{\varepsilon}\right)\right)^2
\end{align*}
et donc
$$
\int_{\varepsilon}^{\varepsilon^{-1}} F'(x) \, dx
\to -  \left(\int_0^{+\infty} e^{-t^2} \, dt \right)^2
\; \mbox{ quand }  \; \varepsilon \to 0^+.
$$
On conclut finalement que 
$$
\int_0^{+\infty} e^{-t^2} \, dt = \sqrt{\frac{\pi}{4}} = \frac{\sqrt{\pi}}{{2}}.
$$



Théorème de convergence dominée
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-exo-TCD}
Imaginons que les fonctions mesurables $f_k$ convergent vers la fonction
$f$ sur $\R \setminus A$ où $A$ est négligeable, et satisfont 
$g \leq f_k \leq h$ sur l'ensemble $\R \setminus B_k$ où $B_k$ est
négligeable.

Alors l'ensemble $C := A \cup (\cup_{k=1}^{+\infty} B_k)$ est négligeable,
comme on l'a montré dans l'exercice "Union d'ensembles négligeables" du
chapitre précédent.
On peut aussi s'en convaincre avec le calcul intégral :
$A$ et les $B_k$ [sont négligeables, donc mesurables et de longueur nulle](#négligeable-longueur-nulle) ;
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
<!--
Alternativement, il suffit de recouvrir $A$ puis chaque $B_k$ par des intervalles
sont la somme de longueurs soit inférieure à $\varepsilon/2$, puis $\varepsilon/2^{k+2}$.
La collection de l'intégralité de ces intervalle est dénombrable, recouvre
l'ensemble $C$, et la somme des longueurs des intervalles est inférieure à 
$$
\frac{\varepsilon}{2} + \sum_{k=0}^{+\infty} \frac{\varepsilon}{2^{k+1}} = \varepsilon.
$$-->
L'ensemble $C$ [est de longueur nulle et donc négligeable](#négligeable-longueur-nulle).

Sachant que $C$ est négligeable, c'est-à-dire mesurable et de longueur nulle,
il suffit alors de rédéfinir chaque fonction $f_k$, $f$, $g$ et $h$ pour leur
assigner la valeur $0$ en tout $x \in C$ ; cette opération ne change pas leur
caractère mesurable ou intégrable, ni la valeur des intégrales associées.
Et les nouvelles fonctions satisfont partout les hypothèses de convergence
et d'encadrement du [théorème de convergence dominée](#TCD). On peut donc
conclure sous les hypothèses plus faibles considérées dans cet exercice.

Ensembles de longueur finie 
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-lf}
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
[Le théorème de convergence monotone](#TCM) nous garantit l'intégrabilité de
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
De toute évidence, si $f$ est intégrable sur tout intervalle fermé borné,
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
La suite des points centraux $(a_k+b_k)/2$ étant de Cauchy, elle a une limite
$x$ appartenant à tous ces intervalles fermés ;
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
En effet, quand $2^{-k} \leq \varepsilon$, on a
$$
\begin{split}
\int_{-\varepsilon}^{\varepsilon} f_k(x) \, dx 
&= \int_{-\varepsilon}^{-2^{-k}} \frac{dx}{x^2} + \int_{2^{-k}}^{\varepsilon} \frac{dx}{x^2} \\
&= \left[ -\frac{1}{x} \right]_{-\varepsilon}^{-2^{-k}} + \left[ -\frac{1}{x}\right]_{2^{-k}}^{\varepsilon} \\
&= (2^k - 1/\varepsilon) + (2^k - 1/\varepsilon) = 2^{k+1} - 2/\varepsilon.
\end{split}
$$
Cette grandeur tendant vers $+\infty$ quand $k \to +\infty$, 
[le théorème de convergence monotone](#TCM) nous garantit que
la fonction $f$ n'est pas intégrable sur $[-\varepsilon, \varepsilon]$.

Fonction mesurables
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-fm-1}

Compte tenu du [critère de l'image réciproque](#CIR),
comme tous les ensembles $\left]-\infty, a\right]$ sont fermés, 
le critère de l'énoncé est bien vérifié pour toute fonction mesurable.

Montrons désormais la réciproque. Supposons le critère de l'énoncé vérifié et 
soit $U$ un ouvert de $\R$ ; l'ensemble $U$ peut être décomposé comme
union dénombrable d'intervalles ouverts bornés $I_k$ de $\R$.
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
En effet, si $f(x) \leq a$ et $f(y) \leq a$ et $x \leq y$, 
pour tout point intermédiaire $x \leq z \leq y$, $f(z) \leq a$. 
Par conséquent, $f$ est mesurable.

De plus, $f$ étant croissante, pour tout intervalle fermé borné $[a, b]$ et tout
$x \in [a, b]$, on a $f(a) \leq f(x) \leq f(b)$.
Par le [critère d'intégrabilité dominée](#CID), $f$ est intégrable sur
$[a, b]$.


Composition de fonctions et mesurabilité 
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-cfm}
Soient $\dots \leq a_{-k} \leq \dots \leq a_{-1} \leq a_0 \leq a_1 \leq \dots \leq a_k$ des nombres réels 
tels que la fonction $g$ soit continue sur
chaque intervalle ouvert $\left]a_j, a_{j+1} \right[$. Soit $U$ un ouvert
de $\R$ ; alors pour tout $j$, 
si $g_j$ désigne la restriction de $g$ à $\left]a_j, a_{j+1} \right[$, 
par continuité de $g_j$, 
l'image réciproque $V_j = g_j^{-1}(U)$ est ouverte dans $\left]a_j, a_{j+1} \right[$
et donc dans $\R$. L'image réciproque de $U$ par $g$ est donc la réunion $V$
de ces ouverts, c'est-à-dire un ouvert, 
et éventuellement d'un sous-ensemble $N$ 
des $\{a_k\}$ qui est nécessairement dénombrable, 
donc mesurable (et de longueur nulle).

L'image réciproque de $U$ par $g\circ f$ est donc l'image réciproque de 
$V \cup N$ par $f$. La fonction $f$ étant mesurable, $f^{-1}(V)$ et
$f^{-1}(N)$ sont mesurables, 
ainsi que $f^{-1}(V \cup N) = f^{-1}(V) \cup f^{-1}(N)$.
La fonction composée $g \circ f$ est donc mesurable.


Composition par une fonction lipschitzienne 
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-cfl-1}
Oui, car toute fonction lipschitzienne est continue ; 
$g \circ f$ est donc mesurable 
comme [composée d'une fonction mesurable et d'une fonction continue](#CFC).

<!--
### Question 2 {.answer #answer-cfl-2}
Pas nécessairement; si $f$ est une fonction conditionnellement
intégrable sur $[0,1]$, la fonction $|f|$ n'est pas intégrable ; 
or, l'application $t \mapsto |t|$ est lipschitzienne (avec $K=1$).
-->

### Question 2 {.answer #answer-cfl-2}
Oui. D'une part, $f$ étant  intégrable, elle est mesurable et
donc par la question 1, la composée $g \circ f$ est mesurable.
D'autre part, pour tout $x \in [0,1]$, on a
$$
|g \circ f(x) - g \circ f(0)| \leq K |f(x) - f(0)|
$$
et donc
$$
|g \circ f(x)| \leq K |f(x)| + (K |f(0)| + |g \circ f(0)|)
$$
Le membre de droite de cette inégalité est une fonction
intégrable sur $[0, 1]$, donc par [le critère d'intégrabilité dominée](#CID),
la fonction $g \circ f$ est intégrable.

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
à l'ensemble fermé borné $[0, 2\pi] \times [0, R]$.
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
est bornée par la fonction intégrable (constante)
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


Références
================================================================================
