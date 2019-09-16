% Calcul Intégral IV

<!-- LaTeX Macros -->
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}

\newcommand{\ds}{\mathbin{\Delta}}

### TODO

Référence @Hun11 proprement.

TODO -- Mesure de Lebesgue dans $\R^n$
================================================================================

Dans les volets [II](Calcul Intégral II.pdf) et [III](Calcul Intégral) 
du "Calcul Intégral", 
nous avons défini le volume d'un pavé 
$$
P = [a_1, b_1] \times \dots \times [a_n, b_n]
$$
au moyen de la formule
$$
v(P) := (b_1  -a_1) \times \dots \times (b_n - a_n).
$$
L'intégrable de Henstock-Kurzweil nous permet alors d'étendre la fonction
$v$ en une fonction définie sur tous les ensembles mesurables $A$ de $\R^n$,
par la relation
$$
v(A) = \int 1_A(x) dx
$$
si $1_A$ est intégrable et $v(A) = +\infty$ sinon.
Cette approche n'est pas totalement satisfaisante intellectuellement : 
d'une part on peut considérer l'usage de l'intégrale comme un chemin
tortueux pour étendre $v$ ; d'autre part on peut avoir l'impression
que cette approche -- qui ne permet pas de mesure le volume de tout
ensemble de $\R^n$ -- n'atteint pas totalement son objectif. 
Cette limitation pourrait être un artefact du passage par l'intégrale.
Dans cette section, nous allons donner une méthode directe pour étendre
la mesure du volume dans $\R^n$ au-delà des pavés.
Quant à la seconde préoccupation, 
malheureusement nous n'allons pas réussir à faire
mieux que l'approche par l'intégrale par la méthode directe ;
néanmoins, nous allons pouvoir établir précisement en quoi mesurer le volume
de tous les ensembles de $\R^n$ est problématique.

Un processus "raisonnable" pour évaluer le volume consiste à généraliser
la démarche déjà entreprise dans la définition des ensembles négligeables : 
nous nous basons sur le recouvrement d'un ensemble arbitraire par un 
recouvrement dénombrable de pavés (pouvant se recouvrir entre eux) pour 
obtenir une estimation supérieure du volume de l'ensemble. Formellement :

### Mesure extérieure de Lebesgue {.definition}
On appelle *mesure extérieure de Lebesgue* dans $\R^n$ la fonction
qui a tout ensemble de $\R^n$ associe un nombre réel étendu positif
$$v^*: \mathcal{P}(\R^n) \to [0, +\infty],$$ 
définie par
$$
v^*(A) 
= 
\inf 
\left\{
\sum_{k=1}^p v(P_k)
\; \left| \vphantom{\bigcup_{k=1}^{+\infty}} \right. \; 
\mbox{$P_k$ pavé de $\R^n$,} \, A \subset \bigcup_{k=1}^p P_k
\right\},
$$

Cette définition "raisonnable" ne satisfait toutefois pas les propriétés que
nous attendons (implicitement) d'un volume. Ce décalage est mise en évidence
par un résultat paradoxal de la théorie des ensembles dans $\R^3$ :

### Paradoxe de Banach-Tarski {.theorem}
Il est possible de partitionner une sphère $S_0$ de rayon unitaire de $\R^3$ 
en un nombre fini d'ensembles, qui, 
après rotations et translations, 
forment une partition de deux sphères $S_1$ et $S_2$ disjointes de rayon unitaire.

Soient $A_1, \dots, A_p$([^how-many]) des ensembles disjoints et non vides
de $\R^3$ tels que $S = A_1 \cup \dots\cup A_p$,
tels que des ensembles disjoints $B_1, \dots, B_p$ 
qui s'en déduisent par rotation et translation, 
vérifient $S_1 \cup S_2 = B_1 \cup \dots \cup B_p$.

[^how-many]: il est possible de prendre 6 morceaux d'après 
la preuve originale de Banach et Tarski (1924) ; 
Robinson a prouvé en 1947 que $p=5$ était suffisant.

Si le résultat semble paradoxal, c'est qu'il nous semble intuitivement 
que le volume devrait être préservé par les les opérations subies par 
la sphère initiale. Or, le volume d'une sphère de rayon un et de deux 
sphères disjointes de même rayon diffère d'un facteur $2$ ...
Pour dépasser ce paradoxe, nous allons devoir examiner un par un les
résultats qui nous semblent évidents dans ce raisonnement.

