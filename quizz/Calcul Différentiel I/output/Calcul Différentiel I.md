---
author:
- 'STEP, MINES ParisTech'
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
title: Calcul Différentiel I
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

Déterminer le gradient et la matrice jacobienne de la fonction
$(x_1, x_2) \in \mathbb{R}^2 \mapsto x_1x_2 \in \mathbb{R}$.
:::

::: {.section}
#### Question 2

Déterminer en tout point la matrice jacobienne de l'application
$(x_1, x_2, x_3) \in \mathbb{R}^3 \mapsto (x_2 - x_1^2, x_3 - x_2^2) \in \mathbb{R}^2.$
:::

::: {.section}
#### Question 3

Soit $f: \mathbb{R}\to \mathbb{R}^m$ une fonction dérivable. Dans
l'expression $df(x) \cdot h$, à quels ensembles appartiennent $df(x)$ et
$h$ ? Que vaut l'expression en fonction de $f'(x)$ ?
:::

::: {.section}
#### Question 4

Soit $p: \mathbb{R}^2 \to \left]0, +\infty\right[$ une fonction
différentiable. Calculer le gradient de
$x \in \mathbb{R}^2 \mapsto \ln p(x) \in \mathbb{R}$ en fonction du
gradient de $p$.
:::

::: {.section}
#### Question 5

Soit $f: \mathbb{R}^n \to \mathbb{R}^n$ une fonction différentiable,
bijective et dont l'inverse $g:=f^{-1}$ est également différentiable.
Déterminer l'expression de la différentielle de $g$ en
$y \in \mathbb{R}^n$ en fonction de la différentielle de $f$.
:::

::: {.section}
#### Question 6

En exploitant la loi des gaz parfaits $PV = nRT$, donner une expression
de $dT$ en fonction de $dP$ et $dV$ ($n$ et $R$ sont des constantes).
:::

::: {.section}
#### Question 7

Soit $f:\mathbb{R}^2 \to \mathbb{R}$ une fonction telle que $f(0,0) = 0$
et $\nabla f(x_1, x_2) = (2x_1+x_2, x_1)$ en tout point. Déterminer la
valeur de $f(x_1, x_2)$ en tout point.
:::

::: {.section}
#### Question 8

Soit $f : \mathbb{R}^2 \to \mathbb{R}^m$ une fonction différentiable et
vérifiant $\|df(x_1, x_2)\| \leq 1$ quand $|x_1| \geq 1$ ou
$|x_2| \geq 1$. Quelle(s) inégalité(s) êtes-vous en mesure de prouver ?

-   [ ] A: $\|f(1, 1) - f(-1, -1) \| \leq 2 \sqrt{2} \approx 2.83$

-   [ ] B: $\|f(1, 1) - f(-1, -1) \| \leq 4$

-   [ ] C: $\|f(1, 1) - f(-1, -1) \| \leq \pi \sqrt{2} \approx 4.44$
:::
