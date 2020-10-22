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

<!--
Objectifs
================================================================================


### TODO -- Basique


### TODO -- Standard


### TODO -- Avancé


### TODO -- Hors-programme

-->


Dérivées faibles
================================================================================

Nous généralisons dans cette section la notion classique de dérivée de fonction,
pour répondre aux besoins de disciplines variées : les probabilités, 
les équations différentielles (et aux dérivées partielles), le 
traitement du signal, etc.

Dans un premier temps, nous nous intéressons au cas où une fonction ordinaire
joue effectivement le rôle de la dérivée mais sans en être une stricto sensu.
L'exemple basique serait la "solution" $x: \R \to \R$, "initialement au repos"
($x(t)=0$ pour $t \leq 0$) de l'équation différentielle
$$
\dot{x}(t) = e(t), \, t \in \R
$$
où $e(t)$ est l'échelon unitaire (ou fonction d'Heaviside), défini par
$$
e(t) = 1_{\left[0, +\infty\right[} = \left|
\begin{array}{rl}
0 &\mbox{si $t<0$,} \\
1 & \mbox{si $t\geq 0$.}
\end{array}
\right.
$$
Cette équation peut être considérée par exemple comme un modèle simpliste de 
l'évolution de la température $x$ en fonction du temps $t$ d'un système thermique 
que l'on décide de chauffer (avec un flux de chaleur constant) à partir de $t=0$.

![](images/step.py)\

La "solution" physiquement raisonnable $x(t) = t e(t)$ n'est toutefois pas dérivable
classiquement pour $t=0$ et il est nécessaire d'invoquer un 
"principe de continuité" pour "recoller" les deux fragments de solutions 
de l'équation différentielle pour $t<0$ et $t>0$. 
Nous pourrons bientôt adopter un discours plus clair et à l'issue de cette
section, énoncer que la fonction $x: t \mapsto te(t)$ a pour *dérivée faible* 
la fonction $e: t \mapsto e(t)$ sur tout $\R$. Dans ce cadre, la continuité de
$x$ résultera du cadre mathématique adopté plutôt que de devoir être rajoutée
comme une hypothèse supplémentaire. 

<!-- Le même cadre nous permettra
également de considérer si nécessaire des fonctions des fonctions plus 
irrégulières que des fonctions continûment différentiables par morceaux
où la continuité résultera du cadre mathématique choisi. 
-->

<!--
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
-->

### Fonctions localement absolument intégrables
Une fonction $f: \R \to \R$ est *localement absolument
intégrable* (ou *ordinaire*) si elle est 
absolument intégrable au sens de Henstock-Kurzweil sur tout intervalle compact $[a, b]$ :
$$
\int_a^b f(t) \, dt \in \R \; \mbox{ et } \; \int_a^b |f(t)| \, dt \in \R_+.
$$

### {.post}
Compte tenu des liens entre intégrale de Henstock-Kurzweil et de Lebesgue,
si $\ell$ désigne la mesure de Lebesgue sur $\R$, cela équivaut à dire que
$f$ est $\ell$-intégrable sur tout intervalle compact $[a, b]$ :
$$
\int_{[a, b]} f(t) \, \ell(dt)=
\int 1_{[a, b]} f \, \ell \in \R.
$$




### Dérivée faible {.definition}
La fonction $f:\R \to \R$ est *dérivable faiblement* s'il existe une 
fonction $g:\R \to \R$ localement absolument intégrable et une constante $c \in \R$ 
telles que pour tout $x \in \R$, 
$$
f(x) = c + \int_0^x g(t) \, dt.
$$
La fonction $g$ est alors appelée *dérivée faible* de $f$.

### Les fonctions faiblement dérivables sont continues.

### {.post}
En particulier, une fonction faiblement dérivable est nécessairement 
localement absolument intégrable.

### Démonstration {.proof}
La continuité des intégrales indéterminées, de la forme
$$
x \in \R \mapsto \int_a^x h(t) \, dt
$$
est prouvée dans le chapitre "Calcul Intégral I" au moyen du lemme de Henstock, 
sous l'hypothèse que $h$ est intégrable (pour un réel étendu $a$ arbitraire). 
Or pour tout $r>0$, la fonction $h = g 1_{[-r,r]}$ est intégrable. 
Comme pour tout $x \in \left]-r, r\right[$,
$$
\int_0^x g(t) \, dt = \int_0^x h(t) \, dt,
$$
l'intégrale indéterminée de $g$, et donc $f$, est continue en $x$. 
Le choix de $r$ étant arbitraire, $f$ est continue sur $\R$ tout entier.


### Dérivée faible et classique
Si une fonction $f: \R \to \R$ est faiblement dérivable, de dérivée faible $g$,
alors elle est dérivable (classiquement) presque partout et $f' = g$ presque
partout. On a donc pour tout $x \in \R$,
$$
f(x) = f(0) + \int_0^x f'(t) \, dt.
$$

### 
En particulier, la dérivée faible d'une fonction, si elle existe, est unique
presque partout.

### Démonstration {.proof}
Une conséquence directe du résultat de 
[dérivation des intégrales indéterminées de "Calcul Intégral II"](Calcul Intégral II.pdf/#DII).

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
ce qui n'est pas le cas. Alternativement, on peut aussi remarquer 
qu'elle n'est pas continue et par conséquent qu'elle ne peut pas être 
faiblement dérivable.

### Attention ! {.post}
Une fonction peut également être dérivable en tout point de $\R$ 
mais de dérivée non localement absolument intégrable, 
auquel cas elle n'est pas faiblement dérivable[^Tao]. 
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
que conditionnellement intégrable sur $[0, 1]$ par exemple, et donc
elle n'est pas localement absolument intégrable (cf. [Calcul Intégral II](Calcul Intégral II.pdf)).

[^Tao]: C'est la seule obstruction possible : une fonction qui serait dérivable 
**en tout point de $\R$**
et dont la dérivée classique est localement absolument intégrable est
automatiquement faiblement dérivable [@Tao11, prop. 1.6.41, p. 176].

### Fonctions continûment différentiables par morceaux {.theorem}
Toute fonction $f: \R \to \R$  continue et continûment dérivable par morceaux 
est faiblement dérivable.

### {.post}
A noter que l'on peut être continûment différentiable par morceaux mais pas
continue ; dans ce cas on ne peut pas être faiblement dérivable.
La fonction signe est un bon exemple de fonction
continûment dérivable par morceaux mais qui n'est pas continue (et donc
pas faiblement dérivable).

### Démonstration {.proof}
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
$\left]a_k, b_k\right[$ la fonction $f$ soit continûment dérivable, 
avec une dérivée ayant un prolongement par continuité à $[a_k, b_k]$.

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
Elle est faiblement dérivable ; en effet, son intégrande est 
localement absolument intégrable 
(il est positif et intégrable sur $\R$, d'intégrale $1$) 
et l'on a par additivité de l'intégrale pour tout $x\in\R$
$$
F(x) = F(0) + \int_{0}^x \frac{\exp (-{t^2}/{2})}{\sqrt{2\pi}} \, dt.
$$
Cett relation montre également que la fonction 
$$
f : t \in \R \mapsto  \frac{\exp (-{t^2}/{2})}{\sqrt{2\pi}}
$$
est une dérivée faible de $F$. 


![skdjslkdjs](images/gauss.py)\ 


### Exercice -- Loi de probabilité uniforme {.exercise}
Montrer que la fonction de répartion $F$ associée la loi de probabilité
uniforme sur $[0, 1]$, définie par
$$
F(x) = \left|
\begin{array}{rl}
0 & \mbox{si $x < 0$,} \\
x & \mbox{si $0 \leq x < 1$,} \\
1 & \mbox{si $1 \leq x$.} \\
\end{array}
\right.
$$
est faiblement dérivable et calculer (presque partout) sa dérivée faible.

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




<!--
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

-->

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
de dérivée que nous allons aborder où les dérivées ne seront plus
nécessairement des fonctions "ordinaires", mais des fonctions "généralisées".

### Fonctions tests
On note $D^k(\R)$ l'espace des fonctions continues $\varphi: \R \to \R$
dont le support
$$\mbox{supp } \varphi := \overline{\{x \in \R \; | \; \varphi(x) \neq 0\}}$$
est compact et qui sont continues si $k=0$ ou $k$ fois continûment différentiables
quand $k \geq 1$.


### Dérivation faible et fonctions tests {#dfft}
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
si et seulement si elle continue.

Supposons que cela soit le cas pour la fonction $f$.
Alors, si $\varphi \in D^1(\R)$,
le produit $f \varphi$ est continûment différentiable par morceaux et 
continu, de dérivée classique presque partout égale à $f' \varphi + f \varphi'$.
Les deux termes de cette somme sont intégrables. De plus, pour $r>0$
assez grand et $|t| \geq r$, on a $\varphi(t) = 0$, donc
$$
\int_{-\infty}^{+\infty} f'(t) \varphi(t) \, dt 
+ \int_{-\infty}^{+\infty} f(t) \varphi'(t) \, dt
=
\int_{-r}^{+r} (f \varphi)'(t) \, dt
= 
[f \varphi]^{+r}_{-r} = 0.
$$
Réciproquement, supposons que $f$ et $g$ soient continûment différentiables et 
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
Le second membre étant continu par rapport à $x$ et $f$ supposée continue par
morceaux, elle est en fait continue et $f(x) = f(x^-)$. Le cas $x<0$ se traite
de façon similaire. La fonction $f$ admet donc $g$ comme dérivée faible.

Mesures signées et dérivées
================================================================================

### {.ante}
Aller plus loin dans la dérivation des fonctions -- pouvoir dériver des
fonctions discontinues par exemple -- suppose d'accepter que des dérivées
ne soient pas des fonctions ordinaires, mais des fonctions *généralisées*.
Nous montrerons dans cette section comment des opérateurs linéaires agissant 
sur des fonctions tests peuvent remplir ce rôle et établiront le lien entre
ces opérateurs et les mesures signées.

### Formes linéaires continues sur $D^0(\R)$.
On dira qu'une application linéaire $T: D^0(\R) \to \R$ 
-- c'est-à-dire une *forme linéaire* sur $D^0(\R)$ --
est *continue* si pour tout
intervalle compact $[a, b]$ de $\R$ il existe une constante $K$ telle que pour 
toute fonction $\varphi \in D^0(\R)$ dont le support soit inclus dans $[a, b]$, 
on ait
$$
|T \cdot \varphi| \leq K \sup_{x \in \R} |\varphi(x)|
$$
<!--  = K \|\varphi|_{[a, b]}\|_{\infty} -->

### Cas des fonctions ordinaires {.theorem}
Si $f:\R \to \R$ est localement absolument intégrable, l'opérateur
$$
T[f] : \varphi \in D^0(\R) \mapsto \int_{-\infty}^{+\infty} f(t) \varphi(t) \, dt 
$$
est linéaire continu. 
De plus, si $g :\R \to \R$ est localement absolument intégrable, 
$T[f] = T[g]$ si et seulement si $f=g$ presque partout.

### Démonstration {.proof}
La fonction $f$ est localement intégrable donc mesurable et la fonction
$\varphi$ est continue donc mesurable. Le produit $f \varphi$ est donc mesurable.
Soit $[a, b]$ un intervalle compact contenant le support de $\varphi$ et 
$M$ un majorant de $|\varphi|$ sur ce compact. Alors le produit $|f \varphi|$ est
dominé par la fonction $|f|M 1_{[a, b]}$ qui est intégrable ; le produit 
$f \varphi$ est donc absolument intégrable et par l'inégalité triangulaire, 
$$
\left|\int_{-\infty}^{+\infty} f(t) \varphi(t) \, dt\right|
\leq 
\left(\int_{-\infty}^{+\infty} |f(t)| \, dt\right) \sup_{x \in \R} |\varphi(x)|.
$$
L'opérateur $T[f]$ est donc continu. Par ailleurs, la linéarité de 
$f \mapsto T[f]$ résulte de la linéarité de l'intégrale.

La fonction 
$$
\int_{-\infty}^x f(t) \,dt
$$
est dérivable presque partout, de dérivée $f(x)$. 
En tout point $x$ de ce type on a donc
$$
f(x) = \lim_{h \to 0} \frac{1}{h} \int_x^{x+h} f(t) \, dt.
$$
Or, on peut construire une famille de fonction $\varphi_{h, \varepsilon} \in D^1(\R)$,
de support inclus dans $[x, x+h]$, vérifiant pour tout $t \in [x, x+h]$,
$0 \leq \varphi_{h,\varepsilon}(t) \leq 1$ et telle que
$$
\lim_{\varepsilon \to 0} \varphi_{h, \varepsilon} = 1_{\left]x, x+h\right[}.
$$
(on pourra s'inspirer des fonctions tests utilisées dans la démonstration de 
["Dérivation faible et fonctions tests"](#dfft)).
Par le théorème de convergence dominée, on a donc pour presque tout $x$
$$
\begin{split}
f(x) &= \lim_{h \to 0} \frac{1}{h} \int_x^{x+h} f(t) \, dt \\
&= \lim_{h \to 0} \lim_{\varepsilon \to 0}\frac{1}{h} \int_{-\infty}^{+\infty} f(t) \varphi_{h, \varepsilon}(t) \, dt \\
&= 
\lim_{h \to 0} \lim_{\varepsilon \to 0}\frac{1}{h} T[f] \cdot \varphi_{h, \varepsilon}.
\end{split}
$$
La fonction $f$ est donc déterminée uniquement presque partout par la donnée de 
$T[f]$.

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

### Mesure signée {.definition} 
Soit $(X, \mathcal{A})$ un ensemble mesurable.
Une *mesure signée* $\nu$ sur $(X, \mathcal{A})$ est une application
$$
\nu : \mathcal{A} \to \R \cup \{\bot\}
$$
pour laquelle il existe une mesure $\mu : \mathcal{A} \to [0, +\infty]$ 
et une application $\mu$-mesurable $\sigma: X \to \{-1, +1\}$ telles que
pour tout $A \in \mathcal{A}$,
$$
\nu(A) := \sigma \mu(A) := \left|
\begin{array}{rl}
\displaystyle \int_A \sigma(x) \, \mu(dx) = \int 1_A \sigma \, \mu & \mbox{si $1_A \sigma$ est $\mu$-intégrable,} \\
\bot & \mbox{sinon.}
\end{array}
\right.
$$


### A propos du symbole $\bot$ {.post}
Le symbole $\bot$ peut être interprété comme "valeur réelle indéfinie" ou
plus simplement "indéfini"[^nan]. Dans les calculs, on conviendra que toute opération
impliquant $\bot$ a pour résultat $\bot$ ; par exemple $\bot$ est absorbant pour
l'addition, c'est-à-dire que pour tout $x$ réel ou indéfini,
$$
x+ \bot = \bot + x = \bot.
$$
Dans ce contexte, on considérera également que les séries sans limites 
dans $\R$ ont pour limite $\bot$. Le symbole $\bot$ joue un rôle très
similaire à celui que joue $+\infty$ dans le cas des calculs impliquant 
des nombres positifs.

[^nan]: concept assez similaire au "non-nombre" `nan` (*not-a-number*) des 
numériciens, que l'on obtient par exemple avec NumPy en calculant `inf - inf`.


### Les mesure (positives) sont des mesures signées
Toute mesure classique (dans le contexte des mesures signées, en cas d'ambiguité,
on parlera de mesure *positive* pour les désigner) $\mu: \mathcal{A} \to [0, +\infty]$
peut être "convertie" en mesure signée $\nu$ : il suffit de lui associer 
la mesure $\mu$ et la fonction de signe $\sigma$ constante égale à $+1$.
On a alors
$$
\nu(A) = \left|
\begin{array}{rl}
\mu(A) & \mbox{si $\mu(A) < +\infty$,} \\
\bot & \mbox{si $\mu(A) = +\infty$.}
\end{array}
\right.
$$
L'identification inverse est possible si $\nu$ ne prend que des valeurs
positives ou indéfinies, en convertissant les valeurs indéfinies en $+\infty$.



### Exercice -- Une mesure signée {.exercise}
Soit $\ell$ la mesure de Lebesgue dans $\R$.
Montrer que la fonction qui a un ensemble $A$ de $\mathcal{L}(\R)$ associe
$$
\mu(A) = \ell|_{\R_+} (A) - \ell|_{\R_-}(A)  =\ell(\left[0, +\infty\right[\cap A) - \ell(\left]-\infty, 0\right]\cap A)
$$
est une mesure signée.

### Exercice -- Propriétés des mesures signées {.exercise}
Les mesure signées sont-elles comme les mesures positives nulles en $0$
(telles que $\mu(\varnothing)=0$) ? Croissantes (telles que $\mu(A) \leq \mu(B)$
quand $A \subset B$) ? 

### {.post}
Contrairement aux mesures positives, les combinaisons linéaires à coefficients
réels (et pas seulement positifs) de mesures signées sont des mesures signées.
On peut ainsi par exemple combiner des mesures de Dirac positives $\delta_x$
et construire la mesure $\mu = \delta_0 - 1/2 \times \delta_1$, 
qui associe à l'ensemble $A \subset \R$ la quantité
$$
\mu(A) = (\delta_0 - 1/2 \times \delta_1)(A) = 1_A(0) - 1/2 \times 1_A(1).
$$

![Les combinaisons linéaires de Dirac sont souvent représentées comme des "pics"
surmontés d'un triangle ou d'un rond. La mesure de Dirac $\alpha \delta_x$ 
est représentée par un pic à l'abscisse $x$ et de hauteur $\alpha$ (positive ou negative).](images/dirac.py)




### Intégrale associée à une mesure signée {.definition}
Soit $\nu = \sigma \mu$ une mesure signée sur $(X, \mathcal{A})$.
La fonction $\mathcal{A}$-mesurable $f: \R \to [-\infty, +\infty]$ est 
dite *$\nu$-intégrable* si la fonction $f$ (ou $f\sigma$) est $\mu$-intégrable.
L'intégrale de $f$ par rapport à $\nu$ est alors définie comme
$$
\int f \nu = \int_X f(x) \, \nu(dx) := \int f \sigma \, \mu \in \R.
$$

<!--
### Mesures de Dirac

### Mesure positive vers mesure signée
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
-->



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

<!--
### TODO -- Décomposition de Hahn
(trivial, mais bon)



### TODO -- $\sigma$-additivité


### TODO 
$f$ $\mu-$intégrable à valeurs réelles fois $\mu$ défini une mesure signée

### TODO -- Intégrale par rapport à une mesure signée

-->

### Mesures de Radon {.definition}
Une mesure signée $\mu$ sur $(\R, \mathcal{A})$ est une *mesure de Radon* 
si pour tout fonction $\varphi \in D^0(\R)$, l'intégrale
$$
T[\mu] \cdot \varphi := \int \varphi \, \mu 
$$
est bien définie et que l'opérateur $T[\mu] : D^0(\R) \to \R$ est linéaire continu.

<!--

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
-->

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


<!--


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

-->

<!--
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
-->

### La mesure de Lebesgue est de Radon {.proposition}

### Démonstration {.proof}
Soit $[a, b]$ un intervalle compact de $\R$. Pour tout $\varphi \in D^0(\R)$ 
dont le support est inclus dans $[a, b]$, $\varphi$ est mesurable et bornée
par la fonction $(\sup_{x\in \R} |\varphi(x)|) 1_{[a, b]}$, donc $\ell$-intégrable.
$$
|T \cdot \varphi| = \left|\int_{a}^b \varphi \, \ell \right| 
\leq \int_a^b |\varphi| \ell \leq \sup_{x\in \R} |\varphi(x)| \int_a^b \ell
= (b-a) \sup_{x\in \R} |\varphi(x)|.
$$

### Les mesures de Dirac sont de Radon
La mesure (positive) $\delta_x$ de Dirac en $x \in \R$ est une mesure de
Radon. En effet, toute fonction $f :\R\to\R$ est intégrable pour la mesure
de Dirac, d'intégrale
$$
\int f \, \delta_x  = f(x).
$$
En particulier, si $\varphi \in D^1(\R)$, $\varphi$ est $\delta_x$-intégrable
et de plus
$$
|T[\delta_x] \cdot \varphi| = |\varphi(x)| \leq \sup_{x \in \R} |\varphi(x)|.
$$
L'opérateur $T[\delta_x]$ est donc continu.

### Exercice -- Peigne de Dirac {.exercise}
Soit $c_k$, une famille de réels indexés par $k \in \Z$. 
Montrer que la mesure signée
$\mu = \sum_{k \in \Z} c_k \delta_k$
est de Radon.

### Exercice -- Mesure de comptage {.exercise}
La mesure de comptage $c$ est-elle une mesure de Radon ?


### Les fonctions ordinaires sont (identifiables à) des mesures de Radon
Soit $f:\R \to \R$ une fonction localement absolument intégrable.
Alors si $\ell$ désigne la mesure de Lebesgue sur $\R$, la mesure
signée $f \ell$, telle que pour tout $A \in \mathcal{L}(\R)$,
$$
f\ell(A) := \left|
\begin{array}{rl}
\displaystyle \int 1_A f \, \ell = \int 1_A(x) f(x) \, dx & \mbox{si $1_A f$ est $\ell$-intégrable,} \\
\bot & \mbox{sinon.}
\end{array}
\right.
$$
est une mesure de Radon.

### {.post}
Ce résultat nous permet d'identifier implicitement 
une fonction ordinaire $f$ à la mesure de Radon $f \ell$, notamment
quand des calculs impliquant fonctions et mesures rendront cette démarche
nécessaire.

### Exercice -- Somme de fonction et de mesure {.exercise}
Comment interpréter $\mu = 1_{[0, 1]} - \delta_1$ comme une mesure de Radon ?
Calculer $\mu([0, 1/2])$, $\mu([1/2, 1])$ et $\mu([1, 3/2])$.

![Une représentation d'une mesure signée combinant fonction ordinaire $f$ 
(identifiée à la mesure $f\ell$ ou $\ell$ est la mesure de Lebesgue) et
mesure de Dirac. La partie fonction est représentée par le graphique
habituel et la partie Dirac par les pics déjà décrits.](images/dirac2.py)

### Dérivée mesure {.definition}
Une fonction $f: \R \to \R$ localement absolument intégrable admet 
comme dérivée la mesure de Radon $\mu$ si pour toute fonction test
$\varphi \in D^1(\R)$ on a 
$$
\int_{-\infty}^{+\infty} f(t) \varphi'(t) \, dt
= 
- \int_{-\infty}^{+\infty}\varphi(t) \, \mu(dt).
$$

### Exercice -- Dérivée de l'échelon unitaire {.exercise}
Montrer que l'échelon unitaire $e = 1_{\left[0, +\infty\right[}$ admet pour 
dérivée la mesure de Dirac $\delta_0$.

### {.post}
On remarque que si $f$ admet $g$ comme dérivée faible alors
$$
\begin{split}
\int_{-\infty}^{+\infty} f(t) \varphi'(t) \, dt
&= 
- \int _{-\infty}^{+\infty} g(t) \varphi(t) \, dt \\
&=
- \int _{-\infty}^{+\infty} g(t) \varphi(t)  \, \ell(dt) \\
&= -\int_{-\infty}^{+\infty}\varphi(t) \, g \ell(dt). 
\end{split}
$$
donc $f$ admet $g\ell$ comme dérivée mesure : la convention que nous avons
choisie pour identifier fonctions ordinaires et mesures de Radon
est telle que la notion de dérivée mesure étende celle de dérivée faible.


### Formule des sauts
Soit $f:\R \to \R$ une fonction continûment différentiable par morceaux.
Soit $S$ l'ensemble (dénombrable) des points de discontinuité de $f$ et 
$$
\sigma(x) := f(x_+) - f(x_-) = \lim_{y \to x_+} f(y) - \lim_{y \to x_-} f(y)
$$
le *saut de $f$ en $x$*. 
Si l'on désigne par $f'_{\rm pp}$ une fonction ordinaire égale à la dérivée 
classique de $f$ presque partout, alors $f$ admet comme dérivée mesure 
la somme
$$
f'_{\rm pp} + \sum_{x \in S} \sigma(x) \delta_{x}.
$$


### Démonstration
Soit $\varphi \in D^1(\R)$ et $[a, b]$ un intervalle compact contenant le
support de $\varphi$. Soient $x_j, x_{j+1}, \dots, x_{j+n}$ ceux des 
$x_k$ qui appartiennent à $[a, b]$ (ils sont nécessairement en
nombre fini). Alors on a
$$
\begin{split}
\int_{-\infty}^{+\infty} f(t) \varphi'(t) \, dt
&=
\int_a^{x_j} f(t) \varphi'(t)\, dt
+
\sum_{i=0}^{n-1} \int_{x_{j+i}}^{x_{j+i+1}} f(t) \varphi'(t)\, dt
+
\int_{x_{j+n}}^{b} f(t) \varphi'(t)\, dt \\
\end{split}
$$
et donc par intégration par parties, en utilisant sur chaque segment le
prolongement continument différentiable de $f$ :
$$
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
$$
et par conséquent
$$
\begin{split}
\int_{-\infty}^{+\infty} f(t) \varphi'(t) \, dt
&=
- \int_{a}^b f'(t)\varphi(t) \, dt  \\
&\phantom{=} + f(x_j^-)\varphi(x_j) - f(x_j^+)\varphi(x_j) + \cdots \\
&\phantom{=} + f(x_{j+n}^-)\varphi(x_{j+n}) - f(x_{j+n}^+)\varphi(x_{j+n}).
\end{split}
$$
Il suffit alors de constater que
$$
(f(x_{j+i}^-) - f(x_{j+i}^+)) \varphi(x_{j+i})
= -\sigma({x_{j+i}}) \varphi(x_{j+i})
= - \sigma({x_{j+i}}) \int \varphi \, \delta_{x_{j+i}}
$$
pour conclure.

### Exercice -- Fonction signe {.exercise}
Déterminer la dérivée mesure de la fonction signe.

### Exercice -- Escalier {.exercise}
Déterminer la dérivée mesure de la fonction partie entière.

### Exercice -- "Primitive" {.exercise}
Trouver une fonction continument dérivable par morceaux $f$ dont la dérivée 
mesure soit $\mu = 1_{[0, 1]} - \delta_1$.

-----

### Fonction à variation bornée {.definition}
Une fonction $f:[a, b] \subset \R \to \R$ est à *variation bornée* s'il
existe un réel $M > 0$ tel que pour tout $n \in \N^*$ et tout $n+1$-uplet
$a \leq x_0 \leq \dots \leq x_n \leq b$, 
$$
\sum_{i=0}^{n-1} |f(x_{i+1}) - f(x_i)| \leq M.
$$
Le plus petit $M$ qui convienne est la *variation de $f$ sur $[a, b]$*.
Une fonction $f:\R \to \R$ est *localement à variation bornée* si
sa restriction à tout intervalle compact $[a, b]$ à variation bornée.

### {.ante}
Nous admettrons le résultat suivant :

### Théorème de représentation de Riesz
Une fonction ordinaire $f:\R \to \R$ a une dérivée mesure si et seulement
elle est égale presque partout à une fonction localement à variation 
bornée.

### Fonction de répartition
Une fonction de répartition $F:\R \to \R$ a une dérivée mesure $\mathbb{P}$ 
qui vérifie 
$$\forall a\leq b \in \R, \, F(b) - F(a)= \mathbb{P}(\left]a, b\right]).$$

### Démonstration {.proof}
La fonction de répartition $F$ est croissante ; par conséquent, si
$a \leq x_0 \leq \dots \leq x_n \leq b$
$$
\sum_{i=0}^{n-1} |F(x_{i+1}) - F(x_i)| = \sum_{i=0}^{n-1} (F(x_{i+1}) - F(x_i))
= F(b) - F(a).
$$
La fonction $F$ est donc localement à variation bornée ; 
elle a donc une dérivée mesure $\mu$, 
qui satisfait pour tout $\varphi \in D^1(\R)$
$$
- \int_{-\infty}^{+\infty} F(t) \varphi'(t) \, dt
= 
\int _{-\infty}^{+\infty}\varphi(t) \, \mu(dt).
$$
De façon similaire à la démonstration de ["Dérivation faible et fonctions tests"](#dfft) 
introduisons pour tout intervalle compact $[a, b]$ et pour $\varepsilon>0$ suffisamment
petit les fonctions
$\psi_{\varepsilon} : \R \to \R$ définies par
$$
\psi_{\varepsilon}(t) =
\left| 
\begin{array}{rl}
-6 / \varepsilon^3  \times (t - a)  (t - a - \varepsilon) & \mbox{si $a \leq t \leq a+\varepsilon$,} \\
6 / \varepsilon^3  \times (t - b + \varepsilon)  (t - b) & \mbox{si $b - \varepsilon \leq t \leq b$,} \\
0 & \mbox{sinon.}
\end{array}
\right.
$$
puis $\varphi_{\varepsilon} \in D^1(\R)$ par
$$
\varphi_{\varepsilon}(t) = \int_{-\infty}^t \psi_{\varepsilon}(s) \, ds.
$$
Comme dans la démonstration de ["Dérivation faible et fonctions tests"](#dfft),
en utilisant un changement de variable et le théorème de convergence dominée,
on établit que quand $\varepsilon \to 0$,
$$
-\int_{-\infty}^{+\infty} F(t) \varphi_{\varepsilon}'(t) \, dt
\to F(b^-) - F(a^+).
$$
Par ailleurs, quand $\varepsilon \to 0$, les fonctions $\varphi_{\varepsilon}$ 
convergent simplement vers $1_{\left]a, b\right[}$. Notons $\mu = \sigma \nu$
ou $\nu$ est positive et $\sigma$ est la fonction de signe associée.
Comme les fonctions $\varphi_{\varepsilon}$ peuvent être encadrées par une 
fonction $\nu$-intégrable -- toute fonction positive de $D^1(\R)$ valant plus 
que $1$ sur $[a, b]$ -- par le théorème de convergence dominée on obtient
$$
\int _{-\infty}^{+\infty}\varphi_{\varepsilon}(t) \, \mu(dt) 
\to \int _{-\infty}^{+\infty} 1_{\left]a, b\right[}(t) \, \mu(dt)
= \mu(\left]a, b\right[).
$$
En considérant des intervalles de la forme $\left]a, b\right] \subset \left]a, c\right[$
et en faisant tendre $c$ vers $b^+$, on a d'une part 
$$
F(c^-) - F(a^+) \to F(b^+) - F(a^+)
$$
et d'autre part
$$
\mu(\left]a, c\right[) = \int 1_{\left]a, c\right[} \mu \to \int 1_{\left]a, b\right]} \mu
= \mu(\left]a, b\right])
$$
par le théorème de convergence dominée. On en déduit, comme $F$ est continue
à droite, que $F(b) - F(a) = \mu(\left]a, b\right])$ comme désiré.

