---
author:
- 'STEP, MINES ParisTech[^1]'
bibliography: bibliography.json
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
link-citations: true
title: Equations Différentielles II
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

-   [Introduction](#introduction)
-   [Objectifs du cours](#objectifs-du-cours)
-   [Limites du schéma d'Euler](#limites-du-schéma-deuler)
    -   [Systèmes raides](#sec_systRaides)
    -   [Systèmes hamiltoniens](#sec_systHamiltoniens)
-   [Méthodes à un pas](#méthodes-à-un-pas)
    -   [Principe](#principe)
    -   [Exemples](#exemples)
    -   [Définition implicite de $\Phi$](#sec_def_impl)
-   [Analyse d'erreur](#analyse-derreur)
    -   [Erreur de troncature locale](#erreur-de-troncature-locale)
    -   [Stabilité](#stabilité)
    -   [Convergence](#convergence)
    -   [Erreurs d'arrondi et pas
        optimal](#erreurs-darrondi-et-pas-optimal)
-   [Annexe -- Choix du pas de temps](#annexe-choix-du-pas-de-temps)
    -   [Pas fixe](#pas-fixe)
    -   [Adaptation du pas de temps](#adaptation-du-pas-de-temps)
-   [Projet numérique](#projet-numérique)
-   [Exercices](#exercices)
    -   [Consistance et ordre de schémas](#exo_consist)
    -   [Explicite ou implicite ?](#exo_exp_impl)
    -   [Euler symplectique](#exo_symplectique)
-   [Corrections](#corrections)
    -   [Consistance et ordre de schémas](#correc_consist)
    -   [Explicite ou implicite ?](#explicite-ou-implicite)
    -   [Euler symplectique](#euler-symplectique)
-   [Références](#références)

```{=tex}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\Rgeq}{\R_{\geq 0}}
\newcommand{\Rg}{\R_{> 0}}
\renewcommand{\C}{\mathbb{C}}
```
```{=tex}
\newcommand{\dt}{{\Delta t}}
```
::: {.section}
Introduction
============

Ce chapitre est consacré à la résolution numérique d'équations
différentielles $$
\dot{x} = f(t,x) \qquad , \qquad x(t_0)=x_0 \ .
$$ La nécessité de développer des méthodes d'intégration numériques
vient du constat que seule une infime partie des équations
différentielles sont résolubles exactement. Or, on a parfois besoin de
connaître le plus précisément possible le comportement futur d'un
système dynamique :

-   soit en temps fini, par exemple pour déterminer la trajectoire d'une
    fusée pour la mise en orbite d'un satellite;

-   soit en temps *long*, par exemple pour déterminer un cycle limite
    asymptotique (dynamique de population) ou bien se prononcer sur la
    stabilité de notre système solaire.

La méthode la plus connue est la *méthode d'Euler* datant de 1768, qui
consiste à implémenter $$
x^{j+1} = x^j + {\Delta t}\, f(t_j,x^j) \qquad x^0 = x_0 
$$ pour un pas de temps ${\Delta t}$ suffisamment petit. Cette méthode
appartient à la famille des méthodes *explicites*, c'est-à-dire que
$x^{j+1}$ est directement et explicitement défini en fonction de
$x^{j}$. En 1824, Cauchy montre la convergence de cette méthode lorsque
le pas de temps ${\Delta t}$ tend vers 0, et prouve ainsi l'existence et
l'unicité des solutions (en fait, il utilise plutôt la version
*implicite* de la méthode d'Euler).

Même si la méthode d'Euler suffit dans les cas simples, elle exige
parfois de recourir à des pas très faibles pour obtenir une précision
acceptable sur des temps longs (voir [Systèmes raides (p.
`\pageref*{sec_systRaides}`{=tex})](#sec_systRaides)). Parfois, le
compromis entre précision à chaque itération et accumulation des erreurs
d'arrondis devient même impossible. De plus, cette méthode n'est pas
adaptée à la simulation de certains systèmes dont certaines propriétés
cruciales (comme la conservation de l'énergie) ne sont pas préservées
(voir [Systèmes Hamiltoniens (p.
`\pageref*{sec_systHamiltoniens}`{=tex})](#sec_systHamiltoniens)). Au
cours des derniers siècles, les scientifiques ont donc progressivement
développé des méthodes de plus en plus complexes et performantes :
schémas multi-pas d'ordre supérieur, méthodes implicites, variation du
pas, schémas symplectiques etc.

En fait, dans l'histoire des équations différentielles, c'est souvent la
mécanique céleste qui a été motrice des plus grandes avancées. Au milieu
du XIX$^e$ siècle, les astronomes Adams et Le Verrier prédisent
mathématiquement l'existence et la position de la planète Neptune et
l'on entend parler pour la première fois de méthodes multi-pas. Ensuite,
les progrès se sont enchaînés au rythme des modèles physiques. La
première tendance a été de rechercher des schémas permettant toujours
plus de précision à pas plus grand. Parmi les dates clés, on peut citer
la publication en 1895 de la première méthode de Runge-Kutta par Runge,
puis en 1901, de la populaire méthode de Runge-Kutta d'ordre 4 par
Kutta, et ensuite en 1910, de l'*extrapolation de Richardson* permettant
la montée en ordre et donc le recours à des pas plus grand pour une même
précision. Mais au milieu du XX$^e$ siècle, on découvre des systèmes,
dits *raides* (Hirschfelder, 1952), pour lesquels cette montée en ordre
ne suffit pas et pour lesquels il faut repenser de nouveaux schémas
(Dalquist, 1968). Enfin, à partir des années 80, les scientifiques
développent l'intégration numérique *géométrique*, c'est-à-dire qui
préservent les propriétés structurelles du système (symétrie,
conservation d'énergie etc.), utile en particulier pour la simulation
des systèmes hamiltoniens.
:::

::: {.section}
Objectifs du cours
==================

Ce cours a pour but de sensibiliser aux problèmes apparaissant lors de
la simulation numérique des solutions d'équations différentielles, et de
donner les bases d'analyse d'erreur numérique. Pour un exposé plus
approfondi, on pourra par exemple se référer à [@Dem06].

En première lecture :

-   comprendre les limites d'un schéma d'Euler.

-   comprendre qu'un schéma numérique à un pas consiste à discrétiser
    une intégrale, en connaître quelques-uns autres que le schéma
    d'Euler.

-   comprendre les notions de consistance/convergence d'un schéma et
    leur ordre. Savoir montrer que le schéma d'Euler explicite est
    convergent d'ordre 1.

En deuxième lecture :

-   comprendre comment fonctionne un schéma implicite et comment
    l'implémenter.

-   comprendre que la convergence est la combinaison de deux concepts :
    la consistance et la stabilité ; savoir utiliser ces notions pour
    évaluer l'impact des erreurs d'arrondi.

-   savoir calculer l'ordre de consistance et montrer la convergence de
    schémas de base.

-   comprendre l'apport de schémas symplectiques pour les systèmes
    hamiltoniens.
:::

::: {.section}
Limites du schéma d'Euler
=========================

La première limite du schéma d'Euler est qu'il est d'ordre 1,
c'est-à-dire qu'il produit une erreur en ${\Delta t}^2$ à chaque pas.
Nous verrons dans la suite des algorithmes d'ordre supérieur qui
permettent d'utiliser un pas plus grand pour une précision donnée. Mais
au delà de cette problématique, il existe des systèmes pour lesquels de
telles méthodes (même d'ordre supérieur) échouent. En voici deux
exemples célèbres.

::: {.section}
Systèmes raides {#sec_systRaides .section}
---------------

La dénomination *systèmes raides* a été introduite en 1952 par
Hirschfelder pour désigner des systèmes comprenant des dynamiques aux
constantes de temps très différentes. Dans ce cas, le pas nécessaire
pour simuler avec précision les dynamiques très rapides est si petit,
qu'il est alors impossible de simuler assez longtemps pour observer les
parties lentes. La particularité de ces systèmes est que cette
décroissance du pas apparaît alors que la solution est parfaitement
régulière, et non pas proche de singularités. C'est le cas des systèmes
linéaires $$
\dot{x} = A x + b
$$ avec $A$ de Hurwitz quand le rapport entre les parties réelles
maximales et minimales des valeurs propres devient très grand. Ce
phénomène peut notamment apparaître dans un simple système masse/ressort
$$
m\ddot{y} = -\rho \dot{y} - k y
$$ qui se met sous la forme précédente avec
$x=(y,\dot{y})\in \mathbb{R}^2$ et
$A=\left(\begin{smallmatrix} 0&1\\-\dfrac{k}{m} & -\dfrac{\rho}{m} \end{smallmatrix}\right)$.
Lorsque les valeurs propres sont réelles (i.e. $\rho>2\sqrt{mk}$), leur
rapport est donné par $$
\frac{1+\sqrt{1-4\dfrac{mk}{\rho^2}}}{1-\sqrt{1-4\dfrac{mk}{\rho^2}}}
$$ qui explose lorsque $\frac{mk}{\rho^2}$ tend vers 0. Par exemple,
lorsque les frottements sont très grands par rapport à la raideur du
ressort, ou bien lorsque $\rho$ et $k$ sont du même ordre de grandeur et
très grands.

Plus généralement, la coexistence de dynamiques très lentes à très
rapides apparaît en cinétique chimique ou en biologie. La réaction de
Robertson (1966) `\begin{align*}
A & \stackrel{0.04}{\longrightarrow}  B \quad \text{(lente)} \\ 
B + B & \stackrel{3 \times 10^7}{\longrightarrow}  B + C \quad \text{(très rapide)}  \\
B + C & \stackrel{10^4}{\longrightarrow}  A + C  \quad \text{(rapide)} 
\end{align*}`{=tex} modélisée par `\begin{align*}
\dot{x}_a &= -0.04 x_b + 10^4 x_bx_c \\
\dot{x}_b &= 0.04 x_a - 10^4 x_bx_c - 3\times 10^7 x_b^2\\
\dot{x}_c &= 3\times 10^7 x_b^2
\end{align*}`{=tex} en est un exemple classique, souvent utilisée pour
tester les schémas numériques. Il s'avère que pour ces systèmes, des
schémas dits *implicites* performent beaucoup mieux car ils autorisent
l'utilisation de pas plus grands pour une même précision et plus de
stabilité (voir l'exercice [*Explicite ou Implicite?* (p.
`\pageref*{exo_exp_impl}`{=tex})](#exo_exp_impl)). Pour plus de détails
voir [@Hairer96]. L'impossibilité de trouver un pas approprié avec un
schéma d'Euler explicite pour ce système est aussi illustré dans le
notebook Equations Differentielles II.ipynb.
:::

::: {.section}
Systèmes hamiltoniens {#sec_systHamiltoniens .section}
---------------------

La mécanique hamiltonienne permet typiquement de modéliser le
comportement de systèmes dont une certaine énergie est conservée au
cours du temps. Il peut s'agir par exemple de planètes en interaction
gravitationnelle, de particules en interaction électromagnétique, etc.

Par exemple, dans un problème à $N$ corps en interaction
gravitationnelle, l'hamiltonien s'écrit[^2] $$
H(q,p) = \sum_{i=1}^{N} \frac{1}{2 m_i}p_i^\top p_i  - \sum_{1\leq i< k \leq N} G\frac{m_i m_j}{\|q_i-q_k\|}
$$ où $q_i\in \mathbb{R}^3$ désigne la position de chaque corps, $m_i$
sa masse, et $p_i=m_i\dot{q}_i\in \mathbb{R}^3$ sa quantité de
mouvement. Le comportement de chaque corps est alors régi par la
dynamique hamiltonienne[^3] `\begin{align*}
\dot{q}_i &= \nabla_{p_i} H(q,p) = \frac{1}{m_i} p_i \\
\dot{p}_i &= -\nabla_{q_i} H(q,p) = -G \sum_{k\neq i} \frac{m_i m_j}{\|q_i-q_k\|^3}(q_i-q_k)
\end{align*}`{=tex} On a alors le long des trajectoires $$
\frac{d}{dt}H(q(t),p(t)) = \left< \nabla_q H(t,q(t),p(t)), \dot{q} \right> + \left< \nabla_p H(t,q(t),p(t)), \dot{p} \right> = 0
$$ et l'énergie $H(q,p)$ est donc conservée.

Or, lorsqu'on essaye de simuler le système solaire avec un schéma
d'Euler (explicite), l'énergie augmente peu à peu à chaque révolution et
les trajectoires sont des spirales divergentes. Avec un schéma d'Euler
implicite, Jupiter et Saturne s'effondre vers le soleil et sont éjectées
du système solaire ! Même des schémas d'ordre supérieur ne permettent
pas de simuler correctement ce système sur des temps "courts" sur
l'échelle de temps astronomique (à moins de prendre des pas
déraisonnablement petits). En fait, le problème c'est que ces méthodes
d'intégration ne préservent pas les propriétés structurelles des
solutions telles que la conservation de l'énergie. Il faut donc
développer des schémas particuliers, appelés *symplectiques*, comme
illustré sur un simple oscillateur dans l'exercice [*Schéma
symplectique* (p.
`\pageref*{exo_symplectique}`{=tex})](#exo_symplectique). Pour aller
plus loin sur ces méthodes, voir [@Hairer10]. Un exemple simple de
système à deux corps est aussi donné dans le notebook Equations
Differentielles II.ipynb.
:::
:::

::: {.section}
Méthodes à un pas
=================

::: {.section}
Principe
--------

Pour approximer les solutions d'une équation différentielle sur un
intervalle $[0,T]$, les méthodes numériques à un pas se basent sur la
représentation intégrale $$
x(t) = x_0 + \int_{t_0}^t f(s,x(s)) ds  = x_0 + \sum_{j=0}^{J-1} \int_{t_j}^{t_{j+1}}f(s,x(s)) ds
$$ où $t_0 < t_1 < \ldots < t_J$ avec $t_J=T$. L'idée est d'approximer
les intégrales $\int_{t_j}^{t_{j+1}}f(s,x(s))$ sur des intervalles
$[t_j,t_{j+1}]$ suffisamment petits.

Dans la suite, on note $x^j$ l'approximation au temps $t_j$ de la valeur
exacte $x(t_j)$ et ${\Delta t}_j = t_{j+1}-t_j$ le $j$ème pas de temps.
L'idée est de calculer récursivement $$
x^{j+1} = x^j + {\Delta t}_j \Phi(t_j,x^j,{\Delta t}_j)
$$ où $\Phi(t_j,x^j,{\Delta t}_j)$ doit donc approximer $$
\frac{1}{t_{j+1}-t_j} \int_{t_j}^{t_{j+1}}f(s,x(s)) ds \ .
$$ Les différentes méthodes de quadrature, i.e. d'approximation de
l'intégrale, peuvent donc être mises à profit. La difficulté ici est que
seule la valeur initiale $f(t_j,x(t_j))$ de $f$ est connue (ou du moins
estimée) à l'itération $j$, par $f(t_j,x^j)$. On distingue donc les
méthodes *explicites* où $\Phi(t_j,x^j,{\Delta t}_j)$ est écrite
directement explicitement en fonction de la valeur initiale $x^j$, et
les méthodes *implicites* où cette expression n'est connue
qu'implicitement et des étapes intermédiaires de calcul sont
nécessaires.
:::

::: {.section}
Exemples
--------

1.  Méthodes explicites:

-   Euler explicite: l'intégrale est approximée par l'aire d'un
    rectangle déterminé par la valeur initiale de $f$ à *gauche de
    l'intervalle*, i.e.\
    $$
      x^{j+1} = x^j + {\Delta t}_j \, f(t_j,x^j) \ .
      $$

-   méthode de Heun : l'intégrale est approximée par l'aire d'un trapèze
    déterminé par la valeur initiale de $f$ et une approximation de sa
    valeur finale, i.e., $$
      x^{j+1} = x^j+\frac{{\Delta t}_j}{2}\Big(f(t_j,x^j) + f\big(t_{j+1},x^j+{\Delta t}_j f(t_j,x^j)\big) \Big) \ .
      $$

-   schéma de Runge--Kutta d'ordre 4: $$
    \left\{
    \begin{aligned}
    F_1 & = f(t_j,x^{j}) \\
    F_2 & = f\left(t_j+\frac{{\Delta t}_j}{2}, x^{j} + \frac{{\Delta t}_j}{2} F_1\right) \\
    F_3 & = f\left(t_j+\frac{{\Delta t}_j}{2}, x^{j} + \frac{{\Delta t}_j}{2} F_2\right) \\
    F_4 & = f(t_j + {\Delta t}_j, x^j + {\Delta t}_j F_3),
    \end{aligned}
    \right.
    $$ et on pose $$
    x^{j+1} = x^{j} + {\Delta t}\, \frac{F_1 + 2F_2 + 2F_3 + F_4}{6} \ .
    $$

2.  Méthodes implicites:

-   Euler implicite : l'intégrale est approximée par l'aire d'un
    rectangle déterminé par la valeur finale de $f$ à *droite de
    l'intervalle*, i.e.\
    $$
      x^{j+1} = x^j + {\Delta t}_j \, f(t_{j+1},x^{j+1}) \ .
      $$

-   méthode des trapèzes (ou Crank--Nicolson) : l'intégrale est
    approximée par l'aire du trapèze déterminé par les valeurs initiales
    et finales de $f$, i.e.  $$
    x^{j+1} = x^j+\frac{{\Delta t}_j}{2} \, \Big( f(t_j,x^j) + f(t_{j+1},x^{j+1})\Big) \ .
    $$

-   méthode du point milieu : l'intégrale est approximée par l'aire d'un
    rectangle déterminé par une approximation de la valeur de $f$ au
    milieu de l'intervale, i.e. $$
      x^{j+1} = x^j + {\Delta t}_j f\left(\frac{t_j+t_{j+1}}{2}, \frac{x^j+x^{j+1}}{2}\right) \ .
      $$

On peut bien sûr construire des méthodes plus compliquées et plus
précises pour des méthodes de Runge--Kutta d'ordre supérieur (explicites
ou implicites).
:::

::: {.section}
Définition implicite de $\Phi$ {#sec_def_impl .section}
------------------------------

Dans les schémas implicites, l'application $\Phi$ est définie de manière
implicite. Par exemple, pour le schéma d'Euler, on a : $$
\Phi(t_j,x^j,{\Delta t}_j) = f\Big(t_j + {\Delta t}_j, x^j + {\Delta t}_j\Phi(t_j,x^j,{\Delta t}_j) \Big).
$$ Il faut donc s'assurer que $\Phi$ est bien définie, c'est-à-dire
qu'il existe bien $x^{j+1}$ tel que $$
x^{j+1} = x^j + {\Delta t}_j \, f(t_{j+1},x^{j+1}) \ .
$$ Pour cela, nous pouvons voir $x^{j+1}$ comme le point fixe de
l'application $F_j$ définie par $$
F_j(x) = x^j + {\Delta t}_j \, f(t_{j+1},x) \ .
$$ à $x^j$, ${\Delta t}_j$, $t_{j+1}$ fixés. L'existence (et l'unicité)
de ce point fixe peut alors être démontrée par le théorème de point fixe
de Banach. Si $x\mapsto f(t_{j+1},x)$ est Lipschitzienne, c'est-à-dire
s'il existe $L_j$ tel que $$
\|f(t_{j+1},x_a)-f(t_{j+1},x_b)\| \leq L_j \|x_a-x_b\| \qquad \forall (x_a,x_b)\in \mathbb{R}^n\times \mathbb{R}^n \ ,
$$ alors $F_j:\mathbb{R}^n \to \mathbb{R}^n$ est contractante pour un
pas de temps ${\Delta t}_j$ suffisamment petit puisque $$
\|F_j(x_a)-F_j(x_b)\| \leq  {\Delta t}_j L_j \|x_a-x_b\| \ .
$$ Puisque $\mathbb{R}^n$ est complet, on déduit par le théorème du
point fixe que $x^{j+1}$ existe bien.

En pratique, on peut utiliser la méthode itérative de construction de ce
point fixe donnée par la preuve du théorème pour approcher $x^{j+1}$.
Une stratégie est de partir de la valeur donnée par le schéma d'Euler
explicite $$
x^{j,0} = x^{j} + {\Delta t}_j f(t_j,x^{j})
$$ et affiner ensuite par l'algorithme du point fixe en itérant $$
x^{j,k+1} = F(x^{j,k}) 
$$ jusqu'à ce que l'évolution relative $$
\frac{x^{j,k+1}-x^{j,k}}{x^{j,0}}
$$ devienne inférieure à un seuil choisi par l'utilisateur. Puisque la
suite $(x^{j,k})_{k\in \mathbb{N}}$ est de Cauchy, on sait que cette
algorithme s'arrête en un nombre fini d'itérations.

Un tel schéma est plus lourd en terme de calculs qu'un algorithme
explicite mais il apporte en général plus de stabilité et permet souvent
d'utiliser un pas plus grand. C'est en particulier utile pour les
systèmes raides, comme illustré dans l'exercice [*Explicite ou
Implicite?* (p. `\pageref*{exo_exp_impl}`{=tex})](#exo_exp_impl).
:::
:::

::: {.section}
Analyse d'erreur
================

L'objectif de l'analyse d'erreur *a priori* est de donner une estimation
de l'erreur commise par la méthode numérique en fonction des paramètres
du problème (temps d'intégration, pas de temps, propriétés de $f$).
L'idée générale est de remarquer qu'à chaque pas de temps, on commet une
erreur d'intégration locale (erreur de troncature dans la discrétisation
de l'intégrale, à laquelle s'ajoutent souvent des erreurs d'arrondi), et
que ces erreurs locales s'accumulent au fil des pas. Le contrôle de
cette accumulation demande l'introduction d'une notion de stabilité
adéquate, alors que les erreurs locales sont liées à une notion de
consistance. L'alliance de stabilité et de consistante donne une
propriété de convergence qui est souhaitée lors de l'implémentation de
méthodes numériques.

::: {.section}
Erreur de troncature locale
---------------------------

L'erreur de troncature locale à l'itération $j$ est l'erreur que l'on
commet en une seule itération lors de l'approximation de l'intégrale
pour passer de $x^j$ à $x^{j+1}$. C'est donc l'erreur théorique que l'on
obtiendrait si l'on appliquait le schéma numérique à la solution exacte
$x(t_j)$. Elle est ainsi définie comme $$
\eta^{j+1} := \frac{x(t_{j+1}) - x(t_j) - {\Delta t}_j \Phi(t_j,x(t_j),{\Delta t}_j)}{{\Delta t}_j}.
$$

::: {.section}
### Définition -- Consistance {#def_consistance .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Consistance}`{=latex}

On note ${\Delta t}= \max_{0\le j\le J-1} {\Delta t}_j$ le pas de temps
maximal. On dit qu'une méthode numérique est *consistante* si $$
\lim_{{\Delta t}\to 0} \left( \max_{1\le j\le J} \|\eta^{j}\| \right) = 0 \ ,
$$ et qu'elle est *consistante d'ordre $\geq p$* s'il existe une
constante $c_s$ telle que, pour tout $0\le j\le J-1$, $$
\|\eta^{j+1}\| \le c_s \, ({\Delta t}_j)^{p} \ .
$$ Une méthode est donc *consistante d'ordre $p$* si elle est
consistante d'ordre $\geq p$, mais pas $\geq p+1$.
:::

::: {.section}
### Théorème -- Condition nécessaire et suffisante de consistance {#theo_CS_consistance .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Condition nécessaire et suffisante de consistance}`{=latex}

Si $\Phi$ est continue, alors le schéma est consistant si et seulement
si $$
\Phi(t,x,0) = f(t,x) \qquad \forall (t,x)\in \left[ 0,T \right]\times \mathbb{R}^n \ .
$$
:::

::: {.section}
#### Démonstration {#démonstration .proof}

Soit $C$ un ensemble fermé et borné tel que $x(t)\in C$ pour tout
$t\in \left[ 0,T \right]$. On note toujours
${\Delta t}= \max_{0\le j\le J-1} {\Delta t}_j$. Par la représentation
intégrale des solutions, $$
x(t_{j+1}) = x(t_j) + \int_{t_j}^{t_{j+1}} f(x(s),s)ds
$$ l'erreur de troncature locale s'écrit $$
\eta^{j+1} = \frac{1}{{\Delta t}_j}  \int_{t_j}^{t_{j+1}} \Big( f(s,x(s)) - \Phi(t_j,x(t_j),{\Delta t}_j) \Big)ds \ .
$$ Si le schéma est consistant alors cette erreur tend vers 0 lorsque
${\Delta t}$ tend vers 0 (pour n'importe quel système et n'importe
quelle trajectoire). Or, $$
\lim_{{\Delta t}\to 0} \frac{1}{{\Delta t}_j}  \int_{t_j}^{t_j+{\Delta t}} \Big( f(s,x(s)) - \Phi(t_j,x(t_j),{\Delta t}_j) \Big)ds = f(t_j,x(t_j)) - \Phi(t_j,x(t_j),0)
$$ qui doit donc être nul.

Réciproquement, supposons $\Phi(\cdot,\cdot,0)=f$. On doit montrer que
l'erreur de consistance tend vers 0 lorsque ${\Delta t}$ tend vers 0
(uniformément en $j=1,\hdots,N$). Soit $\varepsilon >0$. Par la
continuité de $\Phi$ et $f$ et puisque $\Phi(\cdot,\cdot,0)=f$, il
existe $\Delta_1 >0$ tel que si ${\Delta t}\leq \Delta_1$, alors $$
\|\Phi(t,x,{\Delta t}_j) -f(t,x) \| \leq \varepsilon \qquad \forall (t,x) \in \left[ 0,T \right]\times C \quad \forall j=1,\hdots,N \ .
$$ Donc $$
\|\eta^{j+1}\| \leq  \varepsilon + \frac{1}{{\Delta t}_j}  \int_{t_j}^{t_{j+1}} \big\| f(s,x(s)) - f(t_j,x(t_j)) \big\|ds \ .
$$ Puisque $s\mapsto f(s,x(s))$ est continue sur l'intervalle fermé et
borné $\left[ 0,T \right]$, elle y est uniformément continue, donc il
existe $\Delta_2 >0$ tel que si ${\Delta t}\leq \Delta_2$, $$
\big\| f(s,x(s)) - f(t_j,x(t_j)) \big\| \leq \varepsilon \qquad \forall s \in \left[ t_j,t_{j+1} \right]\quad \forall j=1,\hdots,N
$$ et donc $\|\eta^{j+1}\|\leq 2 \varepsilon$ pour tout $j$. Le schéma
est donc bien consistant.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Exemple -- Schémas consistants {#ex_consistance .example .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Schémas consistants}`{=latex}

Reprenons les exemples donnés plus haut.

-   Euler explicite : $\Phi(t,x,{\Delta t})= f(t,x)$ indépendamment de
    ${\Delta t}$ donc la condition est trivialement satisfaite.

-   Méthode de Heun :
    $\Phi(t,x,{\Delta t}) = \frac{f(t,x) + f(t,x+{\Delta t}f(t,x))}{2}$
    donne bien $f(t,x)$ si ${\Delta t}=0$.

-   Runge Kutta d'ordre 4 : lorsque ${\Delta t}=0$,
    $F_1=F_2=F_3=F_4=f(t,x)$ donc
    $\Phi(t,x,0) = \frac{F_1+2F_2+2F_3+F_4}{6}=f(t,x)$.

De même, la consistance des méthodes implicites s'obtiennent en
remarquant que $x^{j+1}=x^{j}$ lorsque ${\Delta t}=0$.
:::

::: {.section}
Cette condition suffisante permet donc de prouver facilement le
caractère consistant d'un schéma. Cependant, en pratique, on s'intéresse
surtout à son ordre de consistance. Pour cela, l'erreur de consistance
se calcule souvent par des développements de Taylor des solutions
lorsque celles-ci sont suffisamment régulières, et la constante $c_s$
s'exprime alors comme une borne sur les dérivées des solutions. En fait,
on remarque que lorsque $f$ est continue, la solution est $C^1$ (par
définition de nos solutions). Mais puisque $\dot{x}(t)=f(t,x(t))$,
$\dot{x}$ hérite de la régularité de $f$: si $f$ est $C^k$ alors les
solutions $x$ sont $C^{k+1}$. Le calcul de l'ordre de consistance dans
le cas dus schéma d'Euler explicite est donné ci-dessous. Pour les
autres schémas, voir l'exercice [*Consistance de schémas* (p.
`\pageref*{exo_consist}`{=tex})](#exo_consist)
:::

::: {.section}
#### Exemple -- Ordre de consistance du schéma d'Euler explicite {#ex_consistance_Euler .example .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Ordre de consistance du schéma d'Euler explicite}`{=latex}

L'erreur de troncature s'écrit $$
\eta^{j+1} = \frac{x(t_j + {\Delta t}_j) - \Big( x(t_j) + {\Delta t}_j \, f(t_j,x(t_j)) \Big)}{{\Delta t}_j}.
$$ Or, si $f$ est $C^1$, alors $x$ est $C^2$ et par application la
formule de Taylor avec reste intégral, on a $$
x(t_j + {\Delta t}_j) =  x(t_j) + {\Delta t}f(t_j,x(t_j))  + {\Delta t}_j^2 \int_{0}^{1} \ddot{x}(t_j+s{\Delta t}_j)  (1-s) ds ,
$$ en utilisant $\dot{x}(t_j)=f(t_j,x(t_j))$. Ceci donne donc $$
\|\eta^{j+1}\| \leq {\Delta t}_j  \int_{0}^{1} \ddot{x}(t_j+s{\Delta t}_j)  (1-s) ds \leq \frac{{\Delta t}_j}{2} \max_{t\in [t_j,t_{j+1}]} \|\ddot{x}(t)\| \leq \frac{{\Delta t}_j}{2} \max_{t\in [0,T]} \|\ddot{x}(t)\| \ .
$$ Le schéma d'Euler explicite est donc consistant d'ordre $\geq 1$ avec
$$
c_s= \frac{\max_{t\in [0,T]} \|\ddot{x}(t)\|}{2} \ .
$$

Notons qu'en utilisant $\dot{x}(t) = f(t,x(t))$, $$
\ddot{x}(t) = \partial_t f(t,x(t)) + \partial_x f(t,x(t)) \cdot f(t,x(t)),
$$ et on peut exprimer $c_s$ en fonction de bornes sur $x$ et sur les
dérivées de $f$. Plus généralement, en dérivant successivement lorsque
$f$ est $C^k$, notons
$f^{[k]} : \mathbb{R}\times \mathbb{R}^n \to \mathbb{R}^n$ la fonction
dépendant des dérivées successives de $f$ telle que $$
x^{(k+1)}(t) = f^{[k]}(t,x(t)) \ .
$$ On a alors le théorème suivant, généralisant les calculs précédents.
:::

::: {.section}
### Théorème -- Condition nécessaire et suffisante de consistance d'ordre $\geq p$ {#theo_CS_consistance_ordre_p .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Condition nécessaire et suffisante de consistance d'ordre \(\geq p\)}`{=latex}

Si $\Phi$ et $f$ sont $C^p$ alors le schéma est consistant d'ordre
$\geq p$ si et seulement si $$
\frac{\partial^k \Phi}{\partial {\Delta t}^k}(t,x,0) = \frac{1}{k+1}  f^{[k]}(t,x) \qquad \forall 0\leq k\leq p-1 \ , \quad \forall (t,x)\in \left[ 0,T \right]\times \mathbb{R}^n \ .
$$
:::

::: {.section}
#### Démonstration {#démonstration-1 .proof}

L'erreur de troncature s'écrit $$
\eta^{j+1} = \frac{x(t_j + {\Delta t}_j) - \Big( x(t_j) + {\Delta t}_j \, \Phi(t_j,x(t_j),{\Delta t}_j) \Big)}{{\Delta t}_j}.
$$ Or, si $f$ est $C^p$, alors $x$ est $C^{p+1}$ et par application la
formule de Taylor avec reste intégral, on a `\begin{align*}
x(t_j + {\Delta t}_j) &= x(t_j) + \sum_{k=1}^p \frac{{\Delta t}_j^k}{k!}  x^{(k)} (t_j) +  \frac{{\Delta t}_j^{p+1}}{p!}\int_{0}^{1} x^{(p+1)}(t_j+s{\Delta t}_j)  (1-s)^p ds \\
&= x(t_j) + \sum_{k=0}^{p-1} \frac{{\Delta t}_j^{k+1}}{(k+1)!}  f^{[k]}(t_j,x(t_j)) +  \frac{{\Delta t}_j^{p+1}}{p!}\int_{0}^{1} x^{(p+1)}(t_j+s{\Delta t}_j)  (1-s)^p ds
\end{align*}`{=tex} Par ailleurs, puisque $\Phi$ est $C^p$, $$
\Phi(t,x,{\Delta t}) = \sum_{k=0}^{p-1} \frac{{\Delta t}^{k}}{k!}  \frac{\partial^k \Phi}{\partial {\Delta t}^k}(t,x,0) +  \frac{{\Delta t}^{p}}{(p-1)!}\int_{0}^{1} \frac{\partial^{p} \Phi}{\partial {\Delta t}^p}(t,x,t_j+s{\Delta t}_j)  (1-s)^{p-1} ds
$$ Il s'ensuit que $$
\eta^{j+1} = \sum_{k=0}^{p-1} \frac{{\Delta t}_j^k}{k!} \left[ \frac{1}{k+1}  f^{[k]}(t_j,x(t_j)) - \frac{\partial^k \Phi}{\partial {\Delta t}^k}(t_j,x(t_j),0)\right] + {\Delta t}_j^p R_j
$$ où $R_j$ est borné (uniformément en ${\Delta t}_j$) par continuité de
$\frac{\partial^{p} \Phi}{\partial {\Delta t}^p}$ et $x^{(p+1)}$.

Maintenant, si le schéma est d'ordre $\geq p$, alors
$\frac{\eta^{j+1}}{{\Delta t}_j^p}$ doit rester borné lorsque
${\Delta t}_j$ tend vers 0 et on obtient bien la condition du théorème.
Réciproquement, si la condition du théorème est vérifiée, on obtient
directement que $\eta^{j+1}$ est borné en
${\Delta t}_j^p$.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Exemple -- Ordre de consistance de schémas {#ex_consistance_Euler .example .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Ordre de consistance de schémas}`{=latex}

On a vu que si $f$ est $C^1$, le schéma d'Euler explicite est consistant
d'ordre $\geq 1$. On peut le retrouver ici en appliquant le critère
précédent pour $p=1$ puisque $\Phi(\cdot,\cdot,0)=f$. Ensuite, si $f$
est $C^2$, on constate que $$
\frac{\partial\Phi}{\partial {\Delta t}}(t,x,0) = 0 \neq f^{[1]}(t,x) =\partial_t f(t,x) + \partial_x f(t,x) \cdot f(t,x)
$$ donc le schéma d'Euler explicite est consistant d'ordre exactement
$1$.

Par contre, toujours si $f$ est $C^2$, on constate que l'on a bien pour
le schéma de Heun $$
\frac{\partial\Phi}{\partial {\Delta t}}(t,x,0) =  f^{[1]}(t,x) =\partial_t f(t,x) + \partial_x f(t,x) \cdot f(t,x)
$$ donc ce schéma est d'ordre $\geq 2$. On peut vérifier que si $f$ est
$C^3$, le critère n'est pas vérifié à l'ordre supérieur donc il est
consistant d'ordre égal à 2.
:::
:::

::: {.section}
Stabilité
---------

Une fois que l'on a étudié l'erreur locale commise en une itération, on
s'intéresse à la manière dont elle va se propager au fur et à mesure des
itérations. Pour cela, la notion de stabilité quantifie la robustesse de
l'approximation numérique par rapport à l'accumulation des erreurs
locales et perturbations.

::: {.section}
### Définition -- Stabilité {#def_stab .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Stabilité}`{=latex}

On dit qu'une méthode numérique est *stable* s'il existe une constante
$S(T) > 0$ (indépendente des ${\Delta t}_j$) telle que, pour toutes
suites $x = \{ x^j \}_{1 \leq j \leq J}$ et
$z = \{ z^j \}_{1 \leq j \leq J}$ vérifiant $$
\left\{ \begin{aligned}
x^{j+1} & = x^j + {\Delta t}_j \Phi(t_j,x^j,{\Delta t}_j), \\
z^{j+1} & = z^j + {\Delta t}_j \Phi(t_j,z^j,{\Delta t}_j) + \delta^{j+1},
\end{aligned} \right.
$$ on ait $$
\max_{1 \leq j \leq J} \| x^j - z^j\| \leq S(T) \, \Big( \|x^0 -z^0\| + \sum_{j = 1}^J  \|\delta^j\| \Big).
$$
:::

::: {.section}
### Théorème -- Condition suffisante de stabilité {#theo_CS_stab .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Condition suffisante de stabilité}`{=latex}

Si $\Phi$ sont Lipschitziennes en $x$, c'est-à-dire il existe $L>0$ tel
que pour tout $0\leq j\leq J$, $$
\|\Phi(t_j,x_a,{\Delta t}_j)-\Phi(t_j,x_b,{\Delta t}_j)\|\leq L \|x_a-x_b\| \qquad \forall (x_a,x_b)\in \mathbb{R}^n \times \mathbb{R}^n
$$ alors le schéma est stable avec $S(T)=e^{L T}$.
:::

::: {.section}
#### Démonstration {#démonstration-2 .proof}

On a alors $$
\| x^{j+1} - z^{j+1} \| \leq  \| \delta^{j+1} \| + (1 + {\Delta t}_j L) \| x^{j} - z^{j} \| \leq \| \delta^{j+1} \| +  e^{{\Delta t}_j L} \| x^{j} - z^{j} \| 
$$ puisque $1+x \leq e^{x}$ pour tout $x\in \mathbb{R}$. Par récurrence,
on montre alors que pour tout $1\leq j \leq J$, $$
\| x^{j} - z^{j} \| \leq e^{(t_j-t_0) L} \|x^0 -z^0\| + \sum_{k=1}^j e^{(t_j-t_k)L} \| \delta^{k} \|  \ .
$$ Il s'ensuit que $$
\| x^{j} - z^{j} \| \leq e^{TL}\left(\|x^0 -z^0\|+ \sum_{k=1}^j \| \delta^{k} \|\right) \ ,
$$ ce qui donne le résultat.`\hfill$\blacksquare$`{=latex}
:::
:::

::: {.section}
Convergence
-----------

La combinaison de consistance et de stabilité donne une propriété dite
de *convergence* qui dit que l'erreur commise par le schéma par rapport
à la vraie solution converge vers 0 lorsque le pas de temps converge
vers 0. C'est une propriété cruciale pour un schéma numérique.

::: {.section}
### Définition -- Convergence {#def_conv .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Convergence}`{=latex}

Soit ${\Delta t}= \max_{0 \leq j \leq J-1} {\Delta t}_j$. Un schéma
numérique est *convergent* si $$
\lim_{{\Delta t}\to 0} \max_{1 \leq j \leq J} \|x^j - x(t_j)\| = 0
$$ lorsque $x^0 = x(t_0)$. S'il existe $p\in \mathbb{N}_{>0}$ et $c_v>0$
(indépendent de ${\Delta t}$) tel que $$
\max_{1 \leq j \leq J} \|x^j - x(t_j)\| \leq c_v ({\Delta t})^{p}
$$ on dit que le schéma est *convergent à l'ordre $p$*.
:::

::: {.section}
### Théorème -- Théorème de Lax {#theo_Lax .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Théorème de Lax}`{=latex}

Une méthode stable et consistante (à l'ordre $p$) est convergente (à
l'ordre $p$).
:::

::: {.section}
#### Démonstration {#démonstration-3 .proof}

Notons $z^j=x(t_j)$. On remarque que $$
z^{j+1}  = z^j + {\Delta t}_j \Phi(t_j,z^j,{\Delta t}_j) + {\Delta t}_j\, \eta^{j+1},
$$ où $\eta$ est l'erreur de consistance. D'après la propriété de
stabilité, on a donc $$
\|x^j - x(t_j)\| \leq S(T) \,  \sum_{j = 1}^J {\Delta t}_{j-1}\, \|\eta^j\| \ ,
$$ et par consistance $$
\|x^j - x(t_j)\| \leq S(T) \,  c_s \,  \sum_{j = 1}^J {\Delta t}_{j-1}\, ({\Delta t}_{j-1})^{p} \leq  c_s \, S(T) \, T \, ({\Delta t})^{p}  \ . 
$$`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Théorème -- Condition suffisante de convergence {#theo_CS_conv .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Condition suffisante de convergence}`{=latex}

L'inconvénient du théorème de Lax est qu'il faut prouver la stabilité
pour obtenir la convergence. Or la seule condition suffisante dont nous
disposions à cet effet, est le caractère globalement Lipschitzien de
$x\mapsto \Phi(t,x,{\Delta t})$. Mais il s'agit d'une condition très
forte. En fait, il est possible de prouver la convergence sous la
condition plus faible que $x\mapsto \Phi(t,x,{\Delta t})$ est
"localement Lipschitzienne" :

Si

1.  le schéma est consistant d'ordre $p$,

2.  pour tout boule fermée $B$ de $\mathbb{R}^n$, il existe $L>0$,
    ${\Delta t}_m>0$ tels que pour tout $t\in \left[ 0,T \right]$ et
    pour tout ${\Delta t}\in \left[ 0, {\Delta t}_m \right]$, $$
    \|\Phi(t_j,x_a,{\Delta t}_j)-\Phi(t_j,x_b,{\Delta t}_j)\|\leq L \|x_a-x_b\| \qquad \forall (x_a,x_b)\in B\times B 
    $$

Alors il existe un pas de temps maximal ${\Delta t}_{\max}>0$ tel que le
schéma est convergent d'ordre $p$.

L'hypothèse 2. est en particulier vérifiée si
$x\mapsto \Phi(t,x,{\Delta t})$ est $C^1$ d'après une version un peu
plus générale du théorème des accroissement finis.
:::

::: {.section}
#### Exemple -- Convergence du schéma d'Euler explicite {#ex_conv_Euler .example .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Convergence du schéma d'Euler explicite}`{=latex}

On a déjà montré que le schéma d'Euler explicite est consistant d'ordre
1. Par ailleurs, si $f$ est $C^1$ par rapport à $x$, alors
$x\mapsto \Phi(t,x) = f(t,x,{\Delta t})$ est $C^1$. Donc d'après le
théorème précédent, le schéma est convergent d'ordre 1.
:::
:::

::: {.section}
Erreurs d'arrondi et pas optimal
--------------------------------

A chaque itération, lorsque la machine calcule $x^{j+1}$, elle commet en
plus de l'erreur de troncature de l'intégrale des erreurs d'arrondi de
l'ordre de la précision machine. La solution obtenue est donc en fait
donnée par $$
\hat{x}^{j+1} = \hat{x}^j + {\Delta t}_j \left( \Phi(t_j,\hat{x}^j,{\Delta t}_j) + \rho^{j+1} \right)+ \varepsilon^{j+1}
$$ au lieu de $$
x^{j+1} = x^j + {\Delta t}_j \Phi(t_j,x^j,{\Delta t}_j) \ ,
$$ où $\rho$ modélise l'erreur commise sur le calcul de $\Phi$ et
$\epsilon$ l'erreur sur l'addition finale. La stabilité nous donne alors
l'écart $$
\max_{0\leq j \leq J} \|x^j-\hat{x}^j\| \leq S(T) \sum_{j=1}^J {\Delta t}_{j-1} \|\rho^{j}\| + \|\varepsilon^{j}\| \ .
$$ En considérant une borne $\varepsilon$ des $\varepsilon^{j}$ et
$\rho$ des $\rho^{j}$, on obtient $$
\max_{0\leq j \leq J} \|x^j-\hat{x}^j\| \leq S(T) (T\rho + J \varepsilon) \leq S(T) T \left(\rho + \frac{\varepsilon}{\min {\Delta t}_j} \right) \ ,
$$ et donc finalement, en supposant l'algorithme convergent d'ordre $p$,
`\begin{align*}
\max_{0\leq j \leq J} \|x(t_j)-\hat{x}^j\| &\leq \max_{0\leq j \leq J} \|x(t_j)-x^j\| + \|x^j - \hat{x}^j\| \\
&\leq c_v (\max_j {\Delta t}_j)^p +  S(T) T \left(\rho + \frac{\varepsilon}{\min_j {\Delta t}_j} \right) \ .
\end{align*}`{=tex} Les paramètres $\varepsilon$ et $\rho$ sont
typiquement petits de l'ordre d'un facteur de la précision machine.
Cependant, on voit que plus le pas de temps décroit, plus il y a
d'itérations et plus les erreurs d'arrondi se propagent. D'un autre
côté, plus il augmente, plus les erreurs de quadrature augmentent. En
supposant le pas constant, il y a donc un pas \`\`optimal'' donné par $$
{\Delta t}_{opt} = \left( \frac{S(T) T\varepsilon}{c_vp}\right)^{\frac{1}{p+1}} \ .
$$
:::
:::

::: {.section}
Annexe -- Choix du pas de temps
===============================

Jusqu'à présent, on a présenté des schémas dépendant de pas de temps
${\Delta t}_j$, sans jamais dire comment les choisir. Le plus simple est
de choisir un pas ${\Delta t}$ fixe mais il est difficile de savoir à
l'avance quel pas est nécessaire. En particulier, comment savoir si la
solution obtenue est suffisamment précise, sans connaître la vraie ?

::: {.section}
Pas fixe
--------

Une voie empirique est de fixer un pas, lancer la simulation, puis fixer
un pas plus petit, relancer la simulation, jusqu'à ce que les résultats
*ne semble plus changer* (au sens de ce qui nous intéresse d'observer).
Notons que la connaissance des constantes de temps présentes dans le
système peut aider à fixer un premier ordre de grandeur du pas. On
pourrait aussi directement choisir le pas ${\Delta t}_{opt}$ obtenu plus
haut en prenant en compte les erreurs d'arrondis. Mais les constantes
$c_v$ et $S(T)$ sont souvent mal connues et conservatives.
:::

::: {.section}
Adaptation du pas de temps
--------------------------

Les méthodes à pas fixe exploitent la convergence des schémas, mais

-   on ne peut pas prendre un pas de temps arbitrairement petit car on
    est contraint par le temps de simulation.

-   on n'a aucune idée de l'erreur commise et on n'est jamais sûr
    d'avoir la bonne solution.

-   l'utilisation d'un pas très petit peut n'être nécessaire qu'autour
    de certains points *sensibles* (proches de singularités par exemple)
    et consomme des ressources inutiles ailleurs.

L'idée serait donc plutôt d'adapter la valeur du pas ${\Delta t}_j$ à
chaque itération. En d'autres termes, on se fixe une tolérance d'erreur
que l'on juge acceptable et on modifie le pas de temps en ligne, selon
si l'on estime être au-dessus ou en-dessous du seuil d'erreur. Mais cela
suppose d'avoir une idée de l'erreur commise... Il existe justement des
moyens de l'estimer.

Tout d'abord, de quelle erreur parle-t-on ?

-   erreur *globale* ? L'idéal serait de contrôler
    $\max_{0\leq j\leq N} \|x^j - x(t_j)\|$. Or la stabilité nous dit
    que $$
    \max_{0\leq j\leq N} \|x^j - x(t_j)\| \leq S(T) \,  \sum_{j = 1}^J {\Delta t}_{j-1}\, \|\eta^j\|
    $$ avec $\eta^j$ les erreurs de consistances locales. Donc si on se
    fixe une tolérance sur l'erreur globale $\texttt{Tol}_g$, on a $$
    \|\eta^j\| \leq \frac{\texttt{Tol}_g}{TS(T)} \qquad \Longrightarrow \qquad \max_{0\leq j\leq N} \|x^j - x(t_j)\| \leq \texttt{Tol}_g \ .
    $$ En d'autre termes, $\texttt{Tol}_g$ nous fixe une erreur maximale
    *locale* sur $\eta^j$, à chaque itération. Notons cependant que
    cette borne ne prend pas en compte la propagation des erreurs
    d'arrondis : plus ${\Delta t}$ diminue, plus l'erreur globale risque
    d'augmenter. Ce phénomène devrait donc en toute rigueur aussi nous
    donner un pas de temps minimal ${\Delta t}_{\min}$. Notons que tous
    ces calculs dépendent des constantes $c_v$ et $S(T)$ qui sont
    souvent mal connues ou très conservatives.

-   erreur (absolue) *locale* ? A chaque itération, une erreur locale
    est commise dûe à l'approximation de l'intégrale. Cette erreur est
    donnée par $$
    e^{j+1} = \tilde{x}(t_{j+1}) -x^{j+1} = \left(x^j + \int_{t_j}^{t_{j+1}} f(s,\tilde{x}(s))ds\right)
    $$ où $\tilde{x}$ est la solution de $\dot{x}=f(t,x)$ qui serait
    initialisée à $x^j$ au temps $t_j$. Notons que si on avait
    $x^j=x(t_j)$, on aurait exactement
    $e^{j+1}={\Delta t}_j \eta^{j+1}$, où $\eta^{j+1}$ est l'erreur de
    consistance. On se donne donc une tolérance d'erreur locale $$
    \|e^{j+1}\| \leq \texttt{Tol}_{abs} \ .
    $$

-   erreur *relative* ? Fixer une erreur absolue est parfois trop
    contraignant et n'a de sens que si les solutions gardent un certain
    ordre de grandeur. En effet, l'erreur acceptable quand la solution
    vaut 1000 n'est peut-être pas la même que lorsqu'elle vaut 1. On
    peut donc plutôt exiger une certaine erreur relative
    $\texttt{Tol}_{rel}$, i.e., $$
    \frac{\|e^{j+1}\|}{\|x^j\|}\leq \texttt{Tol}_{rel} \ .
    $$

En général, les solvers assurent (approxivement) $$
\|e^{j+1}\| \leq \texttt{Tol}_{abs} + \texttt{Tol}_{rel} \|x^j\| \ .
$$ Par défaut, dans les solvers de Numpy, $\texttt{Tol}_{abs} = 10^{-6}$
et $\texttt{Tol}_{rel}= 10^{-3}$.

Mais pour cela nous devons trouver un moyen d'estimer l'erreur locale.
C'est souvent fait en utilisant une même méthode à deux pas différents
(par exemple ${\Delta t}_j$ et ${\Delta t}_j/2$), ou bien en imbriquant
des schémas de Runge-Kutta d'ordres différents.

En fait, il est possible de montrer (exercice) que si $f$ est $C^1$, on
a pour un schéma d'Euler explicite $$
\|e^{j+1}\| = {\Delta t}_j \, \frac{\big\|f(t_{j+1},x^{j+1}) - f(t_j,x^j)\big\|}{2} + o({\Delta t}_j^2) \ 
$$

On peut donc estimer à chaque itération l'erreur commise $e^{j+1}$ et
adapter le pas selon si celle-ci est inférieure ou supérieure au seuil
de tolérance. En effet, puisque l'on sait par ailleurs que
$e^{j+1} = O({\Delta t}_j^2)$, une possible stratégie d'adaptation est
de prendre\
$$
{\Delta t}_{new} = {\Delta t}_j \sqrt{\frac{\texttt{Tol}_{abs}}{\|e^{j+1}\|}}
$$ (éventuellement avec une marge de sécurité)

La fonction correspondante

    def solve_euler_explicit_variable_step(f, x0, t0, tf, dtmin, dtmax, atol):
      ...
      return t, x

est fournie dans le notebook Equations Differentielles II.ipynb.
:::
:::

::: {.section}
Projet numérique
================

Les équations de Lotka-Volterra, ou "modèle proie-prédateur", sont
couramment utilisées pour décrire la dynamique de systèmes biologiques
dans lesquels un prédateur et sa proie interagissent dans un milieu
commun. Elles ont été proposées indépendamment par A. J. Lotka en 1925
et V. Volterra en 1926 et s'écrivent de la manière suivante :
`\begin{align*}
\dot{x}_1 &= x_1(\alpha -\beta x_2) \\
\dot{x}_2 &= -x_2(\gamma - \delta x_1)
\end{align*}`{=tex} où $x_1$ et $x_2$ désignent le nombre (positif) de
proies et de prédateurs respectivement et $\alpha$, $\beta$, $\gamma$,
$\delta$ sont des paramètres strictement positifs.

1.  Donner une interprétation physique à chaque terme de la dynamique.
    Montrer qu'il existe deux points d'équilibre $(0,0)$ et
    $\bar{x}\in \mathbb{R}_{> 0}\times\mathbb{R}_{> 0}$. Que peut-on
    dire de leur stabilité à ce stade ?

2.  A l'aide des fonctions `meshgrid` et `quiver`, visualiser
    graphiquement le champ de vecteurs. Intuiter le comportement des
    solutions. On pourra aussi utiliser `streamplot` pour visualiser le
    portrait de phase.

3.  Par le théorème de Cauchy-Lipschitz, démontrer que toute solution
    initialisée dans $\mathbb{R}_{> 0}\times\mathbb{R}_{> 0}$ reste dans
    $\mathbb{R}_{> 0}\times\mathbb{R}_{> 0}$ sur son ensemble de
    définition.

4.  On considère la fonction $$
    H(x_1,x_2) = \delta x_1 - \gamma \ln x_1 + \beta x_2 - \alpha \ln x_2  
    $$ définie sur $\mathbb{R}_{> 0}\times \mathbb{R}_{> 0}$. Calculer
    la dérivée de $H$ le long des solutions initialisées dans
    $\mathbb{R}_{> 0}\times \mathbb{R}_{> 0}$. En déduire que toute
    solution maximale initialisée dans
    $\mathbb{R}_{> 0}\times \mathbb{R}_{> 0}$ est définie sur
    $\mathbb{R}$.

5.  Représenter les courbes de niveau de $H$. Où se trouve $\bar{x}$ ?
    Qu'en conclut-on sur le comportement des solutions ? En déduire
    (graphiquement) que $\bar{x}$ est stable, au sens de la définition
    de stabilité.

On souhaite maintenant simuler numériquement les trajectoires.

6.  Coder une fonction du type

        def solve_euler_explicit(f, x0, dt, t0, tf):
            ...
            return t, x

    prenant en entrée une fonction
    $f:\mathbb{R}\times \mathbb{R}^n \to \mathbb{R}^n$ quelconque, une
    condition initiale $x_0$, un pas de temps $dt$, les temps initiaux
    et finaux, et renvoyant le vecteur des temps $t^j$ et de la solution
    $x^j$ du schéma d'Euler explicite appliqué à $\dot{x}=f(t,x)$. La
    tester sur une équation différentielle aux solutions exactes
    connues. Vérifier la convergence du schéma lorsque $dt$ tend vers 0.
    Comment visualiser graphiquement l'ordre de convergence ?

7.  Utiliser le schéma d'Euler explicite pour simuler les équations de
    Lotka-Volterra. Que constate-t-on en temps long ? Cette résolution
    vous semble-t-elle fidèle à la réalité ? On pourra tracer
    l'évolution de la fonction $H$.

8.  Coder maintenant une fonction du type

        def solve_euler_implicit(f, x0, dt, t0, tf, itermax = 100):
            ...
            return t, x

    donnant la solution d'un schéma d'Euler implicite appliqué à
    $\dot{x}=f(t,x)$ selon la méthode présentée dans le cours. Vérifier
    de nouveau sa convergence sur des solutions connues. Que se
    passe-t-il cette fois-ci sur les équations de Lotka-Volterra ?

On propose maintenant de modifier ces schémas de façon à stabiliser $H$
et assurer sa conservation le long des solutions numériques.

9.  Expliquer pourquoi les solutions de `\begin{align*}
     \dot{x}_1 &= x_1(\alpha -\beta x_2) - u_1(x_1,x_2) (H(x_1,x_2)-H_0) \\
     \dot{x}_2 &= -x_2(\gamma - \delta x_1) - u_2(x_1,x_2) (H(x_1,x_2)-H_0) 
     \end{align*}`{=tex} sont identiques à celles de Lotka-Volterra si
    $H_0 = H(x(0))$ pour tout choix de $u:\mathbb{R}^2 \to \mathbb{R}^2$
    continûment différentiable.

10. Soit $H_0\in \mathbb{R}$. Calculer la dérivée de $H-H_0$ le long des
    solutions de ce nouveau système. Montrer que l'on peut choisir $u$
    tel que $$
     \frac{d }{dt} (H(x(t))-H_0) = -k \| \nabla H(x(t)) \|^2 (H(x(t))-H_0) \ .
     $$ En déduire qu'alors $H(x(t))$ converge exponentiellement vers
    $H_0$ lorsque $t$ tend vers l'infini si $x$ reste à une distance
    strictement positive de $\bar{x}$.

11. En déduire comment modifier l'implémentation du schéma d'Euler pour
    assurer la stabilité de $H$. Quel est le rôle de $k$ ? Peut-il être
    choisi arbitrairement grand ? Pourquoi ? On pourra exprimer
    $H(x^{j+1})-H(x_0)$ en fonction de $H(x^{j})-H(x_0)$ au premier
    ordre en $dt$.
:::

::: {.section}
Exercices
=========

::: {.section}
Consistance et ordre de schémas {#exo_consist .exo}
-------------------------------

Supposons $f$ de classe $C^2$. Montrer que :

::: {.section}
#### Question 1 {#consist-1 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

le schéma de Heun est consistant d'ordre $\geq 2$ et égal à 2 si $f$ est
$C^3$. ([Solution p.
`\pageref*{answer-consist-1}`{=tex}](#answer-consist-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 {#consist-2 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

le schéma d'Euler implicite est consistant d'ordre $\geq 1$ ([Solution
p.
`\pageref*{answer-consist-2}`{=tex}](#answer-consist-2){.no-parenthesis}.)
:::

::: {.section}
#### Question 3 {#consist-3 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

la méthode des trapèzes est consistante d'ordre $\geq 2$. ([Solution p.
`\pageref*{answer-consist-3}`{=tex}](#answer-consist-3){.no-parenthesis}.)
:::

::: {.section}
#### Question 4 {#consist-4 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 4}`{=latex}

le schéma du point milieu est consistant d'ordre $\geq 2$. ([Solution p.
`\pageref*{answer-consist-4}`{=tex}](#answer-consist-4){.no-parenthesis}.)
:::

::: {.section}
#### Question 5 {#consist-5 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 5}`{=latex}

le schéma de Runge-Kutta d'ordre 4 est bien consistant d'ordre $4$ si
$f$ est $C^5$. ([Solution p.
`\pageref*{answer-consist-5}`{=tex}](#answer-consist-5){.no-parenthesis}.)
:::

::: {.section}
On supposera le pas suffisamment petit pour que les schémas implicites
soient définis.
:::
:::

::: {.section}
Convergence de schémas {#conv .question .unnumbered .unlisted}
----------------------

`\addcontentsline{toc}{subsection}{Convergence de schémas}`{=latex}

Sous l'hypothèse que $f$ est $C^1$, montrer que les schémas de Heun et
d'Euler implicite sont convergents. ([Solution p.
`\pageref*{answer-conv}`{=tex}](#answer-conv){.no-parenthesis}.)
:::

::: {.section}
Explicite ou implicite ? {#exo_exp_impl .exo}
------------------------

::: {.section}
#### Question 1 {#impl-1 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Comparer les performances des schémas d'Euler implicites et explicites à
pas fixe dans le cas de $\dot{x} = -\lambda x$, $x(0)=1$, et
$\dot{x} = \lambda x$, $x(0)=1$, sur un horizon de temps $T$ donné.
([Solution p.
`\pageref*{answer-impl-1}`{=tex}](#answer-impl-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 {#impl-2 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Lorsqu'on modélise des systèmes chimiques ou biologiques, on obtient
souvent des réactions aux constantes de temps très différentes. Vaut-il
mieux utiliser un schéma d'Euler implicite ou explicite pour simuler $$
\dot{x} = \left(
  \begin{matrix}
  -1 & 0 \\
  0 & -\mu
  \end{matrix}
  \right) x 
$$ avec $\mu >> 1$ ? ([Solution p.
`\pageref*{answer-impl-2}`{=tex}](#answer-impl-2){.no-parenthesis}.)
:::
:::

::: {.section}
Euler symplectique {#exo_symplectique .exo}
------------------

Pour $\omega>0$ donné, considérons le système $$
\dot{x}_1 \;=\;  x_2
\quad ,\qquad 
\dot{x}_2(t)\;=\; -\omega^2 x_1
$$ de condition initiale $x(0)\;=\; (1,0)$. On rappelle que pour une
suite de la forme $x^{j+1}=A x^j$ converge vers 0 si les valeurs propres
de $A$ sont à l'intérieur du cercle unité et diverge si au moins une
valeur propre est à l'extérieur.

::: {.section}
#### Question 1 {#symp-1 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Montrer que pour n'importe quel pas ${\Delta t}$ fixé, un schéma d'Euler
explicite donne une solution divergente, et un schéma d'Euler implicite
donne une solution qui converge vers 0. Lequel a raison ? ([Solution p.
`\pageref*{answer-symp-1}`{=tex}](#answer-symp-1){.no-parenthesis}.)
:::

::: {.section}
On définit maintenant le schéma suivant qui \`\`mélange'' les schémas
d'Euler implicites et explicites : `\begin{align*}
x^{j+1}_1 &= x^{j}_1 + {\Delta t}\, x^{j}_2 \\
x^{j+1}_2 &= x^{j}_2 - {\Delta t}\, \omega^2 x^{j+1}_1
\end{align*}`{=tex}
:::

::: {.section}
#### Question 2 {#symp-2 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Montrer que la quantité
$\omega^2 x_1^2 + x_2^2 +{\Delta t}\, \omega^2 x_1x_2$ est conservée.
Quelle est alors la forme des solutions obtenues dans le plan de phase
si $\omega {\Delta t}<2$ ? En déduire la pertinence de ce schéma. On
parle de schéma *symplectique*, car il conserve les volumes. ([Solution
p. `\pageref*{answer-symp-2}`{=tex}](#answer-symp-2){.no-parenthesis}.)
:::

::: {.section}
#### Question 3 {#symp-3 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

En écrivant le schéma sous la forme $x^{j+1}=Ax^j$, montrer qu'il
diverge par contre si ${\Delta t}\, \omega > 2$. ([Solution p.
`\pageref*{answer-symp-3}`{=tex}](#answer-symp-3){.no-parenthesis}.)
:::

::: {.section}
#### Question 4 {#symp-4 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 4}`{=latex}

Plus généralement, proposer un schéma pour simuler un système
Hamiltonien du type `\begin{align*}
\dot{q} &= \nabla_p H(q,p) \\
\dot{p} &= - \nabla_q H(q,p)
\end{align*}`{=tex} où $(q,p)\in \mathbb{R}^N \times \mathbb{R}^N$ sont
les positions généralisées et quantités de mouvement, $H$ est le
Hamiltonien que l'on pourra vérifier être conservé le long des
trajectoires. ([Solution p.
`\pageref*{answer-symp-4}`{=tex}](#answer-symp-4){.no-parenthesis}.)
:::

::: {.section}
A noter que les conclusions de cet exercice sont les mêmes si l'on
utilise un schéma d'Euler implicite sur la première composante et un
schéma d'Euler explicite sur la deuxième. Ces deux schémas s'appellent
respectivement Euler symplectique A et B.
:::
:::
:::

::: {.section}
Corrections
===========

::: {.section}
Consistance et ordre de schémas {#correc_consist .correc}
-------------------------------

Vu que $f$ est $C^2$, la dérivée seconde (en temps) des solutions
s'écrit `\begin{align*}
\ddot{x}(t) &= \frac{d}{dt}\Big( f(t,x(t)) \Big) = \partial_t f(t,x(t))+ \partial_x f(t,x(t)) \dot{x}(t)\\ 
&= \partial_t f(t,x(t))+ \partial_x f(t,x(t)) f(t,x(t)).
\end{align*}`{=tex} On a donc $$
f^{[1]}(t,x) = \partial_t f(t,x)+ \partial_x f(t,x) f(t,x)
$$ et la formule de Taylor le long des solutions donne `\begin{equation}
\label{eq:DL_sol_exacte}
\begin{aligned}
x(t_{j+1}) = x(t_j) & + {\Delta t}f(t_j,x(t_j)) \\
& + \frac{{\Delta t}^2}{2} \Big( \partial_t f(t_j,x(t_j)) + \partial_x f(t_j,x(t_j)) f(t_j,x(t_j)) \Big) + \mathrm{O}({\Delta t}^3).
\end{aligned}
\end{equation}`{=tex}

Pour les calculs de consistance, deux options possibles:

-   soit on compare à la main `\eqref{eq:DL_sol_exacte}`{=tex} aux
    développements en puissances de ${\Delta t}$ de la solution
    numérique $x^{j+1}$, partant de $x(t_j)$.

-   soit on utilise la [condition nécessaire et suffisante de
    consistance (p.
    `\pageref*{theo_CS_consistance_ordre_p}`{=tex})](#theo_CS_consistance_ordre_p).

::: {.section}
#### Question 1 {#answer-consist-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

A la main, pour la méthode de Heun, $$
\eta^{j+1} = \frac{1}{{\Delta t}}\left( x(t_{j+1}) - x(t_j) - \frac{{\Delta t}}{2}\left[ f(t_j,x(t_j)) + f\Big(t_{j+1},x(t_j)+{\Delta t}f(t_j,x(t_j)) \Big) \right]\right). 
$$ Or, $$
\begin{aligned}
f\Big(t_{j+1},&x(t_j)+{\Delta t}f(t_j,x(t_j)) \Big)\\ 
&= f(t_j,x(t_j)) +  \partial_t f(t_j,x(t_j))(t_{j+1}-t_j) + \partial_x f(t_j,x(t_j)) {\Delta t}f(t_j,x(t_j)) + \mathrm{O}({\Delta t}^2)\\
& = f(t_j,x(t_j)) + {\Delta t}\Big( \partial_t f(t_j,x(t_j)) + \partial_x f(t_j,x(t_j)) f(t_j,x(t_j)) \Big) + \mathrm{O}({\Delta t}^2).
\end{aligned}
$$ On en déduit que $\eta^{j+1} = \mathrm{O}({\Delta t}^2)$ en utilisant
`\eqref{eq:DL_sol_exacte}`{=tex}. Donc on a une consistance d'ordre
$\geq 2$.

Sinon il suffit de constater que $$
\Phi(t,x,0) = f(t,x) \quad ,\quad \frac{\partial \Phi}{\partial {\Delta t}}(t,x,0) = \frac{1}{2} f^{[1]}(t,x)   \ .
$$ Par contre, si $f$ est $C^3$,
$\frac{\partial^2 \Phi}{\partial {\Delta t}^2}(t,x,0) \neq \frac{1}{3} f^{[2]}(t,x)$
donc le schéma n'est pas d'ordre 3 et donc il est d'ordre égal
exactement à 2.
:::

::: {.section}
#### Question 2 {#answer-consist-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Pour le schéma d'Euler implicite $$
\eta^{j+1} = \frac{x(t_{j+1}) - x(t_j) - \Delta t f(t_{j+1},x^{j+1})}{{\Delta t}},
$$ où $x^{j+1}$ est solution de $$
x^{j+1} = x(t_j) + {\Delta t}f\left(t_{j+1},x^{j+1}\right).
$$ Comme vu dans la section [Définition implicite de $\Phi$ (p.
`\pageref*{sec_def_impl}`{=tex})](#sec_def_impl), cette définition
implicite de $x^{j+1}$ admet une unique solution pour ${\Delta t}$
suffisamment petit si $f$ est Lipschitzienne par rapport à $x$. On
aimerait dire ici que $x^{j+1} = x(t_j) + \mathrm{O}({\Delta t})$ pour
${\Delta t}$ suffisamment petit. Pour faire ça proprement, fixons
$(t_j,x(t_j))$ et posons $$
F(x,{\Delta t}) = x - \big(x(t_j) + {\Delta t}f\left(t_j+{\Delta t},x\right)\big) 
$$ qui est de classe $C^1$. On a alors $$
F(x(t_j),0) = 0 \quad , \quad F(x^{j+1},{\Delta t})=0 \ .
$$ Puisque $\partial_x F(x(t_j),0) = \text{Id}$ est inversible, le
théorème des fonctions implicites nous dit que pour $\Delta t$
suffisamment petit, il existe une fonction $\psi$ de classe $C^1$ telle
que $$
F(x^{j+1},{\Delta t})=0 \qquad , \qquad x^{j+1} = \psi({\Delta t}) 
$$ au voisinage de $(x(t_j),0)$. Puisque $\psi$ est continue, il
s'ensuit donc bien que $x^{j+1} = x(t_j) + \mathrm{O}({\Delta t})$. On a
donc `\begin{align*}
f(t_{j+1},x^{j+1}) &= f(t_j,x(t_j)) + \partial_t f(t_j,x(t_j)) (t_{j+1}-t_j) +  \partial_x f(t_j,x(t_j))(x^{j+1} - x(t_j)) + \mathrm{O}(\|h\|^2) \\
&= f(t_j,x(t_j)) + \mathrm{O}({\Delta t})
\end{align*}`{=tex} avec l'incrément $h=(t_{j+1}-t_j,x^{j+1} - x(t_j))$
qui vérifie $\|h\|=\mathrm{O}({\Delta t})$.

Ainsi, toujours au vu de `\eqref{eq:DL_sol_exacte}`{=tex}, $$
\eta^{j+1} = \frac{1}{{\Delta t}}\left[ x(t_{j+1}) - \Big( x(t_j) + \Delta t f(t_j,x(t_j)) + \mathrm{O}({\Delta t}^2) \Big) \right]= \mathrm{O}({\Delta t}).
$$
:::

::: {.section}
#### Question 3 {#answer-consist-3 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Pour la méthode des trapèzes, on a l'erreur $$
\eta^{j+1} = \frac{x(t_{j+1}) - x(t_j) - \frac{{\Delta t}}{2} \left(f(t_j,x(t_j))+ f(t_{j+1},x^{j+1})\right)}{{\Delta t}},
$$ où $x^{j+1}$ est solution de $$
x^{j+1} = x(t_j) + \frac{{\Delta t}}{2} \left(f(t_j,x(t_j))+ f(t_{j+1},x^{j+1})\right) .
$$ Cette fois-ci on voudrait montrer que
$x^{j+1} = x(t_j)+{\Delta t}f(t_j, x(t_j)) + \mathrm{O}({\Delta t}^2)$.
Pour cela, on redéfinit $$
F(x,{\Delta t}) = x - \big(x(t_j) +\frac{{\Delta t}}{2} \left(f(t_j,x(t_j))+ f(t_{j}+{\Delta t},x^{j+1})\right) \big) 
$$ qui est de classe $C^1$. On a alors $$
F(x(t_j),0) = 0 \quad , \quad F(x^{j+1},{\Delta t})=0 \ .
$$ Puisque $\partial_x F(x(t_j),0) = \text{Id}$ est inversible, le
théorème des fonctions implicites nous dit que pour $\Delta t$
suffisamment petit, il existe une fonction $\psi$ de classe $C^1$ telle
que $$
F(x^{j+1},{\Delta t})=0 \qquad , \qquad x^{j+1} = \psi({\Delta t}) 
$$ au voisinage de $(x(t_j),0)$ et de plus, $$
\psi'(0) = \text{Id}^{-1} \cdot \partial_{\Delta t} F(x(t_j),0) = f(t_j,x(t_j)) \ .
$$ Puisque $\psi$ est de classe $C^1$, on a donc bien $$
x^{j+1} = x(t_j)+{\Delta t}f(t_j, x(t_j)) + \mathrm{O}({\Delta t}^2) \ .
$$ Il s'ensuit que $$
f(t_{j+1},x^{j+1}) = f(t_j, x(t_j)) + {\Delta t}\left(\partial_t f(t_j,x(t_j)) + \partial_x f(t_j,x(t_j))f(t_j, x(t_j))\right) + \mathrm{O}({\Delta t}^2)
$$ soit $$
x^{j+1} = x(t_j) + {\Delta t}f(t_j,x(t_j) + \frac{{\Delta t}^2}{2} \left(\partial_t f(t_j,x(t_j)) + \partial_x f(t_j,x(t_j))f(t_j, x(t_j))\right) + \mathrm{O}({\Delta t}^3)
$$ On en déduit donc $\eta^{j+1}=\mathrm{O}({\Delta t}^2)$.
:::

::: {.section}
#### Question 4 {#answer-consist-4 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 4}`{=latex}

Enfin, pour la méthode du point milieu, on a l'erreur $$
\eta^{j+1} = \frac{x(t_{j+1}) - x(t_j) - {\Delta t}f\left(t_j+\frac{{\Delta t}}{2},\frac{x(t_j)+x^{j+1}}{2}\right)}{{\Delta t}},
$$ où $x^{j+1}$ est solution de $$
x^{j+1} = x(t_j) + {\Delta t}f\left(t_j+\frac{{\Delta t}}{2},\frac{x(t_j)+x^{j+1}}{2}\right) .
$$ On montre de la même façon qu'à la question précédente que pour
${\Delta t}$ suffisamment petit,
$x^{j+1} = x(t_j)+{\Delta t}f(t_j, x(t_j)) + \mathrm{O}({\Delta t}^2)$
et donc `\begin{align*}
f&\left(t_j+\frac{{\Delta t}}{2},\frac{x(t_j)+x^{j+1}}{2}\right)\\ &= f(t_j,x(t_j)) + \partial_t f(t_j,x(t_j)) \frac{{\Delta t}}{2} +  \partial_x f(t_j,x(t_j))\left(\frac{x(t_j)+x^{j+1}}{2} - x(t_j)\right) + \mathrm{O}(\|h\|^2) \\
&= f(t_j, x(t_j)) + \frac{{\Delta t}}{2} (\partial_t f(t_j,x(t_j)) + \partial_x f(t_j,x(t_j))f(t_j,x(t_j))) + \mathrm{O}({\Delta t}^2)
\end{align*}`{=tex} avec l'incrément
$h=\left(\frac{{\Delta t}}{2}, \frac{x(t_j)+x^{j+1}}{2} - x(t_j)\right)$,
soit $$
x^{j+1} = x(t_j) + {\Delta t}f(t_j,x(t_j) + \frac{{\Delta t}^2}{2} (\partial_t f(t_j,x(t_j)) + \partial_x f(t_j,x(t_j))f(t_j,x(t_j))) + \mathrm{O}({\Delta t}^3)
$$ On en déduit donc $\eta^{j+1}=\mathrm{O}({\Delta t}^2)$.
:::

::: {.section}
#### Question 5 {#answer-consist-5 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 5}`{=latex}

On vérifie que le critère est vérifié pour $0\leq k \leq 3$ mais pas
pour $k=4$ !
:::
:::

::: {.section}
Convergence de schémas {#answer-conv .answer .unnumbered .unlisted}
----------------------

`\addcontentsline{toc}{subsection}{Convergence de schémas}`{=latex}

Tout d'abord, dans l'exercice précédent, nous avons montré que les
schémas de Heun et d'Euler implicite étaient consistants d'ordre 2 et 1
respectivement. Il ne nous reste donc plus qu'à montrer que $\Phi$ est
localement lipschitzienne (ou $C^1$) par rapport à $x$ pour ${\Delta t}$
suffisamment petit, pour en déduire la convergence à l'ordre 2 et 1
respectivement.

Pour le schéma de Heun, $$
\Phi(t,x,{\Delta t}) = \frac{1}{2}\Big(f(t,x) + f\big(t+{\Delta t},x+{\Delta t}f(t,x)\big)\Big)
$$ donc $\Phi$ est $C^1$ par rapport à $x$ si $f$ l'est.

Prenons maintenant le schéma d'Euler implicite. Pour
${\Delta t}\leq {\Delta t}_m$, $\Phi$ est définie par $$
\Phi(t,x,{\Delta t}) = f\Big(t+ {\Delta t}, x + {\Delta t}\Phi(t,x,{\Delta t}) \Big).
$$ Soit $B$ un compact de $\mathbb{R}^n$. Soit $B'$ un compact tel que
$x + {\Delta t}\Phi(t,x,{\Delta t}) \in B'$ pour tout $x\in B$, tout
$t\in [ 0,T ]$ et tout ${\Delta t}\in [ 0,{\Delta t}_m ]$. Puisque $f$
est continue, et $C^1$ par rapport à $x$, il existe $L_f>0$ tel que $$
\|f(t,x_a) - f(t,x_b) \| \leq L_f \|x_a-x_b\| \qquad \forall (x_a,x_b,t)\in B'\times B' \times [ 0,T+{\Delta t}_m ] \ . 
$$ Ceci est vrai par le théorème des accroissements finis appliqué à
$x\mapsto f(t,x)$ et pour $t$ dans un intervalle fermé et borné. Prenons
maintenant $(x_a,x_b)\in B\times B$, $t\in [ 0,T ]$ et
${\Delta t}\in [ 0,{\Delta t}_m ]$, alors `\begin{align*}
\|&\Phi(t,x_a,{\Delta t})-\Phi(t,x_b,{\Delta t}) \|\\ &= \| f\Big(t+ {\Delta t}, x_a + {\Delta t}\Phi(t,x_a,{\Delta t}) \Big)-f\Big(t+ {\Delta t}, x_b + {\Delta t}\Phi(t,x_b,{\Delta t}) \Big) \|\\
&\leq L_f \left( \|x_a-x_b \| + {\Delta t}\|\Phi(t,x_a,{\Delta t})-\Phi(t,x_b{\Delta t}) \| \right)
\end{align*}`{=tex} soit $$
\|\Phi(t,x_a,{\Delta t})-\Phi(t,x_b,{\Delta t}) \| \leq \frac{L_f}{1-L_f {\Delta t}} \|x_a-x_b \|
$$ si ${\Delta t}< 1/L_f$. Donc $\Phi$ est bien localement
lipschitzienne par rapport à $x$.
:::

::: {.section}
Explicite ou implicite ? {#explicite-ou-implicite}
------------------------

::: {.section}
#### Question 1 {#answer-impl-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Prenons d'abord $\dot{x}= -\lambda x$, $x(0)=1$, dont la solution exacte
est $x(t)=e^{-\lambda t}$.

Le schéma d'Euler explicite donne $$
x^{j+1} = x^j - \lambda{\Delta t}x^j =(1-\lambda{\Delta t})^j
$$ soit $$
x^{J} = (1-\lambda{\Delta t})^J = (1-\lambda{\Delta t})^{\frac{T}{{\Delta t}}} = \left((1-\lambda{\Delta t})^{\frac{T}{\lambda{\Delta t}}} \right)^\lambda \ .
$$ On a bien $$
\lim_{{\Delta t}\to 0} x^{J} = e^{-\lambda T} \ .
$$ Cependant, il faut $|1-\lambda{\Delta t}|<1$ pour que la solution
converge au moins vers 0. Sinon, pour $\lambda{\Delta t}= 2$,
$x^J = (-1)^J$, qui n'a rien à voir avec la solution. Pire, pour
$\lambda{\Delta t}= 2$, l'algorithme diverge. Il faut donc adapter
${\Delta t}$ à la constante de temps $\lambda$ du système. Ceci peut
poser problème lorsque l'on simule des systèmes sur des temps longs (par
rapport à $\lambda$)

De l'autre côté, le schéma d'Euler implicite donne $$
x^{j+1} = x^j - \lambda{\Delta t}x^{j+1} 
$$ soit $$
x^J = \frac{1}{(1+\lambda {\Delta t})^J} =  \frac{1}{(1+\lambda {\Delta t})^\frac{T}{{\Delta t}}}
$$ qui tend vers 0 quelque soit le pas ${\Delta t}$ ! On parle de
stabilité inconditionnelle. Ceci est très pratique pour des simulations
sur temps longs, où la condition $\lambda{\Delta t}<1$ est trop
contraignante.

Prenons maintenant $\dot{x}= \lambda x$, $x(0)=1$, dont la solution
exacte est $x(t)=e^{\lambda t}$. Cette fois-ci, Euler explicite donne $$
x^{J} = (1+\lambda{\Delta t})^{\frac{T}{{\Delta t}}}
$$ qui fait maintenant sens même pour des pas grands. Par contre, Euler
implicite donne $$
x^J =   \frac{1}{(1-\lambda {\Delta t})^\frac{T}{{\Delta t}}}
$$ qui n'est pas défini pour $\lambda {\Delta t}=1$ et qui explose pour
des valeurs proche de 1.
:::

::: {.section}
#### Question 2 {#answer-impl-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Lorsque l'on a deux dynamiques asymptotiquement stables aux constantes
de temps très différentes la condition de stabilité de Euler explicite
exige de choisir un pas câlé sur la plus petite constante de temps,
i.e. il faut ${\Delta t}<\frac{1}{\mu}$. Ceci est très exigeant car il
faut attendre un nombre d'itérations de l'ordre de $\mu$ pour voir
l'évolution du système lent. Par contre, une méthode implicite permet de
choisir librement le pas de temps en fonction des performances
souhaitées.
:::
:::

::: {.section}
Euler symplectique {#euler-symplectique}
------------------

::: {.section}
#### Question 1 {#answer-symp-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Dans le cas d'Euler explicite, $x^{j+1}=Ax^j$ avec $$
A = \left(
\begin{matrix}
1 & {\Delta t}\\
-{\Delta t}\, \omega^2 & 1
\end{matrix}
\right)
$$ dont les valeur propres sont $1 \pm i\omega {\Delta t}$ de norme
$\sqrt{1+{\Delta t}^2 \, \omega^2}>1$. Donc les solutions divergent.

Dans le cas d'Euler implicite, $x^{j+1}=Ax^j$ avec $$
A = \frac{1}{1+{\Delta t}^2 \, \omega^2} \left(
\begin{matrix}
1 & {\Delta t}\\
-{\Delta t}\, \omega^2 & 1
\end{matrix}
\right)
$$ dont les valeurs propres sont $1/(1 \pm i\omega {\Delta t})$ de norme
$1/\sqrt{1+{\Delta t}^2 \, \omega^2}<1$. Donc les solutions convergent
vers 0.

Or on peut vérifier que le long des vraies solutions, l'énergie
$\omega^2 x_1^2 + x_2^2$ est constante donc les trajectoires sont
bornées et ne peuvent pas converger vers zéro. Aucun des deux schémas
n'approxime les solutions correctement sur le long-terme.
:::

::: {.section}
#### Question 2 {#answer-symp-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

On vérifie par le calcul que $$
\omega^2 x_1^2 + x_2^2 +{\Delta t}\, \omega^2 x_1x_2 = 
x^\top
\left( 
  \begin{matrix}
  \omega^2 & \frac{{\Delta t}\, w^2}{2} \\
  \frac{{\Delta t}\, w^2}{2} & 1
  \end{matrix}
\right)
x
$$ est constante. Pour $\omega^2-\frac{{\Delta t}^2 \omega^4}{4}>0$,
soit $\omega {\Delta t}<2$, cette matrice est définie positive, donc les
solutions restent sur une ellipse. Cette ellipse se rapproche de la
vraie solution lorsque ${\Delta t}$ tend vers 0. Ce schéma est donc
approprié pour simuler les trajectoires sur un temps long.
:::

::: {.section}
#### Question 3 {#answer-symp-3 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

L'algorithme symplectique est décrit par $x^{j+1}=Ax^j$ avec $$
A = \left(
\begin{matrix}
1 & {\Delta t}\\
-{\Delta t}\, \omega^2 & 1-{\Delta t}^2 \, \omega^2
\end{matrix}
\right)
$$ dont le polynôme caractéristique s'écrit $$
s^2 - (2-{\Delta t}^2 \, \omega^2) s + 1
$$ On a les cas suivants :

-   si $(1-{\Delta t}^2 \, \omega^2)^2 -4 <0$, i.e., si
    $\omega {\Delta t}<2$, les valeurs propres sont imaginaires
    conjuguées et de module 1.

-   si $\omega {\Delta t}> 2$, les valeurs propres sont réelles de
    produit 1, donc l'une est supérieure à 1 est le schéma diverge.

-   dans le cas extrême où $\omega {\Delta t}= 2$, il y a une valeur
    propre double en -1.
:::

::: {.section}
#### Question 4 {#answer-symp-4 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 4}`{=latex}

Pour un système hamiltonien, on peut donc proposer `\begin{align*}
q^{j+1} &= q^{j} + {\Delta t}\, \nabla_p H(q^{j},p^{j}) \\
p^{j+1} &= p^{j} - {\Delta t}\, \nabla_q H(q^{j+1},p^{j+1})
\end{align*}`{=tex} ou bien `\begin{align*}
q^{j+1} &= q^{j} + {\Delta t}\, \nabla_p H(q^{j+1},p^{j+1}) \\
p^{j+1} &= p^{j} - {\Delta t}\, \nabla_q H(q^{j},p^j)
\end{align*}`{=tex} pour ${\Delta t}$ suffisamment petit.
:::
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

[^2]: Pour obtenir l'hamiltonien, on commence par définir le lagrangien
    $L(t,q,\dot{q})$, puis la quantité de mouvement
    $p = \nabla_{\dot{q}} L(t,q,\dot{q})$, et enfin l'hamiltonien
    $H(t,q,p)$ est obtenu par transformée de Legendre. Notons que dans
    ce cas général où $H$ peut dépendre explicitement du temps (par
    exemple si de l'énergie est injectée ou prélevée par une action
    extérieure au système), on a
    $\frac{d}{dt}H(t,q(t),p(t)) = \nabla_t H(t,q(t),p(t))$, donc
    l'hamiltonien varie selon cet effet extérieur, et n'est plus
    constant.

[^3]: L'application des lois de Newton donnerait directement $$
    m_i a_i = m_i \ddot{q_i} =  \sum_{k\neq i} F_k = -G \sum_{k\neq i} \frac{m_i m_j}{\|q_i-q_k\|^2}\frac{(q_i-q_k)}{\|q_i-q_k\|}
    $$ où $F_k$ sont les forces de gravitation exercées par chaque corps
    $k$ sur le corps $i$.
