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
#### Question 1 (réponse multiple)

Si les ensembles $A_k \subset \mathbb{R}$, $k \in \mathbb{N}$, sont tous
mesurables, déterminer quels ensembles dans la liste ci-dessous sont
nécessairement mesurables.

-   [ ] A: l'ensemble des $x \in \mathbb{R}$ appartenant (au moins) à
    l'un des $A_k$,

-   [ ] B: l'ensemble des $x \in \mathbb{R}$ n'appartenant à aucun
    $A_k$,

-   [ ] C: l'ensemble des $x \in \mathbb{R}$ appartenant exactement à
    l'un des $A_k$.
:::

::: {.section}
#### Question 2 (réponse multiple)

Une fonction $f: \mathbb{R}\to \mathbb{R}$ est nécessairement intégrable
si

-   [ ] A: elle est mesurable,

-   [ ] B: elle est limite de fonctions mesurables,

-   [ ] C: elle est mesurable et bornée.
:::

::: {.section}
#### Question 3 (réponse multiple)

Si la fonction $f: \mathbb{R}\to \left[0, +\infty\right[$ est
intégrable, alors l'ensemble $\{x \in \mathbb{R}\; | \; f(x) \geq 1\}$
est nécessairement :

-   [ ] A: mesurable,

-   [ ] B: de longueur finie,

-   [ ] C: de longueur nulle,

-   [ ] D: négligeable.
:::

::: {.section}
#### Question 4 (réponses multiple)

Si $f: \mathbb{R}\to \mathbb{R}$ et $g: \mathbb{R}\to \mathbb{R}$ sont
des fonctions mesurables, lister quelles fonctions dans la liste
ci-dessous sont nécessairement mesurables.

-   [ ] A: $f+g$,

-   [ ] B: $f \times g$,

-   [ ] C: $\max(f, g)$,

-   [ ] D: $g \circ f$.
:::

::: {.section}
#### Question 5 (réponse multiple)

Si $f: \mathbb{R}\to \mathbb{R}$ est intégrable sur tout intervalle
$[-r, r]$ avec $r\geq 0$ et que $$
\int_{-r}^r f(t) \, dt \to A \in \mathbb{R}\; \mbox{ quand } \; r \to +\infty,
$$ alors on peut conclure que $f$ est intégrable sur $\mathbb{R}$ et
d'intégrale $A$

-   [ ] A: sans hypothèse supplémentaire,

-   [ ] B: si $|f| \leq g$ où $g:\mathbb{R}\to \left[0,+\infty\right[$
    est intégrable,

-   [ ] C: si $$
        \displaystyle \sup_{r\geq 0}\int_{-r}^r |f(t)| \,dt < + \infty.
        $$
:::
