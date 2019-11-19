% Calcul Intégral V

<!-- LaTeX Macros -->
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

Objectifs
================================================================================


### TODO -- Basique


### TODO -- Standard


### TODO -- Avancé


### TODO -- Hors-programme



Dérivées faibles
================================================================================

**Intro à creuser.** "Généraliser" la dérivée mais pourquoi ? Quels uses cases ?


**Motivation:** étendre la notion de dérivation pour traiter des uses cases 
comme les équations différentielles avec second membre discontinu en $t$, 
sans "bricolage" (qui serait: résoudre portion par portion et recoller
par continuité, si l'on suppose que l'on est $C^1$ par morceaux).
Motivation analogue pour les probas: variable aléatoire à densité
uniforme sur $[0,1]$: $p$ n'est pas (partout) la dérivée de $F$.

Dans les deux cas néanmoins, on a le même schéma ou la "dérivée" 
permet d'obtenir la fct originale par intégration.
(pour les ODEs, pour travailler sur $\R$, prolonger rhs par $0$
pour $t\neq 0$ et $x(t)$ par $x_0$.)

Idée: dérivation initialement source de définition de l'intégrale (de Newton);
l'intégration est une opération inverse, mais sait aussi intégrer
des fonctions qui ne sont *pas* des dérivées (exemple).
On peut retourner le problème et définir une nouvelle notion,
généralisée de dérivée, à partir de l'intégrale.

### Dérivée faible {.definition}
La fonction $f:\R \to \R$ est *dérivable faiblement* s'il existe une 
fonction $g:\R \to \R$ localement absolument<!--[^foo]--> intégrable,
c'est-à-dire mesurable et dont la valeur absolue soit intégrable sur
tout intervalle compact $[a, b] \subset \R$
$$
\int_a^b |g(x)|\, dx < + \infty,
$$
et une constante $c \in \R$ 
telles que pour tout $x \in \R$, 
$$
f(x) = c + \int_0^x g(t) \, dt.
$$
La fonction $g$ est alors appelée *dérivée faible* de $f$.

### Les fonctions faiblement dérivables sont continues.