Tout d'abord, on a bien
$$
v^*(S) = \frac{4\pi}{3} \; \mbox{ et } \; v^*(S_1 \cup S_2) = 2 \times \frac{4 \pi}{3}.
$$
Les ensembles $S_0$, $S_1$ et $S_2$ sont intégrables et dans ce cas $v^*(A)$ 
peut être évalué par l'intégrable de Henstock-Kurzweil, 
ce qui fournit le résultat.

On peut croire que le point critique dans notre définition est la préservation
de la valeur de $v^*(A)$ par translation et rotation ; s'il est facile d'établir
que si $B$ se déduit de $A$ par une translation, $v^*(A) = v^*(B)$, on peut douter
du résultat pour les rotations. Après tout, la définition de $v^*(A)$ fait appel
à des rectangles qui sont parallèles aux axes, une propriété qui n'est pas
conservée par rotation. 
Mais si le résultat n'est pas évident, il s'avère pourtant que
la mesure $v^*$ est bien invariante par
rotation (cf. (@Hun11, section 2.8).

La propriété qui nous fait défaut est plus fondamentale : la fonction $v^*$
n'est pas additive ! Même si les ensembles $A_1, \dots, A_p$ sont disjoints,
il est possible que 
$$
v^*(A_1 \cup \dots \cup A_p) \neq v^*(A_1) + \dots + v^*(A_p).
$$
On peut par contre établir avec la définition de $v^*$ qu'elle est 
sous-additive : pour tous les ensembles $A_1, \dots, A_p$ (disjoints ou non),
on a 
$$
v^*(A_1 \cup \dots \cup A_p) \leq v^*(A_1) + \dots + v^*(A_p).
$$
Elle est même $\sigma$-sous-additive : si $A_k$, $k \in \N$ sont des
sous-ensembles de $\R^n$, 
$$
v^*\left(\bigcup_{k=1}^{+\infty} A_k\right)
= \sum_{k=1}^n v^*\left(A_k\right).
$$

Cette propriété est caractéristique des mesures extérieures :

### Mesure extérieure {.definition}
On appelle *mesure extérieure* sur l'ensemble $X$ toute application
$\mu^* :\mathcal{P}(X) \to [0, +\infty]$ telle que $\mu(\varnothing) = 0$
et pour tous $A_k \subset X$, $k \in \N$, 
$$
\mu^*\left(\bigcup_{k=1}^{+\infty} A_k\right)
= \sum_{k=1}^n \mu^*\left(A_k\right).
$$

Il existe un procédé général permettant de déduire d'une mesure extérieure
une application qui soit additive -- à condition d'accepter de réduire
son domaine de définition ; la fonction qui en résulte est non seulement
additive, mais même $\sigma$-additive. Dans le cas de la mesure extérieure
de Lebesgue, elle donne lieu à la mesure de Lebesgue.

### Ensemble mesurable au sens de Carathédory
Soit $\mu^*$ une mesure extérieure sur l'ensemble $X$ ;
un ensemble $A \subset X$ est dit *$\mu^*$-mesurable* 
si pour tout $B \subset X$, on a 
$$
\mu^*(B) = \mu^*(B \cap A) + \mu^*(B \setminus A).
$$

### {.post}
Une façon alternative de voir les choses : si l'on note $\mu^*_{|A}$ 
la trace de $\mu^*$ sur un ensemble $A$ de $X$, définie pour tout
sous-ensemble $B$ de $X$ par
$$\mu^*_{|A}(B) = \mu^*(B \cap A),$$
alors l'ensemble $A$ est $\mu^*$ mesurable si et seulement si
$$
\mu^* = \mu^*_{|A} + \mu^*_{|A^c},
$$


### Tribu {.definition}
Une *tribu* ou *$\sigma$-algèbre* $\mathcal{A}$ sur un ensemble $X$ est une 
collection d'ensembles de $X$ contenant l'ensemble vide et stable par passage 
au complémentaire et à l'union dénombrable. 
Un ensemble de $\mathcal{A}$ est dit *mesurable* ; 
l'ensemble $X$ muni de $\mathcal{A}$ est un *espace mesurable*.

### Mesure {.definition}
Une *mesure* $\mu$ sur un espace mesurable $(X, \mathcal{A})$
est une fonction de $\mathcal{A}$ dans $[0, +\infty]$ telle que $\mu(\varnothing)= 0$
et pour toute collection dénombrable $\{A_1,\dots, A_k, \dots\}$ d'ensembles de
$\mathcal{A}$ disjoints deux à deux, on ait
$$
\mu \left( \bigcup_{k} A_k \right) = \sum_{k} \mu(A_k) ;
$$
on dit que $\mu$ est *$\sigma$-additive*.
L'ensemble $X$ muni de $\mathcal{A}$ et $\mu$ est un *espace mesuré*.

### Mesure déduite d'une mesure extérieure {.theorem}
Soit $X$ un ensemble et $\mu^*$ une mesure extérieure sur $X$.
La collection $\mathcal{A}$ des ensembles $\mu^*$-mesurables de $X$
est une tribu sur $X$, et la restriction $\mu$ de $\mu^*$ à 
$\mathcal{A}$ est une mesure sur $X$.

### TODO -- Démonstration {.proof}

### TODO: Lebesgue, étend bien le volume des rectangles


TODO -- Mesure de grandeurs
================================================================================

### TODO ; refocus Lebesgue directement.

Il est possible même au sein d'un espace unique comme $\R^3$ de vouloir
mesurer différentes grandeurs attachées à un ensemble $A$. 
On peut ainsi vouloir compter le nombre de points que contient $A$
(sa "mesure de comptage"), sa longueur, sa surface ou encore son volume.

L'exemple du volume a déjà été traité avec l'intégrale de Henstock-Kurzweil
dans $\R^3$. L'exemple de la surface, a été partiellement traité, 
dans un cas très limité (la frontière de compacts à bord réguliers) 
et au prix d'un processus complexe
permettant de se ramener à des calculs d'intégrale dans $\R^2$.
Il est en fait possible de traiter ces quatres type de grandeurs, 
ces quatre *mesures* différentes de façon similaire, et sans requérir
à la notion d'intégrale. 

Détaillons tous d'abord le cas de la mesure du volume dans $\R^3$.
Le volume de la sphère de même diamètre qu'un ensemble $B$ arbitraire 
est donnée par
$$
\frac{4 \pi}{3} \left(\frac{\mathrm{diam} \, B}{2}\right)^3.
$$
On peut alors calculer pour tout $\delta > 0$ estimer le volume d'un ensemble
$A$ à partir de tous les recouvrements dénombrables de $A$ par des ensembles
de diamètre inférieur ou égal à $\delta$ par
$$
\mathcal{H}^3_{\delta}(A) =
\inf \left\{
\sum_{j=1}^{+\infty} \frac{4\pi}{3} \left(\frac{\mathrm{diam} \, B_j}{2}\right)^k
\; \left| \vphantom{\left(\frac{\mathrm{diam} \, B_j}{2}\right)^k} \right. \; 
A \subset \sum_{j=1}^{+\infty} B_j, \, \mathrm{diam} \, B_j \leq \delta 
\right\},
$$
puis passer à la limite sur $\delta$. 
Il s'avère que le résultat
-- on parle de *mesure de Hausdorff* de dimension $3$ de $A$ --
est identique à l'approche par l'intégrale de Henstock-Kurzweil quand
l'ensemble $A$ est mesurable :
$$
\mathcal{H}^3(A) = \int_A \, dx.
$$
On pense a priori avoir amélioré notre approche pour définir le volume d'un
ensemble $A$, puisque l'on a supprimé la limitation que l'ensemble $A$ soit 
mesurable. Toutefois, la mesure $\mathcal{H}^3$ qui résulte de cette définition
perd une propriété importante qui est implicitement attachée à toutes les
grandeurs que nous avons cité.

Ce problème sera mis en évidence par le résultat suivant :



Notons $A_1, \dots, A_n$ la partition de la sphère initiale
et $B_1, \dots, B_n$ leurs images après rotation et translation.
Comme par construction la mesure $\mathcal{H}^3$ est invariante par
rotation et translation, il semble que l'on doive avoir
$$
\mathcal{H}^3(S) = \sum_{i=1}^n \mathcal{H}^3(A_i)
= \sum_{i=1}^n \mathcal{H}^3(B_i) = \mathcal{H}^3(S_1) + \mathcal{H}(S_2)
=2 \times \mathcal{H}^3(S),
$$ 
une contradiction puisque $\mathcal{H}^3(S) = 4\pi/3$.

**TODO** négation de l'additivité, comment la retrouver (ensembles qui
"splittent" proprement la mesure) et on retombe sur les ensembles
mesurables.

