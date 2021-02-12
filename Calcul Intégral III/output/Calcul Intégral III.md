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
title: Calcul Intégral III
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
-   [Intégrale de fonctions de plusieurs
    variables](#intégrale-de-fonctions-de-plusieurs-variables)
    -   [Volume d'un pavé](#volume-dun-pavé)
    -   [Subdivision pointée](#subdivision-pointée)
    -   [Propriétés élémentaires](#propriétés-élémentaires)
    -   [Produit d'ensembles mesurables](#produit-densembles-mesurables)
-   [Intégrale multiple](#intégrale-multiple-1)
-   [Changement de variables](#changement-de-variables)
-   [Annexe -- Théorème de la divergence](#annexe)
-   [Exercices complémentaires](#exercices-complémentaires)
    -   [Aire du disque unité](#adu)
    -   [Intégrabilité des fonctions
        puissances](#intégrabilité-des-fonctions-puissances)
    -   [Déformations d'un compact à bord
        régulier](#déformations-dun-compact-à-bord-régulier)
    -   [Ovales de Cassini](#ovales-de-cassini)
    -   [Intégrales de surface](#intégrales-de-surface)
    -   [Rétraction](#rétraction)
    -   [Intégration par parties](#intégration-par-parties)
-   [Solutions](#solutions)
    -   [Exercices essentiels](#exercices-essentiels)
    -   [Intégrabilité des fonctions
        puissances](#intégrabilité-des-fonctions-puissances-1)
    -   [Déformations d'un compact à bord
        régulier](#déformations-dun-compact-à-bord-régulier-1)
    -   [Ovales de Cassini](#ovales-de-cassini-1)
    -   [Intégrales de surface](#intégrales-de-surface-1)
    -   [Rétraction](#rétraction-1)
    -   [Intégration par parties](#intégration-par-parties-1)
-   [Réferences](#réferences)

```{=tex}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}
```
```{=tex}
\newcommand{\zero}{$\mathord{\boldsymbol{\circ}}$}
\newcommand{\one}{$\mathord{\bullet}$}
\newcommand{\two}{$\mathord{\bullet}\mathord{\bullet}$}
\newcommand{\three}{$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$}
\newcommand{\four}{$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$}
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
#### Construction de l'intégrale dans $\mathbb{R}^n$

-   `$\mathord{\bullet}$ `{=tex}savoir définir un pavé de $\mathbb{R}^n$
    (ou de $[-\infty, \infty]^n$),

-   `$\mathord{\bullet}$ `{=tex}savoir calculer son volume
    $n$-dimensionnel,

-   savoir comment exploiter dans ce cadre $n$-dimensionnel les
    concepts :

    -   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}d'ensemble
        négligeable,

    -   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}de subdivision
        pointée,

    -   `$\mathord{\bullet}$ `{=tex}de somme de Riemman,

    -   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}de jauge et de
        subdivision subordonnée,

    -   `$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$ `{=tex}d'intégrale
        de Lebesgue.
:::

::: {.section}
#### Ensembles et fonctions mesurables

-   savoir caractériser :

    -   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}les ensembles de
        mesure finie et mesurables de $\mathbb{R}^n$,

    -   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}les fonctions
        mesurables (critère de l'image réciproque),

    -   `$\mathord{\bullet}$ `{=tex}les fonctions intégrables (critère
        d'intégrabilité dominée).
:::

::: {.section}
#### Propriétés de l'intégrale dans $\mathbb{R}^n$

-   savoir exploiter

    -   `$\mathord{\bullet}$ `{=tex}la linéarité de l'intégrale,

    -   `$\mathord{\bullet}$ `{=tex}sa croissance et l'inégalité
        triangulaire,

    -   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}les relations entre
        intégrale et égalité presque partout,

    -   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}les théorèmes de
        convergence.
:::

::: {.section}
#### Intégrale multiple

-   `$\mathord{\bullet}$ `{=tex}savoir calculer une intégrale dans
    $\mathbb{R}^n$ au moyen de $n$ intégrales dans $\mathbb{R}$,

-   `$\mathord{\bullet}$ `{=tex}connaître les variantes de cette
    technique (ordre et nombre des variables),

-   `$\mathord{\bullet}$ `{=tex}connaître l'hypothèse d'intégrabilité
    validant ce calcul (Fubini),

-   `$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$ `{=tex}connaître
    les propriétés des fonctions intermédiaires (Fubini),

-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir caractériser
    l'intégrabilité des fonctions positives (Tonelli),

-   `$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$ `{=tex}connaître
    les propriétés des fonctions intermédiaires (Tonelli),

-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir caractériser
    l'intégrabilité des fonctions signées (via Tonelli).
:::

::: {.section}
#### Changement de variables

-   `$\mathord{\bullet}$ `{=tex}connaître la formule du changement de
    variables,

-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}connaître les
    hypothèses du théorème et son résultat d'intégrabilité,

-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir appliquer le
    théorème de façon relativement directe,

-   `$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir
    introduire un changement de variables quand c'est pertinent.
:::

::: {.section}
#### Théorème de la divergence

-   `$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir
    caractériser un compact à bord $C^1$,

-   `$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir
    calculer la normale extérieure d'un tel ensemble,

-   `$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$ `{=tex}connaître
    la définition d'intégrale de surface,

-   `$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir
    exploiter le théorème de la divergence.
:::
:::

::: {.section}
Intégrale de fonctions de plusieurs variables
=============================================

::: {.section}
### Remarque -- Domaine des variables {#dv .remark .ante .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Domaine des variables}`{=latex}

Comme pour les fonctions d'une seule variable, la théorie de l'intégrale
de jauge des fonctions de plusieurs variables est applicable à des
variables pouvant prendre des valeurs réelles ou infinies. Mais il
s'agit largement d'un "détail d'implémentation" : en pratique, le besoin
que nous souhaitons satisfaire, c'est l'intégration des fonctions de
variables réelles ; pour nous conformer à ce cas d'usage principal, et
après avoir construit l'intégrale dans le domaine $[-\infty,\infty]^n$,
nous énoncerons uniquement les propriétés de l'intégrale dans le domaine
$\mathbb{R}^n$. Quand il sera nécessaire de considérer une fonction de
variables réelles comme fonction de variables réelles étendues (pouvant
être infinies), on prolongera la fonction initiale en lui assignant la
valeur zéro dès qu'une de leur variables est infinie[^3]. De façon
similaire, il est possible de définir l'intégrale d'une fonction
$f: A \to \mathbb{R}$ où $A \subset \mathbb{R}^n$ en la prolongeant par
zéro sur $\mathbb{R}^n$ (ou directement sur $[-\infty, +\infty]^n$).
:::

::: {.section}
#### Exercice -- Prolongements ($\mathord{\bullet}$) {#p .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Prolongements}`{=latex}

A quelles fonctions de $[-\infty, +\infty]^2 \to \mathbb{R}$ sont
associées la fonction
$(x, y) \in \mathbb{R}^2 \mapsto \exp(-x^2-y^2) \in \mathbb{R}$, la
fonction
$(x, y) \in \mathbb{R}^2 \mapsto \arctan (x^2 + y^2) \in \mathbb{R}$, la
fonction $(x, y) \in [-1,1]^2 \mapsto 1 \in \mathbb{R}$ ? ([Solution p.
`\pageref*{answer-p}`{=tex}](#answer-p){.no-parenthesis}.)
:::

::: {.section}
Dans la suite, les pavés joueront pour l'intégration des fonctions de
plusieurs variables le rôle qui était dévolu aux intervalles pour les
fonctions d'une variable :
:::

::: {.section}
### Définition -- Pavés {#pavés .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Pavés}`{=latex}

On appelle *pavé* de $[-\infty,+\infty]^n$ tout ensemble $I$ de la forme
$$
I = I_1 \times \dots \times I_n
$$ où les $I_i$ sont des intervalles de $[-\infty,+\infty]$.

![Réprésentation du pavé $[1,3] \times [1, 2]$ du plan
(étendu).](images/pavé.svg.pdf)
:::

::: {.section}
#### Exercice -- Partition en pavés ($\mathord{\bullet}$) {#pp .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Partition en pavés}`{=latex}

Montrer que l'ensemble $\mathbb{R}^2 \setminus [-1,1]^2$ peut être
partitionné en 4 pavés. ([Solution p.
`\pageref*{answer-pp}`{=tex}](#answer-pp){.no-parenthesis}.)
:::

::: {.section}
### Volume d'un pavé

On appelle *volume $n$-dimensionnel* (ou parfois simplement *volume*
quand le contexte est clair) du pavé $I = I_1 \times \dots \times I_n$
de $[-\infty,+\infty]^n$ la valeur $$
\lambda(I) := \ell(I_1) \times \dots \times \ell(I_n) \in \left[0, +\infty \right],
$$ en adoptant la convention que $0 \times \infty = 0$.
:::

::: {.section}
### Remarque -- Longueur, aire, volume {#longueur-aire-volume .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Longueur, aire, volume}`{=latex}

On pourra continuer à appeler cette grandeur *longueur* plutôt que
*volume $n$-dimensionnel* si l'on travaille dans $\mathbb{R}$ (ou
$[-\infty,+\infty]$) ; dans $\mathbb{R}^2$ (ou $[-\infty,+\infty]^2$) il
est approprié de la désigner sous le terme d'*aire* et dans
$\mathbb{R}^3$ (ou $[-\infty, +\infty]^3$) sous le terme de *volume*. On
pourra dans ces trois cas particuliers préférer les notation $\ell$, $a$
et $v$ au symbole $\lambda$.
:::

::: {.section}
#### Exercice -- Volume de pavés ($\mathord{\bullet}$) {#exo-volume-pavé .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Volume de pavés}`{=latex}

Calculer l'aire des pavés $\{(0,0)\}$, $[-1, 1]^2$,
$[-1, 1] \times [0, +\infty]$ et $\{0\} \times \mathbb{R}$ de
$[-\infty, +\infty]^2$. ([Solution p.
`\pageref*{answer-exo-volume-pavuxe9}`{=tex}](#answer-exo-volume-pavé){.no-parenthesis}.)
:::

::: {.section}
### Définition -- Ensemble négligeable {#ensemble-négligeable .definition .two .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Ensemble négligeable}`{=latex}

Un ensemble $A$ de $[-\infty, +\infty]^n$ est *négligeable* si pour tout
$\varepsilon > 0$, il existe une collection dénombrable de pavés $I_1$,
$I_2$, $\dots$, de $[-\infty,+\infty]^n$ qui recouvre l'ensemble $A$ --
telle que $A \subset \bigcup_{i} I_i$ -- et vérifiant $$
\sum_i \lambda(I_i) \leq  \varepsilon.
$$
:::

::: {.section}
#### Exercice -- Domaine à l'infini ($\mathord{\bullet}$) {#dai .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Domaine à l'infini}`{=latex}

Montrer que l'ensemble $[-\infty,+\infty]^n \setminus \mathbb{R}^n$ est
d'aire négligeable. ([Solution p.
`\pageref*{answer-dai}`{=tex}](#answer-dai){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Graphe du sinus ($\mathord{\bullet}\mathord{\bullet}$) {#gs .exercise .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Graphe du sinus}`{=latex}

Montrer que l'ensemble $$G = \{(x, \sin x) \; | \; x \in [0, 2\pi]\}$$
est d'aire négligeable.

![Graphe de la fonction $\sin$ sur $[0, 2\pi]$.](images/sin.py.pdf)

([Solution p.
`\pageref*{answer-gs}`{=tex}](#answer-gs){.no-parenthesis}.)
:::

::: {.section}
### Définition -- Presque partout {#presque-partout .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Presque partout}`{=latex}

Une propriété $P$ dépendant d'un vecteur $x \in [-\infty,\infty]^n$ est
vraie *presque partout* si l'ensemble des points $x$ où elle est fausse
est un ensemble négligeable. On pourra utiliser la notation "$P$ p.p."
ou "$P(x)$ p.p." pour signifier que la propriété $P$ est vraie presque
partout.
:::

::: {.section}
### Subdivision pointée

Une *subdivision pointée* du pavé fermé $I$ de $[-\infty,+\infty]^n$ est
une famille finie $$
\{(t_i, J_i) \; | \; \; 0 \leq i \leq k-1\}
$$ où les $J_i$ sont des pavés fermés de $I$ *sans chevauchement* (les
intersections deux à deux des pavés de cette collection sont des
ensembles négligeables) qui recouvrent $I$ et tels que $t_i \in J_i$
pour tout $i \in \{0, \dots, k-1\}.$

![Une subdivision pointée de $[-\infty, \infty]^2$ comportant 12
pavés.](images/pavage.svg.pdf)
:::

::: {.section}
### Définition -- Somme de Riemman {#somme-de-riemman .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Somme de Riemman}`{=latex}

La *somme de Riemann* associée à la fonction $f:I \to \mathbb{R}$, où
$I$ est un pavé fermé de $[-\infty,+\infty]^n$, et à la subdivision
pointée $\mathcal{D}$ de $I$ est la grandeur $$
S(f, \mathcal{D}) = \sum f(t) \lambda(J), \; \; (t, J) \in \mathcal{D}, \, \lambda(J) < + \infty.
$$
:::

::: {.section}
### Définition -- Jauge {#jauge .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Jauge}`{=latex}

Une *jauge* $\gamma$ sur un pavé fermé $I$ de $[-\infty,+\infty]^n$ est
une fonction qui associe à tout $t \in I$ un pavé ouvert $\gamma(t)$ de
$[-\infty,+\infty]^n$ contenant $t$.
:::

::: {.section}
### Définition -- Subdivision pointée subordonnée à une jauge {#subdivision-pointée-subordonnée-à-une-jauge .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Subdivision pointée subordonnée à une jauge}`{=latex}

Une subdivision $\mathcal{D}$ du pavé fermé $I$ de $[-\infty,+\infty]^n$
est *subordonnée à une jauge* $\gamma$ sur $I$ si pour tout
$(t, J) \in \mathcal{D}$, $J \subset \gamma(t).$
:::

::: {.section}
### Définition -- Intégrale dans $\mathbb{R}^n$ {#intégrale-dans-mathbbrn .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Intégrale dans \(\mathbb{R}^n\)}`{=latex}

Une fonction $f:[-\infty,\infty]^n \to \mathbb{R}$ est dite *intégrable
au sens de Henstock-Kurzweil* s'il existe un réel $A$ tel que pour tout
$\varepsilon > 0$ il existe une jauge $\gamma$ de $[-\infty,+\infty]^n$
telle que pour toute subdivision pointée $\mathcal{D}$ de
$[-\infty,+\infty]^n$ subordonnée à $\gamma$, on ait
$|S(f, \mathcal{D}) - A| \leq \varepsilon$. Le réel $A$ quand il existe
est unique ; il est appelé *intégrale de Henstock-Kurzweil de $f$ sur
$\mathbb{R}^n$*.

La fonction $f$ est dite *intégrable (au sens de Lebesgue)* si $f$ et
$|f|$ sont intégrables au sens de Henstock-Kurzweil. L'intégrale (de
Lebesgue) de $f$ est alors définie comme l'intégrale de
Henstock-Kurzweil de $f$ et notée $$
\int f \; \mbox{ ou } \;
\int f(x) \, dx \; \mbox{ ou } \; \int f(x_1,\dots, x_n) \, dx_1\dots dx_n.
$$ Lorsque la fonction $f$ est définie sur
$A \subset [-\infty,\infty]^n$ on dira que $f$ est intégrable sur $A$ si
son prolongement $\bar{f}$ par zéro à $[-\infty, \infty]^n$ est
intégrable sur $[-\infty,\infty]^n$ ; s'il est nécessaire d'être
explicite quant au domaine d'intégration $A$, on utilisera les notations
$$
\int_A f := \int_A f(x) \, dx := \int \bar{f}(x) \, dx.
$$
:::

::: {.section}
### Propriétés élémentaires

Dans cette section, nous énonçons sans preuve dans le cadre
$\mathbb{R}^n$ les propriétés de l'intégrale déjà connues dans
$\mathbb{R}$.
:::

::: {.section}
### Théorème -- Linéarité {#linéarité .theorem .one .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Linéarité}`{=latex}

Si les fonctions $f: \mathbb{R}^n \to \mathbb{R}$ et
$g: \mathbb{R}^n \to \mathbb{R}$ sont intégrables et
$\alpha \in \mathbb{R}$, alors les fonctions $f+g$ et $\alpha f$ sont
intégrables. De plus, $$
\int f(x) + g(x) \, dx 
= 
\int f(x) \, dx +
\int  g(x) \, dx
\;
\mbox{ et }
\;
\int  \alpha f(x) \, dx
=
\alpha \int f(x) \, dx.
$$
:::

::: {.section}
#### Exercice -- Additivité I ($\mathord{\bullet}$) {#exo-additivité-I .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Additivité I}`{=latex}

Soit $f :\mathbb{R}^n \to \mathbb{R}$. Montrer que si $f$ est intégrable
sur $A \subset \mathbb{R}^n$ et sur $B \subset \mathbb{R}^n$ et que $A$
et $B$ sont d'intersection vide alors $f$ est intégrable sur $A\cup B$
et $$
\int_{A \cup B} f(x) \, dx = \int_A f(x) \, dx + \int_B f(x) \, dx.
$$

([Solution p.
`\pageref*{answer-exo-additivituxe9-I}`{=tex}](#answer-exo-additivité-I){.no-parenthesis}.)
:::

::: {.section}
### Proposition -- Croissance de l'intégrale {#croissance .proposition .one .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Croissance de l'intégrale}`{=latex}

Si les fonctions $f: \mathbb{R}^n \to \mathbb{R}$ et
$g: \mathbb{R}^n \to \mathbb{R}$ sont intégrables et que $f \leq g$,
alors $$
\int f(x) \, dx \leq \int g(x)\,dx.
$$
:::

::: {.section}
### Corollaire -- Inégalité triangulaire {#inégalité-triangulaire .corollary .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Inégalité triangulaire}`{=latex}

Si $f: \mathbb{R}^n \to \mathbb{R}$ est intégrable alors $|f|$ est
intégrable et $$
\left|\int f(x) \, dx \right| \leq \int |f(x)|\, dx.
$$
:::

::: {.section}
### Proposition -- Fonctions égales presque partout {#fepp .proposition .two .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Fonctions égales presque partout}`{=latex}

Une fonction $f:\mathbb{R}^n \to \mathbb{R}$ égale presque partout à une
fonction $g:\mathbb{R}^n \to \mathbb{R}$ intégrable est elle-même
intégrable et $$
\int f(x) \, dx = \int g(x) \, dx.
$$
:::

::: {.section}
### Proposition -- Fonctions égales presque partout (réciproque) {#fepp-réciproque .proposition .two .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Fonctions égales presque partout (réciproque)}`{=latex}

Si les fonctions $f:\mathbb{R}^n \to \mathbb{R}$ et
$g: \mathbb{R}^n \to \mathbb{R}$ sont intégrables et si $$
f \leq g \, \mbox{ presque partout} 
\; \mbox{ et } \;
\int f(x) \, dx \geq \int g(x) \, dx,
$$ alors $f = g$ presque partout.
:::

::: {.section}
Un théorème de changement de variables généralise le théorème déjà
énoncé pour une variable ; il est suffisamment complexe pour mériter [sa
propre section dans ce chapitre (p.
`\pageref*{changement-de-variables}`{=tex})](#changement-de-variables).
L'équivalent dans $\mathbb{R}^n$ du théorème fondamental du calcul est
le théorème de la divergence[^4] ; [l'annexe (p.
`\pageref*{annexe}`{=tex})](#annexe) lui est entièrement consacrée.
:::

::: {.section}
La notion d'ensemble mesurable est inchangée (modulo le remplacement des
intervalles fermés bornés de $\mathbb{R}$ par les pavés fermés bornés de
$\mathbb{R}^n$) ; les trois propriétés élémentaires de la collection des
ensembles mesurables de $\mathbb{R}^n$ sont toujours vérifiées (la
collection est une tribu), cette famille contient tous les fermés (et
tous les ouverts) et "négligeable" et "(mesurable et) de mesure
($n$-dimensionnelle) nulle" sont toujours synonymes.
:::

::: {.section}
### Définition -- Ensemble mesurable {#def-em .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Ensemble mesurable}`{=latex}

Un ensemble $E$ de $\mathbb{R}^n$ est *de mesure (de Lebesgue ou
$n$-dimensionnelle) finie* si sa fonction caractéristique $1_E$ est
intégrable sur $\mathbb{R}^n$ ; il est *mesurable* si sa fonction
caractéristique est intégrable sur tout pavé fermé borné de
$\mathbb{R}^n$. La *mesure (de Lebesgue ou $n$-dimensionnelle)*
$\lambda(E)$ d'un ensemble $E$ mesurable est définie par $$
\lambda(E) := \int 1_E(x) \, dx
$$ si $E$ est de mesure finie et $$
\lambda(E) := +\infty
$$ dans le cas contraire (si $E$ est mesurable mais pas de mesure
finie).
:::

::: {.section}
### Théorème -- Propriétés élémentaires (tribu) {#pptés-tribu .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Propriétés élémentaires (tribu)}`{=latex}

1.  L'ensemble vide est mesurable.

2.  Le complémentaire d'un ensemble mesurable est mesurable.

3.  L'union d'une collection dénombrable d'ensembles mesurables est
    mesurable.
:::

::: {.section}
### Théorème -- Topologie et ensembles mesurables {#OSM .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Topologie et ensembles mesurables}`{=latex}

Tout ensemble fermé (ou ouvert) est mesurable.
:::

::: {.section}
#### Exercice -- Disque fermé ($\mathord{\bullet}$) {#df .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Disque fermé}`{=latex}

Montrer que le disque
$D = \{(x_1,x_2) \in \mathbb{R}^2 \; | \; x_1^2 + x_2^2 \leq 1\}$ est
mesurable. ([Solution p.
`\pageref*{answer-df}`{=tex}](#answer-df){.no-parenthesis}.)
:::

::: {.section}
### Théorème -- Ensembles négligeables {#négligeable-longueur-nulle .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Ensembles négligeables}`{=latex}

Un ensemble est de mesure de Lebesgue nulle si et seulement s'il est
négligeable.
:::

::: {.section}
#### Exercice -- Additivité II ($\mathord{\bullet}\mathord{\bullet}$) {#exo-additivité-II .exercise .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Additivité II}`{=latex}

Soit $f :\mathbb{R}^n \to \mathbb{R}$. Montrer que si $f$ est intégrable
sur $A \subset \mathbb{R}^n$ et sur $B \subset \mathbb{R}^n$ et que $A$
et $B$ sont sans chevauchement ($A\cap B$ est négligeable) alors $f$ est
intégrable sur $A\cup B$ et $$
\int_{A \cup B} f(x) \, dx = \int_A f(x) \, dx + \int_B f(x) \, dx.
$$

([Solution p.
`\pageref*{answer-exo-additivituxe9-II}`{=tex}](#answer-exo-additivité-II){.no-parenthesis}.)
:::

::: {.section}
Les fonctions mesurables ont la même définition que dans $\mathbb{R}$ ;
le critère de mesurabilité par l'image réciproque est toujours valide.
:::

::: {.section}
### Définition -- Fonction mesurable {#fonction-mesurable .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Fonction mesurable}`{=latex}

Une fonction $f:\mathbb{R}^n \to \mathbb{R}$ est *mesurable* si elle est
la limite simple d'une suite de fonctions intégrables, c'est-à-dire s'il
existe une suite de fonctions intégrables
$f_k:\mathbb{R}^n \to \mathbb{R}$ telle que pour tout $x\in \mathbb{R}$,
$f_k(x) \to f(x)$ quand $k \to +\infty$. Une fonction
$f:\mathbb{R}^n \to \mathbb{R}^m$ est mesurable si chacune de ses
composantes est mesurable.
:::

::: {.section}
### Théorème -- Critère de l'image réciproque {#CIR .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Critère de l'image réciproque}`{=latex}

Une fonction $f:\mathbb{R}^n \to \mathbb{R}^m$ est mesurable si et
seulement l'image réciproque de tout fermé (ou de tout ouvert) de
$\mathbb{R}^m$ par $f$ est mesurable.
:::

::: {.section}
### Proposition -- Ensemble mesurable {#emfc .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Ensemble mesurable}`{=latex}

Un sous-ensemble $E$ de $\mathbb{R}^n$ est mesurable si et seulement si
sa fonction caractéristique $1_E$ est mesurable.

::: {.section}
Un cas particulier important sans équivalent dans $\mathbb{R}$ : les
produits d'ensembles mesurables sont mesurables.
:::
:::

::: {.section}
### Produit d'ensembles mesurables

Si les ensembles $A \subset \mathbb{R}^m$ et $B \subset \mathbb{R}^n$
sont mesurables, alors leur produit cartésien
$A \times B \subset \mathbb{R}^m \times \mathbb{R}^n$ est mesurable.

::: {.section}
#### Démonstration {#démonstration .proof}

Comme
$A \times B = (A \times \mathbb{R}^n) \cap (\mathbb{R}^m \times B)$ et
que [l'intersection de deux ensembles mesurables est mesurable (p.
`\pageref*{pptuxe9s-tribu}`{=tex})](#pptés-tribu), il suffit d'établir
que $A \times \mathbb{R}^n$ et $\mathbb{R}^m \times B$ sont mesurables.
Nous nous contenterons de prouver que $A \times \mathbb{R}^n$ est
mesurable, la preuve pour $\mathbb{R}^m \times B$ étant presque
identique.

Soient $P_1$ et $P_2$ deux pavés fermés arbitraires de $\mathbb{R}^m$ et
$\mathbb{R}^n$ respectivement ; nous allons établir que la fonction
$(x, y) \in P_1 \times P_2 \to 1_{A}(x)$ est intégrable. Cela montrera
que
$(x, y) \in \mathbb{R}^m \times \mathbb{R}^n \to 1_A(x) \times 1_{\mathbb{R}^n}(y)$
est mesurable [et donc que $A \times \mathbb{R}^n$ est mesurable (p.
`\pageref*{emfc}`{=tex})](#emfc).

Par construction, $A \cap P_1$ est de mesure finie [donc
$1_{A \cap P_1}$ est intégrable (p.
`\pageref*{def-em}`{=tex})](#def-em). Soit $\varepsilon > 0$ et
$\gamma_1$ une jauge sur $\mathbb{R}^m$ telle que pour toute subdivision
pointée $\mathcal{D}_1$ de $P_1$ subordonnée à $\gamma_1$ on ait $$
\left|S(1_{A}, \mathcal{D}_1) - \int_{P_1} 1_{A}(x) \, dx\right| \leq \varepsilon.
$$ Soit $\gamma$ la jauge sur $P_1 \times P_2$ définie par $$
\gamma(x, y) = \gamma_1(x) \times [-\infty,+\infty]^m.
$$ Soit $\mathcal{D}$ une subdivision pointée de $P_1 \times P_2$
subordonnée à $\gamma$. Soit $\mathcal{I}_2$ une collection de $p$ pavés
fermés sans chevauchement tels que si $I_1 \times I_2$ appartienne à
$\mathcal{D}$ alors $I_2$ est l'union d'un nombre fini d'éléments de
$\mathcal{I}_2$. En jouant sur le fait que les valeurs de
$(x, y) \mapsto 1_{A}(x)$ sont indépendantes de $y$ et en décomposant
les pavés de $\mathcal{D}_1$ selon leur seconde composante, on peut
trouver $p$ subdivisions pointées $\mathcal{D}_1^i$ de $P_1$ toutes
subordonnées à $\gamma_1$ et des réels positifs $\alpha_i$ tels que
$\sum_{i=1}^p \alpha_i = \lambda(P_2)$ et $$
S((x, y) \mapsto 1_{A}(x), \mathcal{D}) = \sum_{i=1}^p \alpha_i S(1_A, \mathcal{D}_1^i).
$$ Par conséquent, $$
\left|S((x, y) \mapsto 1_{A}(x), \mathcal{D}) - \lambda(P_2)\int_{P_1\times P_2} 1_{A}(x) \, dx \right| \leq \lambda(P_2) \varepsilon
$$ et $(x, y) \in P_1 \times P_2 \mapsto 1_{A}(x)$ est donc bien
intégrable.`\hfill$\blacksquare$`{=latex}
:::
:::

::: {.section}
Les théorèmes de convergence (dominée, monotone) et le critère
d'intégrabilité dominée se transposent à l'identique pour les fonctions
de plusieurs variables.
:::

::: {.section}
### Théorème -- Théorème de convergence dominée {#TCD .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Théorème de convergence dominée}`{=latex}

Si une suite de fonctions intégrables $f_k:\mathbb{R}^n \to \mathbb{R}$
converge simplement vers la fonction $f$, c'est-à-dire si pour tout
$x \in \mathbb{R}^n$, $$
\lim_{k \to +\infty} f_k(x) = f(x)
$$ et qu'il existe une fonction intégrable
$g:\mathbb{R}\to \left[0, +\infty\right[$ dominant la suite $f_k$,
c'est-à-dire telle que pour tout $k \in \mathbb{N}$ et pour tout
$x \in \mathbb{R}^n$, $$
|f_k(x)| \leq g(x)
$$ alors la fonction $f$ est intégrable et $$
\int f(x) \, dx 
=
\int \lim_{k \to +\infty} f_k(x) \, dx
= 
\lim_{k \to +\infty} \int f_k(x) \, dx.
$$
:::

::: {.section}
### Théorème -- Théorème de convergence monotone {#TCM .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Théorème de convergence monotone}`{=latex}

Si une suite de fonctions intégrables $f_k:\mathbb{R}^n \to \mathbb{R}$
est croissante et majorée en tout point, c'est-à-dire si pour tout $x$
de $\mathbb{R}^n$ $$
\mbox{pour tout } \, k \in \mathbb{N}, \, f_k(x) \leq f_{k+1}(x) 
\; \mbox{ et } \;
\sup_k f_k(x) < + \infty,
$$ alors la limite simple $f$ des $f_k$ est intégrable si et seulement
si $$
\sup_k \int f_k(x) \, dx < +\infty.
$$ et dans ce cas, $$
\int f(x) \, dx 
=
\int \lim_{k \to +\infty} f_k(x) \, dx
= 
\lim_{k \to +\infty} \int f(x) \, dx.
$$
:::

::: {.section}
### Théorème -- Critère d'intégrabilité dominée {#CID .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Critère d'intégrabilité dominée}`{=latex}

Une fonction $f: \mathbb{R}^n \to \mathbb{R}$ est intégrable si et
seulement si $f$ est mesurable et il existe une fonction intégrable
$g: \mathbb{R}\to \left[0,+\infty\right[$ telle que $|f| \leq g$.
:::
:::

::: {.section}
Intégrale multiple
==================

::: {.section}
### Théorème -- Théorème de Fubini {#Fubini .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Théorème de Fubini}`{=latex}

Soit $f: \mathbb{R}^m\times \mathbb{R}^n \to \mathbb{R}$ une fonction
intégrable. Alors la fonction partielle
$x \in \mathbb{R}^m \mapsto f(x, y)$ est intégrable pour presque tout
$y \in \mathbb{R}^n$, la fonction définie presque partout $$
y \in \mathbb{R}^n \mapsto \int_{\mathbb{R}^m} f(x, y) \, dx
$$ est intégrable et $$
\int_{\mathbb{R}^{m+n}} f(x, y) \, dxdy = \int_{\mathbb{R}^n} \left[ \int_{\mathbb{R}^m} f(x, y) \, dx\right] dy.
$$

![Graphe de la fonction
$f: (x, y) \in \mathbb{R}\times \mathbb{R}\mapsto e^{-x^2-y^2}$ en gris
et des fonctions partielles $x \in \mathbb{R}\mapsto f(x, y)$ pour
$y=-1.5, -1, -0.5$ en noir.](images/fubini.py.pdf)
:::

::: {.section}
### Remarque -- Ordre et nombre des variables {#Fubini-extension .remark .post .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Ordre et nombre des variables}`{=latex}

Deux extensions [du théorème de Fubini (p.
`\pageref*{Fubini}`{=tex})](#Fubini) souvent utiles :

-   Il est possible de changer l'ordre d'intégration des variables : si
    $f$ est intégrable, alors la fonction partielle
    $y \in \mathbb{R}^n \mapsto f(x, y)$ est intégrable pour presque
    tout $x \in \mathbb{R}^m$, la fonction définie presque partout $$
    x \in \mathbb{R}^m \mapsto \int_{\mathbb{R}^n} f(x, y) \, dy
    $$ est intégrable et $$
    \int_{\mathbb{R}^{m+n}} f(x, y) \, dxdy =
    \int_{\mathbb{R}^m} \left[ \int_{\mathbb{R}^n} f(x, y) \, dy\right] dx.
    $$

-   Il est possible de considérer des fonctions de trois variables ou
    plus. Par exemple, si la fonction
    $f : \mathbb{R}^m \times \mathbb{R}^n \times \mathbb{R}^p \to \mathbb{R}$
    est intégrable, alors $$
    \int_{\mathbb{R}^{m+n+p}} f(x, y, z) \, dxdydz =
    \int_{\mathbb{R}^p} \left[\int_{\mathbb{R}^n} \left[ \int_{\mathbb{R}^m} f(x, y, z) \, dx\right] dy \right] dz.
    $$ (étant entendu que tous les fonctions intermédiaires intervenant
    dans le membre de droite de cette équation sont bien définies
    presque partout).
:::

::: {.section}
#### Démonstration {#démonstration-1 .proof}

Se reporter à @Swa01.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Exercice -- Calcul de l'aire d'un triangle ($\mathord{\bullet}$) {#triangle .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Calcul de l'aire d'un triangle}`{=latex}

Considérons le triangle $$
T = \{(x, y) \in \mathbb{R}^2 \; | \; x \geq 0, \, y \geq 0 \mbox{ et } x + y \leq  1\}.
$$ En supposant l'intégrale ci-dessous bien définie, calculer : $$
a(T) = \int_{\mathbb{R}^2} 1_T(x, y) \, dxdy.
$$

([Solution p.
`\pageref*{answer-triangle}`{=tex}](#answer-triangle){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Contre-exemple ($\mathord{\bullet}\mathord{\bullet}$) {#fubini-counter-example .exercise .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Contre-exemple}`{=latex}

Comparer les valeurs des intégrales multiples $$
\int_0^1 \left[\int_0^1 \frac{x^2 - y^2}{(x^2+y^2)^2} \, dx \right] \, dy
\; \mbox{ et } \;
\int_0^1 \left[\int_0^1 \frac{x^2 - y^2}{(x^2+y^2)^2} \, dy \right] \, dx,
$$ puis expliquer le résultat. Indication : on remarquera que $$
\frac{x^2 - y^2}{(x^2+y^2)^2} = \frac{\partial}{\partial x} \left(-\frac{x}{x^2+y^2}\right) 
$$ ([Solution p.
`\pageref*{answer-fubini-counter-example}`{=tex}](#answer-fubini-counter-example){.no-parenthesis}.)
:::

::: {.section}
Pour pouvoir appliquer le théorème de Fubini, il faut savoir a priori
que la fonction est intégrable et pas seulement que ses intégrales
multiples sont bien définies (cf. ["Contre-exemple" ci-dessus (p.
`\pageref*{fubini-counter-example}`{=tex})](#fubini-counter-example)).
Si la fonction est à valeurs positives toutefois, l'examen de ses
intégrales multiples permet de s'assurer de l'intégrabilité ; c'est le
théorème de Tonelli :
:::

::: {.section}
### Théorème -- Théorème de Tonelli {#Tonelli .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Théorème de Tonelli}`{=latex}

Soit $f: \mathbb{R}^m\times \mathbb{R}^n \to \left[0, +\infty\right[$
une fonction mesurable. Alors, pour presque tout $y \in \mathbb{R}^n$,
la fonction $x \in \mathbb{R}^m \mapsto f(x, y)$ est mesurable. Si de
plus pour presque tout $y \in \mathbb{R}^n$ cette fonction est
intégrable, alors la fonction (définie presque partout) $$
g : y \in \mathbb{R}^n \mapsto \int_{\mathbb{R}^m} f(x, y) \, dx
$$ est mesurable. Si elle est intégrable, alors la fonction $f$ est
intégrable. Réciproquement, si $x \in \mathbb{R}^m \mapsto f(x, y)$
n'est pas intégrable presque partout ou que la fonction $g$ n'est pas
intégrable, alors $f$ n'est pas intégrable.
:::

::: {.section}
#### Démonstration {#démonstration-2 .proof}

Se reporter à @Swa01.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Remarque -- Fubini-Tonelli, mode d'emploi {#fubini-tonelli-mode-demploi .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Fubini-Tonelli, mode d'emploi}`{=latex}

Les deux théorèmes sont souvent utilisés ensemble pour intégrer une
fonction $f : \mathbb{R}^m \times \mathbb{R}^n \to \mathbb{R}$, de la
façon suivante :

1.  On vérifie tout d'abord que la fonction $f$ est mesurable. Comme sa
    valeur absolue $|f|$ est mesurable et positive, le théorème de
    Tonelli est alors *susceptible* de lui être appliqué.

2.  On étudie si $|f|$ satisfait bien [toutes les hypothèses du théorème
    de Tonelli (p. `\pageref*{Tonelli}`{=tex})](#Tonelli). Si c'est le
    cas, la fonction $|f|$ est intégrable ; la fonction $f$ étant
    mesurable, [par le critère d'intégrabilité dominée (p.
    `\pageref*{CID}`{=tex})](#CID), $f$ est donc intégrable.

3.  [Le théorème de Fubini (p. `\pageref*{Fubini}`{=tex})](#Fubini) est
    donc applicable ! On peut donc évaluer l'intégrale de $f$ en
    calculant son intégrale multiple.
:::

::: {.section}
#### Exercice -- Triangle d'aire finie ($\mathord{\bullet}$) {#triangle2 .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Triangle d'aire finie}`{=latex}

Montrer que le triangle $$
T = \{(x, y) \in \mathbb{R}^2 \; | \; x \geq 0, \, y \geq 0 \mbox{ et } x + y \leq  1\}
$$ est d'aire finie, c'est-à-dire que $1_T$ est intégrable. ([Solution
p.
`\pageref*{answer-triangle2}`{=tex}](#answer-triangle2){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Intégrabilité des pavés fermés bornés ($\mathord{\bullet}$) {#ipfb .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Intégrabilité des pavés fermés bornés}`{=latex}

Montrer que la fonction caractéristique $1_I$ du pavé
$I = [a_1,b_1] \times \dots \times [a_n,b_n]$ de $\mathbb{R}^n$ est
intégrable et que $$
\lambda(I) := \int 1_I(x) \, dx = (b_1 - a_1) \times \dots \times (b_n - a_n).
$$

([Solution p.
`\pageref*{answer-ipfb}`{=tex}](#answer-ipfb){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Tout droite du plan est négligeable ($\mathord{\bullet}\mathord{\bullet}$) {#dn .exercise .two .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Tout droite du plan est négligeable}`{=latex}

En utilisant les [théorèmes de Tonelli (p.
`\pageref*{Tonelli}`{=tex})](#Tonelli) [et Fubini (p.
`\pageref*{Fubini}`{=tex})](#Fubini), montrer que toute droite du plan
est négligeable. ([Solution p.
`\pageref*{answer-dn}`{=tex}](#answer-dn){.no-parenthesis}.)
:::
:::

::: {.section}
Changement de variables {#changement-de-variables}
=======================

::: {.section}
### Théorème -- Changement de variables {#theorem-changement-de-variables .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Changement de variables}`{=latex}

Soient $D_1$ et $D_2$ des ouverts de $\mathbb{R}^n$ et $h: D_1 \to D_2$
un $C^1$-difféomorphisme de $D_1$ sur $D_2$ : une fonction continûment
différentiable et bijective dont l'inverse $h^{-1}: D_2 \to D_1$ est
également continûment différentiable. La matrice jacobienne associée à
la différentielle de $h$ étant notée $J_h$, la fonction
$f: D_2 \to \mathbb{R}$ est intégrable si et seulement si la fonction
$(f \circ h) |\det J_h| : D_1 \to \mathbb{R}$ est intégrable et dans ce
cas, $$
\int_{D_2} f(y) \, dy = \int_{D_1} f(h(x)) |\det J_h(x)| \, dx.
$$

![Changement de variables](images/changement-de-variables.svg.pdf)
:::

::: {.section}
#### Démonstration {#démonstration-3 .proof}

Se reporter à [@Swa01, annexe 5].`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Exercice -- Homothétie ($\mathord{\bullet}$) {#h .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Homothétie}`{=latex}

Soit $f:\mathbb{R}^n \to \mathbb{R}$ une fonction intégrable. Montrer
que pour tout coefficient $\alpha > 0$, l'intégrale $$
\int_{\mathbb{R}^n} f(\alpha x) dx
$$ est bien définie et la calculer en fonction de l'intégrale de $f$ sur
$\mathbb{R}^n$. ([Solution p.
`\pageref*{answer-h}`{=tex}](#answer-h){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Volume et translation ($\mathord{\bullet}$) {#vr .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Volume et translation}`{=latex}

Montrer que si $A$ est mesurable et de volume fini dans $\mathbb{R}^3$
l'image de $A$ par une translation est également mesurable et de même
volume. ([Solution p.
`\pageref*{answer-vr}`{=tex}](#answer-vr){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Coordonnées polaires ($\mathord{\bullet}\mathord{\bullet}$) {#cp .exercise .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Coordonnées polaires}`{=latex}

Soit $$
C = \{(x, y) \in \mathbb{R}^2 \; | \; y \neq 0 \mbox{ ou } x > 0\}
\; \mbox{ et } \;
P = \{(r,\theta) \in \mathbb{R}^2 \; | \; r>0 \mbox{ et } -\pi < \theta < \pi\}.$$
On note $h$ la fonction de $P$ dans $C$ définie par
$h(r, \theta) = (r \cos \theta, r \sin \theta)$. Montrer que pour toute
fonction $f: C \to \mathbb{R}$ intégrable, si l'on pose
$g(r,\theta) = f(x, y)$ où $(x, y) = h(r,\theta)$, alors $$
\int_{C} f(x, y) \, d(x,y) = \int_{P} g(r,\theta)  r \, d(r, \theta).
$$

([Solution p.
`\pageref*{answer-cp}`{=tex}](#answer-cp){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Absence du déterminant jacobien ($\mathord{\bullet}\mathord{\bullet}$) {#adj .exercise .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Absence du déterminant jacobien}`{=latex}

Supposons $D_1$, $D_2$, $h$ et $f$ conformes aux hypothèses [du théorème
de changement de variables (p.
`\pageref*{theorem-changement-de-variables}`{=tex})](#theorem-changement-de-variables).
On suppose de plus que $f \circ h$ est intégrable sur $D_1$. Exprimer
l'intégrale $$
\int_{D_1} f (h(x)) \, dx
$$ comme une intégrale sur $D_2$. ([Solution p.
`\pageref*{answer-adj}`{=tex}](#answer-adj){.no-parenthesis}.)
:::
:::

::: {.section}
Annexe -- Théorème de la divergence {#annexe}
===================================

::: {.section}
### Définition -- Compact à bord régulier {#cbr .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Compact à bord régulier}`{=latex}

Un sous-ensemble $K$ de $\mathbb{R}^n$ est *un compact à bord $C^1$*
s'il est compact (fermé et borné) et peut être caractérisé au voisinage
de tout point de sa frontière $\partial K$, et après un éventuel
changement de repère, comme l'*hypographe* -- l'ensemble des points
en-dessous du graphe -- d'une fonction continûment différentiable.
Autrement dit, pour tout point $x_0 \in \partial K$, il existe une
application affine inversible $T: \mathbb{R}^n \to \mathbb{R}^n$ et un
voisinage ouvert $V$ de $x_0$ de la forme $V = T(U \times I)$, où $U$
est un ouvert de $\mathbb{R}^{n-1}$ et $I$ est un intervalle ouvert de
$\mathbb{R}$, et une fonction $f: U \to I$ continûment différentiable
tels que $$
K \cap V = T\left(\{(y_1,\dots, y_n) \in U \times I \; | \;  y_n \leq f(y_1, \dots, y_{n-1})\}\right).
$$
:::

::: {.section}
### Remarque -- Changement de repère orthonormé {#cbr-isom .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Changement de repère orthonormé}`{=latex}

Il est possible d'imposer dans [la définition des compacts à bord $C^1$
(p. `\pageref*{cbr}`{=tex})](#cbr) que $T$ soit une isométrie directe
(qui conserve la distance et l'orientation) ; cela revient à n'autoriser
que les changements de repère orthonormés directs. La caractérisation
des compacts à bord $C^1$ qui en résulte est inchangée.
:::

::: {.section}
### Théorème -- Caractérisation implicite des compacts à bord régulier {#cbr-implicit .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Caractérisation implicite des compacts à bord régulier}`{=latex}

Un sous-ensemble compact $K$ de $\mathbb{R}^n$ est un compact à bord
$C^1$ si pour tout point $x_0$ de sa frontière $\partial K$ il existe un
voisinage ouvert $V$ de $x_0$ et une fonction continûment différentiable
$g: V \to \mathbb{R}$ dont la différentielle est non nulle en $x_0$,
telle que pour tout point $x$ de $V$, $x$ appartient à $K$ si et
seulement si $g(x) \leq 0$.
:::

::: {.section}
#### Démonstration {#démonstration-4 .proof}

Si $K$ est un compact à bord $C^1$, il existe une application affine
inversible $T: \mathbb{R}^n \to \mathbb{R}^n$ et un voisinage ouvert $V$
de $x_0$ de la forme $V = T(U \times I)$, où $U$ est un ouvert de
$\mathbb{R}^{n-1}$ et $I$ est un intervalle ouvert de $\mathbb{R}$, et
une fonction $f: U \to I$ continûment différentiable tels que $$
K \cap V = T\left(\{(y_1,\dots, y_n) \in U \times I \; | \;  y_n \leq f(y_1, \dots, y_{n-1})\}\right).
$$ Par conséquent, si l'on définit la fonction $g: V \to \mathbb{R}$ par
$$
g(x) = y_n - f(y_1, \dots, y_{n-1}) \, \mbox{ où } \,
(y_1, \dots, y_n) = T^{-1}(x),
$$ on obtient la caractérisation implicite souhaitée. La seule
vérification qui n'est pas évidente par construction est le caractère
non-nul de la différentielle $dg$ en $x_0$. Si $T(x) = A \cdot x + b$ où
$A$ est une application linéaire (nécessairement inversible) et
$b \in \mathbb{R}^n$, en posant
$\phi(y) = y_n - f(y_1, \dots, y_{n-1})$, on obtient $$
dg(x) = d (\phi \circ T^{-1})(x) = d\phi(T^{-1}(x)) \cdot dT^{-1}(x) 
= d\phi(T^{-1}(x)) \cdot A^{-1}.
$$ Or, $\partial_n \phi(y) = 1$ en tout point $y$ de $U \times I$.
L'application $A^{-1}$ étant inversible, il existe un vecteur $h$ de
$\mathbb{R}^n$ tel que $A^{-1} \cdot h = (0, \dots, 0, 1)$ ; pour un tel
vecteur on a donc $$
dg(x) \cdot h = d\phi(T^{-1}(x)) \cdot A^{-1} \cdot h = 
\sum_{i=1}^n \partial_i \phi(T^{-1}(x)) (A^{-1} \cdot h)_i = 1.
$$ La différentielle de $g$ est donc bien non-nulle en tout point de $V$
(et donc a fortiori en $x_0$).

Réciproquement, considérons un $x_0 \in \partial K$ et supposons qu'il
existe une fonction $g: V \to \mathbb{R}$ satisfaisant les propriétés de
l'énoncé. La différentielle de $g$ étant non nulle en $x_0$, par
continuité de l'application $x \mapsto dg(x) \cdot u$ pour tout
$u \in \mathbb{R}^n$, il existe un vecteur de $u$ de $\mathbb{R}^n$ tel
que $$
dg(x) \cdot u > 0
$$ dans un voisinage $V'$ de $x_0$ contenu dans $V$. Soit $T$ une
application affine inversible de la forme $T(x) = A \cdot x + b$ telle
que $A \cdot e_n = u$. La fonction $g \circ T$ définie sur de
$T^{-1}(V')$ satisfait alors $$
\begin{split}
\partial_n (g \circ T)(y) &= dg(T(y)) \cdot dT(y) \cdot e_n \\
&= dg(T(y)) \cdot A \cdot e_n  \\
&= dg(T(y)) \cdot u > 0. \\
\end{split}
$$ L'application du théorème des fonctions implicites fournit un ouvert
non vide $U \times I$ inclus dans $T^{-1}(V')$ où
$U \subset \mathbb{R}^{n-1}$ et $I$ est un intervalle ouvert de
$\mathbb{R}$, ainsi qu'une fonction $f: U \to I$ continûment
différentiable telle que dans $U \times I$, $$
g \circ T(y_1,\dots,y_n) = 0 
\, \Leftrightarrow \, 
y_n = f(y_1,\dots, y_{n-1}).
$$ Par le théorème fondamental du calcul, $$
\begin{split}
g \circ T(y_1,\dots,y_n) &= 
g \circ T(y_1,\dots,f(y_1, \dots, y_{n-1})) \\
& \phantom{=}+
\int_{f(y_1, \dots, y_{n-1})}^{y_n}
\partial_n  (g\circ T)(y_1,\dots,y_{n-1}, t) \, dt \\
&=
\int_{f(y_1, \dots, y_{n-1})}^{y_n}
\partial_n  (g\circ T)(y_1,\dots,y_{n-1}, t) \, dt, \\
\end{split}
$$ ce qui garantit que dans $T(U \times I)$, $g(x) \leq 0$ --
c'est-à-dire $x \in K$ -- si et seulement si $x = T(y)$ et
$y_n \leq f(y_1, \dots, y_{n-1})$.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Définition -- Normale extérieure {#normale-extérieure .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Normale extérieure}`{=latex}

Une *normale* à un compact à bord $C^1$ $K$ de $\mathbb{R}^n$ en un
point $x \in \partial K$ de sa frontière est un vecteur
$n(x) \in \mathbb{R}^n$ unitaire (de norme $1$) tel que $$
\lim_{\substack{y \to x \\ y \in \partial K}} \left<n(x), \frac{y-x}{\|y-x\|}\right> = 0.
$$ Cette normale $n(x)$ est *extérieure* si pour $\varepsilon>0$ assez
petit, $x + \varepsilon n(x) \not \in K$.
:::

::: {.section}
On admettra l'unicité de la normale extérieure ainsi définie ; son
expression peut être calculée simplement dans le cas d'une
représentation implicite ou explicite (comme hypographe) du compact à
bord.
:::

::: {.section}
### Proposition -- Normale extérieure et caractérisation implicite {#neci .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Normale extérieure et caractérisation implicite}`{=latex}

Si $K$ est un compact à bord $C^1$ caractérisé au voisinage de
$x_0 \in \partial K$ par l'inégalité $g(x) \leq 0$, où $V$ est un
voisinage ouvert de $x$ et $g: V \to \mathbb{R}$ est continûment
différentiable de différentielle non nulle sur $V$, alors la *normale
extérieure* de $K$ en $x \in \partial K \cap V$ est le vecteur de
$\mathbb{R}^n$ donné par $$
n(x) = \frac{\nabla g(x)}{\|\nabla g(x)\|}.
$$
:::

::: {.section}
#### Démonstration {#démonstration-5 .proof}

La fonction $g$ étant différentiable en $x \in \partial K$, on a
localement $$
g(y) = g(x) + dg(x) \cdot (y - x) + o(\|y - x\|)
=\left<\nabla g(x), y-x \right> + o(\|y-x\|).
$$ Si $y \in \partial K$, $g(y) = 0$, donc $$
\left<\nabla g(x), \frac{y-x}{\|y-x\|} \right> = o(1)
\to 0 \, \mbox{ quand } \, y \to x.
$$ Si $y = x + \varepsilon \nabla g(x) /\|\nabla g(x)\|$, avec
$\varepsilon >0$, $$
g(y) = \left<\nabla g(x), y-x \right> + o(\|y-x\|)
= \varepsilon \|\nabla g(x)\| + o(\varepsilon),
$$ et donc $g(y) > 0$ -- soit $y \not \in K$ -- pour $\varepsilon$
suffisamment petit.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Proposition -- Normale extérieure et hypographe {#neh .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Normale extérieure et hypographe}`{=latex}

Si $K$ est un compact à bord $C^1$ caractérisé au voisinage de
$x_0 \in \partial K$ comme l'hypographe de la fonction $f: U \to I$ où
$U$ est un ouvert de $\mathbb{R}^{n-1}$ et $I$ un intervalle ouvert de
$\mathbb{R}$, alors la normale extérieure de $K$ en
$x \in \partial K \cap V$ est le vecteur de $\mathbb{R}^n$ donné par $$
n(x_1, \dots, x_n) = \frac{(-\partial_1 f(x_1,\dots, x_{n-1}), \dots, -\partial_{n-1} f(x_1,\dots, x_{n-1}),1)}{\sqrt{1 +\|\nabla f(x_1, \dots, x_{n-1})\|^2}}.
$$
:::

::: {.section}
#### Démonstration {#démonstration-6 .proof}

Il suffit de constater qu'on peut associer à l'hypographe de $f$ la
description implicite $g(x) \leq 0$ avec $$
g(x_1,\dots, x_{n-1}, x_n) = x_n - f(x_1, \dots, x_{n-1})
$$ puis d'exploiter [la caractérisation de la normale dans ce cas (p.
`\pageref*{neci}`{=tex})](#neci). Comme $$
\nabla g(x_1, \dots, x_n)
= (-\partial_1 f(x_1,\dots, x_{n-1}), \dots, -\partial_{n-1} f(x_1,\dots, x_{n-1}),1)
$$ et que par conséquent $$
\|\nabla g(x_1, \dots,  x_n)\| = \sqrt{1 +\|\nabla f(x_1, \dots, x_{n-1})\|^2},
$$ le résultat s'en déduit.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
Nous allons maintenant définir l'intégrale de surface d'une fonction
continue sur la frontière d'un compact à bord. Pour arriver à nos fins,
nous allons tout d'abord définir l'intégrale de surface pour des
fonctions continues nulles en dehors d'un voisinage -- arbitrairement
petit -- d'un point du compact. Le résultat suivant de partition de
l'unité nous permettra de "recoller" ces contributions à l'intégrale
globale.
:::

::: {.section}
### Définition -- Partition de l'unité {#pu .definition .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Partition de l'unité}`{=latex}

Pour toute famille finie d'ouverts $V_i$ de $\mathbb{R}^n$ recouvrant un
ensemble compact $K$, il existe une famille
$\rho_i: \mathbb{R}^n \to \left[0, +\infty\right[$ de fonctions
continûment différentiables dont le *support* $$
\mbox{supp}(\rho_i) 
=
\overline{\{x \in \mbox{dom}(\rho_i)\, | \, \rho_i(x) \neq 0\}}.
$$ est compact et inclus dans $V_i$ et telles que $$
\sum_{i} \rho_i(x) = 1 \mbox{ pour tout } x \in K.
$$
:::

::: {.section}
La démonstration est donnée [à la fin de cette annexe (p.
`\pageref*{proof-pu}`{=tex})](#proof-pu).
:::

::: {.section}
### Définition -- Intégrale de surface {#intégrale-de-surface .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Intégrale de surface}`{=latex}

Soit $\phi: \partial K \to \mathbb{R}^m$ une fonction continue. Si $K$
est caractérisé dans un voisinage ouvert $V$ de $x_0 \in \partial K$
comme l'hypographe de la fonction $f: U \to I$ après une transformation
$T$ qui soit une isométrie directe, la *contribution de
$V = T(U \times I)$ à l'intégrale de surface de $\phi$* est définie par
la relation $$
\int_{\partial K \cap V} \phi(x) \sigma(dx) 
:= 
\int_{U}
\phi(z, f(z)) \sqrt{1 + \|\nabla f(z)\|^2}\, dz. 
$$ Si les $V_i$ sont de tels ouverts consituant un recouvrement fini de
$\partial K$ et les $\rho_i$ [une partition de l'unité associée (p.
`\pageref*{lrl}`{=tex})](#lrl), alors *l'intégrale de surface de $\phi$
sur $\partial K$* est définie par $$
\int_{\partial K} \phi(x) \sigma(dx) 
:= \sum_i \int_{\partial K \cap V_i} \rho_i(x) \phi(x) \sigma(dx) 
$$
:::

::: {.section}
On admettra que cette définition est indépendante du choix de la
décomposition de $\partial K$.
:::

::: {.section}
### Définition -- Divergence {#divergence .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Divergence}`{=latex}

Soit $V$ un ouvert de $\mathbb{R}^n$. On appelle *divergence* d'une
fonction différentiable $$
v: V \to \mathbb{R}^n,
\;
v=(v_1, \dots, v_n)
$$ la fonction $\mbox{div} \, v: V \to \mathbb{R}$ définie par $$
\mbox{div} \, v(x) = \sum_{i=1}^n \partial_i v_i(x)
$$
:::

::: {.section}
### Lemme -- Lemme de la divergence {#div-lemma .lemma .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Lemme de la divergence}`{=latex}

Soit $f: U \to \mathbb{R}$ une fonction de classe $C^1$ où $U$ est un
pavé ouvert borné de $\mathbb{R}^{n-1}$. Soit
$v: U \times \mathbb{R} \to \mathbb{R}^n$ une fonction de classe $C^1$
de support compact dans $U \times \mathbb{R}^{n-1}$([^5]). L'ensemble
$\Omega$ désignant l'hypographe strict de $f$ -- soit
$\Omega = \{(y, z) \, | \, y \in U, \, z \in \mathbb{R}, \, z < f(y)\}$
-- et $\Gamma$ le graphe de $f$ -- soit
$\Gamma = \{(y, f(y)) \, | \, y \in U\}$ -- et $n$ la normale extérieure
associée, on a la relation $$
\int_{\Omega} \mbox{div} \, v(x) \, dx
=
\int_{\Gamma} \left<v(x), n(x) \right> \, \sigma(dx).
$$
:::

::: {.section}
#### Démonstration {#démonstration-7 .proof}

On remarque que si $v = w e_i$ où
$w: U \times \mathbb{R} \to \mathbb{R}$ est de classe $C^1$ et
$i \in \{1,\dots, n\}$, comme $\mbox{div}\, v = \partial_i w$ et
$\left<v(x), n(x) \right> = w(x) n_i(x)$, le résultat du lemme devient
$$
\int_{\Omega} \partial_i w(x) \, dx
=
\int_{\Gamma} w(x) n_i(x) \, \sigma(dx).
$$ Réciproquement, que si cette relation est valable pour tout
$i \in \{1,\dots, n\}$, la conclusion du lemme de Stokes s'en déduit
facilement. Démontrer la relation ci-dessus suffit donc à prouver le
lemme.

La transformation $h: U \times \left]-\infty, 0\right[ \to \mathbb{R}^n$
définie par $$
h(x_1, \dots, x_{n-1}, x_n) = (x_1, \dots, x_{n-1}, x_n + f(x_1, \dots, x_{n-1}))
$$ est une application de classe $C^1$. Par construction, $$
h(U \times \left]-\infty, 0\right[) = \Omega
$$ et admet une inverse, donnée par $$
h^{-1}(x_1, \dots, x_{n-1}, x_n) = (x_1, \dots, x_{n-1}, x_n - f(x_1, \dots, x_{n-1}))
$$ qui est également de classe $C^1$. La matrice jacobienne associée à
$h$ vaut $$
J_h(x)
=
\left[
\begin{array}{c|c}
I & 0 \\
\hline
J_f(x) & 1
\end{array}
\right]
$$ et par conséquent son déterminant jacobien satisfait $$
\mbox{det} \, J_h(x) = 1.
$$ Par conséquent, le changement de variable associé à $h$ fournit $$
\begin{split}
\int_{\Omega} \partial_i w(x) \, dx
&= \int_{h(U \times \left]-\infty, 0\right[)} \partial_i w(x) \, dx \\
&= \int_{U \times \left]-\infty, 0\right[} \partial_i w(h(x)) |\det J_h(x)| \, dx \\
&= \int_{U \times \left]-\infty, 0\right[} \partial_i w(x_1, \dots, x_{n-1}, x_n + f(x_1, \dots, x_{n-1})) 
\, dx
\end{split}
$$ ou encore, en notant $\pi(x) = (x_1,\dots, x_{n-1})$, $$
\int_{\Omega} \partial_i w(x) \, dx
=
\int_{U \times \left]-\infty, 0\right[} 
\partial_i w(\pi(x), x_n + f(\pi(x))) 
\, dx.
$$ Nous allons évaluer cette expression en comparant l'intégrande dans
le membre de droite de cette équation avec la dérivée partielle de
$w(\pi(x), x_n + f(\pi(x)))$ par rapport à $x_i$.

Si $i \in \{1,\dots, n-1\}$, la règle de dérivation en chaîne fournit $$
\begin{split}
\partial_i \left( w(\pi(x), x_n + f(\pi(x)) \right)
&= 
\partial_i w(\pi(x), x_n + f(\pi(x)) \\
&\phantom{=}
+ \partial_n w(\pi(x), x_n + f(\pi(x)) \times 
\partial_i f (\pi(x))
\end{split}
$$ et dans le cas contraire, $$
\partial_n \left( w(\pi(x), x_n + f(\pi(x)) \right)
= 
\partial_n w(\pi(x), x_n + f(\pi(x))).
$$

Si $U = I_1 \times \dots \times I_{n-1}$ et si pour
$i \in \{1,\dots, n-1\}$, on a $I_i = \left]a_i, b_i\right[$, alors par
le théorème fondamental du calcul, $$
\begin{split}
\int_{I_i} 
\partial_i (w(\pi(x), x_n + f(\pi(x))) 
\, dx_i
&=
\lim_{\varepsilon \to 0}
\int_{a_i+\varepsilon}^{b_i-\varepsilon}
\partial_i (w(\pi(x), x_n + f(\pi(x))) 
\, dx_i \\
&=
\lim_{\varepsilon \to 0}
\left[
w(\pi(x), x_n + f(\pi(x)))
\right]_{a_i + \varepsilon}^{b_i - \varepsilon}
\end{split}
$$ Comme $w$ est de support compact, pour toute valeur de $x_1$, $x_2$,
$\dots$, $x_{i-1}$, $x_{i+1}$, $\dots$, $x_n$, la fonction partielle $$
x_i \in \left]a_i, b_i \right[ \to w(\pi(x), x_n + f(\pi(x)))
$$ est également de support compact. Par conséquent, $$
S_i(x_1, \dots, x_{i-1}, x_{i+1}, \dots) :=
\int_{I_i} 
\partial_i (w(\pi(x), x_n + f(\pi(x)))) 
\, dx_i
=
0.
$$ Par le théorème de Fubini, on peut alors déduire que
`\begin{multline*}
\int_{U \times \left]-\infty, 0\right[} 
\partial_i (w(\pi(x), x_n + f(\pi(x)))) 
\, dx
=  \\
\int_{I_1\times\dots I_{i-1} \times I_{i+1} \times \dots \times \left]-\infty, 0\right[}
\!\!\!\!\!
S_i(x_1, \dots, x_{i-1}, x_{i+1}, \dots)  \, d(x_1,\dots,x_{i-1}, x_{i+1},\dots)
= 0.
\end{multline*}`{=tex} Si $i \in \{1,\dots, n-1\}$, on a donc $$
\int_{\Omega} 
\partial_i w(x) 
\, dx
= 
\int_{U \times \left]-\infty, 0\right[} 
\partial_n w(\pi(x), x_n + f(\pi(x)) \times 
(- \partial_i f (\pi(x))) \, dx
$$ et pour $i=n$, $$
\int_{\Omega} 
\partial_n w(x) 
\, dx
= 
\int_{U \times \left]-\infty, 0\right[} 
\partial_n w(\pi(x), x_n + f(\pi(x)) \, dx.
$$ Dans ce second cas, en raison de la compacité du support $w$, le
théorème fondamental du calcul fournit $$
\begin{split}
\int_{-\infty}^0 
\partial_n w(\pi(x), x_n + f(\pi(x)) \, dx_n
&= 
\lim_{z \to -\infty}\left[
x_n \mapsto 
w(\pi(x), x_n + f(\pi(x)))
\right]^0_{z} \\
&= 
w(\pi(x), f(\pi(x)),
\end{split}
$$ et donc par le théorème de Fubini, $$
\int_{\Omega} 
\partial_n w(x) 
\, dx
= 
\int_U w(y, f(y)) \, dy.
$$ Quand $i \in \{1, \dots, n-1\}$, un calcul analogue fournit $$
\int_{\Omega} 
\partial_n w(x) 
\, dx
= 
\int_U w(y, f(y)) \times (- \partial_i f(y)) \, dy.
$$

Quel que soit la valeur de $i \in \{1, \dots, n\}$, comme la normale
extérieure $n$ est donnée par $$
n(y, f(y)) = \frac{(-\partial_1 f(y), \dots, -\partial_{n-1} f(y), 1)}{\sqrt{1 +\|\nabla f(y)\|^2}}, 
$$ on constate que l'on a $$
\int_{\Omega} 
\partial_i w(x) 
\, dx
= 
\int_U w(y, f(y)) n_i(y, f(y)) \sqrt{1 +\|\nabla f(y)\|^2} \, dy,
$$ et par conséquent $$
\int_{\Omega} 
\partial_i w(x) 
\, dx
= 
\int_{\Gamma} w(x) n_i(x)\, d\sigma(x).
$$`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Théorème -- Théorème de la divergence {#div-theorem .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Théorème de la divergence}`{=latex}

Soit $U$ un ouvert de $\mathbb{R}^n$ et $K$ un ensemble compact $K$ à
bord $C^1$ inclus dans $U$. Pour toute fonction $v: U \to \mathbb{R}^n$
continûment différentiable, $$
\int_{K} \mbox{div} \, v(x) \, dx
=
\int_{\partial K} \left<v(x), n(x) \right> \, \sigma(dx).
$$ Pour toute fonction $f: U \to \mathbb{R}$ continûment différentiable
et tout $i \in \{1,\dots, n\}$, $$
\int_{K} \partial_i f(x) \, dx
=
\int_{\partial K} n_i(x) f(x) \, \sigma(dx).
$$
:::

::: {.section}
#### Démonstration {#démonstration-8 .proof}

Comme dans la démonstration du [lemme de la divergence (p.
`\pageref*{div-lemma}`{=tex})](#div-lemma), il suffit d'établir une
version du résultat, par exemple la première, et la seconde version s'en
déduit.

Pour tout $x \in \partial K$, il existe un pavé ouvert borné $U_x$ de
$\mathbb{R}^{n-1}$, un intervalle ouvert $I_x$ de $\mathbb{R}$, une
isométrie affine directe $T_x$ et une fonction continûment
différentiable $f_x:U_x \to I_x$ telle que $T_x(U_x \times I_x)$ soit un
voisinage de $x$ et $K \cap T_x(U_x \times I_x)$ soit l'image de
l'hypographe de $f_x$ par $T_x$. Si $x \in \mathring{K}$, il existe un
pavé ouvert borné $U_x$ de $\mathbb{R}^{n-1}$ et un intervalle ouvert
$I_x$ de $\mathbb{R}$ tels que $U_x \times I_x \subset \mathring{K}$ ;
on prendra ici $T_x=I$ (l'identité) et pour $f_x: U_x \to \mathbb{R}$
une fonction constante dont la valeur soit un majorant de $I_x$.

Par compacité, $K$ peut être recouvert par un nombre fini des ensembles
$V_x := T_x(U_x \times I_x)$, associés au points $x_1, \dots, x_k$. Soit
$\rho_j$, $j \in \{1,\dots, k\}$ une [partition de l'unité (p.
`\pageref*{pu}`{=tex})](#pu) associée. On a alors $$
\begin{split}
\int_{K} \mathrm{div}\, v(x) \, dx
&= \int_{K} \mathrm{div}\, \left({\textstyle \sum}_{j=1}^k  \rho_j(x) v(x) \right) \, dx \\
&= \sum_{j=1}^k \int_{K \cap V_{x_j}} \mathrm{div}\, (\rho_j(x) v(x)) \, dx.
\end{split}
$$ L'application du [lemme de la divergence (p.
`\pageref*{div-lemma}`{=tex})](#div-lemma) quand $x_j$ est un point
intérieur à $K$ fournit $$
\int_{K \cap V_{x_j}} \mathrm{div}\, (\rho_j(x) v(x)) \, dx = 0,
$$ car $v$ est nulle sur le graphe de $f_{x_j}$, et quand $x_j$ est un
point frontière $$
\begin{split}
\int_{K \cap V_{x_j}} \mathrm{div}\, (\rho_j(x) v(x)) \, dx &= 
\int_{\partial K \cap V_{x_j}}  \left<\rho_j(x) v(x), n(x)\right> \, d\sigma(x) \\
&=\int_{\partial K \cap V_{x_j}}  \rho_j(x) \left< v(x), n(x)\right> \, d\sigma(x).
\end{split}
$$ Par conséquent, $$
\begin{split}
\int_{K} \mathrm{div}\, v(x) \, dx
&= \sum_{j=1}^{k} \int_{\partial K \cap V_{x_j}}  \rho_j(x) \left< v(x), n(x)\right> \, d\sigma(x) \\
&= \int_{\partial K} \left< v(x), n(x)\right> \, d\sigma(x).
\end{split}
$$`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
La preuve de l'existence d'une partition de l'unité repose sur le lemme
suivant :
:::

::: {.section}
### Lemme -- Lemme de recouvrement de Lebesgue {#lrl .lemma .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Lemme de recouvrement de Lebesgue}`{=latex}

Soit $K$ un compact de $\mathbb{R}^n$ et une famille arbitraire
d'ouverts $V_i$ recouvrant $K$. Alors il existe un rayon $r>0$ tel que
pour tout $x \in K$, il existe un indice $i$ telle que la boule ouverte
$B(x, r)$ de rayon $r$ centrée en $x$ soit incluse dans $V_i$.
:::

::: {.section}
#### Démonstration {#démonstration-9 .proof}

Supposons au contraire que pour tout $r>0$ il existe un $x \in K$ tel
que pour tout indice $i$, la distance entre $x$ et le complémentaire de
$V_i$ soit (strictement) inférieure à $r$. Soit $x_k$ une suite de
points de $K$ tels que pour tout $i$,
$d(x_k, \mathbb{R}^n \setminus V_i) \leq 2^{-k}$ ; par compacité de $K$,
il existe une suite extraite des $x_k$ qui converge vers un
$\ell \in K$. En passant à la limite sur cette suite, on établit que
pour tout indice $i$ on a $d(\ell, \mathbb{R}^n \setminus V_i) = 0$,
soit $x \in \mathbb{R}^n \setminus V_i$ puisque
$\mathbb{R}^n \setminus V_i$ est fermé. Par conséquent, pour tout $i$,
$x \not \in V_i$, ce qui contredit l'hypothèse que les $V_i$ forment un
recouvrement de $K$.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Démonstration de l'existence d'une partition de l'unité {#proof-pu .proof}

Nous allons initialement établir l'existence d'une suite de fonctions
$\rho_i:\mathbb{R}^n \to \mathbb{R}$ continues, nulles en dehors de
$V_i$ dont la somme vaut $1$ sur un voisinage ouvert $V$ de $K$, puis
déduire de cette construction l'existence de fonctions continûment
différentiables $\rho'_i$ satisfaisant satisfaisant le théorème.

Notons $V=\cup_i V_i$ ; l'ensemble $V_i$ étant ouvert, la fonction
$x \in V \mapsto d(x, \mathbb{R}^n \setminus V_i)$, qui est continue,
est strictement positive sur $V_i$ et nulle ailleurs. La somme
$x \in \mathbb{R}^n \mapsto \sum_j d(x, \mathbb{R}^n \setminus V_j)$,
également continue, est donc strictement positive sur $V$. Les fonctions
$\rho_i$ définies par $$
\rho_i(x) = \frac{d(x, \mathbb{R}^n \setminus V_i)}{\sum_j d(x, \mathbb{R}^n \setminus V_j)}
$$ satisfont donc les propriétés requises pour l'étape 1.

[Le lemme de recouvrement de Lebesgue (p. `\pageref*{lrl}`{=tex})](#lrl)
établit l'existence d'un $r>0$ tel que pour tout $x \in K$, il existe au
moins un indice $i$ tel que $B(x, r) \subset V_i$. Notons $V'_i$ l'union
des boules ouverts $B(x,r)$ pour lequel l'incide $i$ convient quand $x$
décrit $K$. Par construction, les $V'_i$ sont ouverts et recouvrent
$K$ ; de plus, les adhérences $\overline{V'_i}$ sont bornées (ce sont
des sous-ensembles de $\{x \in K \, | \, d(x, K) \leq r\}$) et vérifient
$d(\overline{V'}_i, \mathbb{R}^n \setminus V_i) \geq r$.

Considérons les fonctions $\rho_i$ de l'étape initiale associées à la
famille des $V'_i$ et prolongées par $0$ en dehors de $\bigcup_i V'_i$.
Définissons alors les fonctions
$\rho'_i:\mathbb{R}^n \to \left[0, +\infty \right[$ par $$
\rho'_i(x) = \int_{\mathbb{R}^n} \rho_i(y) \phi(x-y) \, dy
$$ où $\phi:\mathbb{R}^n \to \left[0, +\infty\right[$ est une fonction
continûment différentiable, de support inclus dans
$\overline{B}(0, r/2)$ et telle que $$
\int_{\mathbb{R}^n} \phi(x) \, dx = 1.
$$ Le théorème de dérivation sous le signe somme établit que les
$\rho'_i$ sont continûment différentiables. Par construction, le support
de $\rho'_i$ est inclus dans $V'_i + \overline{B}(x, r/2)$, ce qui
garantit que $\mathrm{supp}(\rho'_i) \subset V_i$. Finalement, pour tout
$x \in K$, $$
\begin{split}
\sum_{i} \rho'_i(x) &= 
\sum_i \int_{\mathbb{R}^n} \rho_i(y) \phi(x-y) \, dy \\
&= 
\int_{\mathbb{R}^n} \sum_i \rho_i(y) \phi(x-y) \, dy \\
&= 
\int_{\mathbb{R}^n} \phi(x-y) \, dy \\ &= 1. \\
\end{split}
$$`\hfill$\blacksquare$`{=latex}
:::
:::

::: {.section}
Exercices complémentaires
=========================

::: {.section}
Aire du disque unité {#adu}
--------------------

Soit $D = \overline{B}(0,1)$ le disque unité fermé de $\mathbb{R}^2$.

::: {.section}
#### Question 1 ($\mathord{\bullet}$) {#adu-1 .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Montrer que $1_D$ est intégrable. ([Solution p.
`\pageref*{answer-adu-1}`{=tex}](#answer-adu-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 ($\mathord{\bullet}\mathord{\bullet}$) {#adu-2 .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Calculer l'aire de $D$ en utilisant le théorème de Fubini puis un
changement de variable dans $\mathbb{R}$. ([Solution p.
`\pageref*{answer-adu-2}`{=tex}](#answer-adu-2){.no-parenthesis}.)
:::

::: {.section}
#### Question 3 ($\mathord{\bullet}\mathord{\bullet}$) {#adu-3 .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Calculer l'aire de $D$ en utilisant un changement de variables dans
$\mathbb{R}^2$. ([Solution p.
`\pageref*{answer-adu-3}`{=tex}](#answer-adu-3){.no-parenthesis}.)
:::
:::

::: {.section}
Intégrabilité des fonctions puissances
--------------------------------------

Soit $C$ la couronne $\{x \in \mathbb{R}^2 \; | \; \|x\| > 1\}$ ; on
souhaite prouver dans cet exercice que l'intégrale $$
I = \int_C \frac{dx}{\|x\|^{\alpha}}
$$ est bien définie si et seulement si $\alpha > 2$.

::: {.section}
#### Question 1 ($\mathord{\bullet}$) {#ifp-1 .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Soit
$C_{++} = C \cap \{(x_1,x_2) \in \mathbb{R}^2 \; | \; x_1 > 0 \mbox{ et } x_2 > 0\}$.
Montrer que $x \mapsto \|x\|^{-\alpha}$ est intégrable sur $C$ si et
seulement si elle est intégrable sur $C_{++}$. ([Solution p.
`\pageref*{answer-ifp-1}`{=tex}](#answer-ifp-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 ($\mathord{\bullet}$) {#ifp-2 .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Déterminer l'image de $C_{++}$ par la fonction $$
h: (x_1, x_2) \mapsto (x_1, r) \; \mbox{ où } r = \|(x_1,x_2)\|
$$ et montrer que $h$ est un $C^1$-difféomorphisme de $C_{++}$ sur cette
image. ([Solution p.
`\pageref*{answer-ifp-2}`{=tex}](#answer-ifp-2){.no-parenthesis}.)
:::

::: {.section}
#### Question 3 ($\mathord{\bullet}\mathord{\bullet}$) {#ifp-3 .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Déterminer (formellement) l'expression de l'intégrale $I$ au moyen des
variables $(x_1, r)$, puis $(y, r)$ où $y = x_1/r$. En déduire que $I$
est bien définie si et seulement si $\alpha > 2$. ([Solution p.
`\pageref*{answer-ifp-3}`{=tex}](#answer-ifp-3){.no-parenthesis}.)
:::
:::

::: {.section}
Déformations d'un compact à bord régulier
-----------------------------------------

Soit $K$ un compact à bord $C^1$ de $\mathbb{R}^n$ et
$T:\mathbb{R}^n \to \mathbb{R}^n$ une application continûment
différentiable telle que $T = I + H$, où l'application continûment
différentiable $H:\mathbb{R}^n \to \mathbb{R}^n$ satisfait
$\sup_{x \in \mathbb{R}^n} \|dH(x)\| < 1$.

::: {.section}
#### Question 1 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#dcbr .question .four .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Montrer que l'ensemble $$
T(K) = \{x + T(x) \, | \, x \in K\}
$$ est un compact à bord $C^1$ de $\mathbb{R}^n$. ([Solution p.
`\pageref*{answer-dcbr}`{=tex}](#answer-dcbr){.no-parenthesis}.)
:::
:::

::: {.section}
Ovales de Cassini
-----------------

Soit $a$ et $b$ deux nombres réels strictements positifs. On désigne par
$K$ l'ensemble du plan délimité par les *ovales de Cassini* $$
K = \{(x,y) \in \mathbb{R}^2 \, | \, (x^2+y^2)^2 - 2a^2 (x^2 - y^2) + a^4 \leq b^4\}.
$$

::: {.section}
#### Question 1 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#oc .question .four .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Montrer que si $a \neq b$, l'ensemble $K$ est un compact à bord $C^1$.

![Compact à bord $C^1$ délimité par les ovales de
Cassini.](images/cassini-ovals.py.pdf)

![Ensemble délimité par les ovales de Cassini quand
$a=b=1$.](images/cassini-ovals-limite.py.pdf)

([Solution p.
`\pageref*{answer-oc}`{=tex}](#answer-oc){.no-parenthesis}.)
:::
:::

::: {.section}
Intégrales de surface
---------------------

Soit $B = \overline{B}(0,1)$ le disque unité fermé de $\mathbb{R}^2$.

::: {.section}
#### Question 1 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#is .question .four .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Calculer $$
\int_{\partial B} \sigma(dx)
\; \mbox{ et } \;
\int_{\partial B} x_1^2 \, \sigma(dx).
$$

([Solution p.
`\pageref*{answer-is}`{=tex}](#answer-is){.no-parenthesis}.)
:::
:::

::: {.section}
Rétraction
----------

Soit $B = \overline{B}(0,1)$ le disque unité fermé de $\mathbb{R}^2$ et
$f: B \to B$ une fonction de classe $C^2$ (c'est-à-dire admettant un
prolongement de classe $C^2$ sur un ouvert $U$ contenant $B$). Une telle
fonction $f$ est une *rétraction* de $B$ sur $\partial B$ si
$f(B) = \partial B$ et pour tout $x\in \partial B$, $f(x) = x$.

::: {.section}
#### Question 1 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#pfb-1 .question .four .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Montrer que pour une telle rétraction $f$, on a $$
\int_B \det J_f(x) \, dx = 0.
$$

([Solution p.
`\pageref*{answer-pfb-1}`{=tex}](#answer-pfb-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#pfb-2 .question .four .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

En déduire l'impossibilité d'une telle rétraction. ([Solution p.
`\pageref*{answer-pfb-2}`{=tex}](#answer-pfb-2){.no-parenthesis}.)
:::
:::

::: {.section}
Intégration par parties
-----------------------

::: {.section}
#### Question 1 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#IPP-n .question .four .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Si l'équivalent dans $\mathbb{R}^n$ du théorème fondamental du calcul
est le théorème de la divergence, quel résultat est l'équivalent dans
$\mathbb{R}^n$ de l'intégration par parties ? ([Solution p.
`\pageref*{answer-IPP-n}`{=tex}](#answer-IPP-n){.no-parenthesis}.)
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
#### Prolongements {#answer-p .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Prolongements}`{=latex}

Si l'on s'en tient sans réfléchir [à la section "Domaine des variables"
(p. `\pageref*{dv}`{=tex})](#dv), il faut associer à la première
fonction la fonction $$
(x,y) \in [-\infty,\infty]^2 \mapsto \left|
\begin{array}{rl}
\exp(-x^2-y^2) & \mbox{si $x\in\mathbb{R}$ et $y \in\mathbb{R}$,} \\
0 & \mbox{sinon.}
\end{array}
\right.
$$ à la seconde la fonction $$
(x,y) \in [-\infty,\infty]^2 \mapsto \left|
\begin{array}{rl}
\arctan(x^2 + y^2) & \mbox{si $x\in\mathbb{R}$ et $y \in\mathbb{R}$,} \\
0 & \mbox{sinon.}
\end{array}
\right.
$$ et à la troisième la fonction $$
(x,y) \in [-\infty,\infty]^2 \mapsto \left|
\begin{array}{rl}
\arctan(x^2y^2) & \mbox{si $x\in[-1,1]$ et $y \in[-1, 1]$,} \\
0 & \mbox{sinon.}
\end{array}
\right.
$$ Dans le second cas, la note de bas de page nous autorise aussi à
considérer la fonction $$
(x,y) \in [-\infty,\infty]^2 \mapsto \left|
\begin{array}{rl}
\arctan(x^2 + y^2) & \mbox{si $x\in\mathbb{R}$ et $y \in\mathbb{R}$,} \\
\pi/2 & \mbox{sinon.}
\end{array}
\right.
$$ qui peut sembler un choix plus naturel car le prolongement ainsi
construit est continu. Par contre, dans le troisième cas, c'est bien par
zéro que nous avons l'obligation d'étendre la fonction initiale
(techniquement, car l'ensemble $[-\infty,\infty]^2\setminus [-1, 1]^2$
n'est pas négligeable.)
:::

::: {.section}
#### Partition en pavés {#answer-pp .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Partition en pavés}`{=latex}

L'ensemble $\mathbb{R}^2 \setminus [-1, 1]$ est l'union des quatres
ensembles disjoints non vides suivants :
$\left]-\infty, -1\right[ \times \mathbb{R}$,
$[-1, 1] \times \left]1, +\infty\right[$,
$[-1, 1] \times \left]-\infty, -1\right[$ et
$\left]1, +\infty\right[ \times \mathbb{R}$.
:::

::: {.section}
#### Volume de pavés {#answer-exo-volume-pavé .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Volume de pavés}`{=latex}

On a $a(\{(0,0)\}) = a([0,0]^2) = 0 \times 0 = 0$,
$a([-1,1]^2) = 2 \times 2 = 4$,
$a([-1, 1] \times [0, +\infty]) = 2 \times (+\infty) = +\infty$ et
$a(\{0\} \times \mathbb{R}) = 0 \times (+\infty) = 0$.
:::

::: {.section}
#### Domaine à l'infini {#answer-dai .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Domaine à l'infini}`{=latex}

L'ensemble $[-\infty,+\infty]^n \setminus \mathbb{R}^n$ est recouvert
par les quatres pavés $\{-\infty\} \times [-\infty, \infty]$,
$\{+\infty\} \times [-\infty, +\infty]$,
$[-\infty, +\infty] \times \{-\infty\}$ et
$[-\infty, +\infty] \times \{+\infty\}$. Chacun de ces pavés est d'aire
nulle : on a par exemple $$
a(\{-\infty\} \times [-\infty, +\infty]) = \ell(\{-\infty\}) \times \ell([-\infty, +\infty]) = 0 \times (+\infty) = 0.
$$ Par conséquent l'ensemble considéré est négligeable.
:::

::: {.section}
#### Graphe du sinus {#answer-gs .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Graphe du sinus}`{=latex}

Notons $G = \{(x, \sin x) \; | \; x \in [0, 2\pi]\}$. Comme
$(\sin)' = \cos$ et que le cosinus est majoré par $1$, par le théorème
des accroissements finis, pour tout $x, y \in [0, 2\pi]$ on a
$|\sin x - \sin y| \leq |x - y|$. Par conséquent, pour tout
$x \in [0, 2\pi]$ et $h>0$, $$
G \cap ([x-h, x+h] \times [-\infty, +\infty]) \subset [x-h, x+h] \times [(\sin x) - h, (\sin x) + h].
$$ En choisissant $h = \pi / n$ et $x= \pi/n, 3 \pi/n, 5 \pi /n, \dots$,
on recouvre donc $G$ par la collection de pavés $$
I_k = \left[k\frac{2\pi}{n}, (k+1)\frac{2\pi}{n} \right] \times 
\left[y_k - \frac{\pi}{n}, 
y_k+\frac{\pi}{n} \right], \; k \in \{0, 1,\dots, n-1\}
$$ où $$
y_k = \sin \left(\left(k+\frac{1}{2} \right) \frac{2\pi}{n} \right).
$$

![Graphe de la fonction $\sin$ et recouvrement par les pavés $I_k$
($n=12$).](images/sin-cover.py.pdf)

La somme des aires des pavés $I_k$ satisfait $$
\sum_{k=0}^{n-1} a(I_k) = n \times \frac{2\pi}{n} \times \frac{2\pi}{n} = 
\frac{4 \pi^2}{n}.
$$ Il est donc possible de rendre cette somme arbitrairement faible en
sélectionnant un $n$ suffisamment grand. L'ensemble $G$ est donc
négligeable.
:::

::: {.section}
#### Additivité I {#answer-exo-additivité-I .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Additivité I}`{=latex}

Si $f$ est intégrable sur $A \subset \mathbb{R}^n$ et sur
$B \subset \mathbb{R}^n$ alors les prolongements de $f|_A$ et de $f|_B$
par zéro à $\mathbb{R}^n$, qui sont les fonctions $1_A f$ et $1_B f$,
sont intégrables sur $\mathbb{R}^n$. On a également $$
\int_A f(x) \, dx = \int_{\mathbb{R}^n} 1_A(x) f(x) \, dx
\; \mbox{ et } \; 
\int_B f(x) \, dx = \int_{\mathbb{R}^n} 1_B(x) f(x) \, dx.
$$ Si $A$ et $B$ sont d'intersection vide, on a
$1_{A \cup B} = 1_A + 1_B$, donc [par linéarité de l'intégrale (p.
`\pageref*{linuxe9arituxe9}`{=tex})](#linéarité),
$1_{A \cup B} f = 1_A f + 1_B f$ est intégrable, la fonction $f$ est
intégrable sur $A \cup B$ et `\begin{align*}
\int_{A \cup B} f(x) \, dx &= \int_{\mathbb{R}^n} 1_{A \cup B} (x) f(x) \, dx \\
&= \int_{\mathbb{R}^n} 1_A(x) f(x) + 1_B(x) f(x) \, dx \\
&= \int_A f(x) \, dx + \int_B f(x) \, dx.
\end{align*}`{=tex}
:::

::: {.section}
#### Disque fermé {#answer-df .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Disque fermé}`{=latex}

L'ensemble $D$ est fermé (c'est par exemple l'image réciproque du fermé
$[0, 1]$ par l'application continue $(x_1, x_2) \mapsto x_1^2 + x_2^2$),
[par conséquent il est mesurable (p. `\pageref*{OSM}`{=tex})](#OSM).
:::

::: {.section}
#### Additivité II {#answer-exo-additivité-II .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Additivité II}`{=latex}

La trame de la démonstration est similaire [à l'exercice "Additivité I"
(p. `\pageref*{exo-additivituxe9-I}`{=tex})](#exo-additivité-I). On
constate ici que $1_{A \cup B} = 1_A + 1_B - 1_{A \cap B}$ ; comme
$A \cap B$ est négligeable, la fonction $1_{A \cap B} f$ est nulle
presque partout, donc intégrable et d'intégrale nulle. La fonction
$1_{A \cup B}$ est donc intégrable [par linéarité de l'intégrale (p.
`\pageref*{linuxe9arituxe9}`{=tex})](#linéarité) et `\begin{align*}
\int_{A \cup B} f(x) \, dx &= \int_{\mathbb{R}^n} 1_{A \cup B} (x) f(x) \, dx \\
&= \int_{\mathbb{R}^n} 1_A(x) f(x) + 1_B(x) f(x) - 1_{A\cap B} f(x) \, dx \\
&= \int_{\mathbb{R}^n} 1_A(x) f(x) + \int_{\mathbb{R}^n} 1_B(x) f(x) - \int_{\mathbb{R}^n} 1_{A\cap B} f(x) \, dx \\
&= \int_A f(x) \, dx + \int_B f(x) \, dx.
\end{align*}`{=tex}
:::

::: {.section}
#### Calcul de l'aire d'un triangle {#answer-triangle .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Calcul de l'aire d'un triangle}`{=latex}

Si la fonction $1_D$ est intégrable, alors [le théorème de Fubini est
applicable (p. `\pageref*{Fubini}`{=tex})](#Fubini). On a donc $$
a(T) = \int_{\mathbb{R}}\left[ \int_{\mathbb{R}} 1_T(x, y) \, dx \right] \, dy.
$$ Or, si $0 \leq y \leq 1$, $$
1_T(x, y) = \left| 
\begin{array}{rl}
1 & \mbox{si $0 \leq x \leq 1-y$,} \\
0 & \mbox{sinon.}
\end{array}
\right.
$$ et dans le cas contraire, $1_T(x, y) = 0$. On a donc $$
a(T) = \int_0^1\left[ \int_0^{1-y} dx \right] \, dy
=\int_0^1 (1 - y) \, dy= \left[y - \frac{y^2}{2} \right]_0^1 = \frac{1}{2}.
$$
:::

::: {.section}
#### Contre-exemple {#answer-fubini-counter-example .answer .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Contre-exemple}`{=latex}

Pour tout $y \in \left]0,1\right]$ (et donc presque tout
$y \in [0, 1]$), on a $$
\int_0^1 \frac{x^2 - y^2}{(x^2+y^2)^2} \, dx 
= 
\left[x \mapsto - \frac{x}{x^2+y^2} \right]_0^1
= 
- \frac{1}{1+y^2},
$$ par conséquent $$
\int_0^1 \left[ \int_0^1 \frac{x^2 - y^2}{(x^2+y^2)^2} \, dx \right] \, dy
= - \int_0^1 \frac{dy}{1+y^2} \\
= - [y \mapsto \arctan y]_0^1
= - \frac{\pi}{4}.
$$ En exploitant la relation $$
\frac{x^2 - y^2}{(x^2+y^2)^2} = \frac{\partial}{\partial y} \left(\frac{y}{x^2+y^2}\right) 
$$ on établit de façon similaire que $$
\int_0^1 \left[ \int_0^1 \frac{x^2 - y^2}{(x^2+y^2)^2} \, dy \right] \, dx
= \frac{\pi}{4}.
$$

Or, si [le théorème de Fubini (p. `\pageref*{Fubini}`{=tex})](#Fubini)
était applicable, [on pourrait intervertir l'ordre d'intégration des
variables sans changer le résultat (p.
`\pageref*{Fubini-extension}`{=tex})](#Fubini-extension). Comme cela
n'est pas le cas, on en déduit que l'hypothèse exigée par le théorème de
Fubini ne tient pas : la fonction $$
(x, y) \in [0,1] \times [0,1] \mapsto \frac{x^2 - y^2}{(x^2+y^2)^2}
$$ n'est pas intégrable.
:::

::: {.section}
#### Triangle d'aire finie {#answer-triangle2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Triangle d'aire finie}`{=latex}

La fonction $1_T : \mathbb{R}^2 \to \mathbb{R}$ est positive et
mesurable, car l'ensemble $T$ est fermé donc mesurable. Par conséquent
on peut essayer d'appliquer [le théorème de Tonelli (p.
`\pageref*{Tonelli}`{=tex})](#Tonelli) qui donnerait la conclusion
voulue. Les calculs à effectuer pour vérifier que ses hypothèses sont
vérifiées sont exactement les mêmes que ceux nécessaires au calcul de
l'aire dans l'exercice ["Calcul de l'aire d'un triangle" (p.
`\pageref*{triangle2}`{=tex})](#triangle2) : ils montrent que pour tout
$y$, $x \mapsto 1_T(x, y)$ est intégrable, puis que $$
y \mapsto \int 1_T(x, y) \, dy
$$ est intégrable, ce qui nous permet de conclure.
:::

::: {.section}
#### Intégrabilité des pavés fermés bornés {#answer-ipfb .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Intégrabilité des pavés fermés bornés}`{=latex}

On procède par récurrence sur la dimension $n$ de l'espace. Admettons le
résultat prouvé au rang $n-1$. La fonction caractéristique $1_I$ de
$I = [a_1,b_1] \times \dots \times [a_n,b_n]$ est mesurable ; en effet,
pour tout ensemble ouvert de $\mathbb{R}$, l'image réciproque de cet
ensemble par $1_I$ est $\varnothing$, $I$, $\mathbb{R}^2 \setminus I$ ou
$\mathbb{R}^2$ et tous ces ensembles sont mesurables ([car fermé ou
ouverts (p. `\pageref*{OSM}`{=tex})](#OSM)). Fixons
$(x_2,\dots,x_n) \in \mathbb{R}^{n-1}$ ; la fonction
$x_1 \in \mathbb{R}\mapsto f(x_1,x_2,\dots, x_n)$ est intégrable : en
effet si $(x_2,\dots, x_n) \in [a_2,b_2] \times \dots \times [a_n,b_n]$
on a $$
1_I(x_1,x_2,\dots, x_n) = \left| 
\begin{array}{rl}
1 & \mbox{si $a_1 \leq x_1 \leq b_1$,} \\
0 & \mbox{sinon.}
\end{array}
\right.
$$ et $1_I(x_1,x_2,\dots, x_n) = 0$ sinon. On a donc $$
\int 1_I(x_1,x_2,\dots, x_n) \, dx_1 = (b_1-a_1) 1_{[a_2,b_2] \times \dots \times [a_n,b_n]}(x_2,\dots,x_n).
$$ Par l'hypothèse de récurrence,
$1_{[a_2,b_2] \times \dots \times [a_n,b_n]}$ est intégrable d'intégrale
$(b_2 - a_2) \times \dots \times (b_n - a_n)$, donc par [le théorème de
Tonelli (p. `\pageref*{Tonelli}`{=tex})](#Tonelli), $1_I$ est intégrable
et `\begin{align*}
\int 1_I(x) \, dx &= (b_1-a_1) \int 1_{[a_2,b_2] \times \dots \times [a_n,b_n]}(x_2,\dots,x_n) \, d(x_2,\dots x_n) \\
&= (b_1 - a_1) \times \dots \times (b_n - a_n).
\end{align*}`{=tex}
:::

::: {.section}
#### Tout droite du plan est négligeable {#answer-dn .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Tout droite du plan est négligeable}`{=latex}

Deux cas se présentent : soit la droite considérée est de la forme
$D = \{(x, y) \in \mathbb{R}^2 \; | \; y = a x + b\}$, soit elle est de
la forme $D = \{(x, y) \in \mathbb{R}^2 \; | \; x = c\}$. Dans les deux
cas, [la droite est un ensemble fermé de $\mathbb{R}^2$, donc mesurable
(p. `\pageref*{OSM}`{=tex})](#OSM) ; par [le critère de l'image
réciproque (p. `\pageref*{CIR}`{=tex})](#CIR), la fonction
caractéristique associée $1_D$ est donc mesurable. Dans le premier cas
considéré, pour tout $x \in \mathbb{R}$, la fonction
$y \mapsto 1_D(x, y)$ est nulle, sauf en $y = ax+b$ ; elle est donc
nulle presque partout et donc intégrable et d'intégrale nulle. On a donc
pour tout $x \in \mathbb{R}$, $$
\int 1_D(x, y) \, dy = 0
$$ et par conséquent la fonction $$
x \in \mathbb{R}\mapsto  \int 1_D(x, y) \, dy
$$ est donc intégrable. [Par le théorème de Tonelli (p.
`\pageref*{Tonelli}`{=tex})](#Tonelli), la fonction $f$ est donc
intégrable et [par le théorème de Fubini (p.
`\pageref*{Fubini}`{=tex})](#Fubini), on a $$
a(D) = \int_{\mathbb{R}^2} 1_D(x, y) d(x, y) = \int_{\mathbb{R}}\left[\int_{\mathbb{R}} 1_D(x,y) \, dy \right] \, dx = 0.
$$ La droite $D$ est donc [négligeable car mesurable et d'aire nulle (p.
`\pageref*{nuxe9gligeable-longueur-nulle}`{=tex})](#négligeable-longueur-nulle).

Le cas où $D = \{(x, y) \in \mathbb{R}^2 \; | \; x = c\}$ se traite de
façon similaire. On constate alors pour tout $x \in \mathbb{R}$, à
l'exception de $x=c$, la fonction $y \mapsto 1_D(x, y)$ est nulle et
donc intégrable et d'intégrale nulle et pour $x=c$ elle n'est pas
intégrable. Mais cette fonction est donc à nouveau intégrable pour
presque tout $x \in \mathbb{R}$ et d'intégrale nulle. La fin du
raisonnement est identique à celle du cas précédent.
:::

::: {.section}
#### Homothétie {#answer-h .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Homothétie}`{=latex}

Si l'on pose $D_1 = \mathbb{R}^n$, $D_2 = \mathbb{R}^n$, l'application
$h:D_1 \to D_2$ définie par $h(x) = \alpha x$ est un
$C^1$-difféomorphisme. De plus, on a $$
|\det J_{h}(x)| = \left|\det \left[
  \begin{array}{cccc}
  \alpha & 0  & \cdots & 0 \\
  0 & \alpha & \dots & 0 \\
  \vdots & \vdots & \vdots & \vdots \\
  0 & 0 & \dots & \alpha
  \end{array} \right] \right|  = |\alpha^n| = \alpha^n.
$$ Par conséquent, le [théorème de changement de variables (p.
`\pageref*{theorem-changement-de-variables}`{=tex})](#theorem-changement-de-variables)
fournit $$
\int_{\mathbb{R}^n} f(y) \, dy = \int_{\mathbb{R}^n} f(\alpha x) \alpha^n \, dx,
$$ soit $$
\int_{\mathbb{R}^n} f(\alpha x) \, dx = \frac{1}{\alpha^n} \int_{\mathbb{R}^n} f(y) \, dy.
$$
:::

::: {.section}
#### Volume et translation {#answer-vr .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Volume et translation}`{=latex}

L'ensemble $A$ mesurable et de volume fini a une fonction
caractéristique $1_A$ intégrable et $$
\lambda(A) = \int 1_A(x) \, dx.
$$ Soit $h(x) = x - u$ ou $u \in \mathbb{R}^3$. La fonction $h$ est une
bijection de $\mathbb{R}^3$ sur lui-même, continûment différentiable
ainsi que son inverse, $h^{-1}(x) = x + u$ et $J_h(x) = I$, donc
$\det J_h(x) = 1$. Par [le théorème de changement de variables (p.
`\pageref*{theorem-changement-de-variables}`{=tex})](#theorem-changement-de-variables),
la fonction $1_{h^{-1}(A)} = 1_{A} \circ h$ est donc intégrable sur
$\mathbb{R}^3$ et $$
\int 1_{h^{-1}(A)}\, dx = \int_{\mathbb{R}^3} (1_A \circ h) |\det J_h(x)| \, dx = \int_{\mathbb{R}^3} 1_A(x) \, dx = \lambda(A).
$$ L'ensemble translaté $A + u = h^{-1}(A)$ est donc mesurable, de
volume fini égal au volume de $A$.
:::

::: {.section}
#### Coordonnées polaires {#answer-cp .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Coordonnées polaires}`{=latex}

Les ensembles $P$ et $C$ sont ouverts et la fonction $h$ -- qui permet
de passer des coordonnées polaires aux coordonnées cartésiennes -- est
une bijection de $P$ dans $C$. Elle est continûment différentiable ; sa
matrice jacobienne en $(r, \theta)$ vaut $$
J_{h}(r, \theta) = 
\left[ 
\begin{array}{cr}
\cos \theta & -r \sin \theta \\
\sin \theta & r \cos \theta
\end{array}
\right],
$$ et son déterminant satisfait $$
\det J_{h}(r, \theta) = (\cos \theta)(r \cos \theta) - (\sin \theta)(-r\sin \theta)
= r > 0.
$$ Le jacobien est donc inversible et $h^{-1}$ est continûment
différentiable par le théorème d'inversion locale. On peut donc
appliquer [le théorème de changement de variables (p.
`\pageref*{theorem-changement-de-variables}`{=tex})](#theorem-changement-de-variables)
à la fonction $f$, ce qui fournit `\begin{align*}
\int_C f(x, y) \, d(x, y) &= \int_P f(h(r, \theta)) |\det J_h(r,\theta)| d(r,\theta) \\
&= \int_P g(r, \theta)  r \, d(r,\theta).
\end{align*}`{=tex}
:::

::: {.section}
#### Absence du déterminant jacobien {#answer-adj .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Absence du déterminant jacobien}`{=latex}

La façon la plus rapide de procéder consiste à considérer que
$f \circ h$ joue le rôle de $f$ dans [le théorème de changement de
variables (p.
`\pageref*{theorem-changement-de-variables}`{=tex})](#theorem-changement-de-variables),
que $h$ dans notre énoncé désigne $h^{-1}$ dans ce théorème et que les
rôles de $D_1$ et $D_2$ sont intervertis. Une fois que l'on a permuté
ces notations, on réalise que l'intégrale que l'on souhaite calculer est
le membre de gauche de l'équation du théorème de changement de
variables, dont toutes les hypothèses sont par ailleurs satisfaites. Par
conséquent on a $$
\int_{D_1} f (h(x)) \, dx = \int_{D_2} (f \circ h)(h^{-1}(y)) |\det J_{h^{-1}}(y)| \, dy.
$$ On peut simplifier $(f \circ h)(h^{-1}(y))$ en $f(y)$ et
éventuellement exprimer le jacobien de $h^{-1}$ en fonction du jacobien
de $h$ : $J_{h^{-1}}(y) = [J_{h}(h^{-1}(y))]^{-1}$ ; on obtient donc $$
\int_{D_1} f (h(x)) \, dx = 
\int_{D_2} f(y) |\det J_{h^{-1}}(y)| \, dy = 
\int_{D_2} f(y) \frac{1}{|\det J_{h}(h^{-1}(y))|} \, dy.
$$
:::
:::

::: {.section}
Aire du disque unité {#answer-adu .answer .unnumbered .unlisted}
--------------------

`\addcontentsline{toc}{subsection}{Aire du disque unité}`{=latex}

::: {.section}
#### Question 1 {#answer-adu-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

La fonction $1_D$ est intégrable : en effet, [l'ensemble $B$ est fermé
donc mesurable (p. `\pageref*{OSM}`{=tex})](#OSM) et la fonction $1_D$
est dominée par la fonction caractéristique du pavé fermé $[-1,1]^2$,
qui est intégrable. Par [le critère d'intégrabilité dominée (p.
`\pageref*{CID}`{=tex})](#CID), $1_D$ est donc intégrable.
:::

::: {.section}
#### Question 2 {#answer-adu-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Le théorème de Fubini nous fournit $$
\int_D dx = \int_{-1}^1 \left[\int_{-\sqrt{1-x^2}}^{\sqrt{1-x^2}} dy\right] dx
= 2 \int_{-1}^1 \sqrt{1 - x^2} \, dx.
$$ Comme $$
\int_{-1}^1 \sqrt{1 - x^2} \, dx
= \int_{[-1, 1]} \sqrt{1 - x^2} \, dx
= \int_{\left]-1, 1\right[} \sqrt{1 - x^2} \, dx,
$$ on peut donc opérer le changement de variable $$
\theta \in \left]0, \pi\right[ \mapsto x = -\cos \theta \in \left]-1,1\right[
$$ (bijectif, continûment différentiable ainsi que son inverse). Comme
$(-\cos \theta)' = \sin \theta$, on a $$
\int_{0}^{\pi} \sqrt{1-(-\cos^2 \theta)} \sin \theta  \, d\theta = \int_{-1}^1 \sqrt{1 - x^2} \, dx
$$ et donc $$
\int_{-1}^1 \sqrt{1 - x^2} \, dx
=
\int_{0}^{\pi} \sin^2 \theta  \, d\theta
=
\int_{0}^{\pi} \frac{1 - \cos 2\theta}{2} \, d\theta
=
\left[\frac{\theta}{2} - \frac{\sin 2\theta}{4} \right]_0^{\pi}
=\frac{\pi}{2},
$$ et finalement $$
\int_D \, dx = \pi.
$$
:::

::: {.section}
#### Question 3 {#answer-adu-3 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

On remarque que l'union $N$ de la frontière $\partial D$ de $D$ et du
segment $\{(x, 0) \, | \, x \in [-1, 0]\}$ est négligeable dans
$\mathbb{R}^2$ et donc que $$
\int_D \, dx = \int_{D \setminus N} dx,
$$ ce qui nous permet de considérer le changement de variable $$
\phi: (r, \theta) \in \left]0, 1\right[ \times \left]-\pi ,\pi\right[
\mapsto (x, y) = (r \cos \theta, r \sin \theta) \in D \setminus N
$$ (bijectif, continûment différentiable ainsi que son inverse). On
calcule la matrice jacobienne $$
J_{\phi}(r, \theta) = 
\left[ 
\begin{array}{cr}
\cos \theta & -r \sin \theta \\
\sin \theta & r \cos \theta
\end{array}
\right],
$$ dont le déterminant vaut $$
\det J_{\phi}(r, \theta) = (\cos \theta)(r \cos \theta) - (\sin \theta)(-r\sin \theta)
= r.
$$ On a donc $$
\int_{\left]0, 1\right[ \times \left]-\pi ,\pi\right[} r \, drd\theta
=
\int_D \, dx,
$$ et donc par le théorème de Fubini, $$
\int_D \, dx
= \int_{-\pi}^{\pi} \left[\int_{0}^1 r \, dr \right] \, d\theta
= \int_{-\pi}^{\pi} \frac{1}{2} \, d\theta
= \pi.
$$
:::
:::

::: {.section}
Intégrabilité des fonctions puissances
--------------------------------------

::: {.section}
#### Question 1 {#answer-ifp-1 .answer .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

L'ensemble $C$ peut être partitionné en 5 ensembles : $C_{++}$,
$C_{+-}$, $C_{-+}$, $C_{--}$ (où les signes en indices déterminent les
signes autorisés pour les variables $x_1$ et $x_2$) et $$
N := C \setminus (C_{++} \cup C_{+-} \cup C_{-+} \cup C_{--}).
$$ L'ensemble $C_{++}$ est ouvert, donc mesurable. Par conséquent, si
$f: x \mapsto \|x\|^{-\alpha}$ est intégrable sur $C$, elle est
intégrable sur $C_{++}$. Réciproquement, si $f$ est intégrable sur
$C_{++}$, elle est intégrable sur chacun des ensembles $C_{\pm\pm}$ par
changement de variable : le changement de variable
$h: (x_1, x_2) \mapsto (x_1, -x_2)$ est par exemple un difféomorphisme
de $C_{++}$ sur $C_{+-}$ tel que $|\det J_h| = 1$, donc [par changement
de variables (p.
`\pageref*{changement-de-variables}`{=tex})](#changement-de-variables)
l'intégrale de $f$ est bien définie sur $C_{+-}$ et $$
\int_{C_{+-}} \|x\|^{-\alpha} \, dx =
\int_{C_{+-}} \|h(x)\|^{-\alpha} |\det J_{h}(x)|\, dx = 
\int_{C_{++}} \|y\|^{-\alpha} \, dy = I.
$$ Comme $N$ est négligeable, $f$ est également intégrable sur $N$ et
par conséquent $f$ est intégrable sur $C$ comme somme des fonctions
intégrables $$
f = f 1_{C_{++}} +  f 1_{C_{+-}} + f 1_{C_{-+}} + f 1_{C_{--}} + f 1_N.
$$
:::

::: {.section}
#### Question 2 {#answer-ifp-2 .answer .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Si $x$ appartient à $C_{++}$, $\|x\|>1$, $x_1 >0$ et $x_2>0$, donc
$r=\|x\| > 1$ et $x_1 = \sqrt{r^2 - x_2^2} < r$. Réciproquement, si
$r>0$ et $0 < x_1 < r$, l'unique antécédent de $(x_1, r)$ par $h$ dans
$C_{++}$ est $(x_1, \sqrt{x_1^2 - r^2})$. La fonction $h$ est donc une
bijection de $C_{++}$ dans $$
U :=\{(x_1, r) \in \left]0,+\infty\right[\; | \; x_1 < r\}.
$$ De plus, $h$ est continûment différentiable, car elle est partout
différentiable et les coefficients de sa matrice jacobienne $$
J_h(x_1,x_2) = \left[ 
  \begin{array}{cc}
  1 & 0 \\
  \frac{x_1}{\sqrt{x_1^2+x_2^2}} & \frac{x_2}{\sqrt{x_1^2+x_2^2}}
  \end{array}
  \right]
$$ sont continus par rapport à $(x_1, x_2)$. On à également $$
J_{h^{-1}}(x_1,r) = \left[ 
  \begin{array}{cc}
  1 & 0 \\
  -\frac{x_1}{\sqrt{r^2 - x_1^2}} & \frac{r}{\sqrt{r^2-x_1^2}}
  \end{array}
  \right]
$$
:::

::: {.section}
#### Question 3 {#answer-ifp-3 .answer .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Si l'on considère les variables $x_1$ et $x_2$, la formule du [théorème
de changement de variables (p.
`\pageref*{changement-de-variables}`{=tex})](#changement-de-variables)
nous fournit $$
\int_{C++} \|x\|^{-\alpha} \, dx = \int_U r^{-\alpha} |\det J_{h^{-1}}(x_1,r)| \, dx_1 dr,
$$ soit $$
\int_{C++} \|x\|^{-\alpha} \, dx = \int_U r^{-\alpha} \frac{r}{\sqrt{r^2-x_1^2}} \, dx_1 dr
=
\int_U r^{-\alpha} \frac{1}{\sqrt{1-(x_1/r)^2}} \, dx_1 dr ;
$$ un nouveau changement de variable introduisant
$y = x_1/r \in \left]0, 1\right[$ fournit `\begin{align*}
\int_{C++} \|x\|^{-\alpha} \, dx &=
\int_{\left]0, 1\right[ \times \left]0,+\infty\right[} r^{-\alpha} \frac{1}{\sqrt{1-y^2}} r\, dy dr \\
&=
\int_{\left]0, 1\right[ \times \left]0,+\infty\right[} \frac{1}{r^{\alpha -1}} \frac{1}{\sqrt{1-y^2}} \, dy dr
\end{align*}`{=tex} La fonction $x\mapsto \|x\|^{-\alpha}$ est donc
intégrable si et seulement si cette dernière intégrale est bien définie.
Or, l'intégrande $$
(y, r) \in \left]0, 1\right[ \times \left]0,+\infty\right[ \mapsto \frac{1}{r^{\alpha -1}}\frac{1}{\sqrt{1-y^2}}
$$ -- et donc son extension par zéro à $\mathbb{R}^2$ -- sont mesurables
et positives, donc la caractérisation par [le théorème de Tonelli (p.
`\pageref*{Tonelli}`{=tex})](#Tonelli) est valable. Pour tout $r > 0$,
la fonction en question est intégrable par rapport à $y$ sur
$\left]0, 1\right[$ et $$
\int_{\left]0, 1\right[} 
\frac{1}{r^{\alpha -1}} \frac{1}{\sqrt{1-y^2}} \, dy
=
\frac{1}{r^{\alpha -1}} [\arcsin y]_0^1
= \frac{\pi}{2 r^{\alpha -1}}.
$$ La fonction $r \left]0, +\infty \right[ \mapsto r^{\alpha-1}$ étant
intégrable si et seulement si $\alpha > 2$, nous avons bien établi le
résultat recherché.
:::
:::

::: {.section}
Déformations d'un compact à bord régulier
-----------------------------------------

::: {.section}
#### Question 1 {#answer-dcbr .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Sous les hypothèses de l'énoncé, nous avons établi en exercice de
"Calcul Différentiel II" que la fonction $T$ est un
$C^1$-difféomorphisme global de $\mathbb{R}^n$ dans l'ouvert
$T(\mathbb{R}^n)$.

L'ensemble $T(K)$ est un ensemble compact comme image d'un ensemble
compact par une application continue. Comme $T$ est un difféomorphisme,
un point $y$ de $\mathbb{R}^n$ est intérieur à $T(K)$ si et seulement si
$x = T^{-1}(y)$ est intérieur à $K$. Les points de la frontière
$\partial T(K)$ sont donc les images des points de $\partial K$ par $T$.

Soit $y_0 \in \partial T(K)$ et $x_0 = T^{-1}(y_0) \in \partial K$. Dans
un voisinage $V$ de $x_0$, il existe une fonction continûment
différentiable $g:V \to \mathbb{R}$ de différentielle non nulle en $x_0$
telle que $g(x) \leq 0$ équivaut à $x \in K$. Par conséquent,
$y \in T(V)$ appartient à $T(K)$ si et seulement si
$g \circ T^{-1}(y) \leq 0$. La fonction $g \circ T^{-1}$ est continûment
différentiable et $$
d (g \circ T^{-1})(y_0) = dg (T^{-1}(y_0)) \cdot dT^{-1}(y_0)
= dg(x_0) \cdot (dT(x_0))^{-1}.
$$ Soit $u \in \mathbb{R}^n$ tel que $dg(x_0) \cdot u \neq 0$ ; si
$v = (dT(x_0)) \cdot u$, $d(g \circ T^{-1})(y_0) \cdot v \neq 0$. La
différentielle de $g \circ T^{-1}$ est donc non nulle en $y_0$. Par la
[caractérisation implicite des compacts à bord $C^1$ (p.
`\pageref*{cbr-implicit}`{=tex})](#cbr-implicit), $T(K)$ est donc un
compact à bord $C^1$ de $\mathbb{R}^n$.
:::
:::

::: {.section}
Ovales de Cassini
-----------------

::: {.section}
#### Question 1 {#answer-oc .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Montrons tout d'abord que l'ensemble $K$ est compact. Si les points
$(x_k, y_k)$ de $\mathbb{R}^2$ appartiennent à $K$, ils vérifient
$(x_k^2+y_k^2)^2 - 2a^2 (x_k^2 - y_k^2) + a^4 \leq b^4$ ; si la suite
converge vers $(x, y)$, par continuité
$(x^2+y^2)^2 - 2a^2 (x^2 - y^2) + a^4 \leq b^4$ et donc $(x, y) \in K$.
L'ensemble $K$ est donc fermé. De plus pour tout $(x, y) \in K$, comme
$$
\|(x, y)\|^4 = (x^2 + y^2)^2 \, \mbox{ et } \, x^2- y^2 \leq \|(x, y)\|^2, 
$$ on a $\|(x, y)\|^4 \leq b^4 - a^4 + 2a^2 \|(x, y)\|^2,$ donc si $$
\frac{\|(x, y)\|^4}{2} \geq b^4 
\, \mbox{ et } \,
\frac{\|(x, y)\|^2}{2} \geq 2a^2,
$$ le point $(x, y)$ n'appartient pas à $K$ ; l'ensemble $K$ est donc
borné. Fermé et borné dans $\mathbb{R}^2$, l'ensemble $K$ est donc
compact.

Pour montrer que l'on a affaire à un ensemble compact à bord $C^1$, nous
souhaitons utiliser le résultat sur [la caractérisation implicite de ces
ensembles (p. `\pageref*{cbr-implicit}`{=tex})](#cbr-implicit). La
fonction $g$ de ce théorème prend bien sûr ici la forme $$
g(x, y) := (x^2+y^2)^2 - 2a^2 (x^2 - y^2) + a^4 - b^4
$$ puisque $x \in K$ si et seulement si $g(x, y) \neq 0$. Il nous suffit
donc de vérifier que $g$ est $C^1$, ce qui est évident, et qu'en tout
point de la frontière de $K$, la différentielle de $g$ -- ou son
gradient -- est non-nulle. On se convaincra que tout point $(x, y)$ de
la frontière de $K$ vérifie nécessairement $g(x, y)$ en exploitant la
continuité de $g$. Par conséquent, notre démonstration sera achevée si
nous montrons qu'aucun point $(x, y)$ de $\mathbb{R}^2$ ne satisfait
simultanément $$
g(x, y) = 0, \, \partial_x g(x, y) = 0 \, \mbox{ et } \, \partial_y g(x, y) = 0.
$$ Or $\partial_x g(x, y) = 4(x^2+y^2)x - 4a^2x$ et
$\partial_x g(x, y) = 4(x^2+y^2)y + 4a^2 y$ ; de la nullité de ces deux
dérivées partielles, on déduit $$
(x^2+y^2)x = a^2 x \, \mbox{ et } \, (x^2 + y^2) y = -a^2 y.
$$ Il nous faut désormais envisager les cas possibles selon que $x$ et
$y$ sont nuls ou non:

-   $x \neq 0$ et $y \neq 0$ est impossible car les deux équations
    ci-dessus entraînent alors $(x^2+y^2) = a^2 = -a^2$ or $a > 0$.

-   $x = y = 0$ est impossible car $g(0, 0) = a^4 - b^4 \neq 0$, car
    $a>0$, $b>0$ et $a\neq b$.

-   $x = 0$ et $y \neq 0$ entraîne $x^2 + y^2 = y^2 = -a^2$, impossible
    car $a>0$.

-   finalement, si $x\neq 0$ et $y = 0$, $x^2 + y^2 = x^2 = a^2$, ce qui
    réinjecté dans $g(x, 0)= 0$ fournit $a^4 -2 a^4 + a^4 - b^4 = 0,$
    soit $b^4=0$, également impossible car $b>0$.

Aucun point $(x, y)$ de $\mathbb{R}^2$ n'annule simulanément $g$ et son
gradient ; l'ensemble $K$ est donc bien un compact à bord $C^1$.
:::
:::

::: {.section}
Intégrales de surface
---------------------

::: {.section}
#### Question 1 {#answer-is .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Comme la normale extérieure à $B$ en $\partial B$ vaut
$n(x) = (x_1, x_2)$ et que $x_1^2 + x_2^2 = 1$ sur $\partial B$, on a en
posant $v(x) = (x_1, x_2)$ sur $B$ l'égalité $$
\int_{\partial B} \sigma(dx) = \int_{\partial B} (x_1^2 + x_2^2) \, \sigma(dx)
= 
\int_{\partial B} \left<v(x), n(x)\right> \sigma(dx)
$$ et donc par le théorème de la divergence $$
\int_{\partial B} \sigma(dx)
= \int_{B} \mathrm{div} \, v(x) \, dx
= \int_{B} (\partial_1 x_1 + \partial_2 x_2) \, dx
= 2 \int_{B} \, dx.
$$ L'intégrale initiale est donc égale au double de l'aire du disque
unité, soit $2\pi$. Concernant la seconde intégrale, on à l'égalité $$
\int_{\partial B} x_1^2 \sigma(dx) = \int_{\partial B} \left<v(x), n(x)\right> \sigma(dx)
\, \mbox{ avec } \, v(x) = (x_1, 0)
$$ et donc par le théorème de la divergence $$
\int_{\partial B} x_1^2 \sigma(dx)
= \int_{B} \mathrm{div} \, v(x) \, dx
= \int_{B} (\partial_1 x_1 + \partial_2 0) \, dx
= \int_{B} \, dx.
$$ L'intégrale initiale est donc égale à l'aire du disque unité, soit
$\pi$.
:::
:::

::: {.section}
Rétraction
----------

Source: [@Kan81]

::: {.section}
#### Question 1 {#answer-pfb-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

On déduit de l'identité $\|f(x)\|^2=\left<f(x), f(x)\right> =1$ valable
sur $B$ que pour tout $h \in \mathbb{R}^2$, $$
\left<df(x) \cdot h, f(x) \right> + \left<f(x), df(x) \cdot h \right>=
2 \left<df(x)^{\top} \cdot f(x), h \right> = 0
$$ et donc la relation $J_f(x)^t f(x) = 0$. La valeur $f(x)$ étant non
nulle, cela entraîne la non-inversibilité de la matrice jacobienne
$J_f(x)$, ou ce qui est équivalent, la nullité du déterminant jacobien
$\det J_f(x)$. En conséquence, $$
\int_B \det J_f(x) \, dx = 0.
$$
:::

::: {.section}
#### Question 2 {#answer-pfb-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

La fonction $f$ étant de classe $C^2$, on a $$
\begin{split}
\det J_f 
&= (\partial_1 f_1) (\partial_2 f_2) - (\partial_1 f_2) (\partial_2 f_1) \\
&= \partial_1 (f_1 \partial_2 f_2) - f_1 \partial^2_{12} f_2
   -\partial_2 (f_1 \partial_1 f_2) + f_1 \partial^2_{21} f_2 \\
&= \partial_1 (f_1 \partial_2 f_2) 
   -\partial_2 (f_1 \partial_1 f_2)
\end{split}
$$ Par le théorème de la divergence, on a donc $$
\begin{split}
\int_B \det J_f(x) \, dx &=
\int_{\partial B} (n_1 (f_1 \partial_2 f_2) 
   -n_2 (f_1 \partial_1 f_2)) \sigma \\
&=\int_{\partial B} f_1 \left<\nabla f_2, t\right> \sigma
\end{split}
$$ où $t(x)$ désigne le vecteur tangent à $\partial B$ en $x$ : $$
t(x) = (-n_2(x), n_1(x)).
$$ Comme la normale extérieure à $B$ en $x=(x_1, x_2) \in \partial B$
est donnée par $n(x) = (x_1, x_2)$, on a $t(x) = (-x_2, -x_1)$. Par
ailleurs, comme $f(x)$ vaut identiquement $x$ sur $\partial B$, $f_2(x)$
vaut $x_2$ et par conséquent $$
\left<\nabla f_2(x), t(x)\right>  = \left<\nabla (x_2), t(x)\right>= x_1,
$$ soit, puisque $f_1(x) = x_1$ sur $\partial B$, $$
\int_B \det J_f(x) \, dx = \int_{\partial B} x_1^2 \, \sigma(dx) > 0.
$$ Si une telle rétraction existait, on aurait donc une contradiction.
:::
:::

::: {.section}
Intégration par parties
-----------------------

::: {.section}
#### Question 1 {#answer-IPP-n .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

On obtient le théorème d'intégration par parties en appliquant le
théorème fondamental du calcul à la dérivée du produit $fg$.

Supposons de façon analogue que $U$ est un ouvert de $\mathbb{R}^n$, $K$
un ensemble compact à bord $C^1$ de $U$ et que $f, g: U \to \mathbb{R}$
sont deux fonctions de classe $C^1$. Le produit $fg$ est également de
classe $C^1$ et pour tout $i \in \{1,\dots, n\}$, $$
\int_{K} \partial_i (fg) (x) \, dx
=
\int_{\partial K} n_i(x) f(x)g(x) \, \sigma(dx),
$$ soit $$
\int_{K} (\partial_i f(x))g(x) \, dx
=
\int_{\partial K} n_i(x) f(x)g(x) \, \sigma(dx) 
- \int_{K} f(x)(\partial_i g(x)) \, dx.
$$ Alternativement, si $f:U \to \mathbb{R}$ et $v: U \to \mathbb{R}^n$
sont deux fonctions de classe $C^1$, comme $fv$ est de classe $C^1$ et
que
$\mathrm{div} \, fv = f \mathrm{div} \, v + \left<\nabla f, v\right>$,
par le théorème de la divergence appliqué à $fv$ on obtient $$
\int_{K} \left<\nabla f(x), v(x)\right> \, dx
=
\int_{\partial K} f(x) \left<v(x), n(x) \right> \, \sigma(dx)
-\int_{K} f(x) \mathrm{div} \, v(x) \, dx.
$$
:::
:::
:::

::: {.section}
Réferences
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

[^2]: L'étude des démonstrations du cours peut toutefois contribuer à
    votre apprentissage, au même titre que la résolution d'exercices.

[^3]: Toute autre valeur que zéro conviendrait aussi bien ici, car la
    différence entre le domaine de définition du prolongement et le
    domaine initial est $[-\infty, \infty]^n \setminus \mathbb{R}^n$,
    qui est un ensemble négligeable (cf. [exercice "domaine à l'infini"
    (p. `\pageref*{dai}`{=tex})](#dai)). Dans le cas d'un domaine de
    définition initial $A$ quelconque, il est par contre nécessaire de
    prolonger par zéro (au moins presque partout).

[^4]: même si cela ne saute pas forcément aux yeux !

[^5]: La fonction $v$ étant continue et définie dans un ouvert
    ($U \times \mathbb{R}^{n-1}$), son support est compact dans cet
    ensemble si et seulement si l'ensemble $\{x \, | \, v(x) \neq 0\}$
    est borné et sa distance au complémentaire de $U\times \mathbb{R}$
    dans $\mathbb{R}^n$ est strictement positive.
