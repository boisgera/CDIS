% Calcul Intégral IV

<!-- LaTeX Macros -->
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}
\newcommand{\ds}{\mathbin{\Delta}}

Objectifs
================================================================================

Cette section -- expérimentale -- s'efforce d'expliciter et de hiérarchiser
les acquis d'apprentissages associés au chapitre. 
Ces objectifs sont organisés en paliers :

($\bullet$) Fondamental ($\bullet\bullet$) Standard ($\bullet\!\bullet\!\bullet$) Avancé
($\circ$) Expert (non exigible)

Sauf mention particulière, la connaissance des démonstrations du document 
n'est pas exigible[^hp] ; les notions développées en annexe sont toutes hors-programme.

[^hp]: l'étude des démonstrations du cours peut toutefois 
contribuer à votre apprentissage, au même titre que la résolution 
d'exercices.



### Tribu

  - terminologie : tribu $\mathcal{A}$, ensemble mesurable, espace mesurable. ($\bullet$).

  - connaître : tribu $\mathcal{P}(X)$ des parties de $X$, tribu de Lebesgue $\mathcal{L}(\R^n)$ ($\bullet$).

  - savoir exploiter que si $A, B \in \mathcal{A}$, $A\cup B \in \mathcal{A}$, $A\cap B \in \mathcal{A}$ et
    $A\setminus B \in \mathcal{A}$ ($\bullet$).

  - savoir exploiter que si $A_k \in \mathcal{A}$, alors
    $\cup_{k=0}^{+\infty} A_k \in \mathcal{A}$ et 
    $\cap_{k=0}^{+\infty} A_k \in \mathcal{A}$ ($\bullet\bullet$).

  - plus généralement, savoir déterminer quand un ensemble, 
    produit par des opérations ensemblistes à partir d'ensembles de $\mathcal{A}$, 
    appartient à $\mathcal{A}$ ($\bullet\bullet$/$\bullet\!\bullet\!\bullet$).

  - savoir caractériser si une collection d'ensembles est une tribu ($\bullet\!\bullet\!\bullet$).

  - savoir que la raison d'être d'une tribu est d'être le domaine de définition d'une mesure ($\bullet$).

### Mesure

  - terminologie : mesure $\mu$, espace mesuré ($\bullet$).

  - connaître : mesures de Dirac, de comptage, de Lebesgue ($\bullet$).

  - savoir déterminer si une fonction est une mesure 
    ($\bullet\bullet$/$\bullet\!\bullet\!\bullet$).

  - savoir exploiter que les mesures sont nulles en zéro, additives et croissantes ($\bullet$).

  - savoir exploiter la $\sigma$-additivité des mesures ($\bullet\bullet$).

  - savoir calculer des mesures d'ensembles ($\bullet\bullet$/$\bullet\!\bullet\!\bullet$).

  - terminologie : ensemble $\mu$-négligeable, propriété vraie $\mu$-presque partout ($\bullet$).

  - savoir déterminer si un ensemble est $\mu$-négligeable ($\bullet\bullet$).

