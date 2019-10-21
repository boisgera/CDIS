% Calcul Intégral V

<!-- LaTeX Macros -->
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}

Misc.
================================================================================

  - fcts définies dans $\R$, au moins dans un premier temps

Dérivées faibles
================================================================================

**Motivation:** étendre la notion de dérivation pour traiter des uses cases 
comme les équations différentielles avec second membre discontinu en $t$, 
sans "bricolage" (qui serait: résoudre portion par portion et recoller
par continuité, si l'on suppose que l'on est $C^1$ par morceaux).
Motivation analogue pour les probas: variable aléatoire à densité
uniforme sur $[0,1]$: $p$ n'est pas (partout) la dérivée de $F$.

Dans les deux cas néanmoins, on a le même schéma ou la "dérivée" 
permet d'obtenir la fct originale par intégration.
(pour les ODEs, pour travailler sur $\R$, prolonger rhs par $0$
pour $t\neq 0$ et $x(t)$ par $x_0$.)

Idée: dérivation initialement source de définition de l'intégrale (de Newton);
l'intégration est une opération inverse, mais sait aussi intégrer
des fonctions qui ne sont *pas* des dérivées (exemple).
On peut retourner le problème et définir une nouvelle notion,
généralisée de dérivée, à partir de l'intégrale.

### Dérivée faible {.definition}
La fonction $f:\R \to \R$ est *faiblement dérivable*, s'il existe une 
fonction $g:\R \to \R$ localement absolument[^foo] intégrable
c'est-à-dire mesurable et telle que $|g|$ soit intégrable sur
tout intervalle compact $[a, b] \subset \R$,
$$
\int_a^b |g(x)|\, dx < + \infty,
$$
et une constante $c \in \R$ 
telles que pour tout $x \in \R$, 
$$
f(x) = c + \int_0^x g(t) \, dt.
$$
La fonction $g$ est alors définie uniquement presque partout ; 
elle est appelée *dérivée faible* de $f$ et pourra être notée $f'$.

### TODO -- Démonstration {.proof}

[^foo]: si $f$ est conditionnellement intégrable, l'application
$$
\phi \in D^0(\R) \mapsto \int f \phi 
$$
n'est pas (nécessairement ?) bornée, $f$ ne peut donc pas être représentée
comme une mesure, contrairement aux fonctions absolument continue. 
C'est trop tôt à ce stade pour parler de ça, mais la motivation est 
importante pour se limiter aux fonction absolument continues ...

### TODO -- extension "p.p." ?
Aka fct de départ définie pp ? Bof ... Mmm quand même nécessaire pour la
suite. (euh, mais où ça ?)

### TODO -- Terminologie
Opter pour "généralisée" en 1ere instance ?
dérivée généralisée, dérivable au sens des distributions (cf. + tard)

### TODO -- Dérivable faiblement implique dérivable pp {.proposition}
Corollaire: dérivable faiblement implique dérivée classique existe pp et
est égale à la dérivée faible

### TODO -- Exemples
$x \mapsto |x|$ ?

### Dérivabilité classique et faible 
Si $f: \R \to \R$ admet une dérivée faible $g$, alors $f$ est dérivable
presque partout et $f'=g$ presque partout.

### TODO
Lien du truc dessus avec unicité pp de $g$ évoquée plus haut.

### TODO -- Warning, pas de réciproque
attention: dérivée classique définie pp suffit pas à avoir dérivée
faible (ex: fct de Heaviside).
Dérivée faible implique dérivée pp, réciproque pas vraie, même si on ajoute
continue (idée qui vient naturellement quand on construit un contre-exemple).
Exemple avec ensembles de Cantor / devil's staircase.
Même dérivable partout ne suffit pas ...

### Absolue continuité {.definition}
Une fonction $f:\R \to \R$ est *absolument continue* si et seulement si
pour tout $\varepsilon > 0$, il existe un $\delta > 0$ tel que pour toute
collection finie d'intervalles compacts $([a_k, b_k])_{k=0}^{n-1}$ de $\R$ 
ne se chevauchant pas, on ait
$$
\sum_{k=0}^{n-1} (b_k - a_k) \leq \delta
\; \Rightarrow \; 
\sum_{k=0}^n |f(b_n) - f(a_n)| \leq \varepsilon.
$$

