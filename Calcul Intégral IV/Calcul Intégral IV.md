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

Ou mesure image et intégrale associée ? Ou mesures construites à partir
d'une mesure de référence et d'une fonction positive ?
Ou ensemble négligeable et impact sur l'intégrale ... et positivité et nullité ? 

### TODO -- Basique

  - Tribu $\mathcal{A}$ et mesure $\mu$ (définitions + application directe)

  - Mesures classiques 
    (de Lebesgue, de Dirac et de comptage)

  - Fonctions mesurables (définition + caractérisation comme des
    limites simples de fonction étagées mesurables)

  - ...

### TODO -- Standard

  - Intégrale des fonctions positives
    (propriétés caractéristiques)

  - Intégrale des fonctions signées 
    (définition)

  - Construction de nouvelles mesures et intégrales associées
    (mesure image, restrictions, mesure via l'intégrale)

  - Intégrale de Lebesgue et de Henstock-Kurzweil.

  - ...

### TODO -- Avancé

  - Construction de l'intégrale par rapport à $\mu$.

  - Tribu engendrée, Boréliens

  - Mesure produit, Fubini

  - ...

### TODO -- Hors-programme

  - Construction directe (sans l'intégrale de H.-K.) de la mesure de Lebesgue.

  - Démonstration des propriétés caractéristiques de l'intégrale.

  - Notion de mesure extérieure

  - Mesure de Hausdorff

  - ...


Mesure
================================================================================

### Tribu et espace mesurable {.definition}
Une *tribu* (ou *$\sigma$-algèbre*) $\mathcal{A}$ sur un ensemble $X$ est une 
collection d'ensembles de $X$ contenant l'ensemble vide et stable par passage 
au complémentaire et à l'union dénombrable :

  1. $\varnothing \in \mathcal{A}$.

  2. Si $A \in \mathcal{A}$, $A^c = X \setminus A \in \mathcal{A}$.

  3. Si pour tout $k \in \N$, $A_k \in \mathcal{A}$, alors
     $\cup_{k=0}^{+\infty} A_k \in \mathcal{A}.$

Un ensemble $A \in \mathcal{A}$ est dit *mesurable* 
(relativement à la tribu $\mathcal{A}$ ou $\mathcal{A}$-mesurable).
L'ensemble $X$ muni de $\mathcal{A}$ 
-- c'est-à-dire formellement la paire $(X,\mathcal{A})$ -- 
est un *espace mesurable*.

### Mesure et espace mesuré {.definition}
Une *mesure* $\mu$ sur un espace mesurable $(X, \mathcal{A})$
est une fonction 
$$
\mu: \mathcal{A} \to [0, +\infty]
$$ 
telle que $\mu(\varnothing)= 0$ et telle que pour toute suite
$(A_k)_{k\in \N}$ d'ensembles de $\mathcal{A}$ disjoints deux à deux, on ait
$$
\mu \left( \bigcup_{k=0}^{+\infty} A_k \right) = \sum_{k=0}^{+\infty} \mu(A_k) ;
$$
on dit que $\mu$ est *$\sigma$-additive*.
L'ensemble $X$ muni de $\mathcal{A}$ et $\mu$ 
-- c'est-à-dire formellement le triplet $(X, \mathcal{A}, \mu)$ -- 
est un *espace mesuré*.

### Exercice -- Les mesures sont (finiment) additives {.exercise}
Vérifier que tout mesure $\mu$ sur $(X, \mathcal{A})$ est additive, 
c'est-à-dire que si les ensembles $A_0, A_1, A_2, \dots, A_j$ de $\mathcal{A}$
sont deux à deux disjoints, alors
$$
\mu \left( \bigcup_{k=0}^{j} A_k \right) = \sum_{k=0}^{j} \mu(A_k).
$$

### Exercice -- Monotonie {.exercise}
Vérifier que tout mesure est *croissante* (on dit aussi *monotone*), 
c'est-à-dire que si $A, B \in \mathcal{A}$
et $A \subset B$, $\mu(A) \subset \mu(B)$.

### Exercice -- Cas dégénéré {.exercise} 
Existe-t'il des fonctions $\mu: \mathcal{A} \to [0, +\infty]$ qui soient
$\sigma$-additives mais telles que $\mu(\varnothing) \neq 0$ ?

### Exercice -- Ca commence par un $\mathbb{P}$ {.exercise}
Comment appelle-t'on une mesure $\mu$ sur $(X, \mathcal{A})$ telle que
$\mu(X) = 1$ ? Une fois que vous avez deviné, justifier la réponse.

### Mesure de Lebesgue
Les ensembles mesurables de $\R^n$ (au sens du chapitre "Calcul Intégral III"[^rapp])
forment une tribu qui est notée $\mathcal{L}(\R^n)$ et est appelée *tribu de Lebesgue*
sur $\R^n$. 
La fonction $v$ qui a un ensemble mesurable $A$ associe
$$
v(A) = \left|
\begin{array}{cl}
\displaystyle \int 1_A(x) \, dx & \mbox{si $1_A$ est intégrable au sens de Henstock-Kurzweil,}\\
+\infty & \mbox{sinon.}
\end{array}
\right.
$$
est une mesure nommé *mesure de Lebesgue* sur $\R^n$.

[^rapp]: c'est-à-dire les ensembles $A$ de $\R^n$ tels que pour tout pavé compact $P$ de 
$\R^n$, la fonction caractéristique $1_{A \cap P}$ est intégrable au sens de Henstock-Kurzweil.

### Démonstration {.proof}
La démonstration que les ensembles mesurables forment une tribu a été fournie 
dans le chapitre "Calcul Intégral II" dans $\R$ 
(cf. "Propriétés élémentaires" des ensembles mesurables) ; 
la démonstration dans le cas général de $\R^n$ est tout à fait similaire.
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
$$A = \cup_{k=0}^{+\infty} A_k \; \mbox{ et } \; f_j = 1_{\cup_{k=0}^j A_k}.$$ 
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
de $X$ (l'ensemble des sous-ensembles de $X$)
et soit $x \in X$. On appelle *mesure de Dirac* en $x$ la fonction 
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
Soit $X$ et $\mathcal{A} = \mathcal{P}(X)$ l'ensemble des parties
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

Intégrale
================================================================================

### Fonction mesurable
Soit $(X, \mathcal{A})$ un espace mesuré.
Une fonction $f: X \to [-\infty,+\infty]^n$ est *mesurable* 
(on trouvera aussi les terminologies *$\mathcal{A}$-mesurable* 
ou $\mu$-mesurable pour lever toute ambiguité) 
si l'image réciproque 
de tout fermé (ou de tout ouvert) de $\R^n$ par $f$ est un ensemble mesurable
(qui appartient à $\mathcal{A}$).

### Exercice -- Ensemble des parties de $X$ {.exercise}
Soit $X$ un ensemble et $\mathcal{A} = \mathcal{P}(X)$. A quelle condition
une fonction $f: X \to \mathbb{R}^n$ est-elle $\mathcal{A}$-mesurable ?

### Exercice -- Fonctions étagées {.exercise}
Soit $(X, \mathcal{A})$ un espace mesuré. A quelle condition
une fonction $f: X \to \mathbb{R}^n$ qui ne prend 
qu'un nombre fini de valeurs est-elle $\mathcal{A}$-mesurable ?

### Intégrale d'une fonction positive -- Propriétés caractéristiques
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré. L'intégrale par rapport à $\mu$
est l'unique application qui à toute application mesurable positive 
$f : X \to [0, +\infty]$ associe la grandeur notée
$$
\int f\mu = \int_X f(x) \, \mu(dx) \in [0, +\infty]
$$
et qui est caractérisée par

 1. Pour tout ensemble $A \in \mathcal{A}$,
    $$
    \int_X 1_A(x) \, \mu(dx) = \mu(A).
    $$

 2. L'intégrale de $f$ par rapport à $\mu$ 
    $$
    \int_X f(x) \mu(dx)
    $$
    est linéaire par rapport à $f$.

 3. Si la suite de fonctions mesurables $f_n:X \to [0, +\infty]$ est croissante 
    et converge simplement vers $f$, alors
    $$
    \int_X f(x) \, \mu(dx) = \lim_{n \to +\infty} \int_X f_n(x) \, \mu(dx).
    $$

### Intégrale d'une fonction signée
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré. 
Soit $f : X \to [-\infty, +\infty]$ une fonction mesurable.
On dit que $f$ est *intégrable* (par rapport à $\mu$ ou $\mu$-intégrable) 
si les intégrales des fonctions positives
$$
f_+ := \max(f, 0) \; \mbox{ et } f_- = -\min(f, 0) \;
$$
sont finies et on définit alors l'intégrale de $f$ par rapport à $\mu$
comme
$$
\int f \mu = \int_X f(x) \, \mu(dx) := \int_X f_+(x) \, \mu(dx) - \int_X f_-(x) \, \mu(dx) \in \R.
$$

### Exercice -- Absolue intégrabilité {.exercise}
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré. Montrer que si $f: X \to [-\infty,+\infty]$
est intégrable alors $|f|$ est également intégrable.

### Exercice -- Fonctions étagées {.exercise}
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré, soient $A_0, A_1, \dots, A_{n-1}$ 
des ensemble mesurables disjoints et $y_0, \dots, y_{n-1} \in \R \setminus \{0\}$. 
A quelle condition la fonction
$$
f = \sum_{j=0}^k y_k 1_{A_k}
$$
est-elle intégrable ? Quelle est alors la valeur de son intégrale ?

### Intégrale de Lebesgue et de Henstock-Kurzweil {.theorem}
Soit $f: \R^n \to \R$. La fonction $f$ est intégrable
par rapport à la mesure de Lebesgue $v$ si et seulement si 
$f$ est absolument intégrable ($f$ et $|f|$ sont intégrables) 
pour l'intégrale de Henstock-Kurzweil. Dans ce cas, les
deux intégrales sont égales.


### TODO 
Rah compliqué, il faut parler d'ensemble négligeable 
... et de l'impact sur l'intégrale. Bon, bascule en exo ?

### Exercice -- Fonctions à valeurs infinies {.exercise}
Soit $f: \R^n \to [-\infty,+\infty]$. Montrer que si $f$ est intégrable par 
rapport à la mesure de Lebesgue $v$ alors 
$$
v(f^{-1}(+\infty)) = v(f^{-1}(-\infty)) = 0.
$$
**TODO**


Mesure de Lebesgue -- Approche directe
================================================================================

Dans les volets précédents du "Calcul Intégral", 
nous avons défini le volume d'un pavé compact de $\R^n$ 
$$
P = [a_1, b_1] \times \dots \times [a_n, b_n]
$$
au moyen de la formule
$$
v(P) := (b_1  -a_1) \times \dots \times (b_n - a_n).
$$
L'intégrable de Henstock-Kurzweil nous permet de prolonger la fonction $v$ en 
une fonction définie pour tous les ensembles mesurables $A$ de $\R^n$,
par la relation
$$
v(A) = \int 1_A(x) \, dx
$$
si $1_A$ est intégrable et $v(A) = +\infty$ sinon.
Mais cette approche n'est pas totalement satisfaisante intellectuellement.
D'une part on peut considérer l'usage de l'intégrale comme un chemin
tortueux pour étendre $v$.
D'autre part on peut avoir l'impression
que cette approche -- qui ne permet pas de mesurer le volume de tout
ensemble de $\R^n$ -- n'atteint pas totalement son objectif ;
cette limitation pourrait être un artefact de la méthode choisie
plutôt qu'une limitation intrinsèque.
Dans cette section, nous allons donner une autre méthode, plus directe, 
due à Lebesgue et Carathéodory[^autz],
qui nous permettra de définir la mesure (extérieure) du volume de tout ensemble 
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
nous généralisons la méthode utilisée pour définir les ensembles négligeables 
(de volume nul) : nous considérons l'ensemble des collections dénombrables
de pavés recouvrant ce sous-ensemble et nous utilisons chacun des ces 
recouvrements pour produire une estimation (supérieure) du volume
de l'ensemble. Formellement :

### Mesure extérieure de Lebesgue {.definition #mel}
On appelle *mesure extérieure de Lebesgue* dans $\R^n$ la fonction
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

--------------------------------------------------------------------------------


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
$v^*$ coïncide avec $v$ dont la définition exploite l'intégrable de Henstock-Kurzweil.
Un simple calcul intégral fournit alors le résultat.

On peut croire que le point faible de notre raisonnement est la préservation
de la valeur de $v^*(A)$ par translation et rotation ; s'il est facile d'établir
que lorsque $B$ se déduit de $A$ par une translation, alors $v^*(A) = v^*(B)$, 
on peut douter du résultat pour les rotations. 
Après tout, la définition de $v^*(A)$ fait appel
à des rectangles qui sont parallèles aux axes, une propriété qui n'est pas
conservée par rotation. 
Mais si le résultat n'est pas évident, il s'avère pourtant que
la mesure $v^*$ est bien invariante par
rotation (cf. [@Hun11, section 2.8]).

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
Elle est même $\sigma$-sous-additive : si $A_k$, $k \in \N$ sont des
sous-ensembles de $\R^n$, 
$$
v^*\left(\bigcup_{k=0}^{+\infty} A_k\right)
\leq \sum_{k=0}^{+\infty} v^*\left(A_k\right).
$$

Cette propriété est une caractéristique des *mesures extérieures* :

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
la trace de $\mu^*$ sur un ensemble $A$ de $X$, définie pour tout
sous-ensemble $B$ de $X$ par
$$\mu^*|_A(B) = \mu^*(B \cap A),$$
alors l'ensemble $A$ est $\mu^*$ mesurable si et seulement si
$$
\mu^* = \mu^*|_A + \mu^*|_{A^c}.
$$


### Mesure associée à une mesure extérieure {.theorem}
Soit $X$ un ensemble et $\mu^*$ une mesure extérieure sur $X$.
La collection $\mathcal{A}$ des ensembles $\mu^*$-mesurables de $X$
est une tribu sur $X$, et la restriction $\mu$ de $\mu^*$ à 
$\mathcal{A}$ est une mesure sur $X$.

### Démonstration {.proof}
Cf. [@Hun11, théorème 2.9, pp. 15-17].

### {.remark .ante}
La spécialisation de ce procédé au cas de la mesure extérieure de Lebesgue,
produit la mesure de Lebesgue.

### Mesure de Lebesgue {.theorem .definition}
La "[mesure extérieure de Lebesgue](#mel)" $v^*:\mathcal{P}(\R^n) \to [0, +\infty]$
précédemment définie est bien une mesure extérieure sur $\R^n$.
On appelle *tribu de Lebesgue* et on note $\mathcal{L}(\R^n)$ la collection 
des ensembles $v^*$-mesurables (au sens de Caratheodory) ; 
la mesure $v: \mathcal{L}(\R^n) \to [0, +\infty]$ qui lui est associée 
est appelée *mesure de Lebesgue sur $\R^n$*. 

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

<!--
### {.post}
Nous renvoyons le lecteur intéressé par la preuve que la mesure de Lebesgue
prolonge bien la mesure de volume des pavés compacts à [@Hun11, section 2.2].
-->

### {.remark .ante} 
On admettra également sans preuve le résultat suivant, qui montre que la notation
"$v$" que nous avons employé deux fois est dépourvue d'ambiguité :

### Mesure de Lebesgue et intégrale de Henstock-Kurzweil
La tribu $\mathcal{L}(\R^n)$ des ensembles $v^*$-mesurables 
au sens de Caratheodory coïncide avec la tribu des ensembles mesurables 
définis au moyen de l'intégrale de Henstock-Kurzweil. La mesure de Lebesgue
$v: \mathcal{L}(\R^n) \to [0, +\infty]$ vérifie
$$
v(A) = \int 1_A(x) \, dx
$$ 
si $1_A$ est intégrable au sens de Henstock-Kurzweil et
$v(A)= +\infty$ sinon.

<!--
TODO -- Mesure de grandeurs
================================================================================

### TODO ; refocus Lebesgue directement.

Il est possible même au sein d'un espace unique comme $\R^3$ de vouloir
mesurer différentes grandeurs attachées à un ensemble $A$. 
On peut ainsi vouloir compter le nombre de points que contient $A$
(sa "mesure de comptage"), sa longueur, sa surface ou encore son volume.

L'exemple du volume a déjà été traité avec l'intégrale de Henstock-Kurzweil
dans $\R^3$. L'exemple de la surface, a été partiellement traité, 
dans un cas très limité (la frontière de compacts à bord réguliers) 
et au prix d'un processus complexe
permettant de se ramener à des calculs d'intégrale dans $\R^2$.
Il est en fait possible de traiter ces quatres type de grandeurs, 
ces quatre *mesures* différentes de façon similaire, et sans requérir
à la notion d'intégrale. 

Détaillons tous d'abord le cas de la mesure du volume dans $\R^3$.
Le volume de la sphère de même diamètre qu'un ensemble $B$ arbitraire 
est donnée par
$$
\frac{4 \pi}{3} \left(\frac{\mathrm{diam} \, B}{2}\right)^3.
$$
On peut alors calculer pour tout $\delta > 0$ estimer le volume d'un ensemble
$A$ à partir de tous les recouvrements dénombrables de $A$ par des ensembles
de diamètre inférieur ou égal à $\delta$ par
$$
\mathcal{H}^3_{\delta}(A) =
\inf \left\{
\sum_{j=1}^{+\infty} \frac{4\pi}{3} \left(\frac{\mathrm{diam} \, B_j}{2}\right)^k
\; \left| \vphantom{\left(\frac{\mathrm{diam} \, B_j}{2}\right)^k} \right. \; 
A \subset \sum_{j=1}^{+\infty} B_j, \, \mathrm{diam} \, B_j \leq \delta 
\right\},
$$
puis passer à la limite sur $\delta$. 
Il s'avère que le résultat
-- on parle de *mesure de Hausdorff* de dimension $3$ de $A$ --
est identique à l'approche par l'intégrale de Henstock-Kurzweil quand
l'ensemble $A$ est mesurable :
$$
\mathcal{H}^3(A) = \int_A \, dx.
$$
On pense a priori avoir amélioré notre approche pour définir le volume d'un
ensemble $A$, puisque l'on a supprimé la limitation que l'ensemble $A$ soit 
mesurable. Toutefois, la mesure $\mathcal{H}^3$ qui résulte de cette définition
perd une propriété importante qui est implicitement attachée à toutes les
grandeurs que nous avons cité.

Ce problème sera mis en évidence par le résultat suivant :



Notons $A_1, \dots, A_n$ la partition de la sphère initiale
et $B_1, \dots, B_n$ leurs images après rotation et translation.
Comme par construction la mesure $\mathcal{H}^3$ est invariante par
rotation et translation, il semble que l'on doive avoir
$$
\mathcal{H}^3(S) = \sum_{i=1}^n \mathcal{H}^3(A_i)
= \sum_{i=1}^n \mathcal{H}^3(B_i) = \mathcal{H}^3(S_1) + \mathcal{H}(S_2)
=2 \times \mathcal{H}^3(S),
$$ 
une contradiction puisque $\mathcal{H}^3(S) = 4\pi/3$.

**TODO** négation de l'additivité, comment la retrouver (ensembles qui
"splittent" proprement la mesure) et on retombe sur les ensembles
mesurables.

Généralisation de la démarche : le procédé utilisée, qq soit la mesure
élémentaire, génère une fct sous-additive appelée mesure extérieures. 
Les ensembles qui splittent proprement la mesure sont appelés ensembles
mesurables, la restriction de la mesure à ces ensembles est additive,
et même $\sigma$-additive.

Et on "reboote" la théorie abstraite de la mesure à ce point.

--------------------------------------------------------------------------------

$$
\mathcal{H}^k_{\delta}(A) 
= 
\inf \left\{
\sum_{j=1}^{+\infty} \alpha(k)\left(\frac{\mathrm{diam} \, B_j}{2}\right)^k
\; \left| \vphantom{\left(\frac{\mathrm{diam} \, B_j}{2}\right)^k} \right. \; 
A \subset \sum_{j=1}^{+\infty} B_j, \, \mathrm{diam} \, B_j \leq \delta 
\right\}
$$
où $\alpha(k)$ est le volume de la $k$-sphère unité dans $\R^k$([^G])
$$
\alpha(k) = \int_{\R^k} 1_{S_k}(x) \, dx 
\; \mbox{ où } \; 
S_k = \left\{x \in \R^k \; | \; x_1^2 + \dots + x_k^2 \leq 1 \right\}.
$$

La mesure de Hausdorff $\mathcal{H}^k(A)$ de dimension $k$ de l'ensemble
$A \subset \R^n$ est définie par 
$$
\mathcal{H}^k(A) = \lim_{\delta \to 0} \mathcal{H}^k_{\delta}(A).
$$

[^G]: on a $$\alpha(k) = \frac{\pi^{k/2}}{\Gamma \left( \frac{k}{2}+1 \right)} 
\; \mbox{ avec } \; 
\Gamma(x) = \int_0^{+\infty} e^{-t} t^{x-1}\, dt.$$ 
La fonction $\Gamma$ est caractérisée pour des valeurs entières et
demi-entières par $\Gamma(1/2) = \sqrt{\pi}$, $\Gamma(1) = 1$ et généralement
par $\Gamma(x+1)= x\Gamma(x)$.
-->

Mesure et intégrale
================================================================================

### Ensemble négligeable {.definition}
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré. Un ensemble $N \subset X$
est *$\mu$-négligeable* s'il existe un ensemble mesurable $A \in \mathcal{A}$ 
tel que $N \subset A$ et $\mu(A) = 0$.

### Presque partout {.definition}
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré. Une propriété $P$ dépendant 
d'un $x \in X$ est vraie *presque partout* si l’ensemble des éléments $x$ 
où elle est fausse est un ensemble négligeable.

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

### Fonction étagée {.definition}
On appelle *fonction étagée* <!-- (ou *fonction simple*) --> toute fonction $f: X \to Y$ 
qui ne prenne qu'un nombre fini de valeurs distinctes 
(ou telle que l'image réciproque de $Y$ par $f$ soit finie).

### TODO -- retarder l'apparition du résultat suivant ?

### Fonction mesurable
Soit $\mathcal{A}$ une tribu sur l'ensemble $X$.
Une fonction $f: X \to [-\infty, +\infty]$ est
$\mathcal{A}/$Borel- mesurable si et seulement si $f$ est la limite
simple de fonctions étagées $X \to \R$ qui soient $\mathcal{A}$/Borel-mesurables.

### TODO -- Démonstration {.proof}

### Fonction étagées mesurables
Soit $(X, \mathcal{A})$ un espace mesurable.
Une fonction $f: X \to \R$ est simple et mesurable 
si et seulement s'il existe une collection finie d'ensembles mesurables
$A_0, \dots, A_{n-1} \in \mathcal{A}$ et de valeurs 
$y_0, \dots, y_{n-1} \in \R$ telles que
$$
f = \sum_{k=0}^{n-1} y_k 1_{A_k}. 
$$

### {.post}
La preuve de ce résultat montre qu'il est possible d'être plus prescriptif 
si nécessaire sur les ensembles $A_k$ et les valeurs $y_k$ : 
une fonction est en effet simple et mesurables si et seulement 
s'il existe une collection finie d'ensembles mesurable **disjoints**
$A_0, \dots, A_{n-1} \in \mathcal{A}$ et de valeurs **distinctes et non nulles**
$y_0, \dots, y_{n-1} \in \R$ telles que
$$
f = \sum_{k=0}^{n-1} y_k 1_{A_k}. 
$$

### Démonstration {.proof}
Soit $f: X \to \R$ une fonction simple ;
il existe donc des réels $y_0, \dots, y_{n-1}$ tels que
$f(X) = \{y_0,\dots, y_{n-1}\}.$
On a alors
$$f = \sum_{k=0}^{n-1} y_k 1_{A_k} \, \mbox{ avec } \, A_k = f^{-1}(y_k).$$ 
Si de plus $f$ est mesurable, les singletons de $\R$ étant (Borel-)mesurables 
(car fermés), les ensembles $A_k$ sont nécessairement ($\mathcal{A}$-)mesurables.

Réciproquement, si $f$ est de la forme $f = \sum_{k=0}^{n-1} y_k 1_{A_k}$ où
les ensembles $A_k$ sont mesurables, il est clair que la fonction $f$ est simple. 
En considérant les ensembles 
-- mesurables -- $B_k$ définis par $B_0 = A_0$ et $B_{k+1}= A_{k+1} \setminus A_k$
on obtient une somme $\sum_k w_k 1_{B_k}$ du même type mais basée sur des 
ensembles disjoints $B_k$. En faisant l'union $C_j$ des $B_k$ qui correspondent à
des valeurs $z_j = w_k$ identiques, on peut de plus s'assurer d'avoir une somme
de la forme $f = \sum_j z_j 1_{C_j}$ où les valeurs $z_j$ sont distinctes et les $C_j$ sont
mesurables. 
Le cas échéant, si l'un des $z_j$ est nul, on peut même omettre le terme correspondant de la somme.
Il devient maintenant clair que $f$ est également mesurable : si $A$ est un
ensemble mesurable de $\R$, l'image réciproque de $A$ par $f$ est l'union
d'une sous-collection des $C_j$ ($C_j$ étant inclus dans la collection 
si et seulement si $z_j \in A$)
et si $0 \in A$, de $X \setminus \cup_j C_j$.

### Intégrale d'une fonction étagée
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré et 
$f: X \mapsto \left[0, +\infty\right[$ une fonction étagée positive et mesurable.
On appelle *intégrale de Lebesgue de $f$ relativement à la mesure $\mu$*
la grandeur positive (finie ou infinie)
$$
\int f \mu := \int_X f(x) \mu(dx) := \sum_{y \in \left[0, +\infty\right[} y \times \mu(f^{-1}(y))),
$$
avec la convention que $0 \times (+\infty) = 0$.
Si $A_0, \dots, A_{n-1} \in \mathcal{A}$ et
$y_0, \dots, y_{n-1} \in \left[0, +\infty\right[$,
alors cette définition se traduit par
$$
f = \sum_{k=0}^{n-1} y_k 1_{A_k} \rightarrow
\int f \mu = \sum_{k=0}^{n-1} y_k \times \mu(A_k).
$$

----

### {.post}
A noter que dans la somme définissant l'intégrale, si $y$ ne fait pas partie
des valeurs prises par $f$, alors $\mu(f^{-1}(y)) = \mu(\varnothing) = 0$. 
Comme $f$ est supposée simple, cette somme est donc composée d'un nombre 
fini de termes non nuls. 
Si l'on veut mettre cela mieux en évidence,
on peut remplacer la somme dans l'énoncé ci-dessus par 
$$
\sum_{y \in f(X)} y \times \mu(f^{-1}(\{y\})),
$$
voire
$$
\sum_{y \in f(X) \setminus \{0\}} y \times \mu(f^{-1}(\{y\}))
$$
ce qui permet également de se dispenser de la convention $0 \times (+\infty) = 0$.

### Intégrale d'une fonction positive
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré et 
$f: X \to [0, +\infty]$ une fonction mesurable.
Soit $\mathcal{F}(f)$ la collection des fonctions étagées positives (à valeurs 
finies) et mesurables qui soient inférieures à $f$.
On appelle *intégrale de Lebesgue de $f$ relativement à la mesure $\mu$*
la grandeur positive (finie ou infinie)
$$
\int f \mu := \int_X f(x) \mu(dx) := \sup_{g \in \mathcal{F}(f)} \int g \mu.
$$

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

### Intégrales finies, infinies et indéfinies {.post}
Une fonction positive peut avoir une intégrale bien définie --
il faut et il suffit qu'elle soit mesurable -- sans être pour autant 
intégrable. Elle est intégrable si et seulement si elle est mesurable et que 
son intégrale est finie. 
Pour les fonctions positives, la formule
$$
\int f \mu < + \infty
$$
signifera donc à la fois "l'intégrale est bien définie" (mesurable)
et "l'intégrale est finie" (c'est-à-dire : la fonction est intégrable).
Pour les fonctions signées par contre, il est nécessaire d'être
plus strict et l'intégrale n'est définie que pour les fonctions intégrables.
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
est un concept très proche). Mais à ce stade nous n'allons pas explorer cette
piste.

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
pour l'intégrale de Henstock-Kurzweil. Dans ce cas, les
deux intégrales sont égales.

Propriétés de l'intégrale
================================================================================

### {.ante .remark}
On mettra en avant dans cette section sur les propriétés de l'intégrale de
fonctions positives ; les propriétés correspondantes de l'intégrale de fonctions
signées s'en déduisent simplement.

### Linéarité {.theorem #lin}
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré.
L'intégrale par rapport à $\mu$ de fonctions positives (à valeurs finies ou
infinies) est homogène et additive :
si $\lambda \in \left[0, +\infty\right[$ et $f, g: X \to [0, +\infty]$ sont deux
applications $\mu$-mesurables,  
$$
\int (\lambda f) \mu = \lambda \int f\mu
\; \mbox{ et } \;
\int (f + g) \mu = \int f \mu + \int g \mu.
$$

### TODO -- Pb causalité

La preuve utilise la version "concrête" de l'intégrale, par les suites,
qui n'est vue que plus tard. Même chose pour TCM. Au minimum, en ante,
pointer sur cette inversion.

### Démonstration {.proof}
La preuve de l'homogénéité est immédiate si $\lambda =0$ ; 
dans le cas contraire, l'application
$$
h \in \mathcal{F}(f) \mapsto \lambda h \in \mathcal{F}(\lambda f)
$$
qui associe à une application $h$ mesurable, étagée et inférieure 
à $f$ l'application $\lambda h$ qui est mesurable, étagée et 
inférieure à $\lambda f$ est bijective.
Par conséquent,
$$
\begin{split}
\int (\lambda f) \mu &=
\sup_{h \in \mathcal{F}(\lambda f)} \sum_{y \in \left[0, +\infty\right[} y \times \mu(g^{-1}(y)) \\
&=
\sup_{k \in \mathcal{F}(f)} \sum_{y \in \left[0, +\infty\right[} y \times \mu((\lambda k)^{-1}(y)) \\
&=
\sup_{k \in \mathcal{F}(f)} \sum_{z \in \left[0, +\infty\right[} (\lambda z) \times \mu((\lambda k)^{-1}(\lambda z)) \\
&=
\lambda \sup_{k \in \mathcal{F}(f)} \sum_{z \in \left[0, +\infty\right[} z \times \mu(k^{-1}(z)) \\
&= \lambda \int f \mu.\\
\end{split}
$$

L'application
$$
(h, k) \in \mathcal{F}(f) \times \mathcal{F}(g) \mapsto h+k \in \mathcal{F}(f + g)
$$
est également bien définie mais il n'est pas immédiat qu'elle soit bijective.
Mais heureusement, [la définition alternative, concrête, à l'intégrale d'une fonction positive](#ifpII)
nous fournit des suites croissantes de fonctions positives, mesurables et étagées
$f_k$ et $g_k$, convergeant respectivement vers $f$ et $g$. Pour ces suites,
$$
\lim_{k \to + \infty} \int f_k \mu = \int f\mu
\; \mbox{ et } \;
\lim_{k \to + \infty} \int g_k \mu = \int g\mu.
$$
La suite $h_k = f_k + g_k$ est croissante, composée de fonctions positives
étagées et mesurable ; elle converge simplement vers $f+g$, par conséquent,
par [le théorème de convergence monotone](#TCM), on a
$$
\int (f+g) \mu = \lim_{k \to +\infty} \int (f_k + g_k) \mu. 
$$
On pourra aisément se convaincre que l'intégrale des fonctions
positives étagées et mesurables est additive ; par conséquent,
$$
\begin{split}
\int (f+g) \mu &= \lim_{k \to +\infty} \int f_k \mu + \int g_k \mu \\
&= \lim_{k \to +\infty} \int f_k \mu + \lim_{k \to +\infty} \int g_k \mu \\
&= \int f\mu + \int g \mu. \\
\end{split}
$$

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
$\{x \in X \; | \; f(x) > 0\}$ -- c'est-à-dire $f^{-1}(\left]0, +\infty\right[)$ -- 
est mesurable par construction, "négligeable" est bien équivalent à "de mesure nulle"
le concernant.

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

<!--
[^cup]: l'ensemble $\left]0, +\infty\right]$ peut être partitionné de façon
dénombrable comme
  $$
  \left]0, +\infty\right] =
  \left[1, +\infty \right] \cup
  \bigcup_{n=0}^{+\infty} \left[2^{-(n+1)},2^{-n}\right[
  $$
ce qui induit directement la décomposition suivante de $f^{-1}(\left]0, +\infty\right])$
en une collection dénombrable d'ensemble disjoints mesurables
  $$
  f^{-1}(\left]0, +\infty\right]) =
  f^{-1}(\left[1, +\infty \right]) \cup
  \bigcup_{n=0}^{+\infty} f^{-1}\left( \left[2^{-(n+1)},2^{-n}\right[ \right) 
  $$
  Par $\sigma$-additivité de $\mu$, on a donc
  $$
  \mu\left(f^{-1}\left(\left]0, +\infty\right]\right)\right) =
  \mu(f^{-1}(\left[1, +\infty \right])) 
  + 
  \sum_{n=0}^{+\infty} \mu \left( f^{-1}\left(  \left[2^{-(n+1)},2^{-n}\right[   \right)\right)
  $$
  et par conséquent
  $$
  \lim_{n \to + \infty} \mu\left(f^{-1}\left([2^{-n}, +\infty]\right)\right)
  = 
  \lim_{n \to + \infty}
  \mu(f^{-1}(\left[1, +\infty \right])) 
  + 
  \sum_{n=0}^{+\infty} \mu \left( f^{-1}\left(  \left[2^{-(n+1)},2^{-n}\right[   \right)\right)
  =
  \mu\left(f^{-1}\left(\left]0, +\infty\right]\right)\right).
  $$
-->

Notons $A_n = f^{-1}([2^{-n}, +\infty])$ ; c'est un ensemble
mesurable de mesure positive. La fonction $2^{-n}1_{A_n}$ est positive, étagée, 
mesurable et inférieure à $f$. On a donc
$$
0 < 2^{-n}\mu(A_n) = \int 2^{-n}1_{A_n} \mu \leq \int f\mu.
$$
L'intégrale de $f$ par rapport $\mu$ est donc strictement positive.

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
La positivité et la linéarité de l'intégrale entraînent
$$
\int f_0 \mu \leq \dots \leq \int f_k \mu \leq \dots \int f_k \mu \leq \int f \mu.
$$
et donc
$$
\lim_{k\to+\infty} \int f_k\mu \leq \int f\mu.
$$

Soit $g: X \to \left[0, +\infty\right[$ une fonction étagée mesurable, donc
de la forme
$$
g(x) = \sum_{j=0}^{n-1} y_j 1_{A_j}
$$
avec $y_j \in \left[0, +\infty\right[$ et $A_j$ mesurable.
Soit $t \in \left[0, 1\right[$. Comme la suite des $f_k$ est croissante et 
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
\int f_k \mu \geq \int t g 1_{E_k} = t\sum_{j=0}^{n-1} y_j \mu(A_j \cap E_k).
$$
et comme $\cup_{k=0}^{+\infty} A_j \cap E_k = A_j$, par $\sigma$-additivité
de $\mu$,
$$
\lim_{k\to +\infty} \int f_k \mu \geq 
t\lim_{k\to +\infty} \sum_{j=0}^{n-1} y_j \mu(A_j \cap E_k) = 
t \left(\sum_{j=0}^{n-1} y_j \mu(A_j)\right) = t \int g\mu. 
$$
Cette inégalité étant valable pour tout $t \in \left[0, 1\right[$
et pour toute fonction positive étagée et mesurable $g$, on en déduit
$$
\lim_{k\to +\infty} \int f_k \mu \geq \sup_{g \in \mathcal{F}(f)}\int g\mu
= \int f\mu.
$$

### {.remark .ante}
[Le théorème de convergence monotone](#TCM) fournit une alternative concrète
à la construction initiale de l'intégrale.

### Intégrale d'une fonction positive II {.theorem #ifpII}
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré et 
$f: X \to [0, +\infty]$ une fonction mesurable.
Il existe une suite croissante de fonctions $f_k$ étagées positives finies et 
mesurables, convergeant simplement vers $f$ ; pour toute suite de ce type, 
$$
\lim_{k\to +\infty} \int f_k \mu = \int f \mu
$$

### Démonstration {.proof}
Soit $\varepsilon_k \geq 0$ une suite de valeurs telles que
$$
\lim_{k\to +\infty} \varepsilon_k  = 0 
\; \mbox{ et } \;
\sum_{k=0}^{+\infty} \varepsilon_k = +\infty.
$$
La suite des fonctions $f_k$ définies par $f_0=0$, puis
$$
f_{k+1} = f_{k} + \varepsilon_k 1_{E_k} \, \mbox{ où } \,
E_k = \{x \in X \, | \, f(x) \geq f_k(x) + \varepsilon_k\}
$$
est croissante, et composée de fonctions étagées positives et mesurables.
Sa limite simple est la fonction $f$. 
Par [le théorème de convergence monotone](#TCM), 
$$
\lim_{k \to +\infty} \int f_k \mu  = \int f \mu
$$
pour toute suite de ce type.

### Théorème de convergence dominée {.theorem #TCD}
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré et
$f_k: X \to [0, +\infty]$, $k \in \N$, une suite de fonctions 
mesurables, dominées par la fonction intégrable $g: X \to [0, +\infty]$
c'est-à-dire telles que pour tout tout $k \in \N$ et tout $x \in X$,
$$
0 \leq f_k(x) \leq g(x) \; \mbox{ et } \; \int_X g \mu < +\infty.
$$
Si la suite des $f_k$ à une limite simple $f: X \to [0, +\infty]$,
c'est-à-dire si pour tout $x \in X$,
$f_k(x) \to f(x) \mbox{ quand } k \to +\infty,$
alors
$$
\lim_{k \to +\infty} \int f_k \mu  = \int f \mu.
$$

### TODO -- Démonstration {.proof}

Produit de mesures
================================================================================



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

Annexe
================================================================================

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

-----

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


Exercices
================================================================================

Anagramme {.question #BT}
--------------------------------------------------------------------------------

Quel est l'anagramme de "Banach-Tarski" ?

Mesures de Dirac
--------------------------------------------------------------------------------

Soit $x \in \R$. Soit $\delta_x^*: \mathcal{P}(\R) \to [0, +\infty]$ l'application
définie par
$$
\delta_x^*(A) = \left|
\begin{array}{rl}
1 & \mbox{si $x \in A$,} \\
0 & \mbox{sinon.}
\end{array}
\right.
$$

### Question 1 {.question #d1}
Montrer que $\delta^*_x$ est une mesure extérieure sur $\R$.

### Question 2 {.question #d2}
Déterminer les ensembles mesurables associés.

### {.remark}
On note $\delta_x$ la mesure correspondante que l'on appelle
*mesure de Dirac en $x$*.

### Question 3 {.question #d3}
Qu'est-ce qu'un ensemble négligeable sur $\R$ pour la mesure de Dirac en $x$ ?
A quelle condition une fonction $f :\R \to \R$ est-elle nulle presque partout ?

### Question 4 {.question #d4}
A quelle condition la fonction $f: \R \to [-\infty, +\infty]$ est-elle 
$\delta_x$-mesurable ? $\delta_x$-intégrable ? Calculer alors
$$
\int f \delta_x.
$$

### TODO Question 5 {.question #d5}
qqch sur la mesure de comptage 

Approximation par des ensembles mesurables
--------------------------------------------------------------------------------

Soit $A$ un sous-ensemble de $\R^n$.

### Question 1 {.question #enm-1}
Montrer qu'il existe un ensemble $v^*$-mesurable $B$ contenant $A$ et tel que
$v^*(A) = v^*(B)$.

### Question 2 {.question #enm-2}
A quelle condition portant sur $v^*(B \setminus A)$ l'ensemble $A$ est-il 
$v^*$-mesurable ?

Mesure intérieure
--------------------------------------------------------------------------------

Soit $A$ un ensemble borné de $\R^n$ et $P$ un pavé compact de $\R^n$
contenant $A$.
On appelle *mesure intérieure de $A$* la grandeur
$$
v_*(A) = v^*(P) - v^*(P \setminus A).
$$

### Question 1 {.question #mi-1}
Montrer que la définition de $v_*(A)$ ne dépend pas du choix du pavé $P$.

### Question 2 {.question #mi-2}
Montrer que $v_*(A) \leq v^*(A)$, avec égalité si $A$ est $v^*$-mesurable.

### Question 3 {.question #mi-3}
Montrer la réciproque de la question précédente : si $A \subset \R^n$ est borné
et $v_*(A) = v^*(A)$, alors $A$ est $v^*$-mesurable.

Mesure image 
--------------------------------------------------------------------------------

Soit $(X, \mathcal{A}, \mu)$ un espace mesuré et $h: X \to Y$ une application.
On définit la collection 
$$
\mathcal{B} = \{B \subset Y \, | \, h^{-1}(B) \in \mathcal{A}\}
$$
et la fonction $\mu \circ h^{-1}: \mathcal{B} \to [0, +\infty]$ par
$$
\mu \circ h^{-1}(B) = \mu(h^{-1}(B)).
$$

### Question 1 {.question #mi-1}
Montrer que $\mathcal{B}$ est une tribu.

### Question 2 {.question #mi-2}
Montrer que $\mu \circ h^{-1}$ est une mesure sur $\mathcal{B}$ ; 
on l'appelle la *mesure image de $\mu$ par $h$*.

### Question 3 {.question #mi-3}
Montrer que la fonction $f:Y \to \R$ est $\mu \circ h^{-1}$-intégrable 
si et seulement si $f \circ h$ est $\mu$-intégrable et qu'alors,
$$
\int_Y f \, (\mu \circ h^{-1})(dx) = \int_X (f \circ h) \mu(dx).
$$

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



Complétion d'une mesure {#complétion}
--------------------------------------------------------------------------------

Soit $(X, \mathcal{A}, \mu)$ un espace mesuré. 
On note $A \ds B$ la différence symétrique
de deux sous-ensembles $A$ et $B$ de $X$ l'ensemble, 
définie par
$$
A \ds B = (A \setminus B) \cup (B \setminus A) = (A \cap B^c) \cup (A^c \cap B).
$$

### Question 1 {.question #cm-1}
Caractériser au moyen de la différence symétrique $\ds$ 
la tribu -- notée $\overline{\mathcal{A}}$ -- engendrée par 
l'union entre $\mathcal{A}$ et la collection $\mathcal{N}$ 
des ensembles négligeables pour $\mu$ :
$$
\mathcal{N} = 
\{
N \subset X 
\; | \;
\mbox{il existe $A \in \mathcal{A}$ tel que $N \subset A$ et $\mu(A) = 0$.} 
\}.
$$

### Question 2 {.question #cm-2}
Montrer que la mesure $\mu$ peut être étendue d'une façon unique en une
mesure $\overline{\mu}$ définie sur $\overline{\mathcal{A}}$.

<!--

TODO -- Fonctions mesurables
--------------------------------------------------------------------------------

(pour des mesures "exotiques" ... mesure de comptage, densité uniforme,
sur $[0, 1]$, mesure de dirac en $0$ ?)

TODO -- Mesures de Hausdorff
--------------------------------------------------------------------------------

Que faire ? Définir le volume, la surface et la longueur dans $\R^3$, 
montrer que l'on a affaire à des mesures extérieures ?

Travailler sur une mesure de Hausdorff "rectangulaire" plutôt que sur 
la "vraie" ?

Ou mesure de Hausdorff de dimension 1/2 dans $\R$, telle que présentée
dans <https://terrytao.wordpress.com/2009/05/19/245c-notes-5-hausdorff-dimension-optional/> ?

TODO -- Extension
--------------------------------------------------------------------------------

Tribu générée à partir d'un anneau (e.g. ens. des intervalles $\left[a,b\right[$),
extension d'une prémesure ? Problématique de non-unicité ? Unicité sous
caractère $\sigma$-fini ? cf <https://mpaldridge.github.io/teaching/ma40042-notes-06.pdf> 


TODO -- Mesure produit
--------------------------------------------------------------------------------

### Question 1 
Montrer que $\mathcal{B}(\R^{m+n}) = \mathcal{B}(\R^m) \otimes \mathcal{B}(\R^n)$.

### Question 2
Est-ce que $\mathcal{L}(\R^{m+n}) = \mathcal{L}(\R^m) \otimes \mathcal{L}(\R^n)$ ?


TODO -- Intégrale itérée
--------------------------------------------------------------------------------

Exemple classique (e.g. <https://en.wikipedia.org/wiki/Fubini's_theorem#Failure_of_Fubini's_theorem_for_non-integrable_functions>)
de calcul et comparaison de 
$$
\int_0^1 \left( \int_0^1 \frac{x^2 - y^2}{(x^2 + y^2)^2}\, dy\right) \, dx
$$
et
$$
\int_0^1 \left( \int_0^1 \frac{x^2 - y^2}{(x^2 + y^2)^2}\, dx\right) \, dy.
$$

### TODO 
check / version conditionnellement continue de Fubini. 
Pourquoi ça ne marche pas ?
-->


Solutions
================================================================================

Anagramme {.answer #answer-BT}
--------------------------------------------------------------------------------

"Banach-Tarski Banach-Tarski".

Mesures de Dirac
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-d1}
Le réel $x$ n'appartient pas à l'ensemble vide, 
donc $\delta^*_x(\varnothing) = 0$. Si $A \subset B \subset \R$
et si $x \in A$, alors $x \in B$ ; on a donc 
$\delta^*_x(A) \leq \delta^*_x(B)$. Finalement, 
si $A = \cup_{k=0}^{+\infty} A_k$ et si $x \in A$, alors il existe un $k \in \N$
tel que $x \in A_k$, donc $1 \leq \sum_{k=0}^{+\infty} \delta_x^*(A_k)$ ;
en conséquence, $\delta_x^*(A) \leq \sum_{k=0}^{+\infty} \delta_x^* (A_k)$.
La fonction $\delta_x^*$ est donc une mesure extérieure sur $\R$.

### Question 2 {.answer #answer-d2}
Soient $A, B \in \mathcal{P}(\R)$. Si $x \not \in B$, alors
$x \not \in A\cap B \subset B$ et $x \not \in A^c \cap B \subset B$, donc
$$
\delta_x^*(A \cap B) + \delta_x^*(A^c \cap B) = \delta_x^*(B) = 0.
$$
Dans le cas contraire, $x$ appartient $A\cap B$ ou à $A^c \cap B$, mais
pas au deux ensembles simultanément car ils sont disjoints ; on a donc
$$
\delta_x^*(A \cap B) + \delta_x^*(A^c \cap B) = \delta_x^*(B) = 0.
$$
Tous les sous-ensembles de $\R$ sont donc $\delta_x^*$-mesurables.
 
### Question 3 {.answer #answer-d3}
Comme tout ensemble $A$ de $\R$ est mesurable, $A$ est négligeable pour
la mesure de Dirac en $x$ si et seulement si $\delta_x(A) = 0$, c'est-à-dire
si et seulement si $x \not \in A$. La fonction $f: \R \to \R$ est donc nulle
presque partout si et seulement si $f(x) = 0$.


### Question 4 {.answer #answer-d4}
Quelle que soit la fonction $f: \R \to [-\infty, +\infty]$ et l'ouvert 
$U$ de $\mathbb{R}$, $f^{-1}(U) \in \mathcal{P}(\R)$ et donc est 
$\delta_x$-mesurable. La fonction $f$ est donc mesurable.
Elle est intégrable si et seulement si $f_+$ et $f_-$ sont d'intégrales
finies. Or, les fonctions simples positives et $\delta_x$-mesurable 
inférieure $f_{+}$ sont de la forme
$$
g(y) = \sum_{k=0}^{n-1} y_k 1_{A_k}(y) 
\; \mbox{ où } \;
g(y) = \sum_{k=0}^{n-1} y_k 1_{A_k}(y) \leq f_{+}(y)
$$
avec $y_k \geq 0$ et $A_k \in \mathcal{P}(\R)$.
On a donc
$$
\int g \delta_x = \sum_{k=0}^{n-1} y_k 1_{A_k}(x) \leq  f_{+}(x).
$$
Comme par ailleurs, la fonction $g  =f_+(x) 1_{\{x\}}$ est 
simple, positive, $\delta_x$-mesurable, inférieure à $f_{+}$ et vérifie
$$
\int g \delta_x = f_+(x),
$$
on a par conséquent
$$
\int f_+ \delta_x  = \sup_{g \in \mathcal{F}(f_+)} \int g \delta_x = f_+(x).
$$
De façon similaire, on peut montrer que 
$$
\int f_- \delta_x  = f_-(x).
$$
La fonction $f$ est donc $\delta_x^*$-intégrable si et seulement si 
les valeurs $f_-(x)$ et $f_+(x)$ sont finies, c'est-à-dire si et seulement
si $f(x) \not \in \{-\infty, +\infty\}$. On a alors
$$
\int f \delta_x = f_+(x) - f_-(x) = f(x).
$$

Approximation par des ensembles mesurables {#aem}
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

Mesure intérieure
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


Mesure image 
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-mi-1}
L'ensemble $\mathcal{B}$ est une tribu ; en effet :

  - $\varnothing \in \mathcal{A}$ et $\varnothing = h^{-1}(\varnothing)$,
    donc $\varnothing \in \mathcal{B}$.

  - Si $B \in \mathcal{B}$, l'ensemble 
    $A = h^{-1}(B)$ appartient à $\mathcal{A}$. 
    Le complémentaire $Y \setminus B$ de $B$ dans $Y$
    vérifie $h^{-1}(Y \setminus B) = X \setminus h^{-1}(B) = X \setminus A$
    et appartient donc à $\mathcal{A}$. L'ensemble $Y \setminus B$ appartient
    donc à $\mathcal{B}$.

  - Si les ensembles $B_k$, $k \in N$ appartiennent à $\mathcal{B}$, 
    comme $h^{-1}(\cup_k B_k) = \cup_k h^{-1}(B_k)$, cet ensemble
    appartient à $\mathcal{A}$. L'union dénombrable $\cup_k B_k$
    appartient donc à $\mathcal{B}$.

### Question 2 {.answer #answer-mi-2}
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
    
### Question 3 {.answer #answer-mi-3}
Montrons tout d'abord que la fonction $f:Y \to \R$ est mesurable 
si et seulement si $f \circ h$ est mesurable. Par définition,
$f$ est mesurable si pour tout ensemble borélien $B$ de $\R$,
l'ensemble $f^{-1}(B)$ appartient $\mathcal{B}$, c'est-à-dire
si et seulement si
$$
h^{-1} (f^{-1}(B)) = (f \circ h)^{-1}(B) \in \mathcal{A},
$$
c'est-à-dire si et seulement si $f \circ h$ est mesurable.

Comme $(f \circ h)_+ = f_+ \circ h$ et $(f \circ h)_- = f_- \circ h$,
il nous suffit de montrer que pour toute fonction mesurable
$f: Y \to \left[0, +\infty\right]$, on a
$$
\int (f \circ h) \mu = \int f (\mu \circ h^{-1})
$$
pour pouvoir conclure que $f: Y \to \R$ est $\mu \circ h^{-1}$-intégrable si et
seulement si $f \circ h$ est $\mu$-intégrable et que l'égalité ci-dessus
est valable.

Or pour une telle fonction $f$, il existe une suite croissante de fonctions 
$f_k$ simples, positives et mesurables convergeant simplement vers $f$,
et l'on a 
$$
\int f (\mu \circ h^{-1}) 
=
\lim_{k \to +\infty} \int f_k (\mu \circ h^{-1}).
$$
Comme 
$$
\begin{split}
\int f_k (\mu \circ h^{-1}) 
&= \sum_{y \in f_k(Y)} y \times (\mu \circ h^{-1})(f_k^{-1}(\{y\})) \\
&= \sum_{y \in f_k(Y)} y \times \mu (h^{-1}(f_k^{-1}(\{y\})) \\
&= \sum_{y \in f_k(Y)} y \times \mu ((f_k \circ h) ^{-1}(\{y\})) \\
\end{split}
$$
si $y \in f_k(Y)$, mais $y \not \in f_k(h(X))$, alors 
$\mu ((f_k \circ h) ^{-1}(\{y\})) = 0$. Par conséquent,
$$
\begin{split}
\int f_k (\mu \circ h^{-1}) 
&=
\sum_{y \in (f_k \circ h)(X)} y \times \mu ((f_k \circ h) ^{-1}(\{y\})) \\
&=
\int (f_k \circ h) \mu.
\end{split}
$$
Les fonctions $f_k \circ h$ sont simples, positives et mesurables,
leur suite est croissante et converge simplement vers $f \circ h$.
[Par le théorème de convergence monotone](#TCM), on a donc
$$
\int f (\mu \circ h^{-1}) 
=
\int (f \circ h) \mu.
$$



<!--
Une fonction $f: Y \to \R$ est positive, mesurable et étagée 
(appartient à $\mathcal{F}(f)$) si et seulement si elle est 
de la forme
$$
f = \sum_{k=0}^n y_k \times 1_{B_k} \; \mbox{ et } \; y_k \geq 0, \, B_k \in \mathcal{B},
$$
On a donc, pour toute fonction mesurable et positive $f: Y \to \R$,
$$
\int_Y f (h_*\mu) 
= 
\sup 
\left\{
\sum_{k=0}^n y_k \times (\mu \circ h^{-1})(B_k) 
\, \left| \vphantom{\sum} \right. \, 
\sum_{k=0}^n y_k \times 1_{B_k} \leq f, \, y_k \geq 0, \, B_k \in \mathcal{B}
\right\}.
$$
Or, si $A_k := h^{-1}(B_k)$, $A_k \in \mathcal{A}$ et
$$
\left(\sum_{k=0}^n y_k \times 1_{B_k}\right) \circ h = \sum_{k=0}^n y_k \times 1_{A_k}
\; \mbox{ et } \;
\sum_{k=0}^n y_k \times (\mu \circ h^{-1})(B_k) = \sum_{k=0}^n y_k \times \mu(A_k)
$$
La fonction $\sum_{k=0}^n y_k \times 1_{A_k}$ est donc étagée, mesurable, 
positive et inférieure à $f \circ h$. Si $f \circ h$ est intégrable, $f$ est
donc intégrable et 
$$
\int_Y f (\mu \circ h^{-1}) \leq \int_X (f\circ h) \mu.
$$
Par ailleurs, pour toute collection finie $A_k \in \mathcal{A}$, 
$k\in\{1,\dots, n\}$, si 
$$
\sum_{k=0}^n y_k \times 1_{A_k} \leq f \circ h 
$$

**TODO:** finir !

**TODO:** réécrire en utilisant le MCT, ou trouver la preuve à laquelle fait
référence Tao *sans* le MCT.
-->



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

Complétion d'une mesure
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-cm-1}
Nous allons établir que la tribu engendrée par $\mathcal{A} \cup \mathcal{N}$
est l'ensemble
$$
\mathcal{B} = \{A \ds  N \; | \; A \in \mathcal{A}, \, N \in \mathcal{N}\}.
$$
Tout d'abord, comme tout $A \in \mathcal{A}$ et $N \in \mathcal{N}$ 
appartiennent à cette tribu engendrée, $A^c$ et $N^c$ également et donc
$(A \cap N^c) \cup (A^c \cap N) = A \ds N$ également. 
L'ensemble $\mathcal{B}$ est donc inclus dans la tribu engendrée par 
$\mathcal{A}$ et $\mathcal{N}$. Il suffit donc de montrer qu'il s'agit
bien d'une tribu pour pouvoir conclure qu'elle est la tribu engendrée
recherchée.

Il est clair que $\varnothing$ appartient à $\mathcal{B}$,
comme différence symétrique entre $\varnothing$ et $\varnothing$.
Si $B = A \ds N$ appartient à $\mathcal{B}$, alors
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
et par conséquent $B^c \in \mathcal{B}$.

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
Comme $\cup_k A_k \in \mathcal{A}$, on en déduit que $\mathcal{B}$ est stable
par union dénombrable. Cet collection contient l'ensemble vide, est stable
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


<!--
Nous avons déjà évoqué le fait à la question précédente que si 
les $A_k$, $k \in \N$, appartiennent $\mathcal{A}$ et les 
$N_k$, $k \in \N$, appartiennent à $\mathcal{N}$, alors 
$$
\cup_k (A_k \ds N_k) = (\cup_k A_k) \ds N 
\; \mbox{ avec } \;
N \in \mathcal{N},
$$
donc
$$
\overline{\mu}(\cup_k (A_k \ds N_k)) = \overline{\mu}(\cup_k A_k).
$$ 

Si $A_0 \ds N_0$ et $A_1 \ds N_1$ sont disjoints, alors, comme l'intersection
est distributive via-à-vis de la différence symétrique
($A \cap (B \ds C) = (A\cap B) \ds (A \cap C)$), on a
$$
\begin{split}
\varnothing &= (A_0 \ds N_0) \cap (A_1 \ds N_1) \\
&=
(A_0 \cap A_1) \ds ((A_0 \cap N_1) \ds (N_0 \cap A_1) \ds (N_0 \cap N_1))\\
\end{split}
$$  
soit 
$$
A_0 \cap A_1 = M_1 :=  ((A_0 \cap N_1) \ds (N_0 \cap A_1) \ds (N_0 \cap N_1)) \in \mathcal{N}.
$$
Donc $A_0$ et $A_1 \ds M_1$ sont disjoints et 
$\overline{\mu}(A_1 \ds M_1) = \overline{\mu}(A_1)$. De proche en proche
on peut ainsi construire une suite d'ensembles négligeables $M_k$ tels
que les $A_k \ds M_k$ soient disjoints et $\cup_k A_k  = \cup_k A_k \ds M_k$.
Par conséquent,
$$
\overline{mu}(\cup_k A_k \ds N_k) = \mu(\cup_k A_k) = \overline{\mu} ...
$$
-->

Réferences
================================================================================