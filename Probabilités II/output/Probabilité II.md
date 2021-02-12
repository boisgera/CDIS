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

-   [Objectifs d'apprentissage](#objectifs-dapprentissage)
-   [Moments d'une variable aléatoire à
    densité](#moments-dune-variable-aléatoire-à-densité-1)
    -   [Exemples](#exemples)
        -   [*Loi uniforme*](#loi-uniforme)
        -   [*Loi exponentielle*](#loi-exponentielle)
        -   [*Loi gamma*](#loi-gamma)
        -   [*Loi normale*](#loi-normale)
-   [Vecteurs aléatoires à densité](#vecteurs-aléatoires-à-densité)
    -   [Définitions](#définitions)
        -   [Démonstration](#démonstration-2)
    -   [Moments d'un vecteur aléatoire](#moments-dun-vecteur-aléatoire)
-   [Variables aléatoires
    indépendantes](#variables-aléatoires-indépendantes)
    -   [Remarque](#remarque)
-   [Identification de densité](#identification-de-densité-1)
-   [Exercices complémentaires](#exercices-complémentaires)
    -   [Loi de vie et de mort](#loi-de-vie-et-de-mort)
    -   [Durée de vie](#durée-de-vie)
    -   [Crues centennales de la Seine](#crues-centennales-de-la-seine)
    -   [Indépendance et vecteurs
        gaussiens](#indépendance-et-vecteurs-gaussiens)
    -   [Symétrie de la gaussienne](#symétrie-de-la-gaussienne)
    -   [Loi du $\chi^2$](#loi-du-chi2)
    -   [Combinaisons linéaires de variables Gaussiennes
        indépendantes](#combinaisons-linéaires-de-variables-gaussiennes-indépendantes)
-   [Solutions](#solutions)
    -   [Exercices essentiels](#exercices-essentiels)
        -   [Moments d'une variable aléatoire de loi uniforme sur
            $[a,b]$](#answer-moments-unif)
    -   [Loi de vie et de mort](#loi-de-vie-et-de-mort-1)
    -   [Durée de vie](#durée-de-vie-1)
    -   [Crues centennales de la
        Seine](#crues-centennales-de-la-seine-1)
    -   [Indépendance et vecteurs
        gaussiens](#indépendance-et-vecteurs-gaussiens-1)
    -   [Symétrie de la gaussienne](#symétrie-de-la-gaussienne-1)
    -   [Loi du $\chi^2$](#loi-du-chi2-1)
    -   [Combinaisons linéaires de variables Gaussiennes
        indépendantes](#combinaisons-linéaires-de-variables-gaussiennes-indépendantes-1)

```{=tex}
\newcommand{\R}{\mathbb{R}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\Z}{\mathbb{Z}}
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

::: {.section}
#### Moments d'une variable aléatoire à densité

-   `$\mathord{\bullet}$ `{=tex}connaître la définition de l'espérance
    d'une variable aléatoire à densité
-   `$\mathord{\bullet}$ `{=tex}connaître l'interprétation de
    l'espérance
-   `$\mathord{\bullet}$ `{=tex}connaître les propriétés de base de
    l'espérance
-   `$\mathord{\bullet}$ `{=tex}connaître la définition de la variance
    d'une variable aléatoire à densité
-   `$\mathord{\bullet}$ `{=tex}savoir que la variance est toujours
    positive
-   `$\mathord{\bullet}$ `{=tex}savoir ce que signifie variable
    centrée-réduite
-   `$\mathord{\bullet}$ `{=tex}connaître la définition de la covariance
-   `$\mathord{\bullet}$ `{=tex}savoir que la covariance est une forme
    bilinéaire
-   `$\mathord{\bullet}$ `{=tex}connaître et savoir manipuler
    l'inégalité de Cauchy-Schwarz
-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}connaître les
    conditions d'existence de l'espérance d'une fonction (mesurable)
    d'une variable aléatoire
-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir exprimer la
    probabilité d'un événement de la forme $X \in A$ sous la forme d'une
    espérance
-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}connaître et savoir
    calculer les moments des lois usuelles
:::

::: {.section}
#### Vecteurs aléatoires

-   `$\mathord{\bullet}$ `{=tex}savoir que les composantes d'un vecteur
    aléatoire sont des variables aléatoires définies sur le même espace
    de probabilité
-   `$\mathord{\bullet}$ `{=tex}connaître la définition d'un vecteur
    aléatoire à densité
-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}connaître les
    conditions d'existence de l'espérance d'une fonction (mesurable)
    d'un vecteur aléatoire à densité
-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir calculer les
    densités marginales d'un vecteur aléatoire à densité
-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir qu'un couple de
    variables aléatoires à densité n'admet pas nécessairement de densité
-   `$\mathord{\bullet}$ `{=tex}connaître la définition de l'espérance
    d'un vecteur aléatoire à densité
-   `$\mathord{\bullet}$ `{=tex}connaître la définition de la matrice de
    covariance d'un vecteur aléatoire à densité
-   `$\mathord{\bullet}$ `{=tex}savoir que la matrice de covariance est
    semi-définie positive
:::

::: {.section}
#### Variables et vecteurs aléatoires indépendantes

-   `$\mathord{\bullet}$ `{=tex}connaître la définition de
    l'indépendance de deux vecteurs/variables aléatoires
-   `$\mathord{\bullet}$ `{=tex}savoir caractériser l'indépendance de
    deux vecteurs/variables aléatoires à densité
-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir que si $X$ et
    $Y$ sont indépendantes, alors $g(X)$ et $h(Y)$ sont aussi
    indépendantes
-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir que si $X$ et
    $Y$ sont indépendantes et si $g(X)$ et $h(Y)$ sont intégrables alors
    $\mathbb{E}(g(X)g(Y)) = \mathbb{E}(g(X))\mathbb{E}(g(Y))$
-   `$\mathord{\bullet}$ `{=tex}savoir que la covariance de deux
    variables indépendantes est nulle
-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir que la
    réciproque est fausse et connaître un contre-exemple
:::

::: {.section}
#### Identification de densité

-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir identifier la
    densité d'une fonction d'une variable aléatoire par la méthode de la
    fonction muette
-   `$\mathord{\bullet}\mathord{\bullet}$ `{=tex}savoir identifier la
    densité d'une fonction d'un vecteur aléatoire par la méthode de la
    fonction muette
:::
:::

::: {.section}
Moments d'une variable aléatoire à densité
==========================================

La densité de probabilité d'une variable aléatoire va nous permettre de
calculer aisément des grandeurs caractéristiques telles que sa valeur
moyenne et sa variance (lorsqu'elles existent). Elles sont définies
ci-dessous.

::: {.section}
### Définition -- Espérance d'une variable aléatoire à densité {#defesp .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Espérance d'une variable aléatoire à densité}`{=latex}

La variable aléatoire $X : \Omega \to \mathbb{R}$ de densité $f$ est
dite *intégrable* si l'intégrale $\int_\mathbb{R}|x|f(x) dx$ est
définie, autrement dit si le produit $x f(x)$ est intégrable. On définit
alors son *espérance* par $$\mathbb{E}(X) = \int_\mathbb{R}x f(x)dx$$
:::

::: {.section}
### Remarque -- Interprétation {#interprétation .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Interprétation}`{=latex}

$\mathbb{E}(X)$ est un nombre réel qui donne une valeur moyenne résumant
la variable aléatoire $X$.

L'espérance mathématique d'une variable aléatoire est un concept
fondamental de la théorie des probabilités. La dénomination d'espérance
pour cette quantité fait référence aux problèmes de jeux et d'espérance
de gain. Cette terminologie imagée a été introduite par Pascal.

On note $\mathcal{L}^1$ l'ensemble de toutes les variables réelles $X$ à
densité intégrables. Les propriétés suivantes découlent directement des
propriétés de l'intégrale.
:::

::: {.section}
### Proposition -- Propriétés de base {#propl1 .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Propriétés de base}`{=latex}

-   $\mathcal{L}^1$ est un espace vectoriel et
    $\forall X,Y \in \mathcal{L}^1$, $\forall a,b \in \mathbb{R}$
    $$\mathbb{E}(aX + bY) = a\mathbb{E}(X) + b\mathbb{E}(Y).$$
-   $X \in \mathcal{L}^1 \Leftrightarrow |X| \in \mathcal{L}^1$, et dans
    ce cas $$|\mathbb{E}(X)| \leq \mathbb{E}(|X|).$$
-   Si $X \geq 0$ et $X \in \mathcal{L}^1$, alors
    $\mathbb{E}(X) \geq 0.$
-   Si $\exists b \in \mathbb{R}_+$ tel que $|X| \leq b$, alors
    $X \in \mathcal{L}^1$ et $\mathbb{E}(X) \leq b$.
:::

::: {.section}
### Remarque -- Rappel : cas discret {#rappel-cas-discret .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Rappel : cas discret}`{=latex}

Dans le cas d'une variable aléatoire discrète $Y$ à valeurs dans
$\mathbb{N}^\ast$, son espérance est définie par la quantité
$\mathbb{E}(Y) = \sum_{i\in\mathbb{N}^\ast} i\mathbb{P}(Y=i)$, pourvu
que celle-ci soit finie. On voit immédiatement que les propriétés
ci-dessus sont également vérifiées.

Outre l'espace $\mathcal{L}^1$, nous pouvons définir l'espace
$\mathcal{L}^2$ des variables aléatoires réelles dont le carré $X^2$ est
dans $\mathcal{L}^1$.
:::

::: {.section}
### Définition -- Variance {#defvar .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Variance}`{=latex}

La variable aléatoire $X : \Omega \to \mathbb{R}$ de densité $f$ est
dite *de carré intégrable* si
$\mathbb{E}(X^2) = \int_\mathbb{R}x^2 f(x)dx$ est définie, autrement dit
si le produit $x^2 f(x)$ est intégrable. Sa *variance* est définie par
$$\mathbb{V}(X) = \mathbb{E}((X-\mathbb{E}(X))^2)$$
:::

::: {.section}
### Proposition -- Propriétés {#propl2 .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Propriétés}`{=latex}

$\mathcal{L}^2$ est un sous-espace vectoriel de $\mathcal{L}^1$, et si
$X \in \mathcal{L}^2$,
$$|\mathbb{E}(X)| \leq \mathbb{E}(|X|) \leq \sqrt{\mathbb{E}(X^2)}$$
:::

::: {.section}
#### Démonstration {#démonstration .proof}

Soient $X$ et $Y$ deux variables aléatoires réelles de $\mathcal{L}^2$
et $a \in \mathbb{R}$. Comme $(aX+ Y)^2 \leq 2 a^2 X^2 + 2 Y^2$, alors
$aX + Y \in \mathcal{L}^2$. Ainsi, $\mathcal{L}^2$ est un espace
vectoriel.

L'inclusion $\mathcal{L}^2 \subset \mathcal{L}^1$ découle de
$|X| \leq 1 + X^2$ et de la [proposition précédente (p.
`\pageref*{propl1}`{=tex})](#propl1) (linéarité).

La première inégalité a déjà été vue [ci-dessus (p.
`\pageref*{propl1}`{=tex})](#propl1). Pour la seconde, nous pouvons nous
limiter au cas où $X$ est positive. Soit alors $a = \mathbb{E}(X)$ et
$Y = X-a$. Par linéarité, on a
$$ \mathbb{E}(Y^2) = \mathbb{E}(X^2) - 2a \mathbb{E}(X) + a^2 = \mathbb{E}(X^2)-a^2.$$
Et $\mathbb{E}(Y^2) \geq 0$ par le troisième point de la [proposition
ci-dessus (p. `\pageref*{propl1}`{=tex})](#propl1). Par conséquent,
$\mathbb{E}(X)^2 = a^2 \leq \mathbb{E}(X^2)$ ce qui est le résultat
recherché.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Exercice -- Approximation par une constante ($\mathord{\bullet}$) {#exo-approx .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Approximation par une constante}`{=latex}

Soit $X$ une v.a. de carré intégrable. Montrer que
$\mathbb{E}((X - a)^2 )$ atteint son minimum lorsque
$a = \mathbb{E}(X)$. ([Solution p.
`\pageref*{answer-exo-approx}`{=tex}](#answer-exo-approx){.no-parenthesis}.)
:::

::: {.section}
### Remarque -- La variance est positive {#la-variance-est-positive .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{La variance est positive}`{=latex}

En vertu de cette [proposition (p. `\pageref*{propl2}`{=tex})](#propl2),
$\mathbb{V}(X)$ est **positive** et sa racine carrée $\sigma_X$
s'appelle l'*écart-type* de $X$. L'écart-type est une grandeur qui
mesure la moyenne (en un certain sens) de l'écart des valeurs de $X$ à
sa moyenne, d'où son nom.

On a également $$\mathbb{V}(X) = \mathbb{E}(X^2)-\mathbb{E}(X)^2$$ que
l'on obtient en développant $(X-\mathbb{E}(X))^2$. Cette manipulation
anodine est fort utile dans la pratique. On retiendra que "La variance
est égale à la moyenne des carrés moins le carré de la moyenne". On
désigne le terme $\mathbb{E}(X^2)$ par l'expression *moment d'ordre
deux* tandis que la variance est parfois appelée *moment centré d'ordre
deux*.
:::

::: {.section}
### Remarque -- Variable centrée réduite {#variable-centrée-réduite .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Variable centrée réduite}`{=latex}

D'après ce qui précède, si $X$ est une variable aléatoire de carré
intégrable, d'espérance $\mathbb{E}(X)$ et d'écart-type $\sigma_X >0$,
alors la variable aléatoire $$\frac{X-\mathbb{E}(X)}{\sigma_X}$$ est
d'espérance nulle et de variance 1. On dira qu'une telle variable
aléatoire est *centrée et réduite*.

On peut remarquer que si $X$ et $Y$ sont dans $\mathcal{L}^2$, la
variable aléatoire $XY$ est dans $\mathcal{L}^1$, puisque
$|XY| \leq \frac{1}{2}(X^2+Y^2)$. On peut ainsi définir la *covariance*
de deux variables aléatoires :
:::

::: {.section}
### Définition -- Covariance {#defcov .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Covariance}`{=latex}

Si $X$ et $Y$ sont dans $\mathcal{L}^2$, la variable aléatoire
$(X-\mathbb{E}(X))(Y-\mathbb{E}(Y))$ est intégrable. On appelle la
*covariance* de $X$ et $Y$ l'espérance de cette variable aléatoire et on
la note :
$$\text{Cov}(X,Y) = \mathbb{E}((X-\mathbb{E}(X))(Y-\mathbb{E}(Y))).$$ Le
*coefficient de corrélation* des variables aléatoires $X$ et $Y$ est le
nombre
$$\rho(X,Y) = \frac{\text{Cov}(X,Y)}{\sqrt{\mathbb{V}(X)}\sqrt{\mathbb{V}(Y)}}$$
qui est bien défini lorsque $\mathbb{V}(X)>0$ et $\mathbb{V}(Y)>0$.
:::

::: {.section}
#### Exercice -- Calcul d'une covariance ($\mathord{\bullet}$) {#cov-unif .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Calcul d'une covariance}`{=latex}

Soit $U \sim \mathcal{U}_{[0,1]}$ et $V = 1-U$. Calculer
$\text{Cov}(U,V)$ et $\rho(U,V)$. ([Solution p.
`\pageref*{answer-cov-unif}`{=tex}](#answer-cov-unif){.no-parenthesis}.)
:::

::: {.section}
Du fait de la linéarité de l'espérance, on a
$$\text{Cov}(X,Y) = \mathbb{E}(XY) - \mathbb{E}(X)\mathbb{E}(Y)$$ et
d'ailleurs, on voit que la formule de calcul de la variance donnée plus
haut est un cas particulier de cette formulation car
$\mathbb{V}(X) = \text{Cov}(X,X)$. La linéarité de l'espérance nous
donne encore pour $a,a',b,b' \in \mathbb{R}$ `\begin{align*} 
\mathbb{E}((aX+b)(a'Y+b')) &= aa'\mathbb{E}(XY) + ab'\mathbb{E}(X) +a'b\mathbb{E}(Y) + bb'\\
\mathbb{E}(aX+b)\mathbb{E}(a'Y+b') &= aa'\mathbb{E}(X)\mathbb{E}(Y) + ab'\mathbb{E}(X) +a'b\mathbb{E}(Y) + bb'
\end{align*}`{=tex} On en déduit que la covariance est une forme
bilinéaire sur l'espace vectoriel des variables aléatoires de carré
intégrable, et nous avons
$$\text{Cov}(aX+b,a'Y+b') = aa'\text{Cov}(X,Y)$$ En particulier, on a
$$ \mathbb{V}(aX) = a^2\mathbb{V}(X)$$ On en déduit que les coefficients
de corrélation de $X$ et $Y$ et de $aX+b$ et $a'Y+b'$ sont égaux lorsque
$aa' >0$.
:::

::: {.section}
### Proposition -- Inégalité de Cauchy-Schwarz {#CS .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Inégalité de Cauchy-Schwarz}`{=latex}

Soit $X$ et $Y$ deux variables aléatoires de carré intégrable, alors on
a *l'inégalité de Cauchy-Schwarz* :
$$|\mathbb{E}(XY)| \leq \mathbb{E}(|XY|) \leq \sqrt{\mathbb{E}(X^2)\mathbb{E}(Y^2)}$$
avec égalité si et seulement si $X$ et $Y$ sont presque-sûrement
proportionnelles.
:::

::: {.section}
#### Démonstration {#démonstration-1 .proof}

La première inégalité a été démontrée plus haut. Pour la seconde, on a
$\forall x \in \mathbb{R}$ d'après la linéarité de l'espérance :
$$x^2\mathbb{E}(X^2) + 2x\mathbb{E}(XY)+ \mathbb{E}(Y^2) = \mathbb{E}((xX+Y)^2) \geq 0.$$
Mais ceci n'est possible que si ce trinôme en $x$ n'a au plus qu'une
seul racine réelle ; son discriminant
$$4\left((\mathbb{E}(XY))^2 - \mathbb{E}(X^2)\mathbb{E}(Y^2)\right)$$
doit donc être négatif ou nul ce qui donne le résultat.

Le discriminant est nul si et seulement si le trinôme admet une racine
double $x_0$ et dans ce cas, $Y(\omega) = -x_0 X(\omega)$ pour presque
tout $\omega$.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Exercice -- Coefficient de corrélation ($\mathord{\bullet}$) {#CS-corr .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Coefficient de corrélation}`{=latex}

Montrer que le coefficient de corrélation de $X$ et $Y$ vérifie
$$-1\leq \rho(X,Y) \leq 1.$$

Enfin, il peut être intéressant de pouvoir calculer l'espérance d'une
fonction mesurable d'une variable aléatoire réelle à densité qui est une
variable aléatoire en vertu de la [proposition vue de
composition](Probabilité%20I.pdf%20#composition). ([Solution p.
`\pageref*{answer-CS-corr}`{=tex}](#answer-CS-corr){.no-parenthesis}.)
:::

::: {.section}
### Proposition -- Espérance de $g(X)$ {#esperanceg .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Espérance de \(g(X)\)}`{=latex}

Soit $X$ une variable aléatoire réelle admettant la densité $f$, et $g$
une fonction mesurable de $\mathbb{R}$ dans $\mathbb{R}$. Alors $g(X)$
est intégrable si et seulement si l'intégrale
$$\int_\mathbb{R}|g(x)|f(x) dx,$$ est définie et dans ce cas
$$\mathbb{E}(g(X)) = \int_\mathbb{R}g(x)f(x) dx.$$

Nous n'avons pas tous les éléments permettant de démontrer ce résultat,
mais l'argument heuristique suivant permet de comprendre pourquoi il est
vrai : supposons $g$ continue telle que $|g|f$ soit intégrable. Alors il
existe une jauge $\gamma(t)$, sur $[-\infty, +\infty]$ telle que, si la
subdivision pointée (totale ou partielle)
$\mathcal{D} =\{(t_i, I_i)\}_i$ est subordonnée à $\gamma$, on a $$
S(gf, \mathcal{D}) = \left|S(gf, \mathcal{D}) - \int _\mathbb{R}g(x)f(x) dx \right| 
\leq 
\varepsilon.
$$ Posons $X_n = t_i$ si $X \in I_i$, pour $i \in \{0,\ldots,n-1\}$.
Ainsi, pour tout $\omega$,
$X_n(\omega) \xrightarrow[n \to \infty]{} X(\omega)$ et par continuité
de $g$, on a $g(X_n) \xrightarrow[n \to \infty]{} g(X)$. Comme $X_n$ est
une variable aléatoire discrète, on a
$$\mathbb{E}(g(X_n)) = \sum_{i=0}^{n-1}g(t_i)\mathbb{P}(X\in I_i)l(I_i) \approx \sum_{i=0}^{n-1}g(t_i)f(t_i).$$
:::

::: {.section}
### Remarque -- Cas particulier {#cas-particulier .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Cas particulier}`{=latex}

L'espérance et la variance sont des cas particulier de ce résultat. On a
de plus pour $A \in \mathcal{B}(\mathbb{R})$ :
$$\mathbb{E}(1_A(X)) = \int_A f(x)dx = \mathbb{P}(X\in A)$$
:::

::: {.section}
Exemples
--------

Nous donnons ici quelques exemples de densités de probabilité. Nous
reprenons en particulier les [trois exemples de densités donnés au
premier cours](Probabilité%20I.pdf%20#exampledens) :

::: {.section}
### *Loi uniforme*

sur $[a,b]$, où $a < b$ et on note $X \sim \mathcal{U}_{[a,b]}$ si $X$
est de densité $$ f(x) = \frac{1}{b-a} 1_{[a,b]} (x).$$
:::

::: {.section}
#### Exercice -- Moments d'une variable aléatoire de loi uniforme sur $[a,b]$ ($\mathord{\bullet}$) {#moments-unif .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Moments d'une variable aléatoire de loi uniforme sur \([a,b]\)}`{=latex}

Soit $X \sim \mathcal{U}_{[a,b]}$. Montrer que son espérance vaut
$$ \mathbb{E}(X) = \int_a^b \frac{x}{b-a} dx = \frac{a+b}{2}$$ et que sa
variance vaut
$$ \mathbb{V}(X) = \mathbb{E}(X^2) - \mathbb{E}(X)^2 = \frac{(b-a)^2}{12}.$$

([Solution p.
`\pageref*{answer-moments-unif}`{=tex}](#answer-moments-unif){.no-parenthesis}.)
:::

::: {.section}
### *Loi exponentielle*

de paramètre $\theta > 0$ et on note $X \sim \mathcal{E}(\theta)$ si $X$
est de densité $$ f(x) = \theta e^{-\theta x} 1_{\{x>0\}} (x).$$
:::

::: {.section}
#### Exercice -- Moments d'une v.a. exponentielle ($\mathord{\bullet}$) {#moments-expo .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Moments d'une v.a. exponentielle}`{=latex}

Montrer que son espérance et sa variance valent
$$ \mathbb{E}(X) = \frac{1}{\theta} \text{ et } \mathbb{V}(X) = \frac{1}{\theta^2}$$

([Solution p.
`\pageref*{answer-moments-expo}`{=tex}](#answer-moments-expo){.no-parenthesis}.)
:::

::: {.section}
### *Loi gamma*

On rappelle tout d'abord que la fonction gamma est définie pour
$\alpha \in \left] 0, + \infty \right[$ par
$$\Gamma(\alpha) = \int_0^{+\infty} x^{\alpha-1}e^{-x} dx.$$ En
intégrant par partie, on obtient la relation
$\Gamma(\alpha+1) = \alpha \Gamma(\alpha)$, et on a $\Gamma(1) = 1$. On
en déduit que $\Gamma(n) = (n-1)!$.

Une variable aléatoire $X$ suit une loi gamma de paramètre d'échelle
$\theta$ et d'indice $\alpha$ et on note $X \sim \Gamma(\alpha,\theta)$,
si sa loi admet la densité
$$f(x) = \frac{1}{\Gamma(\alpha)}\theta^\alpha x^{\alpha -1} e^{-\theta x}.$$
:::

::: {.section}
#### Exercice -- Moments d'une v.a. de loi gamma ($\mathord{\bullet}$) {#moments-gamma .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Moments d'une v.a. de loi gamma}`{=latex}

Soit $X\sim \Gamma(\alpha,\theta)$. Montrer que son espérance et sa
variance valent :

$$ \mathbb{E}(X) = \frac{\alpha}{\theta} \text{ et } \mathbb{V}(X) = \frac{\alpha}{\theta^2}.$$

On remarquera que $\Gamma(1,\theta)$ est la loi exponentielle de
paramètre $\theta$.

Lorsque $\alpha$ est entier, la loi gamma permet de modéliser le temps
d'attente avant la $n$-ième occurence d'événements indépendants de loi
exponentielle de paramètre $\theta$. ([Solution p.
`\pageref*{answer-moments-gamma}`{=tex}](#answer-moments-gamma){.no-parenthesis}.)
:::

::: {.section}
### *Loi normale*

de paramètres $\mu$ et $\sigma^2$ et on note
$X \sim \mathcal{N}(\mu,\sigma^2)$ si $X$ est de densité
$$f(x) = \frac{1}{\sqrt{2\pi}\sigma}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$
Son espérance et sa variance valent
$$\mathbb{E}(X) =  \mu \text{ et } \mathbb{V}(X) = \sigma^2$$
:::

::: {.section}
#### Exercice -- Moments d'une v.a. gaussienne ($\mathord{\bullet}$) {#moments-gauss .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Moments d'une v.a. gaussienne}`{=latex}

Après avoir vérifié que $f$ est bien une densité, calculer l'espérance
et la variance de $X \sim \mathcal{N}(\mu,\sigma^2)$ ([Solution p.
`\pageref*{answer-moments-gauss}`{=tex}](#answer-moments-gauss){.no-parenthesis}.)
:::

::: {.section}
### Remarque -- Estimation statistique {#estimation-statistique .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Estimation statistique}`{=latex}

Dans les exemples ci-dessus, on peut remarquer que les densités sont
paramétrées par des nombres réels qui sont liés directement aux valeurs
de l'espérance et de la variance de la variable. C'est très utile en
statistique où l'on cherchera à estimer la valeur de ces paramètres à
partir des observations disponibles. Dans le cas de la loi normale, la
moyenne et la variance (empiriques) des échantillons fourniront ainsi
directement des estimateurs des paramètres.

Il existe des variables aléatoires qui n'ont pas d'espérance, comme le
montre l'exercice suivant.
:::

::: {.section}
#### Exercice -- *Loi de Cauchy* ($\mathord{\bullet}\mathord{\bullet}$) {#exo-cauchy .exercise .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{\emph{Loi de Cauchy}}`{=latex}

Un gyrophare envoie un flash lumineux dans une direction aléatoire
uniforme d'angle $\theta$. On cherche la distribution de l'abscisse $X$
du point d'impact du rayon lumineux sur un écran plan infini situé à
distance 1 du gyrophare. Donner la densité de $X$. Calculer son
espérance. ([Solution p.
`\pageref*{answer-exo-cauchy}`{=tex}](#answer-exo-cauchy){.no-parenthesis}.)
:::
:::
:::

::: {.section}
Vecteurs aléatoires à densité
=============================

Nous allons généraliser ici la notion de variable aléatoire en
considérant qu'elle peut prendre ses valeurs dans $\mathbb{R}^n$. Les
vecteurs aléatoires se rencontrent naturellement lorsqu'on s'intéresse à
plusieurs quantités conjointement, par exemple dans le cas de la météo,
la température, la pluviométrie et la vitesse et la direction du vent.

::: {.section}
Définitions
-----------

Une variable aléatoire $X$ à valeurs dans $\mathbb{R}^n$ (ou vecteur
aléatoire) est simplement une collection de $n$ variables réelles
définies sur le même espace probabilisé
$(\Omega, \mathcal{A}, \mathbb{P})$, qui sont les *composantes* de $X$.
On écrit $X = (X_1,\ldots,X_n)$.

De même qu'en dimension 1, la loi de $X$ est caractérisée par la
fonction de répartition multi-dimensionnelle
$F : \mathbb{R}^n \to \mathbb{R}$ définie par
$$F(x_1,\ldots,x_n) = \mathbb{P}_X(X_1\leq x_1,\ldots,X_n\leq x_n)$$
Mais caractériser les fonctions de répartition sur $\mathbb{R}^n$ est
délicat, de sorte que cette notion est rarement utilisée. Nous allons
plus particulièrement nous intéresser aux vecteurs aléatoires à densité.

::: {.section}
### Définition -- Vecteur aléatoire à densité {#defvect .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Vecteur aléatoire à densité}`{=latex}

On dit que $X$ admet la densité $f$ si la fonction réelle $f$ sur
$\mathbb{R}^n$ est positive, intégrable et vérifie
$$\int_{\mathbb{R}^n} f(x) dx = \int_{-\infty}^{+\infty} \ldots \int_{-\infty}^{+\infty} f(x_1,\ldots,x_n) dx_1 \ldots dx_n= 1$$
et si
$$\mathbb{P}_X(X_1\leq x_1,\ldots,X_n\leq x_n) = \int_{-\infty}^{x_1} \ldots \int_{-\infty}^{x_n} f(x_1,\ldots,x_n) dx_1 \ldots dx_n.$$

De la même manière que dans le [cas unidimensionnel (p.
`\pageref*{esperanceg}`{=tex})](#esperanceg), on a :
:::

::: {.section}
### Proposition -- Fonction d'un vecteur aléatoire {#esperancegvect .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Fonction d'un vecteur aléatoire}`{=latex}

Soit $X$ un vecteur aléatoire de densité $f$, et soit $g$ une fonction
de $\mathbb{R}^n$ dans $\mathbb{R}$, mesurable. On a alors
$g(X)\in \mathcal{L}^1$ si et seulement si
$$\int_{-\infty}^{+\infty} \ldots \int_{-\infty}^{+\infty} |g(x_1,\ldots,x_n)|f(x_1,\ldots,x_n) dx_1 \ldots dx_n,$$
est définie et dans ce cas, on a
$$\mathbb{E}(g(X)) = \int_{-\infty}^{+\infty} \ldots \int_{-\infty}^{+\infty} g(x_1,\ldots,x_n)f(x_1,\ldots,x_n) dx_1 \ldots dx_n.$$

Pour revenir à la densité d'une composante d'un vecteur aléatoire, on
intègre par rapport aux autres variables. On le présente ici dans le cas
d'un couple $Z=(X,Y)$ de variables aléatoires. On généralise aisément à
une dimension supérieure.
:::

::: {.section}
### Proposition -- Densités marginales {#loimarg .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Densités marginales}`{=latex}

Supposons que $Z$ admette une densité $f$. Alors $X$ et $Y$ admettent
les densités $f_X$ et $f_Y$ données par
$$f_X(x) = \int_\mathbb{R}f(x,y) dy,\,\,\, f_Y(y) = \int_\mathbb{R}f(x,y) dx.$$

Les fonctions $f_X$ et $f_Y$ s'appellent les *densités marginales* de
$f$.
:::

::: {.section}
### Démonstration {#démonstration-2 .prooof}

Pour tout $x \in \mathbb{R}$, on a par définition
$$ \mathbb{P}(X \leq x) = \mathbb{P}(Z \in ]-\infty,x] \times \mathbb{R}) = \mathbb{E}(1_{]-\infty,x] \times \mathbb{R}}(Z)) = \int_{-\infty}^x du \left(\int_\mathbb{R}f(u,v) dv\right),$$
où l'on a utilisé le [théorème de
Fubini](Calcul%20Intégral%20III.pdf%20#Fubini) pour
$1_{]-\infty,x] \times \mathbb{R}}(u,v)f(u,v)$ intégrable. Donc si $f_X$
est définie par $f_X(x) = \int_\mathbb{R}f(x,y) dy$, on obtient que
$\mathbb{P}(X \leq x) = \int_{-\infty}^x f_X(u) du$, ce qui montre que
$f_X$ est la densité de $X$. Le raisonnement est analogue pour $Y$.
:::

::: {.section}
### Remarque -- Réciproque ? {#réciproque .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Réciproque ?}`{=latex}

La réciproque de cette proposition est fausse en revanche : les
variables aléatoires $X$ et $Y$ peuvent avoir des densités sans que le
couple $Z = (X, Y )$ en ait une.

Supposons par exemple que $X = Y$. Si
$\Delta = \{(x,x) ; x\in \mathbb{R}\}$ est la diagonale de
$\mathbb{R}^2$, nous avons évidemment $\mathbb{P}_Z(\Delta) = 1$ mais si
la [proposition précédente (p.
`\pageref*{esperancegvect}`{=tex})](#esperancegvect) était valide pour
$\mathbb{P}_Z$, on aurait
$\mathbb{P}_Z(\Delta) = \mathbb{E}(1_\Delta) = \int_{\mathbb{R}^2} 1_\Delta f_Z(z)dz = 0$
car $\Delta$ est de volume nul dans $\mathbb{R}^2$.

En particulier, il faut faire attention au fait que dans le cas général,
la densité d'un couple de variables aléatoires n'est pas le produit des
densités.
:::

::: {.section}
#### Exercice -- Lancer de fléchette ($\mathord{\bullet}\mathord{\bullet}$) {#exo-flechette .exercise .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Lancer de fléchette}`{=latex}

On lance une fléchette sur une cible circulaire de rayon unité. Le
joueur est suffisamment maladroit pour que le point $M$ d'impact de la
fléchette soit supposé uniformément distribué sur la cible (On décide de
n'observer que les lancés qui atteignent la cible). Exprimer la densité
du couple formé par les coordonnées cartésiennes $(X,Y)$ de $M$ puis
leurs densités marginales. ([Solution p.
`\pageref*{answer-exo-flechette}`{=tex}](#answer-exo-flechette){.no-parenthesis}.)
:::
:::

::: {.section}
Moments d'un vecteur aléatoire
------------------------------

::: {.section}
### Définition -- Vecteur espérance et covariance {#vecteur-espérance-et-covariance .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Vecteur espérance et covariance}`{=latex}

Si les composantes $X_i$ du vecteur aléatoire $X = (X_1,\ldots,X_n)$
sont intégrables, on peut définir le *vecteur espérance*
$$\mathbb{E}(X) = (\mathbb{E}(X_1),\ldots,\mathbb{E}(X_n))$$ Si les
composantes $X_i$ du vecteur aléatoire $X = (X_1,\ldots,X_n)$ sont de
carré intégrable, la *matrice de covariance* de $X$ est la matrice
$C_X = (c_{i,j})_{1 \leq i \leq n , 1 \leq j \leq n}$ de taille
$n \times n$ et dont les éléments valent
$$c_{i,j} = \text{Cov}(X_i,X_j)$$
:::

::: {.section}
### Proposition -- Matrice de covariance {#matrice-de-covariance .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Matrice de covariance}`{=latex}

La matrice de covariance est symétrique non-négative (ou encore
semi-définie positive).
:::

::: {.section}
#### Démonstration {#démonstration-3 .proof}

La symétrie est évidente. Non-négative signifie que pour tous réels
$a_1,\ldots,a_n$, on a
$\sum_{i=1}^n \sum_{j=1}^n a_i a_j c_{i,j} \geq 0$. Un calcul simple
montre que
$$ \sum_{i=1}^n \sum_{j=1}^n a_i a_j c_{i,j} = \mathbb{V}(\sum_{i=1}^n a_i X_i) \geq 0.$$`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Exemple -- Vecteur Gaussien $n$-dimensionel {#vecteur-gaussien-n-dimensionel .example .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Vecteur Gaussien \(n\)-dimensionel}`{=latex}

Un exemple important de vecteurs aléatoires est celui des vecteurs
gaussiens, que nous étudierons plus en détail au chapitre suivant.
Soient $m \in \mathbb{R}^n$ et $C$ une matrice symétrique définie
positive (c'est-à-dire telle que pour tout $x \in \mathbb{R}^n$ non
identiquement nul $x^tCx > 0$ où $^t$ désigne la transposée). Le vecteur
$X \in \mathbb{R}^n$ est un vecteur aléatoire gaussien d'espérance $m$
et de matrice de covariance $C$ si sa densité s'écrit
$$ f(x) = \frac{1}{(2\pi)^{n/2}\sqrt{\det (C)}}\exp (-\frac{1}{2}(x-m)^tC^{-1}(x-m)) $$
On a alors $\mathbb{E}(X) = m$ et $C_X =C$.

![Densité de probabilité de la loi normale bivariée centrée, réduite, de
coefficient de corrélation 1/2](images/PdfGauss3D.tex.pdf)
:::
:::
:::

::: {.section}
Variables aléatoires indépendantes
==================================

Lorsqu'on modélise plusieurs variables conjointement, une hypothèse
importante est celle de l'indépendance. Ce caractère traduit l'absence
de lien de causalité entre les variables. Par exemple, on fait
naturellement l'hypothèse d'indépendance lorsque l'on considère une
répétition d'une même expérience dans les mêmes conditions.

Dans ce paragraphe, on considère un couple $(X,Y)$ de vecteurs
aléatoires respectivement à valeurs dans $\mathbb{R}^m$ et
$\mathbb{R}^n$. Les résultats s'étendent sans peine à une famille finie
quelconque.

On peut se ramener aux évènements pour caractériser l'indépendance de
deux vecteurs aléatoires. En effet, considérons le vecteur aléatoire
$Z = (X,Y)$, $A$ et $B$ deux ensembles dans
$\mathcal{B}({\mathbb{R}^m})$ et $\mathcal{B}({\mathbb{R}^n})$. On a vu
que les évènements $X\in A$ et $Y \in B$ sont indépendants si et
seulement si
$\mathbb{P}_Z(X \in A, Y \in B) = \mathbb{P}(X^{-1}(A) \cap Y^{-1}(B)) = \mathbb{P}(X^{-1}(A))\mathbb{P}(Y^{-1}(B)) = \mathbb{P}_X(X \in A)\mathbb{P}_Y(Y \in B)$.
Pour que deux vecteurs aléatoires soient indépendants, on va donc
demander que ceci soit valable quels que soient $A$ et $B$.

::: {.section}
### Définition -- Vecteurs aléatoires indépendants {#defvai .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Vecteurs aléatoires indépendants}`{=latex}

Les vecteurs aléatoires $X$ et $Y$ sont *indépendants* si pour tous
ensembles $A$ et $B$ des tribus correspondantes,
$$\mathbb{P}(X \in A, Y \in B) = \mathbb{P}(X \in A)\mathbb{P}(Y \in B)$$

Cette définition se traduit en termes de densités dans la proposition
suivante que l'on énonce sans perte de généralité pour un couple de
variables aléatoires.
:::

::: {.section}
### Proposition -- Caractérisation de l'indépendance {#caractérisation-de-lindépendance .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Caractérisation de l'indépendance}`{=latex}

Soient $X$ et $Y$ deux variables aléatoires réelles de densités $f_X$ et
$f_Y$. $X$ et $Y$ sont indépendantes si et seulement si le couple
$Z = (X,Y)$ a pour densité (sur $\mathbb{R}^2$) :
$$f_Z(x,y) = f_X(x)f_Y(y).$$
:::

::: {.section}
#### Démonstration {#démonstration-4 .proof}

S'il y a indépendance, la [définition (p.
`\pageref*{defvai}`{=tex})](#defvai) implique
$$P(X\leq x, Y\leq y) = P(X\leq x) \mathbb{P}(Y\leq y) = \int_{-\infty}^x f_X(u) du \int_{-\infty}^y f_Y(v) dv$$
ce qui montre que $\mathbb{P}_Z$ vérifie la [définition d'un vecteur
aléatoire à densité (p. `\pageref*{defvect}`{=tex})](#defvect) avec
$f_Z=f_X f_Y$.

Inversement, si $f_Z=f_X f_Y$, on a pour tous $A$, $B$ de
$\mathcal{B}({\mathbb{R}})$
$$\mathbb{P}(X\in A, Y\in B) = \int_A \int_B f_X(x) f_Y(y) dxdy = \mathbb{P}(X \in A)\mathbb{P}(Y \in B)$$
où on a utilisé le [théorème de
Fubini](Calcul%20Intégral%20III.pdf%20#Fubini).`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Exercice -- Lancer de fléchette (suite) ($\mathord{\bullet}$) {#exo-flechettebis .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Lancer de fléchette (suite)}`{=latex}

Les coordonnées cartésiennes $(X,Y)$ de $M$ sont elles indépendantes ?
([Solution p.
`\pageref*{answer-exo-flechettebis}`{=tex}](#answer-exo-flechettebis){.no-parenthesis}.)
:::

::: {.section}
Considérons maintenant deux fonctions $g$ et $h$ définies sur
$\mathbb{R}^m$ et $\mathbb{R}^n$ telles que $g(X)$ et $h(Y)$ soient
aussi des variables aléatoires.
:::

::: {.section}
### Proposition -- Fonctions de vecteurs aléatoires indépendants {#indep_fct .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Fonctions de vecteurs aléatoires indépendants}`{=latex}

Avec les notations précédentes, si $X$ et $Y$ sont indépendantes de
densités respectives $f_X$ et $f_Y$, les variables aléatoires $g(X)$ et
$h(Y)$ sont aussi indépendantes. Si de plus $g(X)$ et $h(Y)$ sont
intégrables, alors le produit $g(X)h(Y)$ est aussi intégrable, et on a
$$ \mathbb{E}(g(X)h(Y)) = \mathbb{E}(g(X))\mathbb{E}(h(Y))$$
:::

::: {.section}
#### Démonstration {#démonstration-5 .proof}

La première assertion est évidente par définition de l'indépendance. Par
ailleurs, si $g(X)$ et $h(Y)$ sont intégrables, en notant $f_{(X,Y)}$ la
densité du couple $(X,Y)$, et en utilisant le [théorème de
Fubini](Calcul%20Intégral%20III.pdf%20#Fubini), on a `\begin{align*}
\mathbb{E}(g(X)h(Y))  & = \int_{\mathbb{R}^{m+n}} g(x)h(y) f_{(X,Y)}(x,y) dx dy \\
                & = \int_{\mathbb{R}^m} \int_{\mathbb{R}^n} g(x)h(y)f_X(x) f_Y(y) dx dy \\
                & = \left(\int_{\mathbb{R}^m}  g(x) f_X(x) dx \right) \left(\int_{\mathbb{R}^n} h(y) f_Y(y) dy\right)\\
                & = \mathbb{E}(g(X))\mathbb{E}(h(Y))
\end{align*}`{=tex}`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Remarque -- Cas général {#cas-général .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Cas général}`{=latex}

Ce résultat est encore valable $X$ et $Y$ dans le cas général (sans
densité), voir @Jacod pour une démonstration.

On déduit de ce résultat et de la [définition de la covariance (p.
`\pageref*{defcov}`{=tex})](#defcov) que :
:::

::: {.section}
### Corollaire -- Covariance de variables aléatoires indépendantes {#covariance-de-variables-aléatoires-indépendantes .corollary .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Covariance de variables aléatoires indépendantes}`{=latex}

Si les variables aléatoires réelles $X$ et $Y$ sont indépendantes et de
carré intégrable, alors $\text{Cov}(X,Y) = 0$ et $\rho(X,Y) = 0$.
:::

::: {.section}
#### Exercice -- Démonstration ($\mathord{\bullet}$) {#demo-cov-indep .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Démonstration}`{=latex}

Démontrer ce résultat. ([Solution p.
`\pageref*{answer-demo-cov-indep}`{=tex}](#answer-demo-cov-indep){.no-parenthesis}.)
:::

::: {.section}
### Remarque

Attention, la réciproque est fausse. Par exemple, si
$X \sim \mathcal{U}_{[-1,1]}$ et $Y = X^2$. $X$ et $Y$ ne sont
clairement pas indépendantes mais on a

$$\text{Cov}(X,Y) = \text{Cov}(X,X^2) = \mathbb{E}(X^3) - \mathbb{E}(X)\mathbb{E}(X^2) = 0$$
:::
:::

::: {.section}
Identification de densité
=========================

Un problème important est le suivant. Soit $X$ une variable aléatoire
réelle, admettant la densité $f_X$. Soit $g$ une fonction mesurable, de
sorte que $Y = g(X)$ soit aussi une variable aléatoire. Est-ce que $Y$
admet une densité, et si oui, comment la calculer ?

On peut déjà remarquer que cette densité n'existe pas toujours. Si par
exemple $g(x) = a$ pour tout $x$, la loi de $Y$ est la masse de Dirac en
$a$, qui n'a pas de densité.

Pour résoudre ce problème, l'idée consiste à essayer de mettre
$E(h(Y )) = E(h \circ g(X))$ sous la forme $\int h(y)f_Y (y)dy$ pour une
fonction convenable $f_Y$, et une classe de fonctions $h$ suffisamment
grande. La fonction $f_Y$ sera alors la densité cherchée.

La [proposition qui assure que $g(X)$ est intégrable pour une variable
aléatoire réelle $X$ (p. `\pageref*{esperanceg}`{=tex})](#esperanceg)
implique
$$ \mathbb{E}(h(Y)) = \mathbb{E}(h \circ g (X)) = \int_{\mathbb{R}} h \circ g(x) f_X(x) dx$$

et on fait le changement de variable $y = g(x)$ dans cette intégrale.
Cela nécessite que $g$ soit dérivable et bijective "par morceaux", et il
faut faire très attention aux domaines où $g$ est croissante ou
décroissante. Puisque la fonction $h$ est arbitraire, on appelle
couramment cette technique la *méthode de la fonction muette*. Cette
approche résulte en fait de la proposition suivante que nous ne
démontrerons pas :

::: {.section}
### Proposition -- Méthode de la fonction muette {#méthode-de-la-fonction-muette .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Méthode de la fonction muette}`{=latex}

Si il existe une fonction $f$ telle que pour toute fonction mesurable
$h$ telle que $h(x) f(x)$ soit intégrable,
$$\mathbb{E}(h(X)) = \int_\mathbb{R}h(x) f(x) dx$$ alors la loi de $X$
admet la densité $f$.
:::

::: {.section}
#### Démonstration {#démonstration-6 .proof}

L'idée de la preuve repose sur le fait que parmi ces fonctions se
trouvent les $h = 1_{]-\infty,y]}$, pour laquelle la formule précédente
donne la fonction de répartition de $f$. Pour une démonstration
complète, voir @Jacod.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
Nous donnons ici quelques exemples d'application de cette méthode :

-   Soit $Y = aX + b$, où $a$ et $b$ sont des constantes. Si $a=0$,
    alors $Y = b$ et la loi de $Y$ est la masse de Dirac en $b$ (sans
    densité). Si $a \neq 0$, on fait le changement de variable
    $y = ax+b$, ce qui donne
    $$ \mathbb{E}(h(Y)) = \int_\mathbb{R}h(ax+b) f_X(x) dx = \int_\mathbb{R}h(y) f_X(\frac{y-b}{a})\frac{1}{|a|} dy $$
    Donc $$ f_Y(y) = f_X(\frac{y-b}{a})\frac{1}{|a|} $$
-   Soit $Y =X^2$. La fonction $g$ est décroissante sur $\mathbb{R}_-$
    et croissante sur $\mathbb{R}_+$. Le changement de variable
    $y = x^2$ donne alors `\begin{align*}
         \mathbb{E}(h(Y)) &= \int_{-\infty}^0 h(x^2) f_X(x) dx + \int_0^{+\infty} h(x^2) f_X(x) dx\\
                    &= \int_0^{+\infty} h(y) f_X(-\sqrt{y})\frac{1}{2\sqrt{y}} dy + \int_0^{+\infty} h(y) f_X(\sqrt{y})\frac{1}{2\sqrt{y}}dy
         \end{align*}`{=tex} et on en déduit
    $$f_Y(y) = (f_X(-\sqrt{y})+f_X(\sqrt{y}))\frac{1}{2\sqrt{y}}1_{\left]0,+\infty\right[}$$
:::

::: {.section}
### Remarque -- Conséquences {#conséquences .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Conséquences}`{=latex}

Dans le cas des vecteurs aléatoires, l'idée est la même. Soit
$X = (X_1,\ldots,X_n)$, un vecteur aléatoire de densité $f_X$ sur
$\mathbb{R}^n$, $g$ une fonction de $\mathbb{R}^n$ dans $\mathbb{R}^m$
et $Y = g(X)$. Plusieurs cas sont à considérer :

1.  $m > n$, le vecteur $Y$ n'admet pas de densité.
2.  $m=n$, on utilise comme dans le cas unidimensionel le changement de
    variable $y = g(x)$ dans
    $$ \mathbb{E}(h(Y)) = \mathbb{E}(h \circ g (X)) = \int_{\mathbb{R}^n} h \circ g(x) f_X(x) dx $$
    Supposons d'abord que $g$ soit une bijection continûment
    différentiable de $A$ dans $B$, ouverts de $\mathbb{R}^n$. Sous
    l'hypothèse que $h \circ g(x) f_X(x)$ soit intégrable, le [théorème
    de changement de variable](Calcul%20Intégral%20III.pdf) nous
    assure :
    $$ \int_A h\circ g (x) f_X(x) dx = \int_B h(y) f_X \circ g^{-1}(y) \frac{1}{|\det J_g (g^{-1}(y))|} dy,$$
    où $J_g$ désigne la matrice de Jacobi associée à la différentielle
    de $g$. Dans le cas où $f_X(x) = 0$ en dehors de $A$, on obtient que
    $Y$ admet la densité
    $$ f_Y(y) = 1_B(y)f_X \circ g^{-1}(y)\frac{1}{|\det J_g (g^{-1}(y))|}.$$
    Lorsque $g$ est simplement continûment différentiable, il existe
    souvent une partition finie $(A_i)_{1\leq i \leq n}$ de l'ensemble
    $\{x ; f(x) >0\}$, telle que $g$ soit injective sur chaque $A_i$. On
    note alors $B_i = g(A_i)$ l'image de $A_i$ par $g$. On découpe alors
    l'intégrale selon les $A_i$, on applique la formule précédente à
    chaque morceau et on somme pour obtenir :
    $$ f_Y(y) = \sum_{i=1}^n 1_{B_i}(y)f_X \circ g^{-1}(y) \frac{1}{|\det J_g (g^{-1}(y))|},$$
    où $g^{-1}$ est bien définie sur chaque $B_i$ comme image réciproque
    de la restriction de g à $A_i$.
3.  $m < n$, on commence par "compléter" $Y$, en essayant de construire
    une application $g'$ de $\mathbb{R}^n$ dans $\mathbb{R}^n$ dont les
    $m$ premières composantes coïncident avec les composantes de $g$ et
    pour laquelle on peut appliquer l'une des deux formules précédentes.
    On obtient ainsi la densité $f_Y'$ de $Y' = g'(X)$ puis on obtient
    la densité de $Y$ en calculant sa loi marginale :
    $$f_Y(y_1,\ldots,y_m) = \int_{\mathbb{R}^{n-m}} f_{Y'}(y_1,\ldots,y_m,y_{m+1},\ldots y_n) dy_{m+1}\ldots dy_n.$$
:::

::: {.section}
#### Exemple -- **Coordonnées polaires** {#polar .example .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{\textbf{Coordonnées polaires}}`{=latex}

Soit $X = (U,V)$ un vecteur aléatoire de $\mathbb{R}^2$, et
$Y = (R,\Theta)$ ses coordonnées polaires. La transformation $g$ est un
difféomorphisme de $A = \mathbb{R}^2\setminus\{0\}$ dans
$B = \left]0,+\infty\right[\times \left]0,2\pi\right]$, et son inverse
$g^{-1}$ s'écrit : $u = r\cos \theta,\, v= r\sin \theta$. Le Jacobien de
$g^{-1}$ au point $(r,\theta)$ vaut $r$, donc le point 2. ci-dessus
entraîne que
$$ f_Y(r,\theta) = r f_X(r\cos\theta,r\sin\theta)1_B(r,\theta)$$ Par
exemple, si $U$ et $V$ sont indépendantes et de loi $\mathcal{N}(0,1)$,
on a $f_X(u,v) = \frac{1}{2\pi}\exp\left(-\frac{u^2+v^2}{2}\right)$ et
donc
$$ f_Y(r,\theta) = \frac{1}{2\pi} r\exp\left(-\frac{r^2}{2}\right)1_{\left]0,+\infty\right[ }(r)1_{\left]0,2\pi\right]}(\theta).$$
En particulier, on remarque que $R$ et $\Theta$ sont indépendantes de
densités respectives
$r\exp\left(-\frac{r^2}{2}\right)1_{\left]0,+\infty\right[}(r)$ et
$1_{\left]0,2\pi\right]}(\theta)$.
:::

::: {.section}
#### Exercice -- Lancer de fléchette (fin) ($\mathord{\bullet}$) {#exo-flechetteter .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Lancer de fléchette (fin)}`{=latex}

Donner la densité du couple $(R,\Theta)$ des coordonnées polaires de
$M$. Sont-elles indépendantes ? ([Solution p.
`\pageref*{answer-exo-flechetteter}`{=tex}](#answer-exo-flechetteter){.no-parenthesis}.)
:::

::: {.section}
#### Exemple -- **Somme de deux variables aléatoires indépendantes** {#sum .example .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{\textbf{Somme de deux variables aléatoires indépendantes}}`{=latex}

Soient $U$ et $V$ indépendantes et admettant les densités $f_U$ et
$f_V$, on cherche la densité de la somme $Z = U+V$. On commence par
compléter $Z$ en le couple $T = (U,Z)$ (par exemple), correspondant à la
bijection $g(u,v) = (u, u+v)$ sur $\mathbb{R}^2$ dont le jacobien est 1
et d'inverse $g^{-1}(x,y) = (x,x-y)$. Appliquant le point 3. ci-dessus,
on obtient :
$$f_Z(z) = \int_{\mathbb{R}}f_U(u)f_V(z-u) du = \int_{\mathbb{R}}f_U(z-v)f_V(v)dv.$$
La fonction $f_Z$ est appelée *le produit de convolution* des des
fonctions $f_U$ et $f_V$.
:::

::: {.section}
#### Exercice -- Loi bêta ($\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$) {#exo-loibeta .exercise .question .three .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Loi bêta}`{=latex}

Soit $X = (U,V)$ un vecteur aléatoire de $\mathbb{R}^2$, avec $U$ et $V$
indépendantes de lois $\Gamma(\alpha,\theta)$ et $\Gamma(\beta,\theta)$.
Identifier la densité de $Y = \frac{U}{U+V}$, puis de $Z = U+V$.
([Solution p.
`\pageref*{answer-exo-loibeta}`{=tex}](#answer-exo-loibeta){.no-parenthesis}.)
:::
:::

::: {.section}
Exercices complémentaires
=========================

::: {.section}
Loi de vie et de mort
---------------------

La durée de vie d'un être vivant ou d'un matériel peut-être assimilée à
une variable aléatoire strictement positive $T$. Dans ce cadre, on peut
définir les notions suivantes :

-   Loi de vie a priori : il s'agit de la loi du temps $T$ caractérisée
    par fonction de répartition complémentaire
    $$G(t) = \mathbb{P}(T>t)$$
-   Loi de survie après $t_0 \geq 0$ : il s'agit de la loi du temps
    $T-t_0$ qu'il lui reste à vivre, sachant qu'il était encore en vie à
    $t_0$, de fonction de répartition complémentaire
    $$G_{t_0}(t) =\mathbb{P}(T>t+t_0|T>t_0)$$

On dira que la loi de vie satisfait la propriété de non vieillissement
(ou d'absence de mémoire) si la loi de survie et la loi de vie sont
égales :
$$\forall t \geq 0 \text{ et } \forall t_0 \geq 0, G_{t_0}(t) = G(t)$$

::: {.section}
#### Question 1 {#viemort1 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Exprimer la loi de survie à partir de la loi de vie a priori. ([Solution
p.
`\pageref*{answer-viemort1}`{=tex}](#answer-viemort1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 {#viemort2 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Montrer qu'une variable aléatoire $T$ satisfait la propriété de
non-vieillissement si et seulement si elle est de loi exponentielle.
([Solution p.
`\pageref*{answer-viemort2}`{=tex}](#answer-viemort2){.no-parenthesis}.)
:::

::: {.section}
#### Question 3 {#viemort3 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

On suppose que $T$ admet une densité continue sur $\mathbb{R}_+^\ast$.
Montrer que l'on peut définir le taux de mort à l'instant $t$ par
$$D(t) = \lim_{\Delta t \to 0} \frac{1}{\Delta t}\mathbb{P}(t < T \leq t + \Delta t | T >t)$$
et exprimer $G$ en fonction de $D$.

Quelles lois correspondent-elles à $D$ constant ? ([Solution p.
`\pageref*{answer-viemort3}`{=tex}](#answer-viemort3){.no-parenthesis}.)
:::
:::

::: {.section}
Durée de vie
------------

La durée de vie, exprimée en années, d'un circuit électronique est une
variable aléatoire $T$ dont la fonction de répartition $F$ est définie
par : $$F (t) = (1 - e^{-t^2 /2} )1_{t\geq 0}$$

::: {.section}
#### Question 1 {#dureevie1 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Donner la densité de probabilité $f$ de $T$ . Calculer $\mathbb{E}(T)$.
([Solution p.
`\pageref*{answer-dureevie1}`{=tex}](#answer-dureevie1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 {#dureevie2 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Sachant que le circuit a déjà fonctionné durant 1 an, quelle est la
probabilité qu'il continue à fonctionner encore durant au moins 2 ans ?
La loi est-elle sans mémoire ?

Un équipement électronique E est composé de 10 circuits identiques et
indépendants. Au circuit $i (1 \leq i \leq 10)$ est associée la variable
aléatoire $X_i$ , avec $X_i = 1$ si la durée de vie du circuit $i$ est
inférieure à un an et $X_i = 0$ sinon. ([Solution p.
`\pageref*{answer-dureevie2}`{=tex}](#answer-dureevie2){.no-parenthesis}.)
:::

::: {.section}
#### Question 3 {#dureevie3 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Quelle est la loi du nombre $N$ de circuits de E dont la durée de vie
est inférieure à 1 an ? ([Solution p.
`\pageref*{answer-dureevie3}`{=tex}](#answer-dureevie3){.no-parenthesis}.)
:::

::: {.section}
#### Question 4 {#dureevie4 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 4}`{=latex}

L'équipement E est dit en série si la défaillance de l'un de ses
circuits entraîne sa défaillance. Quelle est alors la probabilité qu'il
soit défaillant avant 1 an ? ([Solution p.
`\pageref*{answer-dureevie4}`{=tex}](#answer-dureevie4){.no-parenthesis}.)
:::

::: {.section}
#### Question 5 {#dureevie5 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 5}`{=latex}

L'équipement E est dit en parallèle si sa défaillance ne peut se
produire que si tous ses circuits sont défaillants. Quelle est alors la
probabilité qu'il soit défaillant avant 1 an ? ([Solution p.
`\pageref*{answer-dureevie5}`{=tex}](#answer-dureevie5){.no-parenthesis}.)
:::
:::

::: {.section}
Crues centennales de la Seine
-----------------------------

On suppose que la hauteur d'eau maximale au cours de l'année $n$ est
décrite par une variable aléatoire $X_n$ de densité $f(x)$ et de
fonction de répartition $F(x)$, identique pour toutes les $X_n$, que
l'on suppose également indépendantes.

::: {.section}
#### Question 1 {#crue1 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Calculer la fonction de répartition du maximum sur $n$ années
$Y = \max(X_1,\ldots,X_n)$. ([Solution p.
`\pageref*{answer-crue1}`{=tex}](#answer-crue1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 {#crue2 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

En déduire la densité de $Y$. ([Solution p.
`\pageref*{answer-crue2}`{=tex}](#answer-crue2){.no-parenthesis}.)
:::

::: {.section}
#### Question 3 {#crue3 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Expliciter la densité de $Y$ lorsque les $X_i$ sont de loi uniforme sur
$[0,1]$. ([Solution p.
`\pageref*{answer-crue3}`{=tex}](#answer-crue3){.no-parenthesis}.)
:::

::: {.section}
#### Question 4 {#crue4 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 4}`{=latex}

Selon mêmes hypothèses, calculer la hauteur minimale des quais pour que
la probabilité de voir la Seine déborder sur une période de $n$ années
soit inférieure à 1/1000. ([Solution p.
`\pageref*{answer-crue4}`{=tex}](#answer-crue4){.no-parenthesis}.)
:::

::: {.section}
#### Question 5 {#crue5 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 5}`{=latex}

Toujours selon les mêmes hypothèses, calculer la médiane de $Y$. La
comparer avec celle des $X_i$. Commenter. ([Solution p.
`\pageref*{answer-crue5}`{=tex}](#answer-crue5){.no-parenthesis}.)
:::
:::

::: {.section}
Indépendance et vecteurs gaussiens
----------------------------------

Soit $Z := (X,Y)$ un vecteur gaussien (i.e. qui suit une loi Normale
bi-variée) d'espérance $m$ et de matrice de covariance définie positive
$C$. Notons $f_Z$ sa densité.

::: {.section}
#### Question 1 {#covindepgauss-joint .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Rappeler la forme de $f_Z$ et en donner une expression non matricielle
faisant apparaître le coefficient de corrélation noté $\rho$. ([Solution
p.
`\pageref*{answer-covindepgauss-joint}`{=tex}](#answer-covindepgauss-joint){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 {#covindepgauss-marg .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Expliciter les lois marginales de $X$ et de $Y$. ([Solution p.
`\pageref*{answer-covindepgauss-marg}`{=tex}](#answer-covindepgauss-marg){.no-parenthesis}.)
:::

::: {.section}
#### Question 3 {#covindepgauss-indep .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Montrer que $X$ et $Y$ sont indépendantes ssi
$\text{Cov}\left(X,Y\right) = 0$. ([Solution p.
`\pageref*{answer-covindepgauss-indep}`{=tex}](#answer-covindepgauss-indep){.no-parenthesis}.)
:::
:::

::: {.section}
Symétrie de la gaussienne
-------------------------

Soit $X$ une variable aléatoire réelle de loi Normale centrée réduite,
dont la densité est notée $f$ et la fonction de répartition $F$. Pour
tout $c>0$ on pose
$$X_c := \left|\begin{array}{ll} X & \text{si } |X| > c,\\ -X & \text{si } |X| \leq c.\end{array}\right.$$

::: {.section}
#### Question 1 {#gausssym-loi .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Déterminer la loi de $X_c$. ([Solution p.
`\pageref*{answer-gausssym-loi}`{=tex}](#answer-gausssym-loi){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 {#gausssym-cov .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Calculer la covariance de $X$ et de $X_c$ et montrer qu'il existe une
valeur $c_0$ de $c$ qui l'annule. ([Solution p.
`\pageref*{answer-gausssym-cov}`{=tex}](#answer-gausssym-cov){.no-parenthesis}.)
:::

::: {.section}
#### Question 3 {#gausssym-indep .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Les deux variables $X$ et $X_{c_0}$ sont-elles indépendantes ?
([Solution p.
`\pageref*{answer-gausssym-indep}`{=tex}](#answer-gausssym-indep){.no-parenthesis}.)
:::

::: {.section}
#### Question 4 {#gausssym-vecgauss .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 4}`{=latex}

Le vecteur aléatoire $(X,X_{c_0})$ est-il gaussien ? ([Solution p.
`\pageref*{answer-gausssym-vecgauss}`{=tex}](#answer-gausssym-vecgauss){.no-parenthesis}.)
:::
:::

::: {.section}
Loi du $\chi^2$
---------------

On considère une variable aléatoire $X$ gaussienne centrée réduite. On
note $f$ sa densité et $F$ sa fonction de répartition.

::: {.section}
#### A 1 degré de liberté {#khi2-1dl .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{A 1 degré de liberté}`{=latex}

1.  Calculer la densité de la variable aléatoire $Y := X^2$. En donner
    une expression faisant apparaître la fonction gamma (on rappelle que
    $\Gamma\left(\frac{1}{2}\right)=\sqrt{\pi}$).

On dit que $Y$ suit une *loi du $\chi^2$ à $1$ degré de liberté*, et on
note $Y \sim \chi^2$. ([Solution p.
`\pageref*{answer-khi2-1dl}`{=tex}](#answer-khi2-1dl){.no-parenthesis}.)
:::

::: {.section}
#### A n degrés de liberté {#khi2-ndl .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{A n degrés de liberté}`{=latex}

Soient maintenant $n\in\mathbb{N}^\ast$ et $X_1,\dots,X_n$ des copies
indépendantes de $X$. Pour tout $i \in \{1,\dots,n\}$ on pose
$Y_i := X_i^2$.

2.  Montrer que la variable aléatoire $Y := \sum_{i = 1}^n Y_i$ admet
    pour densité
    $$ f_Y : x\in\mathbb{R}\mapsto \left|\begin{array}{ll} \dfrac{x^{\frac{n}{2} - 1}}{2^{\frac{n}{2}}\,\Gamma\left(\frac{n}{2}\right)}\,\exp\left\{ -\dfrac{x}{2} \right\} & \text{si } x> 0,\\ 0 & \text{si } x \leq 0. \end{array}\right.$$
    On pourra procéder par récurrence sur $n$.

On dit que $Y$ suit une *loi du $\chi^2$ à $n$ degrés de liberté* et on
note $Y \sim \chi^2_n$. ([Solution p.
`\pageref*{answer-khi2-ndl}`{=tex}](#answer-khi2-ndl){.no-parenthesis}.)
:::
:::

::: {.section}
Combinaisons linéaires de variables Gaussiennes indépendantes
-------------------------------------------------------------

Soit $X$ une variable aléatoire de loi Normale centrée réduite, dont on
note $f$ la densité et $F$ la fonction de répartition.

::: {.section}
#### Préliminaires {#CLIGauss-pre .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Préliminaires}`{=latex}

1.  Rappeler la loi de la variable aléatoire $s\,X + m$, où
    $s, m \in \mathbb{R}$.

([Solution p.
`\pageref*{answer-CLIGauss-pre}`{=tex}](#answer-CLIGauss-pre){.no-parenthesis}.)
:::

::: {.section}
#### Combinaisons linéaires {#CLIGauss-cl .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Combinaisons linéaires}`{=latex}

Soient maintenant $n\in\mathbb{N}^\ast$ variables aléatoires
$X_1,\dots,X_n$ indépendantes et de même loi que $X$ (on dit que ce sont
des *copies indépendantes* de $X$). Pour tout vecteur
$a = (a_1,\dots,a_n) \in (\mathbb{R}^{*})^n$ on pose
$S_n^a := \sum_{i = 1}^n a_i\,X_i$.

2.  Montrer que pour $S_n^a$ suit une loi Normale d'espérance nulle et
    de variance $\sum_{i = 1}^n a_i^2$ (on pourra raisonner par
    récurrence sur $n$).

3.  Soient $a,b\in(\mathbb{R}^{*})^n$. Sous quelle condition a-t-on
    $\text{Cov}\left(S_n^a, S_n^b\right) = 0$ ?

------------------------------------------------------------------------

([Solution p.
`\pageref*{answer-CLIGauss-cl}`{=tex}](#answer-CLIGauss-cl){.no-parenthesis}.)
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
#### Approximation par une constante {#answer-exo-approx .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Approximation par une constante}`{=latex}

On a
$$\mathbb{E}((X-a)^2) = \mathbb{E}((X-\mathbb{E}(X) + \mathbb{E}(X) - a)^2 = \mathbb{E}((X - \mathbb{E}(X))^2 ) + (\mathbb{E}(X) - a)^2$$
le terme de gauche ne dépend pas de $a$ tandis que celui de droite
s'annule en $a = \mathbb{E}(X)$.
:::

::: {.section}
#### Calcul d'une covariance {#answer-cov-unif .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Calcul d'une covariance}`{=latex}

On a `\begin{align*}
\text{Cov}(U,V) &= \mathbb{E}((U-\mathbb{E}(U))(V-\mathbb{E}(V)))\\
          &= \mathbb{E}(UV - \frac{U}{2} - \frac{U}{2} - \mathbb{E}(U)\mathbb{E}(V))\\
          &= \mathbb{E}(U(1-U)) - 1/4 - 1/4 +1/4 \text{ par linéarité et d'après la solution ci-dessous}\\
          &= 1/2 - 1/3 -1/4 = -1/12
\end{align*}`{=tex} et
$$\rho(U,V) = \frac{\text{Cov}(U,V)}{\sqrt{\mathbb{V}(U)}\sqrt{\mathbb{V}(V)}} = -1$$
:::

::: {.section}
#### Coefficient de corrélation {#answer-CS-corr .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Coefficient de corrélation}`{=latex}

On déduit de l'inégalité de [Cauchy-Schwarz (p.
`\pageref*{CS}`{=tex})](#CS) que
$$|\rho(X,Y)| = \left|\frac{\mathbb{E}((X-\mathbb{E}(X))(X-\mathbb{E}(Y)))}{\sqrt{\mathbb{V}(X)\mathbb{V}(Y)}} \right| \leq \frac{\sqrt{\mathbb{E}((X-\mathbb{E}(X))^2)\mathbb{E}((X-\mathbb{E}(Y))^2)}}{\sqrt{\mathbb{V}(X)\mathbb{V}(Y)}} =1$$
:::

::: {.section}
### Moments d'une variable aléatoire de loi uniforme sur $[a,b]$ {#answer-moments-unif .answser}

Soit $X \sim \mathcal{U}_{[a,b]}$. Son espérance vaut
$$\mathbb{E}(X) = \int_a^b \frac{x}{b-a} dx = \frac{a+b}{2}$$ et puisque
$$\mathbb{E}(X^2) = \int_a^b \frac{x^2}{b-a} dx = \frac{a^2 + ab +b^2}{3},$$
alors sa variance vaut
$$\mathbb{V}(X) = \mathbb{E}(X^2) - \mathbb{E}(X)^2 = \frac{(b-a)^2}{12}.$$
:::

::: {.section}
#### Moments d'une v.a. de loi exponentielle {#answer-moments-expo .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Moments d'une v.a. de loi exponentielle}`{=latex}

Soit $X \sim \mathcal{E}(\theta)$, alors
$$\mathbb{E}(X) = \int_0^{+\infty} x \theta \exp(-\theta x) dx = [\frac{x}{\theta}\exp(-\theta x)]_0^{+\infty} + \int_0^{+\infty} \exp(-\theta x) dx = \frac{1}{\theta}$$
:::

::: {.section}
#### Moments d'une v.a. de loi gamma {#answer-moments-gamma .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Moments d'une v.a. de loi gamma}`{=latex}

Soit $X\sim \Gamma(\alpha,\beta)$. On a `\begin{align*}
\mathbb{E}(X) &= \frac{1}{\Gamma(\alpha)}\int_0^{+\infty} \theta^\alpha x^\alpha e^{-\theta x} dx\\
        &= \frac{1}{\Gamma(\alpha)}\int_0^{+\infty} \frac{1}{\theta} u^\alpha e^{-u} du \text{ par le changement de variable } u = \theta x\\
        &= \frac{\Gamma(\alpha+1)}{\Gamma(\alpha)} \frac{1}{\theta} = \frac{\alpha}{\theta}
\end{align*}`{=tex} puis `\begin{align*}
\mathbb{E}(X^2) &= \frac{1}{\Gamma(\alpha)}\int_0^{+\infty} \theta^\alpha x^{\alpha+1} e^{-\theta x} dx\\
        &= \frac{1}{\Gamma(\alpha)}\int_0^{+\infty} \frac{1}{\theta^2} u^{\alpha+1} e^{-u} du \text{ par le changement de variable } u = \theta x\\
        &= \frac{\Gamma(\alpha+2)}{\Gamma(\alpha)} \frac{1}{\theta^2} = \frac{\alpha(\alpha+1)}{\theta^2}
\end{align*}`{=tex} d'où
$$\mathbb{V}(X) = \mathbb{E}(X^2) - \mathbb{E}(X)^2 = \frac{\alpha}{\theta^2}$$
:::

::: {.section}
#### Moments d'une v.a. gaussienne {#answer-moments-gauss .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Moments d'une v.a. gaussienne}`{=latex}

Pour s'assurer qu'il s'agit bien d'une densité, on remarque que
$I = \int_{-\infty}^{+\infty} f(x) dx$ vérifie
$$ I^2 = \int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} f(x) f(y) dxdy = \int_{0}^{2\pi} d\theta\int_{0}^{+\infty}\frac{1}{2\pi} r e^{-r^2/2}dr $$
(en passant en coordonnées polaires dans l'intégrale double). Le calcul
est ensuite aisé et on obtient $I = 1$.

Pour les moments, on fait d'abord le calcul dans le cas centré réduit
($\mu = 0$ et $\sigma^2 =1$) puis on s'y ramène par le changement de
variable $x \mapsto \frac{x-\mu}{\sigma}$. Soit donc
$X \sim \mathcal{N}(0,1)$, on a `\begin{align*}
\mathbb{E}(X) &= \int_{-\infty}^{+\infty} \frac{x}{\sqrt{2\pi}} e^{-x^2/2} dx\\
         &= \left[-\frac{1}{\sqrt{2\pi}} e^{-x^2/2} \right]_{-\infty}^{+\infty} = 0.
\end{align*}`{=tex} et `\begin{align*}
\mathbb{V}(X) = \mathbb{E}(X^2) &= \int_{-\infty}^{+\infty} \frac{x^2}{\sqrt{2\pi}} e^{-x^2/2} dx\\
         &= \left[-\frac{x}{\sqrt{2\pi}} e^{-x^2/2} \right]_{-\infty}^{+\infty} +\int_{-\infty}^{+\infty} \frac{1}{\sqrt{2\pi}} e^{-x^2/2} dx \\
         &= 0 + 1.
\end{align*}`{=tex}
:::

::: {.section}
#### *Loi de Cauchy* {#answer-exo-cauchy .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{\emph{Loi de Cauchy}}`{=latex}

L'angle $\theta$ est une variable aléatoire uniforme sur
$[-\pi/2,\pi/2]$, de densité
$g(\theta) = \frac{1}{\pi}1_{[ -\pi/2,\pi/2 ]}(\theta)$. L'abscisse $X$
est donnée par $X = \tan \theta$, c'est donc une variable aléatoire, de
fonction de répartition `\begin{align*}        
F(x) & = \mathbb{P}(X \leq x) \\
     & = \mathbb{P}(\theta \leq \arctan x) \\
     & = \int_{-\infty}^{\arctan x} \frac{1}{\pi}1_{[ -\pi/2,\pi/2 ]}(\theta) d\theta \\
     & = \frac{1}{\pi} \arctan x + \frac{1}{2}.
\end{align*}`{=tex}

$F$ est de classe $C^1$ de dérivée
$$f(x) = \frac{1}{\pi(1+x^2)}, x \in \mathbb{R}$$

C'est la densité de la loi de Cauchy. Une variable aléatoire $X$ de loi
de Cauchy n'admet pas d'espérance. En effet,
$\frac{x}{\pi(1+x^2)} \sim_{x\to \infty} \frac{1}{x}$ n'est pas
intégrable.
:::

::: {.section}
#### Lancer de fléchette {#answer-exo-flechette .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Lancer de fléchette}`{=latex}

Les coordonnées cartésiennes de
$M \in D = \{(x,y) \in \mathbb{R}^2 , x^2+y^2 \leq 1\}$ constituent un
couple de variables aléatoires de densité
$$f_{(X,Y)}(x,y) = \frac{1}{\pi}1_{D} (x,y)$$ uniforme sur le disque,
par hypothèse. L'abscisse de $X$ est distribuée selon la densité
marginale
$$f_X(x) = \int f_{(X,Y)}(x,y) dy = \frac{2}{\pi} (1-x^2)^{1/2} 1_{[-1,1]}(x).$$
La loi de $Y$ a la même densité.
:::

::: {.section}
#### Lancer de fléchette (suite) {#answer-exo-flechettebis .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Lancer de fléchette (suite)}`{=latex}

La densité des coordonnées cartésiennes ne s'exprime pas comme le
produit des densités marginales ; elles ne sont pas indépendantes.
:::

::: {.section}
#### Démonstration {#answer-demo-cov-indep .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Démonstration}`{=latex}

Soit $X$ et $Y$ deux v.a. aléatoires indépendantes et de carré
intégrable. On a d'après [la proposition (p.
`\pageref*{indep_fct}`{=tex})](#indep_fct)
$$\mathbb{E}((X-\mathbb{E}(X))(Y-\mathbb{E}(Y))) = \mathbb{E}(X-\mathbb{E}(X))\mathbb{E}(Y-\mathbb{E}(Y)) = 0 = \rho(X,Y)$$
:::

::: {.section}
#### Lancer de fléchette (fin) {#answer-exo-flechetteter .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Lancer de fléchette (fin)}`{=latex}

En coordonnées polaires, le domaine $D$ est décrit par
$D = \{(r,\theta) \in [0,1] \times [0,2\pi]\}$. La densité de
$(R,\theta)$ s'écrit ainsi :
$$f_{(R,\theta)}(r,\theta) = \frac{r}{\pi}1_{D} (r\cos(\theta),r\sin(\theta)) = 2r 1_{[0,1]}(r) \frac{1}{2\pi}1_{[0,2\pi]}(r).$$
Ainsi $R$ et $\Theta$ sont indépendantes de densités respectives
$2r 1_{[0,1]}(r)$ et $\frac{1}{2\pi}1_{[0,2\pi]}(\theta)$.
:::

::: {.section}
#### Loi bêta {#answer-exo-loibeta .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Loi bêta}`{=latex}

On note d'abord que la dimension de $Y$ est plus petite que celle de
$X$. On va donc compléter $Y$ en prenant par exemple $Y' = (Y,Z)$, avec
$Z=U+V$, ce qui correspond à $g(u,v) = \left(\frac{u}{u+v},u+v\right)$.
Cette application est bijective de $A = \left]0,+\infty\right[^2$ dans
$B = \left]0,1\right[ \times \left]0,+\infty\right[$, d'inverse
$g^{-1}(y,z) = (yz,z(1-y))$, qui a pour jacobien $z$.

Comme
$f_X(u,v) = \frac{\theta^{\alpha+\beta}}{\Gamma(\alpha)\Gamma(\beta)}u^{\alpha-1}v^{\beta-1}e^{-\theta(u+v)}1_A(u,v)$,
on a
$$f_{Y'}(y,z) = \frac{\theta^{\alpha+\beta}}{\Gamma(\alpha)\Gamma(\beta)}z^{\alpha+\beta -1}y^{\alpha-1}(1-y)^{\beta-1}e^{-\theta z}1_B(y,z).$$
On obtient alors la densité de Y en intégrant $f_{Y'}(y,z)$ par rapport
à $z\in \left]0,+\infty\right[$ : `\begin{align*}
f_Y(y) &= \int_0^{+\infty} f_{Y'}(y,z) dz\\
       &= \frac{\theta^{\alpha+\beta}}{\Gamma(\alpha)\Gamma(\beta)}y^{\alpha-1}(1-y)^{\beta-1}1_{\left]0,1\right[}(y)\int_0^{+\infty}z^{\alpha+\beta -1}e^{-\theta(z)}dz\\
       &= \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}y^{\alpha-1}(1-y)^{\beta-1}1_{\left]0,1\right[}(y),
\end{align*}`{=tex} où on a utilisé la définition de la fonction gamma
et le changement de variable linéaire $z \mapsto \theta z$. On appelle
loi bêta de paramètres $\alpha$ et $\beta$ la loi admettant cette
densité. Admettant une grande variété de formes, elle permet de
modéliser de nombreuses distributions à support fini.

La loi bêta apparaît naturellement dans une expérience d'urnes, donnée
par George Pólya dans un article de 1930, [*Sur quelques points de la
théorie des
probabilités*](http://www.numdam.org/article/AIHP_1930__1_2_117_0.pdf).
Il décrit l'expérience suivante : on se donne une urne contenant
initialement $r$ boules rouges et $b$ boules bleues, on tire une boule
dans l'urne, puis on la remet dans l'urne avec une deuxième boule de
même couleur. Alors la proportion de boules rouges tend vers une
variable aléatoire de loi Beta$(r,b)$, et, inversement, la proportion de
boules bleues tend vers une variable aléatoire de loi Beta$(b,r)$.

Nous obtenons aussi facilement la densité de $Z$. En effet, on a
$f_{Y'}(y,z) = f_Y(y)f_Z(z)$ ($Y$ et $Z$ sont donc indépendantes), où
$$f_Z(z) = \frac{\theta^{\alpha+\beta}}{\Gamma(\alpha+\beta)}z^{\alpha+\beta -1}e^{-\theta z}1_{\left]0,+\infty\right[}$$
On a ainsi démontré que si $U$ et $V$ sont deux variables aléatoires
indépendantes de lois respectives $\Gamma(\alpha,\theta)$ et
$\Gamma(\beta,\theta)$, alors $U+V$ suit la loi
$\Gamma(\alpha+\beta,\theta)$ et est indépendante de $\frac{U}{U+V}$ qui
suit une loi bêta de paramètres $(\alpha,\beta)$.
:::
:::

::: {.section}
Loi de vie et de mort
---------------------

::: {.section}
#### Question 1 {#answer-viemort1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Par définition, on a
$$ G_{t_0}(t) = \mathbb{P}(T>t+t_0|T>t_0) = \frac{\mathbb{P}(T>t+t_0,T>t)}{\mathbb{P}(T>t)} = \frac{G(t+t_0)}{G(t)}$$
:::

::: {.section}
#### Question 2 {#answer-viemort2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

D'après la question précédente, $G$ vérifie alors
$G(t_0+t) = G(t)G(t_0)$ pour tous $t, t_0 > 0$. Comme $G$ est
décroissante, continue à droite et tend vers 0 à l'infini, on en déduit
que $G(t) = e ^{-\theta t}$, pour un $\theta > 0$. On reconnaît la
fonction de répartition complémentaire d'une loi exponentielle de
paramètre $\theta$.
:::

::: {.section}
#### Question 3 {#answer-viemort3 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

`\begin{align*}
D(t) &= \lim_{\Delta t \to 0} \frac{1}{\Delta t}\mathbb{P}(t < T \leq t + \Delta t | T >t)\\
     &= \lim_{\Delta t \to 0} \frac{1}{\Delta t}\frac{\mathbb{P}(t < T \leq t + \Delta t)}{\mathbb{P}(T >t)}\\
     &= \frac{1}{G(t)} \lim_{\Delta t \to 0} \frac{G(t) - G(t + \Delta t)}{\Delta t}\\
     &= -\frac{g(t)}{G(t)}
\end{align*}`{=tex} Ainsi, $D(t) = \frac{d}{dt}(-\ln G(t))$ et comme
$G(0) = 1$, alors on a pour $t >0$
$$G(t) = \exp\left(-\int_0^tD(s) ds\right)$$ Si $D$ est constant, on
retrouve une loi exponentielle.
:::
:::

::: {.section}
Durée de vie
------------

::: {.section}
#### Question 1 {#answer-dureevie1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

En dérivant, on obtient que la densité de $T$ est
$f(t) = t e^{-t^2/2}1_{t>0}$.

L'espérance vaut :

`\begin{align*}
\mathbb{E}(T) &= \int_0^{+\infty} t^2 e^{-t^2/2} dt\\
        &= \left[-t e^{-t^2/2} \right]_0^{+\infty} + \int_0^{+\infty} e^{-t^2/2} dt \text{ par intégration par parties}\\
        &= \frac{1}{2} \int_{-\infty}^{+\infty} e^{-t^2/2} dt \\
        &= \frac{\sqrt{2\pi}}{2}
\end{align*}`{=tex}
:::

::: {.section}
#### Question 2 {#answer-dureevie2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

La probabilité s'écrit :

$$\mathbb{P}(T\geq 3 |T \geq 1) = \frac{\mathbb{P}(T \geq 3,T \geq 1)}{\mathbb{P}(T \geq 1)} = \frac{\mathbb{P}(T \geq 3)}{\mathbb{P}(T \geq 1)} = \frac{e^{-9/2}}{e^{-1/2}} = e^{-4}$$
:::

::: {.section}
#### Question 3 {#answer-dureevie3 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Les variables aléatoires $X_1 , \ldots , X_{10}$ sont indépendantes et
suivent une loi de Bernoulli de paramètre :
$$ \mathbb{P}(T \leq 1) = F (1) = 1 - e^{- 1/2}$$

On en déduit que la loi de N est la loi binomiale de paramètre
$(10, 1 - e^{- 1/2})$.
:::

::: {.section}
#### Question 4 {#answer-dureevie4 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 4}`{=latex}

La probabilité que l'équipement en série soit défaillant avant 1 an
vaut :
$$ P(N \geq 1) = 1 - \mathbb{P}(N = 0) = 1 - e^{-1/2} \approx 9.9 10 -1 = 99%$$
:::

::: {.section}
#### Question 5 {#answer-dureevie5 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 5}`{=latex}

La probabilité que l'équipement en parallèle soit défaillant avant 1 an
vaut : $$ \mathbb{P}(N = 10) = (1 - e^{-1/2})^10 \approx 8.9 10 -5 $$
:::
:::

::: {.section}
Crues centennales de la Seine
-----------------------------

::: {.section}
#### Question 1 {#answer-crue1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Soit $x\in \mathbb{R}$ `\begin{align*}
F_Y(x) = F(Y\leq x) &= F(X_1\leq x,\ldots,X_n\leq x)\\
           &= \prod_{i=1}^n F(X_i\leq x) \\
           &= F(x)^n
\end{align*}`{=tex} puisque les $X_i$ sont indépendantes et de même loi
:::

::: {.section}
#### Question 2 {#answer-crue2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Soit $x\in \mathbb{R}$ `\begin{align*}
f_Y(x) &= \frac{d}{d x} F_Y(x)\\
       &= \frac{d}{d x} F(x)^n\\
       &= nf(x)F(x)^{n-1}
\end{align*}`{=tex}
:::

::: {.section}
#### Question 3 {#answer-crue3 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

On a alors $f(x) = 1_{[0,1]}(x)$ et
$F(x) = x 1_{[0,1]}(x) + 1_{[1,+\infty]}$. On en déduit
$$ f_Y(x) = n x^{n-1}1_{[0,1]} $$
:::

::: {.section}
#### Question 4 {#answer-crue4 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 4}`{=latex}

On cherche à déterminer $x$ tel que
$\mathbb{P}(Y > x) \leq \frac{1}{1000}$. Or,
$$ \mathbb{P}(Y > x) = 1-\mathbb{P}(Y \leq x) = 1 - F_Y(x) = 1 - F(x)^n = 1-x^n $$
Ainsi
$$ 1-x^n \leq \frac{1}{1000} \Leftrightarrow (1-\frac{1}{1000})^{1/n} \leq x $$
:::

::: {.section}
#### Question 5 {#answer-crue5 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 5}`{=latex}

On rappelle que la médiane est le réel $m$ tel que
$\frac{1}{2} = \mathbb{P}(Y \leq m) = F_Y(m)$.

On cherche donc $m$ tel que $m^n = \frac{1}{2}$, soit
$m = \frac{1}{2^{1/n}}$.

On voit que cette valeur est plus élevée que la médiane des $X_i$ qui
vaut $\frac{1}{2}$. Elle tend même vers 1 lorsque $n$ tend vers
l'infini.
:::
:::

::: {.section}
Indépendance et vecteurs gaussiens
----------------------------------

::: {.section}
#### Question 1 {#answer-covindepgauss-joint .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

D'après le cours, en interprétant les éléments de $\mathbb{R}^2$ comme
des vecteurs colonnes, pour tout $z =(x,y)\in\mathbb{R}^2$ on a $$
f_Z(z) = \dfrac{1}{2\pi\,\sqrt{\det(C)}}\,\exp\left\{ -\dfrac{1}{2}\,\left(z - m\right)^t\,C^{-1}\,\left(z - m\right) \right\}.
$$ Or par construction $C$ peut s'écrire
$$C = \left( \begin{array}{cc} \sigma_X^2 & c\\ c & \sigma_Y^2 \end{array}\right), $$
où $\sigma_X^2 := \mathbb{V}\left(X\right)$,
$\sigma_Y^2 := \mathbb{V}\left(Y\right)$ et
$c = \text{Cov}\left(X,Y\right)$. Comme $C$ est définie positive elle
est inversible, avec $\det(C) = \sigma_X^2\,\sigma_Y^2 - c^2 > 0$ et
$$C^{-1} = \dfrac{1}{\sigma_X^2\,\sigma_Y^2 - c^2}\,\left( \begin{array}{cc} \sigma_Y^2 & -c\\ -c & \sigma_X^2 \end{array}\right).$$
En outre, $m = \left(m_X, m_Y \right)$ avec $m_X := \mathbb{E}(X)$ et
$m_Y := \mathbb{E}(Y)$. On en déduit que `\begin{align*}
f_Z(x,y) &= \dfrac{1}{2\pi\,\sqrt{\sigma_X^2\,\sigma_Y^2 - c^2}}\,\exp\biggl\{ \dfrac{-1}{2\,\left(\sigma_X^2\,\sigma_Y^2 - c^2 \right)}\times\\
&\ \ \ \left( \sigma_Y^2\,(x-m_X)^2 - 2c\,(x-m_X)\,(y-m_Y) + \sigma_X^2\,(y-m_Y)^2 \right) \biggr\}\\
&= \dfrac{1}{2\pi\,\sigma_X\,\sigma_Y\,\sqrt{1-\rho^2}}\,\,\exp\biggl\{ \dfrac{-1}{2\,\left( 1 - \rho^2 \right)}\times\\
&\ \ \ \left( \dfrac{(x-m_X)^2}{\sigma_X^2} - 2\rho\,\dfrac{(x-m_X)}{\sigma_X}\,\dfrac{(y-m_Y)}{\sigma_Y} + \dfrac{(y-m_Y)^2}{\sigma_Y^2} \right) \biggr\}.
\end{align*}`{=tex}
:::

::: {.section}
#### Question 2 {#answer-covindepgauss-marg .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Ici, pour $x,y \in \mathbb{R}^2$, on remarque que : `\begin{align*}
f_Z(x,y) &= \dfrac{1}{2\pi\,\sigma_X\,\sigma_Y\,\sqrt{1-\rho^2}}\,\,\exp\biggl\{ \dfrac{-1}{2\,\left( 1 - \rho^2 \right)}\times\\
&\ \ \ \left( \left(\dfrac{y-m_Y}{\sigma_Y} - \rho\,\dfrac{x-m_X}{\sigma_X}\right)^2 + (1 - \rho^2)\,\dfrac{(x-m_X)^2}{\sigma_X^2} \right) \biggr\}\\
& = \dfrac{1}{\sqrt{2\pi}\,\sigma_X}\,\exp\left\{-\dfrac{(x-m_X)^2}{2\,\sigma_X^2} \right\}\times\\
&\ \ \ \dfrac{1}{\sqrt{2\pi}\,\sigma_Y\,\sqrt{1-\rho^2}}\,\exp\left\{-\dfrac{1}{2\,(1-\rho^2)}\,\left(\dfrac{y-m_Y}{\sigma_Y} - \rho\,\dfrac{x-m_X}{\sigma_X}\right)^2 \right\}.
\end{align*}`{=tex} Ainsi, avec le changement de variable
$u = \dfrac{y-m_Y}{\sigma_Y}$ on obtient `\begin{align*}
f_X(x) &= \int_{-\infty}^{+\infty} f_Z(x,y)\,dy\\
&= \dfrac{1}{\sqrt{2\pi}\,\sigma_X}\,\exp\left\{-\dfrac{(x-m_X)^2}{2\,\sigma_X^2} \right\}\times\\
&\ \ \ \int_{-\infty}^{+\infty} \dfrac{1}{\sqrt{2\pi}\,\sqrt{1-\rho^2}}\,\exp\left\{-\dfrac{1}{2\,(1-\rho^2)}\,\left(u - \rho\,\dfrac{x-m_X}{\sigma_X}\right)^2 \right\}\,du,
\end{align*}`{=tex} et on reconnaît dans cette dernière intégrale la
densité d'une loi Normale d'espérance $\rho\,\dfrac{x-m_X}{\sigma_X}$ et
de variance $1-\rho^2$. Cette intégrale vaut donc $1$ et on conclut que
$$f_X(x) = \dfrac{1}{\sqrt{2\pi}\,\sigma_X}\,\exp\left\{-\dfrac{(x-m_X)^2}{2\,\sigma_X^2} \right\}, $$
qui correspond à la densité d'une loi Normale d'espérance $m_X$ et de
variance $\sigma_X^2$.

En procédant de manière symétrique, on obtient de même que $Y$ suit une
loi Normale d'espérance $m_Y$ et de variance $\sigma_Y^2$.
:::

::: {.section}
#### Question 3 {#answer-covindepgauss-indep .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Le premier sens est évident : si $X$ et $Y$ sont indépendantes, alors
nous avons vu dans le cours que $\text{Cov}\left(X,Y\right) = 0$, et ce
que l'on soit gaussien ou non.

Supposons maintenant que $\text{Cov}\left(X,Y\right) = 0$, et montrons
l'indépendance entre $X$ et $Y$. En reprenant la formule de la question
1 et en remplaçant $\rho$ par $0$, pour tout $(x,y) \in \mathbb{R}^2$ on
a: `\begin{align*}
f_Z(x,y) &= \dfrac{1}{2\,\pi\,\sigma_X\,\sigma_Y}\,\exp\left\{ -\dfrac{1}{2}\,\left( \dfrac{(x-\mu_X)^2}{\sigma_X^2} + \dfrac{(y-\mu_Y)^2}{\sigma_Y^2} \right) \right\}\\
&= \dfrac{1}{\sqrt{2\pi}\,\sigma_X}\,\exp\left\{ -\dfrac{(x-m_X)^2}{2\,\sigma_X^2} \right\} \times \dfrac{1}{\sqrt{2\pi}\,\sigma_Y}\,\exp\left\{ -\dfrac{(y-m_Y)^2}{2\,\sigma_Y^2} \right\}\\
&= f_X(x)\times f_Y(y)
\end{align*}`{=tex} d'après la question 2. On en conclut que $X$ et $Y$
sont bien indépendantes.
:::
:::

::: {.section}
Symétrie de la gaussienne
-------------------------

::: {.section}
#### Question 1 {#answer-gausssym-loi .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Nous avons admis dans le cours que la fonction de répartition $F_c$ de
$X_c$ caractérisait sa loi. Nous allons donc l'expliciter. Soit
$x \in \mathbb{R}$. Par définition de la fonction de répartition d'une
variable aléatoire et d'après la formule des probabilités totales, on a
`\begin{align*}
F_c(x) &= \mathbb{P}\left(X_c \leq x\right) = \mathbb{P}\left( X_c \leq x, |X| > c \right) + \mathbb{P}\left( X_c \leq x, |X| \leq c\right)\\
&= \mathbb{P}\left( X\leq x, |X| > c \right) + \mathbb{P}\left(-X \leq x, |X| \leq c\right)\\
&= \mathbb{P}\left( X\leq x, X > c \right) + \mathbb{P}\left(X \leq x, X < -c \right) + \mathbb{P}\left( X \geq -x, -c \leq X \leq c\right).
\end{align*}`{=tex} Or
$$\mathbb{P}\left( X\leq x, X > c \right) = \left|\begin{array}{ll} \mathbb{P}\left(c < X \leq x \right) = F(x) - F(c) & \text{si } x > c,\\ 0 & \text{si } x\leq c,\end{array}\right.$$
$$ \mathbb{P}\left(X \leq x, X < -c \right) = \mathbb{P}\left( X \leq \min\{-c,x\} \right) = F\left(\min\{-c,x\}\right), $$
$$ \mathbb{P}\left( X \geq -x, -c \leq X \leq c\right) = \left|\begin{array}{ll} \mathbb{P}\left(-c \leq X \leq c \right) = F(c) - F(-c) & \text{si } x > c, \\ \mathbb{P}\left(-x \leq X \leq c \right) = F(c) - F(-x) & \text{si } -c \leq x \leq c,\\ 0 & \text{si } x<-c. \end{array}\right.$$
Ainsi,

-   si $x > c$ alors $\min\{-c,x\} = -c$ et
    $$F_c(x) = F(x) - F(c) + F\left(\min\{-c,x\}\right) + F(c) - F(-c) = F(x),$$

-   si $-c \leq x \leq c$ alors $\min\{-c,x\} = -c$ et
    $$F_c(x) = F\left(\min\{-c,x\}\right) + F(c) - F(-x) = 1 - F(c) + F(c) - 1 + F(x) = F(x)$$
    car la densité de la loi Normale centrée réduite est paire, ce qui
    implique que $F(-x) = 1 - F(x)$ pour tout $x\in\mathbb{R}$,

-   si $x < -c$ alors $\min\{-c,x\} = x$ et
    $$F_c(x) =  F\left(\min\{-c,x\}\right) = F(x).$$

On en conclut que $F_c = F$ : $X_c$ a la même loi que $X$. Ce résultat
est dû à la symétrie de la densité de la loi Normale centrée réduite. On
remarque d'ailleurs que le résultat resterait inchangé si l'on prenait
n'importe quelle autre loi de densité paire !
:::

::: {.section}
#### Question 2 {#answer-gausssym-cov .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Tout d'abord, par définition,
$$\text{Cov}\left(X,X_c\right) = \mathbb{E}\left( \left(X - \mathbb{E}\left(X\right)\right)\,\left(X_c - \mathbb{E}\left(X_c\right) \right) \right) = \mathbb{E}\left(X\,X_c \right) $$
puisque $X$ et $X_c$ sont gaussiennes centrées (d'espérance nulle)
réduites. Or on remarque que l'on peut écrire
$X_c = X\,1_{\mathbb{R}\backslash[-c,c]}(X) - X\,\,1_{[-c,c]}(X)$. On
déduit par linéarité de l'espérance que `\begin{align*}
\mathbb{E}\left(X\,X_c\right) &= \mathbb{E}\left(X^2\,1_{\mathbb{R}\backslash[-c,c]}(X) - X^2\,1_{[-c,c]}(X)\right)\\
&= \mathbb{E}\left(X^2\,\left(1_{\mathbb{R}\backslash[-c,c]}(X) + 1_{[-c,c]}(X) - 1_{[-c,c]}(X)\right) - X^2\,1_{[-c,c]}(X)\right)\\
&= \mathbb{E}\left(X^2\right) - 2\,\mathbb{E}\left(X^2\,1_{[-c,c]}(X)\right).
\end{align*}`{=tex} Etant donné que $X$ est de loi Normale centrée
réduite, on a directement que $\mathbb{E}\left(X^2\right)=1$; il suffit
donc de calculer la dernière espérance pour obtenir le résultat. Comme
$x\mapsto x^2\,1_{[-c,c]}(x)$ est bornée et continue sur
$\mathbb{R}\backslash\{-c,c\}$ (donc continue presque partout), elle est
intégrable et
$$\mathbb{E}\left(X^2\,1_{[-c,c]}(X)\right) = \int_{-\infty}^{+\infty} x^2\,1_{[-c,c]}\,f(x)\,dx = \int_{-c}^c x^2\,f(x)\,dx. $$
Or on pourra remarquer que $f^\prime(x) = -x\,f(x)$ puis que
$f^{\prime\prime}(x) = (x^2-1)\,f(x)$. Puisque $f$, $f^\prime$ et
$f^{\prime\prime}$ sont continues et bornées (voir l'exercice *Densité
et fonction de répartition d'une loi Normale* du chapitre Probabilités
I) elles sont intégrables sur des segments. On en déduit que
`\begin{align*}
\mathbb{E}\left(X^2\,1_{[-c,c]}(X)\right) &= \int_{-c}^c (x^2-1)\,f(x)\,dx + \int_{-c}^c f(x)\,dx\\
&= \left[-x\,f(x) \right]_{-c}^c + F(c) - F(-c)\\
&= -c\,\left(f(c) + f(-c)\right) + F(c) - F(-c)\\
&= 2\,\left(F(c) - c\,f(c)\right) - 1
\end{align*}`{=tex} par parité de $f$. On en conclut que
$\text{Cov}\left(X,X_c\right) = 3 + 4\,\left(c\,f(c) - F(c)\right)$.

La fonction
$g : c\in\mathbb{R}_+^\ast \mapsto 3+4\,\left(c\,f(c) - F(c)\right)$ est
continue, infiniment dérivable et pour tout $c > 0$ on a
$g^\prime(c) = -4\,c^2\,f(c) < 0$. Par conséquent, $g$ est strictement
décroissante, avec $\lim\limits_{c\to0^+} g(c) = 1$ et
$\lim\limits_{c\to+\infty} g(c) = -1$. Le théorème des valeurs
intermédiaires nous permet de conclure qu'il existe bien un unique
$c_0 > 0$ tel que $g(c_0) = 0$.
:::

::: {.section}
#### Question 3 {#answer-gausssym-indep .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Les variables aléatoires $X$ et $X_{c_0}$ sont indépendantes ssi pour
tous ensembles $A,B \in \mathcal{E}_\mathbb{R}$ on a
$$\mathbb{P}\left(X \in A, X_{c_0} \in B \right) = \mathbb{P}\left(X \in A\right)\,\mathbb{P}\left(X_{c_0} \in B \right).$$

Or si l'on prend $A = B = ]-\infty, x]$ où $x < -c_0$, alors
`\begin{align*}
\mathbb{P}\left( X \leq x, X_{c_0} \leq x \right) &= \mathbb{P}\left( X \leq x, X < -c_0 \right) + \mathbb{P}\left( X \leq x, X > c_0 \right)\\
&\ \ \ + \mathbb{P}\left( X\leq x, X \geq -x, -c_0 \leq X \leq c_0 \right)\\
&= \mathbb{P}\left( X \leq x \right) +0 + 0 = F(x)\\
& \neq F(x)\,F(x) = \mathbb{P}\left( X \leq x \right)\,\mathbb{P}\left(X_{c_0} \leq x \right).
\end{align*}`{=tex}

On en conclut que bien que $\text{Cov}\left(X,X_{c_0}\right) = 0$, $X$
et $X_{c_0}$ ne sont pas indépendantes.
:::

::: {.section}
#### Question 4 {#answer-gausssym-vecgauss .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 4}`{=latex}

Supposons que $(X,X_{c_0})$ soit un vecteur gaussien. Alors, puisque
$\text{Cov}\left(X,X_{c_0}\right) = 0$, $X$ et $X_{c_0}$ sont
nécessairement indépendantes. Or nous venons de voir que ce n'était pas
le cas; nous avons donc contradiction. On en conclut que $(X,X_{c_0})$
n'est pas gaussien.
:::
:::

::: {.section}
Loi du $\chi^2$
---------------

::: {.section}
#### A 1 degré de liberté {#answer-khi2-1dl .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{A 1 degré de liberté}`{=latex}

1.  Soit $h : \mathbb{R}\to \mathbb{R}$ une fonction mesurable telle que
    $h\times f$ est intégrable. Alors en opérant le changement de
    variable $u = x^2$ on a `\begin{align*}
    \mathbb{E}\left( h(Y) \right) &= \mathbb{E}\left(h(X^2)\right) = \int_{\mathbb{R}} h(x^2)\,f(x)\,dx\\
    & = \int_{-\infty}^{0} h(x^2)\,f(x)\,dx + \int_{0}^{+\infty} h(x^2)\,f(x)\,dx\\
    &= \int_{0}^{+\infty} h(u)\,f\left(-\sqrt{u}\right)\,\dfrac{1}{2\,\sqrt{u}} \,du + \int_{0}^{+\infty} h(u)\,f\left(\sqrt{u}\right)\,\dfrac{1}{2\,\sqrt{u}} \,du.
    \end{align*}`{=tex} Or $f$ est paire, donc pour tout
    $u \in \mathbb{R}^+$ on a
    $f\left(-\sqrt{u}\right) = f\left(\sqrt{u}\right)$ et
    `\begin{align*}
    \mathbb{E}\left( h(Y) \right) &= \int_{\mathbb{R}_+} h(u)\,f\left(\sqrt{u}\right)\,\dfrac{1}{\sqrt{u}} \,du.
    \end{align*}`{=tex} Par propriété $Y$ possède donc une densité $f_Y$
    valant pour tout $x\in\mathbb{R}$
    $$f_Y(x) = \left|\begin{array}{ll} f\left(\sqrt{x}\right)\,\dfrac{1}{\sqrt{x}} = \dfrac{x^{-\frac{1}{2}}}{2^{\frac{1}{2}}\,\Gamma\left(\frac{1}{2}\right)}\,\exp\left\{-\dfrac{x}{2}\right\} & \text{si } x > 0,\\ 0 & \text{si } x \leq 0. \end{array}\right. $$

**Remarque.** La fonction $f_Y$ est bien une densité : elle est continue
par morceaux donc mesurable, puis positive, et son intégrale sur
$\mathbb{R}$ vaut bien $1$ : `\begin{align*}
\int_{\mathbb{R}} f_Y(x)\,dx &= \dfrac{1}{2\,\Gamma\left(\frac{1}{2}\right)}\,\int_{0}^{+\infty} \left(\dfrac{x}{2}\right)^{\frac{1}{2}-1}\,\exp\left\{-\dfrac{x}{2}\right\}\,dx \\
&= \dfrac{1}{\Gamma\left(\frac{1}{2}\right)}\,\int_{0}^{+\infty} u^{\frac{1}{2}-1}\,e^{-u}\,du = \dfrac{\Gamma\left(\frac{1}{2}\right)}{\Gamma\left(\frac{1}{2}\right)} = 1.
\end{align*}`{=tex}
:::

::: {.section}
#### A n degrés de liberté {#answer-khi2-ndl .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{A n degrés de liberté}`{=latex}

2.  On note $(\mathcal{P}_n)$ la propriété à démonter au rang $n$.

**Initialisation.** Nous avons vu à la question précédente que
$(\mathcal{P}_1)$ est vraie.

**Hérédité.** Soit maintenant $n \geq 2$ et supposons
$(\mathcal{P}_{n-1})$ vraie. Alors $Y = \sum_{i = 1}^{n-1}Y_i + Y_n$ est
la somme de deux variables aléatoires indépendantes, dont la première
suit un $\chi_{n-1}^2$ de densité notée $f_{n-1}$ et la seconde un
$\chi_1^2$ de densité notée $f_1$. Elle possède donc une densité, égale
au produit de convolution de $f_{n-1}$ et $f_1$ : pour tout
$x\in\mathbb{R}$
$$f_Y(x) = \int_{\mathbb{R}} f_1(x-u)\,f_{n-1}(u)\,du.$$ Or pour tout
$x,u\in\mathbb{R}$ on a $f_1(x-u) = 0$ ssi $x \leq u$ et
$f_{n-1}(u) = 0$ ssi $u \leq 0$. Donc leur produit est strictement
positif ssi $x > u > 0$, nul sinon. La densité $f_Y$ est par conséquent
nulle sur $\mathbb{R}^-$ et nous allons maintenant exhiber son
expression sur $\mathbb{R}_+^\ast$. Soit $x > 0$, alors `\begin{align*}
f_Y(x) &= \int_{0}^{x} \dfrac{(x-u)^{-\frac{1}{2}}}{\sqrt{2}\,\Gamma\left(\frac{1}{2}\right)}\,\exp\left\{-\dfrac{x-u}{2}\right\}\,\dfrac{u^{\frac{n-1}{2}-1}}{2^{\frac{n-1}{2}}\,\Gamma\left(\frac{n-1}{2}\right)}\,\exp\left\{-\dfrac{u}{2}\right\} \,du\\
&= \dfrac{\exp\left\{-\dfrac{x}{2} \right\}}{2^{\frac{n}{2}}\,\Gamma\left(\frac{1}{2}\right)\Gamma\left(\frac{n-1}{2}\right)} \,\int_0^x \left(x-u\right)^{-\frac{1}{2}}\,u^{\frac{n-3}{2}}\,du.
\end{align*}`{=tex} Avec le changement de variable $v=\dfrac{u}{x}$ on
obtient `\begin{align*}
f_Y(x) &= \dfrac{x^{\frac{n}{2}-1}\,\exp\left\{-\dfrac{x}{2} \right\}}{2^{\frac{n}{2}}\,\Gamma\left(\frac{1}{2}\right)\Gamma\left(\frac{n-1}{2}\right)} \,\int_0^{1} v^{\frac{n-3}{2}}\,\left(1 - v\right)^{-\frac{1}{2}} \,dv.
\end{align*}`{=tex} Or $f_Y$ est une densité, son intégrale vaut donc
$1$ : `\begin{align*}
\int_{\mathbb{R}} f_Y(x)\,dx &= \int_0^{+\infty} \dfrac{x^{\frac{n}{2}-1}\,\exp\left\{-\dfrac{x}{2} \right\}}{2^{\frac{n}{2}}\,\Gamma\left(\frac{1}{2}\right)\Gamma\left(\frac{n-1}{2}\right)}\,\left(\int_0^{1} v^{\frac{n-3}{2}}\,\left(1 - v\right)^{-\frac{1}{2}} \,dv\right)\,dx\\
&= \left(\int_0^{1} v^{\frac{n-3}{2}}\,\left(1 - v\right)^{-\frac{1}{2}} \,dv\right)\,\left(\int_0^{+\infty} \dfrac{x^{\frac{n}{2}-1}\,\exp\left\{-\dfrac{x}{2} \right\}}{2^{\frac{n}{2}}\,\Gamma\left(\frac{1}{2}\right)\Gamma\left(\frac{n-1}{2}\right)}\,dx\right)\\
& \left(\int_0^{1} v^{\frac{n-3}{2}}\,\left(1 - v\right)^{-\frac{1}{2}} \,dv\right)\,\left(\int_0^{+\infty} \dfrac{x^{\frac{n}{2}-1}\,\exp\left\{-x \right\}}{\Gamma\left(\frac{1}{2}\right)\Gamma\left(\frac{n-1}{2}\right)}\,dx\right)\\
&= \left(\int_0^{1} v^{\frac{n-3}{2}}\,\left(1 - v\right)^{-\frac{1}{2}} \,dv\right)\,\left( \dfrac{\Gamma\left(\frac{n}{2}\right)}{\Gamma\left(\frac{1}{2}\right)\Gamma\left(\frac{n-1}{2}\right)}\right) = 1.
\end{align*}`{=tex}

On en déduit que
$$ \int_0^{1} v^{\frac{n-3}{2}}\,\left(1 - v\right)^{-\frac{1}{2}} \,dv = \dfrac{\Gamma\left(\frac{1}{2}\right)\Gamma\left(\frac{n-1}{2}\right)}{\Gamma\left(\frac{n}{2}\right)}, $$
et finalement que pour tout $x\in\mathbb{R}$
$$f_Y(x) = \left|\begin{array}{ll} \dfrac{x^{\frac{n}{2}-1}}{2^{\frac{n}{2}}\,\Gamma\left(\frac{n}{2}\right)}\,\exp\left\{-\dfrac{x}{2}\right\} & \text{si } x> 0,\\ 0 & \text{sinon;}\end{array}\right.$$
$(\mathcal{P}_n)$ est donc vraie.

**Conclusion.** La propriété est vraie pour tout $n\in\mathbb{N}^\ast$.
:::
:::

::: {.section}
Combinaisons linéaires de variables Gaussiennes indépendantes
-------------------------------------------------------------

::: {.section}
#### Préliminaires {#answer-CLIGauss-pre .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Préliminaires}`{=latex}

Cette question a été traitée de manière générale dans le cours. Nous en
proposons une preuve alternative, basée sur le calcul de la fonction de
répartition de la variable aléatoire $s\,X + m$, qui caractérise sa loi.
Elle dépend clairement des valeurs de $s$.

-   Si $s = 0$, alors $s\,X + m$ est toujours égale à $m$ : sa loi est
    une masse de Dirac en $\{m\}$ et pour tout $x\in\mathbb{R}$ on a
    $\mathbb{P}\left(s\,X +m \leq x\right) = 1_{[m,+\infty[}(x)$.

-   Si $s\neq 0$, alors pour tout $x\in\mathbb{R}$ on a
    $$\mathbb{P}\left( s\,X + m \leq x \right) = \left|\begin{array}{ll}\displaystyle\mathbb{P}\left( X \leq \dfrac{x-m}{s} \right) = \int_{-\infty}^{\frac{x-m}{s}} f(u)\,du & \text{si } s>0,\\[1em] \displaystyle \mathbb{P}\left( X \geq \dfrac{x-m}{s} \right) = \int_{\frac{x-m}{s}}^{+\infty} f(u)\,du & \text{si } s<0,\end{array}\right.$$
    qui en posant le changement de variable $v = s\,x+m$ donne
    $$\mathbb{P}\left( s\,X + m \leq x \right) = \int_{-\infty}^{x} \dfrac{1}{|s|}\,f\left(\dfrac{u-m}{s} \right)\,dx.$$
    Ainsi, $s\,X+m$ admet une densité, qui pour tout $x\in\mathbb{R}$
    est égale à
    $$ \dfrac{1}{|s|}\,f\left(\dfrac{u-m}{s}\right) = \dfrac{1}{\sqrt{2\,\pi}\,|s|}\,\exp\left\{-\dfrac{(x-m)^2}{2\,s^2} \right\}.$$
    On reconnaît la densité d'une loi Normale d'espérance $m$ et de
    variance $s^2$.
:::

::: {.section}
#### Combinaisons linéaires {#answer-CLIGauss-cl .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Combinaisons linéaires}`{=latex}

2.  Commençons par supposer que pour tout $n\in\mathbb{N}^\ast$,
    $a\in\mathbb{R}^n$ est tel qu'aucune de ses composantes n'est nulle.
    Nous allons montrer par récurrence sur $n$ que $S_n^a$ suit une loi
    Normale d'espérance nulle et de variance $\sum_{i = 1}^n a_i^2$. On
    note cette propriété $(\mathcal{P}_n)$.

**Initialisation.**

-   Si $n = 1$ et $a_1 \neq 0$, alors $S_1^a = a_1\,X_1$ suit une loi
    Normale centrée de variance $a_1^2$ d'après la question 1;
    $(\mathcal{P}_1)$ est donc vraie.

-   Si $n=2$ et $a_1,a_2 \neq 0$, alors d'après le cours
    $S_2^a = a_1\,X_1 + a_2\,X_2$ admet une densité, notée $f_n^a$,
    égale au produit de convolution des densités $f_1$ de $a_1\,X_1$ et
    $f_2$ de $a_2\,X_2$. En outre, d'après la question 1, pour tout
    $x\in\mathbb{R}$ on a
    $f_1(x) = \dfrac{1}{|a_1|}\,f\left(\dfrac{x}{a_1} \right)$ et
    $f_2(x) = \dfrac{1}{|a_2|}\,f\left(\dfrac{x}{a_2} \right)$. Par
    conséquent, pour tout $x\in\mathbb{R}$, `\begin{align*}
    f_2^a(x) &= \int_{\mathbb{R}} f_1(x-u)\,f_2(u)\,du = \int_\mathbb{R}\dfrac{1}{|a_1|\,|a_2|}\,f\left(\dfrac{x - u}{a_1}\right)\,f\left(\dfrac{u}{a_2}\right)\,du\\
    &= \dfrac{1}{\sqrt{a_1^2 +a_2^2}}\,f\left(\dfrac{x}{\sqrt{a_1^2+a_2^2}}\right)\, \int_{\mathbb{R}} \dfrac{\sqrt{a_1^2+a_2^2}}{|a_1|\,|a_2|}\,\dfrac{f\left(\dfrac{x - u}{a_1}\right)}{f\left(\dfrac{x}{\sqrt{a_1^2+a_2^2}}\right)}\,f\left(\dfrac{u}{a_2}\right)\,du.
    \end{align*}`{=tex} Or pour tout $x,u\in\mathbb{R}$ on a
    `\begin{align*}
    \dfrac{f\left(\dfrac{x - u}{a_1}\right)}{f\left(\dfrac{x}{\sqrt{a_1^2+a_2^2}}\right)}\,f\left(\dfrac{u}{a_2}\right) & = \dfrac{1}{\sqrt{2\pi}}\,\dfrac{\exp\left\{-\dfrac{(x-u)^2}{2\,a_1^2} \right\}}{\exp\left\{ -\dfrac{x^2}{2\,(a_1^2+a_2^2)} \right\}}\,\exp\left\{ -\dfrac{u^2}{2\,a_2^2} \right\}\\
    & = \dfrac{1}{\sqrt{2\pi}}\,\exp\left\{-\dfrac{1}{2}\,\left( \dfrac{(x-u)^2}{a_1^2} + \dfrac{u^2}{a_2^2} - \dfrac{x^2}{a_1^2+a_2^2} \right) \right\}\\
    &= \dfrac{1}{\sqrt{2\pi}}\,\exp\left\{ -\dfrac{\left(a_2^2\,x - (a_1^2 + a_2^2)\,u\right)^2}{2\,a_1^2\,a_2^2\,(a_1^2+a_2^2)} \right\}\\
    &= \dfrac{1}{\sqrt{2\pi}}\,\exp\left\{-\dfrac{\left(u - \dfrac{a_2^2\,x}{a_1^2 + a_2^2}\right)^2}{2\,\dfrac{a_1^2\,a_2^2}{a_1^2+a_2^2}}\right\},
    \end{align*}`{=tex} qui multiplié par
    $\dfrac{\sqrt{a_1^2+a_2^2}}{|a_1|\,|a_2|}$ correspond à la densité
    d'une loi Normale d'espérance $\dfrac{a_2^2\,x}{a_1^2+a_2^2}$ et de
    variance $\dfrac{a_1^2\,a_2^2}{a_1^2+a_2^2}$. La précédente
    intégrale vaut donc $1$ et $(\mathcal{P}_2)$ est vraie.

**Héritage.** Soit maintenant $n\geq 2$, et supposons
$(\mathcal{P}_{n-1})$ vraie. Alors
$S_n^a = S_{n-1}^{a_{-n}} + a_n\,X_n$, où
$a_{-n} := (a_1,\dots,a_{n-1})$. Or $S_{n-1}^{a_{-n}}$ et $a_n\,X_n$
sont des variables gaussiennes centrées, de variances respectives
$\sum_{i = 1}^{n-1} a_i^2$ d'après $(\mathcal{P}_{n-1})$ et $a_n^2$
d'après la question 1. Par $(\mathcal{P}_2)$, $S_n^a$ suit donc une loi
Normale centrée de variance $\sum_{i = 1}^n a_i^2$.

**Conclusion.** On en conclut que $(\mathcal{P}_n)$ est vraie pour tout
$n\in\mathbb{N}^\ast$.

3.  Calculons cette covariance : `\begin{align*}
    \text{Cov}\left(S_n^a, S_n^b\right) &= \text{Cov}\left(\sum_{i =1}^n a_i\,X_i, \sum_{j = 1}^n b_j\,X_j\right)\\
    &= \sum_{i = 1}^n a_i\,b_i\,\mathbb{V}\left(X_i\right) + \sum_{1\leq i\neq j \leq n} a_i\,b_j\,\text{Cov}\left(X_i,X_j\right).
    \end{align*}`{=tex} Or par hypothèse
    $\mathbb{V}\left(X_i\right) = 1$ pour tout $i\in\{1,\dots,n\}$ et
    par indépendance on a $\text{Cov}\left(X_i,X_j\right) = 0$ pour tous
    $i,j \in \{1,\dots,n\}$ tels que $i\neq j$. Ainsi,
    $$ \text{Cov}\left(S_n^a, S_n^b\right) = \sum_{i = 1}^n a_i\,b_i $$
    qui est nulle ssi $a$ et $b$ sont orthogonaux.
:::
:::
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
