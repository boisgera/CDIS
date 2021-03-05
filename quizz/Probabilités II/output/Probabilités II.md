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
title: Probabilités II
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
\renewcommand{\P}{\mathbb{P}}
\newcommand{\tr}{\operatorname{tr}}
\newcommand{\Esp}{\mathbb{E}}
```
```{=tex}
\newcommand{\zero}{$\mathord{\boldsymbol{\circ}}$}
\newcommand{\one}{$\mathord{\bullet}$}
\newcommand{\two}{$\mathord{\bullet}\mathord{\bullet}$}
\newcommand{\three}{$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$}
\newcommand{\four}{$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$}
```
::: {.section}
#### Question 1 (réponse multiple)

Soit $\lambda \in\mathbb{R}$ et $X$ une variable aléatoire de loi
$\mathbb{P}_X(\lbrace\lambda \rbrace) = \mathbb{P}(X = \lambda ) = 1$

-   [ ] A : $X$ admet une densité.

-   [ ] B : $X$ admet une fonction de répartition.

-   [ ] C : $X$ admet une espérance et $\mathbb{E}(X) = \lambda$.

-   [ ] D : $X$ est de variance nulle.
:::

::: {.section}
#### Question 2

Soit $X$ une variable aléatoire réelle suivant une loi normale de
paramètres $\mu$ et $\sigma^2$ , quelle est la loi de $X+\gamma$ ?

-   [ ] A : $\mathcal{N}(\mu, \sigma^2)$

-   [ ] B : $\mathcal{N} ( \mu + \dfrac{\gamma}{2}, \sigma^2)$

-   [ ] C : $\mathcal{N} ( \mu + \gamma, \sigma^2)$

-   [ ] D : $\mathcal{N}(\mu+\gamma,(\sigma+\gamma)2)$
:::

::: {.section}
#### Question 3

Soient $X$ et $Y$ deux variables aléatoires indépendantes de loi
uniforme sur $[0, 1]$ . La probabilité $\mathbb{P} (Y \leq 2X)$ vaut :

-   [ ] A : 1/2

-   [ ] B : 2/3

-   [ ] C : 3/4

-   [ ] D : 4/5
:::

::: {.section}
#### Question 4

Soient $X$ et $Y$ deux variables aléatoires de densité $f_X$ et $f_Y$ .
Si les ensembles $\{x \in \mathbb{R} \; | \; f_X(x) > 0\}$ et
$\{y \in \mathbb{R} \; | \; f_Y(y) > 0\}$ sont disjoints, alors

-   [ ] A : $X$ et $Y$ sont nécessairement indépendantes,

-   [ ] B : La covariance $\mathrm{Cov}(X, Y)$ est nécessairement nulle,

-   [ ] C : Ni l'un ni l'autre.
:::

::: {.section}
#### Question 5

Soit $U$ une variable aléatoire réelle de loi uniforme sur \[-1,1\].
Quelle est la densité de $U^2$ ?

-   [ ] A: $\frac1{2\sqrt{x}}1_{[0,1]}(x)$

-   [ ] B: $\frac1{4\sqrt{x}}1_{[0,1]}(x)$

-   [ ] C: $\frac12 1_{[-1,1]}(x)$
:::
