% Calcul Intégral I
% Sébastien Boisgérault

**TODO:** intervalle (borné ou non borné par défaut).

**TODO:** longueur $\ell(I)$ d'un intervalle.

**TODO:** "longueur nulle" (dans limitations de Riemann)

**TODO:** intégrale d'une fonction nulle presque partout (par étapes: 1 / nb
finies de valeurs égale à 1, puis fct de Dirichlet, puis fct égale à un sur
un ensemble de mesure nulle, puis cas général, ce type de progression 
(même si pas exactement celle-là, on a peut-être ))

--------------------------------------------------------------------------------

### Subdivision pointée {.definition}
Une *[subdivision]{.index}* de l'intervalle fermé $I = [a,b]$
est une famille finie
$$
\{I_i \; | \; \; 0 \leq i \leq n-1 \}
$$
constituée d'intervalles fermés de $I$, ne se chevauchant pas 
-- si $i$ et $j$ diffèrent, l'intersection de $I_i$ et $I_j$ contient au 
plus un point -- et recouvrant $I$ -- l'union de l'ensemble des $I_i$
est égal à $I$. 
Une *[subdivision pointée]{.index}* de l'intervalle fermé $I = [a, b]$ 
de $\mathbb{R}$ une famille finie 
$$
\{(t_i, I_i) \; | \; \; 0 \leq i \leq n-1\}
$$
où les $I_i$ forment une subdivision de $I$ et 
$t_i \in I_i$ pour tout $i \in \{0, \dots, n-1\}.$

**TODO:** alternative passant par 
$$
a = x_0 \leq \cdots \leq x_i \leq t_i \leq x_{i+1} \leq \cdots \leq x_{n} = b.
$$

### Gauge {.definition}
Une *[gauge]{.index}* sur $I = [a, b]$ est une fonction $\gamma$
qui associe à tout $t$ de $[a, b]$ un intervalle ouvert de $\mathbb{R}$
contenant $t$. 

### Subdivision pointée subordonnée à une gauge {.definition}
Une subdivision $\mathcal{D}$ de l'intervalle fermé $I$ 
est *subordonnée à une gauge* $\gamma$ de $I$ si 
$$
\mbox{pour tout } (t, J) \in \mathcal{D}, \; J \subset \gamma(t). 
$$

### Représentation graphique

On peut associer à une gauge $\gamma$ sur $[a, b]$ l'ensemble du plan
$$
\{(x, y) \; | \; x \in [a, b], \, y \in \gamma(x) \}.
$$
Par construction, cet ensemble contient la diagonale 
$$
D = \{(x,x) \; | \; x \in [a, b]\}.
$$

**TODO:** example, et expliquer pourquoi cette représentation est pratique
pour visualiser si une subdivision pointée est subordonnée à une gauge.

