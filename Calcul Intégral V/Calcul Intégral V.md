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
La fonction $f:\R \to \R$ est *faiblement dérivable*, 
de dérivée (faible) la fonction localement intégrable 
$g: \R \to \R$ s'il existe une constante $c$ telle que
pour tout $x \in \R$, 
$$
f(x) = c + \int_0^x g(t) \, dt.
$$

### TODO -- extension "p.p." ?
Aka fct de départ définie pp ? Bof ... Mmm quand même nécessaire pour la
suite.

### TODO -- Terminologie
Opter pour "généralisée" en 1ere instance ?
dérivée généralisée, dérivable au sens des distributions (cf. + tard)

### TODO -- Dérivable faiblement implique dérivable pp {.proposition}
Corollaire: dérivable faiblement implique dérivée classique existe pp et
est égale à la dérivée faible

### TODO -- Exemples
$x \mapsto |x|$ ?

### TODO -- Warning
attention: dérivée classique définie pp suffit pas à avoir dérivée
faible (ex: fct de Heaviside).
Dérivée faible implique dérivée pp, réciproque pas vraie, même si on ajoute
continue (idée qui vient naturellement quand on construit un contre-exemple).
Exemple avec ensembles de Cantor / devil's staircase.

### TODO -- Continuité absolue {.definition}

### TODO -- Existence de dérivée faible {.proposition}
(équiv abs. cont. si dérivée faible est localement absolument intégrable)

### TODO -- Rk
On peut ne pas se limiter au dérivée loclt abs cont, mais alors la classe
des fcts est $AC^*$ ... Grpmh.

### TODO -- Dérivation faible et IPP
(équivalence)

Mesures signées
================================================================================

Aka section "dérivée est une mesure"

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
Une *mesure signée* $\nu$ sur la tribu $\mathcal{A}$ de $X$ est une application
de $\mathcal{A}$ dans $\R \cup \{\bot\}$ pour laquelle
il existe une mesure positive $\mu$ sur $\mathcal{A}$ et une application
$\mu$-mesurable $\nu: X \to \{-1, +1\}$ telles que
$$
\nu(A) := \sigma \mu(A) := \int_A \sigma(x) \, \mu(dx)
$$
si l'application $1_A \times \sigma$ est $\mu$-intégrable 
et $\nu(A) = \bot$ sinon.

### TODO -- Mesure positive vers mesure signée
"Conversion" de $\inf$ vers $\bot$.

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

### TODO -- Variation totale


### TODO -- $\sigma$-additivité


### TODO 
$f$ $\mu-$intégrable à valeurs réelles fois $\mu$ défini une mesure signée

### TODO -- mesure de Radon (signée)
+ lien avec 

### TODO -- fct localement intégrable
... définie ("est") une mesure de Radon. Et la mesure détermine

### Dérivée généralisée comme mesure
La fonction $f:\R \to \R$ admet comme *dérivée généralisée* la mesure de
Radon $\mu$ sur $\R$ s'il existe une constante $c$ telle que
pour tout $x \in \R$, 
$$
f(x) = c + \int_0^x d\mu(t).
$$
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