% Calcul Différential, Intégral et Stochastique  
  MINES ParisTech/UE 11 -- Examen
%
% 3 novembre 2020, 9h--12h

\newcommand{\N}{\mathbb{N}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\Esp}{\mathbb{E}}

# Coques fines

Dans ce problème, $\|\cdot\|$ désigne la norme euclidienne dans $\R^2$ et
$d$ la distance associée.
$$
\|(x_1, x_2)\| := \sqrt{x_1^2 + x_2^2} \; \mbox{ et } \; d(x, y) := \|y - x\|.
$$
Le symbole $U$ désigne le 
sous-ensemble du plan constitué des points d'abscisse et d'ordonnée
strictement positives
et $C$ l'arc de cercle constitué des points de $U$ 
à distance $1$ de l'origine.
$$
U = \{(x_1,x_2) \in \R^2 \; | \; \mbox{$x_1 > 0$ et $x_2 > 0$}\}
\; \mbox{ et } \;
C = \{x \in U \; | \; \|x\| = 1\}.
$$

On définit la projection $p$ sur
l'arc de cercle $C$ comme la fonction :
$$
p: x \in U \mapsto \frac{x}{\|x\|} \in C.
$$
On rappelle que cette projection $p(x)$ minimise la distance entre $x \in U$ et $C$ :
$$
d(x, p(x)) = \min_{y \in C} d(x, y) =: d(x, C).
$$

Finalement, pour tout $\varepsilon \in \left]0, 1\right]$, 
on définit la coque de $C$ d'épaisseur $2 \varepsilon$ par
$$
V_{\varepsilon} := \{x \in U \; | \; d(x,C) < \varepsilon\}.
$$

![](images/coque.svg) \

## Topologie

#### Question 0
Montrer que l'ensemble $U$ est un ouvert de $\R^2$.
Montrer que pour tout $\varepsilon \in \left]0, 1\right]$ 
$$
V_{\varepsilon} = U \cap \{x \in \R^2 \; | \; 1- \varepsilon < \|x\| < 1 + \varepsilon \},
$$
et en déduire que les ensembles $V_{\varepsilon}$ sont également des ouverts 
de $\R^2$.

## Calcul Différentiel

#### Question 1
Montrer que les dérivées partielles de la fonction $x\in U \mapsto \|x\| \in \R$
existent et en déduire la valeur de
$$
n(x) := \nabla \|x\|.
$$
La fonction $x\in U \mapsto \|x\| \in \R$ est-elle continûment différentiable ?

#### Question 2
Montrer l'existence et calculer la valeur de $\nabla(1/\|x\|)$ quand $x\in U$. 

#### Question 3 
Montrer que si deux fonctions $f: U \mapsto \R$ et $g: U \mapsto \R^2$ sont
différentiables, alors le produit $fg$ également. 
Calculer la jacobienne $J_{fg}(x)$ en fonction de $\nabla f(x)$ et $J_g(x)$.

#### Question 4
Montrer que $p$ est différentiable et que 
$$
J_p(x) = \frac{1}{\|x\|} P(x) \; \mbox{ où } \; P(x) =  I - n(x) \cdot n(x)^{\top}.
$$
($I$ désigne la matrice identité de $\mathbb{R}^2$.)



#### Question 5
On pose
$$
h(x) = p(x) + \varepsilon (x - p(x)).
$$
Montrer que $h: V_1 \to V_{\varepsilon}$ est une bijection et
déterminer $h^{-1}(y)$ quand $y \in V_{\varepsilon}$.


#### Question 6
Calculer $J_{h}(x)$ et 
montrer que $h$ est un $C^1$-difféomorphisme.

#### Question 7
Etablir que
$$
\det J_{h}(x) = \varepsilon 
\left(
\varepsilon + \frac{1-\varepsilon}{\|x\|} \right).
$$

## Calcul Intégral

#### Question 8
On note $S := [0,2] \times [0,2] \subset \mathbb{R}^2$.  Que vaut l'intégrale
$$
\int_{\R^2} 1_S(x) \, dx
$$
et pourquoi ? (On ne demande pas de justifier l'existence de l'intégrale).

#### Question 9
Calculer $(-t(\ln t - 1))'$ pour $t>0$ et en déduire que 
$$
\int_{\varepsilon}^2 (- \ln t) \, dt \to -2(\ln 2 - 1) \; \mbox{ quand } \;
\varepsilon \to 0, \; \varepsilon > 0.
$$
En déduire que la fonction de $\mathbb{R}$ dans $\mathbb{R}$ égale à $-\ln t$ 
quand $t \in \left]0, 2\right]$ et nulle sinon est intégrable sur $[0, 2]$.
Est-ce que l'on pourrait se passer de la mention "et nulle sinon"
pour répondre à cette dernière question ?