Par exemple, la gauge $\gamma$ définie sur $[0,1]$ par 
$\gamma(t) = \left] t-0.25, t+0.25 \right[$ est représentée comme suit:

\newcommand{\lb}{[}
\newcommand{\rb}{]}
\newcommand{\lob}{\left]}
\newcommand{\rob}{\right[}

![Graphe de la jauge $\gamma(t) = \lob t-0.2, t+0.2 \rob ,$
$t \in \lb 0, 1 \rb .$](images/gauge-plot.pdf)

**TODO:** graphique d'une subdivision pointée, avec séparateurs en barres
verticales et $t_i$ en croix.

### Lemme de Cousin {.theorem}
Pour toute fonction de gauge $\gamma$ sur l'intervalle fermé $I$, 
il existe une subdivision $\mathcal{D}$ qui soit subordonnée à $\gamma$.

### Preuve {.proof}
S'il existe un $t \in I^0 = I = [a, b]$ tel que $I \subset \gamma(t)$, 
la subdivision $\mathcal{D} = \{(t, I)\}$ convient.
Sinon, on peut considérer les intervalles $I_0^1 = [a, (a+b)/2]$ et
$I_1^1 = [(a+b)/2, b]$ et examiner pour chacun de ces intervalles
s'il existe un $t_i \in I_i^1$ tel que $I_i^1 \subset \gamma(t_i)$,
dans ce cas ajouter la paire $(t_i, I_i^1)$ à la famille $\mathcal{D}$
et dans le cas contraire décomposer à nouveau l'intervalle posant 
problème. 
Soit ce procédé converge en un nombre fini d'étapes et forme
une subdivision pointée $\mathcal{D}$ de $I$, 
soit nous avons construit une infinité d'intervalles fermés $J_i$ 
emboités ($J_{i+1} \subset J_i$) de $I$ tels que pour tout 
$t \in J_i$, $J_i \not \subset \gamma(t)$.

Montrons que ce second scénario est impossible.
Comme les $J_i$ sont emboités, la collection
$\{J_i \; | \; i \in \mathbb{N}\}$ possède la
propriété de l'intersection finie. 
L'intervalle $I$ étant compact, cela implique qu'il existe un $t \in I$
tel que pour tout $i \in \mathbb{N}$, $t$ soit adhérent à $J_i$.
Les $J_i$ étant fermés, $t$ appartient à chaque $J_i$.
La longueur de $J_i$ étant divisée par deux à chaque incrément de $i$,
$\ell(J_i) = \ell(J_0) / 2^i$ et comme $t_i \in J_i$, 
$J_i \subset [t_i - \ell(J_0) / 2^i, t_i + \ell(J_0) / 2^i]$.
Par conséquent, il existe un rang $i$ à partir duquel
$J_i \subset \gamma(t)$, ce qui contredit l'hypothèse de départ.

#### Note

Si l'argument topologique peut être survolé, la procédure de dichotomie est
intéressante et peut être utilisé sur des exemples concrets, ça vaudrait le
coup de la faire "pour de vrai".

Au passage, il faut s'arranger pour "lemmatiser" le résultats "... et le 
processus termine en un nombre fini d'étapes" plus clairement.

### Somme de Riemman {.definition}

La somme de Riemann associée à la fonction $f:[a, b] \to \mathbb{R}$ 
et à la subdivision pointée $\mathcal{D}$ de $[a, b]$ est la grandeur
$$
S(f, \mathcal{D}) = \sum_{(t, I) \in \mathcal{D}} f(t) \ell(I)
$$

Alternative:
$$
S(f, \mathcal{D}) = \sum_{i=0}^{m-1} f(t_i) (x_{i+1} - x_i)
$$

**TODO.** Notation $\int_a^b$ when $a>b$.

### Intégrale {.definition}
Une fonction $f:[a, b] \to \mathbb{R}$ est dite *intégrable 
(au sens de Henstock-Kurzweil)* s'il existe un réel $I$ tel
que pour tout $\varepsilon > 0$ il existe une gauge $\gamma$
sur $[a, b]$ telle que pour toute subdivision pointée 
$\mathcal{D}$ subordonnée à $\gamma$, on ait
$|S(f, \mathcal{D}) - I| \leq \varepsilon$.
Le réel $I$ quand il existe est unique; il est appelé
*intégrale de $f$ sur $[a, b]$* et noté
$$
\mbox{(HK-)}\int_a^b f(t) \, dt.
$$

### Intégrale de Riemann {.theorem}
Toute fonction $f:[a,b] \mapsto \mathbb{R}$ intégrable au sens de Riemann
est intégrable au sens de Henstock-Kurzweil et les deux intégrales coïncident.

### Def Riemann + Preuve

**TODO**. Passer par l'intermédiaires des gauges numériques ? Bof. Directement
avec de $\delta > 0$ uniforme à l'intervalle ouvert.

### Théorème fondamental du calcul {.theorem}
Si la fonction $f:[a, b] \to \mathbb{R}$ est dérivable sur $[a, b]$,
la dérivée function dérivée $f'$ est intégrable sur $[a, b]$ et 
  $$
  f(b) - f(a) = \int_a^b f'(t) \, dt.
  $$

### Théorème fondamental du calcul (alternatif) (Corollaire ?) {.theorem}
Toute fonction $f:[a,b] \mapsto \mathbb{R}$ intégrable au sens de Newton
est intégrable au sens de Henstock-Kurzweil et les deux intégrales coïncident.

**QUESTION** exfiltrer le "Straddle Lemma"? Ca sera probablement plus clair.
L'autre option est de splitter un cran plus avant la somme qui majore l'erreur
entre somme de Riemann et intégral ... à voir. Arf, ça ne marche pas, tss tss...

### Preuve {.proof}
Nous souhaitons établir que $f':[a, b] \to \mathbb{R}$ est intégrable, 
d'intégrale égale à $f(b) - f(a)$.
Pour cela, nous devons montrer que pour tout $\varepsilon > 0$ il existe 
une fonction de gauge $\gamma$ sur $[a, b]$ telle que, 
si une subdivision pointée 
$$
\mathcal{D} = \{(t_0, [x_0, x_1], \dots, (t_{m-1}, [x_{m-1}, x_m]))\}
$$ 
vérifie pour tout $i \in \{0, \dots, m-1\},$ 
$[x_i,x_{i+1}] \subset \gamma(t_i),$ alors 
$$
|S(f', \mathcal{D}) - (f(b) - f(a))| \leq \epsilon.
$$
Notons que si $\mathcal{D} = \{(t_0, [x_0, x_1], \dots, (t_{m-1}, [x_{m-1}, x_m]))\}$,
le membre de gauche de cette inégalité vérifie
$$
\begin{split}
|S(f', \mathcal{D}) - (f(b) - f(a))| 
  &= \left|\sum_{i=0}^{m-1} f'(t_i)(x_{i+1} - x_i) - (f(b) - f(a))\right| \\
  &= \left|\sum_{i=0}^{m-1} f'(t_i)(x_{i+1} - x_i) - \sum_{i=0}^{m-1} (f(x_{i+1}) - f(x_i)) \right| \\
  &= \left|\sum_{i=0}^{m-1} (f'(t_i)(x_{i+1} - x_i) - (f(x_{i+1}) - f(x_i))) \right| \\
  &\leq \sum_{i=0}^{m-1} \left| f'(t_i)(x_{i+1} - x_i) - (f(x_{i+1}) - f(x_i)) \right| \\
\end{split}
$$

Fixons donc un $\varepsilon' > 0$ arbitraire.
Comme pour tout $t \in [a, b],$ 
$$f(t+h) = f(t) + f'(t) h + o(h),$$
il existe un $\delta(t) > 0$ tel que si $|h| < \delta (t),$
$$
|f'(t) h - (f(t+h) - f(t))| \leq \varepsilon' |h|
$$
Par conséquent, si le sous-intervalle fermé $[c, d]$ de $[a, b]$ est tel
que
$$
t \in [c, d] \subset \left]t-\delta(t), t+\delta(t)\right[,
$$ 
nous avons
$$
|f'(t) (d-t) - (f(d) - f(t))| \leq \varepsilon' |d - t| = \varepsilon' (d-t)
$$
ainsi que
$$
|f'(t) (c-t) - (f(c) - f(t))| \leq \varepsilon' |c - t| = \varepsilon' (t - c).
$$
L'inégalité triangulaire fournit alors
$$
|f'(t)(d - c) - (f(d) - f(c))| \leq \varepsilon' (d - c)
$$
Posons $\gamma(t) = \left]t - \delta(t), t + \delta(t)\right[;$
nous avons ainsi bien défini une fonction de gauge.
Si $\mathcal{D}$ est subordonnée à $\gamma$, 
pour tout $i \in \{0, \dots, m-1\},$ 
$$t_i \in [x_i,x_{i+1}] \subset \left]t_i - \delta(t_i), t_i + \delta(t_i)\right[,$$
par conséquent 
$$
|f'(t_i)(x_{i+1} - x_i) - (f(x_{i+1}) - f(x_i))| \leq \varepsilon' (x_{i+1} - x_i).
$$
Exploitons cette inégalité pour majorer l'erreur entre la somme de Riemann et
l'intégrale de $f'$; nous avons
$$
\begin{split}
|S(f', \mathcal{D}) - (f(b) - f(a))| 
&\leq \sum_{i=0}^{m-1} \left| f'(t_i)(x_{i+1} - x_i) - (f(x_{i+1}) - f(x_i)) \right| \\
&\leq \sum_{i=0}^{m-1} \varepsilon' (x_{i+1} - x_i) \\
&= \varepsilon' \sum_{i=0}^{m-1} (x_{i+1} - x_i) \\
&= \varepsilon' (x_m - x_0) \\
&= \varepsilon' (b - a) \\
\end{split}.
$$
Il suffit de choisir un nombre réel positif $\varepsilon'$ tel que
$\varepsilon' (b-a) \leq \varepsilon$ pour obtenir l'inégalité recherchée.

### Exemple: $x \mapsto e^x$.
La fonction $f: x \mapsto e^x$ est intégrable au sens de Newton
sur tout intervalle compact $[a, b]$ de $\mathbb{R}$
puisqu'elle admet $x \mapsto e^x$ comme primitive. 
On a ainsi
$$
\int_a^b e^x \,dx 
= 
\left[ e^x \right]_a^b
= e^b - e^a. 
$$
Par le théorème fondamental du calcul, 
$f$ est intégrable au sens de Henstock-Kurzweil et l'intégrale associée 
coïncide avec l'intégrale de Newton.
Pour toute intervalle $[a, b]$ et toute précision $\varepsilon > 0$, 
il existe donc une gauge $\gamma$ 
telle que pour toute subdivision pointée $\mathcal{D}$ subordonnée à $\gamma$,
l'écart entre $S(f, \mathcal{D})$ et la valeur de l'intégrale
soit au plus $\varepsilon(b-a)$.

Construisons une telle gauge en nous inspirant de la preuve du théorème
fondamental du calcul. Dans cette preuve, nous avons montré que la précision
$\varepsilon (b-a)$ était atteinte
si nous choisissions 
$\gamma(t) = \left]t-\delta(t), t+\delta(t)\right[$
où $\delta(t) > 0$ est tel que si $|h| \leq \delta(t)$, alors
$$
|f(t+h) - f(t) - f'(t)h| \leq \varepsilon |h|.
$$

Explicitons cette contrainte dans le cas de la fonction 
$x \in \mapsto e^x$. 
Cette fonction étant deux fois différentiable sur
$[0, 1]$, la formule de Taylor avec reste intégral nous fournit
$$
|f(t+h) - f(t) - f'(t)h|
= 
\left| \int_t^{t+h}  f''(x) (t + h - x) \, dx \right|.
$$
Dans ce cas précis, puisque $f''(x) = e^x$, lorsque $h\geq0$ nous avons
$$
\left| \int_t^{t+h}  f''(x) (t + h - x) \, dx \right|
\leq 
e^{x+h} \int_t^{t+h} (t+h-x)\, dx
= e^{x+h} h^2 / 2
$$
Lorsque $h < 0$, on peut montrer que
$$
\left| \int_t^{t+h}  f''(x) (t + h - x) \, dx \right|
\leq
e^x h^2 / 2.
$$
Dans tous les cas,pour garantir que $|f(t+h) - f(t) - f'(t)h| \leq \varepsilon |h|,$
sous l'hypothèse que $|h| \leq \delta(t),$
il est donc suffisant de nous assurer que 
$e^{x+\delta(t)} \delta(t) /2 \leq \varepsilon,$
soit 
$\delta(t) e^{\delta(t)}  \leq 2 e^{-x}\varepsilon.$
La fonction $y \in \mathbb{R} \to y e^y \in \left]0, +\infty\right[$ est 
croissante et bijective; son inverse est par définition 
la fonction $W$ de Lambert. Le plus grand $\delta(t)$ satisfaisant 
l'inégalité précédente est donc donné par
$$
\delta(t) = W \left( 2e^{-x}\varepsilon\right)
$$
En conclusion: pour tout $[a, b]$ et tout $\varepsilon > 0$, 
la gauge $\gamma$ sur $[a, b]$ définie par
$$
\gamma(t) = 
\left]
t - W \left( 2e^{-x}\varepsilon\right),
t + W \left( 2e^{-x}\varepsilon\right)
\right[
$$
est telle que pour toute subdivision pointée $\mathcal{D}$ de $[a, b]$ 
subordonnée à $\gamma$
$$
\left|S(x\mapsto e^x, \mathcal{D}) - \int_a^b e^x \, dx \right| \leq \varepsilon(b-a).
$$

**TODO:** représentation graphique de la gauge pour un (des ?) $\varepsilon$ 
bien choisis.


--------------------------------------------------------------------------------

### Exemple: $1/\sqrt{x}$.

Considérons la fonction $f:[0,1] \to \mathbb{R}$ définie par
$$
f(x) = 
\left|
\begin{array}{rl}
1/\sqrt{x} & \mbox{si } \, x > 0, \\
0          & \mbox{si } \, x = 0.
\end{array}
\right.
$$

Options: "manuellement" avec 3 hunches à avoir ("gérer" le cas $x=0$ à part
et "forcer" la subdivision à prendre la valeur $0$; découpage de la valeur finale
"pressentie" en bouts et recherche d'une somme télescopique). Ou, essayer
d'exploiter la preuve du FTC, qui nécessite d'être détaillée, pour "exhiber"
une gauge qui marche (note: au passage, en supposant $f$ deux fois diff on
peut en construire une explicitement, c'est un exercice intéressant en soi).
Tout est bon ici !

Variante/extension: autre valeur que $0$ en $0$, montrer que cela n'a aucun
impact.

Une stratégie intéressant consisterait à expliciter/construire une gauge
"qui fasse le job" pour $1/\sqrt{x}$ en évitant l'origine en s'inspirant 
de la preuve du FTC (qui "lisse" l'erreur uniformément), PUIS à bootstraper
ça pour la singularité. C'est sans doute une bonne idée, il y a beaucoup
de techniques concentrées sur un seul exercice sinon. Et le coup de 
la méthode de sélection du pas associée au FTC montre une stratégie
qui constraste avec celle de Riemann classique, c'est intéressant à contraster.

#### Préambule

La difficulté de cet exemple est liée à la "singularité" de $f$ en $x=0$,
où la fonction est à la fois discontinue et localement non-bornée. 
Si au lieu de l'intervalle $[0,1]$, on considére l'intervalle
$[a, b]$ où $0 < a \leq b \leq 1$, comme la fonction $f$ restreinte à $[a, b]$
est continue, elle y admet une primitive, par exemple la fonction 
$x \in [a, b] \mapsto 2 \sqrt{x}$.
Elle y est intégrable au sens de Newton 
-- et donc au sens de Henstock-Kurzweil -- 
et
$$
\int_a^b f(x) \, dx = \int_a^b (2\sqrt{x})' \, dx
=
\left[ 2 \sqrt{x} \right]_a^b = 2 (\sqrt{b} - \sqrt{a}).
$$
Si $f$ est bien HK-intégrable sur $[0,1]$, ce que nous allons nous efforcer de
démontrer, l'expression ci-dessus suggère que son intégrale pourrait être
  $$
  \int_0^1 f(x) \, dx \stackrel{?}{=} 2(\sqrt{1} - \sqrt{0}) = 2.
  $$
On va confirmer cette intuition dans la suite.

### La singularité

Soit $\varepsilon > 0$. On cherche à construire une gauge $\gamma$ sur $[0,1]$
telle que toute subdivision pointée $\mathcal{D}$ subordonnée à $\gamma$,
vérifie
$$
\left| S(f, \mathcal{D}) - 2 \right| \leq \varepsilon.
$$ 
On cherche dans un premier temps à expliciter la contribution du voisinage 
de l'origine à la somme de Riemann.
Si $\mathcal{D}$ est composée des paires $([x_i, x_{i+1}], t_i)$ où
$0 \leq x_0 \leq \cdots \leq x_m \leq 1$, et que $x_p$ est le premier
des $x_i$ qui diffère de $0$, on a 
$$
\begin{split}
S(f, \mathcal{D}) &= f(t_0) (x_1 - x_0) + \cdots + f(t_{p-1}) (x_{p} - x_{p-1}) 
+ \sum_{i = p}^m f(t_i) (x_{i+1} - x_i) \\
&= f(t_{p-1}) x_{p} 
+ \sum_{i = p}^m f(t_i) (x_{i+1} - x_i)
\end{split}
$$
soit $S(f, \mathcal{D}) = f(t_{p-1}) x_p + S(f, \mathcal{D}')$
où $\mathcal{D}' = \{(J, t) \in \mathcal{D} \; | \; J \subset [x_p, 1]\}.$

$$
\begin{split}
\left| S(f, \mathcal{D}) - 2 \right| &=
\left| f(t_{p-1}) x-p - 2(\sqrt{x_p} - \sqrt{0}) - (S(f, \mathcal{D}') - 2 (\sqrt{1} - \sqrt{x_p}) )\right|
\end{split}
$$ 

Exercices
================================================================================

Intégrale de Riemann
--------------------------------------------------------------------------------

Montrer que l'intégrale de Riemman est absolue, dans le sens ou si 
une fonction $f$ est intégrable, sa valeur absolue $|f|$ l'est également.

Caractérisation des dérivées
--------------------------------------------------------------------------------

Identifier par les gauges si une fonction est une dérivée (cf papier).
