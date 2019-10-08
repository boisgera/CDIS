% Calcul Intégral I

<!-- LaTeX Macros -->
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}

Somme et intégrale de Riemann
================================================================================

### Intervalle {.definition}
On appelle *intervalle* d'un ensemble ordonné $E$ tout sous-ensemble $I$ de $E$ 
tel que si $x$ et $y$ appartiennent à $I$ et vérifient $x \leq y$
et si $z$ est un point intermédiaire (tel que $x \leq z \leq y$),
alors $z$ appartient également à $I$.

### Intervalles de $\R$ {.remark .post}
Les intervalles de $\R$ peuvent être bornés ou non-bornés,
ouverts, fermés, ouverts et fermés ou ni l'un ni l'autre.
Les intervalles de la forme $\left]-\infty, +\infty\right[$ 
(c'est-à-dire $\R$),
$\left]-\infty, b\right[$, $\left]a,+\infty\right[$ 
et $\left]a,b\right[$ 
-- où $a$ et $b$ désignent des nombres réels -- 
sont ouverts.
Les intervalles de la forme $\left]-\infty, +\infty\right[$,
$\left]-\infty, b\right]$, $\left[a,+\infty\right[$ 
et $\left[a,b \right]$ sont fermés.
Les intervalles compacts (à la fois fermés et bornés) sont de la forme $[a, b]$.

### Longueur d'un intervalle {.definition}
La *longueur* $\ell(I)$ d'un intervalle $I$ 
de $\R$ est le nombre réel étendu positif (appartenant à $[0, +\infty]$)
défini pour tout intervalle borné
$I$ de la forme
$\left[a, b\right]$, $\left]a, b\right[$, $\left[a, b\right[$ ou 
$\left]a, b\right]$ avec $a\leq b$ par
$$
\ell(I) = b - a
$$
et si $I$ est non-borné par
$$
\ell(I) = +\infty.
$$


### Subdivision pointée {.definition}
Une *subdivision* de l'intervalle fermé $[a,b]$
est une collection finie
$$
\{I_i \; | \; \; 0 \leq i \leq n-1 \}
$$
constituée d'intervalles fermés inclus dans $I$, *sans chevauchement*
-- si $i$ et $j$ diffèrent, l'intersection de $I_i$ et $I_j$ contient au 
plus un point -- 
et *recouvrant $I$* 
-- l'union de tous les intervalles $I_i$ inclut $I$. 
Une *subdivision pointée* $\mathcal{D}$ de l'intervalle fermé $I = [a, b]$ 
est une collection finie 
$$
\mathcal{D} = \{(t_i, I_i) \; | \; \; 0 \leq i \leq n-1\}
$$
où les $I_i$ forment une subdivision de $I$ et 
$t_i \in I_i$ pour tout $i \in \{0, \dots, n-1\}.$

### Somme de Riemann {.definition}
La somme de Riemann associée à la fonction $f:[a, b] \to \R$ 
et à la subdivision pointée $\mathcal{D}$ de $[a, b]$ est la grandeur
$$
S(f, \mathcal{D}) = \sum_{(t, I) \in \mathcal{D}} f(t) \ell(I).
$$

### Intégrale de Riemann {.definition}
Une fonction $f:[a, b] \to \R$ est dite *intégrable 
au sens de Riemann* s'il existe un réel $A$ tel
que pour tout $\varepsilon > 0$ il existe un réel $\delta>0$ tel 
que pour toute subdivision pointée $\mathcal{D}$ de $[a, b]$ 
vérifiant pour $(t, J) \in \mathcal{D}$, 
$\ell(J) < \delta$, on ait
$|S(f, \mathcal{D}) - A| \leq \varepsilon$.
Le réel $A$ quand il existe est unique ; 
il est appelé *intégrale de $f$ sur $[a, b]$* et noté
$$
\int_a^b f(t) \, dt
\, \mbox{ ou } \,
\int_{[a, b]} f(t) \, dt
$$

### Quadrature {.example}

Cette définition de l'intégrale permet de garantir l'exactitude asymptotique de 
méthodes de quadrature 
-- c'est-à-dire d'algorithmes de calcul numérique d'intégrales -- 
comme la méthode des rectangles. 
En effet, si $f:[a, b] \to \R$ est une fonction intégrable au sens de 
Riemann, et $\mathcal{D}_m$ une subdivision pointée de $[a, b]$ de la forme
$$
\mathcal{D}_m=
\left\{
\left(a + i \frac{b-a}{m}, \left[a + i \frac{b-a}{m}, a + (i+1) \frac{b-a}{m} \right]\right)
\, \left| \vphantom{\frac{a}{b}}\right.
i \in \{0,\dots, m-1\}
\right\},
$$
la somme de Riemann associée vérifie
$$
\begin{split}
S(f, \mathcal{D}_m) 
&= \sum_{i=0}^{m-1} f\left(a + i\frac{b-a}{m}\right) \ell 
\left(\left[a + i \frac{b-a}{m}, a + (i+1) \frac{b-a}{m} \right]\right)\\
&= \sum_{i=0}^{m-1} f\left(a + i\frac{b-a}{m}\right) \frac{b-a}{m}  \\
&= \frac{b-a}{m} \sum_{i=0}^{m-1} f\left(a + i\frac{b-a}{m}\right)
\end{split}
$$
De plus, quel que soit $\delta > 0$, pour $m$ suffisamment grand, on a
$$
\ell\left(\left[a + i \frac{b-a}{m}, a + (i+1) \frac{b-a}{m} \right]\right)
=
\frac{b-a}{m}
<
\delta.
$$
Par conséquent,
$$
\frac{b-a}{m} \sum_{i=0}^{m-1} f\left(a + i\frac{b-a}{m}\right)
\to \int_a^b f(t) \, dt
\, \mbox{ quand } \, m \to +\infty.
$$
La définition de l'intégrale de Riemann ne se limite pas à une famille 
particulière de subdivisions -- comme ici à des subdivisions régulières de 
$[a, b]$ où tous les intervalles sont de même longueur -- et n'impose 
pas une position fixe au point $t_i$ dans l'intervalle $J_i$ -- 
comme ici à gauche de l'intervalle -- ce qui garantit une forme de robustesse
à la définition de l'intégrale ; d'autres méthodes de quadratures pourront
être utilisées avec le même résultat asymptotique.

### {.remark .ante}

L'intégrale de Riemann possède des limitations qui en font un outil mathématique
difficile à exploiter. 
En particulier la classe des fonctions qui peuvent être intégrées est trop 
restrictive pour certaines applications car les fonctions "trop grandes" ou 
"trop irrégulières" ne sont pas intégrables. 
Les deux théorèmes qui suivent précisent cette situation.

### Seules les fonctions bornées sont intégrables {.lemma}
Si $f:[a, b] \to \R$ est intégrable au sens de Riemann, alors $f$ est bornée. 

### Démonstration {.proof}

Soit $\delta > 0$ tel que pour toute subdivision pointée $\mathcal{D}$ de 
$[a, b]$ vérifiant $\ell(J) < \delta$ pour tout $(t, J) \in \mathcal{D}$, 
on ait
$$\left|S(f, \mathcal{D}) - \int_a^b f(t) \, dt\right| \leq 1.$$
Soit $\mathcal{D} = \{(t_i, [a_i, b_i])\}_{i=0}^{m-1}$ une telle subdivision ;
il est toujours possible de supposer en outre que $\mathcal{D}$ ne contient 
aucun intervalle de longueur nulle (enlever de tels intervalles à $\mathcal{D}$
génère une nouvelle subdivision dont la somme de Riemann est identique).

Soit $J_i = [a_i, b_i]$ un intervalle de $\mathcal{D}$ ; 
si l'on définit $\mathcal{D}'$ à partir de $\mathcal{D}$ en remplaçant 
$t_i$ par un $t$ de $J_i$ quelconque, on obtient
$$
\begin{split}
|f(t) \ell(J_i) - f(t_i) \ell(J_i)| &=
|S(f, \mathcal{D}') - S(f, \mathcal{D})| \\
& \leq
\left|S(f, \mathcal{D}') - \int_a^b f(t) \, dt\right|
+
\left|S(f, \mathcal{D}) - \int_a^b f(t) \, dt\right| \\
& \leq 2
\end{split}
$$
et par conséquent,
$$
|f(t)| \leq |f(t_i)| + \frac{2}{\ell(J_i)}.
$$
Les intervalles $J_i$ recouvrant $[a, b]$, on a pour tout $t\in [a, b]$
$$
|f(t)| \leq \max_i \left\{|f(t_i)| + \frac{2}{\ell(J_i)} 
\, \left| \vphantom{\frac{a}{b}} \right. \, i \in \{0, \dots, m-1\}\right\};
$$
la fonction $f$ est donc bornée.

### Ensemble négligeable  {.definition}
Un ensemble $A$ de $\R$ est *négligeable* si pour tout
$\varepsilon > 0$, il existe un recouvrement de $A$ par une famille
dénombrable d'intervalles $I_i$ de $\R$ tels que
$$
\sum_i \ell(I_i) \leq  \varepsilon.
$$

### {.remark .post}
Nous voyons que le procédé qui définit la notion d'ensemble négligeable
consiste à surestimer la taille de l'ensemble en lui substituant une
collection d'intervalles dont l'union est au moins aussi grande,
puis à surestimer la longueur de l'ensemble résultant en calculant la
somme des longueurs des intervalles, sans tenir compte des éventuels
chevauchements. 
Si à l'issue de cette double surestimation la longueur évaluée est encore 
aussi petite que l'on veut, on peut légitimement considérer que l'ensemble 
de départ est de longueur nulle[^me] 
et que c'est donc ce que signifie "négligeable". 
Nous verrons ultérieurement que cette intuition est valide.

[^me]: plus exactement de mesure *extérieure* (de longueur) nulle.

### Presque partout {.definition}
Une propriété dépendant d'un réel $x$ est vraie *presque partout*
si l'ensemble des points $x$ où elle est fausse est un ensemble
négligeable.

### Les ensembles dénombrables sont négligeables {.example #edn}
Par exemple, les ensembles finis sont négligeables, $\Q$ est
négligeable, etc. En effet, si $A = \{x_n \, | \, n \in \N\}$,
alors pour tout $\varepsilon > 0$, la collection d'intervalle ouverts
$$
\left\{
\left]
x_i - \frac{\varepsilon}{2^{i+2}}, x_i + \frac{\varepsilon}{2^{i+2}}
\right[
\, \left| \vphantom{\frac{a}{b}} \, \right.
i \in \N
\right\}
$$
recouvre $A$ et par ailleurs
$$
\sum_{i=0}^{+\infty} \ell\left(\left]
x_i - \frac{\varepsilon}{2^{i+2}}, x_i + \frac{\varepsilon}{2^{i+2}}
\right[\right)
=
\sum_{i=0}^{+\infty} \frac{\varepsilon}{2^{i+1}}
=
\varepsilon.
$$

### Critère de Lebesgue pour l'intégrabilité au sens de Riemann
La fonction $f:[a, b] \to \R$ est intégrable au sens de Riemann 
si et seulement si $f$ est bornée et continue presque partout.

### {.post #Rcpp}
En particulier, si $f$ est continue par morceaux, elle est intégrable
au sens de Riemann.

### Démonstration {.proof}
[Le lemme ci-dessus][Seules les fonctions bornées sont intégrables] montre
que le caractère borné est nécessaire pour l'intégrabilité au sens de
Riemann. Pour le reste de la preuve, se reporter à [@Bur07, p. 58].


Intégrale de Riemann généralisée
================================================================================

### Jauge {.definition}
Une *jauge* $\gamma$ sur un intervalle $[a, b]$ est une fonction 
qui associe à tout $t \in [a, b]$ un intervalle ouvert $\gamma(t)$ 
contenant $t$. 

### Subdivision pointée subordonnée à une jauge {.definition}
Une subdivision pointée $\mathcal{D}$ de l'intervalle $[a, b]$ 
est *subordonnée à une jauge* $\gamma$ sur $[a, b]$ si pour tout 
$(t, J) \in \mathcal{D}$, $J \subset \gamma(t).$

### Représentation graphique

On peut associer à une jauge $\gamma$ sur $[a, b]$ l'ensemble du plan
$$
\{(x, y) \; | \; y \in [a, b], \, x \in \gamma(y) \}.
$$
Par construction, cet ensemble contient la diagonale 
$D = \{(x,x) \; | \; x \in [a, b]\}.$
La représentation graphique de cet ensemble permet de visualiser si
une subdivision pointée est ou non subordonnée à la jauge considérée.

\newcommand{\lb}{[}
\newcommand{\rb}{]}
\newcommand{\lob}{\left]}
\newcommand{\rob}{\right[}

![Graphe de la jauge $\gamma(t) = \lob t-0.2, t+0.2 \rob ,$
$t \in \lb 0, 1 \rb .$](images/gauge-plot.py){#graphe-gauge}

### Lemme de Cousin {.theorem #cousin}
Pour toute jauge $\gamma$ sur l'intervalle $[a, b]$, 
il existe une subdivision pointée $\mathcal{D}$ 
qui soit subordonnée à $\gamma$.

### Démonstration {.proof}
S'il existe un $t \in I^0 = I = [a, b]$ tel que $I \subset \gamma(t)$, 
la subdivision pointée $\mathcal{D} = \{(t, I)\}$ convient.
Sinon, on peut considérer les intervalles $I_0^1 = [a, (a+b)/2]$ et
$I_1^1 = [(a+b)/2, b]$ et examiner pour chacun de ces intervalles
s'il existe un $t_i \in I_i^1$ tel que $I_i^1 \subset \gamma(t_i)$,
dans ce cas ajouter la paire $(t_i, I_i^1)$ à la famille $\mathcal{D}$
et dans le cas contraire décomposer à nouveau l'intervalle posant 
problème. 
Il s'avère que ce procédé converge en un nombre fini d'étapes ; 
il génère donc une subdivision pointée $\mathcal{D}$ de $I$.

En effet, dans le cas contraire il existerait une infinité 
d'intervalles fermés $J_i$ emboités ($J_{i+1} \subset J_i$) 
tels que $J_0 = I$, $\ell(J_{i+1}) = \ell(J_i)/2$ et 
pour tout $t \in J_i$, $J_i \not \subset \gamma(t)$.
Soit $t_i$ un point de $J_i$ ; la suite des ces points appartient 
à $J_0$ qui est compact et admet donc une suite extraite qui converge.
Comme la suite des $t_k$ appartient à $J_i$ pour tout $k \geq i$,
cette limite $t$ adhère à tous les $J_i$, et donc appartient à tous
les $J_i$ puisqu'ils sont fermés.
La longueur de $J_i$ étant divisée par deux à chaque incrément de $i$,
$\ell(J_i) = \ell(J_0) / 2^i$ ; 
comme $t \in J_i$, 
$J_i \subset [t - \ell(J_0) / 2^i, t + \ell(J_0) / 2^i]$.
Par conséquent, il existe un rang $i$ à partir duquel
$J_i \subset \gamma(t)$, ce qui contredit l'hypothèse de départ.

### {.ante}
La définition de l'intégrale de Henstock-Kurzweil est similaire à l'intégrale
de Riemann classique. 
Comme cette dernière, elle exploite des sommes de Riemann pour fournir une
estimation de l'intégrale et contrôle la finesse des subdivisions employées
pour améliorer la précision de cette estimation ; 
mais contrairement à cette dernière, 
elle permet de contrôler différemment cette finesse 
en fonction de la zone de l'intervalle d'intégration considérée.

### Intégrale de Henstock-Kurzweil {.definition #HK}
Une fonction $f:[a, b] \to \R$ est dite *intégrable 
au sens de Henstock-Kurzweil[^why-HK]* s'il existe un réel $A$ tel
que pour tout $\varepsilon > 0$, 
il existe une jauge $\gamma$ sur $[a, b]$ telle que, 
pour toute subdivision pointée $\mathcal{D}$ de $[a, b]$ subordonnée à $\gamma$, 
on ait
$|S(f, \mathcal{D}) - A| \leq \varepsilon$.
Le réel $A$ quand il existe est unique; il est appelé
*intégrale de $f$ sur $[a, b]$* et noté
$$
\int_a^b f(t) \, dt
\, \mbox{ ou } \,
\int_{[a, b]} f(t) \, dt
$$

![Graphe de la jauge $\gamma(t) = \lob t-0.2, t+0.2 \rob ,$
$t \in \lb 0, 1 \rb$ et de la subdivision pointée
$\{(0.1, [0, 0.2]), \dots, (0.9, [0.8, 1])\}$ ;
les intervalles de la subdivision sont délimités
par des barres verticales et les points associés 
représentés par des croix. La comparaison avec le graphe de la
jauge $\gamma$ montre que cette subdivision pointée 
lui est subordonnée.](images/gauge-plot-subdivision.py)

[^why-HK]: On trouvera également dans la littérature cette intégrale désignée
par le terme d'*intégrale de Riemann généralisée* ou 
d'*intégrale de jauge* (mais ces termes sont génériques ; en particulier 
il existe d'autres intégrales dont la définition repose sur des sommes
de Riemann et des jauges, comme l'intégrale de McShane), 
*intégrale de Kurzweil-Henstock* 
(techniquement Jaroslav Kurzweil a inventé cette 
construction avant Ralph Henstock dans les années 1950, 
mais dans un but bien précis
-- l'étude des équations différentielles généralisées -- probablement sans
réaliser totalement la portée de sa définition) 
ou *intégrale de Denjoy-Perron-Kurzweil-Henstock* (Arnaud Denjoy et Oskar Perron
ont introduit dès les années 1910 des intégrales équivalentes, mais dont les
définitions sont beaucoup plus complexes et en apparence très différentes ; 
en particulier, les sommes de Riemann n'interviennent pas dans 
ces définitions).

### Ordre des bornes de l'intégrale {.notation .remark}
Comme dans le cas de l'intégrale de Riemann,
la première notation peut être étendue sans difficulté au cas où $b < a$ ; 
on définit alors l'intégrale de $a$ à $b$ en se ramenant 
au cas précédent, par
$$
\int_{a}^b f(t) \, dt := - \int_b^a f(t) \, dt.
$$

### Intégrale de Riemann et de Henstock-Kurzweil {.theorem #RHK}
Toute fonction $f:[a,b] \mapsto \R$ intégrable au sens de Riemann
est intégrable au sens de Henstock-Kurzweil et les deux intégrales coïncident.

### Démonstration {.proof}
Soit $f:[a,b] \to \R$ une fonction intégrable au sens de Riemann,
d'intégrale $A$ ;
soit $\varepsilon > 0$ et $\delta>0$ tels que si la subdivision pointée 
$\mathcal{D}$ de $[a, b]$ est telle que pour $(t, I) \in \mathcal{D}$, 
$\ell(J) < \delta$ alors $|S(f,\mathcal{D}) - A| \leq \varepsilon$.

Considérons la jauge $\gamma$ sur $[a, b]$ définie par 
$\gamma(t)= \left]t-\delta/2, t+\delta/2 \right[$.
Si la subdivision pointée $\mathcal{D}$ est subordonnée à $\gamma$,
alors pour tout $(t, J) \in \mathcal{D}$, on a
$J \subset \left]t-\delta/2, t+\delta/2 \right[$ ; 
par conséquent, $\ell(J) < \delta$ et donc
$|S(f,\mathcal{D}) - A| \leq \varepsilon$. 
La fonction $f$ est donc intégrable au sens de Henstock-Kurzweil et 
l'intégrale associée est égale à son intégrale de Riemann.

### {.ante}
Un résultat similaire vaut aussi pour l'intégrale de Newton :

### Intégrale de Newton et de Henstock-Kurzweil {.corollary}
Toute fonction $f:[a,b] \mapsto \R$ intégrable au sens de Newton
est intégrable au sens de Henstock-Kurzweil et les deux intégrales coïncident.

### {.post .ante}
L'énoncé précédent peut être reformulé de la façon suivante : 
l'intégrale de Henstock-Kurzweil satisfait 
[le théorème fondamental du calcul](#TFC) en toute généralité.

### Théorème fondamental du calcul {.theorem #TFC}
Soit $[a, b]$ un intervalle compact de $\R$ ;
si la fonction $f:[a, b] \to \R$ est dérivable, 
sa dérivée $f'$ est intégrable au sens de Henstock-Kurzweil sur $[a, b]$ et 
$$
[f]_a^b := f(b) - f(a) = \int_a^b f'(t) \, dt.
$$



### Démonstration du [théorème fondamental du calcul][Théorème fondamental du calcul] {.proof}
Nous souhaitons établir que $f':[a, b] \to \R$ est intégrable, 
d'intégrale égale à $f(b) - f(a)$.
Pour cela, nous devons montrer que pour tout $\varepsilon > 0$ il existe 
une fonction de jauge $\gamma$ sur $[a, b]$ telle que, 
si une subdivision pointée 
$$
\mathcal{D} = \{(t_0, [x_0, x_1], \dots, (t_{m-1}, [x_{m-1}, x_m]))\}
$$ 
vérifie pour tout $i \in \{0, \dots, m-1\},$ 
$[x_i,x_{i+1}] \subset \gamma(t_i),$ alors 
$$
|S(f', \mathcal{D}) - (f(b) - f(a))| \leq \varepsilon.
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
Si l'on parvient à garantir que pour chacun des termes
de cette somme,
$$
\left| f'(t_i)(x_{i+1} - x_i) - (f(x_{i+1}) - f(x_i)) \right| 
\leq 
\frac{\varepsilon}{b-a} (x_{i+1} - x_i),
$$
ce qui revient à assigner à chaque terme une erreur maximale
proportionnelle à la longueur de l'intervalle $[x_i, x_{i+1}]$,
alors
$$
\begin{split}
|S(f', \mathcal{D}) - (f(b) - f(a))| 
%&\leq \sum_{i=0}^{m-1} \left| f'(t_i)(x_{i+1} - x_i) - (f(x_{i+1}) - f(x_i)) \right| \\
&\leq \sum_{i=0}^{m-1} \frac{\varepsilon}{b-a} (x_{i+1} - x_i) \\
&= \frac{\varepsilon}{b-a} \sum_{i=0}^{m-1} (x_{i+1} - x_i) \\
&= \frac{\varepsilon}{b-a} (b - a) \\
&= \varepsilon. \\
\end{split}
$$
Fixons donc un $\varepsilon > 0$ arbitraire ;
comme pour tout $t \in [a, b],$ 
$$f(t+h) = f(t) + f'(t) h + o(|h|),$$
il existe un $\delta(t) > 0$ tel que si $|h| < \delta (t),$
$$
|f'(t) h - (f(t+h) - f(t))| \leq \frac{\varepsilon}{b-a} |h|
$$
Par conséquent, pour tout sous-intervalle fermé $[c, d]$ de $[a, b]$ tel que
$t \in [c, d]$ et $[c, d] \subset \left]t-\delta(t), t+\delta(t)\right[,$ 
nous avons
$$
|f'(t) (d-t) - (f(d) - f(t))| \leq \frac{\varepsilon}{b-a} |d - t| = \frac{\varepsilon}{b-a} (d-t)
$$
ainsi que
$$
|f'(t) (c-t) - (f(c) - f(t))| \leq \frac{\varepsilon}{b-a} |c - t| = \frac{\varepsilon}{b-a} (t - c).
$$
L'inégalité triangulaire fournit alors
$$
|f'(t)(d - c) - (f(d) - f(c))| \leq \frac{\varepsilon}{b-a} (d - c).
$$
Posons $\gamma(t) = \left]t - \delta(t), t + \delta(t)\right[$ ;
nous avons ainsi bien défini une fonction de jauge sur $[a, b]$.
Si $\mathcal{D}$ est subordonnée à $\gamma$, 
pour tout $i \in \{0, \dots, m-1\},$ 
$$t_i \in [x_i,x_{i+1}] \subset \left]t_i - \delta(t_i), t_i + \delta(t_i)\right[,$$
par conséquent 
$$
|f'(t_i)(x_{i+1} - x_i) - (f(x_{i+1}) - f(x_i))| \leq \frac{\varepsilon}{b-a} (x_{i+1} - x_i).
$$
et donc
$|S(f', \mathcal{D}) - (f(b) - f(a))| \leq \varepsilon$, ce qui prouve le
résultat recherché.

### Intégration de $x \mapsto e^x$ {.example}
La fonction $f: x \mapsto e^x$ est intégrable au sens de Newton sur 
tout intervalle $[a, b]$ puisqu'elle admet $F: x \mapsto e^x$ comme primitive.
Par le théorème fondamental du calcul, 
$f$ est intégrable au sens de Henstock-Kurzweil et l'intégrale associée 
coïncide avec l'intégrale de Newton. On a donc
$$
\int_a^b e^x \,dx 
= 
\left[ e^x \right]_a^b
= e^b - e^a. 
$$

L'intégrabilité au sens de Henstock-Kurzweil signifie que
pour toute précision $\varepsilon > 0$, 
il existe une jauge $\gamma$ sur $[a, b]$
telle que pour toute subdivision pointée $\mathcal{D}$ subordonnée à $\gamma$,
l'écart entre $S(f, \mathcal{D})$ et la valeur de l'intégrale
soit au plus $\varepsilon$.

Construisons une telle jauge en nous inspirant de la preuve du théorème
fondamental du calcul. Dans cette preuve, nous avons montré que si 
$\varepsilon > 0$, et nous pouvions trouver une jauge $\gamma$ telle que 
pour toute subdivision pointée $\mathcal{D}$ subordonnée à $\gamma$ et 
tout $(t, [x, y]) \in \mathcal{D}$ nous avions
$$
|f(t) (y-x) - (F(y) - F(x))| \leq \frac{\varepsilon}{b - a} (y - x),
$$
alors nous avions 
$\left|S(f, \mathcal{D}) - (F(b) - F(a))\right| \leq \varepsilon.$
Nous avons également montré comment sélectionner une jauge $\gamma$ pour
satisfaire cette inégalité en utilisant le fait que $F' = f$.
Nous allons reprendre cette approche ici, mais quantitativement, 
et en exploitant la propriété que la fonction $f$ est continûment
dérivable (et non plus simplement dérivable) et que donc sa dérivée est
bornée sur tout compact. 
Comme
$$
f(t) (y - x) = \int_x^y f(t) \, ds
\; \mbox{ et } \;
F(y) - F(x) = \int_x^y f(s) \, ds,
$$
le membre de gauche de l'inégalité vérifie
$$
|f(t) (y-x) - (F(y) - F(x))|
=
\left| \int_x^y (f(t) - f(s)) \, ds\right|
\leq 
\int_x^y |f(t) - f(s)| \, ds
$$
et par conséquent, comme par [l'inégalité des des accroissements finis](Calcul Différentiel I.pdf#TAF)
$$
|f(t) - f(s)| 
\leq \max_{z \in [x, y]} |f'(z)|  \times |t - s|
\leq \max_{z \in [x, y]} |f'(z)|  \times |t - x|
,
$$
on obtient
$$
\int_x^y |f(t) - f(s)| \, ds \leq \max_{z \in [x, y]} |f'(z)| \times \frac{(y-x)^2}{2}.
$$
Il suffit donc de garantir
$$
\max_{z \in [x, y]} |f'(z)| \times \frac{y - x}{2} \leq \frac{\varepsilon}{b-a}
$$
pour obtenir l'inégalité recherchée.

Si l'on décide de rechercher une jauge $\gamma$ garantissant cette inégalité 
sous la forme $\gamma(t) = \left]t -\delta(t), t+\delta(t)\right[$, comme
$t \in [x, y] \subset \gamma(t)$, nous somme assurés que l'inégalité 
est vraie quand
$$
\max \{ |f'(z)|, \,   z \in [t-\delta(t), t+\delta(t)]  \} \times \delta(t) 
\leq \frac{\varepsilon}{b-a}.
$$

<!--

Dans cette preuve, nous avons montré que la précision
$\varepsilon$ était atteinte
si nous choisissions 
$\gamma(t) = \left]t-\delta(t), t+\delta(t)\right[$
où $\delta(t) > 0$ est tel que si $0 \leq |h| \leq \delta(t)$, alors
$$
|F(t+h) - F(t) - f(t)h| \leq \frac{\varepsilon}{b-a} |h|.
$$

Explicitons cette contrainte dans le cas de la fonction 
$F: x \mapsto e^x$. 
Cette fonction étant deux fois continûment différentiable
(la fonction $f$ étant continûment différentiable), 
quand $h$ est non nul,
la formule de Taylor avec reste intégral nous fournit
$$
\begin{split}
\frac{|F(t+h) - F(t) - f(t)h|}{|h|}
&= 
\frac{1}{|h|}\left| \int_t^{t+h}  f'(x) (t + h - x) \, dx \right| \\
&\leq 
\max \left\{ |f'(x)| \, | \, x \in [t-|h|, t+|h|]\right\} \times \frac{|h|}{2}.
\end{split}
$$
Le second membre de cette inégalité étant une fonction croissante de $|h|$, 
il nous suffit donc pour assurer l'inégalité souhaitée de choisir 
$\delta(t) > 0$ tel que
$$
\max \left\{ |f'(x)| \, | \, x \in [t-\delta(t), t+\delta(t)]\right\} \times \frac{\delta(t)}{2}
\leq \frac{\varepsilon}{b-a}.
$$

Dans ce cas précis, puisque $f'(x) = e^x$, lorsque $h \geq 0$ nous avons
$$
\max \left\{ |f'(x)| \, | \, x \in [t-\delta(t), t+\delta(t)]\right\}
= e^{t + \delta(t)}.
$$
-->
Ici, comme $f'(z) = e^z$,
l'inégalité à satisfaire prend simplement la forme
$$
e^{t+\delta(t)} \times \delta(t) \leq \frac{\varepsilon}{b-a},
\; \mbox{ soit } \;
\delta(t) e^{\delta(t)}  \leq e^{-t} \frac{\varepsilon}{b-a}.
$$
Or la fonction 
$\delta \in \left]0, +\infty\right[ \to \delta e^\delta \in \left]0, +\infty\right[$ est 
croissante et bijective ; notons $W$ son inverse[^W]. 
Le plus grand $\delta(t)$ satisfaisant 
l'inégalité précédente est donc donné par
$$
\delta(t) = W \left(e^{-t}\frac{\varepsilon}{b-a}\right).
$$
En conclusion : pour tout $[0, 1]$ et tout $\varepsilon > 0$, 
la jauge $\gamma$ définie sur $[a, b]$ par
$$
\gamma(t) = 
\left]
t - W \left( e^{-t}\frac{\varepsilon}{b-a}\right),
t + W \left( e^{-t}\frac{\varepsilon}{b-a}\right)
\right[
$$
est telle que pour toute subdivision pointée $\mathcal{D}$ de $[a, b]$ 
subordonnée à $\gamma$ on ait
$$
\left|
S(x \in [a, b] \mapsto e^x, \mathcal{D}) 
- 
\int_a^b e^x \, dx 
\right| 
\leq \varepsilon.
$$

[^W]: La notation $W$ est classique pour désigner [la fonction de Lambert](https://fr.wikipedia.org/wiki/Fonction_W_de_Lambert).

![Graphe de la jauge $\gamma$ garantissant une précision $\varepsilon = 1/2$
à la somme de Riemann pour évaluer l'intégrale de la fonction $x \in [0, 1] \mapsto e^x$.](images/gauge-plot-exp.py)

### Intégration de $x \mapsto 1/\sqrt{x}$ {.example}
Considérons la fonction $f:[0,1] \to \R$ définie par
$$
f(x) = 
\left|
\begin{array}{rl}
1/\sqrt{x} & \mbox{si } \, x > 0, \\
?          & \mbox{si } \, x = 0.
\end{array}
\right.
$$

On ne précise pas pour le moment la valeur de $f$ en $0$ : 
elle est supposée arbitraire (mais finie). 
On verra que l'intégrale de $f$ sur $[0, 1]$ 
existe dans tous les cas et ne dépend pas de la valeur de $f$ en $0$
(même si la sélection d'une jauge assurant une précision $\varepsilon$
en dépend).

<!--

Variante/extension: autre valeur que $0$ en $0$, montrer que cela n'a aucun
impact.

Une stratégie intéressant consisterait à expliciter/construire une jauge
"qui fasse le job" pour $1/\sqrt{x}$ en évitant l'origine en s'inspirant 
de la preuve du FTC (qui "lisse" l'erreur uniformément), PUIS à bootstraper
ça pour la singularité. C'est sans doute une bonne idée, il y a beaucoup
de techniques concentrées sur un seul exercice sinon. Et le coup de 
la méthode de sélection du pas associée au FTC montre une stratégie
qui constraste avec celle de Riemann classique, c'est intéressant à contraster.

-->

#### Préambule

La difficulté de cet exemple est liée à la "singularité" de $f$ en $x=0$,
où la fonction est à la fois discontinue et localement non-bornée. 
Si au lieu de l'intervalle $[0,1]$, on considère l'intervalle
$[a, 1]$ où $0 < a \leq 1$, comme la fonction $f$ restreinte à $[a, 1]$
est continue, elle y admet une primitive, par exemple la fonction 
$F: x \in [a, 1] \mapsto 2 \sqrt{x}$.
Elle y est intégrable au sens de Newton 
-- et donc au sens de Henstock-Kurzweil -- 
et
$$
\int_a^1 f(x) \, dx = \int_a^1 (2\sqrt{x})' \, dx
=
\left[ 2 \sqrt{x} \right]_a^1 = 2 \sqrt{1} - 2\sqrt{a}.
$$
Si $f$ est bien HK-intégrable sur $[0,1]$, ce que nous allons nous efforcer de
démontrer, l'expression ci-dessus suggère que son intégrale pourrait être
  $$
  \int_0^1 f(x) \, dx \stackrel{?}{=} 2\sqrt{1} - 2\sqrt{0} = 2.
  $$
On va confirmer cette intuition dans la suite.

#### Intégrale sur $[a, 1]$, $a>0$
Une primitive de $F$ de $f$ sur $[a, 1]$ est $x \mapsto 2 \sqrt{x}$.
Nous allons rechercher une jauge $\gamma$ sur $[a, 1]$ telle que
$$
|f(t) (y-x) - (F(y) - F(x))| = 
\left| \frac{y-x}{\sqrt{t}} - 2\sqrt{y} + 2 \sqrt{x}\right|
\leq \frac{\varepsilon}{2} (y-x).
$$
quand $t \in [x, y] \subset \gamma(t)$, ce qui garantira que
$$
|S(f_{|[a, 1]}, \mathcal{D}_a) - (F(1) - F(a))| \leq \frac{\varepsilon}{2} (1 - a) \leq \frac{\varepsilon}{2}
$$
pour tout subdivision pointée $\mathcal{D}_a$ de $[a, 1]$ subordonnée à $\gamma$.

On remarque qu'il suffit de prouver d'une part que 
$$
\left| \frac{y-t}{\sqrt{t}} - 2\sqrt{y} + 2 \sqrt{t}\right|
\leq \frac{\varepsilon}{2} (y-t)
$$
et d'autre part que
$$
\left| \frac{t-x}{\sqrt{t}} - 2\sqrt{t} + 2 \sqrt{x} \right|
\leq \frac{\varepsilon}{2} (t-x)
$$
pour obtenir l'inégalité voulue. 
Intéressons-nous au membre de gauche de la première de ces inégalités ; on a
$$
\begin{split}
\frac{y-t}{\sqrt{t}} - 2\sqrt{y} + 2 \sqrt{t}
&=
\frac{y - t -2 \sqrt{t}\sqrt{y} + 2 t}{\sqrt{t}} \\
&=
\frac{\sqrt{y}^2 + \sqrt{t}^2 -2 \sqrt{t}\sqrt{y}}{\sqrt{t}} \\
&= \frac{(\sqrt{y} - \sqrt{t})^2}{\sqrt{t}}.
\end{split}
$$
Pour garantir que ce terme soit plus petit que 
$$
\frac{\varepsilon}{2} (y - t)
= \frac{\varepsilon}{2} (\sqrt{y} - \sqrt{t})(\sqrt{y} + \sqrt{t}),
$$
il suffit donc de s'assurer que
$$
\frac{(\sqrt{y} - \sqrt{t})}{\sqrt{t}} \leq \frac{\varepsilon}{2} (\sqrt{y} + \sqrt{t}),
$$
soit 
$$
\sqrt{y} \leq \sqrt{t} + \frac{\varepsilon}{2} (\sqrt{ty} + t).
$$
C'est le cas si 
$$
\sqrt{y} \leq \sqrt{t} + \frac{\varepsilon}{2} t
\; \mbox{ soit } \;
y \leq \left(\sqrt{t} +  \frac{\varepsilon}{2} t \right)^2.
$$
Par une méthode en tout point identique, on montre que la seconde inégalité
-- impliquant $x$ et $t$ -- est satisfaite si
$$
\sqrt{t} \leq \sqrt{x} + \frac{\varepsilon}{2} x,
$$
soit puisque $x \leq t$, si
$$
\sqrt{x} \geq \sqrt{t} - \frac{\varepsilon}{2} x \geq \sqrt{t} - \frac{\varepsilon}{2} t, 
$$
ce qui est le cas si
$$
x \geq \left(\sqrt{t} -  \frac{\varepsilon}{2} t \right)^2.
$$
La jauge $\gamma$ définie par
$$
\gamma(t) 
= 
\left]
\left(\sqrt{t} -  \frac{\varepsilon}{2} t \right)^2, \left(\sqrt{t} +  \frac{\varepsilon}{2} t \right)^2  \right[
$$
satisfait donc nos critères.


<!-- DEPRECATED
La stratégie est similaire à celle de l'exemple de la fonction 
$x \mapsto e^x$: on recherche une jauge $\gamma$ sous la forme
$\gamma(t) = \left]t -\delta(t), t+\delta(t)\right[$, avec $\delta(t) > 0$
tel que[^wtc]
$$
\max \{ |f'(z)|, \,   z \in [t-\delta(t), t+\delta(t)]  \} \times \delta(t) 
\leq \frac{\varepsilon}{2},
$$
ce qui permettra d'assurer que si $t \in [x, z] \subset \gamma(t)$,
$$
|f(t) (y-x) - (F(y) - F(x))| \leq \frac{\varepsilon}{2} (y-x).
$$

[^wtc]: La division de $\varepsilon$ par deux dans l'inégalité correspond
à allouer 50% du "budget d'erreur" à notre disposition pour le calcul de
l'intégrale sur $[a, 1]$ par les sommes de Riemann. Les 50% restant
nous servirons ultérieurement à gérer l'erreur faite en $t=0$.

Toutefois une précaution supplémentaire doit être prise ici: 
pour avoir l'existence de $f'$ et la majoration associée, 
nous devons éviter la singularité en $0$: 
on s'assurera donc que $\delta(t) < t$, ce qui garantit que
$[t - \delta(t), t + \delta(t)] \subset \left]0, +\infty \right[$.

On a alors $f'(z) = -(1/2) z^{-3/2}$, qui est une fonction décroissante
de $z$; on cherche donc $\delta(t) > 0$ garantissant
$$
\frac{1}{2} (t- \delta(t))^{-3/2} \times  \delta(t) \leq \frac{\varepsilon}{2}.
$$
Cette inégalité prend la forme équivalente
$$
\varepsilon^2 (t - \delta(t))^3 - \delta(t)^2 \geq 0
$$
Le membre de gauche est polynomial en $\delta(t)$; 
le polynôme $P_{t,\varepsilon}(\delta) = \varepsilon^2 (t - \delta)^3 - \delta^2$
étant strictement positif pour $\delta = 0$ et strictement négatif
pour $\delta = t$, on peut prendre pour $\delta(t)$ la plus grande
racine réelle de $P_{t,\varepsilon}$ sur $[0, t]$. 

-->

On remarquera que cette jauge $\gamma$ que nous avons construit
-- et qui est en fait définie sur $\left]0, 1\right]$ --
ne dépend pas de la valeur de $a$ dans $\left]0, 1\right]$.
De plus, quand $\varepsilon$ est suffisamment petit -- 
par exemple $\varepsilon/2 < 1$ -- on constate
que pour tout $t \in \left]0, 1\right]$,
comme $\sqrt{t} -  ({\varepsilon}/{2}) t > 0$, on a
$0 \not \in \gamma(t)$.

### Intégrale sur $[0,1]$

Considérons désormais une jauge sur $[0, 1]$ qui étende la jauge définie
sur $\left]0,1\right]$ à la section précédente.

Comme $\gamma(t) \subset \left]0, +\infty \right[$ si $t>0$,
si $\mathcal{D} = \{(t_i, [x_i, x_{i+1}]), i \in \{0,\dots, m-1\}\}$ est 
une subdivision pointée de $[0, 1]$ subordonnée à $\gamma$, 
si $t_i>0$, $0 \not \in [x_i, x_{i+1}]$. 
Comme les ensembles $[x_i, x_{i+1}]$ doivent recouvrir $[0, 1]$, 
il est nécessaire que le point $t_0$ associé à l'intervalle $[x_0, x_1]$
soit $0$. Le reste de la subdivision est alors subordonnée à
$\gamma$ sur $[x_1,1]$ avec $x_1 > 0$
$$
S(f,\mathcal{D})
=
f(0) (x_1 - x_0) + \sum_{i = 1}^{m-1} f(t_i) (x_{i+1} - x_i)
$$
et d'après la section précédente,
$$
\left| 
\sum_{i = 1}^{m-1} f(t_i) (x_{i+1} - x_i)
- (2\sqrt{1} - 2\sqrt{x_1}))
\right|
\leq \frac{\varepsilon}{2}.
$$
Si l'on choisit $\gamma(0) = \left]-\delta, \delta\right[$ tel que si $[x_0, x_1] \subset \gamma(0)$,
$$
\left|f(0)(x_1 - 0) - (2\sqrt{x_1} - 2\sqrt{x_0})\right| 
\leq 
\frac{\varepsilon}{2},
$$
ce qui est le cas si $|f(0) x_1| + 2\sqrt{x_1} \leq {\varepsilon}/{2},$
alors on a garanti que $|S(f,\mathcal{D}) - 2| \leq \varepsilon$, ce 
qui est le résultat cherché.
Comme sur $[0, 1]$, $x_1 \leq \sqrt{x_1}$, il suffit de s'assurer que
$|f(0)| x_1 + 2 x_1 \leq {\varepsilon}/{2}$, ce qui
est le cas si
$$
\delta = \frac{\varepsilon}{2(|f(0)| + 2)}.
$$
Au final, la jauge $\gamma$ sur $[0,1]$ définie par
$$
\gamma(t) =
\left|
\begin{array}{cl}
\displaystyle \left]- \frac{\varepsilon}{2(|f(0)| + 2)}, \frac{\varepsilon}{2(|f(0)| + 2)} \right[ & \mbox{si } t=0 \\
\displaystyle \left]
\left(\sqrt{t} -  \frac{\varepsilon}{2} t \right)^2, \left(\sqrt{t} +  \frac{\varepsilon}{2} t \right)^2  \right[
& \mbox{si } t \in \left]0,1\right]
\end{array}
\right.
$$
garantit un écart $|S(f, \mathcal{D}) - 2|$ inférieur à $\varepsilon$
pour toute subdivision pointée $\mathcal{D}$ de $[0,1]$ subordonnée à $\gamma$.

![Graphe de la jauge $\gamma$ pour $f(0)=0$ et $\varepsilon=0.5$](images/gauge-plot-sqrt.py)



<!--
#### TODO -- Le voisinage de $0$

Soit $\varepsilon > 0$. On cherche à construire une jauge $\gamma$ sur $[0,1]$
telle que toute subdivision pointée $\mathcal{D}$ subordonnée à $\gamma$,
vérifie
$$
\left| S(f, \mathcal{D}) - 2 \right| \leq \varepsilon.
$$ 
On cherche dans un premier temps à expliciter la contribution du voisinage 
de l'origine à la somme de Riemann.
Si $\mathcal{D}$ est composée des paires $([x_i, x_{i+1}], t_i)$ où
$0 \leq x_0 \leq \dots \leq x_m \leq 1$, et que $x_p$ est le premier
des $x_i$ qui diffère de $0$, on a 
$$
\begin{split}
S(f, \mathcal{D}) &= f(t_0) (x_1 - x_0) + \dots + f(t_{p-1}) (x_{p} - x_{p-1}) 
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

-->

Propriétés élementaires de l'intégrale
================================================================================

### Linéarité {.theorem}
Si $f: [a, b] \to \mathbb{R}$ et $g: [a, b] \to \mathbb{R}$ sont intégrables
et $\lambda \in \mathbb{R}$, alors $f+g$ et $\lambda f$ sont intégrables. 
De plus,
$$
\int_{a}^b f(t) + g(t) \, dt 
= 
\int_{a}^b f(t) \, dt +
\int_{a}^b g(t) \, dt
\;
\mbox{ et }
\;
\int_{a}^b \lambda f(t) \, dt
=
\lambda \int_{a}^b f(t) \, dt.
$$

### Démonstration {.proof}
La linéarité de l'intégrale résulte de la linéarité (additivité et homogénéité)
de la somme de Riemann $S(f, \mathcal{D})$ par rapport à $f$.

En effet, si $\varepsilon > 0$, on peut trouver des jauges $\gamma_f$ et $\gamma_g$
sur $[a, b]$ telles que pour toute subdivision pointée $\mathcal{D}$
subordonnée à $\gamma_f$ et $\gamma_g$, on ait
$$
\left|S(f, \mathcal{D}) - \int_a^b f(t) \, dt \right| \leq \frac{\varepsilon}{2}
\; \mbox{ et } \;
\left|S(g, \mathcal{D}) - \int_a^b f(t) \, dt \right| \leq \frac{\varepsilon}{2}.
$$
Comme $S(f+g, \mathcal{D}) =  S(f, \mathcal{D}) + S(g, \mathcal{D})$, 
toute subdivision pointée $\mathcal{D}$ subordonnée à la jauge $\gamma$
définie par $\gamma(t) = \gamma_f(t) \cap \gamma_g(t)$ vérifie
$$
\left|S(f+g, \mathcal{D}) - \int_a^b f(t)+g(t) \, dt \right| \leq \varepsilon.
$$
La fonction $f+g$ est donc intégrable, et son intégrale sur $[a, b]$ est 
la somme des intégrales de $f$ et de $g$ sur $[a, b]$.

De façon similaire, $S(\lambda f, \mathcal{D}) = \lambda S(f, \mathcal{D})$.
Dans le cas où $\lambda = 0$, il est clair que $\lambda f$ est intégrable, 
d'intégrale nulle ;
dans le cas contraire, on peut trouver une jauge $\gamma$ sur $[a, b]$ telle
que pour toute subdivision pointée $\mathcal{D}$ subordonnée à $\gamma$, 
on ait :
$$
\left|S(f, \mathcal{D}) - \int_a^b f(t) \, dt \right| 
\leq 
\frac{\varepsilon}{|\lambda|}.
$$
On a alors
$$
\left|S(\lambda f, \mathcal{D}) - \lambda \int_a^b f(t) \, dt \right| 
=
|\lambda| 
\left|S(f, \mathcal{D}) - \int_a^b f(t) \, dt \right| 
\leq 
\varepsilon.
$$
La fonction $\lambda f$ est donc intégrable sur $[a, b]$ et son intégrale
est le produit de $\lambda$ et de l'intégrale de $f$ sur $[a, b]$.

### Positivité {.proposition}
Si $f: [a, b] \to \mathbb{R}$ est intégrable et positive alors
$$
\int_a^b f(t) \, dt \geq 0.
$$

### Démonstration {.proof}
Soit $\varepsilon > 0$ et $\gamma$ une jauge telle que toute
subdivision pointée $\mathcal{D}$ de $[a, b]$ subordonnée à $\gamma$
vérifie
$$
\left|S(f, \mathcal{D}) - \int_a^b f(t) \, dt\right| \leq \varepsilon.
$$
Quelle que soit la subdivision pointée $\mathcal{D}$ de $[a, b]$,
la somme de Riemann associée 
$$
S(f, \mathcal{D})
= \sum_{(t,J) \in \mathcal{D}} f(t) \ell(J)
$$ 
est positive, ce qui entraîne par l'inégalité triangulaire
$$
\int_a^b f(t) \, dt  \geq S(f, \mathcal{D}) - \varepsilon \geq -\varepsilon.
$$
Le nombre strictement positif $\varepsilon$ pouvant être choisi arbitrairement
petit, on en déduit que l'intégrale est positive.

### Intégration par parties {.theorem}
Soit $[a, b]$ un intervalle compact de $\R$ ;
si les fonctions $f:[a, b] \to \R$ et $g: [a, b] \to \R$ sont dérivables,
la fonction $f'g$ est intégrable si et seulement si la fonction $fg'$
est intégrable. Si c'est le cas, on a
$$
\int_a^b f'(t)g(t) \, dt = [f g]_a^b - \int_a^b f(t) g'(t)\, dt.
$$

### Démonstration {.proof}
La fonction $f'g + f g'$ est la dérivée du produit $fg$, 
elle est donc intégrable. Par conséquent, si l'une des fonctions 
$f'g$ ou $f g'$ est intégrable, l'autre est la différence de deux fonctions
intégrables et elle est donc intégrable.
Dans ce cas, [le théorème fondamental du calcul](#TFC) appliqué à $(fg)'$ 
fournit
$$
\int_a^b (fg)'(t) \, dt
=
\int_a^b f'(t)g(t) \, dt + \int_a^b f(t)g'(t) \, dt
= [fg]_a^b,
$$
ce qui est le résultat recherché.

<!--
### TODO
Mentionner résultat plus général, avec juste $f$ intégrable (sous hyp plus
restrictives pour $g$ ?). Trouver ref ? Ou attendre chapitre multi-variable
et y faire référence ?
-->

### Changement de variables {.theorem}
Soit $[a, b]$ et $[c, d]$ deux intervalles compacts de $\R$ ;
si la fonction $f:[c, d] \to \R$ admet une primitive et
que la fonction $g:[a, b] \to [c, d]$ est dérivable, 
alors la fonction $(f\circ g) g'$ est intégrable sur $[a, b]$ et
$$
\int_a^b f(g(t)) g'(t)\, dt = \int_{g(a)}^{g(b)} f(x) \, dx.
$$

### Démonstration {.proof}
Soit $h$ une primitive de $f$. La fonction $t \in [a, b] \mapsto h(g(t))$
a pour dérivée $h'(g(t))g'(t) = f(g(t)) g'(t)$. 
Par [le théorème fondamental du calcul](#TFC) on a donc d'une part
$$
\int_a^b f(g(t)) g'(t) \, dt
=
\left[t \mapsto h(g(t)) \right]_a^b = h(g(b)) -  h(g(a))
$$
et d'autre part
$$
\int_{g(a)}^{g(b)} f(x) \, dx = [h]_{g(a)}^{g(b)} = h(g(b)) -  h(g(a)) \, ;
$$
les deux intégrales sont donc égales.


### Additivité {.proposition #addivité}
Si la fonction $f$ est définie et intégrable sur les intervalles
$[a, b]$ et $[b, c]$, alors elle est intégrable sur l'intervalle $[a, c]$
et
$$
\int_a^b f(t) \, dt + \int_b^c f(t) \, dt = \int_a^c f(t) \, dt.
$$

### Démonstration {.proof}
Soit $\varepsilon > 0$. Si la fonction $f$ est intégrable sur $[a, b]$ et
$[b, c]$, alors il existe deux jauges $\gamma_1:[a, b] \to \R$ et
$\gamma_2:[b, c] \to \R$ telles que pour toutes les subdivisions
pointées $\mathcal{D}_1$ et $\mathcal{D}_2$ de $[a, b]$ et $[b, c]$ 
respectivement subordonnées à $\gamma_1$ et $\gamma_2$,
$$
\left| S(f, \mathcal{D}_1) - \int_a^b f(t) \, dt\right| \leq \varepsilon/2
\, \mbox{ et } \, 
\left| S(f, \mathcal{D}_2) - \int_b^c f(t) \, dt\right| \leq \varepsilon/2.
$$
Définissons la fonction $\gamma: [a, b] \to \mathcal{P}(\R)$ par:
$$
\gamma(x) = 
\left| 
\begin{array}{rl}
\gamma_1(x) \cap \left]-\infty, b \right[ & \mbox{ si } \, a < x < b, \\
\gamma_1(x) \cap \gamma_2(x) & \mbox{ si } \, x = b, \\
\gamma_2(x) \cap \left]b, +\infty\right[ & \mbox{ si } \, b < x < c. \\
\end{array}
\right.
$$
Par construction, cette fonction est une jauge sur $[a, c]$ 
(pour tout $x \in [a, c]$, $\gamma(x)$ est un intervalle 
ouvert non vide de $\R$ contenant $x$). 
Supposons que $\mathcal{D} =\{(t_i, I_i)\}_i$ soit une subdivision pointée de 
$[a, c]$ subordonnée à $\gamma$. 
Admettons temporairement que chaque intervalle $I_i$ appartienne
à $[a, b]$ ou bien dans le cas contraire à $[b, c]$. Les
deux subdivisions pointées $\mathcal{D}_1$ et $\mathcal{D}_2$ sont telles
que 
$$
S(f, \mathcal{D}) = S(f, \mathcal{D}_1) + S(f, \mathcal{D}_2).
$$
Elles sont également subordonnées à $\gamma_1$ et $\gamma_2$ respectivement ;
par conséquent
$$
\left|
S(f, \mathcal{D}) 
- 
\int_a^bf(t) \, dt + \int_b^c f(t) \, dt 
\right|
\leq 
\varepsilon. 
$$

Si notre hypothèse temporaire n'est pas vérifié, c'est qu'il
existe un (unique) intervalle $I_i$ à cheval sur $[a, b]$ et $[b, c]$, 
c'est-à-dire d'intersection non vide avec $\left[a, b\right[$ et avec 
$\left]b, c\right]$. 
La jauge $\gamma$ a été choisie de telle sorte que 
si $x \neq b$, alors $b \not \in \gamma(x)$;
par conséquent, si cet intervalle $I_i=[d_i, e_i]$ existe, 
alors $t_i = b$ et on peut remplacer le terme $(t_i, I_i)$ dans la subdivision
pointée $\mathcal{D}$ par $(b, [d_i, b])$ et $(b, [b, e_i])$ sans que
la somme de Riemann associée change 
(le terme $f(b) \ell([d_i, e_i])$ étant égal à 
$f(b) \ell([d_i, b]) + f(b) \ell([b, e_i])$).
La nouvelle subdivision $\mathcal{D}'$ ainsi construite vérifie quant à elle
l'hypothèse de non-chevauchement de $b$. Par conséquent l'inégalité
ci-dessus est satisfaite dans le cas général.

### {.ante}
Dans le cas où l'on souhaite établir l'intégrabilité sans savoir quelle
est la valeur de l'intégrale, le test suivant d'intégrabilité est utile :

### Critère d'intégrabilité de Cauchy {#CIC .theorem}
Une fonction $f: [a, b] \to \R$ est intégrable si et seulement si 
pour tout $\varepsilon > 0$ il existe une jauge $\gamma$ sur $[a, b]$ telle que 
pour tout couple de subdivisions pointées $\mathcal{D}$ et $\mathcal{D}'$
subordonnées à $\gamma$, on ait
$$
|S(f, \mathcal{D}) - S(f, \mathcal{D}')| \leq \varepsilon.
$$

### Démonstration {.proof}
Si la fonction $f$ est intégrable, pour tout $\varepsilon > 0$, 
il existe une jauge $\gamma$ sur $[a, b]$ telle que pour tout couple de 
subdivisions pointées $\mathcal{D}$ et $\mathcal{D}'$ subordonnées à $\gamma$,
on ait
$$
\left|S(f, \mathcal{D}) - \int_a^b f(t) \, dt \right| \leq \frac{\varepsilon}{2}
\; \mbox{ et } \;
\left|S(f, \mathcal{D}') - \int_a^b f(t) \, dt \right| \leq \frac{\varepsilon}{2}.
$$
Par l'inégalité triangulaire, on a alors 
$|S(f, \mathcal{D}) - S(f, \mathcal{D}')| \leq \varepsilon.$

Réciproquement, si la fonction $f$ vérifie le critère du théorème,
pour tout $k \in \N$ il existe une jauge $\gamma_{k}$ sur $[a, b]$ 
telle que pour tout couple de subdivisions pointées 
$\mathcal{D}$ et $\mathcal{D}'$ subordonnées à $\gamma_k$, on ait
$$
|S(f, \mathcal{D}) - S(f, \mathcal{D}')| \leq 2^{-k}.
$$
Il est de plus possible de choisir les jauges $\gamma_k$ telles qu'à tout 
ordre $k$ et pour tout $t \in [a, b]$, 
on ait $\gamma_{k+1}(t) \subset \gamma_k(t)$ (si $\gamma_{k+1}$ ne satisfait
pas ce critère, il suffit de lui substituer la jauge définie par en $t$ par
$\gamma_{k+1}(t) \cap \gamma_k(t)$). 
Soit $\mathcal{D}_k$ une suite de subdivisions pointées sur $[a, b]$
subordonnées à $\gamma_k$. Si $m \geq k$ et $n \geq k$, 
$\mathcal{D}_m$ et $\mathcal{D}_n$ sont subordonnées à $\gamma_k$, donc
$$
|S(f, \mathcal{D}_m) - S(f, \mathcal{D}_n)| \leq 2^{-k}.
$$
La suite des $S(f, \mathcal{D}_k)$ est donc de Cauchy ; la droite des réels
étant complète, cette suite à une limite $A$. En passant à la limite sur
$n$ dans l'inégalité $|S(f, \mathcal{D}) - S(f, \mathcal{D}_n)| \leq 2^{-k}$,
valable quand $\mathcal{D}$ est subordonnée à $\gamma_k$, on obtient
$$
|S(f, \mathcal{D}) - A| \leq 2^{-k}.
$$
La fonction $f$ est donc intégrable et d'intégrale $A$.

### {.ante}
[La propriété d'additivité](#additivité) de l'intégrale -- 
qui permet de prouver l'intégrabilité de l'intégrale sur un intervalle
à partir de son intégrabilité sur des intervalles qui la compose --
admet une réciproque :

### Restriction {.theorem #restriction}
Si $f$ est intégrable sur l'intervalle $[a, b]$, 
elle est intégrable sur tout intervalle $[c, d]$ 
inclus dans $[a, b]$.

### Démonstration {.proof}
Nous démontrons en détail le cas où $c = a$ ; le cas où $d=b$ se prouve de
façon similaire et le cas général se déduit facilement de la combinaison 
de ces deux cas particuliers.

Soit $\varepsilon > 0$. Par le [critère d'intégrabilité de Cauchy](#CIC),
il existe une jauge $\gamma$ sur $[a, b]$ telle
que pour tout couple de subdivisions pointées $\mathcal{D}$ et $\mathcal{D}'$
subordonnées à $\gamma$, on ait
$|S(f, \mathcal{D}) - S(f, \mathcal{D}')| \leq \varepsilon.$

Considérons les restrictions $\gamma_1$ et $\gamma_2$ de $\gamma$ à $[a, d]$ et 
$[d, b]$ respectivement. 
Soient $\mathcal{D}_1$ et $\mathcal{D}_1'$ deux subdivisions pointées de 
$[a, d]$ subordonnées à $\gamma_1$ ;
si $\mathcal{D}_2$ est une subdivision de $[d, b]$ subordonnée à $\gamma_2$,
alors $\mathcal{D}_1 \cup \mathcal{D}_2$ et $\mathcal{D}'_1 \cup \mathcal{D}_2$
sont des subdivisions pointées de $[a, b]$ subordonnées à $\gamma$.
Par conséquent,
$$
|S(f, \mathcal{D}_1 \cup \mathcal{D}_2) 
- S(f, \mathcal{D}'_1 \cup \mathcal{D}_2)|
\leq \varepsilon.
$$
Or
$S(f, \mathcal{D}_1 \cup \mathcal{D}_2) = S(f, \mathcal{D}_1) + S(f, \mathcal{D}_2)$
et $S(f, \mathcal{D}_1' \cup \mathcal{D}_2) = S(f, \mathcal{D}_1') + S(f, \mathcal{D}_2)$,
par conséquent
$$
|S(f, \mathcal{D}_1) - S(f, \mathcal{D}_1')|
\leq \varepsilon.
$$
Par le [critère d'intégrabilité de Cauchy](#CIC), la fonction $f$ est donc
intégrable sur l'intervalle $[a, d]$.

### Fonctions égales presque partout {.proposition #fepp}
Une fonction $f:[a, b] \to \R$ égale presque partout à une 
fonction $g:[a, b] \to \R$ intégrable est elle-même intégrable
et 
$$
\int_a^b f(t) \, dt = \int_a^b g(t) \, dt.
$$

### Démonstration {.proof}

Par linéarité de l'intégrale, il suffit d'établir que si 
$f:[a, b] \to \R$ est nulle presque partout (c'est-à-dire égale
presque partout à la fonction $g:[a, b] \to \R$ identiquement
nulle), alors elle est intégrable et d'intégrale nulle.

Supposons dans un premier temps que $f$ soit bornée.
Alors, pour tout $\varepsilon > 0$, il existe un recouvrement de
$$
A = f^{-1}(\R \setminus \{0\}) = \{x \in [a, b] \, | \, f(x) \neq 0\}
$$ 
par une collection dénombrable
d'intervalles $I_i$ telle que $\sum_i \ell(I_i) \leq \varepsilon$.
Il est de plus possible de supposer les $I_i$ ouverts[^why-open].
Définissons la jauge $\gamma$ sur $[a, b]$ par
$$
\gamma(t) = I_i \, \mbox{ si } \, t \in I_i \;
\mbox{et } \, t \not \in I_j \mbox{ quand } \, j \leq i
$$
et par exemple
$\gamma(t) = \left]-\infty,\infty\right[$ si $t \not \in \cup_i I_i$. 
Pour toute subdivision pointée $\mathcal{D} = \{(t_j, J_j)\}_j$ de $[a, b]$ 
subordonnée à $\gamma$, 
$$
\left|S(f, \mathcal{D})\right| 
= \left|\sum_j f(t_j) \ell(J_j)\right|
= \left|\sum_{t_j \in A} f(t_j) \ell(J_j)\right|
\leq \sup_{[a, b]} |f| \times \sum_j \ell(J_j).
$$
Par construction les $J_j$ ne se chevauchent pas et sont
tous inclus dans un des intervalles $I_i$. On a donc
$$
\sum_j \ell(J_j) \leq  \sum_i \ell(I_i) \leq \varepsilon.
$$
Il suffit par conséquent de choisir un $\varepsilon$ suffisamment petit
initialement pour rendre la somme de Riemann associée arbitrairement petite ;
$f$ est donc intégrable d'intégrale nulle.

[^why-open]: On peut trouver un recouvrement de $A$ par des
intervalles $J_i$ non nécessairement ouverts, tels que 
$\sum_i \ell(J_i) \leq \varepsilon/2$, puis remplacer chaque
$J_i$ par un intervalle $I_i$ ouvert de longueur double contenant $J_i$.

Si $f$ est non-bornée, on peut faire une démonstration similaire en
considérant les ensembles
$$
A_k = \{x \in [a, b] \, | \, k < |f(x)| \leq k+1\},
$$
puis en associant à chaque $A_k$ un recouvrement par une collection dénombrable
d'intervalles ouverts $I^k_i$ tels que 
$$
\sum_i \ell(I^k_i) \leq \frac{\varepsilon}{(k+1)2^{k+1}}
$$
ce qui est possible puisque tous les $A_k$ sont négligeables. 
On définit alors la jauge $\gamma$ sur $[a, b]$ par 
$\gamma(t) = I^k_i$ si $t$ appartient à un $I^k_i$ (et on choisit alors
le plus petit $k$, puis le plus petit $i$ telle que cette propriété
soit vérifiée) et par exemple
$\gamma(t) = \left]-\infty,\infty\right[$ si 
$t \not \in \cup_k \cup_i I^k_i$. L'évaluation d'une somme de Riemann
pour une subdivision pointée subordonnée à cette jauge fournit
$$
\left|S(f, \mathcal{D})\right| 
= \left|\sum_j f(t_j) \ell(J_j)\right|
= \left|\sum_k \sum_{t_j \in A_k} f(t_j) \ell(J_j)\right| \leq
\sum_k \sum_{t_j \in A_k} (k+1) \ell(J_j)
$$
et comme
$$
\sum_{t_j \in A_k} \ell(J_j) 
\leq  \sum_i \ell(I^k_i) 
\leq \frac{\varepsilon}{(k+1)2^{k+1}},
$$
on obtient
$$
\left|S(f, \mathcal{D})\right| 
\leq
\sum_k (k+1) \sum_{i} \ell(I^k_i)
\leq 
\sum_k \frac{\varepsilon}{2^{k+1}} 
= \varepsilon.
$$
La fonction $f$ est donc bien intégrable et d'intégrale nulle.


Intégration sur des intervalles non-bornés
================================================================================

### 
La théorie de l'intégration de Henstock-Kurzweil présentée dans les
sections précédentes peut être modifiée de façon assez mineure pour 
permettre l'intégration de fonctions sur des intervalles non-bornés.
Le travail central consiste à redéfinir la somme de Riemann; 
en effet, comme toute subdivision pointée 
d'un intervalle non-borné comporte nécessairement un ou deux éléments 
de la forme $(t, I)$ où $I$ est un intervalle non-borné de $\R$,
la longueur $\ell(I)$ associée est alors infinie.
La somme de Riemann définie jusqu'à présent comporte alors 
un ou deux termes de la forme $f(t) \times \infty$ ; 
elle donc potentiellement infinie, 
ou même indéfinie si les termes $-\infty$ et $+\infty$ apparaissent.

Pour pallier ce problème, nous adoptons la stratégie suivante:

 1. **Intervalles.** 
    Nous considérons désormais l'intégration de fonctions sur des 
    intervalles de la forme $[a, b]$ où $-\infty \leq a \leq b \leq +\infty$,
    autrement dit les intervalles fermés (ou ce qui revient au même,
    compacts) de la droite réelle achevée $[-\infty, +\infty]$.
    Nous définissons la longueur d'un intervalle de $[-\infty, +\infty]$ 
    comme la longueur de son intersection avec $\R$([^cp]).

 2. **Fonctions.**
    Si les fonctions que nous souhaitons intégrer sont définies sur des 
    intervalles fermés mais non bornés dans $\R$, 
    nous leur assignons une valeur arbitraire en $-\infty$ et/ou en $+\infty$, 
    par exemple la valeur $0$, pour les prolonger à un intervalle qui soit
    fermé dans $[-\infty, +\infty]$.

 3. **Somme de Riemann.** Si $\mathcal{D}$ est une subdivision pointée de 
    $[a, b]$ et $f:[a, b] \to \R$, la somme de Riemann associée est définie
    comme
    $$
    S(f, \mathcal{D}) = \sum f(t) \ell(I) 
    \; \mbox{ où } \; 
    (t, I) \in \mathcal{D}
    \mbox{ et } 
    I \subset \left]-\infty, +\infty\right[.
    $$

[^cp]: En particulier avec cette convention, 
$\ell([-\infty, -\infty]) = \ell([+\infty, +\infty])= \ell(\varnothing) = 0$.

Autrement dit, nous remplaçons les intervalles fermés 
$\R= \left]-\infty, +\infty\right[$ par ceux de
$[-\infty, +\infty]$ et nous excluons de la somme de Riemann les
contributions des intervalles contenant $-\infty$ ou $+\infty$ (ce qui
explique pourquoi les valeurs $f(\pm \infty)$ n'ont pas d'importance).

Dans ce nouveau contexte, les définitions de jauge, de subdivision pointée, 
d'intégrabilité et d'intégrale sur un intervalle fermé restent formellement 
inchangées[^6s]. Les résultats relatifs à la linéarité de l'intégrale, son
additivité, sa restriction, l'égalité des intégrales de fonctions égales
presque partout sont toujours vrais ; des preuves formellement identiques
sont valables.

[^6s]: c'est l'effet "Night Shyamalan" ou "6ème sens": 
il faut relire le document, qui prend un nouveau sens compte tenu 
de ce que l'on sait désormais.

### Intégration de $x \mapsto 1/x^2$ {.example}
Considérons la fonction $f:\left[1, +\infty\right[$ définie par
$$
f(x) = \frac{1}{x^2}.
$$
On étend immédiatement cette fonction sur $[0, +\infty]$ en posant
$f(+\infty)=0$ (on note toujours $f$ la fonction qui en résulte).

La fonction $f$ admettant comme primitive $x \mapsto -1/x$
sur chaque intervalle borné $[a, b]$ 
de $\left[1, +\infty \right[$, par [le théorème fondamental du calcul](#TFC),
$$
\int_a^b f(t) \, dt = \left[x \mapsto -\frac{1}{x}\right]_a^b 
= \frac{1}{a} - \frac{1}{b}.
$$
"Passer à la limite" informellement (sans justification) dans cette expression
peut nous laisser penser que $f$ est intégrable sur 
$\left[1, +\infty \right]$ et vérifie
$$
\int_1^{+\infty} f(t) \, dt \stackrel{?}{=} 1.
$$
La suite confirmera cette intuition.

Nous souhaitons trouver pour tout $\varepsilon > 0$, une jauge $\gamma$ sur 
$\left[1, +\infty \right]$
tels que pour toute subdivision pointée $\mathcal{D}$ de $[1, +\infty]$ 
subordonnée à $\gamma$ on ait
$\left| S(f, \mathcal{D}) - 1 \right| \leq \varepsilon.$
Supposons que $\mathcal{D} = \{(t_i, [x_i, x_{i+1}]), \, i \in \{0, \dots, m\}\}$ et 
que les $x_i$ sont agencés de façon (strictement) croissante ; on a en particulier
$x_{m+1} = +\infty$ et $x_k < +\infty$ quand $k \leq m$. Notons
$\mathcal{D}_f = \{(t_i, [x_i, x_{i+1}]), \, i \in \{0, \dots, m-1\}\}$ ;
on a alors
$$
\begin{split}
\left| S(f, \mathcal{D}) - 1 \right| 
&\leq
\left| S(f, \mathcal{D}) - \left(1 - \frac{1}{x_{m}}\right) \right| + \frac{1}{x_{m}} \\
&\leq \left| \sum_{(t, [x, y]) \in \mathcal{D}_f} f(t)(y-x) - \left(\frac{1}{x} - \frac{1}{y}\right) \right| + \frac{1}{x_{m}} \\
&\leq \sum_{(t, [x, y]) \in \mathcal{D}_f} \left|f(t)(y-x) - \left(\frac{1}{x} - \frac{1}{y}\right) \right| + \frac{1}{x_{m}} \\
\end{split}
$$
Si l'on sélectionne une jauge $\gamma$ telle que
pour tout $t \in \left[1, +\infty\right[$ on ait $\gamma(t) \subset \R$
(et donc $+\infty \not \in \gamma(t)$)
et si la subdivision pointée $\mathcal{D}$ est subordonnée à $\gamma$,
la valeur $t_m$ associée à $(t_m, [x_m, +\infty]) \in \mathcal{D}$
vérifie nécessairement $t_m=+\infty$ et donc $[x_m,+\infty] \subset \gamma(+\infty)$.
Il suffit donc d'imposer par exemple $\gamma(+\infty) = \left]2/\varepsilon, +\infty\right]$
pour garantir que $1/x_{m} \leq \varepsilon/2.$
Si nous disposons ensuite d'un majorant pour chaque terme
$$
\left|f(t)(y-x) - \left(\frac{1}{x} - \frac{1}{y}\right) \right|,
$$
choisi de telle sorte que leur somme soit également inférieure à $\varepsilon/2$, 
nous pourrons alors conclure. 
Toutefois, la stratégie consistant à recherche un majorant proportionnel à 
la longueur de l'intervalle $[x, y]$ n'est plus applicable car l'intervalle
$[0, x_{m}]$ peut être arbitrairement long. 
Au lieu de cela, nous allons tâcher de trouver une jauge $\gamma$ telle que
$$
\left|f(t)(y-x) - \left(\frac{1}{x} - \frac{1}{y}\right) \right| \leq
\frac{\varepsilon}{2xy} (y-x) = \frac{\varepsilon}{2} \left(\frac{1}{x} - \frac{1}{y} \right)
$$
Les termes de droite de cette inégalité forment alors une série télescopique
dont la somme vérifie
$$
\sum_{(t, [x, y]) \in \mathcal{D}_f} \frac{\varepsilon}{2} \left(\frac{1}{x} - \frac{1}{y} \right)
 = \frac{\varepsilon}{2} \left(1- \frac{1}{x_m} \right)
 \leq \frac{\varepsilon}{2}.
$$
On note qu'il suffit d'établir d'une part que
$$
\left|f(t)(y-t) - \left(\frac{1}{t} - \frac{1}{y}\right) \right| \leq
\frac{\varepsilon}{2} \left(\frac{1}{t} - \frac{1}{y} \right)
$$
et d'autre part que
$$
\left|f(t)(t-x) - \left(\frac{1}{x} - \frac{1}{t}\right) \right| \leq
\frac{\varepsilon}{2} \left(\frac{1}{x} - \frac{1}{t} \right)
$$
pour obtenir l'inégalité cherchée. Or,
$$
\begin{split}
f(t)(y-t) - \left(\frac{1}{t} - \frac{1}{y}\right)
&= \frac{y-t}{t^2} - \left(\frac{1}{t} - \frac{1}{y}\right) \\
&= \frac{y}{t}\frac{y-t}{ty} - \left(\frac{1}{t} - \frac{1}{y}\right) \\
&= \frac{y}{t} \left(\frac{1}{t} - \frac{1}{y}\right) - \left(\frac{1}{t} - \frac{1}{y}\right) \\
&= \left(\frac{y-t}{t}\right)\left(\frac{1}{t} - \frac{1}{y}\right). \\
\end{split}
$$
On obtient donc la première inégalité souhaitée si 
$$
\frac{y-t}{t} \leq \frac{\varepsilon}{2}
\; \mbox{ soit } \;
y \leq t + \frac{\varepsilon}{2} t.
$$
De manière similaire, on montre que la seconde inégalité est satisfaite si
$$
\frac{t-x}{t} \leq \frac{\varepsilon}{2}
\; \mbox{ soit } \;
x \geq t - \frac{\varepsilon}{2} t.
$$
Au final, nous avons établi que si $\mathcal{D}$ est subordonnée à la jauge
$\gamma$ définie par
$$
\gamma(t) 
= 
\left|
\begin{array}{rl}
\left]t - \varepsilon/2, t + \varepsilon/2 \right[ & \mbox{ si } t \in \left[1, +\infty\right[, \\
\left]2/\varepsilon, +\infty\right] & \mbox{ si } t = +\infty,
\end{array}
\right.
$$
alors $|S(\mathcal{D}, f) - 1| \leq \varepsilon$ ; 
la fonction $x \mapsto 1/x^2$ est donc intégrable sur $\left[1, +\infty\right]$, 
d'intégrale égale à 1.


<!--
Pour fournir la majoration cherchée, nous formons
$$
\frac{f(t)(y-x) - \left(\frac{1}{x} - \frac{1}{y}\right)}{\frac{(y - x)}{xy}}
= \frac{xy}{t^2} - 1.
$$
Si l'on recherche une jauge $\gamma$ telle que 
$\gamma(t) = \left]t-\delta(t),t+\delta(t)\right[$, 
pour $t < +\infty$, on a alors
$t - \delta(t) \leq x \leq t$ et $t \leq y \leq t =\delta(t)$, et donc
$$
\frac{t(t-\delta(t))}{t^2} - 1 \leq \frac{xy}{t^2} - 1 \leq \frac{t(t+\delta(t))}{t^2} - 1,
$$
soit
$$
\left|  \frac{xy}{t^2} - 1  \right| \leq \frac{\delta(t)}{t}.
$$
Il suffit donc de choisir $\delta(t) = (\varepsilon /2) t$ pour obtenir la
majoration voulue.
-->

--------------------------------------------------------------------------------

### {.ante .remark}
La construction de l'intégrale dans cette section est applicable
indifféremment dans le cas des intervalles bornés ou non de la droite réelle.
Contrairement à l'intégrale de Riemann, il n'est pas nécessaire pour donner
un sens à l'intégrale d'une fonction définie sur un intervalle non-borné 
de calculer tout d'abord son intégrale sur un intervalle borné puis
d'essayer de passer à la limite[^CR]. Toutefois, si on souhaite se livrer
cette démarche avec l'intégrale de Henstock-Kurzweil, le résultat serait
identique à la démarche directe que nous avons adoptée ; avec l'intégrale
de Henstock-Kurzweil, [le théorème de Hake](#hake) montre
qu'il n'existe pas d'intégrale *impropre*, 
qui ne serait pas définissable directement mais uniquement par
un passage à la limite.

[^CR]: sans garantie que ce nouvel objet -- l'intégrale de Cauchy-Riemann --
partage les propriétés utiles de l'intégrale de Riemann.


### Théorème de Hake {.theorem #hake}
Soit $[a, b]$ un intervalle fermé de $[-\infty, +\infty]$ 
et $f: [a, b] \to \R$. La fonction $f$ est intégrable sur $[a, b]$ si
et seulement si elle est intégrable sur tout intervalle $[c, d]$
tel que $a < c$ et $d < b$ et que l'intégrale
$$
\int_c^d f(t) \, dt
$$
a une limite quand $c$ tend vers $a$ et $d$ tend vers $b$.
On a alors
$$
\int_a^b f(t) \, dt = \lim_{(c, d) \to (a,b)} \int_{c}^d f(t) \, dt.
$$

### Démonstration {.proof}
Se reporter à [@Swa01].

### {.post}
Le théorème de Hake permet d'étendre facilement certains résultats valables 
sur des segments de la droite réelle. A titre d'exemple :

### Théorème fondamental du calcul (extension) {.theorem}
Soit $[a, b]$ un intervalle fermé de $[-\infty, +\infty]$ 
et $f: [a, b] \to \R$, une fonction dérivable sur $\left]a, b\right[$ et
continue sur $[a, b]$. La fonction $f'$ (définie partout sauf en $a$ et $b$)
est intégrable sur $[a, b]$ et
$$
[f]_a^b := f(b) - f(a) = \int_a^b f'(t) \, dt.
$$

### Démonstration {.proof}
[Le théorème fondamental du calcul](#TFC) dans le cadre borné nous fournit
pour tous $c$ et $d$ tels que $a < c \leq d < b$ l'intégrabilité de $f'$
sur $[c, d]$ et la relation
$$
f(d) - f(c) = \int_c^d f'(t) \, dt.
$$
Par continuité, le membre de gauche de cette équation a une limite quand
$c$ tend vers $a$ et $d$ vers $b$, qui est $f(b) - f(a)$. 
[Le théorème de Hake](#hake) permet alors de conclure.


### {.remark .ante}
Un facteur vient simplifier l'étude de l'intégration sur des intervalles
(a priori) non bornés : il n'est pas nécessaire de considérer l'intégration 
dans tous les types
d'intervalles possibles car on peut toujours
se ramener au cas où l'on cherche à intégrer une fonction sur la
droite réelle (achevée) toute entière:

### Extension à la droite réelle achevée {.corollary #EDRA}
Une fonction $f:[a, b] \to \R$ est intégrable si et seulement 
si son prolongement $g$ par zéro dans $[-\infty, +\infty]$, 
c'est-à-dire la fonction $g :[-\infty, +\infty] \to \R$ telle que
$$
g(x) = \left|
\begin{array}{rl}
f(x) & \mbox{si } \, x \in  [a, b], \\
0 & \mbox{sinon,}
\end{array}
\right.
$$
est intégrable. Dans ce cas, on a
$$
\int_a^b f(t) \, dt = \int_{-\infty}^{+\infty} g(t) \, dt.
$$

### Démonstration {.proof}
Supposons que $a$ soit fini et que $b = +\infty$. 
Si $g$ est intégrable sur $[-\infty, +\infty]$, 
par [restriction](#restriction), $f$ est intégrable sur $[a, +\infty]$.
Réciproquement, si $f$ est intégrable sur $[a, +\infty]$,
la fonction $g$ étant nulle sur $\left[-\infty, a\right]$ 
à l'exception d'un point, elle y est intégrable ; 
étant égale à $f$ sur $[a, +\infty]$ elle y est également intégrable. 
Par additivité, $g$ est donc
intégrable sur $[-\infty, +\infty]$.
L'additivité fournit également
$$
\int_{-\infty}^{+\infty} g(t) \, dt = \int_{-\infty}^a g(t) \, dt + \int_{a}^{+\infty} g(t) \,dt.
$$
Comme $g$ est nulle sur $\left[-\infty, a\right]$ à l'exception au plus 
d'un point,
son intégrale sur $[-\infty, a]$ est nulle et comme $g=f$ sur $[a, +\infty]$,
$$
\int_{-\infty}^{+\infty} g(t) \, dt = \int_{a}^{+\infty} f(t) \,dt.
$$
Le résultat dans les autres cas ($a=-\infty$ et $b$ fini, $a$ et $b$ finis) 
se démontrent de manière analogue.


Subdivisions partielles
================================================================================

### Subdivision pointée partielle {.definition}
Une *subdivision pointée partielle* $\mathcal{D}$ de l'intervalle fermé 
$I = [a, b]$ de $[-\infty, +\infty]$ est une famille finie 
$$
\mathcal{D} = \{(t_i, I_i) \; | \; \; 0 \leq i \leq n-1\}
$$
où les $I_i$ sont des intervalles fermés de $[a, b]$ sans chevauchement
et $t_i \in I_i$ pour tout $i \in \{0, \dots, n-1\}.$
La somme de Riemann associée à la fonction $f:[a, b] \to \R$ 
et à la subdivision pointée partielle $\mathcal{D}$ de $[a, b]$ est 
la grandeur
$$
S(f, \mathcal{D}) = \sum f(t) \ell(I), \; \mbox{ où }(t, I) \in \mathcal{D}, \, \ell(I) < +\infty.
$$
Une subdivision pointée partielle $\mathcal{D}$ de l'intervalle fermé $[a, b]$ 
est *subordonnée à une jauge* $\gamma$ de $[a, b]$ si 
pour tout $(t, J) \in \mathcal{D}$, $J \subset \gamma(t).$

### Lemme de Henstock  {.theorem #henstock-lemma}
Soit $[a, b]$ un intervalle fermé, 
$f$ une fonction intégrable sur $[a, b]$ et $\gamma$ une jauge sur $[a, b]$ 
telle que pour toute subdivision pointée $\mathcal{D}$ de $[a, b]$ subordonnée
à $\gamma$, on ait
$$
\left|S(f, \mathcal{D}) - \int_a^b f(t) \, dt\right| \leq \varepsilon.
$$
Alors pour toute subdivision pointée partielle $\mathcal{D} = \{(t_k, I_k)\}_k$
de $[a, b]$ subordonnée à $\gamma$, on a également
$$
\left|S(f, \mathcal{D}) - \sum_k \int_{I_k} f(t) \, dt\right| \leq \varepsilon.
$$

### Démonstration du [lemme de Henstock][Lemme de Henstock] {.proof}
Il existe une famille finie d'intervalles fermés $\{J_j\}$, 
$j = 1, \dots, m$ 
telle que l'union des familles $\{I_k\}$ et $\{J_j\}$ forme une subdivision
(complète) de $[a, b]$. 
Pour tout $\eta > 0$, 
sur chaque intervalle $J_j$, il existe une jauge $\gamma_j$ telle que si
$\mathcal{D}_j$ est une subdivision pointée de $J_j$ subordonnée à $\gamma_j$,
alors 
$$
\left|S(f, \mathcal{D}_j) - \int_{J_j} f(t) \, dt \right| \leq \eta.
$$
Si de plus on choisit $\mathcal{D}_j$ subordonnée à la restriction de $\gamma$
à $J_j$, alors $\mathcal{D} \cup (\cup_j \mathcal{D}_j)$ est une subdivision
pointée (complète) de $[a, b]$ subordonnée à $\gamma$.
On déduit de l'hypothèse centrale du lemme que
$$
\left|
S(f, \mathcal{D}) + \sum_j S(f, \mathcal{D}_j) 
- 
\sum_k \int_{I_k} f(t) \, dt + \sum_{j} \int_{J_j} f(t) \, dt
\right|
\leq
\varepsilon
$$
et donc par l'inégalité triangulaire que
$$
\left|
S(f, \mathcal{D}) 
- 
\sum_k \int_{I_k} f(t) \, dt
\right|
\leq
\varepsilon + m \eta.
$$
Le choix de $\eta > 0$ étant arbitraire, l'inégalité cherchée est établie.

### Continuité des intégrales indéterminées {.proposition}
Pour toute fonction $f:\R \to \R$ intégrable 
et pour tout nombre réel étendu $a$, l'application
$$
x \in \R \mapsto \int_a^x f(t) \, dt 
$$
est continue.

### Démonstration {.proof}
Montrons la continuité de l'intégrale à droite en $x$, la continuité à gauche
s'établissant de façon similaire. 
Par additivité de l'intégrale, il suffit de montrer que la grandeur
$$
\int_x^{x+h} f(t) \, dt
$$
tend vers $0$ quand $h>0$ tend vers $0$. Par restriction, la fonction $f$ est 
intégrable sur $[x, +\infty]$ : 
pour tout $\varepsilon > 0$, il existe une jauge
$\gamma$ sur $[x, +\infty]$ telle que pour toute subdivision pointée
$\mathcal{D}$ de $[x, +\infty]$ subordonnée à $\gamma$, 
l'écart entre la somme de Riemann
$S(f,\mathcal{D})$ et l'intégrale de $f$ entre $x$ et $+\infty$ est au
plus $\varepsilon/2$. 

On peut remplacer $\gamma$ par une jauge $\nu$ vérifiant
$\nu(x) \subset \gamma(x)$ et $\nu(t) = \gamma(t) \cap \left]x,+\infty\right]$
sinon ; cela garantit que pour tout subdivision pointée $\mathcal{D}$ 
subordonnée à $\nu$, $\mathcal{D}$ est subordonnée à $\gamma$ et si 
$(t,J) \in \mathcal{D}$ et $x \in J$, alors $t=x$.

[Le lemme de Henstock](#henstock), appliqué à toute subdivision partielle
$\mathcal{D} = \{(x, J)\}$ subordonnée à $\nu$, c'est-à-dire telle que
$J := [x, x+h] \subset \nu(x)$, fournit
$$
\left| 
f(x) h - \int_x^{x+h} f(t) \, dt
\right| \leq \frac{\varepsilon}{2},
$$ 
dont on déduit par l'inégalité triangulaire que
$$
\left| \int_x^{x+h} f(t) \, dt \right|
\leq
\frac{\varepsilon}{2} + |f(x)|h.
$$
Il suffit donc de choisir $\nu(x)$ tel que $|f(x)| h \leq \varepsilon / 2$
quand $[x, x+h] \subset \nu(x)$ pour assurer que
$$
\left| \int_x^{x+h} f(t) \, dt \right|
\leq
\varepsilon.
$$


Exercices
================================================================================

Intervalle {.question #int}
--------------------------------------------------------------------------------

Montrer qu'un sous-ensemble $I$ de $\R$ est un intervalle si et
seulement si il *est connexe par arcs*, c'est-à-dire si et seulement
si pour tout couple de points $x$ et $y$ de $I$ on peut trouver un
chemin de $I$ joignant $x$ à $y$, c'est-à-dire une fonction continue
$\phi:[0, 1] \to I$, telle que $\phi(0) = x$ et $\phi(1) = y$.

Subdivisions subordonnées à une jauge I {.question #subd-subor}
--------------------------------------------------------------------------------

![Graphe de la jauge $\gamma$.](images/gauge-plot-squeeze.py)

Soit $\gamma$ la jauge sur $[0, 1]$ définie par 
$\gamma(0)= \left]-1/2, 1/2\right[$ et $\gamma(t) = \left]0,2t\right[$
si $t>0$.
Déterminer une subdivision pointée de $[0, 1]$ qui soit subordonnée à $\gamma$.



Subdivisions subordonnées à une jauge II {.question #subd-subor-2}
--------------------------------------------------------------------------------

Soit $[a, b]$ un intervalle compact de $\R$ ;
soit $\gamma$ une jauge sur $[a, b]$. On suppose qu'il existe 
un $\varepsilon > 0$ tel que  
$$
\mbox{pour tout } t \in [a, b], \; \left]t-\varepsilon, t+\varepsilon\right[ \subset \gamma(t).
$$
Suggérer un procédé plus simple que le procédé très général utilisé par 
[le lemme de Cousin](#cousin) pour construire une subdivision pointée
subordonnée à $\gamma$.

L'intégrale de Riemann est absolue {.question #Rabs}
--------------------------------------------------------------------------------

Montrer que l'intégrale de Rieman est absolue : 
si une fonction $f$ est intégrable au sens de Riemann, 
sa valeur absolue $|f|$ l'est également.


Continuité presque partout {#cpp}
--------------------------------------------------------------------------------

### Question 1 {.question #cpp-1}
Est-ce qu'une fonction égale presque partout à une fonction continue est
presque partout continue ? La réciproque est-elle vraie ?

### Question 2 {.question #cpp-2}
La fonction de Dirichlet $1_{\Q}$ -- ou fonction indicatrice de $\Q$ -- 
définie par
$$
1_{\Q}(x) = 
\left|
\begin{array}{cl}
1 & \mbox{si } x \mbox{ est rationnel,} \\
0 & \mbox{sinon.}
\end{array}
\right.
$$
est-elle intégrable sur $[0, 1]$ au sens de Riemann ? 
Et au sens de Henstock-Kurzweil ?

Continuité par morceaux {.question #cpm}
--------------------------------------------------------------------------------

Montrer que toute fonction $f:[a, b] \to \R$ continue par morceaux sur un
intervalle compact de $\R$ est intégrable au sens de Henstock-Kurzweil.

Un ensemble de Cantor
--------------------------------------------------------------------------------

Chaque nombre réel $x$ de $\left[0, 1\right[$ peut être représenté
par un développement décimal de la forme $x=0.a_1a_2a_3\cdots$
où $a_i \in \{0,1, \dots, 9\}$, une notation qui signifie que
$$
x = \sum_{i=1}^{+\infty} a_i 10^{-i}.
$$
Ce développement est unique si on lui impose d'être *propre*, 
c'est-à-dire si l'on interdit les séquences infinie de nombres $9$ consécutifs[^wp].

[^wp]: Dans le cas contraire, on pourrait par exemple représenter $x=1/2$ comme
$0.5000\cdots$ ou comme $0.4999\cdots$.

On définit l'ensemble $A$ comme le sous-ensemble de $\left[0, 1\right[$
dont le développement décimal ne comporte que des nombres pairs.
Par exemple, $x=2/3 = 0.666\cdots$ appartient à $A$, mais 
$x=\sqrt{2}/2 = 0.707\cdots$ non.

### Question 1 {.question #cantor-1}

Montrer que l'ensemble $A$ est négligeable.

### Question 2 {.question #cantor-2}

Montrer néanmoins que $A$ n'est pas dénombrable, 
mais a la "puissance du continu" 
(qu'il peut être mis en bijection avec $\R$ 
ou avec un intervalle de longueur non vide de $\R$, 
ce qui revient au même).

<!-- En attente ...
Intégration sur un intervalle non borné  {.question #iinb-1}
--------------------------------------------------------------------------------

Il est possible de définir l'intégrabilité (et l'intégrale) d'une fonction
sur $\R$ de façon élémentaire,
sans avoir recours à la droite achevée.
Le procédé en question est plus élémentaire[^es] ; 
il revient à exiger que partir les subdivisions d'intervalles bornés
exploitées par la somme de Riemann en plus d'être suffisamment "fines" 
soient suffisamment "étendues".

[^es]: mais pas nécessairement plus simple ...

Montrer que la fonction $f:\R \to \R$ est intégrable si et seulement si il
existe un réel $A$ tel que pour tout $\varepsilon > 0$ 
il existe une jauge $\gamma$ de $\R$ 
et un intervalle compact $K$ de $\R$ tels que pour tout intervalle compact 
$[a, b]$ de $\R$ tel que $K \subset [a, b]$
et pour toute subdivision pointée $\mathcal{D}$ de $[a, b]$ 
subordonnée à $\gamma$, on ait
$|S(f, \mathcal{D}) - A| \leq \varepsilon$.

-->




Séries et intégrales {#si}
--------------------------------------------------------------------------------

Soit $a_k \in \R$  une suite de valeurs indexées par $k\in \N$ ; 
on lui associe la fonction $f:\left[0, +\infty\right] \to \R$ définie par
$f(x) = a_k$ quand $k \leq x < k+1$ (et $f(+\infty)=0$ par exemple). 

![Graphe de la fonction $f$ associée à la suite $a_k = (-1)^k / (k+1)$.](images/graph-series.py)

### Question 1 {.question #si-1}
Montrer que si la série $\sum_k a_k$ est divergente, 
$f$ n'est pas intégrable.

### Question 2 {.question #si-2} 
Montrer que si la série $\sum_k a_k$ est convergente,
alors la fonction est intégrable et
$$
\int_0^{+\infty} f(x) \, dx = \sum_{k=0}^{+\infty} a_k.
$$

### Question 3 {.question #si-3}
En déduire une fonction $f:[0, +\infty] \to \R$ qui soit intégrable sans
que $|f|$ le soit (on dit que $f$ est conditionnellement intégrable).


Solutions
================================================================================

## Intervalle {.answer #answer-int}

Montrons tout d'abord que la condition est nécessaire. 
Supposons que $x$ et $y$ appartiennent à $I$ et que $x$ 
soit inférieur ou égal à $y$. Alors pour tout $t \in [0,1]$, 
$\phi(t) = (1-t) x + t y$ est un point intermédiaire entre $x$ et $y$,
et par conséquent, appartient à $I$. La fonction $\phi$ ainsi définie 
est clairement continue et vérifie $\phi(0) = x$ et $\phi(1) = y$ ; 
c'est donc un chemin de $I$ qui joint $x$ à $y$. Par conséquent,
$I$ est connexe par arcs.

Réciproquement, si $I$ est connexe par arcs et contient les points $x$
et $y$, tout chemin de $I$ qui joint $x$ et $y$, continu et à valeurs réelles,
vérifie le théorème des valeurs intermédiaires : pour toute valeur intermédiaire
$z$ entre $x$ et $y$, il existe donc un $t \in [0, 1]$ tel que $\phi(t) = z$.
Comme $\phi$ est à valeurs dans $I$, $z \in I$ ; l'ensemble $I$ est donc un 
intervalle de $\R$.

Subdivisions subordonnées à une jauge I {.answer #answer-subd-subor}
--------------------------------------------------------------------------------

On applique pas à pas la démarche de la preuve du [lemme de Cousin](#cousin).

On considère initialement les subdivisions pointées de la forme $\{(t_1, [0,1])\}$. 
Mais quel que soit $t_1 \in [0, 1]$, on réalise que $[0, 1] \not \subset \gamma(t_1)$.
En effet, $[0, 1] \not \subset \gamma(0) = \left]-1/2, 1/2\right[$ et 
comme pour tout $t_1>0$, $0 \not \in \gamma(t)$, on ne peut avoir
$[0, 1] \subset \gamma(t)$.

On considère donc les subdivisions de la forme
$$\{(t_1, [0,1/2]), (t_2, [1/2, 1])\}.$$ 
Concernant le second terme de cette subdivision, 
on se rend compte que pour $t_2 = 1$, on a 
$\gamma(t_2) = \left]0, 2\right[$ et donc $[1/2, 1] \subset \gamma(t_2)$.
Par contre on peut se convaincre comme à la première étape du processus
qu'il est impossible d'avoir $[0, 1/2] \subset \gamma(t_1)$
quand $t_1 \in [0, 1/2]$.

On considère donc les subdivisions de la forme
$$\{(t_1, [0,1/4]), (t_2, [1/4, 1/2]), (1, [1/2, 1])\}.$$
Cette fois-ci, on constate que $t_1=0$ fournit
$[0,1/4] \subset \gamma(0) = \left]-1/2, 1/2\right[$, et
qu'avec $t_2 = 1/2$, on a $[1/4, 1/2] \subset \gamma(t_2) = \left]0, 1\right[$.

Par conséquent, la subdivision 
$$
\mathcal{D} = \{(t_1, [0,1/4]), (t_2, [1/4, 1/2]), (1, [1/2, 1])\}
$$
est subordonnée à $\gamma$.

![Graphe de la jauge $\gamma$ et de la subdivision pointée $\mathcal{D}$](images/gauge-plot-squeeze-solution.py)

Subdivisions subordonnées à une jauge II {.answer #answer-subd-subor-2}
--------------------------------------------------------------------------------

Sous l'hypothèse énoncée, il suffit de limiter la recherche aux subdivisions
uniformes
$$
\mathcal{D}_m 
= 
\left\{\left(t_k, \left[a + k\frac{b-a}{m}, a + (k+1)\frac{b-a}{m} \right]\right)
\, \left|\vphantom{\frac{a}{b}}\right. k \in \{0, \dots, m-1\}\, \right\},
$$
et le choix des $t_k$ importe peu.
En effet, dès que $m$ est assez grand pour que l'on ait
$$
\frac{b-a}{m} < \varepsilon,
$$
alors pour tout $k \in \{0, \dots, m-1\}$ et pour tout 
$t \in \left[a + k\frac{b-a}{m}, a + (k+1)\frac{b-a}{m} \right]$,
$$
\left[a + k\frac{b-a}{m}, a + (k+1)\frac{b-a}{m} \right] \subset \left]t- \varepsilon, t+\varepsilon \right[
\subset \gamma(t).
$$
La jauge $\mathcal{D}_m$ est donc subordonnée à $\gamma$.


L'intégrale de Riemann est absolue {.answer #answer-Rabs}
--------------------------------------------------------------------------------

Nous exploitons le [critère de Lebesgue pour l'intégrabilité au sens de Riemann][Critère de Lebesgue pour l'intégrabilité au sens de Riemann] : si $f$ est intégrable au sens de Riemann,
elle est bornée -- et donc $f$ également -- et continue presque partout
-- et donc $|f|$ également ($|f|$ est continue en tout point où
$f$ est continue comme composée de fonctions continues en ce point). 
Par conséquent, $|f|$ est intégrable au sens de Riemann.


Continuité presque partout
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-cpp-1}
Une fonction égale presque partout à une fonction continue n'est pas 
nécessairement presque partout continue. La fonction de Dirichlet 
de [la question 2](#cpp-2) fournit un bon exemple : elle est égale à la
fonction identiquement nulle -- qui est continue -- sur tout $\R$ à
l'exception des rationnels et l'ensemble des rationnels est négligeable,
[car dénombrable](#edn). Mais elle n'est continue en aucun point, car
tout nombre rationnel est limite de nombres irrationnels et réciproquement.

La réciproque n'est pas vérifiée non plus : la fonction de Heaviside
$e:\R \to \R$ -- ou fonction indicatrice de $\left[0, +\infty \right[$, 
définie par
$$
e(x) = \left|
\begin{array}{cl}
1 & \mbox{si } x\geq 0,\\
0 & \mbox{sinon.}
\end{array}
\right.
$$
est continue presque partout (sauf en $0$). Mais aucune modification de
cette fonction sur un ensemble négligeable ne pourra la rendre continue
en $0$ ; il faudrait pour cela modifier tout un intervalle de la forme
$\left]-\varepsilon, 0\right[$ ou de la forme $\left]0, \varepsilon\right[$
pour un $\varepsilon > 0$, mais aucun de ces deux intervalles n'est négligeable.

### Question 2 {.answer #answer-cpp-2}
La fonction de Dirichlet $1_{\Q}$ sur $[0, 1]$ est égale presque partout à la
fonction identiquement nulle qui est continue, elle est donc intégrable au
sens de Henstock-Kurzweil. Mais elle n'est pas continue presque partout,
donc elle n'est pas intégrable au sens de Riemann.

Continuité par morceaux {.answer #answer-cpm}
--------------------------------------------------------------------------------

On peut bien sûr exploiter les propriétés de l'intégrale de Riemann
pour répondre à cette question :
toute [fonction continue par morceaux $f:[a, b] \to \R$ 
définie sur un intervalle compact de $\R$ est intégrable au sens de Riemann](#Rcpp) ;
comme [toute fonction intégrable au sens de Riemann est intégrable au sens
de Henstock-Kurzweil](#RHK), le résultat est acquis.

Si l'on souhaite montrer directement ce résultat, sans passer par l'intégrale
de Riemann, on peut tout d'abord réduire ce problème à celui de l'intégrabilité
des fonctions continues $f:[a, b] \to \R$. En effet, supposons les fonctions 
continues sur un intervalle compact de $\R$ intégrables ; si $f$ est
une fonction continue par morceaux sur $[a, b]$, 
on peut décomposer $[a, b]$ en une union finie d'intervalles $[a_k, b_k]$ qui ne
se chevauchent pas, et tels que la restriction de $f$ à chaque $[a_k, b_k]$
soit continue -- ou diffère d'une fonction continue en au plus deux points.
Deux [fonctions égales presque partout étant intégrables](#fepp) (ou non) 
simultanément, ces restrictions sont toutes intégrables. 
Par [additivité](#additivité), la fonction $f$ est donc intégrable.

Supposons désormais $f:[a, b] \to \R$ continue. Comme nous ne connaissons
pas a priori la valeur de son intégrale (éventuelle), nous allons essayer
de prouver son intégrabilité en utilisant le [critère de Cauchy](#CIC).
Soit $\mathcal{D}$ et $\mathcal{D'}$ deux subdivisions pointées de $[a, b]$.
Si $\mathcal{D}$ est composée des paires $(t_i, I_i)$ et $\mathcal{D'}$
des paires $(s_j, J_j)$, en notant $K_{ij} = I_i \cap J_j$, on obtient
$$
\begin{split}
\left|S(f, \mathcal{D}) - S(f,\mathcal{D}')\right|
&=
\left|\sum_i f(t_i) \ell(I_i) - \sum_k f(s_j) \ell(I_j)\right| \\
&=
\left|\sum_i f(t_i) \left(\sum_j \ell(K_{ij})\right) - \sum_j f(s_j) \left(\sum_{i} \ell(K_{ij})\right)\right| \\
&=
\left|\sum_{i, j}  (f(t_i) - f(s_j)) \ell(K_{ij}) \right|.
\end{split}
$$
De toute évidence, on peut limiter dans la dernière expression la somme
aux ensemble $K_{ij}$ non vides, c'est-à-dire tels que 
$I_i \cap J_j \neq \varnothing$.
Supposons que $\mathcal{D}$ et $\mathcal{D}'$ soient subordonnées à une
jauge $\gamma$ de $[a, b]$, telle que si $x \in \gamma(t)$, alors
$$
|f(x) - f(t)| \leq \frac{1}{2}\frac{\varepsilon}{b-a}.
$$
Une telle jauge existe par continuité de $f$.
Alors, si $t_i \in I_i$, $s_j \in J_j$ et $x \in I_i \cap J_j$,
$$
\left|f(t_i) - f(s_j)\right| \leq 
\left|f(x) - f(s_j)\right| + \left|f(x) - f(t_i)\right|
\leq 
\frac{\varepsilon}{b-a}
$$
et par conséquent
$$
\left|S(f, \mathcal{D}) - S(f,\mathcal{D}')\right|
\leq 
\sum_{i, j}  \left|f(t_i) - f(s_j)\right| \ell(K_{ij})
=\frac{\varepsilon}{b-a} \sum_{i, j} \ell(K_{ij})
= \varepsilon.
$$
Par [le critère de Cauchy](#CIC), la fonction $f$ est donc intégrable.

Un ensemble de Cantor
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-cantor-1}

L'ensemble $A$ peut être recouvert par la collection ne contenant que 
l'intervalle $\mathcal{A}_0 = \left[0, 1\right[$, ou par la collection d'intervalles
$$
\mathcal{A}_1 = \{\left[0, 1/10\right[, \left[2/10, 3/10\right[, \dots, \left[8/10, 9/10\right[\}
$$
qui contient exactement les nombres $x$ de $\left[0,1\right[$ dont
le premier chiffre du développement décimal propre est pair.
On a  clairement 
$$
\sum_{I \in \mathcal{A}_1} \ell(I) = \ell(\left[0,1\right[) = 1
\, \mbox{ et } \,
\sum_{I \in \mathcal{A}_1} \ell(I) = 5 \times \frac{1}{10} = \frac{1}{2}.
$$
On peut poursuivre le procédé en considérant la collection 
$\mathcal{A}_n$ des $5^n$ intervalles dont l'union forme l'ensemble
des nombres $x$ dont
les $n$ premiers chiffres du développement décimal propre sont pairs,
ensemble qui inclus $A$.
On peut de plus se convaincre par récurrence que
$$
\sum_{I \in \mathcal{A}_n} \ell(I) = 5^n \times \frac{1}{10^n} = \frac{1}{2^n}.
$$
Comme $1/2^n$ tend vers $0$ quand $n$ tend vers $+\infty$, 
nous avons établi que $A$ est négligeable.

### Question 2 {.answer #answer-cantor-2}

L'opération qui à $x=0.a_1a_2\cdots \in A$ associe
$y=0.b_1b_2\cdots$ où $b_i = a_i/2$ est une bijection
de $A$ sur $\left[0, 0.444\cdots\right[ = \left[0, 4/9\right[$,
ce qui montre que $A$ a la puissance du continu (et donc n'est pas
dénombrable).

<!--

TODO -- Intégration sur un intervalle non borné {.answer #answer-iinb-1}
--------------------------------------------------------------------------------

  -->


Séries et intégrales
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-si-1}
Si $\sum_k a_k$ est divergente, $f$ ne satisfait pas 
[le critère d'intégrabilité de Cauchy](#CIC).
En effet, la série elle-même ne satisfait pas le critère de Cauchy : 
il existe donc un $\varepsilon > 0$ tel que pour tout entier $j$, il existe un
entier $n$ tel que $$\left|\sum_{k=j}^{j+n} a_k\right| > \varepsilon.$$
Soit $\gamma$ une jauge sur $[0, +\infty]$ et soit 
$$\mathcal{D} = \{(t_k, [x_k, x_{k+1}]\}_{k=1}^m$$ une subdivision subordonnée
à $\gamma$ ; on peut toujours supposer que $\gamma(t) \subset \left[0, +\infty \right[$
quand $t \in \left[0, +\infty \right[$ quite à rendre plus fine la jauge initiale,
ce qui entraine $t_{m} = x_{m+1} = +\infty$.
Dans ce cas, on a en particulier $\left[x_m, +\infty\right] \subset \gamma(+\infty)$ ;
si l'entier $j$ est supérieur à $x_k$, la subdivision
$$\mathcal{D}' = \{(t_k, [x_k, x_{k+1}]\}_{k=1}^{m-1} \cup \{(k,[k, k+1])\}_{k=j}^{j+n}
\cup \{(+\infty, [j+n+1, +\infty])\} $$ est
également subordonnée à $\gamma$ et
$$
S(f,\mathcal{D}') = S(f,\mathcal{D}) + \sum_{k=j}^{j+n} a_k.
$$
Il est donc possible de choisir $\mathcal{D}'$ telle que la distance
entre $S(f, \mathcal{D})$ et $S(f, \mathcal{D}')$ soit strictement supérieure
à $\varepsilon$, ce qui contredit le critère d'intégrabilité de Cauchy.
La fonction $f$ n'est donc pas intégrable.

### Question 2 {.answer #answer-si-2} 
Supposons la série $\sum_k a_k$ convergente. 
Soit $\varepsilon > 0$ et $\mathcal{D}$ une
subdivision pointée de $[0, +\infty]$, de la forme
$$\mathcal{D} = \{(t_k, (x_k, x_{k+1})\}_{k=1}^m,$$
subordonnée à une jauge $\gamma$ telle que $\gamma(t) \subset \left[0, +\infty \right[$
quand $t \in \left[0, +\infty \right[$.
Si $\lceil x \rceil$ désigne l'entier immédiatement supérieur au nombre réel $x$
(et $\lfloor x \rfloor$ l'entier immédiatement inférieur), on a 
$$
\left|S(f, \mathcal{D}) - \sum_{k=0}^{+\infty} a_k \right|
\leq 
\left|S(f, \mathcal{D}) - \sum_{k=0}^{\lceil x_{m+1} \rceil} a_k \right|
+
\left|\sum_{k =\lceil x_{m+1}\rceil+1}^{+\infty} a_k \right|.
$$
Si $|\sum_{k=j}^{+\infty} a_k| \leq \varepsilon / 2$, pour tout $j\geq n$, 
il suffit donc d'imposer $\lceil x_{m+1}\rceil+1 \geq n$ pour garantir
que
$$
\left|\sum_{k =\lceil x_{m+1}\rceil+1}^{+\infty} a_k \right| \leq \frac{\varepsilon}{2}.
$$
C'est donc le cas si $\gamma(+\infty) = \left]n, +\infty \right]$.
Pour le reste des valeurs de la jauge, prenons
$\gamma(t) = \left]\lfloor t \rfloor, \lceil t \rceil \right[$ si $t \not \in \N$,
et $\gamma(k) = \left]k - \varepsilon' / 2^{k+1}, k+\varepsilon'/2^{k+1}\right[$ 
si $k \in \N$. Un calcul direct montre alors que
$$
\left|S(f, \mathcal{D}) - \sum_{k=0}^{\lceil x_{m+1} \rceil} a_k \right|
\leq \sum_{k=0}^{+\infty} |a_{k+1} - a_k| \frac{\varepsilon'}{2^{k+1}}
\leq \left(\sup_k |a_{k+1} - a_k|\right) \times \varepsilon'.
$$
Il suffit de sélectionner 
$\varepsilon' = (\varepsilon / 2) / \left(\sup_k |a_{k+1} - a_k|\right)$
pour obtenir
$$
\left|S(f, \mathcal{D}) - \sum_{k=0}^{+\infty} a_k \right|
\leq 
\varepsilon,
$$
ce qui prouve le résultat cherché.

### Question 3 {.answer #answer-si-3}
La fonction $f$ associée à la suite des
$$
a_k = \frac{(-1)^k}{(k+1)}, \, k\geq 0
$$
est conditionnellement convergente. En effet, $\sum_k a_k$ est convergente
-- donc $f$ est intégrable -- mais $\sum_k |a_k|$ ne l'est pas ($\sum_k a_k$
n'est pas absolument convergente). Or la fonction associée aux $|a_k|$ n'est
autre que $|f|$ ; la fonction $|f|$ n'est donc pas intégrable.


Références
================================================================================
