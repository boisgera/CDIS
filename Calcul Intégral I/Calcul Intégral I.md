% Calcul Intégral I

<!-- LaTeX Macros -->
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}

TODO
--------------------------------------------------------------------------------

  - intégrale d'une fonction nulle presque partout (par étapes: 1 / nb
    finies de valeurs égale à 1, puis fct de Dirichlet, puis fct égale à un sur
    un ensemble de mesure nulle, puis cas général, ce type de progression 
    (même si pas exactement celle-là, on a peut-être ))

  - ...



Somme et Intégrale de Riemann
--------------------------------------------------------------------------------

### Intervalle {.definition}

On appelle *intervalle* tout sous-ensemble $I$ de $\R$ 
tel que si $x$ et $y$ appartiennent à $I$ et vérifient $x \leq y$,
et si $z$ est un point intermédiaire (tel que $x \leq z \leq y$) 
alors $z$ appartient à $I$.

### Type d'intervalles {.remark .post}
Avec cette définition, les intervalles peuvent être bornés ou non-bornés,
ouverts, fermés, ouvert et fermés ou ni l'un ni l'autre.
Les intervalles de la forme $\left]-\infty, \infty\right[$ 
(c'est-à-dire $\R$)
$\left]-\infty, b\right[$, $\left]a,\infty\right[$ 
et $\left]a,b\right[$ 
-- où $a$ et $b$ désignent des nombres réels -- 
sont ouverts;
les intervalles de la forme $\left]-\infty, \infty\right[$,
$\left]-\infty, b\right]$, $\left[a,\infty\right[$ 
et $\left[a,b \right]$ sont fermés;
les intervalles compacts (à la fois fermés et bornés) sont de la forme $[a, b]$.

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
Une *subdivision* de l'intervalle fermé $I = [a,b]$
est une collection finie
$$
\{I_i \; | \; \; 0 \leq i \leq n-1 \}
$$
constituée d'intervalles fermés de $I$, *sans chevauchement*
-- si $i$ et $j$ diffèrent, l'intersection de $I_i$ et $I_j$ contient au 
plus un point -- 
et *recouvrant $I$* 
-- l'union de tous les intervalles $I_i$ est égal à $I$. 
Une *subdivision pointée* $\mathcal{D}$ de l'intervalle fermé $I = [a, b]$ 
de $\R$ est une collection finie 
$$
\mathcal{D} = \{(t_i, I_i) \; | \; \; 0 \leq i \leq n-1\}
$$
où les $I_i$ forment une subdivision de $I$ et 
$t_i \in I_i$ pour tout $i \in \{0, \dots, n-1\}.$

### Somme de Riemman {.definition}
La somme de Riemann associée à la fonction $f:[a, b] \to \R$ 
et à la subdivision pointée $\mathcal{D}$ de $[a, b]$ est la grandeur
$$
S(f, \mathcal{D}) = \sum_{(t, I) \in \mathcal{D}} f(t) \ell(I).
$$

### Intégrale de Riemann {.definition}
Une fonction $f:[a, b] \to \R$ est dite *intégrable 
(au sens de Riemann)* s'il existe un réel $A$ tel
que pour tout $\varepsilon > 0$ il existe un réel $\delta>0$ tel 
que pour toute subdivision pointée $\mathcal{D}$ de $[a, b]$ 
vérifiant pour $(t, J) \in \mathcal{D}$, 
$\ell(J) < \delta$, on ait
$|S(f, \mathcal{D}) - A| \leq \varepsilon$.
Le réel $A$ quand il existe est unique; il est appelé
*intégrale de $f$ sur $[a, b]$* et noté
$$
\int_a^b f(t) \, dt
\, \mbox{ ou } \,
\int_{[a, b]} f(t) \, dt
$$

### Quadrature {.example}

Cette définition permet de garantir l'exactitude asymptotique de méthodes de 
quadrature -- c'est-à-dire d'algorithmes de calcul numérique d'intégrales -- 
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
&= \sum_{i=0}^{m-1} f\left(a + \frac{b-a}{m}\right) \ell 
\left(\left[a + i \frac{b-a}{m}, a + (i+1) \frac{b-a}{m} \right]\right)\\
&= \sum_{i=0}^{m-1} f\left(a + \frac{b-a}{m}\right) \frac{b-a}{m}  \\
&= \frac{b-a}{m} \sum_{i=0}^{m-1} f\left(a + \frac{b-a}{m}\right)
\end{split}
$$
De plus, quel que soit $\delta > 0$, pour $m$ suffisamment grand, on a
$$
\ell\left(\left[a + i \frac{b-a}{m}, a + (i+1) \frac{b-a}{m} \right]\right)
=
\frac{b-a}{m}
<
\delta
$$
Par conséquent,
$$
\frac{b-a}{m} \sum_{i=0}^{m-1} f\left(a + \frac{b-a}{m}\right)
\to \int_a^b f(t) \, dt
\, \mbox{ quand } \, m \to +\infty.
$$
La définition de l'intégrale de Riemann, ne se limite pas à une famille 
particulière de subdivisions -- comme ici à des subdivisions régulières de 
$[a, b]$ où tous les intervalles sont de même longueur -- et n'impose 
pas une position fixe au point $t_i$ dans l'intervalle $J_i$ -- 
comme ici à gauche de l'intervalle -- ce qui garantit une forme de robustesse
à la définition de l'intégrale; d'autres méthodes de quadratures pourront
être utilisées avec le même résultat asymptotique.

### {.remark .ante}

L'intégrale de Riemann possède des limitations qui en font un outil mathématique
difficile à exploiter. 
En particulier la classe des fonctions qui peuvent être intégrées est trop 
restrictives pour certaines applications car les fonctions "trop grandes" ou 
"trop irrégulières" ne peuvent être intégrables. 
Les deux théorèmes qui suivent précisent cette situation.

### Seules les fonctions bornées sont intégrables {.lemma}
Si $f:[a, b] \to \R$ est intégrable au sens de Riemann, alors $f$ est bornée. 

### Démonstration {.proof}

Soit $\delta > 0$ tel que pour toute subdivision pointée $\mathcal{D}$ de 
$[a, b]$ vérifiant $\ell(J) < \delta$ pour tout $(t, J) \in \mathcal{D}$, 
on ait
$$\left|S(f, \mathcal{D}) - \int_a^b f(t) \, dt\right| \leq 1.$$
Soit $\mathcal{D} = \{(t_i, [a_i, b_i])\}_{i=0}^{m-1}$ une telle subdivision;
il est toujours possible de supposer en en outre que $\mathcal{D}$ ne contient 
aucun intervalle de longueur nulle (enlever de tels intervalles à $\mathcal{D}$
génère une nouvelle subdivision dont la somme de Riemann est identique).

Soit $J_i = [a_i, b_i]$ un intervalle de $\mathcal{D}$; 
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
Nous verrons ultérieurement que cette intuition sera vérifiée.

[^me]: plus exactement de mesure *extérieure* de longueur nulle.

### Presque partout {.definition}
Une propriété dépendant d'un réel $x$ est vraie *presque partout*
si l'ensemble des points $x$ où elle est fausse est un ensemble
négligeable.

### Les ensembles dénombrables sont négligeables {.example}
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

### Démonstration {.proof}
[Le lemme ci-dessus][Seules les fonctions bornées sont intégrables] montre
que le caractère borné est nécessaire pour l'intégrabilité au sens de
Riemann. Pour le reste de la preuve, se reporter à [@Bur07, p. 58].


Intégrale de Riemann Généralisée
--------------------------------------------------------------------------------

### Jauge {.definition}
Une *jauge* $\gamma$ sur un intervalle $I$ de $\R$ est une fonction 
qui associe à tout $t \in I$ un intervalle ouvert $\gamma(t)$ de $\R$ 
contenant $t$. 

### Subdivision pointée subordonnée à une jauge {.definition}
Une subdivision pointée $\mathcal{D}$ de l'intervalle compact $I$ 
est *subordonnée à une jauge* $\gamma$ sur $I$ si pour tout 
$(t, J) \in \mathcal{D}$, $J \subset \gamma(t).$

### Représentation graphique

On peut associer à une jauge $\gamma$ sur $[a, b]$ l'ensemble du plan
$$
\{(x, y) \; | \; x \in [a, b], \, y \in \gamma(x) \}.
$$
Par construction, cet ensemble contient la diagonale 
$$
D = \{(x,x) \; | \; x \in [a, b]\}.
$$

### TODO
 example, et expliquer pourquoi cette représentation est pratique
pour visualiser si une subdivision pointée est subordonnée à une jauge.

Par exemple, la jauge $\gamma$ définie sur $[0,1]$ par 
$\gamma(t) = \left] t-0.25, t+0.25 \right[$ est représentée comme suit:

### TODO
Check valeur ($0.2$ ou $0.25$ ?) et "langage graphique": l'ensemble est ouvert,
sont bord en noir ne devrait pas apparaître ici.

\newcommand{\lb}{[}
\newcommand{\rb}{]}
\newcommand{\lob}{\left]}
\newcommand{\rob}{\right[}

![Graphe de la jauge $\gamma(t) = \lob t-0.2, t+0.2 \rob ,$
$t \in \lb 0, 1 \rb .$](images/gauge-plot.pdf)

### TODO 
graphique d'une subdivision pointée, avec séparateurs en barres
verticales et $t_i$ en croix.

### Lemme de Cousin {.theorem}
Pour toute jauge $\gamma$ sur l'intervalle compact $I$, 
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
Soit ce procédé converge en un nombre fini d'étapes et forme
une subdivision pointée $\mathcal{D}$ de $I$, 
soit nous avons construit une infinité d'intervalles fermés $J_i$ 
emboités ($J_{i+1} \subset J_i$) de $I$ tels que pour tout 
$t \in J_i$, $J_i \not \subset \gamma(t)$.

Montrons que ce second scénario est impossible.
Comme les $J_i$ sont emboités, la collection
$\{J_i \; | \; i \in \N\}$ possède la
propriété de l'intersection finie. 
L'intervalle $I$ étant compact, cela implique qu'il existe un $t \in I$
tel que pour tout $i \in \N$, $t$ soit adhérent à $J_i$.
Les $J_i$ étant fermés, $t$ appartient à chaque $J_i$.
La longueur de $J_i$ étant divisée par deux à chaque incrément de $i$,
$\ell(J_i) = \ell(J_0) / 2^i$; 
comme $t_i \in J_i$, 
$J_i \subset [t_i - \ell(J_0) / 2^i, t_i + \ell(J_0) / 2^i]$.
Par conséquent, il existe un rang $i$ à partir duquel
$J_i \subset \gamma(t)$, ce qui contredit l'hypothèse de départ.

#### TODO -- Note

Si l'argument topologique peut être survolé, la procédure de dichotomie est
intéressante et peut être utilisé sur des exemples concrets, ça vaudrait le
coup de la faire "pour de vrai".

Au passage, il faut s'arranger pour "lemmatiser" le résultats "... et le 
processus termine en un nombre fini d'étapes" plus clairement.

### Intégrale de Henstock-Kurzweil sur un intervalle compact {.definition}
Une fonction $f:[a, b] \to \R$ est dite *intégrable 
(au sens de Henstock-Kurzweil)* s'il existe un réel $A$ tel
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

### Notation {.remark}

Comme dans le cas de l'intégrale de Riemann,
la première notation peut être étendue au cas où $b < a$; 
on définit alors l'intégrale de $a$ à $b$ en se ramenant 
au cas précédent, par
$$
\int_{a}^b f(t) \, dt := - \int_b^a f(t) \, dt.
$$
Lorsqu'on sera en présence de plusieurs intégrales (Newton, Riemann, etc.), 
on pourra préfixer l'intégrale par les lettres "HK" (pour Henstock-Kurzweil)
pour lever toute ambiguité:
$$
\mbox{HK-}\int_{[a, b]} f(t) \, dt.
$$

### Intégrale de Riemann et de Henstock-Kurzweil {.theorem}
Toute fonction $f:[a,b] \mapsto \R$ intégrable au sens de Riemann
est intégrable au sens de Henstock-Kurzweil et les deux intégrales coïncident.

### TODO -- Démonstration {.proof}

Passer par l'intermédiaires des jauges numériques ? Bof. Directement
avec de $\delta > 0$ uniforme à l'intervalle ouvert.

### Théorème fondamental du calcul {.theorem}
Si la fonction $f:[a, b] \to \R$ est dérivable 
sa dérivée $f'$ est intégrable sur $[a, b]$ et 
$$
[f]_a^b := f(b) - f(a) = \int_a^b f'(t) \, dt.
$$

### {.ante}
Le théorème fondamental du calcul peut être reformulé de la façon suivante:

### Intégrale de Riemann et de Henstock-Kurzweil {.corollary}
Toute fonction $f:[a,b] \mapsto \R$ intégrable au sens de Newton
est intégrable au sens de Henstock-Kurzweil et les deux intégrales coïncident.

**QUESTION** exfiltrer le "Straddle Lemma"? Ca sera probablement plus clair.
L'autre option est de splitter un cran plus avant la somme qui majore l'erreur
entre somme de Riemann et intégral ... à voir. Arf, ça ne marche pas, tss tss...

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
nous avons ainsi bien défini une fonction de jauge sur $[a, b]$.
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

### TODO

Expliquer que le choix de $\delta(t)$ du FTC "lisse" l'erreur faite sur
chaque terme de la somme de Riemann (proportionnellement à la largeur
du pas).

### Intégration de $x \mapsto e^x$ {.example}
La fonction $f: x \mapsto e^x$ est intégrable au sens de Newton sur 
tout intervalle compact $[a, b]$ 
puisqu'elle admet $x \mapsto e^x$ comme primitive.
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
fondamental du calcul. Dans cette preuve, nous avons montré que la précision
$\varepsilon$ était atteinte
si nous choisissions 
$\gamma(t) = \left]t-\delta(t), t+\delta(t)\right[$
où $\delta(t) > 0$ est tel que si $0 < |h| \leq \delta(t)$, alors
$$
\frac{|f(t+h) - f(t) - f'(t)h|}{|h|} \leq \frac{\varepsilon}{b-a}.
$$

Explicitons cette contrainte dans le cas de la fonction 
$x \mapsto e^x$. 
Cette fonction étant deux fois continûment différentiable, 
la formule de Taylor avec reste intégral nous fournit
$$
\begin{split}
\frac{|f(t+h) - f(t) - f'(t)h|}{|h|}
&= 
\frac{1}{|h|}\left| \int_t^{t+h}  f''(x) (t + h - x) \, dx \right| \\
&\leq 
\max \left\{ |f''(x)| \, | \, x \in [t-|h|, t+|h|]\right\} \times \frac{|h|}{2}.
\end{split}
$$
Le second membre de cette inégalité étant une fonction croissante de $|h|$, 
il nous suffit donc pour assurer l'inégalité souhaitée de choisir 
$\delta(t) > 0$ tel que
$$
\max \left\{ |f''(x)| \, | \, x \in [t-\delta(t), t+\delta(t)]\right\} \times \frac{\delta(t)}{2}
\leq \frac{\varepsilon}{b-a}.
$$

Dans ce cas précis, puisque $f''(x) = e^x$, lorsque $h \geq 0$ nous avons
$$
\max \left\{ |f''(x)| \, | \, x \in [t-\delta(t), t+\delta(t)]\right\}
= e^{t + \delta(t)}.
$$
L'inégalité à satisfaire prend donc la forme
$$
e^{t+\delta(t)} \times \frac{\delta(t)}{2} \leq \frac{\varepsilon}{b-a},
\; \mbox{ soit } \;
\delta(t) e^{\delta(t)}  \leq 2 e^{-t} \frac{\varepsilon}{b-a}.
$$
Or la fonction 
$\delta \in \left]0, +\infty\right[ \to \delta e^\delta \in \left]0, +\infty\right[$ est 
croissante et bijective; notons $W$ son inverse[^W]. 
Le plus grand $\delta(t)$ satisfaisant 
l'inégalité précédente est donc donné par
$$
\delta(t) = W \left(2e^{-t}\frac{\varepsilon}{b-a}\right).
$$
En conclusion: pour tout $[0, 1]$ et tout $\varepsilon > 0$, 
la jauge $\gamma$ définie sur $[a, b]$ par
$$
\gamma(t) = 
\left]
t - W \left( 2e^{-t}\frac{\varepsilon}{b-a}\right),
t + W \left( 2e^{-t}\frac{\varepsilon}{b-a}\right)
\right[
$$
est telle que pour toute subdivision pointée $\mathcal{D}$ de $[a, b]$ 
subordonnée à $\gamma$
$$
\left|
S(x \in [a, b] \mapsto e^x, \mathcal{D}) 
- 
\int_a^b e^x \, dx 
\right| 
\leq \varepsilon.
$$

[^W]: La notation $W$ est classique pour désigner [la fonction de Lambert](https://fr.wikipedia.org/wiki/Fonction_W_de_Lambert).

### TODO

représentation graphique de la jauge pour un (des ?) $\varepsilon$ 
bien choisis.


### TODO -- Intégration de $x \mapsto 1/\sqrt{x}$ {.example}

Considérons la fonction $f:[0,1] \to \R$ définie par
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
une jauge qui marche (note: au passage, en supposant $f$ deux fois diff on
peut en construire une explicitement, c'est un exercice intéressant en soi).
Tout est bon ici !

Variante/extension: autre valeur que $0$ en $0$, montrer que cela n'a aucun
impact.

Une stratégie intéressant consisterait à expliciter/construire une jauge
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

#### La singularité

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

Propriétés élementaires de l'intégrale
--------------------------------------------------------------------------------

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
d'intégrale nulle;
dans le cas contraire, on peut trouver une jauge $\gamma$ sur $[a, b]$ telle
que pour toute subdivision pointée $\mathcal{D}$ subordonnée à $\gamma$, on ait:
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

### Intégration par parties {.theorem}
Si les fonctions $f:[a, b] \to \R$ et $g: [a, b] \to \R$ sont dérivables,
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
Dans ce cas, le théorème fondamental du calcul appliqué à $(fg)'$ fournit
$$
\int_a^b (fg)'(t) \, dt
=
\int_a^b f'(t)g(t) \, dt + \int_a^b f(t)g'(t) \, dt
= [fg]_a^b,
$$
ce qui est le résultat recherché.

### TODO
Mentionner résultat plus général, avec juste $f$ intégrable (sous hyp plus
restrictives pour $g$ ?). Trouver ref ?

### Changement de variables {.theorem}
Si la fonction $f:[c, d] \to \R$ admet une primitive,
que la fonction $g:[a, b] \to \R$ est dérivable 
et que $g([a, b]) \subset [c, d]$, alors la fonction
$(f\circ g) g'$ est intégrable sur $[a, b]$ et
$$
\int_a^b f(g(t)) g'(t)\, dt = \int_{g(a)}^{g(b)} f(x) \, dx.
$$

### Démonstration {.proof}
Soit $h$ une primitive de $f$. La fonction $t \in [a, b] \mapsto h(g(t))$
a pour dérivée $h'(g(t))g'(t) = f(g(t)) g'(t)$. Par le théorème fondamental
du calcul on a donc d'une part
$$
\int_a^b f(g(t)) g'(t) \, dt
=
\left[t \mapsto h(g(t)) \right]_a^b = h(g(b)) -  h(g(a))
$$
et d'autre part
$$
\int_{g(a)}^{g(b)} f(x) \, dx = [h]_{g(a)}^{g(b)} = h(g(b)) -  h(g(a));
$$
les deux intégrales sont donc égales.


### Additivité {.proposition}
Si la fonction $f$ est définie et intégrable sur les intervalles compacts
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
Définissons la fonction $\gamma: [a, b] \to \R$ par:
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
Elles sont également subordonnées à $\gamma_1$ et $\gamma_2$ respectivement;
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
si $x \neq b$, alors $x \not \in \gamma(x)$;
par conséquent, si cet intervalle $I_i=[d_i, e_i]$ existe, 
alors $t_i = b$ et on peut remplacer le terme $(t_i, I_i)$ dans la subdivision
pointée $\mathcal{D}$ par $(b, [d_i, b])$ et $(b, [b, e_i])$ sans que
la somme de Riemann associée change 
(le terme $f(b) \ell([d_i, e_i])$ étant égal à 
$f(b) \ell([d_i, b]) + f(b) \ell([b, e_i])$).
La nouvelle subdivision $\mathcal{D}'$ ainsi construite vérifie quant à elle
l'hypothèse de non-chevauchement. Par conséquent l'inégalité
ci-dessus est satisfaite dans le cas général, ce qui conclut la preuve
de ce théorème.

### TODO

Présenter ce qui vient comme une réciproque de l'additivité.
Contextualiser le critère de Cauchy (valeur de l'intégrale inconnue)

### Critère d'intégrabilité de Cauchy {#CIC .theorem}
Une fonction $f: [a, b] \to \R$ est intégrable si et seulement si 
pour tout $\varepsilon > 0$ il existe une jauge $\gamma$ sur $[a, b]$ telle que 
pour tout couple de subdvisions pointées $\mathcal{D}$ et $\mathcal{D}'$
subordonnées à $\gamma$, on ait
$$
|S(f, \mathcal{D}) - S(f, \mathcal{D}')| \leq \varepsilon.
$$

### TODO -- Démonstration {.proof}
Si la fonction $f$ est intégrable, pour tout $\varepsilon > 0$, 
il existe une jauge $\gamma$ sur $[a, b]$ telle que pour tout couple de 
subdvisions pointées $\mathcal{D}$ et $\mathcal{D}'$ subordonnées à $\gamma$,
on ait
$$
|S(f, \mathcal{D}) - \int_a^b f(t) \, dt| \leq \frac{\varepsilon}{2}
\; \mbox{ et } \;
|S(f, \mathcal{D}') - \int_a^b f(t) \, dt| \leq \frac{\varepsilon}{2}.
$$
Par l'inégalité triangulaire, on a alors comme souhaité
$$
|S(f, \mathcal{D}) - S(f, \mathcal{D}')| \leq \varepsilon.
$$

Réciproquement, **TODO**

### TODO:

fusionner "Restriction" avec additivité ou au moins évoquer la relation
entre les deux résultats.

### Restriction {.theorem}

Si $f$ est intégrable sur l'intervalle compact  $[a, b]$, 
elle est intégrable sur tout intervalle compact $[c, d]$ 
inclus dans $[a, b]$.

### Démonstration {.proof}
Nous démontrons en détail le cas où $c = a$; le cas où $d =b$ se prouve de
façon similaire et le cas général se déduit facilement de ces deux cas
particuliers.

Soit $\varepsilon > 0$. Par le [critère d'intégrabilité de Cauchy](#CIC),
il existe une jauge $\gamma$ sur $[a, b]$ telle
que pour tout couple de subdvisions pointées $\mathcal{D}$ et $\mathcal{D}'$
subordonnées à $\gamma$, on ait
$$
|S(f, \mathcal{D}) - S(f, \mathcal{D}')| \leq \varepsilon.
$$
Considérons les restrictions $\gamma_1$ et $\gamma_2$ de $\gamma$ à $[a, d]$ et 
$[d, b]$ respectivement. 
Soient $\mathcal{D}_1$ et $\mathcal{D}_1'$ deux subdivisions pointées de 
$[a, d]$ subordonnées à $\gamma_1$;
si $\mathcal{D}_2$ est une subdivision de $[d, b]$ subordonnée à $\gamma_2$,
alors $\mathcal{D}_1 \cup \mathcal{D}_2$ et $\mathcal{D}_1 \cup \mathcal{D}_2'$
sont des subdvisions pointées de $[a, b]$ subordonnées à $\gamma$.
Par conséquent,
$$
|S(f, \mathcal{D}_1 \cup \mathcal{D}_2) 
- S(f, \mathcal{D}_1 \cup \mathcal{D}_2')|
\leq \varepsilon.
$$
Or
$S(f, \mathcal{D}_1 \cup \mathcal{D}_2) = S(f, \mathcal{D}_1) + S(f, \mathcal{D}_2)$
et $S(f, \mathcal{D}_1 \cup \mathcal{D}_2') = S(f, \mathcal{D}_1) + S(f, \mathcal{D}_2')$,
donc
$$
|S(f, \mathcal{D}_1) - S(f, \mathcal{D}_1)|
\leq \varepsilon,
$$
ce qui prouve l'intégrabilité de $f$ sur $[a, d]$
par le [critère d'intégrabilité de Cauchy](#CIC).

### Fonctions égales presque partout
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
nulle), alors elle est intégrable d'intégrale nulle.

Supposons dans un premier temps que $f$ soit bornée.
Alors, pour tout $\varepsilon > 0$, il existe un recouvrement de
$$
A = f^{-1}(\{0\}) = \{x \in [a, b] \, | \, f(x) \neq 0\}
$$ 
par une collection dénombrable
d'intervalles $I_i$ telle que $\sum_i \ell(I_i) \leq \varepsilon$.
Il est de plus possible de supposer les $I_i$ ouverts[^why-open].
Définissons la jauge $\gamma$ sur $[a, b]$ par
$$
\gamma(t) = I_i \, \mbox{ si } \, t \in I_i \;
(\mbox{et } \, t \not \in I_j \mbox{ quand } \, j \leq i).
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
Mais par construction les $J_j$ ne se chevauchent pas et sont
tous inclus dans un des intervalles $I_i$. On a donc
$$
\sum_j \ell(J_j) \leq  \sum_i \ell(I_i) \leq \varepsilon.
$$
Il suffit par conséquent de choisir un $\varepsilon$ suffisamment petit
initialement pour rendre la somme de Riemann associée arbitrairement petite;
$f$ est donc intégrable d'intégrale nulle.

[^why-open]: On peut trouver un recouvrement de $A$ par des
intervalles $J_i$ non nécessairement ouverts, tels que 
$\sum_i \ell(J_i) \leq \varepsilon/2$, puis remplacer chaque
$J_i$ par un intervalle $I_i$ ouvert de longueur double contenant $J_i$.

Si $f$ est non-bornée, on peut faire un démonstration similaire en
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


Intégration sur des intervalle non-bornés
--------------------------------------------------------------------------------

### TODO

Motiver la définition de l'intégrale sur un intervalle non borné,
disons $\left[0, +\infty\right[$
par l'étude de l'intégrale sur $[a, b]$ et "sautant" le dernier
terme de la somme de Riemann ? En exercice ? Bof.

### TODO

Voir ce qu'il est possible de dire au passage sur l'absence d'intégrale
impropre (théorème de Hake).

### Remarque {.anonymous}

La difficulté d'intégrer une fonction sur un intervalle non borné tel
que $\R$ n'est pas lié au concept de subdivision pointée, 
qui peut être généralisé pour comporter des intervalles non bornés,
mais au calcul de la somme de Riemann associée. 
En effet, toute subdivision pointée d'un intervalle non-borné comporte
nécessairement un ou deux éléments de la forme $(t, I)$ où $I$ est non-borné; 
la longueur $\ell(I)$ associée est alors infinie et la somme de Riemann
correspondante comporte alors un ou deux termes de la forme $f(t) \times \infty$;
elle donc potentiellement infinie, ou même indéfinie ...

Pour éviter cette difficulté technique, nous allons définir l'intégrale 
sur $\R$ à partir de subdivisions d'intervalles compacts, en exigant 
que celles-ci, en plus d'être suffisamment fines comme dans le cas des
intervalles bornés, soient basées sur un intervalle suffisamment grand.


### Intégrale sur un intervalle non borné {.definition}
Soit $I$ un intervalle fermé non borné de $\R$ de bornes $a$ et $b$[^inb].
Une fonction $f:I \to \R$ est dite *intégrable 
(au sens de Henstock-Kurzweil)* s'il existe un réel $A$ tel
que pour tout $\varepsilon > 0$ il existe une jauge $\gamma$ de $\R$ 
et un intervalle compact $K$ de $I$
tels que pour tout intervalle compact $[a, b]$ tel que $K \subset [a, b]$
et pour toute subdivision pointée $\mathcal{D}$ de $[a, b]$ 
subordonnée à $\gamma$, on ait
$|S(f, \mathcal{D}) - A| \leq \varepsilon$.
Le réel $A$ quand il existe est unique; il est appelé
*intégrale de $f$ sur $\R$* et noté
$$
\int_{a}^{b} f(t) \, dt
\, \mbox{ ou } \,
\int_I f(t) \, dt.
$$

[^inb]: 3 cas peuvent se présenter: $I = \left]-\infty, +\infty\right[ =\R$,
$I=\left]-\infty, b\right]$ ou $I=\left[a, +\infty\right[$ où $a, b\in \R$

### TODO: 

simplifier ce qui suit, inutilement compliqué.

### TODO: 

j'ai changé la définition ci-dessus, adapter la suite.

### TODO

Remarquer/Prouver que la définition ci-dessus "marche aussi" pour un
intervalle borné.

### Intégrale sur un intervalle fermé {.definition}
Une fonction $f:I \to \R$ définie sur un intervalle
fermé quelconque $I$ (borné ou non borné) est 
*intégrable (au sens de Henstock-Kurzweil)* si son prolongement
$g$ par zero en dehors de l'intervalle $I$ 
$$
g(x) = \left|
\begin{array}{rl}
f(x) & \mbox{si } \, x \in  I, \\
0 & \mbox{sinon.}
\end{array}
\right.
$$
est intégrable sur $\R$.
On définit alors
$$
\int_I f(t) \, dt := \int_{\R} g(t) \, dt.
$$

### Démonstration (cohérence des définitions) {.proof}

Il convient de vérifier que 
[la définition d'intégrale sur un intervalle fermé $I$][Intégrale sur un intervalle fermé] 
est cohérente avec 
[la définition d'intégrale sur $\R$][Intégrale sur $\R$]
(ce qui est direct) et aussi avec 
[la définition d'intégrale sur un intervalle compact][Intégrale sur un intervalle compact]
que nous avons utilisé jusqu'à présent.

Dans ce second cas, si la fonction $f:[c, d] \to \R$ est
[intégrable au sens de la définition originelle][Intégrale sur un intervalle compact],
et si l'on prend $r>0$ tel que $-r \leq c$ et 
$d \leq r$ et que l'on considère un intervalle
compact $[a, b]$ vérifiant $a \leq -r$ et $r \leq b$, on
a $[c, d] \subset [a, b]$. Par additivité de l'intégrale,
$$
\int_a^b g(t) \, dt  
= 
\int_a^c g(t) \, dt + \int_c^d g(t) \, dt + \int_d^b g(t) \, dt.
$$
Or sur $[a, c]$ et $[d, b]$, la fonction $g$ est nulle sauf peut-être en
$c$ et $b$ ; sur $[c, d]$, elle est égale à $f$. Par conséquent $g$
est intégrable sur $[a, b]$ et 
$$
\int_a^b g(t) \, dt
=
\int_c^d f(t) \, dt.
$$
On peut donc bien trouver une jauge $\gamma$ sur $[a, b]$ telle que toute 
subdivision $\mathcal{D}$ de $[a, b]$ subordonnée à $\gamma$ vérifie
$$
\left|S(f, \mathcal{D}) - \int_c^d f(t) \, dt \right| \leq
\varepsilon
$$

Réciproquement, si la fonction $f:[c, d] \to \R$ est
[intégrable au sens de la définition générale][Intégrale sur un intervalle fermé],
pour tout $r>0$ et $[a, b]$ tel que $a \leq -r$ et $r \leq b$, le prolongement
de $f$ par zéro est intégrable sur $[a, b]$. Il suffit de prendre $r$ tel
que $-r \leq c$ et $d \leq r$ et d'utiliser à nouveau 
[(la réciproque de) l'additivité de l'intégrale][Additivité] pour conclure
que $f$ est intégrable sur $[c, d]$ et que son intégrale est l'intégrale de
$g$.

### TODO

Existence et valeur de:

$$
\int_1^{+\infty} \frac{1}{t^2} \, dt
$$

### TODO

Rappel / généralisation des pptés enoncées pour les intervalles compacts.

Subdivisions Partielles
--------------------------------------------------------------------------------

### Subdivision pointée partielle {.definition}
Une *subdivision pointée partielle* de l'intervalle fermé $I = [a, b]$ 
de $\R$ est une famille finie 
$$
\{(t_i, I_i) \; | \; \; 0 \leq i \leq n-1\}
$$
où les $I_i$ sont des intervalles fermé de $[a, b]$ sans chevauchement
et $t_i \in I_i$ pour tout $i \in \{0, \dots, n-1\}.$
La somme de Riemann associée à la fonction $f:[a, b] \to \R$ 
et à la subdivision pointée partielle $\mathcal{D}$ de $[a, b]$ est 
la grandeur
$$
S(f, \mathcal{D}) = \sum_{(t, I) \in \mathcal{D}} f(t) \ell(I)
$$
Une subdivision pointée partielle $\mathcal{D}$ de l'intervalle fermé $[a, b]$ 
est *subordonnée à une jauge* $\gamma$ de $[a, b]$ si 
$$
(t, J) \in \mathcal{D} \, \Rightarrow \, J \subset \gamma(t). 
$$

### TODO - remarque

(autrement dit, c'est comme une subdivision pointée, sauf que l'on n'exige pas 
que les $I_i$ recouvrent $[a, b]$. Mettre en ante ?)



### Lemme de Henstock  {.theorem}
Soit $[a, b]$ un intervalle fermé de $\R$, 
$f$ une fonction intégrable sur $[a, b]$ et $\gamma$ une jauge sur $[a, b]$ 
telle que pour toute subdivision pointée $\mathcal{D}$ de $[a, b]$, 
on ait
$$
\left|S(f, \mathcal{D}) - \int_{[a, b]} f(t) \, dt\right| \leq \varepsilon.
$$
Alors pour tout subdivision pointée partielle $\mathcal{D} = \{(t_k, I_k)\}_k$
de $[a, b]$ subordonnée à $\gamma$, on a également
$$
\left|S(f, \mathcal{D}) - \sum_k \int_{I_k} f(t) \, dt\right| \leq \varepsilon.
$$


### Preuve du [lemme de Henstock][Lemme de Henstock]

Il existe une famille finie d'intervalles fermés $\{J_j\}$, 
$j = 1, \dots, m$ 
telle que l'union des familles $\{I_k\}$ et $\{J_j\}$ forment une subdivision
(complète) de $[a, b]$. 
Pour tout $\eta > 0$, 
sur chaque intervalle $J_j$, il existe une jauge $\gamma_j$ telle que si
$\mathcal{D}_j$ est une subdivision pointée de $J_j$ subordonnée à $\gamma_j$,
alors 
$$
\left|S(f, \mathcal{D}_j) - \int_{J_j} f(t) \, dt \right| \leq \eta.
$$
Si de plus on choisit $\mathcal{D}_j$ subordonnée à la restriction de $\gamma$
à $J_j$, alors $\mathcal{D} \cup \cup_j \mathcal{D}_j$ est une subdivision
pointée (totale) de $[a, b]$ subordonnée à $\gamma$.
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

Exercices
================================================================================

TODO
--------------------------------------------------------------------------------

Regarder exercices dans le Bartle ("A Modern Theory of Integration")

Intervalle {#e-int}
--------------------------------------------------------------------------------

Montrer qu'un sous-ensemble $I$ de $\R$ est un intervalle si et
seulement si il *est connexe par arcs*, c'est-à-dire si et seulement
si pour tout couple de points $x$ et $y$ de $I$ on peut trouver un
chemin de $I$ joignant $x$ à $y$, c'est-à-dire une fonction continue
$\phi:[0, 1] \to I$, telle que $\phi(0) = x$ et $\phi(1) = y$.

$\to$ [Solution](#s-int)

TODO -- Construction de Jauges {#e-jauge}
--------------------------------------------------------------------------------

**TODO:** faire construire "à la main" une jauge par dichotomie (exemple avec
jauge s'affinant pour "forcer" un tag et/ou variante avec jauge "faciles",
telles qu'on puisse trouver une jauge uniforme qui soit plus fine ? Et csq,
à savoir capacité à trouver une subdivision uniforme associée)

$\to$ [Solution](#s-jauge)

Subdivision pointées {#e-sp}
--------------------------------------------------------------------------------

Demander de construire à partir d'une subdivision une autre subdivision 
"aussi fine", de même somme de Riemann, mais avec les points tjs à gauche
ou à droite de l'intervalle.

$\to$ [Solution](#s-sp)

L'intégrale de Riemann est absolue {#e-abs}
--------------------------------------------------------------------------------

Montrer que l'intégrale de Riemman est absolue: 
si une fonction $f$ est intégrable au sens de Riemann, 
sa valeur absolue $|f|$ l'est également.

$\to$ [Solution](#s-abs)

TODO -- Un ensemble de Cantor {#e-cantor}
--------------------------------------------------------------------------------

Chaque nombre réel $x$ de $\left[0, 1\right[$ peut être représenté de façon
par un développement décimal de la forme noté noté $x=0.a_1a_2a_3\dots$
où $a_i \in \{0,1, \dots, 9\}$, une notation qui signifie que
$$
x = \sum_{i=1}^{+\infty} a_i 10^{-i}.
$$
Ce développement est unique si on lui impose d'être propre, 
c'est-à-dire qu'il n'y ait pas
de séquences infinie de nombres $9$ consécutifs[^wp].

[^wp]: Dans le cas contraire, on pourrait par exemple représenter $x=1/2$ comme
$0.5000\dots$ ou comme $0.4999\dots$.

On définit l'ensemble $A$ comme le sous-ensemble de $\left[0, 1\right[$
dont le développement décimal ne comporte que des nombres pairs.
Par exemple, $x=2/3 = 0.666\dots$ appartient à $A$, mais 
$x=\sqrt{2}/2 = 0.707\dots$ non.

**TODO:** faire qqchose du style "Si vous deviez 
"tirer un nombre au hasard dans $\left[0, 1\right[$", 
quelle serait les chances de tomber sur un nombre de $A$ ?".
Qui suppose de modéliser la séquence des $a_n$, supposé équiprobables,
indépendants, etc.? OK, why not mais est-on en état de relier ça à la
question 1. à ce stade ? Mmmmmmm ....

### Question 1

Montrer que l'ensemble $A$ est négligeable.

$\to$ [Solution](#s-cantor-1)

### Question 2

Montrer néanmoins que $A$ n'est pas dénombrable, 
mais a la "puissance du continu" 
(qu'il peut être mis en bijection avec $\R$ 
ou avec un intervalle de longueur non vide de $\R$, 
ce qui revient au même).

$\to$ [Solution](#s-cantor-2)

TODO -- Caractérisation des dérivées {#e-der}
--------------------------------------------------------------------------------

Identifier par les jauges si une fonction est une dérivée (cf papier).

$\to$ [Solution](#s-der)


Solution aux exercices
================================================================================

Intervalle {#s-int}
--------------------------------------------------------------------------------

Montrons tout d'abord que la condition est nécessaire. 
Supposons que $x$ et $y$ appartiennent à $I$ et que $x$ 
soit inférieur ou égal à $y$. Alors pour tout $t \in [0,1]$, 
$\phi(t) = (1-t) x + t y$ est un point intermédiaire entre $x$ et $y$,
et par conséquent, appartient à $I$. La fonction $\phi$ ainsi définie 
est clairement continue et vérifie $\phi(0) = x$ et $\phi(1) = y$; 
c'est donc un chemin de $I$ qui joint $x$ à $y$. Par conséquent,
$I$ est connexe par arcs.

Réciproquement, si $I$ est connexe par arcs et contient les points $x$
et $y$, tout chemin de $I$ qui joint $x$ et $y$, continu et à valeurs réelles,
vérifie le théorème des valeurs intermédiaires: pour toute valeur intermédiaire
$z$ entre $x$ et $y$, il existe donc un $t \in [0, 1]$ tel que $\phi(t) = z$.
Comme $\phi$ est à valeurs dans $I$, $z \in I$; l'ensemble $I$ est donc un 
intervalle de $\R$.

TODO -- Construction de Jauges {#s-jauge}
--------------------------------------------------------------------------------

TODO -- Subdivision pointées {#s-sp}
--------------------------------------------------------------------------------

L'intégrale de Riemann est absolue {#s-abs}
--------------------------------------------------------------------------------

Nous exploitons le [critère de Lebesgue pour l'intégrabilité au sens de Riemann][Critère de Lebesgue pour l'intégrabilité au sens de Riemann]: si $f$ est intégrable au sens de Riemann,
elle est bornée -- et donc $f$ également -- et continue presque partout
-- et donc $|f|$ également ($|f|$ est continue en tout point où
$f$ est continue comme composée de fonctions continues en un point). 
Par conséquent, $|f|$ est intégrable au sens de Riemann.

TODO -- Un ensemble de Cantor {#s-cantor}
--------------------------------------------------------------------------------

### Question 1 {#s-cantor-1}

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

### Question 2 {#s-cantor-2}

L'opération qui à $x=0.a_1a_2\dots \in A$ associe
$y=0.b_1b_2\dots$ où $b_i = a_i/2$ est une bijection
de $A$ sur $\left[0, 0.444\dots\right[ = \left[0, 4/9\right[$,
ce qui montre que $A$ à la puissance du continu (et donc n'est pas
dénombrable).

TODO -- Caractérisation des dérivées {#s-der}
--------------------------------------------------------------------------------

Références
================================================================================