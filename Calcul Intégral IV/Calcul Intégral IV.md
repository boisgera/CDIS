% Calcul Intégral IV

<!-- LaTeX Macros -->
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}



Mesure de grandeurs
================================================================================

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
perd un propriété importante qui est implicitement attachée à toutes les
grandeurs que nous avons cité.

Ce problème sera mis en évidence par le résultat suivant :

### Paradoxe de Banach-Tarski {.theorem}
Il est possible de partitionner la sphère de rayon unitaire de $\R^3$ 
en un nombre fini d'ensembles[^how-many], qui, 
après rotations et translations, 
forment une partition de deux sphères disjointes de rayon unitaire.

[^how-many]: 6 morceaux dans la preuve originale de Banach et Tarski (1924),
un nombre abaissé à 5 par Robinson en 1947.

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
Une *mesure (positive)* $\mu$ sur un espace probabilisable $(X, \mathcal{A})$
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
Il existe une bonne raison pour adopter cette convention:

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