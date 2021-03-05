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
title: Equations Différentielles I
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
::: {.section}
#### Question 1

Les solutions maximales de $\dot{x} = f(x)$ avec
$f:\mathbb{R}^n\to\mathbb{R}^n$ continue

-   [ ] existent pour toute condition initiale
    $(t_0,x_0)\in\mathbb{R}\times \mathbb{R}^n$.

-   [ ] sont définies sur $\mathbb{R}$.

-   [ ] sont soit définies sur $\mathbb{R}$, soit divergent en temps
    fini.
:::

::: {.section}
#### Question 2

L'équation différentielle $\dot{x} = tx^2 +t$ de condition initiale
$(t_0,x_0)\in\mathbb{R}\times \mathbb{R}$

-   [ ] admet une unique solution.

-   [ ] admet une unique solution maximale définie sur $\mathbb{R}$.

-   [ ] admet une unique solution maximale définie sur un intervalle
    ouvert borné de $\mathbb{R}$.
:::

::: {.section}
#### Question 3

Soit $f: \mathbb{R}^n \to \mathbb{R}^n$ continue. Dire que les solutions
de $\dot{x}=f(x)$ varient continûment par rapport à leur condition
initiale sur leur intervalle de définition est

-   [ ] vrai.

-   [ ] vrai si $f$ est continûment différentiable par rapport à $x$.

-   [ ] aucun des deux.
:::

::: {.section}
#### Question 4

Le comportement d'un système chaotique est difficile à prédire parce que

-   [ ] il admet plusieurs solutions pour certaines conditions
    initiales.

-   [ ] ses solutions ne varient pas continûment par rapport à la
    condition initiale.

-   [ ] il est impossible d'assurer une précision suffisante sur la
    condition initiale pour obtenir une erreur raisonnable au delà d'un
    certain temps caractéristique.
:::

::: {.section}
#### Question 5

On peut dire que le système $\dot{x} = - a x + bx^2$ avec $a,b>0$,

-   [ ] admet un point d'équilibre instable.

-   [ ] admet un point d'équilibre localement asymptotiquement stable.

-   [ ] admet un point d'équilibre globalement asymptotiquement stable.
:::

::: {.section}
### Question 6

Le système `\begin{align*}
\dot{x}_1 &= x_1 - x_2 \\
\dot{x}_2 &= 4x_1 - 3x_2
\end{align*}`{=tex}

-   [ ] admet plusieurs points d'équilibre.

-   [ ] admet 0 comme point d'équilibre localement asymptotiquement
    stable.

-   [ ] admet 0 comme point d'équilibre globalement asymptotiquement
    stable.

-   [ ] a ses solutions de la forme $x(t) = (e^{-t}c_1,e^{-t}c_2)$, avec
    $c_1,c_2$ constantes.
:::
