% Calcul Différentiel II

<!-- LaTeX Macros -->
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}

Théorème des Fonctions Implicites
================================================================================

Objectifs {.meta}
--------------------------------------------------------------------------------

  - comprendre la portée du résultat: permettre la résolution *locale*
    d'équations non-linéaires paramétrique, autour d'une solution connue
    de référence.

  - savoir mettre en oeuvre la version "inversion locale" du théorème des
    fonction implicites pour manipuler des changements de variables.

  - connaître et savoir mettre en oeuvre dans les deux cas le ressort 
    de la preuve: un théorème de point fixe qui exploite la différentielle.

  - applications ? Géométriques d'abord ? Au changements de variables de
    la physique (ex: [thermo](https://fr.m.wikipedia.org/wiki/Gaz_parfait)). 
    Etudier un scope raisonnable. Cf Salamon sur scope géom diff ?


### TODO {.meta}

  - Différentielle partielle nécessaire en amont, pas que dérivée partielle.

  - Donner un jeu d'hypothèse "non minimal" pour le théorème des fonctions
    implicite dans le but de simplifier le résultat. Par exemple, supposer
    au minimum l'existence de la différentielle dans un voisiange du point 
    de référence ? Ou carrément son existence et sa continuité ?
    Et ajouter en remarque que l'on peut nuancer / décomposer le résultats
    en affinant les hypothèses, qui ne sont pas minimales ? En particulier, 
    cela suffit pour énoncer le théorème d'inversion locale, donc go, 
    simplifions.

  - Nota: preuve IFT nécessite point fixe *avec paramètre*. 
    Pas nécessairement si l'on se place directement dans les hypothèses
    de différentiabilité continue ?


### TODO

Exploiter "THE IMPLICIT AND THE INVERSE FUNCTION THEOREMS: EASY PROOFS"
(Oswaldo Rio Branco de Oliveira)

### Théorème des Fonctions Implicites {.theorem}

Soit $f$ une fonction définie sur un ouvert $W$ de 
$\mathbb{R}^n \times \mathbb{R}^m$:
$$
f: (x, y) \in W \subset \mathbb{R}^n \times \mathbb{R}^m \to f(x, y) \in \mathbb{R}^m
$$
qui soit continûment différentiable et telle que la différentielle partielle
$\partial_y f$ soit inversible en tout point de $W$.
Si le point $(x_0, y_0)$ de $W$ vérifie $f(x_0, y_0)= 0$,
alors il existe des voisinages ouverts $U$ de $x_0$ et $V$ de $y_0$ tels que
$U \times V \subset W$ et
une fonction implicite $\psi: U \to \mathbb{R}^m$, continûment différentiable, 
telle que pour tous $x \in  U$ et $y \in V$,
$$
f(x, y) = 0
\; \Leftrightarrow \; 
y = \psi(x).
$$
De plus, la différentielle de $\psi$ est donnée pour tout $x \in U$ par
$$
d \psi(x) = - (\partial_y f(x, y))^{-1} \cdot \partial_x f(x, y) \, \mbox{ où } \, y=\psi(x).
$$

### Extensions {.note}
Il est possible d'affaiblir l'hypothèse concernant $\partial_y f$ en supposant 
uniquement celle-ci inversible en $(x_0, y_0)$ au lieu d'inversible sur tout $W$.
En effet, l'application qui a une application linéaire 
$A: \mathbb{R}^m \to \mathbb{R}^m$ associe son inverse $A^{-1}$
est définie sur un ouvert et continue[^inv]. 
Comme l'application linéaire $\partial_y f(x_0, y_0)$ 
est inversible et que l'application $\partial_y f$
est continue, il existe donc un voisinage ouvert de $(x_0, y_0)$ contenu dans 
$W$ où $\partial_y f$ est inversible. 
Nous retrouvons donc les hypothèses initiales du théorème, 
à ceci près qu'elle sont satisfaites dans un voisinage de $(x_0, y_0)$
qui peut être plus petit que l'ouvert initial $W$.

**TODO:** ref au résultat de Tao sur math overflow où l'on ne dispose que
de la différentiabilité (pas du caractère continûment différentiable).

**TODO:** évoquer cas Lipschitz ?

### Démonstration {.proof}

La partie la plus technique de la démonstration concerne l'existence et 
la différentiabilité de la fonction implicite $\psi$. 
Mais si l'on admet temporairement ces résultats, 
établir l'expression de $d\psi$ est relativement simple.
En effet, l'égalité $f(x, \psi(x)) = 0$ étant satisfaite identiquement sur $U$
et la fonction $x \in U \mapsto f(x, \psi(x))$ étant différentiable
comme composée de fonctions différentiables, la règle de dérivation 
en chaîne fournit en tout point de $U$:
$$
\partial_x f(x, \psi(x)) + \partial_y f(x, \psi(x)) \cdot d\psi(x) = 0.
$$
On en déduit donc que
$$
d\psi(x) = - [\partial_y f(x, \psi(x))]^{-1} \cdot \partial_x f(x, \psi(x)).
$$

**TODO:** ici aussi, nécessaire d'invoquer la continuité de l'inversion
pour conclure quand au caractère $C^1$ de la fonction implicite. 
Factoriser ce résultat avec la remarque précédente ?

[^inv]: une application linéaire de $\mathbb{R}^m \to \mathbb{R}^m$ 
est inversible si et seulement si
le déterminant de la matrice $[A]$ qui la représente dans $\mathbb{R}^{m \times m}$ 
est non-nul. 
Or, la fonction $A \mapsto \det [A]$ est continue 
car le déterminant ne fait intervenir que des produits et des sommes des 
coefficients de $[A]$.
Par conséquent, les applications linéaires inversibles de 
$\mathbb{R}^m \to \mathbb{R}^m$ sont l'image réciproque de l'ouvert 
$\mathbb{R} \setminus \{0\}$ par une application continue:
cet ensemble est donc ouvert. Quand $A$ est inversible, on a 
$$
[A]^{-1} = \frac{\mathrm{co}([A])^t}{\det [A]}
$$
où $\mathrm{co}([A])$ désigne la comatrice de $[A]$. Chaque coefficient de 
cette comatrice ne faisant également intervenir que des sommes et des produits 
des coefficients de $[A]$, l'application $A \mapsto A^{-1}$ est inversible sur
son domaine de définition.

Pour établir l'existence de la fonction implicite $\psi$,
nous allons pour une valeur $x$ suffisamment proche de $x_0$
construire une suite convergente d'approximations $y_k$, 
proches de $y_0$ dont la limite $y$ sera solution de 
$f(x, y)=0$.

L'idée de cette construction repose sur l'analyse suivante: si nous partons
d'une valeur $y_k$ proche de $y_0$ (a priori telle que $f(x, y_k) \neq 0$)
et que nous recherchons une valeur $y_{k+1}$ proche, 
qui soit une (meilleure) solution approchée de $f(x, y) = 0$, 
comme au premier ordre
$$
f(x, y_{k+1}) \approx f(x, y_k) + \partial_y f(x, y_k) \cdot (y_{k+1} - y_k),
$$
nous en déduisons que la valeur $y_{k+1}$ définie par
$$
y_{k+1} := y_k - (\partial_y f(x, y_k))^{-1} \cdot f(x, y_k)
$$
vérifie $f(x, y_{k+1}) \approx 0$.
On peut espérer que répéter ce processus en partant de $y_0$ 
détermine une suite convergente dont la limite soit une
solution exacte $y$ de $f(x, y) = 0$.

Le procédé décrit ci-dessus constitue la méthode de Newton de recherche de zéros.
Nous allons prouver que cette heuristique est ici justifiée,
à une modification mineure près: 
nous allons lui substituer la méthode de Newton modifiée, 
qui n'utilise pas $\partial_y f(x, y_k)$ mais la valeur constante 
$\partial_y f(x_0, y_0)$, c'est-à-dire qui définit la suite
$$
y_{k+1} := y_k - Q^{-1} \cdot f(x, y_k) \, \mbox{ où } \, Q = \partial_y f(x_0, y_0).
$$

... **TODO:** reformuler sous forme de point fixe.

$$
\phi_x(y) = y - Q^{-1} \cdot f(x, y)
$$

...

La fonction $\phi_x$ est différentiable sur l'ensemble 
$\{y \in \mathbb{R}^m \, | \, (x, y) \in W\}$ et sa différentielle est donnée
par
$$
d\phi_x(y) =  I - Q^{-1} \cdot \partial_{y} f(x, y)
$$
où $I$ désigne la fonction identité. 
En écrivant
que $\partial_y f(x, y)$ est la somme de $\partial_y f(x_0, y_0)$ et de 
$\partial_y f(x, y) - \partial_y f(x_0, y_0)$, on obtient
$$
\begin{split}
\|d \phi_x(y)\| 
& \leq \|I - Q^{-1} \cdot Q\| + \|Q^{-1} \cdot (\partial_y f(x, y) - Q)\| \\
& \leq \|Q^{-1}\| \times \|\partial_y f(x, y) - Q\|.
\end{split}
$$
La fonction $f$ étant supposée de classe $C^1$, on peut trouver un $r>0$,
tel que tout couple $(x, y)$ tel que $\|x - x_0\| \leq r$ et
$\|y - y_0\| \leq r$ appartienne à $W$ et vérifie 
$\|\partial_y f(x, y) - Q\| \leq \kappa \|Q^{-1}\|^{-1}$ avec par exemple 
$\kappa = 1/2$, ce qui entraîne $\|d \phi_x(y)\| \leq \kappa$.
Par le théorème des accroissements finis, la restriction de $\phi$
à $\{y \in \mathbb{R}^m \, | \, \|y - y_0\| \leq r\}$
(que l'on continuera à noter $\phi_x$)
est $\kappa$-contractante:
$$
\|\phi_x(y) - \phi_x(z)\| \leq \kappa \|y - z\|.
$$
Par ailleurs,
$$
\begin{split}
\|\phi_x(y) - y_0\| 
&\leq \|\phi_x(y) - \phi_x(y_0)\|  + \|\phi_{x}(y_0) - \phi_{x_0}(y_0)\|. 
\end{split}
$$
On a 
$$\|\phi_x(y) - \phi_x(y_0)\| \leq \kappa\|y - y_0\| \leq \kappa r.$$
De plus, par continuité de $\phi$ en $(x_0, y_0)$, on peut choisir 
un $r'$ tel que $0 < r' < r$ et tel que si $\|x - x_0\| \leq r'$, 
alors $\|\phi_{x}(y_0) - \phi_{x_0}(y_0)\| \leq (1 - \kappa) r$. 
Pour de telles valeurs de $x$,
$$
\|\phi_x(y) - y_0\| \leq \kappa r +  (1- \kappa) r = r.
$$
L'image de la boule fermée 
$B = \{y \in \mathbb{R}^m \, | \, \|y - y_0\| \leq r\}$ 
par l'application $\phi_x$ est donc incluse dans $B$.

**TODO.** conclure existence et unicité (expliciter choix voisinages
$U$ et $V$).

Pour montrer la différentiabilité de la fonction implicite $\psi$,
il est nécessaire au préalable de montrer sa continuité.
Soit $x_1, x_2$ deux points de $V$; notons $y_1 = \psi(x_1)$
et $y_2 = \psi(x_2)$. Ces valeurs sont des solutions des équations
de point fixe
$$
y_1 = \phi_{x_1}(y_1) \, \mbox{ et } \, y_2 = \phi_{x_2}(y_2).
$$
En formant la différence de $y_2$ et $y_1$, on obtient donc
$$
\begin{split}
\|y_2 - y_1\| & = \|\phi_{x_2}(y_2) - \phi_{x_1}(y_1)\| \\
& \leq \|\phi_{x_2}(y_2) - \phi_{x_2}(y_1)\| +
\|\phi_{x_1}(y_1) - \phi_{x_2}(y_1)\|.
\end{split}
$$
La fonction $\phi_{x_2}$ étant $\kappa$-contractante,
le premier terme du membre de droite de cette inégalité est majoré
par $\kappa\|y_2 - y_1\|$, par conséquent
$$
\|y_2 - y_1\| \leq \frac{1}{1 - \kappa} \|\phi_{x_1}(y_1) - \phi_{x_2}(y_1)\|.
$$
L'application $y \mapsto \phi_{x_1}(y)$ étant continue en $y_1$, 
nous pouvons conclure que $y_2$ tend vers $y_1$ quand $x_2$ tend vers $x_1$;
autrement dit: la fonction implicite $\psi$ est continue en $x_1$.

Montrons finalement la différentiabilité de $\psi$ en $x_1$. Pour cela,
il suffit d'exploiter la différentiabilité de $f$ en $(x_1, y_1)$
où $y_1 = \psi(x_1)$. Elle fournit l'existence d'une fonction 
$\varepsilon$ qui soit un $o(1)$ telle que
$$
\begin{split}
f(x, y) &= f(x_1, y_1) 
+ \partial_x f(x_1, y_1) \cdot (x - x_1) 
+ \partial_y f(x_1, y_1) \cdot (y - y_1) \\
& \phantom{=} + \varepsilon((x-x_1, y-y_1)) (\|x-x_1\| + \|y-y_1\|)
\end{split}
$$
On a par construction $f(x_1, y_1) = 0$; en prenant $y = \psi(x)$,
on annule également $f(x, y) = 0$. En notant $P = \partial_x f(x_1, y_1)$
et $Q = \partial_y f(x_1, y_1)$, on obtient 
$$
\begin{split}
\psi(x)  &= \psi(x_1) - Q^{-1} \cdot P \cdot (x - x_1) \\
&\phantom{=} - Q^{-1} \cdot P \cdot \varepsilon((x-x_1, \psi(x)-\psi(x_1)) (\|x-x_1\| + \|\psi(x)-\psi(x_1)\|).
\end{split}
$$
Nous allons exploiter une première fois cette égalité. 
Notons tout d'abord que
$$
\varepsilon_x(x-x_1) := \varepsilon((x-x_1, \psi(x)-\psi(x_1))
$$
est un $o(1)$ du fait de la continuité de $\psi$ en $x_1$.
En choisissant $x$
dans un voisinage suffisamment proche de $x_1$, on peut donc
garantir que ce terme est arbitrairement petit, par
exemple, tel que
$$
\|Q^{-1} \cdot P\| \times \|\varepsilon_x(x-x_1) \| \leq \frac{1}{2},
$$
ce qui permet d'obtenir
$$
\|\psi(x) - \psi(x_1)\|
\leq
\|Q^{-1} P\| \times \|x - x_1\| + \frac{1}{2} \|x - x_1\| + \frac{1}{2} \|\psi(x) - \psi(x_1)\|
$$
et donc
$$
\|\psi(x) - \psi(x_1)\|
\leq \alpha \|x - x_1\|
\, \mbox{ avec } \, \alpha := 2 \|Q^{-1} P\| + 1.
$$
En exploitant une nouvelle fois la même égalité, on peut désormais conclure
que 
$$
\|\psi(x) - \psi(x_1) - Q^{-1} \cdot P \cdot (x - x_1)\|
\leq \|\varepsilon'_x(x-x_1)\| \times \|x - x_1\|.
$$
où la fonction $\varepsilon'_x$ est le $o(1)$ défini par
$$
\varepsilon'_x(x-x_1) := (1+\alpha)  \times \|Q^{-1} \cdot P\| \times \|\varepsilon_x(x-x_1)\|,
$$
ce qui prouve la différentiabilité de $\psi$ en $x_1$ et conclut la démonstration.

### Difféomorphisme {.definition}
Une fonction $f: U \subset \mathbb{R}^n \to V \subset \mathbb{R}^n$,
où les ensembles $U$ et $V$ sont ouverts est un *$C^1$-difféomorphisme* 
(de $U$ sur $V$) si $f$ est bijective et que $f$ ainsi que son inverse $f^{-1}$ 
sont continûment différentiables.

### Inverse de la Différentielle {.theorem}
Si $f: U \to V$ est un $C^1$-difféomorphisme, sa différentielle $df$ est
inversible en tout point $x$ de $U$ et
$$
(df(x))^{-1} = df^{-1}(y) \, \mbox{ où } \, y = f(x).
$$

### Démonstration {.proof}

**TODO**

### Inversion Locale {.theorem}
Soit $f: U \subset \mathbb{R}^n \to \mathbb{R}^n$ continûment différentiable
sur l'ouvert $U$ et telle que $df(x)$ soit inversible
en tout point $x$ de $U$. Alors pour tout $x_0$ in $U$, il existe un voisinage
ouvert $V \subset U$ de $x_0$ tel que $W=f(V)$ soit ouvert et que
la restriction de la fonction $f$ à $V$ soit un $C^1$-difféomorphisme 
de $V$ sur $W$.

### Démonstration {.proof}

Considérons la fonction $\phi: U \times \mathbb{R}^n  \to \mathbb{R}^n$
définie par
$$
\phi(x, y) = f(x) - y.
$$
Par construction $\phi(x, y) = 0$ si et seulement si $f(x) = y$.
De plus, $\phi$ est continûment différentiable et
$\partial_x \phi(x, y) = df(x)$. On peut donc appliquer le théorème
des fonctions implicites au voisinage du point $(x_0, f(x_0))$
et en déduire l'existence de voisinages ouvert $A$ et $B$ de $x_0$
et $f(x_0)$ tels que $A \times B \subset U \times \mathbb{R}^n$,
et d'une fonction continûment différentiable 
$\psi: B \to \mathbb{R}^m$ telle que pour tout $(x, y) \in A \times B$,
$$
f(x) = y \; \Leftrightarrow \; x = \psi(y). 
$$
Par continuité de $f$, $A' = A \cap f^{-1}(B)$ est un sous-ensemble ouvert
de $A$. La fonction $x \in A' \mapsto f(x) \in B$ est bijective par 
construction et son inverse est la fonction $y \in B \mapsto \psi(y) \in A'$;
nous avons donc affaire à un  $C^1$-difféomorphisme de $A'$ sur $B$.

Analyse d'Erreur / Numérique
================================================================================

Objectifs {.meta}
--------------------------------------------------------------------------------

  - Savoir quelles sont les options quand il s'agit de calculer des dérivées,
    gradient, différentielles: "manuelles", symboliques, différences finies,
    diff auto. et avoir au final une idée de la portée de chacune
    (applicabilité, avantages, pbs)

  - Connaitre le principe des méthodes de type différence finie 
    et mes deux sources d'erreurs potentielles associées (très général,
    pas limité au calcul diff): "erreur de troncature" et "erreur d'arrondi".
    Savoir calculer des estimations numériques dans les deux cas.
    (attention, il y a plein de choses ici: il faut en passer par
    le modèle de représentation des nombres flottants, etc.)


Introduction
--------------------------------------------------------------------------------

### TODO

Terminologie "à virgule flottante" utilisée au moins une fois.

-------

Vous avez peut-être déjà utilise une méthode de différentiation numérique 
pour évaluer la dérivée d'une fonction, par exemple l'approximation des 
différences finies de Newton
  $$
  f'(x) \approx \frac{f(x+h) - f(x)}{h}.
  $$

L'implémentation de ce schéma en Python est simple:

    def FD(f, x, h):
        return (f(x + h) - f(x)) / h

Néanmoins, la relation entre la valeur du pas $h$ et la précision de
cette évaluation -- c'est-à-dire l'écart entre la valeur de la dérivée
et son estimation -- est plus complexe. 
Considérons les échantillons de données suivants:

Expression                    Valeur
----------------------------  --------------------------------------------------
$\exp'(0)$                    $1$
`FD(exp, 0, 1e-4)`            `1.000050001667141`
`FD(exp, 0, 1e-8)`            `0.99999999392252903`
`FD(exp, 0, 1e-12)`           `1.000088900582341`

La valeur la plus précise de la dérivée numérique est obtenue pour $h=10^{-8}$
et uniquement 8 nombres après la virgule du résultat sont singificatifs.

Pour la valeur plus grande $h=10^{-4}$, la précision est limitée par la qualité
du développement de Taylor de $\exp$ au premier ordre; 
cette erreur dite *de troncature* décroit linéairement avec la taille du pas.
Pour la valeur plus petite de $h=10^{-12}$, la précision est essentiellement
limitée par les erreurs d'arrondi dans les calculs.

Arithmétique des ordinateurs
--------------------------------------------------------------------------------

Cette section introduit la représentation des nombres réels sur ordinateur
comme des "doubles" et leur propriétés élémentaires. Pour avoir plus 
d'informations sur le sujet, vous pouvez vous reporter au document classique
"What every computer scientist should know about computer arithmetic" [@Gol91]

Les exemples qui suivent exploitent la librairie numérique Python [NumPy];
assurons-nous tout de suite d'avoir importé toutes ses fonctionnalités:

    >>> from numpy import *

[NumPy]: http://www.numpy.org/

### Nombres flottants: premier contact

Dans un interpréteur Python, la façon la plus simple d'afficher un nombre
consiste à invoquer son nom; par exemple

    >>> pi
    3.141592653589793

Cette information est non-ambigüe; par là nous voulons dire que nous disposons
d'assez d'information pour reconstituer le nombre initial:

    >>> pi == eval("3.141592653589793")
    True

Mais cette représentation n'en est pas moins un mensonge:
ça n'est pas une représentation décimale exacte du nombre `pi`
stockée en mémoire. Pour avoir une représentation exacte de `pi`,
nous pouvons demander l'affichage d'un grand nombre de décimales:

    >>> def all_digits(number):
    ...     print("{0:.100g}".format(number))    
    >>> all_digits(pi)
    3.141592653589793115997963468544185161590576171875

Demander 100 chiffres après la virgule est suffisant: 
seul 49 chiffres sont affichés car les suivants sont tous nuls.

Remarquez que nous avons obtenu une représentation exacte du nombre flottant
`pi` avec 49 chiffres. Cela ne signifie pas que tous ces chiffres
-- ou même la plupart d'entre eux -- sont significatifs dans la représentation
du nombre réel $\pi$. En effet, si nous utilisons la bibliothèque Python
[mpmath] pour l'arithmétique flottante multi-précisions, nous voyons que

    #>>> import mpmath
    #>>> mpmath.mp.dps = 49; mpmath.mp.pretty = True
    #>>> +mpmath.pi
    #3.141592653589793238462643383279502884197169399375

[mpmath]: https://mpmath.googlecode.com/svn/trunk/doc/build/index.html

et que les deux représentations ne sont identiques que jusqu'au 16ème chiffre.

### Nombres flottants binaires

Si la représentation des nombres flottants peut apparaître complexe à ce stade,
c'est que nous avons insisté pour utiliser une représentation **décimale**
quand ces nombres sont stockés avec une réprésentation **binaire.**
En d'autres termes; au lieu d'utiliser une suite de chiffres décimaux
$f_i \in \{0,1,\dots,9\}$ pour représenter un nombre réel $x$ comme
  $$
  x = \pm (f_0.f_1f_2 \dots f_i \dots) \times 10^{e} 
  $$
nous devrions utiliser des *chiffres binaires* -- ou *bits** -- 
$f_i \in \{0,1\}$ pour écrire:
  $$
  x = \pm (f_0.f_1f_2 \dots f_i \dots) \times 2^{e}.
  $$
Ces représentations sont **normalisées** si le chiffre avant la virgule est
non nul. Par exemple, avec cette convention, le nombre rationnel $999/1000$
serait représenté en base 10 comme $9.99 \times 10^{-1}$ et non comme
$0.999 \times 10^0$. En base $2$, le seul chiffre non-nul est $1$, donc
la *mantisse* d'une représentation normalisée est toujours de la forme
$(1.f_1f_2\dots f_i \dots).$

**TODO below: footnote besoin machine learning qui fonctionne avec des
singles ou half precisions**

En calcul scientifique, les nombres réels sont le plus souvent approximés
sous la forme de "doubles"[^IEEE754]. Dans la bibliothèque standard Python,
les doubles sont disponibles comme instances du type `float` -- 
ou alternativement comme `float64` dans NumPy.

Un triplet de 

  - *bit de signe:* $s \in \{0,1\},$ 
  
  - *exposant (biaisé):* $e\in\{1,\dots, 2046\}$ (11-bit), 

  - *fraction:* $f=(f_1,\dots,f_{52}) \in \{0,1\}^{52}.$ 

représente un double normalisé
  $$
  x = (-1)^s \times 2^{e-1023} \times (1.f_1f_2 \dots f_{52}).
  $$

[^IEEE754]: "Double" est un raccourci pour "format à virgule flottante de 
précision double", comme défini dans le standard IEEE 754, cf. [@ANS85]. 
Un format de simple précision est aussi défini, qui utilise uniquement
32 bits; NumPy le propose sous le nom `float32`.

Les doubles qui ne sont pas normalisés sont *not-a-number* (`nan`),
plus ou moins l'infini (`inf`) et zero (`0.0`) (en fait $\pm$ `0.0`;
car il existe deux zéros distincts, qui différent par leur signe)
et les nombres dits *dénormalisés*. Dans la suite, nous ne parlerons
pas de ces cas particuliers.

### Précision

Presque aucun nombre réel ne peut être représenté exactement comme un double.
Pour faire façe à cette difificulté, il est raisonnable d'associer à un
nombre réel $x$ le double le plus proche $[x]$. Une telle méthode
(*arrondi-au-plus-proche*) totalement spécifiée[^holes] dans le standard IEE754
[@ANS85], ainsi que des modes alternatifs d'arrondi (arrondis "dirigés").

[^holes]: Il faut préciser comme l'opération se comporte quand le réel
est équidistant de deux doubles, comment les "nombres spéciaux" 
(`inf`, `nan`, ...) sont traités, etc. Autant de "détails" dont nous
ne nous préoccuperons pas dans la suite.

Pour avoir la moindre confiance dans le résultats des calculs que nous 
effectuons avec des doubles, nous devons être en mesure d'évaluer l'erreur
faite par la représentation de $x$ par $[x]$. L'*epsilon machine* 
$\varepsilon$ est une grandeur clé à cet égard: il est défini comme l'écart 
entre $1.0$
-- qui peut être représenté exactement comme un double -- 
et le double qui lui est immédiatement supérieur.

    >>> after_one = nextafter(1.0, +inf)
    >>> after_one
    1.0000000000000002
    >>> all_digits(after_one)
    1.0000000000000002220446049250313080847263336181640625
    >>> eps = after_one - 1.0
    >>> all_digits(eps)
    2.220446049250313080847263336181640625e-16

Ce nombre est également disponible comme un attribut de la class `finfo`
de NumPy qui rassemble les constantes limites de l'arithmétique pour les
types flottants.

    >>> all_digits(finfo(float).eps)
    2.220446049250313080847263336181640625e-16

Alternativement, l'examen de la structure des doubles normalisés fournit
directement la valeur de $\varepsilon$: la fraction du nombre après $1.0$
est $(f_1, f_2, \dots, f_{51}, f_{52}) = (0,0,\dots,0,1),$ donc
$\varepsilon =2^{-52},$ un résultat confirmé par:

    >>> all_digits(2**-52)
    2.220446049250313080847263336181640625e-16

L'epsilon machine importe autant parce qu'il fournit une borne simple sur
l'erreur relative de la représentation d'un nombre réel comme un double.
En effet, pour n'importe quelle méthode d'arondi raisonnable, la structure
des doubles normalisés fournit:
    $$
    \frac{|[x] - x|}{|x|} \leq \varepsilon.
    $$
Si la méthode "arrondi-au-plus-proche" est utilisée, il est même possible de
garantir la borne plus contraignante $\varepsilon / 2$ au lieu de $\varepsilon.$

#### Chiffres significatifs

L'erreur relative se traduit directement par combien de chiffres décimaux
sont *significatifs* dans la meilleurs approximation d'un nombre réel par
un double. Considéons la représentation de $[x]$ en notation scientifique:
    $$
    [x] = \pm (f_0.f_1 \dots f_{p-1} \dots) \times 10^{e}.
    $$
On dira qu'elle est *significative jusqu'au $p$-ème chiffre* si
  $$
  |x -  [x]| \leq \frac{10^{e-(p-1)}}{2}.
  $$
D'autre part, la borne d'erreur sur $[x]$ fournit
  $$
  |x - [x]| \leq \frac{\varepsilon}{2} |x| \leq \frac{\varepsilon}{2} \times 10^{e+1}.
  $$
Ainsi, la précision souhaitée est obtenue tant que
  $$
  p \leq - \log_{10} \varepsilon/2 = 52 \log_{10} 2 \approx 15.7.
  $$
Par conséquent, les doubles fournissent une approximation des nombres réels
à 15 décimales.

#### Fonctions

La plupart des nombres réels ne pouvant être représentés par des doubles,
la plupart des fonctions à valeur réelle et à variables réelles ne peuvent 
pas non plus être représentée exactement comme des fonctions opérant sur
des doubles. 
Le mieux que nous puissions espérer est d'avoir des approximation 
*correctement arrondies*. Une approximation $[f]$ d'une fonction $f$
de $n$ variables est correctement arrondie si pour tout $n$-uplet
$(x_1, \dots, x_n)$, on a
  $$
  [f](x_1,\dots,x_n) = [f([x_1], \dots, [x_n])].
  $$
Autrement dit, tout se passe comme si le calcul de $[f](x_1,\dots,x_n)$
était effectué de la façon suivante: approximation au plus proche 
des arguments par des doubles, calcul **exact** de $f$ sur ces arguments, 
et approximation de cette valeur produite au plus proche par un double.

Le standard IEEE 754 [@ANS85] impose que certaines fonction aient des 
implémentations correctement arrondies; elles sont l'addition, la
soustraction, la multiplication, la division, le reste d'une division 
entière et la racine carrée.
D'autres fonctions élémentaires 
-- comme sinus, cosinus, exponentielle, logarithme, etc. --
ne sont en général pas correctement arrondies;
la conception d'algorithmes de calcul qui aient une performance décente et
dont on peut prouver qu'il sont correctement arrondis est un problème
difficile (cf. @FHL07).

Différences Finies
--------------------------------------------------------------------------------

### TODO

Terminologie erreur de troncature

### Différence Avant

Soit $f$ une fonction à valeurs réelles définie sur un intervalle ouvert.
Dans de nombreux cas concrets, on peut faire l'hypothèse que la fonction
$f$ est indéfiniment dérivable sur son domaine de définition;
le développement de Taylor avec reste intégral fournit alors
localement à tout ordre $n$,
  $$
  f(x+h) = f(x) + f'(x) h + \frac{f''(x)}{2} h^2 
           + \dots
           +\frac{f^{(n)}(x)}{n!} h^n 
           + O(h^{n+1})
  $$
où le terme $O(h^k)$ (notation "grand o" de Landau), 
désigne une expression de la forme
$O(h^k) := M(h) h^k$
où $M$ est une fonction définie et bornée dans un voisinage de $0$.

Un calcul direct montre que
  $$
  f'(x) = \frac{f(x+h) - f(x)}{h} + O(h)
  $$
Le comportement asymptotique de ce schéma de *différence avant*
(*forward difference*)
-- controllé par le terme $O(h^1)$ -- est dit d'ordre 1.
En supposant $f$ correctement arrondie,
une implémentation de ce schéma est défini pour les réels $x$ et
$h$ par
  $$
  \mathrm{FD}(f, x, h) = \left[\frac{[[f] ( [x] + [h]) - [f] ([x])]}{[h]} \right].
  $$
ou de façon équivalent en Python par:

    def FD(f, x, h):
        return (f(x + h) - f(x)) / h

<!--
[^Landau]: **Bachmann-Landau notation.** For a real or complex variable $h,$ 
we write $\psi(h) = O(\phi(h))$ if there is a suitable deleted 
neighbourhood of $h=0$ where the functions $\psi$ and $\phi$ are defined 
and the inequality $|\psi(h)| \leq \kappa |\phi(h)|$ holds for some $\kappa > 0.$ 
When $N$ is a natural number, we write 
$\psi(N) = O(\phi(N))$ if there is a $n$ such that $\psi$ and $\phi$ 
are defined for $N\geq n$ and for any such $N,$ 
the inequality $|\psi(N)| \leq \kappa |\phi(N)|$ holds for some $\kappa > 0.$
-->

### Erreur d'arrondi

Nous considérons à nouveau la fonction $f(x) = \exp(x)$ utilisée dans
l'introduction et nous calculons la dérivée numérique basée sur la
différence avant à $x=0$ pour différentes valeurs de $h$.

[Le graphe de $h \mapsto \mathrm{FD}(\exp, 0, h)$](#fdv) montre que pour 
les valeurs de $h$ proches ou inférieures à l'epsilon machine,
la différence entre la dérivée numérique et la valeur exacte de la dérivée
n'est pas expliquée par l'analyse classique liée au développement
de Taylor. 

![Valeurs de la différence avant](images/fd-value.py){#fdv}

Toutefois, si nous prenons en compte la représentation des réels comme des
doubles, nous pouvons expliquer et quantifier le phénomène. 
Pour étudier exclusivement l'erreur d'arrondi, nous aimerions 
nous débarasser de l'erreur de troncature; à cette fin, dans les
calculs qui suivent, au lieu de $\exp$, nous utilisons $\exp_1$,
le développement de Taylor de $\exp$ à l'ordre $1$ à $x=0$,
c'est-à-dire $\exp_1(x) = 1 + x$.

**TODO:** élts / catastrophic cancellation

Supposons que l'arrondi soit calculé au plus proche;
selectionons un double $h>0$ et comparons-le à l'epsilon machine:

  - Si $h \ll \varepsilon,$ alors $1 + h$ est proche de $1,$ en fait plus
    proche de $1$ que du double immédiatemment supérieur à $1$ qui est 
    $1 + \varepsilon.$ 
    Par conséquent, on a $[\exp_0](h) = 1;$ une *annulation catastrophique*
    survient:
      $$
      \mathrm{FD}(\exp_0, 0, h) = \left[\frac{\left[ [\exp_0](h) - 1 \right]}{h}\right] = 0.
      $$

  - Si $h \approx \varepsilon,$ alors $1+h$ est plus proche  $1+\varepsilon$que de $1,$ 
    et donc $[\exp_0](h) = 1+\varepsilon$, ce qui entraîne
      $$
      \mathrm{FD}(\exp_0, 0, h) = \left[\frac{\left[ [\exp_0](h) - 1 \right]}{h}\right]
      = \left[ \frac{\varepsilon}{h} \right].
      $$

  - Si $\varepsilon \ll h \ll 1,$ alors $[1+h] = 1+ h \pm \varepsilon(1+h)$
    (le symbole $\pm$ est utilisé ici pour défini un intervalle de confiance[^pm]). 
    Et donc
      $$
      [[\exp_0](h) - 1] = h \pm \varepsilon \pm \varepsilon(2h + \varepsilon + \varepsilon h)
      $$
    et
      $$
      \left[ \frac{[[\exp_0](h) - 1]}{h} \right] 
      = 
      1 \pm \frac{\varepsilon}{h} + \frac{\varepsilon}{h}(3h + 2\varepsilon + 3h \varepsilon +\varepsilon^2 + \varepsilon^2 h)
      $$
    et par conséquent
      $$
      \mathrm{FD}(\exp_0, 0, h)  = \exp_0'(0) \pm \frac{\varepsilon}{h}  \pm \varepsilon', \; \varepsilon' \ll \frac{\varepsilon}{h}.
      $$
      
[^pm]: L'équation $a = b \pm c$ est à interpréter comme l'inégalité $|a - b| \leq |c|.$

![Erreur de la différence avant](images/fd-error.py)

Si l'on revient à $\mathrm{FD}(\exp, 0, h)$ et si l'on exploite des échelles
log-log pour représenter l'erreur totale, on peut clairement distinguer la
region ou l'erreur est dominée par l'erreur d'arrondi -- l'envellope de cette
section du graphe est $h \mapsto \log(\varepsilon/h)$ -- et ou elle est dominée
par l'erreur de troncature -- une pente $1$ étant caractéristique des schémas
d'ordre 1



### Schémas d'ordre supérieur

Le comportement asymptotique de la différence avant peut être amélioré,
par exemple si au lieu de la différence avant nous utilisons un schéma
de différence centrée. Considérons les développements de Taylor à l'ordre
2 de $f(x+h)$ et $f(x-h)$:
  $$
  f(x+h) = f(x) + f'(x) (+h)+ \frac{f''(x)}{2} (+h)^2 + O\left(h^3\right)
  $$
et
  $$
  f(x-h) = f(x) + f'(x) (-h) + \frac{f''(x)}{2} (-h)^2 + O\left(h^3\right).
  $$
On en déduit
  $$
  f'(x) = \frac{f(x+h) - f(x-h)}{2h} + O(h^2),
  $$
et donc, le schéma de *différence centrale* est d'ordre 2.
Son implémentation sur ordinateur est donnée par
  $$
  \mathrm{CD}(f, x, h) = \left[\frac{[[f] ( [x] + [h]) - [f] ([x]-[h])]}{[2 \times [h]]} \right].
  $$
ou de façon équivalente en Python:

    def CD(f, x, h):
        return 0.5 * (f(x + h) - f(x - h)) / h


![Erreur de la différence centrée](images/cd-error.py){#cde}

[Le graphe d'erreur associé à la différence centrale](#cde) confirme qu'une 
erreur de troncature d'ordre 2 améliore la précision. 
Toutefois, il montre aussi que l'utilisation d'un schéma d'ordre plus
élevé augmente également la région ou l'erreur est dominée par l'erreur
d'arrondi et rend la sélection d'un pas correct $h$ encore plus difficile.




Différentiation Automatique
================================================================================

Objectifs {.meta}
--------------------------------------------------------------------------------

  - avantage et portée de la méthode (plus détaillée: précision, dérivées à
    un ordre arbitraire, "workflow", usages en optimisation, machine learning,
    etc.)

  - connaître les (une version des) principes des différents "morceaux" 
    de la méthode dans le cas de Python: "tracer", "computation graph", etc.
    Solution: en construire un "à la main", au moins les étapes importantes.
    Note: permet aussi d'apprécier les limitations de la méthode.

  - sur péda, essayer forward pass (plus près du cours),
    mais expliquer backward pass pour pouvoir se "plugger" dans l'existant.

  - exploiter un système existant, type `autograd` en python
    (sans doute le plus facile en terme de courbe d'apprentissage)

Tracer le Graphe de Calcul
--------------------------------------------------------------------------------

**TODO:** montrer que les fonction Python n'implémentent pas 
"ce que l'on croit", c'est-à-dire par exemple $[\cos([x])]$
pour la function `lambda x: cos(x)`, parce que le TYPE de
l'argument n'est pas spécifié et que cela à des conséquences
importantes: le disassembleur montre bien que le bytecode
est agnostique et se contente de résoudre des variables 
et d'appliquer une séquence d'instructions, sans de référence 
au type, sans savoir ce qu'il manipule.

    >>> from dis import dis

    >>> from math import *

**TODO:** expliquer notation lambda-fonction pour les expressions 
(ou fonctions anonymes).

    >>> f = lambda x: cos(x)

    >>> dis(lambda x: cos(x))
      1           0 LOAD_GLOBAL              0 (cos)
                  2 LOAD_FAST                0 (x)
                  4 CALL_FUNCTION            1
                  6 RETURN_VALUE

    >>> dis(lambda x: x + 1)
      1           0 LOAD_FAST                0 (x)
                  2 LOAD_CONST               1 (1)
                  4 BINARY_ADD
                  6 RETURN_VALUE

Expliquer en prenant des exemples frappants comment on peut en profiter
pour "intercepter" cette séquence d'appels (big brother ...) pour savoir
ce qui se passe dans la fonction, influencer le résultat, etc.

    >>> math_cos = cos
    >>> def cos(x):
    ...     print(f"trace: cos({x})")
    ...     return math_cos(x)

    >>> y = cos(pi)
    trace: cos(3.141592653589793)
    >>> y
    -1.0

Le cas des opérateurs est plus complexe: le calcul de `x + 1` par exemple est
délégué à la méthode `__add__` de l'objet `x`. Pour intercepter cet appel,
il est donc nécessaire de modifier le type de nombre flottant que nous
allons utiliser:

    >>> class Float(float):
    ...     def __add__(self, other):
    ...         print(f"trace: {self} + {other}")
    ...         return super().__add__(other)

Mais une fois cet effort fait, nous pouvons bien tracer les additions 
effectuées

    >>> x = Float(2.0) + 1.0
    trace: 2.0 + 1.0
    >>> x
    3.0

... à condition que nous travaillions avec des instances de `Float` et 
non de `float` ! Pour commencer à généraliser cet usage, nous allons faire
en sorte de générer des instances de `Float` dans la mesure du possible.
Pour commencer, nous pouvons faire en sorte que les opérations sur nos 
flottants renvoient notre propre type de flottant:

    >>> class Float(float):
    ...     def __add__(self, other):
    ...         print(f"trace: {self} + {other}")
    ...         return Float(super().__add__(other))

Mais cela n'est pas suffisant: les fonction de la library `math` de Python
vont renvoyer des flottants classiques, il nous faut donc à nouveau les
adapter:

    >>> def cos(x):
    ...     print(f"trace: cos({x})")
    ...     return Float(math_cos(x))

Vérifions le résultat:

    >>> cos(pi) + 1.0
    trace: cos(3.141592653589793)
    trace: -1.0 + 1.0
    0.0

Mais nous ne savons pas encore tracer correctement l'expression `1.0 + cos(pi)`:

    >>> 1.0 + cos(pi)
    trace: cos(3.141592653589793)
    0.0

En effet, c'est la méthode `__add__` de `1.0`, une instance de `float` qui
est appelée; cet appel n'est donc pas tracé. Pour réussir à tracer ce type
d'appel, il va falloir ... le faire échouer ! La méthode appellée pour
effectuer la somme jusqu'à présent confie l'opération à la méthode
`__add__` de `1.0` parce ce cette objet sait prendre en charge l'opération,
car il s'agit d'ajouter lui-même avec une autre instance (qui dérive) de
`float`. Si nous faisons en sorte que le membre de gauche soit incapable
de prendre en charge cette opération, elle sera confiée au membre de 
droite; pour cela il nous suffit de remplacer `Float`, un type numérique
par `Node`, une classe qui contient (encapsule) une valeur numérique:

    >>> class Node:
    ...     def __init__(self, value):
    ...         self.value = value

Nous n'allons pas nous attarder sur cette version 0 de `Node`.
Si elle est ainsi nommée, c'est parce qu'elle va représenter un noeud
dans un graphe de calculs. Au lieu d'afficher les opérations réalisées
sur la sortie standard, nous allons entreprendre d'enregistrer les 
opérations que subit chaque variable et comment elle s'organise;
chaque noeud issu d'une opération devra mémoriser quelle opération
a été appliquée, et quels étaient les arguments de l'opération (eux-mêmes
des noeuds). Pour supporter cette démarche, `Node` devient:

    >>> class Node:
    ...     def __init__(self, value, function=None, args=None):
    ...         self.value = value
    ...         self.function = function
    ...         self.args = args if args is not None else []

Il nous faut alors rendre les opérations usuelles compatibles la création
de noeuds; en examinant les arguments de la fonction, on doit décider si
elle est dans un mode "normal" (recevant des valeurs numériques, produisant
des valeurs numérique) ou en train de tracer les calculs. Par exemple:

    >>> def cos(x):
    ...     if isinstance(x, Node):
    ...         cos_x_value = math_cos(x.value)
    ...         cos_x = Node(cos_x_value, cos, [x])
    ...         return cos_x
    ...     else:
    ...         return math_cos(x) 

ou 

    >>> def add(x, y):
    ...     if isinstance(x, Node) or isinstance(y, Node):
    ...         if not isinstance(x, Node):
    ...             x = Node(x)
    ...         if not isinstance(y, Node):
    ...             y = Node(y)
    ...         add_x_y_value = x.value + y.value
    ...         return Node(add_x_y_value, add, [x, y])
    ...     else:
    ...         return x + y




La fonction `add` ne sera sans doute pas utilisée directement, 
mais appelée sous forme d'opérateur `+`; elle doit donc nous
permettre de définir les méthodes `__add__` et `__radd__`:

    >>> Node.__add__ = add
    >>> Node.__radd__ = add


On remarque de nombreuse similarités entre les deux codes;
plutôt que de continuer cette démarche pour toutes les fonctions
dont nous allons avoir besoin, au prix d'un effort d'abstraction,
il serait possible de définir une fonction opérant automatiquement
cette transformation. Il s'agit d'une fonction d'ordre supérieur
car elle prend comme argument une fonction (la fonction numérique
originale) et renvoie une nouvelle fonction, compatible avec la
gestion des noeuds. On pourra ignorer sont implémentation 
en première lecture.

    >>> def wrap(function):
    ...    def wrapped_function(*args):
    ...        if any(isinstance(arg, Node) for arg in args):
    ...            node_args = []
    ...            values = []
    ...            for arg in args:
    ...                if isinstance(arg, Node):
    ...                    node_args.append(arg)
    ...                    values.append(arg.value)
    ...                else:
    ...                    node_args.append(Node(arg)) 
    ...                    values.append(arg)
    ...            output_value = wrapped_function(*values)
    ...            output_node = Node(output_value, wrapped_function, node_args)
    ...            return output_node
    ...        else:
    ...            return function(*args)        
    ...    wrapped_function.__qualname__ = function.__qualname__
    ...    return wrapped_function

Malgré sa complexité apparente, l'utilisation de cette fonction est simple; 
ainsi pour rendre la foncton `sin` et l'opérateur `*` compatible
avec la gestion de noeuds, il suffit de faire:

    >>> sin = wrap(sin)

et

    >>> def multiply(x, y):
    ...     return x * y
    >>> multiply = wrap(multiply)
    >>> Node.__mul__ = Node.__rmul__ = multiply

ce que est sensiblement plus rapide et lisible 
que la démarche entreprise pour `cos` et `+`; 
mais encore une fois, le résultat est le même.

Il est désormais possible d'implémenter le traceur. 
Celui-ci encapsule les arguments de la fonction à tracer 
dans des noeuds, puis appelle la fonction et renvoie le noeud associé
à la valeur retournée par la fonction:

    >>> def trace(f, args):
    ...     args = [Node(arg) for arg in args]
    ...     end_node = f(*args)
    ...     return end_node

Pour vérifier que tout se passe bien comme prévu,
faisons en sorte d'afficher une représentation lisible 
et sympathique des contenus des noeuds:

    >>> def node_repr(node):
    ...    if node.function is not None:
    ...        function_name = node.function.__qualname__
    ...        return f"Node({node.value}, {function_name}, {node.args})"
    ...    else:
    ...        return f"Node({node.value})"

Puis, faisons en sorte qu'elle soit utilisée par défaut par le noeuds
plutôt que la représentation standard des objets:

    >>> Node.__str__ = Node.__repr__ = node_repr

Nous somme prêts à faire notre vérification:

    >>> f = lambda x: 1.0 + cos(x)
    >>> end = trace(f, [pi])
    >>> print(end)
    Node(0.0, add, [Node(-1.0, cos, [Node(3.141592653589793)]), Node(1.0)])

Le résultat se lit de la façon suivante: le calcul de `f(pi)` produit 
la valeur `0.0`, issue de l'addition de `-1.0`, 
calculé comme `cos(3.141592653589793)` et de la constante `1.0`.
Cela semble donc correct !

Un autre exemple -- à deux arguments -- pour la route:

    >>> trace(lambda x, y: x * (x + y), [1.0, 2.0])
    Node(3.0, multiply, [Node(1.0), Node(3.0, add, [Node(1.0), Node(2.0)])])

Calcul Automatique des Dérivées
--------------------------------------------------------------------------------

Registre des functions "élémentaires" dont on connaît la différentielle

    >>> differential = {} 

    >>> def d_cos(x):
    ...     return lambda dx: - sin(x) * dx
    >>> differential[cos] = d_cos

    >>> def d_multiply(x, y):
    ...     return lambda dx, dy: x * dy + dx * y
    >>> differential[multiply] = d_multiply

    >>> def d_from_derivative(f_prime):
    ...     def d_f(x):
    ...        return lambda dx: f_prime(x) * dx
    ...     return d_f
    >>> differential[sin] = d_from_derivative(cos)

    >>> differential[add] = lambda x, y: add

Tri topologique

    >>> def sort_nodes(end_node):
    ...     todo = [end_node]
    ...     nodes = []
    ...     while todo:
    ...         node = todo.pop()
    ...         nodes.append(node)
    ...         for parent in node.args:
    ...             if parent not in nodes + todo:
    ...                 todo.append(parent) 
    ...     done = []
    ...     while nodes:
    ...         for node in nodes[:]:
    ...             if all(parent in done for parent in node.args):
    ...                 done.append(node)
    ...                 nodes.remove(node)
    ...     return done

    >>> def d(f):
    ...     def df(*args): # args=(x1, x2, ...)
    ...         start_nodes = [Node(arg) for arg in args]
    ...         end_node = f(*start_nodes)
    ...         sorted_nodes = sort_nodes(end_node).copy()
    ...         def df_x(*d_args): # d_args = (d_x1, d_x2, ...)
    ...             for node in sorted_nodes:
    ...                 if node in start_nodes:
    ...                     i = start_nodes.index(node)
    ...                     node.d_value = d_args[i]
    ...                 elif node.function is None: # constant node
    ...                     node.d_value = 0.0
    ...                 else:
    ...                     _d_f = differential[node.function]
    ...                     _args = node.args
    ...                     _args_values = [_node.value for _node in _args]
    ...                     _d_args = [_node.d_value for _node in _args]
    ...                     node.d_value = _d_f(*_args_values)(*_d_args)
    ...             return end_node.d_value
    ...         return df_x
    ...     return df

    >>> def f(x):
    ...     return x * x + 2 * x + 1
    >>> x = 1.0
    >>> df_x = d(f)(2.0)
    >>> df_x(1.0)
    6.0


Derivative of f (manual computation)

    >>> def f(x):
    ...    return cos(x) * cos(x) + sin(x) * sin(x)
    >>> df = d(f)
    >>> def f_prime(x):
    ...    return df(x)(1.0)
    >>> f_prime(pi/4)
    0.0

Exercices
================================================================================

Cinématique des Robots Manipulateurs
--------------------------------------------------------------------------------

Position de référence en cartésien, robot plan articulaire (ou extension 3d),
étudier sous quelle conditions on peut "résoudre" un déplacement de 
l'effecteur.

Déformations
--------------------------------------------------------------------------------

Soit $U$ un ouvert convexe de $\mathbb{R}^n$ et 
$T: U \subset \mathbb{R}^n \to \mathbb{R}^n$
une fonction continûment différentiable. 
On suppose que $T$ est de la forme $T=  I + H$ 
où la fonction $H$ vérifie
$$
\sup_{x \in U} \|d H(x)\| := \kappa < 1.
$$
On appellera une telle fonction $T$ une *perturbation de l'identité*.

 1. Montrer que la foncton $T$ est injective.

 2. Montrer que l'image $V= T(U)$ est un ouvert et
    que $T$ est difféomorphisme (global) de $U$ sur $V$.

### Réponses

 1. Par le théorème des accroissements finis, si $x$ et $y$ appartiennent
    à $U$, comme par convexité $[x, y] \subset U$, on a 
    $$
    \|H(x) - H(y)\| \leq \kappa \|x - y\|.
    $$
    Par conséquent,
    $$
    \begin{split}
    \|T(x) - T(y)\| &= \|x + H(x) - (y + H(y))\| \\
    &\geq \|x - y\| - \|H(x) - H(y)\| \\
    &\geq (1 - \kappa) \|x - y\|
    \end{split}
    $$
    et donc si $T(x) = T(y)$, $x=y$: $T$ est injective.

 2. La différentielle $dT(x)$ de $T$ en $x$ est une application 
    de $\mathbb{R}^n$ dans $\mathbb{R}^n$ de la forme
    $$
    dT(x) = I + dH(x).
    $$
    Comme $\mathbb{R}^n$ est ouvert et que la fonction $h \mapsto dH(x) \cdot h$
    a pour différentielle en tout point $y$ de $\mathbb{R}^n$ la function
    $dH(x)$, 
    la fonction linéaire $h \mapsto dT(x) \cdot h$ est une perturbation de 
    l'identité; elle est donc injective, et inversible car elle est linéaire de
    $\mathbb{R}^n$ dans $\mathbb{R}^n$. Les hypothèses du 
    théorème d'inversion locale sont donc satisfaites 
    en tout point $x$ de $U$. La fonction $f$ est donc un difféomorphisme 
    local d'un voisinage ouvert $V_x$ de $x$ sur
    $W_x= f(V_x)$ qui est ouvert. Clairement,
    $$
    f(U) = f\left(\bigcup_{x \in U} V_x\right) = \bigcup_{x \in U} f(V_x)
    $$
    et par conséquent $f(U)$ est ouvert.
    La fonction $f$ est injective et surjective de $U$ dans $f(U)$,
    donc inversible. En tout point $y$ de $f(U)$, il existe $x \in U$
    tel que $f(x) = y$, et un voisinage ouvert $V_x$ de $x$ tel que
    $f$ soit un difféomorphisme local de $V_x$ sur l'ouvert $W_x = f(V_x)$; 
    la fonction
    $f^{-1}$ est donc continûment différentiable dans un voisinage de $y$.
    C'est par conséquent un difféomorphisme global de $U$ dans $f(U)$.





Racines d'un Polynôme
--------------------------------------------------------------------------------

Si racine simple, variation continue (et plus) par rapport aux coefficients.

Lier ça à la sensibilité des valeurs propres (et vecteurs propres ?) par rapport
aux coefficients de la matrice associée ? Avantage: plus de travail de mise en
forme pour se ramener au pb de fct implicite (à ajouter aux objectifs).

Différentielle de $X \mapsto X^{-1}$
--------------------------------------------------------------------------------

Différentiation à pas complexe
--------------------------------------------------------------------------------

**TODO**

Méthode de Newton
--------------------------------------------------------------------------------

Revenir sur la preuve du théorème des fonctions implicites mais sous sous une
hypothèse $C^2$, montrer qu'il n'est pas nécessaire de modifier la méthode
de Newton.

Inversion Locale
--------------------------------------------------------------------------------

**TODO:** exemple où l'on complète le jacobien pour pouvoir appliquer le TIL.

TODO -- Projet Numérique -- Lignes de niveau
================================================================================

L'objectif de ce projet numérique est de développer un programme permettant
de calculer les lignes de niveau d'une fonction $f$ de deux variables 
réelles et à valeurs réelle, c'est-à-dire les ensembles de la forme
$$
\{(x, y) \in \R^2 \, | \, f(x, y) = c\} \, \mbox{ où } \, c \in \R.
$$

La représentation graphique de ces courbes est un *tracé de contour*
(cf. [les exemples d'usage de la fonction `contour` de matplotlib](https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.contour.html#examples-using-matplotlib-pyplot-contour)).

![Lignes de niveau de $(x, y) \mapsto 2(f(x, y) - g(x, y))$
où $f(x, y) = \exp(-x^2 - y^2)$ et $g(x, y) = \exp(-(x - 1)^2 - (y - 1)^2)$. 
Source: ["Contour Demo" (matplotlib)](https://matplotlib.org/3.1.0/gallery/images_contours_and_fields/contour_demo.html#sphx-glr-gallery-images-contours-and-fields-contour-demo-py).](images/contour.py)

On suppose dans un premier temps que la fonction $f$ dont on cherche les courbes
de niveau est définie dans le carré unité $[0,1] \times [0,1]$ et qu'il existe
une amorce à la courbe de niveau $c$ sur l'arête gauche du carré, c'est-à-dire 
un point $(0, y)$ avec $y \in [0, 1]$, tel que $f(0, y) = c$. 
La production de courbes de niveau dans cette situation élémentaire 
deviendra ultérieurement le composant centrale dans un cas plus général.

### Amorce

Considérons une fonction $g:[0, 1] \mapsto \mathbb{R}$ supposée continue.
A quelle condition raisonnable portant sur $g(0)$, $g(1)$ et le réel $c$ 
est-on certain qu'il existe un $t \in [0, 1]$ tel que $g(t) = c$ ?
Développer une fonction, conforme au squelette suivant

    def root(g, c=0, eps=2**(-52)):
        ...
        return t

qui renvoie un flottant éloigné d'au plus `eps` (par défaut, l'epsilon machine) 
d'un tel $t$ (avec $c=0$ par défaut), ou `None` si la condition évoquée ci-dessus
n'est pas satisfaite.

Comment utiliser cette fonction pour trouver une amorce de courbe de niveau 
pour la fonction $f$ si les conditions appropriées sont réunies ?


**TODO:** suggérer des fonctions de tests à ce stade, voire des asserts ?

### Propagation

    def level_curve(f, c=0, delta=0.01):
        ...
        return x, y

Evoquer rôle (flou) de delta, condition d'arrêt (sortir du carré, 
non-convergence, etc.)

**TODO.** Validation / test sur fcts testant tel ou tel aspect
(linéaire, bilin, quad, etc.). 

### Intégration

Passage à l'échelle: grille de cube, seed sur coté arbitraire, 
mise bout à bout des morceaux de courbe, etc.

    def contour(f, domain=(0.0,0.0,1.0,1.0), c=0, n=(10,10)):
        ...
        return xs, ys

Exemple test avec notamment morceaux de courbe distincts

<!--
Idées pour poursuivre l'introduction du moteur de diff auto:

  - gérer fct retournant des constantes

  - compléter les opérateurs arithmétiques, fcts usuelles, etc.

  - gérer le control flow (important et pas dur si un peu guidé !)

  - adapter le code pour faire du backward diff (à évaluer),
    avec pointeurs vers articles introductifs.

  - diff d'ordre deux ? Compliqué, 2 show-stoppers potentiels
    (différentiation "lazy" et nodes nestés).

Faire un projet privé et une document de tests (public) pour permettre la
vérification que ça marche ? Demander résultat comme un fichier autodiff.py
+ notebook mise en oeuvre ou notebook générant autodiff.py ?
Quoi qu'il en soit: code et doc et accès sur github.
Ce qui est fait en cours déjà fourni (sous quelle forme ? fichier, 
notebook, etc ?). Oui, avec jupyter nbconvert, ça ne pose pas de pb.
Intégration doctest/notebook ? Bof, non, on gère ça "normalement",
en dehors, avec le truc comme un doc markdown.

Applications (avec algo type IFT par exemple) ? En plus ?
Eventuellement en utilisant un "vrai" autodiff pour ne pas
être bloqué par des étapes précédentes non réussies ? 

-->

Références
================================================================================