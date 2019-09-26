% Calcul Intégral IV

<!-- LaTeX Macros -->
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}

\newcommand{\ds}{\mathbin{\Delta}}

TODO -- Mesure de Lebesgue dans $\R^n$
================================================================================

Dans les volets précédents du "Calcul Intégral", 
nous avons défini le volume d'un pavé compact de $\R^n$ 
$$
P = [a_1, b_1] \times \dots \times [a_n, b_n]
$$
au moyen de la formule
$$
v(P) := (b_1  -a_1) \times \dots \times (b_n - a_n).
$$
L'intégrable de Henstock-Kurzweil nous permet de prolonger la fonction $v$ en 
une fonction définie pour tous les ensembles mesurables $A$ de $\R^n$,
par la relation
$$
v(A) = \int 1_A(x) dx
$$
si $1_A$ est intégrable et $v(A) = +\infty$ sinon.
Mais cette approche n'est pas totalement satisfaisante intellectuellement.
D'une part on peut considérer l'usage de l'intégrale comme un chemin
tortueux pour étendre $v$.
D'autre part on peut avoir l'impression
que cette approche -- qui ne permet pas de mesure le volume de tout
ensemble de $\R^n$ -- n'atteint pas totalement son objectif ;
cette limitation pourrait a être un artefact de la méthode choisie
plutôt qu'une limitation intrinsèque.
Dans cette section, nous allons donner une autre méthode, plus directe, 
due à Lebesgue et Carathéodory[^autz],
qui nous permettra de définir la mesure du volume de tout ensemble de $\R^n$.
Elle nous donnera également la raison pour laquelle
notre construction initiale du volume se limite à la collection
des ensembles qualifiés de "mesurables".

[^autz]: Henri Lebesgue (1875-1941) était un mathématicien français
et Constantin Carathéodory (1873-1950) un mathématicien grec entrenant
des liens étroits avec l'Allemagne. Ils font partie des fondateurs de 
la théorie abstraite de la mesure qui conduit à un renouveau de la théorie 
de l'intégration au début du XXème siècle.

Pour calculer le volume d'un sous-ensemble de $\R^n$, 
nous généralisons la méthode utilisée pour définir les ensembles négligeables 
(de volume nul) : nous considérons l'ensemble des collections dénombrables
de pavés recouvrant ce sous-ensemble et nous utilisons chacun des ces 
recouvrements pour produire une estimation (supérieure) du volume
de l'ensemble. Formellement :

### Mesure extérieure de Lebesgue {.definition #mel}
On appelle *mesure extérieure de Lebesgue* dans $\R^n$ la fonction
$$v^*: \mathcal{P}(\R^n) \to [0, +\infty],$$ 
qui a tout ensemble $A$ de $\R^n$ associe le nombre réel étendu positif
défini par
$$
v^*(A) 
= 
\inf 
\left\{
\sum_{k=0}^{+\infty} v(P_k)
\; \left| \vphantom{\bigcup_{k=0}^{+\infty}} \right. \; 
\mbox{$P_k$ pavé compact de $\R^n$,} \, A \subset \bigcup_{k=0}^{+\infty} P_k
\right\},
$$

Cette définition "raisonnable" ne satisfait toutefois pas les propriétés que
nous attendons (implicitement) d'un volume. Ce décalage est mise en évidence
par un résultat paradoxal de la théorie des ensembles dans $\R^3$ :

### Paradoxe de Banach-Tarski {.theorem}
Il est possible de partitionner une sphère de rayon un de $\R^3$ 
en un nombre fini d'ensembles, qui, 
après rotations et translations, 
forment une partition de deux sphères disjointes de rayon un.

--------------------------------------------------------------------------------


Si le résultat est qualifié de paradoxe, c'est qu'il nous semble intuitivement 
que le volume devrait être préservé par les les opérations subies par 
la sphère initiale. Or, le volume d'une sphère de rayon un et de deux 
sphères disjointes de même rayon diffère d'un facteur $2$ ...
Pour dépasser ce paradoxe, nous allons devoir examiner un par un les
résultats qui nous semblent évidents dans ce raisonnement.

Soient $A_1, \dots, A_p$ des ensembles disjoints et non vides
de $\R^3$ dont la réunion forme la sphère initiale $S_0 = A_1 \cup \dots\cup A_p$,
et tels que des ensembles disjoints $B_1, \dots, B_p$ 
qui s'en déduisent par rotation et translation, 
vérifient $S_1 \cup S_2 = B_1 \cup \dots \cup B_p$ où $S_1$ et $S_2$
sont les deux sphère finales.

