---
author:
- 'STEP, MINES ParisTech[^1]'
bibliography: bibliography.json
date: '12 février 2021 (`#7d082cf`)'
header-includes:
- |
  ```{=latex}
  \usepackage{fontawesome}
  ```
- |
  ```{=latex}
  \usepackage{grffile}
  ```
- |
  ```{=latex}
  \usepackage{bookmark}
  ```
- |
  ```{=latex}
  \urlstyle{tt}
  ```
link-citations: true
title: Calcul Intégral I
---

```{=latex}
\usepackage{fontawesome}
```

```{=latex}
\usepackage{grffile}
```

```{=latex}
\usepackage{bookmark}
```

```{=latex}
\urlstyle{tt}
```

-   [Objectifs d'apprentissage](#objectifs-dapprentissage)
-   [Somme et intégrale de Riemann](#somme-et-intégrale-de-riemann)
-   [Intégrales de Riemann
    généralisées](#intégrales-de-riemann-généralisées-1)
-   [Propriétés élémentaires de
    l'intégrale](#propriétés-élémentaires-de-lintégrale-1)
-   [Intégration sur des intervalles
    arbitraires](#intégration-sur-des-intervalles-arbitraires)
-   [Annexe](#annexe)
-   [Exercices complémentaires](#exercices-complémentaires)
    -   [Méthode des trapèzes](#méthode-des-trapèzes)
    -   [Fonctions non intégrables](#fonctions-non-intégrables)
    -   [Continuité presque partout](#continuité-presque-partout)
    -   [Poussière de Cantor](#cantor)
-   [Solutions](#solutions)
    -   [Exercices essentiels](#exercices-essentiels)
    -   [Méthode des trapèzes](#méthode-des-trapèzes-1)
    -   [Fonctions non intégrables](#fonctions-non-intégrables-1)
    -   [Continuité presque partout](#continuité-presque-partout-1)
    -   [Poussière de Cantor](#poussière-de-cantor)
-   [Références](#références)

```{=tex}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}
\newcommand{\Rint}{\mbox{(R)}\!\!\int}
\newcommand{\HKint}{\mbox{(HK)}\!\!\int}
\newcommand{\Lint}{\mbox{(L)}\!\!\int}
```
```{=tex}
\newcommand{\zero}{$\mathord{\boldsymbol{\circ}}$}
\newcommand{\one}{$\mathord{\bullet}$}
\newcommand{\two}{$\mathord{\bullet}\mathord{\bullet}$}
\newcommand{\three}{$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$}
\newcommand{\four}{$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$}
```
```{=tex}
\newcommand{\lb}{[}
\newcommand{\rb}{]}
\newcommand{\lob}{\left]}
\newcommand{\rob}{\right[}
```
::: {.section}
Objectifs d'apprentissage
=========================

Cette section s'efforce d'expliciter et de hiérarchiser les acquis
d'apprentissages associés au chapitre. Ces objectifs sont organisés en
paliers :

(`$\mathord{\boldsymbol{\circ}}$`{=tex}) Prérequis
(`$\mathord{\bullet}$`{=tex}) Fondamental
(`$\mathord{\bullet}\mathord{\bullet}$`{=tex}) Standard
(`$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$`{=tex}) Avancé
(`$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$`{=tex})
Expert

Sauf mention particulière, les objectifs "Expert", les démonstrations du
document[^2] et les contenus en annexe ne sont pas exigibles
("hors-programme").

::: {.section}
#### Ensembles négligeables

-   `$\mathord{\boldsymbol{\circ}}$ `{=tex}savoir calculer la longueur
    des intervalles de $\mathbb{R}$,

-   `$\mathord{\bullet}$ `{=tex}savoir que négligeable $\approx$
    "de-longueur-nulle",

-   `$\mathord{\bullet}$ `{=tex}savoir que tout ensemble dénombrable est
    négligeable,

-   `$\mathord{\bullet}$ `{=tex}savoir que les seuls intervalles
    négligeables sont vides ou dégénérés[^3],

-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir définir le terme
    d'ensemble négligeable,

-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir interpréter les
    énoncés comportant des "presque partout",

-   `$\mathord{\bullet}$`{=tex}/`$\mathord{\bullet}\mathord{\bullet}$`{=tex}/`$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir
    démontrer qu'un ensemble est négligeable.
:::

::: {.section}
#### Intégrale de Riemann

-   `$\mathord{\bullet}$ `{=tex}savoir définir les termes subdivision et
    subdivision pointée,

-   `$\mathord{\bullet}$ `{=tex}savoir calculer les sommes de Riemann
    associées,

-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir définir
    intégrale/intégrable au sens de Riemann,

-   `$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir
    calculer les intégrales de Riemann au moyen de la définition,

-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir valider
    asymptotiquement les méthodes de quadrature,

-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir caractériser les
    fonctions intégrables au sens de Riemann.
:::

::: {.section}
#### Intégrales de Riemann généralisées

-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}connaître la définition
    du terme jauge,

-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}connaître la définition
    de subdivision pointée subordonnée à une jauge,

-   `$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir
    définir intégrable/intégrale au sens de Henstock-Kurzweil,

-   `$\mathord{\bullet}$ `{=tex}savoir définir intégrable/intégrale au
    sens de Lebesgue,

-   `$\mathord{\bullet}$ `{=tex}savoir que l'intégrale de Lebesgue étend
    l'intégrale de Riemann,

-   `$\mathord{\bullet}$ `{=tex}connaître deux exemples typiques qui
    motivent le passage à Lebesgue.
:::

::: {.section}
#### Intervalles arbitraires

-   `$\mathord{\bullet}$ `{=tex}savoir passer d'une intégrale sur un
    intervalle arbitraire à $[-\infty, +\infty]$,

-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir définir
    l'intégrale d'une fonction de $[-\infty, +\infty]$ dans
    $\mathbb{R}$.
:::

::: {.section}
#### Propriétés élémentaires de l'intégrale

-   `$\mathord{\bullet}$ `{=tex}connaître le théorème fondamental du
    calcul,

-   `$\mathord{\bullet}$ `{=tex}savoir que l'intégrale est linéaire,
    additive et supporte la restriction,

-   `$\mathord{\bullet}$ `{=tex}savoir que l'intégrale est croissante et
    satisfait l'inégalité triangulaire,

-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir que deux
    fonctions égales presque partout ont même intégrale,

-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}connaître la réciproque
    à ce résultat,

-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir que les
    intégrales indéterminées sont continues,

-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir que les
    intégrales indéterminées sont dérivables presque partout,

-   `$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$ `{=tex}connaître
    le théorème de changement de variable.
:::
:::

::: {.section}
Somme et intégrale de Riemann
=============================

::: {.section}
### Définition -- Intervalle de $\mathbb{R}$ {#intervalle-de-mathbbr .definition .zero .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Intervalle de \(\mathbb{R}\)}`{=latex}

On appelle *intervalle* de $\mathbb{R}$ tout sous-ensemble $I$ de
$\mathbb{R}$ tel que si $x$ et $y$ appartiennent à $I$ et vérifient
$x \leq y$ et si $z$ est un point intermédiaire, tel que
$x \leq z \leq y$, alors $z$ appartient également à $I$.
:::

::: {.section}
Les intervalles de $\mathbb{R}$ peuvent être bornés ou non-bornés,
ouverts, fermés, ouverts et fermés ou ni l'un ni l'autre. Les
intervalles de la forme $\left]-\infty, +\infty\right[$ (c'est-à-dire
$\mathbb{R}$), $\left]-\infty, b\right[$, $\left]a,+\infty\right[$ et
$\left]a,b\right[$ -- où $a$ et $b$ désignent des nombres réels -- sont
les intervalles ouverts. Les intervalles de la forme
$\left]-\infty, +\infty\right[$, $\left]-\infty, b\right]$,
$\left[a,+\infty\right[$ et $\left[a,b \right]$ sont les intervalles
fermés. Les intervalles de la forme $[a, b]$ sont les intervalles
simultanément fermés et bornés (compacts).
:::

::: {.section}
### Définition -- Longueur d'un intervalle de $\mathbb{R}$ {#longueur-dun-intervalle-de-mathbbr .definition .zero .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Longueur d'un intervalle de \(\mathbb{R}\)}`{=latex}

La *longueur* $\ell(I)$ d'un intervalle $I$ de $\mathbb{R}$ est le
nombre réel étendu positif (appartenant à $[0, +\infty]$) défini pour
tout intervalle borné $I$ de la forme $\left[a, b\right]$,
$\left]a, b\right[$, $\left[a, b\right[$ ou $\left]a, b\right]$ avec
$a\leq b$ par $$
\ell(I) = b - a
$$ et si $I$ est non-borné par $$
\ell(I) = +\infty.
$$
:::

::: {.section}
### Définition -- Subdivision pointée {#sp .definition .two .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Subdivision pointée}`{=latex}

Une *subdivision* de l'intervalle $[a,b]$ est une collection finie $$
\{I_i \; | \; i \in \{0, \dots, m-1\}\}
$$ constituée d'intervalles fermés inclus dans $[a, b]$, *sans
chevauchement* -- si $i$ et $j$ diffèrent, l'intersection de $I_i$ et
$I_j$ contient au plus un point -- et *recouvrant $[a, b]$* -- l'union
de tous les intervalles $I_i$ inclut $[a, b]$. $$
[a, b] \subset \bigcup_{i=0}^{m-1} I_i.
$$

Une *subdivision pointée* $\mathcal{D}$ de l'intervalle $[a, b]$ est une
collection finie $$
\mathcal{D} = \{(t_i, I_i) \; | \; i \in \{0, \dots, m-1\}
$$ où $\{I_i\}_{i=0}^{m-1}$ est une subdivision de $[a, b]$ et
$t_i \in I_i$ pour tout $i \in \{0, \dots, m-1\}.$
:::

::: {.section}
### Remarque -- Forme canonique d'une subdivision pointée {#rcsp .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Forme canonique d'une subdivision pointée}`{=latex}

En ordonnant les intervalles $I_i$ d'une subdivision pointée
$\{(t_i, I_i)\; | \; i \in \{0, \dots, m-1\}\}$ "de la gauche vers la
droite" et en notant chaque intervalle comme $I_i =: [x_i, x_{i+1}]$, on
peut la caractériser par des réels
$x_0, x_1, \dots, x_m, t_0, \dots, t_{m-1}$ vérifiant $$
a = x_0 \leq t_0 \leq x_1 \leq t_1 \dots \leq t_{m-1} \leq x_{m} = b. 
$$

![Subdivision pointée
$\mathcal{D} = \{(0.1, [0, 0.2]), \dots, (0.9, [0.8, 1])\}$ de $[0,1]$.
Les intervalles de la subdivision sont délimités par des barres
verticales et les points associés représentés par des
croix.](images/gauge-plot-subdivision-only.py.pdf)
:::

::: {.section}
### Définition -- Somme de Riemann {#somme-de-riemann .definition .two .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Somme de Riemann}`{=latex}

La somme de Riemann associée à la fonction $f:[a, b] \to \mathbb{R}$ et
à la subdivision pointée $\mathcal{D}$ de $[a, b]$ est la grandeur $$
S(f, \mathcal{D}) = \sum_{(t, I) \in \mathcal{D}} f(t) \ell(I).
$$
:::

::: {.section}
Pour une subdivision $\mathcal{D}$ sous forme canonique
$\{(t_i, [x_i, x_{i+1}])\; | \; i \in \{0, \dots, m-1\}\}$, on obtient
$$
S(f, \mathcal{D}) = \sum_{i=0}^{m-1} f(t_i) (x_{i+1} - x_i).
$$

![L'aire de la zone grisée correspond à la valeur de la somme de Riemann
$S(f, \mathcal{D})$ pour $f : t \in [0,1] \mapsto \sqrt{t}/2$ et
$\mathcal{D} = \{(0.1, [0, 0.2]), \dots, (0.9, [0.8, 1])\}$.](images/subdivision-riemann.py.pdf)
:::

::: {.section}
### Définition -- Intégrale de Riemann {#intégrale-de-Riemann .definition .two .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Intégrale de Riemann}`{=latex}

Une fonction $f:[a, b] \to \mathbb{R}$ est dite *intégrable au sens de
Riemann* s'il existe un réel $A$ tel que pour tout $\varepsilon > 0$, il
existe un réel $\delta>0$ tel que pour toute subdivision pointée
$\mathcal{D}$ de $[a, b]$ vérifiant pour $(t, J) \in \mathcal{D}$,
$\ell(J) < \delta$, on ait $|S(f, \mathcal{D}) - A| \leq \varepsilon$.
Le réel $A$ quand il existe est unique ; il est appelé *intégrale (de
Riemann) de $f$ sur $[a, b]$* : $$
\mbox{(R)}\!\!\int_a^b f(t) \, dt := A.
$$
:::

::: {.section}
### Remarque -- Intégrale de fonctions vectorielles {#intégrale-de-fonctions-vectorielles .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Intégrale de fonctions vectorielles}`{=latex}

Les fonctions $f: [a, b] \to \mathbb{R}^m$ ne présentent pas de
difficulté particulière pour l'intégration, nous n'en parlerons donc pas
spécifiquement par la suite. Nous conviendrons qu'une telle fonction est
intégrable au sens de Riemann[^4] si toutes ses composantes $f_i$ le
sont. Nous définirons alors l'intégrale associée comme le vecteur de
$\mathbb{R}^m$ tel que pour tout $i \in \{1,\dots, m\}$, $$
\left[\int_a^b f(t) \, dt \right]_i = \int_a^b f_i(t) \, dt.
$$
:::

::: {.section}
#### Exemple -- Quadrature {#quadrature .example .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Quadrature}`{=latex}

Cette définition de l'intégrale permet de garantir l'exactitude
asymptotique de méthodes de quadrature -- c'est-à-dire d'algorithmes de
calcul numérique d'intégrales -- comme la méthode des rectangles. En
effet, si $f:[a, b] \to \mathbb{R}$ est une fonction intégrable au sens
de Riemann, et $\mathcal{D}_m$ une subdivision pointée de $[a, b]$ de la
forme $$
\mathcal{D}_m=
\left\{
\left(a + i \frac{b-a}{m}, \left[a + i \frac{b-a}{m}, a + (i+1) \frac{b-a}{m} \right]\right)
\; \left| \vphantom{\left(a + i \frac{b-a}{m}, \left[a + i \frac{b-a}{m}, a + (i+1) \frac{b-a}{m} \right]\right)} \; i \in \{0, \dots, m-1\} \right.
\right\},
$$ la somme de Riemann associée vérifie $$
\begin{split}
S(f, \mathcal{D}_m) 
&= \sum_{i=0}^{m-1} f\left(a + i\frac{b-a}{m}\right) \ell 
\left(\left[a + i \frac{b-a}{m}, a + (i+1) \frac{b-a}{m} \right]\right)\\
&= \sum_{i=0}^{m-1} f\left(a + i\frac{b-a}{m}\right) \frac{b-a}{m}  \\
&= \frac{b-a}{m} \sum_{i=0}^{m-1} f\left(a + i\frac{b-a}{m}\right)
\end{split}
$$ De plus, quel que soit $\delta > 0$, pour $m$ suffisamment grand, on
a $$
\ell\left(\left[a + i \frac{b-a}{m}, a + (i+1) \frac{b-a}{m} \right]\right)
=
\frac{b-a}{m}
<
\delta.
$$ Par conséquent, $$
\frac{b-a}{m} \sum_{i=0}^{m-1} f\left(a + i\frac{b-a}{m}\right)
\to \mbox{(R)}\!\!\int_a^b f(t) \, dt
\, \mbox{ quand } \, m \to +\infty.
$$ La définition de l'intégrale de Riemann ne se limite pas à une
famille particulière de subdivisions -- comme ici à des subdivisions
régulières de $[a, b]$ où tous les intervalles sont de même longueur --
et n'impose pas une position fixe au point $t_i$ dans l'intervalle $J_i$
-- comme ici à gauche de l'intervalle -- ce qui garantit une forme de
robustesse à la définition de l'intégrale ; d'autres méthodes de
quadratures pourront être utilisées avec le même résultat asymptotique.
:::

::: {.section}
#### Exercice -- Fonction affine ($\mathord{\bullet}\mathord{\bullet}$) {#fa .exercise .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Fonction affine}`{=latex}

Montrer que toute fonction affine
$x \in \mathbb{R}\mapsto \alpha x + \beta$ est intégrable au sens de
Riemann sur tout intervalle fermé borné $[a, b]$ de $\mathbb{R}$ et que
$$
\mbox{(R)}\!\!\int_a^b (\alpha t +\beta) \, dt = A := \alpha \left(\frac{b^2}{2} - \frac{a^2}{2}\right) + \beta (b-a).
$$ Indication : vérifier tout d'abord que si
$\mathcal{D} = \{(t_i, [x_i, x_{i+1}]) \; | \; i \in \{0, \dots, m-1\} \}$
est une subdivision pointée de $[a, b]$ sous forme canonique, alors $A$
est la somme d'une série télescopique : $$
A = \sum_{i=0}^{m-1} \alpha \left(\frac{x_{i+1}^2}{2} - \frac{x_i^2}{2}\right) + \beta (x_{i+1}-x_i).
$$

([Solution p.
`\pageref*{answer-fa}`{=tex}](#answer-fa){.no-parenthesis}.)
:::

::: {.section}
On rappelle qu'un ensemble est *dénombrable* s'il est fini ou en
bijection avec $\mathbb{N}$.
:::

::: {.section}
### Définition -- Ensemble négligeable {#ensemble-négligeable .definition .two .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Ensemble négligeable}`{=latex}

Un ensemble $A$ de $\mathbb{R}$ est *négligeable* si pour tout
$\varepsilon > 0$, il existe un recouvrement de $A$ par une collection
dénombrable d'intervalles $I_1$, $I_2$, $\dots$, $I_i$, $\dots$ de
$\mathbb{R}$ $$
A \subset \bigcup_{i} I_i 
$$ telle que $$
\sum_i \ell(I_i) \leq  \varepsilon.
$$
:::

::: {.section}
Nous voyons que le procédé qui définit la notion d'ensemble négligeable
consiste à produire des estimations supérieures ou égales à la
"longueur"[^5] de l'ensemble -- un concept non défini à ce stade -- au
moyen d'un recouvrement par des intervalles, ensembles pour lesquels la
notion de longueur est bien définie. Si on peut construire des
estimations supérieures aussi petites que l'on veut, l'ensemble est
négligeable, c'est-à-dire intuitivement, "de longueur nulle". Le
chapitre à venir confirmera cette intuition.
:::

::: {.section}
#### Exercice -- Ensembles finis ($\mathord{\bullet}$) {#ensemble-fini .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Ensembles finis}`{=latex}

Montrer que tout sous-ensemble fini de $\mathbb{R}$ est négligeable.
([Solution p.
`\pageref*{answer-ensemble-fini}`{=tex}](#answer-ensemble-fini){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Intervalles négligeables ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#intervalles-négligeables .exercise .question .four .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Intervalles négligeables}`{=latex}

Montrer que si $a < b$, l'ensemble $[a, b]$ n'est pas négligeable.
Indication : montrer que si les intervalles $I_i$ recouvrent $[a, b]$,
alors $\sum_{i} \ell(I_i) \geq b-a$ ; on commencera par le cas d'une
collection finie d'intervalles. ([Solution p.
`\pageref*{answer-intervalles-nuxe9gligeables}`{=tex}](#answer-intervalles-négligeables){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Sous-ensemble d'un ensemble négligeable ($\mathord{\bullet}$) {#oe .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Sous-ensemble d'un ensemble négligeable}`{=latex}

Montrer que si l'ensemble $A$ est négligeable et que $B \subset A$,
alors $B$ est également négligeable. ([Solution p.
`\pageref*{answer-oe}`{=tex}](#answer-oe){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Union d'ensembles négligeables ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#uen .exercise .question .three .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Union d'ensembles négligeables}`{=latex}

Est-ce que l'union de deux ensembles négligeables est négligeable ?
L'union d'un nombre fini d'ensembles négligeables ? L'union d'une
collection dénombrable d'ensembles négligeables ? L'union d'une
collection arbitraire d'ensembles négligeables ? ([Solution p.
`\pageref*{answer-uen}`{=tex}](#answer-uen){.no-parenthesis}.)
:::

::: {.section}
### Définition -- Presque partout {#presque-partout .definition .one .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Presque partout}`{=latex}

Une propriété $P$ dépendant d'un réel $x$ est vraie *presque partout* si
l'ensemble des points $x$ où elle est fausse est un ensemble
négligeable. On pourra utiliser la notation "$P$ p.p." ou "$P(x)$ p.p."
pour signifier que la propriété $P$ est vraie presque partout.
:::

::: {.section}
#### Exercice -- Etre non nul ($\mathord{\bullet}$) {#enn .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Etre non nul}`{=latex}

Est-ce que la propriété "$x$ est non-nul" est vraie presque partout dans
$\mathbb{R}$ ? ([Solution p.
`\pageref*{answer-enn}`{=tex}](#answer-enn){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Fonction continue nulle presque partout ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#fcnpp .exercise .three .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Fonction continue nulle presque partout}`{=latex}

Montrer que toute fonction continue $f : \mathbb{R}\to\mathbb{R}$ qui
est nulle presque partout est identiquement nulle. ([Solution p.
`\pageref*{answer-fcnpp}`{=tex}](#answer-fcnpp){.no-parenthesis}.)
:::

::: {.section}
### Proposition -- Les ensembles dénombrables sont négligeables {#edn .proposition .one .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Les ensembles dénombrables sont négligeables}`{=latex}

Si le sous-ensemble $E$ de $\mathbb{R}$ est dénombrable alors il est
négligeable.
:::

::: {.section}
#### Démonstration {#démonstration .proof}

L'ensemble $E$ étant dénombrable, il existe une suite de réels $x_n$
tels que $E = \{x_n \, | \, n \in \mathbb{N}\}$. La collection
d'intervalles $\left\{[x_i, x_i]\; | \;i \in \mathbb{N}\right\}$
recouvre $E$. Comme $$
\sum_{i=0}^{+\infty} \ell([x_i, x_i])
=
\sum_{i=0}^{+\infty} 0 
=
0,
$$ l'ensemble est donc négligeable.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Exercice -- Etre irrationnel ($\mathord{\bullet}$) {#ei .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Etre irrationnel}`{=latex}

Est-ce que la propriété "$x$ est irrationnel" est vraie presque partout
dans $\mathbb{R}$ ? ([Solution p.
`\pageref*{answer-ei}`{=tex}](#answer-ei){.no-parenthesis}.)
:::

::: {.section}
L'intégrale de Riemann possède des limitations qui en font un outil
mathématique difficile à exploiter. En particulier, la classe des
fonctions qui peuvent être intégrées est trop restrictive pour certaines
applications car les fonctions "trop grandes" ou "trop irrégulières" ne
sont pas intégrables.
:::

::: {.section}
### Théorème -- Critère d'intégrabilité de Lebesgue {#CIL .theorem .two .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Critère d'intégrabilité de Lebesgue}`{=latex}

La fonction $f:[a, b] \to \mathbb{R}$ est intégrable au sens de Riemann
si et seulement si $f$ est bornée et continue presque partout.
:::

::: {.section}
#### Démonstration {#démonstration-1 .proof}

Nous nous contentons de démontrer ici la partie la plus facile du
résultat, à savoir que seules les fonctions bornées sont potentiellement
intégrables. Pour le reste de la preuve, se reporter à [@Bur07, p. 58].

Soit $\delta > 0$ tel que pour toute subdivision pointée $\mathcal{D}$
de $[a, b]$ vérifiant $\ell(J) < \delta$ pour tout
$(t, J) \in \mathcal{D}$, on ait
$$\left|S(f, \mathcal{D}) - \int_a^b f(t) \, dt\right| \leq 1.$$ Soit
$\mathcal{D} = \{(t_i, [x_i, x_{i+1}])\; | \; i \in \{0, \dots, m-1\}\}$
une telle subdivision ; il est toujours possible de supposer en outre
que $\mathcal{D}$ ne contient aucun intervalle de longueur nulle
(enlever de tels intervalles engendre une nouvelle subdivision dont la
somme de Riemann est identique).

Soit $J_i = [x_i, x_{i+1}]$ un intervalle de $\mathcal{D}$ ; si l'on
définit $\mathcal{D}'$ à partir de $\mathcal{D}$ en remplaçant $t_i$ par
un $t$ de $J_i$ quelconque, on obtient $$
\begin{split}
|f(t) \ell(J_i) - f(t_i) \ell(J_i)| &=
|S(f, \mathcal{D}') - S(f, \mathcal{D})| \\
& \leq
\left|S(f, \mathcal{D}') - \int_a^b f(t) \, dt\right|
+
\left|S(f, \mathcal{D}) - \int_a^b f(t) \, dt\right| \\
& \leq 2
\end{split}
$$ et par conséquent, $$
|f(t)| \leq |f(t_i)| + \frac{2}{\ell(J_i)}.
$$ Les intervalles $J_i$ recouvrant $[a, b]$, on a pour tout
$t\in [a, b]$ $$
|f(t)| \leq \max \left\{|f(t_i)| + \frac{2}{\ell(J_i)} 
\, \left| \vphantom{\frac{2}{\ell(J_i)}} \right. \, i \in \{0, \dots, m-1\}\right\};
$$ la fonction $f$ est donc bornée.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
En particulier,
:::

::: {.section}
### Corollaire -- Les fonctions continues par morceaux sont intégrables {#les-fonctions-continues-par-morceaux-sont-intégrables .corollary .one .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Les fonctions continues par morceaux sont intégrables}`{=latex}

Si la fonction $f:[a, b] \to \mathbb{R}$ est continue par morceaux, elle
est intégrable au sens de Riemann.
:::

::: {.section}
#### Démonstration {#démonstration-2 .proof}

Les fonctions continues par morceaux sur un intervalle fermé borné sont
discontinues en un nombre fini de points, donc continues presque
partout ; elle sont également bornées. Par [le critère d'intégrabilité
de Lebesgue (p. `\pageref*{CIL}`{=tex})](#CIL), elles sont donc
intégrables au sens de Riemann.`\hfill$\blacksquare$`{=latex}
:::
:::

::: {.section}
Intégrales de Riemann généralisées
==================================

::: {.section}
### Définition -- Jauge {#jauge .definition .three .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Jauge}`{=latex}

Une *jauge* $\gamma$ sur un intervalle $[a, b]$ est une fonction qui
associe à tout $t \in [a, b]$ un intervalle ouvert $\gamma(t)$ contenant
$t$.

![Graphe de la jauge $\gamma(t) = \left]t/2-0.25, t+0.25 \right[,$
$t \in [0, 1 ].$](images/gauge-plot.py.pdf){#graphe-gauge}
:::

::: {.section}
### Définition -- Subdivision pointée subordonnée à une jauge {#subdivision-pointée-subordonnée-à-une-jauge .definition .two .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Subdivision pointée subordonnée à une jauge}`{=latex}

Une subdivision pointée $\mathcal{D}$ de l'intervalle $[a, b]$ est
*subordonnée à une jauge* $\gamma$ sur $[a, b]$ si pour tout
$(t, J) \in \mathcal{D}$, $J \subset \gamma(t).$

![Graphe de la jauge $\gamma(t) = \left]t/2-0.25, t+0.25 \right[,$
$t \in [0, 1 ]$ et de la subdivision pointée
$\{(0.1, [0, 0.2]), \dots, (0.9, [0.8, 1])\}$ ; les intervalles de la
subdivision sont délimités par des barres verticales et les points
associés représentés par des croix. La comparaison avec le graphe de la
jauge $\gamma$ montre que cette subdivision pointée lui est
subordonnée.](images/gauge-plot-subdivision.py.pdf)
:::

::: {.section}
### Remarque -- Représentation graphique des jauges {#représentation-graphique-des-jauges .two .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Représentation graphique des jauges}`{=latex}

On peut associer à une jauge $\gamma$ sur $[a, b]$ l'ensemble du plan $$
\{(x, y) \; | \; y \in [a, b], \, x \in \gamma(y) \}.
$$ Par construction, cet ensemble contient la diagonale
$D = \{(x,x) \; | \; x \in [a, b]\}.$ La représentation graphique de cet
ensemble permet de visualiser si une subdivision pointée est ou non
subordonnée à la jauge considérée.
:::

::: {.section}
La définition de l'intégrale de Henstock-Kurzweil est similaire à
l'intégrale de Riemann classique. Comme cette dernière, elle exploite
des sommes de Riemann pour fournir une estimation de l'intégrale et
contrôle la finesse des subdivisions employées pour améliorer la
précision de cette estimation ; mais contrairement à cette dernière,
elle permet de contrôler différemment cette finesse en fonction de la
région de l'intervalle d'intégration considérée.
:::

::: {.section}
### Définition -- Intégrale de Henstock-Kurzweil {#HK .definition .three .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Intégrale de Henstock-Kurzweil}`{=latex}

Une fonction $f:[a, b] \to \mathbb{R}$ est dite *intégrable au sens de
Henstock-Kurzweil* s'il existe un réel $A$ tel que pour tout
$\varepsilon > 0$, il existe une jauge $\gamma$ sur $[a, b]$ telle que,
pour toute subdivision pointée $\mathcal{D}$ de $[a, b]$ subordonnée à
$\gamma$, on ait $|S(f, \mathcal{D}) - A| \leq \varepsilon$. Le réel $A$
quand il existe est unique ; il est appelé *intégrale de
Henstock-Kurzweil de $f$ sur $[a, b]$* : $$
\mbox{(HK)}\!\!\int_a^b f(t) \, dt := A.
$$
:::

::: {.section}
L'intégrale de Henstock-Kurzweil est une intégrale extrêmement générale
qui apporte des réponses satisfaisantes à certaines questions que ses
concurrentes ne traitent qu'imparfaitement[^6]. Mais avec cette
puissance vient une certaine fragilité ; la plupart des mathématiciens
contemporains préfèrent opter pour une intégrale un peu moins expressive
mais un peu plus "confortable", l'intégrale de Lebesgue ; nous
adopterons également ce choix dans la suite : par défaut,
"intégrabilité" et "intégrale" seront à comprendre dans la suite comme
"au sens de Lebesgue". Nous utiliserons l'intégrale de Henstock-Kurzweil
uniquement comme un moyen efficace pour définir l'intégrale de
Lebesgue[^7].
:::

::: {.section}
### Définition -- Intégrale de Lebesgue {#Lebesgue .definition .two .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Intégrale de Lebesgue}`{=latex}

Une fonction $f:[a, b] \to \mathbb{R}$ est dite *intégrable (au sens de
Lebesgue)* si les fonctions $f$ et $|f|$ sont intégrables au sens de
Henstock-Kurzweil. *L'intégrale (de Lebesgue) de $f$ sur $[a, b]$*
coïncide alors avec l'intégrale de Henstock-Kurzweil : $$
\int_a^b f(t) \, dt := \mbox{(L)}\!\!\int_a^b f(t) \, dt
= \mbox{(HK)}\!\!\int_a^b f(t) \, dt.
$$
:::

::: {.section}
On trouvera dans la littérature ce type d'intégrale désignées par le
terme d'*intégrale de Riemann généralisée* ou d'*intégrale de
jauge*[^8]. L'intégrale de Henstock-Kurzweil est aussi appelée
*intégrale de Kurzweil-Henstock[^9]* ou *intégrale de
Denjoy-Perron-Kurzweil-Henstock*[^10].
:::

::: {.section}
L'intégrale de Henstock-Kurzweil présente le "défaut" d'être
*conditionnelle* : il est possible qu'une fonction
$f:[a, b] \to \mathbb{R}$ soit intégrable sans que sa valeur absolue
$|f|$ le soit (cf. exemple dans l'annexe du chapitre "Calcul Intégral
II"). Par construction, l'intégrale de Lebesgue n'a pas cet
inconvénient ; elle est dite *absolue* :
:::

::: {.section}
#### Exercice -- L'intégrale de Lebesgue est absolue ($\mathord{\boldsymbol{\circ}}$) {#lebesgue-absolue .exercise .question .zero .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{L'intégrale de Lebesgue est absolue}`{=latex}

Montrer que si $f: [a, b] \to \mathbb{R}$ est intégrable, alors $|f|$
est intégrable. ([Solution p.
`\pageref*{answer-lebesgue-absolue}`{=tex}](#answer-lebesgue-absolue){.no-parenthesis}.)
:::

::: {.section}
### Remarque -- Ordre des bornes de l'intégrale {#ordre-bornes .notation .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Ordre des bornes de l'intégrale}`{=latex}

Comme dans le cas de l'intégrale de Riemann, la notation désignant
l'intégrale peut être étendue sans difficulté au cas où $b < a$ ; on
définit alors l'intégrale de $a$ à $b$ en se ramenant au cas précédent,
par $$
\int_{a}^b f(t) \, dt := - \int_b^a f(t) \, dt.
$$
:::

::: {.section}
### Théorème -- Intégrale de Riemann et de Lebesgue {#RL .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Intégrale de Riemann et de Lebesgue}`{=latex}

Toute fonction $f:[a,b] \to \mathbb{R}$ intégrable au sens de Riemann
est intégrable (au sens de Lebesgue) et les deux intégrales coïncident.
$$
\int_a^b f(t) \, dt = \mbox{(R)}\!\!\int_a^b f(t) \, dt.
$$
:::

::: {.section}
#### Démonstration {#démonstration-3 .proof}

Soit $f:[a,b] \to \mathbb{R}$ une fonction intégrable au sens de
Riemann, d'intégrale $A$ ; soit $\varepsilon > 0$ et $\delta>0$ tels que
si la subdivision pointée $\mathcal{D}$ de $[a, b]$ est telle que pour
$(t, I) \in \mathcal{D}$, $\ell(J) < \delta$ alors
$|S(f,\mathcal{D}) - A| \leq \varepsilon$.

Considérons la jauge $\gamma$ sur $[a, b]$ définie par
$\gamma(t)= \left]t-\delta/2, t+\delta/2 \right[$. Si la subdivision
pointée $\mathcal{D}$ est subordonnée à $\gamma$, alors pour tout
$(t, J) \in \mathcal{D}$, on a
$J \subset \left]t-\delta/2, t+\delta/2 \right[$ ; par conséquent,
$\ell(J) < \delta$ et donc $|S(f,\mathcal{D}) - A| \leq \varepsilon$. La
fonction $f$ est donc intégrable au sens de Henstock-Kurzweil et
l'intégrale associée est égale à son intégrale de Riemann.

Par ailleurs, par le [critère d'intégrabilité de Lebesgue (p.
`\pageref*{CIL}`{=tex})](#CIL), comme $f$ est intégrable au sens de
Riemann, elle est bornée et continue presque partout. Sa valeur absolue
$|f|$ est donc également bornée et continue presque partout et donc
intégrable au sens de Riemann par le même critère. La fonction $f$ est
donc intégrable au sens de Lebesgue et $$
\int_a^b f(t) \, dt = \mbox{(HK)}\!\!\int_a^b f(t) \, dt = \mbox{(R)}\!\!\int_a^b f(t) \, dt.
$$`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Exemple -- Intégration de $x \mapsto e^x$ {#intégration-de-x-mapsto-ex .example .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Intégration de \(x \mapsto e^x\)}`{=latex}

La fonction $f: x \in [0, 1] \mapsto e^x \in \mathbb{R}$ est continue et
est sa propre primitive. Par [le théorème fondamental du calcul (p.
`\pageref*{TFCL}`{=tex})](#TFCL), on a donc $$
\int_0^1 e^x \,dx 
= 
\left[ x \mapsto e^x \right]_0^1
= e^1 - e^0 = e - 1. 
$$ Nous allons établir ce résultat directement, sans avoir recours au
théorème fondamental du calcul. Précisément, nous allons établir que
pour tout $\varepsilon > 0$, si $\gamma$ est la jauge sur $[0, 1]$
définie par $$
\gamma(t) = \left]t - \frac{\varepsilon}{2 e}, t + \frac{\varepsilon}{2 e}\right[
$$ et que la subdivision pointée $\mathcal{D}$ de $[0, 1]$ est
subordonnée à $\gamma$, alors
$|S(f, \mathcal{D}) - (e-1)| \leq \varepsilon$.

![Graphe de la jauge $\gamma$ garantissant une précision
$\varepsilon = 1/2$ à la somme de Riemann en tant qu'approximation de
l'intégrale de
$x \in [0,1] \mapsto e^x$.](images/gauge-plot-exp-2.py.pdf)

Soit $\mathcal{D}$ une telle subdivision pointée, que l'on suposera de
la forme
$$\mathcal{D} = \{(t_i, [x_i, x_{i+1}]) \; | \; \, i \in \{0, \dots, m-1\}\}$$
où la suite des $x_i$ est croissante. Comme $x_0 = 0$ et $x_m=1$, on a
`\begin{align*}
e - 1= e^{x_m} - e^{x_0} &= 
(e^{x_1} - e^{x_0}) + (e^{x_2} - e^{x_1}) + \dots + (e^{x_m} - e^{x_{m-1}}) \\
&= \sum_{i=0}^{m-1} (e^{x_{i+1}} - e^{x_i}) 
\end{align*}`{=tex} et donc `\begin{align*}
|S(f, \mathcal{D}) - (e - 1)|
&=\left|\sum_{i=0}^{m-1} e^{t_i} (x_{i+1}-x_i) - \sum_{i=0}^{m-1} (e^{x_{i+1}} - e^{x_i})\right| \\
&\leq 
\sum_{i=0}^{m-1} \left| e^{t_i} (x_{i+1}-x_i) - e^{x_{i+1}} + e^{x_i} \right|.
\end{align*}`{=tex} Posons $x=x_i$, $y=x_{i+1}$ et $t=t_i$. On remarque
que $$
e^{t} (y-x) - e^y + e^x = (e^t y - e^y) - (e^t x - e^x).
$$ La fonction $s \in [x, y] \mapsto e^t s - e^s$ étant dérivable de
dérivée $e^t - e^s$, par l'inégalité des accroissements finis, on
obtient $$
|e^{t} (y-x) - e^y + e^x| \leq \sup_{s \in [x, y]} |e^t - e^s| \times (y - x).
$$ Puis, en appliquant à nouveau l'inégalité des accroissements finis à
la fonction $\tau \in [x, y] \mapsto e^\tau$, de dérivée $e^{\tau}$, et
en utilisant l'inclusion $[x, y] \subset \gamma(t)$, on obtient $$
|e^t - e^s| \leq \sup_{\tau \in [x, y]} e^{\tau} \times |t - s| \leq e  \times (y - x)
\leq e \times \frac{\varepsilon}{e} = \varepsilon.
$$ Par conséquent, $|e^{t} (y-x) - e^y + e^x| \leq \varepsilon (y - x)$,
ce dont on déduit l'inégalité souhaitée : `\begin{align*}
|S(f, \mathcal{D}) - (e - 1)|
&\leq 
\sum_{i=0}^{m-1} \left| e^{t_i} (x_{i+1}-x_i) - e^{x_{i+1}} + e^{x_i} \right| \\
&\leq 
\sum_{i=0}^{m-1} \varepsilon (x_{i+1} - x_i) \\ &\leq \varepsilon.
\end{align*}`{=tex}
:::

::: {.section}
#### Exemple -- Intégration de $x \mapsto 1/\sqrt{x}$ {#iis .example .four .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Intégration de \(x \mapsto 1/\sqrt{x}\)}`{=latex}

Considérons la fonction $f:[0,1] \to \mathbb{R}$ définie par $$
f(x) = 
\left|
\begin{array}{rl}
1/\sqrt{x} & \mbox{si } \, x > 0, \\
0          & \mbox{si } \, x = 0.
\end{array}
\right.
$$ La difficulté de cet exemple est liée à la "singularité" de $f$ en
$x=0$, où la fonction est à la fois discontinue et localement
non-bornée. Si au lieu de l'intervalle $[0,1]$, on considère
l'intervalle $[a, 1]$ où $0 < a \leq 1$, la fonction $f$ restreinte à
$[a, 1]$ est continue donc intégrable et la fonction
$F: x \in [a, 1] \mapsto 2 \sqrt{x}$ en est une primitive. Elle y est
intégrable par [le théorème fondamental du calcul (p.
`\pageref*{TFCL}`{=tex})](#TFCL) et $$
\int_a^1 f(x) \, dx = \int_a^1 (2\sqrt{x})' \, dx
=
\left[ 2 \sqrt{x} \right]_a^1 = 2 \sqrt{1} - 2\sqrt{a}.
$$ Si $f$ est bien intégrable sur $[0,1]$, l'expression ci-dessus
suggère que son intégrale pourrait être $$
  \int_0^1 f(x) \, dx \stackrel{?}{=} 2\sqrt{1} - 2\sqrt{0} = 2.
  $$ Cette intuition est fondée : nous prouvons [en annexe (p.
`\pageref*{iis-proof}`{=tex})](#iis-proof) que si $\varepsilon > 0$, on
a $|S(f, \mathcal{D}) - 2| \leq \varepsilon$ quand $\mathcal{D}$ est
subordonnée à la jauge $\gamma$ définie par $$
\gamma(t) =
\left|
\begin{array}{cl}
\displaystyle \left]-1, \frac{\varepsilon^2}{16} \right[ & \mbox{si } t=0, \\
\displaystyle \left]
\frac{t}{\left(1+\varepsilon/\sqrt{t}\right)^2}, t \left(1+ \varepsilon \sqrt{t} \right)^2  \right[
& \mbox{si } t \in \left]0,1\right].
\end{array}
\right.
$$

![Graphe de la jauge $\gamma$ avec
$\varepsilon=0.5$](images/gauge-plot-sqrt.py.pdf)
:::
:::

::: {.section}
Propriétés élémentaires de l'intégrale
======================================

::: {.section}
### Théorème -- Théorème fondamental du calcul {#TFCL .theorem .one .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Théorème fondamental du calcul}`{=latex}

Soit $[a, b]$ un intervalle fermé borné de $\mathbb{R}$ ; si la fonction
$f:[a, b] \to \mathbb{R}$ est dérivable et que sa dérivée est intégrable
alors $$
[f]_a^b := f(b) - f(a) = \int_a^b f'(t) \, dt.
$$
:::

::: {.section}
#### Démonstration {#démonstration-4 .proof}

Si $f'$ existe et est intégrable (au sens de Lebesgue), alors elle est
par définition intégrable au sens de Henstock-Kurzweil et d'après la
forme générale [du théorème fondamental du calcul (p.
`\pageref*{TFC}`{=tex})](#TFC) en annexe, l'égalité souhaitée est
satisfaite.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Intégration de $x \mapsto e^x$ ($\mathord{\boldsymbol{\circ}}$) {#exp .question .exercise .zero .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Intégration de \(x \mapsto e^x\)}`{=latex}

Montrer que $$
\int_0^1 e^x \,dx 
= 
e - 1. 
$$

([Solution p.
`\pageref*{answer-exp}`{=tex}](#answer-exp){.no-parenthesis}.)
:::

::: {.section}
### Théorème -- Linéarité {#linéarité .theorem .one .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Linéarité}`{=latex}

Si $f: [a, b] \to \mathbb{R}$ et $g: [a, b] \to \mathbb{R}$ sont
intégrables et $\alpha \in \mathbb{R}$, alors $f+g$ et $\alpha f$ sont
intégrables. De plus, $$
\int_{a}^b f(t) + g(t) \, dt 
= 
\int_{a}^b f(t) \, dt +
\int_{a}^b g(t) \, dt
\;
\mbox{ et }
\;
\int_{a}^b \alpha f(t) \, dt
=
\alpha \int_{a}^b f(t) \, dt.
$$
:::

::: {.section}
#### Démonstration {#démonstration-5 .proof}

Supposons dans un premier temps uniquement que $f$ et $g$ sont
intégrables au sens de Henstock-Kurzweil. Si $\varepsilon > 0$, on peut
trouver des jauges $\gamma_f$ et $\gamma_g$ sur $[a, b]$ telles que pour
toute subdivision pointée $\mathcal{D}$ subordonnée à $\gamma_f$ et
$\gamma_g$, on ait $$
\left|S(f, \mathcal{D}) - \mbox{(HK)}\!\!\int_a^b f(t) \, dt \right| \leq \frac{\varepsilon}{2}
\; \mbox{ et } \;
\left|S(g, \mathcal{D}) - \mbox{(HK)}\!\!\int_a^b f(t) \, dt \right| \leq \frac{\varepsilon}{2}.
$$ Comme $S(f+g, \mathcal{D}) = S(f, \mathcal{D}) + S(g, \mathcal{D})$,
toute subdivision pointée $\mathcal{D}$ subordonnée à la jauge $\gamma$
définie par $\gamma(t) = \gamma_f(t) \cap \gamma_g(t)$ vérifie $$
\left|S(f+g, \mathcal{D}) - \left(\mbox{(HK)}\!\!\int_a^b f(t) \, dt + \mbox{(HK)}\!\!\int_a^b g(t) \, dt \right)  \right| \leq \varepsilon.
$$ La fonction $f+g$ est donc intégrable au sens de Henstock-Kurzweil et
son intégrale de Henstock-Kurzweil sur $[a, b]$ est la somme des
intégrales de Henstock-Kurzweil de $f$ et de $g$ sur $[a, b]$ : $$
\mbox{(HK)}\!\!\int_{a}^b f(t) + g(t) \, dt 
= 
\mbox{(HK)}\!\!\int_{a}^b f(t) \, dt +
\mbox{(HK)}\!\!\int_{a}^b g(t) \, dt.
$$

De façon similaire,
$S(\alpha f, \mathcal{D}) = \alpha S(f, \mathcal{D})$. Dans le cas où
$\alpha = 0$, il est clair que $\alpha f$ est intégrable au sens de
Henstock-Kurzweil et d'intégrale nulle ; dans le cas contraire, on peut
trouver une jauge $\gamma$ sur $[a, b]$ telle que pour toute subdivision
pointée $\mathcal{D}$ subordonnée à $\gamma$, on ait : $$
\left|S(f, \mathcal{D}) - \mbox{(HK)}\!\!\int_a^b f(t) \, dt \right| 
\leq 
\frac{\varepsilon}{|\alpha|}.
$$ On a alors $$
\left|S(\alpha f, \mathcal{D}) - \alpha \mbox{(HK)}\!\!\int_a^b f(t) \, dt \right| 
=
|\alpha| 
\left|S(f, \mathcal{D}) - \mbox{(HK)}\!\!\int_a^b f(t) \, dt \right| 
\leq 
\varepsilon.
$$ La fonction $\alpha f$ est donc intégrable au sens de
Henstock-Kurzweil sur $[a, b]$ et son intégrale est le produit de
$\alpha$ et de l'intégrale de Henstock-Kurzweil de $f$ sur $[a, b]$ : $$
\mbox{(HK)}\!\!\int_a^b \alpha f(t) \, dt =
\alpha \mbox{(HK)}\!\!\int_a^b f(t) \, dt.
$$

Pour établir les résultats correspondants avec l'intégrale de Lebesgue,
il nous suffit de montrer que si $f$ et $g$ sont intégrables au sens de
Lebesgue, alors c'est également le cas de $\alpha f$ et de $f+g$.

Pour $\alpha f$, il suffit de constater que $|\alpha f| = |\alpha||f|$ ;
$\alpha f$ et $|\alpha f|$ sont donc intégrables au sens de
Henstock-Kurzweil et $\alpha f$ est donc intégrable au sens de Lebesgue.

Concernant $f+g$, en introduisant la partie positive $x_+ := \max(x, 0)$
et négative $x_- := \min(-x, 0) = -(-x)_+$, on peut écrire que $$
|f+g| = (f+g)_+ + (f+g)_- = (f+g)_+ - (-f-g)_+
$$ Comme $f+g$ est intégrable au sens de Henstock-Kurzweil, que
$(f+g)_+ \leq |f|+|g|$ et que $|f|+ |g|$ est intégrable, [la partie
positive $(f+g)_+$ est intégrable (p. `\pageref*{fp}`{=tex})](#fp) ; le
même argument s'applique à $(-f-g)_+$. Donc $|f+g| = (f+g)_+ - (-f-g)_+$
est intégrable au sens de Henstock-Kurzweil ; les fonctions $f+g$ et
$|f+g|$ sont intégrables au sens de Henstock-Kurzweil, $f+g$ est donc
intégrable au sens de Lebesgue.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Intégration par parties ($\mathord{\bullet}$) {#ex-IPP .question .exercise .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Intégration par parties}`{=latex}

Montrer que si les fonctions $f:[a, b] \to \mathbb{R}$ et
$g:[a, b] \to \mathbb{R}$ sont dérivables, et que les fonctions $f'g$ et
$fg'$ sont intégrables, alors $$
\int_a^b f'(t)g(t) \, dt = [fg]_a^b - \int_a^b f(t) g'(t) \, dt.
$$

([Solution p.
`\pageref*{answer-ex-IPP}`{=tex}](#answer-ex-IPP){.no-parenthesis}.)
:::

::: {.section}
### Théorème -- Additivité {#additivité .theorem .one .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Additivité}`{=latex}

Si la fonction $f$ est définie et intégrable sur les intervalles
$[a, b]$ et $[b, c]$, alors elle est intégrable sur l'intervalle
$[a, c]$ et $$
\int_a^b f(t) \, dt + \int_b^c f(t) \, dt = \int_a^c f(t) \, dt.
$$
:::

::: {.section}
#### Démonstration {#démonstration-6 .proof}

Soit $\varepsilon > 0$. Si la fonction $f$ est intégrable (au sens de
Lebesgue) sur $[a, b]$ et $[b, c]$ alors les fonctions $f$ et $|f|$ y
sont intégrables au sens de Henstock-Kurzweil.

Concernant $f$ tout d'abord : il existe donc deux jauges
$\gamma_1:[a, b] \to \mathbb{R}$ et $\gamma_2:[b, c] \to \mathbb{R}$
telles que pour toutes les subdivisions pointées $\mathcal{D}_1$ et
$\mathcal{D}_2$ de $[a, b]$ et $[b, c]$ respectivement subordonnées à
$\gamma_1$ et $\gamma_2$, $$
\left| S(f, \mathcal{D}_1) - \mbox{(HK)}\!\!\int_a^b f(t) \, dt\right| \leq \varepsilon/2
\, \mbox{ et } \, 
\left| S(f, \mathcal{D}_2) - \mbox{(HK)}\!\!\int_b^c f(t) \, dt\right| \leq \varepsilon/2.
$$ Définissons la fonction $\gamma: [a, b] \to \mathcal{P}(\mathbb{R})$
par: $$
\gamma(x) = 
\left| 
\begin{array}{rl}
\gamma_1(x) \cap \left]-\infty, b \right[ & \mbox{ si } \, a < x < b, \\
\gamma_1(x) \cap \gamma_2(x) & \mbox{ si } \, x = b, \\
\gamma_2(x) \cap \left]b, +\infty\right[ & \mbox{ si } \, b < x < c. \\
\end{array}
\right.
$$ Par construction, cette fonction est une jauge sur $[a, c]$ (pour
tout $x \in [a, c]$, $\gamma(x)$ est un intervalle ouvert non vide de
$\mathbb{R}$ contenant $x$). Supposons que
$\mathcal{D} =\{(t_i, I_i) \; | \; i \in \{1,\dots, m\}\}$ soit une
subdivision pointée de $[a, c]$ subordonnée à $\gamma$. Admettons
temporairement que chaque intervalle $I_i$ appartienne à $[a, b]$ ou
bien dans le cas contraire à $[b, c]$. Les deux subdivisions pointées
$\mathcal{D}_1$ et $\mathcal{D}_2$ sont telles que $$
S(f, \mathcal{D}) = S(f, \mathcal{D}_1) + S(f, \mathcal{D}_2).
$$ Elles sont également subordonnées à $\gamma_1$ et $\gamma_2$
respectivement ; par conséquent $$
\left|
S(f, \mathcal{D}) 
- 
\mbox{(HK)}\!\!\int_a^b f(t) \, dt + \mbox{(HK)}\!\!\int_b^c f(t) \, dt 
\right|
\leq 
\varepsilon. 
$$

Si notre hypothèse temporaire n'est pas vérifiée, c'est qu'il existe un
(unique) intervalle $I_i$ à cheval sur $[a, b]$ et $[b, c]$,
c'est-à-dire d'intersection non vide avec $\left[a, b\right[$ et avec
$\left]b, c\right]$. La jauge $\gamma$ a été choisie de telle sorte que
si $x \neq b$, alors $b \not \in \gamma(x)$ ; par conséquent, si cet
intervalle $I_i=[d_i, e_i]$ existe, alors $t_i = b$ et on peut remplacer
le terme $(t_i, I_i)$ dans la subdivision pointée $\mathcal{D}$ par
$(b, [d_i, b])$ et $(b, [b, e_i])$ sans que la somme de Riemann associée
change (le terme $f(b) \ell([d_i, e_i])$ étant égal à
$f(b) \ell([d_i, b]) + f(b) \ell([b, e_i])$). La nouvelle subdivision
$\mathcal{D}'$ ainsi construite vérifie quant à elle l'hypothèse de
non-chevauchement de $b$. Par conséquent l'inégalité ci-dessus est
satisfaite dans le cas général. La fonction $f$ est donc intégrable au
sens de Henstock-Kurzweil sur $[a, b]$ et $$
\mbox{(HK)}\!\!\int_a^b f(t) \, dt + \mbox{(HK)}\!\!\int_b^c f(t) \, dt = \mbox{(HK)}\!\!\int_a^c f(t) \, dt.
$$ L'intégrabilité de $|f|$ se montre de la même façon que celle de
$f$ ; la fonction $f$ est donc intégrable (au sens de Lebesgue) sur
$[a, b]$ et $$
\int_a^b f(t) \, dt + \int_b^c f(t) \, dt = \int_a^c f(t) \, dt.
$$`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
[La propriété d'additivité (p.
`\pageref*{additivituxe9}`{=tex})](#additivité) de l'intégrale -- qui
permet de prouver l'intégrabilité de l'intégrale sur un intervalle à
partir de son intégrabilité sur des intervalles qui la compose -- admet
une réciproque :
:::

::: {.section}
#### Exercice -- Ordre des bornes et additivité ($\mathord{\bullet}$) {#exo-odb .exercise .one .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Ordre des bornes et additivité}`{=latex}

Adapter l'énoncé [du théorème d'additivité (p.
`\pageref*{additivituxe9}`{=tex})](#additivité) pour traiter les cas où
l'on n'a pas nécessairement $a \leq b \leq c$. (On pourra par exemple se
limiter aux cas $c \leq b \leq a$ et $a \leq c \leq b$.) ([Solution p.
`\pageref*{answer-exo-odb}`{=tex}](#answer-exo-odb){.no-parenthesis}.)
:::

::: {.section}
### Théorème -- Restriction {#restriction .theorem .one .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Restriction}`{=latex}

Si $f$ est intégrable sur l'intervalle $[a, b]$, elle est intégrable sur
tout intervalle $[c, d]$ inclus dans $[a, b]$.
:::

::: {.section}
#### Démonstration {#démonstration-7 .proof}

Nous démontrons en détail le cas où $c = a$ ; le cas où $d=b$ se prouve
de façon similaire et le cas général se déduit facilement de la
combinaison de ces deux cas particuliers. Par hypothèse $f$ est
intégrable sur $[a, b]$, donc $f$ et $|f|$ sont intégrables au sens de
Henstock-Kurzweil sur $[a, b]$.

Soit $\varepsilon > 0$. Par le [critère d'intégrabilité de Cauchy (p.
`\pageref*{CIC}`{=tex})](#CIC), il existe une jauge $\gamma$ sur
$[a, b]$ telle que pour tout couple de subdivisions pointées
$\mathcal{D}$ et $\mathcal{D}'$ subordonnées à $\gamma$, on ait
$|S(f, \mathcal{D}) - S(f, \mathcal{D}')| \leq \varepsilon.$

Considérons les restrictions $\gamma_1$ et $\gamma_2$ de $\gamma$ à
$[a, d]$ et $[d, b]$ respectivement. Soient $\mathcal{D}_1$ et
$\mathcal{D}_1'$ deux subdivisions pointées de $[a, d]$ subordonnées à
$\gamma_1$ ; si $\mathcal{D}_2$ est une subdivision de $[d, b]$
subordonnée à $\gamma_2$, alors $\mathcal{D}_1 \cup \mathcal{D}_2$ et
$\mathcal{D}'_1 \cup \mathcal{D}_2$ sont des subdivisions pointées de
$[a, b]$ subordonnées à $\gamma$. Par conséquent, $$
|S(f, \mathcal{D}_1 \cup \mathcal{D}_2) 
- S(f, \mathcal{D}'_1 \cup \mathcal{D}_2)|
\leq \varepsilon.
$$ Or
$S(f, \mathcal{D}_1 \cup \mathcal{D}_2) = S(f, \mathcal{D}_1) + S(f, \mathcal{D}_2)$
et
$S(f, \mathcal{D}_1' \cup \mathcal{D}_2) = S(f, \mathcal{D}_1') + S(f, \mathcal{D}_2)$,
par conséquent $$
|S(f, \mathcal{D}_1) - S(f, \mathcal{D}_1')|
\leq \varepsilon.
$$ Par le [critère d'intégrabilité de Cauchy (p.
`\pageref*{CIC}`{=tex})](#CIC), la fonction $f$ est donc intégrable au
sens de Henstock-Kurzweil sur l'intervalle $[a, d]$. De la même façon,
on montre que $|f|$ est intégrable au sens de Henstock-Kurzweil sur
l'intervalle $[a, d]$. La fonction $f$ est donc intégrable (au sens de
Lebesgue) sur l'intervalle $[a, d]$.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Proposition -- Croissance de l'intégrale {#croissance .proposition .one .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Croissance de l'intégrale}`{=latex}

Si $f: [a, b] \to \mathbb{R}$ et $g :[a, b] \to \mathbb{R}$ sont
intégrables et que $f \leq g$, alors $$
\int_a^b f(t) \, dt \leq \int_a^b g(t)\,dt.
$$
:::

::: {.section}
#### Démonstration {#démonstration-8 .proof}

Par [linéarité de l'intégrale (p.
`\pageref*{linuxe9arituxe9}`{=tex})](#linéarité), il suffit de montrer
que si $h = g-f$ est intégrable et positive alors son intégrale est
positive. Soit $\varepsilon > 0$ et $\gamma$ une jauge telle que toute
subdivision pointée $\mathcal{D}$ de $[a, b]$ subordonnée à $\gamma$
vérifie $$
\left|S(f, \mathcal{D}) - \int_a^b h(t) \, dt\right| \leq \varepsilon.
$$ Quelle que soit la subdivision pointée $\mathcal{D}$ de $[a, b]$, la
somme de Riemann associée $$
S(f, \mathcal{D})
= \sum_{(t,J) \in \mathcal{D}} h(t) \ell(J)
$$ est positive, ce qui entraîne par l'inégalité triangulaire $$
\int_a^b h(t) \, dt  \geq S(h, \mathcal{D}) - \varepsilon \geq -\varepsilon.
$$ Le nombre strictement positif $\varepsilon$ pouvant être choisi
arbitrairement petit, on en déduit que l'intégrale est
positive.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Corollaire -- Inégalité triangulaire {#inégalité-triangulaire .corollary .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Inégalité triangulaire}`{=latex}

Si $f: [a, b] \to \mathbb{R}$ est intégrable alors $|f|$ est intégrable
et $$
\left|\int_a^b f(t) \, dt \right| \leq \int_a^b |f(t)|\,dt.
$$
:::

::: {.section}
#### Démonstration {#démonstration-9 .proof}

Si $f$ est intégrable, $f$ et $|f|$ sont intégrables au sens de
Henstock-Kurzweil donc $|f|$ et $||f|| = |f|$ sont intégrables au sens
de Henstock-Kurzweil ; la fonction $|f|$ est donc intégrable. [Par
linéarité (p. `\pageref*{linuxe9arituxe9}`{=tex})](#linéarité), $-f$ est
également intégrable. Comme $f \leq |f|$ et $-f \leq f$, on a [par
croissance de l'intégrale (p.
`\pageref*{croissance}`{=tex})](#croissance) $$
\int_a^b f(t) \, dt \leq \int_a^b |f(t)| \, dt
$$ et [par linéarité (p.
`\pageref*{linuxe9arituxe9}`{=tex})](#linéarité) et [croissance (p.
`\pageref*{croissance}`{=tex})](#croissance) de l'intégrale $$
-\int_a^b f(t) \, dt = \int_a^b -f(t) \, dt \leq \int_a^b |f(t)| \, dt,
$$ ce qui établit l'inégalité
triangulaire.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Exercice -- Lemme M-L ($\mathord{\bullet}$) {#ML .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Lemme M-L}`{=latex}

Montrer que si la fonction $f:[a, b] \to \mathbb{R}$ est intégrable et
que $|f| \leq M$, alors $$
\left|\int_a^b f(t) \, dt \right| \leq M (b-a)
$$

([Solution p.
`\pageref*{answer-ML}`{=tex}](#answer-ML){.no-parenthesis}.)
:::

::: {.section}
### Proposition -- Fonctions égales presque partout {#fepp .proposition .two .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Fonctions égales presque partout}`{=latex}

Une fonction $f:[a, b] \to \mathbb{R}$ égale presque partout à une
fonction $g:[a, b] \to \mathbb{R}$ intégrable est elle-même intégrable
et $$
\int_a^b f(t) \, dt = \int_a^b g(t) \, dt.
$$
:::

::: {.section}
#### Exercice -- Fonctions égales sur un ensemble co-dénombrable ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#feppco .exercise .question .four .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Fonctions égales sur un ensemble co-dénombrable}`{=latex}

Démontrer la proposition ["Fonctions égales presque partout" (p.
`\pageref*{fepp}`{=tex})](#fepp) sous l'hypothèse renforcée suivante :
$f$ et $g$ diffèrent en un nombre dénombrable de points. ([Solution p.
`\pageref*{answer-feppco}`{=tex}](#answer-feppco){.no-parenthesis}.)
:::

::: {.section}
#### Démonstration -- Fonctions égales presque partout {#démonstration-fonctions-égales-presque-partout .proof}

[Par linéarité de l'intégrale (p.
`\pageref*{linuxe9arituxe9}`{=tex})](#linéarité), il suffit d'établir
que si $h = g - f$ est nulle presque partout (c'est-à-dire égale presque
partout à la fonction $[a, b] \to \mathbb{R}$ identiquement nulle),
alors elle est intégrable et d'intégrale nulle.

Supposons dans un premier temps que $h$ soit bornée. Alors, pour tout
$\varepsilon > 0$, il existe un recouvrement de $$
A = h^{-1}(\mathbb{R}\setminus \{0\}) = \{x \in [a, b] \, | \, h(x) \neq 0\}
$$ par une collection dénombrable d'intervalles $I_i$ telle que
$\sum_i \ell(I_i) \leq \varepsilon$. Il est de plus possible de supposer
les $I_i$ ouverts[^11]. Définissons la jauge $\gamma$ sur $[a, b]$ par
$$
\gamma(t) = I_i \, \mbox{ si } \, t \in I_i \;
\mbox{et } \, t \not \in I_j \mbox{ quand } \, j \leq i
$$ et par exemple $\gamma(t) = \left]-\infty,\infty\right[$ si
$t \not \in \cup_i I_i$. Pour toute subdivision pointée
$\mathcal{D} = \{(t_j, J_j)\}_j$ de $[a, b]$ subordonnée à $\gamma$, $$
\left|S(h, \mathcal{D})\right| 
= \left|\sum_j h(t_j) \ell(J_j)\right|
= \left|\sum_{t_j \in A} h(t_j) \ell(J_j)\right|
\leq \sup_{[a, b]} |h| \times \sum_j \ell(J_j).
$$ Par construction les $J_j$ ne se chevauchent pas et sont tous inclus
dans un des intervalles $I_i$. On a donc $$
\sum_j \ell(J_j) \leq  \sum_i \ell(I_i) \leq \varepsilon.
$$ Il suffit par conséquent de choisir un $\varepsilon$ suffisamment
petit initialement pour rendre la somme de Riemann associée
arbitrairement petite ; $h$ est donc intégrable d'intégrale nulle.

Si $h$ est non-bornée, on peut faire une démonstration similaire en
considérant les ensembles $$
A_k = \{x \in [a, b] \, | \, k < |h(x)| \leq k+1\},
$$ puis en associant à chaque $A_k$ un recouvrement par une collection
dénombrable d'intervalles ouverts $I^k_i$ tels que $$
\sum_i \ell(I^k_i) \leq \frac{\varepsilon}{(k+1)2^{k+1}}
$$ ce qui est possible puisque tous les $A_k$ sont négligeables. On
définit alors la jauge $\gamma$ sur $[a, b]$ par $\gamma(t) = I^k_i$ si
$t$ appartient à un $I^k_i$ (et on choisit alors le plus petit $k$, puis
le plus petit $i$ telle que cette propriété soit vérifiée) et par
exemple $\gamma(t) = \left]-\infty,\infty\right[$ si
$t \not \in \cup_k \cup_i I^k_i$. L'évaluation d'une somme de Riemann
pour une subdivision pointée subordonnée à cette jauge fournit $$
\left|S(h, \mathcal{D})\right| 
= \left|\sum_j h(t_j) \ell(J_j)\right|
= \left|\sum_k \sum_{t_j \in A_k} h(t_j) \ell(J_j)\right| \leq
\sum_k \sum_{t_j \in A_k} (k+1) \ell(J_j)
$$ et comme $$
\sum_{t_j \in A_k} \ell(J_j) 
\leq  \sum_i \ell(I^k_i) 
\leq \frac{\varepsilon}{(k+1)2^{k+1}},
$$ on obtient $$
\left|S(h, \mathcal{D})\right| 
\leq
\sum_k (k+1) \sum_{i} \ell(I^k_i)
\leq 
\sum_k \frac{\varepsilon}{2^{k+1}} 
= \varepsilon.
$$ La fonction $h$ est donc bien intégrable et d'intégrale
nulle.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
Sous une hypothèse d'inégalité, la proposition ["Fonction égales presque
partout" (p. `\pageref*{fepp}`{=tex})](#fepp) admet une réciproque :
:::

::: {.section}
### Proposition -- Fonctions égales presque partout (réciproque) {#fepp-réciproque .proposition .two .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Fonctions égales presque partout (réciproque)}`{=latex}

Si les fonctions $f:[a,b] \to \mathbb{R}$ et $g:[a, b] \to \mathbb{R}$
sont intégrables et si $$
f \leq g \, \mbox{ presque partout} 
\; \mbox{ et } \;
\int_a^b f(t) \, dt \geq \int_a^b g(t) \, dt,
$$ alors $f = g$ presque partout.
:::

::: {.section}
#### Démonstration {#démonstration-10 .proof}

La fonction $h = g - f$ étant intégrable, pour tout $x \in [a, b]$, [ses
restrictions à $[a, x]$ et $[x, b]$ sont intégrables (p.
`\pageref*{restriction}`{=tex})](#restriction). Comme il s'agit de
fonctions positives, $$
\int_a^x h(t) \, dt \geq 0 \; \mbox{ et } \; \int_x^b h(t) \, dt \geq 0.
$$ Comme [par additivité (p.
`\pageref*{additivituxe9}`{=tex})](#additivité) $$
\int_a^x h(t) \, dt + \int_x^b h(t) \, dt = \int_a^b h(t) \, dt 
=  \int_a^b g(t) \, dt  - \int_a^b f(t) \, dt \leq 0,
$$ chacune de ces intégrales est nulle. La fonction $$
x \in [a, b] \mapsto \int_a^x h(t) \, dt
$$ est donc identiquement nulle. Or, [sa dérivée existe et vaut $h$
presque partout (p. `\pageref*{dii}`{=tex})](#dii) ; la fonction $h$ est
donc nulle presque partout, c'est-à-dire que $f=g$ presque
partout.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Théorème -- Continuité des intégrales indéterminées {#cii .theorem .one .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Continuité des intégrales indéterminées}`{=latex}

Pour toute fonction $f: [a, b] \to \mathbb{R}$ intégrable et pour tout
$c \in [a, b]$, la fonction $$
g : x \in [a, b] \mapsto \int_c^x f(t) \, dt 
$$ est continue.
:::

::: {.section}
#### Exercice -- Continuité des intégrales indéterminées simplifiée ($\mathord{\bullet}\mathord{\bullet}$) {#exo-ciis .exercise .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Continuité des intégrales indéterminées simplifiée}`{=latex}

Démontrer [le théorème de continuité des intégrales indéterminées (p.
`\pageref*{cii}`{=tex})](#cii) sous l'hypothèse supplémentaire que $f$
est bornée. ([Solution p.
`\pageref*{answer-exo-ciis}`{=tex}](#answer-exo-ciis){.no-parenthesis}.)
:::

::: {.section}
#### Démonstration -- Continuité des intégrales indéterminées {#démonstration-continuité-des-intégrales-indéterminées .proof}

Montrons la continuité de l'intégrale à droite en $x$ quand $x < b$ (la
continuité à gauche peut être établie de façon similaire quand $x>a$).
Par [additivité de l'intégrale (p.
`\pageref*{additivituxe9}`{=tex})](#additivité), il suffit de montrer
que la grandeur $$
\int_x^{x+h} f(t) \, dt
$$ tend vers $0$ quand $h>0$ tend vers $0$. Par [restriction (p.
`\pageref*{restriction}`{=tex})](#restriction), la fonction $f$ est
intégrable sur $[x, b]$ : pour tout $\varepsilon > 0$, il existe une
jauge $\gamma$ sur $[x, b]$ telle que pour toute subdivision pointée
$\mathcal{D}$ de $[x, b]$ subordonnée à $\gamma$, l'écart entre la somme
de Riemann $S(f,\mathcal{D})$ et l'intégrale de $f$ entre $x$ et $b$ est
au plus $\varepsilon/2$.

On peut remplacer $\gamma$ par une jauge $\nu$ telle que
$\nu(x) \subset \gamma(x)$ et
$\nu(t) = \gamma(t) \cap \left]x,+\infty\right]$ sinon ; cela garantit
que pour tout subdivision pointée $\mathcal{D}$ subordonnée à $\nu$,
$\mathcal{D}$ est subordonnée à $\gamma$ et que si
$(t,J) \in \mathcal{D}$ et $x \in J$, alors $t=x$.

[Le lemme de Henstock (p.
`\pageref*{henstock-lemma}`{=tex})](#henstock-lemma), appliqué à toute
subdivision partielle $\mathcal{D} = \{(x, [x, x+h])\}$ subordonnée à
$\nu$, c'est-à-dire telle que $[x, x+h] \subset \nu(x)$, fournit $$
\left| 
f(x) h - \int_x^{x+h} f(t) \, dt
\right| \leq \frac{\varepsilon}{2},
$$ dont on déduit par l'inégalité triangulaire que $$
\left| \int_x^{x+h} f(t) \, dt \right|
\leq
\frac{\varepsilon}{2} + |f(x)|h.
$$ Il suffit donc de choisir $\nu(x)$ tel que
$|f(x)| h \leq \varepsilon / 2$ quand $[x, x+h] \subset \nu(x)$ pour
s'assurer que $$
\left| \int_x^{x+h} f(t) \, dt \right|
\leq
\varepsilon.
$$`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Exercice -- Limite d'intégrale ($\mathord{\bullet}$) {#exo-cii .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Limite d'intégrale}`{=latex}

Montrer que $$
\lim_{\varepsilon \to 0} \int_0^{\varepsilon} \frac{dt}{\sqrt{t}} = 0.
$$

([Solution p.
`\pageref*{answer-exo-cii}`{=tex}](#answer-exo-cii){.no-parenthesis}.)
:::

::: {.section}
### Théorème -- Dérivabilité des intégrales indéterminées {#dii .theorem .two .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Dérivabilité des intégrales indéterminées}`{=latex}

Pour toute fonction $f: [a, b] \to \mathbb{R}$ intégrable et pour tout
$c \in [a, b]$, la fonction $$
g: x \in [a, b] \mapsto \int_c^x f(t) \, dt 
$$ est dérivable presque partout et pour presque tout $x \in [a, b]$, $$
g'(x) = f(x).
$$
:::

::: {.section}
#### Démonstration {#démonstration-11 .proof}

Voir [@Swa01, pp. 135-136].`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Exercice -- Dérivabilité presque partout ($\mathord{\bullet}$) {#dpp .exercise .one .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Dérivabilité presque partout}`{=latex}

Construire une fonction $f:[0, 1] \to \mathbb{R}$ qui soit intégrable et
telle que $$
x \in [0, 1] \mapsto \int_0^x f(t) \, dt
$$ ne soit pas dérivable en tout point de $[0, 1]$. ([Solution p.
`\pageref*{answer-dpp}`{=tex}](#answer-dpp){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Normalisation des fonctions ($\mathord{\bullet}\mathord{\bullet}$) {#pl .exercise .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Normalisation des fonctions}`{=latex}

Soit $f: [a, b] \to \mathbb{R}$ une fonction intégrable. On associe à
$f$ la fonction $g$ "filtrée" qui vaut $$
g(t) = \lim_{\substack{h \to 0 \\ h \neq 0}} \frac{1}{2h}\int_{t-h}^{t+h} f(x) \, dx
$$ si le membre de droite est défini, et $f(t)$ sinon. Montrer que $g$
est égale à $f$ presque partout. ([Solution p.
`\pageref*{answer-pl}`{=tex}](#answer-pl){.no-parenthesis}.)
:::

::: {.section}
### Théorème -- Changement de variable {#changement-de-variable .theorem .three .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Changement de variable}`{=latex}

Soit $g :[a, b] \to \mathbb{R}$ une fonction continue en $a$ et en $b$,
dont la dérivée $g'$ existe sur $\left]a, b\right[$, y est continue et
ne s'y annule pas. Soit $[c, d] = g([a, b])$ et
$f: [c, d] \to \mathbb{R}$. Alors la fonction $f$ est intégrable sur
$[c, d]$ si et seulement si $(f\circ g) g'$ est intégrable sur $[a, b]$
et dans ce cas, on a $$
\int_a^b f(g(t)) g'(t)\, dt = \int_{g(a)}^{g(b)} f(x) \, dx.
$$
:::

::: {.section}
Le calcul différentiel nous a accoutumé à noter le terme $g'(t) dt$ sous
la forme $dg(t)$. Si l'on réutilise ici cette convention, le changement
de variable $x = g(t)$ peut donc être mémorisé sous la forme $$
\int_a^b f(g(t)) dg(t) = \int_{g(a)}^{g(b)} f(x) \, dx.
$$
:::

::: {.section}
On notera que le terme $f(g(t)) g'(t)$ n'est a priori pas défini en
$t=a$ et $t=b$ ; on pourra considérer que l'intégrande vaut $0$ en ces
points, ou plus généralement une valeur quelconque : l'intégrabilité de
la fonction ainsi que son intégrale ne dépendent pas de ce choix, car
ils définissent des [fonctions qui sont égales presque partout (p.
`\pageref*{fepp}`{=tex})](#fepp).
:::

::: {.section}
Les hypothèses concernant le changement de variable $g$ peuvent se
reformuler de la façon suivante: $g:[a, b] \to \mathbb{R}$ est continue
en $a$ et $b$ et est un $C^1$-difféomorphisme de $\left]a, b\right[$ sur
$\left]c, d\right[$.
:::

::: {.section}
#### Démonstration {#démonstration-12 .proof}

Le résultat est un corollaire du théorème de changement de variable dans
$\mathbb{R}^n$ qui sera étudié dans le chapitre calcul intégral
III.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Exercice -- Changement de variables simplifié ($\mathord{\bullet}\mathord{\bullet}$) {#cv .exercise .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Changement de variables simplifié}`{=latex}

Démontrer [le théorème de changement de variables (p.
`\pageref*{changement-de-variable}`{=tex})](#changement-de-variable) au
moyen [du théorème fondamental du calcul (p.
`\pageref*{TFC}`{=tex})](#TFC), sous les hypothèses supplémentaires que
$f$ et $g'$ existent et sont continues sur $[c, d]$ et $[a,b]$
respectivement. (Indication: $f$ étant continue sur $[c, d]$, elle y
admet une primitive $h$.) ([Solution p.
`\pageref*{answer-cv}`{=tex}](#answer-cv){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Changement de variable $x=t^2$ ($\mathord{\bullet}$) {#ft2 .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Changement de variable \(x=t^2\)}`{=latex}

Soit $f:[0,1] \to \mathbb{R}$ une fonction intégrable. Montrer que
l'intégrale $$
\int_0^1 f(x) \, dx
$$ peut s'exprimer comme une intégrale faisant intervenir l'expression
$f(t^2)$. ([Solution p.
`\pageref*{answer-ft2}`{=tex}](#answer-ft2){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Changement de variable $x=\sqrt{t}$ ($\mathord{\bullet}$) {#fst .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Changement de variable \(x=\sqrt{t}\)}`{=latex}

Soit $f:[0, 1] \to \mathbb{R}$ ; en supposant qu'elle soit bien définie,
calculer l'intégrale $$
\int_0^1 f(\sqrt{t}) \, dt
$$ en faisant intervenir une intégrale portant sur $f(x)$. ([Solution p.
`\pageref*{answer-fst}`{=tex}](#answer-fst){.no-parenthesis}.)
:::
:::

::: {.section}
Intégration sur des intervalles arbitraires
===========================================

Dans cette section, nous allons étendre -- significativement, mais avec
très peu d'efforts -- la théorie de l'intégration sur les intervalles
fermés bornés de $\mathbb{R}$ à des intervalles arbitraires de
$\mathbb{R}$, et en particulier à $\mathbb{R}$ tout entier[^12].

La première étape de cette démarche consiste à prolonger une fonction
définie sur un intervalle quelconque de $\mathbb{R}$, par exemple un
intervalle ouvert $\left]a,b\right[$, en une fonction définie sur
l'intervalle $[a, b]$ en lui assignant la valeur $0$ aux extrémités de
l'intervalle.

$$
f: \left]a,b\right[ \to  \mathbb{R}\; \mapsto \; \bar{f}:\left[a,b\right] \to \mathbb{R}, \,
\bar{f}(x) = \left|
\begin{array}{rl}
f(x) & \mbox{si $x \in \left]a,b\right[$,} \\
0 & \mbox{si $x \in \{a, b\}$.}
\end{array}
\right.
$$

Une fonction $f$ définie sur un intervalle $I$ quelconque de
$\mathbb{R}$ sera alors dite intégrable sur $I$ si son extension
$\bar{f}$ sur l'intervalle fermé $\bar{I}$ correspondant l'est, et
l'intégrale de $f$ sur $I$ est alors *définie* comme l'intégrale de
$\bar{f}$ sur $\bar{I}$.

Si l'intervalle initial est borné, on s'est ramené au cas déjà étudié
des intervalles fermés et bornés de $\mathbb{R}$. Mais si l'intervalle
initial est non-borné, par exemple
$\mathbb{R}= \left]-\infty, +\infty \right[$, cette même technique
suppose d'introduire une fonction définie sur la droite réelle étendue
$[-\infty, +\infty]$.

::: {.section}
### Définition -- Intervalle de $[-\infty,+\infty]$ {#intervalle-de--inftyinfty .definition .one .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Intervalle de \([-\infty,+\infty]\)}`{=latex}

On appelle *intervalle* de $[-\infty,+\infty]$ tout sous-ensemble $I$ de
$[-\infty,+\infty]$ tel que si $x$ et $y$ appartiennent à $I$ et
vérifient $x \leq y$ et si $z$ est un point intermédiaire -- tel que
$x \leq z \leq y$ -- alors $z$ appartient également à $I$.
:::

::: {.section}
Les intervalles de $\left]-\infty,+\infty \right[$ peuvent être ouverts,
fermés, ouverts et fermés ou ni l'un ni l'autre. Les intervalles de la
forme $\left[-\infty, +\infty\right]$, $\left]-\infty, +\infty\right[$
(c'est-à-dire $\mathbb{R}$), $\left]-\infty, b\right[$,
$\left[-\infty, b\right[$, $\left]a,+\infty\right[$,
$\left]a,+\infty\right]$ et $\left]a,b\right[$ -- où $a$ et $b$
désignent des nombres réels étendus -- sont ouverts. Les intervalles de
la forme $\left[a,b \right]$ sont fermés. Tous les intervalles de
$[-\infty,+\infty]$ sont bornés, avec comme majorant $+\infty$ et comme
minorant $-\infty$.
:::

::: {.section}
### Définition -- Longueur d'un intervalle de $[-\infty,+\infty]$ {#longueur-dun-intervalle-de--inftyinfty .definition .one .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Longueur d'un intervalle de \([-\infty,+\infty]\)}`{=latex}

La *longueur* $\ell(I)$ d'un intervalle $I$ de $[-\infty, +\infty]$ est
le nombre réel étendu positif défini par $$
\ell(I) := \ell(I \cap \mathbb{R}).
$$ En particulier avec cette convention,
$\ell([-\infty, -\infty]) = \ell([+\infty, +\infty])= \ell(\varnothing) = 0$.

La notion d'ensemble négligeable de $[-\infty, +\infty]$ est identique à
celle [d'ensemble négligeable de $\mathbb{R}$ (p.
`\pageref*{ensemble-nuxe9gligeable}`{=tex})](#ensemble-négligeable) à
ceci près qu'il faut remplacer les intervalles de $\mathbb{R}$ par ceux
de $[-\infty, +\infty]$ dans la définition.

[La définition de subdivision pointée (p. `\pageref*{sp}`{=tex})](#sp)
reste formellement inchangée en passant des intervalles fermés bornés de
$\mathbb{R}$ aux intervalles fermés bornés de $[-\infty, +\infty]$. Il
en est de même pour [la définition d'une jauge (p.
`\pageref*{jauge}`{=tex})](#jauge) si l'on interprète "un intervalle
ouvert $\gamma(t)$ contenant $t$" comme il se doit par "un intervalle
ouvert $\gamma(t)$ de $[-\infty, +\infty]$ contenant $t$".
:::

::: {.section}
Le travail central consiste à redéfinir la somme de Riemann, car il faut
se prémunir contre les termes $f(t) \ell(I)$ infinis qui pourraient
engendrer une somme de Riemann infinie ou même indéfinie.
:::

::: {.section}
### Définition -- Somme de Riemann (extension) {#somme-de-riemann .definition .two .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Somme de Riemann (extension)}`{=latex}

Soit $[a, b] \subset [-\infty, +\infty]$. La somme de Riemann associée à
la fonction $f:[a, b] \to \mathbb{R}$ et à la subdivision pointée
$\mathcal{D}$ de $[a, b]$ est la grandeur $$
S(f, \mathcal{D}) := \sum f(t) \ell(I) 
\; \mbox{ où } \; 
(t, I) \in \mathcal{D}
\mbox{ et } 
\ell(I) < +\infty.
$$
:::

::: {.section}
Avec cette extension de la somme de Riemann, [la définition de
l'intégrale de Henstock-Kurzweil (p. `\pageref*{HK}`{=tex})](#HK) et [de
Lebesgue (p. `\pageref*{Lebesgue}`{=tex})](#Lebesgue) restent
formellement inchangées.
:::

::: {.section}
#### Exemple -- Intégration de $x \mapsto 1/x^2$ {#intégration-de-x-mapsto-1x2 .example .three .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Intégration de \(x \mapsto 1/x^2\)}`{=latex}

Considérons la fonction $f:\left[1, +\infty\right[ \to \mathbb{R}$
définie par $$
f(x) = \frac{1}{x^2}.
$$ On étend immédiatement cette fonction sur $[1, +\infty]$ en posant
$f(+\infty)=0$ (on note toujours $f$ la fonction qui en résulte). La
fonction $f$ est continue et admet comme primitive $x \mapsto -1/x$ sur
toute intervalle borné $[a, b]$ de $\left[1, +\infty \right[$. Par [le
théorème fondamental du calcul (p. `\pageref*{TFC}`{=tex})](#TFC), on a
donc $$
\int_a^b f(t) \, dt = \left[x \mapsto -\frac{1}{x}\right]_a^b 
= \frac{1}{a} - \frac{1}{b}.
$$ "Passer à la limite" informellement (sans justification) dans cette
expression peut nous laisser penser que $f$ est intégrable sur
$\left[1, +\infty \right]$ et vérifie $$
\int_1^{+\infty} f(t) \, dt \stackrel{?}{=} 1.
$$ Les calculs confirment cette intuition : nous pouvons en effet
établir que pour tout $\varepsilon > 0$, la jauge $\gamma$ sur
$[1, +\infty]$ définie par $$
\gamma(t) = \left|
\begin{array}{rl}
\left]t(1 - \varepsilon/4), t(1 + \varepsilon / 4) \right[ & \mbox{si $t < +\infty$,} \\
\left]2 / \varepsilon, +\infty \right] & \mbox{si $t=+\infty$}
\end{array}
\right.
$$ est telle que pour toute subdivision pointée $\mathcal{D}$ de
$[1, + \infty]$ subordonnée à $\gamma$, on a
$|S(f,\mathcal{D}) - 1| \leq \varepsilon$ (cf. [calculs en annexe (p.
`\pageref*{jauge-non-bornuxe9}`{=tex})](#jauge-non-borné)).
:::

::: {.section}
Un facteur vient simplifier l'étude de l'intégration sur des intervalles
(a priori) non bornés : il n'est pas nécessaire de considérer
l'intégration dans tous les types d'intervalles possibles car on peut
toujours se ramener au cas où l'on cherche à intégrer une fonction sur
la droite réelle (achevée) toute entière.
:::

::: {.section}
### Proposition -- Extension à la droite réelle achevée {#EDRA .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Extension à la droite réelle achevée}`{=latex}

Une fonction $f:[a, b] \to \mathbb{R}$ est intégrable si et seulement si
son prolongement $\bar{f}$ par zéro dans $[-\infty, +\infty]$,
c'est-à-dire la fonction $\bar{f} :[-\infty, +\infty] \to \mathbb{R}$
telle que $$
\bar{f}(x) = \left|
\begin{array}{rl}
f(x) & \mbox{si } \, x \in  [a, b], \\
0 & \mbox{sinon,}
\end{array}
\right.
$$ est intégrable. Dans ce cas, on a $$
\int_a^b f(t) \, dt = \int_{-\infty}^{+\infty} \bar{f}(t) \, dt.
$$
:::

::: {.section}
#### Démonstration {#démonstration-13 .proof}

Supposons que $a$ soit fini et que $b = +\infty$. Si $\bar{f}$ est
intégrable sur $[-\infty, +\infty]$, par [restriction (p.
`\pageref*{restriction}`{=tex})](#restriction), $f$ est intégrable sur
$[a, +\infty]$. Réciproquement, si $f$ est intégrable sur
$[a, +\infty]$, la fonction $\bar{f}$ étant nulle sur
$\left[-\infty, a\right]$ à l'exception d'un point, elle y est
intégrable ; étant égale à $f$ sur $[a, +\infty]$ elle y est également
intégrable. Par additivité, $\bar{f}$ est donc intégrable sur
$[-\infty, +\infty]$. L'additivité fournit également $$
\int_{-\infty}^{+\infty} g(t) \, dt = \int_{-\infty}^a g(t) \, dt + \int_{a}^{+\infty} g(t) \,dt.
$$ Comme $\bar{f}$ est nulle sur $\left[-\infty, a\right]$ à l'exception
au plus d'un point, son intégrale sur $[-\infty, a]$ est nulle et comme
$g=f$ sur $[a, +\infty]$, $$
\int_{-\infty}^{+\infty} g(t) \, dt = \int_{a}^{+\infty} f(t) \,dt.
$$ Le résultat dans les autres cas ($a=-\infty$ et $b$ fini, $a$ et $b$
finis) se démontrent de manière analogue.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
L'extension que nous venons d'apporter à l'intégration sur des
intervalles non-bornés de $[-\infty, +\infty]$ ne perturbe finalement
que très peu la pratique du calcul intégral : l'essentiel des propriétés
élémentaires de l'intégrale sont encore valables dans ce nouveau
cadre[^13].
:::

::: {.section}
### Théorème -- Propriétés élémentaires de l'intégrale {#pei .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Propriétés élémentaires de l'intégrale}`{=latex}

Sont valables pour tous les intervalles fermés de $[-\infty, +\infty]$ :

-   La [linéarité de l'intégrale (p.
    `\pageref*{linuxe9arituxe9}`{=tex})](#linéarité),

-   Les propriétés [d'additivité (p.
    `\pageref*{additivituxe9}`{=tex})](#additivité) et [de restriction
    (p. `\pageref*{restriction}`{=tex})](#restriction),

-   [Le changement de variable (p.
    `\pageref*{changement-de-variable}`{=tex})](#changement-de-variable),

-   [La croissance de l'intégrale (p.
    `\pageref*{croissance}`{=tex})](#croissance), [l'inégalité
    triangulaire (p.
    `\pageref*{inuxe9galituxe9-triangulaire}`{=tex})](#inégalité-triangulaire),
    les [fonctions égales presque partout (p.
    `\pageref*{fepp}`{=tex})](#fepp) et [réciproque (p.
    `\pageref*{fepp-ruxe9ciproque}`{=tex})](#fepp-réciproque),

-   [La continuité (p. `\pageref*{cii}`{=tex})](#cii) et [dérivabilité
    (p. `\pageref*{dii}`{=tex})](#dii) des intégrales indéterminées.
:::

::: {.section}
À noter que [le théorème de changement de variable (p.
`\pageref*{changement-de-variable}`{=tex})](#changement-de-variable)
nous fournit également un moyen alternatif pour définir l'intégrale
entre $-\infty$ et $+\infty$, en nous ramenant à une intégrale sur un
intervalle borné.
:::

::: {.section}
#### Exercice -- Prendre la tangente {#plt .exercise .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Prendre la tangente}`{=latex}

Montrer qu'une fonction $f:\mathbb{R}\to \mathbb{R}$ est intégrable
entre $-\infty$ et $+\infty$ si et seulement si l'intégrale $$
\int_{-\frac{\pi}{2}}^{\frac{\pi}{2}} f(\tan t)(1+\tan^2 t) \, dt
$$ est bien définie, et que dans ce cas, les deux intégrales sont
égales. ([Solution p.
`\pageref*{answer-plt}`{=tex}](#answer-plt){.no-parenthesis}.)
:::
:::

::: {.section}
Annexe
======

::: {.section}
### Théorème -- Lemme de Cousin {#cousin .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Lemme de Cousin}`{=latex}

Pour toute jauge $\gamma$ sur l'intervalle $[a, b]$, il existe une
subdivision pointée $\mathcal{D}$ qui soit subordonnée à $\gamma$.
:::

::: {.section}
#### Démonstration {#démonstration-14 .proof}

S'il existe un $t \in I^0 = I = [a, b]$ tel que $I \subset \gamma(t)$,
la subdivision pointée $\mathcal{D} = \{(t, I)\}$ convient. Sinon, on
peut considérer les intervalles $I_0^1 = [a, (a+b)/2]$ et
$I_1^1 = [(a+b)/2, b]$ et examiner pour chacun de ces intervalles s'il
existe un $t_i \in I_i^1$ tel que $I_i^1 \subset \gamma(t_i)$, dans ce
cas ajouter la paire $(t_i, I_i^1)$ à la collection $\mathcal{D}$ et
dans le cas contraire décomposer à nouveau l'intervalle posant problème.
Il s'avère que ce procédé converge en un nombre fini d'étapes ; il
génère donc une subdivision pointée $\mathcal{D}$ de $I$.

En effet, dans le cas contraire il existerait une infinité d'intervalles
fermés $J_i$ emboités ($J_{i+1} \subset J_i$) tels que $J_0 = I$,
$\ell(J_{i+1}) = \ell(J_i)/2$ et pour tout $t \in J_i$,
$J_i \not \subset \gamma(t)$. Soit $t_i$ un point de $J_i$ ; la suite de
ces points appartient à $J_0$ qui est compact et admet donc une suite
extraite qui converge. Comme la suite des $t_k$ appartient à $J_i$ pour
tout $k \geq i$, cette limite $t$ adhère à tous les $J_i$, et donc
appartient à tous les $J_i$ puisqu'ils sont fermés. La longueur de $J_i$
étant divisée par deux à chaque incrément de $i$,
$\ell(J_i) = \ell(J_0) / 2^i$ ; comme $t \in J_i$,
$J_i \subset [t - \ell(J_0) / 2^i, t + \ell(J_0) / 2^i]$. Par
conséquent, il existe un rang $i$ à partir duquel
$J_i \subset \gamma(t)$, ce qui contredit l'hypothèse de
départ.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Théorème -- Théorème fondamental du calcul (forme générale) {#TFC .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Théorème fondamental du calcul (forme générale)}`{=latex}

Soit $[a, b]$ un intervalle fermé borné de $\mathbb{R}$ ; si la fonction
$f:[a, b] \to \mathbb{R}$ est dérivable, sa dérivée $f'$ est intégrable
au sens de Henstock-Kurzweil sur $[a, b]$ et $$
[f]_a^b := f(b) - f(a) = \int_a^b f'(t) \, dt.
$$
:::

::: {.section}
#### Démonstration {#démonstration-15 .proof}

Nous souhaitons établir que $f':[a, b] \to \mathbb{R}$ est intégrable,
d'intégrale égale à $f(b) - f(a)$. Pour cela, nous devons montrer que
pour tout $\varepsilon > 0$ il existe une fonction de jauge $\gamma$ sur
$[a, b]$ telle que, si une subdivision pointée $$
\mathcal{D} = \{(t_0, [x_0, x_1], \dots, (t_{m-1}, [x_{m-1}, x_m]))\}
$$ vérifie pour tout $i \in \{0, \dots, m-1\},$
$[x_i,x_{i+1}] \subset \gamma(t_i),$ alors $$
|S(f', \mathcal{D}) - (f(b) - f(a))| \leq \varepsilon.
$$ Notons que si
$\mathcal{D} = \{(t_0, [x_0, x_1], \dots, (t_{m-1}, [x_{m-1}, x_m]))\}$,
le membre de gauche de cette inégalité vérifie $$
\begin{split}
|S(f', \mathcal{D}) - (f(b) - f(a))| 
  &= \left|\sum_{i=0}^{m-1} f'(t_i)(x_{i+1} - x_i) - (f(b) - f(a))\right| \\
  &= \left|\sum_{i=0}^{m-1} f'(t_i)(x_{i+1} - x_i) - \sum_{i=0}^{m-1} (f(x_{i+1}) - f(x_i)) \right| \\
  &= \left|\sum_{i=0}^{m-1} (f'(t_i)(x_{i+1} - x_i) - (f(x_{i+1}) - f(x_i))) \right| \\
  &\leq \sum_{i=0}^{m-1} \left| f'(t_i)(x_{i+1} - x_i) - (f(x_{i+1}) - f(x_i)) \right| \\
\end{split}
$$ Si l'on parvient à garantir que pour chacun des termes de cette
somme, $$
\left| f'(t_i)(x_{i+1} - x_i) - (f(x_{i+1}) - f(x_i)) \right| 
\leq 
\frac{\varepsilon}{b-a} (x_{i+1} - x_i),
$$ ce qui revient à assigner à chaque terme une erreur maximale
proportionnelle à la longueur de l'intervalle $[x_i, x_{i+1}]$, alors $$
\begin{split}
|S(f', \mathcal{D}) - (f(b) - f(a))| 
%&\leq \sum_{i=0}^{m-1} \left| f'(t_i)(x_{i+1} - x_i) - (f(x_{i+1}) - f(x_i)) \right| \\
&\leq \sum_{i=0}^{m-1} \frac{\varepsilon}{b-a} (x_{i+1} - x_i) \\
&= \frac{\varepsilon}{b-a} \sum_{i=0}^{m-1} (x_{i+1} - x_i) \\
&= \frac{\varepsilon}{b-a} (b - a) \\
&= \varepsilon. \\
\end{split}
$$ Fixons donc un $\varepsilon > 0$ arbitraire ; comme pour tout
$t \in [a, b],$ $$f(t+h) = f(t) + f'(t) h + o(|h|),$$ il existe un
$\delta(t) > 0$ tel que si $|h| < \delta (t),$ $$
|f'(t) h - (f(t+h) - f(t))| \leq \frac{\varepsilon}{b-a} |h|
$$ Par conséquent, pour tout sous-intervalle fermé $[c, d]$ de $[a, b]$
tel que $t \in [c, d]$ et
$[c, d] \subset \left]t-\delta(t), t+\delta(t)\right[,$ nous avons $$
|f'(t) (d-t) - (f(d) - f(t))| \leq \frac{\varepsilon}{b-a} |d - t| = \frac{\varepsilon}{b-a} (d-t)
$$ ainsi que $$
|f'(t) (c-t) - (f(c) - f(t))| \leq \frac{\varepsilon}{b-a} |c - t| = \frac{\varepsilon}{b-a} (t - c).
$$ L'inégalité triangulaire fournit alors $$
|f'(t)(d - c) - (f(d) - f(c))| \leq \frac{\varepsilon}{b-a} (d - c).
$$ Posons $\gamma(t) = \left]t - \delta(t), t + \delta(t)\right[$ ; nous
avons ainsi bien défini une fonction de jauge sur $[a, b]$. Si
$\mathcal{D}$ est subordonnée à $\gamma$, pour tout
$i \in \{0, \dots, m-1\},$
$$t_i \in [x_i,x_{i+1}] \subset \left]t_i - \delta(t_i), t_i + \delta(t_i)\right[,$$
par conséquent $$
|f'(t_i)(x_{i+1} - x_i) - (f(x_{i+1}) - f(x_i))| \leq \frac{\varepsilon}{b-a} (x_{i+1} - x_i).
$$ et donc $|S(f', \mathcal{D}) - (f(b) - f(a))| \leq \varepsilon$, ce
qui prouve le résultat recherché.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Exemple -- Intégration de $x \mapsto 1/\sqrt{x}$ {#iis-proof .example .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Intégration de \(x \mapsto 1/\sqrt{x}\)}`{=latex}

Suite de [l'exemple (p. `\pageref*{iis}`{=tex})](#iis). Nous allons tout
d'abord prouver que si $0 < x \leq t \leq y \leq 1$, alors $$
|f(t) (y-x) - (F(y) - F(x))| = 
\left| \frac{y-x}{\sqrt{t}} - 2\sqrt{y} + 2 \sqrt{x}\right|
\leq \frac{\varepsilon}{2} (y-x).
$$ quand $[x, y] \subset \gamma(t)$, ce qui garantira que $$
|S(f_{|[a, 1]}, \mathcal{D}_a) - (F(1) - F(a))| \leq \frac{\varepsilon}{2} (1 - a) \leq \frac{\varepsilon}{2}
$$ pour tout subdivision pointée $\mathcal{D}_a$ de $[a, 1]$ subordonnée
à $\gamma$. On remarque qu'il suffit de prouver d'une part que $$
\left| \frac{y-t}{\sqrt{t}} - 2\sqrt{y} + 2 \sqrt{t}\right|
\leq \frac{\varepsilon}{2} (y-t)
$$ et d'autre part que $$
\left| \frac{t-x}{\sqrt{t}} - 2\sqrt{t} + 2 \sqrt{x} \right|
\leq \frac{\varepsilon}{2} (t-x)
$$ pour obtenir l'inégalité voulue. Intéressons-nous au membre de gauche
de la première de ces inégalités ; on a $$
\begin{split}
\frac{y-t}{\sqrt{t}} - 2\sqrt{y} + 2 \sqrt{t}
&=
\frac{y - t -2 \sqrt{t}\sqrt{y} + 2 t}{\sqrt{t}} \\
&=
\frac{\sqrt{y}^2 + \sqrt{t}^2 -2 \sqrt{t}\sqrt{y}}{\sqrt{t}} \\
&= \frac{(\sqrt{y} - \sqrt{t})^2}{\sqrt{t}}.
\end{split}
$$ Pour garantir que ce terme soit plus petit que $$
\frac{\varepsilon}{2} (y - t)
= \frac{\varepsilon}{2} (\sqrt{y} - \sqrt{t})(\sqrt{y} + \sqrt{t}),
$$ il suffit donc de s'assurer que $$
\frac{(\sqrt{y} - \sqrt{t})}{\sqrt{t}} \leq \frac{\varepsilon}{2} (\sqrt{y} + \sqrt{t}),
$$ soit $\sqrt{y} \leq \sqrt{t} + ({\varepsilon}/{2}) (\sqrt{ty} + t)$.
Comme $t \leq y$, c'est le cas si $$
\sqrt{y} \leq \sqrt{t} + \varepsilon t
\; \mbox{ soit } \;
y \leq t \left(1 +  \varepsilon \sqrt{t} \right)^2.
$$ Par une méthode en tout point identique, on montre que la seconde
inégalité -- impliquant $x$ et $t$ -- est satisfaite si $$
\frac{(\sqrt{t} - \sqrt{x})}{\sqrt{x}} \leq \frac{\varepsilon}{2} (\sqrt{t} + \sqrt{x}),
$$ soit $$
\frac{(\sqrt{x^{-1}} - \sqrt{t^{-1}})}{\sqrt{t^{-1}}} \leq \frac{\varepsilon}{2} (\sqrt{x^{-1}} + \sqrt{t^{-1}}),
$$ ou encore
$\sqrt{x^{-1}} \leq \sqrt{t^{-1}} + ({\varepsilon}/{2}) (\sqrt{x^{-1}t^{-1}} + t^{-1})$.
Comme $t^{-1} \leq x^{-1}$, c'est le cas si $$
\sqrt{x^{-1}} \leq \sqrt{t^{-1}} + \varepsilon t^{-1}
\; \mbox{ soit } \;
x \geq \frac{t}{\left(1 +  \varepsilon / \sqrt{t} \right)^2}.
$$

Intéressons nous désormais à ce qui se passe pour une subdivision
$\mathcal{D}$ de $[0, 1]$. Comme
$\gamma(t) \subset \left]0, +\infty \right[$ si $t>0$, si
$\mathcal{D} = \{(t_i, [x_i, x_{i+1}]), i \in \{0,\dots, m-1\}\}$ est
une subdivision pointée de $[0, 1]$ subordonnée à $\gamma$, si $t_i>0$,
$0 \not \in [x_i, x_{i+1}]$. Comme les ensembles $[x_i, x_{i+1}]$
doivent recouvrir $[0, 1]$, il est nécessaire que le point $t_0$ associé
à l'intervalle $[x_0, x_1]$ soit $0$. Le reste de la subdivision est
alors subordonnée à $\gamma$ sur $[x_1,1]$ avec $x_1 > 0$ $$
S(f,\mathcal{D})
=
f(0) (x_1 - x_0) + \sum_{i = 1}^{m-1} f(t_i) (x_{i+1} - x_i)
$$ et d'après la section précédente, $$
\left| 
\sum_{i = 1}^{m-1} f(t_i) (x_{i+1} - x_i)
- (2\sqrt{1} - 2\sqrt{x_1}))
\right|
\leq \frac{\varepsilon}{2}.
$$ Avec $\gamma(0) = \left]-1, \frac{\varepsilon^2}{16}\right[$,
l'inclusion $[x_0, x_1] \subset \gamma(0)$ fournit $$
\left|f(0)(x_1 - 0) - (2\sqrt{x_1} - 2\sqrt{x_0})\right| 
= 2\sqrt{x_1}
\leq 
\frac{\varepsilon}{2}.
$$ On a donc garanti que $|S(f,\mathcal{D}) - 2| \leq \varepsilon$, ce
qui est le résultat cherché. Au final, la jauge $\gamma$ sur $[0,1]$
définie initialement garantit un écart $|S(f, \mathcal{D}) - 2|$
inférieur à $\varepsilon$ pour toute subdivision pointée $\mathcal{D}$
de $[0,1]$ subordonnée à $\gamma$.
:::

::: {.section}
Dans le cas où l'on souhaite établir l'intégrabilité sans savoir quelle
est la valeur de l'intégrale, le test suivant d'intégrabilité est
utile :
:::

::: {.section}
### Théorème -- Critère d'intégrabilité de Cauchy {#CIC .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Critère d'intégrabilité de Cauchy}`{=latex}

Une fonction $f: [a, b] \to \mathbb{R}$ est intégrable si et seulement
si pour tout $\varepsilon > 0$ il existe une jauge $\gamma$ sur $[a, b]$
telle que pour tout couple de subdivisions pointées $\mathcal{D}$ et
$\mathcal{D}'$ subordonnées à $\gamma$, on ait $$
|S(f, \mathcal{D}) - S(f, \mathcal{D}')| \leq \varepsilon.
$$
:::

::: {.section}
#### Démonstration {#démonstration-16 .proof}

Si la fonction $f$ est intégrable, pour tout $\varepsilon > 0$, il
existe une jauge $\gamma$ sur $[a, b]$ telle que pour tout couple de
subdivisions pointées $\mathcal{D}$ et $\mathcal{D}'$ subordonnées à
$\gamma$, on ait $$
\left|S(f, \mathcal{D}) - \int_a^b f(t) \, dt \right| \leq \frac{\varepsilon}{2}
\; \mbox{ et } \;
\left|S(f, \mathcal{D}') - \int_a^b f(t) \, dt \right| \leq \frac{\varepsilon}{2}.
$$ Par l'inégalité triangulaire, on a alors
$|S(f, \mathcal{D}) - S(f, \mathcal{D}')| \leq \varepsilon.$

Réciproquement, si la fonction $f$ vérifie le critère du théorème, pour
tout $k \in \mathbb{N}$ il existe une jauge $\gamma_{k}$ sur $[a, b]$
telle que pour tout couple de subdivisions pointées $\mathcal{D}$ et
$\mathcal{D}'$ subordonnées à $\gamma_k$, on ait $$
|S(f, \mathcal{D}) - S(f, \mathcal{D}')| \leq 2^{-k}.
$$ Il est de plus possible de choisir les jauges $\gamma_k$ telles qu'à
tout ordre $k$ et pour tout $t \in [a, b]$, on ait
$\gamma_{k+1}(t) \subset \gamma_k(t)$ (si $\gamma_{k+1}$ ne satisfait
pas ce critère, il suffit de lui substituer la jauge définie par en $t$
par $\gamma_{k+1}(t) \cap \gamma_k(t)$). Soit $\mathcal{D}_k$ une suite
de subdivisions pointées sur $[a, b]$ subordonnées à $\gamma_k$. Si
$m \geq k$ et $n \geq k$, $\mathcal{D}_m$ et $\mathcal{D}_n$ sont
subordonnées à $\gamma_k$, donc $$
|S(f, \mathcal{D}_m) - S(f, \mathcal{D}_n)| \leq 2^{-k}.
$$ La suite des $S(f, \mathcal{D}_k)$ est donc de Cauchy ; la droite des
réels étant complète, cette suite à une limite $A$. En passant à la
limite sur $n$ dans l'inégalité
$|S(f, \mathcal{D}) - S(f, \mathcal{D}_n)| \leq 2^{-k}$, valable quand
$\mathcal{D}$ est subordonnée à $\gamma_k$, on obtient $$
|S(f, \mathcal{D}) - A| \leq 2^{-k}.
$$ La fonction $f$ est donc intégrable et d'intégrale
$A$.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Définition -- Subdivision pointée partielle {#subdivision-pointée-partielle .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Subdivision pointée partielle}`{=latex}

Une *subdivision pointée partielle* $\mathcal{D}$ de l'intervalle fermé
$I = [a, b]$ de $[-\infty, +\infty]$ est une collection finie $$
\mathcal{D} = \{(t_i, I_i) \; | \; \; 0 \leq i \leq n-1\}
$$ où les $I_i$ sont des intervalles fermés de $[a, b]$ sans
chevauchement et $t_i \in I_i$ pour tout $i \in \{0, \dots, n-1\}.$ La
somme de Riemann associée à la fonction $f:[a, b] \to \mathbb{R}$ et à
la subdivision pointée partielle $\mathcal{D}$ de $[a, b]$ est la
grandeur $$
S(f, \mathcal{D}) = \sum f(t) \ell(I), \; \mbox{ où }(t, I) \in \mathcal{D}, \, \ell(I) < +\infty.
$$ Une subdivision pointée partielle $\mathcal{D}$ de l'intervalle fermé
$[a, b]$ est *subordonnée à une jauge* $\gamma$ de $[a, b]$ si pour tout
$(t, J) \in \mathcal{D}$, $J \subset \gamma(t).$
:::

::: {.section}
### Théorème -- Lemme de Henstock {#henstock-lemma .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Lemme de Henstock}`{=latex}

Soit $[a, b]$ un intervalle fermé, $f$ une fonction intégrable au sens
de Henstock-Kurzweil sur $[a, b]$ et $\gamma$ une jauge sur $[a, b]$
telle que pour toute subdivision pointée $\mathcal{D}$ de $[a, b]$
subordonnée à $\gamma$, on ait $$
\left|S(f, \mathcal{D}) - \mbox{(HK)}\!\!\int_a^b f(t) \, dt\right| \leq \varepsilon.
$$ Alors pour toute subdivision pointée partielle
$\mathcal{D} = \{(t_k, I_k)\}_k$ de $[a, b]$ subordonnée à $\gamma$, on
a également $$
\left|S(f, \mathcal{D}) - \sum_k \mbox{(HK)}\!\!\int_{I_k} f(t) \, dt\right| \leq \varepsilon.
$$
:::

::: {.section}
#### Démonstration {#démonstration-17 .proof}

Il existe une famille finie d'intervalles fermés $\{J_j\}$,
$j = 1, \dots, m$ telle que l'union des familles $\{I_k\}$ et $\{J_j\}$
forme une subdivision (complète) de $[a, b]$. Pour tout $\eta > 0$, sur
chaque intervalle $J_j$, il existe une jauge $\gamma_j$ telle que si
$\mathcal{D}_j$ est une subdivision pointée de $J_j$ subordonnée à
$\gamma_j$, alors $$
\left|S(f, \mathcal{D}_j) - \mbox{(HK)}\!\!\int_{J_j} f(t) \, dt \right| \leq \eta.
$$ Si de plus on choisit $\mathcal{D}_j$ subordonnée à la restriction de
$\gamma$ à $J_j$, alors $\mathcal{D} \cup (\cup_j \mathcal{D}_j)$ est
une subdivision pointée (complète) de $[a, b]$ subordonnée à $\gamma$.
On déduit de l'hypothèse centrale du lemme que $$
\left|
S(f, \mathcal{D}) + \sum_j S(f, \mathcal{D}_j) 
- 
\sum_k \mbox{(HK)}\!\!\int_{I_k} f(t) \, dt + \sum_{j} \mbox{(HK)}\!\!\int_{J_j} f(t) \, dt
\right|
\leq
\varepsilon
$$ et donc par l'inégalité triangulaire que $$
\left|
S(f, \mathcal{D}) 
- 
\sum_k \mbox{(HK)}\!\!\int_{I_k} f(t) \, dt
\right|
\leq
\varepsilon + m \eta.
$$ Le choix de $\eta > 0$ étant arbitraire, l'inégalité cherchée est
établie.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Lemme -- Partie positive d'une fonction {#fp .lemma .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Partie positive d'une fonction}`{=latex}

Soit $f: [a,b] \to \mathbb{R}$ une fonction intégrable au sens de
Henstock-Kurzweil dont la partie positive $f_+$ est majorée par $g$ $$
f_+ := \max(f, 0) \leq g,
$$ où $g:[a, b] \to \left[0, +\infty\right[$ est intégrable. Alors la
fonction $f_+$ est intégrable.
:::

::: {.section}
#### Démonstration {#démonstration-18 .proof}

Nous allons montrer que $f_+$ est intégrable au sens de
Henstock-Kurzweil -- et donc intégrable puisque positive par
construction -- et que $$
\int_a^b f_+(t) \, dt 
= S :=
\sup_{\mathcal{D}} 
\sum_{(t, I) \in \mathcal{D}} \left( \mbox{(HK)}\!\!\int_I f(t) \, dt\right)_{\!\!+}
$$ où le supremum est calculé sur toutes les subdivisions pointées de
$[a, b]$. Tout d'abord, ce supremum est fini ; en effet pour toute
subdivision $\mathcal{D}$, on a $$
\begin{split}
\sum_{(t, I) \in \mathcal{D}} \left( \mbox{(HK)}\!\!\int_I f(t) \, dt\right)_{\!\!+}
&\leq
\sum_{(t, I) \in \mathcal{D}} \left( \int_I g(t) \, dt\right)_{\!\!+} \\
&=
\sum_{(t, I) \in \mathcal{D}} \int_I g(t) \, dt \\
&=
\int_a^b g(t) \, dt.
\end{split}
$$ Soit $\varepsilon > 0$ et $\mathcal{D}_{0}$ une subdivision pointée
de $\mathbb{R}$ telle que $$
S - \frac{\varepsilon}{2} 
\leq \sum_{(t, I) \in \mathcal{D}_0} \left( \mbox{(HK)}\!\!\int_I f(t) \, dt\right)_{\!\!+} 
\leq S.
$$ Soit $\lambda$ une jauge sur $[a, b]$ assurant une précision
$\varepsilon/2$ dans l'estimation de l'intégrale de $f$ par les sommes
de Riemann. Soit $\nu$ une jauge sur $[a, b]$ telle que si
$(t, [c, d]) \in \mathcal{D}_0$ et $t \in \left]c,d\right[$ alors
$\nu(t) \subset \left]c,d\right[$ ; on note $\gamma$ la jauge définie
par $\gamma(t) = \lambda(t) \cap \nu(t)$. Si $\mathcal{D}$ est
subordonnée à $\gamma$, quitte à découper des intervalles en deux si
$(t, I) \subset \mathcal{D}$ et $t$ appartient à la frontière d'un
intervalle composant $\mathcal{D}_0$ -- ce qui ne change pas la somme de
Riemann associée -- les éléments $(t, J) \in \mathcal{D}$ tels que
$J \subset I$, où $(x, I) \subset \mathcal{D}_0$ forment une subdivision
pointée de $I$. Par conséquent, comme `\begin{align*}
\left( \mbox{(HK)}\!\!\int_I f(t) \, dt\right)_{\!\!+} 
&=
\left( \sum_{(t, J) \in \mathcal{D}, J \subset I}\mbox{(HK)}\!\!\int_J f(t) \, dt\right)_{\!\!+} \\
&\leq 
\sum_{(t, J) \in \mathcal{D}, J \subset I} \left(\mbox{(HK)}\!\!\int_J f(t) \, dt\right)_{\!\!+} 
\end{align*}`{=tex} et donc $$
S - \frac{\varepsilon}{2} \leq 
\sum_{(t, I) \in \mathcal{D}_0} \left( \mbox{(HK)}\!\!\int_I f(t) \, dt\right)_{\!\!+} 
\leq 
\sum_{(t, I) \in \mathcal{D}} \left( \mbox{(HK)}\!\!\int_I f(t) \, dt\right)_{\!\!+}
\leq S, 
$$ on obtient $$
\left|
\sum_{(t, I) \in \mathcal{D}} \left( \mbox{(HK)}\!\!\int_I f(t) \, dt\right)_{\!\!+}
- S \right| \leq \frac{\varepsilon}{2}.
$$ Par ailleurs, si l'on considère la subdivision (partielle) pointée
$\mathcal{D}_+$ extraite de $\mathcal{D}$ composée des paires
$(t, I) \in \mathcal{D}$ et telles que $$
f(t) \ell(I) \geq \mbox{(HK)}\!\!\int_I f(x) \, dx,
$$ alors le [lemme de
Henstock](Calcul%20Intégral%20I.pdf/#henstock-lemma) fournit $$
\sum_{(t, I) \in \mathcal{D}} 
\left( f(t) \ell(I) - \mbox{(HK)}\!\!\int_I f(x) \, dx \right)_{\!\!+}
\leq \frac{\varepsilon}{2}.
$$ Comme $(x+y)_+ \leq x_+ + y_+$, on en déduit $$
\sum_{(t, I) \in \mathcal{D}} 
f_+(t) \ell(I) - 
\sum_{(t, I) \in \mathcal{D}} 
\left(\mbox{(HK)}\!\!\int_I f(x) \, dx \right)_{\!\!+}
\leq \frac{\varepsilon}{2}.
$$ De façon similaire, en raisonnant sur la subdivision partielle
complémentaire à $\mathcal{D}_+$ dans $\mathcal{D}$, on peut montrer que
$$
\sum_{(t, I) \in \mathcal{D}} 
\left(\mbox{(HK)}\!\!\int_I f(x) \, dx \right)_{\!\!+} - 
\sum_{(t, I) \in \mathcal{D}} 
f_+(t) \ell(I)
\leq \frac{\varepsilon}{2}.
$$ On obtient donc au final $$
\left|
\sum_{(t, I) \in \mathcal{D}} f_+(t) \ell(I) 
- 
S
\right| 
\leq 
\frac{\varepsilon}{2};
$$ la fonction $f_+$ est donc comme annoncé intégrable au sens de
Henstock-Kurzweil, d'intégrale égale à
$S$.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
[Le théorème de Hake (p. `\pageref*{hake}`{=tex})](#hake) montre qu'avec
l'intégrale de Henstock-Kurzweil, il n'existe pas d'intégrale
*impropre*, qui ne serait pas définissable directement mais uniquement
par un passage à la limite. Attention : ce résultat n'a pas d'équivalent
pour l'intégrale de Lebesgue, qui admet des intégrales impropres.
:::

::: {.section}
### Théorème -- Théorème de Hake {#hake .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Théorème de Hake}`{=latex}

Soit $[a, b]$ un intervalle fermé de $[-\infty, +\infty]$ et
$f: [a, b] \to \mathbb{R}$. La fonction $f$ est intégrable au sens de
Henstock-Kurzweil sur $[a, b]$ si et seulement si elle est intégrable
sur tout intervalle $[c, d]$ tel que $a < c$ et $d < b$ et que
l'intégrale $$
\mbox{(HK)}\!\!\int_c^d f(t) \, dt
$$ a une limite quand $c$ tend vers $a$ et $d$ tend vers $b$. On a alors
$$
\mbox{(HK)}\!\!\int_a^b f(t) \, dt = \lim_{(c, d) \to (a,b)} \mbox{(HK)}\!\!\int_{c}^d f(t) \, dt.
$$
:::

::: {.section}
#### Démonstration {#démonstration-19 .proof}

Se reporter à [@Swa01].`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
Le théorème de Hake permet d'étendre facilement certains résultats
valables sur des segments de la droite réelle. A titre d'exemple :
:::

::: {.section}
### Théorème -- Théorème fondamental du calcul (extension) {#théorème-fondamental-du-calcul-extension .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Théorème fondamental du calcul (extension)}`{=latex}

Soit $[a, b]$ un intervalle fermé de $[-\infty, +\infty]$ et
$f: [a, b] \to \mathbb{R}$, une fonction dérivable sur
$\left]a, b\right[$ et continue sur $[a, b]$. La fonction $f'$ (définie
partout sauf en $a$ et $b$) est intégrable au sens de Henstock-Kurzweil
sur $[a, b]$ et $$
[f]_a^b := f(b) - f(a) = \mbox{(HK)}\!\!\int_a^b f'(t) \, dt.
$$
:::

::: {.section}
#### Démonstration {#démonstration-20 .proof}

[Le théorème fondamental du calcul (p. `\pageref*{TFC}`{=tex})](#TFC)
dans le cadre borné nous fournit pour tous $c$ et $d$ tels que
$a < c \leq d < b$ l'intégrabilité au sens de Henstock-Kurzweil de $f'$
sur $[c, d]$ et la relation $$
f(d) - f(c) = \mbox{(HK)}\!\!\int_c^d f'(t) \, dt.
$$ Par continuité, le membre de gauche de cette équation a une limite
quand $c$ tend vers $a$ et $d$ vers $b$, qui est $f(b) - f(a)$. [Le
théorème de Hake (p. `\pageref*{hake}`{=tex})](#hake) permet alors de
conclure.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Exemple -- Intégration de $x \in \left[1, +\infty\right[ \mapsto 1/x^2$ {#jauge-non-borné .example .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Intégration de \(x \in \left[1, +\infty\right[ \mapsto 1/x^2\)}`{=latex}

Soit $\mathcal{D}$ une subdivision pointée de $[1, +\infty]$ subordonnée
à la jauge $\gamma$ définie par $$
\gamma(t) = \left|
\begin{array}{rl}
\left]t(1 - \varepsilon/4), t(1 + \varepsilon / 4) \right[ & \mbox{si $t < +\infty$,} \\
\left]2 / \varepsilon, +\infty \right] & \mbox{si $t=+\infty$}
\end{array}
\right.
$$ Supposons que
$$\mathcal{D} = \{(t_i, [x_i, x_{i+1}]), \, i \in \{0, \dots, m\}\}$$ et
que les $x_i$ sont agencés de façon (strictement) croissante ; on a en
particulier $x_k < +\infty$ quand $k \leq m$ et $x_{m+1} = +\infty$.
Notons
$\mathcal{D}_f = \{(t_i, [x_i, x_{i+1}]), \, i \in \{0, \dots, m-1\}\}$ ;
on a alors $$
\begin{split}
\left| S(f, \mathcal{D}) - 1 \right| 
&\leq
\left| S(f, \mathcal{D}) - \left(1 - \frac{1}{x_{m}}\right) \right| + \frac{1}{x_{m}} \\
&\leq \left| \sum_{(t, [x, y]) \in \mathcal{D}_f} f(t)(y-x) - \left(\frac{1}{x} - \frac{1}{y}\right) \right| + \frac{1}{x_{m}} \\
&\leq \sum_{(t, [x, y]) \in \mathcal{D}_f} \left|f(t)(y-x) - \left(\frac{1}{x} - \frac{1}{y}\right) \right| + \frac{1}{x_{m}}. \\
\end{split}
$$ On remarque que si $t < +\infty$, alors $+\infty \not \in \gamma(t)$.
Comme $x_{m+1} = +\infty$ et que $[x_m, x_{m+1}] \subset \gamma(t_m)$,
nécessairement $t_m = +\infty$. Par conséquent,
$[x_m, x_{m+1}] \subset \gamma(+\infty) = \left]2 / \varepsilon, +\infty \right]$
et donc $$\frac{1}{x_m} \leq \frac{\varepsilon}{2}.$$

D'autre part, on a $$
\left|f(t)(y-x) - \left(\frac{1}{x} - \frac{1}{y}\right) \right|
=
\left|\frac{y-x}{t^2}- \left(\frac{1}{x} - \frac{1}{y}\right) \right|
= 
|y-x|
\left|\frac{1}{t^2} - \frac{1}{xy} \right|.
$$ Comme $y - x = (y -t) + (t - x)$, on a
$|y -x| \leq (\varepsilon/2) t$ et donc $$
\left|f(t)(y-x) - \left(\frac{1}{x} - \frac{1}{y}\right) \right|
\leq \frac{\varepsilon}{2} \left|\frac{1}{t} - \frac{t}{xy}\right|.
$$ La fonction $t \in [x, y] \mapsto 1/t - t / xy$ est dérivable, de
dérivée $-1/t^2 - 1/xy \leq 0$. En $t=x$ et $t=y$, elle vaut
respectivement $1/x - 1/y$ et $1/y - 1/x$. Dans tous les cas, on a donc
$$
\left|f(t)(y-x) - \left(\frac{1}{x} - \frac{1}{y}\right) \right|
\leq \frac{\varepsilon}{2} \left(\frac{1}{x}  - \frac{1}{y} \right)
$$ et par conséquent `\begin{multline*}
\sum_{(t, [x, y]) \in \mathcal{D}_f} \left|f(t)(y-x) - \left(\frac{1}{x} - \frac{1}{y}\right) \right| \\
\leq \frac{\varepsilon}{2}\left(\frac{1}{x_{0}}  - \frac{1}{x_1} + \frac{1}{x_1}  - \frac{1}{x_2} + \dots + \frac{1}{x_{m-1}}  - \frac{1}{x_m} \right)
= \frac{\varepsilon}{2} \left(1 - \frac{1}{x_m} \right) \leq \frac{\varepsilon}{2}.
\end{multline*}`{=tex} On en déduit l'inégalité recherchée
$|S(f, \mathcal{D}) -1| \leq \varepsilon/2$.
:::
:::

::: {.section}
Exercices complémentaires
=========================

::: {.section}
Méthode des trapèzes
--------------------

La méthode des trapèzes est une méthode de quadrature qui approxime
l'intégrale d'une fonction $f:[a, b] \to \mathbb{R}$ en utilisant une
subdivision $$
\mathcal{D}_m=
\left\{
\left[a + i \frac{b-a}{m}, a + (i+1) \frac{b-a}{m} \right]
\; \left| \vphantom{\left(a + i \frac{b-a}{m}, \left[a + i \frac{b-a}{m}, a + (i+1) \frac{b-a}{m} \right]\right)} \; i \in \{0, \dots, m-1\} \right.
\right\},
$$ pour construire la somme $$
S_m = \frac{b-a}{m}\sum_{i=0}^{m-1} \frac{f\left(a + i \frac{b-a}{m}\right) + f\left(a + (i+1) \frac{b-a}{m}\right)}{2}
$$

::: {.section}
#### Question 1 {#mt-1 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Calculer l'aire (algébrique) du trapèze délimité par les segments de
droite $$
\left[\left(
  a+i\frac{b-a}{m}, 0 
\right),
\left(
  a+(i+1)\frac{b-a}{m}, 0 
\right)
\right]
$$ et $$
\left[\left(
  a+i\frac{b-a}{m}, f\left(a+i\frac{b-a}{m}\right)
\right),
\left(
  a+(i+1)\frac{b-a}{m}, f\left(a+(i+1)\frac{b-a}{m}\right)
\right)
\right],
$$ puis interpréter géométriquement la grandeur $S_m$. ([Solution p.
`\pageref*{answer-mt-1}`{=tex}](#answer-mt-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 {#mt-1 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Montrer que si la fonction $f$ est intégrable au sens de Riemann alors
$$
\lim_{m \to +\infty} S_m = \int_a^b f(t) \, dt.
$$

([Solution p.
`\pageref*{answer-mt-1}`{=tex}](#answer-mt-1){.no-parenthesis}.)
:::
:::

::: {.section}
Fonctions non intégrables
-------------------------

Soit $a \in \mathbb{R}$ et $f: \left[a, +\infty\right[ \to \mathbb{R}$
une fonction intégrable sur tout intervalle fermé et borné de
$\left[a, +\infty\right[$.

::: {.section}
#### Question 1 {#id1 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Montrer que si $$
\lim_{x \to +\infty} \int_a^x |f(t)| \, dt  = +\infty
$$ alors $f$ n'est pas intégrable sur $\left[a, +\infty\right[$.
([Solution p.
`\pageref*{answer-id1}`{=tex}](#answer-id1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 {#id2 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

La fonction $$x \in \left[1, +\infty\right[ \mapsto \frac{1}{x}$$
est-elle intégrable ? ([Solution p.
`\pageref*{answer-id2}`{=tex}](#answer-id2){.no-parenthesis}.)
:::

::: {.section}
#### Question 3 {#id3 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

La fonction
$$\mbox{sinc}: x \in \left[1, +\infty\right[ \mapsto \frac{\sin x}{x}$$
est-elle intégrable ? ([Solution p.
`\pageref*{answer-id3}`{=tex}](#answer-id3){.no-parenthesis}.)
:::
:::

::: {.section}
L'intégrale de Riemann est absolue {#Rabs .question .unnumbered .unlisted}
----------------------------------

`\addcontentsline{toc}{subsection}{L'intégrale de Riemann est absolue}`{=latex}

Montrer que l'intégrale de Rieman est absolue : si une fonction $f$ est
intégrable au sens de Riemann, sa valeur absolue $|f|$ l'est également.
([Solution p.
`\pageref*{answer-Rabs}`{=tex}](#answer-Rabs){.no-parenthesis}.)
:::

::: {.section}
Continuité presque partout
--------------------------

::: {.section}
#### Question 1 {#cpp-1 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Est-ce qu'une fonction égale presque partout à une fonction continue est
presque partout continue ? La réciproque est-elle vraie ? ([Solution p.
`\pageref*{answer-cpp-1}`{=tex}](#answer-cpp-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 {#cpp-2 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

La fonction de Dirichlet $1_{\mathbb{Q}}$ -- ou fonction indicatrice de
$\mathbb{Q}$ -- définie par $$
1_{\mathbb{Q}}(x) = 
\left|
\begin{array}{cl}
1 & \mbox{si } x \mbox{ est rationnel,} \\
0 & \mbox{sinon.}
\end{array}
\right.
$$ est-elle intégrable sur $[0, 1]$ au sens de Riemann ? Et au sens de
Lebesgue ? ([Solution p.
`\pageref*{answer-cpp-2}`{=tex}](#answer-cpp-2){.no-parenthesis}.)
:::
:::

::: {.section}
Poussière de Cantor {#cantor}
-------------------

Chaque nombre réel $x$ de $\left[0, 1\right[$ peut être représenté par
un développement en base 3 de la forme $x=0.a_1a_2a_3\cdots$ où
$a_i \in \{0,1,2\}$, une notation qui signifie que $$
x = \sum_{i=1}^{+\infty} a_i 3^{-i}.
$$ Ce développement de $x$ est unique si on lui impose d'être *propre*,
c'est-à-dire si l'on interdit les séquences infinies de chiffres $2$
consécutifs[^14].

On définit l'ensemble $C$ comme le sous-ensemble de $\left[0, 1\right[$
dont le développement en base 3 ne comporte pas le chiffre 1.

::: {.section}
#### Question 1 {#cantor-1 .question .exercise .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Montrer que l'ensemble $C$ est négligeable. ([Solution p.
`\pageref*{answer-cantor-1}`{=tex}](#answer-cantor-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 {#cantor-2 .question .exercise .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Montrer néanmoins que $C$ n'est pas dénombrable, mais a la "puissance du
continu" (qu'il peut être mis en bijection avec $\mathbb{R}$ ou avec un
intervalle de longueur non vide de $\mathbb{R}$, ce qui revient au
même). ([Solution p.
`\pageref*{answer-cantor-2}`{=tex}](#answer-cantor-2){.no-parenthesis}.)
:::
:::
:::

::: {.section}
Solutions
=========

::: {.section}
Exercices essentiels
--------------------

::: {.section}
#### Fonction affine {#answer-fa .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Fonction affine}`{=latex}

Nous déduisons de l'indication que `\begin{align*}
\left|S(f, \mathcal{D}) -  A\right|
&=  \left|\sum_{i=0}^{m-1} (\alpha t_i + \beta)(x_{i+1} - x_i) -  \alpha \left(\frac{x_{i+1}^2}{2} - \frac{x_i^2}{2}\right) - \beta (x_{i+1}-x_i) \right|
\end{align*}`{=tex} et donc que $$
\left|S(f, \mathcal{D}) -  A\right|
\leq 
\sum_{i=0}^{m-1}|\alpha| \left|t_i  -  \frac{x_{i} + x_{i+1}}{2} \right| (x_{i+1} - x_i).
$$ Dans les cas où $a = b$ ou $\alpha=0$, il est évident que $f$ est
intégrable au sens de Riemann et d'intégrale $A$ car le membre de droite
de l'inégalité ci-dessus est nul. Dans le cas contraire, pour tout
$\varepsilon > 0$, on peut poser $$
\delta := \frac{2\varepsilon}{|\alpha|(b-a)} > 0.
$$ Si la subdivision $\mathcal{D}$ est telle que pour tout
$i \in \{0, \dots, m-1\}$ on ait
$\ell([x_i, x_{i+1}]) = x_{i+1} - x_i < \delta$, alors $$
\left|t_i  -  \frac{x_{i} + x_{i+1}}{2} \right| < \frac{\delta}{2} 
$$ et par conséquent $$
\left|S(f, \mathcal{D}) -  A\right|
\leq 
\sum_{i=0}^{m-1}|\alpha| \frac{\varepsilon}{|\alpha|(b-a)} (x_{i+1} - x_i)
= \frac{\varepsilon}{(b-a)} \sum_{i=0}^{m-1} (x_{i+1} - x_i)
= \varepsilon.
$$
:::

::: {.section}
#### Ensembles finis {#answer-ensemble-fini .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Ensembles finis}`{=latex}

Soit $E = \{x_1, \dots, x_m\} \subset \mathbb{R}$. Pour tout
$\varepsilon > 0$, la collection (finie) d'intervalles
$\{\left[x_i, x_i\right]\}_{i=1}^m$ recouvre $E$ et la somme des
longueurs de ces intervalles est nulle, donc $E$ est négligeable.
:::

::: {.section}
#### Intervalles négligeables {#answer-intervalles-négligeables .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Intervalles négligeables}`{=latex}

Pour démontrer que l'ensemble $[a, b]$ n'est pas négligeable quand
$a < b$, nous allons établir que si la collection dénombrable
d'intervalles $I_i$ recouvre $[a, b]$, alors la somme des longueurs des
$I_i$ est supérieure ou égale à $b-a > 0$ et donc l'intervalle n'est pas
négligeable.

Prouvons dans un premier temps ce résultat quand la collection des $I_i$
est finie. Considérons une telle collection $\{I_i\}_{i=1}^m$ ; on peut
supposer que les $I_i$ sont rangés "de la gauche vers la droite",
c'est-à-dire que si $i < j$, il existe un $x \in I_i$ tel que $x \leq y$
pour tout $y \in I_j$ et que tous les $I_i$ intersectent $[a, b]$.
Alors, la collection $\{J_i\}_{i=1}^m$ définie par $J_1 = I_1$, puis
$J_{i+1} = I_{i+1} \setminus (\cup_{j=1}^{i} I_j)$ est composée
d'intervalles disjoints recouvrant $[a, b]$, telle que
$\ell(J_i) \leq \ell(I_i)$ pour tout $i$. Notons $x_i$ et $x_{i+1}$ les
extrémités de gauche et de droite de $J_i$ respectivement ; on a alors
$$
\sum_{i=1}^m \ell(I_i) \geq 
\sum_{i=1}^m \ell(J_i) = \sum_{i=1}^m (x_{i+1} - x_i) = x^{m+1} - x_1 \geq b-a.
$$

Considérons désormais une collection d'intervalles
$\{I_i\}_{i \in \mathbb{N}}$ recouvrant $[a, b]$. Si
$\sum_{i=1}^{+\infty} \ell(I_i) \leq \varepsilon$, alors pour tout
$\varepsilon'>0$, il existe une collection d'intervalles ouverts
$\{J_i\}_{i \in \mathbb{N}}$ tels que $I_i \subset J_i$ et
$\ell(J_i) \leq \ell(I_i) + \varepsilon'/2^{i}$ et donc tels que $$
\sum_{i=1}^{+\infty} \ell(J_i) \leq 
\sum_{i=1}^{+\infty} \ell(I_i) + \sum_{i=1}^{+\infty} \frac{\varepsilon'}{2^i} 
\leq \varepsilon +\varepsilon'.
$$ Or l'ensemble $[a, b]$ étant fermé et borné, il est compact ; les
$\{J_i\}_{i \in \mathbb{N}}$ forment un recouvrement de ce compact par
une collection d'ouverts, on peut donc en extraire un sous-recouvrement
fini $\{K_j\}_{j=1}^m$. En utilisant le résultat précédemment établi
pour de telles collections finies, on en déduit que $$
b - a \leq \sum_{j=1}^{m} \ell(K_j) \leq \sum_{i=1}^{+\infty} \ell(J_i) \leq \varepsilon +\varepsilon',
$$ soit comme $\varepsilon'>0$ est arbitraire, $b - a \leq \varepsilon$.
:::

::: {.section}
#### Sous-ensemble d'un ensemble négligeable {#answer-oe .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Sous-ensemble d'un ensemble négligeable}`{=latex}

Si l'ensemble $A$ est négligeable, pour tout $\varepsilon > 0$, il
existe un recouvrement de $A$ par une collection dénombrable
d'intervalles $I_i$ tels que $\sum_i \ell(I_i) \leq \varepsilon$. La
même collection d'intervalles recouvre tout sous-ensemble $B$ de $A$
donc un tel ensemble $B$ est également négligeable.
:::

::: {.section}
#### Union d'ensembles négligeables {#answer-uen .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Union d'ensembles négligeables}`{=latex}

L'union d'une collection dénombrable d'ensembles négligeables est
négligeable, donc en particulier l'union de deux ou d'un nombre fini
d'ensembles négligeables est négligeable. Soient $A_0$, $A_1$, $\dots$,
$A_i$, $\dots$ une collection dénombrable d'ensembles négligeables. Pour
tout $\varepsilon > 0$, il existe une collection dénombrable
$\{I_{ij}\}_j$ d'intervalles $I_{ij}$ tels que $$
A_i \subset \sum_{j} I_{ij} \; \mbox{ et } \; \sum_{j} \ell(I_{ij}) \leq \frac{\varepsilon}{2^{i+1}}.
$$ Alors la collection des $\{I_{ij}\}_{ij}$ est dénombrable, recouvre
$\cup_i A_i$ et $$
\sum_i \sum_{j} \ell(I_{ij}) \leq \sum_i \frac{\varepsilon}{2^{i+1}}
\leq \varepsilon.
$$

Par contre, l'union d'une collection arbitraire d'ensembles négligeables
n'est pas nécessairement négligeable. Par exemple, la collection des
singletons $\{\{x\} \; | \; x \in [0,1] \}$ est composée d'ensembles
négligeables, mais son union $[0,1]$ n'est pas négligeable
([cf. exercice "Intervalles négligeables" (p.
`\pageref*{intervalles-nuxe9gligeables}`{=tex})](#intervalles-négligeables)).
:::

::: {.section}
#### Fonction continue nulle presque partout {#answer-fcnpp .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Fonction continue nulle presque partout}`{=latex}

Soit $f : \mathbb{R}\to\mathbb{R}$ une fonction continue et nulle
presque partout. Soit $x \in \mathbb{R}$ ; s'il existe une suite de
$x_k \in \mathbb{R}$ tels que $f(x_k) = 0$ et
$\lim_{k\to +\infty} x_k = x$, alors par continuité $f(x) = 0$. Mais
dans le cas contraire, c'est qu'il existe un $\varepsilon > 0$ tel que
pour tout $y \in [x-\varepsilon, x+\varepsilon]$, on ait $f(y)\neq 0$.
Or $[x-\varepsilon, x+\varepsilon]$ n'est pas négligeable ([cf. exercice
"Intervalles négligeables" (p.
`\pageref*{intervalles-nuxe9gligeables}`{=tex})](#intervalles-négligeables)),
donc l'ensemble $\{t \in \mathbb{R}\; | \; f(t) \neq 0\}$ n'est pas
négligeable ([cf. exercice "Sous-ensemble d'un ensemble négligeable" (p.
`\pageref*{oe}`{=tex})](#oe)) ce qui contredit l'hypothèse que $f$ est
nulle presque partout.
:::

::: {.section}
#### Etre non nul {#answer-enn .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Etre non nul}`{=latex}

L'ensemble des réels $x$ ne vérifiant pas la propriété "$x$ est non-nul"
est composé de l'unique réel $0$. Le singleton $\{0\}$ est (fini donc)
négligeable, par conséquent la propriété initiale est bien vérifiée
presque partout.
:::

::: {.section}
#### Etre irrationnel {#answer-ei .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Etre irrationnel}`{=latex}

L'ensemble des réels $x$ ne vérifiant pas la propriété "$x$ est
irrationnel" est l'ensemble des rationnels $\mathbb{Q}$. Cet ensemble
est dénombrable, par conséquent la propriété initiale est bien vérifiée
presque partout.
:::

::: {.section}
#### L'intégrale de Lebesgue est absolue {#answer-lebesgue-absolue .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{L'intégrale de Lebesgue est absolue}`{=latex}

Si $f: [a, b] \to \mathbb{R}$ est intégrable (au sens de Lebesgue),
alors $|f|$ est intégrable au sens de Henstock-Kurzweil ; les fonctions
$|f|$ et $||f|| = |f|$ sont donc intégrables au sens de
Henstock-Kurzweil, donc $|f|$ est également intégrable (au sens de
Lebesgue).
:::

::: {.section}
#### Intégration de $x \mapsto e^x$ {#answer-exp .answer .zero .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Intégration de \(x \mapsto e^x\)}`{=latex}

La fonction $x \in [0, 1] \mapsto e^x \in \mathbb{R}$ est continue donc
intégrable. De plus, $(e^x)' = e^x$, donc par [le théorème fondamental
du calcul (p. `\pageref*{TFCL}`{=tex})](#TFCL), on a $$
\int_0^1 e^x \,dx 
= 
\left[ x \mapsto e^x \right]_0^1
= e^1 - e^0 = e - 1. 
$$
:::

::: {.section}
#### Intégration par parties {#answer-ex-IPP .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Intégration par parties}`{=latex}

Si les fonctions $f:[a, b] \to \mathbb{R}$ et $g:[a, b] \to \mathbb{R}$
sont dérivables, le produit $fg$ est dérivable et $(fg)' = f'g + f g'$.
Par hypothèse les fonctions $f'g$ et $fg'$ sont intégrables, donc [par
linéarité de l'intégrale (p.
`\pageref*{linuxe9arituxe9}`{=tex})](#linéarité), $(fg)'$ également et
$$
\int_a^b (fg)'(t) \, dt = \int_a^b f(t)g'(t) \, dt + \int_a^b f(t)g'(t) \, dt.
$$ Or, par [le théorème fondamental du calcul (p.
`\pageref*{TFC}`{=tex})](#TFC), on a $$
\int_a^b (fg)'(t) \, dt = [fg]_a^b,
$$ ce qui fournit l'égalité recherchée.
:::

::: {.section}
#### Ordre des bornes et additivité {#answer-exo-odb .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Ordre des bornes et additivité}`{=latex}

Quand $c \leq b \leq a$, on peut utiliser [le théorème d'additivité (p.
`\pageref*{additivituxe9}`{=tex})](#additivité) directement, en faisant
l'hypothèse que $f$ est intégrable sur $[c, b]$ et sur $[b, a]$, pour en
conclure qu'elle l'est donc sur $[a, c]$ et que $$
\int_c^a f(t) \, dt  = \int_c^b f(t) \, dt + \int_b^a f(t) \, dt, 
$$ soit $$
-\int_c^a f(t) \, dt  = -\int_c^b f(t) \, dt - \int_b^a f(t) \, dt, 
$$ ce qui équivaut, avec [la convention des bornes inversées (p.
`\pageref*{ordre-bornes}`{=tex})](#ordre-bornes), à $$
\int_a^c f(t) \, dt  = \int_b^c f(t) \, dt + \int_b^a f(t) \, dt.
$$ Si $a \leq c \leq b$ et si l'on suppose que $f$ est intégrable sur
$[a, c]$ et sur $[c, b]$, on établit que $f$ est intégrable sur $[a, b]$
et que $$
\int_a^b f(t) \, dt  = \int_a^c f(t) \, dt + \int_c^b f(t) \, dt,
$$ ou encore $$
\int_a^c f(t) \, dt = \int_a^b f(t) \, dt -  \int_c^b f(t) \, dt,
$$ soit avec [la convention des bornes inversées (p.
`\pageref*{ordre-bornes}`{=tex})](#ordre-bornes), $$
\int_a^c f(t) \, dt = \int_a^b f(t) \, dt +  \int_b^c f(t) \, dt,
$$
:::

::: {.section}
#### Lemme M-L {#answer-ML .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Lemme M-L}`{=latex}

L'inégalité triangulaire fournit $$
\left|\int_a^b f(t) \, dt \right| \leq \int_a^b |f(t)| \, dt.
$$ Comme pour tout $t \in [a, b]$, on a $|f(t)| \leq M$, [par croissance
(p. `\pageref*{croissance}`{=tex})](#croissance) et [linéarité (p.
`\pageref*{linuxe9arituxe9}`{=tex})](#linéarité) de l'intégrale, on a
donc $$
\left|\int_a^b f(t) \, dt \right| \leq \int_a ^b M \, dt = M \int_a^b\, dt
= M (b-a).
$$
:::

::: {.section}
#### Fonctions égales sur un ensemble co-dénombrable {#answer-feppco .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Fonctions égales sur un ensemble co-dénombrable}`{=latex}

[Par linéarité de l'intégrale (p.
`\pageref*{linuxe9arituxe9}`{=tex})](#linéarité), il suffit d'établir
que si $h = g - f$ est nulle sauf sur l'ensemble dénombrable
$A = \{a_0, a_1, \dots\}$ de $[a, b]$, alors elle est intégrable et
d'intégrale nulle. Soit $\varepsilon > 0$ ; considérons la jauge de
$[a, b]$ définie par $$
\gamma(t) = \left| 
\begin{array}{rl}
\left]a_i - \varepsilon / (2^{i+2}  |h(a_i)|), t_i + \varepsilon / (2^{i+2} |h(a_i)|)  \right[ & \mbox{si $t=t_i \in A$,} \\
\mathbb{R}& \mbox{sinon.}
\end{array}
\right.
$$ Si la subdivision pointée $\mathcal{D}$ de $[a, b]$ est subordonnée à
$\gamma$ et si $(t, I) \in \mathcal{D}$, on a donc soit $t = a_i \in A$
auquel cas $$
|h(t) \ell(I)| \leq |h(a_i)|\times 2 \times \frac{\varepsilon}{2^{i+2}|h(a_i)|}
= \frac{\varepsilon}{2^{i+1}},
$$ soit $t \not \in A$ auquel cas $h(t) =0$ et donc $h(t) \ell(I) = 0$.
Dans tous les cas, la somme de Riemann $S(h, \mathcal{D})$ vérifie $$
|S(h,\mathcal{D}) - 0| \leq \sum_{i=0}^{+\infty} \frac{\varepsilon}{2^{i+1}} = \varepsilon.
$$ La fonction $h$ est donc intégrable et d'intégrale nulle.
:::

::: {.section}
#### Continuité des intégrales indéterminées simplifiée {#answer-exo-ciis .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Continuité des intégrales indéterminées simplifiée}`{=latex}

Supposons que $|f| \leq M$ sur $[a, b]$. Alors, si $$
g(x) := \int_c^x f(t) \, dt 
$$ et $h\geq 0$, [l'addivité de l'intégrale (p.
`\pageref*{additivituxe9}`{=tex})](#additivité), [l'inégalité
triangulaire (p.
`\pageref*{inuxe9galituxe9-triangulaire}`{=tex})](#inégalité-triangulaire)
et [la croissance de l'intégrale (p.
`\pageref*{croissance}`{=tex})](#croissance) nous fournissent $$
|g(x+h) - g(x)| = \left|\int_{x}^{x+h} f(t) \, dt\right| \leq  \int_{x}^{x+h} |f(t)| \, dt
\leq \int_{x}^{x+h} M \, dt
$$ et donc $|g(x+h) - g(x)| \leq M h$. Un raisonnement similaire pour
$h \leq 0$ nous fournit dans tous les cas $|g(x+h) - g(x)| \leq M|h|$.
La fonction $g$ est donc continue.
:::

::: {.section}
#### Limite d'intégrale {#answer-exo-cii .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Limite d'intégrale}`{=latex}

D'après [un exercice précédent (p. `\pageref*{iis}`{=tex})](#iis), la
fonction $f$ nulle en $0$ et égale à $1/\sqrt{t}$ sur
$\left]0, 1\right]$ est intégrable. Comme $$
\int_0^0 f(t) \, dt = 0,
$$ [par continuité des intégrales indéterminées (p.
`\pageref*{cii}`{=tex})](#cii), on en déduit que $$
\lim_{\varepsilon \to 0} \int_0^{\varepsilon} f(t) \, dt = \int_0^0 f(t) \, dt = 0.
$$
:::

::: {.section}
#### Dérivabilité presque partout {#answer-dpp .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Dérivabilité presque partout}`{=latex}

On peut par exemple considérer la fonction $f:[0, 1] \to \mathbb{R}$
définie par $$
f(x) = \left| 
\begin{array}{rl}
0 & \mbox{si $x \leq 1/2,$} \\
1 & \mbox{sinon.}
\end{array}
\right.
$$ On vérifie facilement que $$
g(x) := \int_0^x f(t) \, dt = \max(0, x-1/2)
$$ et cette fonction n'est pas dérivable en $x=1/2$.
:::

::: {.section}
#### Normalisation des fonctions {#answer-pl .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Normalisation des fonctions}`{=latex}

Sauf pour $t=a$ ou $t=b$, on a pour tout $h$ suffisamment petit $$
\int_{t-h}^{t+h} f(x) \, dx
= \int_a^{t+h} f(x) \, dx - \int_{a}^{t-h} f(x) \, dx,
$$ donc en posant $$
F(t) = \int_a^t f(x) \, dx,
$$ on obtient `\begin{align*}
\frac{1}{2h}\int_{t-h}^{t+h} f(x) \, dx &= \frac{F(t+h) - F(t-h)}{2h} \\
&= \frac{1}{2}\frac{F(t+h) - F(t)}{h} + \frac{1}{2}\frac{F(t-h) - F(t)}{(-h)}.
\end{align*}`{=tex} Or d'après [le théorème de dérivation des intégrales
indéterminées (p. `\pageref*{dii}`{=tex})](#dii), $F$ est dérivable en
presque tout $x$ et de dérivée $f(x)$. On a donc en un tel point $$
g(x) = \lim_{\substack{h\to 0 \\ h\neq 0}} \frac{1}{2h}\int_{t-h}^{t+h} f(x) \, dx
= \frac{1}{2}F'(x) + \frac{1}{2}F'(x) = f(x).
$$ Les fonctions $f$ et $g$ sont donc égales presque partout.
:::

::: {.section}
#### Changement de variables simplifié {#answer-cv .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Changement de variables simplifié}`{=latex}

La fonction $f$ étant continue sur $[c,d]$, elle y admet une primitive
$h$. Par la règle de dérivation en chaîne, la fonction
$t \in [a, b] \mapsto h(g(t))$ a pour dérivée
$h'(g(t))g'(t) = f(g(t)) g'(t)$. Avec les hypothèses supplémentaires,
cette fonction est continue, comme composée et produit de fonctions
continues, donc intégrable sur $[a, b]$. Par [le théorème fondamental du
calcul (p. `\pageref*{TFC}`{=tex})](#TFC), on a donc $$
\int_a^b f(g(t)) g'(t) \, dt
=
\left[h \circ g\right]_a^b = h(g(b)) -  h(g(a)).
$$ D'autre part, comme $f$ est continue et a $h$ comme primitive, $$
\int_{g(a)}^{g(b)} f(x) \, dx = \int_{g(a)}^{g(b)} h'(x) \, dx = [h]_{g(a)}^{g(b)} = h(g(b)) -  h(g(a)) \, ;
$$ les deux intégrales sont donc égales.
:::

::: {.section}
#### Changement de variable $x=t^2$ {#answer-ft2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Changement de variable \(x=t^2\)}`{=latex}

La fonction $g: t \in [0, 1] \to t^2 \in \mathbb{R}$ vérifie [les
hypothèses du théorème de changement de variable (p.
`\pageref*{changement-de-variable}`{=tex})](#changement-de-variable)
avec $g([0,1]) = [0,1]$. En effet $g$ est continue en $0$ et en $1$ et
$g'$ est définie sur $\left]0,1\right[$, de valeur $g'(t) = 2t$ ; elle y
est donc continue et ne s'y annule pas. Par conséquent, $$
\int_0^1 f(x) \, dx = \int_{g(0)}^{g(1)} f(x) \, dx = 
\int_0^1 f(t^2) \times (2 t) \, dt
= 2 \int_0^1 t f(t^2) \, dt.
$$
:::

::: {.section}
#### Changement de variable $x=\sqrt{t}$ {#answer-fst .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Changement de variable \(x=\sqrt{t}\)}`{=latex}

L'expression suggère que l'on utilise le changement de variable
$x=\sqrt{t}$, et la fonction
$g : t\in[0, 1] \mapsto \sqrt{t} \in \mathbb{R}$ est [un changement de
variable valide (p.
`\pageref*{changement-de-variable}`{=tex})](#changement-de-variable)
avec $g([0,1]) = [0,1]$ : elle est continue en $0$ et $1$, dérivable sur
$\left]0, 1\right[$, de dérivée $g'(t) = 1/2\sqrt{t}$ qui est continue
et ne s'annule pas sur $\left]0, 1\right[$. Par contre, l'application du
changement de variable suppose de faire apparaître le terme $g'(t) dt$.
On écrit donc $$
\int_0^1 f(\sqrt{t}) \, dt 
= \int_0^1 (2\sqrt{t}) f(\sqrt{t}) \frac{1}{2\sqrt{t}}\, dt
= 
\int_{g(0)}^{g(1)} 2 x f(x) dx
= 
2 \int_0^1 x f(x) dx.
$$
:::

::: {.section}
#### Prendre la tangente {#answer-plt .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Prendre la tangente}`{=latex}

On applique [le théorème de changement de variable (p.
`\pageref*{changement-de-variable}`{=tex})](#changement-de-variable)
avec à la fonction $$
g : 
t \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right] 
\mapsto 
\left|
\begin{array}{rl}
-\infty & \mbox{si $x=-\pi/2$,} \\
\tan t & \mbox{si $-\pi/2 < x < \pi/2$,} \\
+\infty & \mbox{si $x=\pi/2$.}
\end{array}
\right.
$$ Cette fonction est bien continue en $-\pi/2$ et $\pi/2$, dérivable
sur $\left]-\pi/2,\pi/2\right[$, de dérivée $$
g'(t) = (\tan t)' = 1+ \tan^2 t,
$$ qui est continue et ne s'annule pas. Par conséquent, comme
$g([-\pi/2, \pi/2]) = [-\infty, \infty]$, une fonction
$f: [-\infty, +\infty] \to \mathbb{R}$ (ou de $\mathbb{R}$ dans
$\mathbb{R}$) est intégrable si et seulement si $$
\int_{-\pi/2}^{\pi/2} f(g(t))g'(t) \, dt
=
\int_{-\pi/2}^{\pi/2} f(\tan t)(1 + \tan^2 t) \, dt
$$ est intégrable et dans ce cas, les deux intégrales sont égales.
:::
:::

::: {.section}
Méthode des trapèzes
--------------------

::: {.section}
#### Question 1 {#answer-mt-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

L'aire du trapèze considéré est identique à l'aire du rectangle de
largeur $(b-a)/m$ et dont la hauteur est la moyenne de $f(a + i(b-a)/m)$
et $f(a + (i+1)(b-a)/m)$, soit $$
\frac{b-a}{m} \left(\frac{f\left(a + i\frac{b-a}{m}\right) + f\left(a + (i+1)\frac{b-a}{m}\right) }{2}\right).
$$ La méthode des trapèzes approxime donc l'aire sous le graphe de la
fonction $f$ en approximant cette région par $m$ trapèzes.

![L'aire de la zone grisée correspond l'estimation de l'intégrale de
$f : t \in [0,1] \mapsto \sqrt{t}/2$ par la méthode des trapèzes pour la
subdivision
$\mathcal{D} = \{[0, 0.2], \dots, [0.8, 1]\}$.](images/subdivision-trapèzes.py.pdf)
:::

::: {.section}
#### Question 2 {#answer-mt-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

On peut constater en réarrangeant les termes de la somme $S_m$ que
`\begin{align*}
S_m &= \frac{b-a}{m}\sum_{i=0}^{m-1} \frac{f\left(a + i \frac{b-a}{m}\right) + f\left(a + (i+1) \frac{b-a}{m}\right)}{2} \\
&= \frac{b-a}{m}
\left(
  \frac{1}{2} f(a) 
  + \sum_{i=1}^{m-1} 
      f\left(a + i \frac{b-a}{m}\right)
  + \frac{1}{2} f(b)
\right),
\end{align*}`{=tex} soit, en introduisant la subdivision pointée
`\begin{align*}
\mathcal{D}^*_m &= 
\left\{
\left(f(a), \left[0, \frac{b-a}{2m}\right]\right), \vphantom{\int} \right. \left(f\left(a+\frac{b-a}{m}\right), \left[\frac{b-a}{2m}, \frac{3(b-a)}{2m}\right]\right), \\
&\phantom{=}\; \dots, \\
&\phantom{=}
\left(f\left(a+\frac{(m-1)(b-a)}{m}\right), \left[(2(m-2)+1)\frac{b-a}{2m}, (2(m-1)+1)\frac{b-a}{2m}\right]\right), \\
&\phantom{=}\left.\vphantom{\int} \left(f(b), \left[b - \frac{b-a}{2m}, b \right]\right)
\right\}
\end{align*}`{=tex} que $S_m = S(f, \mathcal{D}^*_m)$. Comme
$\max \left\{\ell(I) \left| (t, I) \in \mathcal{D}^*_m \right.\right\} = (b-a)/m$,
quel que soit $\delta > 0$, ce maximum tend vers $0$ quand
$m \to +\infty$. Par conséquent, si $f$ est intégrable au sens de
Riemann, $$
\lim_{m\to +\infty} S_m = \lim_{m\to +\infty} S(f, \mathcal{D}^*_m) = \int_a^b f(t) \, dt.
$$
:::
:::

::: {.section}
Fonctions non intégrables
-------------------------

::: {.section}
#### Question 1 {#answer-id1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Supposons que $f:\left[a, +\infty \right[\to \mathbb{R}$ est intégrable.
La valeur $$
I := \int_a^{+\infty} |f(t)| \, dt
$$ est bien définie (et finie) car $f$ est intégrable. [Par restriction
(p. `\pageref*{restriction}`{=tex})](#restriction), pour tout
$x \in \left[a, +\infty \right[$, les intégrales $$
\int_a^x |f(t)| \, dt \; \mbox{ et } \; \int_x^{+\infty} |f(t)| \, dt
$$ existent et sont positives [par croissance de l'intégrale (p.
`\pageref*{croissance}`{=tex})](#croissance) ; [par additivité (p.
`\pageref*{additivituxe9}`{=tex})](#additivité), comme $$
\int_a^x |f(t)| \, dt + \int_x^{+\infty} |f(t)| \, dt = \int_a^{+\infty} |f(t)|\, dt
$$ on a pour tout $x \in \left[a, +\infty \right[$ $$
\int_a^x |f(t)| \, dt \leq \int_a^{+\infty} |f(t)| \, dt < +\infty.
$$ L'hypothèse de départ ($f$ intégrable) est donc incompatible avec la
propriété $$
\lim_{x \to +\infty} \int_a^x f(t) \, dt = +\infty.
$$
:::

::: {.section}
#### Question 2 {#answer-id2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Par le théorème fondamental du calcul, pour tout
$x \in \left[1, +\infty\right[$, on a $$
\int_1^x \frac{dx}{x} = [\ln]_1^x = \ln x.
$$ Par conséquent, $$
\lim_{x \to +\infty} \int_1^x \frac{dx}{x} = +\infty
$$ et la fonction $x \mapsto 1/x$ n'est pas intégrable sur
$\left[1, +\infty\right[$.
:::

::: {.section}
#### Question 3 {#answer-id3 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Soit $x \in \left[1, +\infty \right[$ et soit $n_x$ le plus grand entier
tel que $2\pi(n_x + 3/4) \leq x$, soit $$
n_x := \left \lfloor \frac{x}{2\pi} - \frac{3}{4} \right \rfloor.
$$ Par [additivité (p. `\pageref*{additivituxe9}`{=tex})](#additivité)
et [croissance de l'intégrale (p.
`\pageref*{croissance}`{=tex})](#croissance), on a `\begin{align*}
\int_1^x \left|\frac{\sin t}{t} \right| \,dt &\geq \sum_{i=1}^{n_x} \int_{2\pi(i+1/4)}^{2\pi(i+3/4)} \left|\frac{\sin t}{t} \right| \, dt \\
&\geq \sum_{i=1}^{n_x} \int_{2\pi(i+1/4)}^{2\pi(i+3/4)} \left|\frac{\sin t}{2\pi(i+3/4)} \right| \, dt \\
&\geq \sum_{i=1}^{n_x} \frac{1}{{2\pi(i+3/4)}} \int_{2\pi(i+1/4)}^{2\pi(i+3/4)} \sin t \, dt \\
&\geq \frac{1}{2\pi} \sum_{i=1}^{n_x} \frac{1}{i+3/4} \left[-\cos\right]_{2\pi(i+1/4)}^{2\pi(i+3/4)}  \\
&\geq \frac{1}{\sqrt{2}\pi} \sum_{i=1}^{n_x} \frac{1}{i+3/4}.
\end{align*}`{=tex} Comme $n_x \to +\infty$ quand $x\to +\infty$ et que
la série des $1/(i+3/4)$ tend vers $+\infty$, la fonction
$x \mapsto (\sin x)/ x$ n'est pas intégrable sur
$\left[1, +\infty\right[$.
:::
:::

::: {.section}
L'intégrale de Riemann est absolue {#answer-Rabs .answer .unnumbered .unlisted}
----------------------------------

`\addcontentsline{toc}{subsection}{L'intégrale de Riemann est absolue}`{=latex}

Nous exploitons [le critère de Lebesgue pour l'intégrabilité au sens de
Riemann (p. `\pageref*{CIL}`{=tex})](#CIL) : si $f$ est intégrable au
sens de Riemann, elle est bornée -- et donc $f$ également -- et continue
presque partout -- et donc $|f|$ également ($|f|$ est continue en tout
point où $f$ est continue comme composée de fonctions continues en ce
point). Par conséquent, $|f|$ est intégrable au sens de Riemann.
:::

::: {.section}
Continuité presque partout
--------------------------

::: {.section}
#### Question 1 {#answer-cpp-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Une fonction égale presque partout à une fonction continue n'est pas
nécessairement presque partout continue. La fonction de Dirichlet de [la
question 2 (p. `\pageref*{cpp-2}`{=tex})](#cpp-2) fournit un bon
exemple : elle est égale à la fonction identiquement nulle -- qui est
continue -- sur tout $\mathbb{R}$ à l'exception des rationnels et
l'ensemble des rationnels est négligeable, [car dénombrable (p.
`\pageref*{edn}`{=tex})](#edn). Mais elle n'est continue en aucun point,
car tout nombre rationnel est limite de nombres irrationnels et
réciproquement.

La réciproque n'est pas vérifiée non plus : la fonction de Heaviside
$e:\mathbb{R}\to \mathbb{R}$ -- ou fonction indicatrice de
$\left[0, +\infty \right[$, définie par $$
e(x) = \left|
\begin{array}{cl}
1 & \mbox{si } x\geq 0,\\
0 & \mbox{sinon.}
\end{array}
\right.
$$ est continue presque partout (sauf en $0$). Mais aucune modification
de cette fonction sur un ensemble négligeable ne pourra la rendre
continue en $0$ ; en effet, comme aucun intervalle de la forme
$\left]-\varepsilon, 0\right[$ ou $\left]0, \varepsilon\right[$ n'est
négligeable, après modification de $f$ sur un ensemble négligeable, la
fonction $g$ qui en résulte est encore égale à $f$ sur une suite de
valeurs $x_k<0$ tendant vers $0$ et sur une suite de valeurs $y_k > 0$
tendant vers $0$. On a donc $$
\lim_{k \to +\infty} g(y_k) - g(x_k) = \lim_{k \to +\infty} f(y_k) - f(x_k) = 1.
$$ La fonction $g$ ne peut donc pas être continue en $0$.
:::

::: {.section}
#### Question 2 {#answer-cpp-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

La fonction de Dirichlet $1_{\mathbb{Q}}$ sur $[0, 1]$ est égale presque
partout à la fonction identiquement nulle qui est continue, elle est
donc intégrable au sens de Lebesgue. Mais elle n'est pas continue
presque partout, donc elle n'est pas intégrable au sens de Riemann.
:::
:::

::: {.section}
Poussière de Cantor {#poussière-de-cantor}
-------------------

::: {.section}
#### Question 1 {#answer-cantor-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

L'ensemble $C$ peut être recouvert par la collection ne contenant que
l'intervalle $\mathcal{A}_0 = \left[0, 1\right[$, ou par la collection
d'intervalles $$
\mathcal{A}_1 = \{\left[0, 1/3\right[, \left[2/3, 1\right[\}
$$ qui contient exactement les nombres $x$ de $\left[0,1\right[$ dont le
premier chiffre du développement propre en base 3 est 0 ou 2 : $$
x = 0.0\cdots \, \mbox{ ou } \, x = 0.2\cdots
$$ On a clairement $$
\sum_{I \in \mathcal{A}_1} \ell(I) = \ell(\left[0,1\right[) = 1
\, \mbox{ et } \,
\sum_{I \in \mathcal{A}_1} \ell(I) = 2 \times \frac{1}{3} = \frac{2}{3}.
$$ On peut poursuivre le procédé en considérant la collection
$\mathcal{A}_n$ des $2^n$ intervalles dont l'union $C_n$ forme
l'ensemble des nombres $x$ dont les $n$ premiers chiffres du
développement décimal propre sont $0$ ou $2$, ensemble qui contient $C$.

![Représentation de $C_n$ pour
$n \in \{0, 1, \dots, 5\}$.](images/cantor-dust.py.pdf)

On peut de plus se convaincre par récurrence que $$
\sum_{I \in \mathcal{A}_n} \ell(I) = 2^n \times \frac{1}{3^n} = \left(\frac{2}{3}\right)^n.
$$ Comme $(2/3)^n$ tend vers $0$ quand $n$ tend vers $+\infty$, nous
avons établi que $C$ est négligeable.
:::

::: {.section}
#### Question 2 {#answer-cantor-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

L'opération $$
x=\sum_{i=1}^{+\infty} a_i 3^{-n} \in C \mapsto y=\sum_{i=1}^{+\infty} b_i 2^{-i} \in \left[0, 1\right[
\; \mbox{ où } \;
b_i = \left|
\begin{array}{rl}
0 &\mbox{si $a_i = 0$,} \\
1 &\mbox{si $a_i = 2$.}
\end{array}
\right.
$$ est une bijection de $C$ sur $\left[0, 1\right[$, ce qui montre que
$C$ a la puissance du continu (et donc n'est pas dénombrable).
:::
:::
:::

::: {.section}
Références
==========
:::

[^1]: Ce document est un des produits du projet [$\mbox{\faGithub}$
    `boisgera/CDIS`](https://github.com/), initié par la collaboration
    de [(S)ébastien
    Boisgérault](mailto:sebastien.boisgerault@mines-paristech.fr)
    (CAOR), [(T)homas Romary](mailto:thomas.romary@mines-paristech.fr)
    et [(E)milie Chautru](mailto:emilie.chautru@mines-paristech.fr)
    (GEOSCIENCES), [(P)auline
    Bernard](mailto:pauline.bernard@mines-paristech.fr) (CAS), avec la
    contribution de [Gabriel
    Stoltz](mailto:gabriel-stolz@mines-paristech.fr) (Ecole des Ponts
    ParisTech, CERMICS). Il est mis à disposition selon les termes de
    [la licence Creative Commons "attribution -- pas d'utilisation
    commerciale -- partage dans les mêmes conditions" 4.0
    internationale](http://creativecommons.org/licenses/by-nc-sa/).

[^2]: l'étude des démonstrations du cours peut toutefois contribuer à
    votre apprentissage, au même titre que la résolution d'exercices.

[^3]: c'est-à-dire réduits à un point.

[^4]: et par la suite, au sens de Henstock-Kurzweil ou de Lebesgue.

[^5]: techniquement, compte tenu du procédé employé, on devrait parler
    de "mesure extérieure de longueur", la longueur d'un ensemble
    arbitraire de $\mathbb{R}$ n'étant pas toujours définie.

[^6]: Par exemple, [la forme générale du théorème fondamental du calcul
    (p. `\pageref*{TFC}`{=tex})](#TFC) n'est valable ni pour l'intégrale
    de Riemann, ni pour l'intégrale de Lebesgue, mais elle l'est pour
    l'intégrale de Henstock-Kurzweil. On rappelle que cette forme
    générale permet d'établir la preuve de l'inégalité des
    accroissements finis. [Le théorème de Hake (p.
    `\pageref*{hake}`{=tex})](#hake), qui établit que les intégrales
    impropres ne sont jamais nécessaires, est aussi spécifique à
    l'intégrale de Henstock-Kurzweil.

[^7]: La définition originale de Lebesgue de l'intégrale, antérieure à
    la définition qui exploite l'intégrale de Henstock-Kurzweil,
    n'utilise ni jauge ni somme de Riemann, mais introduit une rupture
    franche dans la façon d'aborder la question.

[^8]: Mais ces termes sont génériques ; en particulier il existe
    d'autres intégrales dont la définition repose sur des sommes de
    Riemann et des jauges, comme l'intégrale de McShane.

[^9]: Techniquement, Jaroslav Kurzweil a inventé cette construction
    avant Ralph Henstock dans les années 1950, mais dans un but bien
    précis -- l'étude des équations différentielles généralisées --
    probablement sans réaliser totalement la portée de sa définition.

[^10]: Arnaud Denjoy et Oskar Perron ont introduit dès les années 1910
    des intégrales équivalentes, mais dont les définitions sont beaucoup
    plus complexes et en apparence très différentes ; en particulier,
    les sommes de Riemann n'interviennent pas dans leurs définitions.

[^11]: On peut trouver un recouvrement de $A$ par des intervalles $J_i$
    non nécessairement ouverts, tels que
    $\sum_i \ell(J_i) \leq \varepsilon/2$, puis remplacer chaque $J_i$
    par un intervalle $I_i$ ouvert de longueur double contenant $J_i$.

[^12]: Contrairement à l'intégrale de Riemann, il n'est pas nécessaire
    pour donner un sens à l'intégrale sur $\mathbb{R}$ d'une fonction de
    calculer tout d'abord son intégrale sur un intervalle borné puis
    d'essayer de passer à la limite, sans garantie que le nouveau type
    d'intégrale qui en résulte -- l'intégrale de Cauchy-Riemann --
    partage les propriétés de l'intégrale de Riemann.

[^13]: Vous remarquerez que nous n'avons pas listé le [théorème
    fondamental du calcul (p. `\pageref*{TFC}`{=tex})](#TFC) dans les
    propriétés valables en non borné ; celui-ci peut également être
    exprimé sous une forme valable dans ce cadre, mais elle est un peu
    plus complexe, avec des hypothèses qui rappellent celles du
    [théorème de changement de variable (p.
    `\pageref*{changement-de-variable}`{=tex})](#changement-de-variable)
    : si $f:[a, b] \mapsto \mathbb{R}$ est continue sur $[a, b]$,
    dérivable sur $\left]a, b\right[$ et que cette dérivée $f'$ est
    intégrable, alors $$
    f(b) - f(a) = \int_a^b f'(t) \, dt.
    $$

[^14]: Dans le cas contraire, $x=1/3$ par exemple s'écrit $0.1000\cdots$
    en base 3 mais aussi $0.0222\cdots$.