Généralisation de la démarche : le procédé utilisée, qq soit la mesure
élémentaire, génère une fct sous-additive appelée mesure extérieures. 
Les ensembles qui splittent proprement la mesure sont appelés ensembles
mesurables, la restriction de la mesure à ces ensembles est additive,
et même $\sigma$-additive.

Et on "reboote" la théorie abstraite de la mesure à ce point.

--------------------------------------------------------------------------------

$$
\mathcal{H}^k_{\delta}(A) 
= 
\inf \left\{
\sum_{j=1}^{+\infty} \alpha(k)\left(\frac{\mathrm{diam} \, B_j}{2}\right)^k
\; \left| \vphantom{\left(\frac{\mathrm{diam} \, B_j}{2}\right)^k} \right. \; 
A \subset \sum_{j=1}^{+\infty} B_j, \, \mathrm{diam} \, B_j \leq \delta 
\right\}
$$
où $\alpha(k)$ est le volume de la $k$-sphère unité dans $\R^k$([^G])
$$
\alpha(k) = \int_{\R^k} 1_{S_k}(x) \, dx 
\; \mbox{ où } \; 
S_k = \left\{x \in \R^k \; | \; x_1^2 + \dots + x_k^2 \leq 1 \right\}.
$$

La mesure de Hausdorff $\mathcal{H}^k(A)$ de dimension $k$ de l'ensemble
$A \subset \R^n$ est définie par 
$$
\mathcal{H}^k(A) = \lim_{\delta \to 0} \mathcal{H}^k_{\delta}(A).
$$

