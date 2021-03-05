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
#### Question 1

Déterminer l'aire des pavés suivants du plan étendu :

  Ensemble de $[-\infty,+\infty]^2$                    Aire (mesure de Lebesgue)
  ---------------------------------------------------- ------------------------------------------
  $[0, 1] \times \left]-1, 1\right[$                   ........................................
  $\mathbb{R}^2$                                       ........................................
  $\{+\infty\} \times \left[-\infty, +\infty\right]$   ........................................
:::

::: {.section}
### Question 2 (réponse multiple)

Soit $D = \{(x,y) \in \mathbb{R}^2 \; | \; x = y\}$ la diagonale
principale de $\mathbb{R}^2$. Alors

-   [ ] A: pour tout $r>0$, $D \cap [-r, r]^2$ est négligeable,

-   [ ] B: l'ensemble $D$ est négligeable,

-   [ ] C: l'aire de l'ensemble $D$ est nulle.

::: {.section}
#### Question 3 (réponse multiple)

Si $f: \mathbb{R}^2 \to \mathbb{R}$ est mesurable et que $$
\int_{-\infty}^{+\infty} \left[\int_{-\infty}^{+\infty} f(x,y) \, dx\right] \, dy
$$ est bien définie, alors

-   [ ] A: l'intégrale $\int_{-\infty}^{+\infty} f(x,y) \, dx$ est
    nécessairement définie pour tout $y \in \mathbb{R}$,

-   [ ] B: l'intégrale $\int_{\mathbb{R}^2} f(x, y) \, dxdy$ est bien
    définie,

-   [ ] C: l'intégrale
    $\int_{-\infty}^{+\infty} \left[\int_{-\infty}^{+\infty} f(x,y) \, dy\right] \, dx$
    est bien définie,

-   [ ] D: si
    $\int_{-\infty}^{+\infty} \left[\int_{-\infty}^{+\infty} f(x,y) \, dy\right] \, dx$
    est également bien définie, alors les deux intégrales sont égales,
:::

::: {.section}
#### Question 4 (réponse multiple)

Soient $f: \mathbb{R}\to \left[0, +\infty \right[$ et
$g: \mathbb{R}\to \left[0, +\infty \right[$ deux fonctions intégrables.
Alors,

-   [ ] A: la fonction $(x, y) \in \mathbb{R}^2 \mapsto f(x) g(y)$ est
    mesurable,

-   [ ] B: la fonction $(x, y) \in \mathbb{R}^2 \mapsto f(x) g(y)$ est
    intégrable,

-   [ ] C: on a
    $$\int_{\mathbb{R}^2} f(x) g(y) \, dxdy = \left(\int_{-\infty}^{+\infty} f(x) \, dx\right)\left(\int_{-\infty}^{+\infty} g(y) dy\right).$$
:::

::: {.section}
#### Question 5 (réponse multiple)

Soient $f: \mathbb{R}^2 \to \mathbb{R}$. L'intégrale $$
  \int_{\mathbb{R}^2} f(x, y-x) \, dxdy
  $$

-   [ ] A: est définie si $f$ est mesurable et positive,

-   [ ] B: est égale à $\int_{\mathbb{R}^2} f(x, y) \, dxdy$ si $f$ est
    intégrable.
:::
:::