### TODO 
ne se chevauchant pas est nécessaire (note Bartle : c'est crucial) ? 
Pas suffisant de se limiter aux subdivisions complètes ?

### Existence de dérivée faible {.proposition}
Une fonction $f:\R \to \R$ admet une dérivée faible si et seulement si
elle est absolument continue.

### TODO -- Démonstration

### TODO -- Rk
Il serait possible d'élargir la notion de fonction faiblement dérivable en exigeant
uniquement que $g$ soit localement intégrable au sens de Henstock-Kurzweil,
et non localement absolument intégrable. Comme toute dérivée est localement
intégrable au sens de Henstock-Kurzweil, cette extension aurait le mérite
de proposer une notion de dérivée faible qui soit une *vraie* extension de la
notion de dérivée classique (en l'état, il est possible qu'une fonction ait
une dérivée en tout point mais pas de dérivée faible ...).  
Néanmoins, aussi séduisante soit-elle, 
nous ne considérerons pas cette extension, car la classe des fonctions
faiblement dérivables serait alors sensiblement plus complexe à caractériser
que dans le cadre absolument continu que nous avons choisi[^ACG].

[^ACG]: Il s'agit d'une classe de fonctions absolument continues 
mais **généralisées**, notée $\mathrm{ACG}_*$, cf. [@Bar01, pp. 242-243].

### TODO -- Dérivation faible et IPP
(équivalence)

Mesures signées
================================================================================

### TODO
Perspective fonction sans dérivée faible fonction (ex: fct avec saut),
mais qui peut être dérivée comme une mesure. Perspective de patch :
analyse de l'IPP pour les dérivées faibles et comment le rhs est une
forme linéaire sur $C_c$.

### Note
Sauf erreur, la définition "naturelle" (ressemblant) de mesure à valeurs
dans $\R$ ne garantit pas l'existence d'une décomposition de Hahn et ne
permet donc pas de se ramener au cas des mesures positives (cf. 
Dunford-Schwarz pour la preuve de ce résultat). Cela a donc du sens
d'insister sur une définition de mesure signée, prenant comme base une
mesure et une fonction de signe.
(à plus long-terme, j'aimerais un exemple de mesure à valeurs réelles
qui n'admet pas de décompo de Hahn)


### TODO -- Mesure signée {.definition} 
Soit $(X, \mathcal{A})$ un ensemble mesurable.
Une *mesure signée* $\nu$ sur $(X, \mathcal{A})$ est une application
$$
\nu : \mathcal{A} \to \left]-\infty, +\infty\right[ \cup \{\bot\}
$$
pour laquelle il existe une mesure positive $\mu$ sur $\mathcal{A}$ et 
une application $\mu$-mesurable $\sigma: X \to \{-1, +1\}$ telles que
pour tout $A \in \mathcal{A}$,
$$
\nu(A) := \sigma \mu(A) := \int_A \sigma(x) \, \mu(dx)
$$
si l'application $1_A \sigma$ est $\mu$-intégrable 
et $\nu(A) = \bot$ sinon.

### TODO -- Mesure positive vers mesure signée
Expliquer "conversion" de $\inf$ vers $\bot$, règles de calcul avec $\bot$.

### TODO -- Variation d'une mesure signée.
Soit $\nu$ une mesure signée sur $(X, \mathcal{A})$.
Il existe une mesure positive $\mu$ sur $(X, \mathcal{A})$ et 
une unique application une application $\mu$-mesurable 
$\sigma: X \to \{-1, +1\}$ telle que 
$\nu = \sigma \mu$. On appelle $\mu$ la *variation de $\nu$* et on la note
$|\nu|$.

### TODO -- Check pptés usuelles mesure ($\sigma$-add, etc.)
Warning : plus de monotonie !

### TODO
Comment on a défini $\mu$-intégrable dans le chapitre précédent ?
Précisément, est-ce qu'une intégrale avec "une valeur infinie" est
intégrable ? Le "problème", outre l'absence de cohérence par rapport
aux chapitres précédents, est qu'on peut alors avoir une fonction
intégrable, et la rendre non-intégrable en la multipliant par une
fonction de signe mesurable. OK, bon, intégrable veut dire intégrale
finie, le cas $+\infty$ sera a décrire comme une extension dans les
cas simples (comme fct mesurable positive non intégrable par exemple).

### TODO -- Convention $\bot$, absorption $\inf$ ou non ?
Disons pas d'absorption par défaut ? A voir, y réfléchir.
Avec absorption c'est plus simple quand même ...

### TODO -- Décomposition de Hahn
(trivial, mais bon)

### TODO -- Variation d'une mesure


### TODO -- rk

Souligner parallèle avec valeur absolue, considérer le
cas particulier à densité.

### TODO -- $\sigma$-additivité


### TODO 
$f$ $\mu-$intégrable à valeurs réelles fois $\mu$ défini une mesure signée

### TODO -- Intégrale par rapport à une mesure signée

### TODO -- Mesure de Radon
On appelle *mesure de Radon* (signée) sur $\R$ toute mesure signée sur
$(\R,\mathcal{B}(\R))$ telle que pour tout compact $K$ de $\R$,
$|\mu|(K) < +\infty$, c'est-à-dire $\mu(K) \neq \bot$.

<!--
Une mesure de Borel positive $\mu : \mathcal{B}(\R) \to [0, +\infty]$ est *de Radon* si :

  1. Pour tout compact $K \subset \R$, $\mu(K) < +\infty$ (*localement finie*).

  2. Pour tout $A \in \mathcal{B}(\R)$, 
     $$
     \mu(A) = \sup \{\mu(K) \; | \; \mbox{$K$ compact de $\R$}, \, K \subset A\}.
     $$
    (régularité intérieure).

  3. Pour tout $A \in \mathcal{B}(\R)$,
     $$
      \mu(A) = \inf \{\mu(V) \; | \; \mbox{$V$ ouvert de $\R$}, \, A \subset V\}.
     $$
    (régularité extérieure).

### TODO
(dans le cas réel, 2. et 3. sont gratuits ? Chercher. Je crois oui, cf
<https://www.lpsm.paris/cours/processus-html/node6.html> par exemple).
Supprimer de la def donc ... (éventuellement, faire une rq sur la régularité).
-->


### Fonctions tests continues
On note $D^0(\R)$ l'espace des fonctions continues $\varphi: \R \to \R$
dont le support
$$\mbox{supp } \varphi := \overline{\{x \in \R \; | \; \varphi(x) \neq 0\}}$$
est compact.

### Formes linéaires continues sur $D^0(\R)$.
Une application linéaire $T: D^0(\R) \to \R$ 
-- c'est-à-dire une *forme linéaire* sur $D^0(\R)$ --
est dite *continue* si pour tout
intervalle compact $[a, b]$ de $\R$ et toute fonction $\varphi \in D^0(\R)$ dont
le support soit inclus dans $[a, b]$, il existe une constante $K$ telle que
$$
|T \cdot \phi| \leq K \sup_{x \in [a, b]} |\varphi(x)| = K \|\varphi|_{[a, b]}\|_{\infty}
$$


### Théorème de Riesz-Markov-Kakutani
Il existe une bijection entre l'ensemble des applications linéaire continues 
$T : D^0(\R) \to \R$ et l'ensemble des mesures de Radon $\mu$ sur $\R$, 
déterminée par la relation 
$$
\forall \, \varphi \in D^0(\R), \; T \cdot \varphi = \int \varphi \mu.
$$

### TODO -- Démonstration {.proof}
Si $\mu$ est une mesure de Radon sur $\R$, de la forme
$\mu = \sigma |\mu|$ où $\sigma$ ess une fonction borélienne à valeurs
dans $\{-1, 1\}$, alors la fonction
$$
T: \varphi \in D^0(\R) \mapsto \int \varphi \mu  = \int \varphi \sigma |\mu| \in \R
$$
est bien définie : $\varphi$ est continue donc $|\mu|$-mesurable ainsi que 
le produit $\varphi \sigma$ et si le support de $\varphi$ est inclus dans le compact 
$[a, b]$, alors
$$
|\varphi(y) \sigma(y)| \leq 1_{[a, b]}(y) \times \sup_{x \in [a, b]} |\varphi(x)|.
$$ 
Comme la mesure $\mu$ est de Radon, $|\mu|([a, b]) < +\infty$, donc
la fonction $\varphi \sigma$ est dominée par une fonction $|\mu|$-intégrable.
Elle est donc $|\mu|$-intégrable.

La fonction $T$ ainsi définie est également linéaire par linéarité de l'intégrale. 
De plus, si le support de $\varphi$ est inclus dans $[a, b]$, alors
$$
|T \cdot \varphi| 
\leq \int |\varphi| |\mu|
\leq \int \left(\sup_{x \in [a, b]}|\varphi(x)|\right) |\mu|
= |\mu|(A) \left(\sup_{x \in [a, b]}|\varphi(x)|\right).
$$
Elle est donc continue sur $D^0(\R)$.

TODO -- Renvoyer à un ref (Arverson ?) pour le reste.

### TODO
Représentation "concrête" des mesures de Radon dans $\R$ (via les fcts 
de variation localement bornée) ??? Ou pas ?

### TODO -- mesure de Radon (signée)
+ lien avec 

### TODO -- fct localement intégrable
... définie ("est") une mesure de Radon. Et la mesure détermine

### TODO

def intégrale fonction des bornes "dans le mauvais sens" ...

### Dérivée généralisée comme mesure
La fonction $f:\R \to \R$ admet comme *dérivée généralisée* la mesure de
Radon $\mu$ sur $\R$ s'il existe une constante $c$ telle que
pour tout $x \in \R$, 
$$
f(x) = c + \int_0^x \mu(dt).
$$


### TODO -- extension "p.p." ?
Aka fct de départ définie pp ? Là peut-être plus légitime que pour les
fcts, sinon quand il y a un saut, la fct de départ est tjs continue à gauche ?
Grpmh la déf est peut-être pas terrible. On ferait mieux d'intégrer sur
$\left[0, x\right[$ (ne serait-ce que pour avoir la "bonne" constante en 
$0$, et l'additivité) ; nécessaire alors de définir ça comme ça dans
la section sur la théorie de la mesure. Nota: pas évident, les probabilités
avec la convention de la fonction de répartition suggère plutôt
d'interpréter $\int_a^b$ comme l'intégrale sur $\left]a, b\right]$
(si l'on veut garder l'additivité).

### TODO -- Fonction de variation localement bornée {.definition}

### TODO -- Existence d'une dérivée comme mesure {.proposition}
Fct de variation localement bornée iff dérivée est une mesure de Radon

### TODO -- Notation Stieltjes
(explication en définissant explicitement la mesure associée à la
fct de variation bornées)

### TODO -- Explication notation, lien Kurzweil-Stieltjes
(en gros: bien que la valeur des intégrales soit différentes
-- et l'explication n'est pas si dure, L-S ignore les valeurs
de la fct à la discontinuité, pas K-S -- intégrable au sens
de L-S implique intégrabilité au sens de K-S, cf. @MAA18)

### TODO -- Rk Stieltjes
Si on intègre des fcts continues, la notation prend du sens.

### TODO -- Exemples

  - Equa diff encore, mais en prologeant $x(t)$ par $0$ pour $t \neq 0$

  - Proba et fct de répartition arbitraire.

### TODO -- Carac mesures par les fcts test (Riesz)
Aka mesure de Radon défini des opérateurs continus de $C^0_0([a, b])$
dans $\R$ et l'inverse aussi (si prolongements compatibles).

### TODO -- Formule des sauts

Distributions
================================================================================

### TODO -- Distribution {.definition}
distribution d'ordre $k$ uniquement. Fonctionnelle définie sur les fcts
$C^k$ telle que si $C^k_0([a, b])$ désigne les fcts nulles
que leurs dérivée au bord, alors (restriction de $T$) 
linéaire bornée de $C^k_0([a, b])$ dans $\R$.

### TODO -- Mesure signée est une distribution

### TODO -- Dérivée d'une distribution

Proba / Fct répartition
================================================================================

Généralisation cas discret et à densité; dans les deux cas, fcts croissante
$\mathbb{R} \to \mathbb{R}$, nulle en $-\infty$, de variation 1, etc.

Montrer comment définir une mesure (extérieure) associée,
notation $\mu (= df)$ (Lebesgue-Stieltjes) ? 

Lien notation avec somme de Riemman-Stieltjes pour l'intégration de fcts
continues ?

Probab $\Omega \neq \R^n$
================================================================================

Exercices
================================================================================

Fonctions lipschitzienne
--------------------------------------------------------------------------------

(d'une variable). Montrer qu'elles ont une dérivée faible (et donc pp),
en utilisante leur caractère absolument continu (cf. Evans-Gariepy dans
le cas multivariable) et que la dérivée (faible) est de norme plus petite
que la constante de Lipschitz.

Fonctions convexes
--------------------------------------------------------------------------------

Equivalent dérivée seconde est une mesure positive ?

Fonction distance
--------------------------------------------------------------------------------

Dérivées seconde fonction distance, squelette, courbure, etc ?

Références
================================================================================