### Démonstration {.proof}
La continuité des intégrales indéterminées, de la forme
$$
x \in \R \mapsto \int_a^x h(t) \, dt
$$
est prouvée dans le chapitre "Calcul Intégral I" au moyen du lemme de Henstock, 
sous l'hypothèse que $h$ est intégrable (pour un réel étendu $a$ arbitraire). 
Or tout $r>0$, la fonction $h = g 1_{[-r,r]}$ est intégrable. 
Comme pour tout $x \in \left]-r, r\right[$,
$$
\int_0^x g(t) \, dt = \int_0^x h(t) \, dt,
$$
l'intégrale indéterminée de $g$, et donc $f$, est continue en $x$. 
Le choix de $r$ étant arbitraire, $f$ est continue sur $\R$ tout entier.


### Dérivée faible et classique
Si une fonction $f: \R \to \R$ est faiblement dérivable, de dérivée faible $g$,
alors elle est dérivable (classiquement) presque partout, et $f' = g$ presque
partout. On a donc pour tout $x \in \R$,
$$
f(x) = f(0) + \int_0^x f'(t) \, dt.
$$

### 
En particulier, la dérivée faible d'une fonction, si elle existe, est unique
presque partout.

### Démonstration {.proof}
Une conséquence directe du résultat de 
[dérivation des intégrales indéterminée](Calcul Intégral II.pdf/#DII).

<!--
[^foo]: si $f$ est conditionnellement intégrable, l'application
$$
\phi \in D^0(\R) \mapsto \int f \phi 
$$
n'est pas (nécessairement ?) bornée, $f$ ne peut donc pas être représentée
comme une mesure, contrairement aux fonctions absolument continue. 
C'est trop tôt à ce stade pour parler de ça, mais la motivation est 
importante pour se limiter aux fonction absolument continues ...
-->

### Valeur absolue {.example #example-abs}
La fonction valeur absolue $|\cdot|: x \in \R \mapsto |x|$ est faiblement dérivable.
En effet, elle est dérivable presque partout (sauf en $0$),
sa dérivée classique valant $1$ quand $x>0$ et $-1$ quand $x < 0$.
Ses seules dérivées faibles potentielles sont dont les fonctions
égales presque partout à la fonction signe
$$
\mbox{sgn}(x) := \left| 
\begin{array}{rl}
-1 & \mbox{si $x<0$,} \\
0 & \mbox{si $x=0$,} \\
+1 & \mbox{si $x>0$.}
\end{array}
\right.
$$
De plus, pour tout $x\geq 0$ on a bien
$$
|x| = x = \int_0^x dt = 0 + \int_0^x \mbox{sgn}(t) \, dt
$$
et pour $x < 0$, 
$$
|x| = -x = \int_0^x - dt = 0 + \int_0^x \mbox{sgn}(t) \, dt.
$$
La fonction $|\cdot|$ est bien faiblement dérivable, de dérivée faible la fonction 
$\mbox{sgn}$.

![](images/abs.py)\ 

On peut remarquer que la fonction signe n'est pas elle-même faiblement
dérivable. Elle est bien dérivable presque partout (sauf en $0$) ;
sa dérivée est nulle presque partout. Si elle était faiblement dérivable,
on aurait donc pour tout $x \in \R$,
$$
\mbox{sgn}(x) = \mbox{sgn}(0) + \int_0^x 0 \, dt = 0,
$$
ce qui n'est pas le cas. On peut aussi remarquer qu'elle n'est pas continue
et par conséquent qu'elle ne peut pas être faiblement dérivable.

<!--
### Fonction régulières par morceaux {.definition}
On dira qu'une fonction $f: \R \to \R$ est *dérivable par 
morceaux* -- respectivement, *continûment dérivable par morceaux* --
s'il existe une collection dénombrable d'intervalles compacts $[a_k, b_k]$
sans chevauchements recouvrant $\R$ telle que la restriction de $f$ à 
tout $\left]a_k, b_k\right[$ puisse être prolongée en une fonction différentiable 
-- respectivement continûment dérivable -- sur $[a_k, b_k]$. 
-->

### Fonctions continûment différentiables par morceaux {.theorem}
Toute fonction $f: \R \to \R$  continue et continûment dérivable par morceaux 
est faiblement dérivable.

### {.post}
A noter que l'on peut être différentiable par morceaux mais pas
continue ; dans ce cas on ne peut pas être faiblement dérivable.
La fonction signe de [l'exemple consacré à la dérivée faible de
la valeur absolue](#example-abs) est un bon exemple de fonction
continûment dérivable par morceaux mais qui n'est continue et donc
pas faiblement dérivable.


### Démonstration {.proof}
<!--
On trouve dans [@Tao11, prop. 1.6.41, p. 176] la clé de la démonstration,
à savoir que si une fonction $f: [a, b] \to \R$ est différentiable 
et de dérivée absolument intégrable, alors 
$$
f(b) - f(a) = \int_a^b f'(x) \, dx. 
$$
Nous omettons ici cette portion critique ; 
la suite de la démonstration est beaucoup plus simple. 
-->
Notons $f(b^-)$ et $f(a^+)$ les limites à gauche de $f$ en $b$ et
à droite de $f$ en $a$ respectivement.
Remarquons tout d'abord que si la fonction $f$ est continûment dérivable sur 
$\left]a, b\right[$ et que sa dérivée y est prolongeable par continuité sur
$[a, b]$, alors on peut prolonger la restriction de $f$ à $\left]a, b\right[$
en une fonction (continûment) dérivable sur $\R$. L'application du 
théorème fondamental du calcul fournit alors
$$
f(b^-) - f(a^+) 
= 
\int_{a}^{b} f'(x) \, dx.
$$

Supposons désormais que $\R$ soit recouvert par des intervalles 
$[a_k, b_k]$ sans chevauchement, indexés par des entiers relatifs 
$k$ consécutifs ordonnés de façon croissante et que sur chaque 
$\left]a_k, b_k\right[$ la fonction $f$ soit dérivable, avec une dérivée ayant un prolongement
par continuité à $[a_k, b_k]$.

On déduit de l'énoncé précédent que 
$$
\int_{a_k}^{b_k} f'(x) \, dx = f(b^-) - f(a^+) = f(b) - f(a)
$$
et si $a_k < x < b_k$,
$$
f(x) - f(a) = f(x) - f(a^+) = \int_a^x f'(t) \, dt
$$
et 
$$
f(x) - f(b) = - (f(b^-) - f(x)) = - \int_x^b f'(t) \, dt = \int_b^x f'(t) \, dt.
$$
<!-- Suppons que les intervalles $[a_k, b_k]$ soient indexés par des entiers relatifs 
$k$ consécutifs et ordonnées de façon croissante. -->
Si $x$ est réel positif, que $0 \in [a_i, b_i]$ et que $x \in [a_j, b_j]$, 
on a donc
$$
\begin{split}
f(x) - f(0) &= (f(x) - f(a_j)) + (f(b_{j-1}) - f(a_{j-1})) + \dots + (f(a_i) - f(0)) \\
& = \int^x_{a_j} f'(t) \, dt + \int_{a_{j-1}}^{b_{j-1}} f'(t) \, dt + \dots + \int_0^{a_i} f'(t) \, dt.
\end{split} 
$$
et donc
$$
f(x) = f(0) + \int_0^x f'(t) \, dt.
$$
Le cas d'un réel $x$ négatif se traite de façon similaire.

### Fonction de répartition et densité de probabilité
La fonction $F: \R \to \R$ définie par 
$$
F(x) = \int_{-\infty}^x \frac{\exp (-{t^2}/{2})}{\sqrt{2\pi}} \, dt
$$
est une fonction de répartition, associée à la loi normale centrée réduite. 
Elle est faiblement dérivable ; en effet, son intégrande est localement absolument intégrable 
(il est positif et intégrable sur $\R$, d'intégrale $1$) 
et l'on a par additivité de l'intégrale pour tout $x\in\R$
$$
F(x) = F(0) + \int_{0}^x \frac{\exp (-{t^2}/{2})}{\sqrt{2\pi}} \, dt.
$$
Cett relation montre également que la fonction 
$$
f : t \in \R \mapsto  \frac{\exp (-{t^2}/{2})}{\sqrt{2\pi}}
$$
est une dérivée faible de $F$<!--([^eaf])-->. 

![skdjslkdjs](images/gauss.py)\ 

### {.ante .post}
Plus généralement, on a :

### Densité et dérivée faible {.proposition}
Une fonction de répartition $F:\R \to \R$ admet une densité si et seulement
si elle est faiblement dérivable. Une fonction $f:\R \to \R$ est une densité 
associée à $F$ si et seulement si elle est une dérivée faible de $F$
(elle est donc déterminée uniquement presque partout par $F$).

### Démonstration {.proof}
Sachant qu'une densité est localement absolument intégrable (car positive et
intégrable), la preuve qu'une fonction de répartition admettant une densité est 
faiblement dérivable et que les deux fonctions coïncident résulte directement de
l'égalité
$$
F(x) = \int_{-\infty}^x f(t) \,dt = \int_{-\infty}^0 f(t)\, dt + \int_0^x f(t) \, dt.
$$

Réciproquement, si $F$ est une fonction de répartition faiblement dérivable,
c'est-à-dire s'il existe une fonction $f:\R \to \R$ localement absolument
intégrable et une constante $c$ telle que pour tout $x\in\R$,
$$
F(x) = c + \int_0^x f(t) \, dt,
$$
alors pour toute paire de réels $a \leq b$, on a
$$
F(b) - F(a) = \int_a^b f(t) \, dt.
$$
La fonction $f$ est donc positive presque partout : en effet la fonction $F$
est dérivable en presque tout point $x \in \R$, de dérivée $f(x)$. 
Si l'on avait $f(x) < 0$, alors pour $h>0$ suffisamment petit, 
on aurait donc
$$
\frac{F(x+h) - F(x)}{h} < 0,
$$
ce qui contredirait le fait que $F$ est croissante. On obtient alors
la relation
$$
F(x) = \int_{-\infty}^x f(t) \, dt
$$
en posant $x=b$ et en passant à la limite $a \to -\infty$ en exploitant le
fait que $F$ a pour limite $0$ en $-\infty$ ; 
le résultat est justifié par le théorème de convergence monotone.
 
Le passage à la limite $x \to +\infty$ fournit alors 
$$
\int_{-\infty}^{+\infty} f(t) \, dt = 1,
$$
à nouveau justifié par application du théorème de convergence monotone, 
en exploitant le fait que $F$ a pour limite $1$ en $+\infty$.


<!--
[^eaf]: Cette fonction $f$ est ici la dérivée classique de $F$ en tout point
(et pas seulement presque partout), car la fonction $f$ est continue en tout 
point $x \in \R$. On a donc
$$
\begin{split}
\left|\frac{F(x+h) - F(x)}{h} - f(x)\right| &=  
\left|\frac{1}{h}\int_x^{x+h} (f(t) - f(x)) \, dt \right| \\
& \leq 
\frac{1}{h}\int_x^{x+h} |f(t) - f(x)| \, dt \\
&\leq \max \, \{ |f(t) - f(x)| \; | \; t \in [x - |h|, x + |h|]\} 
\end{split}
$$
Le taux d'accroissement de $F$ en $x$ tend donc vers $f(x)$ quand $h$ tend vers $0$.
-->


### Warning {.post}
Une fonction peut également être continue et dérivable par morceaux, 
mais de dérivée non localement absolument intégrable, 
auquel cas elle n'est pas non plus faiblement dérivable. 
Ainsi, la fonction $f:\R \to \R$ définie par
$$
f(x) = \left|
\begin{array}{cl}
x^2 \sin 1/x^2 & \mbox{si $x\geq 0$,} \\
0 & \mbox{sinon.}
\end{array}
\right.
$$
est dérivable en tout point (et donc continue), mais sa dérivée n'est
que conditionnellement intégrable sur $[0, 1]$ par exemple, pas absolument
intégrable (cf. [Calcul Intégral II](Calcul Intégral II.pdf)).

### Fonction de Cantor {.remark}
On pourrait croire en prenant connaissance des contre-exemples simples
à l'existence d'une dérivée faible que dès lors qu'une fonction est continue
a une dérivée presque partout et que cette dérivée est localement absolument 
intégrable, elle est faiblement dérivable. Mais ça n'est pas le cas !

Ainsi la fonction de Cantor $f:\R \to \R$ est un exemple de fonction
continue, de dérivée (classique) définie et nulle presque partout et
pourtant telle que $f(0)=0$ et $f(1)=1$, ce qui contredit la relation
$$
f(1) = f(0) + \int_0^1 0\, dt
$$
qu'elle devrait vérifier si elle était faiblement dérivable.

La fonction de Cantor $f$ est définie comme la limite des
suites de fonctions $f_n:\R \to \R$ données par 
$$
f_0(x) = 
\left|
\begin{array}{rl}
0 & \mbox{si $x<0$,} \\
x & \mbox{si $0\leq x\leq 1$,} \\
0 & \mbox{si $1< x$.} \\
\end{array}
\right.
$$
et pour tout $n\geq 1$
$$
f_{n+1}(x) = \left|
\begin{array}{rl}
0.5 \times f_n(3x) & \mbox{si $x < 1/3$}, \\
0.5 & \mbox{si $1/3 \leq x < 2/3$}, \\
0.5 + 0.5 \times f_n(3x-2) & \mbox{si $2/3 \leq x$}.
\end{array}
\right.
$$

![Approximation d'ordre $5$ de la fonction de Cantor](images/devil-staircase.py)

### TODO -- interprétation probabiliste.

(y compris -- ou plutôt surtout -- pour les fonctions intermédiaires 
qui sont "uniformes par morceaux". L'interprétation de la limite n'a
pas besoin d'être formalisée.)

<!--
### Absolue continuité {.definition}
Soit $I$ un intervalle de $\R$.
Une fonction $f:I \to \R$ est *absolument continue* si et seulement si
pour tout $\varepsilon > 0$, il existe un $\delta > 0$ tel que pour toute
collection finie d'intervalles compacts $([a_k, b_k])_{k=0}^{n-1}$ de $I$ 
ne se chevauchant pas, on ait
$$
\sum_{k=0}^{n-1} (b_k - a_k) \leq \delta
\; \Rightarrow \; 
\sum_{k=0}^n |f(b_n) - f(a_n)| \leq \varepsilon.
$$
Elle est *localement absolument continue* si sa restriction à tout intervalle
compact $K$ de $I$ est absolument continue. 

### TODO 
ne se chevauchant pas est nécessaire (note Bartle : c'est crucial) ? 
Pas suffisant de se limiter aux subdivisions complètes ?

### Existence de dérivée faible et absolue continuité {.proposition}
Une fonction $f:\R \to \R$ admet une dérivée faible si et seulement si
elle est localement absolument continue.

### TODO -- Démonstration

### TODO -- exploitation (/ dérivée faible) et exemple de fct abs cont

### TODO -- Une notion plus permissive de dérivée faible ?
Il serait possible d'élargir la notion de fonction faiblement dérivable en exigeant
uniquement que $g$ soit localement intégrable au sens de Henstock-Kurzweil,
et non localement absolument intégrable. Comme toute dérivée est localement
intégrable au sens de Henstock-Kurzweil, cette extension aurait le mérite
de proposer une notion de dérivée faible qui soit une *vraie* extension de la
notion de dérivée classique (en l'état, il est possible qu'une fonction ait
une dérivée en tout point mais pas de dérivée faible ...).  
Néanmoins, aussi séduisante soit-elle, 
nous ne considérerons pas cette extension, car la classe des fonctions
faiblement dérivables serait alors sensiblement plus complexe à caractériser
que dans le cadre absolument continu que nous avons choisi[^ACG].

**TODO:** référence concrête à un exemple de dérivée non absolument intégrable
déjà traité.

**TODO:** faire le lien par exemple avec l'approche par IPP ou fct test 
(forme lin sur); qui ne marche pas avec conditionnellement intégrable.
Du coup, peut-être retarder la remarque ? Appendice ?

[^ACG]: Il s'agit d'une classe de fonctions absolument continues 
mais **généralisées**, notée $\mathrm{ACG}_*$, cf. [@Bar01, pp. 242-243].

-->


### {.ante}
Il existe une façon alternative pour caractériser les fonctions faiblement
dérivables qui repose sur l'usage de fonctions tests. Cette nouvelle approche
se prêtera mieux à la généralisation encore plus "aggressive" de la notion
de dérivée que nous allons aborder, la dérivation au sens des distributions.

### Fonctions tests
On note $D^k(\R)$ l'espace des fonctions continues $\varphi: \R \to \R$
dont le support
$$\mbox{supp } \varphi := \overline{\{x \in \R \; | \; \varphi(x) \neq 0\}}$$
est compact et qui sont continues si $k=0$ ou $k$ fois continûment différentiables
quand $k \geq 1$.


### Dérivation faible et fonctions tests
Une fonction localement absolument intégrable $f:\R \to \R$ 
est faiblement dérivable de dérivée faible la fonction 
localement absolument intégrable $g : \R \to \R$ 
si et seulement si pour tout $\varphi \in D^1(\R)$, on a
$$
\int_{-\infty}^{+\infty} g(t) \varphi(t) \, dt
=
-\int_{-\infty}^{+\infty} f(t) \varphi'(t) \, dt.
$$

### Démonstration {.proof}
Nous admettrons la démonstration dans le cas général et nous limitons à
la preuve du cas des fonctions $f$ et $g$ continûment différentiables par morceaux.
Dans ce cadre, une fonction est faiblement dérivable 
si et seulement si seulement si elle continue.

Supposons que cela soit le cas pour la fonction $f$.
Alors, si $\varphi \in D^1(\R)$,
le produit $f \varphi$ est continûment différentiable par morceaux et 
continu, de dérivée définie classiquement presque partout $f' \varphi + f \varphi'$.
Les deux termes de cette expression sont intégrables. De plus, pour $r>0$
assez grand et $|t| \geq r$, on a $\varphi(t) = 0$, donc
$$
\int_{-\infty}^{+\infty} f'(t) \varphi(t) \, dt 
+ \int_{-\infty}^{+\infty} f(t) \varphi'(t) \, dt
=
\int_{-r}^{+r} (f \varphi)'(t) \, dt
= 
[f \varphi]^{+r}_{-r} = 0.
$$
Réciproquement, supposons que $f$ et $g$ sont continûment différentiables et 
vérifient pour toute fonction $\varphi \in D^1(\R)$ l'égalité
$$
\int_{-\infty}^{+\infty} g(t) \varphi(t) \, dt
=
-\int_{-\infty}^{+\infty} f(t) \varphi'(t) \, dt.
$$
Soit $x>0$. Pour $0 < \varepsilon < x/2$, on définit la fonction 
$\psi_{\varepsilon} : \R \to \R$ par
$$
\psi_{\varepsilon}(t) =
\left| 
\begin{array}{rl}
-6 / \varepsilon^3  \times t  (t - \varepsilon) & \mbox{si $0 \leq t \leq \varepsilon$,} \\
6 / \varepsilon^3  \times (t - x + \varepsilon)  (t - x) & \mbox{si $x - \varepsilon \leq t \leq x$,} \\
0 & \mbox{sinon.}
\end{array}
\right.
$$
puis $\varphi_{\varepsilon} : \R \to \R$ par
$$
\varphi_{\varepsilon}(t) = \int_{-\infty}^t \psi_{\varepsilon}(s) \, ds.
$$

![Représentation de $\varphi_{\varepsilon}$ de sa dérivée quand $x=1$ et $\varepsilon=0.2$.](images/test-function.py) 

On vérifiera que les fonctions $\psi_{\varepsilon}$ ainsi construites 
appartiennent bien à $D^1(\R)$. Lorsque l'on fait tendre $\varepsilon$ vers $0$, 
le théorème de convergence dominée nous fournit
$$
\int_{-\infty}^{+\infty} g(t) \varphi_{\varepsilon}(t) \, dt
\to \int_{-\infty}^{+\infty} g(t) 1_{[0, x]}(t) \, dt
=
\int_0^{x} g(t) \, dt.
$$
D'autre part, on a 
\begin{multline*}
-\int_{-\infty}^{+\infty} f(t) \varphi'_{\varepsilon}(t) \, dt
= \\
\frac{6}{\varepsilon^3}
\left[\int_{0}^{\varepsilon} f(t) t  (t - \varepsilon) \, dt 
- \int_{x -\varepsilon}^x f(t) (t - x + \varepsilon)  (t - x) \, dt\right].
\end{multline*}
Le changement de variable $s = t / \varepsilon$ nous fournit
$$
\frac{6}{\varepsilon^3}
\int_{0}^{\varepsilon} f(t) t  (t - \varepsilon) \, dt
=
6
\int_{0}^{1} f(\varepsilon s) s (s - 1) \, ds
$$
et donc par le théorème de convergence dominée, 
en faisant tendre $\varepsilon$ vers $0$, 
$$
\frac{6}{\varepsilon^3}
\int_{0}^{\varepsilon} f(t) t  (t - \varepsilon) \, dt 
\to f(0^+) \times \left(6 \int_0^1 s(s-1) \, ds\right) = - f(0^+).
$$
En analysant de façon similaire le second terme, on aboutit à
$$
-\int_{-\infty}^{+\infty} f(t) \varphi'_{\varepsilon}(t) \, dt
\to 
f(x^-) - f(0^+),
$$
et donc
$$
f(x^-) = f(0^+) + \int_0^x g(t) \, dt.
$$
Le second membre étant continu par rapport à $x$ et $f$ supposé continue par
morceaux, elle est en fait continue et $f(x) = f(x^-)$. Le cas $x<0$ se traite
de façon similaire. La fonction $f$ admet donc $g$ comme dérivée faible.

Mesures signées et distributions
================================================================================

<!--
### TODO
Perspective fonction sans dérivée faible fonction (ex: fct avec saut),
mais qui peut être dérivée comme une mesure. Perspective de patch :
analyse de l'IPP pour les dérivées faibles et comment le rhs est une
forme linéaire sur $C_c$.

### Note
Sauf erreur, la définition "naturelle" (ressemblant) de mesure à valeurs
dans $\R$ ne garantit pas l'existence d'une décomposition de Hahn et ne
permet donc pas de se ramener au cas des mesures positives (cf. 
Dunford-Schwarz pour la preuve de ce résultat). Cela a donc du sens
d'insister sur une définition de mesure signée, prenant comme base une
mesure et une fonction de signe.
(à plus long-terme, j'aimerais un exemple de mesure à valeurs réelles
qui n'admet pas de décompo de Hahn)
-->

### TODO -- Mesure signée {.definition} 
Soit $(X, \mathcal{A})$ un ensemble mesurable.
Une *mesure signée* $\nu$ sur $(X, \mathcal{A})$ est une application
$$
\nu : \mathcal{A} \to \left]-\infty, +\infty\right[ \cup \{\bot\}
$$
pour laquelle il existe une mesure $\mu : \mathcal{A} \to [0, +\infty]$ 
et une application $\mu$-mesurable $\sigma: X \to \{-1, +1\}$ telles que
pour tout $A \in \mathcal{A}$,
$$
\nu(A) := \sigma \mu(A) := \int_A \sigma(x) \, \mu(dx)
$$
si l'application $1_A \sigma$ est $\mu$-intégrable 
et $\nu(A) = \bot$ sinon.

### TODO -- Mesure positive vers mesure signée
Expliquer "conversion" de $\inf$ vers $\bot$, règles de calcul avec $\bot$.
terminologie mesure positive.

### TODO -- Check pptés usuelles mesure ($\sigma$-add, etc.)
Warning : plus de monotonie !

### TODO -- Variation d'une mesure signée.
Soit $\nu = \sigma \mu$ une mesure signée sur $(X, \mathcal{A})$.
La mesure positive $\mu$ est uniquement déterminée par $\nu$.
La fonction $\sigma$ est déterminée $\mu$-presque partout par $\nu$.
On appelle $\mu$ la *variation de $\nu$* et on la note
$|\nu|$ ; on appelle $\sigma$ la fonction signe de $\nu$.

### TODO -- rk

Souligner parallèle avec valeur absolue, considérer le
cas particulier à densité.



<!--
### TODO
Comment on a défini $\mu$-intégrable dans le chapitre précédent ?
Précisément, est-ce qu'une intégrale avec "une valeur infinie" est
intégrable ? Le "problème", outre l'absence de cohérence par rapport
aux chapitres précédents, est qu'on peut alors avoir une fonction
intégrable, et la rendre non-intégrable en la multipliant par une
fonction de signe mesurable. OK, bon, intégrable veut dire intégrale
finie, le cas $+\infty$ sera a décrire comme une extension dans les
cas simples (comme fct mesurable positive non intégrable par exemple).

### TODO -- Convention $\bot$, absorption $\inf$ ou non ?
Disons pas d'absorption par défaut ? A voir, y réfléchir.
Avec absorption c'est plus simple quand même ...
-->

### TODO -- Décomposition de Hahn
(trivial, mais bon)



### TODO -- $\sigma$-additivité


### TODO 
$f$ $\mu-$intégrable à valeurs réelles fois $\mu$ défini une mesure signée

### TODO -- Intégrale par rapport à une mesure signée

### TODO
Downplay mesure de Radon à ce stade (boréliens pas connus).
Insister sur manip via les fonctions tests, exemples, etc. et uniquement
à la fin parler de Radon et de théorème de Riesz, en renvoyant à la seconde
partie. Ou même mettre ça dans la seconde partie ? Bref quoi qu'il en soit,
ne pas mettre ça sur le chemin critique.

### TODO -- Mesure de Radon
On appelle *mesure de Radon* sur $\R$ toute mesure signée sur
$(\R,\mathcal{B}(\R))$ telle que pour tout compact $K$ de $\R$,
$|\mu|(K) < +\infty$, c'est-à-dire $\mu(K) \neq \bot$.

<!--
Une mesure de Borel positive $\mu : \mathcal{B}(\R) \to [0, +\infty]$ est *de Radon* si :

  1. Pour tout compact $K \subset \R$, $\mu(K) < +\infty$ (*localement finie*).

  2. Pour tout $A \in \mathcal{B}(\R)$, 
     $$
     \mu(A) = \sup \{\mu(K) \; | \; \mbox{$K$ compact de $\R$}, \, K \subset A\}.
     $$
    (régularité intérieure).

  3. Pour tout $A \in \mathcal{B}(\R)$,
     $$
      \mu(A) = \inf \{\mu(V) \; | \; \mbox{$V$ ouvert de $\R$}, \, A \subset V\}.
     $$
    (régularité extérieure).

### TODO
(dans le cas réel, 2. et 3. sont gratuits ? Chercher. Je crois oui, cf
<https://www.lpsm.paris/cours/processus-html/node6.html> par exemple).
Supprimer de la def donc ... (éventuellement, faire une rq sur la régularité).
-->




### Formes linéaires continues sur $D^0(\R)$.
Une application linéaire $T: D^0(\R) \to \R$ 
-- c'est-à-dire une *forme linéaire* sur $D^0(\R)$ --
est dite *continue* si pour tout
intervalle compact $[a, b]$ de $\R$ et toute fonction $\varphi \in D^0(\R)$ dont
le support soit inclus dans $[a, b]$, il existe une constante $K$ telle que
$$
|T \cdot \phi| \leq K \sup_{x \in [a, b]} |\varphi(x)| = K \|\varphi|_{[a, b]}\|_{\infty}
$$


### Théorème de Riesz-Markov-Kakutani
Il existe une bijection entre l'ensemble des applications linéaire continues 
$T : D^0(\R) \to \R$ et l'ensemble des mesures de Radon $\mu$ sur $\R$, 
déterminée par la relation 
$$
\forall \, \varphi \in D^0(\R), \; T \cdot \varphi = \int \varphi \mu.
$$

### TODO -- Démonstration {.proof}
Si $\mu$ est une mesure de Radon sur $\R$, de la forme
$\mu = \sigma |\mu|$ où $\sigma$ ess une fonction borélienne à valeurs
dans $\{-1, 1\}$, alors la fonction
$$
T: \varphi \in D^0(\R) \mapsto \int \varphi \mu  = \int \varphi \sigma |\mu| \in \R
$$
est bien définie : $\varphi$ est continue donc $|\mu|$-mesurable ainsi que 
le produit $\varphi \sigma$ et si le support de $\varphi$ est inclus dans le compact 
$[a, b]$, alors
$$
|\varphi(y) \sigma(y)| \leq 1_{[a, b]}(y) \times \sup_{x \in [a, b]} |\varphi(x)|.
$$ 
Comme la mesure $\mu$ est de Radon, $|\mu|([a, b]) < +\infty$, donc
la fonction $\varphi \sigma$ est dominée par une fonction $|\mu|$-intégrable.
Elle est donc $|\mu|$-intégrable.

La fonction $T$ ainsi définie est également linéaire par linéarité de l'intégrale. 
De plus, si le support de $\varphi$ est inclus dans $[a, b]$, alors
$$
|T \cdot \varphi| 
\leq \int |\varphi| |\mu|
\leq \int \left(\sup_{x \in [a, b]}|\varphi(x)|\right) |\mu|
= |\mu|(A) \left(\sup_{x \in [a, b]}|\varphi(x)|\right).
$$
Elle est donc continue sur $D^0(\R)$.

TODO -- Renvoyer à un ref (Arverson ?) pour le reste.

### TODO
Représentation "concrête" des mesures de Radon dans $\R$ (via les fcts 
de variation localement bornée) ??? Ou pas ?

### TODO -- mesure de Radon (signée)
+ lien avec 

### TODO -- fct localement intégrable
... définie ("est") une mesure de Radon. Et la mesure détermine

### TODO

def intégrale fonction des bornes "dans le mauvais sens" ...

### Dérivée généralisée comme mesure
La fonction $f:\R \to \R$ admet comme *dérivée généralisée* la mesure de
Radon $\mu$ sur $\R$ s'il existe une constante $c$ telle que
pour tout $x \in \R$, 
$$
f(x) = c + \int_0^x \mu(dt).
$$


### TODO -- extension "p.p." ?
Aka fct de départ définie pp ? Là peut-être plus légitime que pour les
fcts, sinon quand il y a un saut, la fct de départ est tjs continue à gauche ?
Grpmh la déf est peut-être pas terrible. On ferait mieux d'intégrer sur
$\left[0, x\right[$ (ne serait-ce que pour avoir la "bonne" constante en 
$0$, et l'additivité) ; nécessaire alors de définir ça comme ça dans
la section sur la théorie de la mesure. Nota: pas évident, les probabilités
avec la convention de la fonction de répartition suggère plutôt
d'interpréter $\int_a^b$ comme l'intégrale sur $\left]a, b\right]$
(si l'on veut garder l'additivité).

### TODO -- Fonction de variation localement bornée {.definition}

### TODO -- Existence d'une dérivée comme mesure {.proposition}
Fct de variation localement bornée iff dérivée est une mesure de Radon

### TODO -- Notation Stieltjes
(explication en définissant explicitement la mesure associée à la
fct de variation bornées)

### TODO -- Explication notation, lien Kurzweil-Stieltjes
(en gros: bien que la valeur des intégrales soit différentes
-- et l'explication n'est pas si dure, L-S ignore les valeurs
de la fct à la discontinuité, pas K-S -- intégrable au sens
de L-S implique intégrabilité au sens de K-S, cf. @MAA18)

### TODO -- Rk Stieltjes
Si on intègre des fcts continues, la notation prend du sens.

### TODO -- Exemples

  - Equa diff encore, mais en prologeant $x(t)$ par $0$ pour $t \neq 0$

  - Proba et fct de répartition arbitraire.

### TODO -- Carac mesures par les fcts test (Riesz)
Aka mesure de Radon défini des opérateurs continus de $C^0_0([a, b])$
dans $\R$ et l'inverse aussi (si prolongements compatibles).

### TODO -- Formule des sauts

Distributions
--------------------------------------------------------------------------------

### TODO -- Distribution {.definition}
distribution d'ordre $k$ uniquement. Fonctionnelle définie sur les fcts
$C^k$ telle que si $C^k_0([a, b])$ désigne les fcts nulles
que leurs dérivée au bord, alors (restriction de $T$) 
linéaire bornée de $C^k_0([a, b])$ dans $\R$.

### TODO -- Mesure signée est une distribution

### TODO -- Dérivée d'une distribution

Proba / Fct répartition
================================================================================

Généralisation cas discret et à densité; dans les deux cas, fcts croissante
$\mathbb{R} \to \mathbb{R}$, nulle en $-\infty$, de variation 1, etc.

Montrer comment définir une mesure (extérieure) associée,
notation $\mu (= df)$ (Lebesgue-Stieltjes) ? 

Lien notation avec somme de Riemman-Stieltjes pour l'intégration de fcts
continues ?



Tribus engendrées & co
================================================================================



### Tribu engendrée par une collection {.definition}
Dans un ensemble $X$, on appelle *tribu engendrée* par une collection 
$\mathcal{B}$ d'ensembles de $X$ la plus petite tribu 
(au sens de l'inclusion) 
$\mathcal{A} = \sigma(\mathcal{B})$ de $X$ contenant $\mathcal{C}$.
Autrement dit : 

  - $\sigma(\mathcal{B})$ est une tribu.
  
  - si $\mathcal{B} \subset \mathcal{C}$ et $\mathcal{C}$ est une tribu de $X$, alors $\sigma(\mathcal{B}) \subset \mathcal{C}$.

 Quand il y a une ambiguité sur l'ensemble $X$ hébergeant la collection 
 $\mathcal{B}$, on pourra noter la tribu engendrée $\sigma_X(\mathcal{B})$.

### Démonstration (existence de la tribu engendrée) {.proof}
Désignons par $\mathfrak{S}$ la collection des tribus de 
contenant $\mathcal{B}$ comme sous-ensemble. 
$$
\mathfrak{S}
=
\{
\mbox{$\mathcal{C}$ tribu de $X$} \; | \; \mathcal{B} \subset \mathcal{C} 
\}
$$
Elle n'est pas vide : elle contient la collection $\mathcal{P}(X)$
des ensembles de $X$ (qui de toute évidence est un sur-ensemble de $\mathcal{B}$
et une tribu de $X$). Montrons que la plus petite tribu $\sigma(\mathcal{B})$
de $X$ contenant $\mathcal{B}$ est l'intersection de toutes les tribus de 
$\mathfrak{S}$, c'est-à-dire que
$$\sigma(\mathcal{B}) = \bigcap_{\mathcal{C} \in \mathfrak{S}} \mathcal{C} 
= \{A \subset X \, | \, A \in \mathcal{C} \mbox{ pour tout } \mathcal{C} \in \mathfrak{S}\}.$$
Il est clair que si $\mathcal{A}$ est une tribu de $X$ contenant $\mathcal{B}$,
alors $\cap_{\mathcal{C} \in \mathfrak{S}} \mathcal{C} \subset \mathcal{A}$, 
car $\mathcal{A} \in \mathfrak{S}$.
Il nous suffit donc de montrer que $\cap \mathfrak{S}$ est une tribu de $X$
pour pouvoir conclure ; on vérifiera aisément que comme chaque élément de $\mathfrak{S}$
est une tribu, cette intersection en est également une.

<!--
### Tribu de Lebesgue {.definition}
On appelle *tribu de Lebesgue* sur $\R^n$ la tribu composée des ensembles $E$
tels que pour tout pavé $P$ de $\R^n$, la fonction caractéristique 
de $E \cap P$ soit intégrable (au sens de Henstock-Kurzweil).

### {.post}
La tribu de Lebesgue est donc composée des ensembles mesurables au sens
du chapitre "Calcul Intégral III".

### TODO -- Référence
Lier au chapitre "Calcul Intégral III" en détail.
-->

### Tribu de Borel {.definition}
On appelle *tribu de Borel* d'un espace topologique $X$ la plus petite tribu
contenant tous les fermés (ou tous les ouverts) de $X$.

### Mesure {.definition}
Une *mesure (positive)* $\mu$ sur un espace mesurable $(X, \mathcal{A})$
est une fonction de $\mathcal{A}$ dans $[0, +\infty]$ telle que $\mu(\varnothing)= 0$
et pour toute collection dénombrable d'ensembles $A_k$ de
$\mathcal{A}$ disjoints deux à deux, on ait
$$
\mu \left( \bigcup_{k} A_k \right) = \sum_{k} \mu(A_k) ;
$$
on dit que $\mu$ est *$\sigma$-additive*.
L'ensemble $X$ muni de $\mathcal{A}$ et $\mu$ est un *espace mesuré*.

<!--
### TODO -- Pb
Gérer "pb" des fonctions à valeurs étendues ? Non, il n'y en a pas ...
-->

### Fonction mesurable
Une fonction $f: X \to Y$ associée aux espaces mesurables $(X, \mathcal{A})$
et $(Y,\mathcal{B})$ est *mesurable* 
(ou *$\mathcal{A}/\mathcal{B}$-mesurable*)
si l'image réciproque $A =f^{-1}(B)$
de tout ensemble $B$ de $\mathcal{B}$ par $f$ appartient à $\mathcal{A}$.

### L'infini
Dans le cadre abstrait de l'intégration selon Lebesgue, on pourra si nécessaire
considérer des fonctions prenant (éventuellement) des valeurs infinies,
c'est-à-dire travailler avec des fonctions à valeurs dans $Y = [-\infty, +\infty]$
plutôt que dans $Y=\R$([^inv]). Cette extension simplifiera notamment
l'énoncé du [théorème de Fubini](#fubini).

[^inv]: dans le cadre de l'intégration de Henstock-Kurzweil, c'est pour 
l'ensemble de départ que nous avions l'habitude de prendre $[-\infty, +\infty]$ ;
il s'agissait d'une "astuce" technique qui permettait d'intégrer des fonctions
définies au départ sur $\R$ avec des techniques déjà développées pour les
intervalles compacts $[a, b]$ de $\R$. Avec l'intégrale de Lebesgue 
il n'est plus nécessaire d'étendre $\R$ comme ensemble de départ.  
La théorie de Henstock-Kurzweil accepte donc volontiers les fonctions dont les 
**arguments** sont infinis -- $f(+\infty) = 0$ par exemple a du sens -- mais 
est "allergique" aux fonctions à **valeurs** infinies. Par exemple, 
si l'on essayait de calculer l'intégrale de Henstock-Kurzweil de la fonction
$$
f(x) = 
\left|
\begin{array}{rl}
+\infty & \mbox{si } x= 0, \\
1 / \sqrt{x} & \mbox{si } x \in \left]0, 1\right] \\
\end{array}
\right.
$$
on obtiendrait $+\infty$, alors même que l'intégrale vaut $2$ pour toute valeur 
finie de $f(0)$. L'intégrale de Lebesgue n'a pas cette difficulté, et produira
la valeur $2$ dans tous les cas.

### Conventions
Lorsque l'ensemble d'arrivée $Y$ de $f$ a une structure topologique, 
par exemple $Y = [-\infty, +\infty]$ ou $Y = [-\infty, +\infty]^m$, 
on supposera par défaut que la tribu associée est la tribu de Borel. 
Lorsque l'ensemble de départ de $f$ est $X = \R^n$ on supposera par défaut 
que la tribu associée est la tribu de Lebesgue. 
Lorsque l'on souhaitera plutôt munir $X$ et $Y$ de la tribu de Borel,
on parlera de fonction *borélienne* (tribu de Borel au départ et à l'arrivée).
Il existe une bonne raison pour adopter par défaut la convention hybride (avec
des tribus d'un type différent au départ et à l'arrivée) pour la définition
de "mesurable" :

### Lebesgue/Borel-mesurable équivaut à H.-K.-mesurable {.proposition}
Une fonction $f:\R^n \to \R^m$ est limite simple de fonctions intégrables 
au sens de Henstock-Kurzweil
-- c'est-à-dire "mesurable" au sens de ["Calcul Intégral III"](Calcul Intégral III.pdf) --
si et seulement si elle est $\mathcal{L}(\R^n)/\mathcal{B}(\R^m)$-mesurable.

La démonstration de ce résultat repose sur le lemme suivant :

### Image réciproque et tribus engendrées {.lemma #irte}
Soit $f : X \to Y$ une application et $\mathcal{B}$ une collection d'ensembles
de $Y$. Alors 
$$
\mathcal{F} := \sigma_X(\{f^{-1}(B) \; | \; B \in \mathcal{B}\}) = \{f^{-1}(A) \; | \; A \in \sigma_Y(\mathcal{B})\}.
$$

![Ce diagramme est *commutatif*.](images/commutative-diagram.tex)

<!--
La tribu engendrée dans $X$ par l'ensemble des images réciproques par
$f$ des ensembles $B \in \mathcal{B}$ est incluse dans
la collection des images réciproques par $f$ des ensembles de la tribu engendrée 
par $\mathcal{B}$ dans $Y$.
$$
\sigma\left(\{f^{-1}(B) \, | \, B \in \mathcal{B}\} \right)
\subset
\{f^{-1}(A) \, | \, A \in \sigma(\mathcal{B})\}.
$$
-->

### Démonstration {.proof}
Notons $\mathcal{A} = \sigma(\mathcal{B})$.
Comme $\mathcal{B} \subset \mathcal{A}$, on a
$$
\{f^{-1}(B) \, | \, B \in \mathcal{B}\} \subset
\{f^{-1}(A) \, | \, A \in \mathcal{A}\}.
$$
Si nous montrons que 
$\mathcal{C}:=\{f^{-1}(A) \, | \, A \in \mathcal{A}\}$ est une tribu 
nous pouvons en déduire que
$$
 \sigma(\{f^{-1}(B) \; | \; B \in \mathcal{B}\}) \subset \{f^{-1}(A) \; | \; A \in \mathcal{A}\}.
$$
L'ensemble vide appartient à $\mathcal{C}$ car 
$\varnothing = f^{-1}(\varnothing)$. Si $A \in \mathcal{A}$,
$X \setminus f^{-1}(A) = f^{-1}(Y \setminus A)$
et $Y \setminus A \in \mathcal{A}$, donc $X \setminus f^{-1}(A) \in \mathcal{C}$.
Finalement, si $A_0, A_1, \dots \in \mathcal{A}$, 
$\cup_k f^{-1}(A_k) = f^{-1}(\cup_k A_k) \in \mathcal{C}$.
La collection $\mathcal{C}$ est donc une tribu.

Réciproquement, posons $\mathcal{E} = \sigma(\{f^{-1}(B) \; | \; B \in \mathcal{B}\})$ 
et considérons 
$$
\mathcal{D} = \{A \in Y \; | \; f^{-1}(A) \in \mathcal{E}\}.
$$
La collection $\mathcal{D}$ est également une tribu. En effet,
$f^{-1}(\varnothing) \in \mathcal{E}$, si $f^{-1}(A) \in \mathcal{E}$ alors
$f^{-1}(Y \setminus A) = X \setminus f^{-1}(A) \in \mathcal{E}$ et si 
$f^{-1}(A_0), f^{-1}(A_1), \dots \in \mathcal{E}$, alors 
$f^{-1}(\cup_k A_k) = \cup_k f^{-1}(A_k) \in \mathcal{E}$.
Par conséquent, comme $\mathcal{B} \subset \mathcal{D}$,
$\mathcal{A} = \sigma(\mathcal{B}) \subset \sigma(\mathcal{D}) = \mathcal{D}$.
Donc pour tout $A \in \mathcal{A}$, on a $f^{-1}(A) \in \mathcal{E}$,
soit
$$
\{f^{-1}(A) \; | \; A \in \mathcal{A}\} \subset \mathcal{E}  =\sigma(\{f^{-1}(B) \; | \; B \in \mathcal{B}\}).
$$


### Démonstration "L./B.-mesurable $\Leftrightarrow$ H.-K.-mesurable" {.proof}
La fonction $f:\R^n \to \R^m$ est limite simple de fonctions intégrables 
au sens de Henstock-Kurzweil si et seulement si elle vérifie 
le critère de l'image réciproque des sections II et III, 
c'est-à-dire si et seulement si l'image réciproque de tout ouvert 
de $\R^m$ est un ensemble $\mathcal{L}(\R^n)$-mesurable.

De toute évidence, si $f$ est Lebesgue/Borel-mesurable, ce critère est 
satisfait. Réciproquement, si l'image réciproque de tout ouvert de $\R^m$
est Lebesgue-mesurable, alors la tribu engendrée par les images réciproques
des ouverts de $\R^m$ est incluse dans la tribu de Lebesgue sur $\R^n$.
Comme cette tribu est d'après [le lemme précédent](#irte) l'ensemble
des images réciproques de la tribu engendrée par les ouverts dans $\R^m$,
c'est-à-dire la tribu de Borel dans $\R^m$, l'image réciproque de tout
borélien est un ensemble de la tribu de Lebesgue : la fonction 
$f$ est Lebesgue/Borel-mesurable.

### Composition de fonctions mesurables {.proposition #compfoncmes}
Soient $(X, \mathcal{A})$, $(Y, \mathcal{B})$ et $(Z, \mathcal{C})$ des
espaces mesurables.
Soit $f: X\to Y$ une fonction $\mathcal{A}/\mathcal{B}$-mesurable et 
$g: Y \to X$ une fonction $\mathcal{B}/\mathcal{C}$-mesurable.
Alors la composition $g \circ f$ de $f$ et $g$ est 
$\mathcal{A}/\mathcal{C}$-mesurable.

### Démonstration {.proof}
Pour tout ensemble $C \in \mathcal{C}$, on a $g^{-1}(C) \in \mathcal{B}$ 
et donc $(g \circ f)^{-1}(C) = f^{-1}(g^{-1}(C)) \in \mathcal{A}$.

### Les fonctions continues sont boréliennes
Soient $X$ et $Y$ deux espaces topologiques.
Toute fonction continue $f : X \to Y$ est borélienne.

### Démonstration {.proof}
Notons $\mathcal{F}_X$ et $\mathcal{F}_Y$ les collections de tous les ensembles 
fermés de $X$ et $Y$ respectivement.
Comme les boréliens de $Y$ sont engendrés par les fermés de $\mathcal{F}_Y$, on a
$$
\{f^{-1}(A) \; | \; A \in \mathcal{B}(Y)\} = \{f^{-1}(A) \; | \; A \in \sigma_Y(\mathcal{F}_Y)\}
$$
et par conséquent, par [commutativité](#irte),
$$
\{f^{-1}(A) \; | \; A \in \mathcal{B}(Y)\} = \sigma_X (\{f^{-1}(A) \; | \; A \in \mathcal{F}_Y\}).
$$
Or la fonction $f$ étant continue, 
$\{f^{-1}(A) \; | \; A \in \mathcal{F}_Y\} \subset \mathcal{F}_X$ et par 
conséquent
$$
\sigma_X(\{f^{-1}(A) \; | \; A \in \mathcal{F}_Y\}) \subset \sigma_X(\mathcal{F}_X) = \mathcal{B}(X).
$$
Au final, 
$\{f^{-1}(A) \; | \; A \in \mathcal{B}(Y)\} \subset \mathcal{B}(X)$
et la fonction $f$ est bien $\mathcal{B}(X)/\mathcal{B}(Y)$-mesurable, 
c'est-à-dire borélienne.


### Limite simple de fonctions mesurables
Soit $(X, \mathcal{A})$ un espace mesurable et $Y=\left[-\infty, +\infty\right]$, 
muni de la tribu de Borel. 
Si les fonctions $f_k: X \to Y$,
$k \in \N$, sont mesurables et convergent simplement vers $f$, 
alors $f$ est mesurable. 

### Démonstration {.proof}
Par [le lemme liant image réciproque et tribus engendrées](#irte),
il suffit de prouver que l'image réciproque par $f$ de tout ouvert $U$ de $Y$
appartient à $\mathcal{A}$.
Or $f(x) \in U$ si et seulement si $f_k(x) \in U$
pour $k$ assez grand, ce qui se traduit par la formule
$$
f^{-1}(U) = \bigcup_{j=0}^{+\infty} \bigcap_{k = j}^{+\infty} f_k^{-1}(U)
$$
qui établit que $f^{-1}(U)$ est un ensemble mesurable, comme union 
(dénombrable) d'intersections (dénombrable) d'ensembles mesurables.


### Fonction mesurable
Soit $\mathcal{A}$ une tribu sur l'ensemble $X$.
Une fonction $f: X \to [-\infty, +\infty]$ est
$\mathcal{A}/$Borel- mesurable si et seulement si $f$ est la limite
simple de fonctions étagées $X \to \R$ qui soient $\mathcal{A}$/Borel-mesurables.

### TODO -- Démonstration {.proof}


<!--

### Intégrale d'une fonction à valeurs réelles
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré et 
$f: X \mapsto [-\infty, +\infty]$ une fonction mesurable.
On dit que la fonction $f$ est *intégrable au sens de Lebesgue 
relativement à la mesure $\mu$* si elle est mesurable et que 
les intégrales des fonctions positives 
$f_+ = \max(f, 0)$ et $f_- = -\min(f, 0)$ sont finies. 
*L'intégrale de Lebesgue de $f$ relativement à la mesure $\mu$*
est alors la grandeur réelle (finie)
$$
\int f \mu :=  \int_X f(x) \mu(dx) := \int_X f_+ \mu - \int_X f_- \mu.
$$ 
-->


<!--

### Une intégrale absolue
On remarquera que l'essentiel de la complexité de l'intégrale de Lebesgue
est encapsulée dans l'intégrale des fonctions positives ; la définition 
(et les propriétés) de l'intégrale de fonctions signées s'en déduisent
facilement. En particulier, comme la valeur absolue d'une fonction vérifie
$|f| = f_+ + f_-$, on constate que si $f$ est intégrable, alors $|f|$
également ; par construction, l'intégrale de Lebesgue est absolue,
contrairement à l'intégrale de Henstock-Kurzweil sur $\R^n$.
On a le résultat plus précis suivant, que l'on admettra :

### Intégrale de Lebesgue et de Henstock-Kurzweil {.theorem}
Soit $f: \R^n \to \R$. La fonction $f$ est intégrable
par rapport à la mesure de Lebesgue $v$ si et seulement si 
$f$ est absolument intégrable ($f$ et $|f|$ sont intégrables) 
au sens de Henstock-Kurzweil. Dans ce cas, les
deux intégrales sont égales :
$$
\int_{\R^n} f(x) v(dx) = \int_{\R^n} f(x) dx.
$$

-->

Produit de mesures
--------------------------------------------------------------------------------



### Tribu produit
Soit $(X ,\mathcal{A})$ et $(Y, \mathcal{B})$ deux espaces mesurables.
On appelle *tribu produit* de $\mathcal{A}$ et $\mathcal{B}$ 
et l'on note $\mathcal{A} \otimes \mathcal{B}$
la tribu sur le produit cartésien $X \times Y$ engendrée par les
ensembles de la forme $A \times B$ où $A \in \mathcal{A}$ et
$B \in \mathcal{B}$.
$$
\mathcal{A} \otimes \mathcal{B} := 
\sigma_{X \times Y}
\left( 
\left\{ A \times B \; | \; A \in \mathcal{A}, \; B \in \mathcal{B} \right\}
\right).
$$

### Produit des boréliens
On peut montrer que pour tout couple d'entiers $m$ et $n$, la tribu des
boréliens sur $\R^{m+n}$ est le produit des tribus des boréliens sur 
$\R^m$ et $\R^n$ :
$$
\mathcal{B}(\R^{m+n}) = \mathcal{B}(\R^{m}) \otimes \mathcal{B}(\R^{n}).
$$
Le résultat analogue n'est pas vrai pour la mesure de Lebesgue : il est 
nécessaire de compléter la tribu produit $\mathcal{L}(\R^m) \otimes \mathcal{L}(\R^n)$
par rapport à la mesure de Lebesgue sur $\R^{m+n}$
pour obtenir $\mathcal{L}(\R^{m+n})$ (cf. [exercice "Complétion d'une mesure"](#complétion)).


### Mesure produit
Soient $(X, \mathcal{A}, \mu)$ et $(Y, \mathcal{B}, \nu)$ deux espaces mesurés.
On appelle *mesure produit* de $\mu$ et $\nu$ et l'on note 
$\mu \otimes \nu$ la fonction définie sur $\mathcal{A} \otimes \mathcal{B}$
par
$$
(\mu \otimes \nu) (C) = \inf
\left\{ 
\sum_{k=0}^{+\infty} \mu(A_k) \nu(B_k) 
\; \left| \vphantom{\sum_{k=0}^{+\infty}} \right. \;
A_k \in \mathcal{A}, \ B_k \in \mathcal{B}, \, C \subset \bigcup_{k=0}^{+\infty} A_k \times B_k \right\}.
$$

### Démonstration {.proof}
Cf. @Hun11.


<!--
### TODO -- Démonstration : la "mesure produit" est une mesure {.proof}

  - introduire $(\mu \otimes \nu)^* (C)$ pour tout $C$, montrer qu'on a 
    affaire à une mesure extérieure.

  - montrer que tout ensemble de $\mathcal{A} \otimes \mathcal{B}$ et 
    $(\mu \otimes \nu)^*$-mesurable (suffit de montrer que $A \times B$
    est $(\mu \otimes \nu)^*$-mesurable).
-->    


### Intégrale dans un espace produit {.notation}
Soient $(X, \mathcal{A}, \mu)$ et $(Y, \mathcal{B}, \nu)$ deux espace mesurés.
Pour toute fonction $\mu \otimes \nu$-mesurable 
$f: X \times Y \to [0, +\infty]$ ou toute fonction $\mu \otimes \nu$-intégrable
$f: X \times Y \to \R$, on notera
$$
\int_{X \times Y} f(x, y) \mu(dx)\nu(dy) := 
\int f (\mu \otimes \nu).
$$

### Mesure $\sigma$-finie
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré. On dit que la mesure $\mu$
est $\sigma$-finie s'il existe une suite d'ensembles mesurables 
$A_k \in \mathcal{A}$, $k \in \N$, telle que 
$$
\bigcup_{k=0}^{+\infty} A_k = X 
\; \mbox{ et } \; 
\forall \, k \in \N, \mu(A_k) < +\infty.
$$

<!--
### TODO -- remark
Gérer la subtilité que la première intégrale est définie uniquement
presque partout, ce qui suffit à montrer que la seconde est définie
(à détailler aussi en amont).
-->

### Théorème de Fubini {.theorem #fubini}
Soit $(X, \mathcal{A}, \mu)$ et $(Y, \mathcal{B}, \nu)$ deux espace mesurés,
tels que les mesures $\mu$ et $\nu$ soient $\sigma$-finies.
Une fonction mesurable $f: X \times Y \to \R$
est intégrable si et seulement l'intégrale itérée
$$
\int_Y \left(\int_X |f(x, y)| \mu(dx) \right) \nu(dy)
$$
est finie. Dans ce cas,
$$
\int f \, (\mu \otimes \nu)
=
\int_Y \left(\int_X f(x, y) \mu(dx) \right) \nu(dy).
$$

### Démonstration {.proof}
cf @Hun11.

### Symétrie
Le rôle joué par $X$ et $Y$ étant symétrique dans l'énoncé du théorème de
Fubini,on peut également dire qu'une fonction mesurable $f: X \times Y \to \R$
est intégrable si et seulement l'intégrale itérée
$$
\int_X \left(\int_Y |f(x, y)| \nu(dy) \right) \mu(dx)
$$
est finie et que dans ce cas,
$$
\int f \, (\mu \otimes \nu)
=
\int_X \left(\int_Y f(x, y) \nu(dy) \right) \mu(dx).
$$

<!--
### TODO -- Complétion
Etudier <https://www.math.fsu.edu/~roberlin/maa5616.f15/homework9sln.pdf>

Aussi, <https://terrytao.wordpress.com/2010/10/30/245a-notes-6-outer-measures-pre-measures-and-product-measures/>

### TODO -- remarque 
remarque évidente sur l'autre intégrale itérée.


-->


Exercices
================================================================================

Dérivée faible
--------------------------------------------------------------------------------

Est-ce que la fonction $f: \R \to \R$ définie par $f(0)=0$ et
$$
f(x) = \sqrt{|x|} \, \mbox{ si $x\neq 0$}
$$
est faiblement dérivable ? Quelle est dans ce cas sa dérivée ?

Fonctions lipschitzienne
--------------------------------------------------------------------------------

(d'une variable). Montrer qu'elles ont une dérivée faible (et donc pp),
en utilisante leur caractère absolument continu (cf. Evans-Gariepy dans
le cas multivariable) et que la dérivée (faible) est de norme plus petite
que la constante de Lipschitz.

Fonctions convexes
--------------------------------------------------------------------------------

Equivalent dérivée seconde est une mesure positive ?

Fonction distance
--------------------------------------------------------------------------------

Dérivées seconde fonction distance, squelette, courbure, etc ?


Tribu engendrée
--------------------------------------------------------------------------------

Une collection $\mathcal{A}$ de sous-ensembles de $X$ est une 
*algèbre (d'ensembles)* si elle contient $\varnothing$ et est stable
par complémentation et par union finie.

De manière similaire au cas des tribus, pour toute collection d'ensembles 
de $X$ il existe une plus petite (au sens de l'inclusion) algèbre qui la 
contient : c'est *l'algèbre engendrée* par cette collection.

### Question 1  {.question #te-1}
Déterminer l'algèbre engendrée sur $\R$ par la collection
$$
\{\left[a, b\right[ \; | \; -\infty < a \leq b \leq +\infty\}
$$

### Question 2  {.question #te-2}
Déterminer la tribu engendrée (ou $\sigma$-algèbre) sur $\R$ par la même 
collection.


Solutions
=================================================================================



Tribu engendrée
--------------------------------------------------------------------------------

### Question 1  {.answer #answer-te-1}
Si $\mathcal{A}$ est une algèbre de $X$ contenant tous les intervalles
$\left[a, b\right[$ quand $-\infty < a \leq b \leq +\infty$, alors 
par complémentation de $\left[a, +\infty\right[$, 
elle contient nécessairement les ensembles de la forme $\left]-\infty, a\right[$ 
et donc par union finie tous les ensembles de la forme
$$
\left]-\infty, a_0\right[ \cup \dots \cup \left[a_k, b_k\right[ \cup \dots \cup \left[a_m, +\infty\right[
$$
où les $a_k$ et les $b_k$ sont finis et le premier et dernier terme de cette union
peuvent être omis. On vérifiera alors que cet ensemble est stable par union
finie et par complémentation : c'est une algèbre de $\R$. Par conséquent, 
c'est la plus petite algèbre de $\R$ qui contienne la collection initiale ;
c'est donc l'algèbre engendrée recherchée.

### Question 2  {.answer #answer-te-2}
Si $\mathcal{A}$ est une tribu de $X$ contenant tous les intervalles
$\left[a, b\right[$ quand $-\infty < a \leq b \leq +\infty$, alors
elle contient aussi
$$
\left]a, b\right[ = \bigcup_{k=0}^{+\infty} \left[a+\frac{b-a}{2^k}, b\right[
$$
et donc tout ouvert de $\R$ puisqu'un tel ensemble est une réunion dénombrable
d'intervalles ouverts de $\R$. Par conséquent, elle contient tous les Boréliens.
Comme l'ensemble des Boréliens est une tribu de $\R$, c'est donc la tribu
engendrée par la collection initiale.  


Références
================================================================================