<!--
En passant à la limite $a\to -\infty$ **ON A LE DROIT ? SI C'EST TCM, c'est NIET**,
**NOTA: ** j'ai l'impression qu'avec une décompo de type Hahn on y arrive
(note: on peut être juste sur l'union disjointe dénombrable ici, ça suffit).

on obtient donc
$$
F(b^-) = \mu(\left]-\infty, b\right[)
$$
**TODO** PUIS, même chose ici, pour conclure c'est encore variante TCM non ?


### TODO
En gros avec des fcts test appropriées le truc serait bouclé -- on pourrait 
prouver que
$$
F(b^-) - F(a^+) = \mu(\left]a, b \right[)
$$
ce qui sauf erreur suffit -- si l'on pouvait appliquer un théorème de 
cgce monotone, mais il faudrait savoir que $\mu$ est positive (ce qui est
compliqué sans aller aux boréliens)

### TODO
Tjs un gap ici intéressant : on n'a pas explicité TOTALEMENT la mesure,
en particulier la tribu associée. On l'a caractérisé partiellement et
implicitement à travers le fait d'impose que toute fonction continue
à support compact est $\mathcal{A}$-mesurable. Et ça suffit pour que
tout ouvert soit nécesairement mesurable, mais ça n'empêche pas d'avoir
des mesures définies sur des tribus plus grandes ... (ce qui peut apparaitre
comme une restriction artificielle, quand on considère un dirac par
exemple.)

Le pb ici c'est que $\mu$ n'est pas déterminée de façon unique si on ne 
se restreint pas aux Boréliens (et si on se restreint aux Boréliens,
comment montrer que la mesure est définie de façon unique ; d'abord les
ouverts par TCM et après ?).
-->

<!--

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

-->

Tribus engendrées
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
pour pouvoir conclure. Or

  - pour tout $\mathcal{C} \in \mathfrak{S}$, $\varnothing \in \mathcal{C}$,
    donc $\varnothing \in \cap_{\mathcal{C} \in \mathfrak{S}} \mathcal{C}$ ;

  - si $A \in \cap_{\mathcal{C} \in \mathfrak{S}} \mathcal{C}$, alors 
    pour tout $\mathcal{C} \in \mathfrak{S}$, $A \in \mathcal{C}$, donc
    $X \setminus A \in \mathcal{C}$ et par conséquent 
    $X \setminus A \in \cap_{\mathcal{C} \in \mathfrak{S}} \mathcal{C}$ ;

  - si pour tout $k \in \N$, $A_k \in \cap_{\mathcal{C} \in \mathfrak{S}} \mathcal{C}$,
    alors pour tout $\mathcal{C} \in \mathfrak{S}$, $A_k \in \mathcal{C}$, donc
    $\cup_{k=0}^{+\infty} A_k \in \mathcal{C}$ et par conséquent
    $\cup_{k=0}^{+\infty} A_k \in \cap_{\mathcal{C} \in \mathfrak{S}} \mathcal{C}$.

### Exercice -- Singletons de $\N$ {.exercise}
Montrer que la collection des singletons de $\N$ $\{\{n\} \; | \; n \in \N\}$
engendre dans $\N$ la tribu des parties $\mathcal{P}(\N)$.

### Exercice -- Tribu engendrée par une collection finie {.exercise}
Montrer que si $\mathcal{B} = \{A_1, A_2\}$ où $A_1$ et $A_2$ sont des
ensembles de $X$, alors la tribu engendrée par $\mathcal{B}$ dans $X$
contient au plus 16 ensembles. Que devient le résultat quand 
$\mathcal{B} = \{A_1, A_2, A_3\}$ ?

### Exercice -- Tribu engendrée par les ensembles dénombrables {.exercise}
Montrer que la tribu engendrée par les ensembles dénombrables de $\R$ est la
collection des ensembles de $\R$ qui sont dénombrables ou dont le
complémentaire est dénombrable.

### Exercice -- Calculs avec les tribus engendrées {.exercise}
Soit $\mathcal{A}$ et $\mathcal{B}$ deux collections d'ensembles de $X$.
Montrer que $\sigma(\sigma(\mathcal{A})) = \sigma(\mathcal{A})$ et que
si $\mathcal{A} \subset \mathcal{B}$, alors $\sigma(\mathcal{A}) \subset \sigma(\mathcal{B})$.
En déduire que si $\mathcal{A} \subset \mathcal{B} \subset \sigma(\mathcal{A})$, 
alors $\sigma(\mathcal{A})  = \sigma(\mathcal{B})$.

### Tribu de Borel {.definition}
On appelle *tribu de Borel* d'un espace topologique $X$ la tribu
notée $\mathcal{B}(X)$ engendrée
par les ensembles fermés (ou les ensembles ouverts) de $X$.
Les ensembles qu'elle contient sont appelés les *boréliens*.

### Exercice -- Ouverts ou fermés {.exercise}
Montrer que la tribu engendrée par les ensembles ouverts de $X$ est bien
identique à la tribu engendrée par les ensembles fermés de $X$.

### Exercice -- Tribu engendrée par les pavés compacts {.exercise}
Montrer que la tribu engendrée par la collection des pavés compacts
$[a_1, b_1] \times \dots \times [a_n, b_n]$ de $\R^n$ est la tribu
de Borel de $\R^n$. (indication[^up])

[^up]: Commencer par montrer que tout ouvert de $\R^n$ s'écrit comme 
une union dénombrable de pavés compacts de la forme
$[k_1/2^m, (k_1+1)/2^m] \times \dots \times [k_n/2^m, (k_n+1)/2^m]$ où
$m \in \N^*$ et $(k_1, \dots, k_n) \in \Z^n$.

### {.ante}
Nous généralisons désormais la notion de fonction $\mathcal{A}$-mesurable du 
chapitre précédent en tenant désormais explicitement compte d'une tribu dans 
l'ensemble d'arrivée de la fonction :

### Fonction $\mathcal{A}/\mathcal{B}$-mesurable
Une fonction $f: X \to Y$ associée aux espaces mesurables $(X, \mathcal{A})$
et $(Y,\mathcal{B})$ est *mesurable* 
(ou *$\mathcal{A}/\mathcal{B}$-mesurable*)
si l'image réciproque $A =f^{-1}(B)$
de tout ensemble $B$ de $\mathcal{B}$ par $f$ appartient à $\mathcal{A}$.

<!--
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

-->

<!--
### Conventions
Lorsque l'ensemble de départ de $f$ est $X = \R^n$ on supposera sauf
mention contraire que la tribu associée est la tribu de Lebesgue :
$$
\mathcal{A} = \mathcal{L}(\R^n)
\, \mbox{ et } 
\mathcal{B} = ?.
$$
Lorsque l'ensemble d'arrivée $Y$ de $f$ a une structure topologique
-- par exemple $Y = [-\infty, +\infty]$ ou $Y = [-\infty, +\infty]^m$ -- 
on supposera par défaut que la tribu associée est la tribu de Borel :
$$
\mathcal{A} = ? \, \mbox{ et } 
\mathcal{B} = \mathcal{B}(Y).
$$
Lorsque l'on souhaitera munir $X$ et $Y$ de la tribu de Borel,
on parlera de fonction *borélienne* :
$$
\mathcal{A} = \mathcal{B}(X) \, \mbox{ et } \, \mathcal{B} = \mathcal{B}(Y).
$$
Il existe une bonne raison pour favoriser par défaut la convention hybride 
(avec tribu de Lebesgue au départ et de Borel à l'arrivée) pour la définition
de "mesurable" :
-->


<!--
### Lebesgue/Borel-mesurable équivaut à H.-K.-mesurable {.proposition}
Une fonction $f:\R^n \to \R^m$ est limite simple de fonctions intégrables 
au sens de Henstock-Kurzweil
-- c'est-à-dire "mesurable" au sens de ["Calcul Intégral III"](Calcul Intégral III.pdf) --
si et seulement si elle est $\mathcal{L}(\R^n)/\mathcal{B}(\R^m)$-mesurable.
-->

### {.ante}
La notions de $\mathcal{A}$-mesurabilité du chapitre précédent correspond
implicitement à la notion plus générale de mesurabilité quand la tribu de Borel 
est sélectionnée sur l'espace d'arrivée :

### $\mathcal{A}$-mesurable équivaut à $\mathcal{A}/\mathcal{B}(Y)$-mesurable.
Soit $(X, \mathcal{A})$ un espace mesurable et $Y$ un espace topologique.
Une fonction $f: X \to Y$ est $\mathcal{A}$-mesurable -- au sens où
l'image réciproque par $f$ de tout ouvert (ou fermé) de $Y$ appartient 
à $\mathcal{A}$ -- si et seulement si elle est $\mathcal{A}/\mathcal{B}(Y)$-mesurable.

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


### Démonstration "$\mathcal{A}$-mesurable $\leftrightarrow$ $\mathcal{A}/\mathcal{B}(Y)$-mesurable" {.proof}
De toute évidence, si $f$ est $\mathcal{A}/\mathcal{B}(Y)$-mesurable, 
comme tout ouvert appartient à la tribu de Borel, l'image réciproque par
$f$ de tout ouvert de $Y$ appartient bien à $\mathcal{A}$ donc
$f$ est $\mathcal{A}$-mesurable.

Réciproquement, si l'image réciproque de tout ouvert de $Y$
est $\mathcal{A}$-mesurable, alors la tribu engendrée par les images réciproques
des ouverts de $Y$ est incluse dans $\mathcal{A}$.
Comme cette tribu est d'après [le lemme précédent](#irte) l'ensemble
des images réciproques par $f$ de la tribu engendrée par les ouverts dans $Y$,
c'est-à-dire la tribu de Borel dans $Y$, l'image réciproque de tout
borélien est un ensemble de $\mathcal{A}$ : la fonction 
$f$ est $\mathcal{A}/\mathcal{B}(Y)$-mesurable.

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

### Fonction boréliennes
Soit $X$ et $Y$ deux espaces topologiques. Une fonction $f : X \to Y$ est
*borélienne* si elle est $\mathcal{B}(X)/\mathcal{B}(Y)$-mesurable.

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

### Exercice -- Fonctions croissantes {.exercise}
Soit $f: \R \to \R$ ; montrer que si l'image réciproque par $f$
de tout intervalle compact est un intervalle compact alors $f$ est borélienne.
En déduire que si $f$ est croissante alors $f$ est borélienne.

<!--
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

-->

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
================================================================================

Dans cette section, nous affirmons sans preuve quelques résultats fondamentaux 
associés aux produits de mesures et aux intégrales associées. 
Le lecteur cherchant plus d'informations sur ce volet 
-- dont les démonstrations sont techniques -- 
pourra consulter @Hun11 ou @Tao11.

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
L'espace mesurable $(X \times Y, \mathcal{A} \otimes \mathcal{B})$ est appelé 
*espace produit* des espaces mesurables $(X, \mathcal{A})$ et 
$(Y, \mathcal{B})$.

### Exercice -- Produit d'ensemble de parties {.exercise}
Montrer que $\mathcal{P}(\N) \otimes \mathcal{P}(\N) = \mathcal{P}(\N \times \N)$
(attention : [le résultat n'est pas vrai si l'on remplace $\N$ par un ensemble
$X$ "trop grand" !](https://math.stackexchange.com/questions/3029309/product-sigma-algebra-of-power-sets)).

### Produit des tribus de Borel
La tribu de Borel sur $\R^{m+n}$ est le produit des tribus de Borel sur 
$\R^m$ et $\R^n$ :
$$
\mathcal{B}(\R^{m+n}) = \mathcal{B}(\R^{m}) \otimes \mathcal{B}(\R^{n}).
$$

<!--
### Exercice -- Produit de tribus de Borel  {.exercise}
Montrer que $\mathcal{B}(\R^{m}) \otimes \mathcal{B}(\R^{n}) \subset \mathcal{B}(\R^{m+n})$.
-->

### Produit et tribu de Lebesgue
Notons que le résultat similaire est faux pour la mesure de Lebesgue : 
  $$
  \mathcal{L}(\R^{m+n}) \neq \mathcal{L}(\R^{m}) \otimes \mathcal{L}(\R^{n}).
  $$
Pour obtenir $\mathcal{L}(\R^{m+n})$, 
il est nécessaire de compléter la tribu produit $\mathcal{L}(\R^m) \otimes \mathcal{L}(\R^n)$
par rapport à la mesure de Lebesgue sur $\R^{m+n}$, c'est-à-dire de rajouter les
ensembles négligeables pour la tribu de Lebesgue à la collection, 
puis de construire la tribu engendrée
(cf. [exercice "Complétion d'une mesure" du chapitre IV](Calcul Intégral IV.pdf#complétion)).

### {.post}
Pour pallier cette difficulté technique, une autre option consiste 
à systématiquement restreindre les mesures que l'on considère aux boréliens.

### Mesure de Borel {.definition}
On appelle *mesure de Borel* sur un espace topologique $X$ toute mesure 
définie sur la tribu des boréliens $\mathcal{B}(X)$.

### {.post}
A toute mesure $\mu$ définie sur une tribu $\mathcal{A}$ de $X$ contenant 
$\mathcal{B}(X)$ on peut associer une tribu de Borel $\nu$ en restreignant
$\mu$ à $\mathcal{B}(X)$. 
$$
\nu :\mathcal{B}(X) \to [0, +\infty] \; \mbox{ et } \; \forall A \in \mathcal{B}(X), \, \nu(A) := \mu(A).
$$
En particulier on appelle 
*mesure de Borel-Lebesgue sur $\R^n$* la restriction de la mesure
de Lebesgue de $\mathcal{L}(\R^n)$ à $\mathcal{B}(\R^n)$.

### Exercice -- Mesures de Borel classiques {.exercise}
Peut-on associer une mesure de Borel à une mesure de Dirac $\delta_x$ sur $\R^n$ ?
A la mesure de comptage sur $\R^n$ ?

### Exercice -- Mesure de Borel ? {.exercise}
Soit $\mathcal{A} = \{\varnothing, \R\}$ et $\mu: \mathcal{A} \to [0, +\infty]$
définie par $\mu(\varnothing)=0$ et $\mu(\R) = 1$. Montrer que $\mu$ est une
mesure sur $(\R, \mathcal{A})$ ; peut-on lui associer une mesure de Borel sur
$\R$ ?


### Mesure produit
Soient $(X, \mathcal{A}, \mu)$ et $(Y, \mathcal{B}, \nu)$ deux espaces mesurés.
On appelle *mesure produit* de $\mu$ et $\nu$ 
et l'on note $\mu \otimes \nu$ la mesure définie sur 
$\mathcal{A} \otimes \mathcal{B}$ par
$$
(\mu \otimes \nu) (C) = \inf
\left\{ 
\sum_{k=0}^{+\infty} \mu(A_k) \nu(B_k) 
\; \left| \vphantom{\sum_{k=0}^{+\infty}} \right. \;
A_k \in \mathcal{A}, \ B_k \in \mathcal{B}, \, C \subset \bigcup_{k=0}^{+\infty} A_k \times B_k \right\}.
$$
L'espace mesuré $(X \times Y, \mathcal{A} \otimes \mathcal{B}, \mu \otimes \nu)$ est appelé 
*espace produit* des espaces mesurés $(X, \mathcal{A}, \mu)$ et 
$(Y, \mathcal{B}, \nu)$.



### Exercice -- Produit de Diracs {.exercise}
Soit $m, n \in \N$ et $\delta_m, \delta_n$ les mesures de Dirac associées sur
$\N$. Montrer que $\delta_m \otimes \delta_n = \delta_{(m, n)}$, c'est-à-dire
que pour tout $C \in \N^2$,
$$
\delta_{(m, n)} (C) = \left|
\begin{array}{rl}
1 & \mbox{si $(m, n) \in C$,} \\
0 & \mbox{sinon.}
\end{array}
\right.
$$

### Exercice -- Produit de mesures de comptage {.exercise}
Soit $c_X$ la mesure de comptage sur $X$.
Montrer que pour tout $C \in \mathcal{P}(X) \otimes \mathcal{P}(Y)$,
$(c_X \otimes c_Y)(C) = c_{X \times Y}(C).$
(indication[^ind])

[^ind]: Montrer que pour tout ensemble fini
$C \subset X \times Y$,
$\sum_{(a,b) \in C} c_X(\{a\}) c(\{b\}) = \mbox{card}(C)$ ;
En déduire que si les $A_k \times B_k$ recouvrent $C$, 
alors $\sum_{k=0}^{+\infty} c_X(A_k) c_Y(B_k) \geq \mbox{card}(C)$
et conclure et calculant $(c_X \otimes c_Y)(C)$ lorsque $C$ est fini
puis infini.


<!--si $A\in\mathcal{P}(X)$, $B \in \mathcal{P}(Y)$, $a \in A$ et
$b \in B$, alors 
$$A \times B = (\{a\} \times \{b\}) \cup ((A \setminus \{a\}) \times \{b\}) \cup (A \times (B \setminus \{b\})).$$-->

### Mesure extérieure produit {.post}
On remarquera que l'expression ci-dessus qui définit $(\mu \otimes \nu) (C)$ a du sens
pour tout ensemble $C$ de $\R^{m+n}$, pas uniquement pour les ensembles de
$\mathcal{A} \otimes \mathcal{B}$. On peut prouver sans difficulté que cette
expression définit en fait une mesure extérieure $(\mu \otimes \nu)^*$
(un concept qui a été introduit dans l'annexe de "Calcul Intégral IV"). 
Pour prouver le théorème ci-dessus il suffit alors d'établir que 
tout produit $A \times B$ où $A \in \mathcal{A}$ et $B \in \mathcal{B}$ est 
$(\mu \otimes \nu)^*$-mesurable.

### Intégrale dans un espace produit {.notation}
Soient $(X, \mathcal{A}, \mu)$ et $(Y, \mathcal{B}, \nu)$ deux espaces mesurés.
Pour toute fonction $\mu \otimes \nu$-mesurable 
$f: X \times Y \to [0, +\infty]$ ou toute fonction $\mu \otimes \nu$-intégrable
$f: X \times Y \to [-\infty, +\infty]$, on notera
$$
\int_{X \times Y} f(x, y) \mu(dx)\nu(dy) := 
\int f (\mu \otimes \nu).
$$

### Mesures finies et $\sigma$-finie
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré. La mesure $\mu$ est *finie* si
$\mu(X) < +\infty$ ; elle est *$\sigma$-finie* s'il existe une suite d'ensembles 
mesurables $A_k \in \mathcal{A}$, $k \in \N$, telle que 
$$
\bigcup_{k=0}^{+\infty} A_k = X 
\; \mbox{ et } \; 
\forall \, k \in \N, \, \mu(A_k) < +\infty.
$$

### Exercice -- Mesure de probabilité {.exercise}
Une mesure de probabilité est-elle finie, $\sigma$-finie ?

### Exercice -- Mesures $\sigma$-finies {.exercise}
Etudier si les mesures suivantes sur $\R^n$ sont ou non finies et/ou $\sigma$-finies : 
les mesures de Dirac, la mesure de comptage, la mesure de Lebesgue.


### Unicité de la mesure produit {.theorem}
Soit $(X, \mathcal{A}, \mu)$ et $(Y, \mathcal{B}, \nu)$ deux espace mesurés,
tels que les mesures $\mu$ et $\nu$ soient $\sigma$-finies.
Alors la mesure produit $\mu \otimes \nu$ est l'unique mesure sur 
$(X \times Y, \mathcal{A} \otimes \mathcal{B})$ telle que
$$
\forall A\in \mathcal{A}, \, \forall B \in \mathcal{B}, 
\, (\mu \otimes \nu) (A \times B) = \mu(A) \times \mu(B).
$$

### Exercice -- Mesure de Borel-Lebesgue
Soit $\ell$ la mesure de Borel-Lebesgue sur $\R$. 
Soit $A = [-2,2] \times [-1,1] \cup [-1,1] \times [-2,2]$  ;
montrer que $A$ est un borélien de $\R^2$ et calculer 
$(\ell \otimes \ell) (A)$.

### Mesure de Borel-Lebesgue
La mesure de Borel-Lebesgue sur $\R^{m+n}$ est le produit des mesures 
de Borel-Lebesgue sur $\R^m$ et $\R^n$.

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

### Symétrie
Le rôle joué par $X$ et $Y$ étant symétrique dans l'énoncé du théorème de
Fubini, on peut également dire qu'une fonction mesurable $f: X \times Y \to \R$
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

### Exercice -- Convolution de Dirac {.exercise}
Soit $a, b \in \R$ et $C \in \mathcal{B}(\R)$. Montrer que
$$
?(C) = \int 1_C(x + y) \, \delta_a(dx) \delta_b(dy).
$$
est bien défini et calculer sa valeur.
(indication[^Cv]) 

[^Cv]: Si l'on note $C - v = \{c - v \; | \; c \in C \}$, alors on
a $1_C(u + v) = 1_{C-v} (u)$.

### Exercice -- Intégrale et séries doubles {.exercise}
Soit $f : \N \times \N\to \R$ une fonction telle que 
$$
\sum_{n=0}^{+\infty} \left(\sum_{m=0}^{+\infty} |f(m, n)| \right) < +\infty.
$$
Montrer que
$$
\sum_{n=0}^{+\infty} \left(\sum_{m=0}^{+\infty} f(m, n) \right)
=
\sum_{m=0}^{+\infty} \left(\sum_{n=0}^{+\infty} f(m, n) \right).
$$

### Exercice -- Asymétrie {.exercise}
Soit $\ell$ la mesure de Lebesgue sur $\R$ et $c$ la mesure de comptage sur
$\R$. On note $D = \{(x, x) \; | \; x \in [0,1]\}$. Calculer (en justifiant
l'existence des termes)
$$
\int \left(\int 1_D(x, y) \, \ell(dx) \right)  c(dy)
\; \mbox{ et } \;
\int \left(\int 1_D(x, y) \, c(dy) \right)  \ell(dx)
$$
et comparer ces deux valeurs. Comment expliquez-vous ce résultat ?

Exercices corrigés
================================================================================

Dérivée faible {.question #dr}
--------------------------------------------------------------------------------

Est-ce que la fonction $f: \R \to \R$ définie par $f(0)=0$ et
$$
f(x) = \sqrt{|x|} \, \mbox{ si $x\neq 0$}
$$
est faiblement dérivable ? Quelle est dans ce cas sa dérivée ?

Mesure signée et $\sigma$-additivité {.question #mssa}
--------------------------------------------------------------------------------
Les mesures signées sont-elles comme les mesures positives
$\sigma$-additives, c'est-à-dire telles que 
$$
\mu\left(\bigcup_{k=0}^{+\infty}A_k \right) = \sum_{k=0}^{+\infty} \mu(A_k)
$$ 
quand les $A_k$ sont disjoints ? 
Indication : on pourra étudier 
$\mu = \ell|_{\R_+} - \ell_{\R_-}$, définie pour tout $A \in \mathcal{L}(\R)$
par
$$
\mu(A) =
\ell(\left[0, +\infty\right[\cap A) - \ell(\left]-\infty, 0\right]\cap A)
$$
et rechercher une partition dénombrable
de $\R$ par des $A_k$ tels que $\mu(A_k) = 0$.


Etudier à nouveau le problème sous l'hypothèse supplémentaire que 
$\mu\left(\bigcup_{k=0}^{+\infty}A_k \right)$ est réel.


Dérivée mesure {.question #dm}
--------------------------------------------------------------------------------

Soit $\tau > 0$. On considère la fonction $f:\R\to\R$ qui est $\tau$-périodique
et telle que 
$$
\forall t \in \left[0, \tau \right[, \; f(t) = \sin t.
$$ 

![](images/sin.py)

Montrer que $f$ admet une dérivée mesure que l'on déterminera. A quelle
condition sur $\tau$ cette mesure est-elle une fonction ordinaire (et $f$
est-elle dérivable faiblement) ?
La fonction $f$ est-elle pour autant dérivable classiquement en tout
point $t$ de $\R$ ?

<!--

Fonctions convexes
--------------------------------------------------------------------------------

Equivalent dérivée seconde est une mesure positive ?

Fonction distance
--------------------------------------------------------------------------------

Dérivées seconde fonction distance, squelette, courbure, etc ?

-->

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


Dérivée faible {.answer #answer-dr}
--------------------------------------------------------------------------------

Si $f$ admet une dérivée faible, elle est nécessairement égale presque partout
à la dérivée classique de $f$, qui vaut
$$
g(x) := f'(x) = \frac{\mathrm{sgn}(x)}{2\sqrt{x}}.
$$
On peut compléter la dérivée faible potentielle $g$ en posant $g(0)=0$.
Il faut ensuite vérifier que pour tout $x \in \R$ on a bien
$$
f(x) = f(0) + \int_0^x g(t) \, dt.
$$
Pour $x >0$ par exemple, on peut déduire de
$$
\int_{\varepsilon}^x g(t) \, dt = \int_{\varepsilon}^x \frac{dt}{2\sqrt{t}}
= \sqrt{t} - \sqrt{\varepsilon}
$$
et du théorème de convergence monotone la relation souhaitée. 
La situation est similaire pour $x < 0$. La fonction $f$ initiale est
donc bien faiblement dérivable.


Mesure signée et $\sigma$-additivité {.answer #answer-mssa}
--------------------------------------------------------------------------------

La réponse est non, les mesures signées ne sont pas nécessairement
$\sigma$-additives. Considérons en effet
$\mu = \ell|_{\R_+} - \ell|_{\R_-}$ et les ensembles mesurables
$$
A_0 = \{0\} \, \mbox{ puis } \, A_k = \left[-k-1, -k\right[ \cup \left]k, k+1\right] \, \mbox{ pour $k\geq 1$}.
$$
Tous ces ensembles sont de mesure $\mu$ nulle et donc 
$$
\sum_{k=0}^{+\infty} \mu(A_k) = 0.
$$
Pourtant ils forment une partition dénombrable de $\R$ et comme la fonction
$\mathrm{sgn}$ n'est pas $\ell$-intégrable sur $\R$, on a 
$$
\mu\left(\cup_{k=0}^{+\infty} A_k\right) = \mu(\R) = \bot.
$$

Par contre, si l'on sait que $A := \cup_{k=0}^{+\infty} A_k$ est de mesure 
$\mu = \sigma \nu$
réelle, cela signifie que la fonction caractéristique $1_A$ est $\nu$-intégrable. 
Les fonctions $f_j$ définies par
$$
f_j \sigma = 1_{\cup_{k=0}^j A_k} \sigma = \sum_{k=0}^j 1_{A_k} \sigma
$$
sont $\nu$-mesurables, dominées en valeur absolue par $1_A$ et 
$f_j \sigma$ converge simplement vers $1_A \sigma$. 
On a donc par le théorème de convergence dominée
$$
\sum_{k=0}^{+\infty} \mu(A_k) = \lim_{j \to +\infty} \int f_j \sigma \, \nu
=
\int 1_A \sigma \, \nu = \mu(A).
$$


Dérivée mesure {.answer #dm}
--------------------------------------------------------------------------------

La fonction $f$ est continûment dérivable par morceaux donc elle admet une
dérivée mesure donnée par la formule des sauts, en l'occurence si l'on 
nomme $g$ la fonction $\tau$-périodique telle que 
$$
\forall t \in \left[0, \tau \right[, \; g(t) = \cos t.
$$ 
alors comme les seuls sauts possibles de $f$ sont en $k\tau$ pour
$k \in \Z$ et valent
$$
\sigma_{k\tau}  = \sin 0 - \sin \tau = \sin \tau
$$
cette dérivée mesure est
$$
g + \sum_{k \in \Z} (\sin \tau) \delta_{k \tau}.
$$
C'est une fonction ordinaire si et seulement si $\sin \tau$ est nul, 
c'est-à-dire si $\tau \in \pi \Z$. Mais la fonction $f$ n'est dérivable
en tout point que si $\tau \in 2\pi \Z$ (c'est-à-dire si $f=\sin$).


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