#### Question 10
Montrer l'existence et calculer
$$
\int_0^2 \frac{dx_1}{\sqrt{x_1^2 + x_2^2}}
$$
quand $x_2 \in \left]0, 2\right]$. 
Indication : $\partial_{x_1} \left( \ln \left(x_1 + \sqrt{x_1^2 + x_2^2} \right) \right) = 1/\sqrt{x_1^2 + x_2^2}$ (la preuve de cette égalité n'est pas exigée).


#### Question 11
Montrer que la frontière $\partial S$ de l'ensemble $S$ dans $\R^2$ est négligeable. 
(On donnera $\partial S$ sans justification.) 
En déduire que la fonction
$$
x \in \R^2
\mapsto 
\left|
\begin{array}{rl}
1 / \|x\| & \mbox{si $x \in S$ et $x \neq (0,0)$,} \\
0 & \mbox{sinon.}
\end{array}
\right.
$$
est mesurable. Puis, déduire des questions précédentes son intégrabilité.


#### Question 12
Soit $f: C \to \R$ une fonction bornée telle que $f \circ p: U \to \R$ soit mesurable
(c'est-à-dire que son prolongement par $0$ à $\R^2$ est mesurable).
Soit $\varepsilon \in \left]0, 1\right]$.
Montrer que l'intégrale
$$\frac{1}{2\varepsilon} \int_{V_{\varepsilon}} f(p(y)) \, dy$$
est bien définie.

#### Question 13
Montrer que
$$
\frac{1}{2\varepsilon} \int_{V_{\varepsilon}} f(p(y)) \, dy=\frac{1}{2} \int_{V_1} f(p(x)) \left(
\varepsilon + \frac{1-\varepsilon}{\|x\|} \right) \, dx.
$$

#### Question 14
Déduire des questions précédentes l'existence et la valeur de
$$
\lim_{\substack{\varepsilon \to 0\\\varepsilon \in \left]0,1\right]}}
\frac{1}{2\varepsilon} \int_{V_{\varepsilon}} f(p(y)) \, dy.
$$

# Probabilités --- Loi de Maxwell 

On désire déterminer la distribution des vitesses des molécules d’un gaz monoatomique parfait à l’équilibre (loi de Maxwell (1859)).

