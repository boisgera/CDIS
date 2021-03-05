---
author:
- 'STEP, MINES ParisTech[^1]'
bibliography: bibliography.json
date: '5 mars 2021 (`#72befad`)'
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
title: Calcul Intégral II
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

-   [Introduction](#introduction)
-   [Objectifs d'apprentissage](#objectifs-dapprentissage)
-   [Théorèmes de convergence](#théorèmes-de-convergence)
-   [Ensembles mesurables](#ensembles-mesurables-1)
-   [Fonctions mesurables](#fonctions-mesurables-1)
    -   [Stabilité par passage à la limite](#SPL)
-   [Annexe -- Intégrabilité
    conditionnelle](#annexe-intégrabilité-conditionnelle)
-   [Exercices](#exercices)
    -   [Intégrale de Gauss](#intégrale-de-gauss)
    -   [Théorème de convergence
        dominée](#théorème-de-convergence-dominée)
    -   [Ensembles de longueur finie](#ensembles-de-longueur-finie)
    -   [Intégrabilité locale](#intégrabilité-locale)
    -   [Fonctions mesurables](#fonctions-mesurables-2)
    -   [Composition de fonctions et
        mesurabilité](#composition-de-fonctions-et-mesurabilité)
    -   [Composition par une fonction
        lipschitzienne](#composition-par-une-fonction-lipschitzienne)
    -   [Formule de la moyenne](#formule-de-la-moyenne)
-   [Solutions](#solutions)
    -   [Exercices essentiels](#exercices-essentiels)
    -   [Intégrale de Gauss](#intégrale-de-gauss-1)
    -   [Théorème de convergence
        dominée](#théorème-de-convergence-dominée-1)
    -   [Ensembles de longueur finie](#ensembles-de-longueur-finie-1)
    -   [Intégrabilité locale](#intégrabilité-locale-1)
    -   [Fonction mesurables](#fonction-mesurables)
    -   [Composition de fonctions et
        mesurabilité](#composition-de-fonctions-et-mesurabilité-1)
    -   [Composition par une fonction
        lipschitzienne](#composition-par-une-fonction-lipschitzienne-1)
    -   [Formule de la moyenne](#formule-de-la-moyenne-1)
-   [Références](#références)

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
Introduction
============

L'intégrale de Lebesgue, introduite dans "Calcul Intégral I", présente
l'avantage de pouvoir intégrer une plus grande gamme de fonctions que
l'intégrale de Riemann : moins régulières, non bornées et/ou définies
sur des intervalles non-bornés[^2].

Il faut néanmoins reconnaître qu'à ce stade de notre exposé l'intégrale
de Riemann est parfois plus pratique. Par exemple : si avec l'intégrale
de Lebesgue, on sait que $\lambda f$ et $f + g$ sont intégrables quand
$f$ et $g$ le sont, il n'est pas certain que le produit $f g$ soit
intégrable ; et nous ne disposons pas encore des outils adaptés pour
étudier cette intégrabilité. Or dans le cadre Riemannien, rien de plus
simple : si $f$ et $g$ sont des fonctions intégrables au sens de Riemann
sur un segment, le produit $fg$ est systématiquement intégrable au sens
de Riemannn sur ce segment[^3].

Cette remarque ne souligne pas à proprement parler un défaut de
l'intégrale de Lebesgue, mais plutôt une conséquence de sa généralité :
en permettant d'intégrer des fonctions telles que
$x \in [0, 1] \mapsto 1/\sqrt{x}$ (presque partout), on s'expose à
devoir refuser d'intégrer le produit d'une fonction par elle-même, ici
$x \in [0,1] \mapsto 1/x$ (presque partout). Il est donc normal de
devoir imposer des conditions supplémentaires pour garantir
l'intégrabilité d'un produit.

Heureusement, comme dans le cas de l'intégrale de Riemann, un critère
d'intégrabilité des fonctions -- nécessaire et suffisant -- existe pour
établir ce type de résultat (et bien d'autres). Comme dans le cas de
l'intégrale de Riemann, il se décompose en deux tests indépendants :
pour être intégrable une fonction doit être "dominée par une fonction
intégrable" et "suffisamment régulière". Bien sûr ici la fonction qui
domine devra être intégrable au sens de Lebesgue (et non plus de
Riemann) ; quant à la régularité, il ne s'agira plus de tester la
continuité presque partout, mais de vérifier la *mesurabilité* de la
fonction considérée, une propriété que possèdent presque toutes les
fonctions "non-pathologiques".

Dans ce chapitre pour des raisons de simplicité, nous mettrons l'accent
sur les fonctions définies sur $\mathbb{R}$ ; par défaut le symbole
intégrale sans bornes désignera donc l'intégrale entre $-\infty$ et
$+\infty$: $$
\int := \int_{-\infty}^{+\infty}.
$$ Si une fonction n'est définie que sur un sous-ensemble $A$ de
$\mathbb{R}$ -- qui pourra être un intervalle ou un ensemble plus
complexe -- il est naturel de l'étendre en une fonction définie sur
$\mathbb{R}$ prenant la valeur $0$ en dehors de $A$ puisque dans le cas
des intervalles, cette opération ne change pas la valeur de l'intégrale.
Le mouvement inverse -- restreindre une fonction définie sur
$\mathbb{R}$ à un sous-ensemble nécessite de considérer le produit
$1_A f$ de $f$ par la fonction caractéristique de $A$, ce qui soulève la
question de l'étude de l'intégrabilité de ces fonctions
caractéristiques.

Mais notre première étape dans ce chapitre sera de nous doter de
théorèmes de convergence qui nous permettront -- sous certaines
conditions qui sont plus simples que dans le cadre Riemannien -- de
calculer l'intégrale d'une fonction $f$ comme la limite d'intégrales de
fonctions convergeant vers $f$.
:::

::: {.section}
Objectifs d'apprentissage
=========================

::: {.section}
#### Ensembles mesurables

-   `$\mathord{\bullet}$ `{=tex}savoir qu'un ensemble est mesurable si
    sa longueur est bien définie,

-   `$\mathord{\bullet}$ `{=tex}connaître la définition formelle
    d'ensemble mesurable,

-   `$\mathord{\bullet}$ `{=tex}savoir calculer sa longueur comme une
    intégrale,

-   connaître les propriétés principales des ensembles mesurables :

    -   `$\mathord{\bullet}$ `{=tex}les ensembles mesurables forment une
        tribu,

    -   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}ensembles ouverts
        (et fermés) sont mesurables,

    -   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}négligeable = de
        longueur nulle.

-   connaître quelques propriétés secondaires qui s'en déduisent :

    -   `$\mathord{\bullet}$ `{=tex}intersection dénombrable d'ensembles
        mesurables.

    -   `$\mathord{\bullet}$ `{=tex}complémentaire relatif d'ensembles
        mesurables,

-   savoir les exploiter pour :

    -   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}montrer qu'un
        ensemble donné est mesurable,

    -   `$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$ `{=tex}déduire
        de nouvelles propriétés secondaires.
:::

::: {.section}
#### Fonctions mesurables

-   `$\mathord{\bullet}$ `{=tex}connaître la définition des fonctions
    mesurables,

-   `$\mathord{\bullet}$ `{=tex}connaître leur caractérisation par le
    critère de l'image réciproque,

-   savoir que les fonctions suivantes sont mesurables :

    -   `$\mathord{\bullet}$ `{=tex}les fonctions intégrables,

    -   `$\mathord{\bullet}$ `{=tex}les fonctions caractéristiques
        d'ensembles mesurables,

    -   `$\mathord{\bullet}$ `{=tex}les fonctions égales presque partout
        à des fonctions mesurables,

    -   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}les limites
        (simples) de fonctions mesurables,

    -   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}les compositions de
        fonctions mesurables et continues.

-   savoir exploiter les éléments précédents pour :

    -   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}montrer qu'une
        fonction donnée est mesurable,

    -   `$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$ `{=tex}déduire
        de nouvelles classes de fonctions mesurables.
:::

::: {.section}
#### Fonctions intégrables

-   `$\mathord{\bullet}$ `{=tex}connaître le critère d'intégrabilité
    dominée,

-   `$\mathord{\bullet}$ `{=tex}connaître le théorème de convergence
    dominée,

-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}connaître le théorème
    de convergence monotone,

-   savoir mettre en oeuvre ces théorèmes pour :

    -   `$\mathord{\bullet}$ `{=tex}montrer qu'une fonction est
        intégrable,

    -   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}calculer
        l'intégrale d'une fonction comme une limite,

    -   `$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$ `{=tex}démontrer
        qu'une fonction n'est pas intégrable.

-   `$\mathord{\bullet}$ `{=tex}connaître la définition d'intégrale sur
    un sous-ensemble (mesurable).
:::
:::

::: {.section}
Théorèmes de convergence
========================

::: {.section}
### Théorème -- Théorème de convergence dominée {#TCD .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Théorème de convergence dominée}`{=latex}

Si une suite de fonctions intégrables $f_k:\mathbb{R}\to \mathbb{R}$
converge simplement vers la fonction $f$, c'est-à-dire si pour tout
$x \in \mathbb{R}$, $$
\lim_{k \to +\infty} f_k(x) = f(x)
$$ et qu'il existe une fonction intégrable
$g:\mathbb{R}\to \left[0, +\infty\right[$ dominant la suite $f_k$,
c'est-à-dire telle que pour tout $k \in \mathbb{N}$ et pour tout
$x \in \mathbb{R}$, $$
|f_k(x)| \leq g(x)
$$ alors la fonction $f$ est intégrable et $$
\int f(t) \, dt 
=
\int \lim_{k \to +\infty} f_k(t) \, dt
= 
\lim_{k \to +\infty} \int f_k(t) \, dt.
$$
:::

::: {.section}
#### Démonstration {#démonstration .proof}

Se reporter à @Dem11.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Exercice -- Défaut de domination ($\mathord{\bullet}$) {#dd .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Défaut de domination}`{=latex}

Comparer $$
\lim_{k \to +\infty} \int f_k(t) \, dt
\; \mbox{ et } \; 
\int \lim_{k \to +\infty} f_k(t) \, dt\;
$$ pour la suite de fonctions $f_k:\mathbb{R}\to \mathbb{R}$ définie par
$$
f_k(t) = \left|
\begin{array}{rl}
1 & \mbox{si $k\leq t \leq k+1$} \\
0 & \mbox{sinon.}
\end{array}
\right.
$$ Expliquer le résultat. ([Solution p.
`\pageref*{answer-dd}`{=tex}](#answer-dd){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Intégrale fonction d'un paramètre ($\mathord{\bullet}\mathord{\bullet}$) {#ifp .exercise .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Intégrale fonction d'un paramètre}`{=latex}

Montrer que $$
\lim_{x \to 0^+} \int_0^1 \frac{e^{-xt}}{1+t^2} \, dt = \frac{\pi}{4}.
$$

([Solution p.
`\pageref*{answer-ifp}`{=tex}](#answer-ifp){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Théorème fondamental du calcul ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#exo-TCD .exercise .three .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Théorème fondamental du calcul}`{=latex}

Déduire de la forme classique du théorème fondamental du calcul et du
[théorème de convergence dominée (p. `\pageref*{TCD}`{=tex})](#TCD) que
si $f: [a, b] \subset [-\infty, +\infty] \to \mathbb{R}$ est continue
sur $[a, b]$, dérivable sur $[a, b]$ et de dérivée $f'$ intégrable,
alors $$
f(b) - f(a) = \int_a^b f'(t) \, dt.
$$ (Indication : considérer une suite d'intervalles fermés bornés
$[a_k, b_k]$ de $\mathbb{R}$ tels que $[a_k, b_k] \subset [a, b]$ et
tels que $a_k \to a$ et $b_k \to b$ quand $k \to +\infty.$) ([Solution
p.
`\pageref*{answer-exo-TCD}`{=tex}](#answer-exo-TCD){.no-parenthesis}.)
:::

::: {.section}
### Théorème -- Dérivation sous le signe somme {#DSS .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Dérivation sous le signe somme}`{=latex}

Soit $I$ un intervalle de $\mathbb{R}$ et
$f: I \times \mathbb{R}\to \mathbb{R}$ une fonction telle que :

1.  pour tout $\lambda \in I$, la fonction
    $t \in \mathbb{R}\mapsto f(\lambda, t)$ est intégrable,

2.  pour tout $t \in \mathbb{R}$, la fonction
    $\lambda \in I \mapsto f(\lambda, t)$ est dérivable et
    $$\sup_{\lambda \in I} |\partial_{\lambda} f(\lambda, t)| \leq g(t)$$
    où $g: \mathbb{R}\to \left[0, +\infty\right[$ est une fonction
    intégrable.

Alors, la fonction $S: I \to \mathbb{R}$ définie par $$
S(\lambda) := \int f(\lambda, t) \, dt
$$ est dérivable ; pour tout $\lambda \in I$, la fonction
$t \in \mathbb{R}\mapsto \partial_{\lambda} f(\lambda, t)$ est
intégrable et $$
S'(\lambda) = \int \partial_{\lambda} f(\lambda, t) \, dt.
$$
:::

::: {.section}
#### Démonstration {#démonstration-1 .proof}

Par linéarité de l'intégrale, pour tout $\lambda \in I$ et tout
$h \in \mathbb{R}^*$ tel que $\lambda + h \in I$, on a $$
\frac{S(\lambda + h) - S(\lambda)}{h}
= \int \frac{f(\lambda + h, t) - f(\lambda, t)}{h} \, dt.
$$ Soit $h_k$ une suite de réels non nuls tels que $\lambda + h_k \in I$
et $h_k \to 0$ quand $k \to +\infty$. En raison de la dérivabilité de
$f$ par rapport à son premier argument, pour tout $t \in \mathbb{R}$, $$
\lim_{k \to +\infty} \frac{f(\lambda + h_k, t) - f(\lambda, t)}{h_k}
= \partial_{\lambda} f(\lambda, t).
$$ De plus, par l'inégalité des accroissement finis, pour tout
$k \in \mathbb{N}$, $$
\left|\frac{f(\lambda + h_k, t) - f(\lambda, t)}{h_k} \right|
\leq \sup_{\mu \in I} |\partial_{\lambda} f(\mu, t)| \leq g(t).
$$ Les taux d'accroissements de $f$ sont donc bornés par une fonction
intégrable. Par [le théorème de convergence dominée (p.
`\pageref*{TCD}`{=tex})](#TCD), on conclut que $$
\lim_{k \to +\infty} \frac{S(\lambda + h_k) - S(\lambda)}{h_k}
=
\int \partial_{\lambda} f(\lambda, t) \, dt,
$$ ce qui achève la démonstration.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Théorème -- Théorème de convergence monotone {#TCM .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Théorème de convergence monotone}`{=latex}

Si une suite de fonctions intégrables $f_k:\mathbb{R}\to \mathbb{R}$ est
croissante et majorée en tout point, c'est-à-dire si pour tout $x$ de
$\mathbb{R}$ $$
\mbox{pour tout } \, k \in \mathbb{N}, \, f_k(x) \leq f_{k+1}(x) 
\; \mbox{ et } \;
\sup_k f_k(x) < + \infty,
$$ alors la limite simple $f$ des $f_k$ est intégrable si et seulement
si $$
\sup_k \int f_k(t) \, dt < +\infty.
$$ et dans ce cas, $$
\int f(t) \, dt 
=
\int \lim_{k \to +\infty} f_k(t) \, dt
= 
\lim_{k \to +\infty} \int  f(t) \, dt.
$$
:::

::: {.section}
#### Démonstration {#démonstration-2 .proof}

Se reporter à @Dem11.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Exercice -- Fonctions puissance ($\mathord{\bullet}$) {#power .one .exercise .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Fonctions puissance}`{=latex}

Montrer que la fonction puissance
$t \in \left[1, +\infty\right[ \mapsto t^{\alpha}$ est intégrable si et
seulement $\alpha < -1$ et que la fonction puissance
$t \in \left]0,1\right] \mapsto t^{\alpha}$ est intégrable si et
seulement si $\alpha > -1$. ([Solution p.
`\pageref*{answer-power}`{=tex}](#answer-power){.no-parenthesis}.)
:::

::: {.section}
#### Intégrabilité et intégrales impropres ($\mathord{\bullet}\mathord{\bullet}$) {#iii .two .question .exercise .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Intégrabilité et intégrales impropres}`{=latex}

Montrer qu'une fonction $f: \mathbb{R}\to \mathbb{R}$ qui est intégrable
sur tout intervalle fermé borné de $\mathbb{R}$ est intégrable sur
$\mathbb{R}$ si et seulement si $$
\lim_{k \to +\infty} \int_{-k}^k |f(t)| \, dt < +\infty.
$$

([Solution p.
`\pageref*{answer-iii}`{=tex}](#answer-iii){.no-parenthesis}.)
:::
:::

::: {.section}
Ensembles mesurables
====================

Il existe un lien étroit entre la notion de longueur d'un ensemble de
réels et le calcul intégral. Nous savons par exemple que pour tout
intervalle fermé borné $E = [a, b]$, la longueur $b-a$ de l'intervalle
peut être calculée par l'intégrale de la fonction caractéristique de
$E$ : $$
\ell(E) = \ell([a, b]):=  b - a  = \int_a^b \, dt = 
\int 1_{[a, b]}(t) \, dt =
\int 1_{E}(t) \, dt.
$$ Si $E$ est une collection finie d'intervalles disjoints $[a_i, b_i]$,
l'intégrale de $1_E$ vaut cette fois-ci $\sum_i b_i - a_i$, ce qui
correspond toujours à la valeur "intuitive" de la longueur de
l'ensemble.

Il apparait donc légitime pour définir la longueur d'un sous-ensemble
$E$ de $\mathbb{R}$ aussi général que possible[^4] de $\mathbb{R}$ de
prendre cette égalité comme une définition, ce qui suppose toutefois que
la fonction caractéristique soit intégrable ; on parle alors d'*ensemble
intégrable* ou *de longueur finie*. Cette définition laisse toutefois de
côté les ensembles "trop grands" pour être intégrables, mais par
ailleurs parfaitement anodins, comme $\mathbb{R}$ tout entier ou
l'ensemble des réels positifs. Nous préférons donc mettre l'accent sur
la notion d'ensemble *mesurable* :

::: {.section}
### Définition -- Ensemble mesurable {#ensemble-mesurable .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Ensemble mesurable}`{=latex}

Un ensemble $E$ de $\mathbb{R}$ est *de longueur finie* si sa fonction
caractéristique $1_E$ est intégrable sur $\mathbb{R}$ ; il est
*mesurable* si sa fonction caractéristique est intégrable sur tout
intervalle fermé borné $[a, b]$ de $\mathbb{R}$. La (mesure de)
*longueur* d'un ensemble $E$ mesurable est définie par $$
\ell(E) := \int 1_E(t) \, dt
$$ si $E$ est de longueur finie et $$
\ell(E) := +\infty
$$ dans le cas contraire (si $E$ est mesurable mais pas de longueur
finie).
:::

::: {.section}
### Remarque -- Interprétation {#interprétation .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Interprétation}`{=latex}

Il faut comprendre le terme "mesurable" littéralement, comme signifiant
"dont on peut définir la mesure (de longueur)", qui est un nombre fini
ou infini. Cette interprétation est cohérente, puisque tous les
ensembles $E$ de longueur finie sont bien mesurables ; en effet si la
fonction caractéristique $1_E$ est intégrable, sa restriction à tout
intervalle fermé borné $[a, b]$ également.
:::

::: {.section}
#### Exercice -- Ensemble de longueur finie I ($\mathord{\bullet}$) {#elfI .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Ensemble de longueur finie I}`{=latex}

Montrer que l'ensemble $E = \left[-1, 0\right[ \cup \left]0, 1\right]$
est de longueur finie et calculer sa longueur. ([Solution p.
`\pageref*{answer-elfI}`{=tex}](#answer-elfI){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Ensemble de longueur finie II ($\mathord{\bullet}$) {#elfII .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Ensemble de longueur finie II}`{=latex}

Montrer que l'ensemble $\mathbb{Q}$ est de longueur finie et calculer sa
longueur. ([Solution p.
`\pageref*{answer-elfII}`{=tex}](#answer-elfII){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Ensemble de longueur finie III ($\mathord{\bullet}\mathord{\bullet}$) {#elfIII .exercise .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Ensemble de longueur finie III}`{=latex}

Montrer que l'ensemble
$E = \cup_{k=0}^{+\infty} \left[k, k+2^{-k}\right[$ est de longueur
finie et calculer sa longueur. ([Solution p.
`\pageref*{answer-elfIII}`{=tex}](#answer-elfIII){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- La longueur est additive ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#la .exercise .question .three .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{La longueur est additive}`{=latex}

Montrer que la longueur $\ell$ est additive : si $A$ et $B$ sont deux
ensembles mesurables de $\mathbb{R}$ disjoints, alors $A\cup B$ est
mesurable et $\ell(A \cup B) = \ell(A) + \ell(B)$. ([Solution p.
`\pageref*{answer-la}`{=tex}](#answer-la){.no-parenthesis}.)
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
(On rappelle qu'un ensemble est *dénombrable* s'il est fini ou en
bijection avec $\mathbb{N}$.)
:::

::: {.section}
On agrège cet ensemble de propriétés en disant que les ensembles
mesurables de $\mathbb{R}$ forment une *tribu* -- ou *$\sigma$-algèbre*
-- de $\mathbb{R}$.
:::

::: {.section}
#### Démonstration {#démonstration-3 .proof}

1.  La fonction caractéristique $1_{\varnothing}$ est identiquement
    nulle ; l'ensemble vide $\varnothing$ est donc de longueur finie et
    par conséquent mesurable.

2.  Si l'ensemble $A$ est mesurable et $B = \mathbb{R}\setminus A$, pour
    tout $[a, b]$, l'ensemble $A \cap [a, b]$ est de longueur finie. Par
    ailleurs, l'ensemble $[a, b]$ est de longueur finie. Donc, comme $$
    1_{B \cap [a, b]} = 1_{[a, b]} - 1_{A \cap [a, b]},
    $$ l'ensemble $B \cap [a, b]$ est de longueur finie ; l'ensemble $B$
    est donc mesurable.

3.  Montrons tout d'abord que l'union d'une collection finie d'ensembles
    mesurables est mesurable ; il suffit d'établir que si $A$ et $B$
    sont mesurables, alors leur union $A \cup B$ l'est également. Or,
    pour tout intervalle fermé borné $[a, b]$, on a $$
    (A \cup B) \cap [a, b]
    = (A \cap [a, b]) \cup (B \cap [a, b]),
    $$ ce qui se traduit au moyen des fonctions caractéristiques par la
    relation `\begin{align*}
    1_{(A \cup B) \cap [a, b]}  &= \max \left(1_{A \cap [a, b]}, 1_{B \cap [a, b]} \right) \\
    &= 1_{A \cap [a, b]} + (1_{B \cap [a, b]} - 1_{A \cap [a, b]})_+
    \end{align*}`{=tex} où $x_+ := \max(x, 0)$. Comme
    $1_{B \cap [a, b]} - 1_{A \cap [a, b]}$ est intégrable et sa partie
    positive majorée par $2 \times 1_{[a, b]}$ qui est également
    intégrable, sa partie positive est intégrable (cf. annexe "Calcul
    Intégral I"). La fonction caractéristique de
    $(A \cup B) \cap [a, b]$ est donc intégrable.

    Considérons désormais une suite d'ensembles mesurables $A_k$, pour
    $k \in \mathbb{N}$. Quitte à remplacer $A_k$ par $\cup_{j=0}^k A_j$
    -- ce qui ne change pas le caractère mesurable des $A_k$ ou leur
    union jusqu'à l'ordre $k$ -- on peut supposer que
    $A_k \subset A_{k+1}$. Pour tout intervalle fermé borné $[a, b]$, $$
    \left(\bigcup_{k=0}^{+\infty} A_k\right) \cap [a, b] = 
    \bigcup_{k=0}^{+\infty} \left(A_k \cap [a, b]\right);$$ les
    ensembles $A_k \cap [a, b]$ sont de longueur finie, c'est-à-dire que
    $1_{A_k \cap [a, b]}$ est intégrable. Pour tout $k\in \mathbb{N}$,
    on a $0 \leq 1_{A_k \cap [a, b]} \leq 1_{[a, b]}$ ; les ensembles
    $A_k \cap [a, b]$ formant une suite croissante pour l'inclusion, la
    suite des fonctions caractéristiques $1_{A_k \cap [a, b]}$ est
    croissante et majorée par $1_{[a, b]}$ ; pour tout réel $x$ on a
    donc $$
    1_{\left(\cup_{k=0}^{+\infty} A_k\right) \cap [a, b]}(x)
    = \lim_{k\to +\infty} 1_{A_k \cap [a, b]}(x)
    $$ Par [le théorème de convergence dominée (p.
    `\pageref*{TCD}`{=tex})](#TCD), la fonction caractéristique de
    $\left(\cup_{k=1}^{+\infty} A_k\right) \cap [a, b]$ est intégrable ;
    cet ensemble est donc mesurable.

$\;\; \blacksquare$
:::

::: {.section}
### Proposition -- Intersection d'ensemble mesurables {#IEM .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Intersection d'ensemble mesurables}`{=latex}

L'intersection d'une collection dénombrable d'ensembles mesurables est
mesurable.
:::

::: {.section}
#### Démonstration {#démonstration-4 .proof}

Notons que pour toute collection $\mathcal{A}$ d'ensembles de
$\mathbb{R}$, $$
\bigcap \mathcal{A} =
\bigcap_{A \in \mathcal{A}} A= \left(\bigcup_{A \in \mathcal{A}} A^c\right)^c.
$$ La conclusion quand $\mathcal{A}$ est dénombrable résulte alors des
[propriétés élémentaires des ensembles mesurables (p.
`\pageref*{pptuxe9s-tribu}`{=tex})](#pptés-tribu).`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Exercice -- Suite d'ensembles ($\mathord{\bullet}\mathord{\bullet}$) {#sde .exercise .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Suite d'ensembles}`{=latex}

Soit $A_k$, $k \in \mathbb{N}$, une suite d'ensembles mesurables de
$\mathbb{R}$, $$
B = \{x \in \mathbb{R}\;| \; \exists \, k_0 \in \mathbb{N}, \, \forall \, k \geq k_0, \, x \in A_k\}
$$ et $$
C = \{x \in \mathbb{R}\; | \; \forall \, k_0 \in \mathbb{N}, \, \exists \, k \geq k_0, \, x \in A_k\}.
$$ Montrer que les ensembles $B$ et $C$ sont mesurables. ([Solution p.
`\pageref*{answer-sde}`{=tex}](#answer-sde){.no-parenthesis}.)
:::

::: {.section}
### Proposition -- Complémentaire relatif {#CR .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Complémentaire relatif}`{=latex}

Si les ensembles $A$ et $B$ sont mesurables, le complémentaire
$B \setminus A$ de $A$ dans $B$ est mesurable.
:::

::: {.section}
#### Démonstration {#démonstration-5 .proof}

Les ensembles $A$ et $B$ appartenant à $\mathbb{R}$, on a
$B \setminus A = B \cap A^c$ ; le complément de $A$ dans $B$ est donc
mesurable comme intersection d'ensembles
mesurables.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Théorème -- Topologie et ensembles mesurables {#OSM .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Topologie et ensembles mesurables}`{=latex}

Tout ensemble fermé (ou ouvert) est mesurable.
:::

::: {.section}
#### Démonstration {#démonstration-6 .proof}

Les ensembles fermés et ouverts étant complémentaires les uns des autres
et le [complémentaire d'un ensemble mesurable étant mesurable (p.
`\pageref*{pptuxe9s-tribu}`{=tex})](#pptés-tribu), on peut se contenter
de démontrer le résultat soit pour les ouverts soit pour les fermés ; la
preuve s'avère plus simple dans le cas des ouverts.

Tout intervalle ouvert $I$ est mesurable : en effet, son intersection
avec un intervalle fermé borné $[a, b]$ est un intervalle inclus dans
$[a, b]$. La fonction caractéristique associée est de la forme
$1_{[c, d]}$, ou en diffère au plus en deux points ; dans tous les cas,
elle est intégrable.

Si maintenant $U$ est un ensemble ouvert, pour chaque point $x$ de $U$
on peut construire le plus grand intervalle ouvert $I_x$ contenant $x$
et inclus dans $U$ (c'est l'union de tous les intervalles ouverts
vérifiant ces deux propriétés). Pour un couple $x$ et $y$ dans $U$, soit
$I_x = I_y$, soit $I_x$ et $I_y$ sont disjoints et l'union de tous les
intervalles $I_x$ est égale à $U$. Comme dans chaque $I_x$ on peut
choisir un nombre rationnel $y$ tel que $I_x = I_y$, la collection de
$I_x$ est dénombrable. L'ouvert $U$ est donc une union dénombrable
d'intervalles ouverts[^5], qui sont tous mesurables, il est donc
mesurable.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Exercice -- Ni ouvert ni fermé ($\mathord{\bullet}$) {#nonf .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Ni ouvert ni fermé}`{=latex}

Exhiber un ensemble mesurable $E$ de $\mathbb{R}$ qui ne soit ni ouvert
ni fermé. ([Solution p.
`\pageref*{answer-nonf}`{=tex}](#answer-nonf){.no-parenthesis}.)
:::

::: {.section}
### Théorème -- Ensembles négligeables {#négligeable-longueur-nulle .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Ensembles négligeables}`{=latex}

Un ensemble est de longueur nulle si et seulement s'il est négligeable.
:::

::: {.section}
#### Démonstration {#démonstration-7 .proof}

Si l'ensemble $A$ est négligeable, sa fonction caractéristique est égale
presque partout à la fonction identiquement nulle, qui est intégrable et
d'intégrale nulle. Par conséquent, $1_A$ est intégrable et d'intégrale
nulle, donc l'ensemble $A$ est intégrable et de longueur nulle.

Réciproquement, supposons l'ensemble $A$ de longueur nulle ; nous
cherchons à montrer que pour tout $\varepsilon >0$, il existe une
famille dénombrable d'intervalles $I_i$ de $\mathbb{R}$ qui recouvre $A$
et telle que $$
\sum_i \ell(I_i) \leq \varepsilon.
$$

Supposons temporairement que $A$ soit inclus dans un intervalle fermé
borné $[a, b]$ de $\mathbb{R}$. La fonction caractéristique $1_A$ de $A$
est intégrable, donc pour tout $\varepsilon > 0$ il existe une jauge
$\gamma$ sur $[a, b]$ telle que, si la subdivision pointée (totale ou
partielle) $\mathcal{D} =\{(t_i, I_i)\}_i$ est subordonnée à $\gamma$,
on a $$
S(1_A, \mathcal{D})
=
\left|S(1_A, \mathcal{D}) - \sum_i \int_{I_i}  1_A (t) \, dt \right| 
\leq 
\varepsilon.
$$ Pour conclure, nous allons construire une famille dénombrable
$\{(t_i, I_i)\}_i$ où les $I_i$ sont des intervalles fermés bornés de
$[a, b]$ sans chevauchement, tels que pour tout $i$, $t_i \in A$,
$I_i \subset \gamma(t_i)$ et tels que la famille des $I_i$ recouvre $A$.
Si cette construction est acquise et que $\mathcal{D}_k$ désigne la
collection des $\{(t_i, I_i)\}$ pour $0 \leq i \leq k-1$, alors c'est
une subdivision pointée partielle de $[a, b]$ subordonnée à $\gamma$ et
donc $$
S(1_A, \mathcal{D}_k) 
=
\sum_{i=0}^{k-1} 1_A(t_i) \ell(I_i)
=
\sum_{i=0}^{k-1} \ell(I_i) \leq \varepsilon.
$$ En passant à la limite sur $k$, cette inégalité fournit comme
souhaité $$
\sum_{i=0}^{+\infty} \ell(I_i) \leq \varepsilon.
$$

Procédons à la construction de la collection de $(t_i, I_i)$, par
dichotomie. S'il existe un $t \in [a, b]$ tel que $t \in A$ et
$[a, b] \subset \gamma(t)$, alors on prend pour collection le singleton
$\{(t, [a, b])\}$. Dans le cas contraire, on considère la décomposition
de $[a, b]$ en $[a, (a+b)/2]$ et $[(a+b)/2, b]$. On examine chacun de
ces intervalles $J$ et s'il existe un $t \in A \cap J$ tel que
$J \subset \gamma(t)$, on inclut la paire $(t, J)$ dans la collection ;
dans le cas contraire, on poursuit la dichotomie. Cette procédure
définit par construction une famille dénombrable $\{(t_i, I_i)\}_i$ où
$t_i \in A$ et les $I_i$ sont des intervalles fermés bornés de $[a, b]$
sans chevauchement tels que pour tout $t_i$, $I_i \subset \gamma(t_i)$.
De plus, les $I_i$ recouvrent $A$ : en effet si l'on considère
$t \in A$, il existe nécessairement un entier $k$ tel que tout
intervalle fermé borné $I$ de longueur inférieure ou égale à $(b-a)/2^k$
contenant $t$ vérifie $I \subset \gamma(t)$. Par conséquent, $t$
appartient à l'un des intervalles inclus par le procédé au plus tard à
l'étape $k$ de la dichotomie.

Finalement, supposons $A$ de longueur nulle mais plus nécessairement
borné. Soit $\varepsilon > 0$. Pour tout $k \in \mathbb{N}$, l'ensemble
$A \cap [-k, k]$ est de longueur nulle et borné ; il peut donc être
recouvert par une famille dénombrable d'intervalles dont la somme des
longueurs est inférieure $\varepsilon / 2^{k+1}$. Comme
$A = \cup_{k=0}^{+\infty} (A \cap [-k, k])$, la collection de tous ces
intervalles recouvre $A$ ; la somme de leur longueur est majorée par
$\sum_{k=0}^{+\infty} \varepsilon/2^{k+1} = \varepsilon.$ L'ensemble $A$
est donc négligeable.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Corollaire -- Complétude de la longueur {#complétude .corollary .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Complétude de la longueur}`{=latex}

Un sous-ensemble d'un ensemble de longueur nulle est de longueur nulle.
:::

::: {.section}
#### Démonstration {#démonstration-8 .proof}

Un sous-ensemble $A$ d'un ensemble négligeable $B$ est négligeable car
pour tout $\varepsilon > 0$, il existe une famille dénombrable
d'intervalles $I_i$ recouvrant $B$ et tels que
$\sum_i \ell(I_i) \leq \varepsilon$ ; or cette famille recouvre aussi
$A$. Comme [un ensemble est négligeable si et seulement si il est de
longueur nulle (p.
`\pageref*{nuxe9gligeable-longueur-nulle}`{=tex})](#négligeable-longueur-nulle),
cet argument conclut la démonstration.`\hfill$\blacksquare$`{=latex}
:::
:::

::: {.section}
Fonctions mesurables
====================

::: {.section}
### Définition -- Fonction mesurable {#fonction-mesurable .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Fonction mesurable}`{=latex}

Une fonction $f:\mathbb{R}\to \mathbb{R}$ est *mesurable* si elle est la
limite simple d'une suite de fonctions intégrables, c'est-à-dire s'il
existe une suite de fonctions intégrables $f_k:\mathbb{R}\to \mathbb{R}$
telle que pour tout $x\in \mathbb{R}$, $f_k(x) \to f(x)$ quand
$k \to +\infty$. Une fonction $f:\mathbb{R}\to \mathbb{R}^m$ est
mesurable si chacune de ses composantes est mesurable.
:::

::: {.section}
### Remarque -- Mesurabilité sur un intervalle {#mesurabilité-sur-un-intervalle .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Mesurabilité sur un intervalle}`{=latex}

Nous nous limitons dans ce chapitre à l'étude des fonctions mesurables
définies sur $\mathbb{R}$. La notion peut être très facilement étendue à
une fonction $f$ définie sur un intervalle $I$ de $\mathbb{R}$ de la
façon suivante : on dira que $f$ est mesurable si son prolongement par
$0$ dans le complémentaire de $I$ est mesurable. Nous vous laissons le
soin de généraliser en conséquence les énoncés qui vont suivre.
:::

::: {.section}
### Théorème -- Critère d'intégrabilité dominée {#CID .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Critère d'intégrabilité dominée}`{=latex}

Une fonction $f: \mathbb{R}\to \mathbb{R}$ est intégrable si et
seulement si $f$ est mesurable et il existe une fonction intégrable
$g: \mathbb{R}\to \left[0,+\infty\right[$ telle que $|f| \leq g$.
:::

::: {.section}
La démonstration de ce théorème, qui nécessite des résultats
intermédiaires, est donnée [à la fin de cette section (p.
`\pageref*{proof-CID}`{=tex})](#proof-CID).
:::

::: {.section}
### Remarque -- Interprétation {#interprétation-1 .post .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Interprétation}`{=latex}

Souvenons-nous qu'une fonction définie sur un intervalle fermé et borné
est intégrable au sens de Riemann si et seulement si elle est encadrée
par deux fonctions intégrables au sens de Riemann et continue presque
partout.

Dans le cas de l'intégrale de Riemann comme de Lebesgue, l'intégrabilité
est donc caractérisée par une structure analogue qui repose sur deux
propriétés distinctes : être encadrée par deux fonctions intégrables
(pour la notion d'intégrale considérée) et être "suffisamment
régulière". La différence est que dans le cas de l'intégrale de Riemann
l'exigence de régularité est forte -- être continue presque partout --
alors que dans le cas de l'intégrale de Lebesgue, la régularité demandée
-- la mesurabilité -- s'avère être une condition très peu
contraignante[^6].
:::

::: {.section}
Plusieurs propriétés des fonctions mesurables se déduisent directement
de leur définition :
:::

::: {.section}
### Proposition -- Les fonctions intégrables sont mesurables {#les-fonctions-intégrables-sont-mesurables .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Les fonctions intégrables sont mesurables}`{=latex}
:::

::: {.section}
#### Démonstration {#démonstration-9 .proof}

Si $f$ est une fonction intégrable, elle est la limite simple de la
suite constante égale à $f$.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Proposition -- Les fonctions mesurables forment un espace vectoriel {#les-fonctions-mesurables-forment-un-espace-vectoriel .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Les fonctions mesurables forment un espace vectoriel}`{=latex}
:::

::: {.section}
#### Démonstration {#démonstration-10 .proof}

Si $f$ et $g$ sont mesurables et $\lambda$ est un nombre réel, il existe
des suites $f_k$ et $g_k$ de fonctions intégrables convergeant
simplement vers $f$ et $g$ respectivement. Les fonctions $f_k + g_k$ et
$\lambda f_k$ sont intégrables et convergent alors simplement vers $f+g$
et $\lambda f$ respectivement.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Proposition -- Les fonctions continues presque partout sont mesurables {#les-fonctions-continues-presque-partout-sont-mesurables .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Les fonctions continues presque partout sont mesurables}`{=latex}
:::

::: {.section}
#### Démonstration {#démonstration-11 .proof}

Soit $f:\mathbb{R}\to \mathbb{R}$ une fonction continue presque partout.
Soit $k \in \mathbb{N}$ ; on note $\sigma_k:\mathbb{R}\to \mathbb{R}$ la
fonction définie par $$
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

Comme $\sigma_k$ est continue et bornée, la fonction
$g_k : [-k, k] \to \mathbb{R}$ définie par $$
x \in [-k, k] \mapsto (\sigma_k \circ f)(x)
$$ est continue presque partout sur $[-k, k]$ et bornée. Par conséquent,
elle est intégrable au sens de Riemann -- et donc de Lebesgue -- sur
$[-k, k]$. Son extension $f_k$ par zéro au reste de $\mathbb{R}$ est
donc intégrable au sens de Lebesgue. De plus, la suite des $f_k$
converge simplement vers $f$ ; la fonction $f$ est donc
mesurable.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Théorème -- Critère de l'image réciproque {#CIR .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Critère de l'image réciproque}`{=latex}

Une fonction $f:\mathbb{R}\to \mathbb{R}^m$ est mesurable si et
seulement l'image réciproque de tout fermé (ou de tout ouvert) de
$\mathbb{R}^m$ par $f$ est mesurable.
:::

::: {.section}
#### Exercice -- Fonctions continues ($\mathord{\bullet}$) {#fcm .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Fonctions continues}`{=latex}

Montrer en utilisant le critère de l'image réciproque que toute fonction
continue est mesurable. ([Solution p.
`\pageref*{answer-fcm}`{=tex}](#answer-fcm){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Image réciproque d'un intervalle ($\mathord{\bullet}$) {#iri .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Image réciproque d'un intervalle}`{=latex}

Montrer que si $f: \mathbb{R}\to \mathbb{R}$ est mesurable, alors
l'image réciproque d'un intervalle arbitraire par $f$ est mesurable.
([Solution p.
`\pageref*{answer-iri}`{=tex}](#answer-iri){.no-parenthesis}.)
:::

::: {.section}
En se basant exclusivement sur ce critère de mesurabilité par les images
réciproques (donc en comprenant temporairement "mesurable" comme
"satisfaisant le critère de l'image réciproque" en attendant la preuve
de l'équivalence des deux propriétés), on peut montrer les résultats
suivants:
:::

::: {.section}
### Stabilité par passage à la limite {#SPL}

Les limites simples de fonctions mesurables sont mesurables.
:::

::: {.section}
#### Démonstration {#démonstration-12 .proof}

Soit $f_k: \mathbb{R}\to \mathbb{R}$ des fonctions vérifiant [le critère
de l'image réciproque (p. `\pageref*{CIR}`{=tex})](#CIR), telles que
pour tout $x \in \mathbb{R}$, $f_k(x) \to f(x)$ quand $k \to +\infty$.
Montrons que $f$ vérifie également ce critère. Il suffit pour cela de
remarquer que comme $U$ est ouvert et que $f_k(x) \to f(x)$,
$f(x) \in U$ si et seulement si $f_k(x) \in U$ pour $k$ assez grand.
Cette déclaration se traduit par la formule $$
f^{-1}(U) = \bigcup_{j=0}^{+\infty} \bigcap_{k = j}^{+\infty} f_k^{-1}(U)
$$ qui établit que $f^{-1}(U)$ est un ensemble mesurable, comme union
(dénombrable) d'intersections (dénombrable) d'ensembles
mesurables.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Théorème -- Fonctions égales presque partout {#FPPE .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Fonctions égales presque partout}`{=latex}

Toute fonction égale presque partout à une fonction mesurable est
mesurable.
:::

::: {.section}
#### Démonstration {#démonstration-13 .proof}

Toute fonction $f$ égale presque partout à une fonction $g$ qui vérifie
[le critère de l'image réciproque (p. `\pageref*{CIR}`{=tex})](#CIR)
vérifie également [le critère de l'image réciproque (p.
`\pageref*{CIR}`{=tex})](#CIR). En effet, si pour tout ouvert $U$
l'ensemble $g^{-1}(U)$ est mesurable, alors $$
f^{-1}(U) = (g^{-1}(U) \setminus E) \cup F
$$ où $E$ et $F$ sont négligeables et donc mesurables puisque [la mesure
de Lebesgue est complète (p.
`\pageref*{compluxe9tude}`{=tex})](#complétude) ; par conséquent,
$f^{-1}(U)$ est mesurable.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Démonstration du [critère de l'image réciproque (p. `\pageref*{CIR}`{=tex})](#CIR) {#pCIR .proof}

Il suffit de démontrer le critère pour les ensembles ouverts : si une
fonction satisfait le critère de d'image réciproque pour tout ouvert de
$\mathbb{R}^m$, alors si $F$ est un fermé de $\mathbb{R}^m$, en
utilisant l'égalité
$f^{-1}(F) = \mathbb{R}\setminus f^{-1}(\mathbb{R}^m \setminus F)$, le
fait que le complémentaire d'un fermé soit un ouvert et que [le
complémentaire d'un ensemble mesurable soit mesurable (p.
`\pageref*{pptuxe9s-tribu}`{=tex})](#pptés-tribu), on établit le critère
pour les fermés.

Montrons tout d'abord le résultat pour les fonctions scalaires ($m=1$).
Supposons [le critère de l'image réciproque (p.
`\pageref*{CIR}`{=tex})](#CIR) satisfait. La démonstration repose sur la
construction explicite d'une suite $f_k(x)$ de fonctions intégrables qui
soient étagées, c'est-à-dire ne prenant qu'un nombre fini de valeurs
possibles.

Définissons $f_0(x) = 0$ et $f_k(x)$ par la relation de récurrence $$
f_{k+1}(x) = f_k(x) + 
\left|
\begin{array}{rl}
-1/k & \mbox{si } \, f(x) \leq f_k(x) -1/k \, \mbox{ et } \, |x| \leq k,\\
+1/k  & \mbox{si } \, f_k(x) + 1/k \leq f(x)  \, \mbox{ et } \, |x| \leq k, \\
0 & \mbox{sinon.}
\end{array}
\right.
$$ Par construction, si $f(x)=0$, $f_k(x)= 0$. Si $f(x) \geq 0$, les
$f_k(x)$ forment une suite croissante convergeant vers $f(x)$, car la
suite des $1/k$ tend vers $0$ quand $k$ tend vers $+\infty$, mais leur
somme est divergente. La situation est similaire si $f(x) \leq 0$, mais
avec une suite $f_k(x)$ décroissante.

Montrons que la suite des $f_k$ est intégrable, ce qui concluera cette
section de la preuve. L'ensemble des valeurs $\{y_j\}$ que prend chaque
$f_k$ est bien fini ; il comprend la valeur $y_0 = 0$ et la fonction
peut s'écrire sous la forme $$
f_k = \sum_{j} y_j 1_{A_j}
$$ où les $A_j = f_k^{-1}(y_j)$ sont en nombre fini et disjoints. A part
$A_0$, les $A_j$ sont également bornés, car $f_k$ est nulle en dehors de
$[-k, k]$. Montrons qu'à tout rang $k$, les ensembles $A_j$ sont
mesurables, ce qui prouvera que chaque $f_k$ est intégrable comme
combinaison linéaire de fonctions intégrables. C'est évident au rang $0$
où $\{y_j\} = \{0\}$ et la collection des $A_j$ se réduit à
$\{A_0\} = \{\mathbb{R}\}$. Supposons cette propriété valable au rang
$k$ ; l'ensemble $E$ des réels $x$ tels que $f_k(x) + 1/k \leq f(x)$ et
$|x| \leq k$ peut être écrit comme $$
E = \left(\bigcup_j \{x \in \mathbb{R}\, | \, y_j + 1/k \leq f(x)\} \cap A_j\right) \cap [-k, k],
$$ qui est mesurable. De même, on peut montrer que l'ensemble $F$ des
réels $x$ tels que $f(x) \leq f_k(x) - 1/k$ et $|x| \leq k$ est
mesurable. On a alors par construction: $$
f_{k+1} = \sum_{j} y_j 1_{A_j} + \frac{1}{k} 1_E - \frac{1}{k} 1_F
$$ qui est sous la forme souhaitée, à ceci près que les ensembles
intervenant ne sont pas nécessairement disjoints. Mais pour toute valeur
$y$ dans l'image de $f_{k+1}$, l'image réciproque de $\{y\}$ par $f$ est
nécessairement une union (finie) d'intersections (finies) d'ensembles
dans la collection $\{\dots, A_j, \dots, E, F\}$ et donc un ensemble
mesurable. La fonction $f_{k+1}$ peut donc être mise sous la forme
souhaitée.

Réciproquement, considérons désormais une fonction intégrable
$f:\mathbb{R}\to \mathbb{R}$. Par le théorème de dérivation des
intégrales indéterminées, si l'on définit la fonction $f_k(x)$ comme le
taux d'accroissement $$
f_k(x) :=  \frac{F(x + 2^{-k}) - F(x)}{2^{-k}}
\; \mbox{ où } \;
F: x \in \mathbb{R}\mapsto \int_0^x f(t) \, dt,
$$ alors $f_k(x) \to f(x)$ presque partout quand $k \to +\infty$. Or
chaque $f_k$ est continue, donc l'image réciproque de tout ouvert par
$f_k$ est un ouvert [et donc un ensemble mesurable (p.
`\pageref*{OSM}`{=tex})](#OSM) ; c'est encore le cas des fonctions qui
sont égales presque partout aux $f_k$ mais valent $0$ aux points ou les
$f_k$ ne convergent pas, car [elles sont égales presque partout aux
fonctions $f_k$ (p. `\pageref*{FPPE}`{=tex})](#FPPE). L'ensemble des
fonctions satisfaisant le critère de l'image réciproque étant [stable
par passage à la limite (p. `\pageref*{SPL}`{=tex})](#SPL), [une
fonction égale à $f$ presque partout satisfait le critère de l'image
réciproque (p. `\pageref*{FPPE}`{=tex})](#FPPE) ; la fonction intégrable
$f$ satisfait donc elle-même le critère de l'image réciproque.

Finalement, une fonction mesurable est une limite simple d'une suite de
fonctions intégrables et les fonctions intégrables vérifient le critère
de l'image réciproque, par une nouvelle application du résultat de
[stabilité par passage à la limite (p. `\pageref*{SPL}`{=tex})](#SPL),
ce critère est également satisfait pour toute fonction mesurable.

Pour établir le résultat dans le cas où $n>1$, il suffit de montrer
qu'une fonction $f:\mathbb{R}\to \mathbb{R}^m$ satisfait le critère de
l'image réciproque si et seulement si toutes ses composantes le
satisfont. Pour le sens direct, il suffit de constater que $$
f_k^{-1}(U) = f^{-1}(\mathbb{R}\times \cdots \times U \times \cdots \mathbb{R})
$$ et que si $U$ est ouvert,
$\mathbb{R}\times \cdots \times U \times \cdots \mathbb{R}$ également.
Pour la réciproque, nous exploitons le fait[^7] que tout ouvert de
$\mathbb{R}^m$ peut être décomposé comme l'union d'une collection
dénombrable $\mathcal{P}$ de pavés ouverts de la forme $$
P = \left]a_1,b_1\right[ \times \dots \times \left]a_n,b_n\right[.
$$ Il nous suffit alors de noter que pour tout pavé $P$, $$
f^{-1}(P) = f_1^{-1}(\left]a_1,b_1\right[) \times \dots \times f_n^{-1}(\left]a_n,b_n\right[)
$$ et donc $f^{-1}(P)$ est mesurable. Comme
$f^{-1}(U) = \cup_{P \in \mathcal{P}} f^{-1}(P)$ et que $\mathcal{P}$
est dénombrable, l'image réciproque de $U$ par $f$ est bien
mesurable.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Démonstration du critère d'intégrabilité dominée {#proof-CID .proof}

Le sens direct est évident : si la fonction $f$ est intégrable, elle est
mesurable et est dominée par la fonction $|f|$ qui est intégrable.

Pour montrer la réciproque dans ce cas, nous approchons la fonction
mesurable $f$ par la suite de fonctions étagées $f_k$ introduites dans
[la démonstration du critère de l'image réciproque (p.
`\pageref*{pCIR}`{=tex})](#pCIR). La fonction $f$ apparaît comme une
limite simple des fonctions $f_k$, qui sont intégrables et dominées par
la fonction intégrable $g$. Par [le théorème de convergence dominée (p.
`\pageref*{TCD}`{=tex})](#TCD), $f$ est
intégrable.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Théorème -- Composition par une fonction continue {#CFC .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Composition par une fonction continue}`{=latex}

Soit $f:\mathbb{R}\to \mathbb{R}^m$ une fonction mesurable et
$g:\mathbb{R}^m \to \mathbb{R}^p$ une fonction continue. La composée
$g \circ f$ de ces deux fonctions est mesurable.
:::

::: {.section}
Dans le cas d'une fonction $g: \mathbb{R}\to \mathbb{R}$, il suffit de
supposer que $g$ soit continue par morceaux pour pouvoir conclure
(cf. exercice ["Composition de fonctions et mesurabilité" (p.
`\pageref*{cfm}`{=tex})](#cfm)). (En général, les fonctions $g$ qui
assurent que $g \circ f$ soit mesurable pour toutes les fonctions
mesurables $f$ sont appelées fonctions *boréliennes*.).
:::

::: {.section}
#### Démonstration {#démonstration-14 .proof}

Si $F$ est un fermé de $\mathbb{R}^p$, par continuité de $g$, l'ensemble
$g^{-1}(F)$ est un fermé de $\mathbb{R}^m$ et par conséquent, par [le
critère de mesurabilité par les images réciproques (p.
`\pageref*{CIR}`{=tex})](#CIR) $$
(g\circ f)^{-1}(F) = f^{-1}(g^{-1}(F))
$$ est un ensemble mesurable. Par le même critère, la composée
$g\circ f$ est donc mesurable.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
Les corollaires de ce résultat sont nombreux et immédiats. Citons les
deux instances les plus directement utiles.
:::

::: {.section}
### Corollaire -- Mesurabilité du produit {#prod .corollary .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Mesurabilité du produit}`{=latex}

Le produit de deux fonctions scalaires mesurables est mesurable.
:::

::: {.section}
#### Démonstration {#démonstration-15 .proof}

Par continuité de l'application produit
$\times: \mathbb{R}\times \mathbb{R}\to \mathbb{R}$.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Corollaire -- Mesurabilité de la valeur absolue {#abs .corollary .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Mesurabilité de la valeur absolue}`{=latex}

La valeur absolue d'une fonction scalaire mesurable est mesurable.
:::

::: {.section}
#### Démonstration {#démonstration-16 .proof}

Par continuité de l'application valeur absolue
$|\, \cdot \,|: \mathbb{R}\to \mathbb{R}$.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Exercice -- Intégrabilité du produit ($\mathord{\bullet}$) {#ip .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Intégrabilité du produit}`{=latex}

Soient $f:\mathbb{R}\to \mathbb{R}$ et $g:\mathbb{R}\to \mathbb{R}$ deux
fonctions mesurables dont les carrés sont intégrables. Montrer que le
produit $fg$ est intégrable. ([Solution p.
`\pageref*{answer-ip}`{=tex}](#answer-ip){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Intégrabilité du maximum ($\mathord{\bullet}$) {#im .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Intégrabilité du maximum}`{=latex}

Soient $f:\mathbb{R}\to \mathbb{R}$ et $g:\mathbb{R}\to \mathbb{R}$ deux
fonctions intégrables. Montrer que la fonction $\max(f, g)$ est
intégrable. ([Solution p.
`\pageref*{answer-im}`{=tex}](#answer-im){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Fonction d'ordre exponentiel ($\mathord{\bullet}$) {#foe .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Fonction d'ordre exponentiel}`{=latex}

Soit $f: \left[0, +\infty\right[ \to \mathbb{R}$ une fonction mesurable
pour laquelle il existe des constantes réelles $M$ et $\sigma$ telles
que $|f(t)| \leq M e^{\sigma t}$. Montrer que si $x \geq \sigma$ alors
l'application $t \in \left[0, +\infty\right[ \mapsto f(t)e^{-xt}$ est
intégrable. ([Solution p.
`\pageref*{answer-foe}`{=tex}](#answer-foe){.no-parenthesis}.)
:::

::: {.section}
### Proposition -- Ensemble mesurable {#ensemble-mesurable-1 .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Ensemble mesurable}`{=latex}

Un sous-ensemble $E$ de $\mathbb{R}$ est mesurable si et seulement si sa
fonction caractéristique $1_E$ est mesurable.
:::

::: {.section}
#### Démonstration {#démonstration-17 .proof}

Si l'ensemble $E$ est mesurable, pour tout $k\in \mathbb{N}$, l'ensemble
$E_k := E \cap [-k,k]$ est de longueur finie, c'est-à-dire que la
fonction $1_{E_k}$ est intégrable. La fonction $1_{E}$ est donc
mesurable car limite simple de fonctions intégrables.

Réciproquement, si une fonction caractéristique $1_E$ est mesurable, par
[le critère de l'image réciproque (p. `\pageref*{CIR}`{=tex})](#CIR),
comme $E = 1_{E}^{-1}(\{1\})$ et que le singleton $\{1\}$ est fermé, $E$
est mesurable.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Définition -- Intégrabilité sur un sous-ensemble {#intégrabilité-sur-un-sous-ensemble .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Intégrabilité sur un sous-ensemble}`{=latex}

Une fonction $f: \mathbb{R}\to \mathbb{R}$ est dite *intégrable sur un
sous-ensemble $E$ de $\mathbb{R}$* si la fonction $f 1_E$ est
intégrable. On note alors $$
\int_E f(t) \, dt := \int 1_E(t) f(t) \, dt.
$$
:::

::: {.section}
Cette définition est cohérente avec la définition existant déjà dans le
cas où $E$ est un intervalle de $\mathbb{R}$ (cf. "Calcul Intégral I").
:::

::: {.section}
### Corollaire -- Restriction à des ensembles mesurables {#restriction-à-des-ensembles-mesurables .corollary .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Restriction à des ensembles mesurables}`{=latex}

Une fonction $f:\mathbb{R}\to \mathbb{R}$ est intégrable si et seulement
si $f$ est intégrable sur $E$ pour tout ensemble mesurable $E$.
:::

::: {.section}
#### Démonstration {#démonstration-18 .proof}

Si $f$ est intégrable, elle est mesurable ; si l'ensemble $E$ est
mesurable, sa fonction caractéristique $1_E$ est également mesurable,
comme limite des $1_{E\cap[-k, k]}$ qui sont intégrables, et donc
mesurables. Par conséquent, le produit $f 1_E$ est mesurable, comme sa
valeur absolue $|f 1_E|$. Par ailleurs, comme $|1_E| \leq 1$, on a
$|f1_E| \leq |f|$. Par [le critère d'intégrabilité dominée (p.
`\pageref*{CID}`{=tex})](#CID), $f 1_E$ est donc intégrable.

Réciproquement, supposons $f 1_E$ intégrable pour tout ensemble
mesurable $E$. En prenant $E = \mathbb{R}$, on constate que $f$ est
nécessairement intégrable.`\hfill$\blacksquare$`{=latex}
:::
:::

::: {.section}
Annexe -- Intégrabilité conditionnelle
======================================

On utilise parfois le terme *conditionnellement intégrable* pour
qualifier les fonctions qui intégrables au sens de Henstock-Kurzweil
mais pas au sens de Lebesgue, car leur valeur absolue n'est pas
intégrable. Nous fournissons dans cette section l'exemple d'une telle
fonction, en démontrant que la fonction $f:[0, 1] \to \mathbb{R}$
définie par $$
f(x) = \frac{1}{x} \cos \frac{1}{x^2} \, \mbox{ si }\,  x > 0 \, \mbox{ et } \, f(0) = 0
$$ est conditionnellement intégrable.

![](images/f.py.pdf)\

Pour montrer qu'elle est intégrable au sens de Henstock-Kurzweil, nous
exploitons la forme générale du théorème fondamental du calcul (cf
"Calcul Intégral I"), appliqué à la fonction $g:[0, 1] \to \mathbb{R}$
définie par $$
g(x) = -\frac{x^2}{2} \sin \frac{1}{x^2} \, \mbox{ si }\,  x > 0 \, \mbox{ et } \, g(0) = 0.
$$ Cette fonction est dérivable en tout point de $[0,1]$ ; en $0$, sa
dérivée est nulle[^8] et quand $x>0$, $$
\left[-\frac{x^2}{2} \sin \frac{1}{x^2} \right]' +
x \sin \frac{1}{x^2} 
= \frac{1}{x} \cos \frac{1}{x^2}.
$$ Par [le critère d'intégrabilité dominée (p.
`\pageref*{CID}`{=tex})](#CID), la fonction $h(x)$ égale à
$x \sin (1/x^2)$ si $x>0$ et nulle en zéro est absolument intégrable car
continue sur $[0, 1]$. La fonction $g'$ étant également intégrable au
sens de Henstock-Kurzweil, $f = g' + h$ est intégrable au sens de
Henstock-Kurzweil comme somme de deux fonctions intégrables au sens de
Henstock-Kurzweil.

La fonction $f$ n'est pourtant pas intégrable au sens de Lebesgue, car
$h$ est intégrable au sens de Lebesgue mais pas $g'$. En effet, si
c'était le cas, toute fonction intégrable au sens de Lebesgue dont la
valeur absolue est majorée par $|g'|$ aurait par l'inégalité
triangulaire son intégrale majorée par celle de $|g'|$. Or nous allons
exhiber une suite de telles fonctions dont l'intégrale tend vers
$+\infty$, ce qui établira la contradiction.

Soit $k\geq 1$ un entier ; on définit la function
$\phi_k:[0,1] \to \mathbb{R}$ par $$
\phi_k(x) = 
\left|
\begin{array}{rl} 
g'(x) & \mbox{si } \, \alpha_j \leq x \leq \beta_j, \, 1 \leq j \leq k\\
0 & \mbox{sinon.}
\end{array}
\right.
$$ où $$
\alpha_j = \frac{1}{\sqrt{2\pi (j + 1/4)}}
\; \mbox{ et } \;
\beta_j = \frac{1}{\sqrt{2\pi(j - 1/4)}},
$$

L'idée sous-jacente est la suivante : les fonctions $\phi_k$ sont faites
pour coïncider avec $g'$ dans les plages de valeurs où $\cos 1/x^2$ est
positif ; comme $g'(x) = - x \sin {1}/{x^2} + (1/x)\cos {1} / {x^2}$, et
que pour $x$ petit, $1/x$ est grand devant $x$, cela correspond
approximativement aux plages où $g'(x)$ est positif.

![](images/g-prime.py.pdf)\

Par construction, $\phi_k$ est continue par morceaux et donc intégrable
au sens de Lebesgue, et bien telle que $|\phi_k| \leq |g'|$. Par
ailleurs, $$
\begin{split}
\int_0^1 \phi_k(t) \, dt &= \sum_{j=0}^k \int_{\alpha_j}^{\beta_k} \phi_k(t) \, dt \\
&=\sum_{j=0}^k \left[-\frac{x^2}{2} \sin \frac{1}{x^2} \right]_{\alpha_j}^{\beta_j} \\
&=\sum_{j=0}^k \left[-\frac{1}{4\pi(j-1/4)} \sin (2\pi(j-1/4)) \right. \\
&\phantom{=\sum_{j=0}^k \left[\right.} \left. +\frac{1}{4\pi(j+1/4)} \sin (2\pi(j+1/4)) \right] \\
&=\sum_{j=0}^k \frac{1}{4\pi}\left[\frac{1}{j-1/4} + \frac{1}{j+1/4}\right] \\
&= \frac{1}{2 \pi}\sum_{j=0}^k \frac{j}{j^2 + 1/16}. \\
\end{split}
$$ Comme la série associée à cette équation est divergente, on peut
rendre l'intégrale arbitrairement grande en choisissant un $k$
suffisamment grand, ce qui permet de conclure.
:::

::: {.section}
Exercices
=========

::: {.section}
Intégrale de Gauss
------------------

Source : @Swa01

On s'intéresse à la valeur de l'intégrale $$
I := \int_0^{+\infty} e^{-t^2} \, dt.
$$ On pose $$
g(x) := \int_0^x e^{-t^2} \, dt
\; \mbox{ et } \;
F(x) := \int_0^1 \frac{e^{-x(1+t^2)}}{1+t^2} \, dt.
$$

::: {.section}
#### Question 1 ($\mathord{\bullet}\mathord{\bullet}$) {#exp-m2-1 .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Montrer que $F$ est continue sur $\left[0, +\infty\right[$. Calculer
$F(0)$ et $\lim_{x \to +\infty} F(x)$. ([Solution p.
`\pageref*{answer-exp-m2-1}`{=tex}](#answer-exp-m2-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 ($\mathord{\bullet}\mathord{\bullet}$) {#exp-m2-2 .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Montrons que la fonction $F$ est dérivable sur $\left]0, +\infty\right[$
et que $$
F'(x) 
= -\frac{e^{-x}}{\sqrt{x}} g(\sqrt{x}).
$$

([Solution p.
`\pageref*{answer-exp-m2-2}`{=tex}](#answer-exp-m2-2){.no-parenthesis}.)
:::

::: {.section}
#### Question 3 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#exp-m2-3 .question .three .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Evaluer de deux façons différentes $$
\lim_{\varepsilon \to 0^+} F(\varepsilon^{-1}) - F(\varepsilon)
$$ et en conclure que $$
I =\frac{\sqrt{\pi}}{{2}}.
$$

([Solution p.
`\pageref*{answer-exp-m2-3}`{=tex}](#answer-exp-m2-3){.no-parenthesis}.)
:::
:::

::: {.section}
Théorème de convergence dominée
-------------------------------

::: {.section}
#### Question 1 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#exo-TCD .question .three .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Montrer que la conclusion [du théorème de convergence dominée (p.
`\pageref*{TCD}`{=tex})](#TCD) est toujours valide si les fonctions
$f_k$ ne satisfont les hypothèses de convergence et d'encadrement que
presque partout. ([Solution p.
`\pageref*{answer-exo-TCD}`{=tex}](#answer-exo-TCD){.no-parenthesis}.)
:::
:::

::: {.section}
Ensembles de longueur finie
---------------------------

::: {.section}
#### Question 1 ($\mathord{\bullet}$) {#lf .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Soit $A$ un ensemble mesurable de $\mathbb{R}$ pour lequel il existe une
constante $L$ (finie) telle que pour tout intervalle fermé borné
$[a, b]$, on ait $$
\int_a^b 1_A(t) \, dt \leq L.
$$

Montrer que $A$ est de longueur finie et que $\ell(A) \leq L$.
([Solution p.
`\pageref*{answer-lf}`{=tex}](#answer-lf){.no-parenthesis}.)
:::
:::

::: {.section}
Intégrabilité locale
--------------------

Une fonction $f: \mathbb{R}\to \mathbb{R}$ est dite *localement
intégrable* si tout point $x$ de $\mathbb{R}$, il existe un
$\varepsilon > 0$ et un intervalle $[x+\varepsilon, x+\varepsilon]$ où
la fonction $f$ soit intégrable.

::: {.section}
#### Question 0 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#il-0 .question .three .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 0}`{=latex}

Montrer que $f$ est localement intégrable si et seulement si pour tout
intervalle fermé borné $[a, b]$ de $\mathbb{R}$, $f$ est intégrable sur
$[a, b]$. ([Solution p.
`\pageref*{answer-il-0}`{=tex}](#answer-il-0){.no-parenthesis}.)
:::

::: {.section}
#### Question 1 ($\mathord{\bullet}$) {#il-1 .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Montrer que toute fonction localement intégrable est mesurable.
([Solution p.
`\pageref*{answer-il-1}`{=tex}](#answer-il-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 ($\mathord{\bullet}\mathord{\bullet}$) {#il-2 .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

La réciproque est-elle vraie ? ([Solution p.
`\pageref*{answer-il-2}`{=tex}](#answer-il-2){.no-parenthesis}.)
:::
:::

::: {.section}
Fonctions mesurables
--------------------

::: {.section}
#### Question 1 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#fm-1 .question .four .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Montrer qu'une fonction $f: \mathbb{R}\to \mathbb{R}$ est mesurable si
et seulement si pour tout nombre réel $a$, l'ensemble $$
f^{-1}(\left]-\infty, a\right]) = \{x \in \mathbb{R}\, | \, f(x) \leq a\}
$$ est mesurable. ([Solution p.
`\pageref*{answer-fm-1}`{=tex}](#answer-fm-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 ($\mathord{\bullet}\mathord{\bullet}$) {#fm-2 .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

En déduire qu'une fonction croissante $f: \mathbb{R}\to \mathbb{R}$ est
intégrable sur tout intervalle fermé borné. ([Solution p.
`\pageref*{answer-fm-2}`{=tex}](#answer-fm-2){.no-parenthesis}.)
:::
:::

::: {.section}
Composition de fonctions et mesurabilité
----------------------------------------

::: {.section}
#### Question 1 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#cfm .question .three .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Montrer que si la fonction $f:\mathbb{R}\to \mathbb{R}$ est mesurable et
que la fonction $g: \mathbb{R}\to \mathbb{R}$ est continue par morceaux,
alors la fonction composée $g \circ f$ est mesurable. ([Solution p.
`\pageref*{answer-cfm}`{=tex}](#answer-cfm){.no-parenthesis}.)
:::
:::

::: {.section}
Composition par une fonction lipschitzienne
-------------------------------------------

Soit $f:[0,1] \to \mathbb{R}$ et $g:\mathbb{R}\to \mathbb{R}$. On
suppose que $g$ et lipschitzienne, c'est-à-dire qu'il existe un $K\geq0$
tel que pour toute paire de réels $x$ et $y$ on ait
$|g(x) - g(y)| \leq K |x - y|$.

::: {.section}
#### Question 1 ($\mathord{\bullet}$) {#cfl-1 .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Si $f$ est mesurable est-ce que $g \circ f$ est mesurable ? ([Solution
p. `\pageref*{answer-cfl-1}`{=tex}](#answer-cfl-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 ($\mathord{\bullet}$) {#cfl-2 .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Si $f$ est intégrable, est-ce que $g \circ f$ est intégrable ?
([Solution p.
`\pageref*{answer-cfl-2}`{=tex}](#answer-cfl-2){.no-parenthesis}.)
:::
:::

::: {.section}
Formule de la moyenne
---------------------

Soit $f: U \subset \mathbb{R}^2 \to \mathbb{R}^2$ une fonction définie
sur un ensemble $U$ ouvert et supposée continûment différentiable. On
considère $c \in U$ et $R > 0$ tel que le disque fermé centré en $c$ et
de rayon $R$ soit inclus dans $U$; on définit alors la grandeur $I(r)$
pour tout $r \in [0, R] \to \mathbb{R}^2$ comme la valeur moyenne du
vecteur $f$ sur le cercle de rayon $c$ et de rayon $r$: $$
I(r) = \frac{1}{2\pi}\int_0^{2\pi} f(z_{\alpha, r}) \, d\alpha
\, \mbox{ où } \, 
z_{\alpha, r} = c + r (\cos \alpha, \sin \alpha).
$$

::: {.section}
#### Question 1 ($\mathord{\bullet}$) {#fmoy-1 .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Que vaut $I(0)$ ? ([Solution p.
`\pageref*{answer-fmoy-1}`{=tex}](#answer-fmoy-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#fmoy-2 .question .three .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Montrer que l'application $r \in [0, R] \mapsto I(r)$ est dérivable et
calculer $I'(r)$ pour tout $r \in [0, R]$. ([Solution p.
`\pageref*{answer-fmoy-2}`{=tex}](#answer-fmoy-2){.no-parenthesis}.)
:::

::: {.section}
#### Question 3 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#fmoy-3 .question .three .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

On suppose désormais que $f$ vérifie les conditions de Cauchy-Riemann en
tout point $(x, y)$ de $U$, c'est-à-dire que $$
    \partial_y f(x, y) = R(\pi/2) \cdot \partial_x f(x, y)
    $$ où $R(\alpha)$ désigne la rotation d'angle $\alpha$ centrée sur
l'origine. Simplifier l'expression de $I'(r)$ et conclure. Indication:
on pourra évaluer $\partial_{\alpha} (f(z_{\alpha, r}))$. ([Solution p.
`\pageref*{answer-fmoy-3}`{=tex}](#answer-fmoy-3){.no-parenthesis}.)
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
#### Défaut de domination {#answer-dd .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Défaut de domination}`{=latex}

On établit sans difficultés que pour tout $k \in \mathbb{N}$, $$
\int f_k(t)\, dt = \int_k^{k+1} dt = 1, 
$$ et donc $$
\lim_{k \to +\infty} \int f_k(t) \, dt  =1.
$$ D'autre part, pour tout $t \in \mathbb{R}$, on a $f_k(t) = 0$ si
$k > t$, donc $f_k(t) \to 0$ quand $k \to + \infty$ ; par conséquent, $$
\int \lim_{k \to +\infty} f_k(t) \, dt = 0.
$$ L'intégrale de la limite des $f_k$ diffère donc de la limite des
intégrales des $f_k$. Cela ne contredit pas [le théorème de convergence
dominée (p. `\pageref*{TCD}`{=tex})](#TCD) puisque nous n'avons pas
exhibé de fonction intégrable dominant les $f_k$ ; en l'occurence, une
fonction $g$ dominant toutes les $f_k$ vérifie nécessairement
$1 \leq g(t)$ pour tout $t \geq 0$, or aucune fonction de ce type n'est
intégrable.
:::

::: {.section}
#### Intégrale fonction d'un paramètre {#answer-ifp .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Intégrale fonction d'un paramètre}`{=latex}

Au préalable, on note que l'application $\arctan$ est continue et donc
intégrable sur $[0, 1]$ ; le théorème fondamental du calcul nous
garantit donc l'intégrabilité de sa primitive
$t \in [0, 1] \mapsto 1/(1+t^2)$ et nous fournit la valeur de son
intégrale : $$
\int_0^1 \frac{dt}{1+t^2}
=
\int_0^1 \arctan'(t) \, dt
=
\arctan(1) - \arctan(0) = \frac{\pi}{4} - 0 = \frac{\pi}{4}.
$$ De plus, pour tout $x \geq 0$ et tout $t\in [0, 1]$, on a
$|e^{-xt}| \leq 1$ ; pour toute suite de réels strictement positifs
$x_k$ tendant vers $0$, on a donc $$
\lim_{k\to +\infty} \frac{e^{-x_kt}}{1+t^2} = \frac{1}{1+t^2}  \mbox{ et } \;
\left| \frac{e^{-x_kt}}{1+t^2} \right| \leq 
 \frac{1}{1+t^2}.
$$ Si l'on introduit des prolongements des fonctions considérées par
zéro en dehors de $[0, 1]$, [le théorème de convergence dominée (p.
`\pageref*{TCD}`{=tex})](#TCD) nous fournit donc $$
\lim_{x \to 0^+} \int_0^1 \frac{e^{-xt}}{1+t^2} \, dt = 
\int_0^1 \frac{dt}{1+t^2} = \frac{\pi}{4}.
$$
:::

::: {.section}
#### Théorème fondamental du calcul {#answer-TCD .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Théorème fondamental du calcul}`{=latex}

Soit $[a_k, b_k]$ une suite d'intervalles fermés bornés de $\mathbb{R}$
tels que $[a_k, b_k] \subset [a, b]$ et tels que $a_k \to a$ et
$b_k \to b$ quand $k \to +\infty.$ Pour tout $k \in \mathbb{N}$, la
fonction $g_k$ définie par $$
g_k(t) = \left| 
\begin{array}{rl}
f'(t) & \mbox{si $t \in [a_k, b_k]$,} \\
0 & \mbox{sinon.}
\end{array}
\right.
$$ est intégrable car $f'|_{[a_k, b_k]}$ est intégrable par
restriction ; la suite des $g_k$ est dominée par la fonction valant
$|f'|$ sur $\left]a, b\right[$ et $0$ en dehors, fonction qui est
intégrable par additivité. De plus la suite des $g_k$ converge
simplement vers la fonction égale à $f'$ sur $\left]a, b\right[$ et
nulle en dehors. Appliquer le théorème fondamental du calcul à
$f'|_{[a_k, b_k]}$ donne par ailleurs $$
\int_{-\infty}^{+\infty} g_k(t) \, dt = \int_{a_k}^{b_k} f'(t) \, dt = f(b_k) - f(a_k).
$$ Par application [du théorème de convergence dominée (p.
`\pageref*{TCD}`{=tex})](#TCD), on obtient donc $$
\int_a^b f'(t) \, dt = \int g(t)\, dt = \lim_{k \to +\infty}  \int g_k(t) \, dt,
$$ donc $$
\int_a^b f'(t) \, dt  = \lim_{k\to+\infty} f(b_k) - f(a_k)
=f(b) - f(a).
$$
:::

::: {.section}
#### Fonctions puissance {#answer-power .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Fonctions puissance}`{=latex}

Pour tout $x \in \left[1, +\infty\right[$, si $\alpha \neq {-1}$, on a
$$
\int_1^x t^{\alpha} \, dt = \left[\frac{t^{\alpha+1}}{\alpha + 1} \right]_1^x
=\frac{x^{\alpha+1}}{\alpha + 1} - \frac{1}{\alpha + 1},
$$ et pour $\alpha = -1$, $$
\int_1^x t^{-1} \, dt = [\ln t]_1^x =\ln x.
$$ Si nous définissons les fonctions $f_k :\mathbb{R}\to \mathbb{R}$
pour $k \geq 1$ par $$
f_k(t) = \left|
\begin{array}{rl}
t^{\alpha} & \mbox{si $t \in [1, k]$,} \\
0 & \mbox{sinon.}
\end{array}
\right.
$$ alors $$
\lim_{k \to +\infty} \int f_k(t) \, dt = \lim_{k \to +\infty} \int_1^k t^{\alpha} \, dt,
$$ donc cette limite est finie si et seulement si $\alpha < -1$. Comme
la suite des fonctions $f_k$ est croissante et converge simplement vers
la fonction égale à $t \mapsto t^{\alpha}$ sur
$\left[1, +\infty \right[$ et nulle ailleurs, nous en déduisons par [le
théorème de convergence monotone (p. `\pageref*{TCM}`{=tex})](#TCM) que
la fonction $t \in \left[1, +\infty\right[ \mapsto t^{\alpha}$ est
intégrable si et seulement si $\alpha < -1$. Le cas de la fonction
puissance sur l'intervalle $\left]0,1\right]$ peut être analysé de façon
similaire, ou bien en pratiquant le changement de variable
$t \mapsto 1/t$ pour se ramener à l'intervalle que nous avons déjà
étudié.
:::

::: {.section}
#### Intégrabilité et intégrales impropres {#answer-iii .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Intégrabilité et intégrales impropres}`{=latex}

Si une fonction $f: \mathbb{R}\to \mathbb{R}$ est intégrable sur tout
intervalle fermé borné de $\mathbb{R}$, alors la suite
$|f_k|: \mathbb{R}\to \mathbb{R}$ des restrictions de $|f|$ à $[-k, k]$
prolongées par zéro à $\mathbb{R}$ est croissante, composée de fonctions
intégrables, et sa limite est la fonction $|f|$. Par [le théorème de
convergence monotone (p. `\pageref*{TCM}`{=tex})](#TCM), on a donc $$
\lim_{k \to +\infty} \int_{k}^k |f(t)| \, dt = \int  |f(t)| \, dt
$$ si la limite du membre de gauche est finie. La fonction $|f|$ est
alors intégrable ; elle domine les fonctions $f_k$ qui convergent
simplement vers $f$, donc $f$ est également intégrable par [le théorème
de convergence dominée (p. `\pageref*{TCD}`{=tex})](#TCD).

Réciproquement, si $$
\lim_{k \to +\infty} \int_{-k}^k |f(t)| \, dt = +\infty,
$$ [le théorème de convergence monotone (p.
`\pageref*{TCM}`{=tex})](#TCM) prouve que la fonction $|f|$ n'est pas
intégrable et donc que $f$ n'est pas intégrable.
:::

::: {.section}
#### Ensemble de longueur finie I {#answer-elfI .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Ensemble de longueur finie I}`{=latex}

La fonction caractéristique $1_E$ est égale presque partout à la
fonction $1_{[-1, 1]}$ qui est intégrable et satisfait $$
\int 1_{[-1, 1]}(t) \, dt = \int_{-1}^1 \, dt  =2.
$$ L'ensemble $E$ est donc de longueur finie égale à $2$.
:::

::: {.section}
#### Ensemble de longueur finie II {#answer-elfII .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Ensemble de longueur finie II}`{=latex}

La fonction caractéristique $1_{\mathbb{Q}}$ est nulle presque partout
puisque $\mathbb{Q}$ est dénombrable. Elle est donc intégrable
d'intégral nulle ; l'ensemble des rationnels $\mathbb{Q}$ est donc de
longueur nulle.
:::

::: {.section}
#### Ensemble de longueur finie III {#answer-elfIII .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Ensemble de longueur finie III}`{=latex}

La fonction caractéristique $f = 1_E$ est la limite de la suite
croissante de fonctions
$f_j = 1_{\cup_{k=0}^j \left[k, k+2^{-k} \right[}$. Comme par linéarité
de l'intégrale on a $$
\int f_j(t) \, dt = \sum_{k=0}^j \int 1_{\left[k, k+2^{-k} \right[}(1) \, dt
= \sum_{k=0}^j \int_k^{k+2^{-k}} \, dt
= \sum_{k=0}^j 2^{-k} = 2 - 2^{-j},
$$ par [le théorème de convergence monotone (p.
`\pageref*{TCM}`{=tex})](#TCM), la fonction $1_E$ est intégrable et $$
\ell(E) = \int 1_E(t) \, dt = 2.
$$
:::

::: {.section}
#### La longueur est additive {#answer-la .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{La longueur est additive}`{=latex}

Si $A$ et $B$ sont deux ensembles de $\mathbb{R}$ disjoints et de
longueur finie, alors $1_{A\cup B} = 1_A + 1_B$ donc $A\cup B$ est de
longueur finie par linéarité de l'intégrale et $$
\ell(A \cup B) = \int 1_{A \cup B}(t) \, dt =
\int 1_A(t) \, dt + \int 1_B(t) \, dt =
\ell(A) + \ell(B).
$$ Si $A$ et $B$ sont mesurables et disjoints, alors sur tout intervalle
fermé borné $[a, b]$ de $\mathbb{R}$, comme $$
1_{(A \cup B) \cap [a, b]} = 1_{A \cap [a, b]} + 1_{B \cap [a, b]},
$$ $A \cup B$ est mesurable. Si l'un des ensembles $A$ et $B$ au moins a
une longueur infinie, disons $A$ par exemple, alors par [le théorème de
convergence monotone (p. `\pageref*{TCM}`{=tex})](#TCM), on a $$
\int_{-k}^k 1_A(t) \, dt \to +\infty \; \mbox{ quand } \; k \to +\infty.
$$ Par conséquent, $$
\int_{-k}^k 1_A(t) \, dt \leq \int_{-k}^k 1_{A \cup B}(t) \, dt \to +\infty \; \mbox{ quand } \; k \to +\infty
$$ et donc dans ce cas aussi on a donc
$\ell(A \cup B) = \ell(A) + \ell(B)$.
:::

::: {.section}
#### Suite d'ensembles {#answer-sde .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Suite d'ensembles}`{=latex}

Il suffit de réaliser que d'après leur définition, $$
B = \bigcup_{k_0=0}^{+\infty} \bigcap_{k=k_0}^{+\infty} A_k
\; \mbox{ et } \;
C = \bigcap_{k_0=0}^{+\infty} \bigcup_{k=k_0}^{+\infty} A_k
$$ puis d'invoquer la stabilité des ensembles mesurables [par union
dénombrable (p. `\pageref*{pptuxe9s-tribu}`{=tex})](#pptés-tribu) et
[intersection dénombrable (p. `\pageref*{IEM}`{=tex})](#IEM).
:::

::: {.section}
#### Ni ouvert ni fermé {#answer-nonf .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Ni ouvert ni fermé}`{=latex}

L'ensemble $E= \left[0, 1\right[$ n'est ni ouvert ni fermé : $0$ est un
point frontière qui appartient à $E$ donc $E$ n'est pas ouvert et $1$
est un point frontière de $E$ qui n'appartient pas à $E$ donc $E$ n'est
pas fermé. Mais $E = [0, 1] \setminus \{0\}$ donc l'ensemble est le
complémentaire d'un ensemble fermé dans un autre ensemble fermé ; or
[les ensembles fermés sont mesurables (p. `\pageref*{OSM}`{=tex})](#OSM)
et [le complémentaire relatif de deux ensembles mesurables est mesurable
(p. `\pageref*{CR}`{=tex})](#CR), donc $E$ est mesurable.
:::

::: {.section}
#### Fonctions continues {#answer-fcm .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Fonctions continues}`{=latex}

L'image réciproque de tout fermé par une application continue
$f:\mathbb{R}\to \mathbb{R}^m$ est fermé. Comme [tout fermé est
mesurable (p. `\pageref*{OSM}`{=tex})](#OSM), [le critère de l'image
réciproque (p. `\pageref*{CIR}`{=tex})](#CIR) prouve qu'une telle
fonction continue est mesurable.
:::

::: {.section}
#### Image réciproque d'un intervalle {#answer-iri .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Image réciproque d'un intervalle}`{=latex}

Tout intervalle de $\mathbb{R}$ peut être décomposé comme l'union
(disjointe) d'un ouvert $U$ et d'un ensemble fermé $F$ (composé de 0, 1
ou 2 points) ; comme [ensembles ouverts ou fermés sont mesurables (p.
`\pageref*{OSM}`{=tex})](#OSM), il est donc mesurable et [son image
réciproque par $f$ est donc mesurable (p.
`\pageref*{CIR}`{=tex})](#CIR).
:::

::: {.section}
#### Intégrabilité du produit {#answer-ip .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Intégrabilité du produit}`{=latex}

Les produits $fg$ est mesurable comme [produit de fonctions mesurables
(p. `\pageref*{prod}`{=tex})](#prod) ; [la fonction $|fg|$ est donc
également mesurable (p. `\pageref*{abs}`{=tex})](#abs). De plus, pour
tout $x \in \mathbb{R}$, comme $(|f(x)| + |g(x)|)^2 \geq 0,$ $$
|fg|(x) \leq \frac{1}{2} f(x)^2 + \frac{1}{2} g(x)^2.
$$ Par le [critère d'intégrabilité dominée (p.
`\pageref*{CID}`{=tex})](#CID), $fg$ est donc intégrable.
:::

::: {.section}
#### Intégrabilité du maximum {#answer-im .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Intégrabilité du maximum}`{=latex}

Les fonctions $f$ et $g$ étant intégrables, elles sont mesurables. Par
[composition avec une fonction continue (p.
`\pageref*{CFC}`{=tex})](#CFC), $\max(f, g)$ est également mesurable.

De plus, on a $|\max(f, g)| \leq |f| + |g|$. La fonction $|\max(f, g)|$
est donc dominée par une fonction intégrable ; par le [critère
d'intégrabilité dominée (p. `\pageref*{CID}`{=tex})](#CID), $\max(f, g)$
est donc intégrable.
:::

::: {.section}
#### Fonction d'ordre exponentiel {#answer-foe .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Fonction d'ordre exponentiel}`{=latex}

La fonction $t \in \left[0, +\infty\right[ \mapsto f(t)e^{-xt}$ est
mesurable comme produit de fonctions mesurables. De plus, $$
|f(t)e^{-xt}| \leq M e^{-\varepsilon t} \; \mbox{ avec } \; \varepsilon = x - \sigma > 0,
$$ La fonction $t \mapsto M e^{-\varepsilon t}$ étant intégrable
(intégrer la fonction sur un intervalle borné, puis passer à la limite
par le [le théorème de convergence monotone (p.
`\pageref*{TCM}`{=tex})](#TCM)), la fonction
$t \in \left[0, +\infty\right[ \mapsto f(t)e^{-xt}$ est intégrable par
[le critère d'intégrabilité dominée (p. `\pageref*{CID}`{=tex})](#CID).
:::
:::

::: {.section}
Intégrale de Gauss
------------------

::: {.section}
#### Question 1 {#answer-exp-m2-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

$$
F(x) = \int_0^1 \frac{e^{-x(1+t^2)}}{1+t^2} \, dt
$$

$$
F(0)= \int_0^1 \frac{dt}{1+t^2}  =[\arctan]^1_0 = \frac{\pi}{4}.
$$

La fonction $F$ est continue sur $\left[0, +\infty\right[$. En effet, si
$x_0 \in \left[0, +\infty\right[$, alors $$
\frac{e^{-x(1+t^2)}}{1+t^2} \to \frac{e^{-x_0(1+t^2)}}{1+t^2}
\; \mbox{ quand } \, x \to x_0.
$$ De plus pour tout $x \in \left[0, +\infty\right[$, $$
\left|\frac{e^{-x(1+t^2)}}{1+t^2}\right| 
\leq 
\frac{1}{1+t^2}
$$ Le second membre de cette équation étant intégrable (il est
intégrable sur tout intervalle fermé borné et décroit quand
$t\to +\infty$ comme $1/t^2$), par [le théorème de convergence dominée
(p. `\pageref*{TCD}`{=tex})](#TCD), $$
F(x) \to F(x_0) \; \mbox{ quand } \; x \to x_0.
$$ De plus, toujours par le théorème de convergence dominée (avec la
même domination), on obtient $$
\lim_{x \to +\infty} F(x) =  \int_0^1 \lim_{x \to +\infty} \frac{e^{-x(1+t^2)}}{1+t^2}\, dt =
\int_0^1 0 \, dt =0.
$$
:::

::: {.section}
#### Question 2 {#answer-exp-m2-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Montrons que la fonction $F$ est dérivable sur
$\left]0, +\infty\right[$. Soit $\varepsilon > 0$ ; la fonction $$
x \in \left]\varepsilon ,+\infty\right[ \mapsto \frac{e^{-x(1+t^2)}}{1+t^2}
$$ est dérivable en tout $x$, de dérivée égale à $-e^{-x(1+t^2)}$, qui
est dominée par $e^{-\varepsilon/(1+t^2)}$. La fonction
$t \in [0, 1] \mapsto e^{-\varepsilon/(1+t^2)}$ est intégrable car
continue. Par [le théorème de dérivation sous le signe somme (p.
`\pageref*{DSS}`{=tex})](#DSS), on a donc $$
F'(x) = -\int_0^1 e^{-x(1+t^2)} \, dt 
$$ quand $x > \varepsilon$ et donc quand $x > 0$ puisque
$\varepsilon > 0$ est arbitraire. Avec
$g : \left[0, +\infty\right[ \mapsto \mathbb{R}$ définie par $$
g(x) = \int_0^x e^{-t^2} \, dt,
$$ pour tout $x > 0$, on a donc $$
F'(x) = -\int_0^1 e^{-x} e^{-x t^2} \, dt
= -e^{-x} \int_0^1  e^{-x t^2} \, dt,
$$ soit avec le changement de variable $u = \sqrt{x} t$, $$
F'(x) 
= -\frac{e^{-x}}{\sqrt{x}} \int_0^{\sqrt{x}}  e^{-u^2} \, du
= -\frac{e^{-x}}{\sqrt{x}} g(\sqrt{x}).
$$
:::

::: {.section}
#### Question 3 {#answer-exp-m2-3 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

On a d'une part par le théorème fondamental du calcul et les résultats
de la question 1 $$
\int_{\varepsilon}^{\varepsilon^{-1}} F'(x) \, dx
= F(\varepsilon^{-1}) - F(\varepsilon) \to - \frac{\pi}{4}
\; \mbox{ quand }  \; \varepsilon \to 0^+,
$$ et d'autre part avec l'expression de la question 2 de $F'$ et le
changement de variable $x=\sqrt{t}$, on obtient `\begin{align*}
\int_{\varepsilon}^{\varepsilon^{-1}} F'(x) \, dx
&= - \int_{\varepsilon}^{\varepsilon^{-1}} \frac{e^{-x}}{\sqrt{x}} g(\sqrt{x}) \, dx \\
&= - 2 \int_{\varepsilon}^{\varepsilon^{-1}} e^{-\sqrt{x}^2}g(\sqrt{x}) \, \frac{dx}{2\sqrt{x}} \\
&=- 2 \int_{\sqrt{\varepsilon}}^{1/\sqrt{\varepsilon}} {e^{-u^2}} g(u) \, du \\
&= - \int_{\sqrt{\varepsilon}}^{1/\sqrt{\varepsilon}} 2g'(u) g(u) \, du \\
&= - \int_{\sqrt{\varepsilon}}^{1/\sqrt{\varepsilon}} ((g(u))^2)' \, du \\
&= - \left[(g(u))^2\right]_{\sqrt{\varepsilon}}^{1/\sqrt{\varepsilon}} \\
&= -\left(g\left(1/\sqrt{\varepsilon}\right)\right)^2 + \left(g\left(\sqrt{\varepsilon}\right)\right)^2
\end{align*}`{=tex} et donc $$
\int_{\varepsilon}^{\varepsilon^{-1}} F'(x) \, dx
\to -  \left(\int_0^{+\infty} e^{-t^2} \, dt \right)^2
\; \mbox{ quand }  \; \varepsilon \to 0^+.
$$ On conclut finalement que $$
\int_0^{+\infty} e^{-t^2} \, dt = \sqrt{\frac{\pi}{4}} = \frac{\sqrt{\pi}}{{2}}.
$$
:::
:::

::: {.section}
Théorème de convergence dominée
-------------------------------

::: {.section}
#### Question 1 {#answer-exo-TCD .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Imaginons que les fonctions mesurables $f_k$ convergent vers la fonction
$f$ sur $\mathbb{R}\setminus A$ où $A$ est négligeable, et satisfont
$g \leq f_k \leq h$ sur l'ensemble $\mathbb{R}\setminus B_k$ où $B_k$
est négligeable.

Alors l'ensemble $C := A \cup (\cup_{k=1}^{+\infty} B_k)$ est
négligeable, comme on l'a montré dans l'exercice "Union d'ensembles
négligeables" du chapitre précédent. On peut aussi s'en convaincre avec
le calcul intégral : $A$ et les $B_k$ [sont négligeables, donc
mesurables et de longueur nulle (p.
`\pageref*{nuxe9gligeable-longueur-nulle}`{=tex})](#négligeable-longueur-nulle) ;
la suite des $C_j := A \cup (\cup_{k=1}^{j} B_k)$ est composée
d'ensemble mesurables, croissante et comme $$
1_{C_j} = 1_{A \cup (\cup_{k=1}^j B_k)} \leq 1_A + \sum_{k=1}^j 1_{B_k},
$$ on a $$
\int 1_{C_j}(x) \,dx \leq \int 1_A(x) \, dx + \sum_{k=1}^j \int 1_{B_k}(x) \,dx = 
\ell(A) + \sum_{k=1}^j \ell(B_k) = 0. 
$$ Par [le théorème de convergence monotone (p.
`\pageref*{TCM}`{=tex})](#TCM), $$
\ell(C) = \int 1_{C}(x) \,dx = \lim_{j\to +\infty} \int 1_{C_j}(x) \,dx = 0.
$$ L'ensemble $C$ [est de longueur nulle et donc négligeable (p.
`\pageref*{nuxe9gligeable-longueur-nulle}`{=tex})](#négligeable-longueur-nulle).

Sachant que $C$ est négligeable, c'est-à-dire mesurable et de longueur
nulle, il suffit alors de rédéfinir chaque fonction $f_k$, $f$, $g$ et
$h$ pour leur assigner la valeur $0$ en tout $x \in C$ ; cette opération
ne change pas leur caractère mesurable ou intégrable, ni la valeur des
intégrales associées. Et les nouvelles fonctions satisfont partout les
hypothèses de convergence et d'encadrement du [théorème de convergence
dominée (p. `\pageref*{TCD}`{=tex})](#TCD). On peut donc conclure sous
les hypothèses plus faibles considérées dans cet exercice.
:::
:::

::: {.section}
Ensembles de longueur finie
---------------------------

::: {.section}
#### Question 1 {#answer-lf .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

La suite des fonctions $f_k:\mathbb{R}\to \mathbb{R}$ définie par $$
f_k(t) = \left|
\begin{array}{rl}
1_A(t) & \mbox{si } \, t \in [-k, k], \\
0      & \mbox{sinon.}
\end{array}
\right.
$$ est croissante, de limite simple $1_A$. A tout rang $k$, on a $$
\int f_k(t) \, dt 
=
\int_{-k}^k 1_A(t) \, dt
\leq L,
$$ donc $$
\sup_k \int f_k(t) \, dt 
\leq 
L < +\infty. 
$$ [Le théorème de convergence monotone (p.
`\pageref*{TCM}`{=tex})](#TCM) nous garantit l'intégrabilité de $1_A$ --
c'est-à-dire le fait que $A$ est de longueur finie -- et fournit $$
\ell(A) = \int 1_A(t) \, dt = 
\lim_{k\to +\infty} \int f_k(t) \, dt
\leq L.
$$
:::
:::

::: {.section}
Intégrabilité locale
--------------------

::: {.section}
#### Question 0 {#answer-il-0 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 0}`{=latex}

De toute évidence, si $f$ est intégrable sur tout intervalle fermé
borné, elle est intégrable sur tous les intervalles de la forme
$[x - \varepsilon, x+\varepsilon]$.

Réciproquement, supposons que pour tout $x$ il existe un
$\varepsilon > 0$ tel que $f$ soit intégrable sur
$[x - \varepsilon, x + \varepsilon]$. Si la fonction $f$ n'est pas
intégrable sur $[a, b]$, par additivité c'est qu'elle n'est pas
intégrable sur $[a, (a+b)/2]$ ou sur $[(a+b)/2, b]$ (voire sur les deux
sous-ensembles). En procédant par récurrence, on construit ainsi une
suite d'intervalles fermés emboités $[a_k, b_k]$, indexés par l'entier
$k$, avec $[a_0, b_0] = [a, b]$, de longueur $(b-a)/2^k$ où la fonction
$f$ n'est pas intégrable. La suite des points centraux $(a_k+b_k)/2$
étant de Cauchy, elle a une limite $x$ appartenant à tous ces
intervalles fermés ; pour $k$ assez grand, on a
$I_k \subset [x -\varepsilon, x+\varepsilon]$. Par restriction, $f$
devrait donc être intégrable sur $I_k$, d'où une contradiction ; $f$ est
donc intégrable sur $[a, b]$.
:::

::: {.section}
#### Question 1 {#answer-il-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Une fonction $f$ localement intégrable est intégrable sur tout
intervalle de la forme $[-k, k]$ où $k \in \mathbb{N}$ par [le résultat
de la question 0 (p. `\pageref*{il-0}`{=tex})](#il-0). La fonction $f$
étant la limite simple des fonctions $f_k = 1_{[-k, k]} f$, elle est
mesurable.
:::

::: {.section}
#### Question 2 {#answer-il-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

La réciproque est fausse. Par exemple, la fonction $f$ définie par $$
f(x) = 
\left|
\begin{array}{cc}
1/x^2 & \mbox{si } x \neq 0, \\
0     & \mbox{si } x = 0
\end{array}
\right.
$$ est mesurable ; c'est par exemple la limite des fonctions intégrables
$$
f_k(x) = 
\left|
\begin{array}{cl}
1/x^2     & \mbox{si } |x| \geq 2^{-k}, \\
0 & \mbox{si } |x| < 2^{-k}, \\
\end{array}
\right.
$$ Mais elle n'est intégrable sur $[-\varepsilon, \varepsilon]$ pour
aucun $\varepsilon > 0$. En effet, quand $2^{-k} \leq \varepsilon$, on a
$$
\begin{split}
\int_{-\varepsilon}^{\varepsilon} f_k(x) \, dx 
&= \int_{-\varepsilon}^{-2^{-k}} \frac{dx}{x^2} + \int_{2^{-k}}^{\varepsilon} \frac{dx}{x^2} \\
&= \left[ -\frac{1}{x} \right]_{-\varepsilon}^{-2^{-k}} + \left[ -\frac{1}{x}\right]_{2^{-k}}^{\varepsilon} \\
&= (2^k - 1/\varepsilon) + (2^k - 1/\varepsilon) = 2^{k+1} - 2/\varepsilon.
\end{split}
$$ Cette grandeur tendant vers $+\infty$ quand $k \to +\infty$, [le
théorème de convergence monotone (p. `\pageref*{TCM}`{=tex})](#TCM) nous
garantit que la fonction $f$ n'est pas intégrable sur
$[-\varepsilon, \varepsilon]$.
:::
:::

::: {.section}
Fonction mesurables
-------------------

::: {.section}
#### Question 1 {#answer-fm-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Compte tenu du [critère de l'image réciproque (p.
`\pageref*{CIR}`{=tex})](#CIR), comme tous les ensembles
$\left]-\infty, a\right]$ sont fermés, le critère de l'énoncé est bien
vérifié pour toute fonction mesurable.

Montrons désormais la réciproque. Supposons le critère de l'énoncé
vérifié et soit $U$ un ouvert de $\mathbb{R}$ ; l'ensemble $U$ peut être
décomposé comme union dénombrable d'intervalles ouverts bornés $I_k$ de
$\mathbb{R}$. Par conséquent, comme $$
f^{-1}(U) = f^{-1} \left(\cup_k I_k \right) = \bigcup_{k} f^{-1}(I_k),
$$ il nous suffit de montrer que l'image réciproque de tout intervalle
ouvert borné $\left]a, b\right[$ par $f$ est mesurable, pour conclure
que $f^{-1}(U)$ est mesurable, comme union dénombrable d'ensembles
mesurables.

Or, un point $x$ vérifie $a < f(x) < b$ si et seulement il ne vérifie
pas $f(x) \leq a$ et vérifie $f(x) \leq b - 2^{-k}$ pour au moins un
entier $k$, ce qui se traduit par la relation ensembliste $$
f^{-1}(\left]a, b\right[) 
= 
\left(\mathbb{R}\setminus
f^{-1}(\left]-\infty,a \right]) \right) 
\cap 
\left( \bigcup_{k=0}^{+\infty} f^{-1}(\left]-\infty, b -2^{-k}\right])\right).
$$ Les images réciproques au second membre sont mesurables par
hypothèse, et sont combinées par complément, union dénombrable et
intersection, par conséquent $f^{-1}(\left]a, b\right[)$ est également
mesurable. Le [critère de l'image réciproque (p.
`\pageref*{CIR}`{=tex})](#CIR) pour la mesurabilité de $f$ est donc bien
vérifié.
:::

::: {.section}
#### Question 2 {#answer-fm-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Si la fonction $f: \mathbb{R}\to \mathbb{R}$ est croissante, les images
réciproques des ensembles de la forme $\left]-\infty,a \right]$ sont des
intervalles. En effet, si $f(x) \leq a$ et $f(y) \leq a$ et $x \leq y$,
pour tout point intermédiaire $x \leq z \leq y$, $f(z) \leq a$. Par
conséquent, $f$ est mesurable.

De plus, $f$ étant croissante, pour tout intervalle fermé borné $[a, b]$
et tout $x \in [a, b]$, on a $f(a) \leq f(x) \leq f(b)$. Par le [critère
d'intégrabilité dominée (p. `\pageref*{CID}`{=tex})](#CID), $f$ est
intégrable sur $[a, b]$.
:::
:::

::: {.section}
Composition de fonctions et mesurabilité
----------------------------------------

::: {.section}
#### Question 1 {#answer-cfm .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Soient
$\dots \leq a_{-k} \leq \dots \leq a_{-1} \leq a_0 \leq a_1 \leq \dots \leq a_k$
des nombres réels tels que la fonction $g$ soit continue sur chaque
intervalle ouvert $\left]a_j, a_{j+1} \right[$. Soit $U$ un ouvert de
$\mathbb{R}$ ; alors pour tout $j$, si $g_j$ désigne la restriction de
$g$ à $\left]a_j, a_{j+1} \right[$, par continuité de $g_j$, l'image
réciproque $V_j = g_j^{-1}(U)$ est ouverte dans
$\left]a_j, a_{j+1} \right[$ et donc dans $\mathbb{R}$. L'image
réciproque de $U$ par $g$ est donc la réunion $V$ de ces ouverts,
c'est-à-dire un ouvert, et éventuellement d'un sous-ensemble $N$ des
$\{a_k\}$ qui est nécessairement dénombrable, donc mesurable (et de
longueur nulle).

L'image réciproque de $U$ par $g\circ f$ est donc l'image réciproque de
$V \cup N$ par $f$. La fonction $f$ étant mesurable, $f^{-1}(V)$ et
$f^{-1}(N)$ sont mesurables, ainsi que
$f^{-1}(V \cup N) = f^{-1}(V) \cup f^{-1}(N)$. La fonction composée
$g \circ f$ est donc mesurable.
:::
:::

::: {.section}
Composition par une fonction lipschitzienne
-------------------------------------------

::: {.section}
#### Question 1 {#answer-cfl-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Oui, car toute fonction lipschitzienne est continue ; $g \circ f$ est
donc mesurable comme [composée d'une fonction mesurable et d'une
fonction continue (p. `\pageref*{CFC}`{=tex})](#CFC).
:::

::: {.section}
#### Question 2 {#answer-cfl-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Oui. D'une part, $f$ étant intégrable, elle est mesurable et donc par la
question 1, la composée $g \circ f$ est mesurable. D'autre part, pour
tout $x \in [0,1]$, on a $$
|g \circ f(x) - g \circ f(0)| \leq K |f(x) - f(0)|
$$ et donc $$
|g \circ f(x)| \leq K |f(x)| + (K |f(0)| + |g \circ f(0)|)
$$ Le membre de droite de cette inégalité est une fonction intégrable
sur $[0, 1]$, donc par [le critère d'intégrabilité dominée (p.
`\pageref*{CID}`{=tex})](#CID), la fonction $g \circ f$ est intégrable.
:::
:::

::: {.section}
Formule de la moyenne
---------------------

::: {.section}
#### Question 1 {#answer-fmoy-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

On a $$
I(0) = \frac{1}{2\pi}\int_0^{2\pi} f(c_1, c_2) \, d\alpha = f(c_1, c_2) = f(c).
$$
:::

::: {.section}
#### Question 2 {#answer-fmoy-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Formons le taux d'accroissement de $I$ en $r$, pour une variation de
l'argument $h$ telle que $r + h \in [0, R]$. On a $$
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
$$ La fonction $g_{\alpha}: r \mapsto f(z_{\alpha, r})$ étant
différentiable pour tout $\alpha$, on a $$
\begin{split}
\lim_{h \to 0} \frac{f(z_{r+h, \alpha}) - f(z_{\alpha, r})}{h}
&= \frac{d}{dr} f(z_{\alpha, r}) \\ 
&= df(z_{r, \alpha}) \cdot (\cos \alpha, \sin \alpha) \\
&= \partial_x f (z_{r, \alpha}) \cos \alpha 
+ \partial_y f (z_{r, \alpha}) \sin \alpha.
\end{split}.
$$ De plus, par le théorème des accroissements finis, $$
\left\| \frac{g_{\alpha}(r+h) - g_{\alpha}(r)}{h} \right\|
\leq
\sup_{r \in [0, R]} \left\| \frac{d}{dr} g_{\alpha}(r) \right\|
$$ où le sup du membre de droite est bien fini puisque
$dg_{\alpha}(r)/dr$ est une fonction continue du couple $(\alpha, r)$
qui appartient à l'ensemble fermé borné $[0, 2\pi] \times [0, R]$. Par
conséquent, pour toute suite $h_k$ tendant vers $0$ et telle que
$r+h_k \in [0, R]$, la suite des $$
\frac{g_{\alpha}(r+h_k) - g_{\alpha}(r)}{h_k}
$$ associée converge simplement vers $$
\partial_x f (z_{r, \alpha}) \cos \alpha 
+ \partial_y f (z_{r, \alpha}) \sin \alpha
$$ et chacune des composantes de ce vecteur de $\mathbb{R}^2$ est bornée
par la fonction intégrable (constante) $$
\alpha \in [0, 2\pi] \mapsto \sup_{r \in [0, R]} \left\| \frac{d}{dr} g_{\alpha}(r) \right\|.
$$ Par conséquent, par le théorème de convergence dominée, la dérivée de
$I$ est définie en tout point $r$ et est donnée par $$
I'(r)
= \frac{1}{2\pi}\int_{0}^{2\pi} 
  \left(
  \partial_x f (z_{r, \alpha}) \cos \alpha 
  + \partial_y f (z_{r, \alpha}) \sin \alpha
  \right) \, d\alpha.
$$
:::

::: {.section}
#### Question 3 {#answer-fmoy-3 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Evaluons la dérivée par rapport à $\alpha$ de $f(z_{\alpha, r})$. On a
$$
\begin{split}
\partial_{\alpha} (f(z_{\alpha, r}))
&=
\partial_{\alpha} (f(c_1 + r \cos \alpha, c_2 + r \sin \alpha)) \\
&= \partial_x f(z_{\alpha, r}) (- r\sin \alpha)
+ \partial_y f(z_{\alpha, r}) (r\cos \alpha).
\end{split}
$$ Comme
$\partial_y f(z_{\alpha, r}) = R(\pi/2) \partial_x f(z_{\alpha, r})$, on
en déduit que $$
\begin{split}
\partial_{\alpha} (f(z_{\alpha, r}))
&= r(- \sin \alpha \times I + \cos \alpha  \times R(\pi/2)) \cdot \partial_x f(z_{\alpha, r}) \\
& = r R(\pi/2 + \alpha) \cdot \partial_x f(z_{\alpha, r}) \\
& = r R(\pi/2) R(\alpha) \cdot \partial_x f(z_{\alpha, r})
\end{split}
$$ D'un autre coté, l'intégrande dans l'expression de $I'(r)$ s'écrit $$
\begin{split}
\partial_x f (z_{r, \alpha}) \cos \alpha 
+ 
\partial_y f (z_{r, \alpha}) \sin \alpha
&= 
(\cos \alpha \times I + \sin \alpha \times R(\pi/2)) \cdot \partial_x f(z_{r, \alpha}) \\
&=
R(\alpha) \cdot \partial_x f(z_{r, \alpha}).
\end{split}
$$ Par conséquent lorsque $r$ est non nul $$
\partial_x f (z_{r, \alpha}) \cos \alpha 
+ 
\partial_y f (z_{r, \alpha}) \sin \alpha
= \frac{1}{r} R(-\pi/2) \cdot \partial_{\alpha} (f(z_{\alpha, r}))
$$ et donc $$
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
$$ Par ailleurs, un calcul direct montre que $I'(0) = 0$. La dérivée de
$I$ est donc identiquement nulle ; on en conclut que pour tout $r$, $$
I(r) = \frac{1}{2\pi}\int_0^{2\pi} f(z_{\alpha, r}) \, d\alpha
= I(0) = f(c).
$$
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

[^2]: Sans nécessiter de construction supplémentaire ; dans le cadre de
    l'intégrale de Riemann, certaines de ces intégrales peuvent être
    calculées comme des intégrales *impropres*, par un passage à la
    limite d'intégrales de Riemann de fonctions définies sur un
    sous-ensemble. Mais l'intégrale qui en résulte -- on parle parfois
    d'intégrale de *Cauchy-Riemann* -- perd une bonne partie des
    propriétés de l'intégrale de Riemann.

[^3]: En première approche on pourra rapidement s'en convaincre en
    remplaçant "intégrables au sens de Riemann" par "continues". Dans le
    cas général, supposons que $f$ et $g$ sont intégrables au sens de
    Riemann sur un segment $[a, b]$ de $\mathbb{R}$, c'est-à-dire
    bornées et continues presque partout. De toute évidence, leur
    produit est borné. Si $f$ est continue en tout point de $[a, b]$ à
    l'exception de l'ensemble négligeable $A$ et $g$ en tout point de
    $[a, b]$ à l'exception de l'ensemble négligeable $B$, l'ensemble $C$
    des points de discontinuité de $fg$ est nécessairement dans
    $A\cup B$, donc négligeable. Le produit $fg$ est donc intégrable au
    sens de Riemann.

[^4]: Il existe des ensembles dont on ne peut pas définir
    raisonnablement la longueur, sauf à accepter un concept de longueur
    aux propriétés très étranges. Cette situation ne résulte pas de la
    méthode de définition de la longueur par l'intégrale ; c'est au
    contraire une limitation intrinsèque de la théorie de la mesure que
    nous étudierons plus en détail par la suite. Malheureusement pour la
    didactique, il n'existe aucun exemple explicite (élaboré par un
    procédé constructif) d'ensemble qui ne soit pas mesurable. On peut
    se consoler en apprenant que, du point de vue logique, si l'on
    suppose que tous les ensembles sont mesurables -- ce qui peut
    sembler relativement anodin -- on peut alors prouver des
    propositions beaucoup plus perturbantes, comme l'existence de
    partitions de $\mathbb{R}$ "contenant strictement plus d'éléments"
    que $\mathbb{R}$ lui-même.

[^5]: le résultat correspondant est faux pour les intervalles fermés.

[^6]: À tel point que, si l'on peut prouver l'existence d'une fonction
    non-mesurable, sa "construction explicite" est impossible. Les
    fonctions non-mesurables font partie des objets "intangibles"
    (cf. @Sch96) dont l'existence est prédite par la théorie mais que
    l'on ne rencontre jamais en pratique ...

[^7]: Pour chaque point $x$ de $U \subset \mathbb{R}^m$ ouvert dont les
    coordonnées sont rationnelles, on considère le plus grand pavé
    ouvert de la forme
    $$\left]x_1-h, x_1+h\right[ \times \dots \times \left]x_m-h, x_m+h\right[,
    \; h > 0$$ qui soit inclus dans $U$ ; ces pavés forment une
    collection dénombrable et leur union est égale à $U$ par
    construction.

[^8]: En effet, $$
    \left| \frac{g(h) - g(0)}{h} \right| \leq \frac{|h|}{2} \to 0 \, \mbox{ quand } \, h \to 0.
    $$
