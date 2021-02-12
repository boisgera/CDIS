---
author:
- 'STEP, MINES ParisTech[^1]'
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
title: 'Examen -- Corrigé'
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
-   [Calcul Différentiel](#calcul-différentiel)
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
\renewcommand{\P}{\mathbb{P}}
\newcommand{\Esp}{\mathbb{E}}
```
```{=tex}
\newcommand{\cC}{C}
\newcommand{\cD}{\mathcal{D}}
```
::: {.section}
Calcul intégral
===============

::: {.section}
#### Question 1 {#question-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Si $\delta>0$ et $t \in [0, x_n]$,
$\gamma(t) = \left]t-\delta/2, t+\delta/2\right[$ est un intervalle
ouvert de $\mathbb{R}$ qui contient $t$. La fonction $\gamma$ est donc
une jauge sur $[0, x_n]$.
:::

::: {.section}
#### Question 2 {#question-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Le lemme de Cousin établit l'existence d'une telle jauge. Si l'on
souhaite une solution plus explicite, on peut par exemple rechercher une
telle subdivision pointée $\mathcal{D}_m$ sous la forme $$
\left\{ 
  \left(\frac{k+1/2}{m}, \left[\frac{k}{m} x_n, \frac{k+1}{m} x_n \right]\right)\; \left| \vphantom{\int}\right. k \in \{0, \dots, m-1\}\; 
  \right\}
$$ (on vérifiera qu'il s'agit bien d'une subdivision pointée de
$[0, x_n]$). Pour tout $k \in \{0, \dots, m-1\}$, on a $$
\gamma\left(\frac{k+1/2}{m}\right) 
=
\left]\frac{k+1/2}{m} - \frac{\delta}{2}, \frac{k+1/2}{m} + \frac{\delta}{2}\right[,
$$ donc si ${1}/{2m} < \delta / 2$ -- c'est-à-dire si $m>1/\delta$ -- on
a $$
\left[\frac{k}{m} x_n, \frac{k+1}{m} x_n \right] \subset \gamma\left(\frac{k+1/2}{m}\right)
$$ et $\mathcal{D}_m$ est subordonnée à $\gamma$. Il suffit donc de
choisir un entier $m$ strictement plus grand que $1/\delta$ pour que
$\mathcal{D}_m$ fournisse l'exemple de subdivision recherché.
:::

::: {.section}
#### Question 3 {#question-3 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Pour tout entier $k$, la restriction de la fonction $f$ à l'intervalle
$[x_k, x_{k+1}]$ est égale presque partout (sauf en $x_{k+1}$) à la
fonction constante égale à $1$ si $k$ est pair et $-1$ sinon ; cette
restriction est donc intégrable et de même intégrale que la constante
considérée. La fonction constante égale à $\lambda \in \{-1,1\}$ admet
comme primitive la fonction $x \mapsto \pm \lambda x$ ; par le théorème
fondamental du calcul, son intégrale sur $[x_k, x_{k+1}]$ existe et vaut
$$
\int_{x_{k}}^{x_{k+1}} f(x) \, dx = [x \mapsto x]_{x_{k}}^{x_{k+1}} = x_{k+1} - x_{k} = 
a_{k/2} \; \mbox{ si $k$ est pair}
$$ et de même $$
\int_{x_{k}}^{x_{k+1}} f(x) \, dx = [x \mapsto -x]_{x_{k}}^{x_{k+1}} = x_{k+1} - x_{k} = 
-b_{(k-1)/2} \; \mbox{ si $k$ est impair.}
$$ La fonction $f$ étant intégrable sur tous les intervalles
$[x_k, x_{k+1}]$ tels que $0 \leq k \leq n-1$, elle est intégrable sur
$[0, x_n]$ et $$
\int_0^{x_n} f(x) \, dx = \sum_{k=0}^{n-1} \int_{x_k}^{x_{k+1}} f(x) \, dx
= \sum_{k\leq (n-1)/2} a_k - \sum_{k \leq (n-2)/2} b_k.
$$
:::

::: {.section}
#### Question 4 {#question-4 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 4}`{=latex}

Soit $\mathcal{D}$ une subdivision pointé subordonnée à $\gamma$. Si
$(t, [a, b]) \in \mathcal{D}$ et l'intervalle $[a,b]$ ne contient aucun
$x_k$, alors la restriction de $f$ à $[a, b]$ est constante. On a donc
dans ce cas $$
\left|f(t) (b-a) - \int_a^b f(x) \, dx\right| = 0.
$$ En général, on note que $|f|$ est constante et égale à $1$ sur
$[0, x_n]$. Par conséquent, pour tout $(t, [a, b]) \in \mathcal{D}$,
$$|f(t)(b-a)| \leq |f(t)| |b-a| = (b-a)$$ et $$
\left|\int_a^b f(x) \, dx \right| \leq \int_a^b |f(x)| \, dx = (b-a),
$$ donc $$
\left|f(t)(b-a) - \int_a^b f(x) \, dx \right| \leq 2 (b-a).
$$ Il y a au plus $(n+1)$ éléments $(t, J) \in \mathcal{D}$ tels que
$\ell(J) > 0$ qui contiennent un $x_k$ avec $k \in \{0,\dots, n\}$ et
pour tous ces intervalles $J$, comme $J\subset \gamma(t)$ et que
$\ell(\gamma(t)) = \delta$, on a $\ell(J) \leq \delta$. Par conséquent,
$$
\begin{split}
\left|S(f, \mathcal{D}) - \int_0^{x_n} f(x) \, dx \right| 
&= \left|\sum_{(t,J) \in \mathcal{D}} f(t) \ell(J) - \int_J f(x) \, dx\right| \\
&\leq \sum_{(t, J) \in \mathcal{D}} \left|f(t) \ell(J) - \int_J f(x) \, dx\right| \\
&\leq 2 (n+1) \delta.
\end{split}
$$
:::

::: {.section}
#### Question 5 {#question-5 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 5}`{=latex}

Par récurrence, on peut établir que pour tout $k \in \mathbb{N}$, on a
$x_k = 1 - 2^{-k}$. En effet, cette relation est vraie au rang $0$ ; si
elle est vraie pour $x_{2k}$ alors $$
x_{2k+1} = x_{2k} + a_k = (1-2^{-2k}) + 2^{-2k-1} = 1 - 2^{-2k}(1 - 1/2)=
1 - 2^{-2k-1}
$$ et de même, si elle est vraie pour $x_{2k+1}$ alors $$
x_{2k+2} = x_{2k+1} + b_k = (1 - 2^{-2k-1}) + 2^{-2k-2}
= 1 - 2^{-2k-1}(1 - 1/2)= 1 - 2^{-2k-2}.
$$ On a donc $S:=\lim_{k\to +\infty} 1 - 2^{-k} = 1$.
:::

::: {.section}
#### Question 6 {#question-6 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 6}`{=latex}

La fonction $f_n$ est intégrable car elle est l'extension par zéro à
$\mathbb{R}$ de la restriction de $f$ à $[0, x_n]$, dont nous savons
qu'elle est intégrable. Or $f$ est la limite simple des fonctions
$f_n$ :

-   pour tout $x \in \left[0, S\right[$, $f_n(x) = f(x)$ à partir du
    moment où $x_n > x$, ce qui finit nécessairement par arriver puisque
    $\lim_{k \to +\infty} x_k = S$.

-   pour tout $x \not \in \left[0, S\right[$, $f_n(x) = f(x) =0$ pour
    tout entier $n$.

La fonction $f$ est donc mesurable comme limite simple de fonctions
intégrables.
:::

::: {.section}
#### Question 7 {#question-7 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 7}`{=latex}

Soit $(a, b)$ une paire de réels telle que
$0 \leq a \leq b \leq +\infty$. On a $$
\left[a, b\right[ = [a, b] \setminus \{b\}.
$$ Les ensembles $[a, b]$ et $\{b\}=[b, b]$ sont (des intervalles)
fermés, donc mesurables. Le complémentaire $\left[a, b\right[$ de
$\{b\}$ dans $[a, b]$ est donc mesurable.

Si $A$ est un sous-ensemble de $\mathbb{R}$, comme
$f(\mathbb{R}) = \{-1, 0, 1\}$, on a $$
f^{-1}(A) = f^{-1}(A \cap \{-1, 0, 1\})
$$ Il suffit donc de déterminer l'image réciproque par $f$ des
sous-ensembles de $\{-1, 0, 1\}$, qui sont en nombre fini. Or pour tout
$A \subset \{-1,0,1\}$, on a $$
f^{-1}(A) = \bigcup_{a \in A} f^{-1}(a).
$$ Comme
$$E_0 := f^{-1}(0) = \left]-\infty,0\right[ \cup \left[S, +\infty\right[=
\mathbb{R}\setminus \left[0, S\right[,$$ $$
E_1 := f^{-1}(1) = \bigcup_{k=0}^{+\infty} \left[x_{2k}, x_{2k+1}\right[
\; \mbox{ et } \;
E_{-1} := f^{-1}(-1) = 
\bigcup_{k=0}^{+\infty} \left[x_{2k+1}, x_{2k+2}\right[,
$$ l'ensemble $f^{-1}(A)$ peut être égal à $\varnothing$, $E_1$,
$E_{-1}$, $E_0$, $E_1 \cup E_0$, $E_{-1} \cup E_0$ , $E_{-1}\cup E_1$
(c'est-à-dire $\left[0, S\right[$) ou bien $\mathbb{R}$.

Dans tous les cas, $f^{-1}(A)$ est un ensemble mesurable (comme union
dénombrable d'ensembles mesurables ou complémentaire d'ensemble
mesurable) et ce quel que soit l'ensemble $A$ (il n'est même pas
nécessaire de se restreindre aux ensembles ouverts ou fermés). Par le
critère de l'image réciproque, la fonction $f$ est donc mesurable.
:::

::: {.section}
#### Question 8 {#question-8 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 8}`{=latex}

Pour tout $n \in \mathbb{N}$, la fonction $f_n$ coïncide avec $f$ sur
$[0, x_n]$ et est nulle en dehors ce cet intervalle ; on a donc $$
\int_{-\infty}^{+\infty} f_n(x) \, dx = \int_{0}^{x_n} f(x) \, dx
$$

Les fonction $f_n$ sont intégrables et convergent simplement vers $f$.
On a également $-h \leq f_n \leq h$ pour tout $n \in \mathbb{N}$ où la
fonction $h:\mathbb{R}\to \mathbb{R}$ définie par $$
h(x) = \left\{
\begin{array}{rl}
1 & \mbox{si $0 \leq x < S$,} \\
0 & \mbox{sinon.}
\end{array}
\right.  
$$ est intégrable (ainsi que $-h$ par linéarité de l'intégrale). Par le
théorème de convergence dominée, $f$ est intégrable et $$
\int_{-\infty}^{+\infty} f(x) = 
\lim_{n \to +\infty} \int_0^{x_n} f(x) \, dx =
\lim_{n \to +\infty}
\sum_{k\leq (n-1)/2} a_k - \sum_{k \leq (n-2)/2} b_k.
$$ On a $$
\sum_{k=0}^p a_k = \sum_{k=0}^p 2^{-2k-1} = \frac{1}{2} \sum_{k=0}^p  \left(\frac{1}{4}\right)^k
=\frac{1}{2} \frac{1- (1/4)^{p+1}}{1 - 1/4}
$$ et $$
\sum_{k=0}^p b_k = \sum_{k=0}^p 2^{-2k-2} = \frac{1}{4} \sum_{k=0}^p  \left(\frac{1}{4}\right)^k
=\frac{1}{4} \frac{1- (1/4)^{p+1}}{1 - 1/4}
$$ Par conséquent, $$
\int_{-\infty}^{+\infty} f(x) =
\lim_{n \to +\infty}
\sum_{k\leq (n-1)/2} a_k - \sum_{k \leq (n-2)/2} b_k
=\frac{1}{2} \frac{4}{3} - \frac{1}{4}  \frac{4}{3}  =\frac{1}{3}.
$$
:::

::: {.section}
#### Question 9 {#question-9 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 9}`{=latex}

La restriction de $f$ à l'intervalle $[0, S]$ est encadrée par les
constantes $-1$ et $1$. Elle est également continue en tout point
$x \in [0, S]$ qui n'appartient pas à l'ensemble
$\{x_k \; | \; k \in \mathbb{N}\}\cup \{S\},$ ensemble qui est
dénombrable, donc négligeable ; la fonction $f$ est donc continue
presque partout. Par le critère d'intégrabilité de Lebesgue, elle est
donc Riemann-intégrable sur $[0, S]$.
:::
:::

::: {.section}
Calcul Différentiel
===================

::: {.section}
#### Question 1 {#question-1-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Si $x=(0,0)$ alors tout point de $C$ est à une distance de 1 de $x$,
donc $$
d_C(x) = 1 \qquad , \qquad \Pi_C(x) = C \ .
$$

Supposons maintenant $x\neq (0,0)$. $x=(r\cos\theta,r\sin\theta)$ avec
$r=\|x\|$ et $\theta\in[0,2\pi]$. Par ailleurs, un point $a\in C$
s'écrit $a=(\cos\rho,\sin \rho)$, $\rho\in[0,2\pi]$. On a donc
`\begin{align*}
\|x-a\|^2 &= (r\cos\theta-\cos\rho)^2 + (r\sin\theta-\sin\rho)^2 \\
&= r^2 + 1 -2r(\cos\theta-\cos\rho+\sin\theta-\sin\rho) = r^2 + 1 -2r\cos(\theta-\rho)
\end{align*}`{=tex} Donc le minimum est atteint pour
$\cos(\theta-\alpha)=1$, i.e. $\theta=\rho$. On a alors $$
\|x-a\|^2 = r^2 + 1 -2r = (r-1)^2 = (\|x\|-1)^2
$$ d'où $d_C(x)=\pm (\|x\|-1)$. De plus, le point $a\in C$ pour laquelle
cette distance est atteinte est $(\cos\theta,\sin\theta)$, i.e., $$
\Pi_C(x) = \left\{\frac{x}{\|x\|} \right\} \ .
$$
:::

::: {.section}
#### Question 2 {#question-2-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Au voisinage de $x=(0,0)$, $$
d_C(x) = 1 - \|x\| = 1- \sqrt{x_1^2+x_2^2}  \ .
$$ La dérivée partielle par rapport à $x_1$ de $d_C$ en $x=0$, si elle
existe, est donnée par $$
\lim_{t\to 0} \frac{d_C(t,0)-d_C(0,0)}{t} = 
\lim_{t\to 0} \frac{1 - |t| -1}{t}  
=\lim_{t\to 0} -\frac{|t|}{t} \ .
$$ Mais cette limite n'existe pas car $-t/|t| = -1$ pour $t>0$ et $1$
pour $t<0$. Donc $d_C$ n'est pas différentiable en 0.

Prenons maintenant $x\in C$, c'est-à-dire tel que $\|x\|=1$. L'idée est
de montrer que dans la direction donnée par le vecteur $x$, la
différentielle n'existe pas. Supposons en effet que $d_C$ est
différentiable en $x$. Alors pour tout $t\in \mathbb{R}$, $$
d_C(x+tx) = d_C(x) + dd_C(x) \cdot tx + o(|t|) = dd_C(x) \cdot tx + o(|t|) \ ,
$$ donc $$
\lim_{t\to 0} \frac{d_C(x+tx)}{t} = dd_C(x) \cdot x
$$ Mais pour $t$ petit, selon si $t>0$ ou $t<0$, $x+tx$ est à
l'intérieur du cercle ou à l'extérieur et donc puisque $\|x\|=1$, soit
$$
d_C(x+tx) = \|x+t x\| -1 = (1+t)\|x\| -1 = t
$$ soit $$
d_C(x+tx) = 1-\|x+t x\|  = 1- (1+t)\|x\| = -t.
$$ Donc ${d_C(x+tx)}/{t}$ n'admet pas de limite quand $t$ tend vers 0 et
$d_C$ n'est pas différentiable en $x$.
:::

::: {.section}
#### Question 3 {#question-3-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

De l'expression de $d_C(x)$ on déduit que pour tout
$x \in \mathbb{R}^2$, $$
f(x)=\|x\|-1 = \sqrt{x_1^2 +x_2^2}-1.
$$ Pour $(x_1,x_2)\neq (0,0)$, $f$ admet pour dérivées partielles $$
\frac{\partial f}{\partial x_1}(x_1,x_2) = \frac{x_1}{\sqrt{x_1^2 +x_2^2}} 
\quad, \quad
\frac{\partial f}{\partial x_2}(x_1,x_2) = \frac{x_2}{\sqrt{x_1^2 +x_2^2}} 
$$ qui sont continues au voisinage de $x$. Donc $f$ est continûment
différentiable sur $\mathbb{R}\setminus \{(0,0)\}$. On en déduit $$
\nabla f(x) = \left(
\begin{matrix}
\frac{x_1}{\sqrt{x_1^2 +x_2^2}}\\
\frac{x_2}{\sqrt{x_1^2 +x_2^2}}
\end{matrix}
\right)
= 
\frac{x}{\|x\|} \ .
$$ De même, $\nabla f$ est continûment différentiable sur
$\mathbb{R}\setminus \{(0,0)\}$ donc $f$ est deux fois continûment
différentiable de matrice Hessienne $$
H_f(x) = \frac{1}{\sqrt{x_1^2 +x_2^2}} \left(
  \begin{matrix}
  1- \frac{x_1^2}{x_1^2 +x_2^2} & - \frac{x_1x_2}{x_1^2 +x_2^2} \\
  -\frac{x_1x_2}{x_1^2 +x_2^2} & 1- \frac{x_2^2}{x_1^2 +x_2^2}
  \end{matrix}
\right) = \frac{1}{\|x\|^3} 
\left(
\begin{matrix}
  x_2^2 & - x_1x_2 \\
  -x_1x_2 & x_1^2
  \end{matrix}
  \right)
$$ On note que $f$ est différentiable partout sauf en $x=(0,0)$,
c'est-à-dire seulement là où $\Pi_C(x)$ est un singleton.
:::

::: {.section}
#### Question 4 {#question-4-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 4}`{=latex}

Pour tout $x\in \mathbb{R}^2$, $\|\nabla f(x) \| = 1$. Par l'inégalité
des accroissements finis, on déduit que pour tout $(x_a,x_b)$ tels que
le segment $\left[ x_a,x_b \right]\subset\mathbb{R}\setminus \{ 0 \}$,
$|f(x_a)-f(x_b)| \leq \|x_a-x_b\|$. Si maintenant
$0 \in \left[ x_a,x_b \right]$, il existe une direction
$v\in \mathbb{R}^2$ telle que $0 \notin \left[ x_a+tv,x_b +tv\right]$
pour tout $t>0$. Alors pour tout $t>0$,
$|f(x_a+tv)-f(x_b+tv)| \leq \|(x_a+tv)-(x_b+tv)\| = \|x_a-x_b\|$, et en
passant à la limite lorsque $t$ tend vers 0, on obtient l'inégalité
demandée car $f$ est continue sur $\mathbb{R}^2$.
:::

::: {.section}
#### Question 5 {#question-5-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 5}`{=latex}

$d_A(x)=\inf_{a \in A} \|x - a\|=0$ implique qu'il existe une suite de
point $a_n\in A$ tels que $$
\lim_{n\to \infty} \|x - a_n\| = 0 
$$ donc que $x$ est dans l'adhérence de $A$. Réciproquement, si une
telle suite existe, $\inf_{a \in A} \|x - a\|\leq 0$ et donc
nécessairement puisque $\|x - a\|\geq 0$ pour tout $a\in A$, $d_A(x)=0$.
:::

::: {.section}
#### Question 6 {#question-6-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 6}`{=latex}

Soit $x\in \mathbb{R}^n$. Fixons $a_0\in A$ et $r:=\|x-a_0\|$. Soit $B$
la boule fermée centrée en $a_0$ et de rayon $r$. Comme
$a_0\in A\cap B$, $A\cap B$ est non vide. De plus, $A\cap B$ est fermé
comme intersection de fermés, et borné car $B$ est bornée. Donc
$A\cap B$ est compact. L'application $a \mapsto \|x-a\|$ est continue
sur $A\cap B$ donc elle admet un minimum atteint en $a^* \in A\cap B$.
Par définition de $d_A$, on a donc $d_A(x) = \|x-a^*\|$ et
$a^*\in \Pi_A(x)$.

Soit $x\in A$. Alors $d_A(x)=0$ et donc nécessairement $\Pi_A(x)=\{x\}$.

Soit $x\notin A$. Par définition, $\Pi_A(x) \subset A$, donc pour
montrer le résultat il faut montrer que $\Pi_A(x) \cap \mathring{A}$ est
vide. Prenons donc un point $a_0\in \mathring{A}$ et montrons que
$a_0\notin \Pi_A(x)$. Par définition de l'intérieur, il existe une boule
$B$ centrée en $a_0$ et incluse dans $A$. L'idée est de montrer qu'il y
aura forcément un point plus près de $x$ dans $B$. Prenons un point $a'$
sur le segment $[x,a_0]$ c'est-à-dire pour lequel il existe
$\lambda\in [0,1]$ tel que $$
a' = \lambda x + (1-\lambda) a_0 \ .
$$ On a alors $$
\|a'-x\| = \|(1-\lambda)(a_0-x)\| = |1-\lambda|\|a_0-x\| <  \|a_0-x\|
$$ pour tout $\lambda \in \left]0,1\right]$. Or pour $\lambda$
suffisamment petit, $a'\in B\subset A$ et $a'$ est plus proche de $x$
que $a_0$. Donc $a_0 \notin \Pi_A(x)$ et $\Pi_A(x)\subset \partial A$.
:::

::: {.section}
#### Question 7 {#question-7-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 7}`{=latex}

Soit $x\in D_A$. On nous dit qu'alors $d_A^2$ est différentiable en $x$.
Alors par définition du gradient, pour tout $v\in \mathbb{R}^n$, pour
tout $t\in \mathbb{R}$, $$
d_A(x+tv)^2 = d_A(x)^2 + \left<\nabla d_A^2 (x),tv\right> + o(t\|v\|)
$$ et donc $$
\lim_{t\to 0} \frac{d_A(x+tv)^2-d_A(x)^2}{t} = \left<\nabla d_A^2 (x),v\right> \ .
$$ D'après l'équation (1) de l'énoncé, on en déduit que $$
\nabla d_A^2 (x) = 2(x-p_A(x)) \ .
$$
:::

::: {.section}
#### Question 8 {#question-8-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 8}`{=latex}

Tout d'abord $d_A$ est constante égale à zero sur l'ouvert
$\mathring{A}$ donc elle y est différentiable de gradient
$\nabla d_A =0$.

Ensuite, vu que $d_A = \sqrt{d_A^2}$, $d_A$ est différentiable en $x$ si
$d_A^2$ est différentiable en $x$ et $d_A^2(x)\neq 0$, donc si
$\Pi_A(x)\in D_A \setminus A$. Soit
$g_1:\left]0, +\infty\right[ \to \left]0, +\infty\right[$ défini par
$g_1(t)=\sqrt{t}$ et $g_2:D_A \setminus A \to \left]0, +\infty\right[$
défini par $g_2=d_A^2$. On a $$
d_A = g_1\circ g_2 
$$ et donc par la règle de différentiation en chaîne, pour tout
$x\in D_A \setminus A$, $$
d d_A(x) \cdot h =  d g_1( g_2(x)) \cdot d g_2(x) \cdot h \ .
$$ Or pour $k\in \mathbb{R}$ et $t\in \left]0, +\infty\right[$,
$d g_1( t)\cdot k = \frac{1}{2\sqrt{t}} k$, et pour $h\in \mathbb{R}^n$
et $x\in \mathbb{R}^n$,
$d g_2(x) \cdot h = \left< \nabla d_A^2(x),h\right>$. Donc $$
d d_A(x) \cdot h = \frac{1}{2\sqrt{d_A^2(x)}} \left< \nabla d_A^2(x),h\right>
$$ soit $$
\nabla d_A(x) = \frac{1}{d_A(x)} (x-p_A(x)) = \frac{x-p_A(x)}{\|x-p_A(x)\|}  \ .
$$

On a donc la différentiabilité sur
$(D_A \setminus A) \cup \mathring{A} = D_A\setminus \partial A$.
:::

::: {.section}
#### Question 9 {#question-9-1 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 9}`{=latex}

Soient $v\in \mathbb{R}^n$, et $x\in \mathbb{R}^n$.

-   Soient $t>0$ et $p\in \Pi_A(x)$. Pour tout $p_t\in \Pi_A(x+tv)$,
    `\begin{align*}
     \frac{d_A(x+tv)^2-d_A(x)^2}{t} &=   \frac{\|x+tv-p_t\|^2-\|x-p\|^2}{t}\\
     &\leq    \frac{\|x+tv-p\|^2-\|x-p\|^2}{t}\\
     &\leq 2 \left<v, x-p\right> + t\|v\|^2 \ .
    \end{align*}`{=tex} puisque $d_A(x+tv)$ minimise la distance à $A$
    et $p_t\in A$.

-   Soit une suite $(t_k)_{k\in \mathbb{N}}$ de $\mathbb{R}^+$ telle que
    $\lim_{k\to +\infty} t_k = 0$, et $(p_{k})_{k\in \mathbb{N}}$ une
    suite de $A$ telle que $p_k\in \Pi_A(x+t_kv)$ pour tout
    $k\in \mathbb{N}$. On a `\begin{align*}
    |p_k| = |x+t_kv + p_k - (x+t_kv) |  &\leq |x+t_kv| + |x+t_kv - p_k|  \\
    & \leq d_A(x+t_kv) + |x+t_kv| \\
    & \leq d_A(x+t_kv) - d_A(x) +d_A(x) + |x+t_kv|
    \end{align*}`{=tex} Et d'après le point précédent,
    $\lim d_A(x+t_kv) - d_A(x) =0$ donc $(p_k)$ est bornée. $(p_k)$ est
    bornée dans le fermé $A$ donc elle vit dans un compact et on peut en
    extraire une sous-suite $(p_{\sigma(k)})$ qui converge vers
    $p_0 \in A$. Vu que
    $\lim \|x+t_{\sigma(k)}v - p_{\sigma(k)}\| = \|x-p_0\|$, et que
    $\|x+t_{\sigma(k)}v - p_{\sigma(k)}\|=d_A(x+t_\sigma(k)v)$, on en
    déduit $\|x-p_0\|=d_A(x)$ et donc que $p_0\in \Pi_A(x)$.

-   Finalement, puisque pour tout $k$, $d_A(x)\geq \|x- p_{\sigma(k)}\|$
    par définition de la distance, `\begin{align*}
    \frac{d_A(x+t_{\sigma(k)}v)^2-d_A(x)^2}{t_{\sigma(k)}} &= \frac{\|x+t_{\sigma(k)}v - p_{\sigma(k)}\|^2-\|x- p_{\sigma(k)}\|^2}{t_{\sigma(k)}} \\
    &\geq 2 \left<v, x-p_{\sigma(k)}\right> + t_{\sigma(k)}\|v\|^2   \\
    &\geq 2 \left<v, x-p_0\right> + 2 \left<v, p_0-p_{\sigma(k)}\right> + t_{\sigma(k)}\|v\|^2 \\
    &\geq 2 \inf_{p\in \Pi_A(x)} \left<v, x-p\right> + \Delta_k
    \end{align*}`{=tex} avec $\lim_{k\to +\infty} \Delta_k=0$. Donc
    $\liminf_{t\to 0}\frac{d_A(x+tv)^2-d_A(x)^2}{t} \geq 2 \inf_{p\in \Pi_A(x)} \left<v, x-p\right>$.
    Par ailleurs, on sait par le premier point que
    $\frac{d_A(x+tv)^2-d_A(x)^2}{t}\leq 2\inf_{p\in \Pi_A(x)} \left<v, x-p\right> + \Delta(t)$
    avec $\lim_{t\to0} \Delta(t)=0$. On en déduit que
    $\limsup_{t\to 0}\frac{d_A(x+tv)^2-d_A(x)^2}{t}\geq 2\inf_{p\in \Pi_A(x)} \left<v, x-p\right>$.
    Ceci montre donc que la limite existe et vaut nécessairement
    $2\inf_{p\in \Pi_A(x)} \left<v, x-p\right>$.
:::

::: {.section}
#### Question 10 {#question-10 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 10}`{=latex}

Supposons que $d_A^2$ est différentiable en $x$. Alors nécessairement,
d'après la question précédente, pour tout $v\in \mathbb{R}^n$, $$
\left< \nabla d_A^2(x), v \right> = 2\inf_{p\in \Pi_A(x)} \left<v, x-p\right> \ .
$$ Une idée est de montrer que la fonction à droite n'est pas linéaire
si $\Pi_A(x)$ n'est pas un singleton. Soient donc
$p_1,p_2 \in \Pi_A(x)$. Vu que pour tout $p\in \Pi_A(x)$,
$\|x-p\|=d_A(x)$, en prenant $v_1=-(x-p_1)$, on obtient $$
\left< \nabla d_A^2(x), v_1 \right> = 2\inf_{p\in \Pi_A(x)} -\left<x-p_1, x-p\right> = -2 \left<x-p_1, x-p_1\right>= -2d_A(x)^2 \ .
$$ De même, pour $v_2=-(x-p_2)$ $$
\left< \nabla d_A^2(x), v_2 \right> = -2 \left<x-p_2, x-p_2\right>= -2d_A(x)^2 \ .
$$ Par linéarité, on obtient donc $$
\left< \nabla d_A^2(x), v_1+ v_2 \right> = -4 d_A(x)^2 \ .
$$ Mais par ailleurs, $$
\left< \nabla d_A^2(x), v_1+ v_2 \right> = 2\inf_{p\in \Pi_A(x)} -\left<x-p_1, x-p\right>-\left<x-p_2, x-p\right>\ ,
$$ et le seul moyen d'obtenir $-4 d_A(x)^2$ est d'avoir simultanément $$
-\left<x-p_1, x-p\right>= -d_A(x)^2 \qquad , \qquad -\left<x-p_2, x-p\right>= -d_A(x)^2 
$$ et donc $x-p_1= x-p=x-p_2$, soit $p_1=p_2$. Donc il faut que
$\Pi_A(x)$ soit réduit à un singleton.
:::
:::

::: {.section}
Probabilités
============

::: {.section}
Préliminaires -- Espérance et fonction de répartition
-----------------------------------------------------

::: {.section}
#### Question 1 {#question-1-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 1}`{=latex}

Etudions la fonction
$$g : (x,u) \in \mathbb{R}_+^2 \mapsto 1_{[x,+\infty[}(u)\,f(u) = \left|\begin{array}{ll} f(u) & \text{si } x \leq u,\\0 & \text{si } x > u. \end{array}\right.$$

i.  Remarquons d'abord que $f$ étant positive (c'est une densité),
    toutes les fonctions partielles de $g$ le sont aussi ;
    l'intégrabilité coïncide ici avec l'absolue intégrabilité. Soient
    $x,u \in\mathbb{R}_+$.

-   D'après l'expression de $g$ on a $g_u(x) \leq f(u)\,1_{[0,u]}(x).$
    La fonction partielle $g_u$ est donc positive et majorée par le
    produit d'une constante et de l'indicatrice d'un segment, qui est
    trivialement intégrable sur $\mathbb{R}_+$. Par le critère
    d'intégrabilité dominée, $g_u$ l'est donc aussi pour tout
    $u\in\mathbb{R}_+$.\
-   De même, $g_x(u) \leq f(u)$. La fonction partielle $g_x$ est donc
    positive et majorée par une densité, par définition (absolument)
    intégrable. Par le critère d'intégrabilité dominée, $g_x$ l'est donc
    aussi sur $\mathbb{R}_+$ pour tout $x\in\mathbb{R}_+$.

ii. Comme $g_x$ est intégrable sur $\mathbb{R}_+$, on peut calculer son
    intégrale : `\begin{align*}
        \int_{\mathbb{R}_+} g(x,u)\,du &= \int_{\mathbb{R}_+} 1_{[x,+\infty[}(u)\,f(u)\,du\\
        & = \int_{\mathbb{R}_+} (1 - 1_{[0,x[}(u))\,f(u)\,du\\
        & = \left(\int_{\mathbb{R}_+} f(u)\,du - \int_0^x f(u)\,du\right)\\
        &= 1 - F(x)
        \end{align*}`{=tex} car $X$ est une variable positive (sa
    densité est nulle sur $\mathbb{R}_-^\ast$).

iii. Comme $g_u$ est intégrable sur $\mathbb{R}_+$, on peut calculer son
     intégrale : `\begin{align*}
         \int_{\mathbb{R}_+} g(x,u) \,dx &= \int_{\mathbb{R}_+} 1_{[x,+\infty[}(u)\,f(u) \,dx = f(u)\,\int_{\mathbb{R}_+} 1_{[0,u]}(x)\,dx\\
         &= f(u)\,\int_0^u 1\, dx =  u\,f(u).
         \end{align*}`{=tex}
:::

::: {.section}
#### Question 2 {#question-2-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 2}`{=latex}

Nous allons montrer les deux sens de l'équivalence.

-   Commençons par supposer que $1-F$ est intégrable sur $\mathbb{R}_+$.
    D'après la question précédente, cela signifie que
    $x \in \mathbb{R}_+ \mapsto \int_{\mathbb{R}_+} g(x,u)\,du$ est
    (absolument) intégrable. D'après le théorème de Tonelli, $g$ est
    donc absolument intégrable sur $\mathbb{R}_+^2$. Le théorème de
    Fubini garantit alors que la fonction
    $u \in \mathbb{R}_+ \mapsto \int_{\mathbb{R}_+} g(x,u) \,dx = u\,f(u)$
    est intégrable, ce qui signifie justement que $X \in \mathcal{L}^1$
    pour $X$ une variable aléatoire positive.

-   Réciproquement, supposons que $X \in \mathcal{L}^1$, c'est-à-dire
    que
    $u \in \mathbb{R}_+ \mapsto u\,f(u) = \int_{\mathbb{R}_+} g(x,u) \,dx$
    est (absolument) intégrable. Le théorème de Tonelli garantit alors
    que $g$ est absolument intégrable sur $\mathbb{R}_+^2$, puis celui
    de Fubini que la fonction
    $x \in \mathbb{R}_+ \mapsto \int_{\mathbb{R}_+} g(x,u)\,du = 1-F(x)$
    l'est également.

Nous avons donc montré l'équivalence $(E)$.
:::

::: {.section}
#### Question 3 {#question-3-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 3}`{=latex}

Par définition, puisque $X$ est positive nous avons d'abord
$$\mathbb{E}\left(X\right) = \int_{\mathbb{R}_+} x\,f(x)\,dx.$$ Or
d'après la question 1, en utilisant à nouveau le théorème de Fubini :
`\begin{align*}
 \int_{\mathbb{R}_+} u\,f(u)\,du &= \int_{\mathbb{R}_+} \left(\int_{\mathbb{R}_+} g(x,u)\,dx\right)\,du = \int_{\mathbb{R}_+} \left(\int_{\mathbb{R}_+} g(x,u)\,du\right)\,dx\\
 & = \int_{\mathbb{R}_+} 1-F(x)\,dx.
 \end{align*}`{=tex} On peut donc écrire de manière équivalente
$$\mathbb{E}(X) = \int_{\mathbb{R}_+} 1-F(x)\,dx.$$
:::
:::

::: {.section}
Etude du maximum -- Loi de Fréchet
----------------------------------

::: {.section}
#### Question 4 {#question-4-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 4}`{=latex}

La loi de $X^\alpha$ est déterminée par sa fonction de répartition que
nous allons donc expliciter. Par définition, pour tout $x\in\mathbb{R}$
elle vaut $\mathbb{P}\left(X^\alpha \leq x \right)$. Or comme $X$ est
positive ($F(0) = 0$), pour tout $x \in \mathbb{R}_-$ on a directement
$\mathbb{P}\left(X^\alpha \leq x \right) = 0$. Pour tout
$x \in \mathbb{R}_+^\ast$, l'application
$x \in \mathbb{R}_+^\ast \mapsto x^\alpha$ étant bijective et croissante
($\alpha > 0$ par hypothèse), on obtient
$$\mathbb{P}\left(X^\alpha \leq x\right) = \mathbb{P}\left(X \leq x^{\frac{1}{\alpha}} \right)= F_{\frac{1}{\alpha}}(x).$$
Puisque $F_{\frac{1}{\alpha}}$ est nulle sur $\mathbb{R}_-$, on en
déduit que l'égalité ci-dessus est vraie pour tout $x\in\mathbb{R}$.
Ainsi, $X^\alpha$ suit une loi de Fréchet de paramètre
$\dfrac{1}{\alpha}$.
:::

::: {.section}
#### Question 5 {#question-5-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 5}`{=latex}

i.  Comme $X$ est positive, d'après la première partie et la question
    précédente, $X^{\alpha} \in \mathcal{L}^1$ ssi
    $1-F_{\frac{1}{\alpha}}$ est intégrable sur $\mathbb{R}_+^\ast$
    (inclure ou non $\{0\}$ ne change rien).

    La convexité de l'exponentielle nous assure que pour tout
    $x\in\mathbb{R}$, $$1 + x \leq e^x \leq 1 + x\,e^x.$$ Ainsi, pour
    tout $x > 0$ on a
    $$x^{-\frac{1}{\alpha}}\,\exp\left\{-x^{-\frac{1}{\alpha}} \right\} \leq 1 - F_{\frac{1}{\alpha}}(x) \leq x^{-\frac{1}{\alpha}}.$$
    En outre, pour tout $x\in\mathbb{R}$ on a aussi `\begin{equation}
    0 < 1 - F_{\frac{1}{\alpha}}(x) \leq 1. \tag{2}
    \end{equation}`{=tex}

    -   Soit $\alpha < 1$. La fonction d'intérêt
        $1-F_{\frac{1}{\alpha}}$ est positive et majorée sur
        $\mathbb{R}_+^\ast$ par
        $$x\in\mathbb{R}_+^\ast \mapsto \left|\begin{array}{ll} x^{-\frac{1}{\alpha}} & \text{si } x > 1,\\ 1 & \text{si } 0< x \leq 1.\end{array}\right.$$
        Or, quand $\alpha < 1$, cette dernière fonction est bien
        intégrable (par morceaux) sur $\mathbb{R}_+^\ast$. Par le
        critère d'intégrabilité dominée, $1-F_{\frac{1}{\alpha}}$ l'est
        donc également. On en conclut que le "si" de l'équivalence à
        démontrer est vrai.

    -   Soit $\alpha \geq 1$. On a
        $\exp\left\{-x^{-\frac{1}{\alpha}}\right\} \to 1$ lorsque
        $x\to +\infty$ ; il existe donc $x_0 > 0$ tel que pour tout
        $x>x_0$ on a
        $\exp\left\{-x^{-\frac{1}{\alpha}}\right\} > \frac{1}{2}$. Or la
        fonction $x \mapsto \frac{1}{2}\,x^{-\frac{1}{\alpha}}$ n'est
        pas intégrable sur $]x_0, +\infty[$ pour $\alpha \geq 1$. Comme
        elle minore $1-F_{\frac{1}{\alpha}}$ sur ce même intervalle,
        $1-F_{\frac{1}{\alpha}}$ n'y est pas non plus intégrable. A
        fortiori, elle ne l'est donc pas non plus sur tout
        $\mathbb{R}_+^\ast$. On en conclut que le "seulement si" de
        l'équivalence recherchée est vrai lui aussi.

    Finalement, nous avons bien $X^{\alpha} \in \mathcal{L}^1$ ssi
    $\alpha < 1$.

ii. Soit $\alpha < 1$. Ici, il est plus facile d'utiliser la définition
    de $\mathbb{E}\left(X^\alpha\right)$ faisant intervenir la densité
    de $X^\alpha$. Puisque $F_{\frac{1}{\alpha}}$ est continue et
    dérivable partout, il en existe bien une, qui coïncide avec la
    dérivée de $F_{\frac{1}{\alpha}}$ :
    $$f_{\frac{1}{\alpha}} : x \in \mathbb{R}\mapsto \left|\begin{array}{ll} \frac{1}{\alpha}\,x^{-\frac{1}{\alpha}-1}\,\exp\left\{-x^{-\frac{1}{\alpha}} \right\} & \text{si } x > 0,\\ 0 & \text{sinon.}  \end{array}\right.$$
    Alors
    $$\mathbb{E}\left(X^\alpha\right) = \int_\mathbb{R}x\,f_{\frac{1}{\alpha}}(x)\,dx = \int_{0}^{+\infty} \dfrac{1}{\alpha}\,x^{-\frac{1}{\alpha}}\,\exp\left\{-x^{-\frac{1}{\alpha}} \right\}\,dx,$$
    et par le changement de variable $u = x^{-\frac{1}{\alpha}}$ on
    obtient directement
    $$\mathbb{E}\left(X^\alpha\right) = \int_0^{+\infty} u^{-\alpha}\,\exp\left\{-u\right\} \,du = \Gamma\left(1 - \alpha \right).$$
:::

::: {.section}
#### Question 6 {#question-6-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 6}`{=latex}

i.  Lorsque $x\to+\infty$,
    $$1-F(x) = 1-F_{\xi}(x) = 1 - \exp\left\{ -x^{-\xi}\right\} = 1 - \left( 1 - x^{-\xi} + o(x^{-\xi}) \right) \sim x^{-\xi}.$$
    Par conséquent, pour tout $x>1$, lorsque $t\to+\infty$, on a
    `\begin{align*}
    \mathbb{P}\left(X > xt \mid X > t \right) &= \dfrac{\mathbb{P}\left(X > xt\right)}{\mathbb{P}\left(X > t\right)} = \dfrac{1 - F(xt)}{1-F(t)} \sim \dfrac{x^{-\xi}\,t^{-\xi}}{t^{-\xi}} = x^{-\xi}.
    \end{align*}`{=tex}

ii. D'après la question 5, $X$ a la même loi que $Y^{\frac{1}{\xi}}$, où
    $Y$ suit une loi de Fréchet standard. On a donc
    $X^\alpha\in\mathcal{L}^1$ ssi
    $Y^{\frac{\alpha}{\xi}} \in \mathcal{L}^1$, qui est équivalent,
    d'après la question 5.i, à $\alpha < \xi$.

iii. Ces résultats illustrent pourquoi la loi de Fréchet est dite *à
     queue épaisse* : $1-F_\xi$ décroit lentement vers $0$, à la même
     vitesse que l'inverse d'une fonction puissance, et ce d'autant plus
     que $\xi$ est petit. Puisque pour tout $x\in\mathbb{R}$,
     $1-F_{\xi}(x) = \mathbb{P}\left(X > x\right)$, cela signifie que
     les événements extrêmes que sont les dépassements de très grandes
     hauteurs d'eau (qui auraient des conséquences environnementales,
     sociales, économiques dramatiques) ne sont pas si rares que ça. En
     particulier, lorsque $\xi \leq 1$, ils sont tellement fréquents que
     $X$ n'admet pas d'espérance ; cela n'a plus de sens de définir un
     comportement moyen lorsque la variabilité est trop grande. En
     outre, la convergence $\mathbb{P}(X>xt\mid X>t) \to x^{-\xi}$ quand
     $t\to+\infty$ et $x>1$ indique que sachant qu'une crue
     exceptionnelle a déjà eu lieu, la probabilité d'en observer une
     plus importante encore reste (relativement) élevée. Le choix de la
     loi de Fréchet pour modéliser la hauteur d'eau maximale de la Seine
     permet donc de se prémunir des risques dans le cadre du changement
     climatique.

**Remarque.** On se rend encore plus compte de l'aspect "queue épaisse"
si on compare $1-F_\xi$ à $1-\Phi$, où $\Phi$ est la fonction de
répartition d'une gaussienne centrée réduite, de densité $\varphi$. En
effet, nous avons vu en TD que quand $x\to+\infty$,
$$1-\Phi(x) \sim \dfrac{\varphi(x)}{x} = \dfrac{1}{\sqrt{2\pi}\,x}\,\exp\left\{-\dfrac{x^2}{2}\right\},$$
qui décroit exponentiellement vite vers $0$. Ainsi, pour $x\to+\infty$
on a
$$\dfrac{1-F_\xi(x)}{1-\Phi(x)} \sim \dfrac{x^{1-\xi}}{\sqrt{2\pi}}\,\exp\left\{\dfrac{x^2}{2}\right\},$$
qui tend d'autant plus vite vers $+\infty$ que $\xi$ est petit,
c'est-à-dire que la queue de la distribution de $X$ est épaisse.
:::

::: {.section}
#### Question 7 {#question-7-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 7}`{=latex}

i.  Soit $x\in\mathbb{R}$, alors par indépendance et même distribution
    que $X$ des variables aléatoires $X_1,\dots,X_n$ on a
    `\begin{align*}
      \mathbb{P}\left( M_n \leq x \right) &= \mathbb{P}\left( \max_{1\leq i \leq n} X_i \leq x \right) = \mathbb{P}\left( X_1\leq x,\dots, X_n \leq x \right)\\
      & = \prod_{i = 1}^n \mathbb{P}\left( X_i \leq x \right) = \mathbb{P}\left(X \leq x\right)^n= F_\xi(x)^n\\
      & = \exp\left\{ -n\,x^{-\xi}\right\} = \exp\left\{ -\left(n^{-\frac{1}{\xi}}\,x\right)^{-\xi} \right\}\\
      &= F_\xi\left( n^{-\frac{1}{\xi}}\,x \right).
      \end{align*}`{=tex}\
    Par conséquent, si l'on pose $a_n = n^{-\frac{1}{\xi}}$ on obtient
    bien
    $$\mathbb{P}\left(a_n\,M_n \leq x \right) = \mathbb{P}\left(n^{-\frac{1}{\xi}}\,M_n \leq x \right) = \mathbb{P}\left(M_n \leq n^{\frac{1}{\xi}}\,x \right) = F_\xi (x),$$
    ce qui signifie que $a_n\,M_n$ a la même loi que $X$.

ii. En utilisant les questions 6.i et 7.i, quand $x\to+\infty$ on a
    directement `\begin{align*}
      \dfrac{\mathbb{P}\left(M_n > x\right)}{n\,\mathbb{P}\left(X > x \right)} &= \dfrac{1}{n}\,\dfrac{1 - \mathbb{P}\left(M_n \leq x\right)}{1 - \mathbb{P}\left(X\leq x\right)} = \dfrac{1}{n}\,\dfrac{1 - F_\xi\left(n^{-\frac{1}{\xi}}\,x\right)}{1-F_\xi(x)} \\
      & \sim \dfrac{1}{n}\,\dfrac{\left(n^{-\frac{1}{\xi}}\,x\right)^{-\xi}}{x^{-\xi}} = 1.
      \end{align*}`{=tex} Ce résultat signifie que pour un seuil $x$
    très grand, la hauteur d'eau maximale sur $n$ années a $n$ fois plus
    de chances de dépasser $x$ qu'en une seule année. Le risque de crue
    exceptionnelle croît de manière linéaire avec le nombre d'années
    écoulées.
:::

::: {.section}
#### Question 8 {#question-8-2 .answer .unnumbered .unlisted}

`\addcontentsline{toc}{paragraph}{Question 8}`{=latex}

Notons $\left(\mathcal{P}_n\right)$ l'équivalence à démontrer.

-   **Initialisation.** $\left(\mathcal{P}_1\right)$ est trivialement
    vraie.

-   **Hérédité.** Soit $n > 1$ et supposons que
    $\left(\mathcal{P}_{n-1}\right)$ est vraie. On fixe pour le moment
    $x>0$.

    On a l'inclusion des événements
    $$\Bigl(\{S_{n-1} > x\} \cup \{X_n > x\}\Bigr) \subset \{S_n > x\},$$
    qui combinée au caractère indépendant et identiquement distribué de
    $X_1,\dots,X_n$ donne `\begin{align*}
    \mathbb{P}(S_n > x) &\geq \mathbb{P}\left( S_{n-1} > x \right) + \mathbb{P}\left(X_n > x \right) - \mathbb{P}\left(S_{n-1} > x, X_n > x \right)\\
    & = \mathbb{P}\left(S_{n-1} > x\right) + \mathbb{P}\left(S_{n-1} \leq x\right)\,\mathbb{P}\left(X > x \right).
    \end{align*}`{=tex} Ainsi, quand $x \to +\infty$, d'après
    $\left(\mathcal{P}_{n-1}\right)$ on a `\begin{align*}
    \dfrac{\mathbb{P}(S_n > x)}{n\,\mathbb{P}(X > x)} &\geq \dfrac{n-1}{n}\,\dfrac{\mathbb{P}\left(S_{n-1} > x\right)}{(n-1)\,\mathbb{P}\left(X > x\right)} + \dfrac{1}{n}\,\mathbb{P}\left(S_{n-1} \leq x\right)\\
    & \to \dfrac{n-1}{n} + \dfrac{1}{n} = 1.
    \end{align*}`{=tex} Par ailleurs, pour
    $\delta \in \left] 0, \frac{1}{2} \right[$ on a l'inclusion
    $$\{S_n > x\} \subset \{S_{n-1} > (1-\delta)x \} \cup \{X_n > (1-\delta)x \} \cup \{ S_{n-1} > \delta x, X_n > \delta x \},$$
    qui donne sous les hypothèses d'indépendance et de même loi de
    $X_1,\dots,X_n$ `\begin{align*}
    \mathbb{P}(S_n > x) &\leq \mathbb{P}\left(S_{n-1} > (1-\delta)x\right) + \mathbb{P}\left(X_n > (1-\delta)x\right)\\
    &\hspace*{2em} + \mathbb{P}\left(S_{n-1} > \delta x, X_n > \delta x\right)\\
    &= \mathbb{P}\left(S_{n-1} > (1-\delta)x\right) + \mathbb{P}\left(X_n > (1-\delta) x\right)\\
    &\hspace*{2em} + \mathbb{P}\left(S_{n-1} > \delta x\right)\,\mathbb{P}\left(X > \delta x\right).
    \end{align*}`{=tex} Par conséquent, quand $x\to+\infty$, d'après
    $\left(\mathcal{P}_{n-1}\right)$ et la question 6.i on a
    `\begin{align*}
    \dfrac{\mathbb{P}(S_n > x)}{n\,\mathbb{P}(X>x)} &\leq \dfrac{\mathbb{P}\left(S_{n-1} > (1-\delta)x\right)}{n\,\mathbb{P}(X>x)} + \dfrac{\mathbb{P}\left(X > (1-\delta)x\right)}{n\,\mathbb{P}(X>x)}\\
    &\hspace{2em} + \dfrac{\mathbb{P}\left(X > \delta x\right)}{n\,\mathbb{P}(X>x)}\,\mathbb{P}\left(S_{n-1} > \delta x\right)\\
    & = (n-1)\dfrac{\mathbb{P}\left(S_{n-1} > (1-\delta)x\right)}{(n-1)\,\mathbb{P}(X> (1-\delta)x)}\,\dfrac{\mathbb{P}\left(X > (1-\delta)x\right)}{n\,\mathbb{P}(X>x)}\\
    &\hspace*{2em} + \dfrac{\mathbb{P}\left(X > (1-\delta)x\right)}{n\,\mathbb{P}(X>x)}\\
    &\hspace*{2em} + \dfrac{\mathbb{P}\left(X > \delta x\right)}{n\,\mathbb{P}(X>x)}\,\dfrac{\mathbb{P}\left(S_{n-1} > \delta x\right)}{(n-1)\,\mathbb{P}\left(X > \delta x\right)}\,(n-1)\,\mathbb{P}\left(X > \delta x\right)\\
    &\sim \left(\dfrac{n-1}{n} + \dfrac{1}{n}\right)\,(1-\delta)^{-\xi} + \dfrac{\delta^{-2\xi}}{n}\,(n-1)\,x^{-\xi} \\
    &\to (1-\delta)^{-\xi},
    \end{align*}`{=tex} qui tend vers $1$ lorsque $\delta \to 0$.

    Le théorème des gendarmes nous permet de conclure que
    $\left(\mathcal{P}_n\right)$ est vraie.

-   **Conclusion**. La propriété $\left(\mathcal{P}_n\right)$ est vraie
    pour tout $n\in\mathbb{N}^\ast$.

    En combinant ce résultat avec celui de la question 7.ii on obtient
    $$\mathbb{P}\left(S_n > x\right) \sim \mathbb{P}\left(M_n > x\right)$$
    quand $x\to+\infty$. Cela implique que la loi des excès du maximum
    domine celle de la somme. En d'autres termes, pour un très grand
    seuil $x >0$, l'événement extrême $\{S_n > x\}$ est essentiellement
    dû à l'événement $\{M_n > x\}$.
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