On représente la vitesse d’une molécule d’un gaz monoatomique parfait à l’équilibre dans un repère orthonormal par un vecteur aléatoire $V = (V_1 , V_2 , V_3 )$. Le choix du repère étant arbitraire, il est naturel de supposer que la loi de $V$ est invariante par rotation (autour de l'origine) et que les composantes de $V$ sont indépendantes.

## Partie 1 

Soit $(X, Y, Z)$ un vecteur aléatoire  à valeurs dans $\R^3$ de densité $f_{(X, Y, Z)}$.
Ce vecteur aléatoire est supposé invariant par rotation : il existe une fonction $\phi: \left[0, +\infty\right[ \to \left]0, +\infty\right[$ (strictement positive) telle que
$$
f_{(X, Y, Z)}(x,y,z) = \phi(x^2+y^2+z^2) \;  \mbox{ pour tout $(x, y, z) \in \R^3$.}
$$ 

<!--
#### Question 0
Soit $(X, Y, Z)$ un vecteur aléatoire  à valeurs dans $\R^3$ de densité $f_{(X, Y, Z)}$.
Montrer que l'ensemble 
$$
P = \{ (x,y,z) \in \R^3 \; | \; f_{(X, Y, Z)}(x,y,z) \neq 0 \}
$$ 
n'est pas négligeable (c'est-à-dire que son volume est strictement positif).
-->

#### Question 1
On suppose de plus les variables aléatoires
$X$, $Y$ et $Z$ indépendantes. Montrer qu'il existe une fonction
$f: \R \to \left[0, +\infty\right[$ qui soit une densité telle que 
$$
f_{(X, Y, Z)}(x, y, z) = f(x) f(y) f(z) \; \mbox{ pour tout $(x, y, z) \in \R^3$.} 
$$
Montrer finalement que $f(x) > 0$ pour tout $x \in \R$.

#### Question 2

On suppose de plus que les densités marginales de $X, Y$ et $Z$ ainsi que la fonction $\phi$ sont continûment différentiables (c'est-à-dire de classe $C^1$). Montrer que la densité de chacune des composantes s'écrit sous la forme $f (x) = a e^{cx^2/2}$, avec $a$ et $c$ deux constantes réelles.

#### Question 3

En déduire que le vecteur $(X, Y, Z)$ suit une loi gaussienne d'espérance l'origine dont on précisera la matrice de covariance en fonction de la constante $\sigma = 1/\sqrt{|c|}$.

## Partie 2

On suppose que le vecteur aléatoire $(X, Y, Z) = V$ vérifie les hypothèses des
questions précédentes. 

#### Question 4

Calculer l'énergie cinétique moyenne d'un atome du gaz, c'est-à-dire l'espérance 
$$
E_c := \mathbb{E}\left(\frac{1}{2}m\|V\|^2\right)
$$ 
où $m$ est la masse d'un atome du gaz.
L’énergie cinétique moyenne d’un atome du gaz de masse $m$ étant égale à $\frac{3}{2} kT$ où $k$ est la constante de Boltzmann et $T$ la température du gaz, en déduire la valeur de
$\sigma^2$ en fonction de $k$, $T$ et $m$.

#### Question 5

On rappelle que si $X$ et $Y$ sont deux variables aléatoires indépendantes de loi respective $\Gamma (a,\lambda)$ et $\Gamma (b,\lambda)$, alors la loi de $X + Y$ est la loi $\Gamma (a+b,\lambda)$. On rappelle également que la densité $g$ de la loi $\Gamma (a,\lambda)$ vérifie
$$
g(x) = \frac{1}{\Gamma(a)}\lambda^a x^{a -1} e^{-\lambda x} 1_{]0,+\infty[}(x)
\; \mbox{ pour tout $x\in\R$},
$$
où $\Gamma$ est la fonction définie par
$$\Gamma(a) = \int_0^{+\infty} x^{a-1}e^{-x} dx \text{ pour } a \in \left] 0, + \infty \right[.$$
On remarquera que $\Gamma(1/2) = \sqrt{\pi}$ et que $\Gamma(x+1) = x \Gamma(x).$ 

Calculer la loi de $V_1^2$. 
En déduire la loi de $\|V \|^2$ puis la densité de $\|V \| = \sqrt{V_1^2 + V_2^2 + V_3^2}$.
La probabilité associée est appelée loi de Maxwell.


Solutions
================================================================================

## Topologie

#### Question 0

Pour tout $x=(x_1, x_2) \in U$, $d(x, U^c) = \min(x_1, x_2) > 0$ ;
l'ensemble $U$ est donc ouvert. 

Par définition, un point $x$ appartient à $V_{\varepsilon}$ si et seulement 
s'il appartient à $U$ et vérifie $d(x, C) < \varepsilon$. Or,
$$
d(x, C) = d(x, p(x)) = \left\|\frac{x}{\|x\|} - x\right\| = \left|\frac{1}{\|x\|} - 1 \right| \|x\| = |1  - \|x\||.
$$
L'inégalité $d(x, C) < \varepsilon$ est donc équivalente à 
$1 - \|x\| < \varepsilon$ et $\|x\| - 1 < \varepsilon$, soit
$1 - \varepsilon < \|x\| < 1 + \varepsilon.$
On a donc bien
$$
V_{\varepsilon} = U \cap \{x \in \R^2 \; | \; 1- \varepsilon < \|x\| < 1 + \varepsilon \},
$$

Notons $U_{\varepsilon}:= \{x \in \R^2 \; | \; 1- \varepsilon < \|x\| < 1 + \varepsilon \}.$
L'ensemble $U_{\varepsilon}$ est un ouvert de $\R^2$ comme image réciproque 
de l'intervalle ouvert $\left]1-\varepsilon, 1+\varepsilon\right[$ 
par l'application continue $x \in \R^2 \mapsto \|x\|$. 
L'ensemble $V_{\varepsilon} = U \cap U_{\varepsilon}$ est donc ouvert : 
en effet pour tout $x\in V_{\varepsilon}$, 
$$
d(x, V_{\varepsilon}^c)
=
d(x, (U \cap U_{\varepsilon})^c)
= 
d(x, U^c \cup U_{\varepsilon}^c)
= \min (d(x, U^c), d(x, U_{\varepsilon}^c)) > 0.
$$

## Calcul Différentiel


#### Question 1
Comme pour tout $x=(x_1, x_2) \in U$, $\|x\| = \sqrt{x_1^2 + x_2^2}$, 
l'application partielle $x_1 \in \left]0, +\infty\right[ \mapsto \|x\|$
est dérivable par rapport à $x_1$ par dérivation en chaîne en tout point 
et l'on a
$$
\frac{\partial \|x\|}{\partial x_1}  = \frac{1}{2\sqrt{x_1^2 + x_2^2}} \times 2 x_1 = \frac{x_1}{\|x\|}.
$$
Par un argument similaire, la dérivée par rapport à $x_2$ existe également et
vaut
$$
\frac{\partial \|x\|}{\partial x_2} = \frac{x_2}{\|x\|}.
$$
On a donc
$$
n(x) := \nabla \|x\| = \left[\frac{\partial \|x\|}{\partial x_1} , \frac{\partial \|x\|}{\partial x_2}\right]^{\top}
=\left[\frac{x_1}{\|x\|}, \frac{x_2}{\|x\|}\right]^{\top} = p(x).
$$
La fonction $p$ est bien continue ; la fonction $x \in U \mapsto \|x\|$ est 
donc continûment différentiable.

#### Question 2

La fonction $x \in U \mapsto 1 /\|x\|$ est différentiable comme composée des
fonctions différentiables $f: x \in U \mapsto \|x\| \in \left]0, +\infty\right[$,
dont la matrice jacobienne en $x$ est
$$J_f(x) = (\nabla \|x\|)^{\top} = p(x)^{\top} \in \R^{1 \times 2}$$
et $g: y \in \left]0, +\infty\right[ \mapsto 1/y$, dont la matrice jacobienne en
$y$ est $$J_g(y) = g'(y)= -1/y^2 \in \R^{1 \times 1}.$$ La règle de différentiation
en chaîne fournit
$$
J_{g \circ f}(x) = J_g(f(x)) \cdot J_f(x) = \frac{-1}{\|x\|^2} p(x)^{\top}
= \left(-\frac{x}{\|x\|^3} \right)^{\top}.
$$
On en déduit que le gradient de $g \circ f$ existe en tout point et satisfait
$$
\nabla \left(\frac{1}{\|x\|}\right) = J_{g \circ f}(x)^{\top} = -\frac{x}{\|x\|^3}.
$$

#### Question 3

La fonction $fg$ est continûment différentiable car ses composantes 
$(fg)_1 = fg_1$ et $(fg)_2 = fg_2$ le sont par la règle du produit 
et le lien entre différentiabilité d'une fonction et de ses composantes. 
On a en outre
$$
\partial_j (f g)_i = \partial_j (f g_i) = f \partial_j g_i + g_i \partial_j f
$$
ce qui fournit
$$
J_{fg} = f J_g + g \cdot \nabla f^{\top}.
$$

#### Question 4
En appliquant le résultat de la question précédente avec
$f(x) = 1/\|x\|$ et $g(x) = x$, qui en vérifient bien les hypothèses,
on obtient :
$$
J_p(x) = \frac{1}{\|x\|} I + x \cdot \left(\nabla \frac{1}{\|x\|} \right)^{\top}
=
\frac{1}{\|x\|}\left( I -  \frac{x}{\|x\|} \frac{x}{\|x\|}^{\top}\right)
$$
donc on a bien
$$
J_p(x) = \frac{1}{\|x\|} P(x).
$$

#### Question 5

Soit $x \in V_1$ (c'est-à-dire $x \in U$ et $0 < \|x\| < 2$) et $y := h(x)$.
En utilisant les définitions de $h(x)$ et de $p(x)$ on constate que
$$
y = \left(\frac{1-\varepsilon}{\|x\|} + \varepsilon \right) x \in U
$$
et donc que $p(y) = p(x)$ puisque $x$ et $y$ sont colinéaires.
Par conséquent, $y$ vérifie
$$\|y - p(y)\| = \|y - p(x)\| = |\varepsilon|\|x - p(x)\| < \varepsilon$$
et appartient donc à $V_{\varepsilon}$. Réciproquement, si 
$y \in V_{\varepsilon}$, alors
$y = p(x) + \varepsilon (x- p(x))$ fournit
$y = p(y) + \varepsilon(x - p(y))$ et donc
$$
x = p(y) + \frac{1}{\varepsilon} (y - p(y))
$$
donc on vérifie qu'il appartient bien à $V_1$ par la même méthode.

#### Question 6

La fonction $h$ est bijective ; de plus par linéarité de la différentielle
$$
dh(x) = d(p(x) + \varepsilon (x- p(x))) = \varepsilon I + (1-\varepsilon) dp(x)
= \varepsilon I + \frac{1 - \varepsilon}{\|x\|} P(x). 
$$
De façon analogue, on montre que $dh^{-1}$ existe et que
$$
dh^{-1}(y) = \varepsilon^{-1}I + \frac{1 - \varepsilon^{-1}}{\|y\|} P(y).
$$
Ces deux matrices dépendent continûment de leur arguments respectifs. 
La fonction $h$ est donc un $C^1$-difféomorphisme.


#### Question 7

Pour tout $x \in U$, le vecteur $n(x)$ étant unitaire, il existe une rotation 
$R \in \R^{2\times 2}$ telle que $R \cdot n(x) = e_1 := (1,0)$. On a $R \cdot R^{\top} =I$
et donc $\det R \times \det R^{\top} = 1$. Par conséquent
$$
\begin{split}
\det dh(x) &= \det R \times \det dh(x) \times \det R^{\top} \\
&= \det \left(R \left(\varepsilon I  + \frac{1 - \varepsilon}{\|x\|} (I - n(x) \cdot n(x)^{\top}) \right) R^{\top}\right) \\
&= \det \left(\left(\varepsilon I  + \frac{1 - \varepsilon}{\|x\|} (I - e_1 \cdot e_1^{\top}) \right) \right) \\
&= \det \left[ 
\begin{array}{cc}
\varepsilon & 0 \\
0 & \varepsilon + \frac{1 - \varepsilon}{\|x\|} \\
\end{array} 
\right]
\\
&=\varepsilon\left(\varepsilon + \frac{1 - \varepsilon}{\|x\|} \right).
\end{split}
$$

## Calcul Intégral


#### Question 8

Il y a plusieurs façons d'aborder cette question. Géométriquement, 
dans le cadre de la théorie de la mesure tout d'abord : on remarque 
que l'intégrale à calculer est par définition la mesure 
de l'aire de l'ensemble $S$ (sous réserve que l'intégrale existe, ce que l'on nous
demande d'admettre). Comme $S = [0,2]\times [0,2]$ est un pavé de $\mathbb{R}^2$, 
son aire est le carré de la longueur de l'intervalle $[0,2]$, qui est
$2 - 0 = 2$. Par conséquent,
$$
\int_{\mathbb{R}^2} 1_S(x) \, dx = 2^2 = 4.
$$
Alternativement, nous pouvons mener un calcul direct de l'intégrale : 
la fonction caractéristique $1_S$ vérifie pour tout $(x_1, x_2) \in \R^2$
$$
1_S(x_1, x_2) = 1_{[0, 2]}(x_1) \times 1_{[0, 2]}(x_2)
$$
Si l'on admet que la fonction est intégrable, alors par le théorème de Fubini,
$$
\int_{\R^2} 1_S(x) \, dx = \int_{\R} \left[\int_{\R} 1_S(x_1, x_2) \, dx_1\right] \, dx_2
$$
et par conséquent, par linéarité et le théorème fondamental du calcul
\begin{align*}
\int_{\R^2} 1_S(x) \, dx 
&= \int_{\R} \left[\int_{\R} 1_{[0, 2]}(x_1) \times 1_{[0, 2]}(x_2) \, dx_1\right] \, dx_2 \\
&= \int_{\R} 1_{[0, 2]}(x_2) \left[\int_{\R} 1_{[0, 2]}(x_1) \, dx_1\right] \, dx_2 \\
&= \int_{\R} 1_{[0, 2]}(x_1) \, dx_1 \times \int_{\R} 1_{[0, 2]}(x_2) \, dx_2 \\
&= \int_{0}^2 dx_1 \times \int_{0}^2 dx_2 \\
& = [x_1]_0^2 \times [x_2]_0^2 \\
& = 2 \times 2 \\
&=4.
\end{align*}

#### Question 9

Pour tout $t>0$, on a $(-t(\ln t - 1))' = -(\ln t - 1) - t(1/t) = -\ln t$ 
(la fonction est dérivable comme produit de fonctions dérivables).
Pour tout $\varepsilon \in \left]0, 2\right]$, la fonction
$t \in [\varepsilon, 2] \mapsto -\ln t$ est continue sur un intervalle fermé
borné de $\R$ donc y est intégrable ;
donc, par le théorème fondamental du calcul,
\begin{align*}
\int_{\varepsilon}^2 (- \ln t) \, dt 
&= \left[ -t(\ln t - 1) \right]_{\varepsilon}^2 
= -2(\ln 2 - 1) + \varepsilon (\ln \varepsilon -1) \\
& \to -2(\ln 2 - 1) \; \mbox{ quand } \;
\varepsilon \to 0, \, \varepsilon >0.  
\end{align*}


Si pour tout $k \in \N$, nous définissons $f_k :\R \to \R$ par
$$
f_k(t) = \left| 
\begin{array}{rl}
- \ln t & \mbox{ si $t \in [2^{-k}, 2]$,} \\
0 & \mbox{sinon,}
\end{array}
\right.
$$
alors par additivité, on a affaire à une suite croissante de fonctions intégrables, 
telle que
$$
\lim_{k\to +\infty} \int_{\R} f_k(t) \, dt \to -2(\ln 2 - 1) \; \mbox{ quand $k \to +\infty$.}
$$
Cette suite de fonction
converge simplement vers la fonction $f: \mathbb{R} \to \mathbb{R}$ 
égale à $-\ln t$ quand $t \in \left]0, 2\right]$ et nulle sinon. 
Par le théorème de convergence
monotone, cette fonction est donc intégrable sur $\R$, 
tout comme sa restriction à $[0,2]$.

Si l'on pose la même question pour une fonction $g: \mathbb{R} \to \mathbb{R}$ 
égale à $-\ln t$ quand $t \in \left]0, 2\right]$ et valant des valeurs arbitraires
sinon, la réponse est identique. En effet sur $[0,2]$, la restriction de $g$ 
ne diffère de la restriction de $f$ que sur le singleton $\{0\}$ (ou pas du tout). 
Comme il s'agit d'un ensemble négligeable, $g$ est intégrable sur $[0,2]$ car
$f$ est intégrable sur $[0,2]$.


#### Question 10

Pour tout $x_2 \in \left]0,2\right]$, la fonction 
$x_1 \in \left[0, 2 \right] \mapsto \ln \left(x_1 + \sqrt{x_1^2 + x_2^2}\right)$
est dérivable par la règle de dérivation en chaîne et
\begin{align*}
\partial_{x_1} \left(\ln \left(x_1 + \sqrt{x_1^2 + x_2^2}\right)\right) 
&= \frac{1}{x_1 + \sqrt{x_1^2 + x_2^2}}\left(1+ \frac{2x_1}{2\sqrt{x_1^2+x_2^2}}\right)\\
&= \frac{1}{x_1 + \sqrt{x_1^2 + x_2^2}}\frac{\sqrt{x^2+y^2} + x}{\sqrt{x_1^2+x_2^2}}\\
&= \frac{1}{\sqrt{x_1^2+x_2^2}}.
\end{align*}

