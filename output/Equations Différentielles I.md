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

-   [Un peu d'histoire](#un-peu-dhistoire)
-   [Objectifs du cours](#objectifs-du-cours)
-   [Cadre de l'étude](#cadre-de-létude)
    -   [Equations différentielles en physique](#ex_equaDiffPhys)
    -   [Portrait de phase](#portrait-de-phase)
-   [Etude du problème de Cauchy](#etude-du-problème-de-cauchy)
    -   [Existence de solutions
        locales](#existence-de-solutions-locales)
    -   [Domaine d'existence des
        solutions](#domaine-dexistence-des-solutions)
    -   [Unicité des solutions
        maximales](#unicité-des-solutions-maximales)
-   [Régularité et stabilité des
    solutions](#régularité-et-stabilité-des-solutions)
    -   [Sensibilité aux conditions initiales et erreurs de
        modèle](#sensibilité-aux-conditions-initiales-et-erreurs-de-modèle)
    -   [Propriétés asymptotiques](#propriétés-asymptotiques)
-   [Exercices complémentaires](#exercices-complémentaires)
    -   [Ecoulement dans un réservoir ($+$)](#exo_Torricelli)
    -   [Autour du Lemme de Grönwall](#exo_gronwall)
    -   [Cycle limite ($+$)](#exo_cycle-lim)
    -   [Contrôle d'un système](#exo_cont_lin)
-   [Solutions](#solutions)
    -   [Exercices essentiels](#exercices-essentiels)
    -   [Ecoulement dans un réservoir](#correc_Torricelli)
    -   [Autour du Lemme de Grönwall](#correc_gronwall)
    -   [Cycle limite](#correc_cycle_lim)
    -   [Contrôle d'un système](#correc_cont_lin)
-   [Annexes](#annexes)
    -   [Preuve du théorème de Peano-Arzelà
        (Hors-programme)](#app_peano)
    -   [Preuve du théorème du domaine maximal
        d'existence](#pr_theo_bouts)
    -   [Stabilité et linéarisé tangent](#app_stab_lin)
-   [Références](#références)

```{=tex}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\Rgeq}{\R_{\geq 0}}
\renewcommand{\C}{\mathbb{C}}
```
```{=tex}
\newcommand{\cS}{\mathcal{S}}
\newcommand{\cC}{\mathcal{C}}
```
```{=tex}
\newcommand{\inter}{\mathop{\rm int}\nolimits}
```
```{=tex}
\newcommand{\tmin}{t_m^-}
\newcommand{\tmax}{t_m^+}
```
::: {.section}
Un peu d'histoire
=================

L'étude des équations différentielles remonte au XVII$^e$ siècle lors de
la découverte du calcul infinitésimal et de la modélisation du mouvement
par Kepler et Newton. Avec Leibniz, leur premier réflexe est alors de
chercher à résoudre ces équations de manière exacte, par exemple par des
primitives de fonctions connues ou bien sous forme de série, mais ces
méthodes atteignent vite leurs limites, sauf dans des cas très
particuliers.

Alors que l'idée d'approximer les solutions apparaît au milieu du
XVIII$^e$ siècle avec Euler, on cherche ensuite plutôt à caractériser
leurs propriétés sans les connaître explicitement. Cauchy, et
parallèlement Lipschitz, démontrent les premiers, au milieu du XIX$^e$
siècle, l'existence et l'unicité des solutions sous des hypothèses de
régularités de l'équation différentielle. Laplace, qui s'intéresse alors
à la mécanique céleste, s'émerveille devant la capacité de l'Homme à
prédire l'évolution du monde physique. C'est l'avénement du
*déterminisme* c'est-à-dire la certitude que l'état du monde futur (ou
passé) peut être prédit de manière unique par la connaissance de l'état
initial.

Cependant, à la fin du XIX$^e$ siècle, les travaux de Poincaré et de ses
contemporains mettent en évidence les limites de ce déterminisme. Le
constat que le modèle physique n'est jamais exactement connu, ni sa
condition initiale, amène les scientifiques à étudier la sensibilité des
solutions à ces erreurs. Une sensibilité extrême chez certains systèmes
rend leur simulation impossible sur des temps longs et mène à la théorie
du *chaos* qui occupera les scientifiques durant une grande partie du
XX$^e$ siècle.

En parallèle, l'étude de la stabilité et du comportement asymptotique
des solutions intéresse dès le XIX$^e$ siècle, d'abord dans le cas des
systèmes linéaires avec des mathématiciens comme Ruth, Hurwitz, etc.
Mais c'est finalement la thèse de Lyapunov à la fin du XIX$^e$ siècle
qui lance la théorie générale de la stabilité des systèmes non linéaires
qui sera ensuite étayée tout au long des XX$^e$ et XXI$^e$ siècles.
:::

::: {.section}
Objectifs du cours
==================

Ce cours est une introduction à l'étude non linéaire des équations
différentielles. Pour une étude plus complète voir par exemple [@Hale].
En première lecture, les objectifs "opérationnels" sont les suivants :

-   savoir réduire une équation différentielle à l'ordre 1.

-   savoir justifier l'existence de solutions par le théorème de Peano
    lorsque "$f$ est continue"

-   comprendre la notion de solution maximale et savoir qu'elles sont
    définies tant qu'elles "n'explosent" pas et tant qu'elles
    n'atteignent pas la frontière du domaine où l'équation
    différentielle est définie. Savoir justifier qu'une solution est
    globale si ces éventualités ne peuvent se réaliser en temps fini
    et/ou en faisant appel au critère "linéairement borné".

-   savoir justifier l'unicité des solutions maximales par le théorème
    de Cauchy-Lipschitz lorsque "$f$ est continûment différentiable par
    rapport à $x$".

-   comprendre (qualitativement) dans quelle mesure une erreur sur la
    condition initiale se répercute sur les solutions en temps fini.

-   savoir trouver les points d'équilibre.

-   savoir déterminer si un système linéaire est globalement
    asymptotiquement stable en regardant le signe de la partie réelle de
    ses valeurs propres.

-   savoir déterminer si un point d'équilibre est localement
    asymptotiquement stable/instable par les valeurs propres de la
    matrice Jacobienne associée.

-   savoir calculer la dérivée d'une fonction de Lyapunov le long des
    trajectoires et en déduire qu'un point d'équilibre est stable ou
    localement/globalement asymptotiquement stable.

En deuxième lecture :

-   comprendre la preuve du théorème de Cauchy-Lipschitz en voyant la
    solution comme un point fixe de la représentation intégrale des
    solutions.

-   savoir que l'on peut relâcher l'hypothèse du théorème de
    Cauchy-Lipschitz à "$f$ Lipschitzienne par rapport à $x$".

-   comprendre ce qu'est un système chaotique et ce que représente son
    exposant de Lyapunov.

-   comprendre ce que la notion de stabilité apporte en plus de
    l'attractivité dans la notion de stabilité asymptotique.

**Notations**

-   $B(x,r)$ : boule ouverte centrée en $x$ et de rayon $r$.

-   $\overline{B}(x,r)$ : boule fermée centrée en $x$ et de rayon $r$.

-   Pour $x:I\subset\mathbb{R}\to \mathbb{R}^n$,
    $\dot{x}(t)=\frac{dx}{dt}(t)$ et $\ddot{x}(t)=\frac{d^2x}{dt^2}(t)$.
:::

::: {.section}
Cadre de l'étude
================

Les équations différentielles apparaissent couramment en physique pour
décrire l'évolution des grandeurs décrivant le système.

::: {.section}
### Equations différentielles en physique {#ex_equaDiffPhys .exemple}

-   La tension $u_c$ aux bornes d'un condensateur dans un circuit RLC en
    série évolue selon $$
    \ddot{u}_c = -\frac{R}{L} \dot{u}_c - \frac{1}{LC} u_c + u(t)
    $$ où $R$, $L$, $C$ notent la résistance, inductance et capacité
    respectivement, et $u$ la tension appliquée par le générateur. Cette
    équation différentielle implique les dérivées de $u_c$ jusqu'à
    l'ordre 2, donc on parle d'équation différentielle d'ordre 2.

```{=html}
<!-- -->
```
-   En cinétique chimique, les concentrations des espèces chimiques
    intervenant dans une réaction $$
    A+ B \overset{k}{\underset{k'}{\leftrightarrows}}  C 
    $$ sont régies par une équation différentielle d'ordre 1 donnée par
    `\begin{align*}
    \dot{c}_A &= -k \, c_Ac_B + k'c_C \\
    \dot{c}_B &= -k \, c_Ac_B + k'c_C\\
    \dot{c}_C &= k \, c_Ac_B - k'c_C
    \end{align*}`{=tex} avec $k,k'$ les constantes de réaction. Cette
    équation différentielle n'a pas de terme extérieur variant avec le
    temps. On dit qu'elle est *autonome*.

-   La mécanique Newtonienne ou Lagrangienne amène typiquement à des
    équations du type $$
    M \ddot{q} = \sum_k F_k(t,q,\dot{q})
    $$ où $q\in \mathbb{R}^n$ modélise la position du système (spatiale,
    angulaire, etc), $\dot{q}$ sa vitesse et $\ddot{q}$ son
    accélération, avec $M$ la matrice d'inertie, et $F_k$ les
    forces/couples agissant sur le système. Ici il s'agit d'une équation
    différentielle d'ordre 2.

Dans tous ces cas, on s'intéresse aux signaux du temps $t\mapsto y(t)$
de classe $C^p$ qui vérifient une équation du type $$
y^{(p)}(t) = \psi\left(t,y(t),\dot{y}(t),\ldots, y^{(p-1)}(t)\right)
$$ sur son ensemble de définition, où $p\in \mathbb{N}^*$ désigne
l'ordre de l'équation différentielle. En fait, on se rend compte que $y$
de classe $C^p$ vérifie l'équation différentielle ci-dessus si et
seulement si $x=(y,\dot{y},\ldots,y^{(p-1)})$ de classe $C^1$ vérifie $$
\dot{x} = f(t,x) \ , 
$$ où $f$ est définie par $$
f(t,y_0,y_1,\ldots,y_{p-1}) = (y_1,y_2,\ldots,y_{p-1},\psi(t,y_0,\ldots,y_{p-1})) \ .
$$

Nous déduisons que résoudre une équation différentielle d'ordre $p$ est
en fait équivalent à résoudre une équation différentielle d'ordre 1,
quitte à considérer comme inconnue la suite des dérivées
$x=(y,\dot{y},\ldots,y^{(p-1)})$ de classe $C^1$, au lieu de $y$ de
classe $C^p$. $x$ est appelé l'*état* du système.
:::

::: {.section}
#### Exemple -- Réduction à l'ordre 1 {#ex_reducOrdre1 .example .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Réduction à l'ordre 1}`{=latex}

Reprenons les exemples plus haut :

-   pour un circuit RLC, on prend $x=(u_c,\dot{u}_c)\in \mathbb{R}^2$,
    et $$
    f(t,x_1,x_2) = 
    \left[
      \begin{matrix}
          x_2\\
          -\frac{R}{L} x_2 - \frac{1}{LC} x_1 + u(t)
      \end{matrix}
    \right] \ .
    $$

```{=html}
<!-- -->
```
-   en cinétique chimique, $x=(c_A,c_B,c_C)\in \mathbb{R}^3$ et $$
    f(t,x_1,x_2,x_3) = \left[
      \begin{matrix}
           -k \, x_1x_2 + k'x_3 \\
           -k \, x_1x_2 + k'x_3\\
           k \, x_1x_2 - k'x_3
      \end{matrix}
    \right]
    $$

-   en mécanique, $x=(q,\dot{q})$ et $$
    f(t,x_1,x_2) = 
    \left[
      \begin{matrix}
          x_2\\
          M^{-1} \sum_k F_k(t,x_1,x_2)
      \end{matrix}
    \right] \ .
    $$

Ainsi, même si la physique nous donne initialement une équation
différentielle d'ordre supérieur, on pourra toujours se ramener à
l'ordre 1. Cette réduction est cruciale pour l'étudier mathématiquement
ainsi que numériquement, et devra donc être systématique.

Commençons par définir le cadre de cette étude.
:::

::: {.section}
### Définition -- Solution d'une équation différentielle {#solution-dune-équation-différentielle .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Solution d'une équation différentielle}`{=latex}

Soient $n\in \mathbb{N}^*$, $J$ ouvert de $\mathbb{R}$, $X$ ouvert de
$\mathbb{R}^{n}$ et $f:J\times X \to \mathbb{R}^n$ une application
continue. Une fonction $x:I\to \mathbb{R}^n$ définie sur un intervalle
de temps $I\subset J$ non réduit[^2] à un point, est dite solution[^3]
de l'équation différentielle $$
\dot{x} = f(t,x)
$$ si $x$ est continue sur $I$ avec $x(t)\in X$ pour tout $t\in I$, et
de classe $C^1$ sur $\mathring{\overline{I}}$ avec
$\dot{x}(t) = f(t,x(t))$ pour tout $t\in \mathring{\overline{I}}$.

L'équation différentielle est dite *autonome* si l'application $f$ ne
dépend pas de $t$. Dans ce cas, on peut aussi définir directement
$f: X \to \mathbb{R}^n$.

Lorsque l'intervalle de temps $I$ de définition de la solution est $J$
entier, on dira que la solution est *globale*. Mais on verra qu'il peut
parfois arriver qu'une solution ne puisse être définie sur $J$ entier,
par exemple si elle explose avant, ou si elle s'apprête à quitter $X$.

Notons que $f$ sera souvent définie sur $J=\mathbb{R}$ et
$X = \mathbb{R}^{n}$. Cependant, il peut arriver que cela ne soit pas le
cas, comme par exemple pour deux corps de position $y_a,y_b$ dont la
force d'interaction gravitationnelle $\frac{Gm_a m_b}{\|y_a-y_b\|^2}$
n'est définie que pour $y_a\neq y_b$.
:::

::: {.section}
La physique s'intéresse souvent aux solutions partant d'une *condition
initiale* donnée. La recherche et l'étude de ces solutions particulières
est due à Cauchy et porte le nom de *Problème de Cauchy* :

> Dans mes leçons données à l'École Polytechnique, comme dans la plupart
> des ouvrages ou mémoires que j'ai publiés sur le calcul intégral, j'ai
> cru devoir placer en premier lieu la recherche, non pas des intégrales
> générales, mais des particulières ; en sorte que la détermination des
> constantes ou des fonctions arbitraires ne fût plus séparée de la
> recherche des intégrales.
:::

::: {.section}
### Définition -- Problème de Cauchy (*Initial Value Problem*) {#def_cauchy .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Problème de Cauchy (\emph{Initial Value Problem})}`{=latex}

Soient $J$ ouvert de $\mathbb{R}$, $X$ ouvert de $\mathbb{R}^{n}$,
$(t_0,x_0)\in J\times X$ et $f: J\times X \to \mathbb{R}^n$ continue. Le
*problème de Cauchy* associé fait référence au système $$
\dot{x}=f(t,x) \quad , \quad x(t_0)=x_0 \ .
$$ On dira donc que $x:I\to \mathbb{R}^n$ est solution du problème de
Cauchy défini par $f$ et $(t_0,x_0)$ si

-   $t_0\in I$ et $x(t_0)=x_0$

-   $x$ est solution de l'équation différentielle $\dot{x}=f(t,x)$ sur
    $I$.

On notera alors $x\in S_f(t_0,x_0)$.

Avant d'étudier les solutions d'un problème de Cauchy, il est crucial de
remarquer la caractérisation qui suit.
:::

::: {.section}
### Théorème -- Représentation intégrale des solutions {#theo_eq_integrale .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Représentation intégrale des solutions}`{=latex}

Soient $J$ ouvert de $\mathbb{R}$, $X$ ouvert de $\mathbb{R}^{n}$,
$f: J\times X \to \mathbb{R}^n$ continue, $I\subset J$ un intervalle de
$\mathbb{R}$ non réduit à un point, $t_0\in I$, $x_0\in X$, et
$x: I\to \mathbb{R}^n$ continue telle que $x(t)\in X$ pour tout
$t\in I$. Alors, $x\in S_f(t_0,x_0)$ si et seulement si $x$ est solution
de l'équation intégrale $$
x(t) = x_0 + \int_{t_0}^t f(s,x(s))ds \qquad \forall t\in I \ .
$$

Notons que cette caractérisation n'aurait pas été possible si l'on avait
gardé une équation différentielle d'ordre $p>1$.
:::

::: {.section}
#### Démonstration {#démonstration .proof}

Supposons $x\in S_f(t_0,x_0)$. Alors $x: I\to \mathbb{R}^n$ est de
classe $C^1$ sur $\mathring{\overline{I}}$, et pour tout $t\in I$, $$
x_0 + \int_{t_0}^t f(s,x(s))ds = x(t_0)  + \int_{t_0}^t \dot{x}(s) ds = x(t) \ .
$$ Réciproquement, si $x$ vérifie l'équation intégrale sur $I\subset J$,
$x(t_0)=x_0$, et puisque $f$ est continue sur $I\times X$, $x$ est de
classe $C^1$ sur $I$ et par dérivation, $\dot{x}(t)=f(t,x(t))$ pour tout
$t\in I$.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Remarque -- Classe plus générale de solutions {#classe-plus-générale-de-solutions .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Classe plus générale de solutions}`{=latex}

La définition sous forme intégrale des solutions montre que la recherche
de solutions $C^1$ et l'hypothèse de continuité de $f$ pourraient être
relachées : il suffirait de pouvoir définir l'objet
$\int_{t_0}^t f(s,x(s))ds$. Mais il est tout de même souhaitable
d'assurer un minimum de propriétés telles que l'existence de solutions,
comme nous allons le voir dans la section suivante.
:::

::: {.section}
### Portrait de phase

En dimension 2 (ou 3), il est possible de visualiser géométriquement le
comportement des solutions en traçant les courbes paramétriques
$t\mapsto(x_1(t),x_2(t))$ dans le plan (ou
$t\mapsto(x_1(t),x_2(t),x_3(t))$ dans l'espace) pour différentes
conditions initiales. C'est ce que l'on appelle un *portrait de phase*.
Voir [Figure (p. `\pageref*{fig_pendule}`{=tex})](#fig_pendule)
ci-dessous dans le cas d'un pendule.

![Portraits de phase d'un pendule non amorti en haut et amorti en bas.
$x_1$ représente l'angle du pendule en abscisse et $x_2$ sa vitesse de
rotation en ordonnée. Le pendule sera décrit et étudié plus en détail
dans la suite du cours.](images/pendule.py.pdf){#fig_pendule}
:::
:::

::: {.section}
Etude du problème de Cauchy
===========================

::: {.section}
Existence de solutions locales
------------------------------

Notre point de départ est le théorème suivant établi à la fin du XIX$^e$
siècle, qui assure l'existence locale de solutions au [problème de
Cauchy (p. `\pageref*{def_cauchy}`{=tex})](#def_cauchy) sous une simple
hypothèse de continuité de $f$. En d'autres termes, dans le cadre de ce
cours où $f$ est supposée continue, il existe toujours des solutions
pour toute condition initiale, définies au moins pour un certain temps.

::: {.section}
### Théorème -- Théorème de Peano-Arzelà {#theo_peano .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Théorème de Peano-Arzelà}`{=latex}

Soient $J$ ouvert de $\mathbb{R}$, $X$ ouvert de $\mathbb{R}^{n}$,
$f: J\times X \to \mathbb{R}^n$ continue. Pour tout
$(t_0,x_0)\in J\times X$, il existe $\tau_m >0$ et
$x :[t_0-\tau_m,t_0+\tau_m]\to\mathbb{R}^n$ tels que
$x\in S_f(t_0,x_0)$.
:::

::: {.section}
#### Démonstration {#démonstration-1 .proof}

La démonstration de ce résultat est hors-programme et fait appel au
théorème d'Ascoli(-Arzelà). Seule la connaissance et la compréhension du
résultat est exigible. Pour les curieux, la preuve est donnée en [annexe
(p.
`\pageref*{app_peano}`{=tex})](#app_peano).`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Remarque -- Classe plus générale de solutions (pour la culture) {#classe-plus-générale-de-solutions-pour-la-culture .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Classe plus générale de solutions (pour la culture)}`{=latex}

L'existence de solutions $C^1$ est garantie lorsque $f$ est continue. Il
s'avère que l'existence de solutions *absolument continues*, est
garantie sous les hypothèses plus faibles suivantes dans un voisinage de
$(t_0,x_0)$ :

-   pour tout $t$, $x\mapsto f(t,x)$ est continue ;

-   pour tout $x$, $t\mapsto f(t,x)$ est mesurable ;

-   il existe une fonction intégrable $t\mapsto b(t)$ telle que
    $|f(t,x)|\leq b(t)$ pour tout $(t,x)$.

Ce sont les conditions de *Carathéodory*. Voir [@Hale]. Un cadre encore
plus général consiste à autoriser des discontinuités de $f$ par rapport
à $x$ mais l'étude des solutions passe alors par celle des *inclusions
différentielles* du type $\dot{x} \in F(t,x)$, ce qui nous amènerait
bien trop loin de ce cours. Voir [@Fil].
:::
:::

::: {.section}
Domaine d'existence des solutions
---------------------------------

Nous venons de voir que des solutions locales au problème de Cauchy
existent si $f$ est continue. Nous savons qu'elles sont définies *au
moins un certain temps*, mais il est intéressant de se demander quel est
l'intervalle de temps *maximal* sur lequel elles peuvent être définies.
En d'autre terme, on s'intéresse aux *solutions maximales*.

::: {.section}
### Définition -- Solution maximale {#def_sol_max .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Solution maximale}`{=latex}

Soient $J$ ouvert de $\mathbb{R}$, $X$ ouvert de $\mathbb{R}^{n}$,
$f: J\times X \to \mathbb{R}^n$ continue. On dit que
$x : I \to\mathbb{R}^n$ est une solution *maximale* de l'équation
différentielle $$
\dot{x}=f(t,x)
$$ si elle n'est pas *prolongeable* en une solution définie plus
longtemps dans $J\times X$. En d'autres termes, il n'existe pas de
solution $x' : I'\to\mathbb{R}^n$ avec $I'\supsetneq I$ et $x=x'$ sur
$I$.

Il s'avère que l'intervalle maximal de définition $I$ d'une solution
maximale n'est pas nécessairement $\mathbb{R}$ entier même si $f$ est
définie globalement sur $\mathbb{R}\times \mathbb{R}^n$ et $f$ est de
classe $C^\infty$.
:::

::: {.section}
#### Exemple -- Explosion en temps fini {#ex_explTempsFini .example .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Explosion en temps fini}`{=latex}

Considérons le problème de Cauchy $$
\dot{x} = x^2 \quad , \qquad (t_0,x_0)\in \mathbb{R}^2 \ .
$$ L'application $f:(t,x)\mapsto x^2$ est continue sur $\mathbb{R}^2$,
donc il existe au moins une solution. On peut par exemple vérifier que
$x:I\to \mathbb{R}$ définie par $$
x(t)=\frac{x_0}{1-x_0(t-t_0)} \quad , \quad I=\left]-\infty,t_0+\frac{1}{x_0}\right[ 
$$ est bien solution. Vu qu'elle diverge au temps $t_0+\frac{1}{x_0}$,
elle ne peut être prolongée au delà. Elle est donc maximale et on dit
qu'elle *explose en temps fini*.

![Solutions à $\dot{x} = x^2$ pour $t_0=0$ et différentes valeurs de
$x_0$](images/explosion_temps_fini.py.pdf){#fig_explo_temps_fini}

En fait, le théorème suivant montre que les solutions maximales sont
définies sur un intervalle ouvert, et cet intervalle n'est borné que si
$t\mapsto x(t)$ diverge en temps fini ou $t\mapsto(t,x(t))$ tend vers la
frontière de l'ensemble de définition $J\times X$ de $f$ en temps fini.
:::

::: {.section}
### Théorème -- Domaine maximal d'existence {#theo_bouts .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Domaine maximal d'existence}`{=latex}

Soient $J$ ouvert de $\mathbb{R}$, $X$ ouvert de $\mathbb{R}^{n}$,
$f: J\times X \to \mathbb{R}^n$ continue et $(t_0,x_0)\in J\times X$.
Toute solution maximale $x:I\to \mathbb{R}^n$ dans $S_f(t_0,x_0)$ est
définie sur un intervalle ouvert $\left]t_m^-,t_m^+\right[$ avec
$t_m^-,t_m^+\in \mathbb{R}\cup\{+\infty,-\infty\}$. De plus, si $t_m^-$
est fini alors $$
\lim_{t\to t_m^-} d\Big((t,x(t)),\partial (J\times X) \Big) = 0  \quad  \text{ou} \quad 
\lim_{t\to t_m^-} \|x(t)\| = +\infty 
$$ et si $t_m^+$ est fini alors $$
\lim_{t\to t_m^+} d\Big((t,x(t)),\partial (J\times X) \Big) = 0  \quad  \text{ou} \quad 
\lim_{t\to t_m^+} \|x(t)\| = +\infty  \ .
$$
:::

::: {.section}
#### Démonstration {#démonstration-2 .proof}

La preuve complète est donnée en [annexe (p.
`\pageref*{pr_theo_bouts}`{=tex})](#pr_theo_bouts). On commence par
observer que si l'intervalle d'existence n'était pas ouvert, la solution
pourrait être prolongée au bord grâce au théorème de Peano, ce qui
contredirait sa maximalité. Ensuite, la preuve consiste à montrer que si
$t_m^+$ (resp. $t_m^-$) est fini, alors $(t,x(t))$ finit forcément par
sortir définitivement de tout sous-ensemble fermé et borné de
$J\times X$ lorsque $t$ tend vers $t_m^+$ (resp. $t_m^-$), et donc soit
diverger soit tendre vers la frontière de l'ouvert
$J\times X$.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Théorème -- Critère d'existence globale {#theo_exist_glob .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Critère d'existence globale}`{=latex}

Soient $J$ un intervalle ouvert de $\mathbb{R}$ et
$f:J\times\mathbb{R}^n\to\mathbb{R}^n$ continue. S'il existe
$a,b: J\to\mathbb{R}$ continues telles que\
$$
\|f(t,x)\|\leq a(t) \|x\| + b(t) \quad \forall (t,x)\in J\times \mathbb{R}^n \ ,
$$ alors toute solution maximale est définie sur $J$ entier. On dit
alors que $f$ a une *croissance au plus affine*.
:::

::: {.section}
#### Démonstration {#démonstration-3 .proof}

Prouvé dans l'exercice [*Autour du Lemme de Grönwall* (p.
`\pageref*{exo_gronwall}`{=tex})](#exo_gronwall).`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Exemple -- Solutions globales {#ex_solGlob .example .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Solutions globales}`{=latex}

-   Considérons une équation différentielle *linéaire*, c'est-à-dire
    pour laquelle il existe $A:\mathbb{R}\to\mathbb{R}^{n\times n}$ et
    $b:\mathbb{R}\to\mathbb{R}^n$ continues telles que $$
    f(t,x) = A(t) x + b(t) \ .
    $$ D'après le théorème précédent, quelle que soit sa condition
    initiale $(t_0,x_0)\in I\times\mathbb{R}^n$, sa solution maximale
    est définie sur $I$ entier. Dans le cas où $A$ est constant, on en a
    même une formule explicite (obtenue par la méthode de *variation de
    la constante*) $$
    x(t) = e^{A(t-t_0)}x_0 + \int_{t_0}^t e^{A(t-s)} b(s)ds \ ,
    $$ où $e^{A(t-s)}$ est l'exponentielle de matrice définie par $$
    e^{A(t-s)}=\sum^{+\infty}_{p=0} \frac{A^p(t-s)^p}{p!} \ .
    $$ Attention, cette formule ne fonctionne que si $A$ est constant.
    Notons que si $A$ est diagonalisable, i.e., il existe
    $P\in \mathbb{R}^{n\times n}$ telle que $A = P^{-1} D P$ avec
    $D\in \mathbb{R}^{n\times n}$ une matrice diagonale contenant les
    valeurs propres de $A$, alors $$
    e^{A(t-s)} = P^{-1} e^{D(t-s)}  P
    $$ donc les solutions avec $b=0$ sont des combinaisons linéaires de
    $e^{\lambda_i t}$ où $\lambda_i$ sont les valeurs propres de $A$.
    Ceci n'est plus vrai lorsque $A$ n'est pas diagonalisable. Voir
    l'[étude de stabilité d'un système linéaire (p.
    `\pageref*{Hurwitz}`{=tex})](#Hurwitz).

-   Un autre cas important d'une croissance au plus affine est lorsque
    $f$ est globalement bornée en $x$. Par exemple, $$
    f(t,x)=c(t)\arctan(x) \qquad \text{ ou } \qquad 
    f(t,x)=\frac{c(t)}{1+x^2}
    $$ engendrent des problèmes de Cauchy aux solutions globales.
:::

::: {.section}
#### Exercice -- Solutions globales I ($\mathord{\bullet}$) {#glob_sol .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Solutions globales I}`{=latex}

Justifier que pour toute condition initiale,\
$$
\begin{array}{rcl}
\dot{x}_1 &=& \sin x_1 - \sqrt{|t|} x_2 \\
\dot{x}_2 &=& \sqrt{1+x_1^2}
\end{array}
$$ admet des solutions et les solutions maximales sont définies sur
$\mathbb{R}$. ([Solution p.
`\pageref*{answer-glob_sol}`{=tex}](#answer-glob_sol){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Solutions globales II ($\mathord{\bullet}\mathord{\bullet}$) {#glob_sol2 .exercise .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Solutions globales II}`{=latex}

Soient $f:\mathbb{R}\times \mathbb{R}^n \to \mathbb{R}^n$ continue et
$V:\mathbb{R}^n \to \mathbb{R}$ définie par $V(x) = x^\top x$ telles que
$$
\langle\nabla V (x), f(t,x)\rangle \leq a(t) V(x) + b(t)  \qquad \forall (t,x)\in \mathbb{R}\times \mathbb{R}^n
$$ avec $a,b:\mathbb{R}\to \mathbb{R}$ continues. Montrer que quelque
soit la condition initiale $(t_0,x_0)\in \mathbb{R}\times \mathbb{R}^n$,
les solutions maximales de $$
\dot{x} = f(t,x)
$$ sont définies sur $[t_0,+\infty[$. On pourra pour cela étudier
l'évolution de $t\mapsto V(x(t))$. ([Solution p.
`\pageref*{answer-glob_sol2}`{=tex}](#answer-glob_sol2){.no-parenthesis}.)
:::
:::

::: {.section}
Unicité des solutions maximales
-------------------------------

Si des solutions maximales existent toujours, elles ne sont pas toujours
uniques.

::: {.section}
#### Exemple -- Non-unicité des solutions {#ex_nonUnique .example .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Non-unicité des solutions}`{=latex}

Considérons le problème de Cauchy $$
\dot{x}=-\sqrt{|x|} \qquad , \qquad (t_0,x_0)=(0,0) \ .
$$ Ce système permet en particulier de modéliser l'écoulement d'un
fluide dans un réservoir, selon la loi de *Torricelli* (voir [exercice
(p. `\pageref*{exo_Torricelli}`{=tex})](#exo_Torricelli)). La fonction
$f:(t,x)\mapsto -\sqrt{|x|}$ est continue sur
$\mathbb{R}\times \mathbb{R}$, donc ce problème de Cauchy admet au moins
une solution. Mais on montrera en [exercice (p.
`\pageref*{exo_Torricelli}`{=tex})](#exo_Torricelli) qu'il existe une
infinité de solutions maximales. Plus de détails sont donnés dans le
notebook Equations Différentielles I.ipynb.

Le théorème suivant, dit de *Cauchy-Lipschitz*, montre que l'unicité des
solutions maximales est garantie si $f$ est de plus continûment
différentiable par rapport à la variable $x$. On voit que ce n'est pas
le cas de $x\mapsto -\sqrt{|x|}$ en 0. Le théorème et la preuve de
l'époque est disponible en ligne dans des notes de cours [@cauchy].
:::

::: {.section}
### Théorème -- Théorème de Cauchy-Lipschitz (ou de Picard-Lindelöf) {#theo_lips .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Théorème de Cauchy-Lipschitz (ou de Picard-Lindelöf)}`{=latex}

Soient $J$ ouvert de $\mathbb{R}$, $X$ ouvert de $\mathbb{R}^{n}$,
$f: J\times X \to \mathbb{R}^n$ continue telle que sa dérivée partielle
$(t,x)\mapsto \partial_x f(t,x)$ existe et est continue sur $J\times X$
(i.e., $f$ est continûment différentiable par rapport à $x$). Alors pour
tout $(t_0,x_0)\in J\times X$, il existe une unique solution maximale
$x:I\to\mathbb{R}^n$ dans $S_f(t_0,x_0)$.
:::

::: {.section}
#### Démonstration {#démonstration-4 .proof}

Nous donnons ici le principe de la preuve qui peut être passée en
première lecture, mais qu'il est intéressant de comprendre d'un point de
vue scientifique. L'essentiel est en fait de montrer que sous
l'hypothèse de régularité de $f$ par rapport à $x$, il existe une unique
solution locale au problème de Cauchy. De là on peut ensuite déduire
qu'elle se prolonge en une unique solution maximale dans $J\times X$. La
partie cruciale est donc le résultat local suivant qui constitue en fait
le théorème initial de Cauchy-Lipschitz (sa généralisation aux solutions
globales étant plutôt dûe à [Picard et Lindelöf (p.
`\pageref*{rem_approx_succ}`{=tex})](#rem_approx_succ)).

**Théorème de Cauchy-Lipschitz local** Soient $J$ ouvert de
$\mathbb{R}$, $X$ ouvert de $\mathbb{R}^{n}$,
$f: J\times X \to \mathbb{R}^n$ continue et continûment différentiable
par rapport à $x$, et $(t_0,x_0)\in J\times X$. Soient $\tau>0$ et $r>0$
tels que $$
\mathcal{C}:=\left[t_0-\tau,t_0+\tau \right]\times \overline{B}(x_0,r)\subset J\times X \ .
$$ Pour tout $\tau_m\in \left[0,\tau \right]$ tel que
$\tau_m \max_{\mathcal{C}} \|f\| \leq r$, il existe une unique fonction
$x\in S_f(t_0,x_0)$ définie sur $[t_0-\tau_m,t_0+\tau_m]$.

**Démonstration**

La preuve consiste à voir les solutions comme des points fixes d'un
certain opérateur intégral, obtenu par la représentation intégrale des
solutions. Le théorème du point fixe de Banach permet ensuite de montrer
l'existence et l'unicité de ce point fixe.

Tout d'abord, $\mathcal{C}$ étant fermé et borné en dimension finie, par
continuité de $f$, $\max_\mathcal{C}\|f\|$ existe bien. Rappelons nous
du cours de Topologie que $E:=C([t_0-\tau_m,t_0+\tau_m],\mathbb{R}^n)$,
l'ensemble des fonctions continues de $[t_0-\tau_m,t_0+\tau_m]$ dans
$\mathbb{R}^n$ est un espace de Banach pour la norme uniforme
$\|\cdot\|_\infty$, et définissons\
$$
F = \{x\in E \: : \: x(\left[t_0-\tau_m,t_0+\tau_m \right])\subset \overline{B}(x_0,r) \} \ .
$$ On peut montrer que[^4] $F$ est un sous-ensemble fermé de $E$. $F$
est donc complet (toujours pour la norme uniforme $\|\cdot\|_\infty$).
Pour tout $x\in F$, par définition,
$(s,x(s))\in \mathcal{C}\subset J\times X$ pour tout
$s\in \left[t_0-\tau_m,t_0+\tau_m \right]$ ; on peut donc définir
l'opérateur $\Gamma : F\to E$ par $$
\Gamma(x)(t) = x_0+\int_{t_0}^t f(s,x(s))ds \qquad \forall t\in \left[ t_0-\tau_m,t_0+\tau_m \right] \ .
$$ Or d'après la [représentation intégrale des solutions (p.
`\pageref*{theo_eq_integrale}`{=tex})](#theo_eq_integrale), on sait
qu'une fonction $x\in F$ est solution du problème de Cauchy sur
$\left[ t_0-\tau_m,t_0+\tau_m \right]$ si et seulement si elle vérifie
$$
\Gamma(x)=x
$$ c'est-à-dire $x$ est un point fixe de $\Gamma$. Par ailleurs, on peut
prouver[^5] que pour tout $x\in S_f(t_0,x_0)$ définie sur
$\left[t_0-\tau_m,t_0+\tau_m \right]$, $x$ est dans $F$ : c'est donc un
point fixe $x^*$ de $\Gamma$ sur $F$. L'idée de la preuve est donc de
montrer que $\Gamma$ (ou une de ses itérées) est contractante pour
utiliser le théorème de point fixe sur un espace de Banach et en déduire
l'existence et l'unicité de ce point fixe.

D'abord, pour tout $x\in F$, pour tout
$t\in \left[t_0-\tau_m,t_0+\tau_m \right]$, $$
\|\Gamma(x)(t)-x_0\| \leq \left|\int_{t_0}^t \|f(s,x(s))\| ds \right| \leq \tau_m \max_{\mathcal{C}} \|f\| \leq r
$$ de sorte que $\Gamma(x)\in F$, i.e. $\Gamma:F\to F$. Ensuite, pour
tout $(x_a,x_b)\in F\times F$, pour tout
$t\in \left[t_0-\tau_m,t_0+\tau_m \right]$, $$
\|\Gamma(x_a)(t)-\Gamma(x_b)(t)\|\leq \left|\int_{t_0}^t \|f(s,x_a(s))-f(s,x_b(s))\| ds \right| \ .
$$ Soit $k=\max_\mathcal{C}\left\|\partial_x f \right\|$ (bien défini
car $\mathcal{C}$ est fermé et borné dans $\mathbb{R}^n$ et
$\partial_x f$ est continue par hypothèse). Alors l'application du
théorème des accroissement finis nous donne $$
\|\Gamma(x_a)(t)-\Gamma(x_b)(t)\|\leq  \left|\int_{t_0}^t k\|x_a(s)-x_b(s)\| ds \right| \leq |t-t_0| k \|x_a-x_b\|_{\infty} 
$$ et donc
$\|\Gamma(x_a)-\Gamma(x_b)\|_\infty \leq \tau_m k \|x_a-x_b\|_{\infty}$.
A ce stade, sauf si $\tau_m k<1$, $\Gamma$ n'est pas contractante.
Cependant, on peut montrer par récurrence que pour tout
$p\in \mathbb{N}$, et pour tout
$t\in \left[t_0-\tau_m,t_0+\tau_m \right]$, $$
\|\Gamma^p(x_a)(t)-\Gamma^p(x_b)(t)\|_\infty \leq \frac{(|t-t_0| k)^p}{p!} \|x_a-x_b\|_{\infty}
$$ en notant
$\Gamma^p = \underbrace{\Gamma \circ \Gamma \circ \ldots \circ \Gamma}_{p \text{ fois }}$.
Donc pour tout $p\in \mathbb{N}$,
$\|\Gamma^p(x_a)-\Gamma^p(x_b)\|_\infty \leq \frac{(\tau_m k)^p}{p!} \|x_a-x_b\|_{\infty}$.
Il existe donc $p$ suffisamment grand tel que $\Gamma^{p}$ est
contractante. D'après le théorème de point fixe de Banach, $\Gamma$
admet un unique point fixe $x^*$ dans $F$.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Remarque -- Relâchement à $f$ localement Lipschitzienne {#rem_f_lips .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Relâchement à \(f\) localement Lipschitzienne}`{=latex}

La première preuve d'existence et unicité locale de solutions sous
l'hypothèse que $f$ est continûment différentiable par rapport à $x$ est
dûe à Augustin Louis Cauchy (1820) et repose sur l'utilisation du
théorème d'accroissements finis[^6]. Mais on remarque dans notre preuve
qu'il suffirait qu'il existe $k>0$ tel que `\begin{multline*}
\|f(t,x_a)-f(t,x_b)\|\leq k \|x_a-x_b\| \\
 \forall t\in \left[t_0-\tau_m,t_0+\tau_m \right], \forall (x_a,x_b)\in \overline{B}(x_0,r)\times \overline{B}(x_0,r) \ ,
\end{multline*}`{=tex} c'est-à-dire que la fonction $f$ soit
*lipschitzienne* par rapport à $x$ au voisinage de $(t_0,x_0)$. Cette
propriété fut introduite par le mathématicien allemand Rudolf Lipschitz
quelques années plus tard (1868) pour prouver le même résultat de façon
indépendante : d'où le nom de *théorème de Cauchy-Lipschitz*. Notons que
cette dernière hypothèse est plus faible que celle de Cauchy car elle
impose seulement que $x\mapsto f(t,x)$ soit lipschitzienne au voisinage
de $(t_0,x_0)$, au lieu de différentiable. Par exemple, $x\mapsto |x|$
est lipschitzienne (mais pas différentiable) et $\dot{x}=|x|$ admet donc
une unique solution maximale quelque soit la condition initiale.
:::

::: {.section}
### Remarque -- Approximations successives {#rem_approx_succ .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Approximations successives}`{=latex}

Mise à part quelques formes particulières de $f$, il est très rare de
savoir résoudre explicitement une équation différentielle. Cependant, la
preuve (dans sa forme moderne donnée plus haut) caractérise la solution
comme le point fixe de l'opérateur $\Gamma$. Or, on sait par la preuve
du théorème du point fixe de Banach que ce point fixe est la limite
uniforme de la suite des itérées de $\Gamma$. En pratique, on peut donc
s'approcher arbitrairement proche de la solution sur l'intervalle
$\left[t_0-\tau_m,t_0+\tau_m \right]$ (au sens de la norme uniforme), en
calculant la suite $x_{p+1} = \Gamma(x_p)$ définie par $$
x_{p+1}(t) =  x_0+\int_{t_0}^t f(s,x_p(s))ds  ,
$$ en notant ici de manière abusive $x_0$ la fonction constante égale à
$x_0$. Cette méthode de recherche de point fixe porte le nom
d'*approximations successives* et est introduite pour la première fois
par le mathématicien français Emile Picard à la fin du XIXème siècle
grâce aux progrès de l'analyse fonctionnelle. C'est finalement le
mathématicien finlandais Ernst Lindelöf qui donne à la preuve sa forme
moderne en utilisant en 1894 la théorie des espaces de Banach. Pour les
anglophones, ce théorème s'appelle d'ailleurs le *théorème de
Picard-Lindelöf*.
:::

::: {.section}
#### Exemple -- Unicité des solutions maximales {#ex_lips .example .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Unicité des solutions maximales}`{=latex}

-   Une équation différentielle *linéaire*, c'est-à-dire pour laquelle
    il existe $A:I\to\mathbb{R}^{n\times n}$ et $b:I\to\mathbb{R}^n$
    continues telles que $$
    f(t,x) = A(t) x + b(t) \ ,
    $$ admet une unique solution maximale quelque-soit sa condition
    initiale $(t_0,x_0)\in \mathbb{R}\times \mathbb{R}^n$, car
    $J_f(t,x) = A(t)$ est continue.

-   Les équations décrivant l'évolution de la tension dans un circuit
    RLC ou la cinétique chimique données au début de ce cours admettent
    une unique solution maximale au voisinage de toute condition
    initiale $(t_0,x_0)$. C'est aussi le cas des équations de la
    mécanique Newtonnienne ou Lagrangienne si les forces/couples
    $F_k(t,q,\dot{q})$ sont continûment différentiable par rapport à la
    position et la vitesse $(q,\dot{q})$.
:::

::: {.section}
#### Exercice -- Unicité de la solution maximale ($\mathord{\bullet}$) {#ini_sol .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Unicité de la solution maximale}`{=latex}

Justifier que pour toute condition initiale,\
$$
\begin{array}{rcl}
\dot{x}_1 &=& \sin x_1 - \sqrt{|t|} x_2 \\
\dot{x}_2 &=& \sqrt{1+x_1^2}
\end{array}
$$ admet une unique solution maximale définie sur $\mathbb{R}$.
([Solution p.
`\pageref*{answer-ini_sol}`{=tex}](#answer-ini_sol){.no-parenthesis}.)
:::
:::
:::

::: {.section}
Régularité et stabilité des solutions
=====================================

Depuis l'apparition de la mécanique Newtonienne au XVIIème sciècle,
l'étude des équations différentielles a toujours été motivée par
l'espoir de compréhension et de prédiction du comportement futur ou
passé de systèmes physiques. En particulier, une question ayant taraudé
et divisé les scientifiques au cours des siècles est celle de la
stabilité du système à trois corps (Terre-Lune-Soleil), ou plus
généralement du système solaire. Enchanté devant les avancées de la
mécanique céleste, Pierre-Simon Laplace écrit en 1814 :

> Nous devons donc envisager l'état présent de l'univers comme l'effet
> de son état antérieur, et comme la cause de celui qui va suivre. Une
> intelligence qui pour un instant donné connaîtrait toutes les forces
> dont la nature est animée et la situation respective des êtres qui la
> composent, si d'ailleurs elle était assez vaste pour soumettre ses
> données à l'analyse, embrasserait dans la même formule les mouvements
> des plus grands corps de l'univers et ceux du plus léger atome : rien
> ne serait incertain pour elle, et l'avenir comme le passé serait
> présent à ses yeux.

Cette conviction *déterministe*, c'est-à-dire que les phénomènes
physiques passés ou futurs sont entièrement déterminés par leur
condition initiale, fut confirmée par le théorème de Cauchy-Lipschitz
quelques années plus tard. Ce dernier suggère en effet que l'on peut
prévoir l'évolution des systèmes physiques par la seule connaissance de
leur condition initiale et de leur modèle physique.

Cependant, à la fin du XIXème siècle, on se rend vite compte que la
réalité est en fait toute autre :

-   d'une part, la condition initiale et le modèle ne sont jamais
    parfaitement connus : quelle est alors la qualité de notre
    prédiction ?

-   d'autre part, ne pouvant généralement pas calculer explicitement la
    solution, comment anticiper son comportement sur des temps longs,
    voire son comportement asymptotique ?

::: {.section}
Sensibilité aux conditions initiales et erreurs de modèle
---------------------------------------------------------

La première question fut soulevée par Henri Poincaré à la fin du XIXème
siècle alors qu'il s'attelle à la question de la stabilité du système
solaire.

Le théorème suivant nous montre que pour un horizon de temps fini donné,
on peut obtenir une solution arbitrairement précise si le système est
initialisé suffisamment précisément et si les perturbations (ou erreurs
de modèle) sont suffisamment faibles. En d'autres termes, la solution
est *continue* par rapport aux perturbations en temps fini. Ceci est
crucial en physique puisque l'on ne peut jamais modéliser tous les
phénomènes parfaitement.

::: {.section}
### Théorème -- Régularité en temps fini {#theo_reg_CI .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Régularité en temps fini}`{=latex}

Soient $J$ ouvert de $\mathbb{R}$, $X$ ouvert de $\mathbb{R}^{n}$,
$f: J\times X \to \mathbb{R}^n$ continue et continûment différentiable
par rapport à $x$, $(t_0,x_0)\in J\times X$, et $x:I\to\mathbb{R}^n$
l'unique solution maximale dans $S_f(t_0,x_0)$. Pour tout
$\underline{t},\overline{t}$ tel que
$t_0\in\left[\underline{t},\overline{t} \right]\subset I$, il existe
$\delta_m>0$ et $\lambda\in \mathbb{R}$ tels que pour
$\delta\in \mathbb{R}^n$ tel que $|\delta|\leq \delta_m$, l'unique
solution maximale $x_\delta$ dans $S_f(t_0,x_0+\delta)$ est définie au
moins sur $\left[\underline{t},\overline{t} \right]$ et vérifie $$
|x(t)-x_{\delta}(t)| \leq e^{\lambda (t-t_0)} |\delta| \qquad \forall t\in \left[\underline{t},\overline{t} \right] \ .
$$

La présence du facteur exponentiel n'est pas cruciale ici, et servira
dans la suite. Ce qui est important, c'est que plus l'erreur de
condition initiale $\delta$ est faible, plus l'erreur sur la trajectoire
à horizon de temps fini $\overline{t}$ est faible. On dit alors que la
solution du problème de Cauchy est continue par rapport à la condition
initiale à horizon de temps fini. Attention, l'hypothèse "continûment
différentiable par rapport à $x$" est importante encore ici, comme
illustré dans l'exercice *[Ecoulement dans un réservoir (p.
`\pageref*{exo_Torricelli}`{=tex})](#exo_Torricelli)*. Elle peut
toutefois être relâchée à "$f$ localement lipschitzienne par rapport à
$x$" comme dans le cas du Théorème de Cauchy-Lipschitz.
:::

::: {.section}
#### Démonstration {#démonstration-5 .proof}

Prouvé dans l'exercice [*Autour du Lemme de Grönwall* (p.
`\pageref*{exo_gronwall}`{=tex})](#exo_gronwall).`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Exemple -- Continuité des solutions par rapport aux perturbations {#ex_contCI .example .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Continuité des solutions par rapport aux perturbations}`{=latex}

-   Si $\lambda<0$, l'erreur commise sur la condition initiale disparait
    au cours du temps dans les solutions : on dit qu'elles "oublient"
    leur condition initiales et que le système est *contractant*.

-   On peut aussi déduire de ce résultat la continuité des solutions par
    rapport à des paramètres $p$ intervenant dans la fonction $f$. En
    effet, il suffit de considérer le système étendu `\begin{align*}
    \dot{y} &= f(t,y,p)\\
    \dot{p} &= 0
    \end{align*}`{=tex} pour lequel l'incertitude de paramètre se ramène
    à une incertitude de condition initiale.

-   Considérons un système linéaire à paramètre et/ou condition initiale
    incertains $$
    \dot{x} = (a+\delta_a) x \qquad , \qquad x_0 = c +\delta_{c}
    $$ Pour $\delta_a=0=\delta_c$, la solution est $x(t)=ce^{at}$, et
    sinon $$
    x_\delta(t)= (c+\delta_c)e^{(a+\delta_a)t} \ .
    $$ On a donc pour tout $t$, $$
    \|x(t)-x_\delta(t)\| = \|c- (c+\delta_c)e^{\delta_a t}\| e^{at} \leq \left(|\delta_c|e^{\delta_a t} + |1-e^{\delta_a t}| |c| \right) e^{at} 
    $$ et pour tout $\overline{t}>0$ et
    $|\delta_a| \leq \frac{1}{\overline{t}}$ $$
    \sup_{t\in [0,\overline{t}] } \|x(t)-x_\delta(t)\| \leq \left( |\delta_c|e^{\delta_a\overline{t}} + |\delta_a|  |c| \overline{t}\right) e^{a\overline{t}}
    $$ qui peut être rendu aussi faible que voulu si $\delta_a$ et
    $\delta_c$ sont suffisamment petits. On voit bien ici que cette
    différence est bornée en temps fini, mais pas forcément
    aymptotiquement en particulier si $a>0$.

-   L'outil [Fibre](https://portsmouth.github.io/fibre/)[^7] permet
    d'observer en dimension 3 cette continuité des solutions par rapport
    aux conditions initiales, en affichant les trajectoires pour un
    ensemble de conditions initiales dont la taille est contrôlée à la
    souris: à "Integration Time" fixé, plus on réduit la *boîte* de
    condition initiales, plus les solutions se rapprochent les unes des
    autres. Par contre, lorsque l'on augmente le "Integration Time" les
    solutions s'écartent.
:::

::: {.section}
### Remarque -- Chaos déterministe et horizon de Lyapunov {#rem_chao .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Chaos déterministe et horizon de Lyapunov}`{=latex}

Même si la continuité des solutions par rapport aux
paramètres/conditions initiales donne à espérer de pouvoir simuler et
prédire l'évolution de systèmes physiques, elle est malheureusement
parfois insuffisante. Henri Poincaré écrit :

> Si nous connaissions exactement les lois de la nature et la situation
> de l'univers à l'instant initial, nous pourrions prédire exactement la
> situation de ce même univers à un instant ultérieur. Mais, lors même
> que les lois naturelles n'auraient plus de secret pour nous, nous ne
> pourrions connaître la situation qu'approximativement. Si cela nous
> permet de prévoir la situation ultérieure avec la même approximation,
> c'est tout ce qu'il nous faut, nous disons que le phénomène a été
> prévu, qu'il est régi par des lois ; mais il n'en est pas toujours
> ainsi, il peut arriver que de petites différences dans les conditions
> initiales en engendrent de très grandes dans les phénomènes finaux ;
> une petite erreur sur les premières produirait une erreur énorme sur
> les derniers. La prédiction devient impossible.

En effet, le précédent théorème nous prouve seulement que des
perturbations suffisamment petites donnent des solutions arbitrairement
proches en temps fini. Mais, en pratique, il est rarement possible de
choisir l'amplitude des perturbations (erreurs de capteurs, erreurs
numériques etc.) et il se pourrait que l'ordre de grandeur des
perturbations produisant des erreurs *acceptables* sur les solutions ne
soit pas réalisable. Plus précisément, le théorème suggère qu'à
perturbation $|\delta|$ donnée, l'écart entre les solutions pourrait
croître exponentiellement vite. C'est le cas bien sûr des systèmes qui
divergent exponentiellement (tels que $\dot{x}=x$), mais aussi de
certains systèmes à trajectoires bornées, pour lesquels il existe
$\overline{t}>0$ tel que $$
\frac{|x(t)-x_\delta(t)|}{|\delta|} \approx e^{\lambda t}  \qquad \forall t\leq \overline{t} \ .
$$ Dans ce cas, $\frac{1}{\lambda}$ représente l'ordre de grandeur du
temps maximal jusqu'auquel l'erreur sur les solutions reste du même
ordre de grandeur que l'erreur initiale : on parle d'*horizon de
Lyapunov*. Toute prédiction au delà de cet horizon est illusoire et le
système est alors dit *chaotique*.

Il est important d'insister sur le caractère *déterministe* de ce
chaos : chaque cause entraîne un effet bien déterminé mais deux causes
très proches peuvent avoir des effets très différents.
:::

::: {.section}
#### Exemple -- Systèmes chaotiques {#ex_chaos .example .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Systèmes chaotiques}`{=latex}

-   Henri Poincaré met en évidence le premier un comportement chaotique
    des solutions du problème à 3 corps. Ses livres sont disponibles en
    ligne [@poincare].

-   En 1963, Edward Lorenz met en évidence pour la première fois le
    comportement possiblement chaotique de la météorologie à travers un
    modèle simplifié à trois dimensions de convection donné par
    `\begin{align*}
    \dot{x}_1 &= \sigma (x_2-x_1) \\
    \dot{x}_2 &= \rho \, x_1 - x_2 -x_1x_3 \\
    \dot{x}_3 &= x_1x_2-\beta x_3 
    \end{align*}`{=tex} où $\sigma$, $\rho$ et $\beta$ sont des
    paramètres strictement positifs. Pour $\sigma=10$, $\beta=8/3$ et
    $\rho=28$, ce système présente un attracteur en forme de papillon,
    où les trajectoires passent de manière *chaotique* d'une aile à
    l'autre, comme représenté sur la [figure (p.
    `\pageref*{fig_attracteur_lorenz}`{=tex})](#fig_attracteur_lorenz)
    ci-dessous. La croissance exponentielle de l'erreur se visualise en
    simulation : voir pour cela le notebook Equations
    Différentielles.ipynb.

-   En 1989, l'astronome français Jacques Laskar met en évidence
    numériquement le caractère chaotique des orbites des planètes de
    notre système solaire, en particulier celle de Mercure, dont les
    variations d'excentricité pourraient entraîner des collisions ou
    éjections de planètes dans certains scénarios long-termes. Ces
    travaux sont confirmés en 1992 par Gerald Jay Sussman et Jack
    Wisdom, qui démontrent que le système solaire est chaotique avec un
    horizon de Lyapunov de l'ordre de 4 million d'années [@SussWis].

-   Plus généralement, les systèmes chaotiques apparaissent dans des
    domaines très divers, comprenant l'économie, l'électricité, la
    mécanique, la médecine. Parfois, le comportement chaotique apparaît
    seulement lorsque le système est soumis à certaines excitations, par
    exemple une excitation sinusoïdale du pendule ou de l'oscillateur de
    Van der Pol [@HolRand].

![Trajectoire de l'oscillateur de
Lorenz](images/attracteur_lorenz.py.pdf){#fig_attracteur_lorenz}
:::
:::

::: {.section}
Propriétés asymptotiques
------------------------

Dans la section précédente nous avons répondu à la première question qui
était la sensibilité des solutions aux erreurs de condition initiale et
de modèle. Mais cette étude était en temps fini et nous nous intéressons
maintenant à la seconde question qui est le comportement asymptotique
des solutions. L'étude théorique asymptotique des solutions prend ses
origines dans la thèse de Lyapunov [@lyap]. Le but est de rechercher des
critères sur la fonction $f$ qui nous permettent de prédire ce
comportement : est-ce que les solutions divergent ? est-ce qu'elles
tendent vers un point en particulier ? vers un cycle limite ?

Dans la suite, pour simplifier, nous étudions les équations
différentielles dites *autonomes*, c'est-à-dire dont la fonction $f$ est
indépendante du temps. On se donne donc une fonction continue
$f:X\subset\mathbb{R}^n\to \mathbb{R}^n$, et on prend par défaut
$t_0=0$.

::: {.section}
### Définition -- Point d'équilibre {#def_ptEq .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Point d'équilibre}`{=latex}

On appelle *point d'équilibre* un point $a\in X$ tel que $$
f(a) = 0  \ .
$$ En d'autres termes, la fonction constante égale à $a$ est alors
solution de $\dot{x}=f(x)$.
:::

::: {.section}
#### Exemple -- Pendule {#ex_pendule .example .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Pendule}`{=latex}

L'évolution d'un pendule de longueur $\ell$ et de masse $m$ dans le
champ de l'apesanteur $g$ peut être décrit par une dynamique du type $$
\ddot{\theta} = - \frac{\rho}{m} \dot{\theta} -\frac{g}{\ell} \sin\theta 
$$ avec $\rho\geq 0$ un coefficient de frottement. En prenant
$x=(\theta,\dot{\theta})$, on obtient le système $$
\begin{array}{rcl}
\dot{x}_1 &=& x_2 \\
\dot{x}_2 &=& - \frac{\rho}{m} x_2 -\frac{g}{\ell} \sin x_1
\end{array}
$$ Ce système a pour points d'équilibre $(k\pi,0)$, $k\in \mathbb{Z}$,
qui correspondent soit à la position *basse* du pendule $\theta=0$ ou la
position *haute* $\theta=\pi$, toutes deux à vitesse nulle
$\dot{\theta}=0$. Si le pendule est initialisé exactement à sa position
haute ou basse à vitesse nulle alors il y reste indéfiniment.
:::

::: {.section}
### Définition -- Attractivité {#def_attract .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Attractivité}`{=latex}

Un point d'équilibre $a$ est dit *localement attractif* si *toutes les
solutions maximales initialisées suffisamment proche de $a$ sont
globales et convergent vers $a$*, c'est-à-dire s'il existe $\eta>0$ tel
que pour tout $x_0$ vérifiant $|x_0-a|\leq \eta$, toute solution
maximale $x \in S_f(x_0)$ est définie sur $\mathbb{R}_{\geq 0}$ et
vérifie $$
\lim_{t\to+\infty} x(t)=a \ .
$$ De plus, $a$ est dit *globalement attractif* si *toutes les solutions
maximales sont globales et convergent vers $a$*.

Cette notion intuitive ne dit rien sur le comportement des solutions
pendant le transitoire, c'est-à-dire avant de converger vers $a$. Des
solutions initialisées proche de $a$ pourraient s'en éloigner
arbitrairement loin avant de converger, ou mettre un temps
arbitrairement long pour revenir dans un voisinage de $a$. Pour garantir
une certaine uniformité et robustesse de cette attractivité par rapport
à la condition initiale, on a recours à une notion plus forte qui est la
*stabilité asymptotique*.
:::

::: {.section}
### Définition -- Stabilité, stabilité asymptotique {#def_stab .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Stabilité, stabilité asymptotique}`{=latex}

Un point d'équilibre $a$ est dit:

-   *stable* si *les solutions restent arbitrairement proche de $a$
    quand elles sont initialisées suffisamment proche de $a$*,
    c'est-à-dire pour tout $\varepsilon >0$, il existe $\eta>0$ tel que
    pour tout $x_0$ vérifiant $|x_0-a|\leq \eta$, toute solution
    maximale $x \in S_f(x_0)$ est définie sur $\mathbb{R}_{\geq 0}$ et
    vérifie $$
    |x(t)-a|\leq \varepsilon \quad \forall t\in \mathbb{R}_{\geq 0}\ .
    $$

-   *instable* s'il n'est pas stable.

-   *localement (resp. globalement) asymptotiquement stable* s'il est à
    la fois stable en plus d'être localement (resp. globalement)
    attractif.
:::

::: {.section}
#### Exemple -- Stabilité du pendule {#ex_stab .example .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Stabilité du pendule}`{=latex}

-   Lorsqu'un pendule amorti est initialisé arbitrairement proche de sa
    position haute ou dans sa position haute mais à vitesse
    arbitrairement faible, il se met à osciller en passant par sa
    position basse : l'équilibre haut est donc instable, puisqu'on ne
    peut pas garder les trajectoires dans son voisinage. Par contre,
    lorsqu'il est initialisé proche de sa position basse, il oscille de
    façon amortie en tendant vers l'équilibre bas, qui est donc
    localement asymptotiquement stable. Voir le [portrait de phase du
    pendule amorti (p. `\pageref*{fig_pendule}`{=tex})](#fig_pendule).

-   Dans le cas d'un pendule non amorti par contre, c'est-à-dire avec
    $\rho=0$, le pendule oscille indéfiniment à énergie constante : la
    position basse est alors toujours stable mais plus attractive, et
    donc plus asymptotiquement stable. Voir le [portrait de phase du
    pendule non amorti (p.
    `\pageref*{fig_pendule}`{=tex})](#fig_pendule).
:::

::: {.section}
### Remarque -- Robustesse vis-à-vis des perturbations (pour la culture) {#rem_robustStab .remark .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Robustesse vis-à-vis des perturbations (pour la culture)}`{=latex}

L'avantage de la propriété de *stabilité asymptotique* par rapport à la
simple *attractivité* est qu'elle apporte de la robustesse par rapport
aux perturbations. En effet, lorsque qu'un point d'équilibre est
asymptotiquement stable, on peut montrer qu'en présence d'une
perturbation de la dynamique, les solutions restent asymptotiquement
arbitrairement proche de ce point d'équilibre si la perturbation est
suffisamment petite. Il y a donc une sorte de continuité des solutions
par rapport aux perturbations en temps infini (contrairement au résultat
général de continuité par rapport aux conditions initiales qui n'est
qu'en temps fini). Cette propriété n'est pas garantie lorsque le point
d'équilibre n'est qu'attractif et c'est la raison pour laquelle en
pratique, on essaye toujours d'assurer la stabilité asymptotique d'un
système : on sait alors que même en présence de perturbations
(inévitables en physique), le comportement du système sera proche du
comportement voulu.
:::

::: {.section}
### Théorème -- Stabilité d'un système linéaire stationnaire {#Hurwitz .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Stabilité d'un système linéaire stationnaire}`{=latex}

Soit $A\in \mathbb{R}^{n\times n}$. Le point d'équilibre 0 est
globalement asymptotiquement stable pour le système $$
\dot{x} = Ax
$$ si et seulement si les valeurs propres de $A$ sont toutes à partie
réelle strictement négative. On dit alors que la matrice est de
*Hurwitz*, du nom du mathématicien allemand Adolf Hurwitz.
:::

::: {.section}
#### Démonstration {#démonstration-6 .proof}

La notion de *globalement asymptotiquement stable* contient deux
propriétés : la stabilité et l'attractivité globale. On montrera en
[exercice (p. `\pageref*{attrac_stab}`{=tex})](#attrac_stab) que pour un
système linéaire, elles sont équivalentes à l'attractivité (locale),
c'est-à-dire que la stabilité et la globalité viennent gratuitement.
C'est une propriété propre aux systèmes linéaires. Il suffit donc de
trouver un critère caractérisant l'attractivité de 0. On a vu que les
solutions s'écrivent $$
x(t)= e^{At} x_0 \ .
$$ Si $A$ est diagonale, on a $x_i(t)=e^{\lambda_i t}x_{0,i}$, où
$\lambda_i$ sont les valeurs propres de $A$ et l'on voit bien que la
convergence des solutions vers 0 est équivalente à avoir $\lambda_i<0$.
Maintenant, si $A$ est diagonalisable, i.e., il existe
$P\in \mathbb{R}^{n\times n}$ inversible telle que $P^{-1} A P$ est
diagonale, on a $P^{-1} x(t) P = e^{P^{-1} A P t} P^{-1} x_0 P$, et
reproduisant le même argument, $P^{-1} x P$ (et donc $x$) converge vers
0 si et seulement si les entrées diagonales de $P^{-1} A P$, qui sont
les valeurs propres de $A$, sont à partie réelle strictement négative.
Ceci dit, toute matrice $A$ n'est pas diagonalisable. Par contre, il
existe toujours $P\in \mathbb{R}^{n\times n}$ inversible telle que $$
P^{-1} A P = D + N
$$ où $D$ est diagonale contenant les valeurs propres de $A$, $N$ est
nilpotente, c'est-à-dire qu'il existe $k\in \mathbb{N}$ tel que $N^k=0$,
et $D$ et $N$ commutent. C'est la forme dite *de Jordan*. Il s'ensuit
que $$
P^{-1} e^{At} P = e^{P^{-1} A Pt} = e^{Dt}e^{Nt} = e^{Dt}\sum_{i=0}^k \frac{1}{i!} N^i t^i
$$ converge vers zéro si et seulement si, encore, les valeurs propres de
$A$ sont à partie réelle négative.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
Attention ce critère n'est valable que pour $A$ constant. Le fait que
$A(t)$ soit de Hurwitz pour tout $t$ n'implique pas que les solutions du
système $$
\dot{x} = A(t) x 
$$ tendent vers 0 ou même restent bornées. Par exemple, la matrice $$
A(t) = \left( \begin{matrix} 
-1+1.5\cos^2t & 1-1.5\sin t \cos t \\
-1-1.5 \sin t \cos t & -1+\sin^2 t
\end{matrix}
\right)
$$ a des valeurs propres constantes égales à $-0.25\pm 0.25\sqrt{7}j$.
Pourtant, $\dot{x} = A(t) x$ admet des solutions non bornées pour $x(0)$
arbitrairement proche de 0.
:::

::: {.section}
#### Exercice -- Critère de stabilité d'un système linéaire plan ($\mathord{\bullet}$) {#crit_stab_dim2 .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Critère de stabilité d'un système linéaire plan}`{=latex}

Montrer que $A\in \mathbb{R}^{2\times 2}$ est de Hurwitz si et seulement
si $\text{tr} A <0$ et $\text{det} A >0$. Attention, ce critère ne
marche qu'en dimension 2 ! ([Solution p.
`\pageref*{answer-crit_stab_dim2}`{=tex}](#answer-crit_stab_dim2){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Oscillateur I ($\mathord{\bullet}$) {#ressort-1 .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Oscillateur I}`{=latex}

Considérons une masse $m$ évoluant sur un support horizontal et
accrochée à un mur via un ressort de raideur $k$. L'évolution de sa
position par rapport à sa position d'équilibre est décrite par\
$$
m\ddot{y} = - \lambda \dot{y} -k y \ ,
$$ où $\lambda$ est un coefficient de frottement.

1.  Réduire l'équation différentielle à l'ordre $1$ et déterminer les
    points d'équilibre.

2.  Justifier que les solutions maximales sont uniques et globales
    quelque soit la condition initiale $(y(0),\dot{y}(0))$.

3.  Etudier la stabilité des points d'équilibre pour $\lambda>0$ et
    $\lambda = 0$.

([Solution p.
`\pageref*{answer-ressort-1}`{=tex}](#answer-ressort-1){.no-parenthesis}.)
:::

::: {.section}
### Théorème -- Lien entre stabilité et stabilité du linéarisé tangent {#theo_linTangent .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Lien entre stabilité et stabilité du linéarisé tangent}`{=latex}

Soit $f:X \to \mathbb{R}^n$ continûment différentiable et $a\in X$ un
point d'équilibre.

Si les valeurs propres de la matrice jacobienne $J_f(a)$ sont toutes à
partie réelle strictement négative (Hurwitz) alors $a$ est localement
asymptotiquement stable.

Si $J_f(a)$ a au moins une valeur propre à partie réelle strictement
positive, alors $a$ est instable.
:::

::: {.section}
#### Démonstration {#démonstration-7 .proof}

Voir l'annexe [`\textit{Stabilité locale et linéarisé tangent}`{=tex}
(p.
`\pageref*{app_stab_lin}`{=tex})](#app_stab_lin).`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
Notons cependant que rien ne peut être conclu quant à la stabilité (ou
stabilité asymptotique) de $a$ si les parties réelles de $J_f(a)$ sont
négatives ou nulles : on peut avoir asymptotiquement stable, seulement
stable ou instable. Par exemple, 0 est globalement asymptotiquement
stable pour $$
\dot{x} = - x^3
$$ dont le linéarisé est nul en zéro, alors que $(0,0)$ est instable
pour `\begin{align*}
\dot{x}_1 &= x_2 \\
\dot{x}_2 &= 0
\end{align*}`{=tex} qui admet deux valeurs propres nulles.
:::

::: {.section}
#### Exemple -- Retour au pendule {#ex_pendule_jacob .example .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Retour au pendule}`{=latex}

Reprenons l'[exemple du pendule amorti (p.
`\pageref*{ex_pendule}`{=tex})](#ex_pendule). On a $$
J_f(0,0) = \left( \begin{matrix} 
0 & 1\\
-\frac{g}{\ell} & - \frac{\rho}{m}
\end{matrix}
\right) 
\qquad , \qquad 
J_f(\pi,0)= \left( \begin{matrix} 
0 & 1\\
\frac{g}{\ell} & - \frac{\rho}{m}
\end{matrix}
\right) 
$$ Dans le premier cas, $\text{tr}(J_f(0,0))<0$ et
$\text{det}(J_f(0,0))>0$. Comme prouvé en [exercice (p.
`\pageref*{answer-crit_stab_dim2}`{=tex})](#answer-crit_stab_dim2), ceci
implique en dimension 2 que $J_f(0,0)$ est de Hurwitz. Donc la position
basse $(0,0)$ est bien un équilibre asymptotiquement stable. Dans le
deuxième cas par contre, le produit des valeurs propres
$\lambda_1\lambda_2 = \text{det}(J_f(0,0))<0$. Elles ne peuvent donc pas
être complexes conjuguées et sont nécessairement réelles de signes
opposés. Il s'ensuit que l'une est strictement positive et la position
haute $(\pi,0)$ est donc bien instable.

Notons que si $\rho=0$, c'est-à-dire que le pendule n'est pas amorti,
les valeurs propres $J_f(0,0)$ sont imaginaires pures, et l'on ne peut
donc rien conclure quant à la stabilité des points d'équilibre. Une
étude plus approfondie est nécessaire.
:::

::: {.section}
#### Stabilité asymptotique I ($\mathord{\bullet}$) {#asymp_glob-1 .exercice .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Stabilité asymptotique I}`{=latex}

Montrer que le point d'équilibre $(0,0)$ est localement asymptotiquement
stable pour le système $$
\begin{array}{rcl}
\dot{x}_1 &=& x_2(1-x_2^2)\\
\dot{x}_2 &=& -(x_1+x_2)(1-x_1^2)
\end{array}
$$ L'est-il globalement ? ([Solution p.
`\pageref*{answer-asymp_glob-1}`{=tex}](#answer-asymp_glob-1){.no-parenthesis}.)
:::

::: {.section}
Lorsque le linéarisé ne permet pas de conclure sur la stabilité
asymptotique locale, ou que l'on veut un résultat global, on a recours à
la caractérisation non linéaire suivante.
:::

::: {.section}
### Théorème -- Caractérisation par Lyapunov {#theo_lyap .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Caractérisation par Lyapunov}`{=latex}

Soit $f: X \to \mathbb{R}^n$ continue, $a$ un point d'équilibre de $f$
dans $X$, et $W$ un voisinage de $a$ dans $X$. Soit
$V:W\to\mathbb{R}_{\geq 0}$ continûment différentiable telle que $$
V(x) > 0 \quad  \forall x\in W\setminus\{a\} \qquad , \qquad V(a)= 0 \ .
$$

-   Si $\langle\nabla V (x), f(x)\rangle \leq 0$ pour tout $x\in W$
    alors $a$ est stable.

-   Si $\langle \nabla V (x), f(x) \rangle < 0$ pour tout
    $x\in W\setminus \{a\}$ alors $a$ est localement asymptotiquement
    stable.

-   Si $\lim_{\|x\|\to +\infty} V(x) = +\infty$, $W=\mathbb{R}^n$, et
    $\langle\nabla V (x), f(x)\rangle < 0$ pour tout $x\neq a$ alors $a$
    est globalement asymptotiquement stable.

$V$ est alors appelée *fonction de Lyapunov*. En fait, $$
\langle\nabla V (x(t)), f(x(t))\rangle = \langle\nabla V (x(t)), \dot{x}(t)\rangle = \frac{d}{dt} V(x(t))
$$\
le long d'une trajectoire $t\mapsto x(t)$ de l'équation différentielle
$\dot{x} = f(x)$. $V$ représente donc une grandeur positive qui décroît
ou est conservée le long des trajectoires. Pour des systèmes physiques,
elle est souvent reliée à l'énergie.

Le fait que $\lim_{\|x\|\to +\infty} V(x)= +\infty$ sert à montrer que
toute les trajectoires sont bornées et donc définies pour tout $t$. Sans
cette hypothèse, et même si $V$ décroit strictement le long de toutes
les trajectoires, on pourrait avoir des trajectoires qui explosent en
temps fini.
:::

::: {.section}
#### Démonstration {#démonstration-8 .proof}

Supposons d'abord que $\langle\nabla V (x), f(x)\rangle \leq 0$ pour
tout $x\in W$. On a donc pour toute solution $t\mapsto x(t)$ initialisée
dans $W$, $V(x(t))\leq V(x(0))$ tant que $x(t)\in W$. Prenons
$\varepsilon>0$ suffisamment petit tel que
$\overline{B}(a,2\varepsilon)\subset W$. On veut montrer qu'il existe
$\eta$ tel que toute trajectoire initialisée dans $B(a,\eta)$ reste dans
$B(a,\varepsilon)\subset W$. Tout d'abord, il existe $\varepsilon_V>0$
tel que $$
\forall x\in \overline{B}(a,2\varepsilon) \ : \ V(x)\leq \varepsilon_V \ \Longrightarrow x\in B(a,\varepsilon) \ .
$$ En effet, sinon, il existerait une suite $(x_k)_{k\in \mathbb{N}}$
d'éléments de $\overline{B}(a,2\varepsilon)$ telle que pour tout $k>0$,
$V(x_k)\leq \frac{1}{k}$ et $\|x_k-a\|\geq \varepsilon$. L'ensemble
$\overline{B}(a,2\varepsilon)$ étant fermé et borné donc compact, on
peut en extraire une sous-suite convergeant vers $x^\star$ qui vérifie
nécessairement $V(x^\star)=0$ par continuité de $V$ et
$\|x^\star-a\|\geq \varepsilon$, i.e. $x^\star \neq a$. Ceci est
impossible par hypothèse. On a donc l'existence de $\varepsilon_V$.
Maintenant, par continuité de $V$ en $a$ et puisque $V(a)=0$, il existe
aussi $\eta>0$ tel que $$
x\in B(a,\eta)  \ \Longrightarrow V(x)\leq \varepsilon_V \ .
$$ Alors si $x(0)\in B(a,\eta)$, $V(x(t))\leq V(x(0))\leq \varepsilon_V$
donc $x(t)\in B(a,\varepsilon)\subset W$ pour tout $t$ tant qu'elle est
définie. Par le [théorème du domaine maximal d'existence (p.
`\pageref*{theo_bouts}`{=tex})](#theo_bouts), $x$ est définie sur
$\mathbb{R}_{\geq 0}$. Ceci prouve la stabilité de $a$.

Supposons maintenant $\langle\nabla V (x), f(x)\rangle < 0$ pour tout
$x\in W\setminus \{a\}$. Alors par le point précédent $a$ est stable. Il
suffit de montrer l'attractivité locale. Par stabilité, si
$x(0)\in B(a,\eta)$, $x(t)\in B(a,\varepsilon)\subset W$ pour tout $t$
et $t\to V(x(t))$ est donc strictement décroissante. Comme elle est
aussi bornée inférieurement par 0, elle converge vers $\ell \geq 0$.
Supposons $\ell>0$. Alors, par continuité de $V$, il existe
$0<\nu<\varepsilon$ et $\overline{t}>0$ tel que pour tout
$t\geq \overline{t}$, $\|x(t)-a\| \geq \nu$. Soit $$
\gamma = \max_{\nu \leq \max \|x(t)-a\| \leq \varepsilon} \langle\nabla V (x), f(x)\rangle   
$$ qui existe par continuité de $V$ sur un compact. Puisque
$\langle\nabla V (x), f(x)\rangle < 0$ sur $W\setminus \{a\}$,
$\gamma<0$. Alors, pour tout $t\geq \overline{t}$, $$
V(x(t)) = V(x(\overline{t})) + \int_0^t \langle\nabla V (x(t)), f(x(t))\rangle \leq  V(x(\overline{t})) + \gamma (t-\overline{t}) \ .
$$ Mais comme $\gamma<0$ cette quantité devient strictement négative au
bout d'un certain temps, ce qui est impossible. Donc
$\lim_{t\to +\infty} V(x(t))=0$. Finalement, reproduisant le même
raisonnement que pour l'existence de $\varepsilon_V$, on peut garantir
que $\|x-a\|$ est arbitrairement petit en prenant $V(x)$ suffisamment
petit. Donc on en déduit que $\lim_{t\to +\infty} \|x(t)-a\|=0$.

Supposons enfin que $\lim_{\|x\|\to +\infty} V(x) = +\infty$ et
$W=\mathbb{R}^n$. Alors $V(x(t))< V(x(0))$ pour tout $t\in I$ donc
$x(t)\in V^{-1}(\left[ 0,V(x(0)) \right])$ pour tout $t$. Le fait que
$\lim_{\|x\|\to +\infty} V(x) = +\infty$ est équivalent au fait que
l'image réciproque de toute compact est compact (on dit que $V$ est
propre). Donc $V^{-1}(\left[ 0,V(x(0)) \right])$ est compact et par le
[théorème du domaine maximal d'existence nécessairement (p.
`\pageref*{theo_bouts}`{=tex})](#theo_bouts) $x(t)$ est défini pour tout
$t\geq 0$, et reste dans ce compact. Alors on peut reproduire le même
raisonnement que plus haut et obtenir la convergence de $x$ vers
$a$.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Exemple -- Pendule par Lyapunov {#ex_pendule_lyap .example .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Pendule par Lyapunov}`{=latex}

Reprenons le [pendule (p. `\pageref*{ex_pendule}`{=tex})](#ex_pendule)
mais cette fois-ci, non amorti, c'est-à-dire avec $\rho=0$. Nous n'avons
pas pu prouver la stabilité du point d'équilibre $(0,0)$ par l'étude de
la matrice Jacobienne car ses valeurs propres sont imaginaires pures.
Essayons par analyse de Lyapunov. Inspirés par la physique, considérons
$V:\left] -\pi, \pi\right[\times \mathbb{R}\to \mathbb{R}_{\geq 0}$
définie par $$
V(x_1,x_2) = \frac{1}{2} m\ell^2 x_2^2 + mg\ell(1-\cos(x_1)) \ .
$$ Le premier terme correspond à l'énergie cinétique du pendule, et le
deuxième son énergie potentielle. $V$ est continûment différentiable, à
valeurs positives et s'annule seulement en $x=0$. De plus, $$
\langle\nabla V (x), f(x)\rangle = m\ell^2 x_2\left(-\frac{g}{\ell} \sin x_1\right) + mg \ell \sin x_1 x_2 = 0
$$ ce qui traduit la conservation de l'énergie en l'absence de
frottement. On en déduit donc la stabilité du point d'équilibre $(0,0)$.

On peut se demander s'il existe toujours une fonction de Lyapunov autour
d'un point d'équilibre stable/asymptotiquement stable. La réponse est
oui, mais c'est une question délicate étudiée en détail dans [@BacRos].
:::

::: {.section}
#### Exercice -- Oscillateur II ($\mathord{\bullet}$) {#ressort-2 .exercise .question .one .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Oscillateur II}`{=latex}

Reprendre l'[exercice sur le ressort (p.
`\pageref*{ressort-1}`{=tex})](#ressort-1) et montrer que l'équilibre
$(0,0)$ est stable pour $\lambda =0$. ([Solution p.
`\pageref*{answer-ressort-2}`{=tex}](#answer-ressort-2){.no-parenthesis}.)
:::

::: {.section}
#### Exercice -- Stabilité asymptotique II ($\mathord{\bullet}\mathord{\bullet}$) {#asymp_glob-2 .exercise .question .two .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Stabilité asymptotique II}`{=latex}

Montrer que $(0,0)$ est globalement asymptotiquement stable pour $$
\begin{array}{rcl}
\dot{x}_1 &=& x_2\\
\dot{x}_2 &=& -x_1^3-x_2
\end{array}
$$ *Indice : Essayer de trouver une fonction de Lyapunov... $x_2^2$
donne de la négativité en $x_2$, $(x_1+x_2)^2$ de la négativité en
$x_1$... voir comment compléter...*. ([Solution p.
`\pageref*{answer-asymp_glob-2}`{=tex}](#answer-asymp_glob-2){.no-parenthesis}.)
:::
:::
:::

::: {.section}
Exercices complémentaires
=========================

En plus des exercices essentiels, les exercices à maîtriser sont marqués
d'une croix (+).

::: {.section}
Ecoulement dans un réservoir ($+$) {#exo_Torricelli .exercice}
----------------------------------

Considérons un réservoir cylindrique de section $S$ qui se vide par une
ouverture de section $s$ située à sa base. On note $x$ la hauteur de
liquide dans le réservoir. D'après la *loi de Torricelli*[^8],
l'équation d'évolution de $x$ est donnée par $$
\dot{x}=-k\sqrt{|x|} \qquad k = \frac{s}{S}\sqrt{2g}
$$ où $g$ est la pesanteur.

::: {.section}
#### Question 1 {#tor-1 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Etant donné un temps initial $t_0$ et une hauteur initiale $x_0\geq 0$,
justifier sans calcul que le problème de Cauchy associé admet des
solutions et que les solutions maximales sont globales. Pour quelles
valeurs de $x_0$ pouvons-nous dire qu'elles sont uniques ? ([Solution p.
`\pageref*{answer-tor-1}`{=tex}](#answer-tor-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 {#tor-2 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Pour $(t_0,x_0)\in \mathbb{R}\times \mathbb{R}_{\geq0}$, résoudre le
problème de Cauchy associé en se restreignant aux solutions
$x(t)\geq 0$. ([Solution p.
`\pageref*{answer-tor-2}`{=tex}](#answer-tor-2){.no-parenthesis}.)
:::

::: {.section}
#### Question 3 {#tor-3 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Comment pourrait s'interpréter physiquement la multitude de solutions
trouvées ? ([Solution p.
`\pageref*{answer-tor-3}`{=tex}](#answer-tor-3){.no-parenthesis}.)
:::

::: {.section}
#### Question 4 {#tor-4 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 4}`{=latex}

Les solutions sont-elles continues par rapport aux conditions initiales
au sens du [théorème de régularité des solutions (p.
`\pageref*{theo_reg_CI}`{=tex})](#theo_reg_CI) donné plus haut ?
Pourquoi ? ([Solution p.
`\pageref*{answer-tor-4}`{=tex}](#answer-tor-4){.no-parenthesis}.)
:::
:::

::: {.section}
Autour du Lemme de Grönwall {#exo_gronwall .exercice}
---------------------------

::: {.section}
#### Question 1 (Lemme de Grönwall) {#gro-1 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1 (Lemme de Grönwall)}`{=latex}

Soient $t^-, t^+\in \mathbb{R}$,
$u,\alpha, \beta : [t^-,t^+]\to\mathbb{R}_{\geq 0}$ continues, tels que
$$
u(t) \leq \alpha(t) + \int_{t_0}^{t}\beta(s) u(s)ds \qquad \forall t\in [t^-,t^+] \ .
$$ Montrer qu'alors $$
u(t) \leq \alpha(t) +  \int_{t_0}^{t} \alpha(s)\beta(s) \exp\left(\int_{s}^t\beta(r)dr \right) ds\qquad \forall t\in [t^-,t^+]\ .
$$ En déduire que si $\alpha$ est constant, $$
u(t) \leq \alpha \exp\left(\int_{t_0}^t\beta(r)dr \right) \qquad \forall t\in [t^-,t^+] \ .
$$ *Indice : poser $v(t)=\int_{t_0}^t\beta(s)u(s)ds$ et étudier la
dérivée de $v(t)\exp\left(-\int_{t_0}^t\beta(r)dr\right)$*. ([Solution
p. `\pageref*{answer-gro-1}`{=tex}](#answer-gro-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 {#gro-2 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Utiliser le Lemme de Grönwall pour montrer le [théorème d'existence
globale de solutions (p.
`\pageref*{theo_exist_glob}`{=tex})](#theo_exist_glob). ([Solution p.
`\pageref*{answer-gro-2}`{=tex}](#answer-gro-2){.no-parenthesis}.)
:::

::: {.section}
#### Question 3 {#gro-3 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Utiliser le Lemme de Grönwall pour montrer le [théorème de continuité
par rapport aux conditions initiales (p.
`\pageref*{theo_reg_CI}`{=tex})](#theo_reg_CI). Expliquer pourquoi le
théorème est toujours valable si $f$ est seulement localement
Lipschitzienne par rapport à $x$ sur $J\times X$. ([Solution p.
`\pageref*{answer-gro-3}`{=tex}](#answer-gro-3){.no-parenthesis}.)
:::
:::

::: {.section}
Cycle limite ($+$) {#exo_cycle-lim .exercice}
------------------

Considérons le système $$
\begin{array}{rcl}
\dot{x}_1 &=& x_1+x_2-x_1(x_1^2 + x_2^2)\\
\dot{x}_2 &=& -x_1+x_2-x_2(x_1^2 + x_2^2)
\end{array}
$$

::: {.section}
#### Question 1 {#cycle-lim-1 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Montrer que ce système admet un seul point d'équilibre. Etudier sa
stabilité. ([Solution p.
`\pageref*{answer-cycle-lim-1}`{=tex}](#answer-cycle-lim-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 {#cycle-lim-2 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Montrer que quelque-soit la condition initiale, le système admet une
unique solution maximale $x:I\to \mathbb{R}^2$. Soit
$V:\mathbb{R}^2\to\mathbb{R}$ définie par
$V(x) = \|x\|^2 = x_1^2+x_2^2$. En étudiant le signe de
$\frac{d}{dt}V(x(t))$, montrer que $[t_0,+\infty[ \subset I$. ([Solution
p.
`\pageref*{answer-cycle-lim-2}`{=tex}](#answer-cycle-lim-2){.no-parenthesis}.)
:::

::: {.section}
#### Question 3 {#cycle-lim-3 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Montrer que si $\|x(t_0)\|\neq 1$ alors $\|x(t)\|\neq 1$ pour tout
$t\in I$. ([Solution p.
`\pageref*{answer-cycle-lim-3}`{=tex}](#answer-cycle-lim-3){.no-parenthesis}.)
:::

::: {.section}
#### Question 4 {#cycle-lim-4 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 4}`{=latex}

En déduire le comportement des solutions en fonction de la condition
initiale. ([Solution p.
`\pageref*{answer-cycle-lim-4}`{=tex}](#answer-cycle-lim-4){.no-parenthesis}.)
:::
:::

::: {.section}
Attractivité locale implique stabilité asymptotique globale pour un système linéaire {#attrac_stab .question .unnumbered .unlisted}
------------------------------------------------------------------------------------

`\addcontentsline{toc}{subsection}{Attractivité locale implique stabilité asymptotique globale pour un
système linéaire}`{=latex}

Soit $A\in \mathbb{R}^{n\times n}$. Montrer que si 0 est localement
attractif pour $$
\dot{x} = Ax
$$ alors il l'est globalement et 0 est stable. ([Solution p.
`\pageref*{answer-attrac_stab}`{=tex}](#answer-attrac_stab){.no-parenthesis}.)
:::

::: {.section}
Contrôle d'un système {#exo_cont_lin .exercice}
---------------------

Soit le système décrit par $$
\dot{x} = x + u(t)
$$ où $t\mapsto u(t)$ est une entrée à choisir.

::: {.section}
#### Question 1 {#cont-lin-1 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Comment se comporte le système si $u\equiv 0$ ? ([Solution p.
`\pageref*{answer-cont-lin-1}`{=tex}](#answer-cont-lin-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 {#cont-lin-2 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Si on mesure $t\mapsto x(t)$, comment choisir $u$ pour rendre 0
globalement asymptotiquement stable ? ([Solution p.
`\pageref*{answer-cont-lin-2}`{=tex}](#answer-cont-lin-2){.no-parenthesis}.)
:::

::: {.section}
Plus généralement, considérons un système du type $$
\begin{array}{rcl}
\dot{x}_1 &=& x_2 \\
\dot{x}_2 &=& x_3 \\
&\vdots&\\
\dot{x}_{n-1} &=& x_n \\
\dot{x}_n &=& \phi(x) + u(t)
\end{array}
$$ avec $\phi:\mathbb{R}^n \to \mathbb{R}$ continue et
$u:\mathbb{R}\to \mathbb{R}$ à choisir.
:::

::: {.section}
#### Question 3 {#cont-lin-3 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Si on mesure $t\mapsto x(t)$, montrer que l'on peut toujours choisir
$t\mapsto u(t)$ pour rendre 0 globalement asymptotiquement stable.
([Solution p.
`\pageref*{answer-cont-lin-3}`{=tex}](#answer-cont-lin-3){.no-parenthesis}.)
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
#### Solutions globales I {#answer-glob_sol .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Solutions globales I}`{=latex}

Fixons une condition initiale dans $\mathbb{R}\times \mathbb{R}^2$. La
fonction
$f:(t,x_1,x_2)\mapsto (\sin x_1 - \sqrt{|t|} x_2 ,\sqrt{1+x_1^2})$ est
continue sur $\mathbb{R}\times\mathbb{R}^2$. Donc d'après les théorème
de Peano des solutions existent. D'après le théorème du domaine maximal
d'existence, les solutions maximales sont définies sur un intervalle de
temps $I$ ouvert.

Par ailleurs, on peut vérifier que pour tout $y\in \mathbb{R}$,
$\sqrt{1+y^2}\leq 1+|y|$, donc $$
|f_1(x)| \leq 1 + \sqrt(|t|) |x_2| \quad , \quad |f_2(x)|\leq 1 + |x_1|
$$ et $f$ est bornée par une fonction affine en $\|x\|$. Toutes les
solutions maximales sont donc globales, i.e. $I=\mathbb{R}$.
:::

::: {.section}
#### Solutions globales II {#answer-glob_sol2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Solutions globales II}`{=latex}

Considérons une condition initiale dans $\mathbb{R}\times \mathbb{R}^n$
et une solution maximale $t\mapsto x(t)$ définie sur un intervalle $I$
(qui existe d'après le théorème de Peano car $f$ est continue sur
$\mathbb{R}\times \mathbb{R}^n$). Alors $$
\frac{d}{dt} V(x(t)) = \langle\nabla V (x(t)), f(t,x(t))\rangle \leq a(t) V(x(t)) + b(t) \quad \forall t\in I \ ,
$$ et donc $$
\frac{d}{dt} \left[e^{-\int_{t_0}^t a(\tau) d\tau}  V(x(t))\right] \leq e^{-\int_{t_0}^t a(\tau) d\tau} b(t)  \quad \forall t\in I \ .
$$ En intégrant entre $t_0$ et $t\geq t_0$, $$
e^{-\int_{t_0}^t a(\tau) d\tau} V(x(t)) - V(x(t_0)) \leq \int_{t_0}^t e^{-\int_{t_0}^s a(\tau) d\tau} b(s) ds \quad \forall t\in I \cap [t_0,+\infty[
$$ et donc $$
V(x(t)) \leq e^{\int_{t_0}^t a(\tau) d\tau} V(x(t_0)) + \int_{t_0}^t e^{\int_{s}^t a(\tau) d\tau} b(s) ds \quad \forall t\in I \cap [t_0,+\infty[ \ .
$$ Une autre manière de faire est de montrer que $V(x(t))\leq v(t)$ où
$v$ est solution maximale de $$
\dot{v} = a(t) v + b(t)
$$ pour la condition initiale $v(t_0) = V(x(t_0))$, qui est définie est
continue sur $\mathbb{R}$ car la dynamique de $v$ est affine.

Or si $t_m^+= \sup I$ est fini, d'après le théorème du domaine maximal,
$(t,x(t))$ tend soit vers la frontière du domaine de définition de $f$,
soit diverge. Comme $f$ est définie et continue sur
$\mathbb{R}\times \mathbb{R}^n$, nécessairement
$\lim_{t\to t_m^+} \|x(t)\| = +\infty$ et donc
$\lim_{t\to t_m^+} V(x(t)) = +\infty$. Or par continuité de $a,b$ sur
$\mathbb{R}$, $$
\lim_{t\to t_m^+} V(x(t)) \leq e^{\int_{t_0}^{t_m^+} a(\tau) d\tau} V(x(t_0)) + \int_{t_0}^{t_m^+} e^{\int_{s}^{t_m^+} a(\tau) d\tau} b(s) ds   \ .
$$ C'est donc impossible et $t_m^+= +\infty$.
:::

::: {.section}
#### Unicité de la solution maximale {#answer-ini_sol .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Unicité de la solution maximale}`{=latex}

Nous avons vu dans l'exercice Solutions globales I que les solutions
maximales de ce système sont définies sur $\mathbb{R}$. Par ailleurs, la
fonction
$f:(t,x_1,x_2)\mapsto (\sin x_1 - \sqrt{|t|} x_2 ,\sqrt{1+x_1^2})$ est
continûment différentiable par rapport à $x$ sur
$\mathbb{R}\times\mathbb{R}^2$. Donc pour chaque condition initiale dans
$\mathbb{R}\times\mathbb{R}^2$, il existe une unique solution maximale.
:::

::: {.section}
#### Critère de stabilité d'un système linéaire plan {#answer-crit_stab_dim2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Critère de stabilité d'un système linéaire plan}`{=latex}

Soient $\lambda_1$ et $\lambda_2$ les valeurs propres d'une matrice $A$
de dimension 2. Son polynôme caractéristique est donné par $$
s^2 - \text{tr} A s + \det A = (s-\lambda_1)(s-\lambda_2) = s^2 - (\lambda_1+\lambda_2)  s + \lambda_1\lambda_2 \ .
$$ Donc $\text{tr} A = \lambda_1+\lambda_2$ et
$\det A = \lambda_1\lambda_2$. Il y a deux cas: soit les valeurs propres
sont complexes conjuguées, soit elles sont réelles.

Si $\lambda_i = \lambda_0 \pm j\omega$, alors
$\lambda_1\lambda_2=\lambda_0^2+\omega^2$ et
$\lambda_1+\lambda_2 = 2\lambda_0$. Donc $\lambda_0<0$ si et seulement
si $\text{tr} A <0$ (et on a alors toujours $\det A>0$).

Si les valeurs propres sont réelles, les avoir toutes deux strictement
négatives implique que $\lambda_1\lambda_2>0$ et
$\lambda_1+\lambda_2<0$. Réciproquement, si $\lambda_1\lambda_2>0$,
elles sont non nulles et du même signe, et si de plus
$\lambda_1+\lambda_2<0$, ce signe est nécessairement négatif.

Donc dans tous les cas, $\lambda_i$ à parties réelles strictement
négatives équivaut à $\text{tr} A <0$ et $\det A>0$.
:::

::: {.section}
#### Oscillateur I {#answer-ressort-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Oscillateur I}`{=latex}

Prenons $x=(y,\dot{y})$ qui vérifie $$
\dot{x} = 
\left(
\begin{matrix}
x_2\\
-\frac{k}{m} x_1 &-\frac{\lambda}{m} x_2
\end{matrix}
\right) 
=
A x
$$ avec
$A=\left( \begin{matrix} 0&1\\ -\frac{k}{m}&-\frac{\lambda}{m} \end{matrix} \right)$.
Puisque $A$ est inversible ($\text{det} A=\frac{k}{m}\neq 0$), le seul
point d'équilibre est $x=(0,0)$.

$x\mapsto Ax$ est continûment différentiable donc d'après le théorème de
Cauchy-Lipschitz, les solutions maximales sont uniques. De plus, la
dynamique est linéaire (donc a fortiori linéairement bornée) donc les
solutions maximales sont définies pour tout $t$. Elles sont données par
$x(t)=e^{At}x_0$.

Si $\lambda>0$, on a $\text{tr} A= -\frac{\lambda}{m}<0$ et
$\text{det} A=\frac{k}{m}>0$ donc d'après l'exercice [Critère de
stabilité en dimension 2 (p.
`\pageref*{answer-crit_stab_dim2}`{=tex})](#answer-crit_stab_dim2), $A$
est de Hurwitz et il s'ensuit que 0 est globalement asymptotiquement
stable. On peut aussi calculer explicitement les valeurs propres et
vérifier qu'elles sont à partie réelle strictement négative.

Lorsque $\lambda=0$, les frottements sont absents et les valeurs propres
sont $\pm i \sqrt{\frac{k}{m}}$. Comme le système est linéaire, on peut
dire que 0 n'est pas attratif donc pas asymptotiquement stable. Par
contre, il faut une étude plus approfondie pour étudier sa stabilité.
:::

::: {.section}
#### Stabilité asymptotique I {#answer-asymp_glob-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Stabilité asymptotique I}`{=latex}

La jacobienne de la dynamique est donnée par $$
J_f(x_1,x_2) = 
\left(
\begin{matrix}
0 & 1-3x_2^2 \\
-1+3x_1^2+2x_1x_2 & -(1-x_1^2)
\end{matrix}
\right)
$$ soit $$
J_f(0,0) = 
\left(
\begin{matrix}
0 & 1 \\
-1 & -1
\end{matrix}
\right)
$$ qui est de Hurwitz (valeurs propres $\frac{-1\pm i \sqrt{3}}{2}$)
Donc $(0,0)$ est bien localement asymptotiquement stable. Cependant, il
ne l'est pas globalement car $(1,1)$ est aussi un point d'équilibre : la
fonction constante égale à $(1,1)$ est solution (et ne tend pas vers 0).
:::

::: {.section}
#### Oscillateur II {#answer-ressort-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Oscillateur II}`{=latex}

Lorsque $\lambda=0$, les valeurs propres sont $\pm i \sqrt{\frac{k}{m}}$
et nous avons vu que 0 n'est pas asymptotiquement stable. Dans ce cas,
l'énergie du système $$
V(x)
= \frac{1}{2} k x_1^2 + \frac{1}{2} m x_2^2
$$ est conservée le long des trajectoires, c'est-à-dire, $$
\dot{\overline{V(x)}} = kx_1x_2 -kx_1x_2 = 0 \ .
$$ D'après le théorème de Lyapunov, puisque $V$ est à valeurs positives,
continûment différentiable et telle que $V(x)=0$ est équivalent à $x=0$,
la position d'équilibre 0 est donc stable. En fait, la masse oscille
autour de sa position d'équilibre à énergie constante et à la pulsation
$\sqrt{\frac{k}{m}}$.

Les portraits de phase de ces deux scénarios sont donnés sur la [Figure
(p. `\pageref*{fig_osci}`{=tex})](#fig_osci) ci-dessous.

![Plan de phase d'un oscillateur amorti à droite et non amorti à
gauche](images/oscillateur.py.pdf){#fig_osci}
:::

::: {.section}
#### Stabilité asymptotique II {#answer-asymp_glob-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Stabilité asymptotique II}`{=latex}

La jacobienne de la dynamique est donnée par $$
J_f(0,0) = 
\left(
\begin{matrix}
0 & 1 \\
0 & -1
\end{matrix}
\right)
$$ qui admet 0 et -1 comme valeurs propres. Nous ne pouvons donc rien
conclure sur la stabilité de 0 par le linéarisé.

Considérons plutôt la fonction $V:\mathbb{R}^2\to \mathbb{R}_{\geq 0}$
définie par $$
V(x_1,x_2)= x_1^4 + x_2^2 + (x_1+x_2)^2
$$ $V$ est continûment différentiable, positive et ne s'annule qu'en
$x=0$. De plus, elle vérifie `\begin{align*}
\langle \nabla V(x) , f(x) \rangle 
&= 4x_1^3x_2 - 2 x_1^3x_2 - 2x_2^2 + 2(x_1+x_2)(x_2-x_1^3-x_2)\\
&= -2x_2^2 -2 x_1^4 \qquad <0 \quad \forall x\neq 0
\end{align*}`{=tex} $V$ est donc une fonction de Lyapunov et on a bien
la stabilité asymptotique locale. De plus, $V$ est propre, i.e.,
$\lim_{\|x\|\to +\infty} V(x) = +\infty$, donc la stabilité asymptotique
est globale.
:::
:::

::: {.section}
Ecoulement dans un réservoir {#correc_Torricelli .correction}
----------------------------

::: {.section}
#### Question 1 {#answer-tor-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

$f:(t,x)\mapsto -k\sqrt{|x|}$ est continue sur
$\mathbb{R}\times \mathbb{R}$ donc le théorème de Peano nous garantie
l'existence de solutions au problème de Cauchy pour toute condition
initiale.

De plus, $\sqrt{|x|}\leq 1+|x|$ pour tout $x\in \mathbb{R}$ donc $f$ est
linéairement bornée et toute solution maximale est globale, donc ici
définie sur $\mathbb{R}$.

Enfin, $f$ est continûment différentiable sur
$\mathbb{R}\times (\mathbb{R}\setminus \{0\})$ donc lorsque $x_0\neq 0$,
il existe une unique solution maximale dans $\mathbb{R}\setminus \{0\}$
d'après le théorème de Cauchy-Lipschitz. Lorsque $x_0=0$ par contre, $f$
n'est pas différentiable en 0 (ni même lipschitzienne) donc le théorème
de Cauchy-Lipschitz ne s'applique pas.
:::

::: {.section}
#### Question 2 {#answer-tor-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Soit d'abord $x_0>0$. Tant que $x(t)>0$, on a $$
\dot{x}=-k\sqrt{|x|} \quad \Leftrightarrow \quad \frac{\dot{x}}{\sqrt{x}}=-k  \quad \Leftrightarrow \quad x(t) = \left(\sqrt{x_0}-\frac{k}{2}(t-t_0)\right)^2
$$ Donc tant que $x(t)>0$, la solution est unique (comme prévu dans la
question précédente) et par continuité, elle atteint 0 en
$t=t_0+2\sqrt{x_0}/k$. A partir de là, vu que $\dot{x}\leq 0$, la seule
solution possible qui reste positive est la solution constamment égale à
0 : le réservoir est vide et le reste. Donc pour $(t_0,x_0)$ avec
$x_0>0$, il existe une unique solution maximale positive au problème de
Cauchy définie par $$
x(t)= 
\left\{
\begin{array}{ll}
\left(\sqrt{x_0}-\frac{k}{2}(t-t_0)\right)^2 & \forall t\in ]-\infty,t_0+2\sqrt{x_0}/k] \\
0 & \forall t\in [t_0+2\sqrt{x_0}/k,+\infty[
\end{array}
\right.
$$

Maintenant si $x_0=0$. Pour $t\geq t_0$, la seule possibilité est de
rester à 0. En temps rétrograde, soit $x$ reste à 0 soit il existe
$t_1 < t_0$ tel que $x(t_1)>0$. Alors la solution correspondante est
unique et donnée par la formule ci-dessus en remplaçant $(t_0,x_0)$ par
$(t_1,x(t_1))$. Après réécriture, les solutions maximales s'écrivent en
fait $$
x(t)= 
\left\{
\begin{array}{ll}
\frac{k^2}{4}(t-t^-)^2 & \forall t\in ]-\infty,t^-] \\
0 & \forall t\in [t^-,+\infty[
\end{array}
\right.
$$ pour chaque $t^-\leq t_0$. Il y a donc une infinité de solutions.

*Remarque*: si l'on s'était intéressé aux solutions négatives, on aurait
trouvé une infinité de solutions au problème de Cauchy pour $x_0>0$. En
effet, à partir de $x_0=0$, on a aussi de manière symétrique, les
solutions $$
x(t)= 
\left\{
\begin{array}{ll}
0 & \forall t\in [t_0, t^+[\\
-\frac{k^2}{4}(t-t^+)^2 & \forall t\in [t^+,+\infty[
\end{array}
\right.
$$ pour tout $t^+\geq t_0$. Ceci ne contredit pas le théorème de Cauchy
Lispchitz. En effet, celui-ci ne garantie l'unicité de la solution
maximale que dans le domaine où $f$ est continûment différentiable par
rapport à $x$, c'est-à-dire ici tant qu'elle est non nulle, plus
précisément sur l'intervalle ouvert $]-\infty,t_0+2\sqrt{x_0}/k[$.
:::

::: {.section}
#### Question 3 {#answer-tor-3 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

La multiplicité des solutions peut être expliquée par le fait que
lorsqu'on voit le réservoir vide à $t_0$ on ne sait pas depuis quand il
est vide.
:::

::: {.section}
#### Question 4 {#answer-tor-4 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 4}`{=latex}

Lorsque $x_0>0$, les solutions sont continues par rapport à la condition
initiale tant qu'elles restent positives. Par contre, si $x_0=0$, une
solution possible est $x\equiv 0$ alors que pour tout $\delta>0$, la
solution partant de $x_0+\delta$ est donnée par
$x_\delta(t)=\left(\sqrt{x_0+\delta}-\frac{k}{2}(t-t_0)\right)^2$ pour
$t\leq t_0$. Donc sur un horizon de temps fixé (rétrograde)
$[\underline{t},t_0]$, la différence $\|x-x_\delta\|$ ne peut être
rendue arbitrairement petite en faisant tendre $\delta$ vers 0. Le même
phénomène apparaît en temps positif lorsque l'on considère les solutions
négatives (voir remarque plus haut). En ce sens, on n'a pas la
continuité des solutions par rapport à la condition initiale. Cela ne
contredit pas le théorème car $f(x)=-\sqrt{|x|}$ n'est pas $C^1$, ni
lipschitzienne en 0.
:::
:::

::: {.section}
Autour du Lemme de Grönwall {#correc_gronwall .correction}
---------------------------

::: {.section}
#### Question 1 (Lemme de Grönwall) {#answer-gro-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1 (Lemme de Grönwall)}`{=latex}

Soit $v$ l'application définie par $v(t)=\int_{t_0}^t\beta(s)u(s)ds$ sur
$[t^-,t^+]$. Elle vérifie $$
\dot{v}(t) = \beta(t)u(t) \quad , \quad u(t) \leq \alpha(t)+v(t) \ ,
$$ et donc puisque $\beta$ est à valeurs positives, $$
\dot{v}(t) \leq \alpha(t)\beta(t)+\beta(t)v(t) \ .
$$ Soit maintenant $w$ l'application définie par
$w(t)=v(t)\exp\left(-\int_{t_0}^t\beta(r)dr\right)$. $w$ est dérivable
sur $[t^-,t^+]$ et `\begin{align*}
\dot{w}(t) &= (\dot{v}(t)-\beta(t)v(t))\exp\left(-\int_{t_0}^t\beta(r)dr\right)\\
&\leq \alpha(t)\beta(t)\exp\left(-\int_{t_0}^t\beta(r)dr\right)
\end{align*}`{=tex} En intégrant des deux côté entre $t_0$ et $t$, on
obtient $$
w(t)-w(t_0)\leq \int_{t_0}^t \alpha(s)\beta(s)\exp\left(-\int_{t_0}^s\beta(r)dr\right)ds
$$ et en remplaçant $w$ par son expression, $$
v(t)\leq \int_{t_0}^t \alpha(s)\beta(s)\exp\left(\int_{t_0}^t\beta(r)dr\right)ds \ ,
$$ ce qui donne le résultat. Finalement, si $\alpha$ est constant alors
`\begin{align*}
u(t) &\leq \alpha +\alpha \left[-\exp\left(\int_s^t\beta(r)dr \right) \right]_{t_0}^t \\
& \leq \alpha -\alpha +\alpha \exp\left(\int_{t_0}^t\beta(r)dr \right)
\end{align*}`{=tex} ce qui donne le résultat.
:::

::: {.section}
#### Question 2 {#answer-gro-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Soit $x:I\subset J\to \mathbb{R}^n$ une solution maximale au problème de
Cauchy. Par le théorème de [représentation intégrale des solutions (p.
`\pageref*{theo_eq_integrale}`{=tex})](#theo_eq_integrale), $$
x(t)=x_0 + \int_{t_0}^t f(s,x(s))ds \ ,
$$ et donc, utilisant l'hypothèse de borne au plus affine de $f$, $$
\|x(t)\| \leq \|x_0\| + \int_{t_0}^t |b(s)| + |a(s)|\|x(s)\|ds \ .
$$ Sur tout segment $[t^-,t^+]\subset I$, on peut donc appliquer le
Lemme de Grönwall, ce qui donne $$
\|x(t)\| \leq \alpha(t) +  \int_{t_0}^{t} \alpha(s)\beta(s) \exp\left(\int_{s}^t\beta(r)dr \right)
$$ avec $\alpha(t)=\|x_0\| + \int_{t_0}^t |b(s)|$ et $\beta(t)= |a(t)|$
qui sont continues sur $J$. Donc $x$ ne peut pas exploser pour $t\in J$,
donc d'après le [théoreme du domaine maximal d'existence (p.
`\pageref*{theo_bouts}`{=tex})](#theo_bouts), vu que $f$ est définie sur
$J\times\mathbb{R}^n$, nécessairement $I=J$.
:::

::: {.section}
#### Question 3 {#answer-gro-3 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Soient $(t_0,x_0)\in J\times X$ et $\delta\in \mathbb{R}^n$ tel que
$(t_0,x_0+\delta)\in J\times X$. Soient $x:I\to \mathbb{R}^n$ et
$x_\delta : I'\to \mathbb{R}^n$ les solutions maximales aux problèmes de
Cauchy associés (uniques par le théorème de Cauchy Lipschitz), et
$\underline{t},\overline{t}>0$ tel que
$[ \underline{t},\overline{t}]\subset I$. On sait que `\begin{align*}
x(t)&=x_0  + \int_{t_0}^t f(s,x(s))ds & \forall t\in I\\
x_\delta(t)&=x_0 +\delta  + \int_{t_0}^t f(s,x_\delta(s))ds &\forall t\in I'
\end{align*}`{=tex} ce qui donne $$
|x(t)-x_\delta(t)|\leq |\delta| + \int_{t_0}^t |f(s,x(s))-f(s,x_\delta(s))|ds \qquad \forall t\in I\cap I' \ .
$$ Puisque $x$ est continue, l'ensemble
$x([ \underline{t},\overline{t}])$ est un sous-ensemble fermé et borné
de l'ouvert $X$. Donc il existe $\varepsilon>0$ tel que le "tube" $$
\mathcal{C}= \{ (t,x_\delta) \in [ \underline{t},\overline{t}]\times \mathbb{R}^n \: | \: \|x_\delta-x(t) \| \leq \varepsilon \} 
$$ est inclus dans $J\times X$. On va montrer que $(t,x_\delta(t))$ est
définie et reste dans ce tube sur $[ \underline{t},\overline{t}]$ si
$\delta$ est suffisamment petit. Soit $\underline{t}'$ et
$\overline{t}'$ les temps minimaux et maximaux sur
$[ \underline{t},\overline{t}]$ tel que $$
(t,x_\delta(t)) \in \mathcal{C}\qquad \forall t\in [ \underline{t}',\overline{t}']
$$ Puisque $\mathcal{C}$ est fermé et borné, et $\partial_x f$ est
continue sur $\mathcal{C}$, $M= \max_\mathcal{C}\|\partial_x f\|$ est
bien défini. Donc d'après le théorème des accroissements finis appliqué
sur le segment $[ (s,x(s)),(s,x_\delta(s))]$ inclus dans $\mathcal{C}$,
$$
|x(t)-x_\delta(t)|\leq |\delta| + \int_{t_0}^t M |x(s)-x_\delta(s)|ds \qquad \forall t\in [ \underline{t}',\overline{t}'] \ .
$$ Donc par le Lemme de Grönwall, $$
|x(t)-x_\delta(t)|\leq |\delta|e^{M(t-t_0)} \qquad \forall t\in [ \underline{t}',\overline{t}'] \ .
$$ Pour $\delta$ suffisamment petit,
$|\delta|e^{M(t-t_0)}\leq \varepsilon$ sur $[ t_0,\overline{t}]$. On a
alors nécessairement $\underline{t}'=\underline{t}$ et
$\overline{t}'=\overline{t}$ et le résultat est montré. Notons que la
preuve est bien toujours valable pour $f$ localement Lipschitzienne par
rapport à $x$ sur $J\times X$, puisqu'il suffit alors de prendre pour
$M$ la constante de Lipschitz de $f$ par rapport à $x$ sur $\mathcal{C}$
qui est fermé et borné (compact).
:::
:::

::: {.section}
Cycle limite {#correc_cycle_lim .correction}
------------

On étudie le comportement des solutions de $\dot{x}=f(x)$ pour $$
f(x) = 
\left(
\begin{array}{c}
x_1+x_2-x_1(x_1^2+x_2^2) \\
-x_1+x_2-x_2(x_1^2+x_2^2) 
\end{array}
\right)
$$

::: {.section}
#### Question 1 {#answer-cycle-lim-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Chercher les points d'équilibre du système revient à résoudre $$
\begin{array}{rcl}
0&=& x_1+x_2-x_1(x_1^2+x_2^2) \\
0&=& -x_1+x_2-x_2(x_1^2+x_2^2) 
\end{array}
$$ Multiplier la première ligne par $x_2$, la deuxième par $x_1$ et
soustraire, donne $x_1^2+x_2^2=0$, soit $x_1=x_2=0$. Il n'y a donc qu'un
point d'équilibre $(0,0)$. La jacobienne de la dynamique est donnée par
$$
J_f(x_1,x_2) = 
\left(
\begin{matrix}
1-(x_1^2+x_2^2) -2 x_1^2 & 1-2 x_1x_2 \\
-1-2 x_1x_2 & 1-(x_1^2+x_2^2)-2 x_2^2
\end{matrix}
\right)
$$ soit $$
J_f(0,0) = 
\left(
\begin{matrix}
1  & 1 \\
-1 & 1
\end{matrix}
\right)
$$ qui a pour valeurs propres $1\pm i$. La partie réelle étant positive,
le point d'équilibre est instable.
:::

::: {.section}
#### Question 2 {#answer-cycle-lim-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

$f:\mathbb{R}^2 \to \mathbb{R}^2$ définie par
$f(x) =(x_1+x_2-x_1(x_1^2+x_2^2) ,-x_1+x_2-x_2(x_1^2+x_2^2))$ est
continûment différentiable sur $\mathbb{R}^2$. Donc d'après le théorème
de Cauchy-Lipschitz, le système admet une unique solution maximale pour
toute condition initiale. De plus, `\begin{align*}
\frac{d}{dt}V(x(t)) &= \langle \nabla V(x) , f(x) \rangle \\
&= x_1^2+x_1x_2-x_1^2(x_1^2+x_2^2) -x_1x_2 +x_2^2 - x_2^2(x_1^2+x_2^2)\\
&= -(x_1^2+x_2^2-1)(x_1^2+x_2^2)
\end{align*}`{=tex} Donc $\frac{d}{dt}V(x(t))$ est négatif à l'extérieur
du disque de centre 0 et de rayon 1, zéro sur la frontière, et positif à
l'intérieur si $x\neq 0$ et zéro sinon. Il s'ensuit en particulier que
$\|x\|$ décroit lorsque $\|x\|>1$, donc les solutions restent bornées en
temps positif. Or, vu que $f$ est continue sur $\mathbb{R}^2$, on sait
du [Théorème du domaine maximal d'existence (p.
`\pageref*{theo_bouts}`{=tex})](#theo_bouts) que la seule raison pour
laquelle une solution maximale ne serait pas définie pour tout
$t\geq t_0$ serait qu'elle explose en temps fini. C'est impossible ici.
:::

::: {.section}
#### Question 3 {#answer-cycle-lim-3 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Supposons que $x_0:=x(t_0)$ vérifie $\|x_0\|\neq 1$ et qu'il existe
$t_1$ tel que $\|x(t_1)\|= 1$. Considérons le problème de Cauchy de
condition initiale $x^*:=x(t_1)$ à $t=t_1$. Il admet donc une solution
qui au temps $t_0$ vaut $x_0$. Mais il existe une autre solution $$
\left(
\begin{matrix}
\cos(t-t_1) & \sin(t-t_1) \\
-\sin(t-t_1) & \cos(t-t_1)
\end{matrix}
\right) x^*
$$ qui reste sur le cercle en tout temps et qui vaut aussi $x^*$ à
$t=t_1$, ce qui est impossible par le théorème de Cauchy Lipschitz (car
$f$ est continûment différentiable)
:::

::: {.section}
#### Question 4 {#answer-cycle-lim-4 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 4}`{=latex}

Si $V(x(t_0))=\|x(t_0)\|^2=1$, alors $V$ est constant donc les
trajectoires initialisées sur le cercle de rayon 1 y restent. Sur le
cercle, la dynamique suit celle d'un oscillateur $$
\begin{array}{rcl}
\dot{x}_1 &=& x_2\\
\dot{x}_2 &=& -x_1\\
\end{array}
$$ donc les trajectoires "tournent" sur le cercle.

Si $V(x(t_0))=x_1(t_0)^2+x_2(t_0)^2>1$ alors $V$ décroit strictement
tant qu'il reste plus grand que 1. Donc les trajectoires initialisées à
l'extérieur du cercle s'en approchent mais ne le rencontrent jamais
d'après la question précédente.

Si $0< V(x(t_0))=x_1(t_0)^2+x_2(t_0)^2<1$ alors $V$ croit strictement
tant qu'il reste plus petit que 1.

Enfin, la trajectoire initialisée à zéro reste à zéro.

Le portrait de phase est donné [ci-dessous (p.
`\pageref*{fig_cycle_limite}`{=tex})](#fig_cycle_limite).

![Portrait de phase de l'exercice Cycle
Limite](images/cycle_limite.py.pdf){#fig_cycle_limite}
:::
:::

::: {.section}
Attractivité locale implique stabilité asymptotique globale pour un système linéaire {#answer-attrac_stab .answer .unnumbered .unlisted}
------------------------------------------------------------------------------------

`\addcontentsline{toc}{subsection}{Attractivité locale implique stabilité asymptotique globale pour un
système linéaire}`{=latex}

Tout d'abord, montrons que l'attractivité locale de 0 implique
l'attractivité globale. Ceci est dû à la propriété d'*homogénéité* des
systèmes linéaires: si $x$ une solution initialisée à
$x_0\in\mathbb{R}$, alors $\lambda x$ est solution initialisée à
$\lambda x_0$ puisque $$
\lambda x(t) = \lambda e^{At} x_0 = e^{At} (\lambda x_0) \ .
$$ Donc soit $\eta>0$ tel que toute solution initialisée dans
$B(0,\eta)$ converge vers 0. Soit $x$ une solution initialisée à
$x_0\in\mathbb{R}$. Alors $\lambda x$ avec $\lambda < \eta / |x_0|$ est
solution initialisée dans $B(0,\eta)$ et converge vers 0. Donc $x$
converge vers 0.

Maintenant, montrons la stabilité. Soit $\varepsilon >0$. Notons
$(x_i)_{i=1...n}$ une base orthonormale de $\mathbb{R}^n$. Soit alors
$M>0$ tel que $$
|e^{At} x_i | \leq M \quad \forall t \in \mathbb{R}_{\geq 0}\quad \forall i\in \{1,...,n\}
$$ qui existe bien puisque toutes les solutions convergent vers 0 et $n$
est fini. Soit maintenant $\eta >0$. Pour tout $x_0 \in B(0,\eta)$ dont
la décomposition dans la base s'écrit $$
x_0 = \sum_{i=1}^n \alpha_i x_i
$$ on a $|\alpha_i|\leq \eta$ et donc pour tout
$t \in \mathbb{R}_{\geq 0}$, $$
\left| e^{At} x_0 \right| \leq \left| \sum_{i=1}^n  e^{At} \alpha_i x_i\right|  \leq  n \eta M 
$$ On conclut que pour des conditions initiales suffisamment petites
($\eta <\frac{\varepsilon}{nM}$), les solutions restent inférieures à
$\varepsilon$ en norme. Donc le système est stable.
:::

::: {.section}
Contrôle d'un système {#correc_cont_lin .correction}
---------------------

::: {.section}
#### Question 1 {#answer-cont-lin-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Si $u\equiv 0$, les solutions sont $x(t) = e^t x_0$ donc le point
d'équilibre 0 est instable et les solutions divergent.
:::

::: {.section}
#### Question 2 {#answer-cont-lin-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Si l'on mesure $x(t)$, on peut prendre $u(t) = - kx(t)$, ce qui donne $$
\dot{x} = -(k-1) x
$$ pour lequel 0 est globalement asymptotiquement stable si $k>1$.
:::

::: {.section}
#### Question 3 {#answer-cont-lin-3 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Prenons $u(t) = -k_1 x_1(t) - k_2 x_2(t) - \ldots - k_n x_n(t)$. Alors
le système devient $$
\dot{x} = A x
$$ avec $A$ de la forme $$
A = \left(
\begin{array}{ccccc}
0&1&0 & \ldots & 0 \\
\vdots &\ddots & \ddots & & \vdots\\
\vdots&&\ddots & 1  &0\\
0&&&0&1 \\
-k_1 &-k_2&\ldots& \ldots& -k_n
\end{array}
\right)
$$ qui admet pour polynôme caractéristique $$
s^n + k_1 s^{n-1} + \ldots + k_2 s + k_1\ .
$$ Il suffit donc de choisir les coefficients $k_i$ tels que ce polynôme
ait ses racines à partie réelle strictement négative. Ces dernières
peuvent d'ailleurs être choisies à souhait.
:::
:::
:::

::: {.section}
Annexes
=======

::: {.section}
Preuve du théorème de Peano-Arzelà (Hors-programme) {#app_peano .app}
---------------------------------------------------

Cette preuve repose sur le théorème d'Ascoli :

> Soient $X$ un espace métrique compact, $Y$ un espace métrique complet,
> et $S\subset C(X,Y)$, où $C(X,Y)$ est l'ensemble des fonctions
> continues de $X$ dans $Y$. Les deux propriétés suivantes sont
> équivalentes :
>
> 1.  $S$ est *relativement compact* dans $C(X,Y)$
>
> 2.  $S$ est *équicontinu* et pour tout $x\in X$,
>     $\{f(x) \ , \ f\in S \}$ est *relativement compacte* dans $Y$.

On dit qu'un ensemble est *relativement compact* si son adhérence est
compacte. En dimension finie, vue que "compact" est équivalent à
"fermé-borné" et que l'adhérence est fermée par définition,
"relativement compact" est équivalent à "borné". Mais ce n'est pas le
cas en dimension infinie (en particulier $C(X,Y)$) où "relativement
compact" est alors équivalent au fait de pouvoir extraire des suites
convergentes dans l'adhérence de l'ensemble.

Ici, puisque $X$ est compact et $Y$ complet, on peut montrer que
$C(X,Y)$ muni de la norme uniforme $\|\cdot\|_\infty$ est complet, donc
fermé. Il s'ensuit que "$S$ est relativement compact dans $C(X,Y)$"
implique pouvoir extraire de toute suite de $S$ une sous-suite
convergente dans $C(X,Y)$ (au sens de $\|\cdot\|_\infty$). C'est ce que
nous allons utiliser pour prouver l'existence d'une solution au problème
de Cauchy.

Maintenant, le deuxième terme nécessitant des explications est
l'*équicontinuité* de $S$. Cette notion veut simplement dire que les
fonctions dans $S$ sont toutes continues *au même rythme*, i.e., plus
précisément, $$
\forall \varepsilon >0 \ \exists \delta \ , \quad \ d_X(x_a,x_b)\leq \delta \; \Longrightarrow \;\forall f\in S \ , \  d_Y(f(x_a),f(x_b)) \leq \varepsilon \ ,
$$ où $d_X$ et $d_Y$ sont les distances sur $X$ et $Y$ respectivement.

Revenons maintenant à nos moutons. On suppose donc $f$ continue sur
$J\times X$ et on veut montrer que $S_f(t_0,x_0)\neq \emptyset$. Soient
d'abord $\tau >0$ et $r>0$, tels que
$\mathcal{C}:= [t_0-\tau,t_0+\tau]\times \overline{B}(x_0,r) \subset J\times X$.
Soit $\tau_m\in]0, \tau]$ tel que $\tau_m\max_\mathcal{C}\|f\|\leq r$.
On va montrer l'existence d'une solution définie par sa forme intégrale
$$
x(t) = x_0 + \int_{t_0}^t f(s,x(s)) ds
$$ sur $[t_0,t_0+\tau_m]$ et la preuve sur $[t_0-\tau_m,t_0]$ se fait de
la même façon.

L'idée est d'approximer de plus en plus finement la forme intégrale et
montrer que ce procédé converge. On définit donc pour
$\epsilon \in ]0,1[$ la fonction `\begin{align*}
x_\epsilon(t) &= x_0 & \forall t\in [t_0-1,t_0] \\
&= x_0 + \int_{t_0}^t f(s,x_\epsilon(s-\epsilon)) ds & \forall t\in [t_0,t_0+\tau_m]
\end{align*}`{=tex} Ces fonctions sont définies et continues sur
$[t_0-1,t_0]$. Puis sur $[t_0,t_0+\epsilon]\cap[t_0,t_0+\tau_m]$, on
voit que l'intégrale ne dépend que de $x_\epsilon$ sur $[t_0-1,t_0]$,
donc elle est toujours bien définie et continue. De proche en proche,
$x_\epsilon$ est donc bien définie et continue sur $[t_0-1,t_0+\tau_m]$.
En fait, $\epsilon$ représente un petit retard introduit dans
l'intégrale pour la rendre explicite. Si l'on arrive à montrer que ces
fonctions converge vers une fonction continues lorsque $\epsilon$ tend
vers 0, cette limite sera solution de l'équation intégrale sur
$[t_0,t_0+\tau_m]$ et sera donc solution.

La première étape est de montrer de proche en proche, grâce au retard,
que $x_\epsilon(t)\in \overline{B}(x_0,r)$ pour tout
$t\in [t_0-1,t_0+\tau_m]$ puisque $\tau_m\max_\mathcal{C}\|f\|\leq r$.
Donc $$
\forall \epsilon \in ]0,1[ \ , \ x_\epsilon \in E:=C([t_0-1,t_0+\tau_m],\overline{B}(x_0,r)) \ .
$$ De plus, pour tout $\epsilon \in ]0,1[$ et pour tout
$(t,t')\in [t_0-1,t_0+\tau_m]^2$, $$
\|x_\epsilon(t) - x_\epsilon(t') \| \leq \max_\mathcal{C}\|f\| \, |t-t'|
$$ donc la famille $S:=\{x_\epsilon , \ \epsilon \in ]0,1[ \}$ est
équicontinue. De plus, vu que leur image est bornée dans
$\overline{B}(x_0,r)$ de dimension finie, elle est bien bien
relativement compacte. Le théorème d'Ascoli nous dit alors que $S$ est
relativement compacte dans $E$. Il existe donc une sous suite
$x_{\epsilon_k}$ telle que $\lim_{k\to +\infty} \epsilon_k =0$ et
$\lim_{k\to +\infty} x_{\epsilon_k} = x^\star \in E$ au sense de la
norme uniforme $\|\cdot \|$. Par uniforme continuité de $f$ sur le
compact $\mathcal{C}$, on en déduit alors que pour tout
$s\in [t_0,t_0+\tau_m]$,
$\lim_{k\to +\infty} f(s,x_{\epsilon_k}(s-\epsilon_k))= f(s,x^\star(s))$
et donc que $x^\star$ est bien solution de l'équation intégrale, ce qui
donne le résultat.
:::

::: {.section}
Preuve du théorème du domaine maximal d'existence {#pr_theo_bouts .app}
-------------------------------------------------

Soit $x: I \to \mathbb{R}^n$ une solution maximale dans $S_f(t_0,x_0)$.
Par définition, $I$ est un intervalle contenant $t_0$. Soient
$t_m^+= \sup I$ et $t_m^-= \inf I$. Supposons $t_m^+\in I$ et dénotons
$(t_1,x_1) = (t_m^+,x(t_m^+))$. Toujours par définition,
$(t_1,x_1)\in J\times X$, donc par le [théorème de Peano (p.
`\pageref*{theo_peano}`{=tex})](#theo_peano) il existe $\tau>0$ et
$x' : [t_m^+-\tau,t_m^++\tau] \to \mathbb{R}^n$ dans $S_f(t_1,x_1)$.
Considérons $\tilde{I} = I\cup [t_m^+,t_m^++\tau]$, et
$\tilde{x}: \tilde{I} \to \mathbb{R}^n$ définie par $$
\tilde{x}(t) = 
\left\{
\begin{array}{ll}
x(t) & \text{si } t\in I \\
x'(t) & \text{si } t>t_m^+
\end{array}
\right.
$$ $\tilde{x}$ est bien continue et à valeurs dans $J\times X$ sur
$\tilde{I}$. De plus, elle est de classe $C^1$ sur
$\mathring{\tilde{I}}\setminus \{ t_m^+\}$ telle que
$\dot{\tilde{x}}(t) = f(t,\tilde{x}(t))$ pour tout
$t\in \mathring{\tilde{I}}\setminus \{ t_m^+\}$. Par continuité de
$\tilde{x}$ en $t_m^+$ et de $f$ en $(t_1,x_1)$, on en déduit que
$\tilde{x}$ est bien $C^1$ sur $\mathring{\tilde{I}}$. Donc
$\tilde{x}\in S_f(t_0,x_0)$, ce qui contredit la maximalité de $x$ car
$I \subsetneq \tilde{I}$. On conclut donc que $t_m^+\notin I$ et de même
$t_m^-\notin I$. Donc $I$ est ouvert.

Supposons $t_m^+$ fini. Montrons qu'alors lorsque $t$ tend vers $t_m^+$,
soit $x(t)$ diverge, soit $(t,x(t))$ tend vers la frontière de
$J\times X$. La propriété se montre de manière similaire en $t_m^-$.
Pour cela, nous allons montrer que lorsque $t$ se rapproche de $t_m^+$,
$(t,x(t))$ finit par sortir définitivement de tout sous-ensemble $K$
fermé et borné de $J\times X$. Soit donc $K$ fermé et borné de
$J\times X$.

Supposons d'abord qu'il existe $\tau$ tel que $(t,x(t))\in K$ pour tout
$t\in [\tau,t_m^+[$. Puisque $f$ est continue, $\|f(t,x)\|$ est borné
disons par $M$ sur $K$. Donc pour toute suite $(t_k)$ d'éléments de
$[\tau,t_m^+[$ tendant vers $t_m^+$, par la représentation intégrale des
solutions, $$
\|x(t_{k+p}) - x(t_{k}) \| \leq \int_{t_k}^{t_{k+p}} \|f(s,x(s))\| ds \leq M (t_{k+p}-t_k) \ .
$$ Donc la suite $(x(t_k))$ est de Cauchy et donc aussi la suite
$(t_k,x(t_k))$ dans $K$. Puisque $K$ est un sous-ensemble fermé de
$\mathbb{R}\times \mathbb{R}^n$ complet, il est complet. Donc
$(t_k,x(t_k))$ converge vers $(t_m^+,\bar{x})\in K \subset J\times X$.
Donc $x$ peut-être prolongée par continuité en une solution sur
$]t_m^-,t_m^+]$, ce qui est impossible par maximalité. Donc $(t,x(t))$
sort de manière persistente de $K$.

Supposons maintenant que $(t,x(t))$ entre aussi de manière persistente
dans $K$, i.e., $$
 \forall t_K \in \left[t_0,t_m^+\right[ \, , \, \exists t\in \left[t_K,t_m^+\right[ \: : \: (t,x(t))\in K
$$ Alors il existe une suite $(t_p)_{p\in \mathbb{N}}$ telle que $$
t_m^+-\frac{1}{p}\leq  t_p < t_m^+\quad \text{et} \quad (t_p,x(t_p))\in K \quad \forall p\in \mathbb{N}
$$ On a donc $\lim_{p\to+\infty} t_p = t_m^+$, et par compacité de $K$,
on peut extraire de $(t_p,x(t_p))_{p\in \mathbb{N}}$ une sous-suite qui
converge vers $(t_m^+,\overline{x})\in K$. Pour simplifier les
notations, on suppose donc directement
$\lim_{p\to+\infty} x(t_p) =\overline{x}$.

Notons $\xi =(t_m^+,\overline{x})$. Soit $\varepsilon >0$ tel que
$\overline{B}(\xi,2\varepsilon)\subset J\times X$. Il existe $p^*$ tel
que pour tout $p\geq p^*$,
$(t_{p},x(t_{p}))\in \overline{B}(\xi,\varepsilon)$. Mais puisque
$\overline{B}(\xi,2\varepsilon)$ est un sous-ensemble fermé et borné de
$J\times X$, on sait que $(t,x(t))$ en sort de manière persistente. Donc
sans perte de généralité, on peut supposer que pour tout $p$, il existe
$t_p < t_p' < t_{p+1}$ tel que $$
\| (t_p',x(t_p')) - \xi \| = 2\varepsilon  \qquad , \qquad (t,x(t))\in \overline{B}(\xi,2\varepsilon) \quad \forall t\in [ t_p,t_p' ] \ .
$$ Soit alors $M$ le maximum de $\| f\|$ sur le fermé borné
$\overline{B}(\xi,2\varepsilon)$. Par la représentation intégrale, et
pour $p$ suffisamment grand, on a donc $$
\frac{\varepsilon}{2} \leq \|x(t_p')-x(t_p) \| \leq \int_{t_p}^{t_p'} \|f(s,x(s))\| ds \leq M (t_p'-t_p) \leq M (t_{p+1}-t_p)  \ .
$$ Il s'ensuit que pour $p$ suffisamment grand,
$t_{p+1}-t_p \geq \frac{\varepsilon}{2M}$, ce qui est impossible puisque
$(t_p)$ tend vers $t_m^+$. On peut donc conclure que $(t,x(t))$ sort de
manière définitive de tout fermé borné $K$ lorsque $t$ s'approche de
$t_m^+$.
:::

::: {.section}
Stabilité et linéarisé tangent {#app_stab_lin .app}
------------------------------

Soit $a$ un point d'équilibre de $f$. Définissons $$
\Delta(x) = f(x)-f(a) - J_f(a)(x-a) = f(x)- J_f(a)(x-a)\ ,
$$ puisque $f(a)=0$. Par la définition de la différentiabilité de $f$,
il existe $\varepsilon>0$ et une fonction
$\delta:\mathbb{R}^n\to \mathbb{R}^n$ tels que
$\lim_{x\to a} \delta(x)=0$ et\
$$
\Delta(x) = \delta(x) \|x-a\| \qquad \forall x\in B(a,\varepsilon) \ .
$$

La preuve repose ensuite sur le lemme suivant dû à Lyapunov :

> Pour toute matrice $A\in \mathbb{R}^{n\times n}$ à valeurs propres à
> parties réelles strictement négatives, et pour toute matrice
> symmétrique définie positive $Q\in \mathbb{R}^{n\times n}$, il existe
> une (unique) matrice symmétrique définie positive
> $P\in \mathbb{R}^{n\times n}$ telle que $$
> A^\top P +P A = - Q \ .
> $$

En effet, la solution est alors donnée par
$P=\int_0^{+\infty}\left(e^{As}\right)^\top Q e^{As}ds$.

Supposons donc que $J_f(a)$ ait ses valeurs propres à partie réelle
strictement négative. Il existe alors $P=P^\top>0$ telle que $$
J_f(a)^\top P +P J_f(a) = -I \ .
$$ Considérons alors $V(x) = (x-a)^\top P (x-a)$ qui est bien positive,
et nulle seulement pour $x=a$. Pour tout $x\in B(a,\varepsilon)$,
`\begin{align*}
\left< \nabla V(x), f(x) \right> & = (x-a)^\top P f(x) + f(x)^\top P(x-a) \\
&= (x-a)^\top\left( J_f(a)^\top P +P J_f(a)\right) (x-a) + 2 (x-a)^\top P\Delta(x) \\
&\leq - \|x-a\|^2 + 2 \|x-a\| \|P\| \|\Delta(x)\| \\
&\leq - \|x-a\|^2\left(1- 2\|P\|  \|\delta(x) \| \right)
\end{align*}`{=tex} Donc $\left< \nabla V(x), f(x) \right><0$ pour tout
$x\in B(a,\epsilon')$ avec $\epsilon'<\epsilon$ suffisamment petit tel
que $$
\|\delta(x) \| \leq  \frac{1}{2\|P\|}  \qquad \forall x\in B(a,\epsilon') \ .
$$ D'après le théorème de Lyapunov, $a$ est donc localement
asymptotiquement stable.
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

[^2]: Certaines références autorisent les solutions définies sur un
    intervalle d'intérieur vide, c'est-à-dire réduit à un point, qui
    sont dites "triviales". Mais cela n'a pas grand intérêt ici et nous
    supposons donc que les solutions sont définies au moins "pendant un
    certain temps".

[^3]: On omet de préciser l'intervalle $I$ sur lequel $x$ est solution
    lorsque $I$ est l'ensemble de définition naturel (ou clairement
    défini) de $x$. Lorsque celui-ci est ambigu ou bien lorsque l'on
    veut insister sur l'intervalle de définition, on dira *solution sur
    $I$*.

[^4]: Pour toute suite $(x_n)$ d'éléments de $F$ convergeant vers $x^*$,
    pour tout $t\in [t_0-\tau_m,t_0+\tau_m]$, $$
    \|x_n(t)-x^*(t)\|\leq \|x_n-x^*\|_{\infty} \quad \underset{n\to \infty}{\longrightarrow} 0
    $$ donc la suite $(x_n(t))$ d'éléments du fermé
    $\overline{B}(x_0,r)$ converge dans $\mathbb{R}^n$ vers $x^*(t)$ qui
    est donc dans $\overline{B}(x_0,r)$. Ceci implique $x^*\in F$.

[^5]: Il suffit de montrer que
    $x([t_0-\tau_m,t_0+\tau_m])\subset \overline{B}(x_0,r)$. Supposons
    le contraire et sans perdre en généralité supposons que
    $S := \{ t\in [t_0,t_0+\tau_m] \: : \: \|x(t)-x_0\|>r \}$ est non
    vide. Soit $t^*=\inf S$. Nécessairement $t_0 < t^* < t_0+\tau_m$.
    Donc par la [représentation intégrale (p.
    `\pageref*{theo_eq_integrale}`{=tex})](#theo_eq_integrale), $$
    \|x(t^*)-x_0\|\leq (t^*-t_0) \max_{s\in [t_0,t^*]} \|f(s,x(s)) \| < \tau_m \max_\mathcal{C}\|f\|< r \ .
    $$ Par continuité de $x$, $\|x(t)-x_0\|\leq r$ pour un temps après
    $t^*$, ce qui contredit sa définition.

[^6]: En l'absence d'outils d'analyse fonctionnelle à cette époque, la
    preuve de Cauchy consistait plutôt à discrétiser en temps
    l'intégrale de plus en plus finement et montrer la convergence vers
    une solution.

[^7]: https://portsmouth.github.io/fibre/

[^8]: Sous l'hypothèse d'incompressibilité du fluide, la loi de
    Bernoulli dit que $$
    p_s + \rho g h_s + \rho \frac{v_s^2}{2}=p_o + \rho g h_o + \rho \frac{v_o^2}{2}
    $$ où $s$ fait référence aux quantités à la surface et $o$ à
    l'ouverture. On a $p_s=p_o$ égales à la pression atmosphérique,
    $h_s-h_o=x$, $v_s=\frac{s}{S}v_o$ par conservation du débit, et
    $\dot{x} = - v_s$. On obtient donc $$
    \dot{x} = - \frac{1}{\sqrt{\left(\frac{S}{s}\right)^2-1}} \sqrt{2gx} \approx -\frac{s}{S} \sqrt{2gx}
    $$ en supposant que $s\ll S$.
