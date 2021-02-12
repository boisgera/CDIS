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
title: Calcul Différentiel III
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
-   [Matrice hessienne et différentielle d'ordre
    $2$](#matrice-hessienne-et-différentielle-dordre-2)
-   [Différentielle d'ordre
    supérieur](#différentielle-dordre-supérieur-1)
    -   [Puissance symbolique](#puissance-symbolique)
    -   [Développement de Taylor avec reste intégral I](#DTRI-I)
    -   [Développement de Taylor avec reste intégral II](#DTRI-II)
-   [Annexe](#annexe)
-   [Exercices complémentaires](#exercices-complémentaires)
    -   [Convexité](#convexité)
    -   [Différentiation en chaîne à l'ordre
        2](#différentiation-en-chaîne-à-lordre-2)
    -   [Différentielle d'ordre 2 et symétrie
        I](#différentielle-dordre-2-et-symétrie-i)
    -   [Différentielle d'ordre 2 et symétrie
        II](#différentielle-dordre-2-et-symétrie-ii)
    -   [Conditions d'optimalité](#conditions-doptimalité)
    -   [Différentiation matricielle](#différentiation-matricielle)
-   [Solutions](#solutions)
    -   [Exercices essentiels](#exercices-essentiels)
    -   [Convexité](#convexité-1)
    -   [Différentiation en chaîne à l'ordre
        2](#différentiation-en-chaîne-à-lordre-2-1)
    -   [Différentielle d'ordre 2 et symétrie
        I](#différentielle-dordre-2-et-symétrie-i-1)
    -   [Différentielle d'ordre 2 et symétrie
        II](#différentielle-dordre-2-et-symétrie-ii-1)
    -   [Conditions d'optimalité](#conditions-doptimalité-1)
    -   [Différentiation matricielle](#différentiation-matricielle-1)
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
```{=tex}
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
#### Matrice hessienne et différentiabilité d'ordre 2

-   `$\mathord{\bullet}$ `{=tex}connaître les définitions et notations
    de la matrice hessienne et des dérivées partielles d'ordre 2.

-   `$\mathord{\bullet}$ `{=tex}savoir définir et relier existence de la
    matrice hessienne, différentiabilité d'ordre 2 et continue
    différentiabilité d'ordre 2.

-   `$\mathord{\bullet}$ `{=tex}savoir à quelle condition la matrice
    hessienne est symétrique ; savoir exploiter cette symétrie.

-   `$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$ `{=tex}comprendre
    le concept de fonctions linéaires d'ordre $2$ ; savoir manipuler les
    notations associées ("$\to$", "$\cdot$", avec associativité à droite
    et à gauche respectivement).

-   `$\mathord{\bullet}$ `{=tex}savoir définir la différentielle d'ordre
    $2$ de $f$ en $x$.

-   `$\mathord{\bullet}$ `{=tex}savoir déterminer $d^2f(x)$ en fonction
    de $H_f(x)$ et réciproquement.

-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}connaître et savoir
    exploiter les développements limités et avec reste intégral faisant
    intervenir la matrice Hessienne.
:::

::: {.section}
#### Différentielle d'ordre supérieur

-   `$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$ `{=tex}appréhender
    le concept de différentielle d'ordre $k$ : sa nature d'application
    linéaire d'ordre supérieur, quand elle existe, comment la calculer.

-   `$\mathord{\bullet}$ `{=tex}savoir définir et exploiter les dérivées
    partielles d'ordre $k$, leurs relations avec la différentielle
    d'ordre $k$, leurs symétries.

-   `$\mathord{\bullet}$ `{=tex}savoir caractériser la continue
    différentiabilité d'ordre $k$ et savoir l'exploiter pour établir la
    différentiabilité d'ordre $k$.

-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}connaître la notion de
    tenseur, les concepts d'ordre, type et contraction associés, et
    comment ces notions généralisent des concepts et opérations déjà
    connues.

-   `$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir
    représenter une application linéaire d'ordre supérieur par un
    tenseur et réciproquement ; faire le lien entre les coefficients du
    tenseur de la différentielle d'ordre $k$ et les dérivées partielles
    d'ordre $k$.

-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}connaître et savoir
    exploiter les développements limités et avec reste intégral à
    l'ordre $k$.
:::
:::

::: {.section}
Matrice hessienne et différentielle d'ordre $2$
===============================================

::: {.section}
### Définition -- Dérivées partielles d'ordre $2$ {#dérivées-partielles-dordre-2 .definition .one .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Dérivées partielles d'ordre \(2\)}`{=latex}

Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}$ et
$x \in U$. Si la $j_1$-ème dérivée partielle de $f$ est définie sur $U$,
et que la $j_2$-ème dérivée partielle de $\partial_{j_1} f$ en $x$
existe, on note $$
\partial^2_{j_2j_1} f(x) := \partial_{j_2} (\partial_{j_1} f)(x) \in \mathbb{R}.
$$ sa *dérivée partielle d'ordre $2$ par rapport aux $j_1$-ème et
$j_2$-ème variables*.
:::

::: {.section}
### Définition -- Matrice hessienne {#hessienne .definition .one .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Matrice hessienne}`{=latex}

Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}$ et $x$ un
point de $U$. Si toutes les dérivées partielles au premier ordre de $f$
existent sur $U$ et que toutes leurs dérivées partielles au premier
ordre existent en $x$, on définit *la matrice hessienne $H_f(x)$ de $f$
en $x$* par $$
[H_f(x)]_{j_1j_2} = \partial^2_{j_2 j_1} f(x) \in \mathbb{R}^{n \times n},
$$ c'est-à-dire $$
H_f(x) = J_{\nabla f}(x) = \left[
\begin{array}{cccc}
\partial^2_{11} f (x) & \partial^2_{21} f (x) & \cdots & \partial^2_{n1} f (x) \\
\partial^2_{12} f (x) & \partial^2_{22} f (x) & \cdots & \partial^2_{n2} f (x) \\
\vdots & \vdots & \vdots & \vdots \\
\partial^2_{1n} f (x) & \partial^2_{2n} f (x) & \cdots & \partial^2_{nn} f (x) \\
\end{array}
\right].
$$
:::

::: {.section}
#### Exercice -- Laplacien et matrice hessienne ($\mathord{\boldsymbol{\circ}}$) {#laplacien .exercise .question .zero .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Laplacien et matrice hessienne}`{=latex}

Soient $U$ un ouvert de $\mathbb{R}^n$, $x \in U$ et
$f: U \to \mathbb{R}$ une fonction dont la matrice hessienne en $x$ est
bien définie. Exprimer le laplacien de $f$ en $x$,
$\Delta f (x) := \sum_{i=1}^n \partial^2_{ii} f(x)$, en fonction de
$H_f(x)$. ([Solution p.
`\pageref*{answer-laplacien}`{=tex}](#answer-laplacien){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Matrice hessienne d'un monôme ($\mathord{\bullet}$) {#simple .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Matrice hessienne d'un monôme}`{=latex}

Soit $f: (x_1, x_2) \in \mathbb{R}^2 \to \mathbb{R}$ la fonction définie
par $f(x_1,x_2) = x_1x_2^2$. Montrer que la matrice $H_f(x)$ est définie
en tout point $x \in \mathbb{R}^2$ et la calculer. ([Solution p.
`\pageref*{answer-simple}`{=tex}](#answer-simple){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Matrice hessienne d'un lagrangien ($\mathord{\bullet}$) {#lagrangien .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Matrice hessienne d'un lagrangien}`{=latex}

Soient $U$ un ouvert de $\mathbb{R}^n$ et $f: U \to \mathbb{R}$ et
$g: U \to \mathbb{R}$ deux applications dont les matrices hessiennes
sont définies sur $U$. Soient $c \in \mathbb{R}$ une constante et
$L : U \times \mathbb{R}\to \mathbb{R}$ la fonction telle que
$L(x, \lambda) = f(x) + \lambda (g(x) - c)$. Calculer $H_L(x, \lambda)$.
([Solution p.
`\pageref*{answer-lagrangien}`{=tex}](#answer-lagrangien){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Matrice hessienne diagonale ($\mathord{\bullet}\mathord{\bullet}$) {#hessienne-diag .exercise .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Matrice hessienne diagonale}`{=latex}

Soit $f: \mathbb{R}^2 \to \mathbb{R}$ une fonction dont la matrice
hessienne est définie en tout point. Montrer que sa matrice hessienne
$H_f$ est diagonale en tout point de $\mathbb{R}^2$ si et seulement si
$f(x_1,x_2) = g(x_1) + h(x_2)$ où $g:\mathbb{R}\to\mathbb{R}$ et
$h:\mathbb{R}\to\mathbb{R}$ sont des fonctions deux fois dérivables.
([Solution p.
`\pageref*{answer-hessienne-diag}`{=tex}](#answer-hessienne-diag){.no-parenthesis}.)
:::

::: {.section}
### Définition -- Continue différentiabilité d'ordre 2 {#continue-différentiabilité-dordre-2 .definition .one .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Continue différentiabilité d'ordre 2}`{=latex}

Soient $U$ un ouvert de $\mathbb{R}^n$ et $f:U \to \mathbb{R}$. La
fonction $f$ est *deux fois continûment différentiable* si pour tout
$j_1 \in \{1,\dots, n\}$ et tout $j_2 \in \{1,\dots, n\}$, la dérivée
partielle d'ordre deux $\partial^2_{j_2j_1} f:U \to \mathbb{R}$ existe
et est continue.
:::

::: {.section}
Alternativement, la fonction $f$ est deux fois continûment
différentiable si la fonction
$x \in U \mapsto H_f(x) \in \mathbb{R}^{n\times n}$ est définie et
continue.
:::

::: {.section}
### Définition -- Différentielle d'ordre 2 {#d2 .definition .three .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Différentielle d'ordre 2}`{=latex}

Soient $U$ un ouvert de $\mathbb{R}^n$,
$f: U \subset \mathbb{R}^n \to \mathbb{R}$ et $x \in U$. On dira que $f$
est *deux fois différentiable en $x$* si $f$ est différentiable sur $U$
et si pour tout vecteur $h_1$ de $\mathbb{R}^n$, la fonction
$x \in U \mapsto df(x) \cdot h_1$ est différentiable en $x$. La
*différentielle d'ordre $2$ de $f$ en $x$*, notée $d^2f(x)$, est définie
comme l'application linéaire telle que pour tout $h_1$ dans
$\mathbb{R}^n$, $$
d^2 f(x) \cdot h_1 := d(x\mapsto df(x)\cdot h_1)(x),
$$ c'est-à-dire pour tout vecteur $h_2$ de $\mathbb{R}^n$, $$
(d^2f(x) \cdot h_1) \cdot h_2 = d(x\mapsto df(x)\cdot h_1)(x) \cdot h_2.
$$ On dit que $f$ est *deux fois différentiable (sur $U$)* si elle est
deux fois différentiable en tout point $x$ de $U$.
:::

::: {.section}
Dans cette définition, le caractère linéaire de $d^2f(x)$ repose sur le
lemme technique suivant :
:::

::: {.section}
### Lemme -- Linéarité de $d(x \mapsto df(x) \cdot h_1)(x)$ par rapport à $h_1$ {#linéarité-de-dx-mapsto-dfx-cdot-h_1x-par-rapport-à-h_1 .lemma .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Linéarité de \(d(x \mapsto df(x) \cdot h_1)(x)\) par rapport à \(h_1\)}`{=latex}

Soient $U$ un ouvert de $\mathbb{R}^n$,
$f: U \subset \mathbb{R}^n \to \mathbb{R}$ et $x\in U$. Si $f$ est
différentiable sur $U$ et si pour tout vecteur $h_1$ de $\mathbb{R}^n$,
la fonction $x \in U \mapsto df(x) \cdot h_1$ est différentiable en $x$,
alors la fonction $d(x \mapsto df(x) \cdot h_1)(x)$ dépend linéairement
de $h_1 \in \mathbb{R}^n$.
:::

::: {.section}
#### Démonstration {#démonstration .proof}

Pour tous $h_1, k_1 \in \mathbb{R}^n$, par additivité de $df(x)$ et de
la différentiation, `\begin{align*}
d(x\mapsto df(x)\cdot (h_1+k_1))(x) &= 
d(x\mapsto (df(x)\cdot h_1 + df(x)\cdot k_1))(x) \\ 
&= d((x\mapsto df(x)\cdot h_1) + (x \mapsto df(x)\cdot k_1))(x) \\ 
&= d(x\mapsto df(x)\cdot h_1)(x)  + d(x\mapsto df(x)\cdot k_1)(x) 
\end{align*}`{=tex} et pour tout $\alpha \in \mathbb{R}$, par
homogénéité de $df(x)$ et de la différentiation, `\begin{align*}
d(x\mapsto df(x)\cdot (\alpha h_1))(x) &=  d(x\mapsto \alpha df(x)\cdot h_1)(x) \\
&=d(\alpha(x\mapsto df(x)\cdot h_1))(x)
&= \alpha d(x\mapsto df(x)\cdot h_1)(x).
\end{align*}`{=tex}`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Remarque -- Applications linéaires d'ordre 2 {#applications-linéaires-dordre-2 .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Applications linéaires d'ordre 2}`{=latex}

Par construction, le terme $d(x\mapsto df(x)\cdot h_1)(x)$ est une
application linéaire de $\mathbb{R}^n$ dans $\mathbb{R}$, donc la
fonction $d^2f(x)$ associe linéairement à un vecteur de $\mathbb{R}^n$
une application linéaire de $\mathbb{R}^n$ dans $\mathbb{R}$.

Notons $A \to B$ l'ensemble des applications de $A$ dans $B$ ; on a donc
$$
d^2f(x) \in \mathbb{R}^n \rightarrow (\mathbb{R}^n \rightarrow \mathbb{R}),
$$ ce qui se décline successivement en $$
d^2f(x) \cdot h_1 \in \mathbb{R}^n \to \mathbb{R}
\; \mbox{ et } \;
(d^2f(x) \cdot h_1) \cdot h_2 \in \mathbb{R}.
$$ Pour simplifier les notations, on conviendra que dans ce contexte le
symbole "$\to$" associe à droite : $$
\mathbb{R}^n \to \mathbb{R}^n \to \mathbb{R} := \mathbb{R}^n \to (\mathbb{R}^n \to \mathbb{R}).
$$ La convention associée veut que lors de l'application d'une fonction
linéaire, le symbole "$\cdot$" associe à gauche : $$
d^2f(x) \cdot h_1 \cdot h_2 :=  (df^2(x) \cdot h_1) \cdot h_2.
$$

L'usage du "$.$" doit nous rappeller que les dépendances de
$df(x) \cdot h_1$ en $h_1$ et de $d^2f(x) \cdot h_1 \cdot h_2$ en $h_2$
sont linéaires[^3]. Cela signifie pour la linéarité de $d^2f(x)$ que
$d^2f(x) \cdot (\alpha h_1) = \alpha d^2f(x) \cdot h_1$ et
$d^2f(x) \cdot (h_1+k_1) = d^2f(x) \cdot h_1 + d^2f(x) \cdot k_1$ ; il
s'agit d'égalités entre fonctions de $\mathbb{R}^n \to \mathbb{R}$, que
nous devons donc interpréter comme : $$
\left|
\begin{array}{lll}
d^2f(x) \cdot (\alpha h_1) \cdot h_2 &=& \alpha d^2f(x) \cdot h_1 \cdot h_2 \\
d^2f(x) \cdot (h_1+k_1)\cdot h_2 &=& d^2f(x) \cdot h_1 \cdot h_2 + d^2f(x) \cdot k_1 \cdot h_2
\end{array}
\right.
$$ La linéarité de $d^2f(x)\cdot h_1$ conduit quant à elle à $$
\left|
\begin{array}{lll}
d^2f(x) \cdot h_1 \cdot (\beta h_2) &=& \beta d^2f(x) \cdot h_1 \cdot h_2 \\
d^2f(x) \cdot h_1 \cdot (h_2+k_2) &=& d^2f(x) \cdot h_1 \cdot h_2 + 
d^2f(x) \cdot h_1 \cdot k_2
\end{array}
\right.
$$ L'expression $d^2f(x) \cdot h_1 \cdot h_2$ est donc linéaire par
rapport à $h_1$ et $h_2$ pris isolément ; on parlera de dépendance
*bilinéaire* dans le couple $(h_1, h_2)$.
:::

::: {.section}
### Remarque -- Différentiation automatique d'ordre 2 {#différentiation-automatique-dordre-2 .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Différentiation automatique d'ordre 2}`{=latex}

La bibliothèque autograd nous a déjà permis de calculer automatiquement
le gradient de fonctions scalaires et la matrice jacobienne de fonctions
scalaires ou vectorielles.

    import autograd as ag
    from autograd import numpy as np

    def grad(f):
        def grad_f(*x):
            n = len(x)
            return np.array([ag.grad(f, i)(*x) for i in range(n)])
        return grad_f

    def J(f):
        def J_f(*x):
            n = len(x)
            di_f_x = [ag.jacobian(f, i)(*x) for i in range(n)]
            return np.array(di_f_x).T
        return J_f

Autograd permet également le calcul des dérivées partielles d'ordre
supérieur. Concrètement, on peut appliquer à nouveau un opérateur
différentiel sur une fonction qui est issue d'un calcul fait par
autograd. L'implémentation de la fonction qui calcule la matrice
hessienne d'une fonction scalaire est donc particulièrement simple :

    def H(f):
        return J(grad(f))

Un exemple d'usage :

    def f(x1, x2):
        return np.exp(-0.5 * (x1 * x1 + x2 * x2))

exercé de la façon suivante :

    >>> H_f = H(f)
    >>> H_f(1.0, 2.0)
    array([[0.      , 0.16417 ],
           [0.16417 , 0.246255]])
:::

::: {.section}
### Proposition -- Différentielle d'ordre 2 et matrice hessienne {#d2mh .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Différentielle d'ordre 2 et matrice hessienne}`{=latex}

Soient $U$ un ouvert de $\mathbb{R}^n$,
$f: U \subset \mathbb{R}^n \to \mathbb{R}$ et $x \in U$. La fonction $f$
est deux fois différentiable en $x$ si et seulement si elle est
différentiable sur $U$ et que son gradient $\nabla f$ est différentiable
en $x$. Sa matrice hessienne est alors définie en $x$ et pour tous
$h_1, h_2 \in \mathbb{R}^n$, $$
d^2f(x) \cdot h_1 \cdot h_2 = \left<h_1, H_f(x) \cdot h_2 \right> = h_1^{\top} \cdot H_f(x) \cdot h_2
=\sum_{j_1=1}^n \sum_{j_2=1}^n [H_f(x)]_{j_1j_2} h_{1j_1} h_{2j_2}.
$$ En particulier $$
[H_f(x)]_{j_1j_2} = d^2f(x) \cdot e_{j_1} \cdot e_{j_2}.
$$
:::

::: {.section}
#### Démonstration {#démonstration-1 .proof}

Si la fonction $f$ est deux fois différentiable en $x$, la fonction $f$
est différentiable donc son gradient existe. Pour tout
$h_1 \in \mathbb{R}^n$, la fonction $x \mapsto df(x) \cdot h_1$ est
également différentiable en $x$ donc en particulier, pour tout
$j_1 \in \{1, \dots, n\}$,
$(\nabla f(x))_{j_1} = \left<\nabla f(x), e_{j_1} \right> = df(x) \cdot e_{j_1}$ ;
le gradient de $f$ est différentiable composante par composante et donc
différentiable. Réciproquement, si $f$ est différentiable et que son
gradient est différentiable en $x$, pour tout $h \in \mathbb{R}^n$ on a
$$
df(x) \cdot h_1 = df(x) \cdot \left(\sum_{j_1=1}^n h_{1j_1} e_{j_1}\right)
= \sum_{j=1}^n h_{1j_1} df(x) \cdot e_{j_1}
= \sum_{j=1}^n h_{1j_1} (\nabla f(x))_{j_1} ;
$$ la fonction $x \mapsto (df(x)\cdot h)$ est donc différentiable en $x$
comme combinaison linéaire de fonction différentiables en $x$.

Par définition,
$[H_f(x)]_{j_1j_2}(x) = \partial^2_{j_2j_1} f(x) = \partial_{j_2} (\partial_{j_1} f) (x)$
et donc
$$[H_f(x)]_{j_1j_2}(x) = \partial_{j_2} (x \mapsto df(x)\cdot e_{j_1})(x)
= d(x \mapsto df(x)\cdot e_{j_1})(x) \cdot e_{j_2},$$ c'est-à-dire
$[H_f(x)]_{j_1j_2}(x) = d^2f(x) \cdot e_{j_1} \cdot e_{j_2}$. Pour
prouver l'égalité restante, on exploite la linéarité de
$d^2f(x) \cdot h_1 \cdot h_2$ par rapport à $h_1$ et à $h_2$ : $$
\begin{split}
d^2f(x) \cdot h_1 \cdot h_2
&=
d^2 f(x) \cdot 
\left( \sum_{j_1=1}^n h_{1j_1} e_{j_1} \right) \cdot \left( \sum_{j_2=1}^n h_{2j_2} e_{j_2} \right) \\
&=
\sum_{j_2=1}^n h_{2j_2} \left(
d^2 f(x) \cdot 
\left( \sum_{j_1=1}^n h_{1j_1} e_{j_1} \right) \cdot e_{j_2} \right) \\
&=
\sum_{j_1=1}^n \sum_{j_2=1}^n h_{1j_1}h_{2j_2} 
\left(d^2 f(x) \cdot e_{j_1} \cdot e_{j_2}\right) \\
&=
\sum_{j_1=1}^n \sum_{j_2=1}^n [H_f(x)]_{j_1j_2} h_{1j_1}h_{2j_2}. \\
\end{split}
$$`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Proposition -- Continue différentiabilité et différentiabilité d'ordre 2 {#continue-différentiabilité-et-différentiabilité-dordre-2 .proposition .one .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Continue différentiabilité et différentiabilité d'ordre 2}`{=latex}

Soient $U$ un ouvert de $\mathbb{R}^n$ et $f : U \to \mathbb{R}$. Si $f$
est deux fois continûment différentiable, alors $f$ est deux fois
différentiable.
:::

::: {.section}
#### Démonstration {#démonstration-2 .proof}

La fonction $f$ est différentiable à l'ordre 2 [si elle est
différentiable et que son gradient est également différentiable (p.
`\pageref*{d2mh}`{=tex})](#d2mh). Or, si $f$ est deux fois continûment
différentiable, toutes les dérivées partielles à l'ordre 1 de $\nabla f$
existent et sont elles-mêmes partiellement dérivables, de dérivées
partielles continues. Donc, le gradient de $f$ est continûment
différentiable et donc différentiable. En particulier, il est continu,
la fonction $f$ est donc continûment différentiable et donc
différentiable. `\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Proposition -- Développement limité du gradient {#dlg .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Développement limité du gradient}`{=latex}

Soient $U$ un ouvert de $\mathbb{R}^n$,
$f: U \subset \mathbb{R}^n \to \mathbb{R}$ et $x \in U$. Si la fonction
$f$ est deux fois différentiable en $x$ alors $$
\nabla f(x+h) = \nabla f(x) + H_f(x) \cdot h + \varepsilon(h) \|h\|
$$ où $\lim_{h \to 0} \varepsilon(h) = 0$.
:::

::: {.section}
#### Démonstration {#démonstration-3 .proof}

D'après la proposition ["Différentielle d'ordre 2 et matrice hessienne"
(p. `\pageref*{d2mh}`{=tex})](#d2mh), $\nabla f$ existe et est
différentiable en $x$. Par conséquent, $\nabla f$ admet un développement
limité au 1er ordre en $x$ : $$
\nabla f(x+h) = \nabla f(x) + J_{\nabla f}(x) \cdot h + \varepsilon(h) \|h\|.
$$ D'après [la définition de la matrice hessienne (p.
`\pageref*{hessienne}`{=tex})](#hessienne), $H_f(x) = J_{\nabla f}(x)$
d'où l'égalité de l'énoncé.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Théorème -- Symétrie de la différentielle d'ordre $2$ {#SD2 .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Symétrie de la différentielle d'ordre \(2\)}`{=latex}

Soient $f: U \subset \mathbb{R}^n \to \mathbb{R}$ une fonction deux fois
différentiable en un point $x$ de $U$. Pour tout couple de vecteurs
$h_1$ et $h_2$ de $\mathbb{R}^n$, on a $$
d^2 f (x) \cdot h_1 \cdot h_2 = d^2 f(x) \cdot h_2 \cdot h_1,
$$ ou de façon équivalente, la matrice hessienne de $f$ en $x$ est
symétrique $$
H_f(x)^{\top} = H_f(x),
$$ c'est-à-dire, pour tous $j_1, j_2 \in \{1,\dots,n\}$, $$
\partial^2_{j_2j_1} f(x) = \partial^2_{j_1j_2} f(x).
$$
:::

::: {.section}
#### Démonstration {#démonstration-4 .proof}

Notons au préalable que $$
\begin{split}
\Delta^2 f(x, h_1, h_2) &:= (f(x+h_2+h_1) - f(x+h_2)) - (f(x+h_1) - f(x)) \\
&= f(x+h_1+h_2) - f(x+h_1) - f(x+h_2) + f(x) \\
&= (f(x+h_2+h_1) - f(x+h_1)) - (f(x+h_2) - f(x)) \\
&= \Delta^2 f(x, h_2, h_1).
\end{split}
$$ La variation d'ordre $2$ de $f$ en $x$ est donc symétrique par
rapport à ses arguments $h_1$ et $h_2$. On peut alors exploiter [la
relation entre variation d'ordre $2$ et différentielle d'ordre 2 (p.
`\pageref*{D2d2}`{=tex})](#D2d2) en notant que `\begin{multline*}
\|d^2f(x) \cdot h_1 \cdot h_2 - d^2f(x) \cdot h_2 \cdot h_1 \|
\leq \\
\|\Delta^2f(x, h_1, h_2) - d^2f(x)\cdot h_1\cdot h_2\| + \| \Delta^2f(x, h_2, h_1) - d^2f(x)\cdot h_1\cdot h_2\|.
\end{multline*}`{=tex} On obtient pour tout $\varepsilon > 0$ et quand
$h_1$ et $h_2$ sont suffisamment petits, $$
\begin{split}
\|d^2f(x) \cdot h_1 \cdot h_2 - d^2f(x) \cdot h_2 \cdot h_1 \| 
\leq 2\varepsilon (\|h_1\|+\|h_2\|)^2.
\end{split}
$$ Si $h_1$ et $h_2$ sont arbitraires, en substituant $th_1$ à $h_1$ et
$th_2$ à $h_2$ pour un $t>0$ suffisamment petit pour que l'inégalité
ci-dessus soit valable, comme $$
d^2f(x) \cdot th_1 \cdot th_2 - d^2f(x) \cdot th_2 \cdot th_1
=t^2 \times (d^2f(x) \cdot h_1 \cdot h_2 - d^2f(x) \cdot h_2 \cdot h_1)
$$ et $$
2 \varepsilon (\|th_1\|+\|th_2\|)^2 = t^2 \times 2 \varepsilon (\|h_1\|+\|h_2\|)^2,
$$ on voit que l'inégalité est en fait valable pour des $h_1$ et $h_2$
arbitraires. On en déduit que
$d^2f(x) \cdot h_1 \cdot h_2 - d^2f(x) \cdot h_2 \cdot h_1 = 0.$`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Exercice -- Analyse vectorielle ($\mathord{\bullet}$) {#analyse-vectorielle .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Analyse vectorielle}`{=latex}

Soient $U$ un ouvert de $\mathbb{R}^3$ et $f: U \to \mathbb{R}^3$. On
note (quand les expressions ont du sens) $$
\mathrm{div} \, f(x) := \partial_1 f_1(x) + \partial_2 f_2(x) + \partial_3 f_3(x)
\; \mbox{ et } \;
\mathrm{rot} \, f(x) := \left[
\begin{array}{c}
\partial_2 f_3(x) - \partial_3 f_2(x) \\
\partial_3 f_1(x) - \partial_1 f_3(x) \\
\partial_1 f_2(x) - \partial_2 f_1(x)
\end{array}
\right].
$$ Soient $f: U \to \mathbb{R}^3$ et $g: U \to \mathbb{R}$ des fonctions
deux fois différentiables en $x \in U$. Calculer
$\mathrm{div} \, (\mathrm{rot} \, f)(x)$ et
$\mathrm{rot}\, (\nabla g)(x)$ ([Solution p.
`\pageref*{answer-analyse-vectorielle}`{=tex}](#answer-analyse-vectorielle){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Gradient unitaire ($\mathord{\bullet}$) {#gradient-unitaire .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Gradient unitaire}`{=latex}

Soient $U$ un ouvert de $\mathbb{R}^n$ et $f: U \to \mathbb{R}$ une
fonction deux fois différentiable. Montrer que si $\|\nabla f\| = 1$,
alors $H_f \cdot \nabla f = 0$. ([Solution p.
`\pageref*{answer-gradient-unitaire}`{=tex}](#answer-gradient-unitaire){.no-parenthesis}.)
:::

::: {.section}
### Proposition -- Développement limité à l'ordre $2$ {#dl2 .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Développement limité à l'ordre \(2\)}`{=latex}

Soient $U$ un ouvert de $\mathbb{R}^n$,
$f: U \subset \mathbb{R}^n \to \mathbb{R}$ et $x \in U$. Si la fonction
$f$ est deux fois différentiable en $x$ alors $$
f(x+h) = f(x) + \left<\nabla f(x), h\right> + \frac{1}{2}\left<h,  H_f(x) \cdot h\right> + \varepsilon(h) \|h\|^2
$$ où $\lim_{h\to 0} \varepsilon(h) = 0$.
:::

::: {.section}
#### Démonstration {#démonstration-5 .proof}

Il s'agit de montrer que pour tout $\varepsilon > 0$, on peut trouver un
seuil $r>0$ tel que si $\|h\| \leq r$, alors $$
\left\|
f(x+h) - f(x) - \left<\nabla f(x), h\right> - \frac{1}{2}\left<h,  H_f(x) \cdot h\right> 
\right\| 
\leq \varepsilon \|h\|^2.
$$ La fonction
$g : h \mapsto f(x+h) - f(x) - \left<\nabla f(x), h\right> - \frac{1}{2}\left<h, H_f(x) \cdot h\right> \in \mathbb{R}$
est différentiable, de gradient en $h$ $$
\nabla g(h) = \nabla f(x+h) - \nabla f(x) - \left(\frac{ H_f(x) + H_f(x)^{\top}}{2}\right) \cdot h,
$$ c'est-à-dire, comme [la matrice hessienne est symétrique (p.
`\pageref*{SD2}`{=tex})](#SD2), $$
\nabla g(h) = \nabla f(x+h) - \nabla f(x) - H_f(x) \cdot h.
$$ Compte tenu [du développement limité du gradient de $f$ en $x$ (p.
`\pageref*{dlg}`{=tex})](#dlg), il existe un seuil $r > 0$ tel que pour
tout $k$ tel que $\|k\| \leq r$, $$
\|\nabla g(k)\| = \|\nabla f(x+k) - \nabla f(x) - H_f(x) \cdot k\| \leq \varepsilon \|k\|.
$$ Par l'inégalité des accroissements finis, quand $\|h\| \leq r$, on a
donc `\begin{align*}
\|g(h)\| = \|g(h) - g(0)\| 
&\leq \sup_{k \in [0,h]} \|dg(k)\| \times \|h\| \\
&= \sup_{k \in [0,h]} \|\nabla g(k)\| \times \|h\| \\
&\leq \sup_{k \in [0,h]} \varepsilon \|k\| \times \|h\| \\
&\leq \varepsilon \|h\|^2.
\end{align*}`{=tex}`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Proposition -- Développement de Taylor d'ordre 1 avec reste intégral {#dt1 .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Développement de Taylor d'ordre 1 avec reste intégral}`{=latex}

Soient $U$ un ouvert de $\mathbb{R}^n$,
$f: U \subset \mathbb{R}^n \to \mathbb{R}$, $x \in U$ et
$h \in \mathbb{R}^n$ tel que $[x, x+h] \subset U$. Si la fonction $f$
est deux fois continûment différentiable, alors $$
f(x+h) = f(x) + \left<\nabla f(x), h\right> + \int_0^1 (h^{\top} \cdot H_f(x+th) \cdot h) \times (1-t) \, dt.
$$
:::

::: {.section}
#### Démonstration {#démonstration-6 .proof}

Définissons la fonction $\phi : [0, 1] \to \mathbb{R}$ par
$\phi(t) = f(x+th)$. Par le théorème fondamental du calcul, puis par
intégration par parties, on obtient `\begin{align*}
\phi(1) 
&= \phi(0) + \int_0^1 \phi'(t) \, dt \\
&= \phi(0) + [\phi'(t)(t-1)]_0^1 - \int_0^1 \phi''(t) \times (t-1) \, dt \\
&= \phi(0) + \phi'(0) + \int_0^1 \phi''(t) \times (1-t) \, dt
\end{align*}`{=tex} Or, on a $\phi(0) = f(x)$, $\phi(1) = f(x + h)$ ;
par la règle de dérivation en chaîne on obtient également
$\phi'(t) = df(x+th) \cdot h$ et
$\phi''(t) = d^2f(x+th) \cdot h \cdot h$. Par conséquent $$
f(x+h) = f(x) + df(x) \cdot h + \int_0^1 (d^2f(x+th)\cdot h \cdot h) \times (1-t) \, dt,
$$ ce qui est équivalent à l'équation
recherchée.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Exercice -- Accroissements finis d'ordre 2 ($\mathord{\bullet}$) {#maj2 .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Accroissements finis d'ordre 2}`{=latex}

Montrer que si $f: \mathbb{R}^n \to \mathbb{R}$ est deux fois
continûment différentiable et que la norme d'opérateur de $H_f$ est
bornée par la constante $M$ sur $\mathbb{R}^n$, alors pour tous
$x, h \in \mathbb{R}^n$, $$
\|f(x+h) - f(x) - \left<\nabla f(x), h \right> \| \leq M \frac{\|h\|^2}{2}.
$$

([Solution p.
`\pageref*{answer-maj2}`{=tex}](#answer-maj2){.no-parenthesis}.)
:::
:::

::: {.section}
Différentielle d'ordre supérieur
================================

::: {.section}
### Définition -- Tenseur d'ordre $n$ {#tenseur-dordre-n .definition .one .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Tenseur d'ordre \(n\)}`{=latex}

On appelera *tenseur d'ordre $n \in \mathbb{N}$* et de *type*
$(m_1,m_2,\dots, m_n) \in \mathbb{N}^{n}$ un élément de
$\mathbb{R}^{m_1 \times m_2 \times \dots \times m_n}$ c'est-à-dire un
réel $$
 A_{i_1 i_2 \dots i_n} \in \mathbb{R},
$$ indexé par $n$ indices $$
(i_1,  i_2, \dots , i_n) \in \{1, \dots, m_1\} \times \{1,\dots, m_2\} \times \dots \times \{1,\dots, m_n\}.
$$
:::

::: {.section}
### Remarque -- Scalaires, vecteurs, matrices {#scalaires-vecteurs-matrices .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Scalaires, vecteurs, matrices}`{=latex}

Le concept de tenseur englobe et généralise les scalaires, vecteurs et
matrices :

1.  Les scalaires sont les tenseurs d'ordre 0 (ils ne dépendent d'aucun
    indice). Il n'existe qu'un type de tenseur d'ordre $0$ : $()$
    (l'unique $0$-uplet).

2.  Les vecteurs sont les tenseurs d'ordre 1 ; le type d'un vecteur de
    $\mathbb{R}^m$ est $(m)$ (le $1$-uplet contenant $m$).

3.  Les matrices sont les tenseurs d'ordre $2$ ; le type d'une matrice
    de $\mathbb{R}^{m \times n}$ est $(m, n)$ (la paire contenant $m$ et
    $n$).

Les tenseurs d'ordre $n \geq 3$ généralisent ces constructions.
:::

::: {.section}
### Remarque -- Les tenseurs avec NumPy {#les-tenseurs-avec-numpy .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Les tenseurs avec NumPy}`{=latex}

Les tenseurs sont des tableaux $n$-dimensionnels ; ils sont donc
représentés comme des instances du type `array` de NumPy. Leur ordre est
donné par la méthode `ndim` (nombre de dimensions), leur type par la
méthode `shape`. Ainsi, avec

    >>> T0 = np.array(1.0)
    >>> T1 = np.array([1.0, 2.0, 3.0])
    >>> T2 = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    >>> T3 = np.array([[[1.0], [2.0], [3.0]], [[4.0], [5.0], [6.0]]])

on a

    >>> (T0.ndim, T1.ndim, T2.ndim, T3.ndim)
    (0, 1, 2, 3)

et

    >>> T0.shape
    ()
    >>> T1.shape
    (3,)
    >>> T2.shape
    (2, 3)
    >>> T3.shape
    (2, 3, 1)

Les coefficients d'un tenseur `T` s'obtiennent au moyen du crochet `T[]`
(méthode `__getitem__`)[^4], mais avec une indexation commençant à 0 et
non 1 comme la convention mathématique classique. Ainsi :

    >>> T1[1]
    2.0
    >>> T2[1,2]
    6.0
    >>> T3[1,2,0]
    6.0
:::

::: {.section}
### Remarque -- Applications linéaires d'ordre supérieur {#applications-linéaires-dordre-supérieur .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Applications linéaires d'ordre supérieur}`{=latex}

La raison d'être des matrices de $\mathbb{R}^{m \times n}$ est de
représenter concrètement les applications linéaires de
$\mathbb{R}^n \to \mathbb{R}^m$, dont l'espace est noté
$\mathcal{L}(\mathbb{R}^n, \mathbb{R}^m)$. Si l'on désigne par $A$ une
telle application linéaire et par $[a_{ij}]_{ij}$ la matrice associée,
$$
a_{ij} = (A \cdot e_j)_i 
\; \mbox{ et } \;
A \cdot x = \sum_i \left( \sum_{j} a_{ij} x_j \right) e_i
$$ pour tout $x \in \mathbb{R}^n$. (Par abus de notation, $e_j$ désigne
le $j$-ème vecteur de la base canonique de $\mathbb{R}^p$ quel que soit
$p$). Cette correspondance légitime l'identification fréquemment opérée
entre l'application linéaire $A$ et la matrice $[a_{ij}]_{ij}$.

Une correspondance similaire existe pour les tenseurs d'ordre supérieur
à $2$. Ainsi, à l'ordre $3$, on peut mettre en correspondance un tenseur
$(t_{ijk})_{ijk}$ de type $(m, n, p)$ et une application linéaire $T$ de
$\mathbb{R}^p$ dans l'espace des applications linéaires de
$\mathbb{R}^n$ dans $\mathbb{R}^m$, c'est-à-dire établir la
correspondance $$
(t_{ijk})_{ijk} \in \mathbb{R}^{m \times n \times p} 
\; \longleftrightarrow \;
T \in \mathcal{L}(\mathbb{R}^p, \mathcal{L}(\mathbb{R}^n, \mathbb{R}^m))
$$ de la façon suivante : $$
t_{ijk} = ((T \cdot e_k) \cdot e_j)_i
\; \mbox{ et } \;
(T \cdot x) \cdot y
= 
\sum_i \left( \sum_{j} \left(\sum_{k} t_{ijk} x_k\right) y_j\right) e_i
$$ (sous-entendu, pour tout $x\in \mathbb{R}^p$ et
$y \in \mathbb{R}^n$). Cette représentation du tenseur d'ordre $3$ par
une application linéaire est dite d'ordre supérieur car les valeurs des
applications (linéaires) en question sont elles-mêmes des applications
(linéaires).

Le processus décrit dans ce paragraphe se généralise à des tenseurs
d'ordre supérieur à $3$.
:::

::: {.section}
### Remarque -- Applications multilinéaires {#applications-multilinéaires .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Applications multilinéaires}`{=latex}

Les tenseurs vus comme des tableaux permettent de représenter d'autres
objets mathématiques, équivalents aux applications linéaires (d'ordre
supérieur). À titre d'exemple, si l'on considère les tenseurs d'ordre 2,
une matrice $[a_{ij}]_{ij} \in \mathbb{R}^{m \times n}$ correspond à une
application $\mathcal{L}(\mathbb{R}^n, \mathbb{R}^m)$ mais également à
une forme bilinéaire
$Q \in \mathcal{L}_2(\mathbb{R}^n \times \mathbb{R}^m, \mathbb{R})$,
c'est-à-dire une fonction de deux variables dans $\mathbb{R}^n$ et
$\mathbb{R}^m$, linéaire par rapport à chacune de ces variables
indépendamment et à valeurs dans $\mathbb{R}$. Cette forme bilinéaire
$B$ est donnée par $$
B(x, y) = \sum_{i=1}^m \sum_{j=1}^n a_{ij} x_i y_j.
$$ Dans le cas général, un tenseur d'ordre $n$ correspond à une forme
$n$-linéaire.
:::

::: {.section}
### Définition -- Contraction tensorielle {#contraction-tensorielle .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Contraction tensorielle}`{=latex}

Soient $A$ et $B$ des tenseurs de type respectifs
$(m_1,m_2,\dots, m_n) \in \mathbb{N}^{n}$ et
$(p_1,p_2,\dots, p_q) \in \mathbb{N}^{q}$. Si $m_n = p_1$, la
*contraction de $A$ et $B$* est le tenseur de type
$(m_1, \dots, m_{n-1}, p_2, \dots, p_q) \in \mathbb{N}^{n+q-2}$ noté
$A \cdot B$ défini par $$
(A \cdot B)_{i_1 \dots i_{n-1} i_{n+1} \dots i_{n+q}} 
= 
\sum_{i_{n}=1}^{m_n} A_{i_1 i_2 \dots i_n} B_{i_n i_{n+1}\dots i_{n+q}} .
$$
:::

::: {.section}
### Remarque -- Contractions tensorielles classiques {#contractions-tensorielles-classiques .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Contractions tensorielles classiques}`{=latex}

Pour $x, y \in \mathbb{R}^n$, on a $$
x \cdot y  = \sum_{i=1}^m x_i y_i \in \mathbb{R}.
$$ La contraction de deux vecteurs est bien défini et coïncide avec leur
produit scalaire[^5]. Si de plus $A \in \mathbb{R}^{m \times n}$ et
$B \in \mathbb{R}^{n \times p}$, $$
A\cdot x \in \mathbb{R}^m, \; (A \cdot x)_i = \sum_{j=1}^n A_{ij} x_j  
$$ $$
A \cdot B \in \mathbb{R}^{m \times p}\; \mbox{ et } \;
(A \cdot B)_{ik} = \sum_{j=1} A_{ij} B_{jk}.
$$ Autrement dit, les contractions matrices-vecteurs et
matrices-matrices coïncident avec les produits classiques de l'algèbre
linéaire.
:::

::: {.section}
### Remarque -- Contraction tensorielle avec NumPy {#contraction-tensorielle-avec-numpy .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Contraction tensorielle avec NumPy}`{=latex}

Si $A$ et $B$ sont deux tenseurs de type compatibles pour la contraction
(la dernière dimension de $A$ égale à la première dimension de $B$)
représentés par les tableaux $n$-dimensionnels `A` et `B`, **et tant que
l'ordre de $B$ est inférieur ou égal à $2$**, on peut calculer la
contraction de $A$ et $B$ au moyen de la méthode `dot`. Par exemple,
avec :

    >>> x = np.array([0.0, 1.0])
    >>> y = np.array([2.0, 4.0])
    >>> A = np.array([[1.0, 2.0], [3.0, 4.0]])
    >>> B = np.array([[5.0, 6.0], [7.0, 8.0]])
    >>> T = np.array([[[1.0, 2.0], [3.0, 4.0]], 
    ...               [[5.0, 6.0], [7.0, 8.0]]])

on obtient des contraction variées par les appels :

    >>> x.dot(y)
    4.0
    >>> A.dot(x)
    array([2., 4.])
    >>> A.dot(B)
    array([[19., 22.],
           [43., 50.]])
    >>> T.dot(A)
    array([[[ 7., 10.],
            [15., 22.]],
    <BLANKLINE>
           [[23., 34.],
            [31., 46.]]])

Par contre, si l'ordre de $B$ est $3$ ou plus, on ne pourra pas utiliser
cette méthode pour calculer la contraction tensorielle $A \cdot B$ car
son résultat diffère de la contraction tensorielle telle que nous
l'avons défini [(cf. documentation de
`numpy.dot`)](https://numpy.org/doc/stable/reference/generated/numpy.dot.html).

    >>> x.dot(T) # Not what we expect here!
    array([[3., 4.],
           [7., 8.]])

Une option consiste alors (dans ce cas particulier ou systématiquement)
à utiliser la fonction NumPy `tensordot` avec l'option `axes=1` :

    >>> def dot(A, B): # Let's define our own tensor product
    ...     return np.tensordot(A, B, axes=1)           
    >>> dot(x, T) # Problem solved!
    array([[5., 6.],
           [7., 8.]])

Pour un contrôle plus fin des opérations tensorielles, on pourra
également avoir recours [à la fonction
`numpy.einsum`](https://numpy.org/doc/stable/reference/generated/numpy.einsum.html),
une fonction qui exploite la *convention de sommation (des indices
répétés) d'Einstein*. Pour calculer
$(x \cdot T)_{jk} = \sum_{i} x_i T_{ijk}$, comme nous le souhaitons :

    >>> np.einsum("i, ijk -> jk", x, T)
    array([[5., 6.],
           [7., 8.]])

Ici le tenseur calculé par `x.dot(T)` correspond à
$S_{jk} = \sum_{i} x_i T_{jik}$ ; si c'est ce que l'on souhaite, on peut
aussi l'obtenir par :

    >>> np.einsum("i, jik -> jk", x, T)
    array([[3., 4.],
           [7., 8.]])
:::

::: {.section}
Armés de la notion d'application linéaire d'ordre supérieur, et de sa
représentation concrête comme tenseur, nous pouvons désormais
généraliser la notion de différentielle à un ordre $k \geq 2$
arbitraire, pour des fonctions à valeurs scalaires ou vectorielles de
$\mathbb{R}^m$, par induction sur l'ordre de la différentielle.
:::

::: {.section}
### Définition -- Différentielle d'ordre $k$ {#dos .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Différentielle d'ordre \(k\)}`{=latex}

Soient $f: U \subset \mathbb{R}^n \to \mathbb{R}^m$ une fonction
différentiable à l'ordre $k-1$ dans un voisinage d'un point $x$ de $U$.
On dira que $f$ est *$k$ fois différentiable en $x$* si pour tous
vecteurs $h_1, \dots, h_{k-1}$ de $\mathbb{R}^n$, la fonction
$$x \mapsto d^{k-1}f(x) \cdot h_1 \cdot h_2 \cdot \hdots \cdot h_{k-1}$$
est différentiable en $x$. La *différentielle d'ordre $k$ de $f$ en
$x$*, notée $d^k f(x)$ est définie comme l'application linéaire telle
que pour tout $h_1, \dots, h_{k-1}$ de $\mathbb{R}^n$, $$
d^k f(x) \cdot h_1 \cdot h_2 \cdot \hdots \cdot h_{k-1} := d(x\mapsto d^{k-1}f(x) \cdot h_1 \cdot h_2 \cdot \hdots \cdot h_{k-1})(x)
$$ ou de façon équivalente $$
d^k f(x) \cdot h_1 \cdot h_2 \cdot \hdots \cdot h_{k-1} \cdot h_k:= d(x\mapsto d^{k-1}f(x) \cdot h_1 \cdot h_2 \cdot \hdots \cdot h_{k-1})(x) \cdot h_k
$$
:::

::: {.section}
Les dérivées partielles d'ordre supérieur -- qui se définissent par
récurrence -- vont permettre d'expliciter les différentielles d'ordre
supérieurs comme un tenseur.
:::

::: {.section}
### Définition -- Dérivées partielles d'ordre $k$ {#dérivées-partielles-dordre-k .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Dérivées partielles d'ordre \(k\)}`{=latex}

Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}^m$ et
$x \in U$. Soient $i_1, i_2, \dots, i_k$ des indices de
$\{1,\dots, n\}$. Si $k=1$, et que $f$ est différentiable par rapport à
la $i_1$-ème variable en $x$, $$
\partial^1_{i_1} f(x) := \partial_{i_1} f(x).
$$ Dans le cas contraire, lorsque la dérivée partielle
$\partial^{k-1}_{i_{k-1} \dots i_1} f$ est définie en tout point de $U$
et est différentiable par rapport à la $i_k$-ème variable en $x$ $$
\partial^k_{i_k \dots i_1} f(x) 
:= \partial_{i_k} (\partial^{k-1}_{i_{k-1} \dots i_1} f)(x).
$$
:::

::: {.section}
#### Dérivées partielles d'ordre 3 ($\mathord{\bullet}$) {#dpo3 .exercice .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Dérivées partielles d'ordre 3}`{=latex}

Calculer les 8 dérivées partielles d'ordre $3$ de la fonction
$f: (x_1, x_2) \in \mathbb{R}^2 \mapsto x_1^4 + 4x_1^3 x_2 \in \mathbb{R}$.
([Solution p.
`\pageref*{answer-dpo3}`{=tex}](#answer-dpo3){.no-parenthesis}.)
:::

::: {.section}
### Proposition -- Calcul des dérivées partielles d'ordre $k$ {#calcul-des-dérivées-partielles-dordre-k .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Calcul des dérivées partielles d'ordre \(k\)}`{=latex}

Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}^m$ et
$x \in U$. Si $f$ est $k$ fois différentiable en $x$, alors pour tous
$i_1, i_2, \dots, i_k$ dans $\{1,\dots, n\}$, $$
\partial^k_{i_k i_2\dots i_1} f(x) 
= 
d^k f(x) \cdot e_{i_1} \cdot \hdots \cdot e_{i_k}.
$$
:::

::: {.section}
#### Démonstration {#démonstration-7 .proof}

A l'ordre $1$, $\partial^1_{i_1} f(x) = \partial_{i_1} f(x)$ ; l'égalité
$\partial_{i_1} f(x) = df(x) \cdot e_{i_1}$ a été démontrée dans le
chapitre "Calcul Différentiel I". Supposons que l'égalité soit vraie à
l'ordre $k-1$. Alors, `\begin{align*}
\partial^k_{i_k \dots i_1} f(x)
&=
\partial_{i_k} (\partial^{k-1}_{i_{k-1} \dots i_1} f)(x) \\
&=
\partial_{i_k} (x \mapsto d^{k-1}f(x) \cdot e_{i_1} \cdot \hdots \cdot e_{i_{k-1}}) \\
&=
d (x \mapsto d^{k-1} f(x) \cdot e_{i_1} \cdot \hdots \cdot e_{i_{k-1}} ) \cdot e_{i_k} \\
&=
d^k f (x) \cdot e_{i_1} \cdot \hdots \cdot e_{i_{k-1}} \cdot e_{i_k}
\end{align*}`{=tex} et l'égalité est donc également vraie à l'ordre $k$,
ce qui prouve le résultat recherché par
récurrence.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Proposition -- Différentielle d'ordre $k$ et tenseur {#différentielle-dordre-k-et-tenseur .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Différentielle d'ordre \(k\) et tenseur}`{=latex}

On a $$
d^kf(x) \in \overbrace{\mathbb{R}^n \to \mathbb{R}^n \to \cdots \to  \mathbb{R}^n}^{k \; \mathrm{termes}} \to \mathbb{R}^m,
$$ chaque application dans la chaîne étant linéaire. La différentielle
$d^k f(x)$ peut donc être représentée concrètement par un tenseur $T$
d'ordre $k+1$ et de type $(m, n, \dots, n)$ : $$
T_{ji_1 \dots i_{k}} := 
(d^k f(x) \cdot e_{i_1} \cdot \hdots \cdot e_{i_{k}}) \cdot e_{j}
=
(\partial^k_{i_{k} \dots i_1} f(x))\cdot e_{j}.
$$ Par linéarité par rapport à chacun des $h_i$, on a : `\begin{align*}
d^k f(x) \cdot h_1 \cdot \hdots \cdot h_k
&=
\sum_{j,i_1\dots, i_{k}}
\left(
\partial^k f_{i_k \dots i_{1}}(x)
h_{1i_{1}} \cdots  h_{ki_k} 
\right) e_j. \\
\end{align*}`{=tex}
:::

::: {.section}
### Définition -- Continue différentiabilité d'ordre $k$ {#continue-différentiabilité-dordre-k .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Continue différentiabilité d'ordre \(k\)}`{=latex}

Soient $U$ un ouvert de $\mathbb{R}^n$ et $f:U \to \mathbb{R}^m$. La
fonction $f$ est *$k$ fois continûment différentiable* si pour tout
$i_{k}, \dots, i_i \in \{1,\dots, n\}$,
$\partial^k_{i_k \dots i_1} f:U \to \mathbb{R}^m$ existe et est
continue.
:::

::: {.section}
### Proposition -- Continue différentiabilité et différentiabilité {#continue-différentiabilité-et-différentiabilité .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Continue différentiabilité et différentiabilité}`{=latex}

Soient $U$ un ouvert de $\mathbb{R}^n$ et $f : U \to \mathbb{R}$. Si $f$
est $k$ fois continûment différentiable, alors $f$ est $k$ fois
différentiable.
:::

::: {.section}
#### Démonstration {#démonstration-8 .proof}

Le résultat est connu à l'ordre 1 ; supposons-le établi à l'ordre $k-1$.
Si $f$ est $k$ fois continûment différentiable à l'ordre $k$, comme pour
tout $k-1$-uplet $h_1$, $h_2$, $\dots$, $h_{k-1}$, dans $\mathbb{R}^n$
on a $$
d^{k-1}f(x) \cdot h_1 \cdot h_2 \cdot \hdots \cdot h_{k-1} 
=
\sum_{j,i_1\dots, i_{k-1}}
\left(
\partial^{k-1} f_{i_{k-1} \dots i_{1}}(x)
h_{1i_{1}} \cdots  h_{k-1i_{k-1}} 
\right) e_j,
$$ la fonction
$x \mapsto d^{k-1}f(x) \cdot h_1 \cdot h_2 \cdot \hdots \cdot h_{k-1}$
est différentiable et par conséquent $f$ est $k$ fois
différentiable.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Lemme -- Stratification {#stratification .lemma .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Stratification}`{=latex}

Si $f: U \subset \mathbb{R}^n \to \mathbb{R}^m$ est une fonction $k$
fois différentiable en un point $x$ de $U$, pour tous vecteurs $h_1$,
$h_2$, $\dots$, $h_k$ de $\mathbb{R}^n$, et tout $p \in \{0,\dots, k\}$,
on a $$
d^k f(x) \cdot h_1 \cdot \hdots \cdot h_k
=
d^{k-p} (x \mapsto d^p f(x) \cdot h_1 \cdot \hdots \cdot h_{p})(x) \cdot h_{p+1} \cdot \hdots \cdot h_k.
$$
:::

::: {.section}
#### Démonstration {#démonstration-9 .proof}

Faisons l'hypothèse que le théorème est satisfait lorsque la fonction
est $j$ fois différentiable pour tout $j \leq k$. C'est de toute
évidence le cas pour $k=0, 1, 2$ ; montrons qu'il est encore vrai pour
$j=k+1$.

Notons tout d'abord que si $p=0$, le résultat est évident ; on supposera
donc dans la suite que $p \in \{1,\dots,k+1\}$. Par [définition des
différentielles d'ordre supérieur (p. `\pageref*{dos}`{=tex})](#dos), $$
d^{k+1} f(x) \cdot h_1 \cdot \hdots \cdot h_{k+1}
= d (d^k f(x) \cdot h_1 \cdot \hdots \cdot h_{k}) \cdot h_{k+1}.
$$ Or, par l'hypothèse de récurrence à l'ordre $k$, $$
d^k f(x) \cdot h_1 \cdot \hdots \cdot h_{k}
= d^{k-p} (d^p f(x) \cdot h_1 \cdot \hdots \cdot h_p) \cdot h_{p+1} \cdot \hdots \cdot h_k
$$ donc si l'on pose $g(x) = d^p f(x) \cdot h_1 \cdot \hdots \cdot h_p$
et que l'on applique l'hypothèse de récurrence à l'ordre $k+1-p$ (un
nombre compris entre $0$ et $k$), on obtient $$
\begin{split}
d^{k+1} f(x) \cdot h_1 \cdot \hdots \cdot h_{k+1}
&=
d(d^{k-p} g(x) \cdot h_{p+1} \cdot \hdots \cdot h_k)\cdot h_{k+1} \\
&=
d^{k+1-p} g(x) \cdot h_{p+1} \cdot \hdots \cdot h_k \cdot h_{k+1}
\end{split}
$$ et donc au final $$
d^{k+1} f(x) \cdot h_1 \cdot \hdots \cdot h_{k+1}
=
d^{k+1-p} (d^p f(x) \cdot h_1 \cdot \hdots \cdot h_p) \cdot h_{p+1} \cdot \hdots \cdot h_k \cdot h_{k+1}.
$$ L'hypothèse de récurrence est donc prouvée au rang $k+1$, ce qui
établit le résultat.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Proposition -- Symétrie des différentielles d'ordre supérieur {#sdos .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Symétrie des différentielles d'ordre supérieur}`{=latex}

Soit $f: U \subset \mathbb{R}^n \to \mathbb{R}^m$ une fonction $k$ fois
différentiable en un point $x$ de $U$. Pour toute permutation $\sigma$
de $\{1,\dots, n\}$ et pour tous vecteurs $h_1$, $h_2$, $\dots$, $h_k$
de $\mathbb{R}^n$, on a: $$
d^k f(x) \cdot h_{\sigma(1)} \cdot \hdots \cdot h_{\sigma(i)} \cdot \hdots \cdot h_{\sigma(k)}
=
d^k f(x) \cdot h_{1} \cdot \hdots \cdot h_{i} \cdot \hdots \cdot h_{k}.
$$
:::

::: {.section}
#### Démonstration {#démonstration-10 .proof}

Toute permutation peut être décomposée en une succession de
transpositions $\tau_{ij}$, où $\tau_{ij}(i) = j$, $\tau_{ij}(j)=i$ et
$\tau_{ij}(k) = k$ si $k$ diffère de $i$ et de $j$. Il suffit donc
d'établir le résultat quand $\sigma$ est une transposition. Nous
procédons par récurrence sur $k$. Le résultat dans le cas $k=2$ résulte
de [la symétrie de la différentielle d'ordre 2 (p.
`\pageref*{SD2}`{=tex})](#SD2). Supposons désormais le résultat établi
au rang $k \geq 2$. En utilisant [la stratification de
$d^{k+1} f(x) \cdot h_1 \cdot \hdots \cdot h_k \cdot h_{k+1}$ pour $p=1$
et $p=k$ (p. `\pageref*{stratification}`{=tex})](#stratification), on
peut établir le résultat si $i$ et $j$ appartiennent tous les deux à
$\{2,\dots, k+1\}$ ou à $\{1,\dots, k\}$. Dans l'unique cas restant, on
peut décomposer $\tau_{1(k+1)}$ en
$\tau_{2(k+1)} \circ \tau_{12} \circ \tau_{2(k+1)}$ et se ramener au cas
précédent.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Remarque -- Dérivées partielles d'ordre supérieur et multi-indices {#dérivées-partielles-dordre-supérieur-et-multi-indices .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Dérivées partielles d'ordre supérieur et multi-indices}`{=latex}

Pour compacter la notation $\partial^k_{i_k \dots i_1} f(x)$, on peut
exploiter le fait que si $f$ est $k$ fois différentiable en $x$, on a
$$\partial^k_{i_k \dots i_1} f(x) = d^k f(x) \cdot e_{i_1} \cdot \hdots \cdot e_{i_k}$$
et utiliser ensuite la symétrie de $d^k f(x)$. Peu importe l'ordre
d'apparition de $i_1$, $\dots$, $i_k$, seul le nombre de fois où un
indice donné apparaît compte. Cette remarque fonde une notation basée
sur les multi-indices
$\alpha=(\alpha_1, \dots, \alpha_n) \in \mathbb{N}^n$ où $\alpha_i$
détermine le nombre de fois où l'indice $i$ apparait. Formellement, le
symbole $\partial^{\alpha} f(x)$ désigne $f(x)$ si
$\alpha = (0, \dots, 0)$ et dans le cas contraire : $$
\partial^{(\alpha_1, \cdots, \alpha_i + 1, \cdots, \alpha_n)} f(x) = \partial_i (\partial^{\alpha} f)(x).
$$
:::

::: {.section}
### Puissance symbolique

Comme les différentielles d'ordre supérieur sont fréquemment évaluées
lorsque les termes $h_1$, $h_2$, $\dots$, sont égaux, on adoptera la
notation (purement syntaxique) suivante : $$
(\cdot \, h)^k := \overbrace{\cdot h \cdot \hdots \cdot h}^{k \; \mathrm{termes}}.
$$
:::

::: {.section}
### Théorème -- Développement limité d'ordre supérieur {#dl .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Développement limité d'ordre supérieur}`{=latex}

Soit $f: U \subset \mathbb{R}^n \to \mathbb{R}^m$ une fonction $j$ fois
différentiable au point $x \in U$. Alors $$
f(x+h) = \sum_{i=0}^{j}  \frac{d^i f(x)}{i!} (\cdot \, h)^i
+ \varepsilon(h) \times \|h\|^j.
$$ où $\varepsilon(h) \to 0$ quand $h \to 0$.
:::

::: {.section}
#### Démonstration {#démonstration-11 .proof}

Le résultat est clair pour $j=0$. Supposons le vrai à un rang $j-1$
arbitraire pour toute fonction $j-1$ fois différentiable et supposons
que $f$ est $j$ fois différentiable. Formons le reste d'ordre $j$
associé à $f$: $$
r(h) = f(x+h) - \sum_{i=0}^{j} \frac{d^i f(x)}{i!} (\cdot \, h)^i.
$$ Il nous faut montrer que $r(h)$ est de la forme
$\varepsilon(h) \times \|h\|^j$ où $\varepsilon(h) \to 0$ quand
$h \to 0$, ce qui nous allons accomplir en établissant que
$\|dr(h)\| = \varepsilon'(h) \times \|h\|^{j-1}$ avec
$\varepsilon'(h) \to 0$ quand $h \to 0$. En effet, si c'est le cas,
$dr(h) = E(h) \|h\|^{j-1}$ où l'application linéaire $E$ tend vers $0$
quand $h$ tend vers $0$, et pour tout $\varepsilon > 0$ et $h$ assez
proche de $0$ on a $\|E(h)\| \leq \varepsilon$ et donc par l'inégalité
des accroissements finis, $$
\|r(h)\| = \|r(h) - r(0)\| \leq \varepsilon \|h\|^{j-1} \times \|h\|
= \varepsilon \|h\|^j,
$$ ce qui établit que $r(h) = \varepsilon(h) \times \|h\|^j$ avec
$\varepsilon(h) \to 0$ quand $h \to 0$.

Etablissons donc ce résultat. Les termes
$d^i f(x)\cdot h_1 \cdot \hdots \cdot h_i$ sont linéaires par rapport à
chacun des $h_j$, donc pour tout vecteur $k$, compte tenu de la symétrie
de $d^i f(x)$, $$
d^i f(x) (\cdot \, (h+k))^i
= 
d^i f(x) (\cdot \, h)^i
+ i d^i f(x) (\cdot \, h)^{i-1} \cdot k
+ \varepsilon(k)\|k\|.
$$ La différentielle de $h \mapsto {d^i f(x)} (\cdot \, h)^i$ vaut donc
$id^i f(x) (\cdot \, h)^{i-1}$ et $$
d r(h) \cdot k = df(x+h) \cdot k - d f(x) \cdot k - 
d^2f(x) \cdot h\cdot k - \dots -
\frac{d^i f(x)}{(i-1)!} (\cdot \, h)^{i-1} \cdot k.
$$ Par [le lemme de stratification (p.
`\pageref*{stratification}`{=tex})](#stratification) et [la symétrie des
différentielles d'ordre supérieur (p. `\pageref*{sdos}`{=tex})](#sdos),
on obtient `\begin{multline*}
d r(h) \cdot k = df(x+h) \cdot k - d f(x) \cdot k  \\ 
- d(x \mapsto df(x) \cdot k)(x) \cdot h - \dots -
\frac{d^{i-1} (x \mapsto df(x) \cdot k)(x)}{(i-1)!} (\cdot \, h)^{i-1}.
\end{multline*}`{=tex} soit en posant $\phi(x) = df(x) \cdot k$, $$
d r(h) \cdot k = \phi(x+h) - \phi(x) - 
d \phi(x) \cdot h - \dots -
\frac{d^{i-1} \phi(x)}{(i-1)!} (\cdot h)^{i-1}.
$$ L'hypothèse de récurrence nous garantit donc que
$d r(h) \cdot k = \varepsilon(h)\|h\|^{j-1}$ à $k$ fixé, ce qui, combiné
avec la linéarité de $d r(h)$, fournit
$\|dr(h)\| = \varepsilon(h)\|h\|^{j-1}$.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Développement de Taylor avec reste intégral I {#DTRI-I}

Soit $f:[a, a+h] \to \mathbb{R}^m$ où $a \in \mathbb{R}$,
$h \in \left[0, +\infty\right[$. Si $f$ est $j+1$ fois dérivable sur
$[a,a+h]$, $$
f(a+h)  = \sum_{i=0}^n \frac{f^{(i)}(a)}{i!} h^i + \int_a^{a+h} \frac{f^{(j+1)}(t)}{j!} (a+h-t)^j \, dt.
$$
:::

::: {.section}
#### Démonstration {#démonstration-12 .proof}

A l'ordre $j=0$, la relation à prouver est $$
f(a+h) = f(a) + \int_a^{a+h} f'(t) \, dt
$$ qui n'est autre que le théorème fondamental du calcul. Si l'on
suppose la relation vérifiée à l'ordre $j$, et $f$ $j+2$ fois dérivable,
par intégration par parties, on obtient `\begin{multline*}
\int_a^{a+h} f^{(j+1)}(t) \frac{(a+h-t)^j}{j!} \, dt
= \\
\left[ f^{(j+1)}(t) \times \left( -\frac{(a+h-t)^{j+1}}{(j+1)!} \right) \right]_a^{a+h} \\
- 
\int_a^{a+h} f^{(j+2)}(t) \left( -\frac{(a+h-t)^{j+1}}{(j+1)!} \right) \, dt,
\end{multline*}`{=tex} soit `\begin{multline*}
\int_a^{a+h} f^{(j+1)}(t) \frac{(a+h-t)^j}{j!} \, dt
= \\
f^{(j+1)}(a) \times \frac{h^{j+1}}{(j+1)!}
+ 
\int_a^{a+h} f^{(j+2)}(t) \frac{(a+h-t)^{j+1}}{(j+1)!} \, dt,
\end{multline*}`{=tex} ce qui achève la preuve par
récurrence.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Développement de Taylor avec reste intégral II {#DTRI-II}

Si $f: U \subset \mathbb{R}^n \to \mathbb{R}^m$ est $j+1$ fois
différentiable et $[a, a+h] \subset U$, $$
f(a+h)  = \sum_{i=0}^{j} \frac{df^{(i)}(a)}{i!} (\cdot \, h)^i
+ \int_0^{1} \frac{df^{(j+1)}(a+th)}{j!} (\cdot \, h)^{j+1} (1-t)^j\, dt.
$$
:::

::: {.section}
#### Démonstration {#démonstration-13 .proof}

La démonstration découle directement du [développement de Taylor avec
reste intégral dans le cas d'une fonction d'une variable réelle (p.
`\pageref*{DTRI-I}`{=tex})](#DTRI-I), appliqué à la fonction
$\phi: t \in [0, 1] \mapsto f(a+th) \in \mathbb{R}^m$. Il nous suffit de
montrer que $\phi$ est $j+1$ fois différentiable et que pour tout entier
$i$ inférieur ou égal à $j+1$,
$\phi^{(i)}(t) = df^{(i)}(a+th) (\cdot \, h)^i$.

Cette relation est évidemment satisfaite pour $i=0$. Supposons qu'elle
soit vérifiée au rang $i \leq j$. La fonction $f$ étant $i+1$ fois
différentiable, la fonction
$g:x \in U \mapsto df^{(i)}(x) (\cdot \, h)^i$ est différentiable, et $$
dg(x) \cdot h = df^{(i+1)}(x) (\cdot \, h)^{i+1}.
$$ Par dérivation en chaîne, la fonction
$t \mapsto df^{(i)}(a+th) (\cdot \, h)^i$ est donc dérivable, de dérivée
$dg(a+th) \cdot h$, soit
$df^{(i+1)}(a+th) (\cdot \, h)^{i+1}.$`\hfill$\blacksquare$`{=latex}
:::
:::

::: {.section}
Annexe
======

::: {.section}
### Définition -- Variation d'ordre 1 et 2 {#variation-dordre-1-et-2 .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Variation d'ordre 1 et 2}`{=latex}

Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}^m$ et
$x \in U$. Quand cette expression est définie, on appelle *variation
d'ordre 1* de $f$ en $x$ associée à la variation $h_1$ de l'argument la
grandeur $$
\Delta f(x, h_1) := f(x+h_1) - f(x)
$$ et *variation d'ordre 2* de $f$ en $x$, associée aux variations $h_1$
et $h_2$ de l'argument, la grandeur $$
\begin{split}
\Delta^2 f(x, h_1, h_2) &:=\Delta(x \mapsto \Delta f(x, h_1))(x, h_2) \\
&\phantom{:}= \Delta f(x+h_2, h_1) - \Delta f(x, h_1).
\end{split}
$$
:::

::: {.section}
### Lemme -- Variation d'ordre 2 et matrice hessienne {#D2d2 .lemma .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Variation d'ordre 2 et matrice hessienne}`{=latex}

Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}^m$ et
$x \in U$. Si $f$ est deux fois différentiable en $x$, pour tout
$\varepsilon > 0$, il existe un $r > 0$ tel que si $\|h_1\| \leq r$ et
$\|h_2\| \leq r$, alors $$
\left\|\Delta^2f(x, h_1, h_2) - h_1^{\top} \cdot H_f(x) \cdot h_2 \right\| 
\leq \varepsilon (\|h_1\| + \|h_2\|)^2.
$$
:::

::: {.section}
#### Démonstration {#démonstration-14 .proof}

Considérons des vecteurs $h_1$ et $h_2$ tels que $x+h_1$, $x+h_2$ et
$x+h_1+h_2$ soient dans le domaine de définition de $f$. La différence
$e$ entre $\Delta^2 f(x,h_1, h_2)$ et $d^2 f(x) \cdot h_1 \cdot h_2$
vaut $$
\begin{split}
e &= (f(x+h_1+h_2) - f(x+h_2)) - (f(x+h_1) - f(x))) - d^2f(x)\cdot h_1\cdot h_2 \\
  &= (f(x+h_1+h_2) - f(x+h_1) - h_1^{\top} \cdot H_f(x) \cdot h_2 \\
  &\phantom{=} - (f(x+h_2) - f(x) - 0^{\top} \cdot H_f(x) \cdot h_2
\end{split}
$$ Par conséquent, si l'on définit $g$ par $$
g(u) = f(x+u+h_2) - f(x+u) - u^{\top} \cdot H_f(x) \cdot h_2,
$$ la différence vaut $e = g(h_1) - g(0)$. Cette différence peut être
majorée par l'inégalité des accroissements finis : $g$ est
différentiable sur le segment $[0, h_1]$ et $$
\nabla g(u) = \nabla f(x+u+h_2) - df(x+u) - H_f(x) \cdot h_2.
$$ Comme $$
\begin{split}
\nabla g(u) &= (\nabla f(x+u+h_2) - \nabla f(x) - H_f(x) \cdot (u+h_2) )\\
      &\phantom{=} - (\nabla f(x+u) - \nabla f(x) - H_f(x) \cdot u),
\end{split}
$$ par [le développement limité du gradient de $f$ (p.
`\pageref*{dlg}`{=tex})](#dlg), pour $\varepsilon > 0$ quelconque, comme
$\|u+h_2\| \leq \|h_1\| + \|h_2\|$ et $\|u\| \leq \|h_1\|$, on peut
trouver un $r > 0$ tel que si $\|h_1\| < r$ et $\|h_2\| < r,$ alors $$
\|\nabla g(u)\| \leq \frac{\varepsilon}{2} (\|h_1\| + \|h_2\|) + \frac{\varepsilon}{2} \|h_1\|.
$$ Par conséquent, l'inégalité des accroissements finis fournit
`\begin{align*}
\|e\| = \|\nabla g(u) - \nabla g(0)\| 
&\leq  \left( \frac{\varepsilon}{2} (\|h_1\| + \|h_2\|) + \frac{\varepsilon}{2} \|h_1\|\right)\|h_1\| \\ 
&\leq \varepsilon (\|h_1\| + \|h_2\|)^2.
\end{align*}`{=tex}`\hfill$\blacksquare$`{=latex}
:::
:::

::: {.section}
Exercices complémentaires
=========================

::: {.section}
Convexité
---------

Soient $U$ un ensemble ouvert et convexe de $\mathbb{R}^n$ et
$f: U \to \mathbb{R}$ une fonction deux fois différentiable.

::: {.section}
#### Question 0 ($\mathord{\bullet}$) {#c-0 .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 0}`{=latex}

Calculer le développement limité à l'ordre 2 de
$f(x+2h) - 2f(x+h) + f(x)$. ([Solution p.
`\pageref*{answer-c-0}`{=tex}](#answer-c-0){.no-parenthesis}.)
:::

::: {.section}
#### Question 1 ($\mathord{\bullet}\mathord{\bullet}$) {#c-1 .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Montrer que si $f$ est convexe, c'est-à-dire si pour tous $x, y \in U$
et $\lambda\in[0,1]$, $$
f((1-\lambda) x + \lambda y) \leq (1 - \lambda) f(x) + \lambda f(y),
$$ alors pour tout $x \in U$ et $h \in \mathbb{R}^n$, $$
d^2f(x) (\cdot h)^2 = h^{\top} \cdot H_f(x) \cdot h \geq 0.
$$

([Solution p.
`\pageref*{answer-c-1}`{=tex}](#answer-c-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#c-2 .question .three .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Montrer la réciproque de ce résultat. ([Solution p.
`\pageref*{answer-c-2}`{=tex}](#answer-c-2){.no-parenthesis}.)
:::
:::

::: {.section}
Différentiation en chaîne à l'ordre 2
-------------------------------------

Soient $U$ et $V$ des ouverts de $\mathbb{R}^n$ et de $\mathbb{R}^m$,
$f: U \to \mathbb{R}^m$ et $g : V \to \mathbb{R}$ deux applications deux
fois différentiables telles que $f(U) \subset V$.

::: {.section}
#### Question 1 ($\mathord{\bullet}$) {#cr2-1 .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Montrer que $g \circ f$ est deux fois différentiable sur $U$. ([Solution
p. `\pageref*{answer-cr2-1}`{=tex}](#answer-cr2-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#cr2-2 .question .three .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Montrer que pour tout $x \in U$, $$
H_{g \circ f}(x) = J_f(x)^{\top}\cdot H_g(f(x)) \cdot J_f(x) +  
\sum_{k=1}^m \partial_k g (f(x)) H_{f_k} (x).
$$

([Solution p.
`\pageref*{answer-cr2-2}`{=tex}](#answer-cr2-2){.no-parenthesis}.)
:::
:::

::: {.section}
Différentielle d'ordre 2 et symétrie I
--------------------------------------

On considère la fonction $f : \mathbb{R}^2 \to \mathbb{R}$ définie par
$$
    f(x_1, x_2) = \left\{\begin{array}{ll}
                \frac{x_1^2x_2^2}{x_1^2+x_2^2} & \text{si $(x_1 ,x_2) \neq (0,0)$} \\
                0 & \text{si $(x_1,x_2) = (0,0)$.}
            \end{array} \right.
$$

::: {.section}
#### Question 1 ($\mathord{\bullet}$) {#dos1-1 .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Montrer que $\partial_1 f$ et $\partial_2 f$ existent en $(0,0)$.
Calculer $\partial_1 f(0,0)$ et $\partial_2 f(0,0)$. ([Solution p.
`\pageref*{answer-dos1-1}`{=tex}](#answer-dos1-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 ($\mathord{\bullet}$) {#dos1-2 .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Montrer que $\partial_{12} f(0,0)$ et $\partial_{21} f(0,0)$ existent et
sont telles que $\partial_{12} f(0,0)=\partial_{21} f(0,0)$. ([Solution
p. `\pageref*{answer-dos1-2}`{=tex}](#answer-dos1-2){.no-parenthesis}.)
:::

::: {.section}
#### Question 3 ($\mathord{\bullet}$) {#dos1-3 .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

La fonction $f$ est-elle deux fois continûment différentiable en $0$ ?
([Solution p.
`\pageref*{answer-dos1-3}`{=tex}](#answer-dos1-3){.no-parenthesis}.)
:::

::: {.section}
#### Question 4 ($\mathord{\bullet}\mathord{\bullet}$) {#dos1-4 .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 4}`{=latex}

Est-elle deux fois différentiable en $0$ ? ([Solution p.
`\pageref*{answer-dos1-4}`{=tex}](#answer-dos1-4){.no-parenthesis}.)
:::
:::

::: {.section}
Différentielle d'ordre 2 et symétrie II
---------------------------------------

On considère la fonction $f : \mathbb{R}^2 \to \mathbb{R}$ définie par
$$
    f(x_1, x_2) = \left\{\begin{array}{ll}
                \frac{x_1x_2(x_1^2 -x_2^2)}{x_1^2+x_2^2} & \text{si $(x_1 ,x_2) \neq (0,0)$} \\
                0 & \text{si $(x_1,x_2) = (0,0)$.}
            \end{array} \right.
$$

::: {.section}
#### Question 1 ($\mathord{\bullet}\mathord{\bullet}$) {#dos2-1 .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Montrer que $f$, $\partial_1 f$ et $\partial_2 f$ sont continues sur
$\mathbb{R}^2$. ([Solution p.
`\pageref*{answer-dos2-1}`{=tex}](#answer-dos2-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 ($\mathord{\bullet}$) {#dos2-2 .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Calculer $\partial_{12}f(0,0)$ et $\partial_{21} f(0,0)$. Conclure sur
la régularité de $f$ en $(0,0)$. ([Solution p.
`\pageref*{answer-dos2-2}`{=tex}](#answer-dos2-2){.no-parenthesis}.)
:::
:::

::: {.section}
Conditions d'optimalité
-----------------------

Pour cet exercice, on rappelle le théorème spectral : toute matrice
symétrique de $\mathbb{R}^{n\times n}$ est diagonalisable dans une base
orthonormée et ses valeurs propres sont réelles. En d'autres termes,
pour tout $H\in \mathbb{R}^{n\times n}$ symétrique, il existe une base
orthonormée $(e_i)_{1\leq i\leq n}$ de $\mathbb{R}^n$ telle que pour
tout $i\in \{1,\ldots, n\}$, $H \cdot e_i = \lambda_i e_i$ avec
$(\lambda_i)_{1\leq i\leq n}$ les valeurs propres réelles de $H$.

Soient $U$ un ouvert de $\mathbb{R}^n$ et $f : U \to \mathbb{R}$ deux
fois différentiable sur $U$.

::: {.section}
#### Question 1 ($\mathord{\bullet}\mathord{\bullet}$) {#optim-1 .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Montrer que si $x^* \in U$ est un minimum local de $f$, alors pour tout
$h \in \mathbb{R}^n$, $$
df(x^*) \cdot h = 0 \quad \text{et} \quad d^2 f(x^*)(\cdot h)^2 = h^T \cdot H_f(x^*) \cdot h \geq 0.
$$

([Solution p.
`\pageref*{answer-optim-1}`{=tex}](#answer-optim-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#optim-2 .question .three .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Montrer que si, en $x^* \in U$, $f$ vérifie $df(x^*) \cdot h = 0$ et
$d^2 f(x^* ) (\cdot h)^2 > 0$ pour tout
$h \in \mathbb{R}^n\setminus \{0\}$, alors $x^*$ est un minimum local de
$f$. ([Solution p.
`\pageref*{answer-optim-2}`{=tex}](#answer-optim-2){.no-parenthesis}.)
:::

::: {.section}
#### Question 3 ($\mathord{\bullet}$) {#optim-3 .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Soit $f : (x_1, x_2) \in \mathbb{R}^2 \to x_1^3 - 12x_1 x_2 + 8x_2^3$.
Déterminer les extrema locaux de la fonction $f$. ([Solution p.
`\pageref*{answer-optim-3}`{=tex}](#answer-optim-3){.no-parenthesis}.)
:::
:::

::: {.section}
Différentiation matricielle
---------------------------

Source: [@Tao13]

```{=tex}
\newcommand{\tr}{\mathrm{tr} \,}
```
Dans cet exercice :

1.  Une fonction $F: U \subset \mathbb{R}^n \to \mathbb{R}^{m \times p}$
    à valeurs matricielles est différentiable en $x$ si chacune de ses
    composantes $F_{ij} : U \to \mathbb{R}$ est différentiable en $x$.
    La différentielle de $F$ en $x$ est alors définie par
    $[dF(x)]_{ij} = dF_{ij}(x)$.

2.  Une fonction
    $f : U \subset \mathbb{R}^{m\times n} \to \mathbb{R}^{p}$ dont
    l'argument $X$ est matriciel est différentiable en $X$ si la
    fonction $g : \pi(U) \subset \mathbb{R}^{mn} \to \mathbb{R}^p$
    caractérisée par $$
      g(x)
      :=
      f\left(\left[\begin{array}{ccc}
      X_{11} & \dots & X_{1n}  \\
      \vdots & \vdots &  \vdots \\
      X_{m1} & \dots  & X_{mn} \\
      \end{array}\right] \right)
      $$ avec $$
      x =  \pi(X) := (X_{11}, \dots, X_{1n}, \dots, X_{m1},\dots, X_{mn})
      $$ est différentiable en $x$. On définit alors pour tout
    $H \in \mathbb{R}^{m\times n}$ $$
      df(X) \cdot H = dg(x) \cdot h \; \mbox{ avec } \; x = \pi(X), \, h = \pi(H).
      $$ La construction se généralise sans difficulté aux fonctions
    dépendant de plusieurs matrices.

3.  Il est possible de combiner les deux cas précédents pour définir la
    différentielle de fonctions d'arguments et de valeur matriciels.

::: {.section}
#### Question 1 ($\mathord{\bullet}\mathord{\bullet}$) {#dm-1 .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Montrer que l'application
$\det: A \in \mathbb{R}^{n \times n} \to \det A \in \mathbb{R}$ est
différentiable en l'identité ($A = I$) et calculer cette différentielle.
([Solution p.
`\pageref*{answer-dm-1}`{=tex}](#answer-dm-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 ($\mathord{\bullet}$) {#dm-2 .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

L'identité de Weinstein--Aronszajn $\det (I + AB) = \det (I + BA)$ vaut
pour toutes les matrices carrées $A$ et $B$ de même dimension. En
déduire une identité concernant $\mathrm{tr} \,A B$ et
$\mathrm{tr} \,BA$. ([Solution p.
`\pageref*{answer-dm-2}`{=tex}](#answer-dm-2){.no-parenthesis}.)
:::

::: {.section}
#### Question 3 ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#dm-3 .question .three .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Montrer que l'application $A \mapsto A^{-1}$ est définie dans un
voisinage ouvert de l'identité, est différentiable en ce point et
calculer cette différentielle. ([Solution p.
`\pageref*{answer-dm-3}`{=tex}](#answer-dm-3){.no-parenthesis}.)
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
#### Laplacien et matrice hessienne {#answer-laplacien .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Laplacien et matrice hessienne}`{=latex}

Le laplacien de $f$ en $x$ est la somme des coefficients diagonaux --
donc la trace -- de la matrice hessienne de $f$ en $x$ : $$
\Delta f(x) = \mathrm{tr} \,H_f(x).
$$
:::

::: {.section}
#### Matrice hessienne d'un monôme {#answer-simple .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Matrice hessienne d'un monôme}`{=latex}

Le gradient de $f$ est défini en tout point de $\mathbb{R}^2$ et vaut $$
\nabla f(x_1, x_2) = 
\left[ \begin{array}{c} \partial_1 (x_1x_2^2) \\ \partial_2 (x_1 x_2^2) \end{array}\right] =
\left[ \begin{array}{c} x_2^2 \\ 2x_1x_2\end{array}\right].
$$ Toutes les dérivées partielles des composantes de $\nabla f$ sont
définies ; on a donc $$
H_f(x) = J_{\nabla f} (x_1, x_2) = 
\left[ 
\begin{array}{ll} 
\partial_1 (x_2^2) & \partial_2 (x_2^2) \\
\partial_1 (2x_1 x_2) & \partial_2 (2x_1 x_2) \\
\end{array}\right]
=
\left[ 
\begin{array}{cc} 
0 & 2x_2 \\
2x_2 & 2 x_1 \\
\end{array}\right].
$$
:::

::: {.section}
#### Matrice hessienne d'un lagrangien {#answer-lagrangien .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Matrice hessienne d'un lagrangien}`{=latex}

Le gradient de $L$ en $(x, \lambda)$ vaut $$
\nabla L(x,  \lambda) = 
\left[ 
  \begin{array}{c}
  \nabla_x (f(x) + \lambda (g(x) - c)) \\
  \partial_{\lambda} (f(x) + \lambda (g(x) - c))
  \end{array}
\right]
=
\left[ 
  \begin{array}{c}
  \nabla f(x) + \lambda \nabla g(x) \\
  g(x) - c
  \end{array}
\right],
$$ par conséquent $$
H_L(x, \lambda) = J_{{\nabla}L}(x, \lambda)
=
\left[ 
  \begin{array}{cc}
  H_f(x) + \lambda H_g(x) & \nabla g(x) \\
  \nabla g(x)^{\top} & 0
  \end{array}
\right].
$$
:::

::: {.section}
#### Matrice hessienne diagonale {#answer-hessienne-diag .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Matrice hessienne diagonale}`{=latex}

Soit $f: \mathbb{R}^2 \to \mathbb{R}$ une fonction dont la matrice
hessienne est partout définie. Si $f(x_1,x_2) = g(x_1) + h(x_2)$ où
$g:\mathbb{R}\to\mathbb{R}$ et $h:\mathbb{R}\to\mathbb{R}$ sont des
fonctions deux fois dérivables, alors $f$ est différentiable et $$
\nabla f(x_1, x_2) = 
\left[ 
\begin{array}{c}
g'(x_1) \\
h'(x_2)
\end{array}
\right].
$$ Ce gradient admet bien une matrice jacobienne et $$
H_f(x_1,x_2) = J_{\nabla f}(x_1, x_2) = 
\left[
\begin{array}{cc}
g''(x_1) & 0 \\
0 & h''(x_2)
\end{array}
\right].
$$ Cette matrice est bien diagonale pour tout
$(x_1, x_2) \in \mathbb{R}^2$. Réciproquement, si $H_f$ est diagonale,
alors $\partial^2_{12} f = \partial_1 \partial_2 f = 0$. Par le théorème
fondamental du calcul on a pour tout $(x_1,x_2) \in \mathbb{R}^2$, $$
\partial_2 f(x_1, x_2) 
= 
\partial_2 f(0,x_2) + \int_{0}^{x_1} \partial^2_{12} f(y_1,x_2) \, dy_1
=
\partial_2 f(0,x_2).
$$ La fonction $\partial_2 f(0, x_2)$ étant dérivable par rapport à
$x_2$, elle est continue par rapport à $x_2$ et à nouveau par le
théorème fondamental du calcul, on obtient $$
f(x_1, x_2) 
= f(x_1, 0) + \int_0^{x_2} \partial_2 f(x_1, y_2) \, dy_2
= f(x_1, 0) + \int_0^{x_2} \partial_2 f(0, y_2) \, dy_2.
$$ Cette fonction est de la forme $f(x_1,x_2) = g(x_1) + h(x_2)$ avec $$
g(x_1) = f(x_1,0) \; \mbox{ et } \; h(x_2) = \int_0^{x_2} \partial_2 f(0, y_2) \, dy_2.
$$ Les fonctions $f$ et $g$ sont bien deux fois dérivables.
:::

::: {.section}
#### Analyse vectorielle {#answer-analyse-vectorielle .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Analyse vectorielle}`{=latex}

Soient $f: U \to \mathbb{R}^3$ et $g: U \to \mathbb{R}$ des fonctions
deux fois différentiable en $x \in U$. On a `\begin{align*}
\mathrm{div} \, (\mathrm{rot} \, f)(x) 
&= \mathrm{div} \left[
\begin{array}{c}
\partial_2 f_3(x) - \partial_3 f_2(x) \\
\partial_3 f_1(x) - \partial_1 f_3(x) \\
\partial_1 f_2(x) - \partial_2 f_1(x)
\end{array}
\right] \\
&= \partial_1(\partial_2 f_3 - \partial_3 f_2)(x)
+ \partial_2 (\partial_3 f_1 - \partial_1 f_3)(x)
+ \partial_3 (\partial_1 f_2 - \partial_2 f_1)(x) \\
&= (\partial^2_{12} f_3 - \partial^2_{21} f_3)(x)
+ (\partial^2_{23} f_1 - \partial^2_{32} f_1)(x)
+ (\partial^2_{31} f_2 - \partial^2_{13} f_2)(x),
\end{align*}`{=tex} et donc $\mathrm{div} \, (\mathrm{rot} \, f)(x) = 0$
[par symétrie de la différentielle d'ordre 2 (p.
`\pageref*{SD2}`{=tex})](#SD2). On a également `\begin{align*}
\mathrm{rot} \, \nabla g(x) &:= \left[
\begin{array}{c}
\partial_2 (\nabla g)_3(x) - \partial_3 (\nabla g)_2(x) \\
\partial_3 (\nabla g)_1(x) - \partial_1 (\nabla g)_3(x) \\
\partial_1 (\nabla g)_2(x) - \partial_2 (\nabla g)_1(x) \\
\end{array}
\right] \\
&=
\left[
\begin{array}{c}
\partial_2 \partial_3 g(x) - \partial_3 \partial_2 g(x) \\
\partial_3 \partial_1 g(x) - \partial_1 \partial_3 g(x) \\
\partial_1 \partial_2 g(x) - \partial_2 \partial_1 g(x)
\end{array}
\right]\\
\end{align*}`{=tex} et donc -- à nouveau [par symétrie de la
différentielle d'ordre 2 (p. `\pageref*{SD2}`{=tex})](#SD2) -- on
obtient $\mathrm{rot} \, \nabla g(x)=0$
:::

::: {.section}
#### Gradient unitaire {#answer-gradient-unitaire .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Gradient unitaire}`{=latex}

Si $\|\nabla f\| = 1$, alors $$
\|\nabla f\|^2 = \left<\nabla f, \nabla f\right> = \sum_i (\partial_i f)^2 = 1
$$ et donc pour tout $j \in \{1,\dots, n\}$, $$
\partial_j \left( \sum_i \partial_i f^2 \right) =  2 \sum_i {\partial^2_{ji} f \times \partial_i f} = 
2 H_f^{\top} \cdot \nabla f = 0.
$$ Le résultat $H_f \cdot \nabla f = 0$ s'en déduit donc [par symétrie
de la différentielle d'ordre 2 (p. `\pageref*{SD2}`{=tex})](#SD2).
:::

::: {.section}
#### Accroissements finis d'ordre 2 {#answer-maj2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Accroissements finis d'ordre 2}`{=latex}

[Le développement de Taylor avec reste intégral (p.
`\pageref*{dt1}`{=tex})](#dt1) et l'inégalité triangulaire nous
fournissent `\begin{align*}
\|f(x+h) - f(x) - \left<\nabla f(x), h\right> \| &\leq
\left\| \int_0^1 (h^{\top} \cdot H_f(x+th) \cdot h) \times (1-t) \, dt \right\| \\
&\leq 
\int_0^1 \| h^{\top} \cdot H_f(x+th) \cdot h \|(1-t)\, dt.
\end{align*}`{=tex} L'inégalité de Cauchy-Schwarz et la définition de la
norme d'opérateur donnent : `\begin{align*}
\| h^{\top} \cdot H_f(x+th) \cdot h \| &\leq \|h\| \times \|H_f(x+th) \cdot h\| \\
&\leq \|h\| \times \|H_f(x+th)\| \times \|h\| \\ &\leq M \|h\|^2.
\end{align*}`{=tex} Le résultat cherché se déduit alors comme suit :
`\begin{align*}
\int_0^1 \| h^{\top} \cdot H_f(x+th) \cdot h \|(1-t)\, dt
& \leq 
\int_0^1 M\|h\|^2 (1-t) \, dt \\
&= M \|h\|^2 \int_0^1 (1-t) \, dt \\
&= M\frac{\|h\|^2}{2}.
\end{align*}`{=tex}
:::

::: {.section}
#### Dérivées partielles d'ordre 3 {#answer-dpo3 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Dérivées partielles d'ordre 3}`{=latex}

On a $$\partial_1 f(x_1, x_2) = 4 x_1^3 + 12 x_1^2 x_2 
\; \mbox{ et } \; \partial_2 f(x_1, x_2) = 4x_1^3.$$

Puis, `\begin{align*}
&\partial^2_{11} f(x_1, x_2) = 
\partial_1 (\partial_1 f)(x_1, x_2) =
\partial_1 (4 x_1^3 + 12 x_1^2 x_2) = 12 x_1^2+24 x_1 x_2,
\\
&\partial^2_{12} f(x_1, x_2) = 
\partial_1(\partial_2 f)(x_1, x_2) = \partial_1 (4x_1^3) = 12 x_1^2,
\\
&\partial^2_{21} f(x_1, x_2) = \partial_2 (\partial_1 f)(x_1, x_2) = \partial_2(4 x_1^3 + 12 x_1^2 x_2) = 12 x_1^2,
\\
&\partial^2_{22} f(x_1, x_2) = \partial_2 (\partial_2 f)(x_1, x_2) = \partial_2 (4x_1^3)  
=0.
\\
\end{align*}`{=tex}

Et enfin `\begin{align*}
&\partial^3_{111} f(x_1, x_2) = \partial_1 (\partial^2_{11} f)(x_1, x_2) = \partial_1 (12 x_1^2+24 x_1 x_2) = 24 x_1 + 24 x_2, \\
&\partial^3_{112} f(x_1, x_2) = \partial_1 (\partial^2_{12} f)(x_1, x_2) = \partial_1 (12 x_1^2)  =  24 x_1,\\
&\partial^3_{121} f(x_1, x_2) = \partial_1 (\partial^2_{21} f)(x_1, x_2) = \partial_1 (12 x_1^2)  = 24 x_1,\\
&\partial^3_{122} f(x_1, x_2) = \partial_1 (\partial^2_{22} f)(x_1, x_2) = \partial_1 (0) =0,\\
&\partial^3_{211} f(x_1, x_2) = \partial_2 (\partial^2_{11} f)(x_1, x_2) = \partial_2 (12 x_1^2+24 x_1 x_2) = 24x_1,\\
&\partial^3_{212} f(x_1, x_2) = \partial_2 (\partial^2_{12} f)(x_1, x_2) = \partial_2 (12 x_1^2) = 0, \\
&\partial^3_{221} f(x_1, x_2) = \partial_2 (\partial^2_{21} f)(x_1, x_2) = \partial_2 (12 x_1^2) = 0, \\
&\partial^3_{222} f(x_1, x_2) = \partial_2 (\partial^2_{22} f)(x_1, x_2) = \partial_2 (0) =0.\\
\end{align*}`{=tex}
:::
:::

::: {.section}
Convexité
---------

::: {.section}
#### Question 0 {#answer-c-0 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 0}`{=latex}

(Dans cette question $\varepsilon$ désigne un symbole de fonction
générique -- plutôt que $\varepsilon_1, \varepsilon_2,$ etc. -- qui tend
vers $0$ quand son argument tend vers $0$.) [Le développement limité à
l'ordre 2 de $f$ en $x$ (p. `\pageref*{dl}`{=tex})](#dl) fournit $$
f(x+h) = f(x) + df(x) \cdot h + \frac{d^2f(x)}{2} (\cdot h)^2 + \varepsilon(h) \times \|h\|^2
$$

et donc $$
f(x+2h) = f(x) + 2 df(x) \cdot h + 4 \frac{d^2f(x)}{2} (\cdot h)^2 + \varepsilon(h) \times \|h\|^2.
$$ Par conséquent, $$
f(x+2h) - 2 f(x+h) + f(x) = d^2 f(x) (\cdot h)^2 + \varepsilon(h) \times \|h\|^2.
$$
:::

::: {.section}
#### Question 1 {#answer-c-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

En considérant $y = x+2h$ et $\lambda = 1/2$, on voit que l'hypothèse de
convexité de $f$ entraîne $$
f(x+h) \leq \frac{1}{2} f(x) + \frac{1}{2} f(x+2h),
$$ soit $$f(x+2h) - 2 f(x+h) - f(x) \geq 0.$$ En utilisant le résultat
de la question précédente, on obtient
$$d^2 f(x) (\cdot h)^2 + \varepsilon(h) \times \|h\|^2 \geq 0$$ et donc,
en substituant $th$ à $h$ pour $t \in \left]0, 1\right]$, $$
t^2 d^2f(x) (\cdot h)^2 = d^2 f(x) (\cdot th)^2   
\geq  
- \varepsilon(th) \times \|th\|^2
=
- \varepsilon(th) \times t^2 \|h\|^2,
$$ soit $$
d^2f(x) (\cdot h)^2 \geq - \varepsilon(th) \times \|h\|^2
$$ et donc en faisant tendre $t$ vers $0$ à $h$ fixé,
$d^2 f(x) (\cdot h)^2 \geq 0.$
:::

::: {.section}
#### Question 2 {#answer-c-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Comme $f((1-\lambda) x + \lambda y) = f(x + \lambda (y-x))$, l'inégalité
de Taylor avec reste intégral fournit $$
\begin{split}
f((1-\lambda) x + \lambda y)
&= f(x) + df(x) \cdot \lambda (y-x) \\
&\phantom{=} + \int_0^1 d^2f(x+ t\lambda (y-x)) (\cdot \lambda(y-x))^2 (1- t) \, dt.
\end{split}
$$ L'intégrale ci-dessus étant égale à $$
\lambda \int_0^1 d^2f(x+ t\lambda (y-x)) (\cdot (y-x))^2 
\left(1- \frac{ \lambda t}{\lambda} \right) \, \ \lambda dt,
$$ par le changement de variable $t \lambda \to t$ elle est égale à $$
\lambda \int_0^{\lambda} d^2f(x+ t (y-x)) (\cdot (y-x))^2 
\left(1 - \frac{t}{\lambda} \right)\, dt.
$$ En utilisant le développement de Taylor avec reste intégral pour
$\lambda \in \left]0, 1\right]$ et $\lambda=1$, on obtient donc $$
\begin{split}
f((1-\lambda) x + \lambda y) - \lambda f(y)
&= f(x) - \lambda f(x) + df(x) \cdot \lambda (y-x) - \lambda df(x) \cdot (y-x) \\
&\phantom{=} + \lambda \int_0^{\lambda} d^2f(x+ t (y-x)) (\cdot (y-x))^2  \left(1 - \frac{t}{\lambda} \right)\, dt
\\
&\phantom{=} - \lambda \int_0^{1} d^2f(x+ t (y-x)) (\cdot (y-x))^2 
\left(1 - t \right)\, dt,
\end{split}
$$ soit $$
f((1-\lambda) x + \lambda y) - \lambda f(y)
- (1 - \lambda) f(x) 
=\lambda \int_0^1 \phi_f(t) \psi_{\lambda} (t) \, dt
$$ où $\phi_f(t) := d^2f(x+ t (y-x)) (\cdot (y-x))^2$ est positive par
hypothèse et $$
\psi_{\lambda}(t) :=
\left|
\begin{array}{cc}
t(1 - 1/\lambda) & \mbox{si } t \leq \lambda\\
(t - 1) & \mbox{sinon.}
\end{array}
\right.
$$ La fonction $\psi_{\lambda}$ étant négative, on en conclut que
$f((1-\lambda) x + \lambda y) - \lambda f(y) - f(x)$ est négative pour
tout $\lambda \in \left]0, 1\right]$ ; cette inégalité est également
trivialement satisfaite si $\lambda=0$. La fonction $f$ est donc
convexe.
:::
:::

::: {.section}
Différentiation en chaîne à l'ordre 2
-------------------------------------

::: {.section}
#### Question 1 {#answer-cr2-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Nous savons par la règle de différentiation en chaîne que $g \circ f$
est différentiable et vérifie
$d (g\circ f) (x) = dg(f(x)) \cdot df (x)$, ou encore $$
\nabla(g\circ f) (x) = \nabla f(x) \cdot [J_g(f(x))]^{\top}.
$$ Les coefficients de $J_g$ sont différentiables ainsi que les
composants de $f$, par conséquent tous les coefficients de $J_g \circ f$
sont différentiables par la règle de différentiation en chaîne. Les
composants de $\nabla f$ sont également différentiables ; les composants
de $\nabla(g\circ f)$ se déduisant de tous ces composants par des
opérations différentiables -- des produits et des sommes -- ils sont
tous différentiables. La fonction $\nabla (g \circ f)$ est donc
différentiable et $g \circ f$ est deux fois différentiable.
:::

::: {.section}
#### Question 2 {#answer-cr2-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Comme pour tout indice $i \in \{1,\dots, n\}$, $$
\partial_i (g\circ f) (x)
=
d (g \circ f)(x) \cdot e_i,
$$ la règle de différentiation en chaîne donne $$
\partial_i (g\circ f) (x) = d g(f(x)) \cdot df(x)\cdot e_i = dg(f(x)) \cdot \partial_i f(x) = \sum_{k=1}^m \partial_k g(f(x)) \partial_i f_k (x).
$$ Pour tout $j \in \{1,\dots, m\}$, on a donc `\begin{align*}
\partial^2_{ji} (g\circ f)
&= \partial_{j} (\partial_i (g\circ f)) \\
&= \partial_j \left(\sum_{k=1}^m (\partial_k g) \circ f \times \partial_i f_k \right) \\
&= \sum_{k=1}^m \partial_j ((\partial_k g) \circ f)\times \partial_i f_k + (\partial_k g) \circ f \times \partial_j (\partial_i f_k)
\end{align*}`{=tex} Comme par la règle de différentiation en chaîne $$
\partial_j ((\partial_k g) \circ f) = [d((\partial_k g) \circ f)]_j 
= [(d(\partial_k g) \circ f) \cdot df]_j 
= \sum_{\ell=1}^m \partial_{\ell} (\partial_k g) \circ f \times \partial_{j} f_{\ell},
$$ on en déduit que $$
\partial^2_{ji} (g\circ f)
= 
\sum_{k=1}^m \left[\sum_{\ell=1}^m (\partial^2_{\ell k} g)\circ f \times \partial_{j} f_{\ell} \times \partial_i f_k\right] + 
\sum_{k=1}^m (\partial_k g) \circ f \times \partial^2_{ji} f_k,
$$ soit $$
[H_{g\circ f}]_{ij} = \sum_{k=1}^m \sum_{\ell=1}^m [J_f^{\top}]_{ik} \times ([H_g]_{k\ell} \circ f) \times [J_f]_{\ell j}
+ \sum_{k=1}^m (\partial_k g) \circ f \times [H_{f_k}]_{ij},
$$ ce qui prouve pour tout $x \in U$ la relation matricielle $$
H_{g \circ f}(x) = J_f(x)^{\top}\cdot H_g(f(x)) \cdot J_f(x) +  \sum_{k=1}^m \partial_k g (f(x)) H_{f_k} (x).
$$
:::
:::

::: {.section}
Différentielle d'ordre 2 et symétrie I
--------------------------------------

::: {.section}
#### Question 1 {#answer-dos1-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Pour $h \in \mathbb{R}$, on remarque que $f(h,0) = f(0,h) = 0$. En
particulier,

$$ 
\lim_{h\to 0} \frac{f(h,0) - f(0,0)}{h} = 0.
$$

Par définition de la dérivée partielle, cette limite est égale à
$\partial_1 f(0,0)$. On montre de même que $\partial_2 f$ existe en
$(0,0)$, et $\partial_1 f(0,0) = \partial_2 f(0,0) = 0$.
:::

::: {.section}
#### Question 2 {#answer-dos1-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Le calcul de $\partial_1 f$ pour $(x_1, x_2) \neq (0,0)$ donne $$
\partial_1 f(x_1, x_2) = \left\{\begin{array}{ll}
                \frac{2x_1 x_2^4}{\left(x_1^2+ x_2^2\right)^2} & \text{si $(x_1 ,x_2) \neq (0,0)$} \\
                0 & \text{si $(x_1,x_2) = (0,0)$.}
            \end{array} \right.
$$ Comme $\partial_1 f(0, h) = 0$, le raisonnement précédent s'applique,
et $\partial_{21} f(0,0) = 0$. Et de même, $$
\partial_2 f(x_1, x_2) = \left\{\begin{array}{ll}
                \frac{2x_1^4 x_2}{\left(x_1^2+ x_2^2\right)^2} & \text{si $(x_1 ,x_2) \neq (0,0)$} \\
                0 & \text{si $(x_1,x_2) = (0,0)$.}
            \end{array} \right.
$$ donc $\partial_2 f(h, 0) = 0$ et donc $\partial_{12} f(0,0) = 0$.
:::

::: {.section}
#### Question 3 {#answer-dos1-3 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Pour $(x_1, x_2) \neq (0,0)$, le calcul de $\partial_{21}f$ donne\
$$
\partial_{21} f (x_1, x_2) = \left(\frac{2x_1x_2}{x_1^2+x_2^2}\right)^3.
$$ La fonction $\partial_{21} f$ n'est pas continue en $(0,0)$. En
effet, pour $h \in \mathbb{R}$, $\partial_{21} f(h, h) = 1$, donc en
particulier $$
\partial_{21} f(h, h)\xrightarrow[h \to 0]{} 1 \neq \partial_{21} f(0,0).
$$ Par conséquent, $f$ n'est pas deux fois continûment différentiable en
$(0,0)$.
:::

::: {.section}
#### Question 4 {#answer-dos1-4 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 4}`{=latex}

Supposons par l'absurde que $f$ est deux fois différentiable en $(0,0)$.
Alors $\partial_1 f$ est différentiable en $(0,0)$. En ce point, son
développement limité s'écrit, avec $h = (h_1, h_2)$, $$
            \partial_1 f(h_1, h_2) = \partial_1 f(0,0) + h_1\partial_{11} f(0,0) + h_2 \partial_{21} f(0,0) + \varepsilon(h) \times \| h \|, 
$$ avec $\varepsilon(h) \to 0$ quand $h \to 0$. D'après la question 2,
$\partial_{21} f(0,0)=0$ ; on montre de la même manière que
$\partial_{11} f(0,0) = 0$. Le développement limité de $\partial_1 f$ en
$(0,0)$ s'écrit alors simplement
$\partial_1 f(h) = \varepsilon (h) \|h\|$. Ainsi, $\varepsilon(h)$
vérifie $$
\varepsilon(h) = \frac{\partial_1 f(h_1, h_2)}{\|h\|} = \frac{2h_1 h_2^4}{(h_1^2 + h_2^2)^{5/2}}. 
$$ Avec $h = (h_1, h_1)$, $\varepsilon$ vérifie
$\varepsilon(h) = 1/2^{\frac{3}{2}} \neq 0$, ce qui est absurde puisque
$\varepsilon(h) \to 0$ lorsque $h \to 0$. La fonction $f$ n'est donc pas
deux fois différentiable en $(0,0)$, même si
$\partial_{21} f(0,0) = \partial_{12}f(0,0)$.
:::
:::

::: {.section}
Différentielle d'ordre 2 et symétrie II
---------------------------------------

::: {.section}
#### Question 1 {#answer-dos2-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

D'après l'inégalité de Young,
$\lvert x_1 x_2 \rvert \leq (x_1^2 + x_2^2)/2$. Donc pour
$(x_1, x_2) \neq (0,0)$, $$
\lvert f(x_1, x_2) \rvert \leq \frac{1}{2} \lvert x_1^2 - x_2^2 \rvert.
$$ Ainsi, $f(x_1, x_2) \to 0 = f(0,0)$ lorsque $(x_1, x_2) \to (0,0)$.
La fonction $f$ est donc continue en $(0,0)$. De plus, pour
$(x_1, x_2) \neq 0$, $\partial_1 f$ vérifie $$
\partial_1 f(x_1, x_2) = \frac{x_2(x_1^4 + 4x_1^2x_2^2 - x_2^4)}{(x_1^2 + x_2^2)^2}.
$$\
La fonction $\partial_1 f$ est donc continue en $(x_1, x_2) \neq (0,0)$.
Par ailleurs, $$
\lvert \partial_1 f(x_1, x_2) \rvert \leq \lvert x_2 \rvert \frac{ x_1^4 + 4x_1^2 x_2^2 + x_2^4 }{ (x_1^2 + x_2^2)^2} \leq 2 \lvert x_2 \rvert.
$$ Donc $\partial_1 f(x_1,x_2) \to 0$ quand $(x_1,x_2) \to (0,0)$.
$\partial_1f$ est bien continue en $(0,0)$, et $\partial_1 f(0,0) = 0$.
On montre de la même manière que $\partial_2 f$ est continue sur
$\mathbb{R}^2$, avec $\partial_2 f(0,0) = 0$, et $$
\partial_2 f(x_1, x_2) = \frac{-x_1(- x_1^4 + 4x_1^2 x_2^2 + x_2^4)}{(x_1^2 + x_2^2)^2}
$$
:::

::: {.section}
#### Question 2 {#answer-dos2-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Pour $h_2 \in \mathbb{R}$, et d'après l'expression de $\partial_1 f$
précédemment calculée, $\partial_1 f(0,h_2) = -h_2$, donc en particulier

$$
\lim_{h_2\to 0} \frac{\partial_1 f(0,h_2) - \partial_1 f(0,0)}{h_2} = -1.
$$

Par définition de la dérivée partielle, cette limite est égale à
$\partial_{21} f(0,0)$. De la même manière, $\partial_2 f(h_1,0) = h_1$,
donc

$$
\partial_{12}f(0,0) = \lim_{h_1 \to 0}\frac{\partial_2 f(h_1,0) - \partial_2 f(0,0)}{h_1} = 1.
$$

Ainsi, $\partial_{21} f(0,0) = -1$ et $\partial_{12} f(0,0) = 1$. Si $f$
était deux fois différentiable en $(0,0)$, la différentielle d'ordre
deux de $f$ en ce point serait symétrique, ce qui n'est pas le cas ici.
La fonction $f$ n'est donc pas deux fois différentiable en $(0,0)$.
:::
:::

::: {.section}
Conditions d'optimalité
-----------------------

::: {.section}
#### Question 1 {#answer-optim-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Soit $h \in \mathbb{R}^n$. La fonction $f$ étant différentiable en
$x^*$, son développement limité à l'ordre un en $x^*$ s'écrit $$ 
f(x^* + th) = f(x^*) + df(x^*) \cdot th + \varepsilon_1(t) \|th \|.
$$ avec $\varepsilon_1 (t) \to 0$ quand $t \to 0$. La fonction $f$ admet
un minimum local en $x^*$, donc il existe un voisinage ouvert $V$ de
$x^*$ tel que pour $x \in V$, $f(x) \geq f(x^*)$. De plus, pour $t > 0$
suffisamment petit, $x^* + th \in V$, d'où $$ 
f(x^* + th) - f(x^*) = df(x^*) \cdot th + \varepsilon_1(t)\|th \| \geq 0.
$$ En divisant par $t$ et en faisant tendre $t > 0$ vers $0$, on obtient
$df(x^*) \cdot h \geq 0$. Cette inégalité est aussi vérifiée par $-h$,
et comme $df(x^*) \cdot -h = - df(x^*) \cdot h$, on obtient aussi que
$-df(x^*) \cdot h \geq 0$, et donc $df(x^*) \cdot h = 0$.

Le développement limité à l'ordre deux de $f$ en $x^*$ s'écrit $$ 
f(x^* + th) = f(x^*) + df(x^*) \cdot th + \frac{1}{2} d^2 f(x^*) (\cdot th)^2 + \varepsilon_2(t) \| th \|^2,
$$ avec $\varepsilon_2 (t) \to 0$ quand $t \to 0$. D'après ce qui
précède, $df(x^*)\cdot th = 0$, et donc pour $t$ suffisamment petit $$
f(x^* + th) - f(x^*) = \frac{1}{2} d^2 f(x^*) (\cdot th)^2 + \varepsilon_2(t) \| t \| \geq 0.
$$ Diviser par $t^2$ et faire tendre $t\to 0$ donne bien
$d^2 f(x^*)(\cdot h)^2 \geq 0$.
:::

::: {.section}
#### Question 2 {#answer-optim-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Pour $h\in \mathbb{R}^n$, le développement limité à l'ordre deux de $f$
en $x^*$ s'écrit `\begin{align*}
f(x^* + h) - f(x^*) &= df(x^*)\cdot h +  \frac{1}{2} d^2f(x^*)(\cdot h)^2  + \varepsilon_2(h) \| h \|^2 \\
 &= \frac{1}{2} d^2f(x^*)(\cdot h)^2  + \varepsilon_2(h) \| h \|^2 .
\end{align*}`{=tex} Par hypothèse,
$d^2 f(x^*) (\cdot h)^2 = h^T \cdot H_f (x^*) \cdot h >0$ pour tout
$h\neq 0$. Or, la matrice hessienne $H_f (x^*)$ est symétrique, donc par
le théorème spectral, ses valeurs propres sont réelles et il existe une
base orthonormée $(e_i)$ de vecteurs propres de $H_f (x^*)$. Tout
$h\in \mathbb{R}^n$ se décompose donc sous la forme
$h=\sum_{i=1}^n h_i e_i$ et $H\cdot h=\sum_{i=1}^n \lambda_ih_i e_i$. On
a donc $$
h^T \cdot H_f (x^*) \cdot h = \sum_{i=1}^n h_i^2 \lambda_i  \ .
$$ En appliquant cette formule au vecteurs $e_i$ de la base, on déduit
que toutes les valeurs propres $\lambda_i$ doivent être strictement
positives. De plus, en notant $\lambda_m>0$ la plus petite valeur
propre, $h^T \cdot H_f (x^*) \cdot h \geq \lambda_m \| h \|^2$. Or,
comme $\varepsilon_2(h) \to 0$ quand $h \to 0$, il existe $\eta > 0$ tel
que pour $\|h\| \leq \eta$,
$|\varepsilon_2 (h)|\|h\|^2 \leq \lambda_m\|h\|^2/4$. Ainsi, pour
$\|h\| \leq \eta$,
$f(x^* + h) - f(x^*) \geq \lambda_1 \times \|h\|^2 /4 \geq 0$. La
fonction $f$ admet donc bien un minimum local en $x^*$.
:::

::: {.section}
#### Question 3 {#answer-optim-3 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Tout d'abord notons que $x^*$ est un maximum local de $f$ si et
seulement si $x^*$ est un minimum local de $-f$. On en déduit donc que
si $x^*$ est un maximum de $f$ alors nécessairement $$
df(x^*) \cdot h = 0 \quad \text{et} \quad d^2 f(x^*)(\cdot h)^2 = h^T \cdot H_f(x^*) \cdot h \leq 0
$$ pour tout $h \in \mathbb{R}^n$, et que réciproquement, si
$df(x^*) \cdot h = 0$ et $d^2 f(x^* ) (\cdot h)^2 < 0$ pour tout
$h \in \mathbb{R}^n\setminus \{0\}$, alors $x^*$ est un maximum local de
$f$.

La fonction $f$ est deux fois différentiable ; son gradient s'écrit $$
\nabla f(x_1, x_2) = 
\left[
\begin{array}{c}
    3x_1^2 - 12x_2 \\
    -12x_1 + 24x_2^2
\end{array}
\right].
$$

Il s'annule si et seulement si $(x_1, x_2) = (0,0)$ ou $(2,1)$. Le
calcul de la matrice hessienne donne

$$
H_f(x_1, x_2) = 
\left[
\begin{array}{cc}
    6x_1 & -12 \\
    -12 & 48x_2 
\end{array}
\right].
$$ Son évaluation en $(0,0)$ donne $$ 
H_f(0,0) = 
\left[
\begin{array}{cc}
    0 & -12 \\
    -12 & 0 
\end{array}
\right] .
$$ Pour $h=(1,1)$, on a $h^\top H_f(0,0) h = -24$ et pour $h=(-1,1)$, on
a $h^\top H_f(0,0) h = 24$. Donc aucune des deux conditions nécessaires
d'extrema n'est vérifiée et le point $(0,0)$ n'est donc ni un minimum,
ni un maximum local de $f$. En $(2,1)$, $$
H_f(2,1) = 
\left[
\begin{array}{cc}
    12 & -12 \\
    -12 & 48 
\end{array}
\right].
$$ La trace et le déterminant de cette matrice, étant respectivement la
somme et le produit des valeurs propres, sont positifs donc $H_f(2,1)$ a
ses valeurs propres strictement positives. Comme vu à la question
précédente, en appliquant le théorème spectral, on a pour tout
$h\in \mathbb{R}^2\setminus \{0\}$,\
$$
h^T \cdot H_f (2,1) \cdot h = h_1^2 \lambda_1 + h_2^2 \lambda_2 > 0 \ .
$$ La condition suffisante de la Question 2 est vérifiée donc $(2,1)$
est un minimum local de la fonction $f$.
:::
:::

::: {.section}
Différentiation matricielle
---------------------------

::: {.section}
#### Question 1 {#answer-dm-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Soit $H \in \mathbb{R}^{n\times n}$, telle que $$
H = 
\left[
\begin{array}{cccc}
h_{11} & h_{12} & \hdots & h_{1n} \\
h_{21} & h_{22} & \hdots & h_{2n} \\
\vdots & \vdots & \vdots & \vdots \\
h_{n1} & h_{n2} & \hdots & h_{nn} \\
\end{array} 
\right].
$$ En développant le déterminant selon la première colonne, on constate
que $$
\begin{split}
\det (I+H) &= 
\left|
\begin{array}{cccc}
1+h_{11} & h_{12} & \hdots & h_{1n} \\
h_{21} & 1+h_{22} & \hdots & h_{2n} \\
\vdots & \vdots & \vdots & \vdots \\
h_{n1} & h_{n2} & \hdots & 1+h_{nn} \\
\end{array} 
\right| \\
&=(1 + h_{11}) 
\left| \begin{array}{ccc}
1+h_{22} & \hdots & h_{2n} \\
\vdots & \vdots & \vdots \\
h_{n2} & \hdots & 1+h_{nn} \\
\end{array} \right| 
+ \varepsilon(\|H\|), \\
\end{split}
$$ une relation dont on tire par récurrence que $$
\begin{split}
\det (I+H) 
&= \prod_{i = 1}^n (1 + h_{ii}) + \varepsilon(\|H\|)
=\det I + \sum_{i=1}^n h_{ii} + \varepsilon(\|H\|) \\
&= \det I + \mathrm{tr} \,H + \varepsilon(\|H\|).
\end{split}
$$ La différentiel du déterminant existe donc en l'identité et
$d\det(I) \cdot H = \mathrm{tr} \,H$.
:::

::: {.section}
#### Question 2 {#answer-dm-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Pour tout réel $\varepsilon$ et $A$, $B$ matrices carrées de même
taille, on a $$
\det (I + \varepsilon A B) = \det (I + \varepsilon B A).
$$ Les deux membres de cette équations sont dérivables par rapport à
$\varepsilon$ en $0$ par la règle de différentiation en chaîne et
l'égalité de ces dérivées fournit $$
\mathrm{tr} \,A B = \mathrm{tr} \,B A.
$$
:::

::: {.section}
#### Question 3 {#answer-dm-3 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Le déterminant étant une application continue, si
$A \in \mathbb{R}^{n\times n}$ est suffisamment proche de l'identité --
dont le déterminant vaut $1$ -- son déterminant est positif ; la matrice
$A$ est alors inversible.

Quand la matrice $A \in \mathbb{R}^{n \times n}$ est suffisamment proche
de l'identité pour être inversible, la formule de Cramer établit $$
A^{-1} = \frac{1}{\det A}  \mathrm{co}(A)^t.
$$ Chaque coefficient de $\mathrm{co}(A)^t$ (la transposée de la
comatrice de $A$) est une fonction polynomiale des coefficients $a_{ij}$
de $A$ ; chaque coefficient de $\mathrm{co}(A)^t$ est donc une fonction
continûment différentiable des coefficients de $A$ et donc
différentiable en $A=I$. Par la règle du produit, chaque coefficient de
$A^{-1}$ est donc différentiable en $A=I$ ; l'application
$A \mapsto A^{-1}$ est donc différentiable en $A=I$.

Notons $\mathrm{inv}(A) = A^{-1}$ ; comme
$\mathrm{inv}(I+H) = I + d \, \mathrm{inv}(I) \cdot H + \varepsilon(\|H\|),$
l'identité $(I+ H) (I + H)^{-1} = I$ fournit : $$
(I+H)(I + d\,\mathrm{inv}(I) \cdot H + \varepsilon(\|H\|)) 
= I + H + d\,\mathrm{inv}(I) \cdot H + \varepsilon(\|H\|)
= I,
$$ et donc $$d \,\mathrm{inv} (I) \cdot H= - H.$$
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

[^2]: L'étude des démonstrations du cours peut toutefois contribuer à
    votre apprentissage, au même titre que la résolution d'exercices.

[^3]: la notation "générique" serait sinon $d^2f(x) (h_1)$ et
    $d^2f(x)(h_1)(h_2)$, voire $(d^2f(x)) (h_1)$ et
    $((d^2f(x))(h_1))(h_2)$ si l'on souhaitait être tout à fait
    explicite.

[^4]: La notation `T2[(1,2)]` ($n$-uplet explicite) est équivalente à
    `T2[1,2]` ($n$-uplet implicite). Cette remarque est utile pour
    accéder au contenu des tenseurs d'ordre 0, car la notation `T0[]`
    n'est pas acceptée :

        >>> T0[()]
        1.0
        >>> T0[]
        Traceback (most recent call last):
        ...
        SyntaxError: invalid syntax

[^5]: Souvenons-nous à l'inverse que si l'on interprête "$\cdot$" comme
    un produit matriciel et que l'on représente implicitement $x$ et $y$
    comme deux vecteurs-colonnes de $\mathbb{R}^{n \times 1}$,
    l'expression $x \cdot y$ n'a pas de sens ; il faut alors considérer
    $x^{\top} \cdot y$ à la place, puis assimiler ensuite le résultat --
    qui est une matrice $1 \times 1$ -- à un nombre réel. Les
    conventions du calcul tensoriel ont donc ici une action
    simplificatrice.