Si $x_2 \in \left]0,2\right]$, 
la fonction $x_1 \in \left[0, 2\right] \mapsto 1/\sqrt{x_1^2 + x_2^2}$ est définie
(sur un intervalle fermé borné de $\mathbb{R}$)
et continue, donc intégrable. Par le théorème fondamental du calcul, on
a donc
$$
\int_0^2 \frac{1}{\sqrt{x_1^2+x_2^2}} \, dx_1 = \ln \left( \frac{2 +\sqrt{4+x_2^2}}{x_2} \right).
$$

#### Question 11

La frontière $\partial S$ de $S$ est donnée comme union de quatre pavés :
$$
[0,2] \times [0,0], \, [0,2] \times [2,2], \, [0,0] \times [0,2] \mbox{ et } [2,2] \times [0,2].
$$
Les intervalles $[0,0]$ et $[2,2]$ étant de longueur nulle, l'aire de chacun
de ces pavés est nulle ; chaque pavé est donc négligeable et leur union est
donc négligeable.

La fonction étudiée est donc mesurable car continue presque partout
(partout sauf sur $\partial S$, qui est négligeable). 
Elle est également positive ; on peut donc exploiter
le théorème de Tonelli pour tenter de prouver son intégrabilité. 
Pour presque tout $x_2 \in \R$ (à part pour $x_2=0$), 
la fonction partielle $x_1 \mapsto 1_S(x_1, x_2) / \|(x_1,x_2)\|$ est intégrable et
$$
 \int_{\R} \frac{1_S(x,y)}{\|(x_1,x_2)\|}\, dx_1 
