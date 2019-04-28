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
   

Théorèmes de Convergence
================================================================================

### Théorème de convergence dominée {#TCD .theorem}

Si une suite de fonctions intégrables $f_n:\mathbb{R} \to \mathbb{R}$
converge simplement vers la fonction $f$, c'est-à-dire si pour tout
$x \in \mathbb{R}^n$,
$$
\lim_{n \to +\infty} f_n(x) = f(x)
$$
et qu'il existe deux fonctions intégrables $g$ et $h$ encadrant la suite $f_n$,
c'est-à-dire telles que pour tout $n\in \mathbb{N}$ et pour tout 
$x \in \mathbb{R}$,
$$
g(x) \leq f_n(x) \leq h(x)
$$
alors la fonction $f$ est intégrable et 
$$
\int_{\mathbb{R}} f(t) \, dt 
=
\int_{\mathbb{R}} \lim_{n \to +\infty} f_n(t) \, dt
= 
\lim_{n \to +\infty} \int_{\mathbb{R}} f_n(t) \, dt.
$$

### TODO:

MCT, dérivation sous le signe somme (exercice ?)

Ensembles mesurables
================================================================================

Il existe un lien étroit entre la notions de longueur d'un ensemble de réels
et le calcul intégral. Nous savons par exemple que pour tout intervalle 
compact $E = [a, b]$, la longueur $b-a$ de l'intervalle peut être calculée
par l'intégrale de la fonction caractéristique de $E$:
$$
\ell(E) = \ell([a, b]):=  b - a  = \int_a^b \, dt = 
\int_{\mathbb{R}} \chi_{[a, b]}(t) \, dt =
\int_{\mathbb{R}} \chi_{E}(t) \, dt.
$$
Si $E$ est une collection finie d'intervalles disjoints $[a_i, b_i]$,
l'intégrale de $\chi_E$ vaut cette fois-ci $\sum_i b_i - a_i$, 
ce qui correspond toujours à la valeur "intuitive" de la longueur 
de l'ensemble. 

Il apparait donc légitime pour définir la longueur d'un sous-ensemble $E$
de $\mathbb{R}$ aussi général que possible[^loop] de $\mathbb{R}$ de prendre cette 
égalité comme une définition, ce qui suppose toutefois que la fonction 
caractéristique soit intégrable; on parle alors d'ensemble intégrable. 
Cette définition laisse toutefois de coté les ensembles "trop grands" 
pour être intégrables, mais par ailleurs parfaitement anodins, 
comme par exemple $\mathbb{R}$ tout entier ou l'ensemble des réels positifs. 
Nous préférons donc mettre l'accent sur la notion d'ensemble mesurable:

[^loop]: Oui il existe des ensembles dont on ne pas pas définir raisonnablement
la longueur, sauf à accepter un concept de longueur aux propriétés
très étranges. Non, cette situation ne résulte pas de la méthode de définition
de la longueur par l'intégrale; c'est au contraire une limitation intrinsèque
de la théorie de la mesure que nous étudierons plus en détail par la suite.
Et non, il n'existe aucun construction "facile" (constructive, explicite) 
d'ensemble qui ne soit pas mesurable (et c'est une chose que l'on peut prouver).

### Ensemble mesurable {.definition}

Un ensemble $E$ de $\mathbb{R}$ est *intégrable* si sa fonction 
caractéristique $\chi_E$ est intégrable; il est *mesurable*
si son intersection avec tout intervalle compact
$[a, b]$ de $\mathbb{R}$ est intégrable.
La (mesure de) *longueur* d'un ensemble $E$ mesurable est définie par
$$
\ell(E) := \int_{\mathbb{R}} \chi_E(t) \, dt
$$
si $E$ est intégrable et
$$
\ell(E) := +\infty
$$
dans le cas contraire ($E$ mesurable mais pas intégrable).

### TODO

