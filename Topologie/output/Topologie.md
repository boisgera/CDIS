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
title: Topologie
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
-   [Conventions](#conventions)
-   [Espaces vectoriels normés](#espaces-vectoriels-normés-1)
-   [Espaces métriques](#espaces-métriques-1)
    -   [Distance](#distance)
    -   [Distance point-ensemble et
        ensemble-ensemble](#distance-point-ensemble-et-ensemble-ensemble)
-   [Bestiaire topologique](#bestiaire-topologique)
-   [Suites, limites et continuité](#suites-limites-et-continuité-1)
    -   [Continuité et image réciproque](#CIR)
-   [Complétude](#complétude)
    -   [Points fixes et zéros](#points-fixes-et-zéros)
    -   [Algorithmes et critères de
        convergence](#algorithmes-et-critères-de-convergence)
    -   [Réciproque ?](#réciproque)
-   [Annexe -- Espaces produits](#annexe-espaces-produits)
-   [Annexe -- Compacité](#annexe-compacité)
    -   [Compacité et compacité
        séquentielle](#compacité-et-compacité-séquentielle)
-   [Annexe -- Espace topologique](#annexe-espace-topologique)
    -   [Structure topologique d'un espace
        métrique](#structure-topologique-dun-espace-métrique)
    -   [Composée d'applications
        continues](#composée-dapplications-continues)
    -   [Les espaces métriques sont des espaces
        topologiques](#les-espaces-métriques-sont-des-espaces-topologiques)
    -   [L'espace topologique généralise l'espace
        métrique](#lespace-topologique-généralise-lespace-métrique)
    -   [Calcul topologique -- Axiomes de
        Kuratowksi](#calcul-topologique-axiomes-de-kuratowksi)
-   [Exercices](#exercices)
    -   [Normes d'opérateurs](#normes-dopérateurs)
    -   [Droite réelle achevée](#dra)
    -   [Localement fermé](#localement-fermé)
    -   [Distance entre ensembles](#distance-entre-ensembles)
    -   [Plongement de Kuratowski](#plongement-de-kuratowski)
    -   [Le nombre d'or](#golden-ratio)
    -   [Spirale d'Euler](#spirale-deuler)
    -   [Point fixe](#TPFB2)
    -   [Résolution itérative de systèmes
        linéaires](#résolution-itérative-de-systèmes-linéaires)
    -   [Équation différentielle](#équation-différentielle)
-   [Solutions](#solutions)
    -   [Exercices essentiels](#exercices-essentiels)
    -   [Normes d'opérateurs](#normes-dopérateurs-1)
    -   [Droite réelle achevée](#droite-réelle-achevée)
    -   [Localement fermé](#localement-fermé-1)
    -   [Distance entre ensembles](#distance-entre-ensembles-1)
    -   [Plongement de Kuratowski](#plongement-de-kuratowski-1)
    -   [Le nombre d'or](#golden-ratio)
    -   [Spirale d'Euler](#spirale-deuler-1)
    -   [Point fixe](#point-fixe-1)
    -   [Résolution itérative de systèmes
        linéaires](#résolution-itérative-de-systèmes-linéaires-1)
    -   [Équation différentielle](#équation-différentielle-1)
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
```{=latex}
\newpage
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
#### Généralités

-   `$\mathord{\bullet}$ `{=tex}savoir que la topologie est une branche
    de la géométrie,

-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir que la topologie
    s'occupe en particulier de "proximité",

-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir que les notions
    de limite et de continuité relèvent de la topologie,

-   `$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir
    reconnaître quand un problème est de nature topologique.
:::

::: {.section}
#### Espaces vectoriels normés

-   savoir exploiter les espaces vectoriels normés suivants :

    -   `$\mathord{\boldsymbol{\circ}}$ `{=tex}l'espace $\mathbb{R}^n$
        muni de la norme euclidienne,

    -   `$\mathord{\bullet}$ `{=tex}l'espace $\mathbb{R}^{m\times n}$
        muni de la norme d'opérateur,

    -   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}l'espace des
        fonctions $A \to \mathbb{R}^n$ bornées, muni de la norme du sup.

-   `$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir
    adapter les espaces précédents aux normes non-euclidiennes,

-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir définir et
    caractériser une norme, un espace vectoriel normé.
:::

::: {.section}
#### Espaces métriques

L'accent est mis sur les espace métriques "concrets" : les
sous-ensembles arbitraires d'espaces vectoriels normés, munis de la
distance induite par la norme.

-   `$\mathord{\boldsymbol{\circ}}$ `{=tex}savoir construire une
    distance (entre points) à partir d'une norme,

-   `$\mathord{\bullet}$ `{=tex}savoir que tout sous-ensemble d'un
    e.v.n. "est" un espace métrique,

-   `$\mathord{\bullet}$ `{=tex}savoir définir la distance entre un
    point et un ensemble,

-   savoir définir à partir d'une distance :

    -   `$\mathord{\bullet}$ `{=tex}adhérence, frontière, intérieur,

    -   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}ensemble ouvert et
        fermé,

    -   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}boule ouverte,
        boule fermée,

    -   `$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$ `{=tex}propriété
        satisfaite dans un voisinage / localement,

-   savoir exploiter des rudiments de calcul topologique :

    -   `$\mathord{\bullet}$ `{=tex}$\partial A = \overline{A} \cap \overline{A^c}$,
        $A^{\circ} = \overline{(A^c)}^c$,

    -   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}$A \subset \overline{A}$,
        $\overline{\overline{A}} = \overline{A}$,
        $\overline{A} = A^{\circ} \cup \partial A$ (union disjointe),

    -   `$\mathord{\bullet}\mathord{\bullet}$`{=tex}/`$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir
        deviner et prouver de nouvelles identités.

Ces connaissances se transposent aux espaces métriques "abstraits" tels
que la droite réelle étendue $[-\infty, \infty]$, ou la collection des
ensembles fermés bornés non vides de $\mathbb{R}^n$.

-   `$\mathord{\bullet}$ `{=tex}connaître la définition générale
    d'espace métrique,

-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir quels axiomes
    caractérisent une distance,

-   `$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir
    vérifier qu'une fonction est une distance,

-   `$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir
    construire une distance appropriée à un contexte donné.
:::

::: {.section}
#### Suites, limites et continuité

Dans les espaces métriques, tous les concepts topologiques peuvent être
caractérisés à travers l'étude des suites de points.

-   savoir définir et exploiter les notions suivantes :

    -   `$\mathord{\bullet}$ `{=tex}limite d'une suite de points dans un
        espace métrique,

    -   `$\mathord{\bullet}$ `{=tex}limite d'une fonction
        $A \subset X \to Y$ en un point adhérent à $A$,

-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}connaître la
    caractérisation séquentielle des objets topologiques,

-   savoir caractériser les fonctions continues (en un point, sur son
    domaine) :

    -   `$\mathord{\bullet}$ `{=tex}définition séquentielle :
        $f(x) \to f(x_0)$ quand $x\to x_0$,

    -   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}: par l'adhérence :
        $x_0 \in \overline{A} \implies f(x_0) \in \overline{f(A)}$,

    -   `$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$ `{=tex}:
        par le critère de l'image réciproque.

-   `$\mathord{\bullet}$ `{=tex}savoir exploiter que la composition de
    fonctions continues est continue.
:::

::: {.section}
#### Espaces complets

-   `$\mathord{\bullet}$ `{=tex}comprendre les liens entre zéro de
    fonction et point fixe,

-   `$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir
    définir et caractériser une suite de Cauchy,

-   savoir caractériser un espace métrique complet, en exploitant :

    -   `$\mathord{\bullet}$ `{=tex}que $\mathbb{R}^n$ est complet,

    -   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}qu'un sous-espace
        fermé d'un espace complet est complet,

    -   `$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$ `{=tex}directement
        la définition d'espace métrique complet.

-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir quand une
    fonction scalaire continue admet un maximum,

-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir caractériser une
    application contractante,

-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir utiliser le
    théorème de point fixe de Banach.
:::
:::

::: {.section}
Conventions
===========

On définit le *complémentaire de $A$ dans $X$* comme l'ensemble $$
X \setminus A := \{x \in X \; | \; x \not \in A\}.
$$ Dans le cas où l'ensemble $X$ est clairement déterminé par le
contexte, on notera simplement $A^c$ ce complémentaire : $$
A^c := X \setminus A.
$$
:::

::: {.section}
Espaces vectoriels normés
=========================

::: {.section}
### Définition -- Norme {#norme .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Norme}`{=latex}

Une *norme* sur un espace vectoriel $E$ (sur $\mathbb{R}$) est une
application $$
\| \cdot \|: E \to \left[0, +\infty\right[
$$ telle que pour tous les points $x$ et $y$ de $E$ et tous les
scalaires $\lambda$ on ait

1.  [$\|x\| = 0$ si et seulement si $x=0$
    (*séparation*)`\label{norme-sep}`{=tex}]{#norme-sep},

2.  [$\|\lambda x\| = |\lambda| \|x\|$
    (*homogénéité*)`\label{norme-homo}`{=tex}]{#norme-homo},

3.  [$\|x+y\| \leq \|x\| + \|y\|$ (*inégalité
    triangulaire*).`\label{norme-ineg}`{=tex}]{#norme-ineg}
:::

::: {.section}
### Définition -- Espace vectoriel normé {#espace-vectoriel-normé .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Espace vectoriel normé}`{=latex}

Un espace vectoriel $E$ muni d'une norme sur $E$ est *un espace
vectoriel normé*.
:::

::: {.section}
### Proposition -- Espace $\mathbb{R}^n$ {#espace-mathbbrn .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Espace \(\mathbb{R}^n\)}`{=latex}

L'espace $E = \mathbb{R}^n$ muni de la *norme euclidienne*
$\|\cdot\|_2$, définie par $$
\|x\| := \|x\|_2 = \sqrt{x_1^2 + \dots + x_n^2}
$$ est un espace vectoriel normé.
:::

::: {.section}
### Remarque -- Normes alternatives sur $\mathbb{R}^n$ {#normes-alternatives-sur-mathbbrn .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Normes alternatives sur \(\mathbb{R}^n\)}`{=latex}

Par défaut, la norme privilégiée sur $\mathbb{R}^n$ est la norme
euclidienne ; elle se déduit du *produit scalaire* usuel $$
\left<x, y\right> = x_1 y_1 + \dots + x_n y_n
$$ par la relation $\|x\|_2 = \sqrt{\left<x, x\right>}$. On la notera
simplement $\|\cdot\|$ s'il n'y a pas d'ambiguité. Mais on peut doter
$\mathbb{R}^n$ d'autres normes ; par exemple la norme $\|\cdot\|_1$,
définie par $$
\|x\|_1 = |x_1| + \dots + |x_n|
$$ et la norme $\|\cdot\|_{\infty}$, définie par $$
\|x\|_{\infty} = \max(|x_1|,\dots, |x_n|)
$$
:::

::: {.section}
### Proposition -- Espace des matrices $\mathbb{R}^{m \times n}$ {#espace-des-matrices-mathbbrm-times-n .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Espace des matrices \(\mathbb{R}^{m \times n}\)}`{=latex}

L'ensemble des matrices $A \in \mathbb{R}^{m \times n}$, muni de *la
norme d'opérateur* $$
\|A\| := \|A\|_{22} := \sup_{x \neq 0} \frac{\|A \cdot x\|_2}{\|x\|_2},
$$ est un espace vectoriel normé.
:::

::: {.section}
#### Démonstration {#démonstration .proof}

Démontrons tout d'abord que pour toute matrice
$A \in \mathbb{R}^{m \times n}$, le ratio $\|A \cdot x\|_2/ \|x\|_2$ est
borné. Soit $e_i$ le $i$-ème vecteur de la base canonique de
$\mathbb{R}^n$ et soit $x=(x_1, \dots, x_n) \in \mathbb{R}^n$. Comme
$x = x_1 e_1 + \dots + x_n e_n$, on a $$
A \cdot x
= A \cdot (x_1 e_1 + \dots + x_n e_n) = 
\sum_{i=1}^n x_i (A \cdot e_i).
$$ Par [l'inégalité triangulaire (p.
`\pageref*{norme-ineg}`{=tex})](#norme-ineg) et par [homogénéité de la
norme (p. `\pageref*{norme-homo}`{=tex})](#norme-homo), $$
\|A \cdot x\|_2 \leq \sum_{i=1}^n |x_i| \|A \cdot e_i\|_2.
$$ Comme pour la norme euclidienne on a $|x_i| \leq \|x\|_2$, on en
déduit que $$
\|A \cdot x\|_2 
\leq \sum_{i=1}^n \|x\|_2 \|A \cdot e_i\|_2
= \left(\sum_{i=1}^n \|A \cdot e_i\|_2\right) \|x\|_2,
$$ le ratio $\|A \cdot x\|_2/ \|x\|_2$ est donc majoré par
$\sum_{i=1}^n \|A \cdot e_i\|_2$.

L'ensemble des matrices $\mathbb{R}^{m \times n}$ est un espace
vectoriel, muni des opérations $$
[A + B]_{ij} := A_{ij} + B_{ij} \; \mbox{ et } \; 
[\lambda A]_{ij} = \lambda A_{ij}.
$$ De plus la valeur $\|A\|$ est positive ; si $\|A\| = 0$, c'est-à-dire
si $$
\sup_{x \neq 0} \frac{\|A \cdot x\|_2}{\|x\|_2} = 0,
$$ nécessairement $A \cdot x$ est nulle pour tout
$x \in \mathbb{R}^n \setminus \{0\}$. Comme $A \cdot 0 = 0$ par
linéarité, la matrice $A$ est nulle. On a également $$
\|\lambda A\| = \sup_{x \neq 0} \frac{\|\lambda A \cdot x\|_2}{\|x\|_2} 
= \sup_{x \neq 0} \frac{|\lambda| \|A \cdot x\|_2}{\|x\|_2} 
= |\lambda|\sup_{x \neq 0} \frac{\|A \cdot x\|_2}{\|x\|_2}
= |\lambda| \|A\| 
$$ et $$
\begin{split}
\|A+B\| 
    &= \sup_{x \neq 0} \frac{\|(A+B) \cdot x\|_2}{\|x\|_2} \\
    &= \sup_{x \neq 0} \frac{\|A\cdot x + B \cdot x\|_2}{\|x\|_2} \\
    &\leq \sup_{x \neq 0} \frac{\|A\cdot x\|_2 + \|B \cdot x\|_2}{\|x\|_2} \\
    &\leq \sup_{x \neq 0} \frac{\|A\cdot x\|_2}{\|x\|_2} 
        + \sup_{x \neq 0} \frac{\|B\cdot x\|_2}{\|x\|_2} \\
    &= \|A\| + \|B\|
\end{split}
$$ ce qui prouve que la norme d'opérateur est bien une norme sur
l'espace des matrices
$\mathbb{R}^{m \times n}$.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
La norme d'opérateur $\|A\|$ vérifie par construction les inégalités $$
\forall \, x \in \mathbb{R}^n, \; \|A \cdot x\| \leq \|A\| \|x\|.
$$ Plus précisément, $\|A\|$ est la meilleure -- c'est-à-dire la plus
stricte, la plus petite -- des bornes $\kappa$ telles que
$\|A \cdot x\| \leq \kappa \|x\|$ pour tout $x$ : $$
\|A\| = \min \{\kappa \in \left[0, +\infty\right[ \; | \; \forall x \in \mathbb{R}^n, \, \|A \cdot x\| \leq \kappa \|x\|\}.
$$
:::

::: {.section}
#### Exercice -- Norme d'une matrice $2\times3$ ($\mathord{\bullet}$) {#nm23 .exercise .one .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Norme d'une matrice \(2\times3\)}`{=latex}

Montrer que la norme d'opérateur de la matrice $$
A = \left[
  \begin{array}{rrr}
  1 & 0  & 0\\
  0 & -1 & 0
  \end{array}
\right]
$$ vaut $1$. ([Solution p.
`\pageref*{answer-nm23}`{=tex}](#answer-nm23){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Matrice de rotation ($\mathord{\bullet}$) {#mdr .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Matrice de rotation}`{=latex}

Soit $\theta \in \mathbb{R}$. Calculer la norme d'opérateur de $$
A = \left[
  \begin{array}{rr}
  \cos \theta & -\sin \theta \\
  \sin \theta & \cos \theta
  \end{array}
\right].
$$

([Solution p.
`\pageref*{answer-mdr}`{=tex}](#answer-mdr){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Norme d'une matrice $2 \times 2$ ($\mathord{\bullet}\mathord{\bullet}$) {#nm22 .exercise .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Norme d'une matrice \(2 \times 2\)}`{=latex}

Calculer la norme d'opérateur de $$
A = \left[
  \begin{array}{rr}
  2 & 0 \\
  0 & -1
  \end{array}
\right].
$$

([Solution p.
`\pageref*{answer-nm22}`{=tex}](#answer-nm22){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Sous-multiplicativité de la norme d'opérateur ($\mathord{\bullet}\mathord{\bullet}$) {#sous-multip .exercise .two .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Sous-multiplicativité de la norme d'opérateur}`{=latex}

Montrer que si $A \in \mathbb{R}^{m \times n}$ et
$B \in \mathbb{R}^{n \times p}$, alors la norme du produit des matrices
$A$ et $B$ vérifie $\|A \cdot B\| \leq \|A\| \|B\|$. ([Solution p.
`\pageref*{answer-sous-multip}`{=tex}](#answer-sous-multip){.no-parenthesis}.)
:::

::: {.section}
### Remarque -- Normes alternatives sur $\mathbb{R}^{m \times n}$ {#normes-alternatives-sur-mathbbrm-times-n .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Normes alternatives sur \(\mathbb{R}^{m \times n}\)}`{=latex}

Le résultat précédent est encore valable quand on muni $\mathbb{R}^n$ et
$\mathbb{R}^m$ de normes arbitraires $\|\cdot\|_{\mathbb{R}^n}$ et
$\|\cdot\|_{\mathbb{R}^m}$ et que l'on définit la norme d'opérateur
associée comme $$
\|A\| := \|A\|_{\mathbb{R}^m\mathbb{R}^n} := \sup_{x \neq 0} \frac{\|A \cdot x\|_{\mathbb{R}^m}}{\|x\|_{\mathbb{R}^n}}.
$$ Ce résultat nécessite un argument de compacité (cf. [annexe (p.
`\pageref*{annexe-compacituxe9}`{=tex})](#annexe-compacité)) qui n'est
valable que dans les espaces de dimension finie. Mais de façon plus
générale si $E$ et $F$ sont des espaces vectoriels normés -- pas
nécessairement de dimension finie -- l'espace des opérateurs linéaires
de $E$ dans $F$ bornés, c'est-à-dire tels que $$
\|A\| := \|A\|_{FE} := \sup_{x \neq 0} \frac{\|A \cdot x\|_{F}}{\|x\|_{E}},
$$ est également un espace vectoriel normé.
:::

::: {.section}
### Proposition -- Espace de fonctions bornées {#espace-de-fonctions-bornées .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Espace de fonctions bornées}`{=latex}

Soit $A$ un ensemble. L'espace vectoriel des fonctions bornées $f$ de
$A$ dans $\mathbb{R}^n$, muni de $$
\|f\| := \sup_{x \in A} \|f(x)\|_2 < +\infty
$$ est un espace vectoriel normé.
:::

::: {.section}
#### Démonstration {#démonstration-1 .proof}

L'ensemble des fonctions bornées $A \to \mathbb{R}^n$ est un espace
vectoriel quand on le munit des opérations $$
(f+g)(x) := f(x) + g(x) \; \mbox{ et } \; (\lambda f)(x) := \lambda f(x).
$$

De plus, si $\|f\| = \sup_{x \in A} \|f(x)\|_2 = 0$, alors
$\|f(x)\|_2= 0$ pour tout $x \in A$ et donc [par l'axiome de séparation
(p. `\pageref*{norme-sep}`{=tex})](#norme-sep), $f(x) = 0$ pour tout
$x \in A$, c'est-à-dire $f=0$.

Si $\lambda$ est un réel, on a par [homogénéité de la norme
$\|\cdot\|_2$ (p. `\pageref*{norme-homo}`{=tex})](#norme-homo) $$
\sup_{x \in A} \|\lambda f(x)\|_2 = \sup_{x \in A} |\lambda|\|f(x)\|_2 = |\lambda| \sup_{x \in A} \|f(x)\|_2,
$$ soit $\|\lambda f\| = |\lambda|\|f\|$.

Finalement, `\begin{align*}
\sup_{x \in A} \|(f+g)(x)\|_2 &=  \sup_{x \in A} \|f(x)+g(x)\|_2 \\
                            &\leq  \sup_{x \in A} \|f(x)\|_2+\|g(x)\|_2 \\
                            &\leq \sup_{x \in A} \|f(x)\|_2 + \sup_{x \in A} \|g(x)\|_2,
\end{align*}`{=tex} donc $\|f+g\| \leq \|f\|+ \|g\|$. La fonction
$\|\cdot\|$ est donc bien une norme sur l'espace des fonctions bornées
de $A$ dans $\mathbb{R}^n$.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Remarque -- Normes alternatives pour les fonctions bornées {#normes-alternatives-pour-les-fonctions-bornées .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Normes alternatives pour les fonctions bornées}`{=latex}

Si $E$ est un espace vectoriel muni de la norme $\|\cdot\|_E$, une
démonstration en tout point similaire permet d'établir que $$
\|f\| := \sup_{x \in A} \|f(x)\|_E
$$ définit une norme sur l'espace des fonctions bornées de $A$ dans
$(E, \|\cdot\|_E)$.
:::
:::

::: {.section}
Espaces métriques
=================

::: {.section}
Si $X$ est un sous-ensemble d'un espace vectoriel normé $E$, celui-ci
"hérite" de $E$ une mesure de la distance entre deux points $x$ et $y$
avec la grandeur $$
d(x, y) = \|y - x\|.
$$

![Le cercle unité $\{x \in \mathbb{R}^2 \, | \, \|x\|=1\}$. Bien que
$x=(1,0)$ et $y=(0,1)$ appartiennent au cercle unité, ni $x+y$ ni $2 x$
ne lui appartiennent. Il hérite néanmoins d'une distance $d$ de l'espace
euclidien $\mathbb{R}^2$ (telle que $d(x,y) = \|x - y\|_2 = \sqrt{2}$
quand $x=(1,0)$ et $y=(0,1)$), ce qui fait de lui un espace
métrique.](images/circle.tex.pdf)

Par contre, à moins que $X$ soit un sous-espace vectoriel de $E$ les
additions entre éléments de $X$ ou la multiplication d'un élément de $X$
par un scalaire n'ont plus de sens dans $X$ ; nous ne pouvons plus
définir une norme sur $X$.

La fonction $d$ définie ci-dessus sur $X$ vérifie automatiquement les
axiomes qui nous autorisent à la qualifier de "distance" :
:::

::: {.section}
### Distance

Une *distance* sur un ensemble $X$ est une fonction $$
d: X \times X \to \left[0, +\infty\right[
$$ telle que pour tous points $x, y$ et $z$ de $X$, on ait :

1.  [$d(x,y) = 0$ si et seulement si $x = y$
    (*séparation*)`\label{dist-sep}`{=tex}]{#dist-sep},

2.  [$d(x,y) = d(y,x)$ (*symétrie*)`\label{dist-sym}`{=tex}]{#dist-sym},

3.  [$d(x,z) \leq d(x,y) + d(y,z)$ (*inégalité
    triangulaire*)`\label{dist-ineg}`{=tex}]{#dist-ineg}.
:::

::: {.section}
### Définition -- Espace métrique {#espace-métrique .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Espace métrique}`{=latex}

Un *espace métrique* est un ensemble $X$ muni d'une *distance*.
:::

::: {.section}
Une fonction distance est également appelée une *métrique*.
:::

::: {.section}
### Proposition -- Sous-ensemble d'un espace vectoriel normé {#sous-ensemble-dun-espace-vectoriel-normé .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Sous-ensemble d'un espace vectoriel normé}`{=latex}

Soit $X$ un sous-ensemble d'un espace vectoriel normé $E$. La fonction
$d: X \times X \to \left[0, +\infty\right[$ définie par $$
d(x, y) := \|x - y\|
$$ est une distance sur $X$.
:::

::: {.section}
Autrement dit, tout sous-ensemble d'un espace vectoriel normé "est" un
espace métrique, c'est-à-dire qu'il existe une fonction distance
"naturelle" dont on peut le doter, induite par l'espace vectoriel normé.
Cela vaut en particulier pour l'espace vectoriel normé lui-même : tout
espace vectoriel normé "est" un espace métrique.

Réciproquement, les espaces métriques ne sont pas plus généraux que les
sous-ensembles d'espace vectoriels normés : tout espace métrique peut en
effet être identifié au moyen d'une isométrie avec un tel sous-ensemble
(cf. l'exercice "[Plongement de Kuratowski (p.
`\pageref*{plongement-de-kuratowski-1}`{=tex})](#plongement-de-kuratowski-1)").
Les espaces métriques n'exhibent donc aucune propriété qui ne soit déjà
manifeste dans l'étude des sous-ensembles d'espaces vectoriel normés.
:::

::: {.section}
#### Démonstration {#démonstration-2 .proof}

Par construction, la fonction $d$ est bien positive. De plus, pour tous
points $x, y$ et $z$ de $X$ :

1.  Par l'[axiome de séparation des normes (p.
    `\pageref*{norme-sep}`{=tex})](#norme-sep), $$
    \|x - y\| = 0 \, \Leftrightarrow \, x - y = 0 \, \Leftrightarrow \, x = y.
    $$ Cela entraîne que $d(x, y) = 0$ si et seulement si $x=y$, soit
    l'[axiome de séparation pour la distance $d$ (p.
    `\pageref*{dist-sep}`{=tex})](#dist-sep).

2.  Par [homogénéité de la norme $\| \cdot \|$ (p.
    `\pageref*{norme-homo}`{=tex})](#norme-homo), on a $$
    \|x - y\| = \|(-1) \times (y-x)\| = |-1| \times \|y - x\| = \|y - x\|,
    $$ et donc $d(x, y) = d(y, x)$, d'où la [symétrie de la fonction $d$
    (p. `\pageref*{dist-sym}`{=tex})](#dist-sym).

3.  Par l'[inégalité triangulaire pour les normes (p.
    `\pageref*{norme-ineg}`{=tex})](#norme-ineg), on a $$
    \|x - z\| = \|x - y - (y - z)\| \leq \|x - y\| + \|y - z\|,
    $$ ce qui établit l'[inégalité triangulaire pour la distance $d$ (p.
    `\pageref*{dist-ineg}`{=tex})](#dist-ineg).

$\;\; \blacksquare$
:::

::: {.section}
### Distance point-ensemble et ensemble-ensemble

Une distance $d$ sur $X$ associe à deux points de $X$ un réel positif.
Cette fonction peut servir de base pour définir une distance entre un
point $x$ de $X$ et un ensemble de points de $A$ de $X$ : $$
d(x, A) := \inf_{a \in A} d(x, a) \in \left[0, +\infty \right]
$$ ou même entre deux ensembles $A$ et $B$ de points de $X$ : $$
d(A, B) = \inf_{a \in A} d(a, B) = \inf_{a \in A} \inf_{b \in B} d(a, b)
\in \left[0, +\infty \right].
$$ Si $A$ est l'ensemble vide, on a $d(x, A) = +\infty$ et si $A$ ou $B$
est vide on a $d(A, B)= +\infty$ ; ce sont les seuls cas où ces
extensions de la distance entre points peuvent prendre des valeurs
infinies.
:::

::: {.section}
### Définition -- Isométries {#isométries .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Isométries}`{=latex}

Une application $f: X \to Y$ définie entre deux espaces métriques
$(X, d_X)$ et $(Y, d_Y)$ telle que : $$
d_Y(f(x), f(y)) = d_X(x, y)
$$ est une *isométrie*.
:::

::: {.section}
Les isométries sont les *morphismes* des espaces métriques : les
applications qui préservent la structure des espaces métriques.
Construire des isométries peut aller de pair avec la construction d'une
métrique sur un ensemble qui en est initialement dépourvu ; voir à ce
propos l'exercice "[Droite réelle achevée (p.
`\pageref*{droite-ruxe9elle-achevuxe9e}`{=tex})](#droite-réelle-achevée)".
:::

::: {.section}
### Définition -- Sous-espace métrique {#sous-espace-métrique .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Sous-espace métrique}`{=latex}

Un sous-ensemble $Y$ d'un espace métrique $X$ est un *sous-espace
métrique* de $X$ lorsqu'il est muni de la distance de $X$, restreinte
aux points de $Y$.
:::
:::

::: {.section}
Bestiaire topologique
=====================

::: {.section}
### Définition -- Adhérence, frontière, intérieur {#adhérence-frontière-intérieur .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Adhérence, frontière, intérieur}`{=latex}

Soit $X$ un espace métrique et $A$ un ensemble de points de $X$. On note

-   $\overline{A}$ l'*adhérence* de $A$, c'est-à-dire l'ensemble des
    *points adhérents* à $A$ : $$
    \overline{A} := \{x \in X \; | \; d(x, A)= 0 \},
    $$

-   $\partial A$ la *frontière* de $A$, c'est-à-dire l'ensemble des
    *points frontières* de $A$ : $$
    \partial A := \{x \in X \; | \; d(x,A) = d(x, A^c) = 0\},
    $$

-   $A^{\circ}$ l'*intérieur* de $A$, c'est-à-dire l'ensemble des
    *points intérieurs* à $A$ : $$
    A^{\circ} := \{x \in X \; | \; d(x, A^c) > 0\}.
    $$
:::

::: {.section}
![Construction de l'intérieur $A^{\circ}$ et de la frontière
$\partial A$ à partir de l'ensemble $A$, en utilisant l'opérateur
d'adhérence $\overline{(\cdot)}$ et des opérations
ensemblistes.](images/topological-operations.svg.pdf)
:::

::: {.section}
#### Exercice -- Intervalles de $\mathbb{R}$ ($\mathord{\bullet}$) {#ir .exercise .one .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Intervalles de \(\mathbb{R}\)}`{=latex}

Déterminer l'adhérence, la frontière et l'intérieur de
$\left[0,1 \right[$. ([Solution p.
`\pageref*{answer-ir}`{=tex}](#answer-ir){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Ensemble des rationnels ($\mathord{\bullet}\mathord{\bullet}$) {#Q .exercise .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Ensemble des rationnels}`{=latex}

Déterminer l'adhérence de $\mathbb{Q}$. ([Solution p.
`\pageref*{answer-Q}`{=tex}](#answer-Q){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Inclusions ($\mathord{\bullet}$) {#exo-i .exercise .one .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Inclusions}`{=latex}

Montrer que $A^{\circ} \subset A \subset \overline{A}$. ([Solution p.
`\pageref*{answer-exo-i}`{=tex}](#answer-exo-i){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Topologie basée sur l'adhérence ($\mathord{\bullet}$) {#tba .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Topologie basée sur l'adhérence}`{=latex}

Montrer que $\partial A = \overline{A} \cap \overline{A^c}$ et
$A^{\circ} = \left(\overline{A^c}\right)^c$. ([Solution p.
`\pageref*{answer-tba}`{=tex}](#answer-tba){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Adhérence itérée ($\mathord{\bullet}\mathord{\bullet}$) {#ai .exercise .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Adhérence itérée}`{=latex}

Montrer que $\overline{\overline{A}} = \overline{A}$. ([Solution p.
`\pageref*{answer-ai}`{=tex}](#answer-ai){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Décomposition de $\overline{A}$ ($\mathord{\bullet}\mathord{\bullet}$) {#pab .exercise .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Décomposition de \(\overline{A}\)}`{=latex}

Montrer que $A^{\circ} \cap \partial A = \varnothing$ et
$\overline{A} = A^{\circ} \cup \partial A.$ ([Solution p.
`\pageref*{answer-pab}`{=tex}](#answer-pab){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Topologie basée sur la frontière ($\mathord{\bullet}\mathord{\bullet}$) {#tbf .exercise .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Topologie basée sur la frontière}`{=latex}

Montrer que $\overline{A} = A \cup \partial A$ et
$A^{\circ} = A \setminus \partial A.$ ([Solution p.
`\pageref*{answer-tbf}`{=tex}](#answer-tbf){.no-parenthesis}.)
:::

::: {.section}
### Définition -- Ensemble fermé, ouvert {#ensemble-fermé-ouvert .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Ensemble fermé, ouvert}`{=latex}

Un ensemble $A$ est *fermé* si tous les points adhérents à $A$
appartiennent à $A$ : $$
\mbox{$A$ fermé} \; \Leftrightarrow \; A = \overline{A} \; \Leftrightarrow \; (d(x, A) = 0 \Rightarrow x \in A).
$$ Un ensemble $A$ est *ouvert* si la distance de tout point de $A$ au
complémentaire de $A$ est strictement positive : $$
\mbox{$A$ ouvert} \; \Leftrightarrow \;
A = A^{\circ}
\; \Leftrightarrow \; 
(x \in A \Rightarrow d(x, A^c) > 0).
$$
:::

::: {.section}
#### Exercice -- Ouvert $\Leftrightarrow$ non fermé ? ($\mathord{\bullet}$) {#onf .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Ouvert \(\Leftrightarrow\) non fermé ?}`{=latex}

Est-ce que "ouvert" signifie la même chose que "non fermé" ? ([Solution
p. `\pageref*{answer-onf}`{=tex}](#answer-onf){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- L'adhérence est fermée, l'intérieur est ouvert ($\mathord{\bullet}$) {#adio .one .exercise .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{L'adhérence est fermée, l'intérieur est ouvert}`{=latex}

Montrer que l'adhérence $\overline{A}$ d'un ensemble $A$ est fermée et
que son intérieur $A^{\circ}$ est ouvert. ([Solution p.
`\pageref*{answer-adio}`{=tex}](#answer-adio){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Ensemble discret ($\mathord{\bullet}\mathord{\bullet}$) {#ed .two .exercise .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Ensemble discret}`{=latex}

Soit $A$ un sous-ensemble de l'espace métrique $X$ dont tous les points
soient isolés : pour tout $x \in A$, la distance de $x$ à
$A\setminus \{x\}$ est strictement positive. Est-ce que $A$ est
nécessairement fermé ? ([Solution p.
`\pageref*{answer-ed}`{=tex}](#answer-ed){.no-parenthesis}.)
:::

::: {.section}
### Définition -- Boules {#boules .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Boules}`{=latex}

Soit $X$ un espace métrique. Pour tout $x \in X$ et $r\geq 0$, on
définit la *boule ouverte de centre $x$ et de rayon $r$* comme $$
B(x, r) = \{y \in X \, | \, d(x, y) < r\}
$$ et la *boule fermée de centre $x$ et de rayon $r$* comme $$
\overline{B}(x, r) = \{y \in X \, | \, d(x, y) \leq r\}.
$$
:::

::: {.section}
#### Exercice -- Normes et boules ($\mathord{\bullet}$) {#bdn .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Normes et boules}`{=latex}

Dans $\mathbb{R}^2$, représenter graphiquement les boules ouvertes
centrées sur l'origine et de rayon $1$ lorsque la distance est issue la
norme euclidienne $\|x\|_2 = \sqrt{x_1^2+x_2^2}$, puis de la norme
$\|x\|_1 = |x_1| + |x_2|$ et enfin de la norme
$\|x\|_{\infty} = \max(|x_1|, |x_2|)$. ([Solution p.
`\pageref*{answer-bdn}`{=tex}](#answer-bdn){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- C'est une boule ça ? ($\mathord{\bullet}$) {#cubc .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{C'est une boule ça ?}`{=latex}

On considère comme espace métrique le carré de $\mathbb{R}^2$ défini par
$X = \{(x_1, x_2) \in \mathbb{R}^2 \; | \; |x_1| \leq 1 \mbox{ et } |x_2| \leq 1\}$
muni de la distance euclidienne. Expliciter dans cet espace les boules
ouvertes $B((0,0), 1)$, $B((1,0), 1)$ et $B((0,0), 2)$. ([Solution p.
`\pageref*{answer-cubc}`{=tex}](#answer-cubc){.no-parenthesis}.)
:::

::: {.section}
### Définition -- Voisinage {#voisinage .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Voisinage}`{=latex}

Soit $X$ un espace métrique. Un ensemble $V$ de $X$ est un *voisinage*
d'un point $x$ de $X$ si la distance de $x$ au complémentaire de $V$ est
strictement positive : $$
\mbox{$V$ voisinage de $x$}
\; \Leftrightarrow \; 
d(x, V^c) > 0.
$$

![Un voisinage $V$ d'un point $x$ du plan.](images/voisinage.svg.pdf)
:::

::: {.section}
Autrement dit, $V$ est un voisinage de $x$ si et seulement si $x$ est un
point intérieur de $V$, ou encore, s'il existe une boule ouverte centrée
en $x$ de rayon $r >0$ incluse dans $V$ : $$
x \in B(x, r) \subset V.
$$
:::

::: {.section}
#### Exercice -- Dans le plan ($\mathord{\bullet}$) {#dlp .exercise .one .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Dans le plan}`{=latex}

La droite $D$ d'équation $x_1 = x_2$ est-elle un voisinage de l'origine
dans $\mathbb{R}^2$ ? ([Solution p.
`\pageref*{answer-dlp}`{=tex}](#answer-dlp){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Voisinages ouverts / fermés ? ($\mathord{\bullet}$) {#vof .exercise .one .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Voisinages ouverts / fermés ?}`{=latex}

Montrer que si $V$ est un voisinage de $x$, il existe un voisinage
ouvert de $x$ inclus dans $V$ et un voisinage fermé de $x$ inclus dans
$V$. ([Solution p.
`\pageref*{answer-vof}`{=tex}](#answer-vof){.no-parenthesis}.)
:::

::: {.section}
### Définition -- Propriétés vraies dans un voisinage / localement {#propriétés-vraies-dans-un-voisinage-localement .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Propriétés vraies dans un voisinage / localement}`{=latex}

Soit $X$ un espace métrique et $\mathcal{F}$ une collection d'ensembles
de $X$. Une propriété $P$, dépendant d'un ensemble $A$ appartenant à
$\mathcal{F}$ $$
P:  A \in \mathcal{F} \to \{\mbox{vrai}, \mbox{faux}\}
$$ est *vraie au voisinage de $x \in X$* s'il existe un voisinage $V$ de
$x$ tel que $V \in \mathcal{F}$ et $P(V)$ soit vraie. Elle est
*localement vraie* si elle est vraie au voisinage de tout $x \in X$.
:::

::: {.section}
#### Exercice -- Fonction localement bornée ($\mathord{\bullet}\mathord{\bullet}$) {#flb .two .exercise .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Fonction localement bornée}`{=latex}

Montrer qu'une fonction continue $f:\mathbb{R}\to \mathbb{R}$ n'est pas
nécessairement bornée sur $\mathbb{R}$, mais qu'elle y est toujours
localement bornée. ([Solution p.
`\pageref*{answer-flb}`{=tex}](#answer-flb){.no-parenthesis}.)
:::
:::

::: {.section}
Suites, limites et continuité
=============================

::: {.section}
### Définition -- Limite d'une suite de points {#limite-dune-suite-de-points .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Limite d'une suite de points}`{=latex}

Une suite $x_k$ de valeurs d'un espace métrique $X$ a comme *limite* un
point $\ell$ de $X$ -- ou *converge vers $\ell$* -- si $x_{k}$ est
arbitrairement proche de $\ell$ à partir d'un certain rang, c'est-à-dire
si pour tout $\varepsilon > 0$, il existe un entier $n$ tel que pour
tout $k \geq n$, $d(x_k, \ell) \leq \varepsilon$, ou encore si $$
\lim_{k \to +\infty} d(x_k, \ell) = 0.
$$ On utilisera alors une des deux notations : $$
\ell = \lim_{k\to +\infty} x_k
\; \mbox{ ou } \;
x_k \to \ell \mbox{ quand } k \to + \infty.
$$ Une suite possédant une limite est dite *convergente*.
:::

::: {.section}
### Proposition -- Unicité de la limite d'une suite {#unicité-de-la-limite-dune-suite .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Unicité de la limite d'une suite}`{=latex}

Si une suite $x_k$ admet une limite, celle-ci est unique.
:::

::: {.section}
#### Démonstration {#démonstration-3 .proof}

Par [l'inégalité triangulaire (p.
`\pageref*{dist-ineg}`{=tex})](#dist-ineg), si les points $\ell$ et
$\ell'$ sont des limites de la suite des $x_k$, alors pour tout entier
$k$ on a $$
d(\ell, \ell') \leq d(x_k, \ell) + d(x_k, \ell').
$$ Comme il existe des rangs $n$ et $n'$ tels que lorsque $k \geq n$ et
$k\geq n'$, on a $d(x_k, \ell) \leq \varepsilon /2$ et
$d(x_k, \ell') \leq \varepsilon /2$, pour $k = \max(n, n')$, on a
$d(\ell, \ell') \leq \varepsilon$. La valeur $\varepsilon > 0$ étant
arbitraire, on en déduit que $d(\ell, \ell')=0$, soit par [l'axiome de
séparation (p. `\pageref*{dist-sep}`{=tex})](#dist-sep), que
$\ell = \ell'$. Il n'existe donc qu'une limite possible pour la suite
des $x_k$.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Proposition -- Caractérisations séquentielles {#caractérisations-séquentielles .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Caractérisations séquentielles}`{=latex}

Soit $X$ un espace métrique et $A$ un ensemble de points de $X$.

-   Un point adhère à $A$ s'il existe une suite de points de $A$ qui
    converge vers ce point.

-   Un point $x$ est *intérieur* à un ensemble $A$ si toute suite
    convergeant vers $x$ appartient à $A$ à partir d'un certain rang.

-   Un ensemble $A$ est *fermé* si la limite de toute suite de points de
    $A$ qui est convergente (dans $X$) appartient à $A$.

-   Un point est *frontière* de $A$ s'il existe une suite de points de
    $A$ qui converge vers ce point et une suite de points du
    complémentaire de $A$ dans $X$ qui converge vers ce point.

-   Un ensemble $V$ est un *voisinage* d'un point $x$ de $X$ si toute
    suite convergeant vers $x$ appartient à $V$ à partir d'un certain
    rang.

-   Un ensemble $A$ est *ouvert* si toute suite de points de $X$ qui
    converge vers un point de $A$ appartient à $A$ à partir d'un certain
    rang.
:::

::: {.section}
### Définition -- Limite d'une fonction en un point {#limite-dune-fonction-en-un-point .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Limite d'une fonction en un point}`{=latex}

Soit $f: X \subset Y \to Z$ une application définie sur un sous-ensemble
$X$ d'un espace métrique $Y$ et à valeurs dans un espace métrique $Z$.
Soit $x$ un point de $Y$ adhérent à $X$. Le point $\ell \in Z$ est la
*limite* de $f$ en $x$ si pour toute suite $x_k$ de points de $X$
convergeant vers $x$, on a $\lim_{k \to +\infty} f(x_k) = \ell$. On
notera alors $$
\ell = \lim_{y \to x} f(y)
\; \mbox{ ou } \;  
f(y) \to \ell \mbox{ quand } y\to x.
$$
:::

::: {.section}
S'il est nécessaire d'être explicite sur le domaine de $f$, on pourra
noter $$
\ell = \lim_{\substack{y \to x\\ y \in X}} f(y)
\; \mbox{ ou } \; 
f(y) \to \ell \mbox{ quand } y\to x, \, y \in X.
$$
:::

::: {.section}
### Proposition -- Unicité de la limite d'une fonction en un point {#unicité-de-la-limite-dune-fonction-en-un-point .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Unicité de la limite d'une fonction en un point}`{=latex}

Si la fonction $f$ admet une limite en $x$, celle-ci est unique.
:::

::: {.section}
#### Démonstration {#démonstration-4 .proof}

Un corollaire de [l'unicité de la limite des suites (p.
`\pageref*{unicituxe9-de-la-limite-dune-suite}`{=tex})](#unicité-de-la-limite-dune-suite).`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Définition -- Continuité {#continuité .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Continuité}`{=latex}

Soient $X$ et $Y$ deux espaces métriques. Une fonction $f: X \to Y$ est
*continue en $x \in X$* si et seulement si la limite de $f$ existe en
$x$ et vaut $f(x)$ : $$
f(y) \to f(x) \; \mbox{ quand } \; y \to x.
$$ Elle est *continue (sur $X$)* si elle est continue en tout point
$x \in X$.
:::

::: {.section}
Il est évident que si $x_k$ est la suite constante égale à $x$, alors
$f(x_k)$ tend vers $f(x)$ quand $k$ tend vers $+\infty$. La valeur
$f(x)$ est donc la seule limite possible de $f(y)$ quand $y\to x$. Par
conséquent on peut également dire que $f$ est continue en $x \in X$ si
et seulement si elle admet une limite en $x$, sans préciser sa valeur.
:::

::: {.section}
### Proposition -- Composition de fonctions continues {#composition-de-fonctions-continues .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Composition de fonctions continues}`{=latex}

Soient $X$, $Y$ et $Z$ des espaces métriques. Soit $f: X \to Y$ et soit
$g: Y \to Z$ des fonctions continues en $x \in X$ et $y = f(x) \in Y$
respectivement. Alors la fonction composée $g \circ f$ est continue en
$x$.
:::

::: {.section}
#### Démonstration {#démonstration-5 .proof}

Si la suite de points $x_k$ de $X$ converge vers $x$ quand
$k \to +\infty$, alors par continuité, la suite $y_k := f(x_k)$ de
points de $Y$ converge vers $y = f(x)$ quand $k \to +\infty$. Donc la
suite $g(y_k) = (g \circ f)(x_k)$ converge vers quand $k \to +\infty$.
La fonction $g \circ f$ est donc continue en
$x$.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Proposition -- Continuité de la distance {#distance-continue .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Continuité de la distance}`{=latex}

Soit $X$ un espace métrique, $y$ un point de $X$ et $A$ un sous-ensemble
non vide de $X$. Les fonctions "distance au point $y$" : $$
d(\cdot, y) : x \in X \mapsto d(x, y) \in \left[0, +\infty\right[
$$ et "distance à l'ensemble $A$" : $$
d(\cdot, A): x \in X \mapsto d(x, A) \in \left[0, +\infty\right[
$$ sont des applications continues.
:::

::: {.section}
#### Démonstration {#démonstration-6 .proof}

Pour tout $x_0 \in X$, par [inégalité triangulaire (p.
`\pageref*{dist-ineg}`{=tex})](#dist-ineg) on a $$
|d(x, y) - d(x_0, y)| \leq d(x_0, x) \to 0
\; \mbox{ quand } \;
x \to x_0,
$$ la fonction $d(\cdot, y)$ est donc continue en $x_0$.

Pour tout $a \in A$, par [inégalité triangulaire (p.
`\pageref*{dist-ineg}`{=tex})](#dist-ineg), on a
$d(x, a) \leq d(x, x_0) + d(x_0, a)$ et donc par passage à l'inf sur
$A$, $d(x, A) \leq d(x, x_0) + d(x_0, A)$. En intervertissant $x$ et
$x_0$, on obtient également $d(x_0, A) \leq d(x_0, x) + d(x, A)$. Par
[symétrie de la distance (p. `\pageref*{dist-sym}`{=tex})](#dist-sym),
ces deux inégalités entraînent $$
|d(x, A) - d(x_0, A)| \leq d(x_0, x)
$$ et donc $d(x, A) \to d(x_0, A)$ quand
$x \to x_0$.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Proposition -- Continuité et adhérence {#cad .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Continuité et adhérence}`{=latex}

Soit $X$ et $Y$ deux espaces métriques. Une fonction $f : X \to Y$ est
continue en $x \in X$ si et seulement si pour tout $A \subset X$, $f(x)$
adhère à $f(A)$ si $x$ adhère à $A$ : $$
x \in \overline{A} \implies f(x) \in \overline{f(A)}.
$$
:::

::: {.section}
#### Démonstration {#démonstration-7 .proof}

Supposons que $f$ soit continue en $x$, c'est-à-dire que $f(y) \to f(x)$
quand $y \to x$. Soit $A$ un sous-ensemble de $X$ tel que $x$ adhère à
$A$. Dans l'espace métrique $X$, cela signifie que $d(x, A) = 0$,
c'est-à-dire qu'il existe une suite de points $x_k$ de $A$ telle que
$d(x, x_k) \to 0$ quand $x_k \to x$. Par conséquent, $f(x_k) \to f(x)$
quand $k \to +\infty$, soit $d(f(x_k), f(x)) \to 0$ quand
$k \to +\infty$. Comme l'ensemble $\{f(x_k) \, | \, k \in \mathbb{N}\}$
est un sous-ensemble de $f(A)$, nous en déduisons que
$d(f(x), f(A)) = 0$ : le point $f(x)$ adhère à $f(A)$.

Réciproquement, si $f(y) \not \to f(x)$ quand $y \to x$, il existe une
suite de points $x_k$ tendant vers $x$ tels que $f(x_k)$ ne tende pas
vers $f(x)$. Par conséquent, on peut trouver un $\varepsilon > 0$ et une
suite $y_j$ extraite de $x_k$ telle que $y_j \to x$ et pour tout
$j \in \mathbb{N}$, $d(f(y_j), f(x)) > \varepsilon$. Donc $x$ adhère à
$A=\{y_j \, | \, j \in \mathbb{N}\}$, mais $f(x)$ n'adhère pas à
$\{f(y_j) \, | \, j \in \mathbb{N}\} = f(\{y_j \, | \, j \in \mathbb{N}\})$
; $f(x)$ n'adhère donc pas à $f(A)$.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Continuité et image réciproque {#CIR .corollaire}

Une fonction $f: X \to Y$ où $X$ et $Y$ sont des espaces métriques est
continue si et seulement si l'image réciproque de tout ensemble fermé
(resp. ouvert) de $Y$ par $f$ est un ensemble fermé (resp. ouvert) de
$X$.
:::

::: {.section}
#### Démonstration {#démonstration-8 .proof}

La démonstration est donnée [en annexe (p.
`\pageref*{CIR-topo}`{=tex})](#CIR-topo) dans le cadre plus général des
espaces topologiques.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Exercice -- Courbes de niveau ($\mathord{\bullet}$) {#cn .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Courbes de niveau}`{=latex}

Montrer que pour toute fonction continue
$f: \mathbb{R}^2 \to \mathbb{R}$ et tout $c \in \mathbb{R}$, l'ensemble
$\{x \in \mathbb{R}^2 \; | \; f(x) = c\}$ est fermé. ([Solution p.
`\pageref*{answer-cn}`{=tex}](#answer-cn){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Boules ouvertes et fermées ($\mathord{\bullet}\mathord{\bullet}$) {#bof2 .exercise .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Boules ouvertes et fermées}`{=latex}

Montrer que toute "boule ouverte" $B(x, r)$ est ouverte et que toute
"boule fermée" $\overline{B}(x, r)$ est fermée. ([Solution p.
`\pageref*{answer-bof2}`{=tex}](#answer-bof2){.no-parenthesis}.)
:::
:::

::: {.section}
Complétude
==========

::: {.section}
### Définition -- Point fixe {#point-fixe .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Point fixe}`{=latex}

Soit $f: X \to X$ une application d'un ensemble $X$ dans lui-même. Un
élément $x \in X$ est un *point fixe* de $f$ si $x = f(x)$.
:::

::: {.section}
### Points fixes et zéros

Être un point fixe d'une fonction $f: X \to X$, c'est donc être
déterminé **implicitement** par l'équation $x = f(x)$. Si $X$ est un
sous-espace d'un espace vectoriel, cela équivaut à dire que $x$ est une
solution de l'équation $x - f(x) = 0$, soit un *zéro* (appelé également
une *racine*) de la fonction $x \in X \mapsto x - f(x)$.

La démarche inverse -- qui consiste à caractériser les solutions d'une
équation comme des point fixes -- peut être utile pour établir des
résultats d'existence et d'unicité de solutions ou obtenir des méthodes
numériques pour leur calcul. Un exemple élémentaire de ce type de
transformation : le nombre d'or est déterminé comme l'unique solution de
l'équation $$
x^2 = x + 1 , \; x > 0
$$ ou encore comme un zéro de fonction par l'équation $$
x^2 - x - 1 = 0, \; x > 0;
$$ il peut également être caractérisé comme un point fixe par l'équation
$$
x = 1 + \frac{1}{x}, \; x > 0.
$$ Ce type de transformation n'est toutefois pas unique : un zéro de
fonction peut être caractérisé par une infinité d'équations de type
point fixe. Parmi cette multitude de choix, il faudra déterminer une
reformulation qui soit utile aux objectifs poursuivis, ce qui n'a rien
d'automatique. On se reportera à l'exercice "[Le nombre d'or (p.
`\pageref*{golden-ratio}`{=tex})](#golden-ratio)" pour prolonger l'étude
de cet exemple particulier.

![Le nombre d'or comme point fixe de
$x \mapsto 1 + 1/x$.](images/fixed-point.tex.pdf){#golden-ratio}
:::

::: {.section}
### Algorithmes et critères de convergence

Dans un algorithme (idéalisé) de calcul d'une suite de valeurs
numériques, il n'est pas évident d'établir un critère de convergence qui
garantisse exactement que la suite calculée ait une limite, quand cette
limite potentielle est inconnue.

Vérifier que $|x_{k+1} - x_k| \to 0$ par exemple est insuffisant pour
garantir une limite comme en atteste la suite des
$x_k = \sum_{j=0}^k 1 / (j+1).$ Vérifier que la série de terme général
$|x_{k+1} - x_k|$ est bornée, c'est-à-dire que $$
\sum_{k=0}^{+\infty} |x_{k+1} - x_k| < +\infty
$$ va bien garantir la convergence, mais va par contre rejeter des
suites convergentes telle que $x_k = \sum_{j=0}^{k} (-1)^j / (j+1)$. Un
critère plus adapté serait d'examiner le développement décimal de $x_k$
et de vérifier que quel que soit le nombre de décimales souhaité après
la virgule, le développement de $x_k$ finit par se stabiliser au-delà
d'un certain rang $m$ (qui dépend du nombre de décimales). Mais là
aussi, il existe des cas pathologiques qui convergent sans respecter le
critère, comme la suite des $x_k = 1 + (-1)^k 2^{-k}$, dont le
développement avec 0 décimales après la virgule -- c'est-à-dire la
partie entière -- oscille indéfiniment entre $0$ et $1$.

C'est la notion de suite de Cauchy qui capture le bon critère ; pour une
suite numérique (à valeurs réelles ou dans $\mathbb{R}^n$) "être de
Cauchy" -- ou "passer le test de Cauchy" ou encore "vérifier le critère
de Cauchy" -- est équivalent à être convergente.
:::

::: {.section}
### Définition -- Suite de Cauchy {#suite-de-cauchy .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Suite de Cauchy}`{=latex}

Une suite de points $x_k$ d'un espace métrique $X$ *est de Cauchy* si
pour tout $\varepsilon > 0$, il existe un rang $m$ tel que pour tous les
entiers $n \geq m$ et $p \geq m$, $d(x_n, x_p) \leq \varepsilon$.
:::

::: {.section}
### Définition -- Diamètre {#diamètre .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Diamètre}`{=latex}

Le diamètre d'un sous-ensemble $A$ d'un espace métrique $X$ est donné
par : $$
\mbox{diam}(A) = \sup \, \{d(x, y) \, | \, x \in A, \, y \in A\}.
$$
:::

::: {.section}
### Proposition -- Suite de Cauchy et diamètre {#suite-de-cauchy-et-diamètre .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Suite de Cauchy et diamètre}`{=latex}

Une suite de points $x_k$ est de Cauchy si et seulement si $$
\lim_{k \to + \infty} \mbox{diam}(\{x_n \, | \, n \geq k \}) = 0.
$$
:::

::: {.section}
### Proposition -- Toute suite convergente est de Cauchy {#tscc .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Toute suite convergente est de Cauchy}`{=latex}

Toute suite de points convergente dans un espace métrique est de Cauchy.
:::

::: {.section}
#### Démonstration {#démonstration-9 .proof}

Soit $X$ un espace métrique et $x_k$ une suite convergente, de limite
$\ell$. Soit $\varepsilon > 0$ ; il existe un rang $m$ au-delà duquel on
a $d(x_k, \ell) \leq \varepsilon / 2.$ Par conséquent, si $n \geq m$ et
$p\geq m$, $$
d(x_n, x_p) \leq d(x_n, \ell) + d(\ell, x_p) \leq \varepsilon.
$$ La suite $x_k$ est donc de Cauchy.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Réciproque ?

Il est parfois plus facile de vérifier qu'une suite de points dans un
espace métrique satisfait le critère de Cauchy que de vérifier qu'elle
est convergente, en particulier quand la limite de la suite est
inconnue. Malheureusement, dans ce cadre très général, il n'est pas
possible en général de déduire la convergence du fait que la suite
vérifie le critère de Cauchy. Ainsi, dans $\mathbb{Q}$, considéré en
tant que sous-espace métrique de $\mathbb{R}$, la suite qui définie le
développement décimal de $\sqrt{2}$ à l'ordre $k$ : $$
x_k = \frac{a_k}{10^k} \, \mbox{ où } \, a_k = \max \, \{ n \in \mathbb{N}\, | \, n^2 \leq 2(10^k)^2\}
$$ est de Cauchy -- on peut prouver que $|x_n - x_p| \leq {1}/{10^m}$
quand $n \geq m$ et $p \geq m$ -- mais n'est pas convergente. En effet,
la suite converge dans $\mathbb{R}$, mais sa limite $\sqrt{2}$ est
irrationnelle ; cette suite n'a donc pas de limite dans $\mathbb{Q}$
(une telle limite serait aussi une limite dans $\mathbb{R}$, ce qui
contredirait son unicité.)

L'ensemble $\mathbb{R}$ possède une propriété bien utile qui fait défaut
à $\mathbb{Q}$ : toute suite de Cauchy y est convergente.
:::

::: {.section}
### Définition -- Espaces complets {#espaces-complets-1 .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Espaces complets}`{=latex}

Un espace métrique $X$ est *complet* si et seulement si toute suite de
Cauchy est convergente. Un espace vectoriel normé $E$ complet est
qualifié d'*espace de Banach[^3]*.
:::

::: {.section}
### Proposition -- Complétude de l'espace euclidien {#complétude-de-lespace-euclidien .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Complétude de l'espace euclidien}`{=latex}

L'espace $\mathbb{R}^n$ est complet.
:::

::: {.section}
#### Démonstration {#démonstration-10 .proof}

Dans les cas de $\mathbb{R}$ (c'est-à-dire quand $n=1$), le résultat est
une conséquence directe de la construction de $\mathbb{R}$ comme
complété de $\mathbb{Q}$([^4]). Pour des valeurs de $n > 1$, si $x_k$
est une suite de Cauchy, ses composantes $x_k^1, \dots, x_k^n$ sont
aussi de Cauchy car pour tout $i \in \{1, \dots, n\}$, $$
|x_n^i - x_p^i| \leq \left\|x_n - x_p\right\|.
$$ Comme $\mathbb{R}$ est complet, chaque suite $x_k^i$ admet donc une
limite, notée $\ell^i$. Si l'on note $\ell = (\ell^1, \dots, \ell^n)$,
on déduit de l'égalité $$
\|x_k - \ell\| = \sqrt{\sum_{i=1}^n (x_k^i - \ell^i)^2}
$$ la convergence de $x_k$ vers $\ell$. Toute suite de Cauchy de
$\mathbb{R}^n$ est donc convergente.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Proposition -- Caractérisation des sous-espaces complets {#sous-espaces-complets .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Caractérisation des sous-espaces complets}`{=latex}

Soit $X$ un espace métrique complet. Un sous-espace $Y$ de $X$ est
complet si et seulement si $Y$ est un sous-ensemble fermé de $X$.
:::

::: {.section}
#### Démonstration {#démonstration-11 .proof}

Si $Y$ est complet, [toute suite de point de $Y$ qui converge dans $X$
est de Cauchy (p. `\pageref*{tscc}`{=tex})](#tscc), donc a une limite
dans $Y$ puisque celui-ci est complet. L'ensemble $Y$ est donc fermé
dans $X$.

Réciproquement, si $Y$ est fermé dans $X$ et qu'une suite de points de
$Y$ est de Cauchy, elle converge dans $X$ qui est complet et par
conséquent dans $Y$. Le sous-espace $Y$ est donc
complet.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Proposition -- Existence d'un maximum {#existence-dun-maximum .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Existence d'un maximum}`{=latex}

Si $K \subset \mathbb{R}^n$ est fermé et borné, toute fonction continue
$f: K \to \mathbb{R}$ atteint son maximum : $$
\mbox{il existe $a \in K$ tel que } f(a) = \max_{x \in K} f(x).
$$
:::

::: {.section}
En composant une fonction continue vectorielle $f: K \to \mathbb{R}^m$
et la fonction continue norme, on en déduit en particulier :
:::

::: {.section}
### Corollaire -- Borne des fonctions continues {#borne-des-fonctions-continues .corollary .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Borne des fonctions continues}`{=latex}

Si $K \subset \mathbb{R}^n$ est fermé et borné, toute fonction continue
$f: K \subset \mathbb{R}^n \to \mathbb{R}^m$ est bornée : $$
\|f\|_{\infty} := \sup_{x \in K} \|f(x)\| = \max_{x \in K} \|f(x)\| < + \infty.
$$
:::

::: {.section}
#### Démonstration -- Existence d'un maximum {#demo-minimum .proof}

Soit $x_k$ une suite de valeurs de $K$ maximisante pour $f$,
c'est-à-dire telle que $$
\lim_{k \to +\infty} f(x_k) = \sup_{x \in K} f(x) \in \left]0, +\infty\right].
$$ S'il existe une valeur $x \in K$ empruntée une infinité de fois par
la suite $x_k$, la fonction $f$ atteint son maximum en $x$ et la preuve
est achevée. Dans le cas contraire -- ce que nous supposerons désormais
-- toute suite extraite $y_j$ de $x_k$ prend une infinité de valeurs
distinctes et $\lim_{j \to +\infty} f(y_j) = \sup_{x \in K} f(x).$

Pour tout $j \in \mathbb{N}$, l'ensemble $K$ étant borné, il peut être
recouvert par un nombre fini d'ensembles du pavage régulier
$\mathcal{P}_j$ de $\mathbb{R}^n$ composé des pavés : $$
[i_1 2^{-j}, (i_1+1) 2^{-j}] \times \dots \times [i_n 2^{-j}, (i_n+1) 2^{-j}], \; (i_1, \dots, i_n) \in \mathbb{Z}^n.
$$ Dans la collection finie de pavé de $\mathcal{P}_0$ nécessaire pour
recouvrir $K$, il en existe nécessairement au moins un qui contient une
infinité de valeurs de $x_k$ ; notons $P_0$ ce pavé et $y_0$ la première
valeur $x_{k_0}$ de $x_k$ qui soit dans $P_0$. Parmi les $2^n$ pavés de
$\mathcal{P}_1$ qui suffisent pour couvrir $P_0$, l'un d'entre eux au
moins contient une infinité de $x_k$, $k\geq k_1$ ; notons $P_1$ ce pavé
et $y_1$ la première valeur $x_{k_1}$ de $x_k$, $k>k_0$ qui soit dans
$P_1$.

En itérant ce procédé, on construit une suite extraite $y_j$ de $x_k$ et
de pavés $P_j$ tels que $$
\mbox{pour tout $j \in \mathbb{N}$, }
y_j \in P_j \in \mathcal{P}_j
\mbox{ et }
P_{j+1} \subset P_j.
$$

![Suite de pavés imbriqués $P_j$ et suite $y_j$ extraite des
$x_k$.](images/maximum.svg.pdf)

Comme $\mathrm{diam}(P_j) = \sqrt{n} 2^{-j}$, on a pour tout
$j \in \mathbb{N}$ $$
\mathrm{diam}(\{y_i \; | \; i\geq j\}) \leq \sqrt{n} 2^{-j} \to 0
\; \mbox{ quand } \; j\to +\infty.
$$ La suite $y_j$ est donc de Cauchy ; elle a donc une limite dans $K$,
qui est [complet comme sous-ensemble fermé dans l'espace complet
$\mathbb{R}^n$ (p.
`\pageref*{sous-espaces-complets}`{=tex})](#sous-espaces-complets). Si
$\ell \in K$ est sa limite on a donc par continuité de $f$ $$
\sup_{x \in K} f(x) = \lim_{j \to +\infty} f(y_j) = f(\ell).
$$ La fonction $f$ admet donc un maximum en
$\ell$.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Définition -- Application contractante {#application-contractante .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Application contractante}`{=latex}

Soit $X$ un espace métrique. Une fonction $f: X \to X$ est
*$\kappa$-contractante*, où $\kappa \in \left[0, 1\right[$, si pour tout
couple de points $x$ et $y$ de $X$, on a $$
d(f(x), f(y)) \leq \kappa d(x, y).
$$ Une telle application est *contractante* si elle est
$\kappa$-contractante pour un $\kappa \in \left[0, 1\right[$.
:::

::: {.section}
### Théorème -- Théorème de point fixe de Banach {#T-TPFB .theorem .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Théorème de point fixe de Banach}`{=latex}

Soit $f: X \to X$ une application contractante dans un espace métrique
$X$ complet. L'application $f$ admet un unique *point fixe* $x$,
c'est-à-dire une unique solution $x \in X$ à l'équation $$
  x = f(x).
  $$
:::

::: {.section}
#### Démonstration {#démonstration-12 .proof}

L'unicité du point fixe (l'existence d'au plus une solution à $x=f(x)$)
est simple à établir : si $x$ et $y$ sont deux points fixes de $f$,
c'est-à-dire si $x=f(x)$ et $y=f(y)$, alors $d(x, y) = d(f(x), f(y))$.
L'application $f$ étant $\kappa$-contractante, on a donc $$
d(x, y) = d(f(x), f(y)) \leq \kappa d(x, y);
$$ et puisque $0\leq \kappa < 1$, cette inégalité entraîne
$d(x , y) = 0$, soit $x=y$.

Quant à l'existence du point fixe, sa preuve est constructive : nous
allons établir que quel que soit le choix de $x_0 \in E$, la suite de
valeurs définie par $$
x_{n+1} = f(x_n)
$$ converge vers un point fixe. Le point crucial est d'établir que cette
suite admet une limite $\ell$ ; en effet, si ce résultat est acquis, en
passant à la limite sur $n$ dans la relation de récurrence et exploitant
la continuité de l'application $f$, on obtient $$
\ell = \lim_{n \to +\infty} x_{n+1} = \lim_{n \to +\infty}f(x_n) = f(\ell).
$$ À cette fin, nous allons prouver que la suite des $x_n$ est de
Cauchy; l'existence d'une limite se déduira alors de la complétude de
$X$. On remarque tout d'abord que pour tout entier $n$, $$
d(x_{n+2}, x_{n+1}) = d(f(x_{n+1}), f(x_n)) \leq \kappa d(x_{n+1}, x_n),
$$ ce qui par récurrence fournit pour tout $n$ $$
d(x_{n+1}, x_n) \leq \kappa^n d(x_1, x_0).
$$ Par [l'inégalité triangulaire (p.
`\pageref*{dist-ineg}`{=tex})](#dist-ineg), pour tout couple d'entiers
$n$ et $p$, on a $$
d(x_{n+p} , x_n) 
\leq \sum_{k=0}^{p-1} d(x_{n+k+1} , x_{n+k})
\leq \sum_{k=0}^{p-1} \kappa^{n+k} d(x_{1}, x_{0}).
$$ Dans le second membre apparaît une somme de termes d'une suite
géométrique : $$
\sum_{k=0}^{p-1} \kappa^{n+k} = \kappa^n \frac{1 - \kappa^{p}}{1 - \kappa}
\leq \frac{\kappa^n}{1 - \kappa};
$$ on en déduit $$
d(x_{n+p}, x_n) 
\leq  
\frac{\kappa^n}{1 - \kappa} d(x_{1}, x_{0}).
$$ Le second membre de cette inégalité tend vers $0$ indépendamment de
$p$ quand $n$ tend vers $+\infty$; la suite des $x_n$ est bien de
Cauchy.`\hfill$\blacksquare$`{=latex}
:::
:::

::: {.section}
Annexe -- Espaces produits
==========================

::: {.section}
### Définition -- Produit d'espaces vectoriels normés {#produit-despaces-vectoriels-normés .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Produit d'espaces vectoriels normés}`{=latex}

On appelle *produit des espaces vectoriels normés $E_1$, $\dots$,
$E_n$*, munis des normes $\|\cdot\|_{E_1}$, $\dots$, $\|\cdot\|_{E_n}$,
l'espace vectoriel
$E := \prod_{k=1}^n E_k := E_1 \times \dots \times E_n$, muni de la
norme $$
\|(x_1,\dots, x_n)\| := \sqrt{\|x_1\|_{E_1}^2 + \dots + \|x_n\|_{E_n}^2}.
$$
:::

::: {.section}
### Définition -- Produit d'espaces métriques {#produit-despaces-métriques .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Produit d'espaces métriques}`{=latex}

On appelle *produit des espaces métriques $X_1$, $\dots$, $X_n$,* munis
des distances $d_{X_1}$, $\dots$, $d_{X_n}$ le produit cartésien
$X = \prod_{k=1}^n X_k = X_1 \times \dots \times X_n$, muni de la
distance $$
d((x_1,\dots, x_n), (y_1,\dots, y_n)) 
= \sqrt{d_{X_1}(x_1, y_1)^2 + \dots + d_{X_n}(x_n, y_n)^2}.
$$
:::

::: {.section}
### Proposition -- Continuité des projections {#continuité-des-projections .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Continuité des projections}`{=latex}

Soient $X_1$, $\dots$, $X_n$ des espaces métriques. Pour tout
$k \in \{1,\dots, n\}$, l'application
$p_k: \prod_{j} X_j \to x_k \in X_k$ telle que
$$p_k(x_1,\dots,x_k,\dots x_n) = x_k$$ est continue.
:::

::: {.section}
#### Démonstration {#démonstration-13 .proof}

Pour tout couple $x$ et $x^0\in \prod_{j=1}^n X_j$, on a $$
d_{X_k}(x_k, x_k^0) 
\leq \sqrt{d_{X_1}(x_1, x_1^0)^2 + \dots  + d_{X_n}(x_n, x_n^0)^2} 
= d(x, x^0),
$$ par conséquent, $x_k \to x_k^0$ quand
$x \to x_0$.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Proposition -- Continuité des injections {#continuité-des-injections .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Continuité des injections}`{=latex}

Soient $X_1$, $\dots$, $X_n$ des espaces métriques. Pour tout
$k \in \{1,\dots, n\}$, l'application $i_k: X_k \to \prod_{j=1}^n X_j$
telle que $$i_k(x_k) = (0,\dots,0, x_k,0 \dots 0)$$ est continue.
:::

::: {.section}
#### Démonstration {#démonstration-14 .proof}

Pour tout couple $x_k$ et $x_k^0 \in X_k$, on a `\begin{align*}
d(i_k(x_k), i_k(x_k^0)) &= d((0,\dots x_k,\dots 0), (0,\dots, x_k^0,\dots, 0)) 
\\ &= \sqrt{0 + \dots d(x_k, x_k^0)^2+\dots + 0} \\ &= d_{X_k}(x_k, x_k^0),
\end{align*}`{=tex} donc $i_k(x_k) \to i_k(x_k^0)$ quand
$x_k \to x_k^0$.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Proposition -- Continuité de la distance {#continuité-de-la-distance .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Continuité de la distance}`{=latex}

La fonction distance $d: X \times X \to \left[0, +\infty\right[$ est une
application continue pour tout espace métrique $(X, d)$.
:::

::: {.section}
#### Démonstration {#démonstration-15 .proof}

Soient $(x_0, y_0)$ et $(x, y)$ deux points de l'espace produit
$X \times X$. Par [l'inégalité triangulaire (p.
`\pageref*{dist-ineg}`{=tex})](#dist-ineg),
$d(x, y) \leq d(x, x_0) + d(x_0, y_0) + d(y_0, y)$ et
$d(x_0, y_0) \leq d(x_0, x) + d(x, y) + d(y, y_0),$ donc $$
|d(x, y) - d(x_0, y_0)| \leq d(x_0, x) + d(y_0, y).
$$ Or la distance sur le produit $X \times X$ est définie comme $$
d_{X \times X}((x, y), (x_0, y_0)) = \sqrt{d(x, x_0)^2 + d(y, y_0)^2},
$$ donc $$
|d(x, y) - d(x_0, y_0)| \leq 2 d_{X \times X}((x, y), (x_0, y_0))
$$ et $d(x, y) \to d(x_0, y_0)$ quand $(x, y) \to (x_0, y_0)$,
$(x,y) \neq (x_0, y_0)$.`\hfill$\blacksquare$`{=latex}
:::
:::

::: {.section}
Annexe -- Compacité
===================

::: {.section}
### Définition -- Compacité séquentielle {#compacité-séquentielle .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Compacité séquentielle}`{=latex}

Un ensemble $K$ d'un espace métrique est *(séquentiellement) compact* si
toute suite de points de $K$ admet une sous-suite qui converge dans $K$.
:::

::: {.section}
### Théorème -- Théorème de Heine-Borel {#théorème-de-heine-borel .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Théorème de Heine-Borel}`{=latex}

Un ensemble $K$ de l'espace euclidien $\mathbb{R}^n$ est compact si et
seulement s'il est fermé et borné.
:::

::: {.section}
#### Démonstration {#démonstration-16 .proof}

Supposons $K$ compact ; soit $x_k$ une suite de points de $K$ qui
converge dans $\mathbb{R}^n$, vers une limite notée $\ell$. Il existe
alors une sous-suite $y_k$ de $x_k$ qui converge dans $K$; or comme
cette sous-suite a la même limite que $x_k$, $\ell$ appartient à $K$.
L'ensemble $K$ est donc fermé.

Si $K$ est non-borné, il existe une suite $x_k$ non-bornée de points de
$K$. Toute sous-suite de $x_k$ étant également non-bornée, elle ne peut
donc converger et par conséquent $K$ ne peut pas être compact.

Finalement, supposons $K$ fermé et borné. La construction d'une
sous-suite convergente extraite d'une suite arbitraire $x_k$ de $K$ est
identique à celle effectuée dans [la démonstration de l'existence d'un
maximum d'une fonction scalaire continue définie sur un fermé borné de
$\mathbb{R}^n$ (p.
`\pageref*{demo-minimum}`{=tex})](#demo-minimum).`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Théorème -- Image d'un compact {#image-dun-compact .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Image d'un compact}`{=latex}

L'image d'un ensemble compact par une application continue est un
ensemble compact.
:::

::: {.section}
#### Démonstration {#démonstration-17 .proof}

Soit $f: K \subset X \to Y$ où $X$ et $Y$ sont deux espaces métriques et
$K$ un sous-ensemble compact de $X$. Soit $y_k$ une suite de points de
$f(K)$ ; par construction, il existe une suite de points $x_k$ de $K$
tels que $f(x_k) = y_k$. Soit $z_k$ une sous-suite de $x_k$ qui converge
vers un $\ell \in K$; par continuité de $f$ en $\ell$, la suite des
$f(z_k)$ -- qui est une suite extraite des $y_k$ -- converge vers
$f(\ell) \in f(K)$. L'ensemble $f(K)$ est donc
compact.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Corollaire -- Existence d'un maximum {#T-EM .corollary .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Existence d'un maximum}`{=latex}

Une fonction continue $f: K \to \mathbb{R}$ définie sur un ensemble
compact $K$ admet un maximum global.
:::

::: {.section}
#### Démonstration {#démonstration-18 .proof}

Soit $x_k \in K$ une suite maximisante de $f$, c'est-à-dire telle que $$
\lim_{k \to +\infty} f(x_k) = \sup_{x \in K} f(x).
$$ Il existe une suite $y_k$ extraite de $x_k$ qui converge vers un
point $\ell$ de $K$. Par continuité de $f$ en $\ell$, on a $$
f(\ell) = \lim_{k \to +\infty} f(y_k) = \sup_{x \in K} f(x).
$$ La fonction $f$ admet donc un maximum en
$\ell$.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Proposition -- Complétude de l'espace des fonctions bornées {#cfb .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Complétude de l'espace des fonctions bornées}`{=latex}

Soit $X$ un ensemble et $Y$ un espace vectoriel normé complet.
L'ensemble des fonctions $f$ de $X$ dans $Y$ bornées -- telles qu'il
existe un $M\geq 0$ tel que pour tout $x \in X$, $\|f(x)\| \leq M$ --
muni de la norme de la convergence uniforme $$
\|f\|_{\infty} := \sup_{x \in X} \|f(x)\|
$$ est complet.
:::

::: {.section}
#### Démonstration {#démonstration-19 .proof}

Soit $f_k$ une suite de fonctions bornées qui soit de Cauchy pour la
norme de la convergence uniforme. Pour tout $\varepsilon > 0$, il existe
un rang $m \in \mathbb{N}$ tel que si $n\geq m$ et $p\geq m$, on ait $$
\sup_{x \in X} \|f_n(x) - f_p(x)\| \leq \varepsilon.
$$ Par conséquent, pour tout $x \in X$, on a
$\|f_n(x) - f_p(x)\| \leq \varepsilon$, donc la suite des $f_k(x)$ est
de Cauchy dans $Y$. L'espace $Y$ étant par hypothèse complet, cette
suite a une limite, que nous notons $f_{\infty}(x)$. Par [continuité de
la distance (p.
`\pageref*{distance-continue}`{=tex})](#distance-continue), pour tout
$x \in X$ et tout $n \geq m$, on a $$
\|f_n(x) - f_{\infty}(x)\| 
= \lim_{p \to +\infty} \|f_n(x) - f_p(x)\| 
\leq \varepsilon
$$ et donc $\sup_{x \in X} \|f_n(x) - f_{\infty}(x) \|\leq \varepsilon$.
La fonction $f_{\infty}$ est donc bornée, car $$
\|f_{\infty}(x)\| \leq \|f_n(x)\| + \varepsilon,
$$ et est a limite uniforme de la suite des
$f_k$.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Proposition -- Complétude de l'espace des fonctions continues {#complétude-de-lespace-des-fonctions-continues .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Complétude de l'espace des fonctions continues}`{=latex}

Soit $X$ un espace métrique compact et $Y$ un espace vectoriel normé
complet. L'ensemble des fonctions continues de $X$ dans $Y$ muni de la
norme de la convergence uniforme $$
\|f\|_{\infty} := \sup_{x \in X} \|f(x)\|
$$ est complet.
:::

::: {.section}
#### Démonstration {#démonstration-20 .proof}

En préambule : pour toute fonction $f$ continue de $X$ dans $Y$, la
fonction $$x \in X \mapsto \|f(x)\| = d(f(x), 0) \in \mathbb{R},$$
[continue (p. `\pageref*{distance-continue}`{=tex})](#distance-continue)
et définie sur un compact, et donc [admet un maximum (p.
`\pageref*{T-EM}`{=tex})](#T-EM) ; la fonction $f$ est donc bornée.
L'espace des fonction continues de $X$ dans $Y$ est donc un sous-espace
métrique de l'espace des fonctions bornées de $X$ dans $Y$.

Soit $f_k$ une suite de Cauchy de fonctions continues de $X$ dans $Y$.
Cette suite est convergente dans l'espace des fonctions bornées en
raison de [la complétude de ce dernier (p.
`\pageref*{cfb}`{=tex})](#cfb). Il nous suffit de montrer que sa limite
(uniforme) est continue pour conclure la preuve.

Soit $f$ la limite des $f_k$ et soit $\varepsilon > 0$. Soit $k$ tel que
$$\sup_{x \in X}\|f_k(x) - f(x)\| \leq \varepsilon /3.$$ Pour tout
$x \in X$, $f_k$ étant continue en $x$, pour $y$ assez proche de $x$ on
a $\|f_k(x) - f_k(y)\| \leq \varepsilon /3.$ Or, par [l'inégalité
triangulaire (p. `\pageref*{norme-ineg}`{=tex})](#norme-ineg), $$
\|f(x) - f(y)\| \leq \|f(x) - f_k(x)\|  + \|f_k(x) - f_k(y)\| + \|f_k(y) - f(y)\|
\leq \varepsilon.
$$ La fonction $f$ est donc continue.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
La notion de compacité peut également être définie dans des espaces
topologiques généraux, sans recourir à une distance ou aux suites de
points.
:::

::: {.section}
### Définition -- Propriété de l'intersection finie {#propriété-de-lintersection-finie .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Propriété de l'intersection finie}`{=latex}

Une collection d'ensembles vérifie la propriété de l'intersection finie
si toute sous-collection finie est d'intersection non vide.
:::

::: {.section}
### Définition -- Compacité et propriété de l'intersection finie {#compacité .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Compacité et propriété de l'intersection finie}`{=latex}

Un ensemble $K$ d'un espace topologique est *compact* si pour toute
collection de sous-ensembles de $K$ vérifiant la propriété de
l'intersection finie, il existe un point adhérent à tous les ensembles
de la collection.

Autrement dit, si pour tout $A \in \mathcal{A}$, $A$ est un
sous-ensemble de $K$ et si pour toute suite finie
$A_1, \dots, A_k \in \mathcal{A}$ il existe un $x \in K$ tel que
$x \in A_1\cap \dots \cap A_k$, alors il existe un $x \in K$ adhérent à
tout $A \in \mathcal{A}$.
:::

::: {.section}
### Compacité et compacité séquentielle

Dans les espaces métriques, compacité et compacité séquentielle sont
équivalentes.
:::

::: {.section}
#### Démonstration {#démonstration-21 .proof}

Supposons que $K$ est un sous-ensemble compact de l'espace métrique $X$.
Soit $x_k$ une suite de points de $K$. Considerons la collection
d'ensembles $\mathcal{A}$ définie par $$
\mathcal{A} = \{A_k \, | \, k \in \mathbb{N} \}
\; \mbox{ où } \; A_k = \{x_j \,| \, j \geq k \}.
$$ La collection $\mathcal{A}$ vérifie la propriété d'intersection
finie : en effet, si $A_{k_1}$, $A_{k_2}$, $\dots$,
$A_{k_p} \in \mathcal{A}$, alors $$
A_{k_1} \cap A_{k_2} \cap \dots \cap A_{k_p} = A_{k} 
\; \mbox{ avec } \; k = \max(k_1, \dots, k_p)
$$ et donc leur intersection est non-vide. Par conséquent, il existe un
$x \in K$ tel que pour tout rang $k$, $x$ adhère à
$A_k = \{x_j \,| \, j \geq k \}$, c'est-à-dire
$d(x, \{x_j \,| \, j \geq k \}) = 0$. En particulier, il existe un
$y_0 := x_{k_0} \in A_0$ tel que $d(x, y_0) \leq 2^{-0}$, un
$y_1 := x_{k_1} \in A_{k_0+1}$ tel que $d(x, y_1) \leq 2^{-1}$, etc. La
suite $y_k$ est extraite de $x_k$ et vérifie $d(x, y_k) \leq 2^{-k}$,
elle converge donc vers $x$. De toute suite de points de $K$ on peut
donc extraire une sous-suite qui converge dans $K$: $K$ est donc
séquentiellement compact.

Réciproquement, supposons $K$ séquentiellement compact. Nous allons
montrer que si $\mathcal{A}$ est une collection d'ensembles de $K$ telle
que $$
\bigcap_{A \in \mathcal{A}} \, \overline{A} = \varnothing,
$$ où $\overline{A}$ désigne l'adhérence de $A$ dans $K$, alors il
existe un nombre fini d'ensemble de $\mathcal{A}$ dont l'intersection
est vide ; nous aurons alors établi la contraposée de la propriété qui
définit la compacité de $K$ et donc la compacité de $K$. Au préalable,
nous allons montrer que sous l'hypothèse ci-dessus d'intersection vide
des adhérences, il existe un $\varepsilon > 0$ tel que pour tout
$x\in K$, on peut trouver un $A \in \mathcal{A}$ tel que
$B(x, \varepsilon) \cap \overline{A} = \varnothing$. En effet, si cette
propriété n'était pas vérifiée, on pourrait construire une suite $x_k$
de points de $K$ telle que pour tout $A \in \mathcal{A}$, il existe un
$a^A_k \in \overline{A}$ tel que $d(x_k, a^A_k) < 2^{-k}$. Mais une
telle suite aurait alors une sous-suite convergente ; la limite serait
dans l'adhérence de chacun des $A \in \mathcal{A}$, en contradiction
avec l'hypothèse initiale. On utilise ce résultat de la façon suivante :
on sélectionne un $x_0 \in K$ et un $A_0 \in \mathcal{A}$ tel que
$\overline{A_0} \cap B(x_0, \varepsilon) = \varnothing$, puis un
$x_1 \in K \setminus B(x_0, \varepsilon)$ et un $A_1 \in \mathcal{A}$
tel que $\overline{A_1} \cap B(x_1, \varepsilon) = \varnothing$, ce qui
induit $$
(\overline{A_0} \cap \overline{A_1}) \cap (B(x_0, \varepsilon) \cup B(x_1, \varepsilon)) = \varnothing,
$$ puis un
$x_2 \in K \setminus (B(x_0, \varepsilon) \cup B(x_1, \varepsilon))$ et
un $A_2 \in \mathcal{A}$ tel que
$\overline{A_2} \cap B(x_2, \varepsilon) = \varnothing$, etc. Le procédé
s'arrête en un nombre fini d'étapes, dès que
$B(x_0,\varepsilon) \cup \dots \cup B(x_k, \varepsilon)$ recouvre $K$.
Cela arrive nécessairement puisque les $x_k$ ainsi construits vérifient
$d(x_i, x_j) \geq \varepsilon$ si $i\neq j$ ; si cette suite était
infinie, elle ne pourrait admettre de suite extraite convergente, en
contradiction avec l'hypothèse de compacité séquentielle. Par
conséquent, il existe un rang $k$ tel que $$
K \subset B(x_0,\varepsilon) \cup \dots \cup B(x_k, \varepsilon)
$$ et comme $$
(\overline{A_0} \cap \dots \cap \overline{A_k}) 
\cap (B(x_0, \varepsilon) \cup \dots \cup B(x_k, \varepsilon)) = \varnothing,
$$ on en déduit que
$\overline{A_0} \cap \dots \cap \overline{A_k} = \varnothing$ et donc
que $A_0 \cap \dots \cap A_k = \varnothing$, ce qui conclut la
preuve.`\hfill$\blacksquare$`{=latex}
:::
:::

::: {.section}
Annexe -- Espace topologique
============================

::: {.section}
### Structure topologique d'un espace métrique

Dans un espace métrique, il est possible de se livrer à un exercice
d'abstraction en considérant le test d'adhérence entre un point et un
ensemble associé à la distance $$
\mbox{$x$ adhère à $A$} \, \Leftrightarrow \, d(x, A)= 0
$$ et en "oubliant" ensuite la distance qui a servi à construire ce
test. On remplace ainsi une mesure quantitative de proximité entre
points et ensembles par une mesure uniquement qualitative (on teste si
"$x$ est à distance nulle de $A$").

Alternativement, on peut doter un ensemble $X$ directement d'un test
d'adhérence, tant que celui-ci vérifie les axiomes suivants :
:::

::: {.section}
### Définition -- Test d'adhérence {#ak .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Test d'adhérence}`{=latex}

Un *test d'adhérence* sur l'ensemble *X* est une relation entre éléments
de $X$ et sous-ensembles de $X$ telle que :

1.  Aucun point n'adhère à l'ensemble vide,

2.  Tout point d'un ensemble adhère à cet ensemble,

3.  Un point adhère à l'union de deux ensembles si et seulement s'il
    adhère à l'un des deux ensembles,

4.  Un point qui adhère à l'ensemble des points adhérents à un ensemble
    adhère à cet ensemble.
:::

::: {.section}
### Définition -- Espace topologique {#espace-topologique .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Espace topologique}`{=latex}

Un *espace topologique* est un ensemble muni d'[un test d'adhérence (p.
`\pageref*{ak}`{=tex})](#ak). Les éléments de l'ensemble sont appelés
des *points*, ses sous-ensembles des *ensembles de points*.
:::

::: {.section}
### Définition -- Sous-espace topologique {#sous-espace-topologique .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Sous-espace topologique}`{=latex}

Un sous-ensemble $Y$ d'un espace topologique $X$ est un *sous-espace
topologique* de $X$ lorsqu'il est muni du test d'adhérence de $X$,
restreint aux points et sous-ensembles de $Y$.
:::

::: {.section}
### Définition -- Continuité {#continuité-1 .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Continuité}`{=latex}

Une application $f: X \to Y$ définie entre deux espaces topologiques est
*continue en $x \in X$* si, lorsque $x$ adhère à $A$ dans $X$, $f(x)$
adhère à $f(A)$ dans $Y$. Une application continue en tout point
$x \in X$ est *continue (sur $X$)*.
:::

::: {.section}
Les applications continues sont les *morphismes* des espaces
topologiques : elle préservent la structure des espaces topologiques.
:::

::: {.section}
Cette caractérisation "abstraite" des fonctions continues est compatible
avec celle adoptée dans les espaces métriques, puisque cette définition
y est également [une caractérisation de la continuité (p.
`\pageref*{cad}`{=tex})](#cad).

Elle se prête à des preuves concises de certains résultats ; ainsi :
:::

::: {.section}
### Composée d'applications continues

La composée de fonctions $f:X \to Y$ continue en $x \in X$ et $g:Y\to Z$
continue en $f(x) \in Y$ est continue en $x$.
:::

::: {.section}
#### Démonstration {#démonstration-22 .proof}

Si $x$ adhère à $A$, par continuité de $f$ en $x$, $f(x)$ adhère à
$f(A)$ ; donc par continuité de $g$ en $y=f(x)$, $g(y)= (g \circ f)(x)$
adhère à $g(f(A)) = (g \circ f)(A)$. La composée de $f$ et de $g$ est
donc continue en $x$.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Les espaces métriques sont des espaces topologiques

Soit $X$ un espace métrique muni d'une distance $d$. La relation définie
par $$
x \mbox{ adhère à } A \, \Leftrightarrow \, d(x, A) = 0
$$ est un test d'adhérence sur $X$.
:::

::: {.section}
#### Démonstration {#démonstration-23 .proof}

1.  Le point $x$ adhère à l'ensemble vide si et seulement si
    $d(x, \varnothing) = 0$, mais $$
    d(x, \varnothing) = \inf_{y \in \varnothing} d(x, y) = +\infty, 
    $$ par conséquent aucun point d'adhère à l'ensemble vide.

2.  Si $x \in A$, on a $$
    d(x, A) = \inf_{y \in A} d(x, y) = d(x, x) = 0,
    $$ donc $x$ adhère à $A$.

3.  Si $x$ adhère à $A$, c'est-à-dire si $d(x,A)=0$, alors $$
    0 \leq d(x, A \cup B) = \inf_{y \in A \cup B} d(x, y)
    \leq  \inf_{y \in A} d(x, y) = d(x, A)= 0
    $$ et donc $x$ adhère à $A \cup B$. De la même façon, du fait de la
    symétrie des rôles des ensembles $A$ et $B$, si $x$ adhère à $B$
    alors $x$ adhère à $A \cup B$.

    Réciproquement, si $x$ adhère à $A \cup B$, alors il existe une
    suite de points $x_k$ de $A \cup B$ telle que $d(x, x_k) \to 0$
    quand $k \to +\infty$. Cette suite $x_k$ admet une suite extraite de
    points de $A$ et/ou une suite extraite de points de $B$. Dans le
    premier cas on a donc $d(x, A)=0$ et dans le second $d(x, B)=0$,
    c'est-à-dire que $x$ adhère à $A$ et/ou à $B$.

4.  Les points $y$ qui adhèrent à l'ensemble $A$ sont caractérisés par
    $d(y, A) = 0$. Par conséquent, l'ensemble des points $x$ qui
    adhèrent à cet ensemble sont caractérisés par $$
    d(x, \{y \in X \, | \, d(y, A) = 0\}) = 0.
    $$ Pour tout $x$ de ce type et pour tout $\varepsilon > 0$, il
    existe un $y$ tel que $d(y, x) \leq \varepsilon /2$ et $d(y, A)= 0$
    et donc un $z \in A$ tel que $d(y, z) \leq \varepsilon/2$.
    L'[inégalité triangulaire (p.
    `\pageref*{dist-ineg}`{=tex})](#dist-ineg) fournit donc $$
    d(x, A) = \inf_{a \in A} d(x, a) \leq d(x, z) 
    \leq d(x, y) + d(y, z) \leq \varepsilon
    $$ et comme $\varepsilon >0$ est arbitraire, $d(x, A)=0$ : $x$
    adhère à $A$.

$\;\; \blacksquare$
:::

::: {.section}
### L'espace topologique généralise l'espace métrique

Les espaces métriques "sont" donc des espaces topologiques (c'est-à-dire
héritent automatiquement d'un test d'adhérence, défini à partir de leur
distance). A l'inverse, les espaces topologiques qui peuvent être muni
d'une distance compatible avec leur test d'adhérence sont dits
*métrisables*. Toutefois, tous les espaces topologiques ne sont pas
métrisables[^5]; la notion d'espace topologique est donc strictement
plus générale que la notion d'espace métrique.
:::

::: {.section}
### Définition -- Définitions topologiques {#définitions-topologiques .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Définitions topologiques}`{=latex}

Soit $X$ un espace topologique et $A$ un ensemble de points de $X$.

-   L'*adhérence* $\overline{A}$ d'un ensemble $A$ est constituée des
    points qui adhèrent à l'ensemble $A$.

-   Un ensemble $A$ est *fermé* s'il est égal à son adhérence : $$
    A = \overline{A} \; \mbox{ ou } \; (x \in \overline{A} \Leftrightarrow x \in A).
    $$

-   Un point est *frontière* de $A$ s'il appartient à l'adhérence de $A$
    et à celle de son complémentaire : $$
    x \in \partial{A} 
    \; \Leftrightarrow \; 
    (x \in \overline{A} = 0 \mbox{ et } x \in \overline{A^c}).
    $$

-   Un point $x$ est *intérieur* à un ensemble $A$ s'il n'adhère pas au
    complémentaire de $A$ $$
    x \in A^{\circ}
    \; \Leftrightarrow \; 
    x \not \in \overline{A^c}.
    $$

-   Un ensemble $V$ est un *voisinage* d'un point $x$ de $X$ si $x$ est
    intérieur à $V$ $$
    \mbox{$V$ voisinage de $x$} 
    \; \Leftrightarrow \; 
    x \not \in \overline{V^c}.
    $$

-   Un ensemble $A$ est *ouvert* s'il est un voisinage de chacun de ses
    points $$
    A = A^{\circ}
    \; \Leftrightarrow \; 
    (x \in A \Rightarrow x \not \in \overline{A^c}).
    $$
:::

::: {.section}
### Calcul topologique -- Axiomes de Kuratowksi {#calcul-topologique-axiomes-de-kuratowksi .ante}

Avec l'opération d'adhérence $\overline{(\cdot)}$, [les axiomes
définissant un test d'adhérence (p. `\pageref*{ak}`{=tex})](#ak) -- et
donc un espace topologique -- prennent une forme symbolique simple :

1.  $\overline{\varnothing} = \varnothing$,

2.  $A \subset \overline{A}$,

3.  $\overline{A \cup B} = \overline{A} \cup \overline{B}$,

4.  $\overline{\overline{A}} = \overline{A}$.
:::

::: {.section}
### Théorème -- Ouverts et fermés {#ouverts-et-fermés .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Ouverts et fermés}`{=latex}

Un ensemble est ouvert si et seulement si son complémentaire est fermé ;
un ensemble est fermé si et seulement si son complémentaire est ouvert.
:::

::: {.section}
#### Démonstration {#démonstration-24 .proof}

En raisonnant par équivalence, le complémentaire $F = U^c$ d'un ensemble
ouvert $U$ -- qui vérifie aussi $U = F^c$ -- est caractérisé par $$
x \in F^c \Rightarrow x \not \in \overline{(F^c)^c},
$$ soit $x \in F^c \Rightarrow x \not \in \overline{F}$. La contraposée
de cette implication -- qui est une proposition logiquement équivalente
-- est $x \in \overline{F} \Rightarrow x \in F$. Comme
$F \subset \overline{F}$, cela équivaut $\overline{F} =F$, c'est-à-dire
au caractère fermé de $F$.

La démonstration de la seconde partie de l'énoncé est immédiate (le
complémentaire du complémentaire d'un ensemble est cet
ensemble).`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Théorème -- Continuité et image réciproque {#CIR-topo .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Continuité et image réciproque}`{=latex}

Une fonction $f: X \to Y$ où $X$ et $Y$ sont des espaces topologiques
est continue si et seulement si l'image réciproque de tout ensemble
fermé (resp. ouvert) de $Y$ par $f$ est un ensemble fermé (resp. ouvert)
de $X$.
:::

::: {.section}
#### Démonstration {#démonstration-25 .proof}

Supposons $f$ continue. Si $B$ est un ensemble fermé de $Y$, par
continuité, $$
  f(\overline{f^{-1}(B)}) 
  \subset 
  \overline{f(f^{-1}(B))} 
  \subset \overline{B}
  =
  B.
  $$ Prendre l'image réciproque des deux membre de cette équation
fournit $$
  \overline{f^{-1}(B)} = f^{-1}(B),
  $$ par conséquent $f^{-1}(B)$ est fermé.

Réciproquement, supposons que l'image réciproque de tout ensemble fermé
est un ensemble fermé. Soit $A$ un sous-ensemble de $X$ ; l'ensemble
$\overline{f(A)}$ étant fermé, $$
  \overline{f^{-1}(\overline{f(A)})}
  = 
  f^{-1}(\overline{f(A)}).
  $$ Comme $A \subset f^{-1}(\overline{f(A)})$, on a
$\overline{A} \subset f^{-1}(\overline{f(A)})$, donc $$
  f(\overline{A}) 
  \subset f(f^{-1}(\overline{f(A)})) 
  \subset \overline{f(A)}.
  $$ Comme $A$ est arbitraire, $f$ est continue.

Montrons la variante avec des ensembles ouverts plutôt que fermés.
Supposons $f$ continue ; si $C$ est un ensemble ouvert de $Y$, son
complémentaire $B=Y \setminus C$ est un ensemble fermé. Comme $$
f^{-1}(C) = f^{-1}(Y \setminus B) = X \setminus f^{-1}(B),
$$\
son image réciproque est le complémentaire d'un fermé dans $X$ et donc
ouverte. La réciproque est établie de façon
similaire.`\hfill$\blacksquare$`{=latex}
:::
:::

::: {.section}
Exercices
=========

::: {.section}
Normes d'opérateurs
-------------------

[La fonction `norm` du module
`numpy.linalg`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.norm.html#numpy-linalg-norm)
peut calculer des normes de vecteurs de $\mathbb{R}^n$, mais également
de matrices carrées de $\mathbb{R}^{n\times n}$. Ainsi, on a par
exemple :

    >>> from numpy import inf
    >>> from numpy.linalg import norm
    >>> A = [[1.0, 2.0], [3.0, 4.0]]
    >>> norm(A)
    5.477225575051661
    >>> norm(A, 1)
    6.0
    >>> norm(A, 2)
    5.464985704219043
    >>> norm(A, inf)
    7.0

En étudiant [la documentation de cette
fonction]((https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.norm.html#numpy-linalg-norm)),
déterminer pour les quatres exemples d'usage ci-dessus s'il existe une
norme $\|\cdot\|_?$ de vecteurs de $\mathbb{R}^n$ dont la norme
d'opérateur associée correspond à cette norme de matrice, c'est-à-dire
telle que $$
\|A\| = \sup_{x \neq 0} \frac{\|A\cdot x\|_?}{\|x\|_?}.
$$

::: {.section}
#### Etude de `norm(A)` ($\mathord{\bullet}\mathord{\bullet}$) {#no .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Etude de \texttt{norm(A)}}`{=latex}

([Solution p.
`\pageref*{answer-no}`{=tex}](#answer-no){.no-parenthesis}.)
:::

::: {.section}
#### Etude de `norm(A, 1)` ($\mathord{\bullet}\mathord{\bullet}$) {#no-1 .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Etude de \texttt{norm(A,\ 1)}}`{=latex}

([Solution p.
`\pageref*{answer-no-1}`{=tex}](#answer-no-1){.no-parenthesis}.)
:::

::: {.section}
#### Etude de `norm(A, 2)` ($\mathord{\bullet}\mathord{\bullet}$) {#no-2 .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Etude de \texttt{norm(A,\ 2)}}`{=latex}

([Solution p.
`\pageref*{answer-no-2}`{=tex}](#answer-no-2){.no-parenthesis}.)
:::

::: {.section}
#### Etude de `norm(A, inf)` ($\mathord{\bullet}\mathord{\bullet}$) {#no-inf .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Etude de \texttt{norm(A,\ inf)}}`{=latex}

([Solution p.
`\pageref*{answer-no-inf}`{=tex}](#answer-no-inf){.no-parenthesis}.)
:::
:::

::: {.section}
Droite réelle achevée {#dra}
---------------------

La *droite réelle achevée* (ou *droite réelle étendue*) est composée des
nombres réels et de $-\infty$ et $+\infty$. Le but de cet exercice est
de doter cet ensemble $[-\infty, +\infty]$([^6]) d'une distance aux
propriétés "raisonnables". A cette fin, on introduit l'espace métrique
$X$ des points du cercle unité de $\mathbb{R}^2$ d'ordonnée positive :
$$
X = 
\left\{
(x, y) \in \mathbb{R}^2 \, \left| \, \sqrt{x^2+y^2} = 1 \right. \mbox{ et } y \geq 0
\right\},
$$ muni de la distance euclidienne de $\mathbb{R}^2$ puis la fonction
$f: X \to [-\infty, +\infty]$ définie par $$
f(x,y) = 
\left|
\begin{array}{rl}
- \infty & \mbox{si } (x, y)=(-1, 0), \\
x/y & \mbox{si } y > 0, \\
+ \infty & \mbox{si } (x, y)=(1, 0). \\
\end{array}
\right.
$$

::: {.section}
#### Question 1 ($\mathord{\bullet}$) {#dra-1 .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Pouvez-vous donner une interprétation géométrique simple à la grandeur
calculée par la fonction $f$ ?

![Construction d'une métrique pour la droite réelle
achevée.](images/extended-real-numbers.tex.pdf)

([Solution p.
`\pageref*{answer-dra-1}`{=tex}](#answer-dra-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 ($\mathord{\bullet}$) {#dra-2 .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Montrer que $f$ est une bijection. ([Solution p.
`\pageref*{answer-dra-2}`{=tex}](#answer-dra-2){.no-parenthesis}.)
:::

::: {.section}
#### Question 3 ($\mathord{\bullet}\mathord{\bullet}$) {#dra-3 .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

En déduire qu'il existe une et une seule fonction distance sur
$[-\infty, +\infty]$ qui fasse de $f$ une isométrie ; on note
$d^{\pm \infty}$ cette distance. ([Solution p.
`\pageref*{answer-dra-3}`{=tex}](#answer-dra-3){.no-parenthesis}.)
:::

::: {.section}
#### Question 4 ($\mathord{\bullet}$) {#dra-4 .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 4}`{=latex}

Calculer $d^{\pm \infty}(0, +\infty)$,
$d^{\pm \infty}(-\infty, +\infty)$, $d^{\pm \infty}(-1, 1)$. ([Solution
p. `\pageref*{answer-dra-4}`{=tex}](#answer-dra-4){.no-parenthesis}.)
:::

::: {.section}
#### Question 5 ($\mathord{\bullet}$) {#dra-5 .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 5}`{=latex}

Montrer que l'injection canonique
$x \in \mathbb{R} \mapsto x \in [-\infty, +\infty]$ est une fonction
continue. ([Solution p.
`\pageref*{answer-dra-5}`{=tex}](#answer-dra-5){.no-parenthesis}.)
:::

::: {.section}
#### Question 6 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#dra-6 .question .three .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 6}`{=latex}

Yoda a dit "deux façons d'interpréter $x_k \to +\infty$ désormais il y
a". Qu'est-ce qu'il a voulu dire ? Est-ce que c'est un problème ?
([Solution p.
`\pageref*{answer-dra-6}`{=tex}](#answer-dra-6){.no-parenthesis}.)
:::

::: {.section}
#### Question 7 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#dra-7 .question .four .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 7}`{=latex}

Suggérer une variante de la construction précédente pour doter
l'ensemble $\mathbb{R} \cup \{\infty\}$ ($\infty$ sans signe : ni $+$,
ni $-$) d'une métrique $d^{\infty}$ telle $|x_k| \to +\infty$ si et
seulement si $d^{\infty}(x_k, \infty) \to 0$. En déduire que cet
ensemble est compact. ([Solution p.
`\pageref*{answer-dra-7}`{=tex}](#answer-dra-7){.no-parenthesis}.)
:::
:::

::: {.section}
Localement fermé
----------------

::: {.section}
Dans un espace métrique[^7] $X$, un ensemble $A$ est *localement fermé*
si chaque point de $A$ a un voisinage ouvert $V$ tel que $A \cap V$ soit
fermé dans $V$ [@Sat59].
:::

::: {.section}
#### Question 0 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#lf-0 .question .three .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 0}`{=latex}

Expliquer l'expression "fermé dans $V$" dans la définition ci-dessus ;
est-ce que cela fait une différence si l'on remplace cette expression
par "fermé" ? ([Solution p.
`\pageref*{answer-lf-0}`{=tex}](#answer-lf-0){.no-parenthesis}.)
:::

::: {.section}
#### Question 1 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#lf-1 .question .three .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Montrer que dans $\mathbb{R}$, l'intervalle $\left[0, 1\right[$ est
localement fermé et que l'image de toute suite convergente est
localement fermée. Donner un exemple de sous-ensemble de $\mathbb{R}$
qui ne soit pas localement fermé. ([Solution p.
`\pageref*{answer-lf-1}`{=tex}](#answer-lf-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#lf-2 .question .three .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Montrer que tout ensemble fermé est localement fermé, mais aussi que
tout ensemble ouvert est localement fermé. Montrer que l'intersection de
deux ensembles localement fermés est localement fermé. ([Solution p.
`\pageref*{answer-lf-2}`{=tex}](#answer-lf-2){.no-parenthesis}.)
:::

::: {.section}
#### Question 3 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#lf-3 .question .four .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Montrer qu'un ensemble est localement fermé si et seulement s'il est
l'intersection d'un ensemble fermé et d'un ensemble ouvert. ([Solution
p. `\pageref*{answer-lf-3}`{=tex}](#answer-lf-3){.no-parenthesis}.)
:::
:::

::: {.section}
Distance entre ensembles
------------------------

Soit $A$ et $B$ deux ensembles fermés bornés non vides de
$\mathbb{R}^n$ ; on souhaite évaluer à quel point les deux ensembles $A$
et $B$ diffèrent -- en mesurant à quelle distance les points de $A$
peuvent être éloignés de l'ensemble $B$ et réciproquement.

::: {.section}
#### Question 1 ($\mathord{\bullet}$) {#dh-1 .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Est-ce que la distance entre ensembles classique $$
d(A, B) = \inf_{a \in A} d(a, B) = \inf_{a\in A}\inf_{b \in B} d(a, b)
$$ fait l'affaire ? ([Solution p.
`\pageref*{answer-dh-1}`{=tex}](#answer-dh-1){.no-parenthesis}.)
:::

::: {.section}
On définit la grandeur $$
  d[A, B] = \max \left\{ \sup_{a \in A} d(a, B), \, \sup_{b \in B} d(b, A) \right\}.
  $$ appelée *distance de Hausdorff* entre $A$ et $B$.
:::

::: {.section}
#### Question 2 ($\mathord{\bullet}\mathord{\bullet}$) {#dh-2 .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Calculer $d[A, B]$ lorsque $A = [-1,1] \times [-1, 1]$ et
$B = [0, 2] \times [0,2]$.

![Ensembles $A = [-1,1] \times [-1, 1]$ et
$B = [0, 2] \times [0,2]$.](images/hausdorff.tex.pdf){#A-et-B}

([Solution p.
`\pageref*{answer-dh-2}`{=tex}](#answer-dh-2){.no-parenthesis}.)
:::

::: {.section}
#### Question 3 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#dh-3 .question .three .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Cette terminologie de "distance" de Hausdorff est-elle légitime ?
([Solution p.
`\pageref*{answer-dh-3}`{=tex}](#answer-dh-3){.no-parenthesis}.)
:::

::: {.section}
#### Question 4 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#dh-4 .question .four .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 4}`{=latex}

La somme de Minkowksi de deux ensembles $A$ et $B$ est définie comme $$
A + B = \{a + b \, | \, a \in A, \, b \in B \}.
$$ Vérifier que la somme de Minkowski de deux ensembles fermés bornés
non vides de $\mathbb{R}^n$ est un ensemble fermé borné non vide de
$\mathbb{R}^n$. Cette opération est-elle continue pour la distance de
Hausdorff ? ([Solution p.
`\pageref*{answer-dh-4}`{=tex}](#answer-dh-4){.no-parenthesis}.)
:::
:::

::: {.section}
Plongement de Kuratowski
------------------------

Nous souhaitons établir le résultat suivant : tout espace métrique peut
être identifié à un sous-ensemble d'un espace vectoriel normé d'une
façon qui préserve la distance entre points.

Soit $X$ un espace métrique et $x_0$ un point de $X$. On associe à
l'élément $x$ de $X$ la fonction $f_x: X \to \mathbb{R}$ définie par $$
f_x(y) = d(x, y) - d(x_0, y).
$$

::: {.section}
#### Question 1 ($\mathord{\bullet}\mathord{\bullet}$) {#pk-1 .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Montrer que la fonction $x \mapsto f_x$ est injective. ([Solution p.
`\pageref*{answer-pk-1}`{=tex}](#answer-pk-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 ($\mathord{\bullet}\mathord{\bullet}$) {#pk-2 .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Montrer que pour tout point $x$ la fonction $f_x$ est bornée. ([Solution
p. `\pageref*{answer-pk-2}`{=tex}](#answer-pk-2){.no-parenthesis}.)
:::

::: {.section}
#### Question 3 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#pk-3 .question .three .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Montrer que $x \mapsto f_x$ est une isométrie de $X$ dans l'espace des
fonctions bornées de $X$ dans $\mathbb{R}$ muni de la norme
$\|\cdot\|_{\infty}$, c'est-à-dire que pour tout $x$ et $y$ dans $X$, on
a $$
d(x, y) = \|f_x - f_y\|_{\infty}.
$$

([Solution p.
`\pageref*{answer-pk-3}`{=tex}](#answer-pk-3){.no-parenthesis}.)
:::
:::

::: {.section}
Le nombre d'or {#golden-ratio}
--------------

Le but de cet exercice est de montrer l'existence d'un unique réel
positif $x$ tel que $x^2 = x + 1$ -- le *nombre d'or* -- et de produire
une méthode itérative pour l'évaluer.

::: {.section}
#### Question 1 ($\mathord{\bullet}$) {#golden-ratio-1 .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Montrer l'existence d'un unique point fixe associé à l'application $$
f:x \in \left]0, +\infty\right[ \mapsto 1 + \frac{1}{x}
$$ et établir qu'il se situe dans l'intervalle fermé $[4/3, 2]$.
([Solution p.
`\pageref*{answer-golden-ratio-1}`{=tex}](#answer-golden-ratio-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 ($\mathord{\bullet}\mathord{\bullet}$) {#golden-ratio-2 .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Montrer que la suite de réels définie par $x_0 \in [4/3, 2]$ et
$x_{n+1} = f(x_n)$ converge vers le nombre d'or. ([Solution p.
`\pageref*{answer-golden-ratio-2}`{=tex}](#answer-golden-ratio-2){.no-parenthesis}.)
:::

::: {.section}
#### Question 3 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#golden-ratio-3 .question .three .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Etudier la fonction $f \circ f$ et en exploitant le résultat de
l'exercice ["Point fixe" (p. `\pageref*{TPFB2}`{=tex})](#TPFB2), en
déduire que la suite des $x_n$ converge vers le nombre d'or pour toute
valeur initial $x_0$ strictement positive. ([Solution p.
`\pageref*{answer-golden-ratio-3}`{=tex}](#answer-golden-ratio-3){.no-parenthesis}.)
:::
:::

::: {.section}
Spirale d'Euler
---------------

La spirale d'Euler est la courbe paramétrée du plan déterminée pour
$t\geq 0$ par les coordonnées $$
x(t) = \int_0^t \cos s^2 \, ds \, \mbox{ et } \, \, y(t) = \int_0^t \sin s^2 \, ds
$$

![Spirale d'Euler ($0 \leq t \leq 5$)](images/euler.py.pdf)

Nous souhaitons établir que cette spirale à un point limite quand
$t \to +\infty$([^8]).

::: {.section}
#### Question 1 ($\mathord{\bullet}$) {#se-1 .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Montrer que si pour toute suite de valeurs $t_k$ tendant vers l'infini,
la suite de points de coordonnées $(x_k, y_k) := (x(t_k), y(t_k))$ a une
limite dans le plan -- limite qui peut dépendre a priori de la suite
$t_k$ -- alors le point de coordonnées $(x(t), y(t))$ a une limite dans
le plan quand $t$ tend vers $+\infty$. ([Solution p.
`\pageref*{answer-se-1}`{=tex}](#answer-se-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#se-2 .question .three .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Montrer que pour tout couple $(a,b)$ de réels tels que $0 < a \leq b$,
les grandeurs $$
I(a, b) :=
\int_{a}^{b} \cos s^2 \, ds
\mbox{ et }
J(a, b) := \int_{a}^{b} \sin s^2 \, ds
$$ vérifient les inégalités $$
|I(a, b)| \leq \frac{1}{a}
\, \mbox{ et } \,
|J(a, b)| \leq \frac{1}{a}.
$$

([Solution p.
`\pageref*{answer-se-2}`{=tex}](#answer-se-2){.no-parenthesis}.)
:::

::: {.section}
#### Question 3 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#se-3 .question .three .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Conclure. ([Solution p.
`\pageref*{answer-se-3}`{=tex}](#answer-se-3){.no-parenthesis}.)
:::
:::

::: {.section}
Point fixe {#TPFB2}
----------

On souhaite montrer que si $X$ est un espace métrique complet et qu'il
existe un entier $n \geq 1$ tel que la composée $n$ fois d'une
application $f: X \to X$ avec elle-même -- notée $f^n$ -- est
contractante, alors la conclusion du [théorème de point fixe de Banach
(p. `\pageref*{T-TPFB}`{=tex})](#T-TPFB) est toujours valable (bien que
les hypothèses considérées ici soient plus générales).

::: {.section}
#### Question 1 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#pf-1 .question .three .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Soit $X$ un ensemble et $f: X \to X$. Montrer que tout point fixe de $f$
est également un point fixe de $f^n$ ; montrer que si $f^n$ admet un
unique point fixe, il est également l'unique point fixe de $f$.
([Solution p.
`\pageref*{answer-pf-1}`{=tex}](#answer-pf-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#pf-2 .question .three .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

On suppose désormais que $X$ est un espace métrique complet et que $f^n$
est contractante. Montrer que $f$ admet un unique point fixe et que le
procédé habituel pour calculer ce point fixe comme une limite est
toujours valable. ([Solution p.
`\pageref*{answer-pf-2}`{=tex}](#answer-pf-2){.no-parenthesis}.)
:::
:::

::: {.section}
Résolution itérative de systèmes linéaires
------------------------------------------

Une matrice $A \in \mathbb{R}^{n\times n}$ est *diagonalement dominante*
si les coefficients $a_{ij}$ associés vérifient pour tout
$i \in \{1,\dots, n\}$, $$
\sum_{\substack{j=1\\j\neq i}}^n |a_{ij}| < |a_{ii}|.
$$ Soit $D$ la matrice diagonale issue de $A$ : $$
D = \left[
\begin{array}{cccc}
a_{11} & 0 & \cdots & 0 \\
0 & a_{22} & \cdots & 0 \\
\vdots & \vdots & \vdots & \vdots \\
0 & \cdots & 0 & a_{nn} \\
\end{array}
\right]
$$

::: {.section}
#### Question 1 ($\mathord{\bullet}$) {#risl-1 .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Montrer que deux vecteurs $x$ et $y$ de $\mathbb{R}^n$ vérifient
$A \cdot x = y$ si et seulement si
$$x = D^{-1} \cdot (D-A) \cdot x  + D^{-1} \cdot y.$$

([Solution p.
`\pageref*{answer-risl-1}`{=tex}](#answer-risl-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#risl-2 .question .three .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

En déduire que $A$ est inversible et une méthode itérative de calcul de
$A^{-1}$. ([Solution p.
`\pageref*{answer-risl-2}`{=tex}](#answer-risl-2){.no-parenthesis}.)
:::
:::

::: {.section}
Équation différentielle
-----------------------

Soit $A$ une matrice de $\mathbb{R}^{n\times n}$. On souhaite montrer
que pour tout $x_0 \in \mathbb{R}^n$, il existe une unique fonction
dérivable $x: \left[0, +\infty\right[ \to \mathbb{R}^n$ à l'équation
différentielle $$
\dot{x}(t) = A \cdot x(t) \mbox{ pour tout } t \geq 0,
$$ assortie de la condition initiale $x(0) = x_0$.

::: {.section}
#### Question 1 ($\mathord{\bullet}$) {#ed-1 .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Montrer que la fonction $x: \left[0, +\infty\right[ \to \mathbb{R}^n$
est solution du problème ci-dessus si et seulement si elle est continue
et vérifie pour tout $t \geq 0$ la relation $$
x(t) = x_0 + \int_0^t A \cdot x(s) \, ds.
$$

([Solution p.
`\pageref*{answer-ed-1}`{=tex}](#answer-ed-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#ed-2 .question .three .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Soit $T > 0$ ; on note $E$ l'espace des fonctions continues de $[0, T]$
dans $\mathbb{R}^n$, muni de la norme $$
\|x\|_{\infty} = \sup_{t \in [0, T]} \|x(t)\|.
$$ A quelle condition simple l'application $\Phi: E \to E$ définie par
$$
\Phi(x) = \left(t \mapsto x_0 +  \int_0^t A \cdot x(s) \, ds\right)
$$ est-elle contractante ? Quelle conclusion (partielle) quant au
problème initial peut-on en tirer ? ([Solution p.
`\pageref*{answer-ed-2}`{=tex}](#answer-ed-2){.no-parenthesis}.)
:::

::: {.section}
#### Question 3 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#ed-3 .question .three .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Soit $\alpha > 0$. On note $$
\|x\|_{\infty}^{\alpha} = \sup_{t \in [0, T]} \|e^{-\alpha t}x(t)\|.
$$ Montrer que $\|\cdot\|_{\infty}^{\alpha}$ est une norme sur l'espace
des fonctions continues de $[0, T]$ dans $\mathbb{R}^n$ et que muni de
cette norme, l'espace $E$ est complet. ([Solution p.
`\pageref*{answer-ed-3}`{=tex}](#answer-ed-3){.no-parenthesis}.)
:::

::: {.section}
#### Question 4 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#ed-4 .question .three .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 4}`{=latex}

Reprendre la question 2 avec la norme $\|\cdot\|_{\infty}^{\alpha}$ au
lieu de $\|\cdot\|_{\infty}$ et conclure quant à l'existence d'une
solution au problème initial. ([Solution p.
`\pageref*{answer-ed-4}`{=tex}](#answer-ed-4){.no-parenthesis}.)
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
#### Norme d'une matrice $2\times3$ {#answer-nm23 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Norme d'une matrice \(2\times3\)}`{=latex}

Pour tout vecteur non nul $x=(x_1,x_2,x_3) \in \mathbb{R}^3$, on a
$A\cdot x = (x_1, -x_2)$ et donc $$
\frac{\|A\cdot x\|}{\|x\|} = \frac{\sqrt{(x_1)^2 + (-x_2)^2}}{\sqrt{x_1^2 + x_2^2 + x_3^2}}
= \frac{\sqrt{x_1^2 + x_2^2}}{\sqrt{x_1^2 + x_2^2 + x_3^2}} \leq 1,
$$ soit $$
\|A\| = \sup_{x \neq 0} \frac{\|A \cdot x\|}{\|x\|} \leq 1.
$$ De plus, on a $A \cdot (1,0,0) = (1, 0)$, donc $$
\frac{\|A \cdot (1,0,0)\|}{\|(1,0,0)\|} = \frac{\|(1,0)\|}{\|(1,0,0)\|} = \frac{1}{1} = 1,
$$ donc $$
\|A\| = \sup_{x \neq 0} \frac{\|A \cdot x\|}{\|x\|} \geq 1.
$$ Par conséquent, $\|A\| = 1$.
:::

::: {.section}
#### Matrice de rotation {#answer-mdr .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Matrice de rotation}`{=latex}

Un rotation $A$ est une isométrie : pour tout $x \in \mathbb{R}^2$, on a
$\|A \cdot x\| = \|x\|$, donc $$
\|A\| = \sup_{x \neq 0} \frac{\|A \cdot x\|}{\|x\|} = 1.
$$
:::

::: {.section}
#### Norme d'une matrice $2 \times 2$ {#answer-nm22 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Norme d'une matrice \(2 \times 2\)}`{=latex}

Soit $x=(x_1, x_2)$ un vecteur non-nul de $\mathbb{R}^2$. On a
$A \cdot x = (2x_1, -x_2)$, donc $$
\frac{\|A \cdot x\|}{\|x\|} = \frac{\sqrt{4x_1^2 +  x_2^2}}{\sqrt{x_1^2 + x_2^2}}.
$$ En formant $r = (x_1 / x_2)^2$, on obtient donc $$
\|A\| = \sup_{(x_1,x_2) \neq 0} \frac{\sqrt{4x_1^2 +  x_2^2}}{\sqrt{x_1^2 + x_2^2}}= \sup_{r \in [0, +\infty]} \frac{\sqrt{r + 4}}{\sqrt{r + 1}}
=
\sup_{r \in [0, +\infty]} \sqrt{1 + \frac{{3}}{{r + 1}}}.
$$ La fonction $r \in [0, +\infty] \mapsto \sqrt{1 + 3/(r+1)}$ étant
décroissante, son supremum est sa valeur $0$, soit $$
\|A\| = \sup_{r \in [0, +\infty]} \sqrt{1 + \frac{{3}}{{r + 1}}}.
= \sqrt{1 + \frac{{3}}{{0 + 1}}} = \sqrt{4} = 2.
$$
:::

::: {.section}
#### Sous-multiplicativité de la norme d'opérateur {#answer-sous-multip .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Sous-multiplicativité de la norme d'opérateur}`{=latex}

On a pour tout $x\in \mathbb{R}^p$ $$
\|(A \cdot B) \cdot x\| = \|A \cdot (B \cdot x)\|
\leq \|A\| \|B \cdot x\| \leq \|A\| \|B\| \|x\|.
$$ Par conséquent, $$
\|A \cdot B\| = \sup_{x \neq 0} \frac{\|(A \cdot B)\cdot x\|}{\|x\|} \leq \|A\|\|B\|.
$$
:::

::: {.section}
#### Intervalles de $\mathbb{R}$ {#answer-ir .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Intervalles de \(\mathbb{R}\)}`{=latex}

Posons $I := \left[0,1 \right[$. Des calculs élémentaires établissent
que $$
d(x, I) = 
\left|
\begin{array}{rl}
-x & \mbox{si } x \leq 0, \\
0  & \mbox{si } 0 \leq x \leq 1, \\
x-1 & \mbox{si } 1 \leq x.
\end{array}
\right.
\; \mbox{ et } \;
d(x, I^c) = 
\left|
\begin{array}{rl}
0 & \mbox{si } x \leq 0, \\
x  & \mbox{si } 0 \leq x \leq 1/2, \\
1 - x & \mbox{si } 1/2 \leq x \leq 1, \\
0 & \mbox{si } 1 \leq x
\end{array}
\right.
$$

Par conséquent, $d(x, I) = 0$ si et seulement si $x \in [0, 1]$, donc
$\overline{I} = [0,1]$. On a $d(x, I)= d(x, I^c)=0$ si et seulement si
$x=0$ ou $x=1$ donc $\partial A = \{0,1\}$. Finalement, $d(x, I^c) > 0$
si et seulement si $0 < x <1$, donc $I^{\circ} = \left]0, 1\right[$.
:::

::: {.section}
#### Ensemble des rationnels {#answer-Q .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Ensemble des rationnels}`{=latex}

Tout nombre réel $x$ peut être approché par un rationnel avec une
précision arbitraire : si $\lfloor\cdot \rfloor$ désigne la fonction
partie entière, on a par exemple $$
\left|\frac{\lfloor 10^n x \rfloor}{10^n} - x \right| < 10^{-n}.
$$ Par conséquent, pour tout $x \in \mathbb{R}$, $d(x, \mathbb{Q}) = 0$
et donc $\overline{\mathbb{Q}} = \mathbb{R}$.
:::

::: {.section}
#### Inclusions {#answer-exo-i .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Inclusions}`{=latex}

Si $d(x, A^c) > 0$, alors $x \not \in A^c$, donc $x \in A$ ; donc
$A^{\circ} \subset A$. Si $x \in A$ alors $d(x, A) \leq d(x, x) = 0$,
donc $x$ est adhérent à $A$ ; soit $A \subset \overline{A}$.
:::

::: {.section}
#### Topologie basée sur l'adhérence {#answer-tba .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Topologie basée sur l'adhérence}`{=latex}

La relation $\partial A = \overline{A} \cap \overline{A^c}$ résulte
directement de la définition d'adhérence et de frontière. Pour ce qui
est de l'intérieur, on peut noter que
$\overline{A^c} = \{x \in X \; | \; d(x, A^c) = 0\}$ et donc $$
\left(\overline{A^c}\right)^c
= \{x \in X \; | \; d(x, A^c) \neq 0\}
= \{x \in X \; | \; d(x, A^c) > 0\} = A^{\circ}.
$$
:::

::: {.section}
#### Adhérence itérée {#answer-ai .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Adhérence itérée}`{=latex}

De l'inclusion $A \subset \overline{A}$ on déduit que
$\overline{A} \subset \overline{\overline{A}}$. Réciproquement, pour
tout $\varepsilon >0$, si $x \in \overline{\overline{A}}$, il existe un
$y \in \overline{A}$ tel que $d(x, y) \leq \varepsilon /2$ et de même un
$z \in A$ tel que $d(y, z) \leq \varepsilon/2$. Par [l'inégalité
triangulaire (p. `\pageref*{dist-ineg}`{=tex})](#dist-ineg), on a donc
$$
d(x, A) \leq d(x, z) \leq d(x, y)  + d(y, z) \leq \varepsilon.
$$ Le réel positif $\varepsilon$ étant arbitraire, on a $d(x, A) = 0$,
soit $x \in \overline{A}$.
:::

::: {.section}
#### Décomposition de $\overline{A}$ {#answer-pab .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Décomposition de \(\overline{A}\)}`{=latex}

Aucun point $x$ ne peut vérifier simultanément $d(x,A^c)> 0$ et
$d(x, A^c)=0$, donc $A^{\circ} \cap \partial A = \varnothing$. Ensuite,
il est clair d'après la définition de la frontière que
$\partial A \subset \overline{A}$ ; comme tout point $x$ de $A^{\circ}$
vérifie $d(x, A^c)> 0$, on a $x \not \in A^c$, soit $x \in A$ et donc
$d(x, A)=0$, soit $x\in\overline{A}$ ; donc
$A^{\circ} \cup \partial A \subset \overline{A}$. Finalement, si
$x \in \overline{A}$, soit $d(x, A^c) > 0$, auquel cas
$x \in A^{\circ}$, soit $d(x, A^c)=0$, auquel cas $d(x, A)= 0$ et
$d(x, A^c)=0$, c'est-à-dire $x\in\partial A$. On a donc bien
$\overline{A} = A^{\circ} \cup \partial A$.
:::

::: {.section}
#### Topologie basée sur la frontière {#answer-tbf .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Topologie basée sur la frontière}`{=latex}

Il est clair d'après les définitions que $A \subset \overline{A}$ et que
$\partial A \subset \overline{A}$ ; de plus si $x \in \overline{A}$,
soit $x \in A$, soit $x \in A^c$ ; dans le premier cas $x \in A$, dans
le second cas $d(x,A^c)=0$, donc $x \in \partial A$. On a donc bien
$\overline{A} = A \cup \partial A$.

Les points $x \in A^{\circ}$ vérifient $d(x, A^c) > 0$ et donc
$x \not \in A^c$, soit $x \in A$, donc $A^{\circ} \subset A$. De plus,
un point frontière $x$ -- qui vérifie $d(x, A^c) = 0$ -- ne peut
appartenir à l'intérieur de $A$. Par conséquent,
$A^{\circ} \subset A \setminus \partial A$. Réciproquement, un point de
$A$ qui n'appartient pas à $\partial A$ vérifie $d(x, A) > 0$ -- ce qui
est impossible -- ou $d(x, A^c) > 0$, donc appartient à $A^{\circ}$. Par
conséquent, $A \setminus \partial A \subset A^{\circ}$. On a donc bien
$A^{\circ} = A \setminus \partial A$.
:::

::: {.section}
#### Ouvert $\Leftrightarrow$ non fermé ? {#answer-onf .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Ouvert \(\Leftrightarrow\) non fermé ?}`{=latex}

Non ! De nombreux ensembles qui ne sont ni ouverts ni fermés. Par
exemple dans $\mathbb{R}$, l'intervalle $I = \left[0, 1\right[$ n'est ni
ouvert (car que $I^{\circ} = \left]0,1 \right[ \neq I$) ni fermé (car
$\overline{I} = [0,1] \neq I$).
:::

::: {.section}
#### L'adhérence est fermée, l'intérieur est ouvert {#answer-adio .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{L'adhérence est fermée, l'intérieur est ouvert}`{=latex}

L'adhérence $\overline{A}$ d'un ensemble $A$ vérifie
$\overline{\overline{A}} = \overline{A}$, elle est donc fermée. De façon
similaire on a $(A^{\circ})^{\circ} = A^{\circ}$ et l'intérieur de $A$
est ouvert.
:::

::: {.section}
#### Ensemble discret {#answer-ed .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Ensemble discret}`{=latex}

Non. Un contre-exemple est l'ensemble
$A = \{2^{-n} \; | \; n \in \mathbb{N}\}$. Il est bien discret : on a
$d(2^{-n}, A \setminus \{n\}) = 2^{-n-1} > 0$. Mais $x=0$ est à distance
nulle de $A$ et n'appartient pas à $A$. L'ensemble $A$ n'est donc pas
fermé.
:::

::: {.section}
#### Normes et boules {#answer-bdn .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Normes et boules}`{=latex}

Pour toute norme $\|\cdot\|$, on a $$
B((0,0),1) = \{x \in \mathbb{R}^2 \; | \; \|x\| < 1\},
$$ d'où les représentations graphiques associées aux différentes normes.

![Boules ouvertes unitaires associées à $\|\cdot\|_2$,$\|\cdot\|_1$,
$\|\cdot\|_{\infty}$](images/normes-boules.svg.pdf)
:::

::: {.section}
#### C'est une boule ça ? {#answer-cubc .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{C'est une boule ça ?}`{=latex}

Dans $X$, la boule centrée en $(0,0)$ et de rayon $1$ est constituée des
points de $x \in X$ tels que $d((0,0), x) < 1$. Comme tous les points
$x$ de $\mathbb{R}^2$ vérifiant cette inégalité satisfont $|x_1| \leq 1$
et $|x_2| \leq 1$, on a donc $$
B((0,0), 1) = \left\{(x_1,x_2) \in \mathbb{R}^2 \; \left| \; \sqrt{x_1^2 + x_2^2} < 1 \right. \right\}.
$$ Pour la boule de même rayon centrée en $(1, 0)$, on peut se
convaincre que tous les points de $\mathbb{R}^2$ tels que
$d((1,0), x) < 1$ satisfont $x_1 \geq -1$ et $|x_2| \leq 1$, mais pas
nécessairement $x_1 \leq 1$. On a donc $$
B((1,0), 1) = \left\{(x_1,x_2) \in \mathbb{R}^2 \; \left| \; x_1 < 1 \mbox{ et } \sqrt{(x_1-1)^2 + x_2^2} < 1 \right. \right\}.
$$ Concernant la boule ouverte $B((0,0), 2)$, si $x \in X$, alors la
condition $d((0,0), x) < 2$ est automatiquement satisfaite, car $$
\sqrt{x_1^2 + x_2^2} \leq \sqrt{1^2 + 1^2} = \sqrt{2} < 2.
$$ Par conséquent, $B((0,0), 2) = X$.

![Boules ouvertes dans le carré
$\{(x_1, x_2) \in \mathbb{R}^2 \; | \; |x_1| \leq 1 \mbox{ et } |x_2| \leq 1\}$](images/boules.svg.pdf)
:::

::: {.section}
#### Dans le plan {#answer-dlp .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Dans le plan}`{=latex}

Non, car tous les points de la forme $(0,x_2)$, $x_2 \neq 0$
n'appartiennent pas à $D$. Donc toute boule ouverte $B((0,0), r)$ est
d'intersection non vide avec le complémentaire de $D$.
:::

::: {.section}
#### Voisinages ouverts / fermés ? {#answer-vof .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Voisinages ouverts / fermés ?}`{=latex}

Si $V$ est un voisinage de $x$, il contient une boule ouverte non vide
$B(x, r)$, qui est ouverte et un voisinage de $x$, car
$d(x, B(x, r)^c) = r>0$ ce qui répond à la première partie de la
question. La boule fermée $\overline{B}(x, r/2)$ est également un
voisinage de $x$ (car $d(x, \overline{B}(x,r)^c) =r/2 > 0$) et de plus
$\overline{B}(x, r/2) \subset B(x, r) \subset V$.
:::

::: {.section}
#### Fonction localement bornée {#answer-flb .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Fonction localement bornée}`{=latex}

La fonction $x \in \mathbb{R}\mapsto x \in \mathbb{R}$ est continue mais
pas bornée par exemple. Mais si $f: \mathbb{R}\to \mathbb{R}$ est
continue, pour tout $x \in \mathbb{R}$, par continuité de $f$ en $x$, il
existe un $\varepsilon > 0$ tel que $$
y \in \left]x-\varepsilon, x+\varepsilon\right[ \implies |f(y) - f(x)| \leq 1.
$$ Par conséquent, sur l'intervalle ouvert
$\left]x-\varepsilon, x+\varepsilon\right[$ qui est un voisinage de $x$,
la fonction $f$ est bornée par $|f(x)|+1$. Elle est donc localement
bornée.
:::

::: {.section}
#### Courbes de niveau {#answer-cn .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Courbes de niveau}`{=latex}

L'ensemble $\{x \in \mathbb{R}^2 \; | \; f(x) = c\}$ est [l'image
réciproque du singleton $\{c\}$, un ensemble fermé de $\mathbb{R}$, par
la fonction continue $f$ (p. `\pageref*{CIR}`{=tex})](#CIR), il est donc
fermé.
:::

::: {.section}
#### Boules ouvertes et fermées {#answer-bof2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Boules ouvertes et fermées}`{=latex}

On a $B(x, r) = \{y \in X \; | \; d(x, y) < r\}$ ; L'ensemble
$I = \left[0, r\right[$ est ouvert dans l'espace métrique
$\left[0, +\infty\right[$ car
$d(x, I^c) = d(x, \left[r, +\infty\right[) = r-x > 0$ quand
$x \in \left[0, r \right[$. La boule ouverte en question est donc
l'image réciproque par l'application [continue (p.
`\pageref*{distance-continue}`{=tex})](#distance-continue)
$d(x, \cdot) = d(\cdot, x)$ d'un ouvert. Elle est donc ouverte par [le
critère de l'image réciproque (p. `\pageref*{CIR}`{=tex})](#CIR). La
preuve que toute "boule fermée" est fermée est similaire.
:::
:::

::: {.section}
Normes d'opérateurs
-------------------

::: {.section}
#### Etude de `norm(A)` {#answer-no .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Etude de \texttt{norm(A)}}`{=latex}

En l'absence de second argument, la fonction `norm` calcule la norme de
Frobenius de l'opérateur $A$, donnée comme $$
\|A\|_F = \sqrt{\sum_{i=1}^n\sum_{j=1}^n a_{ij}^2}.
$$ Il s'agit bien d'une norme sur matrices de $\mathbb{R}^{n\times n}$,
car on peut la calculer comme la norme euclidienne du vecteur de
$\mathbb{R}^{n^2}$ obtenu par "mise à plat" de la matrice $A$,
c'est-à-dire après avoir opéré la transformation (linéaire et bijective)
$$
\left[
  \begin{array}{ccc}
  a_{11} & \cdots & a_{1n} \\
  \vdots & \vdots & \vdots \\
  a_{n1} & \cdots & a_{nn}
  \end{array}
\right] \in \mathbb{R}^{n\times n}
\mapsto \left[
    \begin{array}{c}
  a_{11} \\ 
  \vdots \\ 
  a_{1n} \\
  \vdots \\
  a_{n1} \\ 
  \vdots \\
  a_{nn} \\
  \end{array}
  \right] \in \mathbb{R}^{n^2}.
$$ Mais elle n'est induite par aucune norme de vecteur ; en effet, s'il
existait une norme $\|\cdot\|_?$ telle que
$\|A\|_F = \sup \|A \cdot x\|_? / \|x\|_?$, alors on aurait en
particulier $$
\|I\|_F  = \sup_{x \neq 0} \frac{\|I \cdot x\|_?}{\|x\|_?} = 
\sup_{x \neq 0} \frac{\|x\|_?}{\|x\|_?}  = 1.
$$ Or, on peut constater que la norme de Frobenius de la matrice
associée à la matrice identité dans $\mathbb{R}^{n\times n}$ est
$\sqrt{n}$, qui diffère de $1$ si $n>1$.
:::

::: {.section}
#### Etude de `norm(A, 1)` {#answer-no-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Etude de \texttt{norm(A,\ 1)}}`{=latex}

L'expression `norm(A, 1)` calcule d'après la documentation de `norm` la
grandeur $$
\|A\|_1 = \max_{j = 1 \dots n} \left(\sum_{i=1}^n |a_{ij}|\right).
$$ Le fait que le second argument de l'appel à `norm` soit $1$ peut
laisser penser que cette norme de matrice est induite par la norme de
vecteurs $$
\|x\|_1 = \sum_{i=1}^n |x_i|.
$$ Vérifions cela ; si $y= A \cdot x$, on a $$
\begin{split}
\|y\|_1 =
\sum_{i=1}^n |y_i| = \sum_{i=1}^n \left|\sum_{j=1}^n a_{ij} x_j \right|
&\leq \sum_{i=1}^n \sum_{j=1}^n |a_{ij}||x_j|
=\sum_{j=1}^n \left(\sum_{i=1}^n |a_{ij}|\right)|x_j| \\
&\leq 
\max_{j=1\dots n} \left(\sum_{i=1}^n |a_{ij}|\right) \sum_{j=1}^n |x_j| \\
&=
\|A\|_1 \|x\|_1.
\end{split}
$$ Pour conclure, il nous suffit désormais d'exhiber un
$x \in \mathbb{R}^n$ tel que $\|A \cdot x\| = \|A\|_1 \|x\|_1$. Si le
maximum de $\sum_{i=1}^n |a_{ij}|$ est réalisé en $j$, il nous suffit de
considérer le $j$-ème vecteur de la base canonique de $\mathbb{R}^n$,
$x = e_j$. En effet, on a alors $\|e_j\|_1 = 1$ et $$
\|A \cdot e_j\|_1 = \left\| (a_{1j}, \dots, a_{nj})\right\|_1
= \sum_{i=1}^n |a_{ij}| = \|A\|_1.
$$
:::

::: {.section}
#### Etude de `norm(A, 2)` {#answer-no-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Etude de \texttt{norm(A,\ 2)}}`{=latex}

La norme en question est définie par NumPy comme $\sigma_1$, la plus
grande valeur singulière de $A$. Les valeurs singulières
$\sigma_1 \geq \sigma_2 \geq \sigma_n \geq 0$ associées à la matrice
$A\in\mathbb{R}^{n\times n}$ sont définies à travers une décomposition
de $A$ de la forme $$
A = U \cdot \Sigma \cdot V^{\top}
$$ où
$\Sigma \cdot (x_1, \dots, x_n) = (\sigma_1 x_1, \dots, \sigma_n x_n)$
et $U \in \mathbb{R}^{n\times n}$ et $V \in \mathbb{R}^{n\times n}$ sont
matrices orthogonales (inversibles et dont l'inverse est la transposée).
Pour montrer que $\sigma_1(\cdot)$ constitue la norme d'opérateur
$\|\cdot\|_{22}$ induite par la norme euclidienne $\|\cdot\|_2$ des
vecteurs de $\mathbb{R}^n$, on constate au préalable que pour toute
application orthogonale $U$, $$
\|U \cdot x\| = \sqrt{\left< U \cdot x, U \cdot x \right>}
= \sqrt{\left<U^{\top} \cdot U \cdot x, x \right>}
= \sqrt{\left<x, x\right>} = \|x\|_2,
$$ puis que $$
\begin{split}
\|A\|_{22} &= \sup_{\|x\|_2 \leq 1} \|(U \cdot \Sigma \cdot V^{\top}) \cdot x\|_2  \\
&= \sup_{\|x\|_2 \leq 1} \|U \cdot (\Sigma \cdot (V^{\top} \cdot x))\|_2 \\
&= \sup_{\|y\|_2 \leq 1} \|\Sigma \cdot y\|_2 \\
&= \sup_{\|y\|_2 \leq 1} \sqrt{\sigma_1^2 y_1^2 + \dots + \sigma_n^2 y_{n}^2} \\
&= \sigma_1.
\end{split}
$$
:::

::: {.section}
#### Etude de `norm(A, inf)` {#answer-no-inf .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Etude de \texttt{norm(A,\ inf)}}`{=latex}

On constate que l'expression donnée dans la documentation de `norm`, à
savoir $$
\|A\|_{\infty} = \max_{i = 1 \dots n} \left(\sum_{j=1}^n |a_{ij}|\right)
$$ entretient une troublante ressemblance avec la norme $\|\cdot\|_1$
pour les opérateurs. Plus précisément, si
$A^{\top} \in \mathbb{R}^{n\times n}$ désigne l'opérateur adjoint de
$A$, alors on a $$
\|A\|_{\infty} = \|A^{\top}\|_1.
$$ C'est un peu trop gros pour être une coincidence ... Pour montrer que
$\|\cdot\|_{\infty}$ est la norme d'opérateur $\|\cdot\|_{\infty\infty}$
associée à la norme de vecteurs $\|\cdot\|_{\infty}$, on peut d'abord
constater que pour les vecteurs, $$
\|x\|_{\infty} = \sup_{\|y\|_1 \leq 1} \left<y, x\right>
\; \mbox{ et } \;
\|x\|_{1} = \sup_{\|y\|_{\infty} \leq 1} \left<y, x\right>
$$ puis en déduire que $$
\begin{split}
\|A\|_{\infty\infty} = \sup_{\|x\|_{\infty} \leq 1} \|A \cdot x\|_{\infty}
&=\sup_{\|x\|_{\infty} \leq 1} \sup_{\|y\|_1 \leq 1} \left<y, A \cdot x\right> \\
&=
\sup_{\|x\|_{\infty} \leq 1} \sup_{\|y\|_1 \leq 1} \left<A^{\top} \cdot y, x\right> \\
&=
\sup_{\|y\|_1 \leq 1} \sup_{\|x\|_{\infty} \leq 1} \left<x, A^{\top} \cdot y \right> \\
&=
\sup_{\|y\|_1 \leq 1} \|A^{\top} \cdot y \| \\
&=\|A^{\top}\|_1 \\ &= \|A\|_{\infty},
\end{split}
$$ et donc $\|\cdot\|_{\infty\infty} = \|\cdot\|_{\infty}$.
:::
:::

::: {.section}
Droite réelle achevée {#droite-réelle-achevée}
---------------------

::: {.section}
#### Question 1 {#answer-dra-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Quand l'ordonnée $y$ du point $p=(x,y)$ est strictement positive, $f(p)$
représente l'abscisse de l'unique point $q$ de l'intersection de la
demi-droite $D$ issue de l'origine $(0,0)$ et passant par $p$ avec la
droite horizontale des points d'ordonnée $y=1$.

En effet, les points de $D$ sont de la forme $(\lambda x, \lambda y)$
pour $\lambda \geq 0$. On a donc $\lambda y = 1$ si et seulement si
$\lambda = 1/y$, auquel cas $\lambda x = x / y$.

Dans les cas limites où $p = (1,0)$ et $p=(-1,0)$, la demi-droite $D$
est horizontale, partant vers la droite de l'origine ou vers sa gauche
selon le cas. Il n'y a donc pas d'intersection avec la droite
horizontale d'équation $y=1$ dans $\mathbb{R}^2$, mais des intersections
"à l'infini".
:::

::: {.section}
#### Question 2 {#answer-dra-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

La fonction $f$ peut être décomposée comme $f = \psi \circ \phi$ où
l'application $\phi: (x, y) \in X \to x \in [-1, 1]$ est bijective,
d'inverse $\phi^{-1}(x) = (x, \sqrt{1 - x^2})$ et l'application
$\psi: [-1, 1] \to [-\infty, +\infty]$ définie par $$
\psi(x) = 
\left|
\begin{array}{cl}
- \infty & \mbox{si } x=-1, \\
\displaystyle \frac{x}{\sqrt{1-x^2}} & \mbox{si } -1 < x < 1, \\
+ \infty & \mbox{si } x=1. \\
\end{array}
\right.
$$ est également bijective, d'inverse $$
\psi^{-1}(x) = 
\left|
\begin{array}{cl}
- 1 & \mbox{si } x=-\infty, \\
\displaystyle \frac{y}{\sqrt{1+y^2}} & \mbox{si } -\infty < x < +\infty, \\
+ 1 & \mbox{si } x=+\infty. \\
\end{array}
\right.
$$ La fonction $f$ est donc bijective comme composée de fonctions
bijectives.
:::

::: {.section}
#### Question 3 {#answer-dra-3 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

La fonction $f$ sera une isométrie quand $[-\infty, +\infty]$ est muni
de la distance $d^{\pm \infty}$ -- et $X$ la distance induite par la
distance euclidienne de $\mathbb{R}^2$ -- si et seulement si pour toute
paire de points $p_1$ et $p_2$ dans $X$ $$
d^{\pm \infty}(f(p_1), f(p_2)) = d(p_1, p_2),
$$ ce qui rend nécessaire le choix de $$
d^{\pm \infty}(x_1, x_2) := d(f^{-1}(x_1), f^{-1}(x_2)).
$$ On vérifiera facilement que ce choix détermine bien une distance sur
la droite réelle achevée.
:::

::: {.section}
#### Question 4 {#answer-dra-4 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 4}`{=latex}

On a $f^{-1}(-\infty) = (-1,0)$,
$f^{-1}(-1) = (-\sqrt{2}/2, \sqrt{2}/2)$, $f^{-1}(0) = (0, 1)$,
$f^{-1}(1) = (\sqrt{2}/2, \sqrt{2}/2)$ et $f^{-1}(\infty) = (1,0)$, donc
$d^{\pm \infty}(0, +\infty) = d((0,1), (1,0)) = \sqrt{2},$
$d^{\pm \infty}(-\infty, +\infty) = d((-1, 0), (1, 0)) = 2$ et
$d^{\pm \infty}(-1, 1) = \sqrt{2}.$
:::

::: {.section}
#### Question 5 {#answer-dra-5 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 5}`{=latex}

Soit $i: x \in \mathbb{R}\to x \in [-\infty, +\infty]$. Pour montrer que
$i$ est continue, il nous faut prouver que pour tout
$x_1 \in \mathbb{R}$, quand $d(x_2, x_1) \to 0$, alors
$d^{\pm \infty}(i(x_2), i(x_1)) = d^{\pm \infty}(x_2, x_1)\to 0$. Or, $$
\begin{split}
d^{\pm \infty}(x_2, x_1)
&= d \left(\left(\frac{x_1}{\sqrt{1 + x_1^2}}, \frac{1}{\sqrt{1 + x_1^2}} \right), 
\left(\frac{x_2}{\sqrt{1 + x_2^2}}, \frac{1}{\sqrt{1 + x_2^2}} \right)\right) \\
&= 
\sqrt{\left(\frac{x_1}{\sqrt{1 + x_1^2}} - \frac{x_2}{\sqrt{1 + x_2^2}}\right)^2 
+ 
\left(\frac{1}{\sqrt{1 + x_1^2}} -  \frac{1}{\sqrt{1 + x_2^2}}\right)^2},
\end{split}
$$ et cette expression est une fonction continue de ses arguments $x_1$
et $x_2$, nulle quand $x_1 = x_2$ ; cette propriété est donc bien
vérifiée.
:::

::: {.section}
#### Question 6 {#answer-dra-6 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 6}`{=latex}

Quand $x_k$ est une suite de réels, $x_k \to +\infty$ est à interpréter
classiquement comme : pour tout $M \in \mathbb{R}$, il existe un rang
$m \in \mathbb{N}$ tel que si $k \geq m$, alors $x_k \geq M$.

Mais il existe maintenant une seconde interprétation si l'on considère
$x_k \in \mathbb{R}$ comme une suite de points dans l'espace métrique
$[-\infty, +\infty]$. Cela signifie alors que
$d^{\pm \infty}(x_k, +\infty) \to 0$ quand $k \to +\infty$. Or, comme $$
\begin{split}
\left(d^{\pm \infty}(x_k, +\infty) \right)^2
&= \left(\frac{x_k}{\sqrt{1+x_k^2}} - 1\right)^2 + \frac{1}{1+x_k^2} \\
&= \left(\mathrm{sign}(x_k)\sqrt{\frac{x_k^2}{1+x_k^2}} - 1\right)^2 + \frac{1}{1+x_k^2},
\end{split}
$$ ces deux conditions sont équivalentes.
:::

::: {.section}
#### Question 7 {#answer-dra-7 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 7}`{=latex}

On admettra sans preuve (la démarche est très similaire à celle menée
dans les questions précédentes) que la construction graphique ci-dessous

![Construction du compactifié de
$\mathbb{R}$.](images/extended-real-numbers-2.tex.pdf)

permet de doter $\mathbb{R}\cup \{\infty\}$ d'une métrique telle que
$|x_k| \to +\infty$ si et seulement si $d^{\infty}(x_k,\infty) \to 0$ et
que l'injection canonique associée est continue. On constate
graphiquement que dans cette variante, quand le point de la droite
d'ordonnée $y=2$ s'éloigne vers l'infini vers la droite ou vers la
gauche, le point correspondant du cercle centré en $(0,1)$ et de rayon
$1$ converge vers l'origine $(0,0)$.

Si l'on considère une suite de points
$x_k \in \mathbb{R}\cup\{\infty\}$, soit il existe une suite de points
réels bornée que l'on peut extraire de $x_k$ -- auquel cas par compacité
des fermés bornés dans $\mathbb{R}$ il existe une sous-suite extraite
des $x_k$ convergeant dans $\mathbb{R}$ (et donc dans
$\mathbb{R}\cup\{\infty\}$) -- soit $|x_k| \to +\infty$ quand
$k\to +\infty$ -- auquel cas $x_k \to \infty$ dans
$\mathbb{R}\cup\{\infty\}$. Dans les deux cas, la suite admet une suite
extraite convergente, l'espace est donc compact.
:::
:::

::: {.section}
Localement fermé
----------------

::: {.section}
#### Question 0 {#answer-lf-0 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 0}`{=latex}

Un sous-ensemble $B$ d'un ensemble $A$ de points d'un espace topologique
$X$ est "fermé dans $A$" s'il est fermé **comme ensemble de points de
l'espace topologique $A$**, muni de la topologie (ou le cas échéant la
métrique) induite par $X$. Et cette propriété peut être différente de
être "fermé" (sous-entendu comme ensemble de points de $X$).

Par exemple, si $X = \mathbb{R}$, $A = \left]0, +\infty\right[$ et
$B = \left]0, +\infty\right[$, $B$ n'est pas fermé dans $\mathbb{R}$,
car la suite $x_k = 2^{-k}$ appartient à $B$, mais
$x_k \to 0 \not \in B$ quand $k \to +\infty$. Par contre, toute suite de
$B$ convergeant dans $A$ converge dans $B$ car les deux ensembles sont
identiques. Par conséquent, $B$ est fermé dans $A$.
:::

::: {.section}
#### Question 1 {#answer-lf-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Soit $x \in A:=\left[0, 1\right[$ ; si $x>0$, on peut prendre
$V=\left]x/2, 1\right[$. C'est bien un voisinage ouvert de $x$ et
$A\cap V = V$. L'ensemble $A \cap V$ est donc fermé dans $V$. Si $x=0$,
on peut prendre $V = \left]-1, 1/2\right[$ ; c'est un voisinage ouvert
de $x$ et $A \cap V = \left[0, 1/2\right[$ est bien fermé dans $V$.

Soit $x_k$ une suite de $\mathbb{R}$ qui converge vers $\ell$ et
$A = \{x_k \, | \, k \in \mathbb{N}\}$. Si $a \in A$ et que
$a \neq \ell$, alors il existe un $\varepsilon > 0$ tel que
$V = ]a - \varepsilon, a + \varepsilon[$ vérifie $A \cap V = \{a\}$. $V$
est un voisinage ouvert de $a$ et $A \cap V$ est bien fermé dans $V$. Si
la valeur limite $\ell$ n'est pas atteinte par un $x_k$, cela conclut la
preuve que $A$ est localement fermé. Dans le cas contraire, pour
$a=\ell$, on peut prendre $V = \mathbb{R}$ ; en effet, $A$ est alors
fermé.

L'ensemble des rationnels $\mathbb{Q}$ n'est pas localement fermé. En
effet si $V$ est un voisinage de $0$ il contient nécessairement un
ensemble de la forme $\left]-\varepsilon, \varepsilon\right[$ pour un
$\varepsilon > 0$. Or cet intervalle contient des irrationnels, qui
peuvent être obtenus comme limite de rationnels dans
$\left]-\varepsilon, \varepsilon\right[$ et donc de $V$. Par conséquent,
$\mathbb{Q} \cap V$ ne peut pas être fermé dans $V$, donc $\mathbb{Q}$
n'est pas localement fermé.
:::

::: {.section}
#### Question 2 {#answer-lf-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Si $A$ est fermé, on peut prendre $V=X$ qui est un voisinage ouvert de
tout point de $A$. On a alors $A \cap V = A$ et donc $A \cap V$ est bien
fermé dans $V=X$.

Si $A$ est ouvert, on peut prendre $V=A$ qui est un voisinage ouvert de
tout point de $A$. On a alors $A \cap V = A$ et donc $A \cap V$ est bien
fermé dans $V=A$.

Si $A$ et $B$ sont localement fermés et $x \in A \cap B$, il existe des
voisinages ouverts $U$ et $V$ de $x$ tels que $A \cap U$ soit fermé dans
$U$ et $B \cap V$ soit fermé dans $V$. Par construction, $U \cap V$ est
un voisinage ouvert de $x$ ; en effet, d'une part cette intersection
contient $x$ et d'autre part pour tout $y$ dans $U \cap V$,
$d(y, X \setminus U) > 0$ et $d(y, X \setminus V) > 0$ ; or $$
\begin{split}
d(y, X \setminus (U \cap V)) 
&= 
d(y, (X \setminus U) \cup (X \setminus V)) \\
&= \min \left( d(y, X \setminus U), d(y, X \setminus V) \right) \\
&> 0.
\end{split}
$$ donc $U \cap V$ est ouvert. L'ensemble $A$, qui est fermé dans $U$,
est donc fermé dans $U \cap V$ (si une suite de $A$ converge dans
$U \cap V$, elle converge dans $U$ et donc sa limite appartient à $A$) ;
de la même façon, $B$ est fermé dans $U \cap V$. Par conséquent,
$A \cap B$ est fermé dans $U \cap V$.
:::

::: {.section}
#### Question 3 {#answer-lf-3 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Si un ensemble est l'intersection d'un ouvert et d'un fermé dans $X$, il
est l'intersection de deux ensembles localement fermés, donc il est
localement fermé (par les résultats de la [question précédente (p.
`\pageref*{lf-2}`{=tex})](#lf-2)).

Réciproquement, supposons que l'ensemble $A$ soit localement fermé. En
tout point $a \in A$, il existe un voisinage ouvert $V_a$ de $a$ tel que
$A\cap V_a$ soit fermé dans $V_a$. L'ensemble
$V_a \setminus (A \cap V_a) = V_a \setminus A$ est donc ouvert dans
$V_a$ et donc dans $X$. Par construction, la collection des $V_a$
recouvre $A$, c'est-à-dire que $A \subset \cup_{a \in A} V_a$, donc $$
A = \bigcup_{a \in A} V_a \setminus \left(\bigcup_{a \in A} V_a \setminus A\right).
$$ Posons $V = \cup_{a \in A} V_a$ ; le complémentaire dans $X$ de
$\bigcup_{a \in A} V_a \setminus A$ est un ensemble fermé $F$ ; de
l'équation ci-dessus on déduit donc que $A = V \cap F$ où $V$ est ouvert
dans $X$ et $F$ est fermé dans $X$.
:::
:::

::: {.section}
Distance entre ensembles
------------------------

::: {.section}
#### Question 1 {#answer-dh-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Non, la distance usuelle $d(A,B)$ en convient pas. En effet, cette
distance est nulle dès que l'intersection de $A$ et $B$ est non vide,
même si des points de $A$ sont très éloignés de $B$.
:::

::: {.section}
#### Question 2 {#answer-dh-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Lorsque $A = [-1,1] \times [-1, 1]$ et $B = [0,2] \times [0,2]$, il est
possible de calculer $d(a, B)$ pour tout $a \in A$. Plus précisément,
$B$ étant fermé, l'infimum qui définit la distance est un minimum. Dans
ce cas précis, il existe un unique projeté $\pi_B(a)$ de $a$ sur $B$,
qui minimise la distance $$
d(a, \pi_B(a)) = \inf_{b \in B} d(a, b).
$$ Il est donné quadrant par quadrant par $$
\pi_B((x, y)) = \left|
\begin{array}{rl}
(0, y) & \mbox{si } (x, y) \in [-1, 0] \times [0,1] \\
(x, y) & \mbox{si } (x, y) \in [0, 1] \times  [0,1] \\
(0, 0) & \mbox{si } (x, y) \in [-1, 0] \times [-1,0] \\
(x, 0) & \mbox{si } (x, y) \in [0, 1] \times [-1,0] \\
\end{array}
\right.
$$ Par conséquent, on a $$
d((x, y), B) = \left|
\begin{array}{rl}
|x| & \mbox{si } (x, y) \in [-1, 0] \times [0,1] \\
0 & \mbox{si } (x, y) \in [0, 1] \times  [0,1] \\
\sqrt{x^2 + y^2} & \mbox{si } (x, y) \in [-1, 0] \times [-1,0] \\
|y| & \mbox{si } (x, y) \in [0, 1] \times [-1,0] \\
\end{array}
\right.
$$ Cette fonction est maximale sur $A$ pour $(x, y) = (-1, -1)$. On a
donc $$
\sup_{a \in A} \inf_{b \in B} d(a, b) = \sqrt{2}.
$$ On montre de la même façon que $$
\sup_{b \in B} \inf_{a \in A} d(a, b) = \sqrt{2}.
$$ La distance de Hausdorff entre $A$ et $B$ vaut donc $\sqrt{2}$.
:::

::: {.section}
#### Question 3 {#answer-dh-3 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Vérifions que la "distance" de Hausdorff est effectivement une distance
sur l'espace des sous-ensembles fermés bornés non vides de
$\mathbb{R}^n$.

1.  Axiome de séparation. Si
    $$d[A, B] = \max(\sup_{a \in A} d(a, B), \sup_{b \in B} d(b, A)) = 0,$$
    alors pour tout $a \in A$, $d(a, B) = 0$ et pour tout $b \in B$,
    $d(b, A) = 0$, c'est-à-dire $a \in \overline{B}$ et
    $b \in \overline{A}$. Par conséquent, puisque $A$ et $B$ sont
    fermés, $A \subset \overline{B} = B$ et $B \subset \overline{A} = A$
    et donc $A = B$.

2.  Axiome de symétrie. Il est clair par construction que pour tous les
    ensembles fermés bornés non vides $A$ et $B$ de $\mathbb{R}^n$, on a
    $d[A, B] = d[B, A]$.

3.  Pour tout $a \in A$, $b \in B$, $c \in C$, l'inégalité triangulaire
    fournit $d(a, c) \leq d(a, b) + d(b, c)$. Par conséquent,
    $\inf_{c \in C} d(a, c) \leq d(a, b) + \inf_{c \in C}d(b, c)$ et
    donc $$
    \begin{split}
    \inf_{c \in C} d(a, c) 
    &\leq \inf_{b \in B} d(a, b) + \inf_{b \in B} \inf_{c \in C}d(b, c) \\
    &\leq
    \inf_{b \in B} d(a, b) + \sup_{b \in B} \inf_{c \in C}d(b, c),
    \end{split}
    $$ inégalité dont on déduit $$
    \sup_{a \in A} \inf_{c \in C} d(a, c) \leq
    \sup_{a \in A} \inf_{b \in B} d(a, b) + \sup_{b \in B} \inf_{c \in C}d(b, c)
    $$ et par conséquent $$
    \sup_{a \in A} \inf_{c \in C} d(a, c) \leq
    d[A, B] + d[B, C].
    $$ De façon similaire, on a $$
    \sup_{c \in C} \inf_{a \in A} d(a, c) \leq
    \sup_{c \in A} \inf_{b \in B} d(c, b) + \sup_{b \in B} \inf_{a \in A}d(b, a)
    $$ et par conséquent $$
    \sup_{c \in C} \inf_{a \in A} d(a, c) \leq
    d[A, B] + d[B, C]
    $$ et donc $d[A, C] \leq d[A, B] + d[B, C]$.
:::

::: {.section}
#### Question 4 {#answer-dh-4 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 4}`{=latex}

Si $A$ et $B$ sont des ensembles non vides de $\mathbb{R}^n$, $A+B$ est
clairement non vide. Si de plus $A$ et $B$ sont fermés et bornés, et que
l'on considère une suite $x_k$ de points de $A+B$, alors il existe des
$a_k$ de $A$ et $b_k$ de $B$ tels que $x_k = a_k + b_k$. Par compacité
de $A$, il existe une suite $a_{\sigma(k)}$ -- où
$\sigma: \mathbb{N}\to \mathbb{N}$ est croissante -- qui converge vers
un $a \in A$ ; par compacité de $B$, il existe une suite
$b_{\tau (\sigma(k))}$ -- où $\tau: \mathbb{N}\to \mathbb{N}$ est
croissante -- qui converge vers un $b \in B$. Par continuité de la somme
dans $\mathbb{R}^n$, la suite des $x_{\tau (\sigma(k))}$, qui est
extraite des $x_k$, converge vers $a+b \in A+B$.

Soit $A$, $B$, $C$ et $D$ quatre ensembles fermés bornés non vides de
$\mathbb{R}^n$. Si $a \in A$, $b \in B$, $c \in C$ et $d \in D$, on a $$
d(a+b, c+d) = \|a+b - c -d\| \leq \|a - c\| + \|b - d\|.
$$ Par conséquent, $$
\begin{split}
\sup_{x \in A + B} \inf_{y \in C + D} d(x, y)
&=
\sup_{a \in A} \sup_{b \in B} \inf_{c \in C} \inf_{d \in D}
\|a + b - c - d\| \\
&\leq
\sup_{a \in A} \sup_{b \in B} \inf_{c \in C} \inf_{d \in D}
\|a - c\| + \|b - d\| \\
&\leq \sup_{a \in A} \inf_{c \in C} 
\|a - c\| 
+ \sup_{b \in B} \inf_{d \in D}
\|b - d\| \\
&\leq d[A, C] + d[B, D].
\end{split}
$$ De même, on peut montrer que $$
\sup_{y \in C+D} \inf_{x \in A + B} d(x, y) \leq d[A, C] + d[B, D]
$$ et par conséquent $d[A + B, C + D] \leq d[A, C] + d[B, D].$ Si
$A_k \to A$ et $C_k \to C$, comme
$d[A_k+C_k, A+C] \leq d[A, A_k] + d[C, C_k]$, on en déduit que
$A_k + C_k \to A + C$. La somme de Minkowski est donc continue.
:::
:::

::: {.section}
Plongement de Kuratowski
------------------------

::: {.section}
#### Question 1 {#answer-pk-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Soit $x$, $x'$ deux points de $X$. Pour tout $y$ dans $X$ on a : $$
\begin{split}
f_x(y) - f_{x'}(y) &= d(x, y) - d(x_0, y) - (d(x', y) - d(x', x_0))\\
&= d(x, y) - d(x', y),
\end{split}
$$ par conséquent, si $f_x = f_{x'}$, on a en particulier
$f_x(x') = f_{x'}(x')$, soit $d(x, x') - d(x', x') = d(x, x') = 0$,
c'est-à-dire $x = x'$ par [l'axiome de séparation (p.
`\pageref*{dist-sep}`{=tex})](#dist-sep).
:::

::: {.section}
#### Question 2 {#answer-pk-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Pour tout $x, y \in X$, on a $$
|f_x(y)| = |d(x, y) - d(x_0, y)| \leq d(x, x_0)
$$ par [l'inégalité triangulaire (p.
`\pageref*{dist-ineg}`{=tex})](#dist-ineg).
:::

::: {.section}
#### Question 3 {#answer-pk-3 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Soient $x, y \in X$ ; on a $$
f_x(z) - f_y(z) = d(z, x) - d(z, x_0) - (d(z, y) - d(z, x_0)) = d(z, x) - d(z, y).
$$ Par conséquent, par [l'inégalité triangulaire (p.
`\pageref*{dist-ineg}`{=tex})](#dist-ineg), $$
\|f_x - f_y\|_{\infty}
= \sup_{y \in X} |d(z, x) - d(z, y)| \leq d(x, y)
$$ et d'autre part $$
\|f_x - f_y\|_{\infty}
= \sup_{y \in X} |d(z, x) - d(z, y)| \geq |d(x, x) - d(x, y)| = d(x, y).
$$ Finalement, on a bien $$
\|f_x - f_y\|_{\infty} = d(x, y)
$$ et $x \mapsto f_x$ est une isométrie.
:::
:::

::: {.section}
Le nombre d'or {#golden-ratio}
--------------

::: {.section}
#### Question 1 {#answer-golden-ratio-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

L'existence d'un unique point fixe associé à l'application $$
f: x \in \left]0, +\infty\right[ \mapsto 1 + \frac{1}{x}
$$ peut être établi par des méthodes classiques d'analyse d'une fonction
d'une variable réelle. La fonction
$g: x \in \left]0, +\infty\right[ \to x - f(x)$ est dérivable. Sa
dérivée en $x$ vaut $1 + 1/x^2$, qui est strictement positive, donc la
fonction $g$ est strictement croissante et il existe donc au plus un
zéro de $g$. De plus, $g(x) \to -\infty$ quand $x\to 0$ et
$g(x) \to +\infty$ quand $g(x) \to +\infty$. Comme $g$ est continue
(puisque dérivable), par le théorème des valeurs intermédiaires, $g$
admet bien un zéro sur $\left]0, +\infty\right[$. La fonction $f$ admet
donc un unique point fixe. Comme $g(4/3) = 4/3 - 1 - 3/4 = -5/12 <0$ et
$g(2) = 2 - 1 - 1/2 = 1/2 > 0$, le point fixe de $f$ se situe dans
l'intervalle $[3/2, 2]$.
:::

::: {.section}
#### Question 2 {#answer-golden-ratio-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Soit $x_k$ la suite de réels définie par $x_0 \in [4/3, 2]$ et
$x_{k+1} = f(x_k)$. La fonction $f$ est continue et décroissante
croissante ; de plus $$
f(4/3) = 1 + \frac{1}{4/3} = 1 + \frac{3}{4} = \frac{7}{4} \in \left[\frac{4}{3}, 2\right]
$$ et $$
f(2) = 1 + \frac{1}{2} = \frac{3}{2}  \in \left[\frac{4}{3}, 2\right].
$$ Par conséquent, $f([4/3,2]) \subset [4/3,2]$. Comme
$f'(x) = - 1/x^2$, pour tout $x \in [4/3,2]$, $|f'(x)| < 9/16 < 1$. Par
le théorème des accroissements finis, la restriction de $f$ à $[4/3, 2]$
est donc contractante. L'ensemble $[4/3, 2]$ est un ensemble fermé de
$\mathbb{R}$ qui est complet ; [il est donc complet (p.
`\pageref*{sous-espaces-complets}`{=tex})](#sous-espaces-complets).
L'existence et l'unicité du point fixe de $f$ sur $[4/3,2]$ ainsi que
son obtention comme limite de la suite $x_k$ résultent du [théorème de
point fixe de Banach (p. `\pageref*{T-TPFB}`{=tex})](#T-TPFB).
:::

::: {.section}
#### Question 3 {#answer-golden-ratio-3 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Compte tenu des résultats de l'exercice ["Point fixe" (p.
`\pageref*{TPFB2}`{=tex})](#TPFB2), il suffit d'établir que sur un
sous-ensemble complet $X$ de $\left]0, +\infty\right[$ tel que
$f(X) \subset X$, $f \circ f$ est contractante pour conclure que $f$
possède un unique point fixe sur $X$, obtenu comme limite de la suite
définie par $x_{k+1} = f(x_k)$ pour tout $x_0 \in X$.

Posons $X = \left[1, +\infty\right[$ ; $X$ est complet car [c'est un
sous-ensemble fermé de $\mathbb{R}$ qui est complet (p.
`\pageref*{sous-espaces-complets}`{=tex})](#sous-espaces-complets). De
plus, comme pour tout $x>0$, $1+1/x > 1$, on a bien
$f(\left[1, +\infty\right[) \subset \left[1, +\infty\right[$. Pour tout
$x \geq 1$, on a $$
f(f(x)) = 1+ \frac{1}{(1+1/x)} = 1 + \frac{x}{x+1} = 1+\frac{x+1}{x+1} - \frac{1}{x+1}
=2 - \frac{1}{x+1}
$$ et donc $$
(f \circ f)'(x) = \frac{1}{(x+1)^2}
$$ ce qui entraîne que $|(f \circ f)'(x)| \leq 1/4 < 1$ si $x\geq 1$. La
restriction de $f \circ f$ à $\left[1, +\infty\right[$ est donc
contractante. Nous avons donc établi toutes les hypothèses garantissant
que la suite $x_{k+1} = f(x_k)$ tend vers le nombre d'or si
$x_0 \geq 1$. Notons finalement que si $x_0 \in \left]0,1\right[$,
$f(x_0) \in \left[1, +\infty\right[$ ; par conséquent le résultat vaut
non seulement pour tout $x_0 \in \left[1, +\infty\right[$ mais bien pour
tout $x_0 \in \left]0, +\infty\right[$.
:::
:::

::: {.section}
Spirale d'Euler
---------------

::: {.section}
#### Question 1 {#answer-se-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Montrer que $(x(t), y(t))$ à une limite quand $t\to+\infty$ suppose de
montrer qu'il existe un point $T \in \mathbb{R}^2$ tel que pour toute
suite de valeurs $t_k$ tendant vers $+\infty$, la suite
$(x(t_k), y(t_k))$ tende vers $T$. Compte tenu de l'hypothèse, cela
revient à montrer que la limite d'une telle suite est indépendante du
choix de la suite des $t_k$.

Considérons deux suites $s_k$ et $r_k$ de réels positifs tendant vers
$+\infty$ et notons $S$ et $R$ les limites de $(x(s_k), y(s_k))$ et
$(x(r_k), y(r_k))$. La suite $t_k$ des réels $s_0$, $r_0$, $s_1$,
$r_1, \dots$ est positive et tend vers $+\infty$. Les $(x(t_k), y(t_k))$
admettent donc une limite $T$ quand $k \to +\infty$ ; toute sous-suite
étant convergente et de même limite, on a nécessairement $T = S = R$, ce
qui prouve le résultat cherché.
:::

::: {.section}
#### Question 2 {#answer-se-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Nous traitons le cas de $I(a, b)$, celui de $J(a, b)$ étant similaire.
Pour tout $a$ et $b$ tels que $0 < a \leq b$, le changement de variable
$\tau = s^2$ fournit : $$
I(a, b) = \int_a^b \cos s^2 \, ds = \int_{a^2}^{b^2} \frac{\cos \tau}{2\sqrt{\tau}} \, d\tau.
$$ Par intégration par parties, on obtient alors $$
I(a, b) = \frac{\sin b^2}{2b} -  \frac{\sin a^2}{2a} 
+ \int_{a^2}^{b^2} \frac{\sin \tau}{4\tau^{3/2}} \, d\tau.
$$ Comme pour tout $\tau \geq 0$, $|\sin \tau| \leq 1$, on a $$
\left|\frac{\sin b^2}{2b} -  \frac{\sin a^2}{2a}\right|
\leq \frac{1}{2b} + \frac{1}{2a}
$$ et par l'inégalité triangulaire, $$
\left| \int_{a^2}^{b^2} \frac{\sin \tau}{4\tau^{3/2}} \, d\tau \right|
\leq \int_{a^2}^{b^2} \frac{d \tau}{4\tau^{3/2}}
= - \frac{1}{2b} + \frac{1}{2a}.
$$ On en déduit donc $$
\left|I(a, b)\right| 
\leq 
\frac{1}{2b} + \frac{1}{2a} - \frac{1}{2b} + \frac{1}{2a} = \frac{1}{a}.
$$
:::

::: {.section}
#### Question 3 {#answer-se-3 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Pour établir l'existence d'un point limite à la spirale d'Euler, compte
tenu du résultat de la question 1, il nous suffit de montrer que pour
toute suite de valeurs $t_k$ tendant vers $+\infty$, la suite des
$(x_k, y_k) = (x(t_k), y(t_k))$ est convergente. Comme nous ne
connaissons par la valeur de cette limite, nous allons établir que cette
suite est de Cauchy ; l'ensemble $\mathbb{R}^2$ étant complet, cela
prouvera la convergence de la suite.

Or, pour tout couple d'entier $n$ et $p$, on a $$
\begin{split}
x_n - x_p = x(t_n) - x(t_p) 
&= \int_0^{t_n} \cos s^2 \, ds - \int_0^{t_p} \cos s^2 \, ds \\
&=\int_{t_p}^{t_n} \cos s^2 \, ds \\& = I(t_p, t_n)
\end{split}
$$ et de façon similaire, $$
y_n - y_p = \int_{t_p}^{t_n} \sin s^2 \, ds  = J(t_p, t_n).
$$ En exploitant le résultat de la question 2, on peut alors en déduire
que `\begin{align*}
\|(x_n, y_n) - (x_p, y_p)\| 
&= 
\sqrt{I(t_p, t_n)^2 + J(t_p, t_n)^2} \\
&\leq \sqrt{\frac{1}{\min(t_p, t_n)^2} + \frac{1}{\min(t_p, t_n)^2}} \\
&= \frac{\sqrt{2}}{\min(t_p, t_n)}.
\end{align*}`{=tex} Pour un $\varepsilon > 0$ donné, il suffit de
choisir un rang $m \in \mathbb{N}$ tel que $$
t_k \geq \frac{\sqrt{2}}{\varepsilon}, \, \mbox{ quand $k\geq m$}
$$ pour avoir la garantie que si $p \geq m$ et $n \geq m$, alors $$
\|(x_n, y_n) - (x_p, y_p)\| 
\leq \varepsilon.
$$ La suite des $(x_k, y_k)$ est donc de Cauchy.
:::
:::

::: {.section}
Point fixe
----------

::: {.section}
#### Question 1 {#answer-pf-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Si $x$ est un point fixe de $f$, $f(x) = x$, par conséquent $$
f^2(x) = f(f(x)) = f(x) = x, 
$$ puis $$
f^3(x) = f(f^2(x)) = f(x) = x,
$$ etc. Par récurrence, il est clair que l'on peut établir que pour tout
$n \geq 1$, on a $f^n(x) = x$ : $x$ est un point fixe de $f^n$.

Supposons désormais que la fonction itérée $f^n$ admette un unique point
fixe $x$. Comme tout point fixe de $f$ est un point fixe de $f^n$, $f$
admet au plus un point fixe. De plus, comme $f^n(x) = x$, en applicant
$f$ aux deux membres de cette équation, on obtient $$
f(f^n(x)) = f^n(f(x)) = f(x).
$$ Par conséquent, $f(x)$ est un point fixe de $f^n$ ; c'est donc
l'unique point fixe $x$ de $f^n$. On a donc $f(x) = x$, c'est-à-dire que
$x$ est un point fixe de $f$.
:::

::: {.section}
#### Question 2 {#answer-pf-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Si $X$ est un espace métrique complet et que $f^n$ est contractante, par
[théorème du point fixe de Banach (p.
`\pageref*{T-TPFB}`{=tex})](#T-TPFB), $f^n$ admet un unique point fixe
$x$, calculable comme limite de toute suite $y_k$ telle que
$y_{k+1} = f^n(y_k)$ et $y_0 \in X$.

Par les résultats de [la question 1 (p.
`\pageref*{pf-1}`{=tex})](#pf-1), $x$ est l'unique point fixe de $f$. Le
"procédé habituel pour construire un point fixe de $f$" consiste à
prendre un $x_0 \in X$ quelconque et à construire par récurrence la
suite des $x_{k+1} = f(x_k)$ ; on souhaite donc montrer que cette suite
converge vers l'unique point fixe $x$ de $f$. La suite $(x_{kn})_k$ --
extraite des $x_k$ -- converge vers $x$, car $x_{(k+1)n} = f^n(x_{kn})$.
Il en est de même pour la suite extraite $(x_{kn+1})_k$, construite à
partir du même procédé mais en initialisant la séquence avec la valeur
$x_1$, pour la suite $(x_{kn+2})_k$, ..., jusqu'à $(x_{kn + (n-1)})_k$.
Ces $n$ suites convergent toutes vers $x$, donc la suite des $(x_k)_k$
converge également vers le point fixe $x$.
:::
:::

::: {.section}
Résolution itérative de systèmes linéaires
------------------------------------------

::: {.section}
#### Question 1 {#answer-risl-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

La relation $A \cdot x = y$ est vérifiée si et seulement si
$D \cdot x + (A - D) \cdot x = y$, soit $$
D \cdot x = (D - A) \cdot x + y.
$$ L'opérateur $A$ étant diagonalement dominant, $a_{ii} > 0$ pour tout
$i$ ; l'opérateur $D$ est donc inversible. La relation ci-dessus est
donc équivalente à $$
x = D^{-1} \cdot (D-A) \cdot x + D^{-1} \cdot y.
$$
:::

::: {.section}
#### Question 2 {#answer-risl-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

La question 1 établit que pour tout $y \in \mathbb{R}^n$, le vecteur
$x \in \mathbb{R}^n$ est solution de $A \cdot x = y$ si et seulement
s'il est un point fixe de l'application $$
\phi: x \in \mathbb{R}^n \mapsto D^{-1} \cdot (D-A) \cdot x + D^{-1} \cdot y \in \mathbb{R}^n.
$$ Cette application est affine : pour tout couple $x_1$ et $x_2$ dans
$\mathbb{R}^n$, $$
\phi(x_1) - \phi(x_2) = D^{-1} \cdot (D-A) \cdot (x_1 - x_2).
$$ Notons qu'avec $B := D^{-1} \cdot (D-A)$ et $[B]_{ij} = b_{ij}$, on a
$b_{ii} = 0$ et si $i \neq j$, $b_{ij} = -a_{ij}/a_{ii}$. Par
conséquent, pour tout $i$, $\sum_{j=1}^n |b_{ij}| < 1$, soit $$
\max_{i=1\dots n} \sum_{j=1}^n  |b_{ij}| < 1.
$$ On reconnait au membre de gauche de cette inégalité la norme
d'opérateur $\|B\|_{\infty}$ de l'exercice ["Normes d'opérateurs" (p.
`\pageref*{no}`{=tex})](#no) ; on a donc pour tout $x \in \mathbb{R}^n$,
$$
\|B \cdot x\|_{\infty} \leq \kappa \|x\|_{\infty}
\; \mbox{ avec } \; \kappa:=\|B\|_{\infty} < 1
$$ (on peut aussi établir ce résultat directement). Si l'on munit
$\mathbb{R}^n$ de la norme $\|\cdot\|_{\infty}$ (l'espace est alors
complet puisque $\|\cdot\|_{\infty}$ est équivalent à la norme
euclidienne : on a
$\|\cdot\|_2 / \sqrt{n} \leq \|\cdot\|_{\infty} \leq \|\cdot\|_2$),
l'application $\phi$ est contractante. Par [le théorème du point fixe de
Banach (p. `\pageref*{T-TPFB}`{=tex})](#T-TPFB), elle admet donc un
unique point fixe $x$, qui est la solution de $A \cdot x = y$.
L'opérateur $A$ est donc inversible et $A^{-1} \cdot y$ peut être
calculé comme la limite de la suite $x_{k+1} = B \cdot x_k+D^{-1}y$ pour
un $x_0 \in \mathbb{R}^n$ arbitraire.
:::
:::

::: {.section}
Équation différentielle
-----------------------

::: {.section}
#### Question 1 {#answer-ed-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Si la fonction $x$ est continue et vérifie pour tout $t\geq0$ l'équation
intégrale $$
x(t) = x_0 + \int_0^t A \cdot x(s) \, ds,
$$ alors nécessairement $$
x(0) =x_0 + \int_0^0 A \cdot x(s) \, ds = x_0,
$$ et sa dérivée satisfait $\dot{x}(t) = A \cdot x(t)$.

Réciproquement, si $x(0) = x_0$ et pour tout $t \geq 0$ on a
$\dot{x}(t) = A \cdot x(t)$, alors comme le second membre de cette
équation est continue comme composée de fonctions continues, $\dot{x}$
est continue, et par intégration entre $0$ et $t$ on retrouve l'équation
intégrale souhaitée.
:::

::: {.section}
#### Question 2 {#answer-ed-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Par linéarité de l'intégrale et de l'opérateur $A$, pour tout couple $x$
et $y$ de fonctions continue de $[0, T]$ dans $\mathbb{R}^n$ et tout
$t \in [0, T]$, on a $$
(\Phi(x) - \Phi(y))(t) = \int_0^t A \cdot (x(s) - y(s)) \, ds,
$$ et donc $$
\begin{split}
\|(\Phi(x)(t) - \Phi(y)(t)\| &\leq \int_0^t \|A \cdot (x(s) - y(s))\| \, ds \\
&\leq  \int_0^t \|A \| \|x - y\|_{\infty} \, ds \\
&= (\|A\| T) \times \|x - y\|_{\infty}, \\
\end{split}
$$ soit $$
\|\Phi(x) - \Phi(y)\|_{\infty} \leq (\|A\| T) \times \|x - y\|_{\infty}.
$$ L'application $\Phi$ est donc contractante si $\|A\| < 1/T$. [Le
théorème du point fixe de Banach (p.
`\pageref*{T-TPFB}`{=tex})](#T-TPFB) prouve alors l'unicité d'une
fonction continue telle que $$
x(t) = x_0 + \int_0^t A \cdot x(s) \, ds
$$ pour tout $t \in [0, T]$.
:::

::: {.section}
#### Question 3 {#answer-ed-3 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Le fait que $\|\cdot\|_{\infty}^{\alpha}$ soit une norme se déduit
facilement du fait que $\|\cdot\|_{\infty}$ en soit une. On peut
constater que pour toute fonction $x$ continue sur $[0, T]$, on a $$
\|e^{-\alpha T} x\|_{\infty}^{\alpha} \leq \|x\|_{\infty}^{\alpha} \leq \|x\|_{\infty}.
$$ Les deux normes sont donc équivalentes. En particulier, les notions
de convergence de suite de points et de suites de Cauchy sont les mêmes
dans les deux espaces. L'espace vectoriel $E$ muni de la norme
$\|\cdot\|_{\infty}$ étant complet, c'est également le cas pour $E$ muni
de la norme $\|\cdot\|^{\alpha}_{\infty}$.
:::

::: {.section}
#### Question 4 {#answer-ed-4 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 4}`{=latex}

Pour tout couple $x$ et $y$ de fonctions continue de $[0, T]$ dans
$\mathbb{R}^n$ et tout $t \in [0, T]$, on a $$
e^{-\alpha t} (x-y)(t) 
= e^{-\alpha t} \int_{0}^t A \cdot (x-y)(s) \, ds
= \int_{0}^t A \cdot e^{-\alpha s}(x-y)(s) e^{-\alpha (t-s)} \, ds
$$ et donc $$
\begin{split}
\left|e^{-\alpha t} (x-y)(t)\right|
&\leq 
\int_{0}^t \|A\| \|e^{-\alpha s}(x-y)(s)\| e^{-\alpha (t-s)} \, ds \\
&\leq 
\left(\|A\| \int_0^t e^{-\alpha (t-s)} \, ds \right) \|x-y\|_{\infty}^{\alpha}.
\end{split}
$$ Comme $$
\int_0^t e^{-\alpha (t-s)} \, ds
= \left[\frac{e^{-\alpha (t-s)}}{\alpha} \right]_0^t
=\frac{1 - e^{-\alpha t}}{\alpha} \leq \frac{1}{\alpha},
$$ on en déduit que $$
\|x - y\|_{\infty}^{\alpha} \leq \frac{\|A\|}{\alpha} \|x-y\|_{\infty}^{\alpha}.
$$ L'application $\Phi$ est donc contractante dès lors que
$\alpha > \|A\|$. Pour tout $T > 0$, [le théorème du point fixe de
Banach (p. `\pageref*{T-TPFB}`{=tex})](#T-TPFB) prouve donc, en
sélectionnant un $\alpha$ adapté, l'unicité d'une fonction continue
telle que $$
x(t) = x_0 + \int_0^t A \cdot x(s) \, ds
$$ pour tout $t \in [0, T]$. Le problème original admet donc une
solution unique.
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

[^3]: d'après [Stefan
    Banach](https://en.wikipedia.org/wiki/Stefan_Banach), un
    mathématicien polonais du 20ème siècle d'après lequel sont nommés
    [de nombreux concepts et
    théorèmes](https://en.wikipedia.org/wiki/List_of_things_named_after_Stefan_Banach).

[^4]: bien sûr si l'on a utilisé une technique alternative pour
    construire $\mathbb{R}$, par exemple par les coupures de Dedekind,
    la complétude de $\mathbb{R}$ n'a rien d'automatique.

[^5]: Par exemple, l'espace formé de deux points $\{0, 1\}$ où $x$
    adhère à $A$ si $x$ appartient à $A$ ou $x=0$ et $A=\{1\}$ --
    c'est-à-dire l'[espace de
    Sierpiński](https://en.m.wikipedia.org/wiki/Sierpi%C5%84ski_space)
    -- est un espace topologique qui n'est pas métrisable. En effet, si
    $d$ était une distance sur cet ensemble, telle que $d(x, A)= 0$ si
    et seulement si $x$ adhère à $A$, alors on aurait
    $d(0, \{1\}) = d(0, 1) = 0$, ce qui contredirait [l'axiome de
    séparation pour les distances (p.
    `\pageref*{dist-sep}`{=tex})](#dist-sep).

[^6]: **Pilule rouge.** Dans le monde réel, on trouvera fréquemment la
    notation $\overline{\mathbb{R}}$ pour désigner l'ensemble des réels
    étendus ; mais cette convention se heurte alors avec la désignation
    de l'adhérence de $\mathbb{R}$ dans lui-même, une interprétation
    selon laquelle on aurait $\overline{\mathbb{R}} = \mathbb{R}$.

[^7]: ou plus généralement dans un espace topologique.

[^8]: Cette courbe a été introduite par Euler en 1744. Il lui apparait
    alors manifeste que la courbe est une spirale qui s'enroule après un
    nombre de tours infinis autour d'un centre bien défini, mais que ce
    point est très difficile à déterminer par cette construction. Il
    faudra attendre 1781 pour qu'Euler puisse calculer analytiquement
    les coordonnées de ce point (cf. @Lev08).