### Intégrale de fonctions positives

  - savoir : chaque mesure détermine une intégrale ($\bullet$).

  - terminologie : intégrale par rapport à $\mu$ ($\mu$-intégrale) ($\bullet$).

  - savoir : si $f\geq 0$, la $\mu$-intégrale de $f$ est définie $\leftrightarrow$ $f$ est $\mu$-mesurable ($\bullet$).

  - terminologie : fonction mesurable (ou $\mathcal{A}$-mesurable ou $\mu$-mesurable) ($\bullet\bullet$)

  - connaître les trois propriétés caractéristiques de la $\mu$-intégrale ($\bullet$).
 
  - terminologie : fonction étagée ($\bullet$)

  - savoir exploiter la forme $\sum_{k=1}^n y_k 1_{A_k}$ des fonctions étagées ($\bullet$)

  - savoir caractériser les fonctions étagées mesurables ($\bullet$).

  - savoir calculer la $\mu$-intégrale d'une fonction étagée $\mu$-mesurable ($\bullet$).

  - savoir que la limite simple de fonctions mesurables est mesurable ($\bullet\bullet$)

  - savoir exploiter le résultat d'approximation des fonctions mesurables par des fonctions étagées
    (en particulier pour montrer la mesurabilité d'une fonction)
    ($\bullet\bullet$) ; connaître la suite de fonctions étagées utilisée dans sa démonstration ($\bullet\!\bullet\!\bullet$).

  - savoir exploiter la propriété de convergence monotone pour calculer l'intégrale de
    fonctions mesurables ($\bullet\bullet$).

  - connaître la définition formelle de la $\mu$-intégrale (avec le sup des intégrales
    des fonctions étagées) ($\bullet\!\bullet\!\bullet$) ;
    savoir démontrer qu'avec cette définition les trois propriétés caractéristiques
    de l'intégrale sont bien vérifiées ($\circ$).

  - savoir à quelle condition l'intégrale d'une fonction est nulle (cf. positivité et nullité) ($\bullet\bullet$).

### Intégrale de fonction signées
  
  - terminologie : $\mu$-intégrale, $\mu$-intégrabilité ($\bullet$).

  - savoir : seule l'intégrale des fonctions signées qui sont mesurables est susceptible
    d'être définie ; mais cette intégrale peut être finie, infinie ou indéfinie ($\bullet$).

  - savoir : une fonction est intégrable si son intégrale est définie et
    réelle ($\bullet$).

  - calcul de l'intégrale d'une fonction $f$ à partir de celle de $f_+$ et $f_-$ ($\bullet$).

  - compétence : savoir transposer les résultats du calcul intégral 
    des fonctions positives au contexte des fonctions signées ($\bullet\bullet$).

  - savoir utiliser le théorème de convergence dominée ($\bullet\bullet$).

  - connaître le lien entre intégrale associée à la mesure de Lebesgue 
    et au sens de Henstock-Kurzweil dans $\R^n$ ($\bullet\bullet$).

Mesure
================================================================================

### Tribu et espace mesurable {.definition}
Une *tribu* (ou *$\sigma$-algèbre*) $\mathcal{A}$ sur un ensemble $X$ est une 
collection d'ensembles de $X$ contenant l'ensemble vide et fermé par passage 
au complémentaire et à l'union dénombrable[^fp] :

[^fp]: c'est-à-dire que ces opérations, 
appliquées à des ensembles de $\mathcal{A}$, produisent des ensembles qui
sont également dans $\mathcal{A}$.

  1. $\varnothing \in \mathcal{A}$.

  2. Si $A \in \mathcal{A}$, $A^c = X \setminus A \in \mathcal{A}$.

  3. Si pour tout $k \in \N$, $A_k \in \mathcal{A}$, alors
     $\cup_{k=0}^{+\infty} A_k \in \mathcal{A}.$

Un ensemble $A \in \mathcal{A}$ est dit *mesurable* 
(relativement à la tribu $\mathcal{A}$) ou *$\mathcal{A}$-mesurable*.
L'ensemble $X$ muni de $\mathcal{A}$ 
-- c'est-à-dire formellement la paire $(X,\mathcal{A})$ -- 
est un *espace mesurable*.

### Exemple -- Tribu de Lebesgue dans $\R^n$
Dans le chapitre "Calcul Intégral III" nous avons montré que les ensembles 
que nous avions alors qualifiés de "mesurables"[^rapp] avaient les propriétés 
caractéristiques d'une tribu. Elle est notée $\mathcal{L}(\R^n)$ et est 
appelée *tribu de Lebesgue* sur $\R^n$. Il est donc équivalent de dire
d'un ensemble qu'il est mesurable au sens du chapitre "Calcul Intégral III"
ou qu'il est $\mathcal{L}(\R^n)$-mesurable.

[^rapp]: c'est-à-dire les ensembles $A$ de $\R^n$ tels que pour tout pavé compact $P$ de 
$\R^n$, la fonction caractéristique $1_{A \cap P}$ est intégrable au sens de Henstock-Kurzweil.

### Exercice -- Ensemble des parties {.exercise}
Montrer que pour tout ensemble $X$, la collection $\mathcal{A} = \mathcal{P}(X)$
des parties (sous-ensembles) de $X$ est une tribu sur $X$.

### Exercice -- Ensembles fermés {.exercise}
La collection des ensembles fermés de $\R^n$ est-elle une tribu sur $\R^n$ ?

### Exercice -- Tribu née sous $X$ {.exercise}
Supposons que la collection $\mathcal{A}$ soit une tribu sur l'ensemble $X$ mais 
que $X$ soit inconnu. Comment peut-on déduire $X$ de la collection $\mathcal{A}$ ?

### Exercice -- Intersection de tribus {.exercise}
Montrer que pour tout ensemble $X$, l'intersection de deux tribus
$\mathcal{A}_1$ et $\mathcal{A}_2$ sur $X$ -- c'est-à-dire la collection 
$\mathcal{A}$ définie par
$\mathcal{A} = \{A \subset X \; | \; A \in \mathcal{A}_1 \mbox{ et } A \in \mathcal{A}_2\}$ 
-- est une tribu sur $X$. 

### Exercice -- Opérations ensemblistes {.exercise}
Montrer que si $A$ et $B$ appartiennent à une tribu $\mathcal{A}$, alors
$A \cup B$, $A \setminus B$ et $A \cap B$ appartiennent également à $\mathcal{A}$.

### Exercice -- Intersection dénombrable {.exercise}
Montrer que si pour tout $k \in \N$, $A_k \in \mathcal{A}$, alors
$\cap_{k=0}^{+\infty} A_k \in \mathcal{A}.$

### Mesure et espace mesuré {.definition}
Une *mesure* $\mu$ sur un espace mesurable $(X, \mathcal{A})$
est une fonction 
$$
\mu: \mathcal{A} \to [0, +\infty]
$$ 
telle que $\mu(\varnothing)= 0$ (*nullité en $0$*) et telle que pour toute suite
$(A_k)_{k\in \N}$ d'ensembles de $\mathcal{A}$ disjoints deux à deux, on ait
$$
\mu \left( \bigcup_{k=0}^{+\infty} A_k \right) = \sum_{k=0}^{+\infty} \mu(A_k) ;
$$
on dit que $\mu$ est *$\sigma$-additive* (on dit aussi *dénombrablement additive*).
L'ensemble $X$ muni de $\mathcal{A}$ et $\mu$ 
-- c'est-à-dire formellement le triplet $(X, \mathcal{A}, \mu)$ -- 
est un *espace mesuré*.

### Exercice -- Les mesures sont (finiment) additives {.exercise}
Vérifier que toute mesure $\mu$ sur $(X, \mathcal{A})$ est additive, 
c'est-à-dire que si les ensembles $A_0, A_1, A_2, \dots, A_n$ de $\mathcal{A}$
sont deux à deux disjoints, alors
$$
\mu \left( \bigcup_{k=0}^{n} A_k \right) = \sum_{k=0}^{n} \mu(A_k).
$$

### Exercice -- Monotonie {.exercise}
Vérifier que toute mesure est *croissante* (on dit aussi *monotone*), 
c'est-à-dire que si $A, B \in \mathcal{A}$
et $A \subset B$, alors $\mu(A) \leq \mu(B)$.

### Exercice -- Cas dégénéré {.exercise} 
Existe-t'il des fonctions $\mu: \mathcal{A} \to [0, +\infty]$ qui soient
$\sigma$-additives mais pas nulles en $0$ ?

### Exercice -- Ca commence par un $\mathbb{P}$ {.exercise}
Comment appelle-t'on une mesure $\mu$ sur $(X, \mathcal{A})$ telle que
$\mu(X) = 1$ ? Une fois que vous avez deviné, justifier la réponse.

### Exercice -- Trace d'une mesure  {.exercise}
Soit $\mu$ une mesure sur $(X, \mathcal{A})$. Montrer que pour tout 
$A \in \mathcal{A}$, la *trace* $\mu|_A$ de $\mu$ sur $A$, définie
comme
$$
\mu|_A: B \in \mathcal{A} \mapsto \mu(A \cap B)
$$ 
est également une mesure sur $(X, \mathcal{A})$.

### Exercice -- Somme de mesures {.exercise}
Montrer que la somme de deux mesures $\mu_1$ et $\mu_2$ sur un espace mesurable 
$(X, \mathcal{A})$ est une mesure sur $(X, \mathcal{A})$.

### Mesure de Lebesgue
La fonction $v$ qui a un ensemble $A \in \mathcal{L}(\R^n)$ associe
$$
v(A) = \left|
\begin{array}{cl}
\displaystyle \int 1_A(x) \, dx & \mbox{si $1_A$ est intégrable au sens de Henstock-Kurzweil,}\\
+\infty & \mbox{sinon.}
\end{array}
\right.
$$
est une mesure nommé *mesure de Lebesgue* sur $\R^n$.

### Démonstration {.proof}
La fonction $v$ est bien à valeurs dans $[0, +\infty]$ ; quand $A = \varnothing$,
$$
v(\varnothing) = \int 1_{\varnothing} (x) \, dx = \int 0 \, dx = 0.
$$

Reste à montrer la $\sigma$-additivité de $v$.
Soit $(A_k)_{k\in \N}$ une suite d'ensembles de $\mathcal{L}(\R^n)$ 
disjoints deux à deux. Trois cas uniquement peuvent se produirent :

  1. La somme $\sum_{k=0}^{+\infty} v(A_k)$ est finie.

  2. Pour tout $k \in \N$, $v(A_k) < +\infty$ mais $\sum_{k=0}^{+\infty} v(A_k) = +\infty$.

  3. Il existe un $k \in \N$ tel que $v(A_k) = +\infty$.

Posons 
$$A = \cup_{k=0}^{+\infty} A_k \; \mbox{ et } \; f_j = 1_{\cup_{k=0}^j A_k} = \sum_{k=0}^j 1_{A_k}.$$ 
La suite des $f_j$ est croissante, composée de fonctions mesurables et converge
simplement vers $1_A$.

 1. Dans le premier cas, comme $f_j = \sum_{k=0}^j 1_{A_k}$ que chaque 
    fonction caractéristique $1_{A_k}$ est intégrable, $f_j$ est intégrable.
    Par ailleurs,
    $$
    \int f_j(x) \, dx = \sum_{k=0}^j \int 1_{A_k}(x) \, dx = \sum_{k=0}^j v(A_k) \leq \sum_{k=0}^{+\infty} v(A_k) < +\infty.
    $$
    Par le théorème de convergence monotone, on a donc
    $$
    v(A) = \int 1_A(x) \, dx = \lim_{j \to +\infty} \int f_j(x) \, dx =  \sum_{k=0}^{+\infty} v(A_k).
    $$

 2. Dans le second cas, comme
    $$
    \sup_j \int f_j(x) \, dx = \sum_{k=0}^{+\infty} v(A_k) = + \infty,
    $$
    le théorème de convergence monotone nous affirme que $1_A$ n'est pas intégrable.
    Par définition de $v(A)$, on a donc $v(A) = +\infty$ et donc on a également
    $$
    v(A) = \sum_{k=0}^{+\infty} v(A_k).
    $$

 3. Dans le dernier cas, par le critère d'intégrabilité dominée, 
    si $v(A_k)=+\infty$, $f_k$ n'est pas intégrable et donc $1_A$ non plus,
    ce qui entraîne $v(A) = +\infty$. On a donc à nouveau
    $$
    v(A) = \sum_{k=0}^{+\infty} v(A_k).
    $$

Nous avons bien démontré la $\sigma$-additivité de $v$.

### Exercice -- Mesure de Lebesgue d'un pavé {.exercise}
Déterminer la mesure de Lebesgue du pavé compact 
$P = [a_1,b_1] \times \dots \times [a_n, b_n]$.

### Mesure de Dirac
Soit $X$ un ensemble et $\mathcal{A} = \mathcal{P}(X)$ l'ensemble des parties
de $X$ (la collection des sous-ensembles de $X$ : $A \in \mathcal{P}(X)$ si 
et seulement si $A \subset X$.)
Soit $x \in X$ ; on appelle *mesure de Dirac* en $x$ la fonction 
$\delta_x : \mathcal{P}(X) \to [0, +\infty]$ définie par
$$
\delta_x(A) = \left|
\begin{array}{rl}
1 & \mbox{si $x \in A$,} \\
0 & \mbox{sinon.}
\end{array}
\right. 
$$

### Exercice -- Démonstration {.exercise}
Montrer que les mesures de Dirac sont bien des mesures.

### Exercice -- Et en changeant de point de vue ? {.exercise}
Quand on considère $\delta_x(A)$ comme une fonction de $x$ à $A$ fixé,
qu'obtient-on ?

### Mesure de comptage
Soit $X$ un ensemble et $\mathcal{A} = \mathcal{P}(X)$ l'ensemble des parties
de $\R^n$. On appelle *mesure de comptage* sur $X$ la fonction 
$c : \mathcal{P}(X) \to [0, +\infty]$ définie par
$$
c(A) = \left|
\begin{array}{rl}
\mathrm{card}(A) & \mbox{si $A$ est fini} \\
+\infty & \mbox{sinon.}
\end{array}
\right. 
$$
La notation $\mathrm{card}(A)$ désigne le cardinal de $A$ -- c'est-à-dire dans
le cas d'un ensemble fini, le nombre d'éléments de $A$.

### Exercice -- Démonstration {.exercise}
Montrer que les mesures de comptage sont bien des mesures.

### Ensemble négligeable {.definition}
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré. Un ensemble $N \subset X$
est *négligeable* (ou *$\mu$-négligeable*) s'il existe un ensemble mesurable 
$A \in \mathcal{A}$ tel que $N \subset A$ et $\mu(A) = 0$.

### Presque partout {.definition}
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré. Une propriété $P$ dépendant 
d'un $x \in X$ est vraie *presque partout* (ou *$\mu$-presque partout*) 
si l’ensemble des éléments $x$ 
où elle est fausse est un ensemble $\mu$-négligeable.

### Exercice -- Négligeable pour la mesure de comptage {.exercise}
Caractériser les ensembles négligeables pour la mesure de comptage $c$.

### Exercice -- Négligeable pour la mesure de Dirac {.exercise}
Caractériser les ensembles négligeables pour la mesure de Dirac $\delta_x$.

### Exercice -- Négligeable et mesurable {.exercise}
Montrer qu'un ensemble mesurable est négligeable si et seulement si il
est de mesure nulle.

Intégrale
================================================================================

### Fonction mesurable
Soit $(X, \mathcal{A})$ un espace mesurable.
Une fonction $f: X \to [-\infty,+\infty]$  est *mesurable* 
(ou *$\mathcal{A}$-mesurable* 
pour lever toute ambiguité) 
si l'image réciproque 
de tout fermé (ou de tout ouvert) de $[-\infty,+\infty]$ par 
$f$ est un ensemble mesurable (qui appartient à $\mathcal{A}$).

### {.post}
Quand la tribu $\mathcal{A}$ est le domaine de définition d'une mesure $\mu$,
on trouvera également le terme *$\mu$-mesurable* utilisé pour désigner une
fonction $\mathcal{A}$-mesurable.

### {.remark .post}
Cette définition est directement applicable
si $f$ est à valeurs positives ($f(X) \subset [0, +\infty]$) ou finies
($f(X) \subset \R$), voire les deux simultanément 
($f(X) \subset \left[0, +\infty \right[$).

### Exercice -- Ensemble des parties de $X$ {.exercise}
Soit $X$ un ensemble et $\mathcal{A} = \mathcal{P}(X)$. A quelle condition
une fonction $f: X \to [-\infty, +\infty]$ est-elle $\mathcal{A}$-mesurable ?

### Exercice -- Fonction caractéristique {.exercise}
Soit $(X, \mathcal{A})$ un espace mesurable et $A$ un sous-ensemble de $X$.
A quelle condition la fonction $1_A: X \to \R$ est-elle mesurable ?

### Limite simple de fonctions mesurables
Soit $(X, \mathcal{A})$ un espace mesurable. 
Si les fonctions $f_k: X \to \left[-\infty, +\infty\right]$,
$k \in \N$, sont mesurables et convergent simplement vers $f$, 
alors $f$ est mesurable. 

### Démonstration {.proof}
Il suffit de prouver que l'image réciproque par $f$ de tout ouvert $U$ de 
$\left[-\infty, +\infty\right]$ appartient à $\mathcal{A}$.
Or $f(x) \in U$ si et seulement si $f_k(x) \in U$
pour $k$ assez grand, ce qui se traduit par la formule
$$
f^{-1}(U) = \bigcup_{j=0}^{+\infty} \bigcap_{k = j}^{+\infty} f_k^{-1}(U)
$$
qui établit que $f^{-1}(U)$ est un ensemble mesurable, comme union 
(dénombrable) d'intersections (dénombrable) d'ensembles mesurables.

### Fonction étagée
Une fonction $f: X \to [-\infty, +\infty]$ est *étagée* si et seulement
l'image de $X$ par $f$ ne comporte qu'un nombre fini de valeurs distinctes.

### Exercice -- Fonction étagée {.exercise}
Soit $(X, \mathcal{A})$ un espace mesurable. 
A quelle condition une fonction $f: X \to [-\infty, +\infty]$ qui ne prend 
qu'un nombre fini de valeurs est-elle $\mathcal{A}$-mesurable ?



### Fonction étagées mesurables
Soit $(X, \mathcal{A})$ un espace mesurable.
Une fonction $f: X \to \R$ est étagée et mesurable 
si et seulement s'il existe une collection finie d'ensembles mesurables
$A_1, \dots, A_{n} \in \mathcal{A}$ et de valeurs 
$y_1, \dots, y_{n} \in \R$ telles que
$$
f = \sum_{k=1}^{n} y_k 1_{A_k}. 
$$

### {.post}
La démonstration de ce résultat montre qu'il est possible d'être plus prescriptif 
si nécessaire sur les ensembles $A_k$ et les valeurs $y_k$ : 
une fonction est en effet étagée et mesurables si et seulement 
s'il existe une collection finie d'ensembles mesurable **disjoints**
et **non vides** $A_1, \dots, A_{n} \in \mathcal{A}$ et de valeurs 
**distinctes et non nulles**
$y_1, \dots, y_{n} \in \R$ telles que
$$
f = \sum_{k=1}^{n} y_k 1_{A_k}. 
$$

### Démonstration {.proof}
Soit $f: X \to \R$ une fonction étagée ;
il existe donc des réels $y_1, \dots, y_{n}$ distincts non nuls tels que
$f(X) \setminus \{0\}= \{y_1,\dots, y_{n-1}\}.$
On a alors
$$f = \sum_{k=1}^{n} y_k 1_{A_k} \, \mbox{ avec } \, A_k = f^{-1}(y_k).$$ 
Si de plus $f$ est mesurable, les singletons de $\R$ étant fermés, 
les ensembles $A_k$ sont nécessairement ($\mathcal{A}$-)mesurables.

Réciproquement, si $f$ est de la forme $f = \sum_{k=1}^{n} y_k 1_{A_k}$ où
les ensembles $A_k$ sont mesurables, il est clair que la fonction $f$ est étagée
car $f$ ne peut prendre comme valeurs que les sommes partielles des $y_k$, 
sommes qui sont en nombre fini. 
En considérant les ensembles 
-- mesurables -- $B_k$ définis par $B_1 = A_1$ et $B_{k+1}= A_{k+1} \setminus A_k$
on obtient une somme $\sum_k w_k 1_{B_k}$ du même type mais basée sur des 
ensembles mesurables disjoints $B_k$. En faisant l'union $C_j$ des $B_k$ qui correspondent à
des valeurs $z_j = w_k$ identiques, on peut de plus s'assurer d'avoir une somme
de la forme $f = \sum_j z_j 1_{C_j}$ où les valeurs $z_j$ sont distinctes et les $C_j$ sont
mesurables et non vides. 
Le cas échéant, si l'un des $z_j$ est nul, on peut même omettre le terme correspondant de la somme.
Il devient maintenant clair que $f$ est également mesurable : si $U$ est un
ensemble ouvert de $\R$ (l'argument vaut en fait pour n'importe quel ensemble), 
l'image réciproque de $U$ par $f$ est l'union
d'une sous-collection des $C_j$ ($C_j$ étant inclus dans la collection 
si et seulement si $z_j \in A$)
et si $0 \in U$, de $X \setminus \cup_j C_j$.

### Approximation par des fonctions étagées positives {.theorem}
Soit $(X, \mathcal{A})$ un espace mesurable. 
Soit $f: X \to [0, +\infty]$ une fonction mesurable positive. 
Il existe une suite croissante de fonctions 
étagées mesurables positives $f_k : X \to \left[0, +\infty\right[$ (à valeurs
finies) convergeant simplement vers $f$.
$$
0 \leq f_0(x) \leq f_1(x) \leq \dots \leq f_k(x) \to f(x)
$$

### Démonstration {.proof}
Soit $\varepsilon_k \geq 0$ une suite de valeurs réelles positives.
La suite des fonctions $f_k$ définies par $f_0=0$, puis
$$
f_{k+1} = f_{k} + \varepsilon_k 1_{E_k} \, \mbox{ où } \,
E_k = \{x \in X \, | \, f(x) \geq f_k(x) + \varepsilon_k\}
$$
est croissante et composée de fonctions étagées positives finies.

![Approximation de la fonction 
$f : x \in [0,\pi] \mapsto \sin x$ au moyen des fonctions étagées $f_k$ associées
à la suite $\varepsilon_k = 1.25/(k+1)$.](images/étagées.py)

De plus, on peut prouver par récurrence que ces fonctions $f_k$ sont 
mesurables. En effet, $f_0$ est évidemment mesurable (et étagée) ;
supposons que $f_k$ soit mesurable (et étagée), et donc de la 
forme $f_k = \sum_{j=1}^{n}y_j 1_{A_j}$ où les $A_j$ sont mesurables,
non vides, disjoints et $0 < y_1 < y_1 < \dots < y_{n} < +\infty$. 
Si l'on pose $y_0 = 0$ et $A_0 = X \setminus \cup_{j=1}^n A_j$, 
on a donc
$$
\begin{split}
E_k &= \{x \in X \; | \; f(x) \geq f_k(x) + \varepsilon_k\} \\
&= \bigcup_{j=0}^{n} \{x \in A_j \; | \; f(x) \geq f_k(x) + \varepsilon_k\} \\
&= \bigcup_{j=0}^{n} \{x \in A_j \; | \; f(x) \geq y_j + \varepsilon_k\} \\
&= \bigcup_{j=0}^{n} f^{-1}([y_j+\varepsilon_k,+\infty]) \cap A_j.
\end{split}
$$
La fonction $f$ étant mesurable, chaque ensemble $f^{-1}([y_j+\varepsilon_k,+\infty])$
est mesurable ; l'ensemble $E_k$ est donc mesurable comme union finie d'intersections
finies d'ensembles mesurables. La fonction $f_{k+1} = f_k + \varepsilon_k 1_{E_k}$
est donc mesurable (et étagée).


Si la suite $\varepsilon_k$ est choisie telle que
$$
\lim_{k\to +\infty} \varepsilon_k  = 0 
\; \mbox{ et } \;
\sum_{k=0}^{+\infty} \varepsilon_k = +\infty,
$$
alors la suite des $f_k(x)$ converge vers $f(x)$ pour tout $x \in X$. 

### Exercice -- Trace de fonction {.exercise}
Soient $f: X \to [0, +\infty]$ une fonction mesurable positive
(à valeurs finies ou infinies) et soit $A \in \mathcal{A}$.
Montrer que $1_A f$ est mesurable.

### Exercice -- Somme de fonctions {.exercise}
Soient $f, g : X \to [0, +\infty]$ deux fonctions mesurables positives
(à valeurs finies ou infinies). Montrer que $f+g$ est mesurable.

### Composition par une fonction continue
Soit $(X, \mathcal{A})$ un espace mesurable.
Si la fonction $f: X \to [-\infty, +\infty]$ est mesurable et
la fonction $h : [-\infty, +\infty] \to [-\infty,+\infty]$ est continue, 
la function composée $h \circ f$ est mesurable. 

### Démonstration {.proof}
Pour tout ouvert $U$ de $[-\infty, +\infty]$, l'image réciproque de 
$U$ par $h$ est un ouvert de $[-\infty, +\infty]$ et comme 
$f$ est mesurable, l'image réciproque de cet ensemble par $f$ est un ensemble
mesurable. La fonction composée $h \circ f$ est donc mesurable.

### Approximation par des fonctions étagées
Soit $(X, \mathcal{A})$ un espace mesurable. 
Soit $f: X \to [-\infty, +\infty]$ une fonction mesurable. 
Il existe une suite de fonctions 
étagées mesurables $f_k : X \to \left[0, +\infty\right[$ (à valeurs
finies) dont la suite des valeurs absolues $|f_k|$ est croissante 
$$
0 \leq |f_0| \leq \cdots \leq |f_k| \leq |f_{k+1}| \leq \cdots
$$
et qui convergent simplement vers $f$.

### Démonstration {.proof}
Les fonctions $f_+ = \max(f, 0)$ et $f_- = - \min(f, 0)$ sont mesurables
comme composées de fonctions mesurables et de fonctions continues.
Elle sont également positives, telles que $f = f_+ - f_-$ et $|f| = f_+ + f_-$. 
Il existe donc deux suites croissantes de fonctions $f_{k+}$ et $f_{k-}$ 
de fonctions étagées mesurables positives telles $f_{k+} \to f_+$ et 
$f_{k-} \to f_-$ et donc $f_k := f_{k+} - f_{k-} \to f$ quand $k \to +\infty$.
Par construction, $|f_{k}| = f_{k+} + f_{k-}$ est également croissante comme
somme de deux suites croissantes. 

### Exercice -- Calculs et infinis {.exercise}
Quand $f, g$ sont deux fonctions $X \to [-\infty, +\infty]$, 
les fonctions $f+g$, $fg$ et $\max(f,g)$ sont-elles bien définies ?

### Exercice -- Combinaison linéaire {.exercise}
Soit $\lambda \in \R$ et soient $f, g : X \to \left[0, +\infty\right[$ 
deux fonctions mesurables à valeurs finies. Montrer que les fonctions
$\lambda f$ et $f+g$ sont mesurables.

### Intégrale d'une fonction positive -- Propriétés caractéristiques {#carac}
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré. *L'intégrale (de Lebesgue)
par rapport à la mesure $\mu$* (ou *$\mu$-intégrale*) est l'unique application 
qui à toute fonction mesurable positive $f : X \to [0, +\infty]$ associe la 
grandeur notée
$$
\int f\mu = \int_X f(x) \, \mu(dx) \in [0, +\infty]
$$
et qui est caractérisée par

 1. *Intégrale et mesure:* pour tout ensemble $A \in \mathcal{A}$,
    $$
    \int 1_A \, \mu = \mu(A).
    $$

 2. *Linéarité :* si $\lambda \in \left]0, +\infty\right[$ et $f, g: X \to [0, +\infty]$
    sont mesurables, alors 
    $$
    \int (\lambda f) \, \mu  = \lambda \int f \, \mu
    \; \mbox{ et } \;
    \int (f+g) \, \mu = \int f \, \mu + \int g \, \mu.
    $$

 3. *Convergence monotone :* si la suite de fonctions mesurables $f_n:X \to [0, +\infty]$ est croissante 
    et converge simplement vers $f$, alors
    $$
    \int f \, \mu = \lim_{n \to +\infty} \int f_n \, \mu.
    $$

### {.post}
La construction explicite de l'intégrale de Lebesgue associée à la mesure $\mu$
-- construction qui complète l'approche descriptive ci-dessus --
sera donnée dans le reste de cette section. La preuve que l'intégrale ainsi 
construite satisfait bien les trois propriétés caractéristiques ci-dessus 
sera donnée dans la section suivante. 

### Exercice -- Intégrale et mesures de Dirac {.exercise}
Soit $x \in \R$ et $f:\R \to [0, +\infty]$. Sachant que 
$f$ est limite simple d'une suite croissante de fonctions étagées
$f_k : \R \to \left[0, +\infty\right[$, en déduire, en exploitant
les propriétés caractéristiques de l'intégrale, la valeur de
$$
\int f \, \delta_x = \int_{\R} f(y) \, \delta_x(dy).
$$

### Intégrale d'une fonction signée
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré. 
Soit $f : X \to [-\infty, +\infty]$ une fonction mesurable.
*L'intégrale (de Lebesgue) de $f$ par rapport à la mesure $\mu$* 
(où *$\mu$-intégrale*) 
est définie si au moins l'une des intégrales des fonctions positives
$$
f_+ := \max(f, 0) \; \mbox{ et } f_- := -\min(f, 0) \;
$$
est finie. On définit alors l'intégrale de $f$ par rapport à $\mu$ comme
$$
\int f \mu = \int_X f(x) \, \mu(dx) 
:= \int f_+ \, \mu - \int f_- \, \mu \in [-\infty, +\infty].
$$
On dit que $f$ est *intégrable* (par rapport à $\mu$) ou *$\mu$-intégrable* 
si les intégrales de $f_+$ et de $f_-$ sont toutes les deux finies ou, 
ce qui revient au même, si l'intégrale de $f$ est définie et réelle :
$$
\int f \mu = \int_X f(x) \, \mu(dx) \in \R.
$$

### Exercice -- Absolue intégrabilité {.exercise}
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré. Montrer que si $f: X \to [-\infty,+\infty]$
est intégrable alors $|f|$ est également intégrable.

### Exercice -- Fonctions étagées {.exercise}
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré et soient $A_1, \dots, A_n$ 
des ensemble mesurables disjoints non vides et 
$y_1, \dots, y_{n-1} \in [-\infty, +\infty] \setminus \{0\}$. 
A quelle condition la fonction
$$
f = \sum_{k=1}^n y_k 1_{A_k}
$$
est-elle intégrable ? Quelle est alors la valeur de son intégrale ?

### Intégrales finies, infinies et indéfinies {.post}
Une fonction positive peut avoir une intégrale bien définie (finie ou infinie) 
-- il faut et il suffit qu'elle soit mesurable -- sans être pour autant 
intégrable. Elle est intégrable si et seulement si elle est mesurable et que 
son intégrale est finie. 

Par contre, dans le cadre des fonctions signées, une fonction mesurable
peut avoir une intégrale indéfinie.
En effet, même si l'on peut définir
$$
\int f_+\mu \; \mbox{ et } \; \int f_- \mu
$$
dès que $f$ est mesurable, il est possible que ces deux intégrales soient égales
à $+\infty$ ; il n'y a alors pas de façon "raisonnable"
de définir la différence des deux grandeurs[^tbh].

[^tbh]: sauf à introduire un nouveau nombre "indéfini" $\bot$, 
absorbant pour l'addition, tel que $\bot = +\infty - \infty$
(le [NaN ou *not-a-number* des numériciens](https://en.wikipedia.org/wiki/NaN) 
est un concept très proche). Mais nous n'allons pas explorer cette piste ici.

### Exercice {.exercise}
Construire une fonction $f:\R \to \R$ mesurable par rapport à la tribu de 
Lebesgue $\mathcal{L}(\R)$ mais dont l'intégrale n'est pas définie par rapport à
la mesure de Lebesgue $v$ (ni finie ni infinie).


### Intégrale de Lebesgue et de Henstock-Kurzweil {.theorem}
Soit $f: \R^n \to \R$. La fonction $f$ est intégrable
par rapport à la mesure de Lebesgue $v$ si et seulement si 
$f$ est absolument intégrable ($f$ et $|f|$ sont intégrables) 
pour l'intégrale de Henstock-Kurzweil. Dans ce cas, les
deux intégrales sont égales :
$$
\int_{\R^n} f(x) \, v(dx) = \int_{\R^n} f(x) \, dx.
$$

### Démonstration {.proof}
Par construction, la fonction $f$ est intégrable par rapport à la mesure de 
Lebesgue $v$ si et seulement si les fonctions $f_+ = \max(f, 0)$ et 
$f_- = -\min(f, 0)$ sont intégrables par rapport à $v$. Comme
$$
f_+ = \frac{f+|f|}{2}, \, f_- = \frac{f - |f|}{2} \; \mbox{ et } \;
f = f_+ - f_-, \, |f| = f_+ + f_-,
$$
les fonctions $f_+$ et $f_-$ sont HK-intégrables si et seulement 
si $f$ et $|f|$ sont HK-intégrables, c'est-à-dire si et seulement
si $f$ est absolument HK-intégrable. Il nous suffit donc de démontrer le
résultat pour les fonctions positives.

Remarquons qu'une fonction étagée positive
$$
g = \sum_{k=1}^{n} y_k 1_{A_k}
$$
où les ensembles $A_1, \dots, A_{n} \in \mathcal{A}$ sont disjoints,
et $y_1, \dots, y_{n} \in \left]0, +\infty\right[$ est $v$-intégrable
si et seulement si $v(A_k) < +\infty$ pour tout $k$. 
Par définition de la mesure de Lebesgue $v$, c'est équivalent à l'HK-intégrabilité 
de chaque $1_{A_k}$ et donc de $g$ ; 
l'intégrale de $g$ par rapport à $v$ vaut alors
$$
\int g\, v =
\sum_{k=1}^n y_k \, v(A_k)
=\sum_{k=1} y_k \int 1_{A_k}(x) \, dx
= \int \sum_{k=1} y_k 1_{A_k}(x) \, dx
=\int g(x) \, dx.
$$

Si une fonction $f$ positive est $v$-intégrable, elle est la 
limite simple d'une suite croissante telles fonctions étagées positives et 
$v$-intégrables à valeurs finies et son intégrale par rapport à $v$ est la limite
des intégrales par rapport à $v$ des fonctions étagées. D'après
le résultat précédente, elle est donc la limite des intégrales au sens de
Henstock-Kurzweil de ces fonctions, qui, d'après le résultat des convergence
monotone de l'intégrale de Henstock-Kurzweil, converge vers l'intégrale de
Henstock-Kurzweil de $f$. Réciproquement, si $f$ est HK-intégrable, elle
est mesurable -- mesurable au sens de Henstock-Kurzweil et donc par le critère 
de l'image réciproque, également $\mathcal{L}(\R)$-mesurable --
et le même procédé d'approximation par une suite croissante de fonctions étagées
positives est donc applicable. Les théorèmes de convergence monotone, 
pour l'intégrale de Henstock-Kurzweil et pour l'intégrale associée à $v$, 
permettent alors de conclure.

### {.ante}
[Les propriétés caractéristiques](#carac) que nous souhaitons obtenir 
pour l'intégrale par rapport à la mesure $\mu$ ne nous laissent 
pas le choix sur la façon de procéder. 
Le lien entre intégrale et mesure d'une part et la linéarité
de l'intégrale imposent la façon de calculer l'intégrale de fonctions
étagées mesurables positives (à valeurs finies),
puis la propriété de convergence monotone détermine de façon unique 
l'intégrale des fonctions mesurables positives (à valeurs finies ou infinies).

### Intégrale d'une fonction étagée positive {.definition}
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré et 
$f: X \to \left[0, +\infty\right[$ une fonction étagée positive et mesurable,
de la forme
$$f = \sum_{k=1}^{n} y_k 1_{A_k}$$
où les ensembles $A_1, \dots, A_{n}$ sont mesurables ($\in \mathcal{A}$) et
$y_1, \dots, y_{n} \in \left]0, +\infty\right[$. Alors on définit l'intégrale
de $f$ par rapport à $\mu$ comme
$$
\int f \, \mu := \sum_{k=1}^{n} y_k \, \mu(A_k).
$$

### Intégrale d'une fonction positive
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré et 
$f: X \to [0, +\infty]$ une fonction mesurable.
Soit $\mathcal{F}(f)$ la collection des fonctions étagées mesurables 
positives (à valeurs finies) qui soient inférieures à $f$.
On appelle *intégrale de Lebesgue de $f$ relativement à la mesure $\mu$*
la grandeur positive (finie ou infinie)
$$
\int f \, \mu := \int_X f(x) \, \mu(dx) := \sup_{g \in \mathcal{F}(f)} \int g \, \mu.
$$

### {.post}
On pourra se convaincre que cette définition de l'intégrale est bien la seule
possible si l'on souhaite se doter d'une intégrale ayant la propriété de 
convergence monotone[^pro].

[^pro]: En effet, dans ce cas, 
comme pour toute fonction mesurable $f: X \to [0, +\infty]$,
il existe une suite croissante de fonctions étagées mesurables positives 
$f_k : X \to \left[0, +\infty\right[$ convergeant 
simplement vers $f$, notre définition de l'intégrale doit nécessairement vérifier
$$
\int f \mu \leq \sup_{g \in \mathcal{F}(f)} \int g \mu.
$$
Réciproquement, si $g_k: X \to \left[0, +\infty\right[$ est une suite 
de fonctions étagées mesurables positives (à valeurs finies)
inférieures à $f$ telles que
$$
\lim_{k\to+\infty} \int g_k \, \mu =  \sup_{g \in \mathcal{F}(f)} \int g \, \mu,
$$
alors la suite $h_k = \max(g_0,\dots, g_k, f_k)$ est une suite croissante 
de fonctions étagées mesurables positives (à valeurs finies) convergeant
vers $f$ mais supérieures à $g_k$ et vérifiant donc nécessairement
$$
\int f \, \mu = \lim_{k\to+\infty} \int h_k \, \mu \geq \sup_{g \in \mathcal{F}(f)} \int g \, \mu.
$$

Propriétés de l'intégrale
================================================================================

### {.ante .remark}
On mettra l'accent dans cette section sur les propriétés de l'intégrale de
fonctions positives ; les propriétés correspondantes de l'intégrale 
de fonctions signées s'en déduisent simplement.

Nous démontrons tout d'abord que l'intégrale que nous avons construite
satisfait bien [les propriétés caractéristiques souhaitées](#carac), en commençant
-- après l'énoncé du lemme de croissance -- par
le lien entre mesure d'un ensemble et intégrale de sa fonction
caractéristique.

### Lemme de croissance {#lemme-croissance}
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré et
$g, h: X \to \left[0, +\infty\right[$ deux fonction mesurables telles 
que $g\leq h$. Alors
$$
\int g \mu \leq \int h \mu.
$$

### Démonstration {.proof}
L'inclusion $\mathcal{F}(g) \subset \mathcal{F}(h)$ découle des hypothèses,
en conséquence,
$$
\sup_{k \in \mathcal{F}(g)} \int k\mu \leq \sup_{k \in \mathcal{F}(h)}  \int k\mu,
$$
ce qui est l'égalité entre intégrales souhaitée.

### Intégrale et mesure
Pour tout ensemble $A \in \mathcal{A}$, 
$$
\int_X 1_A (x) \mu(dx) = \mu(A).
$$

### Démonstration {.proof}
La fonction caractéristique $1_A$ est mesurable, positive et inférieure à $1_A$. 
C'est de toute évidence la plus grande fonction ayant toute ces propriétés,
donc par [le lemme de croissance](#lemme-croissance),
$$
\sup_{g \in \mathcal{F}(1_A)} \int g \mu = \mu(A).
$$

### Théorème de convergence monotone {.theorem #TCM}
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré et
$f_k: X \to [0, +\infty]$, $k \in \N$, une suite croissante de fonctions 
mesurables et positives ; pour tout $x \in X$,
$$
0 \leq f_0(x) \leq \dots \leq f_{k}(x) \leq f_{k+1}(x) \leq \cdots
$$
La limite simple $f: X \to [0, +\infty]$ des $f_k$,
telle que pour tout $x \in X$,
$$
f_k(x) \to f(x) \mbox{ quand } k \to +\infty,
$$
est mesurable et
$$
\lim_{k \to +\infty} \int f_k \mu = \int f \mu.
$$

### Démonstration {.proof}
La fonction $f$ est mesurable comme limite simple de fonctions mesurables.
Par [le lemme de croissance](#lemme-croissance),
$$
\int f_0 \mu \leq \dots \leq \int f_k \mu \leq \int f_{k+1} \mu \leq \cdots \leq \int f \mu
$$
et donc
$$
\lim_{k\to+\infty} \int f_k\mu \leq \int f\mu.
$$

Soit $g: X \to \left[0, +\infty\right[$ une fonction inférieure à $f$ qui
soit étagée et mesurable, c'est-à-dire de la forme
$$
g = \sum_{j=0}^{n-1} y_j 1_{A_j}
$$
avec $y_j \in \left[0, +\infty\right[$ et $A_j$ mesurable.
Soit $t \in \left[0, 1\right[$ ; comme la suite des $f_k$ est croissante et 
converge simplement vers $f$, les ensembles
$E_k = \{x \in X \; | \; f_k(x) \geq t g(x) \}$
vérifient
$$
E_0 \subset \cdots \subset E_k \subset \cdots 
\; \mbox{ et } \;
\bigcup_{k=0}^{+\infty} E_k = X.
$$
Les $f_k$ et $g$ étant mesurables, les ensembles $E_k$ sont mesurables.
On a 
$$
\int f_k \mu \geq \int t g 1_{E_k} \mu = 
\int t \sum_{j=0}^{n-1} y_j 1_{A_j} 1_{E_k} \mu
=
t\sum_{j=0}^{n-1} y_j \mu(A_j \cap E_k).
$$
Comme $\cup_{k=0}^{+\infty} A_j \cap E_k = A_j$, 
par [le théorème de continuité monotone (cf annexe)](#cont-monot),
$$
\lim_{k\to +\infty} \int f_k \mu \geq 
t\lim_{k\to +\infty} \sum_{j=0}^{n-1} y_j \mu(A_j \cap E_k) = 
t \left(\sum_{j=0}^{n-1} y_j \mu(A_j)\right) = t \int g\mu. 
$$
Cette inégalité étant valable pour tout $t \in \left[0, 1\right[$
et pour toute fonction positive étagée et mesurable $g$ inférieure à $f$, 
on en déduit
$$
\lim_{k\to +\infty} \int f_k \mu \geq \sup_{g \in \mathcal{F}(f)}\int g\mu
= \int f\mu.
$$

### Linéarité {.theorem #lin}
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré.
L'intégrale par rapport à $\mu$ de fonctions mesurables positives 
(à valeurs finies ou infinies) est homogène et additive :
si $\lambda \in \left[0, +\infty\right[$ et $f, g: X \to [0, +\infty]$ sont deux
applications $\mu$-mesurables,  
$$
\int (\lambda f) \mu = \lambda \int f\mu
\; \mbox{ et } \;
\int (f + g) \mu = \int f \mu + \int g \mu.
$$

### Démonstration {.proof}
Soit $f_k, g_k: X \to \left[0, +\infty\right[$ une paire de suites croissantes 
de fonctions étagées, mesurables et convergeant simplement vers $f$ et $g$
respectivement. On peut se convaincre sans difficultés que l'intégrale
des fonctions étagées et mesurables est additive et homogène et donc que
$$
\int (\lambda f_k) \mu = \lambda \int f_k\mu
\; \mbox{ et } \;
\int (f_k + g_k) \mu = \int f_k \mu + \int g_k \mu.
$$
Comme les suites $\lambda f_k$ et $f_k+g_k$ sont croissantes et 
convergent simplement vers $\lambda f$ et $f+g$ respectivement, 
par [le théorème de convergence monotone](#TCM) on en déduit
les égalités cherchées.

### Positivité et nullité {.theorem #pos}
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré 
et $f: X \to [0, +\infty]$ une fonction mesurable.
L'intégrale de $f$ par rapport à $\mu$ est positive ; 
elle est nulle si et seulement si
$f$ est nulle $\mu$-presque partout :
$$
\int f\mu = 0 \; \Leftrightarrow \; \mu(\{x \in X \; | \; f(x) > 0\}) = 0.
$$

### {.remark}
Notons que comme l'ensemble 
$\{x \in X \; | \; f(x) > 0\}$ -- c'est-à-dire $f^{-1}(\left]0, +\infty\right])$ -- 
est mesurable par construction, "négligeable" est bien équivalent à "de mesure nulle" ici.

### Démonstration {.proof}
La positivité est évidente par construction.
Si $f$ est nulle presque partout, comme pour toute fonction $g$ positive,
mesurable et étagée inférieure à $f$ et tout $y \in \left[0, +\infty\right[$, 
soit $y =0$, soit
$$
g^{-1}(y) \subset f^{-1}(\left]0,+\infty \right]),
$$
et donc
$$
\mu(g^{-1}(y)) \leq \mu(f^{-1}(\left]0,+\infty \right])) = 0,
$$
l'intégrale de $g$ par rapport à $\mu$ vérifie
$$
\int g \mu = \sum_{y \in \left[0, +\infty\right[} y \times \mu(g^{-1}(y)) = 0.
$$
Par conséquent,
$$
\int f \mu = \sup_{g \in \mathcal{F}(f)} \int g \mu = 0.
$$
Réciproquement, si la fonction $f$ n'est pas nulle $\mu$-presque partout, 
c'est-à-dire si $\mu(f^{-1}(\left]0, +\infty\right])) \neq 0$,
alors il existe nécessairement un $n \in \N$ tel que
$$
\mu(f^{-1}([2^{-n}, +\infty]))  > 0.
$$
En effet, les ensembles $f^{-1}\left([2^{-n}, +\infty]\right)$
forment une suite croissante d'ensembles mesurables dont l'union
est $f^{-1}\left(\left]0, +\infty\right]\right)$ donc
par [le théorème de continuité monotone (cf. annexe)](#cont-monot)
$\lim_{n \to + \infty} \mu\left(f^{-1}\left([2^{-n}, +\infty]\right)\right)
=
\mu\left(f^{-1}\left(\left]0, +\infty\right]\right)\right)$.


Notons $A_n = f^{-1}([2^{-n}, +\infty])$ ; c'est un ensemble
mesurable de mesure positive. La fonction $2^{-n}1_{A_n}$ est positive, étagée, 
mesurable et inférieure à $f$. On a donc
$$
0 < 2^{-n}\mu(A_n) = \int 2^{-n}1_{A_n} \mu \leq \int f\mu.
$$
L'intégrale de $f$ par rapport $\mu$ est donc strictement positive.

### {.ante}
La théorie générale de l'intégration possède aussi son théorème de convergence
dominée. Pour le démontrer, un corollaire du théorème de convergence monotone, 
appelée lemme de Fatou, est utile ; ce [lemme technique](#Fatou) est présenté 
en annexe.

### Théorème de convergence dominée {.theorem #TCD}
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré et
$f_k: X \to [-\infty, +\infty]$, $k \in \N$, une suite de fonctions 
mesurables, dominées par la fonction intégrable $g: X \to [0, +\infty]$
c'est-à-dire telles que pour tout tout $k \in \N$ et tout $x \in X$,
$$
0 \leq |f_k(x)| \leq g(x) \; \mbox{ et } \; \int g \mu < +\infty.
$$
Si la suite des $f_k$ a une limite simple $f: X \to [-\infty, +\infty]$,
c'est-à-dire si pour tout $x \in X$,
$f_k(x) \to f(x) \mbox{ quand } k \to +\infty,$
alors
$$
\lim_{k \to +\infty} \int f_k \mu  = \int f \mu.
$$

### Démonstration {.proof}
Comme $f_k + g$ est positif pour tout $k \in \N$, [le lemme de Fatou](#Fatou)
fournit
$$
\begin{split}
\int f \mu + \int g \mu &=
\int (f+ g) \mu  \\
&= \int (\liminf_{k \to +\infty} f_k + g) \mu \\
&\leq \liminf_{k\to +\infty} \int f_k + g \mu \\
&=\left(\liminf_{k\to +\infty} \int f_k \mu \right)+ \int g \mu
\end{split}
$$
et donc
$$
\int f \mu  \leq \liminf_{k\to +\infty} \int f_k \mu.
$$
Comme les fonctions $-f_k + g$ sont également positives pour tout $k \in \N$,
un raisonnement analogue fournit
$$
-\int f \mu  \leq \liminf_{k\to +\infty} \int - f_k \mu = - \limsup_{k\to +\infty} \int f_k \mu.
$$
On a finalement la double inégalité
$$
\limsup_{k\to +\infty} \int f_k \mu \leq \int f \mu  \leq \liminf_{k\to +\infty} \int f_k \mu,
$$
dont on déduit le résultat cherché.


Annexe
================================================================================

Continuité Monotone
--------------------------------------------------------------------------------

### Théorème de continuité monotone {.theorem #cont-monot}
Soit $(X ,\mathcal{A}, \mu)$ un espace mesuré et $(A_n)_{n \in \N}$ une
suite d'ensembles de $\mathcal{A}$. Si la suite $A_n$ est
croissante, c'est-à-dire si $A_n \subset A_{n+1}$ pour tout $n\in\N$,
alors
$$
\lim_{n \to +\infty} \mu(A_n) = \mu \left(\bigcup_{n=0}^{+\infty} A_n \right).
$$
Si $\mu(A_0) < +\infty$ et que $A_n$ est décroissante, c'est-à-dire si 
$A_{n+1} \subset A_{n}$ pour tout $n\in\N$, alors
$$
\lim_{n \to +\infty} \mu(A_n) = \mu \left(\bigcap_{n=0}^{+\infty} A_n \right).
$$

### {.post} 
Il est assez facile de se convaincre que sans une hypothèse de type
$\mu(A_0) < +\infty$, le volet décroissant du théorème est faux. 
Ainsi pour la mesure $\mu=\ell$
de longueur dans $\R$ (mesure de Lebesgue), pour tout $n \in \N$ on a
$\ell(\left[n, +\infty\right[)  =+\infty$
et pourtant
$$
\ell\left(\bigcap_{n=0}^{+\infty} \left[n, +\infty\right[\right) = 
\ell(\varnothing)  = 0.
$$
Toutefois, dans le cas particulier des mesures finies 
(vérifiant $\mu(A) < +\infty$ pour tout $A \in \mathcal{A}$) 
et en particulier des mesures de probabilité, 
la condition $\mu(A_0) < +\infty$ est automatiquement vérifiée. 



### Démonstration {.proof}
Si $(A_n)_{n \in \N}$ est une suite croissante d'ensembles de $\mathcal{A}$, 
alors les ensembles $B_n$ définis par $B_0 = A_0$ puis 
$B_{n+1} = A_{n+1} \setminus A_n$ appartiennent à $\mathcal{A}$ et sont disjoints.
Comme par construction on a $\cup_{k=0}^n B_k = A_n$ par 
(additivité et) $\sigma$-additivité
de $\mu$ on a d'une part
$$
\sum_{k=0}^n \mu(B_k) =  \mu(A_n) 
$$
et d'autre part 
$$
\sum_{k=0}^{+\infty} \mu(B_k) = \mu\left( \bigcup_{k=0}^{+\infty} B_k \right) 
= \mu \left( \bigcup_{n=0}^{+\infty} A_n \right).
$$
Par conséquent, 
$$
\lim_{n \to +\infty} \mu(A_n) = \mu \left(\bigcup_{n=0}^{+\infty} A_n \right).
$$
Si désormais $(A_n)_{n \in \N}$ est une suite décroissante d'ensembles de 
$\mathcal{A}$ vérifiant $\mu(A_0) < +\infty$, les ensembles $B_n$ définis
par $B_n = A_0 \setminus A_n$ forment une suite croissante d'ensembles,
par conséquent
$$
\lim_{n \to +\infty} \mu(A_0 \setminus A_n) = 
\mu \left(\bigcup_{n=0}^{+\infty} (A_0 \setminus A_n) \right)
= \mu \left(A_0 \setminus \bigcap_{n=0}^{+\infty} A_n \right).
$$
Tous les ensembles $A_n$ étant inclus dans $A_0$, on a également
$\mu(A_0 \setminus A_n) + \mu(A_n) = \mu(A_0)$ et
$$
\mu \left(A_0 \setminus \bigcap_{n=0}^{+\infty} A_n \right)
+
\mu \left(\bigcap_{n=0}^{+\infty} A_n \right)
= \mu(A_0)
$$
et par conséquent
$$
\mu(A_0) - \lim_{n \to +\infty} \mu(A_n) = 
\mu(A_0) - \mu \left(\bigcap_{n=0}^{+\infty} A_n \right).
$$
Comme $\mu(A_0)$ est fini, on peut le simplifier de part et d'autre de 
l'égalité et en déduire finalement
$$
\lim_{n \to +\infty} \mu(A_n) = 
\mu \left(\bigcap_{n=0}^{+\infty} A_n \right).
$$

Lemme de Fatou
--------------------------------------------------------------------------------

On rappelle que 
$\liminf_{k\to +\infty} x_k$ désigne l'infimum des limites possibles,
parmi toutes les suites extraites de $x_k$ ayant une limite (finie ou infinie).

### Lemme de Fatou {.lemma #Fatou}
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré et
$f_k: X \to [0, +\infty]$, $k \in \N$, une suite de fonctions 
mesurables. Alors
$$
\int (\liminf_{k \to +\infty} f_k) \mu \leq \liminf_{k\to +\infty} \int f_k \mu.
$$

### Démonstration {.proof} 
La suite des fonctions $\inf_{j \geq k} f_j$, $k \in \N$, est croissante,
composée de fonctions mesurables, et converge simplement vers la limite 
inférieure de la suite des $f_k$ :
$$
\lim_{k\to +\infty} \left(\inf_{j\geq k} f_j\right) = \liminf_{k\to +\infty} f_k.
$$
Par [le théorème de convergence monotone](#TCM) on a donc
$$
\lim_{k\to +\infty} \int \inf_{j \geq k} f_j \mu = \int (\liminf_{k \to +\infty} f_k) \mu.
$$
De plus pour tout $k \in \N$ et tout $\ell \geq k$, on a $\inf_{j \geq k} f_j \leq f_{\ell}$, donc
par [le lemme de croissance](#lemme-croissance),
$$
\int \inf_{j \geq k} f_j \mu \leq \liminf_{\ell \to +\infty} \int f_{\ell} \mu.
$$
Puisque le second membre est indépendant de $k$, on en déduit le résultat
cherché en faisant tendre $k$ vers $+\infty$.


Mesure de Lebesgue -- Approche directe
--------------------------------------------------------------------------------

Dans les volets précédents du "Calcul Intégral", il nous a semblé naturel
de définir le volume d'un pavé compact de $\R^n$ 
$$
P = [a_1, b_1] \times \dots \times [a_n, b_n]
$$
au moyen de la formule
$$
v(P) := (b_1  -a_1) \times \dots \times (b_n - a_n).
$$
L'intégrable de Henstock-Kurzweil nous permet de prolonger cette fonction $v$ 
en une fonction définie pour tous les ensembles mesurables $A$ de $\R^n$,
par la relation
$$
v(A) = \left|
\begin{array}{cl}
\displaystyle \int 1_A(x) \, dx & \mbox{si $1_A$ est intégrable au sens de Henstock-Kurzweil,}\\
+\infty & \mbox{sinon.}
\end{array}
\right.
$$
Mais cette approche n'est pas totalement satisfaisante intellectuellement.
D'une part on peut considérer l'usage de l'intégrale comme un chemin
tortueux pour étendre $v$.
D'autre part on peut avoir l'impression
que cette approche -- qui ne permet pas de mesurer le volume de tout
ensemble de $\R^n$ -- n'atteint pas totalement son objectif ;
cette limitation pourrait être un artefact de la méthode choisie
plutôt qu'une limitation intrinsèque.
Dans cette section, nous allons donner une autre méthode de définition, 
plus directe et géométrique, due à Lebesgue et Carathéodory[^autz],
de définition de la mesure (extérieure) du volume de tout ensemble 
de $\R^n$.
Elle nous donnera également la raison pour laquelle
notre construction initiale du volume se limite à la collection
des ensembles qualifiés de "mesurables".

[^autz]: Henri Lebesgue (1875-1941) était un mathématicien français
et Constantin Carathéodory (1873-1950) un mathématicien grec entrenant
des liens étroits avec l'Allemagne. Ils font partie des fondateurs de 
la théorie abstraite de la mesure qui conduit à un renouveau de la théorie 
de l'intégration au début du XXème siècle.

Pour calculer le volume d'un sous-ensemble de $\R^n$, 
nous généralisons la méthode déjà utilisée pour définir les ensembles négligeables 
(de volume nul) : nous considérons l'ensemble des collections dénombrables
de pavés recouvrant ce sous-ensemble et nous utilisons chacun des ces 
recouvrements pour produire une estimation (supérieure) du volume
de l'ensemble. Formellement :

### Mesure extérieure de Lebesgue {.definition #mel}
On appelle *mesure extérieure de Lebesgue* sur $\R^n$ la fonction
$$v^*: \mathcal{P}(\R^n) \to [0, +\infty],$$ 
qui a tout ensemble $A$ de $\R^n$ associe le nombre réel étendu positif
défini par
$$
v^*(A) 
= 
\inf 
\left\{
\sum_{k=0}^{+\infty} v(P_k)
\; \left| \vphantom{\bigcup_{k=0}^{+\infty}} \right. \; 
\mbox{$P_k$ pavé compact de $\R^n$,} \, A \subset \bigcup_{k=0}^{+\infty} P_k
\right\},
$$

Cette définition "raisonnable" ne satisfait toutefois pas les propriétés que
nous attendons (implicitement) d'un volume. Ce décalage est mis en évidence
par un résultat paradoxal de la théorie des ensembles dans $\R^3$ :

### Paradoxe de Banach-Tarski {.theorem}
Il est possible de partitionner une sphère de rayon un de $\R^3$ 
en un nombre fini d'ensembles, qui, 
après rotations et translations, 
forment une partition de deux sphères disjointes de rayon un.



Si le résultat est qualifié de paradoxe, c'est qu'il nous semble intuitivement 
que le volume devrait être préservé par les les opérations subies par 
la sphère initiale. Or, le volume d'une sphère de rayon un et de deux 
sphères disjointes de même rayon diffère d'un facteur $2$.
Pour dépasser ce paradoxe, nous allons devoir examiner un par un les
résultats qui nous semblent "évidents" dans ce raisonnement pour débusquer
notre erreur.

Soient $A_1, \dots, A_p$ des ensembles disjoints et non vides
de $\R^3$ dont la réunion forme la sphère initiale $S_0 = A_1 \cup \dots\cup A_p$,
et tels que des ensembles disjoints $B_1, \dots, B_p$ 
qui s'en déduisent par rotation et translation, 
vérifient $S_1 \cup S_2 = B_1 \cup \dots \cup B_p$ où $S_1$ et $S_2$
sont les deux sphère finales.

Tout d'abord, on a bien
$$
v^*(S) = \frac{4\pi}{3} \; \mbox{ et } \; v^*(S_1 \cup S_2) = 2 \times \frac{4 \pi}{3},
$$
car les ensembles $S_0$, $S_1$ et $S_2$ considérés sont intégrables 
(au sens de l'intégrale de Henstock-Kurzweil)
et nous verrons ultérieurement que dans ce cas, la mesure extérieure
$v^*$ coïncide avec $v$.
Un simple calcul intégral fournit alors le résultat.

On peut croire que le point faible de notre raisonnement est la préservation
de la valeur de $v^*(A)$ par translation et rotation ; s'il est facile d'établir
que lorsque $B$ se déduit de $A$ par une translation alors $v^*(A) = v^*(B)$, 
on peut douter du résultat pour les rotations. 
Après tout, la définition de $v^*(A)$ fait appel
à des rectangles qui sont parallèles aux axes, une propriété qui n'est pas
conservée par rotation. 
Mais si le résultat n'est pas évident, il s'avère pourtant que
la mesure extérieure $v^*$ est bien invariante par rotation 
(cf. [@Hun11, section 2.8]).

La propriété qui nous fait défaut est plus fondamentale : la fonction $v^*$
n'est tout simplement pas additive ! Même si les ensembles 
$A_1, \dots, A_p$ sont disjoints, il est possible que 
$$
v^*(A_1 \cup \dots \cup A_p) \neq v^*(A_1) + \dots + v^*(A_p).
$$
On peut par contre établir avec la définition de $v^*$ qu'elle est 
sous-additive : pour tous les ensembles $A_1, \dots, A_p$ (disjoints ou non),
on a 
$$
v^*(A_1 \cup \dots \cup A_p) \leq v^*(A_1) + \dots + v^*(A_p).
$$
Elle est même $\sigma$-sous-additive : si $(A_k)_{k \in \N}$ est une suite
de sous-ensembles de $\R^n$, 
$$
v^*\left(\bigcup_{k=0}^{+\infty} A_k\right)
\leq \sum_{k=0}^{+\infty} v^*\left(A_k\right).
$$

Cette propriété est la caractéristique centrale des *mesures extérieures* :

### Mesure extérieure {.definition}
On appelle *mesure extérieure* sur l'ensemble $X$ toute application
$$v^* :\mathcal{P}(X) \to [0, +\infty]$$ telle que :

  1. $\mu^*(\varnothing) = 0$ (*nullité en $\varnothing$*).

  2. $A \subset B \Rightarrow \mu^*(A) \subset \mu^*(B)$ (*croissance*).

  3. $\mu^*\left(\cup_{k=0}^{+\infty}A_k\right) \leq \sum_{k=0}^{+\infty} \mu^*\left(A_k\right)$ (*$\sigma$-subadditivité*).

-----

Il existe un procédé général permettant de déduire d'une mesure extérieure
une application qui soit additive -- à condition d'accepter de réduire
son domaine de définition ; la fonction qui en résulte est additive -- 
et même $\sigma$-additive. 

### Ensemble mesurable 
Soit $\mu^*$ une mesure extérieure sur l'ensemble $X$.
Un ensemble $A \subset X$ est dit *$\mu^*$-mesurable* (au sens de Carathéodory) 
si pour tout $B \subset X$, on a 
$$
\mu^*(B) = \mu^*(B \cap A) + \mu^*(B \setminus A).
$$

### {.post}
Une façon alternative de voir les choses : si l'on note $\mu^*|_A$ 
la *trace* de $\mu^*$ sur un ensemble $A$ de $X$, définie pour tout
sous-ensemble $B$ de $X$ par
$$\mu^*|_A(B) = \mu^*(A \cap B),$$
alors l'ensemble $A$ est $\mu^*$-mesurable si et seulement si
$$
\mu^* = \mu^*|_A + \mu^*|_{A^c}.
$$

### Mesure associée à une mesure extérieure {.theorem}
Soit $X$ un ensemble et $\mu^*$ une mesure extérieure sur $X$.
La collection $\mathcal{A}$ des ensembles $\mu^*$-mesurables de $X$
est une tribu sur $X$ et la restriction $\mu$ de $\mu^*$ à 
$\mathcal{A}$ est une mesure sur $X$.

### Démonstration {.proof}
Cf. [@Hun11, théorème 2.9, pp. 15-17].

### {.remark .ante}
La spécialisation de ce procédé au cas de la mesure extérieure de Lebesgue
produit la mesure de Lebesgue.

### Mesure de Lebesgue {.theorem .definition}
La "[mesure extérieure de Lebesgue](#mel)" $v^*:\mathcal{P}(\R^n) \to [0, +\infty]$
est bien une mesure extérieure sur $\R^n$.
La collection des ensembles $v^*$-mesurables (au sens de Caratheodory)
est identique à la tribu de Lebesgue $\mathcal{L}(\R^n)$ ; 
la mesure $v$ associée à $v^*$ coïncide avec la mesure de Lebesgue sur $\R^n$. 

### Démonstration (partielle : $v^*$ est une mesure extérieure.) {.proof}
Il est clair que $v^*$ satisfait $v^*(\varnothing)=0$ (car le pavé
$[0,0]^n$ recouvre $\varnothing$ par exemple). 
Si $A \subset B \subset \R^n$, alors tout recouvrement de $B$ par des
pavés compacts recouvre également $A$ ; par conséquent $v^*(A) \leq v^*(B)$.
Finalement, pour tout $A_k \subset \R^n$, $k \in \N$, et pour tout $\varepsilon > 0$, 
il existe des pavés compacts $P_{jk}$ tels que 
$$
A_k \subset \bigcup_{j=0}^{+\infty} P_{jk} 
\; \mbox{ et } \;
\sum_{j=0}^{+\infty} v(P_{jk}) - \frac{\varepsilon}{2^{k+1}} 
\leq v^*(A_k) \leq \sum_{j=0}^{+\infty} v(P_{jk}).
$$
Comme la famille des $\{P_{jk}\}_{jk}$ recouvre $\cup_{k=0}^{+\infty} A_k$, 
on a donc
$$
v^*(\cup_{k=0}^{+\infty} A_k) \leq \sum_{k=0}^{+\infty} \sum_{j=0}^{+\infty} v(P_{jk})
\leq 
\sum_{k=0}^{+\infty} \left(v^*(A_k) +\frac{\varepsilon}{2^{k+1}}\right)
= \left(\sum_{k=0}^{+\infty} v^*(A_k)\right) +\varepsilon.
$$
Le réel positif $\varepsilon$ étant arbitrairement petit, on en déduit
que $v^*$ est bien $\sigma$-subadditive.

Exercices
================================================================================



Intégrales et séries
--------------------------------------------------------------------------------

Dans cet exercice, on montre que la théorie générale de l'intégration fournit 
un cadre permettant d'étudier les séries et leur somme.

Soit $c$ la mesure de comptage sur $\N$.

### Question 1 {.question #is-1}
A quelle condition (nécessaire et suffisante) une fonction 
$f:\N \to [-\infty, +\infty]$ est-elle mesurable 
(vis-à-vis de la tribu associée à la mesure de comptage sur $\N$) ?

### Question 2 {.question #is-2}
Soit $f:\N \to [0, +\infty]$ une fonction mesurable.
Montrer que l'intégrale de $f$ par rapport à la mesure de comptage vérifie
$$
\int f \, c = \sum_{n \in \N} f(n).
$$

### Question 3 {.question #is-3}
Soit $f:\N \to [-\infty, +\infty]$ une fonction mesurable.
A quelle condition (nécessaire et suffisante) la fonction $f$ est-elle $c$-intégrable ? 
Calculer alors son intégrale.

### Question 4 {.question #is-4}
Formuler le théorème de convergence dominée associé à la mesure de comptage 
$c$ sur $\N$ comme un résultat portant sur les séries.



Mesure définie par une intégrale
--------------------------------------------------------------------------------
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré. Soit $f:X \to \left[0, +\infty\right[$ 
une fonction mesurable positive à valeurs finies. 

### Question 1 {.question #mdi-1}
Montrer que pour tout $A \in \mathcal{A}$, la fonction $1_A f$ est mesurable.

### Question 2 {.question #mdi-2}
Montrer que la fonction notée $f \mu$ définie par
$$
f \mu : A \in \mathcal{A} \mapsto \int_A f \, \mu := \int 1_A f \, \mu \in [0, +\infty].
$$
est une mesure sur $(X, \mathcal{A})$.

Mesure image 
--------------------------------------------------------------------------------

### Question 0 {.question #mim-0}
Soit $\mu$ une mesure sur $\R$ muni de la tribu de Lebesgue $\mathcal{L}(\R)$.
Soit $h: \R \to \R$ la fonction définie par
$$
h(x) = \left|
\begin{array}{rl}
-1 & \mbox{si $x \leq -1$,} \\
x & \mbox{si $-1 < x <+1$,} \\
+1 & \mbox{si $+1 \leq x$.}
\end{array}
\right.
$$
![](images/mesure-image.py)
Montrer que la fonction
$$
\nu : A \in \mathcal{L}(\R) \to \mu(h^{-1}(A))
$$
est bien définie et est une mesure sur $(\R,\mathcal{L}(\R))$. 
Indication : on essaiera d'exprimer $\nu$ comme la somme de trois mesures.

### {.ante}

Soit $(X, \mathcal{A}, \mu)$ un espace mesuré et $h: X \to Y$ une application.
On définit la collection 
$$
\mathcal{B} = \{B \subset Y \, | \, h^{-1}(B) \in \mathcal{A}\}
$$
et la fonction $\mu \circ h^{-1}: \mathcal{B} \to [0, +\infty]$ par
$$
\mu \circ h^{-1}(B) = \mu(h^{-1}(B)).
$$

### Question 1 {.question #mim-1}
Montrer que $\mathcal{B}$ est une tribu.

### Question 2 {.question #mim-2}
Montrer que $\mu \circ h^{-1}$ est une mesure sur $\mathcal{B}$ ; 
on l'appelle la *mesure image de $\mu$ par $h$*.

### Question 3 {.question #mim-3}
Montrer que la fonction $f:Y \to [-\infty,\infty]$ est 
$\mathcal{B}$-mesurable si et seulement si $f \circ h$ est 
$\mathcal{A}$-mesurable.
Montrer ensuite que
$f:Y \to [-\infty, +\infty]$ est $\mu \circ h^{-1}$-intégrable 
si et seulement si $f \circ h$ est $\mu$-intégrable et qu'alors,
$$
\int_Y f(y) \, (\mu \circ h^{-1})(dy) = \int_X (f \circ h)(x) \, \mu(dx).
$$

Complétion d'une mesure {#complétion}
--------------------------------------------------------------------------------

Soit $(X, \mathcal{A}, \mu)$ un espace mesuré. 
On note $A \ds B$ la différence symétrique
de deux sous-ensembles $A$ et $B$ de $X$, c'est-à-dire l'ensemble défini par
$$
A \ds B = (A \setminus B) \cup (B \setminus A) = (A \cap B^c) \cup (A^c \cap B).
$$
On note $\mathcal{N}$ la collection des ensembles négligeables pour $\mu$ :
$$
\mathcal{N} = 
\{
N \subset X 
\; | \;
\mbox{il existe $A \in \mathcal{A}$ tel que $N \subset A$ et $\mu(A) = 0$.} 
\}.
$$

### Question 1 {.question #cm-1}
Montrer que la collection $\overline{\mathcal{A}}$ définie par
$$
\overline{\mathcal{A}} 
= 
\{A \ds N \; | \; A \in \mathcal{A}, \; N \in \mathcal{N}\}
$$
est une tribu.

### Question 2 {.question #cm-2}
Montrer que la mesure $\mu$ peut être étendue d'une façon unique en une
mesure $\overline{\mu}$ définie sur $\overline{\mathcal{A}}$.


Approximation par des ensembles mesurables (hors-programme)
--------------------------------------------------------------------------------

Soit $A$ un sous-ensemble de $\R^n$.

### Question 1 {.question #enm-1}
Montrer qu'il existe un ensemble $v^*$-mesurable $B$ contenant $A$ et tel que
$v^*(A) = v^*(B)$.

### Question 2 {.question #enm-2}
A quelle condition portant sur $v^*(B \setminus A)$ l'ensemble $A$ est-il 
$v^*$-mesurable ?

Mesure intérieure (hors-programme)
--------------------------------------------------------------------------------

Soit $A$ un ensemble borné de $\R^n$ et $P$ un pavé compact de $\R^n$
contenant $A$.
On appelle *mesure intérieure de $A$* la grandeur
$$
v_*(A) = v^*(P) - v^*(P \setminus A)
$$
où $v^*$ désigne la mesure extérieure de Lebesgue sur $\R^n$.

### Question 1 {.question #mi-1}
Montrer que la définition de $v_*(A)$ ne dépend pas du choix du pavé $P$.

### Question 2 {.question #mi-2}
Montrer que $v_*(A) \leq v^*(A)$, avec égalité si $A$ est $v^*$-mesurable.

### Question 3 {.question #mi-3}
Montrer la réciproque de la question précédente : si $A \subset \R^n$ est borné
et $v_*(A) = v^*(A)$, alors $A$ est $v^*$-mesurable.

Solutions
================================================================================

Intégrales et séries
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-is-1}
La tribu associée à la mesure de comptage $c$ sur $\N$ est l'ensemble des
parties de $\N$ notée $\mathcal{P}(\N)$. 
Or toute fonction $f: \N \to [-\infty, +\infty]$ est $\mathcal{P}(\N)$-mesurable.
En effet, quel que soit l'ouvert $U \subset [-\infty, +\infty]$, 
$f^{-1}(U)$ est un sous-ensemble de $\N$, c'est-à-dire un élément de 
$\mathcal{P}(\N)$.

### Question 2 {.answer #answer-is-2}
Toute fonction $f:\N \to [0, +\infty]$ est $\mathcal{P}(\N)$-mesurable.
Pour tout $k \in \N$, la fonction $f_k:\N \to [0, +\infty]$ définie
par
$$
f_k(n) = \left|
\begin{array}{rl}
f(n) & \mbox{si $k \leq n$,} \\
0 & \mbox{sinon.}
\end{array}
\right.
$$
est également mesurable, positive et étagée (elle prend au plus $k+1$ valeurs
différentes). De plus, il est clair que la suite des $f_k$ est croissante et
que pour tout $n \in \N$, $\lim_{k \to +\infty} f_k(n) = f(n)$.
La propriété de convergence monotone de l'intégrale nous assure alors que
$$
\lim_{k \to +\infty} \int f_k \, c = \int f\, c.
$$
Or, comme la fonction étagée $f_k$ prend la forme
$$
f_k  = \sum_{n=0}^k f(n) 1_{\{n\}}
$$
et que le lien entre intégrale et mesure nous fournit
$$
\int 1_{\{n\}} \, c = c(\{n\}) = 1,
$$
la linéarité de l'intégrale nous permet de conclure que
$$
\int f_k \, c = \sum_{n=0}^k f(n).
$$
Par conséquent,
$$
\int f\, c = \sum_{n=0}^{+\infty} f(n).
$$

### Question 3 {.answer #answer-is-3}
Toute fonction $f:\N \to [-\infty, +\infty]$ est $\mathcal{P}(\N)$-mesurable.
Elle est $c$-intégrable si $f_+$ et $f_-$ ont des intégrales finies, 
c'est-à-dire si
$$
\sum_{n=0}^{+\infty} f_+(n) < + \infty \; \mbox{ et } \;
\sum_{n=0}^{+\infty} f_-(n) < + \infty,
$$
ce qui est le cas si et seulement si 
$$
\sum_{n=0}^{+\infty} f_+(n) + f_-(n) =
\sum_{n=0}^{+\infty} |f|(n) < + \infty,
$$
autrement dit si et seulement si la suite des $f(n)$ est absolument convergente.
Dans ce cas, on a 
$$
\int f\, c = \int f_+ \, c - \int f_- \, c = 
\sum_{n=0}^{+\infty} f_+(n) - \sum_{n=0}^{+\infty} f_-(n)
= \sum_{n=0}^{+\infty} f(n).
$$

### Question 4 {.answer #answer-is-4}
Le théorème de convergence dominée dans le cas de la mesure de comptage
$c$ sur $\N$ devient le résultat suivant sur les (suites de) séries : 

Soit $f_k: \N \to [-\infty, +\infty]$, $k \in \N$, une suite de fonctions 
dominées par la fonction intégrable $g: \N \to [0, +\infty]$
c'est-à-dire telles que pour tout tout $k \in \N$ et tout $n \in \N$,
$$
0 \leq |f_k(n)| \leq g(n) \; \mbox{ et } \; \sum_{n=0}^{+\infty} g(n) < +\infty.
$$
Si pour tout $n \in \N$,
$f_k(n) \to f(n) \mbox{ quand } k \to +\infty,$
alors
$$
\lim_{k \to +\infty} \sum_{n=0}^{+\infty} f_k(n)  = \sum_{n=0}^{+\infty} f(n).
$$


Mesure définie par une intégrale
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-mdi-1}
Pour tout $A \in \mathcal{A}$, la fonction $1_A$ est mesurable, car
l'image réciproque par $1_A$ d'un ouvert de $[0, +\infty]$ est soit 
$A$ soit $\varnothing$. Si $f: X \to \left[0, +\infty\right[$ est mesurable,
on peut l'écrire comme une limite simple et croissante de fonctions 
$f_k: X \to \left[0, +\infty\right[$ mesurables et étagées. La suite 
$1_A f_k$ est de même nature et converge simplement vers $1_A f$ ; la
fonction $1_A f$ est donc mesurable.

### Question 2 {.answer #answer-mdi-2}
La fonction notée $f \mu$ définie par
$$
f \mu : A \in \mathcal{A} \mapsto \int_A f \, \mu := \int 1_A f \, \mu \in [0, +\infty]
$$
est de tout évidence à valeurs dans $[0, +\infty]$ et nulle en zéro.

Si les ensembles de la suite $(A_k)_{k \in N}$ sont mesurables et disjoints, 
les fonctions 
$$
g_k = 1_{\cup_{j=0}^k A_k} = \sum_{j=0}^k 1_{A_k}
$$
forment une suite croissante de fonctions mesurables et $g_k f$ converge
simplement vers $1_{\cup_{k=0}^{+\infty} A_k} f$. Par le théorème de
croissance monotone, on a donc
$$
f\mu\left(\bigcup_{k=0}^{+\infty} A_k\right)
= \int 1_{\cup_{k=0}^{+\infty} A_k} f \, \mu =
\sum_{k=0}^{+\infty} \int 1_{A_k} f \, \mu = \sum_{k=0}^{+\infty} f\mu(A_k).
$$
La fonction $f \mu$ est donc $\sigma$-additive. C'est donc une mesure sur
$(X,\mathcal{A})$.

Mesure image 
--------------------------------------------------------------------------------

### Question 0 {.answer #answer-mim-0}
Pour tout $A \subset \R$,
$h^{-1}(A) \cap \left]-1, 1\right[ = A \cap \left]-1, 1\right[,$
$h^{-1}(A) \cap \left]-\infty, -1\right] = \left]-\infty, -1\right]$ ou $\varnothing$ selon que
$-1$ appartienne ou non à $A$ et $h^{-1}(A) \cap \left[+1, +\infty\right[ = \left[+1, +\infty\right[$ 
ou $\varnothing$ selon que $+1$ appartienne ou non à $A$.

Par conséquent, si $A \in \mathcal{L}(\R)$, l'ensemble 
$$h^{-1}(A) = (h^{-1}(A) \cap \left]-\infty, -1\right]) \cup (h^{-1}(A) \cap \left]-1, 1\right[)   \cup (h^{-1}(A) \cap \left[+1, +\infty\right[)$$ est 
l'union de trois ensembles de $\mathcal{L}(\R)$ ; il appartient donc à $\mathcal{L}(\R)$
et la fonction $\nu$ est bien définie.

En utilisant l'additivité de $\mu$, on constate alors que
$$
\nu(A) = \mu(h^{-1}(A)) = \alpha \delta_{-1}(A) + \mu|_{\left]-1,1\right[} (A) + \beta \delta_{1}(A)
$$
où $\alpha= \mu(\left]-\infty, -1\right])$, $\beta = \mu(\left[+1, +\infty\right[)$
et $\mu|_{\left]-1,1\right[}$ est la mesure
trace de $\mu$ sur $\left]-1,1\right[$,
définie par $\mu|_{\left]-1,1\right[} (A) = \mu(\left]-1,1\right[ \cap A)$.
La fonction $\nu(A)$ est donc une mesure sur $(\R, \mathcal{L}(\R))$ comme somme
de trois mesures sur  $(\R, \mathcal{L}(\R))$.

### Question 1 {.answer #answer-mim-1}
L'ensemble $\mathcal{B}$ est une tribu ; en effet :

  - $\varnothing \in \mathcal{A}$ et $\varnothing = h^{-1}(\varnothing)$,
    donc $\varnothing \in \mathcal{B}$.

  - Si $B \in \mathcal{B}$, l'ensemble 
    $A = h^{-1}(B)$ appartient à $\mathcal{A}$. 
    Le complémentaire $Y \setminus B$ de $B$ dans $Y$
    vérifie $h^{-1}(Y \setminus B) = X \setminus h^{-1}(B) = X \setminus A$
    et appartient donc à $\mathcal{A}$. L'ensemble $Y \setminus B$ appartient
    donc à $\mathcal{B}$.

  - Si les ensembles $B_k$, $k \in \N$ appartiennent à $\mathcal{B}$, 
    comme $h^{-1}(\cup_k B_k) = \cup_k h^{-1}(B_k)$, cet ensemble
    appartient à $\mathcal{A}$. L'union dénombrable $\cup_k B_k$
    appartient donc à $\mathcal{B}$.

### Question 2 {.answer #answer-mim-2}
Montrons que $\mu \circ h^{-1}$ est une mesure sur $\mathcal{B}$.

  - On a $\mu\circ h^{-1}(\varnothing) = \mu(h^{-1}(\varnothing)) = \mu(\varnothing) = 0$.

  - Si les ensembles $B_k$, $k \in \N$, appartiennent à $\mathcal{B}$ et sont
    disjoints, alors les ensembles $h^{-1}(B_k)$ appartiennent à $\mathcal{A}$,
    et sont disjoints. Comme $h^{-1}(\cup_k B_k) = \cup_k h^{-1}(B_k)$, on a
    $$
    \begin{split}
    \mu \circ h^{-1} \left(\bigcup_k B_k \right)
    &=
    \mu\left(h^{-1}\left(\bigcup_k B_k \right)\right) \\
    &=
    \mu\left(\bigcup_k h^{-1}\left( B_k \right)\right) \\
    &=
    \sum_k \mu\left(h^{-1}\left( B_k \right)\right) \\
    &=
    \sum_k \mu \circ h^{-1}\left(B_k\right)
    \end{split}
    $$
    
### Question 3 {.answer #answer-mim-3}
Montrons tout d'abord que la fonction $f:Y \to [-\infty,+\infty]$ est 
$\mathcal{B}$-mesurable si et seulement si $f \circ h$ est 
$\mathcal{A}$-mesurable.
Par définition,
$f$ est mesurable si pour tout ouvert $U$ de $\R$,
l'ensemble $f^{-1}(U)$ appartient $\mathcal{B}$, c'est-à-dire
si et seulement si
$$
h^{-1} (f^{-1}(U)) = (f \circ h)^{-1}(U) \in \mathcal{A},
$$
c'est-à-dire si et seulement si $f \circ h$ est mesurable.

Comme $(f \circ h)_+ = f_+ \circ h$ et $(f \circ h)_- = f_- \circ h$,
il nous suffit de montrer que pour toute fonction mesurable
$f: Y \to \left[0, +\infty\right]$, on a
$$
\int (f \circ h) \mu = \int f (\mu \circ h^{-1})
$$
pour pouvoir conclure que $f: Y \to  [-\infty,+\infty]$ est $\mu \circ h^{-1}$-intégrable si et
seulement si $f \circ h$ est $\mu$-intégrable et que l'égalité ci-dessus
est valable également dans le cas des fonctions signées.

Or pour une telle fonction positive $f$, il existe une suite croissante de fonctions 
$f_k$ étagées, positives et mesurables convergeant simplement vers $f$,
et l'on a 
$$
\int f (\mu \circ h^{-1}) 
=
\lim_{k \to +\infty} \int f_k (\mu \circ h^{-1}).
$$
Si à $k$ fixé, on explicite $f_k$ comme
$$
f_k = \sum_{j=1}^{n} y_j 1_{B_j}
$$
où les $B_j$ sont des ensembles mesurables et $y_j > 0$, alors
$$
\begin{split}
\int f_k (\mu \circ h^{-1}) 
&= \sum_{j=1}^{n} y_j (\mu \circ h^{-1})(B_j)  \\
&= \sum_{j=1}^{n} y_j \mu(h^{-1}(B_j)) \\
&= \int \sum_{j=1}^n y_j 1_{h^{-1}(B_j)} \, \mu \\
&= \int f \circ h^{-1} \, \mu \\
\end{split}
$$
Les fonctions $f_k \circ h$ sont étagées, positives et mesurables,
leur suite est croissante et converge simplement vers $f \circ h$.
[Par le théorème de convergence monotone](#TCM), on a donc comme souhaité
$$
\int f \, (\mu \circ h^{-1}) 
=
\int (f \circ h) \, \mu.
$$





Complétion d'une mesure
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-cm-1}


Il est clair que $\varnothing$ appartient à $\overline{\mathcal{A}}$,
comme différence symétrique entre $\varnothing$ et $\varnothing$.
Si $B = A \ds N$ appartient à $\overline{\mathcal{A}}$, alors
$$
B^c = ((A \cap N^c) \cup (A^c \cap N))^c = (A^c \cup N) \cap (A \cup N^c).
$$
Comme $B^c = X \cap B^c = (A \cup A^c) \cap B^c$, par distributivité on a
$$
\begin{split}
B^c &= (A^c \cap A) \cup (A^c \cap N^c) \cup (N \cap A) \cup (N \cap N^c) \\
    &= (A^c \cap N^c) \cup (A \cap N) \\
    &= ((A^c) \cap N^c) \cup ((A^c)^c \cap N) \\
    &= A^c \ds N 
\end{split}
$$
et par conséquent $B^c \in \overline{\mathcal{A}}$.

Si les $A_k$, $k \in \N$, appartiennent $\mathcal{A}$ et les 
$N_k$, $k \in \N$, appartiennent à $\mathcal{N}$, alors on pourra se
convaincre que
$$
(\cup_k A_k) \setminus (\cup_k N_k) 
\subset \cup_{k} (A_k \ds N_k)
\subset (\cup_k A_k) \cup (\cup_k N_k),
$$
ce qui prouve que 
$$
\cup_k (A_k \ds N_k) = (\cup_k A_k) \ds M 
\; \mbox{ avec } \;
M \subset N:= \cup_k N_k.
$$
Comme $N_k \subset B_k \in \mathcal{A}$ avec $\mu(B_k) =0$,
$$
N = \cup_k N_k \subset \cup_k B_k \in \mathcal{A},
$$
avec $\mu(\cup_k B_k) = 0$ par $\sigma$-additivité de $\mu$.
L'ensemble $N$ (et donc l'ensemble $M$) appartient donc à $\mathcal{N}$.
Comme $\cup_k A_k \in \mathcal{A}$, on en déduit que $\overline{\mathcal{A}}$ est stable
par union dénombrable. Cet collection contient l'ensemble vide, est fermé
par passage au complémentaire et par union dénombrable ; c'est donc une tribu.

### Question 2 {.answer #answer-cm-2}

Supposons que $\overline{\mu}$ soit une mesure sur $\overline{\mathcal{A}}$
qui prolonge $\mu$.
Alors, nécessairement, pour tout ensemble $N \in \mathcal{N}$, on a
$\overline{\mu}(N) = 0$. En effet, il existe un $A \in \mathcal{A}$ tel que
$N \subset A$ et $\mu(A) = 0$, donc par croissance de $\overline{\mu}$,
$$
\overline{\mu}(N) \subset \overline{\mu}(A) = \mu(A) = 0.
$$
Soit alors $A \in \mathcal{A}$ et $N \in \mathcal{N}$. Les ensembles
$N_1 := A \cap N$ et $N_2 = A^c \cap N$ sont inclus dans $N$ et donc 
appartiennent à $\mathcal{N}$, par conséquent
$$
\overline{\mu}(A \ds N) = \overline{\mu}((A \setminus N_1) \cup N_2)
= \overline{\mu}(A) - \overline{\mu}(N_1) + \overline{\mu}(N_2)
= \overline{\mu}(A).
$$ 
Cette équation définit uniquement $\overline{\mu}$ ; 
il faut toutefois s'assurer que cette définition est cohérente, c'est-à-dire
que si $A \ds N = B \ds M$ où $A, B \in \mathcal{A}$ et $N, M \in \mathcal{N}$,
alors $\mu(A) = \mu(B)$. En utilisant l'associativité de $\ds$, on montre que
$$
A \ds (N \ds M) = (A \ds N) \ds M = (B \ds M) \ds M = B \ds (M \ds M) = B.
$$
Par conséquent, $N \ds M \in \mathcal{A}$, et comme $N \ds M \subset
N \cup M$, on en déduit que $\mu(N \ds M) = 0$, et donc
$$
\mu(B) = \mu(A) - \mu(A \cap (N \ds M)) + \mu(A^c \cap (N \ds M)) = \mu(A).
$$


Il est ensuite nécessaire de prouver que $\overline{\mu}$ est bien une mesure.
Soit $A_k \in \mathcal{A}$ et $N_k \in \mathcal{N}$ deux suites d'ensembles
tels que les $A_k \ds N_k$ soient deux à deux disjoints.
Soit $M_k$ un ensemble de $\mathcal{A}$ contenant $N_k$ et tel que
$\mu(M_k) = 0$. L'ensemble $B_k :=  A_k \setminus M_k$ appartient $\mathcal{A}$
et $\mu(B_k) = \mu(A_k)$ ; de plus, comme $B_k \subset A_k \ds N_k$, les
$B_k$ sont disjoints deux à deux. On a déjà vu à la question précédente que
$$
\overline{\mu}(\cup_k A_k \ds N_k)
= \overline{\mu}((\cup_k A_k) \ds N) \; \mbox{ où } \, N \in \mathcal{N},
$$
donc
$$
\begin{split}
\overline{\mu}(\cup_k A_k \ds N_k)
&= \mu(\cup_k A_k) = \mu(\cup_k B_k) \\
&= \sum_k \mu(B_k) = \sum_k \mu(A_k) = \sum_k \overline{\mu}(A_k \ds N_k).
\end{split}
$$
La fonction $\overline{\mu}$ est donc $\sigma$-additive.


Approximation par des ensembles mesurables (hors-programme) {#aem}
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-enm-1}
Par définition de $v^*(A)$, pour tout $j \in \N$, il existe une collection
dénombrable de pavés $P^j_k$ tels que
$$
v^*(A) \leq \sum_{k=0}^{+\infty} v(P^j_k) \leq v^*(A) + 2^{-j}.
$$
Les ensembles $B_j = \cup_k P^j_k$ sont $v^*$-mesurables comme unions 
dénombrables d'ensembles mesurables. 
De plus, comme $A \subset B_j$, et par $\sigma$-subadditivité de $v^*$
$$
v^*(A) 
\leq v^*(B_j) 
\leq \sum_{k=0}^{+\infty} v^*(P^j_k)
\leq \sum_{k=0}^{+\infty} v(P^j_k) \leq v^*(A) + 2^{-j}.
$$
L'intersection $B = \cap_j B_j$ est un ensemble mesurable qui recouvre $A$ 
et est contenu dans chaque $B_j$ ; par conséquent pour tout $j \in \N$,
$$
v^*(A) \leq v(B) \leq v(B_j) \leq v^*(A) + 2^{-j}.
$$
On en déduit donc que $A \subset B$ et $v^*(A) = v^*(B)$ avec $B$ mesurable. 

### Question 2 {.answer #answer-enm-2}
Notons au préalable que si $v^*(A) = +\infty$, alors $A$ est automatiquement 
mesurable. Dans le cas contraire ($v^*(A) < +\infty$)
l'ensemble $A$ est $v^*$-mesurable si et seulement si $v^*(B \setminus A) = 0$.
En effet, si $A$ est $v^*$-mesurable et de mesure finie, comme $A \subset B$, on a 
$$
v^*(B) = v^*(A \cap B) + v^*(A^c \cap B) = v^*(A) + v^*(B \setminus A) = v^*(B) + v^*(B \setminus A).
$$
Comme la mesure $v^*(A)$ est finie, $v^*(B \setminus A) = 0$.
Réciproquement, si $v^*(B \setminus A) = 0$, alors $B \setminus A$ (et donc $A$)
est mesurable.
En effet, pour tout ensemble $C$ de $\R^n$, on a d'une part 
$$
v^*(C) \leq v^*((B \setminus A) \cap C) + v^*((B \setminus A)^c \cap C) 
$$
par subbadditivité de $v^*$.
D'autre part, comme $(B \setminus A) \cap C \subset B \setminus A$, 
$v^*((B \setminus A) \cap C) \leq v^*(B \setminus A) = 0$. 
Par ailleurs, $C \supset (B \setminus A)^c \cap C$, donc
$$
v^*(C) \geq v^*((B \setminus A)^c \cap C) = v^*((B \setminus A) \cap C) + v^*((B \setminus A)^c \cap C).
$$
On a donc l'égalité $v^*(C) = v^*((B \setminus A) \cap C) + v^*((B \setminus A)^c \cap C)$ ;
l'ensemble $B \setminus A$ est donc mesurable, ainsi que $A = B \setminus (B \setminus A)$.

Mesure intérieure (hors-programme)
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-mi-1}
Pour montrer que la définition de $v_*(A)$ ne dépend pas du choix du pavé
$P$ contenant $A$, il suffit de prouver qu'on peut remplacer $P$ par un
pavé compact $P'$ contenant $P$ sans changer la valeur de $v_*(A)$ (pour toute
paire de pavés compacts on peut en effet trouver un pavé compact les contenant).

Comme les pavés compacts $P$ et $P'$ sont mesurables (au sens de Carathéodory,
pour la mesure extérieure $v^*$), l'ensemble $P' \setminus P$ l'est également 
; on a donc
$$
v^*(P') = v^*(P' \setminus P) + v^{*}(P) 
$$
et
$$
v^{*}(P' \setminus A)
=
v^*(P' \setminus P) + v^*(P \setminus A),
$$ 
ce qui établit
$$
v^*(P') - v{*}(P' \setminus A)
=
v^*(P) - v^{*}(P \setminus A).
$$

### Question 2 {.answer #answer-mi-2}
La fonction $v^*$ étant subadditive, on a
$$
v^*(P) \leq v^*(A) + v^*(P\setminus A)
$$
et donc $v_*(A) \leq v^*(A)$. Si $A$ est mesurable, l'inégalité initiale
devient une égalité et donc $v_*(A) = v^*(A)$. 

### Question 3 {.answer #answer-mi-3}
Montrons que la réciproque est également vraie. 
Soit $A$ un ensemble borné de $\R^n$ tel que 
$v_*(A) = v^*(A)$, et soit $B$ un ensemble quelconque de $\R^n$.
Nous cherchons à établir que $v^*(B) = v^*(A \cap B) + v^*(A^c \cap B)$.
Remarquons tout d'abord que si le pavé compact $P$ -- qui est mesurable -- 
contient $A$, on a
$$
v^*(B) = v^*(P \cap B) + v^*(P^c \cap B) \; ;
$$
si nous réussissons à établir que 
$$v^*(P \cap B) = v^*(A \cap (P \cap B)) + v^*(A^c \cap (P \cap B)),$$
on pourra alors conclure que
$$
\begin{split}
v^*(B) &= v^*(P \cap B) + v^*(P^c \cap B) \\
&= v^*(A \cap (P \cap B)) + v^*(A^c \cap (P \cap B)) + v^*(P^c \cap B) \\
&= v^*(A \cap B) + v^*(P \cap (A^c \cap B)) + v^*(P^c \cap (A^c \cap B)) \\
&= v^*(A \cap B) + v^*(A^c \cap B).
\end{split}
$$
Autrement dit, il nous suffit d'établir le résultat cherché quand $B$ est un
ensemble de $\R^n$ contenu dans le pavé compact $P$. 

Pour cela, nous exploitons les résultats de l'exercice "[Approximation par des
ensembles mesurables](#aem)". A l'ensemble $A$ on peut associer un sur-ensemble
$v^*$-mesurable $B$ tel que $v^*(A) = v^*(B)$ ; quitte à remplacer $B$ par
$P \cap B$, on peut également supposer que $B \subset P$. On a 
$$
v^*(P) = v^*(A) + v^*(P \setminus A) = v^*(B) + v^*(P \setminus B)
$$
et donc $v^*(P \setminus A) = v^*(P \setminus B)$. 
D'autre part
$$
\begin{split}
v^*(P) &= v^*(B) + v^*(P \setminus B) \\
&= v^*(A) + v^*(B \setminus A) + v^*(P \setminus B) \\
&= v^*(A) + v^*(B \setminus A) + v^*(P \setminus A) \\
\end{split}
$$
et donc $v^*(B \setminus A) = 0$. Par les résultats de l'exercice 
"[Approximation par des ensembles mesurables](#aem)", on en déduit que 
$A$ est mesurable.


Réferences
================================================================================

-->