Expliciter: intégrable = de longueur finie; mesurable = de longueur
finie ou infinie, mais *bien définie*.
Substituer "de longueur finie" à "intégrable" où est-ce que c'est
risquer des problèmes (la définition de la longueur comme mesure
extérieure ?).

On aurait alors de longueur finie, infinie ou non définie.
Et ensemble mesurable si la longueur est bien définie (finie ou infinie).
C'est sans doute le plus simple ... Revoir la copie.

Evoquer ensemble mesurable comme "localement intégrable" ? BOF.
"mesurable" = que l'on peut mesurer = dont on peut mesurer la longueur.

### TODO

Implicite à expliciter: intégrable implique mesurable (ok, ne nécessite
rien de fondamentalement nouveau, sauf à expliciter une ppté de restriction 
/ d'additivité dans le chapitre 1).

### TODO en exercice

Structure de $\delta$-ring pour les ensembles intégrables ?

### Propriétés élementaires des ensembles mesurables {.theorem}

 1. L'ensemble vide est mesurable.

 2. Le complémentaire d'un ensemble mesurable est mesurable.

 3. L'union d'une collection dénombrable[^dénom] d'ensembles mesurables
    est mesurable.

[^dénom]: fini ou bien strictement dénombrable, c'est-à-dire en bijection 
avec $\mathbb{N}$.

### Démonstration {.proof}

 1. La fonction caractéristique $\chi_{\varnothing}$ est identiquement 
    nulle; l'ensemble vide $\varnothing$ est donc intégrable et par
    conséquent mesurable.

 2. Si l'ensemble $E$ est mesurable et $F = \mathbb{R} \setminus E$,
    pour tout $[a, b]$, l'ensemble $E \cap [a, b]$ est intégrable.
    Par ailleurs, l'ensemble $[a, b]$ est intégrable. 
    Donc, comme
    $$
    \chi_{F \cap [a, b]} = \chi_{[a, b]} - \chi_{E \cap [a, b]},
    $$
    l'ensemble $F \cap [a, b]$ est intégrable;
    l'ensemble $F$ est donc mesurable.

 3. Si les $E_n$ forment une famille dénombrable d'ensemble mesurables,
    pour tout intervalle compact $[a, b]$, $E_n \cap [a, b]$ est 
    intégrable, c'est-à-dire que $\chi_{E_n \cap [a, b]}$ est intégrable.
    Comme $E \cap [a, b] = \cup_n E_n \cap [a, b]$, la suite des
    fonctions caractéristiques
    $\chi_{E_n \cap [a, b]}$ converge simplement vers 
    $\chi_{E \cap  [a, b]}$. Par ailleurs, pour tout $n$, on a
    $0 \leq \chi_{E_n \cap [a, b]} \leq \chi_{[a, b]}$, donc
    par le [théorème de convergence dominée](#TCD), 
    la fonction $\chi_{E \cap [a, b]}$ est intégrable. 
    Par conséquent, l'ensemble $\cup_n E_n$ est mesurable.


### TODO

terminologie $\sigma$-algèbre (ou tribu)

### Topologie et ensembles mesurables

Tout ensemble ouvert est mesurable.

### Démonstration {.proof}

Tout intervalle ouvert $I$ est mesurable. En effet, son intersection avec
un intervalle compact $[a, b]$ est un intervalle inclus dans $[a, b]$.
La fonction caractéristique associée est de la forme $\chi_{[c, d]}$,
ou en diffère au plus en deux points; dans tous les cas, elle est
intégrable.

Si maintenant $U$ est un ensemble ouvert ouvert, pour chaque point $x$ de $U$ 
on peut construire le plus grand intervalle ouvert $I_x$ contenant $x$ et inclus
dans $U$ (c'est l'union de tous les intervalles ouvert vérifiant ces
deux propriétés). Pour un couple $x$ et $y$ dans $U$, soit $I_x = I_y$,
soit $I_x$ et $I_y$ sont disjoints et l'union de tous les intervalles
$I_x$ est égale à $U$. Comme dans chaque $I_x$ on peut choisir
un nombre rationnel $y$ tel que $I_x = I_y$, cette union est dénombrable.
L'ouvert $U$ est donc une union dénombrable d'intervalles ouverts, qui
sont tous mesurables, il est donc mesurable.

### TODO

En amont (chap. I), énoncer que égale pp à intégrable est intégrale
(et intégrale de même valeur). Grpmh ça n'est pas ce que l'on utilise
excatement; la démo montre que ça marche si deux fonctions sont égales
à l'exception d'un ensemble "négligeable", au sens de "de mesure extérieure
de longueur nulle". L'exercice pertinent ici constiste donc à montrer qu'un
ensemble est négligeable ssi il est de longueur nulle. Un sens est évident
(négligeable $\to$ de longueur nulle) avec les résultats du chap précédent
(à énoncer: comparaison intégrale de deux fcts ident sauf sur un ensemble
négligeable)

**NOTA:** shunter cette section "complétude" en première approche ?
Je dois revoir la terminologie du chap précédent, l'usage du terme
"négligeable" n'est pas safe (veut dire autre chose). Ici tout ça
est identique, mais pas en général ...

NOTA: on a quand même assez pour prouver que la mesure est complète ?
Nope, pas encore. Ca plaide pout shunter ...

Réfléchir quand même aux 3 notions: de mesure extérieure nulle,
de mesure nulle et négligeable (dans un ens de mesure nulle).

### Ensembles de longueur nulle {.theorem}

Un ensemble est de longueur nulle si et seulement 
la mesure extérieure de sa longueur est nulle.

### Preuve {.proof}

Un sens pas évident (mesure nulle donne mesure ext nulle)... shunter ?
Je pensais partir sur une somme arbitrairement proche de l'intégrale,
mais pas de raison que l'ensemble d'intervalles associés recouvre
l'original.

Le sens mesure extérieure nulle donne mesure nulle est OK modulo
les bons énoncés dans le chapitre précédent.

### Complétude de la longueur {.corollary}

Un sous-ensemble d'un ensemble de longueur nulle est de longueur nulle.






--------------------------------------------------------------------------------

**TODO:** corollaires immédiats: difference mesurable, ensemble fermés
mesurables, etc. Largement en exercice ...

Fonctions mesurables
================================================================================

### Meta {.meta}
Dans la présentation, commencer par le théorème d'intégrabilité dominée,
son contraste avec le cas Riemann classique, sans utiliser le mot de
mesurabilité, puis en "extraire" la notion de mesurabilité.

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

### Mesurabilité sur un intervalle {.remark}
Nous nous limitons dans ce chapitre à l'étude des fonctions mesurables
définies sur $\mathbb{R}$. La notion peut être très facilement étendue
à une fonction $f$ définie sur un intervalle fermé $I$ de $\mathbb{R}$ de la
façon suivante: on dira que $f$ est mesurable si son prolongement par $0$
à l'extérieur de $I$ est mesurable. Nous laissons le soin au lecteur
de généraliser en conséquence les énoncés qui vont suivre.

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
l'exigence de régularité est forte -- être continue presque partout --
alors que dans le cas de l'intégrale de Henstock-Kurzweil, 
la régularité demandée -- la mesurabilité -- s'avère être une 
condition très peu contraignante[^note].

[^note]: A tel point que s'il l'on peut prouver l'existence d'une fonction
non-mesurable, sa "construction explicite" est impossible. Les fonctions
non-mesurables font partie des objets "intangibles" (cf. @Sch96) dont
l'existence est prédite par la théorie mais que l'on ne rencontre jamais 
par hasard ...

### Ante {.ante}
Plusieurs propriétés des fonctions mesurables se déduisent directement de
leur définition:

### Les fonctions intégrables sont mesurables

### Démonstration {.proof}
Si $f$ est une fonction mesurable, elle est la limite simple de la suite
constante égale à $f$.

### Les fonctions mesurables forment un espace vectoriel

### Démonstration {.proof}

Si $f$, $g$ sont mesurables et $\lambda$ est un nombre réel, 
il existe des suites $f_k$ et $g_k$ de fonctions intégrables
convergeant simplement vers $f$ et $g$ respectivement.
Les fonctions $f_k + g_k$ et $\lambda f_k$ sont intégrables
et convergent alors simplement vers $f+g$ et $\lambda f$ 
respectivement.


### TODO ?

Evoquer fct localement intégrable ? Quand on regarde la preuve ci-dessous,
on n'utilise pas autre chose ...

### Les fonctions continues (presque partout) sont mesurables

### Démonstration {.proof}

Soit $f:\mathbb{R} \to \mathbb{R}$ une fonction continue presque
partout. Pour tout entier $k$, la fonction $f_k$ égale à $f$ sur
l'intervalle $[-k, k]$ est intégrable (car Riemann-intégrable)
et la suite des $f_k$ converge simplement vers $f$, qui est
donc mesurable. 

### Images réciproques des fonctions mesurables {.theorem}

Une fonction $f:\mathbb{R} \mapsto \mathbb{R}^n$ est mesurable si et seulement
pour tout ouvert $U$ de $\mathbb{R}$, l'image réciproque de $U$ par $f$
$$
f^{-1}(U) = \{x \in \mathbb{R} \, | \, f(x) \in U\}
$$
est mesurable.

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

### Ante {.ante}

En se basant exclusivement sur ce critère de mesurabilité par 
les images réciproques (donc en comprenant temporairement 
"mesurable" comme "satisfaisant le critère de l'image réciproque"
en attendant la preuve de l'équivalence des deux propriétés), 
on peut montrer les résultats suivants:

### Stabilité par passage à la limite

Les limites simples de fonction mesurables sont mesurables.

### Démonstration {.proof}

Soit  $f_k: \mathbb{R} \to \mathbb{R}$ des fonctions vérifiant le critère
de l'image réciproque, 
telles que pour tout $x \in \mathbb{R}$, $f_k(x) \to f(x)$ quand $k \to +\infty$.
Montrons que $f$ vérifie également ce critère.
Il suffit pour cela de remarquer que comme $U$ est ouvert et que
$f_k(x) \to f(x)$, $f(x) \in U$ si et seulement si $f_k(x) \in U$
pour $k$ assez grand. Cette déclaration se traduit par la formule
$$
f^{-1}(U) = \bigcup_{j=1}^{+\infty} \bigcap_{k = j}^{+\infty} f_k^{-1}(U)
$$
qui établit que $f^{-1}(U)$ est un ensemble mesurable, comme union 
(dénombrable) d'intersections (dénombrable) d'ensembles mesurables.

### Fonctions presque partout égales {.theorem}

Toute fonction égale presque partout à une fonction mesurable est
mesurable.

### Démonstration {.proof}

Toute fonction $f$ égale presque partout à une fonction $g$ qui vérifie 
le critère de l'image réciproque vérifie également le critère de l'image
réciproque. En effet, si pour
tout ouvert $U$ l'ensemble $g^{-1}(U)$ est mesurable, alors
$$
f^{-1}(U) = (g^{-1}(U) \setminus E) \cup F
$$
où $E$ et $F$ sont de mesure nulle (et donc mesurables puisque la mesure
de Lebesgue est complète);
par conséquent, $f^{-1}(U)$ est mesurable.

**TODO:** des pptés des ensembles mesurables sont utilisés dans la preuve
ci-dessous, repenser l'ordre ? J'aimerais pourtant retard l'apparition 
des ensembles mesurables, ne pas focaliser trop tôt. Sinon, réécrire
la preuve dans le langage des fonctions ? Urk, pas de choix parfait ici ...
Vérifier au passage que je n'utilise pas à travers les ensembles mesurables
de pptés que je n'ai pas encore démontré qui nécessité le critère par les
images réciproques. Même chose au-dessus .... jeez.
Arf, le nouvel ordre pose pb; j'ai de toute évidence bien besoin
des ensembles mesurables pour L'ENONCE du critère de l'image réciproque,
dont j'ai bien besoin au moins d'UN BOUT des ensembles mesurables ...
Décider de l'approche donc pour ces ensembles (fonction carac localement 
intégrable ou mesurable ?)


### Démonstration {.proof}

#### Sens direct

Supposons le critère des images réciproques satisfait. 
La démonstration repose sur la construction explicite d'une suite $f_k(x)$ 
de fonctions intégrables qui soient étagées, c'est-à-dire ne prenant qu'un
nombre fini de valeurs possibles.

Définissons $f_0(x) = 0$ et $f_k(x)$ par la relation de récurrence
$$
f_{k+1}(x) = f_k(x) + 
\left|
\begin{array}{rl}
-1/k & \mbox{si } \, f(x) < f_k(x) -1/k \, \mbox{ et } \, |x| \leq k,\\
+1/k  & \mbox{si } \, f_k(x) + 1/k < f(x)  \, \mbox{ et } \, |x| \leq k, \\
0 & \mbox{sinon.}
\end{array}
\right.
$$
Par construction, si $f(x)=0$, $f_k(x)= 0$. Si $f(x) > 0$, les $f_k(x)$
forment une suite croissante convergeant vers $f(x)$, car la suite des
$1/k$ tend vers $0$ quand $k$ tend vers $+\infty$, mais leur somme est 
divergente. La situation est similaire si $f(x) < 0$, mais avec une
suite $f_k(x)$ décroissante.

Montrons que la suite des $f_k$ est intégrable, ce qui concluera cette 
section de la preuve.
L'ensemble des valeurs $\{\alpha_j\}$ que prend chaque $f_k$ est bien fini;
il comprend la valeurs $\alpha_0 = 0$ et la fonction 
peut s'écrire sous la forme
$$
f_k = \sum_{j} \alpha_j \chi_{A_j}
$$
où les $A_j = f_k^{-1}(\alpha_j)$ sont en nombre fini et disjoints.
A part $A_0$, les $A_j$ sont également bornés, 
car $f_k$ est nulle en dehors de $[-k, k]$.
Montrons qu'à tout rang $k$, les ensembles $A_j$ sont mesurables, 
ce qui prouvera que chaque $f_k$ est intégrable par le critère d'intégrabilité
dominé.
C'est évident au rang $0$ où 
$\{\alpha_j\} = \{0\}$, et la collection des $A_j$ se réduit à 
$\{A_0\} = \{\mathbb{R}\}$;
supposons cette propriété valable au rang $k$. 
L'ensemble $E$ des
réels $x$ tels que $f_k(x) + 1/k < f(x)$ et $|x| \leq k$
peut être écrit comme
$$
E = \left(\bigcup_j \{x \in \mathbb{R} \, | \, \alpha_j + 1/k < f(x)\} \cap A_j\right) \cap [-k, k],
$$
qui est mesurable. De même, on peut montrer que 
l'ensemble $F$ des
réels $x$ tels que $f(x) < f_k(x) - 1/k < f(x)$ et $|x| \leq k$ est mesurable.
On a alors par construction: 
$$
f_{k+1} = \sum_{j} \alpha_j \chi_{A_j} + \frac{1}{k} \chi_E - \frac{1}{k} \chi_F
$$
qui est sous la forme souhaitée, à ceci près que les ensembles intervenant
ne sont pas nécessairement disjoints. Mais pour toute valeur $y$ dans l'image
de $f_{k+1}$, l'image réciproque de $\{y\}$ par $f$ est nécessairement une
union (finie) d'intersections (finies) d'ensembles dans la collection 
$\{\dots, A_j, \dots, E, F\}$ et donc un ensemble mesurable. La fonction 
$f_{k+1}$ peut donc être mise sous la forme souhaitée.

#### Réciproque

Considérons désormais une fonction intégrable $f:\mathbb{R} \to \mathbb{R}$.
Par le [théorème de dérivation de l'annexe][Une intégrale indéterminée est dérivable presque partout],
si l'on définit la fonction $f_k(x)$ comme le taux d'accroissement
$$
f_k(x) :=  \frac{F(x + 2^{-k}) - F(x)}{2^{-k}}
\; \mbox{ où } \;
F: x \in \mathbb{R} \mapsto \int_0^x f(t) \, dt,
$$
alors $f_k(x) \to f(x)$ presque partout quand $k \to +\infty$.
Or chaque $f_k$ est continue, donc l'image réciproque de tout ouvert
par $f_k$ est un ensemble mesurable. Par les deux résultats établis dans
cette section, $f$ vérifie également ce critère.

Par définition, une fonction mesurable est limite simple
d'une suite de fonctions intégrables, et les fonctions intégrables 
vérifient le critère de l'image réciproque. 
Cette classe de fonctions étant [stable par passage à la limite][Stabilité par passage à la limite], 
ce critère est également satisfait pour toute fonction mesurable.


### Composition par une fonction continue {.theorem}

Soit $f:\mathbb{R} \to \mathbb{R}^n$ une fonction mesurable et 
$g:\mathbb{R}^n \to \mathbb{R}^m$ une fonction continue.
La composée $g \circ f$ de ces deux fonctions est mesurable.

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


**TODO:** adapter preuve ci-dessous, la preuve amont a été refaite,
le "patch" pour borner n'est plus nécessaire.

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

Fonctions Absolument Intégrables
================================================================================

### TODO

 remarque nécessaire ou exemples montrant que le critère 
d'intégrabilité dominée est en fait pratique quand on manipule des
fonction absolument intégrables et que les calculs manipulant des 
fonctions uniquement conditionnellement intégrables sont "fragiles".



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

Montrer qu'une fonction $f: \mathbb{R} \to \mathbb{R}$ est mesurable si et
seulement si pour tout nombre réel $a$, l'ensemble
$$
f^{-1}(\left]a, +\infty\right[) = \{x \in \mathbb{R} \, | \, a < f(x)\}
$$
est mesurable.

### Réponse

Compte tenu du [critère de l'image réciproque][Images réciproques des fonctions mesurables],
comme tous les ensembles $\left]a, +\infty\right[$ sont ouverts, 
le critère ci-dessus est bien vérifié pour toute fonction mesurable.

Montrons désormais la réciproque: supposons le critère ci-dessus vérifié et
montrons que le [critère de l'image réciproque][Images réciproques des fonctions mesurables]
l'est également.

Soit $U$ un ouvert de $\mathbb{R}$; l'ensemble $U$ peut être décomposé comme
union d'un nombre dénombrables d'intervalles ouverts bornés $I_k$
de $\mathbb{R}$.
Par conséquent, comme
$$
f^{-1}(U) = f^{-1} \left(\cup_k I_k \right) = \bigcup_{k} f^{-1}(I_k),
$$
il nous suffit de montrer que l'image réciproque de tout intervalle
ouvert borné $\left]a, b\right[$ par $f$ est mesurable, pour conclure
que $f^{-1}(U)$ est mesurable, comme union dénombrable d'ensembles
mesurables.

Or, un point $x$ vérifie $a < f(x) < b$ si et seulement
il vérifie $a < f(x)$ et ne vérifie $b-2^{-k} < f(x)$ pour aucun entier $k$,
ce qui se traduit par la relation ensembliste
$$
f^{-1}(\left]a, b\right[) 
= 
f^{-1}(\left]a, +\infty \right[) 
\cap 
\left(\mathbb{R} \setminus \bigcup_{k=0}^{+\infty} f^{-1}(\left]b -2^{-k}, +\infty \right[)\right).
$$
Les images réciproques au second membre sont mesurables par hypothèse,
et sont combinées par union dénombrable, complément relatif et union finie
par conséquent $f^{-1}(\left]a, b\right[)$ est également mesurable.


Fonctions Boréliennes
--------------------------------------------------------------------------------

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