Tout d'abord, on a bien
$$
v^*(S) = \frac{4\pi}{3} \; \mbox{ et } \; v^*(S_1 \cup S_2) = 2 \times \frac{4 \pi}{3},
$$
car les ensembles $S_0$, $S_1$ et $S_2$ considérés sont intégrables 
(au sens de l'intégrale de Henstock-Kurzweil)
et nous verrons ultérieurement que dans ce cas, la mesure extérieure
$v^*$ coïncide avec celle de $v$ qui exploite l'intégrable de Henstock-Kurzweil.
Un simple calcul intégral fournit alors le résultat.

On peut croire que le point critique dans notre définition est la préservation
de la valeur de $v^*(A)$ par translation et rotation ; s'il est facile d'établir
que lorsque $B$ se déduit de $A$ par une translation, alors $v^*(A) = v^*(B)$, 
on peut douter du résultat pour les rotations. 
Après tout, la définition de $v^*(A)$ fait appel
à des rectangles qui sont parallèles aux axes, une propriété qui n'est pas
conservée par rotation. 
Mais si le résultat n'est pas évident, il s'avère pourtant que
la mesure $v^*$ est bien invariante par
rotation (cf. [@Hun11, section 2.8]).

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
v^*\left(\bigcup_{k=0}^{+\infty} A_k\right)
= \sum_{k=0}^n v^*\left(A_k\right).
$$

Cette propriété est caractéristique des mesures extérieures :

### Mesure extérieure {.definition}
On appelle *mesure extérieure* sur l'ensemble $X$ toute application
$$v^* :\mathcal{P}(X) \to [0, +\infty]$$ telle que $\mu(\varnothing) = 0$
et qui soit *$\sigma$-subadditive* :
pour tout $A \subset X$ et $A_k \subset X$, $k \in \N$, 
$$
\mbox{si } \, A \subset \bigcup_{k=0}^{+\infty} A_k, \; 
\mbox{alors } \,
\mu^*\left(A\right)
\leq 
\sum_{k=0}^{+\infty} \mu^*\left(A_k\right).
$$

### {.post .remark} 
Alternativement, on peut caractériser une mesure extérieure par trois règles
au lieu de deux:

  1. $\mu^*(\varnothing) = 0$.

  2. Si $A \subset B$, alors $\mu^*(A) \subset \mu^*(B)$.

  3. $\mu^*\left(\cup_{k=0}^{+\infty}A_k\right) \leq \sum_{k=0}^{+\infty} \mu^*\left(A_k\right)$.

-----

Il existe un procédé général permettant de déduire d'une mesure extérieure
une application qui soit additive -- à condition d'accepter de réduire
son domaine de définition ; la fonction qui en résulte est non seulement
additive, mais même $\sigma$-additive. 

### Ensemble mesurable 
Soit $\mu^*$ une mesure extérieure sur l'ensemble $X$ ;
un ensemble $A \subset X$ est dit *$\mu^*$-mesurable* (au sens de Carathéodory) 
si pour tout $B \subset X$, on a 
$$
\mu^*(B) = \mu^*(B \cap A) + \mu^*(B \setminus A).
$$

### {.post}
Une façon alternative de voir les choses : si l'on note $\mu^*|_A$ 
la trace de $\mu^*$ sur un ensemble $A$ de $X$, définie pour tout
sous-ensemble $B$ de $X$ par
$$\mu^*|_A(B) = \mu^*(B \cap A),$$
alors l'ensemble $A$ est $\mu^*$ mesurable si et seulement si
$$
\mu^* = \mu^*|_A + \mu^*|_{A^c}.
$$

### Tribu {.definition}
Une *tribu* ou *$\sigma$-algèbre* $\mathcal{A}$ sur un ensemble $X$ est une 
collection d'ensembles de $X$ contenant l'ensemble vide et stable par passage 
au complémentaire et à l'union dénombrable :

  1. $\varnothing \in \mathcal{A}$.

  2. Si $A \in \mathcal{A}$, $A^c = X \setminus A \in \mathcal{A}$.

  3. Si pour tout $k \in \N$, $A_k \in \mathcal{A}$, alors
     $\cup_{k=0}^{+\infty} A_k \in \mathcal{A}.$

Un ensemble de $\mathcal{A}$ est dit *mesurable* ; 
l'ensemble $X$ muni de $\mathcal{A}$ est un *espace mesurable*.

### Mesure {.definition}
Une *mesure* $\mu$ sur un espace mesurable $(X, \mathcal{A})$
est une fonction 
$$
\mu: \mathcal{A} \to [0, +\infty]
$$ 
telle que $\mu(\varnothing)= 0$ et telle que pour toute suite
$A_k$, $k\in \N$, d'ensembles de $\mathcal{A}$ disjoints deux à deux, on ait
$$
\mu \left( \bigcup_{k=0}^{+\infty} A_k \right) = \sum_{k=0}^{+\infty} \mu(A_k) ;
$$
on dit que $\mu$ est *$\sigma$-additive*.
L'ensemble $X$ muni de $\mathcal{A}$ et $\mu$ est un *espace mesuré*.

### {.remark .post}
Notons qu'en prenant une suite de la forme 
$A_0, \dots, A_n, \varnothing, \varnothing, \dots$, 
on montre que pour toute
suite finie $A_0, \dots, A_n$ d'ensembles disjoints de $\mathcal{A}$, on a
$$
\mu \left( \bigcup_{k=0}^n A_k \right) = \sum_{k=0}^n \mu(A_k) ;
$$
la mesure $\mu$ est donc *additive*. En particulier, si $A, B \in \mathcal{A}$
et $A \subset B$, en exploitant ce résultat pour $A$ et $B \setminus A$, 
qui sont deux ensembles disjoints de $\mathcal{A}$, on établit que
$\mu(A) \subset \mu(B)$ ; $\mu$ est donc *croissante*[^mon].

[^mon]: on trouvera également dans la littérature, le terme de *monotone* pour 
désigner cette propriété.

### Mesure associée à une mesure extérieure {.theorem}
Soit $X$ un ensemble et $\mu^*$ une mesure extérieure sur $X$.
La collection $\mathcal{A}$ des ensembles $\mu^*$-mesurables de $X$
est une tribu sur $X$, et la restriction $\mu$ de $\mu^*$ à 
$\mathcal{A}$ est une mesure sur $X$.

### Démonstration {.proof}
Cf. [@Hun11, théorème 2.9, pp. 15-17].

### {.remark .ante}
La spécialisation de ce procédé au cas de la mesure extérieure de Lebesgue,
produit la mesure de Lebesgue.

### Mesure de Lebesgue {.theorem .definition}
La "[mesure extérieure de Lebesgue](#mel)" $v^*:\mathcal{P}(\R^n) \to [0, +\infty]$
précédemment définie est bien une mesure extérieure sur $\R^n$.
On appelle *tribu de Lebesgue* et on note $\mathcal{L}(\R^n)$ la collection 
des ensembles $v^*$-mesurables (au sens de Caratheodory) ; 
la mesure $v: \mathcal{L}(\R^n) \to [0, +\infty]$ qui lui est associée 
est appelée *mesure de Lebesgue sur $\R^n$*. 
La notation "$v$" pour cette mesure est dépourvue d'ambiguité car elle 
prolonge la fonction $v$ initialement définie sur les pavés compacts.

### Démonstration {.proof}
Il est évident que $v^*$ satisfait $v^*(\varnothing)=0$ (car le pavé
$[0,0]^n$ recouvre $\varnothing$ par exemple). Si $A \subset \R^n$
et $A_k \subset \R^n$, pour tout $\varepsilon > 0$, il existe des 
pavés compacts $P_{jk}$ tels que 
$$
A_k \subset \bigcup_{j=0}^{+\infty} P_{jk} 
\; \mbox{ et } \;
\sum_{j=0}^{+\infty} v(P_{jk}) - \frac{\varepsilon}{2^{k+1}} 
\leq v^*(A_k) \leq \sum_{j=0}^{+\infty} v(P_{jk}).
$$
Comme la famille des $\{P_{jk}\}_{jk}$ recouvre $A$, on a donc
$$
v^*(A) \leq \sum_{k=0}^{+\infty} \sum_{j=0}^{+\infty} v(P_{jk})
\leq 
\sum_{k=0}^{+\infty} \left(v^*(A_k) +\frac{\varepsilon}{2^k}\right)
= \left(\sum_{k=0}^{+\infty} v^*(A_k)\right) +\varepsilon.
$$
Le réel positif $\varepsilon$ étant arbitrairement petit, on en déduit
que $v^*$ est bien $\sigma$-subadditive.

Nous renvoyons le lecteur intéressé par la preuve que la mesure de Lebesgue
prolonge bien la mesure de volume des pavés compacts à [@Hun11, section 2.2].

### {.remark .ante} 
On admettra sans preuve le résultat suivant :

### Mesure de Lebesgue et intégrale de Henstock-Kurzweil
La tribu $\mathcal{L}(\R^n)$ coïncide avec la tribu des ensembles mesurables 
définis au moyen de l'intégrale de Henstock-Kurzweil. La mesure de Lebesgue
$v: \mathcal{L}(\R^n) \to [0, +\infty]$ vérifie
$$
v(A) = \int 1_A(x) \, dx
$$ 
si $1_A$ est intégrable au sens de Henstock-Kurzweil et
$v(A)= +\infty$ sinon.

<!--
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
-->

Mesure et intégrale
================================================================================

### Tribu engendrée par une collection {.definition}
Dans un ensemble $X$, on appelle *tribu engendrée* par une collection 
$\mathcal{C}$ d'ensembles de $X$ la plus petite tribu 
(au sens de l'inclusion) 
$\mathcal{A} = \sigma(\mathcal{C})$ de $X$ contenant $\mathcal{C}$.

### Démonstration de l'existence de la tribu engendrée {.proof}
Désignons par $\mathfrak{S}$ la (meta-)collection des tribus de 
$X$ incluant $\mathcal{C}$ (contenant $\mathcal{C}$ comme sous-ensemble). 
$$
\mathfrak{S}
=
\{
\mbox{$\mathcal{B}$ tribu de $X$} \; | \; \mathcal{C} \subset \mathcal{B} 
\}
$$
Elle n'est pas vide : elle contient la collection $\mathcal{P}(X)$
des ensembles de $X$ (qui de toute évidence est un sur-ensemble de $\mathcal{C}$
et une tribu de $X$). Montrons que la plus petite tribu $\sigma(\mathcal{C})$
de $X$ contenant $\mathcal{C}$ est l'intersection de $\mathfrak{S}$
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

<!--
### Tribu de Lebesgue {.definition}
On appelle *tribu de Lebesgue* sur $\R^n$ la tribu composée des ensembles $E$
tels que pour tout pavé $P$ de $\R^n$, la fonction caractéristique 
de $E \cap P$ soit intégrable (au sens de Henstock-Kurzweil).

### {.post}
La tribu de Lebesgue est donc composée des ensembles mesurables au sens
du chapitre "Calcul Intégral III".

### TODO -- Référence
Lier au chapitre "Calcul Intégral III" en détail.
-->

### Tribu de Borel {.definition}
On appelle *tribu de Borel* d'un espace topologique $X$ la plus petite tribu
contenant tous les fermés (ou tous les ouverts) de $X$.

### Mesure {.definition}
Une *mesure (positive)* $\mu$ sur un espace mesurable $(X, \mathcal{A})$
est une fonction de $\mathcal{A}$ dans $[0, +\infty]$ telle que $\mu(\varnothing)= 0$
et pour toute collection dénombrable $\{A_k\}$ d'ensembles de
$\mathcal{A}$ disjoints deux à deux, on ait
$$
\mu \left( \bigcup_{k} A_k \right) = \sum_{k} \mu(A_k) ;
$$
on dit que $\mu$ est *$\sigma$-additive*.
L'ensemble $X$ muni de $\mathcal{A}$ et $\mu$ est un *espace mesuré*.

<!--
### TODO -- Pb
Gérer "pb" des fonctions à valeurs étendues ? Non, il n'y en a pas ...
-->


### Fonction mesurable
Une fonction $f: X \to Y$ associée aux espaces mesurables $(X, \mathcal{A})$
et $(Y,\mathcal{B})$ est *mesurable* 
(ou *$\mathcal{A}/\mathcal{B}$-mesurable*)
si l'image réciproque $A =f^{-1}(B)$
de tout ensemble $B$ de $\mathcal{B}$ par $f$ appartient à $\mathcal{A}$.

### Conventions
Lorsque $Y$ a une structure topologique, on supposera par défaut que la 
tribu associée est la tribu de Borel, et lorsque $X = \R^n$ 
que la tribu associée est la tribu de Lebesgue. 
Lorsque l'on souhaitera munir également $X$ de la tribu de Borel,
on parlera de fonctions *borélienne* (tribu de Borel au départ et à l'arrivée).
Il existe une bonne raison pour adopter cette convention :

### Mesurable ou mesurable ?
Une fonction $f:\R^n \to \R^m$ est limite simple de fonctions intégrables 
au sens de Henstock-Kurzweil 
-- c'est-à-dire "mesurable" au sens de ["Calcul Intégral III"](Calcul Intégral III.pdf) --
si et seulement si elle est $\mathcal{L}(\R^n)/\mathcal{B}(\R^m)$-mesurable.

### TODO -- Démonstration {.proof}
La fonction $f:\R^n \to \R^m$ est limite simple de fonctions intégrables 
au sens de Henstock-Kurzweil si et seulement si elle vérifie 
le critère de l'image réciproque des sections II et III, 
c'est-à-dire si l'image réciproque de tout ouvert de $\R^m$ est un
ensemble $\mathcal{L}(\R^n)$-mesurable.
C'est de toute évidence le cas si $f$ est 
$\mathcal{L}(\R^n)/\mathcal{B}(\R^m)$-mesurable.
Réciproquement, si l'image réciproque de tout ouvert de $\R^m$ est un
ensemble $\mathcal{L}(\R^n)$-mesurable.

### TODO : limite simple de fonctions mesurable est mesurable

### TODO: composition de fcts mesurables
Intérêt de fcts boréliennes dans ce schéma, lien avec Calcul Intégral III
(généralisation résultats composition)

### Fonction étagée {.definition}
On appelle *fonction étagée* toute fonction $f: X \to Y$ telle que
l'image réciproque de $Y$ par $f$ soit finie (telle que $f$ ne
prenne qu'un nombre fini de valeurs).

### TODO

Examiner de plus près gestion valeurs infinies

### Fonction mesurable
Une fonction $f: X \to [-\infty, +\infty]$ associée aux espaces mesurables 
$(X, \mathcal{A})$
et $(\R,\mathcal{B}(\R))$ est *mesurable* si et seulement si $f$ est la limite
simple de fonctions étagées $X \to \R$ mesurables.

### TODO -- Démonstration {.proof}

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
Soit $\mathcal{F}(f)$ la collection des fonctions étagées positives et mesurables
inférieures à $f$.
On appelle *intégrale de Lebesgue de $f$ relativement à la mesure $\mu$*
la grandeur positive (finie ou infinie)
$$
\int_X f \mu := \int_X f(x) \mu(dx) := \sup_{g \in \mathcal{F}(f)} \int_X g \mu.
$$

### TODO
Passer du sup à la limite des intégrales d'une suite croissante de 
fonctions simples et mesurables. D'autant plus nécessaire que dans
la définition avec le sup, on ne voit pas très bien pourquoi il faut
supposer que la fonction $f$ elle-même est mesurable.
Rq qqpart plus bas que si l'on veut que le procédé marche pour
toute suite $\varepsilon_k$, alors il est *nécessaire* que 
$f$ soit mesurable.

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

Propriétés de l'intégrale
================================================================================

### TODO -- Linéarité {.theorem #lin}

### TODO -- Démonstration {.proof}

### TODO -- Positivité {.theorem #pos}

### TODO -- Démonstration {.proof}

### Théorème de convergence monotone {.theorem #TCM}
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré et
$f_k: X \to [0, +\infty]$, $k \in \N$ une suite croissante de fonctions 
mesurables et positives ; pour tout $x \in X$,
$$
0 \leq f_0(x) \leq \dots \leq f_{k}(x) \leq f_{k+1}(x) \leq \cdots
$$
La limite simple $f: X \to [0, +\infty]$ des $f_k$,
telle que pour tout $x \in X$,
$$
f_k(x) \to f(x) \mbox{ quand } k \to +\infty,
$$
est mesurable et
$$
\lim_{k \to +\infty} \int f_k(x) \, \mu(dx) = \int f(x) \, \mu(dx).
$$

### Démonstration {.proof}
La fonction $f$ est mesurable comme limite simple de fonctions mesurables.
La positivité de l'intégrale entraîne
$$
\int f_0 \mu \leq \dots \leq \int f_k \mu \leq \dots \int f_k \mu \leq \int f \mu.
$$
et donc
$$
\lim_{k\to+\infty} \int f_k\mu \leq \int f\mu.
$$

Soit $g: X \to \left[0, +\infty\right[$ une fonction étagée mesurable, donc
de la forme
$$
g(x) = \sum_{j=0}^p c_j 1_{E_j}
$$
avec $c_k \in \left[0, +\infty\right[$ et $E_k$ mesurable.
Soit $t \in \left[0, 1\right[$. Comme la suite des $f_k$ est croissante et 
converge simplement vers $f$, les ensembles
$A_k = \{x \in X \; | \; f_k(x) \geq t g(x) \}$
vérifient
$$
A_0 \subset \cdots \subset A_k \subset \cdots 
\; \mbox{ et } \;
\bigcup_{k=0}^{+\infty} A_k = X.
$$
Les $f_k$ et $g$ étant mesurables, les ensembles $A_k$ sont mesurables.
On a 
$$
\int f_k \mu \geq \int g 1_{A_k} = t\sum_{j=0}^p c_k \mu(A_k \cap E_j).
$$
et comme $\cup_{k=0}^{+\infty} A_k \cap E_j = E_j$, par $\sigma$-additivité
de $\mu$,
$$
\lim_{k\to +\infty} \int f_k \mu \geq 
t\lim_{k\to +\infty} \sum_{j=0}^p c_k \mu(A_k \cap E_j) = 
t \left(\sum_{j=0}^p c_k \mu(E_j)\right) = t \int g\mu. 
$$
Cette inégalité étant valable pour tout $t \in \left[0, 1\right[$
et pour toute fonction positive étagée et mesurable $g$, on en déduit
$$
\lim_{k\to +\infty} \int f_k \mu \geq \sup_{g \in \mathcal{F}(f)}\int g\mu
= \int f\mu.
$$

### {.remark .ante}
[Le théorème de convergence monotone](#TCM) fournit une alternative concrète
à la construction initiale de l'intégrale.

### Intégrale d'une fonction positive II {.theorem}
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré et 
$f: X \mapsto [0, +\infty]$ une fonction mesurable.
Soit $\varepsilon_k \geq 0$ une suite de valeurs telles que
$$
\lim_{k\to +\infty} \varepsilon_k  = 0 
\; \mbox{ et } \;
\sum_{k=0}^{+\infty} \varepsilon_k = +\infty.
$$
La suite des fonctions $f_k$ définies par $f_0=0$, puis
$$
f_{k+1} = f_{k} + \varepsilon_k 1_{E_k} \, \mbox{ où } \,
E_k = \{x \in X \, | \, f(x) \geq f_k(x) + \varepsilon_k\}
$$
est une suite croissante de fonctions étagées positives et mesurables, 
convergeant simplement vers $f$ et 
$$
\int f(x) \mu(dx) = \lim_{k\to +\infty} \int f_k(x) \mu(dx). 
$$

### TODO -- Démonstration {.proof}


### Théorème de convergence dominée {.theorem #TCD}
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré et
$f_k: X \to [-\infty, +\infty]$, $k \in \N$, une suite de fonctions 
mesurables, dominées par la fonction intégrable $g: X \to [-\infty, +\infty]$
c'est-à-dire telles que pour tout tout $k \in \N$ et tout $x \in X$,
$$
|f_k(x)| \leq g(x) \; \mbox{ et } \; \int g(x) \, \mu(dx) < +\infty.
$$
Si la suite des $f_k$ à une limite simple $f: X \to [0, +\infty]$
c'est-à-dire si pour tout $x \in X$,
$$
f_k(x) \to f(x) \mbox{ quand } k \to +\infty,
$$
alors
$$
\lim_{k \to +\infty} \int f_k(x) \, \mu(dx) = \int f(x) \, \mu(dx).
$$

### TODO -- Démonstration {.proof}

Produit de mesures
================================================================================

### Tribu produit
Soit $(X ,\mathcal{A})$ et $(Y, \mathcal{B})$ deux espaces mesurables.
On appelle *tribu produit* de $\mathcal{A}$ et $\mathcal{B}$ 
et l'on note $\mathcal{A} \otimes \mathcal{B}$
la tribu sur le produit cartésien $X \times Y$ engendrée par les
ensembles de la forme $A \times B$ où $A \in \mathcal{A}$ et
$B \in \mathcal{B}$.
$$
\mathcal{A} \otimes \mathcal{B} := 
\sigma 
\left( 
\left\{ A \times B \; | \; A \in \mathcal{A}, \; B \in \mathcal{B} \right\}
\right).
$$

### Mesure produit
Soient $(X, \mathcal{A}, \mu)$ et $(Y, \mathcal{B}, \nu)$ deux espace mesurés.
On appelle *mesure produit* de $\mu$ et $\nu$ et l'on note 
$\mu \otimes \nu$ la fonction définie sur $\mathcal{A} \otimes \mathcal{B}$
par
$$
(\mu \otimes \nu) (C) = \inf
\left\{ 
\sum_{k=0}^{+\infty} \mu(A_k) \nu(B_k) 
\; \left| \vphantom{\sum_{k=0}^{+\infty}} \right. \;
A_k \in \mathcal{A}, \ B_k \in \mathcal{B}, \, C \subset \bigcup_{k=0}^{+\infty} A_k \times B_k \right\}
$$

### TODO -- Démonstration : la "mesure produit" est une mesure {.proof}

  - introduire $(\mu \otimes \nu)^* (C)$ pour tout $C$, montrer qu'on a 
    affaire à une mesure extérieure.

  - montrer que tout ensemble de $\mathcal{A} \otimes \mathcal{B}$ et 
    $(\mu \otimes \nu)^*$-mesurable (suffit de montrer que $A \times B$
    est $(\mu \otimes \nu)^*$-mesurable).
    

### Intégrale dans un espace produit {.notation}
Soient $(X, \mathcal{A}, \mu)$ et $(Y, \mathcal{B}, \nu)$ deux espace mesurés.
Pour toute fonction $\mu \otimes \nu$-mesurable 
$f: X \times Y \to [0, +\infty]$ ou toute fonction intégrable
$f: X \times Y \to \R$, on notera
$$
\int f(x, y) \mu(dx)\nu(dy) := 
\int f (\mu \otimes \nu).
$$

### TODO -- Mesure $\sigma$-finie (plus tôt ? Bof.)

### TODO -- remark
Gérer la subtilité que la première intégrale est définie uniquement
presque partout, ce qui suffit à montrer que la seconde est définie
(à détailler aussi en amont).

### Théorème de Fubini {.theorem #fubini}
Soit $(X, \mathcal{A}, \mu)$ et $(Y, \mathcal{B}, \nu)$ deux espaces
mesurés $\sigma$-finis. Une fonction mesurable $f: X \times Y \to \R$
est intégrable si et seulement l'intégrale itérée
$$
\int_Y \left(\int_X |f(x, y)| \mu(dx) \right) \nu(dy)
$$
est finie. Dans ce cas,
$$
\int_{X \times Y} f \, (\mu \otimes \nu)
=
\int_{X \times Y} f(x, y) \mu(dx)\nu(dy)
=
\int_Y \left(\int_X |f(x, y)| \mu(dx) \right) \nu(dy).
$$

### TODO -- Complétion
Etudier <https://www.math.fsu.edu/~roberlin/maa5616.f15/homework9sln.pdf>

Aussi, <https://terrytao.wordpress.com/2010/10/30/245a-notes-6-outer-measures-pre-measures-and-product-measures/>

### TODO -- remarque 
remarque évidente sur l'autre intégrale itérée.

### Démonstration {.proof}



Exercices
================================================================================

Anagrame {.question #BT}
--------------------------------------------------------------------------------

Quel est l'anagrame de "Banach-Tarski" ?

Approximation par des ensembles mesurables
--------------------------------------------------------------------------------

Soit $A$ un sous-ensemble de $\R^n$.

### Question 1 {.question #enm-1}
Montrer qu'il existe un ensemble $v^*$-mesurable $B$ contenant $A$ et tel que
$v^*(A) = v^*(B)$.

### Question 2 {.question #enm-2}
A quelle condition portant sur $v^*(B \setminus A)$ l'ensemble $A$ est-il 
$v^*$-mesurable ?

Mesure intérieure
--------------------------------------------------------------------------------

Soit $A$ un ensemble borné de $\R^n$ et $P$ un pavé compact de $\R^n$
contenant $A$.
On appelle *mesure intérieure de $A$* la grandeur
$$
v_*(A) = v^*(P) - v^*(P \setminus A).
$$

### Question 1 {.question #mi-1}
Montrer que la définition de $v_*(A)$ ne dépend pas du choix du pavé $P$.

### Question 2 {.question #mi-2}
Montrer que $v_*(A) \leq v^*(A)$, avec égalité si $A$ est $v^*$-mesurable.

### Question 3 {.question #mi-3}
Montrer la réciproque de la question précédente : si $A \subset \R^n$ est borné
et $v_*(A) = v^*(A)$, alors $A$ est $v^*$-mesurable.

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


Complétion d'une mesure
--------------------------------------------------------------------------------

Soit $(X, \mathcal{A}, \mu)$ un espace mesuré. 
On note $A \ds B$ la différence symétrique
de deux sous-ensembles $A$ et $B$ de $X$ l'ensemble, 
définie par
$$
A \ds B = (A \setminus B) \cup (B \setminus A) = (A \cap B^c) \cup (A^c \cap B).
$$

### Question 1 {.question #cm-1}
Caractériser au moyen de la différence symétrique $\ds$ 
la tribu -- notée $\overline{\mathcal{A}}$ -- engendrée par 
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

### Question 2 {.question #cm-2}
Montrer que la mesure $\mu$ peut être étendue d'une façon unique en une
mesure $\overline{\mu}$ définie sur $\overline{\mathcal{A}}$.


TODO -- Fonctions mesurables
--------------------------------------------------------------------------------

(pour des mesures "exotiques" ... mesure de comptage, densité uniforme,
sur $[0, 1]$, mesure de dirac en $0$ ?)

TODO -- Mesures de Hausdorff
--------------------------------------------------------------------------------

Que faire ? Définir le volume, la surface et la longueur dans $\R^3$, 
montrer que l'on a affaire à des mesures extérieures ?

Travailler sur une mesure de Hausdorff "rectangulaire" plutôt que sur 
la "vraie" ?

Ou mesure de Hausdorff de dimension 1/2 dans $\R$, telle que présentée
dans <https://terrytao.wordpress.com/2009/05/19/245c-notes-5-hausdorff-dimension-optional/> ?

TODO -- Extension
--------------------------------------------------------------------------------

Tribu générée à partir d'un anneau (e.g. ens. des intervalles $\left[a,b\right[$),
extension d'une prémesure ? Problématique de non-unicité ? Unicité sous
caractère $\sigma$-fini ? cf <https://mpaldridge.github.io/teaching/ma40042-notes-06.pdf> 


TODO -- Mesure produit
--------------------------------------------------------------------------------

### Question 1 
Montrer que $\mathcal{B}(\R^{m+n}) = \mathcal{B}(\R^m) \otimes \mathcal{B}(\R^n)$.

### Question 2
Est-ce que $\mathcal{L}(\R^{m+n}) = \mathcal{L}(\R^m) \otimes \mathcal{L}(\R^n)$ ?


TODO -- Intégrale itérée
--------------------------------------------------------------------------------

Exemple classique (e.g. <https://en.wikipedia.org/wiki/Fubini's_theorem#Failure_of_Fubini's_theorem_for_non-integrable_functions>)
de calcul et comparaison de 
$$
\int_0^1 \left( \int_0^1 \frac{x^2 - y^2}{(x^2 + y^2)^2}\, dy\right) \, dx
$$
et
$$
\int_0^1 \left( \int_0^1 \frac{x^2 - y^2}{(x^2 + y^2)^2}\, dx\right) \, dy.
$$

### TODO 
check / version conditionnellement continue de Fubini. 
Pourquoi ça ne marche pas ?


Solutions
================================================================================

Anagrame {.answer #answer-BT}
--------------------------------------------------------------------------------

"Banach-Tarski Banach-Tarski".

Approximation par des ensembles mesurables {#aem}
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-enm-1}
Par définition de $v^*(A)$, pour tout $j \in \N$, il existe une collection
dénombrable de pavés $P^j_k$ tels que
$$
v^*(A) \leq \sum_{k=0}^{+\infty} v(P^j_k) \leq v^*(A) + 2^{-j}.
$$
Les ensembles $B_j = \cup_k P^j_k$ sont $v^*$-mesurables comme unions 
dénombrables d'ensembles mesurables. 
De plus, comme $A \subset B_j$, et par $\sigma$-subadditivité de $v^*$
$$
v^*(A) 
\leq v^*(B_j) 
\leq \sum_{k=0}^{+\infty} v^*(P^j_k)
\leq \sum_{k=0}^{+\infty} v(P^j_k) \leq v^*(A) + 2^{-j}.
$$
L'intersection $B = \cap_j B_j$ est un ensemble mesurable qui recouvre $A$ 
et est contenu dans chaque $B_j$ ; par conséquent pour tout $j \in \N$,
$$
v^*(A) \leq v(B) \leq v(B_j) \leq v^*(A) + 2^{-j}.
$$
On en déduit donc que $A \subset B$ et $v^*(A) = v^*(B)$ avec $B$ mesurable. 

### Question 2 {.answer #answer-enm-2}
Notons au préalable que si $v^*(A) = +\infty$, alors $A$ est automatiquement 
mesurable. Dans le cas contraire ($v^*(A) < +\infty$)
l'ensemble $A$ est $v^*$-mesurable si et seulement si $v^*(B \setminus A) = 0$.
En effet, si $A$ est $v^*$-mesurable et de mesure finie, comme $A \subset B$, on a 
$$
v^*(B) = v^*(A \cap B) + v^*(A^c \cap B) = v^*(A) + v^*(B \setminus A) = v^*(B) + v^*(B \setminus A).
$$
Comme la mesure $v^*(A)$ est finie, $v^*(B \setminus A) = 0$.
Réciproquement, si $v^*(B \setminus A) = 0$, alors $B \setminus A$ (et donc $A$)
est mesurable.
En effet, pour tout ensemble $C$ de $\R^n$, on a d'une part 
$$
v^*(C) \leq v^*((B \setminus A) \cap C) + v^*((B \setminus A)^c \cap C) 
$$
par subbadditivité de $v^*$.
D'autre part, comme $(B \setminus A) \cap C \subset B \setminus A$, 
$v^*((B \setminus A) \cap C) \leq v^*(B \setminus A) = 0$. 
Par ailleurs, $C \supset (B \setminus A)^c \cap C$, donc
$$
v^*(C) \geq v^*((B \setminus A)^c \cap C) = v^*((B \setminus A) \cap C) + v^*((B \setminus A)^c \cap C).
$$
On a donc l'égalité $v^*(C) = v^*((B \setminus A) \cap C) + v^*((B \setminus A)^c \cap C)$ ;
l'ensemble $B \setminus A$ est donc mesurable, ainsi que $A = B \setminus (B \setminus A)$.

Mesure intérieure
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-mi-1}
Pour montrer que la définition de $v_*(A)$ ne dépend pas du choix du pavé
$P$ contenant $A$, il suffit de prouver qu'on peut remplacer $P$ par un
pavé compact $P'$ contenant $P$ sans changer la valeur de $v_*(A)$ (pour toute
paire de pavés compacts on peut en effet trouver un pavé compact les contenant).

Comme les pavés compacts $P$ et $P'$ sont mesurables (au sens de Carathéodory,
pour la mesure extérieure $v^*$), l'ensemble $P' \setminus P$ l'est également 
; on a donc
$$
v^*(P') = v^*(P' \setminus P) + v^{*}(P) 
$$
et
$$
v^{*}(P' \setminus A)
=
v^*(P' \setminus P) + v^*(P \setminus A),
$$ 
ce qui établit
$$
v^*(P') - v{*}(P' \setminus A)
=
v^*(P) - v^{*}(P \setminus A).
$$

### Question 2 {.answer #answer-mi-2}
La fonction $v^*$ étant subadditive, on a
$$
v^*(P) \leq v^*(A) + v^*(P\setminus A)
$$
et donc $v_*(A) \leq v^*(A)$. Si $A$ est mesurable, l'inégalité initiale
devient une égalité et donc $v_*(A) = v^*(A)$. 

### Question 3 {.answer #answer-mi-3}
Montrons que la réciproque est également vraie. 
Soit $A$ un ensemble borné de $\R^n$ tel que 
$v_*(A) = v^*(A)$, et soit $B$ un ensemble quelconque de $\R^n$.
Nous cherchons à établir que $v^*(B) = v^*(A \cap B) + v^*(A^c \cap B)$.
Remarquons tout d'abord que si le pavé compact $P$ -- qui est mesurable -- 
contient $A$, on a
$$
v^*(B) = v^*(P \cap B) + v^*(P^c \cap B) \; ;
$$
si nous réussissons à établir que 
$$v^*(P \cap B) = v^*(A \cap (P \cap B)) + v^*(A^c \cap (P \cap B)),$$
on pourra alors conclure que
$$
\begin{split}
v^*(B) &= v^*(P \cap B) + v^*(P^c \cap B) \\
&= v^*(A \cap (P \cap B)) + v^*(A^c \cap (P \cap B)) + v^*(P^c \cap B) \\
&= v^*(A \cap B) + v^*(P \cap (A^c \cap B)) + v^*(P^c \cap (A^c \cap B)) \\
&= v^*(A \cap B) + v^*(A^c \cap B).
\end{split}
$$
Autrement dit, il nous suffit d'établir le résultat cherché quand $B$ est un
ensemble de $\R^n$ contenu dans le pavé compact $P$. 

Pour cela, nous exploitons les résultats de l'exercice "[Approximation par des
ensembles mesurables](#aem)". A l'ensemble $A$ on peut associer un sur-ensemble
$v^*$-mesurable $B$ tel que $v^*(A) = v^*(B)$ ; quitte à remplacer $B$ par
$P \cap B$, on peut également supposer que $B \subset P$. On a 
$$
v^*(P) = v^*(A) + v^*(P \setminus A) = v^*(B) + v^*(P \setminus B)
$$
et donc $v^*(P \setminus A) = v^*(P \setminus B)$. 
D'autre part
$$
\begin{split}
v^*(P) &= v^*(B) + v^*(P \setminus B) \\
&= v^*(A) + v^*(B \setminus A) + v^*(P \setminus B) \\
&= v^*(A) + v^*(B \setminus A) + v^*(P \setminus A) \\
\end{split}
$$
et donc $v^*(B \setminus A) = 0$. Par les résultats de l'exercice 
"[Approximation par des ensembles mesurables](#aem)", on en déduit que 
$A$ est mesurable.


Mesure image 
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

  - On a $\mu\circ h^{-1}(\varnothing) = \mu(h^{-1}(\varnothing)) = \mu(\varnothing) = 0$.

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
    
### Question 3 {.answer #answer-mi-3}
Montrons tout d'abord que la fonction $f:Y \to \R$ est mesurable 
si et seulement si $f \circ h$ est mesurable. Par définition,
$f$ est mesurable si pour tout ensemble borélien $B$ de $\R$,
l'ensemble $f^{-1}(B)$ appartient $\mathcal{B}$, c'est-à-dire
si et seulement si
$$
h^{-1} (f^{-1}(B)) = (f \circ h)^{-1}(B) \in \mathcal{A},
$$
c'est-à-dire si et seulement si $f \circ h$ est mesurable.

Comme $(f \circ h)_+ = f_+ \circ h$ et $(f \circ h)_- = f_- \circ h$,
il nous suffit de montrer que pour toute fonction mesurable
$f: Y \to \left[0, +\infty\right]$, on a
$$
\int (f \circ h) \mu = \int f (\mu \circ h^{-1})
$$
pour pouvoir conclure que $f: Y \to \R$ est $\mu \circ h^{-1}$-intégrable si et
seulement si $f \circ h$ est $\mu$-intégrable et que l'égalité ci-dessus
est valable.

Or pour une telle fonction $f$, il existe une suite croissante de fonctions 
$f_k$ simples, positives et mesurables convergeant simplement vers $f$,
et l'on a 
$$
\int f (\mu \circ h^{-1}) 
=
\lim_{k \to +\infty} \int f_k (\mu \circ h^{-1}).
$$
Comme 
$$
\begin{split}
\int f_k (\mu \circ h^{-1}) 
&= \sum_{y \in f_k(Y)} y \times (\mu \circ h^{-1})(f_k^{-1}(\{y\})) \\
&= \sum_{y \in f_k(Y)} y \times \mu (h^{-1}(f_k^{-1}(\{y\})) \\
&= \sum_{y \in f_k(Y)} y \times \mu ((f_k \circ h) ^{-1}(\{y\})) \\
\end{split}
$$
si $y \in f_k(Y)$, mais $y \not \in f_k(h(X))$, alors 
$\mu ((f_k \circ h) ^{-1}(\{y\})) = 0$. Par conséquent,
$$
\begin{split}
\int f_k (\mu \circ h^{-1}) 
&=
\sum_{y \in (f_k \circ h)(X)} y \times \mu ((f_k \circ h) ^{-1}(\{y\})) \\
&=
\int (f_k \circ h) \mu.
\end{split}
$$
Les fonctions $f_k \circ h$ sont simples, positives et mesurables,
leur suite est croissante et converge simplement vers $f \circ h$.
[Par le théorème de convergence monotone](#TCM), on a donc
$$
\int f (\mu \circ h^{-1}) 
=
\int (f \circ h) \mu.
$$



<!--
Une fonction $f: Y \to \R$ est positive, mesurable et étagée 
(appartient à $\mathcal{F}(f)$) si et seulement si elle est 
de la forme
$$
f = \sum_{k=0}^n y_k \times 1_{B_k} \; \mbox{ et } \; y_k \geq 0, \, B_k \in \mathcal{B},
$$
On a donc, pour toute fonction mesurable et positive $f: Y \to \R$,
$$
\int_Y f (h_*\mu) 
= 
\sup 
\left\{
\sum_{k=0}^n y_k \times (\mu \circ h^{-1})(B_k) 
\, \left| \vphantom{\sum} \right. \, 
\sum_{k=0}^n y_k \times 1_{B_k} \leq f, \, y_k \geq 0, \, B_k \in \mathcal{B}
\right\}.
$$
Or, si $A_k := h^{-1}(B_k)$, $A_k \in \mathcal{A}$ et
$$
\left(\sum_{k=0}^n y_k \times 1_{B_k}\right) \circ h = \sum_{k=0}^n y_k \times 1_{A_k}
\; \mbox{ et } \;
\sum_{k=0}^n y_k \times (\mu \circ h^{-1})(B_k) = \sum_{k=0}^n y_k \times \mu(A_k)
$$
La fonction $\sum_{k=0}^n y_k \times 1_{A_k}$ est donc étagée, mesurable, 
positive et inférieure à $f \circ h$. Si $f \circ h$ est intégrable, $f$ est
donc intégrable et 
$$
\int_Y f (\mu \circ h^{-1}) \leq \int_X (f\circ h) \mu.
$$
Par ailleurs, pour toute collection finie $A_k \in \mathcal{A}$, 
$k\in\{1,\dots, n\}$, si 
$$
\sum_{k=0}^n y_k \times 1_{A_k} \leq f \circ h 
$$

**TODO:** finir !

**TODO:** réécrire en utilisant le MCT, ou trouver la preuve à laquelle fait
référence Tao *sans* le MCT.
-->


Complétion d'une mesure
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-cm-1}
Nous allons établir que la tribu engendrée par $\mathcal{A} \cup \mathcal{N}$
est l'ensemble
$$
\mathcal{B} = \{A \ds  N \; | \; A \in \mathcal{A}, \, N \in \mathcal{N}\}.
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
B^c &= (A^c \cap A) \cup (A^c \cap N^c) \cup (N \cap A) \cup (N \cap N^c) \\
    &= (A^c \cap N^c) \cup (A \cap N) \\
    &= ((A^c) \cap N^c) \cup ((A^c)^c \cap N) \\
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

### Question 2 {.answer #answer-cm-2}

Supposons que $\overline{\mu}$ soit une mesure sur $\overline{\mathcal{A}}$
qui prolonge $\mu$.
Alors, nécessairement, pour tout ensemble $N \in \mathcal{N}$, on a
$\overline{\mu}(N) = 0$. En effet, il existe un $A \in \mathcal{A}$ tel que
$N \subset A$ et $\mu(A) = 0$, donc par croissance de $\overline{\mu}$,
$$
\overline{\mu}(N) \subset \overline{\mu}(A) = \mu(A) = 0.
$$
Soit alors $A \in \mathcal{A}$ et $N \in \mathcal{N}$. Les ensembles
$N_1 := A \cap N$ et $N_2 = A^c \cap N$ sont inclus dans $N$ et donc 
appartiennent à $\mathcal{N}$, par conséquent
$$
\overline{\mu}(A \ds N) = \overline{\mu}((A \setminus N_1) \cup N_2)
= \overline{\mu}(A) - \overline{\mu}(N_1) + \overline{\mu}(N_2)
= \overline{\mu}(A).
$$ 
Cette équation définit uniquement $\overline{\mu}$ ; 
il faut toutefois s'assurer que cette définition est cohérente, c'est-à-dire
que si $A \ds N = B \ds M$ où $A, B \in \mathcal{A}$ et $N, M \in \mathcal{N}$,
alors $\mu(A) = \mu(B)$. En utilisant l'associativité de $\ds$, on montre que
$$
A \ds (N \ds M) = (A \ds N) \ds M = (B \ds M) \ds M = B \ds (M \ds M) = B.
$$
Par conséquent, $N \ds M \in \mathcal{A}$, et comme $N \ds M \subset
N \cup M$, on en déduit que $\mu(N \ds M) = 0$, et donc
$$
\mu(B) = \mu(A) - \mu(A \cap (N \ds M)) + \mu(A^c \cap (N \ds M)) = \mu(A).
$$


Il est ensuite nécessaire de prouver que $\overline{\mu}$ est bien une mesure.
Soit $A_k \in \mathcal{A}$ et $N_k \in \mathcal{N}$ deux suites d'ensembles
tels que les $A_k \ds N_k$ soient deux à deux disjoints.
Soit $M_k$ un ensemble de $\mathcal{A}$ contenant $N_k$ et tel que
$\mu(M_k) = 0$. L'ensemble $B_k :=  A_k \setminus M_k$ appartient $\mathcal{A}$
et $\mu(B_k) = \mu(A_k)$ ; de plus, comme $B_k \subset A_k \ds N_k$, les
$B_k$ sont disjoints deux à deux. On a déjà vu à la question précédente que
$$
\overline{\mu}(\cup_k A_k \ds N_k)
= \overline{\mu}((\cup_k A_k) \ds N) \; \mbox{ où } \, N \in \mathcal{N},
$$
donc
$$
\begin{split}
\overline{\mu}(\cup_k A_k \ds N_k)
&= \mu(\cup_k A_k) = \mu(\cup_k B_k) \\
&= \sum_k \mu(B_k) = \sum_k \mu(A_k) = \sum_k \overline{\mu}(A_k \ds N_k).
\end{split}
$$
La fonction $\overline{\mu}$ est donc $\sigma$-additive.


<!--
Nous avons déjà évoqué le fait à la question précédente que si 
les $A_k$, $k \in \N$, appartiennent $\mathcal{A}$ et les 
$N_k$, $k \in \N$, appartiennent à $\mathcal{N}$, alors 
$$
\cup_k (A_k \ds N_k) = (\cup_k A_k) \ds N 
\; \mbox{ avec } \;
N \in \mathcal{N},
$$
donc
$$
\overline{\mu}(\cup_k (A_k \ds N_k)) = \overline{\mu}(\cup_k A_k).
$$ 

Si $A_0 \ds N_0$ et $A_1 \ds N_1$ sont disjoints, alors, comme l'intersection
est distributive via-à-vis de la différence symétrique
($A \cap (B \ds C) = (A\cap B) \ds (A \cap C)$), on a
$$
\begin{split}
\varnothing &= (A_0 \ds N_0) \cap (A_1 \ds N_1) \\
&=
(A_0 \cap A_1) \ds ((A_0 \cap N_1) \ds (N_0 \cap A_1) \ds (N_0 \cap N_1))\\
\end{split}
$$  
soit 
$$
A_0 \cap A_1 = M_1 :=  ((A_0 \cap N_1) \ds (N_0 \cap A_1) \ds (N_0 \cap N_1)) \in \mathcal{N}.
$$
Donc $A_0$ et $A_1 \ds M_1$ sont disjoints et 
$\overline{\mu}(A_1 \ds M_1) = \overline{\mu}(A_1)$. De proche en proche
on peut ainsi construire une suite d'ensembles négligeables $M_k$ tels
que les $A_k \ds M_k$ soient disjoints et $\cup_k A_k  = \cup_k A_k \ds M_k$.
Par conséquent,
$$
\overline{mu}(\cup_k A_k \ds N_k) = \mu(\cup_k A_k) = \overline{\mu} ...
$$
-->

Réferences
================================================================================