= \phi(x_2) := \left|
\begin{array}{rl}
\ln \left(\left({2 +\sqrt{4+x_2^2}}\right) /{x_2} \right) & \mbox{si $x_2 \in \left]0,2\right]$,} \\
0 & \mbox{sinon.}
\end{array}
\right.
$$
Il nous suffit donc d'établir que cette fonction $\phi$ 
est intégrable pour pouvoir conclure que la fonction de départ est intégrable.
Or pour tout $x_2 \in \left]0,2\right]$, 
$$
0 \leq \ln \left(\frac{2 +\sqrt{4+x_2^2}}{x_2}\right) \leq \ln (2+2\sqrt{2}) - \ln x_2
$$
et le second membre de cette équation est (défini presque partout et) 
intégrable sur $\left[0,2\right]$ d'après la question 9.
La fonction $\phi$, mesurable d'après le théorème de Tonelli, 
est donc bien intégrable par le critère d'intégrabilité dominée.
Le théorème de Tonelli nous garantit donc l'intégrabilité de la fonction
de départ.

#### Question 12


Si $f$ est bornée par la constante $M$, la fonction $f\circ p$ 
est bornée par la même constante $M$. Soit $\overline{f \circ p}$ le prolongement
de $f \circ p$ par zéro à $\R^2$.
Comme $V_{\varepsilon} \subset S$, la fonction
 $1_{V_{\varepsilon}} \overline{f \circ p}$ est dominée par $1_{S} M$.
