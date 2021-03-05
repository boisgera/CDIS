---
author:
- 'STEP, MINES ParisTech'
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

```{=tex}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}
\newcommand{\tr}{\operatorname{tr}}
```
```{=tex}
\newcommand{\zero}{$\mathord{\boldsymbol{\circ}}$}
\newcommand{\one}{$\mathord{\bullet}$}
\newcommand{\two}{$\mathord{\bullet}\mathord{\bullet}$}
\newcommand{\three}{$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$}
\newcommand{\four}{$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$}
```
::: {.section}
#### Question 1 (réponses multiples)

Soit $f: (x_1, x_2) \in \mathbb{R}^2 \mapsto x_1 x_2 \in \mathbb{R}$. On
a

-   [ ] A:
    $$H_f(x) = \left[\begin{array}{cc} 0 & 1 \\ 1 & 0 \end{array} \right]$$

-   [ ] B: Si $h_1 = (h_{11}, h_{12}) \in \mathbb{R}^2$ et
    $h_2 = (h_{21}, h_{22}) \in \mathbb{R}^2$,
    $$d^2 f(x_1, x_2) \cdot h_1 \cdot h_2 = h_{11}h_{22} - h_{21}h_{12}$$

-   [ ] C: Pour tout $x \in \mathbb{R}^2$
    $$\nabla f(x+h) = \nabla f(x) + \frac{1}{2} \left< h, H_f(x) \cdot h\right> + \varepsilon(h) \|h\|^2$$
    où $\varepsilon(h) \to 0$ quand $h \to 0$.
:::

::: {.section}
#### Question 2

Si $f: \mathbb{R}^n \to \mathbb{R}$ est deux fois différentiable en
$x \in U$ et que $df(x) \cdot h \cdot h$ est connu pour tout
$h \in \mathbb{R}^n$, peut-on déterminer $df(x) \cdot h_1 \cdot h_2$
pour tout $h_1, h_2 \in \mathbb{R}^n$ ?

-   [ ] A : oui,

-   [ ] B : non.
:::

::: {.section}
#### Question 3

Si $f: \mathbb{R}^3 \to \mathbb{R}^3$ est deux fois différentiable,
combien y'a-t'il au plus de coefficients différents dans le tenseur
représentant $d^2f(x)$ ?

-   [ ] A : 9,

-   [ ] B : 18,

-   [ ] C : 27.
:::

::: {.section}
#### Question 4 (réponses multiples)

Soient $f: \mathbb{R}^2 \to \mathbb{R}$ et $a \in \mathbb{R}^2$ tels que
$\partial_{12}f(a) = \partial_{21}f(a)$. Alors $f$ est

-   [ ] deux fois continûment différentiable en $a$,

-   [ ] deux fois différentiable en $a$,

-   [ ] différentiable en $a$,

-   [ ] continue en $a$.
:::

::: {.section}
#### Question 5

La différentielle $d^3f$ d'ordre $3$ d'une fonction
$f: U \subset \mathbb{R}^2\to \mathbb{R}^3$

-   [ ] A : associe linéairement à tout vecteur $h$ de $\mathbb{R}^2$
    une application qui associe linéairement à tout vecteur $k$ de
    $\mathbb{R}^2$ une application qui associe linéairement à tout
    vecteur $p$ de $\mathbb{R}^2$ un vecteur de $\mathbb{R}^3$.

-   [ ] B : associe linéairement à tout point $x \in U$ une application
    qui associe linéairement à tout vecteur $h$ de $\mathbb{R}^2$ une
    application qui associe linéairement à tout vecteur $k$ de
    $\mathbb{R}^2$ un vecteur de $\mathbb{R}^3$.

-   [ ] C : associe à tout point $x \in U$ une application qui associe
    linéairement à tout vecteur $h$ de $\mathbb{R}^2$ une application
    qui associe linéairement à tout vecteur $k$ de $\mathbb{R}^2$ une
    application qui associe linéairement à tout vecteur $p$ de
    $\mathbb{R}^2$ un vecteur de $\mathbb{R}^3$.
:::

::: {.section}
#### Question 6

Si $f: \mathbb{R}^2 \to \mathbb{R}^4$ est trois fois différentiable,
quel est le type du tenseur représentant $d^3f(x)$ ?

-   [ ] A : (4, 2, 2, 2),

-   [ ] B : (3, 4, 2),

-   [ ] C : (4, 2, 1).
:::

::: {.section}
#### Question 7 (réponses multiples)

Si $f$ est $k$ fois différentiable en $x$,

-   [ ] A : les dérivées partielles d'ordre $k$ de $f$ en $x$ existent,

-   [ ] B : on a
    $\partial^k_{i_{k} \dots i_1} f(x) = d^k f(x) \cdot e_{i_1} \cdot \hdots \cdot e_{i_{k}},$

-   [ ] C : les dérivées partielles de d'ordre $k$ de $f$ en $x$
    déterminent $d^k f(x)$ de façon unique.
:::