[^G]: on a $$\alpha(k) = \frac{\pi^{k/2}}{\Gamma \left( \frac{k}{2}+1 \right)} 
\; \mbox{ avec } \; 
\Gamma(x) = \int_0^{+\infty} e^{-t} t^{x-1}\, dt.$$ 
La fonction $\Gamma$ est caractérisée pour des valeurs entières et
demi-entières par $\Gamma(1/2) = \sqrt{\pi}$, $\Gamma(1) = 1$ et généralement
par $\Gamma(x+1)= x\Gamma(x)$.

Mesure et intégrale
================================================================================

On rappelle:

### Tribu {.definition}
Une *tribu* ou *$\sigma$-algèbre* $\mathcal{A}$ sur un ensemble $X$ est une 
collection d'ensembles de $X$ contenant l'ensemble vide et stable par passage 
au complémentaire et à l'union dénombrable. 
Un ensemble de $\mathcal{A}$ est dit *mesurable* ; 
l'ensemble $X$ muni de $\mathcal{A}$ est un *espace mesurable*.

### Tribu engendrée par une collection {.definition}
Dans un ensemble $X$, on appelle *tribu engendrée* par une collection 
$\mathcal{C}$ d'ensembles de $X$ la plus petite (au sens de l'inclusion) 
tribu $\mathcal{A} = \sigma(\mathcal{C})$ de $X$ contenant $\mathcal{C}$.

### Démonstration de l'existence de la tribu engendrée {.proof}
Désignons par $\mathfrak{S}$ la (meta-)collection des tribus de 
$X$ incluant $\mathcal{C}$ (contenant $\mathcal{C}$ comme sous-ensemble). 
Elle n'est pas vide : elle contient la collection $\mathcal{P}(X)$
des ensembles de $X$ (qui de toute évidence est un sur-ensemble de $\mathcal{C}$
et une tribu de $X$). Montrons que la plus petite tribu $\sigma(\mathcal{C})$
de $X$ contenant $\mathcal{C}$ est l'intersection de $\mathfrak{S}$:
$$
\sigma(\mathcal{C}) := \bigcap \mathfrak{S} = \bigcap_{\mathcal{A} \in \mathfrak{S}} \mathcal{A},
$$
ou encore
$\sigma(\mathcal{C}) = \{A \subset X \, | \, A \in \mathcal{A} \mbox{ pour tout } \mathcal{A} \in \mathfrak{S}\}.$
Il est clair que si $\mathcal{A}$ est une tribu de $X$ contenant $\mathcal{C}$,
alors $\mathfrak{S} \subset \mathcal{A}$, car alors $\mathcal{A} \in \mathfrak{S}$.
Il nous suffit donc de montrer que $\cap \mathfrak{S}$ est une tribu de $X$
pour conclure ; on vérifiera aisément que comme chaque élément de $\mathfrak{S}$
est une tribu, cette intersection en est également une.

