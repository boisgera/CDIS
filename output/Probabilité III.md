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
title: Probabilités III
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
-   [Probabilités --- cadre général](#probabilités-cadre-général)
    -   [Tribu produit](#tribu-produit)
    -   [Produit des tribus de Borel](#produit-des-tribus-de-borel)
-   [Lois conditionnelles](#lois-conditionnelles-1)
    -   [Introduction](#introduction)
    -   [Lois conditionnelles dans un
        couple](#lois-conditionnelles-dans-un-couple)
    -   [Cas où $X$ est discrète](#cas-où-x-est-discrète)
    -   [Densités conditionnelles](#densités-conditionnelles)
    -   [Cas général](#cas-général)
    -   [Conséquences](#conséquences)
-   [Espérance conditionnelle](#espérance-conditionnelle-1)
    -   [Exemple : vecteurs Gaussiens à
        densité](#exemple-vecteurs-gaussiens-à-densité)
-   [Régression et espérance conditionnelle des variables de carré
    intégrable](#régression-et-espérance-conditionnelle-des-variables-de-carré-intégrable)
    -   [Régression linéaire](#régression-linéaire)
    -   [Espace de Hilbert des variables aléatoires de carré
        intégrable](#espace-de-hilbert-des-variables-aléatoires-de-carré-intégrable)
-   [Exercices](#exercices)
    -   [Couple de variables](#couple-de-variables)
    -   [Mélanges de lois](#mélanges-de-lois)
    -   [Lois conjuguées](#lois-conjuguées)
    -   [Etats cachés --- indépendance
        conditionnelle](#etats-cachés-indépendance-conditionnelle)
    -   [Non-réponse](#non-réponse)
-   [Solutions](#solutions)
    -   [Couple de variables](#couple-de-variables-1)
    -   [Mélanges de lois](#mélanges-de-lois-1)
    -   [Etats cachés --- indépendance
        conditionnelle](#etats-cachés-indépendance-conditionnelle-1)
    -   [Non-réponse](#non-réponse-1)
-   [Références](#références)

```{=tex}
\newcommand{\R}{\mathbb{R}}
\newcommand{\Q}{\mathbb{Q}}
\renewcommand{\P}{\mathbb{P}}
\renewcommand{\C}{\mathbb{C}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\A}{\mathcal{A}}
\newcommand{\E}{\mathcal{E}}
\newcommand{\B}{\mathcal{B}}
\renewcommand{\L}{\mathcal{L}}
\newcommand{\Esp}{\mathbb{E}}
\newcommand{\V}{\mathbb{V}}
\newcommand{\cov}{\text{Cov}}
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

Sauf mention particulière, la connaissance des démonstrations du
document n'est pas exigible[^2]

::: {.section}
#### Cadre général des probabilités

-   `$\mathord{\bullet}$ `{=tex}savoir qu'une probabilité $\mathbb{P}$
    définie sur $(\Omega, \mathcal{A})$ est une mesure finie,
    c'est-à-dire telle que $\mathbb{P}(\Omega)=1$
-   `$\mathord{\bullet}$ `{=tex}savoir qu'une variable aléatoire réelle
    est une application mesurable de $(\Omega, \mathcal{A})$ dans
    $(\mathbb{R},\mathcal{B}(\mathbb{R}))$
-   `$\mathord{\bullet}$ `{=tex}savoir que la loi de probabilité
    $\mathbb{P}_X$ d'une variable aléatoire $X$ définie sur
    $(\Omega,\mathcal{A},\mathbb{P})$ est la mesure image de
    $\mathbb{P}$ par $X$
-   `$\mathord{\bullet}$ `{=tex}connaître la contrepartie des deux point
    précédents dans le cas des vecteurs aléatoires
-   `$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$ `{=tex}connaître
    la définition d'une tribu produit
-   `$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir
    que
    $\mathcal{B}(\mathbb{R}^{m+n}) = \mathcal{B}(\mathbb{R}^{m}) \otimes \mathcal{B}(\mathbb{R}^{n})$
-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir utiliser le
    théorème de Fubini pour les probas
-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}connaître la
    caractérisation de l'indépendance dans le cas général
:::

::: {.section}
#### Lois conditionnelles

-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}connaître le théorème
    de Fubini conditionnel
-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}connaître les formules
    de balayage conditionnel
-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir appliquer ces
    résultats pour différents types de loi de probabilité (à densité ou
    non)
-   `$\mathord{\bullet}$ `{=tex}connaître le critère d'indépendance qui
    résulte du théorème de Fubini conditionnel
:::

::: {.section}
#### Espérance conditionnelle

-   `$\mathord{\bullet}$ `{=tex}connaître les deux points de la
    définition de l'espérance conditionnelle
-   `$\mathord{\bullet}$ `{=tex}connaître les deux points de la
    définition de l'espérance conditionnelle d'une fonction de variables
    aléatoires
-   `$\mathord{\bullet}$ `{=tex}connaître et savoir utiliser la formule
    de l'espérance totale
-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir calculer la
    densité conditionnelle d'un certain nombre de composantes sachant
    les autres dans un vecteur gaussien à densité
-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir que la
    régression linéaire est la meilleure approximation linéaire (au sens
    des moindres carrés) d'une variable aléatoire par une autre
-   `$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir
    retrouver ce résultat
-   `$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$ `{=tex}connaître
    l'interprétation géométrique de l'espérance conditionnelle dans le
    cas $\mathcal{L}^2$
-   `$\mathord{\bullet}$ `{=tex}connaître et savoir utiliser la formule
    de la variance totale
:::
:::

::: {.section}
Probabilités --- cadre général
==============================

Les éléments de théorie de la mesure donnés en calcul intégral
permettent une relecture des premiers chapitres de probabilités. Le
principal avantage est que les différents cas de figures déjà évoqués :
lois de probabilités discrètes, à densité, mixtes vont pouvoir être
traités dans un cadre unifié. L'intégrale que nous considérons est
l'intégrale de Lebesgue. On peut déjà s'apercevoir qu'une
[probabilité](Probabilité%20I.pdf%20#defproba) $\mathbb{P}$ définie sur
un espace probabilisable (mesurable) $(\Omega, \mathcal{A})$ est une
mesure positive *finie* au sens où $\mathbb{P}(\Omega) = 1$ et hérite
ainsi de ses propriétés, on parle aussi de *mesure de probabilité*.

::: {.section}
### Remarque -- Cas particuliers {#cas-particuliers .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Cas particuliers}`{=latex}

-   Dans le cas discret ($\Omega$ au plus dénombrable, muni de
    $\mathcal{P}(\Omega)$), la mesure de probabilité est une somme
    pondérée de mesures de Dirac :
    $$\mathbb{P}= \sum_{\omega \in \Omega} p_{\omega} \delta_{\omega},$$
    où $\sum_{\omega \in \Omega} p_{\omega} =1$ et
    $\forall \omega \in \Omega, p_{\omega} \geq 0$
-   Dans le cas à densité ($\Omega = \mathbb{R}$, muni par exemple de la
    tribu de Borel), la mesure de probabilité s'écrit :
    $$\mathbb{P}= f\ell,$$ où $f$ est une densité et $\ell$ la mesure de
    (Borel-)Lebesgue sur $\mathbb{R}$[^3]. On dit que $\mathbb{P}$ admet
    une densité par rapport à la mesure de (Borel-)Lebesgue.

Une [variable aléatoire réelle](Probabilité%20II.pdf%20#defvar) (v.a.r),
respectivement un vecteur aléatoire, $X$ est une application mesurable
de $(\Omega, \mathcal{A})$ dans $(\mathbb{R},\mathcal{B}(\mathbb{R}))$,
respectivement dans $(\mathbb{R}^n,\mathcal{B}(\mathbb{R}^n))$, et [sa
loi](Probabilité%20II.pdf%20#defloivar) $\mathbb{P}_X$ est la mesure
image de $\mathbb{P}$ par $X$.

Le fait que la composition d'un vecteur aléatoire réel par une
application $\mathcal{B}(\mathbb{R}^n)/\mathcal{B}(\mathbb{R})$
mesurable (borélienne) est une variable aléatoire s'obtient
immédiatement par le résultat du chapitre IV de calcul intégral relatif
à la [composition de fonctions
mesurables](Calcul%20Intégral%20IV.pdf%20#compfoncmes).

On peut généraliser la définition de l'espérance d'une variable
aléatoire et des espaces vectoriels $\mathcal{L}^1$ et $\mathcal{L}^2$
de la manière suivante :
:::

::: {.section}
### Définition -- Espace $\mathcal{L}^1$ {#espace-mathcall1 .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Espace \(\mathcal{L}^1\)}`{=latex}

Soit $X$ une variable aléatoire réelle. $X$ est intégrable et on note
$X \in \mathcal{L}^1$, ou
$\mathcal{L}^1(\Omega,\mathcal{A},\mathbb{P})$, si et seulement si
$\mathbb{E}(|X|) = \int_{\mathbb{R}} |x| \mathbb{P}_X(dx) = \int_{\Omega} |X|(\omega)\mathbb{P}(d\omega) < +\infty$.
:::

::: {.section}
### Définition -- Espace $\mathcal{L}^2$ {#espace-mathcall2 .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Espace \(\mathcal{L}^2\)}`{=latex}

Soit $X$ une variable aléatoire réelle. $X$ est de carré intégrable et
on note $X \in \mathcal{L}^2$, ou
$\mathcal{L}^2(\Omega,\mathcal{A},\mathbb{P})$, si et seulement si
$\mathbb{E}(X^2) = \int_{\mathbb{R}} x^2 \mathbb{P}_X(dx) = \int_{\Omega} X^2(\omega)\mathbb{P}(d\omega) < +\infty$.

Les propriétés des espaces $\mathcal{L}^1$ et $\mathcal{L}^2$ données au
chapitre 2 du cours de probabilités sont vraies en toute généralité.

On peut également réécrire [la proposition portant sur l'espérance de la
composée d'une variable aléatoire et d'une fonction
mesurable](Probabilité%20II.pdf%20#esperanceg) avec l'intégrale de
Lebesgue.
:::

::: {.section}
### Proposition -- Espérance de $g(X)$ (cas général) {#esperanceg2 .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Espérance de \(g(X)\) (cas général)}`{=latex}

Soit $X$ une variable aléatoire réelle de loi $\mathbb{P}_X$ et $g$ une
fonction $\mathcal{B}(\mathbb{R})/\mathcal{B}(\mathbb{R})$-mesurable
(borélienne). Alors $g(X)$ est intégrable si et seulement si l'intégrale
$$\int_\mathbb{R}|g(x)| \mathbb{P}_X(dx) = \int_\Omega |g(X(\omega))|\mathbb{P}(d\omega)$$
est finie et dans ce cas
$$\mathbb{E}(g(X)) = \int_\mathbb{R}g(x) \mathbb{P}_X(dx) = \int_\Omega g(X(\omega))\mathbb{P}(d\omega).$$
:::

::: {.section}
Ce résultat fait l'objet d'un exercice du chapitre IV de calcul intégral
(mesure image).

Enfin, pour généraliser la caractérisation de l'indépendance de deux
variables aléatoires (ou de $n$ variables aléatoires, en itérant), on a
besoin de définir un espace probabilisé (ou mesuré) sur $\mathbb{R}^n$.
Pour ce faire, on introduit (sans preuve) quelques résultats
fondamentaux associés aux produits de mesures de probabilités et aux
intégrales associées. On pourra se reporter à @Jacod pour les
démonstrations, ou bien à @Hun11 ou @Tao11 pour un exposé dans le cadre
plus général de la théorie de la mesure.
:::

::: {.section}
### Tribu produit

Soit $(X ,\mathcal{A})$ et $(Y, \mathcal{B})$ deux espaces mesurables.
On appelle *tribu produit* de $\mathcal{A}$ et $\mathcal{B}$ et l'on
note $\mathcal{A} \otimes \mathcal{B}$ la tribu sur le produit cartésien
$X \times Y$ engendrée par les ensembles de la forme $A \times B$ où
$A \in \mathcal{A}$ et $B \in \mathcal{B}$. $$
\mathcal{A} \otimes \mathcal{B} := 
\sigma_{X \times Y}
\left( 
\left\{ A \times B \; | \; A \in \mathcal{A}, \; B \in \mathcal{B} \right\}
\right).
$$ L'espace mesurable $(X \times Y, \mathcal{A} \otimes \mathcal{B})$
est appelé *espace produit* des espaces mesurables $(X, \mathcal{A})$ et
$(Y, \mathcal{B})$.
:::

::: {.section}
### Produit des tribus de Borel

La tribu de Borel sur $\mathbb{R}^{m+n}$ est le produit des tribus de
Borel sur $\mathbb{R}^m$ et $\mathbb{R}^n$ : $$
\mathcal{B}(\mathbb{R}^{m+n}) = \mathcal{B}(\mathbb{R}^{m}) \otimes \mathcal{B}(\mathbb{R}^{n}).
$$
:::

::: {.section}
### Remarque -- Produit et tribu de Lebesgue {#produit-et-tribu-de-lebesgue .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Produit et tribu de Lebesgue}`{=latex}

Notons que le résultat similaire est faux pour la mesure de Lebesgue :
$$
  \mathcal{L}(\mathbb{R}^{m+n}) \neq \mathcal{L}(\mathbb{R}^{m}) \otimes \mathcal{L}(\mathbb{R}^{n}).
  $$ Pour obtenir $\mathcal{L}(\mathbb{R}^{m+n})$, il est nécessaire de
compléter la tribu produit
$\mathcal{L}(\mathbb{R}^m) \otimes \mathcal{L}(\mathbb{R}^n)$ par
rapport à la mesure de Lebesgue sur $\mathbb{R}^{m+n}$, c'est-à-dire de
rajouter les ensembles négligeables pour la tribu de Lebesgue à la
collection, puis de construire la tribu engendrée (cf. [exercice
"Complétion d'une mesure" du chapitre
IV](Calcul%20Intégral%20IV.pdf#complétion)).
:::

::: {.section}
### Théorème -- Théorème de Fubini (pour les probabilités) {#fubiniproba .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Théorème de Fubini (pour les probabilités)}`{=latex}

Soient $\mathbb{P}_1$ et $\mathbb{P}_2$ deux probabilités définies
respectivement sur $(\mathbb{R}^n, \mathcal{B}(\mathbb{R}^n))$ et
$(\mathbb{R}^m, \mathcal{B}(\mathbb{R}^m))$.

1.  Soient $A \in \mathcal{B}(\mathbb{R}^n)$ et
    $B \in \mathcal{B}(\mathbb{R}^m)$, alors
    $$\mathbb{P}(A \times B) = \mathbb{P}_1(A)\mathbb{P}_2(B)$$ définit
    de manière unique une probabilité sur
    $(\mathbb{R}^{n+m}, \mathcal{B}(\mathbb{R}^{n+m}))$ (que l'on note
    aussi $\mathbb{P}_1 \otimes \mathbb{P}_2$).
2.  Soit $f$ une fonction $\mathcal{B}(\mathbb{R}^{n+m})$-mesurable
    positive ou $\mathbb{P}_1 \otimes \mathbb{P}_2$-intégrable, alors la
    fonction $x \mapsto \int f(x, y)\mathbb{P}_2(dy)$ est
    $\mathcal{B}(\mathbb{R}^{n})$-mesurable, la fonction
    $y \mapsto \int f (x, y) \mathbb{P}_1(dx)$ est
    $\mathcal{B}(\mathbb{R}^m)$-mesurable et
    $$\int f d\mathbb{P}_1\otimes\mathbb{P}_2 = \int \left(\int f(x,y) \mathbb{P}_2(dy) \right) \mathbb{P}_1(dx) = \int \left(\int f(x,y) \mathbb{P}_1(dx) \right) \mathbb{P}_2(dy)$$
:::

::: {.section}
Le théorème de Fubini permet de caractériser l'indépendance de deux
variables aléatoires dans le cas général.
:::

::: {.section}
### Proposition -- Indépendance d'un couple de variables aléatoires {#indépendance-dun-couple-de-variables-aléatoires .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Indépendance d'un couple de variables aléatoires}`{=latex}

Soient $X$ et $Y$ deux variables aléatoires réelles définies toutes deux
sur $(\Omega,\mathcal{A},\mathbb{P})$. Le couple $Z = (X,Y)$ peut-être
considéré comme un vecteur aléatoire à valeurs dans
$(\mathbb{R}^2, \mathcal{B}(\mathbb{R})\otimes \mathcal{B}(\mathbb{R}))$,
et les deux variables aléatoires $X$ et $Y$ sont indépendantes si et
seulement si la loi $\mathbb{P}_{X,Y}$ du couple est égale au produit
$\mathbb{P}_X \otimes \mathbb{P}_Y$ des lois de $X$ et $Y$.
:::

::: {.section}
#### Démonstration {#démonstration .proof}

Soit $A$ et $B$ deux boréliens de $\mathbb{R}$. On a évidemment
$Z^{-1}(A \times B) = X^{-1}(A) \cap Y^{-1}(B) \in \mathcal{A}$ et donc
la mesurabilité
($\mathcal{A}/ \left(\mathcal{B}(\mathbb{R})\otimes \mathcal{B}(\mathbb{R})\right)$)de
$Z$ découle de la définition de la tribu produit de Borel.

L'indépendance de $X$ et $Y$ revient au fait que pour tous boréliens $A$
et $B$ de $\mathbb{R}$, on ait
$$\mathbb{P}((X,Y) \in A\times B) = \mathbb{P}(X\in A)\mathbb{P}(Y \in B),$$
ce qui équivaut à
$$\mathbb{P}_{X,Y}(A \times B) = \mathbb{P}_X(A)\mathbb{P}_Y(B),$$ qui
est assuré par l'unicité de la mesure (de probabilité) produit d'après
le [théorème de Fubini (p.
`\pageref*{fubiniproba}`{=tex})](#fubiniproba).`\hfill$\blacksquare$`{=latex}
:::
:::

::: {.section}
Lois conditionnelles
====================

::: {.section}
Introduction
------------

On s'est consacré jusqu'à présent à l'étude de variables aléatoires
indépendantes. En pratique cependant, on rencontre souvent des variables
dépendant les unes des autres. Dans le cas de la météo, les variables
température, vitesse du vent et pression en fournissent un exemple. Dans
les approches bayésiennes, on résume l'information disponible sur l'état
du système étudié par la **loi a priori** et on met à jour notre
connaissance du système en incorporant de l'information supplémentaire
(par exemple des observations). On cherche alors à caractériser la **loi
a posteriori** de l'état du système, qui est la loi de l'état sachant
l'information supplémentaire. On va ainsi s'attacher dans ce chapitre à
décrire les **lois conditionnelles** qui vont permettre de résumer
l'information apportée par une variable (ou un vecteur) sur une autre et
s'intéresser en particulier à l'**espérance conditionnelle** qui
indiquera le comportement moyen d'une variable conditionnellement à une
autre. Ce dernier cas pose le cadre probabiliste d'un des problèmes
fondamentaux en apprentissage statistique : l'apprentissage supervisé,
où on dispose d'un ensemble de réalisations d'une variable dont on
cherche à prédire le comportement à partir d'un ensemble de variables
dites explicatives (ou prédicteurs).
:::

::: {.section}
Lois conditionnelles dans un couple
-----------------------------------

Soient deux variables aléatoire $X$ et $Y$ définies sur le même espace
probabilisé $(\Omega, \mathcal{A}, \mathbb{P})$. Dans le cas où $X$ et
$Y$ sont indépendantes, on a vu que pour tous boréliens $B_1$ et $B_2$
de $\mathbb{R}$, on a
$$\mathbb{P}(X\in B_1, Y\in B_2)= \mathbb{P}(X\in B_1)\mathbb{P}(Y\in B_2) = \mathbb{P}_X(B_1)\mathbb{P}_Y(B_2) = \int_{B_1}\mathbb{P}_Y(B_2)\mathbb{P}_X(dx),$$
où on a utilisé le [théorème de Fubini (p.
`\pageref*{fubiniproba}`{=tex})](#fubiniproba).

Du fait de l'indépendance, on a aussi
$\mathbb{P}_Y(B_2) = \mathbb{P}(Y\in B_2) = \mathbb{P}(Y \in B_2 | X \in B_1) = \mathbb{P}_Y(B_2|X \in B_1)$
ce qui exprime que pour tout borélien $B_1$, la loi conditionnelle de
$Y$ sachant $X\in B_1$ est identique à la loi de $Y$.

Lorsque $X$ et $Y$ en sont pas indépendantes, on va chercher à établir
une égalité de la forme
$$\mathbb{P}(X\in B_1, Y\in B_2) = \mathbb{P}_X(B_1)\mathbb{P}_Y(B_2 |X\in B_1) = \int_{B_1}\mathbb{P}_{Y|X=x}(B_2)\mathbb{P}_X(dx)$$
et s'intéresser à caractériser la *loi conditionnelle de $Y$ sachant
$X=x$*, que l'on notera donc $\mathbb{P}_{Y|X=x}$.

De même, pour toute application $g : \mathbb{R}^2 \to \mathbb{R}$
borélienne telle que $g(X,Y)$ admette une espérance (relativement à la
loi du couple $\mathbb{P}_{X,Y}$), on voudrait écrire :
$$\mathbb{E}(g(X,Y)) = \int_{\mathbb{R}} \left( \int_{\mathbb{R}} g(x,y) \mathbb{P}_{Y|X=x}(dy)\right) \mathbb{P}_X(dx)$$

Pour bien fixer les idées, on va décrire spécifiquement les cas où $X$
est discrète puis où le couple $(X,Y)$ admet une densité avant d'aborder
le cas général.
:::

::: {.section}
Cas où $X$ est discrète
-----------------------

Dans ce paragraphe, on suppose que la variable aléatoire réelle $X$ est
discrète, c'est-à-dire que l'ensemble $X(\Omega) \subset \mathbb{R}$ des
valeurs $x_k$ prises par $X$ est au plus dénombrable.

On peut imposer que $\forall x \in X(\Omega)$ on ait
$\mathbb{P}(X=x) > 0$, quitte à modifier $X$ sur un ensemble de
probabilité nulle. On va ainsi pouvoir utiliser la définition de la
probabilité conditionnelle pour des événements de la forme $\{X =x\}$.
Ceci permet d'écrire pour tous boréliens $B_1$ et $B_2$ de
$\mathbb{R}$ : `\begin{align*}
\mathbb{P}(X \in B_1, Y \in B_2) &= \sum_{x \in X(\Omega)\cap B_1} \mathbb{P}(X=x, Y\in B_2)\\
                         &= \sum_{x \in X(\Omega)\cap B_1} \mathbb{P}(X=x) \mathbb{P}(Y \in B_2 | X=x)\\
                         &= \int_{B_1} \mathbb{P}(Y \in B_2 | X=x) \mathbb{P}_X(dx)
\end{align*}`{=tex} puisque
$\mathbb{P}_X = \sum_{x \in X(\Omega)} \mathbb{P}(X=x)\delta_x$. On
obtient ainsi l'écriture souhaitée en posant
$$\mathbb{P}_{Y|X=x}(B_2) = \mathbb{P}(Y \in B_2 | X=x),\,\,\,\forall x \in X(\Omega), \forall B_2\in\mathcal{B}(\mathbb{R}).$$

::: {.section}
### Remarque -- Image de la probabilité conditionnelle {#image-de-la-probabilité-conditionnelle .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Image de la probabilité conditionnelle}`{=latex}

$\mathbb{P}_{Y|X=x}$ ainsi définie est simplement la probabilité sur
$(\mathbb{R},\mathcal{B}(\mathbb{R}))$ image par $Y$ de la probabilité
conditionnelle $\mathbb{P}(\cdot|X=x)$ définie sur
$(\Omega,\mathcal{A})$, autrement dit, la **loi de $Y$ relative à
$\mathbb{P}(\cdot|X=x)$** et non à $\mathbb{P}$.

La formule ci-dessus s'écrit
$\mathbb{P}_{X,Y}(B_1 \times B_2) = \int_{B_1} \mathbb{P}(Y \in B_2 | X=x) \mathbb{P}_X(dx)$,
où $\mathbb{P}_{X,Y}$ est la loi du couple. Elle se généralise à tout
borélien $B$ de $\mathbb{R}^2$ de la manière suivante :

`\begin{align*}
\mathbb{P}_{X,Y}(B) &= \mathbb{P}((X,Y)\in B) = \sum_{x \in X(\Omega)} \mathbb{P}(X=x, (x,Y) \in B) \\
      &= \sum_{x \in X(\Omega)} \mathbb{P}(X=x) \mathbb{P}((x,Y) \in B | X=x) \\
      &= \sum_{x \in X(\Omega)} \mathbb{P}(X=x) \mathbb{P}_{Y|X=x}(B_x),
\end{align*}`{=tex}

où $B_x = \{y\in \mathbb{R}, (x,y) \in B\}$. Ainsi, pour tout $B$
borélien de $\mathbb{R}^2$,

$$\mathbb{E}(1_B(X,Y)) = \int_{\mathbb{R}^2} 1_B(x,y)\mathbb{P}_{X,Y}(dx dy) = \int_\mathbb{R}\left(\int_\mathbb{R}1_B(x,y) \mathbb{P}_{Y|X=x}(dy)\right)  \mathbb{P}_X(dx)$$

Par linéarité de l'espérance, on peut ainsi exprimer l'espérance d'une
fonction étagée. Pour avoir le résultat pour une fonction borélienne
positive, on exprime celle-ci comme limite simple d'une suite croissante
de fonctions étagées, et on applique le théorème de convergence
monotone. Enfin, on applique cette construction à $g_+$ et $g_-$ pour
une fonction $g$ de signe quelconque $\mathbb{P}_{X,Y}$-intégrable. En
d'autres termes, on reprend le procédé de construction de l'intégrale de
Lebesgue. On obtient ainsi la formule souhaitée :
$$\mathbb{E}(g(X,Y)) = \int_{\mathbb{R}} \left( \int_{\mathbb{R}} g(x,y) \mathbb{P}_{Y|X=x}(dy)\right) \mathbb{P}_X(dx).$$
:::

::: {.section}
#### Exemple -- Pour fixer les idées (1) {#ex1 .example .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Pour fixer les idées (1)}`{=latex}

Soit $X \geq 0$ une variable aléatoire à valeurs dans $\mathbb{N}$ et
$Y$ une variable aléatoire réelle positive telle que la loi du couple
$\mathbb{P}_{X,Y}$ vérifie pour tout $n\in\mathbb{N}$ et tout borélien
$B_2$ de $\mathbb{R}$ :
$$\mathbb{P}_{X,Y} (\{n\}\times B_2) = (1-\alpha)\alpha^n \int_{B_2 \cap \mathbb{R}_+^\ast}e^{-t}\frac{t^n}{n!}dt,\,\,\, 0 < \alpha <1$$
$\mathbb{P}_{X,Y}$ est bien une probabilité sur $\mathbb{R}^2$ puisque
par convergence monotone : `\begin{align*}
\mathbb{P}_{X,Y} (\mathbb{R}^2) &= \mathbb{P}_{X,Y}(\mathbb{N}\times \mathbb{R}) \\
                &= \sum_{n\in\mathbb{N}} \mathbb{P}_{X,Y} (\{n\}\times \mathbb{R})\\
                &= \sum_{n\in\mathbb{N}} (1-\alpha)\alpha^n \int_{\mathbb{R}_+^\ast}e^{-t}\frac{t^n}{n!}dt \\
                &= (1-\alpha)\int_{\mathbb{R}_+^\ast}e^{-t} \sum_{n\in\mathbb{N}} \frac{(\alpha t)^n}{n!}dt \\
                &= (1-\alpha)\int_{\mathbb{R}_+^\ast}e^{-(1-\alpha)t} dt = 1
\end{align*}`{=tex}\
où on aura reconnu la loi exponentielle de paramètre $(1-\alpha)$.
$\forall n \in \mathbb{N}$,
$$ \int_{\mathbb{R}_+^\ast}e^{-t}\frac{t^n}{n!}dt = \int_{\mathbb{R}_+^\ast}e^{-t}\frac{t^{(n-1)}}{(n-1)!}dt = \ldots = \int_{\mathbb{R}_+^\ast}e^{-t}dt =1$$
par intégrations par parties itérées. La loi marginale de $X$ s'écrit
donc :
$$\forall n \in \mathbb{N}, \mathbb{P}(X=n) = \mathbb{P}_{X,Y} (\{n\}\times \mathbb{R}_+^\ast) = (1-\alpha)\alpha^n,$$
loi géométrique de paramètre $(1-\alpha)$. On en déduit la loi
conditionnelle de $Y$ sachant $X = n$ :
$$\mathbb{P}_{Y|X=n}(B_2) = \mathbb{P}(Y \in B_2 | X=n) = \frac{\mathbb{P}_{X,Y} (\{n\}\times B_2)}{\mathbb{P}(X=n)} = \int_{B_2 \cap \mathbb{R}_+^\ast} e^{-t}\frac{t^n}{n!}dt$$
et $\mathbb{P}_{Y|X=n}$ est la donc la loi gamma de paramètre $(n+1,1)$.
:::
:::

::: {.section}
Densités conditionnelles
------------------------

On suppose maintenant que le couple $(X,Y)$ admet une densité $f_{X,Y}$
(par rapport à la mesure de Borel-Lebesgue). On note
$f_X(x) = \int_\mathbb{R}f_{X,Y}(x,y)dy$ (respectivement
$f_Y(y) = \int_\mathbb{R}f_{X,Y}(x,y)dx$) la loi marginale de $X$ (resp.
de $Y$). On s'intéresse à caractériser la densité de la variable $Y$
connaissant la valeur prise par la variable $X$, c'est la *densité
conditionnelle* de $Y$ sachant $\{X = x\}$ :

::: {.section}
### Proposition -- Densité conditionnelle {#defdenscond .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Densité conditionnelle}`{=latex}

La formule suivante définit une densité sur $\mathbb{R}$, pour tout
$x \in \mathbb{R}$ tel que $f_X(x) > 0$.
$$ f_{Y|X=x}(y) = \frac{f_{X,Y}(x,y)}{f_X(x)}.$$ Cette fonction
s'appelle la *densité conditionnelle de $Y$ sachant $\{X = x\}$*. La
probabilité conditionnelle de $Y$ sachant $\{X = x\}$ s'écrit ainsi
$\mathbb{P}_{Y|X=x} = f_{Y|X=x}\ell$, où $\ell$ représente la mesure de
Borel-Lebesgue.
:::

::: {.section}
#### Démonstration {#démonstration-1 .proof}

La preuve est immédiate puisque $f_{Y|X=x}$ est une fonction positive
d'intégrale 1.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Exercice -- Dans un triangle (1) ($\mathord{\bullet}$) {#etb1 .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Dans un triangle (1)}`{=latex}

Soient $X$ et $Y$ de densité jointe $f_{X,Y}(x,y)= \frac{1}{x}1_T (x,y)$
où $T$ est le triangle $T = \{0< y< x < 1\}$.

1.  Calculer la densité marginale de $X$
2.  Calculer la densité conditionnelle de $Y$ sachant $X=x$.

([Solution p.
`\pageref*{answer-etb1}`{=tex}](#answer-etb1){.no-parenthesis}.)
:::

::: {.section}
L'interprétation de cette définition est la suivante : la fonction
$f_{Y|X=x}$ est la densité de la "loi conditionnelle de $Y$ sachant que
$X = x$". Bien sûr, nous avons $\mathbb{P}(X = x) = 0$ puisque $X$ admet
une densité, donc la phrase ci-dessus n'a pas réellement de sens, mais
elle se justifie heuristiquement ainsi : $dx$ et $dy$ étant de "petits"
accroissements des variables $x$ et $y$ et lorsque $f$ et $f_X$ sont
continues et strictement positives respectivement en $(x,y)$ et $x$ :
`\begin{align*}
f_X(x) dx & \approx \mathbb{P}(X \in [x, x+dx])\\
f_{X,Y}(x,y) dx dy & \approx \mathbb{P}(X \in [x, x+dx], Y \in [y, y+dy])\\
\end{align*}`{=tex} Par suite `\begin{align*}
f_{Y|X=x} (y) dy & \approx \frac{\mathbb{P}(X \in [x, x+dx], Y \in [y, y+dy])}{\mathbb{P}(X \in [x, x+dx])}\\
                 & \approx \mathbb{P}(Y \in [y, y+dy]|X \in [x, x+dx])\\
\end{align*}`{=tex}

On a alors le résultat suivant qui résout le problème posé en
introduction :
:::

::: {.section}
### Proposition -- Proposition {#proposition .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Proposition}`{=latex}

Pour toute fonction $g : \mathbb{R}^2 \to \mathbb{R}$ telle que $g(X,Y)$
admette une espérance, on a :
$$\mathbb{E}(g(X,Y)) = \int_\mathbb{R}\left( \int_\mathbb{R}g(x,y)f_{Y|X=x}(y) dy \right) f_X(x) dx,$$
dont on déduit, en prenant $g=1_{B_1 \times B_2}$, que :
$$\mathbb{P}(X\in B_1, Y\in B_2) = \int_{B_1} \left( \int_{B_2}f_{Y|X=x}(y) dy \right) f_X(x) dx.$$
:::

::: {.section}
#### Démonstration {#démonstration-2 .proof}

On a `\begin{align*}
\mathbb{E}(g(X,Y)) &= \int_{\mathbb{R}^2} g(x,y) f_{X,Y}(x,y) dy dx \\
             &= \int_{\mathbb{R}^2} g(x,y) f_{Y|X=x}(y)f_X(x) dy dx \\
             &= \int_\mathbb{R}\left( \int_\mathbb{R}g(x,y)f_{Y|X=x}(y) dy \right) f_X(x)dx,
\end{align*}`{=tex} les calculs étant licites par application du
[théorème de Fubini (p. `\pageref*{fubiniproba}`{=tex})](#fubiniproba)
et du fait que l'application
$x \mapsto \int_\mathbb{R}g(x,y)f_{Y|X=x}(y) dy$ est définie pour
$f_X(x) >0$, soit presque partout relativement à la mesure
$\mathbb{P}_X = f_X l$.`\hfill$\blacksquare$`{=latex}
:::
:::

::: {.section}
Cas général
-----------

On peut établir le résultat suivant, qui complète le [théorème de Fubini
(p. `\pageref*{fubiniproba}`{=tex})](#fubiniproba) et le résultat
d'existence et d'unicité des mesures produits, et que l'on admettra.

::: {.section}
### Théorème -- Fubini conditionnel {#fubinicond .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Fubini conditionnel}`{=latex}

Soit un couple $(X,Y)$ de variables aléatoires réelles de loi jointe
$\mathbb{P}_{X,Y}$, il existe une famille
$\left(\mathbb{P}_{Y|X=x}\right)_{x\in\mathbb{R}}$ de probabilités sur
$(\mathbb{R},\mathcal{B}(\mathbb{R}))$, unique à une égalité
$\mathbb{P}_X$-presque partout près[^4], qui vérifie pour tous
$B_1, B_2$ boréliens de $\mathbb{R}$ :
$$ \mathbb{P}_{X,Y}(B_1 \times B_2) = \int_{B_1} \left( \int_{B_2} \mathbb{P}_{Y|X=x}(dy) \right) \mathbb{P}_X(dx).$$
Ces probabilités sont appelées *lois conditionnelles* de $Y$ sachant
$X =x$. On a de plus pour toute application
$g : \mathbb{R}^2 \to \mathbb{R}$ telle que $g(X,Y)$ admette une
espérance :
$$\mathbb{E}(g(X,Y)) = \int_\mathbb{R}\left( \int_\mathbb{R}g(x,y)\mathbb{P}_{Y|X=x}(dy) \right) \mathbb{P}_X(dx).$$
:::

::: {.section}
### Remarque -- A noter {#a-noter .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{A noter}`{=latex}

-   Ce résultat peut être interprété comme un **théorème de Fubini
    conditionnel**, dans le sens où il permet une intégration
    séquentielle, mais ici la mesure de probabilité du couple $(X,Y)$
    s'exprime comme un produit de mesures dont l'un des termes dépend de
    la variable d'intégration de l'autre. En particulier, si on change
    l'ordre d'intégration, on change les mesures qui interviennent.
-   Fréquemment, dans les applications, la famille des lois
    conditionnelles est une donnée du modèle considéré, et leur
    existence ne pose donc pas de problème !
-   On retrouve les cas vus précédemment en notant que pour tout
    borélien $B_1$ de $\mathbb{R}$ on a
    $\mathbb{P}_X(B_1) = \int_{B_1}\mathbb{P}_X(dx) = \sum_{x \in B_1} \mathbb{P}(X=x)$
    lorsque $X$ est discrète, et que pour tous boréliens $B_1$ et $B_2$
    de $\mathbb{R}$ on a $\mathbb{P}_X(B_1) = \int_{B_1} f_X(x)dx$ et
    $\mathbb{P}_{X,Y}(B_1 \times B_2) = \int_{B_1 \times B_2}f_{X,Y}(x,y) dx dy$.
-   Dans tout ce qui précède, les rôles de $X$ et $Y$ peuvent évidemment
    être inversés.
:::
:::

::: {.section}
Conséquences
------------

Le [théorème précédent (p. `\pageref*{fubinicond}`{=tex})](#fubinicond)
a deux conséquences majeures. Il fournit d'une part un moyen efficace
d'identifier la loi marginale de $Y$ connaissant la loi marginale de $X$
et la loi de $Y$ sachant $X = x$. En effet, en notant que pour tout
borélien $B$ de $\mathbb{R}$,
$\mathbb{P}_Y(B) = \mathbb{P}_{X,Y}(\mathbb{R}\times B)$ et en
appliquant ce théorème, on a la proposition suivante :

::: {.section}
### Proposition -- Formule de balayage conditionnel {#balcond .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Formule de balayage conditionnel}`{=latex}

-   La loi marginale $\mathbb{P}_Y$ de $Y$ s'exprime comme la moyenne
    des lois conditionnelles $\mathbb{P}_{Y|X=x}$ pondérée par la loi de
    $X$. Pour tout $B$ borélien de $\mathbb{R}$
    $$\mathbb{P}_Y(B) = \int_\mathbb{R}\left( \int_{B} \mathbb{P}_{Y|X=x}(dy) \right) \mathbb{P}_X(dx) = \int_\mathbb{R}\mathbb{P}_{Y|X=x}(B) \mathbb{P}_X(dx)$$
-   Dans le cas où $X$ est discrète (à valeurs dans $I$ dénombrable), on
    retrouve une expression de la formule des probabilités totales et
    composées :
    $$\mathbb{P}_Y(B) = \mathbb{P}(Y\in B) = \sum_{x \in I} \mathbb{P}(Y \in B | X = x)\mathbb{P}(X=x)$$
-   Dans le cas où le couple $(X,Y)$ admet une densité, puisqu'on a
    $f_{X,Y}(x,y) = f_{Y | X=x}(y)f_X(x)$, on obtient l'expression
    suivante pour la densité marginale :
    $$f_Y(y) = \int_\mathbb{R}f_{X,Y}(x,y)dx = \int_\mathbb{R}f_{Y | X=x}(y)f_X(x) dx.$$
    On a en particulier la *formule de Bayes pour les densités* : pour
    tout $x$ tel que $f_X(x) > 0$ et tout $y$ tel que $f_Y(y) > 0$ :
    $$ f_{X|Y=y}(x) = \frac{f_{X,Y}(x,y)}{f_Y(y)} = \frac{f_{Y|X=x}(y)f_X(x)}{f_Y(y)} .$$
:::

::: {.section}
#### Exemple -- Pour fixer les idées (2) {#pour-fixer-les-idées-2 .example .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Pour fixer les idées (2)}`{=latex}

Poursuivons [l'exemple vu plus haut (p. `\pageref*{ex1}`{=tex})](#ex1).
On rappelle qu'on a déjà identifié la loi marginale de $X$ ainsi que la
loi conditionnelle de $Y$ sachant $X=n$ pour $n\in\mathbb{N}$ que l'on
rappelle ici :
$$\mathbb{P}(X=n) = (1-\alpha)\alpha^n,\,n\in\mathbb{N}\text{ et }\forall  B \in \mathcal{B}(\mathbb{R}), \, \mathbb{P}_{Y|X=n}(B) = \int_{B \cap \mathbb{R}_+^\ast} e^{-t}\frac{t^n}{n!}dt$$
On peut en déduire la loi marginale de $Y$ en utilisant la [formule de
balayage conditionnel (p. `\pageref*{balcond}`{=tex})](#balcond) et le
théorème de convergence monotone : `\begin{align*}
\mathbb{P}_Y(B)  &= \sum_{n \in \mathbb{N}} (1-\alpha)\alpha^n \int_{B \cap \mathbb{R}_+^\ast} e^{-t}\frac{t^n}{n!} dt\\
         &= (1-\alpha) \int_{B \cap \mathbb{R}_+^\ast} e^{-t} \sum_{n \in \mathbb{N}} \frac{(\alpha t)^n}{n!} dt \\
         &= \int_B 1_{\mathbb{R}_+}(t)(1-\alpha) e^{-(1-\alpha)t} dt,
\end{align*}`{=tex} de sorte que $Y$ suit une loi exponentielle de
paramètre $(1-\alpha)$.

En inversant les rôles, on va pouvoir identifier la loi de $X$ sachant
$Y \in B$ en notant que `\begin{align*}
\mathbb{P}_{X,Y}(\{n\} \times B) &= \mathbb{P}_X(\{n\})\mathbb{P}_{Y|X=n}(B) \\
                         &= \int_B \frac{(\alpha t)^n}{n!} e^{-\alpha t} \mathbb{P}_Y(dt)\\
                         &= \int_B \mathbb{P}_{X | Y =t}(\{n\}) \mathbb{P}_Y(dt)
\end{align*}`{=tex} où l'on reconnaît que
$\mathbb{P}_{X =n | Y =t}(\{n\}) = \frac{(\alpha t)^n}{n!} e^{-\alpha t}$,
c'est-à-dire que $X$ sachant $Y = t$ suit une loi de Poisson de
paramètre $\alpha t$ pour $\mathbb{P}_Y$-presque tout $t$.
:::

::: {.section}
En utilisant, le [théorème de Fubini conditionnel (p.
`\pageref*{fubinicond}`{=tex})](#fubinicond), on obtient également une
nouvelle caractérisation de l'indépendance de deux variables aléatoires
faisant intervenir les lois conditionnelles.
:::

::: {.section}
### Proposition -- Critère d'indépendance {#critère-dindépendance .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Critère d'indépendance}`{=latex}

1.  $X$ et $Y$ sont indépendantes si et seulement si, pour
    $\mathbb{P}_X$-presque tout $x$, $\mathbb{P}_{Y |X = x}$ ne dépend
    pas de $x$ et dans ce cas, on a
    $\mathbb{P}_{Y |X = x} = \mathbb{P}_Y$, c'est-à-dire que la loi
    conditionnelle est identique à la loi marginale.

2.  Dans le cas où $(X,Y)$ admet une densité, $X$ et $Y$ sont
    indépendantes si et seulement si la densité conditionnelle de $Y$
    sachant $\{X = x\}$ ne dépend pas de $x$.
:::

::: {.section}
#### Démonstration {#démonstration-3 .proof}

1.  Si $X$ et $Y$ sont indépendantes, pour tous $B_1$, $B_2$ boréliens
    de $\mathbb{R}$,
    $\mathbb{P}_{X,Y} (B_1 \times B_2) = \mathbb{P}_X(B_1)\mathbb{P}_Y(B_2) = \int_{B_1}\mathbb{P}_Y(B_2)\mathbb{P}_X(dx) = \int_{B_2}\mathbb{P}_X(B_1) \mathbb{P}_Y(dy)$.
    Le résultat d'unicité du [théorème de Fubini conditionnel (p.
    `\pageref*{fubinicond}`{=tex})](#fubinicond) (à une égalité
    $\mathbb{P}_X$-presque sûre près), nous indique alors que
    $\mathbb{P}_{Y|X=x}(B_2) = \mathbb{P}_Y(B_2)$.

    Inversement, si $\mathbb{P}_{Y |X = x} = \mathbb{P}_Y$, alors
    $\mathbb{P}_{X,Y} (B_1 \times B_2) = \int_{B_1}\mathbb{P}_{Y|X=x}(B_2)\mathbb{P}_X(dx) = \int_{B_1}\mathbb{P}_Y(B_2)\mathbb{P}_X(dx) = \mathbb{P}_X(B_1)\mathbb{P}_Y(B_2)$.

2.  Si $X$ et $Y$ sont indépendantes, $f_{X,Y} (x,y) = f_X(x) f_Y(y)$,
    d'où $f_{Y|X=x}(y) = f_Y(y)$.

    Inversement, si $f_{Y|X=x}(y) = f_Y(y)$ alors
    $f_{X,Y}(x,y) = f_{Y|X=x}(y) f_X(x) = f_Y(y)f_X(x)$ et $X$ et $Y$
    sont indépendantes.

$\;\; \blacksquare$
:::
:::
:::

::: {.section}
Espérance conditionnelle
========================

Puisque $\mathbb{P}_{Y|X=x}$ est la loi d'une variable aléatoire, on
peut définir l'espérance qui lui est associée et introduire la notion
d'espérance conditionnelle dans le cas où $Y$ est intégrable.

::: {.section}
### Définition -- Espérance conditionnelle {#defespcond .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Espérance conditionnelle}`{=latex}

Soit $Y \in \mathcal{L}^1$.

1.  L'*espérance conditionnelle de $Y$ sachant $\{X=x\}$* est définie
    par
    $$\mathbb{E}(Y|X=x) = \int_\mathbb{R}y \mathbb{P}_{Y|X=x} (dy).$$
2.  L'*espérance conditionnelle de $Y$ sachant $X$* est la **variable
    aléatoire** définie par :
    $$\mathbb{E}(Y|X) = \psi(X), \text{ avec } \psi(x) = \mathbb{E}(Y|X=x).$$
:::

::: {.section}
#### Exercice -- Dans un triangle (2) ($\mathord{\bullet}$) {#etb2 .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Dans un triangle (2)}`{=latex}

Soient $X$ et $Y$ de densité jointe $f_{X,Y}(x,y)= \frac{1}{x}1_T (x,y)$
où $T$ est le triangle $T = \{0< y< x < 1\}$. Calculer l'espérance
conditionnelle de $Y$ sachant $X$. ([Solution p.
`\pageref*{answer-etb2}`{=tex}](#answer-etb2){.no-parenthesis}.)
:::

::: {.section}
### Remarque -- Conséquences {#conséquences-1 .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Conséquences}`{=latex}

1.  $\psi(x)$ n'est définie que pour $x \notin N$, avec
    $\mathbb{P}(X\in N) = 0$. Par conséquent, la [définition (p.
    `\pageref*{defespcond}`{=tex})](#defespcond) définit bien
    l'espérance conditionnelle $\psi(X) = \mathbb{E}(Y|X)$
    $\mathbb{P}_X$-presque partout, autrement dit avec probabilité 1, ou
    encore presque sûrement.
2.  $\mathbb{E}(\mathbb{E}(|Y||X)) = \mathbb{E}(|Y|)$ comme conséquence
    directe du [théorème de Fubini conditionnel (p.
    `\pageref*{fubinicond}`{=tex})](#fubinicond). L'espérance
    conditionnelle de $Y$ sachant $X$ est bien définie dès que $Y$ est
    intégrable.
3.  Lorsque $(X,Y)$ admet une densité, l'espérance conditionnelle de $Y$
    sachant $\{X=x\}$ s'écrit
    $$\mathbb{E}(Y|X=x) = \int_\mathbb{R}y f_{Y|X=x}(y) dy.$$
:::

::: {.section}
#### Exercice -- Auto-conditionnement ($\mathord{\bullet}$) {#autocond .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Auto-conditionnement}`{=latex}

Montrer que $\mathbb{E}(Y|Y) = Y$. ([Solution p.
`\pageref*{answer-autocond}`{=tex}](#answer-autocond){.no-parenthesis}.)
:::

::: {.section}
On peut étendre cette définition aux variables de la forme $g(X,Y)$.
:::

::: {.section}
### Définition -- Espérance conditionelle d'une fonction de variables aléatoires {#defespcondg .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Espérance conditionelle d'une fonction de variables aléatoires}`{=latex}

Soit $(X,Y)$ un couple de variables aléatoires réelles et $g$ une
fonction borélienne positive ou $\mathbb{P}_{X,Y}$-intégrable sur
$\mathbb{R}^2$.

1.  L'*espérance conditionnelle de $g(X,Y)$ sachant $\{X=x\}$* est
    définie par
    $$\mathbb{E}(g(X,Y)|X=x) = \int_\mathbb{R}g(x,y) \mathbb{P}_{Y|X=x} (dy).$$
2.  L'*espérance conditionnelle de $g(X,Y)$ sachant $X$* est la
    **variable aléatoire** définie par :
    $$\mathbb{E}(g(X,Y)|X) = \psi(X), \text{ avec } \psi(x) = \mathbb{E}(g(X,Y)|X=x).$$
:::

::: {.section}
### Théorème -- Espérance totale {#espérance-totale .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Espérance totale}`{=latex}

Si $Y$ est intégrable, alors $\psi(X) = \mathbb{E}(Y | X)$ est
intégrable, et $$\mathbb{E}( \psi(X)) = E( Y ) .$$
:::

::: {.section}
#### Démonstration {#démonstration-4 .proof}

C'est une conséquence directe du [théorème de Fubini conditionnel (p.
`\pageref*{fubinicond}`{=tex})](#fubinicond).`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
Ce résultat permet de calculer $\mathbb{E}( Y )$ en conditionnant par
une variable auxiliaire $X$ :
$$\mathbb{E}( Y ) = \int_\mathbb{R}\mathbb{E}(Y | X = x) \mathbb{P}_X(dx)$$

Il généralise la [formule des probabilités
totales](Probabilité%20I.pdf%20#formprobatot), qui correspond ici à
$Y = 1_A$ , et $B_x = \{X = x\}$ où les $B_x$ forment cette fois une
partition non dénombrable de $\mathbb{R}$. On l'écrit souvent sous la
forme $$ \mathbb{E}\left( \mathbb{E}(Y | X) \right) = \mathbb{E}( Y )$$
et on l'appelle la *formule de l'espérance totale*.

L'espérance conditionnelle étant définie comme l'espérance selon la loi
conditionnelle, elle hérite des propriétés usuelles de l'espérance :

1.  si $Y$ et $Z$ sont intégrables,
    $\mathbb{E}(aY + bZ | X) = a \mathbb{E}(Y | X) + b \mathbb{E}(Z | X)$,
2.  $\mathbb{E}(Y | X) \geq 0$ si $Y \geq 0$,
3.  $\mathbb{E}(1 | X) = 1$.

De plus, si $g$ est borélienne positive ou $\mathbb{P}_X$-intégrable,
$$ \mathbb{E}(Y g(X) | X) = g(X) \mathbb{E}(Y | X) $$ est une
généralisation de l'égalité 1. ci-dessus, au cas où $a = g(X)$, qui doit
être considéré "comme une constante" dans le calcul de l'espérance
conditionnelle sachant $X$ ($X$ est fixée comme une donnée connue a
priori). En effet, on a alors $\mathbb{E}(g(x)Y|X=x) = g(x)\psi(x)$.
Enfin, on déduit directement du [théorème de Fubini conditionnel (p.
`\pageref*{fubinicond}`{=tex})](#fubinicond) la proposition suivante.
:::

::: {.section}
### Proposition -- Transfert conditionnel {#transfcond .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Transfert conditionnel}`{=latex}

Soient un couple $(X,Y)$ de variables aléatoires réelles de loi jointe
$\mathbb{P}_{X,Y}$ et $g$ une fonction borélienne positive ou
$\mathbb{P}_{X,Y}$-intégrable sur $\mathbb{R}^2$. On a pour
$\mathbb{P}_X$-presque tout $x$ dans $\mathbb{R}$
$$\mathbb{E}(g(X,Y)|X=x) = \mathbb{E}(g(x,Y)|X=x) = \int_{\mathbb{R}}g(x,y) \mathbb{P}_{Y|X=x} (dy)$$
Si de plus $X$ et $Y$ sont indépendantes, on a :
$$\mathbb{E}(g(X,Y)|X=x) = \mathbb{E}(g(x,Y)|X=x) = \int_{\mathbb{R}}g(x,y) \mathbb{P}_Y(dy).$$

Autrement dit, lorsqu'on conditionne par l'événement $\{X=x\}$, cela
revient à fixer la valeur de la variable aléatoire $X$ à la constante
$x$.
:::

::: {.section}
#### Exercice -- Espérance conditionnelle d'un produit de variables ($\mathord{\bullet}$) {#prod .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Espérance conditionnelle d'un produit de variables}`{=latex}

Calculer $\mathbb{E}(XY|X=x)$ puis $\mathbb{E}(XY|X)$. ([Solution p.
`\pageref*{answer-prod}`{=tex}](#answer-prod){.no-parenthesis}.)
:::

::: {.section}
Exemple : vecteurs Gaussiens à densité
--------------------------------------

Dans ce qui précède, on a décrit les lois et les espérances
conditionnelles dans le cas d'un couple de variables aléatoires à
valeurs dans $\mathbb{R}^2$. Ces résultats sont aussi valables pour des
couples de vecteurs, dont on décrit ici un cas particulier.

Dans le cas des vecteurs gaussiens à densité, c'est-à-dire dont la
matrice de covariance est définie positive et donc inversible, le calcul
des lois conditionnelles de certaines composantes par rapport aux autres
est particulièrement aisé. On va voir en particulier que les lois
conditionnelles ont le bon goût d'être elles-mêmes gaussiennes, ce qui
explique (en partie) le succès de ces modèles dans les applications.

On considère un vecteur gaussien $X = (X_1,\ldots,X_n)$ à valeurs dans
$\mathbb{R}^n$ d'espérance $m$ et de matrice de covariance $C$ définie
positive. On a vu au chapitre 2 que la densité du vecteur $X$ s'écrit
pour $x\in\mathbb{R}^d$ :
$$f_X(x) = \frac{1}{(2\pi)^{n/2}\sqrt{\det (C)}}\exp \left(-\frac{1}{2}(x-m)^t C^{-1}(x-m)\right)$$

Soit $1 \leq k < n$ un entier. On souhaite exprimer $f_{Y|Z=z}$, la
densité conditionnelle de $Y = (X_1,\ldots,X_k)$ sachant
$Z = (X_{k+1},\ldots,X_n) = (x_k,\ldots,x_n) = z$ (si $k+1 = n$, ce
vecteur se réduit à une seul valeur). On a vu que
$$f_X = f_{Y|Z=z} f_Z,$$ où $f_Z$ est la densité marginale de $Z$. On
cherche donc à décomposer $f_X$ de la sorte. On note $m = (m_Y,m_Z)$ et
on remarque que $C$ peut se décomposer en blocs : `\begin{equation*}
C = \left(\begin{array}{cc} C_Y & C_{Y,Z} \\ C_{Z,Y} & C_Z \end{array}\right)
\end{equation*}`{=tex} où $C_Y = \text{Cov}(Y,Y)$,
$C_Z = \text{Cov}(Z,Z)$ et $C_{Y,Z} = \text{Cov}(Y,Z)$. Le *complément
de Schur*[^5] du bloc $C_Y$ est la matrice
$$CS_Y = C_Y - C_{Y,Z}C_Z^{-1}C_{Z,Y}$$ et permet d'exprimer l'inverse
de $C$ comme : `\begin{equation*}
C^{-1} = \left(\begin{array}{cc} CS_Y^{-1} & -CS_Y^{-1}C_{Y,Z}C_Z^{-1} \\ -C_Z^{-1}C_{Z,Y}CS_Y^{-1}  & C_Z^{-1} + C_Z^{-1}C_{Z,Y}CS_Y^{-1}C_{Y,Z}C_Z^{-1} \end{array}\right)
\end{equation*}`{=tex} On peut alors réarranger les termes de la forme
quadratique dans $f_X$ et on obtient : `\begin{align*}
(x-m)^t C^{-1}(x-m) =& \left(y - (m_Y + C_{Y,Z}C_Z^{-1}(z-m_Z))\right)^t CS_Y^{-1}\\
&.\left(y - (m_Y + C_{Y,Z}C_Z^{-1}(z-m_Z))\right)\\
 &+ (z-m_Z)^t C_Z^{-1}(z-m_Z)
\end{align*}`{=tex} Pour la constante, on peut remarquer que :
$$ \det (C) = \det(CS_Y)\det(C_Z).$$ On en déduit ainsi que
$$f_{Y|Z=z}(y) = \frac{1}{(2\pi)^{k/2}\sqrt{\det (CS_Y)}}\exp \left(-\frac{1}{2}\left(y - \psi(z)\right)^t CS_Y^{-1}\left(y - \psi(z))\right)\right)$$

C'est-à-dire que la variable aléatoire $Y|Z=z$ est gaussienne
d'espérance $m_{Y|Z=z} = \psi(z) = m_Y + C_{Y,Z}C_Z^{-1}(z-m_Z)$ et de
matrice de covariance $CS_Y = C_Y - C_{Y,Z}C_Z^{-1}C_{Z,Y}$. Autrement
dit, l'espérance conditionnelle de $Y$ sachant $Z$ est la variable
aléatoire $\mathbb{E}(Y|Z) = \psi(Z) =(m_Y + C_{Y,Z}C_Z^{-1}(Z-m_Z))$.
On notera que la covariance conditionnelle donnée par $CS_Y$ ne dépend
pas de la valeur prise par $Z$.
:::
:::

::: {.section}
Régression et espérance conditionnelle des variables de carré intégrable
========================================================================

La régression est un ensemble de méthodes (d'apprentissage) statistiques
très utilisées pour analyser la relation d'une variable par rapport à
une ou plusieurs autres. Ces méthodes visent notamment à décrire les
liens de dépendance entre variables mais aussi de prédire au mieux la
valeur d'une quantité non observée en fonction d'une ou plusieurs autres
variables. On va en décrire ici le principe du point de vue probabiliste
dans le cas particulier des variables de carré intégrable (ou dans
$\mathcal{L}^2$). On verra dans ce cadre, que l'on rencontre très
fréquemment en pratique, une interprétation géométrique très éclairante
de l'espérance conditionnelle.

::: {.section}
Régression linéaire
-------------------

On considère deux variables aléatoires réelles, de carré intégrable,
définies sur le même espace de probabilité
$(\Omega,\mathcal{A},\mathbb{P})$, et dont on suppose connues les
variances et la covariance. Nous souhaitons trouver la meilleure
approximation de $Y$ par une fonction affine de $X$ de la forme
$aX + b$, au sens des moindres carrés, c'est-à-dire qui minimise la
quantité $\mathbb{E}((Y - (aX + b))^2)$. Il s'agit de déterminer les
constantes $a$ et $b$ telles que $\mathbb{E}((Y - (aX + b))^2)$ soit
minimale. Or, par linéarité,
$$\mathbb{E}((Y - (aX + b))^2) = \mathbb{E}(Y^2) -2a\mathbb{E}(XY) -2b \mathbb{E}(Y) +a^2\mathbb{E}(X^2) +2ab\mathbb{E}(X) +b^2.$$
L'annulation de ses dérivées partielles en à $a$ et $b$ entraîne que les
solutions sont

`\begin{align*}
a & = \frac{\text{Cov}(X,Y)}{\mathbb{V}(X)} = \rho(X,Y)\frac{\sigma_Y}{\sigma_X} \\
b & = \mathbb{E}(Y)  - a \mathbb{E}(X)
\end{align*}`{=tex}

::: {.section}
#### Exercice -- En détail ($\mathord{\bullet}$) {#detail .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{En détail}`{=latex}

Détailler le calcul de $a$ et $b$. ([Solution p.
`\pageref*{answer-detail}`{=tex}](#answer-detail){.no-parenthesis}.)
:::

::: {.section}
On vérifie aisément que ces valeurs donnent bien un minimum pour
$\mathbb{E}((Y - (aX + b))^2)$ qui est convexe, et déterminent ainsi la
meilleure approximation linéaire de $Y$ basée sur $X$ au sens de
l'erreur quadratique moyenne.

Cette approximation linéaire vaut
$$ \mathbb{E}(Y) + \rho(X,Y)\frac{\sigma_Y}{\sigma_X} (X -\mathbb{E}(X))$$
et l'erreur quadratique moyenne vaut alors `\begin{align*}
\mathbb{E}\left(\left(Y - \mathbb{E}(Y) - \rho(X,Y)\frac{\sigma_Y}{\sigma_X} (X -\mathbb{E}(X))\right)^2\right) & = \sigma_Y^2 + \rho^2(X,Y)\sigma^2_Y - 2\rho^2(X,Y)\sigma^2_Y\\
                        & = \sigma^2_Y(1-\rho^2(X,Y)).
\end{align*}`{=tex}

On voit ainsi que cette erreur est proche de 0 lorsque
$|\rho(X,Y)| \approx 1$ tandis qu'elle est proche de
$\mathbb{V}(Y) = \sigma^2_Y$ lorsque $\rho(X,Y) \approx 0$. On notera au
passage qu'on obtient que la meilleure approximation de $Y$ par une
constante est son espérance.
:::

::: {.section}
### Remarque -- Remarque {#remarque .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Remarque}`{=latex}

L'hypothèse d'une relation linéaire est très forte et pas nécessairement
toujours adaptée pour expliquer des relations de dépendances entre
variables. Soit en effet une variable aléatoire réelle $X$ de
$\mathcal{L}^3$ (i.e. $X^3$ est $\mathbb{P}_X$ intégrable) symétrique,
c'est-à-dire telle que $X$ et $-X$ sont de même loi. On a alors
$\mathbb{E}(X) = -\mathbb{E}(X) = 0$. Les variables $X$ et $X^2$ ne sont
clairement pas indépendantes. Pour autant, on a
$\text{Cov}(X,X^2) = \mathbb{E}(X^3) = -\mathbb{E}(X^3) = 0$ et le
coefficient de régression $a$ ci-dessus est nul.
:::
:::

::: {.section}
Espace de Hilbert des variables aléatoires de carré intégrable
--------------------------------------------------------------

Dans le paragraphe précédent, on s'est intéressé à approximer
linéairement une variable aléatoire $Y$ de carré intégrable par une
autre variable $X$ également de carré intégrable. On va montrer ici que
la meilleure approximation, au sens de l'erreur quadratique moyenne, de
$Y$ par une fonction de $X$ est précisément donnée par
$\psi(X) = \mathbb{E}(Y|X)$. Ce paragraphe fait appel à des notions hors
programme et est par conséquent non exigible. Il fournit néanmoins une
interprétation géométrique particulièrement frappante de l'espérance
conditionnelle.

On a besoin en pratique de travailler sur un espace un peu plus petit
que $\mathcal{L}^2$ tout entier. En effet, les outils que nous allons
utiliser ne nous permettent pas de distinguer entre deux variables $X$
et $Y$ égales presque sûrement, c'est-à-dire telles que
$\exists N \in \mathcal{A}$, tel que $\mathbb{P}(N) = 0$ et
$\forall \omega \in N^c,\,\, X(\omega) = Y(\omega)$. Cette notion
d'égalité presque sûre est une relation d'équivalence. On va ainsi
travailler avec l'espace $L^2$ des classes de variables pour l'égalité
presque sûre, c'est-à-dire que $L^2$ contiendra un unique représentant
de chacune de ces classes. Dans ce cadre, au lieu d'écrire $X=0$ p.s.,
on écrit simplement $X=0$.

On peut d'abord montrer que l'espace vectoriel $L^2$ des variables
aléatoires de carré intégrable forme un espace de Hilbert si on le munit
du produit scalaire :
$$<X,Y > = \mathbb{E}(XY) \text{   et de la norme associée   } \|X\| = \mathbb{E}(X^2)^{1/2}.$$
L'écart-type est ainsi la norme des variables centrées et la covariance
le produit scalaire des variables centrées.

Ce produit scalaire est bien défini pour tout couple $(X,Y)$ de
variables de $L^2$ puisque par l'inégalité de Cauchy-Schwartz :
$$\mathbb{E}(XY)^2 \leq \mathbb{E}(X^2)\mathbb{E}(Y^2)$$ et on a bien
$\|X\| = 0$ si et seulement si $X=0$. On peut enfin montrer que $L^2$
est complet pour la norme définie ci-dessus (voir @Jacod pour la
démonstration).

Soient maintenant $X$ et $Y \in L^2(\Omega,\mathcal{A},\mathbb{P})$. On
onsidère $L^2_X$ le sous-espace de $L^2$ constitué des (classes
d'équivalence) des variables aléatoires fonctions seulement de $X$ du
type $\phi(X)$ (avec $\phi$ telle que $\phi(X) \in L^2$). On peut
montrer que $L^2_X$ est convexe et fermé.

Alors, l'espérance conditionnelle de $Y$ sachant $X$, $\mathbb{E}(Y|X)$
s'interprète comme **la projection orthogonale** de $Y$ sur $L^2_X$.

Soit en effet l'opérateur qui à $Y \in L^2$ associe
$\mathbb{E}(Y|X) \in L^2_X$. On a vu que c'est un opérateur linéaire.
Pour montrer qu'il s'agit d'un projecteur orthogonal, on peut vérifier
qu'il est idempotent et auto-adjoint :

-   on a bien $\mathbb{E}(\mathbb{E}(Y|X)|X) = \mathbb{E}(Y|X)$
-   et pour $Z\in L^2$,
    $<Z,\mathbb{E}(Y|X) > = \mathbb{E}(Z\mathbb{E}(Y|X)) = \mathbb{E}(\mathbb{E}(Z|X)\mathbb{E}(Y|X)) = \mathbb{E}(\mathbb{E}(Z|X)\mathbb{E}(Y)) = <\mathbb{E}(Z|X),Y>$.

Le théorème de projection sur un convexe fermé dans les espaces de
Hilbert[^6] assure alors que
$$\underset{\phi(X) \in L^2_X}{\mathrm{arg}\,\mathrm{min}} \|Y-\phi(X)\|^2 = \underset{\phi(X) \in L^2_X}{{\mathrm{arg}\,\mathrm{min}}} \mathbb{E}((Y-\phi(X))^2) = \mathbb{E}(Y|X) = \psi(X)$$

Ainsi, $\mathbb{E}(Y|X)$ est la meilleure approximation (au sens des
moindres carrés) de $Y$ par une fonction de $X$.

Il est alors immédiat que le "résidu" $Y-\mathbb{E}(Y|X)$ est non
corrélé avec $X$ du fait de l'orthogonalité. On en déduit la *formule de
la variance totale* :

`\begin{align*}
\mathbb{V}(Y) = \|Y - \mathbb{E}(Y)\|^2 &=  \|Y - \mathbb{E}(Y|X) + \mathbb{E}(Y|X) - \mathbb{E}(Y)\|^2 \\
                          &=  \|Y - \mathbb{E}(Y|X)\|^2 + \|\mathbb{E}(Y|X) - \mathbb{E}(Y)\|^2 \\
                          &=  \mathbb{E}((Y - \mathbb{E}(Y|X))^2) + \mathbb{E}((\mathbb{E}(Y|X) - \mathbb{E}(Y))^2)\\
                          &= \mathbb{E}(\mathbb{E}((Y - \mathbb{E}(Y|X))^2|X)) + \mathbb{V}(\mathbb{E}(Y|X))\\
                          &= \mathbb{E}(\mathbb{V}(Y|X)) + \mathbb{V}(\mathbb{E}(Y|X)).
\end{align*}`{=tex} où on a utilisé la formule de l'espérance totale et
introduit la variable aléatoire variance conditionnelle
$\mathbb{V}(Y|X) = \mathbb{E}((Y - \mathbb{E}(Y|X))^2|X)$ comme cas
particulier de la [définition vue plus haut (p.
`\pageref*{defespcondg}`{=tex})](#defespcondg).

::: {.section}
#### Exercice -- Variance totale ($\mathord{\bullet}$) {#vartot .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Variance totale}`{=latex}

Redémontrer ce résultat sans utiliser la notion d'orthogonalité.
([Solution p.
`\pageref*{answer-vartot}`{=tex}](#answer-vartot){.no-parenthesis}.)
:::
:::
:::

::: {.section}
Exercices
=========

::: {.section}
Couple de variables
-------------------

Soient $X$ et $Y$ deux v.a. réelles. On suppose que la densité
conditionnelle de $X$ sachant $Y = y$ est la densité
$1_{\mathbb{R}_+}(x)y^2 xe^{-xy}$ et que la loi de $Y$ est de densité
$\frac{1}{y^2} 1_{[1,+\infty[} (y)$. On pose $T = XY$.

::: {.section}
#### Question 1 {#ex1-1 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Trouver la loi du couple $(T,Y)$. Qu'en déduit-on ? ([Solution p.
`\pageref*{answer-ex1-1}`{=tex}](#answer-ex1-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 {#ex1-2 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Trouver la loi conditionnelle de $Y$ sachant $X = x$. ([Solution p.
`\pageref*{answer-ex1-2}`{=tex}](#answer-ex1-2){.no-parenthesis}.)
:::

::: {.section}
#### Question 3 {#ex1-3 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Calculer $E(Y |X)$. ([Solution p.
`\pageref*{answer-ex1-3}`{=tex}](#answer-ex1-3){.no-parenthesis}.)
:::
:::

::: {.section}
Mélanges de lois
----------------

*Adapté du cours de probabilités de S. Bonnabel et M. Schmidt (MINES
ParisTech).*

Pour modéliser un phénomène multimodal, on utilise souvent des mélanges
de gaussiennes. C'est le cas notamment en classification non-supervisée,
où on fait l'hypothèse que chacune des classes suit une loi gaussienne.
Soient $n\in\mathbb{N}^\ast$ et $K$ une variable aléatoire prenant les
valeurs $1,\dots,n$ avec les probabilités non nulles $p_1,\dots,p_n$
telles que $\sum_{i = 1}^n p_i = 1$. Soient $X_1,\dots,X_n$ des
variables aléatoires gaussiennes mutuellement indépendantes,
d'espérances respectives $m_1,\dots,m_n \in \mathbb{R}$ et de variances
respectives $\sigma_1^2,\dots,\sigma_n^2 \in\mathbb{R}_+^\ast$, toutes
indépendantes de $K$. On appelle mélange de gaussiennes la loi de la
variable aléatoire $X = X_K$. Pour tout $i\in\{1,\dots,n\}$, on notera
$f_i$ la densité de la variable aléatoire $X_i$.

::: {.section}
#### Question 1 {#melloi1 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Soit $i \in \{1,\dots,n\}$. Quelle est la densité $f_{X\mid K = i}$ de
$X$ conditionnellement à l'événement $\{K = i\}$ ? ([Solution p.
`\pageref*{answer-melloi1}`{=tex}](#answer-melloi1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 {#melloi2 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Calculer la densité de probabilité de la variable $X$. ([Solution p.
`\pageref*{answer-melloi2}`{=tex}](#answer-melloi2){.no-parenthesis}.)
:::

::: {.section}
#### Question 3 {#melloi3 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Calculer $\mathbb{E}(X)$. Montrer que
$\mathbb{V}(X) = \sum_{i = 1}^n p_i\sigma_i^2 + \bar{\sigma}^2$, où ce
dernier terme peut être interprété comme la dispersion des espérances.
([Solution p.
`\pageref*{answer-melloi3}`{=tex}](#answer-melloi3){.no-parenthesis}.)
:::

::: {.section}
#### Question 4 {#melloi4 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 4}`{=latex}

Comment approximeriez-vous le mélange par une unique gaussienne ? Faire
un schéma dans le cas $m = 2$. ([Solution p.
`\pageref*{answer-melloi4}`{=tex}](#answer-melloi4){.no-parenthesis}.)
:::
:::

::: {.section}
Lois conjuguées
---------------

Soit un vecteur aléatoire $(X,Y)$ de loi jointe $\mathbb{P}_{X,Y}$.
Expliciter la loi conditionnelle de $Y$ sachant $\{X=x\}$ dans les
situations suivantes, en prenant soin d'expliciter pour quelles valeurs
de $x$ ces dernières ont du sens.

::: {.section}
#### Question 1 {#loiconj-expexp .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

$Y$ suit une loi Exponentielle de paramètre
$\lambda \in\mathbb{R}_+^\ast$ et pour tout $y\in\mathbb{R}_+^\ast$, la
variable aléatoire $X$ sachant $\{Y=y\}$ suit une loi Exponentielle de
paramètre $y$. ([Solution p.
`\pageref*{answer-loiconj-expexp}`{=tex}](#answer-loiconj-expexp){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 {#loiconj-gampoi .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

$Y$ suit une loi Gamma de paramètres
$\alpha,\theta \in \mathbb{R}_+^\ast$ et pour tout
$y\in\mathbb{R}_+^\ast$, la variable aléatoire $X$ sachant $\{Y=y\}$
suit une loi de Poisson de paramètre $y$. ([Solution p.
`\pageref*{answer-loiconj-gampoi}`{=tex}](#answer-loiconj-gampoi){.no-parenthesis}.)
:::
:::

::: {.section}
Randomisation {#randomize .question .unnumbered .unlisted}
-------------

`\addcontentsline{toc}{subsection}{Randomisation}`{=latex}

*Extrait du cours de probabilités de S. Bonnabel et M. Schmidt (MINES
ParisTech).*

Des clients arrivent à la boutique SNCF du boulevard Saint-Michel à des
instants aléatoires. On note $T_0$ l'heure d'ouverture puis
$T_1, T_2, \dots$ les temps successifs d'arrivée des clients jusqu'à
l'heure de fermeture. Les études statistiques montrent qu'on peut, dans
une tranche horaire donnée, supposer que les temps d'attente
$X_1 = T_1 -T_0, X_2 = T_2 -T_1,\dots$ peuvent être modélisés par des
variables aléatoires indépendantes et de même loi qu'une variable
aléatoire positive $X$. Par ailleurs, une loterie interne décide que
chaque jour dans la tranche horaire considérée, le $N^{\text{ème}}$
client sera l'heureux gagnant d'un trajet gratuit Paris-La Ciotat, où
$N$ est une variable aléatoire bornée dont la loi dépend du processus de
loterie (e.g. tous les clients entre le premier et le $30^{\text{ème}}$
ont une chance $1/30$ d'être tirés au sort, en supposant qu'on est sûr
d'avoir au moins $30$ clients dans la tranche horaire).

On se demande alors : quel est le temps d'attente moyen avant d'obtenir
un gagnant ? ([Solution p.
`\pageref*{answer-randomize}`{=tex}](#answer-randomize){.no-parenthesis}.)
:::

::: {.section}
Etats cachés --- indépendance conditionnelle
--------------------------------------------

Soucieux de l'évolution du potager de l'école, des élèves à la main
verte s'intéressent à l'évolution de la température dans le jardin côté
Luxembourg. Ils récupèrent pour cela un thermomètre dans un laboratoire,
l'installent près du potager, et en relèvent les mesures à intervalles
de temps réguliers. Les résultats les surprennent rapidement : les
températures affichées ne correspondent pas à celles prévues par
météo-France. Leur thermomètre est sans doute déréglé.

On se propose de les aider à comprendre le phénomène dont ils sont
témoins à l'aide d'un modèle probabiliste particulier, nommé *modèle de
Markov caché*. Précisément, on considère la suite des vraies
températures que l'on aurait souhaité relever comme une suite de v.a.r.
non indépendantes $(X_n)_{n\in\mathbb{N}^\ast}$, dite *d'états cachés*
(on ne les observe pas directement). Les erreurs commises par le
thermomètre sont quant à elles modélisées par une suite de v.a.r.
$(\epsilon_n)_{n\in\mathbb{N}^\ast}$, toutes indépendantes et de même
loi admettant une densité $f_\epsilon$. Elles sont supposées
indépendantes de la suite $(X_n)_{n\in\mathbb{N}^\ast}$ (l'erreur du
thermomètre lui est propre et ne dépend pas de la température réelle). A
chaque instant $n\in\mathbb{N}^\ast$, on suppose que la mesure du
thermomètre est la variable aléatoire $$Y_n = X_n + \epsilon_n,$$ et que
le vecteur aléatoire $(X_1,\dots,X_n)$ possède une densité jointe notée
$f_{1:n}$.

::: {.section}
#### Question 1 {#ec1 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Montrer que pour tout $n \in \mathbb{N}^\ast$ et tout $x\in\mathbb{R}$,
la loi de $Y_n$ sachant $\{X_n = x\}$ admet une densité, que l'on
explicitera. ([Solution p.
`\pageref*{answer-ec1}`{=tex}](#answer-ec1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 {#ec2 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Montrer que les $n\in\mathbb{N}^\ast$ relevés de température
$Y_1,\dots,Y_n$ sont indépendants **conditionnellement** aux états
cachés $X_1,\dots,X_n$. ([Solution p.
`\pageref*{answer-ec2}`{=tex}](#answer-ec2){.no-parenthesis}.)
:::
:::

::: {.section}
Covariance totale {#covtot .question .unnumbered .unlisted}
-----------------

`\addcontentsline{toc}{subsection}{Covariance totale}`{=latex}

Soient $X$, $Y$ et $Z$ trois variables aléatoires réelles de carré
intégrable. La covariance conditionnelle de $X$ et $Y$ sachant $Z$ est
définie comme la variable aléatoire
$$\text{Cov}(X,Y \mid Z) = \mathbb{E}\Bigl( \bigl( X - \mathbb{E}(X\mid Z) \bigr)\bigl( Y - \mathbb{E}(Y\mid Z) \bigr) \Bigm| Z  \Bigr).$$

Etablir la formule de la covariance totale :
$$\text{Cov}(X,Y) = \mathbb{E}\bigl(\text{Cov}(X,Y\mid Z)\bigr) + \text{Cov}\bigl( \mathbb{E}(X\mid Z), \mathbb{E}(Y\mid Z) \bigr).$$

([Solution p.
`\pageref*{answer-covtot}`{=tex}](#answer-covtot){.no-parenthesis}.)
:::

::: {.section}
Non-réponse
-----------

*Inspiré du cours de probabilité de M. Christine (ENSAE ParisTech).*

Un questionnaire est diffusé aux $n\in\mathbb{N}^\ast$ étudiants de
l'école pour savoir combien de temps ils ont consacré à l'étude des
probabilités ce semestre. On note $Y_i$ le temps de travail de
l'étudiant $i \in \{1,\dots,n\}$ et $X_i$ la variable valant $1$ s'il a
répondu au questionnaire et $0$ sinon. On suppose que les
$(X_1,Y_1),\dots,(X_n,Y_n)$ sont des vecteurs aléatoires indépendants de
même distribution qu'un vecteur générique $(X,Y)$ tel que

-   $X$ est une variable de Bernoulli de paramètre $p\in\,]0,1[$
    indiquant la probabilité de réponse,
-   $Y$ est positive, de carré intégrable, d'espérance
    $m\in\mathbb{R}_+$ et de variance $\sigma^2 \in\mathbb{R}_+^\ast$.
    Le coefficient de corrélation entre $X$ et $Y$ est enfin noté
    $\rho \in [-1,1]$.

::: {.section}
#### Question 1 {#nonrep1 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

En reprenant la définition de l'espérance conditionnelle
$\mathbb{E}(Y\mid X)$ comme meilleure approximation au sens des moindres
carrés de $Y$ par une fonction de $X$, montrer qu'elle coïncide ici avec
l'approximation affine de $Y$ par $X$ puis l'écrire en fonction de $m$,
$\rho$, $\sigma$ et $p$. ([Solution p.
`\pageref*{answer-nonrep1}`{=tex}](#answer-nonrep1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 {#nonrep2 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

On pose $m_0 := \mathbb{E}(Y\mid X = 0)$ et
$m_1 = \mathbb{E}(Y\mid X = 1)$. Calculer $m_0$ et $m_1$ en fonction de
$m$, $\rho$, $\sigma$ et $p$. ([Solution p.
`\pageref*{answer-nonrep2}`{=tex}](#answer-nonrep2){.no-parenthesis}.)
:::

::: {.section}
#### Question 3 {#nonrep3 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

On pose $\sigma^2_0 := \mathbb{V}\left(Y\mid X = 0\right)$ et
$\sigma^2_1 := \mathbb{V}\left(Y\mid X = 1\right)$. Vérifier l'égalité
$$\sigma^2 = \dfrac{(1-p)\,\sigma^2_0 + p\,\sigma^2_1}{1-\rho^2}.$$

([Solution p.
`\pageref*{answer-nonrep3}`{=tex}](#answer-nonrep3){.no-parenthesis}.)
:::

::: {.section}
#### Question 4 {#nonrep4 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 4}`{=latex}

Que dire des résultats obtenus aux questions 2 et 3 lorsque :

-   $X$ et $Y$ sont non corrélées,
-   $X$ et $Y$ sont indépendantes ?

------------------------------------------------------------------------

([Solution p.
`\pageref*{answer-nonrep4}`{=tex}](#answer-nonrep4){.no-parenthesis}.)
:::
:::
:::

::: {.section}
Solutions
=========

::: {.section}
#### Dans un triangle (1) {#answer-etb1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Dans un triangle (1)}`{=latex}

La densité marginale de $X$ est donnée par
$f_X(x) = \int f_{X,Y}(x,y) dy = 1_{]0,1[}(x)$ et pour $x \in ]0,1[$,
$$f_{Y|X=x} (y) = \frac{1}{x} 1_{]0,x[}(y)$$ Ainsi $X$ est uniformément
distribué sur $]0,1[$, et la loi de $Y$ sachant $X =x$ est uniforme sur
$]0,x[$ pour $(0 < x < 1)$.
:::

::: {.section}
#### Dans un triangle (2) {#answer-etb2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Dans un triangle (2)}`{=latex}

Pour un tel $x$, l'espérance conditionnelle $\mathbb{E}(Y|X=x)$ vaut
ainsi $x/2$ et nous obtenons $\mathbb{E}(Y|X) = \frac{X}{2}$.
:::

::: {.section}
#### Auto-conditionnement {#answer-autocond .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Auto-conditionnement}`{=latex}

On a $\psi(y) = \mathbb{E}(Y|Y=y) = y$ et donc
$\mathbb{E}(Y|Y) = \psi(Y) = Y$ p.s.
:::

::: {.section}
#### Espérance conditionnelle d'un produit de variables {#answer-prod .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Espérance conditionnelle d'un produit de variables}`{=latex}

On a $\mathbb{E}(XY|X = x) = x\mathbb{E}(Y|X=x)$, d'où
$\mathbb{E}(XY|X) = X\mathbb{E}(Y|X)$ p.s.
:::

::: {.section}
#### En détail {#answer-detail .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{En détail}`{=latex}

Notons $J(a,b) = \mathbb{E}((Y-(aX+b))^2)$
$$\frac{\partial J(a,b)}{\partial b} = -2\mathbb{E}(Y^2) + 2a \mathbb{E}(X) + 2b$$
d'où $b = \mathbb{E}(Y) - a \mathbb{E}(X)$

Par ailleurs, `\begin{align*}
\frac{\partial J(a,b)}{\partial a} & = -2\mathbb{E}(XY) + 2a \mathbb{E}(X^2) + 2b \mathbb{E}(X)\\
                                   & = -2\mathbb{E}(XY) + 2a \mathbb{E}(X^2) + 2\mathbb{E}(X)\mathbb{E}(Y) - 2 a \mathbb{E}(X^2)\\
                                   & = -2\text{Cov}(X,Y) + a\mathbb{V}(X)
\end{align*}`{=tex}

d'où
$a = \frac{\text{Cov}(X,Y)}{\mathbb{V}(X)} = \rho(X,Y)\frac{\sigma_Y}{\sigma_X}$
:::

::: {.section}
#### Variance totale {#answer-vartot .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Variance totale}`{=latex}

`\begin{align*}
\mathbb{V}(Y) =& \mathbb{E}((Y-\mathbb{E}(Y))^2) = \mathbb{E}(\mathbb{E}((Y-\mathbb{E}(Y))^2|X)) \text{   par la formule de l'espérance totale}\\
=& \mathbb{E}(\mathbb{E}((Y-\mathbb{E}(Y|X)+\mathbb{E}(Y|X)-\mathbb{E}(Y))^2|X)) \\
=& \mathbb{E}(\mathbb{E}((Y-\mathbb{E}(Y|X))^2|X)) + \mathbb{E}(\mathbb{E}((\mathbb{E}(Y|X)-\mathbb{E}(Y))^2|X)) \\
 &+ 2\mathbb{E}(\mathbb{E}((Y-\mathbb{E}(Y|X))(\mathbb{E}(Y|X)-\mathbb{E}(Y))|X))\\
=& \mathbb{E}(\mathbb{V}(Y|X)) + \mathbb{E}((\mathbb{E}(Y|X)-\mathbb{E}(Y))^2) + 2\mathbb{E}((\mathbb{E}(Y|X)-\mathbb{E}(Y))\mathbb{E}((Y-\mathbb{E}(Y|X))|X))\\
=& \mathbb{E}(\mathbb{V}(Y|X)) + \mathbb{V}(\mathbb{E}(Y|X)) \text{   car    } \mathbb{E}((Y-\mathbb{E}(Y|X))|X) = 0 
\end{align*}`{=tex}
:::

::: {.section}
Couple de variables
-------------------

::: {.section}
#### Question 1 {#answer-ex1-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

On voit d'abord que la densité du couple $(X,Y)$ vaut :
$$f_{X,Y}(x,y) = f_{X|Y=y}(x)f_Y(y) = xe^{-xy}1_{\mathbb{R}_+}(x) 1_{[1,+\infty[} (y)$$
Soit $h$ une fonction continue bornée sur $\mathbb{R}^2_+$. Le
changement de variable $(x, y) \mapsto (t = xy , y)$ de jacobien $y$,
donne alors que
$$\mathbb{E}(h(T, Y )) = \mathbb{E}(h(XY, Y )) = \int_1^{+\infty}\int_0^{+\infty} h(t,y) e^{-t} \frac{t}{y^2} dt dy$$
et donc la densité du couple $(T, Y)$ vaut
$$f_{T,Y} = e^{-t} \frac{t}{y^2}1_{[1,+\infty[} (y)1_{\mathbb{R}_+}(t)$$
Elle s'écrit comme produit d'une fonction de $t$ et d'une fonction de
$y$. On en déduit que $T$ et $Y$ sont indépendantes et que $T$ a pour
densité $te^{-t} 1_{\mathbb{R}_+}(t)$.
:::

::: {.section}
#### Question 2 {#answer-ex1-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

La loi marginale de $X$ a pour densité
$f_X (x) = \int_1^{+\infty} x e^{-xy} dy = e^{-x}$. Ainsi $X$ suit une
loi exponentielle de paramètre 1 et la loi conditionnelle de $Y$ sachant
$X = x$ admet la densité :
$$f_{Y|X=x}(y) = \frac{f_{X,Y}(x,y)}{f_X(x)} = x e^{-x(y-1)} 1_{[1,+\infty[} (y)$$
pour x \> 0.
:::

::: {.section}
#### Question 3 {#answer-ex1-3 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

On en déduit que
$$\mathbb{E}(Y|X=x ) = \int_1^{+\infty} y x e^{-x(y-1)} dy = \frac{x+1}{x}1_{\mathbb{R}_+}(x)$$
par intégration par parties. Ainsi $\mathbb{E}(Y|X) = \frac{X+1}{X}$.
:::
:::

::: {.section}
Mélanges de lois
----------------

::: {.section}
#### Question 1 {#answer-melloi1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Soit $B$ un borélien. Par indépendance de $K$ avec $X_i$, on a
$$\mathbb{P}(X \in B \mid K = i) = \mathbb{P}(X_i \in B \mid K = i) = \mathbb{P}(X_i \in B).$$
La loi de $X$ sachant $\{K = i\}$ est donc la même que celle de $X_i$,
d'où
$$f_{X\mid K = i} : x\in\mathbb{R}\mapsto f_i(x) = \dfrac{1}{\sqrt{2\pi}\sigma_i}\,\exp\left\{- \dfrac{(x-m_i)^2}{2\sigma_i^2} \right\}.$$
:::

::: {.section}
#### Question 2 {#answer-melloi2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Soit $B$ un borélien. D'après la formule des probabilités totales et la
question précédente, on a
$$\mathbb{P}(X\in B) = \sum_{i = 1}^n p_i\,\mathbb{P}(X \in B \mid K = i) = \sum_{i = 1}^n p_i\,\mathbb{P}(X_i \in B).$$
La variable aléatoire $X$ admet donc une densité, qui vaut
$$f_X : x\in\mathbb{R}\mapsto \sum_{i = 1}^n p_i\,f_i(x).$$
:::

::: {.section}
#### Question 3 {#answer-melloi3 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

D'après la question précédente, $X$ a pour espérance `\begin{align*}
\mathbb{E}(X) &= \int_\mathbb{R}x\,f_X(x)\,dx = \int_\mathbb{R}x \sum_{i = 1}^n p_i\, f_i(x)\,dx =  \sum_{i = 1}^n p_i \int_\mathbb{R}x\,f_i(x)\,dx\\
& = \sum_{i = 1}^n p_i\,m_i.
\end{align*}`{=tex} Quant à la variance de $X$, en utilisant l'égalité
$\sum_{i= 1}^n p_i = 1$, elle vaut `\begin{align*}
\mathbb{V}(X) &= \mathbb{E}\left(X^2\right) - \mathbb{E}(X)^2 = \int_\mathbb{R}x^2\,f_X(x)\,dx - \left(\sum_{i = 1}^n p_i\,m_i\right)^2\\
&= \sum_{i = 1}^n p_i (\sigma_i^2 + m_i^2) - \sum_{i = 1}^n p_i\left(\sum_{j = 1}^n p_j\,m_j\right)^2\\
&= \sum_{i = 1}^n p_i\,\sigma_i^2 + \sum_{i = 1}^n p_i \left(m_i - \sum_{j=1}^n p_j\,m_j \right)^2.
\end{align*}`{=tex} On retrouve bien la forme désirée, avec la
dispersion des espérances
$$\bar{\sigma}^2 := \sum_{i = 1}^n p_i \left(m_i - \sum_{j=1}^n p_j\,m_j \right)^2.$$
:::

::: {.section}
#### Question 4 {#answer-melloi4 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 4}`{=latex}

Si l'on souhaite approcher la loi de $X$ avec une unique Gaussienne, et
non un mélange, les questions précédentes suggèrent de prendre celle
d'espérance $\sum_{i =1}^n p_i\,m_i$ et de variance
$\sum_{i = 1}^n p_i\,\sigma^2_i + \bar{\sigma}^2$. Voir figure
ci-dessous.

![Illustration](images/PdfMelGauss.tex.pdf)
:::
:::

::: {.section}
Lois conjuguées {#answer-loiconj .answer .unnumbered .unlisted}
---------------

`\addcontentsline{toc}{subsection}{Lois conjuguées}`{=latex}

On considère dans tout cet exercice $B_1$ et $B_2$ des Boréliens.

::: {.section}
#### Question 1 {#answer-loiconj-expexp .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

D'après les hypothèses on a `\begin{align*}
\mathbb{P}_{X,Y}(B_1\times B_2) &= \int_{B_2} \left(\int_{B_1} \mathbb{P}_{X\mid Y = y}(dx) \right) \mathbb{P}_Y(dy) \hspace{1em}\text{par Fubini conditionnel,}\\
&= \int_{B_2} \left(\int_{B_1} y\,e^{-y x}\,1_{\mathbb{R}_+^\ast}(x)\,dx \right) \lambda\,e^{-\lambda y}\,1_{\mathbb{R}_+^\ast}(y)\,dy\\
&= \int_{B_1} \int_{B_2} \lambda\, y\,e^{-(x+\lambda)\,y}1_{\mathbb{R}_+^\ast}(x)\,1_{\mathbb{R}_+^\ast}(y) \,dy\, dx \hspace{1em}\text{par Fubini.}
\end{align*}`{=tex} Le vecteur aléatoire $(X,Y)$ possède donc une
densité jointe
$$f_{X,Y} : (x,y) \in\mathbb{R}^2 \mapsto \lambda\, y\,e^{-(x+\lambda)\,y}1_{\mathbb{R}_+^\ast}(x)\,1_{\mathbb{R}_+^\ast}(y).$$
La variable aléatoire $X$ a donc aussi une densité : pour tout
$x\in\mathbb{R}$ `\begin{align*}
f_X(x) &= \int_{\mathbb{R}} f_{X,Y}(x,y)\,dy = \int_\mathbb{R}\lambda\, y\,e^{-(x+\lambda)\,y}1_{\mathbb{R}_+^\ast}(x)\,1_{\mathbb{R}_+^\ast}(y)\,dy\\
&= \left|\begin{array}{ll}\displaystyle \dfrac{\lambda}{x+\lambda} \int_{0}^{+\infty} y\,(x+\lambda)\,e^{-(x+\lambda)\,y}\,dy & \text{si } x>0,\\[1em] 0 & \text{sinon.} \end{array}\right.
\end{align*}`{=tex} On reconnaît dans cette dernière intégrale la
formule de l'espérance d'une loi Exponentielle de paramètre $x+\lambda$,
et on en déduit que pour tout $x\in\mathbb{R}$
$$f_X(x) = \dfrac{\lambda}{(x+\lambda)^2}\,1_{\mathbb{R}_+^\ast}(x).$$
Pour tout $x\in\mathbb{R}_+^\ast$ la variable $Y$ sachant $\{X=x\}$
admet donc aussi une densité, que l'on explicite avec la formule de
Bayes : pour tout $y\in\mathbb{R}$ `\begin{align*}
f_{Y\mid X=x}(y) &= \dfrac{f_{X,Y}(x,y)}{f_X(x)} = \dfrac{\lambda\, y\,e^{-(x+\lambda)\,y}\,1_{\mathbb{R}_+^\ast}(y)}{\dfrac{\lambda}{(x+\lambda)^2}}\\
&= (x+\lambda)^2\,y\,e^{-(x+\lambda)\,y}\,1_{\mathbb{R}_+\ast}(y).
\end{align*}`{=tex} Comme $\Gamma(2) = 1$, on reconnaît ici la densité
d'une loi Gamma d'indice $2$ et de paramètre d'échelle $x+\lambda$.
:::

::: {.section}
#### Question 2 {#answer-loiconj-gampoi .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

D'après les hypothèses, en procédant comme précédemment, on a
`\begin{align*}
\mathbb{P}_{X,Y}(B_1\times B_2) &= \int_{B_2} \left(\int_{B_1} \mathbb{P}_{X\mid Y = y}(dx) \right) \mathbb{P}_Y(dy)\\
&= \int_{B_2} \left(\sum_{x\in B_1} \dfrac{y^{x}}{x!}\,e^{-y}\,1_{\mathbb{N}}(x) \right) \dfrac{\theta^{\alpha}}{\Gamma(\alpha)}\,y^{\alpha-1}e^{-\theta y}\,1_{\mathbb{R}_+}(y)\,dy\\
&= \sum_{x\in B_1\cap\mathbb{N}} \left(\dfrac{1}{x!} \int_{B_2\cap\mathbb{R}_+} \dfrac{\theta^{\alpha}}{\Gamma(\alpha)}\,y^{x+\alpha-1}e^{-(\theta+1) y}\,dy\right)\\
&= \sum_{x\in B_1\cap\mathbb{N}} \biggl(\dfrac{\Gamma(x+\alpha)\,\theta^\alpha}{x!\,\Gamma(\alpha)\,(\theta+1)^{x+\alpha}}\\
&\hspace{5em} \times \int_{B_2\cap\mathbb{R}_+} \dfrac{(\theta+1)^{x+\alpha}}{\Gamma(x+\alpha)}\,y^{x+\alpha-1}e^{-(\theta+1) y}\,dy\biggr).
\end{align*}`{=tex} On reconnaît dans cette dernière intégrale la
densité d'une loi Gamma d'indice $x+\alpha$ et de paramètre d'échelle
$\theta+1$, qui correspond exactement à la loi conditionnelle de $Y$
sachant $\{X=x\}$ pour $x\in\mathbb{N}$. En effet, on a d'une part
`\begin{align*}
\mathbb{P}_X(B_1) &= \mathbb{P}_{X,Y}(B_1 \times \mathbb{R}) = \sum_{x\in B_1\cap\mathbb{N}} \dfrac{\theta^\alpha}{\Gamma(\alpha)}\, \dfrac{\Gamma(x+\alpha)}{x!\,(\theta+1)^{x+\alpha}},
\end{align*}`{=tex} ce qui donne bien pour tout $x\in\mathbb{N}$ :
`\begin{align*}
\mathbb{P}_{Y\mid X=x} (B_2) &= \mathbb{P}\left(Y \in B_2 \mid X = x\right) = \dfrac{\mathbb{P}_{X,Y}\left(\{x\}\times B_2\right)}{\mathbb{P}_X(\{x\})}\\
&= \int_{B_2\cap\mathbb{R}_+} \dfrac{(\theta+1)^{x+\alpha}}{\Gamma(x+\alpha)}\,y^{x+\alpha-1}\,e^{-(\theta+1)y}\,dy.
\end{align*}`{=tex}
:::
:::

::: {.section}
Randomisation {#answer-randomize .answer .unnumbered .unlisted}
-------------

`\addcontentsline{toc}{subsection}{Randomisation}`{=latex}

En termes probabilistes et selon les notations de l'exercice, il s'agit
de calculer $\mathbb{E}(T_N - T_0)$, où la variable aléatoire $T_N$ peut
s'écrire en fonction d'une somme aléatoire de variables aléatoires
indépendantes : $$T_N = \sum_{i = 1}^N X_i + T_0.$$ Comme la boutique
ferme au bout d'un certain temps, toutes les variables aléatoires
figurant dans l'équation précédente sont bornées, donc intégrables. On
peut ainsi calculer $\mathbb{E}(T_N-T_0)$ à l'aide de la formule de
l'espérance totale :
$$\mathbb{E}\left(T_N - T_0\right) = \mathbb{E}\left(\mathbb{E}\left(T_N \mid N\right)\right) - T_0.$$
Pour tout $n\in\mathbb{N}^\ast$ l'énoncé suggère que $N$ est
indépendante de $X_1,\dots,X_n$, elles-mêmes indépendantes et de même
loi que $X$, d'où :
$$\mathbb{E}\left(T_n \mid N = n\right) = \sum_{i = 1}^n \mathbb{E}(X_i\mid N = n) = \sum_{i = 1}^n \mathbb{E}(X_i) = n\mathbb{E}(X).$$
Ainsi, en posant $\psi : n \in\mathbb{N}^\ast \mapsto n \mathbb{E}(X)$,
on obtient
$$\mathbb{E}\left(T_N - T_0\right) = \mathbb{E}\left(\psi(N)\right) - T_0 = \mathbb{E}(N)\mathbb{E}(X) - T_0.$$
C'était prévisible : en posant arbitrairement $T_0 = 0$, le temps
d'attente moyen est le temps d'attente moyen entre deux arrivées,
multiplié par le rang moyen du gagnant. Si la loterie dépendait des
temps d'arrivées, par exemple en faisant gagner le premier client qui
arrive au moins 10 minutes après le client précédent, $\psi$, et donc le
résultat, seraient différents.
:::

::: {.section}
Etats cachés --- indépendance conditionnelle
--------------------------------------------

::: {.section}
#### Question 1 {#answer-ec1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Soit $n\in\mathbb{N}^\ast$. Quels que soient $x\in\mathbb{R}$ et $B$
borélien on a `\begin{align*}
\mathbb{P}_{Y_n \mid X_n = x}(B) &= \mathbb{E}\left(1_B(X_n+\epsilon_n) \mid X_n = x \right)\\
&= \int_\mathbb{R}1_B(x+y)\,\mathbb{P}_{\epsilon_n\mid X_n = x}(dy)\\
& = \int_\mathbb{R}1_B(x+y)\,f_\epsilon(y)\,dy \hspace{1em}\text{par indépendance de $X_n$ et $\epsilon_n$}\\
&= \int_B f_\epsilon(y-x)\,dy.
\end{align*}`{=tex} Ainsi, $\mathbb{P}_{Y_n\mid X_n =x}$ admet bien une
densité :
$$f_{Y_n\mid X_n=x} : y \in\mathbb{R}\mapsto f_\epsilon(y - x).$$
:::

::: {.section}
#### Question 2 {#answer-ec2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Soient $n\in\mathbb{N}^\ast$, $(x_1,\dots,x_n)\in\mathbb{R}^n$ et
$B_1,\dots,B_n$ des boréliens. Pour simplifier les écritures, on note
$x_{1:n}$ tout vecteur $(x_1,\dots,x_n)$ de $\mathbb{R}^n$. Alors
`\begin{align*}
&\mathbb{P}_{Y_{1:n}\mid X_{1:n}=x_{1:n}}(B_1\times\dots\times B_n)
=\mathbb{E}\left(\prod_{i = 1}^n 1_{B_i}(X_i + \epsilon_i) \Bigm\vert X_{1:n} = x_{1:n} \right)\\
&= \int_{\mathbb{R}^n} \prod_{i = 1}^n 1_{B_i}(x_i + y_i)\,\mathbb{P}_{\epsilon_{1:n}\mid X_{1:n} = x_{1:n}}(dy_{1:n})\\
&= \int_{\mathbb{R}^n} \prod_{i = 1}^n 1_{B_i}(x_i + y_i)\,\mathbb{P}_{\epsilon_{1:n}}(dy_{1:n}) \ \text{par indépendance des $\epsilon_i$ et $X_j$,}\\
&= \prod_{i = 1}^n \int_{\mathbb{R}} 1_{B_i}(x_i + y_i)\,f_\epsilon(x_i)\,dy_{i} \ \text{par Fubini et indépendance et même loi des $\epsilon_i$,}\\
&= \prod_{i = 1}^n \int_{\mathbb{R}} 1_{B_i}(y_i)\,f_\epsilon(y_i - x_i)\,dy_i\\
& = \prod_{i = 1}^n \int_{\mathbb{R}} 1_{B_i}(y_i)\,f_{Y_i\mid X_i = x_i}(y_i)\,dy_i\ \text{par la question 1,}\\
&= \prod_{i = 1}^n \mathbb{P}_{Y_i\mid X_i = x_i}(B_i).
\end{align*}`{=tex} Les $n$ relevés de température sont donc bien
indépendants conditionnellement aux états cachés.
:::
:::

::: {.section}
Covariance totale {#answer-covtot .answer .unnumbered .unlisted}
-----------------

`\addcontentsline{toc}{subsection}{Covariance totale}`{=latex}

Tout d'abord, par linéarité de l'espérance conditionnelle on a :
`\begin{align*}
\text{Cov}(X,Y \mid Z) &= \mathbb{E}\Bigl( \bigl( X - \mathbb{E}(X\mid Z) \bigr)\bigl( Y - \mathbb{E}(Y\mid Z) \bigr) \Bigm| Z  \Bigr)\\
&= \mathbb{E}\Bigl( XY - X\mathbb{E}(Y\mid Z) - Y\mathbb{E}(X\mid Z) + \mathbb{E}(X\mid Z)\mathbb{E}(Y\mid Z) \Bigm| Z  \Bigr)\\
&= \mathbb{E}(XY \mid Z) - \mathbb{E}(X\mid Z)\mathbb{E}(Y\mid Z).
\end{align*}`{=tex}

En utilisant la formule de l'espérance totale et la linéarité de
l'espérance, on obtient alors `\begin{align*}
\text{Cov}(X,Y) &= \mathbb{E}(XY) - \mathbb{E}(X)\mathbb{E}(Y)\\
&= \mathbb{E}\bigl( \mathbb{E}(XY \mid Z) \bigr) - \mathbb{E}\bigl( \mathbb{E}(X \mid Z) \bigr)\mathbb{E}\bigl( \mathbb{E}(Y \mid Z) \bigr)\\
&= \mathbb{E}\bigl( \mathbb{E}(XY \mid Z) - \mathbb{E}(X\mid Z)\mathbb{E}(Y\mid Z) \bigr)\\
&\ \ \  + \mathbb{E}\bigl( \mathbb{E}(X\mid Z)\mathbb{E}(Y\mid Z) \bigr) - \mathbb{E}\bigl( \mathbb{E}(X \mid Z) \bigr)\mathbb{E}\bigl( \mathbb{E}(Y \mid Z) \bigr)\\
&= \mathbb{E}\bigl(\text{Cov}(X,Y\mid Z)\bigr) + \text{Cov}\bigl( \mathbb{E}(X\mid Z), \mathbb{E}(Y\mid Z) \bigr).
\end{align*}`{=tex}
:::

::: {.section}
Non-réponse
-----------

::: {.section}
#### Question 1 {#answer-nonrep1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

L'espérance conditionnelle de $Y$ sachant $X$ peut s'écrire comme la
solution au problème de minimisation
$$\min_{\phi(X)\in L^2_X} \mathbb{E}\left(\left(Y-\phi(X)\right)^2\right).$$
Or pour $\phi(X)\in L^2_X$ on a ici
$$\mathbb{E}\left(\left(Y-\phi(X)\right)^2\right) = \mathbb{E}\left( \left(Y - \phi(1)\right)^2 1_{\{1\}}(X) \right) + \mathbb{E}\left( \left(Y - \phi(0)\right)^2 1_{\{0\}}(X) \right),$$
il suffit donc de résoudre pour tout $x\in\{0,1\}$
$$\min_{\lambda \in \mathbb{R}} \mathbb{E}\left(\left(Y-\lambda\right)^2 1_{\{x\}}(X)\right).$$
Soit $x\in\{0,1\}$ et posons
$J_x : \lambda\in\mathbb{R}\mapsto \mathbb{E}\left(\left(Y-\lambda\right)^2 1_{\{x\}}(X)\right)$.
Alors pour tout $\lambda\in\mathbb{R}$
$$J_x(\lambda) = \mathbb{E}\left(Y^21_{\{x\}}(X)\right) + \lambda^2\,\mathbb{P}(X=x) -2\lambda\,\mathbb{E}\left(Y1_{\{x\}}(X)\right)$$
et sa dérivée
$$J_x^\prime(\lambda) = 2\lambda\,\mathbb{P}(X=x) -2\,\mathbb{E}\left(Y1_{\{x\}}(X)\right)$$
s'annule en
$$\lambda_x := \dfrac{\mathbb{E}\left(Y1_{\{x\}}(X)\right)}{\mathbb{P}(X=x)} = \mathbb{E}(Y\mid X = x).$$
On en conclut que
$$\mathbb{E}(Y\mid X) = \mathbb{E}(Y\mid X = 1)1_{\{1\}}(X) + \mathbb{E}(Y\mid X = 0)1_{\{0\}}(X).$$
Or on remarque que $1_{\{1\}}(X) = X$ et $1_{\{0\}}(X) = 1 - X$, ce qui
fait de $\mathbb{E}(Y\mid X)$ une fonction affine de $X$. Elle est par
définition la meilleure approximation de $Y$ par une fonction de $X$,
elle coïncide donc avec l'approximation affine de $Y$ par $X$:
$$\mathbb{E}(Y\mid X) = m + \dfrac{\rho\,\sigma}{\sqrt{p(1-p)}}\,(X - p).$$
:::

::: {.section}
#### Question 2 {#answer-nonrep2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

D'après la question précédente, on a
$\mathbb{E}(Y\mid X) = m_0 + (m_1 - m_0) X$, la meilleure approximation
affine de $Y$ par $X$. Ainsi, $m_0$ et $m_1$ satisfont
$$\left|\begin{array}{l} m_1 - m_0 = \dfrac{\rho\sigma}{\sqrt{p(1-p)}},\\[1em] m_0 = m - (m_1-m_0)p,  \end{array}\right. \Leftrightarrow \left|\begin{array}{l} m_1 = m + \rho\sigma\sqrt{\dfrac{1-p}{p}},\\[1em] m_0 = m - \rho\sigma\sqrt{\dfrac{p}{1-p}}.  \end{array}\right.$$
:::

::: {.section}
#### Question 3 {#answer-nonrep3 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Par la formule de la variance totale et d'après la question 1, on a
`\begin{align*}
\sigma^2 &= \mathbb{V}\left(Y\right) = \mathbb{E}\bigl(\mathbb{V}\left(Y\mid X\right)\bigr) + \mathbb{V}\bigl(\mathbb{E}(Y\mid X)\bigr)\\
&= p\,\sigma^2_1 + (1-p)\,\sigma^2_0 + \dfrac{\rho^2\sigma^2}{p\,(1-p)}\mathbb{V}(X)\\
&= p\,\sigma^2_1 + (1-p)\,\sigma^2_0 + \rho^2\sigma^2.
\end{align*}`{=tex} Cette égalité se simplifie et donne bien
$$\sigma^2 = \dfrac{(1-p)\,\sigma_0^2 + p\,\sigma_1^2}{1-\rho^2}.$$
:::

::: {.section}
#### Question 4 {#answer-nonrep4 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 4}`{=latex}

Lorsque $X$ et $Y$ sont non corrélées, i.e. $\rho = 0$, on obtient
$m_0 = m_1 = m$ puis $\sigma^2 = (1-p)\,\sigma_0^2 + p\,\sigma_1^2$. En
d'autres termes, $\mathbb{E}(Y\mid X) = m$ est une variable aléatoire
constante, et $\mathbb{E}\bigl(\mathbb{V}(Y\mid X)\bigr) = \sigma^2$.
Dans ce cas, la non-réponse n'affecte pas l'espérance, mais
potentiellement la variance (la dispersion du temps de travail peut être
différente chez les répondants et les non-répondants). Ces deux
propriétés sont encore vraies en cas d'indépendance entre $X$ et $Y$,
puisque l'indépendance implique la non corrélation, mais nous avons de
plus $\mathbb{V}(Y\mid X) = \sigma^2 = \sigma^2_1 = \sigma^2_0$; la
variable aléatoire $\mathbb{V}(Y\mid X)$ est elle aussi constante. Cette
fois-ci, la dispersion est la même chez les répondants et les
non-répondants : la non-réponse n'affecte pas la variance.
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

[^3]: Comme on a vu au chapitre 1, quand on considère des variables
    aléaoires, on considère la tribu des boréliens
    $\mathcal{B}(\mathbb{R})$. On appelle mesure de Borel-Lebesgue ou de
    Borel la mesure de Lebesgue restreinte à cette tribu.

[^4]: c'est-à-dire qu'on peut définir ces probabilités de la manière
    qu'on souhaite pour les boréliens $B$ tels que $\mathbb{P}_X(B)=0$.

[^5]: voir par exemple l'excellent [matrix
    cookbook](https://www.ics.uci.edu/~welling/teaching/KernelsICS273B/MatrixCookBook.pdf).

[^6]: voir par exemple les [Rappels mathématiques pour la mécanique
    quantique de Bruno
    Figliuzzi](https://discourse.mines-paristech.fr/uploads/short-url/v4CxgD6KzWUZpmQWbvckL7eaP7C.pdf)
