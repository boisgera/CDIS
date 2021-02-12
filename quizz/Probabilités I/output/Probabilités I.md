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
title: Probabilités I
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

Soit $(\Omega, \mathcal{A}, \mathbb{P})$ un espace de probabilité.
Soient $A$, $B \in \mathcal{A}$ tels que $A \subset B$. On a :

-   [ ] A: $\mathbb{P}(A) \leq \mathbb{P}(B)$

-   [ ] B: $\mathbb{P}(A^c) \geq \mathbb{P}(B^c)$

-   [ ] C: Si $\mathbb{P}(A) >0$, alors
    $\mathbb{P}(B|A) = \frac{\mathbb{P}(B)}{\mathbb{P}(A)}$
:::

::: {.section}
#### Question 2

Soit
$(\Omega, \mathcal(A), \mathbb{P}) = (\mathbb{R}_+,\mathcal{B}(\mathbb{R}_+),\mathbb{P})$
où $\mathbb{P}$ est la loi exponentielle de paramètre $\theta$. Soit la
variable aléatoire
$$X : \omega \in \Omega \mapsto \left\{\begin{array}{ll}
0 & \text{ si } \omega \in [0,1],\\
1 & \text{ si } \omega \in ]1, +\infty[
\end{array}\right.$$

-   [ ] A: $\mathbb{P}(X = 0) = \frac12$

-   [ ] B: $\mathbb{P}(X = 1) = e^{-\theta}$

-   [ ] C: $\mathbb{P}(X \in \{0,1\}) = 1$
:::

::: {.section}
#### Question 3 (réponse multiple)

Soit $X$ une variable aléatoire telle que
$\mathbb{P}(X \in [0, 1]) = 0$. Alors

-   [ ] A: $X(\omega) = 0$ quand $\omega \in [0, 1]$

-   [ ] B: La fonction de répartition $F$ associée est nulle sur \[0,
    1\]

-   [ ] C: Si $X$ est de densité $f$, alors $f$ est nulle sur \[0, 1\] .
:::

::: {.section}
#### Question 4

Soit $X$ une variable aléatoire réelle suivant une loi normale de
paramètres $\mu$ et $\sigma^2$ , quelle est la loi de $2X$ ?

-   [ ] A: $\mathcal{N}(\mu, \sigma^2)$

-   [ ] B: $\mathcal{N}(2\mu, (2\sigma)^2)$

-   [ ] C: $\mathcal{N}(\frac12 \mu, \sigma^2)$

-   [ ] D: $\mathcal{N}(\mu, (2\sigma)^2)$
:::

::: {.section}
#### Question 5

Soit $U$ une variable aléatoire réelle de loi uniforme sur \[0,1\].
$U^2$ admet-elle une densité ?

-   [ ] A: Non

-   [ ] B: Oui : $\frac1{2\sqrt{x}}1_{[0,1]}(x)$

-   [ ] C: Oui : $2x 1_{[0,1]}(x)$
:::
