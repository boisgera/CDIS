---
author:
- 'STEP, MINES ParisTech[^1]'
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
title: 'Examen -- Calcul Différentiel, Intégral et Stochastique'
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

-   [Calcul intégral](#calcul-intégral)
    -   [Préambule](#préambule)
    -   [Intervalle borné](#intervalle-borné)
-   [Calcul Différentiel](#calcul-différentiel)
    -   [Préliminaires dans
        $\mathbb{R}^2$](#préliminaires-dans-mathbbr2)
    -   [Cadre général](#cadre-général)
-   [Probabilités](#probabilités)
    -   [Préliminaires -- Espérance et fonction de
        répartition](#préliminaires-espérance-et-fonction-de-répartition)
    -   [Etude du maximum -- Loi de
        Fréchet](#etude-du-maximum-loi-de-fréchet)

```{=tex}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}
\newcommand{\Esp}{\mathbb{E}}
\renewcommand{\P}{\mathbb{P}}
```
```{=tex}
\newcommand{\cC}{C}
```
```{=tex}
\newcommand{\cD}{\mathcal{D}}
```
L'examen comporte 3 exercices indépendants notés comme suit :

  Intitulé de l'exercice    Barême   Hors barême
  ------------------------ -------- -------------
  Calcul Intégral           20 pts     +4 pts
  Calcul Différentiel       20 pts     +6 pts
  Probabilités              20 pts     +8 pts

Utilisez un jeu de copies différent pour chaque exercice et indiquez
l'intitulé de l'exercice en en-tête de chaque copie.

::: {.section}
Calcul intégral
===============

Soient $(a_k)_{k \in \mathbb{N}}$ et $(b_k)_{k \in \mathbb{N}}$ deux
suites de réels positifs. $$
\mbox{pour tout } k \in \mathbb{N}, \, 0 \leq a_k < + \infty \, \mbox{ et } \, \, 0 \leq b_k < +\infty.
$$ Soit $(x_k)_{k \in \mathbb{N}}$ la suite de valeurs définie par
$x_0 = 0$ et pour tout $k \in \mathbb{N}$, $$
x_{2k+1} = x_{2k} + a_k \; \mbox{ et } \;
x_{2k+2} = x_{2k+1} + b_k.
$$ ($x_0=0$, $x_1=a_0$, $x_2 = a_0 + b_0$, $x_3 = a_0 + b_0 + a_1$,
$x_4 =a_0 + b_0 + a_1 + b_1$, etc.). On définit la fonction
$f: \mathbb{R}\to \mathbb{R}$ par $$
f(x) = \left\{
\begin{array}{rl}
+1 & \mbox{s'il existe $k \in \mathbb{N}$ tel que $x_{2k} \leq x < x_{2k+1}$,} \\
-1 & \mbox{s'il existe $k \in \mathbb{N}$ tel que $x_{2k+1} \leq x < x_{2k+2}$,} \\
0  & \mbox{sinon.}
\end{array}
\right.
$$

![Graphe de $f$ pour $a_k = 2^{-2k-1}$ et
$b_k=2^{-2k-2}$.](images/pwm.py.pdf)

::: {.section}
Préambule
---------

On s'intéresse dans un premier temps à la restriction de la fonction $f$
à l'intervalle $[0, x_n]$ pour un entier $n \in \mathbb{N}$ donné.

1.  Soit $\delta > 0$. Montrer que la fonction $\gamma$ qui a tout
    $t \in [0, x_n]$ associe l'ensemble $$
    \gamma(t) = \left]t-\delta/2,t+\delta/2\right[
    $$ est une jauge sur $[0, x_n]$.

2.  Sommes-nous certains qu'il existe une subdivision pointée
    $\mathcal{D}$ de $[0, x_n]$ subordonnée à la jauge $\gamma$ ? En
    construire une le cas échéant.

3.  Quelle est la valeur de l'intégrale de $f$ sur $[0, x_n]$ ?
    Justifier que $f$ est bien intégrable au sens de Henstock-Kurzweil
    sur $[0, x_n]$ ainsi que la valeur de cette intégrale.

4.  Soit $\mathcal{D}$ une subdivision pointée de $[0, x_n]$ subordonnée
    à $\gamma$. Montrer que[^2] $$
    \left|S(f,\mathcal{D}) - \int_0^{x_n} f(x) \, dx\right| \leq 2 (n+1) \delta .
    $$
:::

::: {.section}
Intervalle borné
----------------

On suppose dans cette section que pour tout $k \in \mathbb{N}$,
$a_k = 2^{-2k-1}$ et $b_k=2^{-2k-2}$.

5.  Calculer $x_k$ pour tout $k \in \mathbb{N}$. Montrer que la limite
    $S := \lim_{k \to +\infty} x_k$ existe et est finie (on donnera sa
    valeur).

6.  Montrer que la fonction $f_n:\mathbb{R}\to \mathbb{R}$ définie par
    $$
    f_n(x) = \left\{
    \begin{array}{cl}
    f(x) & \mbox{si $x \in [0, x_n]$} \\
    0    & \mbox{sinon.}
    \end{array}
    \right.
    $$ est intégrable au sens de Henstock-Kurzweil. En déduire que la
    fonction $f$ est mesurable.

7.  Montrer que pour tout couple $(a, b)$ tel que
    $0 \leq a \leq b \leq +\infty$, l'intervalle $\left[a, b\right[$ est
    mesurable. Quelles sont les ensembles $f^{-1}(A)$ possibles quand
    $A$ est un sous-ensemble de $\mathbb{R}$ ? En déduire la
    mesurabilité de $f$ par une méthode alternative à la question
    précédente.

8.  Relier pour $n \in \mathbb{N}$ les intégrales $$
    \int_{-\infty}^{+\infty} f_{n}(x) \, dx
    \; \mbox{ et } \;
    \int_0^{x_n} f(x) \, dx.
    $$ Est-ce que la fonction $f$ est intégrable au sens de
    Henstock-Kurzweil ? Justifier. Le cas échéant, calculer $$
    \int_{-\infty}^{+\infty} f(x) \, dx.
    $$

9.  Est-ce que la restriction de $f$ à $[0, S]$ est intégrable au sens
    de Riemann ?
:::
:::

::: {.section}
Calcul Différentiel
===================

On définit la fonction distance $d_A:\mathbb{R}^n\to \mathbb{R}^+$ à un
ensemble $A$ non-vide de $\mathbb{R}^n$ par $$
d_A(x) = d(x, A) = \inf_{a \in A} \|x - a\|
$$ où $\|\cdot\|$ désigne la norme euclidienne dans $\mathbb{R}^n$.
Lorsqu'un point $a\in A$ vérifie $\|x-a\|=d_A(x)$, on dit que $a$ est un
*projeté* de $x$ sur $A$. On notera l'ensemble des projetés d'un point
$x \in \mathbb{R}^n$ sur $A$ comme $$
\Pi_A(x) = \{a \in A \; | \; \|x - a\|=d_A(x)\}.
$$

::: {.section}
Préliminaires dans $\mathbb{R}^2$
---------------------------------

Notons $C$ le cercle de $\mathbb{R}^2$ centré en $(0,0)$ et de rayon 1
défini par $$
C= \{ x\in \mathbb{R}^2 \; | \; \|x\|=1 \}.
$$ Dans $\mathbb{R}^2$, on a $\|(x_1,x_2)\|=\sqrt{x_1^2+x_2^2}$.

![Distance d'un point au cercle unité.](images/distance.py.pdf)\

![Distance d'un point au cercle unité : lignes de
niveau](images/contour.py.pdf)\

1.  Justifier que pour $x\in \mathbb{R}^2$, $$
    d_C(x) = \left\{
    \begin{array}{rl}
    \|x\| -1 & \text{si } \|x\|\geq 1 \\
    1- \|x\| & \text{si } \|x\|< 1 \ . 
    \end{array}
    \right.
    $$ Expliciter $\Pi_C(x)$ en fonction de $x\in \mathbb{R}^2$.

2.  Montrer que $d_C$ n'est pas différentiable en $x=(0, 0)$. En
    étudiant le rapport $\frac{d_C(x+tx)}{t}$ lorsque $t$ tend vers 0,
    montrer que $d_C$ n'est pas non plus différentiable en $x\in C$.

On définit maintenant $f:\mathbb{R}^2\to \mathbb{R}$ par $$
f(x) = \left\{
\begin{array}{rl}
d_C(x) & \text{si } \|x\|\geq 1 \\
-d_C(x) & \text{si } \|x\|< 1
\end{array}
\right.
$$

3.  Expliciter $f$. Montrer que $f$ est deux fois continûment
    différentiable sur $\mathbb{R}^2\setminus \{(0,0)\}$ et calculer son
    gradient $\nabla f$ et sa hessienne $H_f$.

4.  Calculer $\|\nabla f\|$. En déduire que $f$ est 1-lipschitzienne,
    c'est-à-dire que\
    $$
    |f(x_a)-f(x_b)| \leq \|x_a-x_b\| \qquad \forall (x_a,x_b)\in \mathbb{R}^2 \times \mathbb{R}^2 \ .
    $$
:::

::: {.section}
Cadre général
-------------

5.  Montrer que pour $x\in \mathbb{R}^n$, $$
    d_A(x) = 0 \qquad \Leftrightarrow \qquad x\in \overline{A} \ .
    $$

6.  En se ramenant à un compact, montrer que si $A$ est fermé alors pour
    tout $x$, $\Pi_A(x)$ est non vide. Montrer de plus que $$
    \forall x \in A \ , \; \Pi_A(x)=\{x\} \qquad \text{et} \qquad \forall x \notin A \ , \; \Pi_A(x)\subset \partial A \ .
    $$

Dans la suite, on suppose $A$ fermé. On admet pour l'instant que le
carré de la distance à $A$, c'est-à-dire $d_A^2$, est différentiable en
$x$ si et seulement si $\Pi_A(x)$ est un singleton, noté $p_A(x)$, et
que les dérivées directionnelles s'écrivent alors pour
$v\in \mathbb{R}^n$,\
`\begin{equation} \label{ddsingle}
\lim_{t\to 0} \frac{d_A(x+tv)^2-d_A(x)^2}{t} = 2  \left<v, x-p_A(x)\right> \ .
\end{equation}`{=tex} Soit $D_A$ l'ensemble des points $x$ tel que
$\Pi_A(x)$ est un singleton.

7.  Soit $x\in D_A$. En utilisant l'équation `\eqref{ddsingle}`{=tex},
    exprimer le gradient de $d_A^2$ en $x$ en fonction de $p_A(x)$ .

8.  En déduire que $d_A$ est différentiable sur
    $D_A\setminus \partial A$ et calculer son gradient.

La dernière question de l'exercice établit une partie de l'équivalence
admise plus haut.

9.  On veut montrer que pour tout $v\in \mathbb{R}^n$, pour tout
    $x\in \mathbb{R}^n$, $$
    \lim_{t\to 0} \frac{d_A(x+tv)^2-d_A(x)^2}{t} = 2 \inf_{p\in \Pi_A(x)}  \left<v, x-p\right> \ .
    $$ Pour cela,

-   Montrer que pour tout $t>0$ et pour tout $p\in \Pi_A(x)$, $$
      \frac{d_A(x+tv)^2-d_A(x)^2}{t} \leq 2 \left<v, x-p\right> + t\|v\|^2 \ .
      $$

-   Soit une suite $(t_k)_{k\in \mathbb{N}}$ de $\mathbb{R}^+$ telle que
    $\lim_{k\to +\infty} t_k = 0$, et $(p_{k})_{k\in \mathbb{N}}$ une
    suite de $A$ telle que $p_k\in \Pi_A(x+t_kv)$ pour tout
    $k\in \mathbb{N}$. Montrer que $(p_k)$ est bornée et en déduire
    qu'il existe une sous-suite $(p_{\sigma(k)})$ convergente vers
    $p_0\in \Pi_A(x)$.

-   Conclure en observant que $$
      \frac{d_A(x+t_{\sigma(k)}v)^2-d_A(x)^2}{t_{\sigma(k)}} \geq 2 \left<v, x-p_{\sigma(k)}\right> + t_{\sigma(k)}\|v\|^2 \ .
      $$

10. En déduire que $d_A^2$ n'est pas différentiable en $x$ si $\Pi_A(x)$
    n'est pas un singleton.
:::
:::

::: {.section}
Probabilités
============

Dans tout cet exercice, nous nous intéressons à la modélisation
probabiliste de la hauteur d'eau maximale de la Seine (sur l'échelle
d'Austerlitz) une année donnée. Nous la représentons par une variable
aléatoire $X$ **positive** de fonction de répartition $F$ et de densité
$f$.

::: {.section}
Préliminaires -- Espérance et fonction de répartition
-----------------------------------------------------

L'objectif de cette première partie est de prouver l'équivalence
`\begin{equation}
\begin{array}{l}
\text{la variable aléatoire positive } X \text{ est intégrable } (X \in \mathcal{L}^1)\\
\Updownarrow\\
1 - F \text{ est intégrable sur } \mathbb{R}_+. 
\end{array}
\tag{$E$}
\end{equation}`{=tex}

1.  Soit
    $g : (x,u) \in \mathbb{R}_+^2 \mapsto 1_{[x,+\infty[}(u)\,f(u)$.

    i.  Vérifier l'absolue intégrabilité de
        $g_u : x \in \mathbb{R}_+ \mapsto g(x,u)$ pour tout
        $u\in\mathbb{R}_+$ et de
        $g_x : u \in \mathbb{R}_+ \mapsto g(x,u)$ pour tout
        $x\in\mathbb{R}_+$.

    ii. Justifier que pour tout $x \in \mathbb{R}_+$
        $$\int_{\mathbb{R}_+} g(x,u)\, du = 1 - F(x).$$

    iii. Montrer que pour tout $u \in \mathbb{R}_+$
         $$\int_{\mathbb{R}_+} g(x,u)\,dx = u\,f(u).$$

2.  En déduire l'équivalence $(E)$.

3.  Supposons $X\in\mathcal{L}^1$. Donner deux expressions équivalentes
    de son espérance.
:::

::: {.section}
Etude du maximum -- Loi de Fréchet
----------------------------------

En théorie des valeurs extrêmes, une distribution classique pour
modéliser des maxima est la loi de Fréchet de paramètre $\xi > 0$, de
fonction de répartition
$$F_\xi : x\in\mathbb{R}\mapsto \left|\begin{array}{ll} \exp\left\{-x^{-\xi}\right\} & \text{si } x >0,\\ 0 & \text{sinon.} \end{array}\right.$$
Elle fait partie de la famille des lois dites *à queue épaisse*. Nous
allons en étudier quelques propriétés et évaluer leur impact sur la
modélisation des crues de la Seine.

On suppose dans un premier temps que $X$ suit une loi de Fréchet de
paramètre $1$ (dite *Fréchet standard*) et on fixe $\alpha > 0$.

4.  Quelle est la loi de $X^\alpha$ ?

5.  On propose d'étudier l'intégrabilité de $X^\alpha$.

    i.  Montrer que $X^\alpha \in \mathcal{L}^1$ ssi $\alpha < 1$.

    ii. Lorsqu'elle est bien définie, calculer
        $\mathbb{E}\left(X^\alpha\right)$. On pourra faire appel à la
        fonction gamma
        $$\Gamma : x \in \mathbb{R}_+^\ast \mapsto \int_{0}^{+\infty} t^{x-1}\,e^{-t}\,dt.$$

On suppose maintenant et dans tout le reste de l'exercice que $X$ suit
une loi de Fréchet de paramètre $\xi > 0$.

6.  Nous allons étudier le comportement de sa queue de distribution.

    i.  Donner un équivalent de $1-F(x)$ quand $x\to+\infty$, puis
        calculer, pour tout $x>1$,
        $\lim\limits_{t\to+\infty} \mathbb{P}\left( X > xt \mid X > t \right)$.

    ii. Rappeler une condition nécessaire et suffisante pour que
        $X^\alpha \in \mathcal{L}^1$.

    iii. Proposer une interprétation de ces résultats au regard du
         phénomène étudié.

Soient $n\in\mathbb{N}^\ast$ et $X_n$ la hauteur d'eau maximale de
l'année $n$. On suppose que les variables aléatoires $X_1,\dots,X_n$
sont indépendantes, de même loi que $X$.

7.  On note $M_n := \max\limits_{1\leq i\leq n} X_i$ la hauteur d'eau
    maximale sur $n$ années.

    i.  Montrer qu'il existe $a_n > 0$ tel que $a_n\,M_n$ a la même loi
        que $X$. On dit que la loi de Fréchet est *max-stable*.

    ii. En déduire que
        $\mathbb{P}\left(M_n > x\right) \sim n\,\mathbb{P}\left(X > x \right)$
        quand $x\to+\infty$. Interpréter ce résultat au regard du
        phénomène réel étudié.

8.  On note $S_n := \sum_{i = 1}^n X_i$ le cumul des hauteurs d'eau
    maximales sur $n$ années. Montrer que
    $\mathbb{P}\left(S_n > x\right) \sim n\,\mathbb{P}\left(X > x \right)$
    quand $x\to+\infty$. Comparer ce résultat au précédent et
    interpréter.

    *Indication* : on pourra procéder par récurrence sur $n$ et faire
    intervenir les événements $\{X_n > (1-\delta)x\}$,
    $\{X_n > \delta x\}$, $\{S_{n-1} > (1-\delta)x\}$ et
    $\{S_{n-1} > \delta x\}$ pour
    $\delta \in \left]0, \frac{1}{2} \right[$ arbitrairement petit.
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

[^2]: **Indication :** on pourra considérer toutes les paires
    $(t, [a, b]) \in \mathcal{D}$ intervenant dans la somme de Riemann
    $S(f, \mathcal{D})$ puis majorer $$
    \left|f(t) (b - a) - \int_{a}^b f(x) \, dx\right|
    $$ en distinguant les intervalles $[a, b]$ qui contiennent au moins
    un $x_k$ ($k \in \{0,\dots, n\}$) et ceux qui n'en contiennent pas.
