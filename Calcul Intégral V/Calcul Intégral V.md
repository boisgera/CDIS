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
La fonction $f:\R \to \R$ est *faiblement dérivable* s'il existe une 
fonction $g:\R \to \R$ localement absolument<!--[^foo]--> intégrable
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
La fonction $g$ est alors appelée *dérivée faible* de $f$.

### Les fonction absolument continues sont continues.

### TODO -- Démonstration.

### Dérivée faible et classique
Si une fonction $f: \R \to \R$ est faiblement dérivable, de dérivée faible $g$,
alors elle est dérivable (classiquement) presque partout, et $f' = g$ presque
partout. On a donc pour tout $x \in \R$,
$$
f(x) = f(0) + \int_0^x f'(t) \, dt.
$$

### 
En particulier, la dérivée faible d'une fonction, si elle existe, est unique
presque partout.

### Démonstration {.proof}
Une conséquence directe du résultat de 
[dérivation des intégrales indéterminée](Calcul Intégral II.pdf/#DII).

<!--
[^foo]: si $f$ est conditionnellement intégrable, l'application
$$
\phi \in D^0(\R) \mapsto \int f \phi 
$$
n'est pas (nécessairement ?) bornée, $f$ ne peut donc pas être représentée
comme une mesure, contrairement aux fonctions absolument continue. 
C'est trop tôt à ce stade pour parler de ça, mais la motivation est 
importante pour se limiter aux fonction absolument continues ...
-->

### Valeur absolue {.example #example-abs}
La fonction valeur absolue $|\cdot|: x \in \R \mapsto |x|$ est faiblement dérivable.
En effet, elle est dérivable presque partout (sauf en $0$),
sa dérivée classique valant $1$ quand $x>0$ et $-1$ quand $x < 0$.
Ses seules dérivées faibles potentielles sont dont les fonctions
égales presque partout à la fonction signe
$$
\mbox{sgn}(x) := \left| 
\begin{array}{rl}
-1 & \mbox{si $x<0$,} \\
0 & \mbox{si $x=0$,} \\
+1 & \mbox{si $x>0$.}
\end{array}
\right.
$$
De plus, pour tout $x\geq 0$ on a bien
$$
|x| = x = \int_0^x dt = |0| + \int_0^x \mbox{sgn}(t) \, dt
$$
et pour $x < 0$, 
$$
|x| = -x = \int_0^x - dt = |0| + \int_0^x \mbox{sgn}(t) \, dt.
$$
La fonction $|\cdot|$ est bien faiblement dérivable, de dérivée faible la fonction 
$\mbox{sgn}$.

![](images/abs.py)\ 

On peut remarquer que la fonction signe n'est pas elle-même faiblement
dérivable. Elle est bien dérivable presque partout (sauf en $0$) ;
sa dérivée est nulle presque partout. Si elle était faiblement dérivable,
on aurait donc pour tout $x \in \R$,
$$
\mbox{sgn}(x) = \mbox{sgn}(0) + \int_0^x 0 \, dt = 0,
$$
ce qui n'est pas le cas.

### Fonction dérivable par morceaux {.definition}
On dira qu'une fonction $f: \R \to \R$ est différentiable par 
morceaux s'il existe une collection dénombrable d'intervalles compacts $[a_k, b_k]$
sans chevauchements recouvrant $\R$ telle que la restriction de $f$ à 
tout $\left]a_k, b_k\right[$ puisse être prolongée en une fonction différentiable 
sur $[a_k, b_k]$.

### {.post}
A noter que l'on peut être différentiable par morceaux mais pas
continue -- la fonction signe de [l'exemple consacré à la dérivée faible de
la valeur absolue est un bon exemple](#example-abs).
Sans la continuité, le caractère différentiable par morceaux
ne suffit pas à garantir l'existence d'une dérivée faible.

### Les fonctions dérivables par morceaux sont faiblement différentiables {.theorem}
Toute fonction $f: \R \to \R$ continue et dérivable par morceaux est faiblement dérivable.


### Démonstration {.proof}
On trouve dans [@Tao11, prop. 1.6.41, p. 176] la clé de la démonstration,
à savoir que si une fonction $f: [a, b] \to \R$ est différentiable 
et de dérivée absolument intégrable, alors 
$$
f(b) - f(a) = \int_a^b f'(x) \, dx. 
$$
Nous omettons cette portion (critique) de la démonstration ; 
en déduire le résultat cherché est beaucoup plus simple. 

Notons $f(b^-)$ et $f(a^+)$ les limites à gauche de $f$ en $b$ et
à droite de $f$ en $a$ respectivement.
On déduit de l'énoncé précédent que si $f$ est dérivable sur $\R$ et 
de dérivée localement absolument intégrable, et si $x \in [a_k, b_k]$, 
alors
$$
\int_{a_k}^{b_k} f'(x) \, dx = f(b^-) - f(a^+) = f(b) - f(a)
$$
et si $a_k < x < b_k$,
$$
f(x) - f(a) = f(x) - f(a^+) = \int_a^x f'(t) \, dt
$$
et 
$$
f(x) - f(b) = - (f(b^-) - f(x)) = - \int_x^b f'(t) \, dt = \int_b^x f'(t) \, dt.
$$
Suppons que les intervalles $[a_k, b_k]$ soient indexés par des entiers relatifs 
$k$ consécutifs et ordonnées de façon croissante.
Alors, si $x$ est réel positif, que $0 \in [a_i, b_i]$ et que $x \in [a_j, b_j]$,
on a
$$
\begin{split}
f(x) - f(0) &= (f(x) - f(a_j)) + (f(b_{j-1}) - f(a_{j-1})) + \dots + (f(a_i) - f(0)) \\
& = \int^x_{a_j} f'(t) \, dt + \int_{a_{j-1}}^{b_{j-1}} f'(t) \, dt + \dots + \int_0^{a_i} f'(t) \, dt.
\end{split} 
$$
et donc
$$
f(x) = f(0) + \int_0^x f'(t) \, dt.
$$
Le cas d'un réel $x$ négatif se traite de façon similaire.

### Fonction de répartition

La fonction $F: \R \to \R$ définie par 
$$
F(x) = \int_{-\infty}^x \frac{\exp (-{t^2}/{2})}{2\pi} \, dt
$$
est une fonction de répartition, associée à la loi normale centrée réduite. 
Elle est faiblement dérivable ; en effet, son intégrande est localement absolument intégrable 
(il est positif et intégrable sur $\R$, d'intégrale $1$) 
et l'on a par additivité de l'intégrale pour tout $x\in\R$
$$
F(x) = F(0) + \int_{0}^x \frac{\exp (-{t^2}/{2})}{2\pi} \, dt.
$$
Cett relation montre également que la fonction 
$$
f : t \in \R \mapsto  \frac{\exp (-{t^2}/{2})}{2\pi}
$$
est une dérivée faible de $F$([^eaf]). 

![skdjslkdjs](images/gauss.py)\ 


Le même argument, appliqué à
la fonction $F: \R \to \R$ définie par 
$$
F(x) = \int_{-\infty}^x f(t) \, dt
$$
où $f:\R \to \R$ est positive et intégrable, démontre
que si une probabilité $\mathbb{P}$ sur $\mathbb{R}$
admet une densité $f$, sa fonction de répartition $F$ est faiblement dérivable
de dérivée faible $f$. La réciproque est également vraie : si une fonction
de répartition $F$ admet $f$ comme dérivée faible, cette fonction $f$ est 
une densité associée à $F$, c'est-à-dire que 
$$
F(x) = \int_{-\infty}^x f(t) \, dt.
$$

### TODO -- preuve en exercice ? Y réfléchir.

[^eaf]: Cette fonction $f$ est aussi la dérivée classique de $F$ en tout point
(et pas seulement presque partout comme la théorie nous le garantit).
En effet la fonction $f$ est continue en tout point $x \in \R$. On a donc
$$
\begin{split}
\left|\frac{F(x+h) - F(x)}{h} - f(x)\right| &=  
\left|\frac{1}{h}\int_x^{x+h} (f(t) - f(x)) \, dt \right| \\
& \leq 
\frac{1}{h}\int_x^{x+h} |f(t) - f(x)| \, dt \to 0 \, \mbox{ quand } \, h \to 0.
\end{split}
$$
Le taux d'accroissement de $F$ en $x$ tend donc vers $f(x)$ quand $h$ tend vers $0$.


### Fonction de Cantor {.remark}
On pourrait croire en prenant connaissance des contre-exemples simples
à l'existence d'une dérivée faible que dès lors qu'une fonction est continue
a une dérivée presque partout et que cette dérivée est localement absolument 
intégrable, elle est faiblement dérivable. Mais ça n'est pas le cas !

Ainsi la fonction de Cantor $f:\R \to \R$ est un exemple de fonction
continue, de dérivée (classique) définie et nulle presque partout et
pourtant telle que $f(0)=0$ et $f(1)=1$, ce qui contredit la relation
$$
f(1) = f(0) + \int_0^1 0\, dt
$$
qu'elle devrait vérifier si elle était faiblement dérivable.

La fonction de Cantor $f$ est définie comme la limite des
suites de fonctions $f_n:\R \to \R$ données par 
$$
f_0(x) = 
\left|
\begin{array}{rl}
0 & \mbox{si $x<0$,} \\
x & \mbox{si $0\leq x\leq 1$,} \\
0 & \mbox{si $1< x$.} \\
\end{array}
\right.
$$
et pour tout $n\geq 1$
$$
f_{n+1}(x) = \left|
\begin{array}{rl}
0.5 \times f_n(3x) & \mbox{si $x < 1/3$}, \\
0.5 & \mbox{si $1/3 \leq x < 2/3$}, \\
0.5 + 0.5 \times f_n(3x-2) & \mbox{si $2/3 \leq x$}.
\end{array}
\right.
$$

![Approximation d'ordre $5$ de la fonction de Cantor](images/devil-staircase.py)

### TODO -- interprétation probabiliste.

(y compris -- ou plutôt surtout -- pour les fonctions intermédiaires 
qui sont "uniformes par morceaux". L'interprétation de la limite n'a
pas besoin d'être formalisée.)

### Absolue continuité {.definition}
Soit $I$ un intervalle de $\R$.
Une fonction $f:I \to \R$ est *absolument continue* si et seulement si
pour tout $\varepsilon > 0$, il existe un $\delta > 0$ tel que pour toute
collection finie d'intervalles compacts $([a_k, b_k])_{k=0}^{n-1}$ de $I$ 
ne se chevauchant pas, on ait
$$
\sum_{k=0}^{n-1} (b_k - a_k) \leq \delta
\; \Rightarrow \; 
\sum_{k=0}^n |f(b_n) - f(a_n)| \leq \varepsilon.
$$
Elle est *localement absolument continue* si sa restriction à tout intervalle
compact $K$ de $I$ est absolument continue. 

### TODO 
ne se chevauchant pas est nécessaire (note Bartle : c'est crucial) ? 
Pas suffisant de se limiter aux subdivisions complètes ?

### Existence de dérivée faible et absolue continuité {.proposition}
Une fonction $f:\R \to \R$ admet une dérivée faible si et seulement si
elle est localement absolument continue.

### TODO -- Démonstration

### TODO -- exploitation (/ dérivée faible) et exemple de fct abs cont

### TODO -- Une notion plus permissive de dérivée faible ?
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

**TODO:** référence concrête à un exemple de dérivée non absolument intégrable
déjà traité.

**TODO:** faire le lien par exemple avec l'approche par IPP ou fct test 
(forme lin sur); qui ne marche pas avec conditionnellement intégrable.
Du coup, peut-être retarder la remarque ? Appendice ?

[^ACG]: Il s'agit d'une classe de fonctions absolument continues 
mais **généralisées**, notée $\mathrm{ACG}_*$, cf. [@Bar01, pp. 242-243].

### TODO

Contexte du résultat à venir, notamment, motiver que ça ressemble à une IPP.

### Fonctions tests
On note $D^k(\R)$ l'espace des fonctions continues $\varphi: \R \to \R$
dont le support
$$\mbox{supp } \varphi := \overline{\{x \in \R \; | \; \varphi(x) \neq 0\}}$$
est compact et qui sont $k$ fois continûment différentiables ou simplement
continues dans le cas $k=0$.

### TODO -- Dérivation faible et fonction test
Une fonction $f:\R \to \R$ est faiblement dérivable de dérivée faible 
$g : \R \to \R$ si et seulement si pour tout $\varphi \in D^1(\R)$, on a
$$
\int_{-\infty}^{+\infty} g(t) \varphi(t) \, dt
=
-\int_{-\infty}^{+\infty} f(t) \varphi'(t) \, dt.
$$

### TODO -- Démonstration {.proof}

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

Dérivée faible
--------------------------------------------------------------------------------

Est-ce que la fonction $f: \R \to \R$ définie par $f(0)=0$ et
$$
f(x) = \sqrt{|x|} \, \mbox{ si $x\neq 0$}
$$
est faiblement dérivable ? Quelle est dans ce cas sa dérivée ?

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