### Tribu de Lebesgue {.definition}
On appelle *tribu de Lebesgue* sur $\R^n$ la tribu composée des ensembles $E$
tels que pour tout pavé $P$ de $\R^n$, la fonction caractéristique 
de $E \cap P$ soit intégrable (au sens de Henstock-Kurzweil).

### {.post}
La tribu de Lebesgue est donc composée des ensembles mesurables au sens
du chapitre "Calcul Intégral III".

### TODO -- Référence
Lier au chapitre "Calcul Intégral III" en détail.

### Tribu de Borel {.definition}
On appelle *tribu de Borel* d'un espace topologique $X$ la plus petite tribu
contenant tous les fermés (ou tous les ouverts) de $X$.

### Mesure {.definition}
Une *mesure (positive)* $\mu$ sur un espace mesurable $(X, \mathcal{A})$
est une fonction de $\mathcal{A}$ dans $[0, +\infty]$ telle que $\mu(\varnothing)= 0$
et pour toute collection dénombrable $\{A_1,\dots, A_k, \dots\}$ d'ensembles de
$\mathcal{A}$ disjoints deux à deux, on ait
$$
\mu \left( \bigcup_{k} A_k \right) = \sum_{k} \mu(A_k) ;
$$
on dit que $\mu$ est *$\sigma$-additive*.
L'ensemble $X$ muni de $\mathcal{A}$ et $\mu$ est un *espace mesuré*.

### TODO -- Pb
Gérer "pb" des fonctions à valeurs étendues ? Non, il n'y en a pas ...

### Fonction mesurable
Une fonction $f: X \to Y$ associée aux espaces mesurables $(X, \mathcal{A})$
et $(Y,\mathcal{B})$ est *mesurable* si l'image réciproque $A =f^{-1}(B)$
de tout ensemble $B$ de $\mathcal{B}$ par $f$ appartient à $\mathcal{A}$.