La fonction $1_{S} M$ étant intégrable et $1_{V_{\varepsilon}}\overline{f \circ p}$ 
étant mesurable comme produit de fonctions mesurables ($V_{\varepsilon}$ est ouvert,
donc mesurable, ce qui garantit que $1_{V_{\varepsilon}}$ est mesurable),
l'intégrale 
$$
\frac{1}{2\varepsilon} \int_{\R^2} 1_{V_{\varepsilon}}(y) \overline{f \circ p}(y) \, dy =
\frac{1}{2\varepsilon} \int_{V_{\varepsilon}} f(p(y)) \, dy
$$ est bien définie.

#### Question 13
On appliquer le changement de variable $y=h(x)$ pour se
ramener d'une intégrale sur $V_{\varepsilon} = h(V_1)$ à une intégrale sur $V_1$.
En exploitant le fait que $p(h(x)) = p(x)$, on obtient :
\begin{align*}
 \frac{1}{2\varepsilon} \int_{V_{\varepsilon}} f(p(y)) \, dy 
&= \frac{1}{2\varepsilon} \int_{V_{1}} f (p(h(x)) |\det J_{h}(x)| \, dx \\
&= \frac{1}{2\varepsilon} \int_{V_1} f(p(x)) |\det J_{h}(x)| \, dx \\
&= \frac{1}{2 \varepsilon} \int_{V_1} f(p(x)) \, \varepsilon \! \left(
\varepsilon + \frac{1-\varepsilon}{\|x\|} \right) \, dx \\
&= \frac{1}{2} \int_{V_1} f(p(x)) \left(
\varepsilon + \frac{1-\varepsilon}{\|x\|} \right) \, dx
\end{align*}

#### Question 14
Comme pour tout $x\neq 0$,
$$
\left|\overline{f \circ p}(x)1_{V_1}(x) \left(
\varepsilon + \frac{1-\varepsilon}{\|x\|} \right) \right|
\leq M 1_S(x) \left(
\varepsilon + \frac{1-\varepsilon}{\|x\|} \right)
\leq M 1_S(x) \left(
1 + \frac{1}{\|x\|} \right)
$$
et que le membre de droite est intégrable (d'après la question 11), 
on peut passer à la limite sur $\varepsilon$ par le théorème de convergence 
dominée dans l'équation de la question 13. On obtient alors
$$
\lim_{\substack{\varepsilon \to 0\\\varepsilon \in \left]0, 1\right]}}
\frac{1}{2\varepsilon} \int_{V_{\varepsilon}} (f \circ p) (x) \, dx
= \frac{1}{2} \int_{V_1} \frac{(f \circ p)(x)}{\|x\|} \, dx.
$$


