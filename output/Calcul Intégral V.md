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
title: Calcul Intégral V
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

-   [Dérivées faibles](#dérivées-faibles)
    -   [Fonctions localement absolument
        intégrables](#fonctions-localement-absolument-intégrables)
    -   [Les fonctions faiblement dérivables sont
        continues.](#les-fonctions-faiblement-dérivables-sont-continues.)
    -   [Dérivée faible et classique](#dérivée-faible-et-classique)
    -   [Attention !](#attention)
    -   [Fonction de répartition et densité de
        probabilité](#fonction-de-répartition-et-densité-de-probabilité)
    -   [Fonctions tests](#fonctions-tests)
    -   [Dérivation faible et fonctions tests](#dfft)
-   [Mesures signées et dérivées](#mesures-signées-et-dérivées)
    -   [Formes linéaires continues sur
        $D^0(\mathbb{R})$.](#formes-linéaires-continues-sur-d0mathbbr.)
    -   [A propos du symbole $\bot$](#a-propos-du-symbole-bot)
    -   [Les mesure (positives) sont des mesures
        signées](#les-mesure-positives-sont-des-mesures-signées)
    -   [Les mesures de Dirac sont de
        Radon](#les-mesures-de-dirac-sont-de-radon)
    -   [Les fonctions ordinaires sont (identifiables à) des mesures de
        Radon](#les-fonctions-ordinaires-sont-identifiables-à-des-mesures-de-radon)
    -   [Formule des sauts](#formule-des-sauts)
    -   [Démonstration](#démonstration-7)
    -   [Théorème de représentation de
        Riesz](#théorème-de-représentation-de-riesz)
    -   [Fonction de répartition](#fonction-de-répartition)
-   [Tribus engendrées](#tribus-engendrées)
    -   [Fonction
        $\mathcal{A}/\mathcal{B}$-mesurable](#fonction-mathcalamathcalb-mesurable)
    -   [$\mathcal{A}$-mesurable équivaut à
        $\mathcal{A}/\mathcal{B}(Y)$-mesurable.](#mathcala-mesurable-équivaut-à-mathcalamathcalby-mesurable.)
    -   [Fonction boréliennes](#fonction-boréliennes)
    -   [Les fonctions continues sont
        boréliennes](#les-fonctions-continues-sont-boréliennes)
-   [Produit de mesures](#produit-de-mesures)
    -   [Tribu produit](#tribu-produit)
    -   [Produit des tribus de Borel](#produit-des-tribus-de-borel)
    -   [Produit et tribu de Lebesgue](#produit-et-tribu-de-lebesgue)
    -   [Mesure produit](#mesure-produit)
    -   [Mesure extérieure produit](#mesure-extérieure-produit)
    -   [Intégrale dans un espace
        produit](#intégrale-dans-un-espace-produit)
    -   [Mesures finies et
        $\sigma$-finie](#mesures-finies-et-sigma-finie)
    -   [Exercice -- Mesure de
        Borel-Lebesgue](#exercice-mesure-de-borel-lebesgue)
    -   [Mesure de Borel-Lebesgue](#mesure-de-borel-lebesgue)
    -   [Symétrie](#symétrie)
-   [Exercices corrigés](#exercices-corrigés)
    -   [Tribu engendrée](#tribu-engendrée)
-   [Solutions](#solutions)
    -   [Tribu engendrée](#tribu-engendrée-1)
-   [Références](#références)

```{=tex}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\P}{\mathbb{P}}
\newcommand{\Esp}{\mathbb{E}}
\newcommand{\A}{\mathcal{A}}
\newcommand{\B}{\mathcal{B}}
\renewcommand{\C}{\mathbb{C}}
\renewcommand{\L}{\mathcal{L}}
\newcommand{\V}{\mathbb{V}}
```
::: {.section}
Dérivées faibles
================

Nous généralisons dans cette section la notion classique de dérivée de
fonction, pour répondre aux besoins de disciplines variées : les
probabilités, les équations différentielles (et aux dérivées
partielles), le traitement du signal, etc.

Dans un premier temps, nous nous intéressons au cas où une fonction
ordinaire joue effectivement le rôle de la dérivée mais sans en être une
stricto sensu. L'exemple basique serait la "solution"
$x: \mathbb{R}\to \mathbb{R}$, "initialement au repos" ($x(t)=0$ pour
$t \leq 0$) de l'équation différentielle $$
\dot{x}(t) = e(t), \, t \in \mathbb{R}
$$ où $e(t)$ est l'échelon unitaire (ou fonction d'Heaviside), défini
par $$
e(t) = 1_{\left[0, +\infty\right[} = \left|
\begin{array}{rl}
0 &\mbox{si $t<0$,} \\
1 & \mbox{si $t\geq 0$.}
\end{array}
\right.
$$ Cette équation peut être considérée par exemple comme un modèle
simpliste de l'évolution de la température $x$ en fonction du temps $t$
d'un système thermique que l'on décide de chauffer (avec un flux de
chaleur constant) à partir de $t=0$.

![](images/step.py.pdf)\

La "solution" physiquement raisonnable $x(t) = t e(t)$ n'est toutefois
pas dérivable classiquement pour $t=0$ et il est nécessaire d'invoquer
un "principe de continuité" pour "recoller" les deux fragments de
solutions de l'équation différentielle pour $t<0$ et $t>0$. Nous
pourrons bientôt adopter un discours plus clair et à l'issue de cette
section, énoncer que la fonction $x: t \mapsto te(t)$ a pour *dérivée
faible* la fonction $e: t \mapsto e(t)$ sur tout $\mathbb{R}$. Dans ce
cadre, la continuité de $x$ résultera du cadre mathématique adopté
plutôt que de devoir être rajoutée comme une hypothèse supplémentaire.

::: {.section}
### Fonctions localement absolument intégrables

Une fonction $f: \mathbb{R}\to \mathbb{R}$ est *localement absolument
intégrable* (ou *ordinaire*) si elle est absolument intégrable au sens
de Henstock-Kurzweil sur tout intervalle compact $[a, b]$ : $$
\int_a^b f(t) \, dt \in \mathbb{R}\; \mbox{ et } \; \int_a^b |f(t)| \, dt \in \mathbb{R}_+.
$$
:::

::: {.section}
Compte tenu des liens entre intégrale de Henstock-Kurzweil et de
Lebesgue, si $\ell$ désigne la mesure de Lebesgue sur $\mathbb{R}$, cela
équivaut à dire que $f$ est $\ell$-intégrable sur tout intervalle
compact $[a, b]$ : $$
\int_{[a, b]} f(t) \, \ell(dt)=
\int 1_{[a, b]} f \, \ell \in \mathbb{R}.
$$
:::

::: {.section}
### Définition -- Dérivée faible {#dérivée-faible .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Dérivée faible}`{=latex}

La fonction $f:\mathbb{R}\to \mathbb{R}$ est *dérivable faiblement* s'il
existe une fonction $g:\mathbb{R}\to \mathbb{R}$ localement absolument
intégrable et une constante $c \in \mathbb{R}$ telles que pour tout
$x \in \mathbb{R}$, $$
f(x) = c + \int_0^x g(t) \, dt.
$$ La fonction $g$ est alors appelée *dérivée faible* de $f$.
:::

::: {.section}
### Les fonctions faiblement dérivables sont continues.
:::

::: {.section}
En particulier, une fonction faiblement dérivable est nécessairement
localement absolument intégrable.
:::

::: {.section}
#### Démonstration {#démonstration .proof}

La continuité des intégrales indéterminées, de la forme $$
x \in \mathbb{R}\mapsto \int_a^x h(t) \, dt
$$ est prouvée dans le chapitre "Calcul Intégral I" au moyen du lemme de
Henstock, sous l'hypothèse que $h$ est intégrable (pour un réel étendu
$a$ arbitraire). Or pour tout $r>0$, la fonction $h = g 1_{[-r,r]}$ est
intégrable. Comme pour tout $x \in \left]-r, r\right[$, $$
\int_0^x g(t) \, dt = \int_0^x h(t) \, dt,
$$ l'intégrale indéterminée de $g$, et donc $f$, est continue en $x$. Le
choix de $r$ étant arbitraire, $f$ est continue sur $\mathbb{R}$ tout
entier.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Dérivée faible et classique

Si une fonction $f: \mathbb{R}\to \mathbb{R}$ est faiblement dérivable,
de dérivée faible $g$, alors elle est dérivable (classiquement) presque
partout et $f' = g$ presque partout. On a donc pour tout
$x \in \mathbb{R}$, $$
f(x) = f(0) + \int_0^x f'(t) \, dt.
$$
:::

::: {.section}
En particulier, la dérivée faible d'une fonction, si elle existe, est
unique presque partout.
:::

::: {.section}
#### Démonstration {#démonstration-1 .proof}

Une conséquence directe du résultat de [dérivation des intégrales
indéterminées de "Calcul Intégral
II"](Calcul%20Intégral%20II.pdf/#DII).`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Exemple -- Valeur absolue {#example-abs .example .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Valeur absolue}`{=latex}

La fonction valeur absolue $|\cdot|: x \in \mathbb{R}\mapsto |x|$ est
faiblement dérivable. En effet, elle est dérivable presque partout (sauf
en $0$), sa dérivée classique valant $1$ quand $x>0$ et $-1$ quand
$x < 0$. Ses seules dérivées faibles potentielles sont dont les
fonctions égales presque partout à la fonction signe $$
\mbox{sgn}(x) := \left| 
\begin{array}{rl}
-1 & \mbox{si $x<0$,} \\
0 & \mbox{si $x=0$,} \\
+1 & \mbox{si $x>0$.}
\end{array}
\right.
$$ De plus, pour tout $x\geq 0$ on a bien $$
|x| = x = \int_0^x dt = 0 + \int_0^x \mbox{sgn}(t) \, dt
$$ et pour $x < 0$, $$
|x| = -x = \int_0^x - dt = 0 + \int_0^x \mbox{sgn}(t) \, dt.
$$ La fonction $|\cdot|$ est bien faiblement dérivable, de dérivée
faible la fonction $\mbox{sgn}$.

![](images/abs.py.pdf) 

On peut remarquer que la fonction signe n'est pas elle-même faiblement
dérivable. Elle est bien dérivable presque partout (sauf en $0$) ; sa
dérivée est nulle presque partout. Si elle était faiblement dérivable,
on aurait donc pour tout $x \in \mathbb{R}$, $$
\mbox{sgn}(x) = \mbox{sgn}(0) + \int_0^x 0 \, dt = 0,
$$ ce qui n'est pas le cas. Alternativement, on peut aussi remarquer
qu'elle n'est pas continue et par conséquent qu'elle ne peut pas être
faiblement dérivable.
:::

::: {.section}
### Attention ! {#attention .post}

Une fonction peut également être dérivable en tout point de $\mathbb{R}$
mais de dérivée non localement absolument intégrable, auquel cas elle
n'est pas faiblement dérivable[^2]. Ainsi, la fonction
$f:\mathbb{R}\to \mathbb{R}$ définie par $$
f(x) = \left|
\begin{array}{cl}
x^2 \sin 1/x^2 & \mbox{si $x\geq 0$,} \\
0 & \mbox{sinon.}
\end{array}
\right.
$$ est dérivable en tout point (et donc continue), mais sa dérivée n'est
que conditionnellement intégrable sur $[0, 1]$ par exemple, et donc elle
n'est pas localement absolument intégrable (cf. [Calcul Intégral
II](Calcul%20Intégral%20II.pdf)).
:::

::: {.section}
### Théorème -- Fonctions continûment différentiables par morceaux {#fonctions-continûment-différentiables-par-morceaux .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Fonctions continûment différentiables par morceaux}`{=latex}

Toute fonction $f: \mathbb{R}\to \mathbb{R}$ continue et continûment
dérivable par morceaux est faiblement dérivable.
:::

::: {.section}
A noter que l'on peut être continûment différentiable par morceaux mais
pas continue ; dans ce cas on ne peut pas être faiblement dérivable. La
fonction signe est un bon exemple de fonction continûment dérivable par
morceaux mais qui n'est pas continue (et donc pas faiblement dérivable).
:::

::: {.section}
#### Démonstration {#démonstration-2 .proof}

Notons $f(b^-)$ et $f(a^+)$ les limites à gauche de $f$ en $b$ et à
droite de $f$ en $a$ respectivement. Remarquons tout d'abord que si la
fonction $f$ est continûment dérivable sur $\left]a, b\right[$ et que sa
dérivée y est prolongeable par continuité sur $[a, b]$, alors on peut
prolonger la restriction de $f$ à $\left]a, b\right[$ en une fonction
(continûment) dérivable sur $\mathbb{R}$. L'application du théorème
fondamental du calcul fournit alors $$
f(b^-) - f(a^+) 
= 
\int_{a}^{b} f'(x) \, dx.
$$

Supposons désormais que $\mathbb{R}$ soit recouvert par des intervalles
$[a_k, b_k]$ sans chevauchement, indexés par des entiers relatifs $k$
consécutifs ordonnés de façon croissante et que sur chaque
$\left]a_k, b_k\right[$ la fonction $f$ soit continûment dérivable, avec
une dérivée ayant un prolongement par continuité à $[a_k, b_k]$.

On déduit de l'énoncé précédent que $$
\int_{a_k}^{b_k} f'(x) \, dx = f(b^-) - f(a^+) = f(b) - f(a)
$$ et si $a_k < x < b_k$, $$
f(x) - f(a) = f(x) - f(a^+) = \int_a^x f'(t) \, dt
$$ et $$
f(x) - f(b) = - (f(b^-) - f(x)) = - \int_x^b f'(t) \, dt = \int_b^x f'(t) \, dt.
$$ Si $x$ est réel positif, que $0 \in [a_i, b_i]$ et que
$x \in [a_j, b_j]$, on a donc $$
\begin{split}
f(x) - f(0) &= (f(x) - f(a_j)) + (f(b_{j-1}) - f(a_{j-1})) + \dots + (f(a_i) - f(0)) \\
& = \int^x_{a_j} f'(t) \, dt + \int_{a_{j-1}}^{b_{j-1}} f'(t) \, dt + \dots + \int_0^{a_i} f'(t) \, dt.
\end{split} 
$$ et donc $$
f(x) = f(0) + \int_0^x f'(t) \, dt.
$$ Le cas d'un réel $x$ négatif se traite de façon
similaire.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Fonction de répartition et densité de probabilité

La fonction $F: \mathbb{R}\to \mathbb{R}$ définie par $$
F(x) = \int_{-\infty}^x \frac{\exp (-{t^2}/{2})}{\sqrt{2\pi}} \, dt
$$ est une fonction de répartition, associée à la loi normale centrée
réduite. Elle est faiblement dérivable ; en effet, son intégrande est
localement absolument intégrable (il est positif et intégrable sur
$\mathbb{R}$, d'intégrale $1$) et l'on a par additivité de l'intégrale
pour tout $x\in\mathbb{R}$ $$
F(x) = F(0) + \int_{0}^x \frac{\exp (-{t^2}/{2})}{\sqrt{2\pi}} \, dt.
$$ Cett relation montre également que la fonction $$
f : t \in \mathbb{R}\mapsto  \frac{\exp (-{t^2}/{2})}{\sqrt{2\pi}}
$$ est une dérivée faible de $F$.

![skdjslkdjs](images/gauss.py.pdf) 
:::

::: {.section}
#### Exercice -- Exercice -- Loi de probabilité uniforme {#exercice-loi-de-probabilité-uniforme .exercise .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Exercice -- Loi de probabilité uniforme}`{=latex}

Montrer que la fonction de répartion $F$ associée la loi de probabilité
uniforme sur $[0, 1]$, définie par $$
F(x) = \left|
\begin{array}{rl}
0 & \mbox{si $x < 0$,} \\
x & \mbox{si $0 \leq x < 1$,} \\
1 & \mbox{si $1 \leq x$.} \\
\end{array}
\right.
$$ est faiblement dérivable et calculer (presque partout) sa dérivée
faible.
:::

::: {.section}
Plus généralement, on a :
:::

::: {.section}
### Proposition -- Densité et dérivée faible {#densité-et-dérivée-faible .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Densité et dérivée faible}`{=latex}

Une fonction de répartition $F:\mathbb{R}\to \mathbb{R}$ admet une
densité si et seulement si elle est faiblement dérivable. Une fonction
$f:\mathbb{R}\to \mathbb{R}$ est une densité associée à $F$ si et
seulement si elle est une dérivée faible de $F$ (elle est donc
déterminée uniquement presque partout par $F$).
:::

::: {.section}
#### Démonstration {#démonstration-3 .proof}

Sachant qu'une densité est localement absolument intégrable (car
positive et intégrable), la preuve qu'une fonction de répartition
admettant une densité est faiblement dérivable et que les deux fonctions
coïncident résulte directement de l'égalité $$
F(x) = \int_{-\infty}^x f(t) \,dt = \int_{-\infty}^0 f(t)\, dt + \int_0^x f(t) \, dt.
$$

Réciproquement, si $F$ est une fonction de répartition faiblement
dérivable, c'est-à-dire s'il existe une fonction
$f:\mathbb{R}\to \mathbb{R}$ localement absolument intégrable et une
constante $c$ telle que pour tout $x\in\mathbb{R}$, $$
F(x) = c + \int_0^x f(t) \, dt,
$$ alors pour toute paire de réels $a \leq b$, on a $$
F(b) - F(a) = \int_a^b f(t) \, dt.
$$ La fonction $f$ est donc positive presque partout : en effet la
fonction $F$ est dérivable en presque tout point $x \in \mathbb{R}$, de
dérivée $f(x)$. Si l'on avait $f(x) < 0$, alors pour $h>0$ suffisamment
petit, on aurait donc $$
\frac{F(x+h) - F(x)}{h} < 0,
$$ ce qui contredirait le fait que $F$ est croissante. On obtient alors
la relation $$
F(x) = \int_{-\infty}^x f(t) \, dt
$$ en posant $x=b$ et en passant à la limite $a \to -\infty$ en
exploitant le fait que $F$ a pour limite $0$ en $-\infty$ ; le résultat
est justifié par le théorème de convergence monotone.

Le passage à la limite $x \to +\infty$ fournit alors $$
\int_{-\infty}^{+\infty} f(t) \, dt = 1,
$$ à nouveau justifié par application du théorème de convergence
monotone, en exploitant le fait que $F$ a pour limite $1$ en
$+\infty$.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
Il existe une façon alternative pour caractériser les fonctions
faiblement dérivables qui repose sur l'usage de fonctions tests. Cette
nouvelle approche se prêtera mieux à la généralisation encore plus
"aggressive" de la notion de dérivée que nous allons aborder où les
dérivées ne seront plus nécessairement des fonctions "ordinaires", mais
des fonctions "généralisées".
:::

::: {.section}
### Fonctions tests

On note $D^k(\mathbb{R})$ l'espace des fonctions continues
$\varphi: \mathbb{R}\to \mathbb{R}$ dont le support
$$\mbox{supp } \varphi := \overline{\{x \in \mathbb{R}\; | \; \varphi(x) \neq 0\}}$$
est compact et qui sont continues si $k=0$ ou $k$ fois continûment
différentiables quand $k \geq 1$.
:::

::: {.section}
### Dérivation faible et fonctions tests {#dfft}

Une fonction localement absolument intégrable
$f:\mathbb{R}\to \mathbb{R}$ est faiblement dérivable de dérivée faible
la fonction localement absolument intégrable
$g : \mathbb{R}\to \mathbb{R}$ si et seulement si pour tout
$\varphi \in D^1(\mathbb{R})$, on a $$
\int_{-\infty}^{+\infty} g(t) \varphi(t) \, dt
=
-\int_{-\infty}^{+\infty} f(t) \varphi'(t) \, dt.
$$
:::

::: {.section}
#### Démonstration {#démonstration-4 .proof}

Nous admettrons la démonstration dans le cas général et nous limitons à
la preuve du cas des fonctions $f$ et $g$ continûment différentiables
par morceaux. Dans ce cadre, une fonction est faiblement dérivable si et
seulement si elle continue.

Supposons que cela soit le cas pour la fonction $f$. Alors, si
$\varphi \in D^1(\mathbb{R})$, le produit $f \varphi$ est continûment
différentiable par morceaux et continu, de dérivée classique presque
partout égale à $f' \varphi + f \varphi'$. Les deux termes de cette
somme sont intégrables. De plus, pour $r>0$ assez grand et $|t| \geq r$,
on a $\varphi(t) = 0$, donc $$
\int_{-\infty}^{+\infty} f'(t) \varphi(t) \, dt 
+ \int_{-\infty}^{+\infty} f(t) \varphi'(t) \, dt
=
\int_{-r}^{+r} (f \varphi)'(t) \, dt
= 
[f \varphi]^{+r}_{-r} = 0.
$$ Réciproquement, supposons que $f$ et $g$ soient continûment
différentiables et vérifient pour toute fonction
$\varphi \in D^1(\mathbb{R})$ l'égalité $$
\int_{-\infty}^{+\infty} g(t) \varphi(t) \, dt
=
-\int_{-\infty}^{+\infty} f(t) \varphi'(t) \, dt.
$$ Soit $x>0$. Pour $0 < \varepsilon < x/2$, on définit la fonction
$\psi_{\varepsilon} : \mathbb{R}\to \mathbb{R}$ par $$
\psi_{\varepsilon}(t) =
\left| 
\begin{array}{rl}
-6 / \varepsilon^3  \times t  (t - \varepsilon) & \mbox{si $0 \leq t \leq \varepsilon$,} \\
6 / \varepsilon^3  \times (t - x + \varepsilon)  (t - x) & \mbox{si $x - \varepsilon \leq t \leq x$,} \\
0 & \mbox{sinon.}
\end{array}
\right.
$$ puis $\varphi_{\varepsilon} : \mathbb{R}\to \mathbb{R}$ par $$
\varphi_{\varepsilon}(t) = \int_{-\infty}^t \psi_{\varepsilon}(s) \, ds.
$$

![Représentation de $\varphi_{\varepsilon}$ de sa dérivée quand $x=1$ et
$\varepsilon=0.2$.](images/test-function.py.pdf)

On vérifiera que les fonctions $\psi_{\varepsilon}$ ainsi construites
appartiennent bien à $D^1(\mathbb{R})$. Lorsque l'on fait tendre
$\varepsilon$ vers $0$, le théorème de convergence dominée nous fournit
$$
\int_{-\infty}^{+\infty} g(t) \varphi_{\varepsilon}(t) \, dt
\to \int_{-\infty}^{+\infty} g(t) 1_{[0, x]}(t) \, dt
=
\int_0^{x} g(t) \, dt.
$$ D'autre part, on a `\begin{multline*}
-\int_{-\infty}^{+\infty} f(t) \varphi'_{\varepsilon}(t) \, dt
= \\
\frac{6}{\varepsilon^3}
\left[\int_{0}^{\varepsilon} f(t) t  (t - \varepsilon) \, dt 
- \int_{x -\varepsilon}^x f(t) (t - x + \varepsilon)  (t - x) \, dt\right].
\end{multline*}`{=tex} Le changement de variable $s = t / \varepsilon$
nous fournit $$
\frac{6}{\varepsilon^3}
\int_{0}^{\varepsilon} f(t) t  (t - \varepsilon) \, dt
=
6
\int_{0}^{1} f(\varepsilon s) s (s - 1) \, ds
$$ et donc par le théorème de convergence dominée, en faisant tendre
$\varepsilon$ vers $0$, $$
\frac{6}{\varepsilon^3}
\int_{0}^{\varepsilon} f(t) t  (t - \varepsilon) \, dt 
\to f(0^+) \times \left(6 \int_0^1 s(s-1) \, ds\right) = - f(0^+).
$$ En analysant de façon similaire le second terme, on aboutit à $$
-\int_{-\infty}^{+\infty} f(t) \varphi'_{\varepsilon}(t) \, dt
\to 
f(x^-) - f(0^+),
$$ et donc $$
f(x^-) = f(0^+) + \int_0^x g(t) \, dt.
$$ Le second membre étant continu par rapport à $x$ et $f$ supposée
continue par morceaux, elle est en fait continue et $f(x) = f(x^-)$. Le
cas $x<0$ se traite de façon similaire. La fonction $f$ admet donc $g$
comme dérivée faible.`\hfill$\blacksquare$`{=latex}
:::
:::

::: {.section}
Mesures signées et dérivées
===========================

::: {.section}
Aller plus loin dans la dérivation des fonctions -- pouvoir dériver des
fonctions discontinues par exemple -- suppose d'accepter que des
dérivées ne soient pas des fonctions ordinaires, mais des fonctions
*généralisées*. Nous montrerons dans cette section comment des
opérateurs linéaires agissant sur des fonctions tests peuvent remplir ce
rôle et établiront le lien entre ces opérateurs et les mesures signées.
:::

::: {.section}
### Formes linéaires continues sur $D^0(\mathbb{R})$.

On dira qu'une application linéaire $T: D^0(\mathbb{R}) \to \mathbb{R}$
-- c'est-à-dire une *forme linéaire* sur $D^0(\mathbb{R})$ -- est
*continue* si pour tout intervalle compact $[a, b]$ de $\mathbb{R}$ il
existe une constante $K$ telle que pour toute fonction
$\varphi \in D^0(\mathbb{R})$ dont le support soit inclus dans $[a, b]$,
on ait $$
|T \cdot \varphi| \leq K \sup_{x \in \mathbb{R}} |\varphi(x)|
$$
:::

::: {.section}
### Théorème -- Cas des fonctions ordinaires {#cas-des-fonctions-ordinaires .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Cas des fonctions ordinaires}`{=latex}

Si $f:\mathbb{R}\to \mathbb{R}$ est localement absolument intégrable,
l'opérateur $$
T[f] : \varphi \in D^0(\mathbb{R}) \mapsto \int_{-\infty}^{+\infty} f(t) \varphi(t) \, dt 
$$ est linéaire continu. De plus, si $g :\mathbb{R}\to \mathbb{R}$ est
localement absolument intégrable, $T[f] = T[g]$ si et seulement si $f=g$
presque partout.
:::

::: {.section}
#### Démonstration {#démonstration-5 .proof}

La fonction $f$ est localement intégrable donc mesurable et la fonction
$\varphi$ est continue donc mesurable. Le produit $f \varphi$ est donc
mesurable. Soit $[a, b]$ un intervalle compact contenant le support de
$\varphi$ et $M$ un majorant de $|\varphi|$ sur ce compact. Alors le
produit $|f \varphi|$ est dominé par la fonction $|f|M 1_{[a, b]}$ qui
est intégrable ; le produit $f \varphi$ est donc absolument intégrable
et par l'inégalité triangulaire, $$
\left|\int_{-\infty}^{+\infty} f(t) \varphi(t) \, dt\right|
\leq 
\left(\int_{-\infty}^{+\infty} |f(t)| \, dt\right) \sup_{x \in \mathbb{R}} |\varphi(x)|.
$$ L'opérateur $T[f]$ est donc continu. Par ailleurs, la linéarité de
$f \mapsto T[f]$ résulte de la linéarité de l'intégrale.

La fonction $$
\int_{-\infty}^x f(t) \,dt
$$ est dérivable presque partout, de dérivée $f(x)$. En tout point $x$
de ce type on a donc $$
f(x) = \lim_{h \to 0} \frac{1}{h} \int_x^{x+h} f(t) \, dt.
$$ Or, on peut construire une famille de fonction
$\varphi_{h, \varepsilon} \in D^1(\mathbb{R})$, de support inclus dans
$[x, x+h]$, vérifiant pour tout $t \in [x, x+h]$,
$0 \leq \varphi_{h,\varepsilon}(t) \leq 1$ et telle que $$
\lim_{\varepsilon \to 0} \varphi_{h, \varepsilon} = 1_{\left]x, x+h\right[}.
$$ (on pourra s'inspirer des fonctions tests utilisées dans la
démonstration de ["Dérivation faible et fonctions tests" (p.
`\pageref*{dfft}`{=tex})](#dfft)). Par le théorème de convergence
dominée, on a donc pour presque tout $x$ $$
\begin{split}
f(x) &= \lim_{h \to 0} \frac{1}{h} \int_x^{x+h} f(t) \, dt \\
&= \lim_{h \to 0} \lim_{\varepsilon \to 0}\frac{1}{h} \int_{-\infty}^{+\infty} f(t) \varphi_{h, \varepsilon}(t) \, dt \\
&= 
\lim_{h \to 0} \lim_{\varepsilon \to 0}\frac{1}{h} T[f] \cdot \varphi_{h, \varepsilon}.
\end{split}
$$ La fonction $f$ est donc déterminée uniquement presque partout par la
donnée de $T[f]$.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Définition -- Mesure signée {#mesure-signée .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Mesure signée}`{=latex}

Soit $(X, \mathcal{A})$ un ensemble mesurable. Une *mesure signée* $\nu$
sur $(X, \mathcal{A})$ est une application $$
\nu : \mathcal{A} \to \mathbb{R}\cup \{\bot\}
$$ pour laquelle il existe une mesure
$\mu : \mathcal{A} \to [0, +\infty]$ et une application $\mu$-mesurable
$\sigma: X \to \{-1, +1\}$ telles que pour tout $A \in \mathcal{A}$, $$
\nu(A) := \sigma \mu(A) := \left|
\begin{array}{rl}
\displaystyle \int_A \sigma(x) \, \mu(dx) = \int 1_A \sigma \, \mu & \mbox{si $1_A \sigma$ est $\mu$-intégrable,} \\
\bot & \mbox{sinon.}
\end{array}
\right.
$$
:::

::: {.section}
### A propos du symbole $\bot$ {#a-propos-du-symbole-bot .post}

Le symbole $\bot$ peut être interprété comme "valeur réelle indéfinie"
ou plus simplement "indéfini"[^3]. Dans les calculs, on conviendra que
toute opération impliquant $\bot$ a pour résultat $\bot$ ; par exemple
$\bot$ est absorbant pour l'addition, c'est-à-dire que pour tout $x$
réel ou indéfini, $$
x+ \bot = \bot + x = \bot.
$$ Dans ce contexte, on considérera également que les séries sans
limites dans $\mathbb{R}$ ont pour limite $\bot$. Le symbole $\bot$ joue
un rôle très similaire à celui que joue $+\infty$ dans le cas des
calculs impliquant des nombres positifs.
:::

::: {.section}
### Les mesure (positives) sont des mesures signées

Toute mesure classique (dans le contexte des mesures signées, en cas
d'ambiguité, on parlera de mesure *positive* pour les désigner)
$\mu: \mathcal{A} \to [0, +\infty]$ peut être "convertie" en mesure
signée $\nu$ : il suffit de lui associer la mesure $\mu$ et la fonction
de signe $\sigma$ constante égale à $+1$. On a alors $$
\nu(A) = \left|
\begin{array}{rl}
\mu(A) & \mbox{si $\mu(A) < +\infty$,} \\
\bot & \mbox{si $\mu(A) = +\infty$.}
\end{array}
\right.
$$ L'identification inverse est possible si $\nu$ ne prend que des
valeurs positives ou indéfinies, en convertissant les valeurs indéfinies
en $+\infty$.
:::

::: {.section}
#### Exercice -- Exercice -- Une mesure signée {#exercice-une-mesure-signée .exercise .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Exercice -- Une mesure signée}`{=latex}

Soit $\ell$ la mesure de Lebesgue dans $\mathbb{R}$. Montrer que la
fonction qui a un ensemble $A$ de $\mathcal{L}(\mathbb{R})$ associe $$
\mu(A) = \ell|_{\mathbb{R}_+} (A) - \ell|_{\mathbb{R}_-}(A)  =\ell(\left[0, +\infty\right[\cap A) - \ell(\left]-\infty, 0\right]\cap A)
$$ est une mesure signée.
:::

::: {.section}
#### Exercice -- Exercice -- Propriétés des mesures signées {#exercice-propriétés-des-mesures-signées .exercise .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Exercice -- Propriétés des mesures signées}`{=latex}

Les mesure signées sont-elles comme les mesures positives nulles en $0$
(telles que $\mu(\varnothing)=0$) ? Croissantes (telles que
$\mu(A) \leq \mu(B)$ quand $A \subset B$) ?
:::

::: {.section}
Contrairement aux mesures positives, les combinaisons linéaires à
coefficients réels (et pas seulement positifs) de mesures signées sont
des mesures signées. On peut ainsi par exemple combiner des mesures de
Dirac positives $\delta_x$ et construire la mesure
$\mu = \delta_0 - 1/2 \times \delta_1$, qui associe à l'ensemble
$A \subset \mathbb{R}$ la quantité $$
\mu(A) = (\delta_0 - 1/2 \times \delta_1)(A) = 1_A(0) - 1/2 \times 1_A(1).
$$

![Les combinaisons linéaires de Dirac sont souvent représentées comme
des "pics" surmontés d'un triangle ou d'un rond. La mesure de Dirac
$\alpha \delta_x$ est représentée par un pic à l'abscisse $x$ et de
hauteur $\alpha$ (positive ou negative).](images/dirac.py.pdf)
:::

::: {.section}
### Définition -- Intégrale associée à une mesure signée {#intégrale-associée-à-une-mesure-signée .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Intégrale associée à une mesure signée}`{=latex}

Soit $\nu = \sigma \mu$ une mesure signée sur $(X, \mathcal{A})$. La
fonction $\mathcal{A}$-mesurable $f: \mathbb{R}\to [-\infty, +\infty]$
est dite *$\nu$-intégrable* si la fonction $f$ (ou $f\sigma$) est
$\mu$-intégrable. L'intégrale de $f$ par rapport à $\nu$ est alors
définie comme $$
\int f \nu = \int_X f(x) \, \nu(dx) := \int f \sigma \, \mu \in \mathbb{R}.
$$
:::

::: {.section}
### Définition -- Mesures de Radon {#mesures-de-radon .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Mesures de Radon}`{=latex}

Une mesure signée $\mu$ sur $(\mathbb{R}, \mathcal{A})$ est une *mesure
de Radon* si pour tout fonction $\varphi \in D^0(\mathbb{R})$,
l'intégrale $$
T[\mu] \cdot \varphi := \int \varphi \, \mu 
$$ est bien définie et que l'opérateur
$T[\mu] : D^0(\mathbb{R}) \to \mathbb{R}$ est linéaire continu.
:::

::: {.section}
### Proposition -- La mesure de Lebesgue est de Radon {#la-mesure-de-lebesgue-est-de-radon .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{La mesure de Lebesgue est de Radon}`{=latex}
:::

::: {.section}
#### Démonstration {#démonstration-6 .proof}

Soit $[a, b]$ un intervalle compact de $\mathbb{R}$. Pour tout
$\varphi \in D^0(\mathbb{R})$ dont le support est inclus dans $[a, b]$,
$\varphi$ est mesurable et bornée par la fonction
$(\sup_{x\in \mathbb{R}} |\varphi(x)|) 1_{[a, b]}$, donc
$\ell$-intégrable. $$
|T \cdot \varphi| = \left|\int_{a}^b \varphi \, \ell \right| 
\leq \int_a^b |\varphi| \ell \leq \sup_{x\in \mathbb{R}} |\varphi(x)| \int_a^b \ell
= (b-a) \sup_{x\in \mathbb{R}} |\varphi(x)|.
$$`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Les mesures de Dirac sont de Radon

La mesure (positive) $\delta_x$ de Dirac en $x \in \mathbb{R}$ est une
mesure de Radon. En effet, toute fonction $f :\mathbb{R}\to\mathbb{R}$
est intégrable pour la mesure de Dirac, d'intégrale $$
\int f \, \delta_x  = f(x).
$$ En particulier, si $\varphi \in D^1(\mathbb{R})$, $\varphi$ est
$\delta_x$-intégrable et de plus $$
|T[\delta_x] \cdot \varphi| = |\varphi(x)| \leq \sup_{x \in \mathbb{R}} |\varphi(x)|.
$$ L'opérateur $T[\delta_x]$ est donc continu.
:::

::: {.section}
#### Exercice -- Exercice -- Peigne de Dirac {#exercice-peigne-de-dirac .exercise .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Exercice -- Peigne de Dirac}`{=latex}

Soit $c_k$, une famille de réels indexés par $k \in \mathbb{Z}$. Montrer
que la mesure signée $\mu = \sum_{k \in \mathbb{Z}} c_k \delta_k$ est de
Radon.
:::

::: {.section}
#### Exercice -- Exercice -- Mesure de comptage {#exercice-mesure-de-comptage .exercise .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Exercice -- Mesure de comptage}`{=latex}

La mesure de comptage $c$ est-elle une mesure de Radon ?
:::

::: {.section}
### Les fonctions ordinaires sont (identifiables à) des mesures de Radon

Soit $f:\mathbb{R}\to \mathbb{R}$ une fonction localement absolument
intégrable. Alors si $\ell$ désigne la mesure de Lebesgue sur
$\mathbb{R}$, la mesure signée $f \ell$, telle que pour tout
$A \in \mathcal{L}(\mathbb{R})$, $$
f\ell(A) := \left|
\begin{array}{rl}
\displaystyle \int 1_A f \, \ell = \int 1_A(x) f(x) \, dx & \mbox{si $1_A f$ est $\ell$-intégrable,} \\
\bot & \mbox{sinon.}
\end{array}
\right.
$$ est une mesure de Radon.
:::

::: {.section}
Ce résultat nous permet d'identifier implicitement une fonction
ordinaire $f$ à la mesure de Radon $f \ell$, notamment quand des calculs
impliquant fonctions et mesures rendront cette démarche nécessaire.
:::

::: {.section}
#### Exercice -- Exercice -- Somme de fonction et de mesure {#exercice-somme-de-fonction-et-de-mesure .exercise .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Exercice -- Somme de fonction et de mesure}`{=latex}

Comment interpréter $\mu = 1_{[0, 1]} - \delta_1$ comme une mesure de
Radon ? Calculer $\mu([0, 1/2])$, $\mu([1/2, 1])$ et $\mu([1, 3/2])$.

![Une représentation d'une mesure signée combinant fonction ordinaire
$f$ (identifiée à la mesure $f\ell$ ou $\ell$ est la mesure de Lebesgue)
et mesure de Dirac. La partie fonction est représentée par le graphique
habituel et la partie Dirac par les pics déjà
décrits.](images/dirac2.py.pdf)
:::

::: {.section}
### Définition -- Dérivée mesure {#dérivée-mesure .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Dérivée mesure}`{=latex}

Une fonction $f: \mathbb{R}\to \mathbb{R}$ localement absolument
intégrable admet comme dérivée la mesure de Radon $\mu$ si pour toute
fonction test $\varphi \in D^1(\mathbb{R})$ on a $$
\int_{-\infty}^{+\infty} f(t) \varphi'(t) \, dt
= 
- \int_{-\infty}^{+\infty}\varphi(t) \, \mu(dt).
$$
:::

::: {.section}
#### Exercice -- Exercice -- Dérivée de l'échelon unitaire {#exercice-dérivée-de-léchelon-unitaire .exercise .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Exercice -- Dérivée de l'échelon unitaire}`{=latex}

Montrer que l'échelon unitaire $e = 1_{\left[0, +\infty\right[}$ admet
pour dérivée la mesure de Dirac $\delta_0$.
:::

::: {.section}
On remarque que si $f$ admet $g$ comme dérivée faible alors $$
\begin{split}
\int_{-\infty}^{+\infty} f(t) \varphi'(t) \, dt
&= 
- \int _{-\infty}^{+\infty} g(t) \varphi(t) \, dt \\
&=
- \int _{-\infty}^{+\infty} g(t) \varphi(t)  \, \ell(dt) \\
&= -\int_{-\infty}^{+\infty}\varphi(t) \, g \ell(dt). 
\end{split}
$$ donc $f$ admet $g\ell$ comme dérivée mesure : la convention que nous
avons choisie pour identifier fonctions ordinaires et mesures de Radon
est telle que la notion de dérivée mesure étende celle de dérivée
faible.
:::

::: {.section}
### Formule des sauts

Soit $f:\mathbb{R}\to \mathbb{R}$ une fonction continûment
différentiable par morceaux. Soit $S$ l'ensemble (dénombrable) des
points de discontinuité de $f$ et $$
\sigma(x) := f(x_+) - f(x_-) = \lim_{y \to x_+} f(y) - \lim_{y \to x_-} f(y)
$$ le *saut de $f$ en $x$*. Si l'on désigne par $f'_{\rm pp}$ une
fonction ordinaire égale à la dérivée classique de $f$ presque partout,
alors $f$ admet comme dérivée mesure la somme $$
f'_{\rm pp} + \sum_{x \in S} \sigma(x) \delta_{x}.
$$
:::

::: {.section}
### Démonstration

Soit $\varphi \in D^1(\mathbb{R})$ et $[a, b]$ un intervalle compact
contenant le support de $\varphi$. Soient $x_j, x_{j+1}, \dots, x_{j+n}$
ceux des $x_k$ qui appartiennent à $[a, b]$ (ils sont nécessairement en
nombre fini). Alors on a $$
\begin{split}
\int_{-\infty}^{+\infty} f(t) \varphi'(t) \, dt
&=
\int_a^{x_j} f(t) \varphi'(t)\, dt
+
\sum_{i=0}^{n-1} \int_{x_{j+i}}^{x_{j+i+1}} f(t) \varphi'(t)\, dt
+
\int_{x_{j+n}}^{b} f(t) \varphi'(t)\, dt \\
\end{split}
$$ et donc par intégration par parties, en utilisant sur chaque segment
le prolongement continument différentiable de $f$ : $$
\begin{split}
\int_{-\infty}^{+\infty} f(t) \varphi'(t) \, dt
&=
- \int_a^{x_j} f'(t)\varphi(t) \, dt
+[f\varphi]_a^{x_j^-} \\
&\phantom{=} -
\sum_{i=0}^{n-1} \int_{x_{j+i}}^{x_{j+i+1}} f'(t) \varphi(t)\, dt
+ [f \varphi]_{x_{j+i}^+}^{x_{i+j+1}^-} \\
&\phantom{=} -
\int_{x_j}^{b} f'(t)\varphi(t) \, dt
+[f\varphi]_{x_j^+}^{b}
\end{split}
$$ et par conséquent $$
\begin{split}
\int_{-\infty}^{+\infty} f(t) \varphi'(t) \, dt
&=
- \int_{a}^b f'(t)\varphi(t) \, dt  \\
&\phantom{=} + f(x_j^-)\varphi(x_j) - f(x_j^+)\varphi(x_j) + \cdots \\
&\phantom{=} + f(x_{j+n}^-)\varphi(x_{j+n}) - f(x_{j+n}^+)\varphi(x_{j+n}).
\end{split}
$$ Il suffit alors de constater que $$
(f(x_{j+i}^-) - f(x_{j+i}^+)) \varphi(x_{j+i})
= -\sigma({x_{j+i}}) \varphi(x_{j+i})
= - \sigma({x_{j+i}}) \int \varphi \, \delta_{x_{j+i}}
$$ pour conclure.
:::

::: {.section}
#### Exercice -- Exercice -- Fonction signe {#exercice-fonction-signe .exercise .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Exercice -- Fonction signe}`{=latex}

Déterminer la dérivée mesure de la fonction signe.
:::

::: {.section}
#### Exercice -- Exercice -- Escalier {#exercice-escalier .exercise .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Exercice -- Escalier}`{=latex}

Déterminer la dérivée mesure de la fonction partie entière.
:::

::: {.section}
#### Exercice -- Exercice -- "Primitive" {#exercice-primitive .exercise .unnumbered .unlisted}

```\addcontentsline{toc}{paragraph}{Exercice -- ``Primitive''}```{=latex}

Trouver une fonction continument dérivable par morceaux $f$ dont la
dérivée mesure soit $\mu = 1_{[0, 1]} - \delta_1$.

------------------------------------------------------------------------
:::

::: {.section}
### Définition -- Fonction à variation bornée {#fonction-à-variation-bornée .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Fonction à variation bornée}`{=latex}

Une fonction $f:[a, b] \subset \mathbb{R}\to \mathbb{R}$ est à
*variation bornée* s'il existe un réel $M > 0$ tel que pour tout
$n \in \mathbb{N}^*$ et tout $n+1$-uplet
$a \leq x_0 \leq \dots \leq x_n \leq b$, $$
\sum_{i=0}^{n-1} |f(x_{i+1}) - f(x_i)| \leq M.
$$ Le plus petit $M$ qui convienne est la *variation de $f$ sur
$[a, b]$*. Une fonction $f:\mathbb{R}\to \mathbb{R}$ est *localement à
variation bornée* si sa restriction à tout intervalle compact $[a, b]$ à
variation bornée.
:::

::: {.section}
Nous admettrons le résultat suivant :
:::

::: {.section}
### Théorème de représentation de Riesz

Une fonction ordinaire $f:\mathbb{R}\to \mathbb{R}$ a une dérivée mesure
si et seulement elle est égale presque partout à une fonction localement
à variation bornée.
:::

::: {.section}
### Fonction de répartition

Une fonction de répartition $F:\mathbb{R}\to \mathbb{R}$ a une dérivée
mesure $\mathbb{P}$ qui vérifie
$$\forall a\leq b \in \mathbb{R}, \, F(b) - F(a)= \mathbb{P}(\left]a, b\right]).$$
:::

::: {.section}
#### Démonstration {#démonstration-8 .proof}

La fonction de répartition $F$ est croissante ; par conséquent, si
$a \leq x_0 \leq \dots \leq x_n \leq b$ $$
\sum_{i=0}^{n-1} |F(x_{i+1}) - F(x_i)| = \sum_{i=0}^{n-1} (F(x_{i+1}) - F(x_i))
= F(b) - F(a).
$$ La fonction $F$ est donc localement à variation bornée ; elle a donc
une dérivée mesure $\mu$, qui satisfait pour tout
$\varphi \in D^1(\mathbb{R})$ $$
- \int_{-\infty}^{+\infty} F(t) \varphi'(t) \, dt
= 
\int _{-\infty}^{+\infty}\varphi(t) \, \mu(dt).
$$ De façon similaire à la démonstration de ["Dérivation faible et
fonctions tests" (p. `\pageref*{dfft}`{=tex})](#dfft) introduisons pour
tout intervalle compact $[a, b]$ et pour $\varepsilon>0$ suffisamment
petit les fonctions $\psi_{\varepsilon} : \mathbb{R}\to \mathbb{R}$
définies par $$
\psi_{\varepsilon}(t) =
\left| 
\begin{array}{rl}
-6 / \varepsilon^3  \times (t - a)  (t - a - \varepsilon) & \mbox{si $a \leq t \leq a+\varepsilon$,} \\
6 / \varepsilon^3  \times (t - b + \varepsilon)  (t - b) & \mbox{si $b - \varepsilon \leq t \leq b$,} \\
0 & \mbox{sinon.}
\end{array}
\right.
$$ puis $\varphi_{\varepsilon} \in D^1(\mathbb{R})$ par $$
\varphi_{\varepsilon}(t) = \int_{-\infty}^t \psi_{\varepsilon}(s) \, ds.
$$ Comme dans la démonstration de ["Dérivation faible et fonctions
tests" (p. `\pageref*{dfft}`{=tex})](#dfft), en utilisant un changement
de variable et le théorème de convergence dominée, on établit que quand
$\varepsilon \to 0$, $$
-\int_{-\infty}^{+\infty} F(t) \varphi_{\varepsilon}'(t) \, dt
\to F(b^-) - F(a^+).
$$ Par ailleurs, quand $\varepsilon \to 0$, les fonctions
$\varphi_{\varepsilon}$ convergent simplement vers
$1_{\left]a, b\right[}$. Notons $\mu = \sigma \nu$ ou $\nu$ est positive
et $\sigma$ est la fonction de signe associée. Comme les fonctions
$\varphi_{\varepsilon}$ peuvent être encadrées par une fonction
$\nu$-intégrable -- toute fonction positive de $D^1(\mathbb{R})$ valant
plus que $1$ sur $[a, b]$ -- par le théorème de convergence dominée on
obtient $$
\int _{-\infty}^{+\infty}\varphi_{\varepsilon}(t) \, \mu(dt) 
\to \int _{-\infty}^{+\infty} 1_{\left]a, b\right[}(t) \, \mu(dt)
= \mu(\left]a, b\right[).
$$ En considérant des intervalles de la forme
$\left]a, b\right] \subset \left]a, c\right[$ et en faisant tendre $c$
vers $b^+$, on a d'une part $$
F(c^-) - F(a^+) \to F(b^+) - F(a^+)
$$ et d'autre part $$
\mu(\left]a, c\right[) = \int 1_{\left]a, c\right[} \mu \to \int 1_{\left]a, b\right]} \mu
= \mu(\left]a, b\right])
$$ par le théorème de convergence dominée. On en déduit, comme $F$ est
continue à droite, que $F(b) - F(a) = \mu(\left]a, b\right])$ comme
désiré.`\hfill$\blacksquare$`{=latex}
:::
:::

::: {.section}
Tribus engendrées
=================

::: {.section}
### Définition -- Tribu engendrée par une collection {#tribu-engendrée-par-une-collection .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Tribu engendrée par une collection}`{=latex}

Dans un ensemble $X$, on appelle *tribu engendrée* par une collection
$\mathcal{B}$ d'ensembles de $X$ la plus petite tribu (au sens de
l'inclusion) $\mathcal{A} = \sigma(\mathcal{B})$ de $X$ contenant
$\mathcal{C}$. Autrement dit :

-   $\sigma(\mathcal{B})$ est une tribu.

-   si $\mathcal{B} \subset \mathcal{C}$ et $\mathcal{C}$ est une tribu
    de $X$, alors $\sigma(\mathcal{B}) \subset \mathcal{C}$.

Quand il y a une ambiguité sur l'ensemble $X$ hébergeant la collection
$\mathcal{B}$, on pourra noter la tribu engendrée
$\sigma_X(\mathcal{B})$.
:::

::: {.section}
#### Démonstration (existence de la tribu engendrée) {#démonstration-existence-de-la-tribu-engendrée .proof}

Désignons par $\mathfrak{S}$ la collection des tribus de contenant
$\mathcal{B}$ comme sous-ensemble. $$
\mathfrak{S}
=
\{
\mbox{$\mathcal{C}$ tribu de $X$} \; | \; \mathcal{B} \subset \mathcal{C} 
\}
$$ Elle n'est pas vide : elle contient la collection $\mathcal{P}(X)$
des ensembles de $X$ (qui de toute évidence est un sur-ensemble de
$\mathcal{B}$ et une tribu de $X$). Montrons que la plus petite tribu
$\sigma(\mathcal{B})$ de $X$ contenant $\mathcal{B}$ est l'intersection
de toutes les tribus de $\mathfrak{S}$, c'est-à-dire que
$$\sigma(\mathcal{B}) = \bigcap_{\mathcal{C} \in \mathfrak{S}} \mathcal{C} 
= \{A \subset X \, | \, A \in \mathcal{C} \mbox{ pour tout } \mathcal{C} \in \mathfrak{S}\}.$$
Il est clair que si $\mathcal{A}$ est une tribu de $X$ contenant
$\mathcal{B}$, alors
$\cap_{\mathcal{C} \in \mathfrak{S}} \mathcal{C} \subset \mathcal{A}$,
car $\mathcal{A} \in \mathfrak{S}$. Il nous suffit donc de montrer que
$\cap \mathfrak{S}$ est une tribu de $X$ pour pouvoir conclure. Or

-   pour tout $\mathcal{C} \in \mathfrak{S}$,
    $\varnothing \in \mathcal{C}$, donc
    $\varnothing \in \cap_{\mathcal{C} \in \mathfrak{S}} \mathcal{C}$ ;

-   si $A \in \cap_{\mathcal{C} \in \mathfrak{S}} \mathcal{C}$, alors
    pour tout $\mathcal{C} \in \mathfrak{S}$, $A \in \mathcal{C}$, donc
    $X \setminus A \in \mathcal{C}$ et par conséquent
    $X \setminus A \in \cap_{\mathcal{C} \in \mathfrak{S}} \mathcal{C}$ ;

-   si pour tout $k \in \mathbb{N}$,
    $A_k \in \cap_{\mathcal{C} \in \mathfrak{S}} \mathcal{C}$, alors
    pour tout $\mathcal{C} \in \mathfrak{S}$, $A_k \in \mathcal{C}$,
    donc $\cup_{k=0}^{+\infty} A_k \in \mathcal{C}$ et par conséquent
    $\cup_{k=0}^{+\infty} A_k \in \cap_{\mathcal{C} \in \mathfrak{S}} \mathcal{C}$.

$\;\; \blacksquare$
:::

::: {.section}
#### Exercice -- Exercice -- Singletons de $\mathbb{N}$ {#exercice-singletons-de-mathbbn .exercise .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Exercice -- Singletons de \(\mathbb{N}\)}`{=latex}

Montrer que la collection des singletons de $\mathbb{N}$
$\{\{n\} \; | \; n \in \mathbb{N}\}$ engendre dans $\mathbb{N}$ la tribu
des parties $\mathcal{P}(\mathbb{N})$.
:::

::: {.section}
#### Exercice -- Exercice -- Tribu engendrée par une collection finie {#exercice-tribu-engendrée-par-une-collection-finie .exercise .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Exercice -- Tribu engendrée par une collection finie}`{=latex}

Montrer que si $\mathcal{B} = \{A_1, A_2\}$ où $A_1$ et $A_2$ sont des
ensembles de $X$, alors la tribu engendrée par $\mathcal{B}$ dans $X$
contient au plus 16 ensembles. Que devient le résultat quand
$\mathcal{B} = \{A_1, A_2, A_3\}$ ?
:::

::: {.section}
#### Exercice -- Exercice -- Tribu engendrée par les ensembles dénombrables {#exercice-tribu-engendrée-par-les-ensembles-dénombrables .exercise .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Exercice -- Tribu engendrée par les ensembles dénombrables}`{=latex}

Montrer que la tribu engendrée par les ensembles dénombrables de
$\mathbb{R}$ est la collection des ensembles de $\mathbb{R}$ qui sont
dénombrables ou dont le complémentaire est dénombrable.
:::

::: {.section}
#### Exercice -- Exercice -- Calculs avec les tribus engendrées {#exercice-calculs-avec-les-tribus-engendrées .exercise .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Exercice -- Calculs avec les tribus engendrées}`{=latex}

Soit $\mathcal{A}$ et $\mathcal{B}$ deux collections d'ensembles de $X$.
Montrer que $\sigma(\sigma(\mathcal{A})) = \sigma(\mathcal{A})$ et que
si $\mathcal{A} \subset \mathcal{B}$, alors
$\sigma(\mathcal{A}) \subset \sigma(\mathcal{B})$. En déduire que si
$\mathcal{A} \subset \mathcal{B} \subset \sigma(\mathcal{A})$, alors
$\sigma(\mathcal{A}) = \sigma(\mathcal{B})$.
:::

::: {.section}
### Définition -- Tribu de Borel {#tribu-de-borel .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Tribu de Borel}`{=latex}

On appelle *tribu de Borel* d'un espace topologique $X$ la tribu notée
$\mathcal{B}(X)$ engendrée par les ensembles fermés (ou les ensembles
ouverts) de $X$. Les ensembles qu'elle contient sont appelés les
*boréliens*.
:::

::: {.section}
#### Exercice -- Exercice -- Ouverts ou fermés {#exercice-ouverts-ou-fermés .exercise .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Exercice -- Ouverts ou fermés}`{=latex}

Montrer que la tribu engendrée par les ensembles ouverts de $X$ est bien
identique à la tribu engendrée par les ensembles fermés de $X$.
:::

::: {.section}
#### Exercice -- Exercice -- Tribu engendrée par les pavés compacts {#exercice-tribu-engendrée-par-les-pavés-compacts .exercise .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Exercice -- Tribu engendrée par les pavés compacts}`{=latex}

Montrer que la tribu engendrée par la collection des pavés compacts
$[a_1, b_1] \times \dots \times [a_n, b_n]$ de $\mathbb{R}^n$ est la
tribu de Borel de $\mathbb{R}^n$. (indication[^4])
:::

::: {.section}
Nous généralisons désormais la notion de fonction
$\mathcal{A}$-mesurable du chapitre précédent en tenant désormais
explicitement compte d'une tribu dans l'ensemble d'arrivée de la
fonction :
:::

::: {.section}
### Fonction $\mathcal{A}/\mathcal{B}$-mesurable

Une fonction $f: X \to Y$ associée aux espaces mesurables
$(X, \mathcal{A})$ et $(Y,\mathcal{B})$ est *mesurable* (ou
*$\mathcal{A}/\mathcal{B}$-mesurable*) si l'image réciproque
$A =f^{-1}(B)$ de tout ensemble $B$ de $\mathcal{B}$ par $f$ appartient
à $\mathcal{A}$.
:::

::: {.section}
La notions de $\mathcal{A}$-mesurabilité du chapitre précédent
correspond implicitement à la notion plus générale de mesurabilité quand
la tribu de Borel est sélectionnée sur l'espace d'arrivée :
:::

::: {.section}
### $\mathcal{A}$-mesurable équivaut à $\mathcal{A}/\mathcal{B}(Y)$-mesurable.

Soit $(X, \mathcal{A})$ un espace mesurable et $Y$ un espace
topologique. Une fonction $f: X \to Y$ est $\mathcal{A}$-mesurable -- au
sens où l'image réciproque par $f$ de tout ouvert (ou fermé) de $Y$
appartient à $\mathcal{A}$ -- si et seulement si elle est
$\mathcal{A}/\mathcal{B}(Y)$-mesurable.

La démonstration de ce résultat repose sur le lemme suivant :
:::

::: {.section}
### Lemme -- Image réciproque et tribus engendrées {#irte .lemma .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Image réciproque et tribus engendrées}`{=latex}

Soit $f : X \to Y$ une application et $\mathcal{B}$ une collection
d'ensembles de $Y$. Alors $$
\mathcal{F} := \sigma_X(\{f^{-1}(B) \; | \; B \in \mathcal{B}\}) = \{f^{-1}(A) \; | \; A \in \sigma_Y(\mathcal{B})\}.
$$

![Ce diagramme est *commutatif*.](images/commutative-diagram.tex.pdf)
:::

::: {.section}
#### Démonstration {#démonstration-9 .proof}

Notons $\mathcal{A} = \sigma(\mathcal{B})$. Comme
$\mathcal{B} \subset \mathcal{A}$, on a $$
\{f^{-1}(B) \, | \, B \in \mathcal{B}\} \subset
\{f^{-1}(A) \, | \, A \in \mathcal{A}\}.
$$ Si nous montrons que
$\mathcal{C}:=\{f^{-1}(A) \, | \, A \in \mathcal{A}\}$ est une tribu
nous pouvons en déduire que $$
 \sigma(\{f^{-1}(B) \; | \; B \in \mathcal{B}\}) \subset \{f^{-1}(A) \; | \; A \in \mathcal{A}\}.
$$ L'ensemble vide appartient à $\mathcal{C}$ car
$\varnothing = f^{-1}(\varnothing)$. Si $A \in \mathcal{A}$,
$X \setminus f^{-1}(A) = f^{-1}(Y \setminus A)$ et
$Y \setminus A \in \mathcal{A}$, donc
$X \setminus f^{-1}(A) \in \mathcal{C}$. Finalement, si
$A_0, A_1, \dots \in \mathcal{A}$,
$\cup_k f^{-1}(A_k) = f^{-1}(\cup_k A_k) \in \mathcal{C}$. La collection
$\mathcal{C}$ est donc une tribu.

Réciproquement, posons
$\mathcal{E} = \sigma(\{f^{-1}(B) \; | \; B \in \mathcal{B}\})$ et
considérons $$
\mathcal{D} = \{A \in Y \; | \; f^{-1}(A) \in \mathcal{E}\}.
$$ La collection $\mathcal{D}$ est également une tribu. En effet,
$f^{-1}(\varnothing) \in \mathcal{E}$, si $f^{-1}(A) \in \mathcal{E}$
alors $f^{-1}(Y \setminus A) = X \setminus f^{-1}(A) \in \mathcal{E}$ et
si $f^{-1}(A_0), f^{-1}(A_1), \dots \in \mathcal{E}$, alors
$f^{-1}(\cup_k A_k) = \cup_k f^{-1}(A_k) \in \mathcal{E}$. Par
conséquent, comme $\mathcal{B} \subset \mathcal{D}$,
$\mathcal{A} = \sigma(\mathcal{B}) \subset \sigma(\mathcal{D}) = \mathcal{D}$.
Donc pour tout $A \in \mathcal{A}$, on a $f^{-1}(A) \in \mathcal{E}$,
soit $$
\{f^{-1}(A) \; | \; A \in \mathcal{A}\} \subset \mathcal{E}  =\sigma(\{f^{-1}(B) \; | \; B \in \mathcal{B}\}).
$$`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Démonstration "$\mathcal{A}$-mesurable $\leftrightarrow$ $\mathcal{A}/\mathcal{B}(Y)$-mesurable" {#démonstration-mathcala-mesurable-leftrightarrow-mathcalamathcalby-mesurable .proof}

De toute évidence, si $f$ est $\mathcal{A}/\mathcal{B}(Y)$-mesurable,
comme tout ouvert appartient à la tribu de Borel, l'image réciproque par
$f$ de tout ouvert de $Y$ appartient bien à $\mathcal{A}$ donc $f$ est
$\mathcal{A}$-mesurable.

Réciproquement, si l'image réciproque de tout ouvert de $Y$ est
$\mathcal{A}$-mesurable, alors la tribu engendrée par les images
réciproques des ouverts de $Y$ est incluse dans $\mathcal{A}$. Comme
cette tribu est d'après [le lemme précédent (p.
`\pageref*{irte}`{=tex})](#irte) l'ensemble des images réciproques par
$f$ de la tribu engendrée par les ouverts dans $Y$, c'est-à-dire la
tribu de Borel dans $Y$, l'image réciproque de tout borélien est un
ensemble de $\mathcal{A}$ : la fonction $f$ est
$\mathcal{A}/\mathcal{B}(Y)$-mesurable.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Proposition -- Composition de fonctions mesurables {#compfoncmes .proposition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Composition de fonctions mesurables}`{=latex}

Soient $(X, \mathcal{A})$, $(Y, \mathcal{B})$ et $(Z, \mathcal{C})$ des
espaces mesurables. Soit $f: X\to Y$ une fonction
$\mathcal{A}/\mathcal{B}$-mesurable et $g: Y \to X$ une fonction
$\mathcal{B}/\mathcal{C}$-mesurable. Alors la composition $g \circ f$ de
$f$ et $g$ est $\mathcal{A}/\mathcal{C}$-mesurable.
:::

::: {.section}
#### Démonstration {#démonstration-10 .proof}

Pour tout ensemble $C \in \mathcal{C}$, on a $g^{-1}(C) \in \mathcal{B}$
et donc
$(g \circ f)^{-1}(C) = f^{-1}(g^{-1}(C)) \in \mathcal{A}$.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
### Fonction boréliennes

Soit $X$ et $Y$ deux espaces topologiques. Une fonction $f : X \to Y$
est *borélienne* si elle est $\mathcal{B}(X)/\mathcal{B}(Y)$-mesurable.
:::

::: {.section}
### Les fonctions continues sont boréliennes

Soient $X$ et $Y$ deux espaces topologiques. Toute fonction continue
$f : X \to Y$ est borélienne.
:::

::: {.section}
#### Démonstration {#démonstration-11 .proof}

Notons $\mathcal{F}_X$ et $\mathcal{F}_Y$ les collections de tous les
ensembles fermés de $X$ et $Y$ respectivement. Comme les boréliens de
$Y$ sont engendrés par les fermés de $\mathcal{F}_Y$, on a $$
\{f^{-1}(A) \; | \; A \in \mathcal{B}(Y)\} = \{f^{-1}(A) \; | \; A \in \sigma_Y(\mathcal{F}_Y)\}
$$ et par conséquent, par [commutativité (p.
`\pageref*{irte}`{=tex})](#irte), $$
\{f^{-1}(A) \; | \; A \in \mathcal{B}(Y)\} = \sigma_X (\{f^{-1}(A) \; | \; A \in \mathcal{F}_Y\}).
$$ Or la fonction $f$ étant continue,
$\{f^{-1}(A) \; | \; A \in \mathcal{F}_Y\} \subset \mathcal{F}_X$ et par
conséquent $$
\sigma_X(\{f^{-1}(A) \; | \; A \in \mathcal{F}_Y\}) \subset \sigma_X(\mathcal{F}_X) = \mathcal{B}(X).
$$ Au final,
$\{f^{-1}(A) \; | \; A \in \mathcal{B}(Y)\} \subset \mathcal{B}(X)$ et
la fonction $f$ est bien $\mathcal{B}(X)/\mathcal{B}(Y)$-mesurable,
c'est-à-dire borélienne.`\hfill$\blacksquare$`{=latex}
:::

::: {.section}
#### Exercice -- Exercice -- Fonctions croissantes {#exercice-fonctions-croissantes .exercise .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Exercice -- Fonctions croissantes}`{=latex}

Soit $f: \mathbb{R}\to \mathbb{R}$ ; montrer que si l'image réciproque
par $f$ de tout intervalle compact est un intervalle compact alors $f$
est borélienne. En déduire que si $f$ est croissante alors $f$ est
borélienne.
:::
:::

::: {.section}
Produit de mesures
==================

Dans cette section, nous affirmons sans preuve quelques résultats
fondamentaux associés aux produits de mesures et aux intégrales
associées. Le lecteur cherchant plus d'informations sur ce volet -- dont
les démonstrations sont techniques -- pourra consulter @Hun11 ou @Tao11.

::: {.section}
### Tribu produit

Soit $(X ,\mathcal{A})$ et $(Y, \mathcal{B})$ deux espaces mesurables.
On appelle *tribu produit* de $\mathcal{A}$ et $\mathcal{B}$ et l'on
note $\mathcal{A} \otimes \mathcal{B}$ la tribu sur le produit cartésien
$X \times Y$ engendrée par les ensembles de la forme $A \times B$ où
$A \in \mathcal{A}$ et $B \in \mathcal{B}$. $$
\mathcal{A} \otimes \mathcal{B} := 
\sigma_{X \times Y}
\left( 
\left\{ A \times B \; | \; A \in \mathcal{A}, \; B \in \mathcal{B} \right\}
\right).
$$ L'espace mesurable $(X \times Y, \mathcal{A} \otimes \mathcal{B})$
est appelé *espace produit* des espaces mesurables $(X, \mathcal{A})$ et
$(Y, \mathcal{B})$.
:::

::: {.section}
#### Exercice -- Exercice -- Produit d'ensemble de parties {#exercice-produit-densemble-de-parties .exercise .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Exercice -- Produit d'ensemble de parties}`{=latex}

Montrer que
$\mathcal{P}(\mathbb{N}) \otimes \mathcal{P}(\mathbb{N}) = \mathcal{P}(\mathbb{N}\times \mathbb{N})$
(attention : [le résultat n'est pas vrai si l'on remplace $\mathbb{N}$
par un ensemble $X$ "trop
grand" !](https://math.stackexchange.com/questions/3029309/product-sigma-algebra-of-power-sets)).
:::

::: {.section}
### Produit des tribus de Borel

La tribu de Borel sur $\mathbb{R}^{m+n}$ est le produit des tribus de
Borel sur $\mathbb{R}^m$ et $\mathbb{R}^n$ : $$
\mathcal{B}(\mathbb{R}^{m+n}) = \mathcal{B}(\mathbb{R}^{m}) \otimes \mathcal{B}(\mathbb{R}^{n}).
$$
:::

::: {.section}
### Produit et tribu de Lebesgue

Notons que le résultat similaire est faux pour la mesure de Lebesgue :
$$
  \mathcal{L}(\mathbb{R}^{m+n}) \neq \mathcal{L}(\mathbb{R}^{m}) \otimes \mathcal{L}(\mathbb{R}^{n}).
  $$ Pour obtenir $\mathcal{L}(\mathbb{R}^{m+n})$, il est nécessaire de
compléter la tribu produit
$\mathcal{L}(\mathbb{R}^m) \otimes \mathcal{L}(\mathbb{R}^n)$ par
rapport à la mesure de Lebesgue sur $\mathbb{R}^{m+n}$, c'est-à-dire de
rajouter les ensembles négligeables pour la tribu de Lebesgue à la
collection, puis de construire la tribu engendrée (cf. [exercice
"Complétion d'une mesure" du chapitre
IV](Calcul%20Intégral%20IV.pdf#complétion)).
:::

::: {.section}
Pour pallier cette difficulté technique, une autre option consiste à
systématiquement restreindre les mesures que l'on considère aux
boréliens.
:::

::: {.section}
### Définition -- Mesure de Borel {#mesure-de-borel .definition .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Mesure de Borel}`{=latex}

On appelle *mesure de Borel* sur un espace topologique $X$ toute mesure
définie sur la tribu des boréliens $\mathcal{B}(X)$.
:::

::: {.section}
A toute mesure $\mu$ définie sur une tribu $\mathcal{A}$ de $X$
contenant $\mathcal{B}(X)$ on peut associer une tribu de Borel $\nu$ en
restreignant $\mu$ à $\mathcal{B}(X)$. $$
\nu :\mathcal{B}(X) \to [0, +\infty] \; \mbox{ et } \; \forall A \in \mathcal{B}(X), \, \nu(A) := \mu(A).
$$ En particulier on appelle *mesure de Borel-Lebesgue sur
$\mathbb{R}^n$* la restriction de la mesure de Lebesgue de
$\mathcal{L}(\mathbb{R}^n)$ à $\mathcal{B}(\mathbb{R}^n)$.
:::

::: {.section}
#### Exercice -- Exercice -- Mesures de Borel classiques {#exercice-mesures-de-borel-classiques .exercise .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Exercice -- Mesures de Borel classiques}`{=latex}

Peut-on associer une mesure de Borel à une mesure de Dirac $\delta_x$
sur $\mathbb{R}^n$ ? A la mesure de comptage sur $\mathbb{R}^n$ ?
:::

::: {.section}
#### Exercice -- Exercice -- Mesure de Borel ? {#exercice-mesure-de-borel .exercise .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Exercice -- Mesure de Borel ?}`{=latex}

Soit $\mathcal{A} = \{\varnothing, \mathbb{R}\}$ et
$\mu: \mathcal{A} \to [0, +\infty]$ définie par $\mu(\varnothing)=0$ et
$\mu(\mathbb{R}) = 1$. Montrer que $\mu$ est une mesure sur
$(\mathbb{R}, \mathcal{A})$ ; peut-on lui associer une mesure de Borel
sur $\mathbb{R}$ ?
:::

::: {.section}
### Mesure produit

Soient $(X, \mathcal{A}, \mu)$ et $(Y, \mathcal{B}, \nu)$ deux espaces
mesurés. On appelle *mesure produit* de $\mu$ et $\nu$ et l'on note
$\mu \otimes \nu$ la mesure définie sur
$\mathcal{A} \otimes \mathcal{B}$ par $$
(\mu \otimes \nu) (C) = \inf
\left\{ 
\sum_{k=0}^{+\infty} \mu(A_k) \nu(B_k) 
\; \left| \vphantom{\sum_{k=0}^{+\infty}} \right. \;
A_k \in \mathcal{A}, \ B_k \in \mathcal{B}, \, C \subset \bigcup_{k=0}^{+\infty} A_k \times B_k \right\}.
$$ L'espace mesuré
$(X \times Y, \mathcal{A} \otimes \mathcal{B}, \mu \otimes \nu)$ est
appelé *espace produit* des espaces mesurés $(X, \mathcal{A}, \mu)$ et
$(Y, \mathcal{B}, \nu)$.
:::

::: {.section}
#### Exercice -- Exercice -- Produit de Diracs {#exercice-produit-de-diracs .exercise .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Exercice -- Produit de Diracs}`{=latex}

Soit $m, n \in \mathbb{N}$ et $\delta_m, \delta_n$ les mesures de Dirac
associées sur $\mathbb{N}$. Montrer que
$\delta_m \otimes \delta_n = \delta_{(m, n)}$, c'est-à-dire que pour
tout $C \in \mathbb{N}^2$, $$
\delta_{(m, n)} (C) = \left|
\begin{array}{rl}
1 & \mbox{si $(m, n) \in C$,} \\
0 & \mbox{sinon.}
\end{array}
\right.
$$
:::

::: {.section}
#### Exercice -- Exercice -- Produit de mesures de comptage {#exercice-produit-de-mesures-de-comptage .exercise .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Exercice -- Produit de mesures de comptage}`{=latex}

Soit $c_X$ la mesure de comptage sur $X$. Montrer que pour tout
$C \in \mathcal{P}(X) \otimes \mathcal{P}(Y)$,
$(c_X \otimes c_Y)(C) = c_{X \times Y}(C).$ (indication[^5])
:::

::: {.section}
### Mesure extérieure produit {#mesure-extérieure-produit .post}

On remarquera que l'expression ci-dessus qui définit
$(\mu \otimes \nu) (C)$ a du sens pour tout ensemble $C$ de
$\mathbb{R}^{m+n}$, pas uniquement pour les ensembles de
$\mathcal{A} \otimes \mathcal{B}$. On peut prouver sans difficulté que
cette expression définit en fait une mesure extérieure
$(\mu \otimes \nu)^*$ (un concept qui a été introduit dans l'annexe de
"Calcul Intégral IV"). Pour prouver le théorème ci-dessus il suffit
alors d'établir que tout produit $A \times B$ où $A \in \mathcal{A}$ et
$B \in \mathcal{B}$ est $(\mu \otimes \nu)^*$-mesurable.
:::

::: {.section}
### Intégrale dans un espace produit {#intégrale-dans-un-espace-produit .notation}

Soient $(X, \mathcal{A}, \mu)$ et $(Y, \mathcal{B}, \nu)$ deux espaces
mesurés. Pour toute fonction $\mu \otimes \nu$-mesurable
$f: X \times Y \to [0, +\infty]$ ou toute fonction
$\mu \otimes \nu$-intégrable $f: X \times Y \to [-\infty, +\infty]$, on
notera $$
\int_{X \times Y} f(x, y) \mu(dx)\nu(dy) := 
\int f (\mu \otimes \nu).
$$
:::

::: {.section}
### Mesures finies et $\sigma$-finie

Soit $(X, \mathcal{A}, \mu)$ un espace mesuré. La mesure $\mu$ est
*finie* si $\mu(X) < +\infty$ ; elle est *$\sigma$-finie* s'il existe
une suite d'ensembles mesurables $A_k \in \mathcal{A}$,
$k \in \mathbb{N}$, telle que $$
\bigcup_{k=0}^{+\infty} A_k = X 
\; \mbox{ et } \; 
\forall \, k \in \mathbb{N}, \, \mu(A_k) < +\infty.
$$
:::

::: {.section}
#### Exercice -- Exercice -- Mesure de probabilité {#exercice-mesure-de-probabilité .exercise .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Exercice -- Mesure de probabilité}`{=latex}

Une mesure de probabilité est-elle finie, $\sigma$-finie ?
:::

::: {.section}
#### Exercice -- Exercice -- Mesures $\sigma$-finies {#exercice-mesures-sigma-finies .exercise .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Exercice -- Mesures \(\sigma\)-finies}`{=latex}

Etudier si les mesures suivantes sur $\mathbb{R}^n$ sont ou non finies
et/ou $\sigma$-finies : les mesures de Dirac, la mesure de comptage, la
mesure de Lebesgue.
:::

::: {.section}
### Théorème -- Unicité de la mesure produit {#unicité-de-la-mesure-produit .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Unicité de la mesure produit}`{=latex}

Soit $(X, \mathcal{A}, \mu)$ et $(Y, \mathcal{B}, \nu)$ deux espace
mesurés, tels que les mesures $\mu$ et $\nu$ soient $\sigma$-finies.
Alors la mesure produit $\mu \otimes \nu$ est l'unique mesure sur
$(X \times Y, \mathcal{A} \otimes \mathcal{B})$ telle que $$
\forall A\in \mathcal{A}, \, \forall B \in \mathcal{B}, 
\, (\mu \otimes \nu) (A \times B) = \mu(A) \times \mu(B).
$$
:::

::: {.section}
### Exercice -- Mesure de Borel-Lebesgue

Soit $\ell$ la mesure de Borel-Lebesgue sur $\mathbb{R}$. Soit
$A = [-2,2] \times [-1,1] \cup [-1,1] \times [-2,2]$ ; montrer que $A$
est un borélien de $\mathbb{R}^2$ et calculer $(\ell \otimes \ell) (A)$.
:::

::: {.section}
### Mesure de Borel-Lebesgue

La mesure de Borel-Lebesgue sur $\mathbb{R}^{m+n}$ est le produit des
mesures de Borel-Lebesgue sur $\mathbb{R}^m$ et $\mathbb{R}^n$.
:::

::: {.section}
### Théorème -- Théorème de Fubini {#fubini .theorem .unnumbered .unlisted}

`\addcontentsline{toc}{subsubsection}{Théorème de Fubini}`{=latex}

Soit $(X, \mathcal{A}, \mu)$ et $(Y, \mathcal{B}, \nu)$ deux espace
mesurés, tels que les mesures $\mu$ et $\nu$ soient $\sigma$-finies. Une
fonction mesurable $f: X \times Y \to \mathbb{R}$ est intégrable si et
seulement l'intégrale itérée $$
\int_Y \left(\int_X |f(x, y)| \mu(dx) \right) \nu(dy)
$$ est finie. Dans ce cas, $$
\int f \, (\mu \otimes \nu)
=
\int_Y \left(\int_X f(x, y) \mu(dx) \right) \nu(dy).
$$
:::

::: {.section}
### Symétrie

Le rôle joué par $X$ et $Y$ étant symétrique dans l'énoncé du théorème
de Fubini, on peut également dire qu'une fonction mesurable
$f: X \times Y \to \mathbb{R}$ est intégrable si et seulement
l'intégrale itérée $$
\int_X \left(\int_Y |f(x, y)| \nu(dy) \right) \mu(dx)
$$ est finie et que dans ce cas, $$
\int f \, (\mu \otimes \nu)
=
\int_X \left(\int_Y f(x, y) \nu(dy) \right) \mu(dx).
$$
:::

::: {.section}
#### Exercice -- Exercice -- Convolution de Dirac {#exercice-convolution-de-dirac .exercise .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Exercice -- Convolution de Dirac}`{=latex}

Soit $a, b \in \mathbb{R}$ et $C \in \mathcal{B}(\mathbb{R})$. Montrer
que $$
?(C) = \int 1_C(x + y) \, \delta_a(dx) \delta_b(dy).
$$ est bien défini et calculer sa valeur. (indication[^6])
:::

::: {.section}
#### Exercice -- Exercice -- Intégrale et séries doubles {#exercice-intégrale-et-séries-doubles .exercise .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Exercice -- Intégrale et séries doubles}`{=latex}

Soit $f : \mathbb{N}\times \mathbb{N}\to \mathbb{R}$ une fonction telle
que $$
\sum_{n=0}^{+\infty} \left(\sum_{m=0}^{+\infty} |f(m, n)| \right) < +\infty.
$$ Montrer que $$
\sum_{n=0}^{+\infty} \left(\sum_{m=0}^{+\infty} f(m, n) \right)
=
\sum_{m=0}^{+\infty} \left(\sum_{n=0}^{+\infty} f(m, n) \right).
$$
:::

::: {.section}
#### Exercice -- Exercice -- Asymétrie {#exercice-asymétrie .exercise .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Exercice -- Asymétrie}`{=latex}

Soit $\ell$ la mesure de Lebesgue sur $\mathbb{R}$ et $c$ la mesure de
comptage sur $\mathbb{R}$. On note $D = \{(x, x) \; | \; x \in [0,1]\}$.
Calculer (en justifiant l'existence des termes) $$
\int \left(\int 1_D(x, y) \, \ell(dx) \right)  c(dy)
\; \mbox{ et } \;
\int \left(\int 1_D(x, y) \, c(dy) \right)  \ell(dx)
$$ et comparer ces deux valeurs. Comment expliquez-vous ce résultat ?
:::
:::

::: {.section}
Exercices corrigés
==================

::: {.section}
Dérivée faible {#dr .question .unnumbered .unlisted}
--------------

`\addcontentsline{toc}{subsection}{Dérivée faible}`{=latex}

Est-ce que la fonction $f: \mathbb{R}\to \mathbb{R}$ définie par
$f(0)=0$ et $$
f(x) = \sqrt{|x|} \, \mbox{ si $x\neq 0$}
$$ est faiblement dérivable ? Quelle est dans ce cas sa dérivée ?
([Solution p.
`\pageref*{answer-dr}`{=tex}](#answer-dr){.no-parenthesis}.)
:::

::: {.section}
Mesure signée et $\sigma$-additivité {#mssa .question .unnumbered .unlisted}
------------------------------------

`\addcontentsline{toc}{subsection}{Mesure signée et \(\sigma\)-additivité}`{=latex}

Les mesures signées sont-elles comme les mesures positives
$\sigma$-additives, c'est-à-dire telles que $$
\mu\left(\bigcup_{k=0}^{+\infty}A_k \right) = \sum_{k=0}^{+\infty} \mu(A_k)
$$ quand les $A_k$ sont disjoints ? Indication : on pourra étudier
$\mu = \ell|_{\mathbb{R}_+} - \ell_{\mathbb{R}_-}$, définie pour tout
$A \in \mathcal{L}(\mathbb{R})$ par $$
\mu(A) =
\ell(\left[0, +\infty\right[\cap A) - \ell(\left]-\infty, 0\right]\cap A)
$$ et rechercher une partition dénombrable de $\mathbb{R}$ par des $A_k$
tels que $\mu(A_k) = 0$.

Etudier à nouveau le problème sous l'hypothèse supplémentaire que
$\mu\left(\bigcup_{k=0}^{+\infty}A_k \right)$ est réel. ([Solution p.
`\pageref*{answer-mssa}`{=tex}](#answer-mssa){.no-parenthesis}.)
:::

::: {.section}
Dérivée mesure {#dm .question .unnumbered .unlisted}
--------------

`\addcontentsline{toc}{subsection}{Dérivée mesure}`{=latex}

Soit $\tau > 0$. On considère la fonction $f:\mathbb{R}\to\mathbb{R}$
qui est $\tau$-périodique et telle que $$
\forall t \in \left[0, \tau \right[, \; f(t) = \sin t.
$$

![](images/sin.py.pdf)

Montrer que $f$ admet une dérivée mesure que l'on déterminera. A quelle
condition sur $\tau$ cette mesure est-elle une fonction ordinaire (et
$f$ est-elle dérivable faiblement) ? La fonction $f$ est-elle pour
autant dérivable classiquement en tout point $t$ de $\mathbb{R}$ ?
([Solution p.
`\pageref*{answer-dm}`{=tex}](#answer-dm){.no-parenthesis}.)
:::

::: {.section}
Tribu engendrée
---------------

Une collection $\mathcal{A}$ de sous-ensembles de $X$ est une *algèbre
(d'ensembles)* si elle contient $\varnothing$ et est stable par
complémentation et par union finie.

De manière similaire au cas des tribus, pour toute collection
d'ensembles de $X$ il existe une plus petite (au sens de l'inclusion)
algèbre qui la contient : c'est *l'algèbre engendrée* par cette
collection.

::: {.section}
#### Question 1 {#te-1 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Déterminer l'algèbre engendrée sur $\mathbb{R}$ par la collection $$
\{\left[a, b\right[ \; | \; -\infty < a \leq b \leq +\infty\}
$$

([Solution p.
`\pageref*{answer-te-1}`{=tex}](#answer-te-1){.no-parenthesis}.)
:::

::: {.section}
#### Question 2 {#te-2 .question .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Déterminer la tribu engendrée (ou $\sigma$-algèbre) sur $\mathbb{R}$ par
la même collection. ([Solution p.
`\pageref*{answer-te-2}`{=tex}](#answer-te-2){.no-parenthesis}.)
:::
:::
:::

::: {.section}
Solutions
=========

::: {.section}
Dérivée faible {#answer-dr .answer .unnumbered .unlisted}
--------------

`\addcontentsline{toc}{subsection}{Dérivée faible}`{=latex}

Si $f$ admet une dérivée faible, elle est nécessairement égale presque
partout à la dérivée classique de $f$, qui vaut $$
g(x) := f'(x) = \frac{\mathrm{sgn}(x)}{2\sqrt{x}}.
$$ On peut compléter la dérivée faible potentielle $g$ en posant
$g(0)=0$. Il faut ensuite vérifier que pour tout $x \in \mathbb{R}$ on a
bien $$
f(x) = f(0) + \int_0^x g(t) \, dt.
$$ Pour $x >0$ par exemple, on peut déduire de $$
\int_{\varepsilon}^x g(t) \, dt = \int_{\varepsilon}^x \frac{dt}{2\sqrt{t}}
= \sqrt{t} - \sqrt{\varepsilon}
$$ et du théorème de convergence monotone la relation souhaitée. La
situation est similaire pour $x < 0$. La fonction $f$ initiale est donc
bien faiblement dérivable.
:::

::: {.section}
Mesure signée et $\sigma$-additivité {#answer-mssa .answer .unnumbered .unlisted}
------------------------------------

`\addcontentsline{toc}{subsection}{Mesure signée et \(\sigma\)-additivité}`{=latex}

La réponse est non, les mesures signées ne sont pas nécessairement
$\sigma$-additives. Considérons en effet
$\mu = \ell|_{\mathbb{R}_+} - \ell|_{\mathbb{R}_-}$ et les ensembles
mesurables $$
A_0 = \{0\} \, \mbox{ puis } \, A_k = \left[-k-1, -k\right[ \cup \left]k, k+1\right] \, \mbox{ pour $k\geq 1$}.
$$ Tous ces ensembles sont de mesure $\mu$ nulle et donc $$
\sum_{k=0}^{+\infty} \mu(A_k) = 0.
$$ Pourtant ils forment une partition dénombrable de $\mathbb{R}$ et
comme la fonction $\mathrm{sgn}$ n'est pas $\ell$-intégrable sur
$\mathbb{R}$, on a $$
\mu\left(\cup_{k=0}^{+\infty} A_k\right) = \mu(\mathbb{R}) = \bot.
$$

Par contre, si l'on sait que $A := \cup_{k=0}^{+\infty} A_k$ est de
mesure $\mu = \sigma \nu$ réelle, cela signifie que la fonction
caractéristique $1_A$ est $\nu$-intégrable. Les fonctions $f_j$ définies
par $$
f_j \sigma = 1_{\cup_{k=0}^j A_k} \sigma = \sum_{k=0}^j 1_{A_k} \sigma
$$ sont $\nu$-mesurables, dominées en valeur absolue par $1_A$ et
$f_j \sigma$ converge simplement vers $1_A \sigma$. On a donc par le
théorème de convergence dominée $$
\sum_{k=0}^{+\infty} \mu(A_k) = \lim_{j \to +\infty} \int f_j \sigma \, \nu
=
\int 1_A \sigma \, \nu = \mu(A).
$$
:::

::: {.section}
Dérivée mesure {#dm .answer .unnumbered .unlisted}
--------------

`\addcontentsline{toc}{subsection}{Dérivée mesure}`{=latex}

La fonction $f$ est continûment dérivable par morceaux donc elle admet
une dérivée mesure donnée par la formule des sauts, en l'occurence si
l'on nomme $g$ la fonction $\tau$-périodique telle que $$
\forall t \in \left[0, \tau \right[, \; g(t) = \cos t.
$$ alors comme les seuls sauts possibles de $f$ sont en $k\tau$ pour
$k \in \mathbb{Z}$ et valent $$
\sigma_{k\tau}  = \sin 0 - \sin \tau = \sin \tau
$$ cette dérivée mesure est $$
g + \sum_{k \in \mathbb{Z}} (\sin \tau) \delta_{k \tau}.
$$ C'est une fonction ordinaire si et seulement si $\sin \tau$ est nul,
c'est-à-dire si $\tau \in \pi \mathbb{Z}$. Mais la fonction $f$ n'est
dérivable en tout point que si $\tau \in 2\pi \mathbb{Z}$ (c'est-à-dire
si $f=\sin$).
:::

::: {.section}
Tribu engendrée
---------------

::: {.section}
#### Question 1 {#answer-te-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Si $\mathcal{A}$ est une algèbre de $X$ contenant tous les intervalles
$\left[a, b\right[$ quand $-\infty < a \leq b \leq +\infty$, alors par
complémentation de $\left[a, +\infty\right[$, elle contient
nécessairement les ensembles de la forme $\left]-\infty, a\right[$ et
donc par union finie tous les ensembles de la forme $$
\left]-\infty, a_0\right[ \cup \dots \cup \left[a_k, b_k\right[ \cup \dots \cup \left[a_m, +\infty\right[
$$ où les $a_k$ et les $b_k$ sont finis et le premier et dernier terme
de cette union peuvent être omis. On vérifiera alors que cet ensemble
est stable par union finie et par complémentation : c'est une algèbre de
$\mathbb{R}$. Par conséquent, c'est la plus petite algèbre de
$\mathbb{R}$ qui contienne la collection initiale ; c'est donc l'algèbre
engendrée recherchée.
:::

::: {.section}
#### Question 2 {#answer-te-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Si $\mathcal{A}$ est une tribu de $X$ contenant tous les intervalles
$\left[a, b\right[$ quand $-\infty < a \leq b \leq +\infty$, alors elle
contient aussi $$
\left]a, b\right[ = \bigcup_{k=0}^{+\infty} \left[a+\frac{b-a}{2^k}, b\right[
$$ et donc tout ouvert de $\mathbb{R}$ puisqu'un tel ensemble est une
réunion dénombrable d'intervalles ouverts de $\mathbb{R}$. Par
conséquent, elle contient tous les Boréliens. Comme l'ensemble des
Boréliens est une tribu de $\mathbb{R}$, c'est donc la tribu engendrée
par la collection initiale.
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

[^2]: C'est la seule obstruction possible : une fonction qui serait
    dérivable **en tout point de $\mathbb{R}$** et dont la dérivée
    classique est localement absolument intégrable est automatiquement
    faiblement dérivable [@Tao11, prop. 1.6.41, p. 176].

[^3]: concept assez similaire au "non-nombre" `nan` (*not-a-number*) des
    numériciens, que l'on obtient par exemple avec NumPy en calculant
    `inf - inf`.

[^4]: Commencer par montrer que tout ouvert de $\mathbb{R}^n$ s'écrit
    comme une union dénombrable de pavés compacts de la forme
    $[k_1/2^m, (k_1+1)/2^m] \times \dots \times [k_n/2^m, (k_n+1)/2^m]$
    où $m \in \mathbb{N}^*$ et $(k_1, \dots, k_n) \in \mathbb{Z}^n$.

[^5]: Montrer que pour tout ensemble fini $C \subset X \times Y$,
    $\sum_{(a,b) \in C} c_X(\{a\}) c(\{b\}) = \mbox{card}(C)$ ; En
    déduire que si les $A_k \times B_k$ recouvrent $C$, alors
    $\sum_{k=0}^{+\infty} c_X(A_k) c_Y(B_k) \geq \mbox{card}(C)$ et
    conclure et calculant $(c_X \otimes c_Y)(C)$ lorsque $C$ est fini
    puis infini.

[^6]: Si l'on note $C - v = \{c - v \; | \; c \in C \}$, alors on a
    $1_C(u + v) = 1_{C-v} (u)$.