### Conventions
Lorsque $Y$ a une structure topologique, on supposera par défaut que la 
tribu associée est la tribu de Borel, et lorsque $X = \R^n$ 
que la tribu associée est la tribu de Lebesgue. 
Lorsque l'on souhaitera munir également $X$ de la tribu de Borel,
on parlera de fonctions *borélienne* (tribu de Borel au départ et à l'arrivée).
Il existe une bonne raison pour adopter cette convention :

### Mesurable ou mesurable ?
Une fonction $f:\R^n \to \R^m$ est mesurable au sens du chapitre III,
c'est-à-dire limite simple de fonctions intégrables 
au sens de Henstock-Kurzweil,
si et seulement si elle est mesurable au sens de ce chapitre quand 
l'espace de départ $\R^n$  est muni de la tribu de Lebesgue et 
l'espace d'arrivée $\R^m$ de la tribu de Borel.

### TODO -- Démonstration {.proof}

### TODO: composition de fcts mesurables
Intérêt de fcts boréliennes dans ce schéma, lien avec Calcul Intégral III
(généralisation résultats composition)

### Fonction étagée {.definition}
On appelle *fonction étagée* toute fonction $f: X \to Y$ telle que
l'image réciproque de $Y$ par $f$ soit finie (telle que $f$ ne
prenne qu'un nombre fini de valeurs).

### Intégrale d'une fonction étagée
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré et 
$f: X \mapsto \left[0, +\infty\right[$ une fonction étagée positive et mesurable.
Soit $Y = f(X)$ l'ensemble des valeurs prises par $f$.
On appelle *intégrale de Lebesgue de $f$ relativement à la mesure $\mu$*
la grandeur positive finie
$$
\int_X f \mu := \int_X f(x) \mu(dx) := \sum_{y \in Y} y \times \mu(f^{-1}(\{y\})).
$$

### Intégrale d'une fonction positive
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré et 
$f: X \mapsto [0, +\infty]$ une fonction mesurable.
Soit $\mathcal{F}$ la collection des fonctions étagées positives et mesurables
inférieures à $f$.
On appelle *intégrale de Lebesgue de $f$ relativement à la mesure $\mu$*
la grandeur positive (finie ou infinie)
$$
\int_X f \mu := \int_X f(x) \mu(dx) := \sup_{g \in \mathcal{F}} \int_X g \mu.
$$

### Intégrale d'une fonction à valeurs réelles
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré et 
$f: X \mapsto [-\infty, +\infty]$ une fonction mesurable.
On dit que la fonction $f$ est *intégrable au sens de Lebesgue 
relativement à la mesure $\mu$* si elle est mesurable et que 
les intégrales des fonctions positives 
$f_+ = \max(f, 0)$ et $f_- = -\min(f, 0)$ sont finies. 
*L'intégrale de Lebesgue de $f$ relativement à la mesure $\mu$*
est alors la grandeur réelle (finie)
$$
\int_X f \mu :=  \int_X f(x) \mu(dx) := \int_X f_+ \mu - \int_X f_- \mu.
$$ 

### TODO 
Noter intégrale de fcts positives "plus souple"  et fct pas considérée
intégrable (même si on peut donner une valeur à son intégrale !) si
l'intégrale est infinie; 
mais on est obligé d'être plus restrictif pour les fonctions signées, 
en raison du risque
de $+\infty - \infty$. Evoquer certains auteurs qui tolèrent l'une ou
l'autre des valeurs

### TODO
Noter intégrale de Lebesgue absolue par construction.

### TODO
aller vers la mesure de longueur. Par les mesures extérieures ? Yes.
Mmmm, oui, mais-pas-que. On a déjà $\ell$ et les ensembles mesurables
associés via la théorie HK (ou $v$ dans $\R^n$), 
on ne vas pas la jeter si ? Non !

### TODO
"Equivalence" intégrabilité Lebesgue et HK absolue (modulo gestion des
valeurs infinies.)

Exercices
================================================================================

Mesure image 
--------------------------------------------------------------------------------

Soit $(X, \mathcal{A}, \mu)$ un espace mesuré et $h: X \to Y$ une application.
On définit la collection 
$$
\mathcal{B} = \{B \subset Y \, | \, h^{-1}(B) \in \mathcal{A}\}
$$
et la fonction $\mu \circ h^{-1}: \mathcal{B} \to [0, +\infty]$ par
$$
\mu \circ h^{-1}(B) = \mu(h^{-1}(B)).
$$

### Question 1 {.question #mi-1}
Montrer que $\mathcal{B}$ est une tribu.

### Question 2 {.question #mi-2}
Montrer que $\mu \circ h^{-1}$ est une mesure sur $\mathcal{B}$ ; 
on l'appelle la *mesure image de $\mu$ par $h$*.

### Question 3 {.question #mi-3}
Montrer que la fonction $f:Y \to \R$ est $\mu \circ h^{-1}$-intégrable 
si et seulement si $f \circ h$ est $\mu$-intégrable et qu'alors,
$$
\int_Y f \, (\mu \circ h^{-1})(dx) = \int_X (f \circ h) \mu(dx).
$$


Complétion d'une tribu {#ct .question}
--------------------------------------------------------------------------------

Soit $(X, \mathcal{A}, \mu)$ un espace mesuré. 
On note $A \ds B$ la différence symétrique
de deux sous-ensembles $A$ et $B$ de $X$ l'ensemble défini par
$$
A \ds B = (A \setminus B) \cup (B \setminus A) = (A \cap B^c) \cup (A^c \cap B).
$$
Caractériser au moyen de la différence symétrique la tribu engendrée par 
l'union entre $\mathcal{A}$ et la collection $\mathcal{N}$ 
des ensembles négligeables pour $\mu$ :
$$
\mathcal{N} = 
\{
N \subset X 
\; | \;
\mbox{il existe $A \in \mathcal{A}$ tel que $N \subset A$ et $\mu(A) = 0$.} 
\}.
$$


TODO -- Fonctions mesurables
--------------------------------------------------------------------------------

(pour des mesures "exotiques" ... mesure de comptage, densité uniforme,
sur $[0, 1]$, mesure de dirac en $0$ ?)

TODO -- Mesures de Hausdorff
--------------------------------------------------------------------------------

Que faire ? Définir le volume, la surface et la longueur dans $\R^3$, 
montrer que l'on a affaire à des mesures extérieures ?

TODO -- Extension
--------------------------------------------------------------------------------

Tribu générée à partir d'un anneau (e.g. ens. des intervalles $\left[a,b\right[$),
extension d'une prémesure ? Problématique de non-unicité ? Unicité sous
caractère $\sigma$-fini ? cf <https://mpaldridge.github.io/teaching/ma40042-notes-06.pdf> 

Solutions
================================================================================

TODO -- Mesure image 
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-mi-1}
L'ensemble $\mathcal{B}$ est une tribu ; en effet :

  - $\varnothing \in \mathcal{A}$ et $\varnothing = h^{-1}(\varnothing)$,
    donc $\varnothing \in \mathcal{B}$.

  - Si $B \in \mathcal{B}$, l'ensemble 
    $A = h^{-1}(B)$ appartient à $\mathcal{A}$. 
    Le complémentaire $Y \setminus B$ de $B$ dans $Y$
    vérifie $h^{-1}(Y \setminus B) = X \setminus h^{-1}(B) = X \setminus A$
    et appartient donc à $\mathcal{A}$. L'ensemble $Y \setminus B$ appartient
    donc à $\mathcal{B}$.

  - Si les ensembles $B_k$, $k \in N$ appartiennent à $\mathcal{B}$, 
    comme $h^{-1}(\cup_k B_k) = \cup_k h^{-1}(B_k)$, cet ensemble
    appartient à $\mathcal{A}$. L'union dénombrable $\cup_k B_k$
    appartient donc à $\mathcal{B}$.

### Question 2 {.answer #answer-mi-2}
Montrons que $\mu \circ h^{-1}$ est une mesure sur $\mathcal{B}$.

  - On a $h_*\mu(\varnothing) = \mu(h^{-1}(\varnothing)) = \mu(\varnothing) = 0$.

  - Si les ensembles $B_k$, $k \in \N$, appartiennent à $\mathcal{B}$ et sont
    disjoints, alors les ensembles $h^{-1}(B_k)$ appartiennent à $\mathcal{A}$,
    et sont disjoints. Comme $h^{-1}(\cup_k B_k) = \cup_k h^{-1}(B_k)$, on a
    $$
    \begin{split}
    \mu \circ h^{-1} \left(\bigcup_k B_k \right)
    &=
    \mu\left(h^{-1}\left(\bigcup_k B_k \right)\right) \\
    &=
    \mu\left(\bigcup_k h^{-1}\left( B_k \right)\right) \\
    &=
    \sum_k \mu\left(h^{-1}\left( B_k \right)\right) \\
    &=
    \sum_k \mu \circ h^{-1}\left(B_k\right)
    \end{split}
    $$
    

### TODO -- Question 3 {.answer #answer-mi-3}
Montrons tout d'abord que la fonction $f:Y \to \R$ est mesurable 
si et seulement si $f \circ h$ est mesurable. Par définition,
$f$ est mesurable si pour tout ensemble borélien $B$ de $\R$,
l'ensemble $f^{-1}(B)$ appartient $\mathcal{B}$, c'est-à-dire
si et seulement si
$$
h^{-1} (f^{-1}(B)) = (f \circ h)^{-1}(B) \in \mathcal{A},
$$
c'est-à-dire si et seulement si $f \circ h$ est mesurable.

Une fonction $f: Y \to \R$ est positive, mesurable et étagée 
(appartient à $\mathcal{F}_Y$) si et seulement si elle est 
de la forme
$$
f = \sum_{k=1}^n y_k \times 1_{B_k} \; \mbox{ et } \; y_k \geq 0, \, B_k \in \mathcal{B},
$$
On a donc, pour toute fonction mesurable et positive $f: Y \to \R$,
$$
\int_Y f (h_*\mu) 
= 
\sup 
\left\{
\sum_{k=1}^n y_k \times (\mu \circ h^{-1})(B_k) 
\, \left| \vphantom{\sum} \right. \, 
\sum_{k=1}^n y_k \times 1_{B_k} \leq f, \, y_k \geq 0, \, B_k \in \mathcal{B}
\right\}.
$$
Or, si $A_k := h^{-1}(B_k)$, $A_k \in \mathcal{A}$ et
$$
\left(\sum_{k=1}^n y_k \times 1_{B_k}\right) \circ h = \sum_{k=1}^n y_k \times 1_{A_k}
\; \mbox{ et } \;
\sum_{k=1}^n y_k \times (\mu \circ h^{-1})(B_k) = \sum_{k=1}^n y_k \times \mu(A_k)
$$
La fonction $\sum_{k=1}^n y_k \times 1_{A_k}$ est donc étagée, mesurable, 
positive et inférieure à $f \circ h$. Si $f \circ h$ est intégrable, $f$ est
donc intégrable et 
$$
\int_Y f (\mu \circ h^{-1}) \leq \int_X (f\circ h) \mu.
$$
Par ailleurs, pour toute collection finie $A_k \in \mathcal{A}$, 
$k\in\{1,\dots, n\}$, si 
$$
\sum_{k=1}^n y_k \times 1_{A_k} \leq f \circ h 
$$

**TODO:** finir !

**TODO:** réécrire en utilisant le MCT, ou trouver la preuve à laquelle fait
référence Tao *sans* le MCT.

Complétion d'une tribu {.answer #answer-ct}
--------------------------------------------------------------------------------

Nous allons établir que la tribu engendrée par $\mathcal{A} \cup \mathcal{N}$
est l'ensemble
$$
\mathcal{B} = \{A \ds  N \; | \; A \in \mathcal{A}, N \in \mathcal{N}\}.
$$
Tout d'abord, comme tout $A \in \mathcal{A}$ et $N \in \mathcal{N}$ 
appartiennent à cette tribu engendrée, $A^c$ et $N^c$ également et donc
$(A \cap N^c) \cup (A^c \cap N) = A \ds N$ également. 
L'ensemble $\mathcal{B}$ est donc inclus dans la tribu engendrée par 
$\mathcal{A}$ et $\mathcal{N}$. Il suffit donc de montrer qu'il s'agit
bien d'une tribu pour pouvoir conclure qu'elle est la tribu engendrée
recherchée.

Il est clair que $\varnothing$ appartient à $\mathcal{B}$,
comme différence symétrique entre $\varnothing$ et $\varnothing$.
Si $B = A \ds N$ appartient à $\mathcal{B}$, alors
$$
B^c = ((A \cap N^c) \cup (A^c \cap N))^c = (A^c \cup N) \cap (A \cup N^c).
$$
Comme $B^c = X \cap B^c = (A \cup A^c) \cap B^c$, par distributivité on a
$$
\begin{split}
B^c &= (A \cap (A^c \cup N) \cap (A \cup N^c)) \cup (A^c \cap (A^c \cup N) \cap (A \cup N^c)) \\
&=(A \cap N) \cup (A^c \cap N^c) \\
&=((A^c) \cap N^c) \cup ((A^c)^c \cap N) \\
&= A^c \ds N
\end{split}
$$
et par conséquent $B^c \in \mathcal{B}$.

Si les $A_k$, $k \in \N$, appartiennent $\mathcal{A}$ et les 
$N_k$, $k \in \N$, appartiennent à $\mathcal{N}$, alors on pourra se
convaincre que
$$
(\cup_k A_k) \setminus (\cup_k N_k) 
\subset \cup_{k} (A_k \ds N_k)
\subset (\cup_k A_k) \cup (\cup_k N_k),
$$
ce qui prouve que 
$$
\cup_k (A_k \ds N_k) = (\cup_k A_k) \ds M 
\; \mbox{ avec } \;
M \subset N:= \cup_k N_k.
$$
Comme $N_k \subset B_k \in \mathcal{A}$ avec $\mu(B_k) =0$,
$$
N = \cup_k N_k \subset \cup_k B_k \in \mathcal{A},
$$
avec $\mu(\cup_k B_k) = 0$ par $\sigma$-additivité de $\mu$.
L'ensemble $N$ (et donc l'ensemble $M$) appartient donc à $\mathcal{N}$.
Comme $\cup_k A_k \in \mathcal{A}$, on en déduit que $\mathcal{B}$ est stable
par union dénombrable. Cet collection contient l'ensemble vide, est stable
par passage au complémentaire et par union dénombrable ; c'est donc une tribu.

Réferences
================================================================================