## Probabilités

<!--
#### Question 0
Si l'ensemble $P := \{(x, y, z) \in \R^3 \; | \; f_{(X,Y,Z)}(x, y, z) \neq 0 \}$
était négligeable, alors comme $f$ est identiquement nulle
sur $P^c$, on aurait
$$
\int_{\R^3} f_{(X, Y, Z)}(x, y, z) \, dxdydz = \int_{P} f(x, y, z) \, dxdydz + \int_{P^c} 0 \, dxdydz
= 0 + 0 = 0.
$$
Mais comme $f_{(X, Y, Z)}$ est une densité, il est nécessaire que cette intégrale soit égale à $1$. L'ensemble $P$ ne peut donc pas être négligeable.
-->

#### Question 1

La densité du triplet $(X, Y, Z)$ étant invariante par rotation,
elle est de la forme $f_{(X,Y,Z)} (x, y, z) = \phi(x^2 + y^2 + z^2)$. 
De plus, les variables $X, Y$ et $Z$ étant indépendantes, on a
$$f_{(X,Y,Z)} (x, y, z) = f_X (x)f_Y (y)f_Z (z) \; \mbox{ pour tout $(x, y, z) \in \R^3$.} $$ 
Soit $(x_0,y_0,z_0) \in \R^3$ ; comme $\phi(x_0^2 + y_0^2 + z_0^2) > 0$ on a
$f_{(X, Y, Z)}(x_0, y_0, z_0) > 0$
et donc $f_X(x_0) \neq 0$,
$f_Y(y_0) \neq 0$ et $f_Z(z_0) \neq 0$. Pour tout $x \in \R^3$, comme
$$
f_X(x) f_Y(y_0) f_Z(z_0) = \phi(x^2 + y_0^2 + z^2) = \phi(y_0^2 + x^2 + z_0^2)
= f_X(y_0) f_Y(x) f_Z(z_0),
$$
on a l'égalité
$$
f_X(x) = \frac{f_X(y_0)}{f_Y(y_0)} f_Y(x).
$$
Comme on a par ailleurs
$$
\int_{-\infty}^{+\infty} f_X(x) \, dx = \int_{-\infty}^{+\infty} f_Y(x) \, dx = 1,
$$
il est nécessaire que le ratio ${f_X(y_0)}/{f_Y(y_0)}$ soit égal à $1$. 
On a donc $f_X = f_Y$ ;  la preuve que 
$f_Y = f_Z$ s'obtient de manière similaire.

Pour finir, puisque pour tout $x \in \R$ on a
$f(x)^3 = f_{(X, Y, Z)}(x, x, x) = \phi(3 x^2) > 0$, 
la fonction $f$ est bien positive en tout point.

#### Question 2

L’égalité
$$f(x)f(y)f(z) = \phi(x^2 + y^2 + z^2 )  \; \text{ pour tout } (x, y, z) \in \R^3$$
implique $f (x)f'(y)f (z) = 2y\phi' (x^2 + y^2 + z^2 )$ 
et $f' (x)f (y)f (z) = 2x\phi' (x^2 + y^2 + z^2 ).$ On en déduit que 
$$xf (x)f' (y)f (z) = f' (x)yf (y)f (z)  \; \text{ pour tout } (x, y, z) \in \R^3.$$

Soit $(x, y_0, z_0) \in \mathbb{R}^3$ avec $y_0 \neq 0$ ; on a $f(x) > 0$,
$f(y_0) > 0$ et $f(z_0) > 0$. En posant 
$$
c = \frac{f'(y_0) f(z_0)}{y_0 f(y_0) f(z_0)},
$$
on voit que
$$f' (x) = cxf(x) \; \mbox{pour tout $x \in \R$.}$$
On peut réécrire cette équation différentielle sous la forme
$$
(\ln f(x))' = cx.
$$
En intégrant les deux membres de l'équation entre $0$ et $x$, on obtient
$$
\ln f(x) - \ln f(0) = c\frac{x^2}{2}
$$
et donc
$$
f(x) = f(0) e^{c x^2/2},
$$
ce qui est bien la forme cherchée $f(x) = a e^{cx^2/2}$.

#### Question 3

Comme $\int_\R f (x) dx = 1$, on a nécessairement $c < 0$ et on en déduit que
$$f (x) = \frac{1}{\sqrt{2\pi \sigma^2}}\exp\left(-\frac{x^2}{2\sigma^2}\right).$$ 
Les variables aléatoires $X$, $Y$ et $Z$ suivent donc loi gaussienne centrée 
et la covariance du vecteur est $\sigma^2 I_3$, où $I_3$ est la matrice identité.

#### Question 4
On a 
$$\frac{1}{2} m\Esp(\|V \|^2 ) = \frac{1}{2} m\Esp(V_1^2 +V_2^2 + V_3^2).$$ 
Comme $\Esp(V_i^2) = \sigma^2$, on en déduit que $E_c = \frac{3}{2}m \sigma^2$
et par conséquent que 
$$\sigma^2 = \frac{kT}{m}.$$


#### Question 5

À l’aide de la méthode de la fonction muette, on montre que $V_1^2$ suit une loi gamma de paramètres $(1/2,\frac{1}{2\sigma^2})$. En effet, en appliquant le changement de variable $y=x^2$ sur $\R_-^\ast$ et $\R_+^\ast$, on obtient :
$$f_{V_1^2} (y) = \left(f(-\sqrt{y}) + f(\sqrt{y})\right) \frac{1}{2\sqrt{y}} 1_{]0,+\infty[}(x) = f(\sqrt{y}) \frac{1}{\sqrt{y}} 1_{]0,+\infty[}(x)$$
par parité de $f$, soit
\begin{align*}
f_{V_1^2} (y) &= \frac{1}{\sqrt{\pi}}\left(\frac{1}{2\sigma^2}\right)^{1/2} y^{-1/2} \exp\left(-\frac{y}{2\sigma^2}\right)\\
              &= \frac{1}{\Gamma(1/2)}\left(\frac{1}{2\sigma^2}\right)^{1/2} y^{-1/2} \exp\left(-\frac{y}{2\sigma^2}\right)
\end{align*}
On déduit de l'indication que $\|V\|^2 = V_1^2 +V_2^2 + V_3^2$ suit une loi gamma de paramètres $(3/2,\frac{1}{2\sigma^2})$.
Sa densité est
$$f_{\|V\|^2}(x) = \frac{1}{\sqrt{2\pi}\sigma^3}\sqrt{x} e^{- x/2\sigma^2}1_{]0,+\infty[}(x).$$

À l’aide de la méthode de la fonction muette, en appliquant le changement de variable $v = \sqrt{x}$ sur $\R_+^\ast$ et avec $\sigma^2 = \frac{kT}{m}$, on montre enfin que $\|V\|$ est une variable de densité :

$$f_{\|V\|}(v) = \frac{\sqrt{2}}{\sqrt{\pi}}\left(\frac{m}{kT}\right)^{3/2}v^2 e^{- mv^2/2kT} 1_{]0,+\infty[}(v).$$

Il s’agit de la densité de la loi de Maxwell.