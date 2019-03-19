% Calcul Différentiel I

TODO & random Notes
================================================================================

**TODO:** dérivée directionnelles, perspective (se ramener au calcul de
fonction d'une variable), limitations (dérivée partielles très limitée,
dérivée directionnelles un peu moins, mais cas assez général pour supporter
la chain rule suppose de paramétriser par des chemins; lien avec définition
d'Hadamard de la dérivée directionnelle ou $h$ est aussi autorisé à varier).

**TODO.** fonctions à argument et/ou valeurs matricielles.

**TODO:** Notation "function application" sur les applis linéaires.
3 options, dont la contraction $\cdot$

**TODO:** notation multiplication scalaire-vecteur et abus vecteur-scalaire,
voire division vecteur scalaire.

**TODO:** convention sur les normes sur $\mathbb{R}^m$ (euclidienne
par défaut) et $\mathbb{R}^{m \times n}$ (norme d'opérateur par défaut,
introduire la SVD, le lien avec les valeurs propres de $A^t A$ ?)

**TODO:** notation $\mathbb{R}^{m \times n}$ et 
$\mathbb{R}^n \stackrel{\ell}{\to} \mathbb{R}^m$ ici ?
Et équivalent tensoriel / multilinéaire ? Ou dans le contexte
d'utilisation ?

**TODO:** rappel dérivée en préambule différentielle.

$x = (x_1, \dots, x_n) \in \mathbb{R}^n$
$$
\|x\|^2 = \sum_{i=1}^n x_i^2
$$

$A \in \mathbb{R}^{m\times n}$
$$
\|A\| 
= 
\min 
\{
K\geq 0 
\;|\; 
\mbox{pour tout } x \in \mathbb{R}^n, \; \|A x\| \leq K \|x\|
\}.
$$

Notations
================================================================================

Ensembles et Fonctions
--------------------------------------------------------------------------------

**TODO.** produits cartésiens, "currying".

La notation classique $f: A \to B$ pour désigner une fonction $f$ d'un
ensemble $A$ dans un ensemble $B$ suggère de noter $A \to B$ 
l'ensemble des fonctions de $A$ dans $B$.
Avec cette convention, la notation classique $f: A \to B$ signifie la
même chose que $f \in A \to B$; on pourra donc parfaitement continer à 
utiliser la notation classique.

La convention que nous adoptons a vocation à simplifier la manipulation
de fonctions dont les valeurs sont des fonctions, un schéma très fréquent
en calcul différentiel. Nous désignerons ainsi $A \to B \to C$ l'ensemble
des fonctions qui associent à un élément de $A$ une fonction de $B$ dans
$C$, c'est-à-dire une fonction appartenant à $A \to (B \to C)$ (notre
convention est donc associative à droite).

Si $f: A \to B$ et $g: B \to C$, la composée des functions $f$ et de $g$,
notée $g \circ f$, appartient à $A \to C$ et est définie par
$$
(g \circ f) (x) = g(f(x)).
$$
Si l'on applique bien $f$ à $x$, puis $g$ au résultat, il est néanmoins
naturel d'inverser l'ordre d'apparition des functions dans la notation $g \circ f$;
il faut en effet s'adapter à la notation classique (infixe ou polonaise) 
qui désigne par $f(x)$ l'image de $x$ par $f$. 
Pour cette même raison, il pourra être utile de
d'utiliser $B \leftarrow A$ comme une variante de $A \to B$.
On pourra alors utiliser la règle mécanique
$$
\begin{array}{c}
g: C \leftarrow B, \; f: B \leftarrow A \\
\implies \\
g \circ f: C \leftarrow A
\end{array}
$$
ou les notations des ensembles et fonctions $g$, $f$, $A$, $B$ et $C$
restent dans le même ordre d'apparition et les deux occurrences de 
l'ensemble intermédiaire $B$ se touchent.

Applications Linéaires et Calcul Matriciel
--------------------------------------------------------------------------------

Pour tout scalaire $\lambda \in \mathbb{R}$ et vecteur $x \in \mathbb{R}^n$,
on notera $\lambda x$ ou parfois $x \lambda$ la multiplication du vecteur $x$ 
par le scalaire $\lambda$. Lorsque $\lambda$ est non nul, on
notera également $x / \lambda$ le vecteur $(1 / \lambda) x$.

**TODO:** multiplication scalaire et matrice ? produit tensoriel également
noté sans rien ...

En cohérence avec la notation choisie pour les ensembles de fonctions, 
nous noterons
$\mathbb{R}^n \stackrel{\ell}{\to} \mathbb{R}^m$ 
(ou $\mathbb{R}^m \stackrel{\ell}{\leftarrow} \mathbb{R}^n$ 
quand c'est opportun)
l'ensemble des applications linéaires de $\mathbb{R}^n$ dans $\mathbb{R}^m$.

Nous noterons $\mathbb{R}^{m \times n}$ l'ensemble des matrices à 
$m$ lignes et $n$ colonnes à coefficients réels. 
Attention, dans cette notation, $\times$ est un symbole de séparation, 
purement syntactique; 
$m \times n$ n'est pas une expression ayant vocation à être calculée. 
Ainsi $\mathbb{R}^{2 \times 2}$ désigne l'ensemble des matrices
à $2$ lignes et deux colonnes à coefficients réels quand $\mathbb{R}^4$
désigne l'ensemble des $4$-uplets à coefficients réels. Cette similarité
dans la notation n'est toutefois pas anodine: pour toute matrice 
$A \in \mathbb{R}^{m\times n}$, on peut construire un $mn$-uplet en 
listant tous les coefficients de la matrices, par exemple en parcourant
chaque ligne de haut en bas, puis au sein de chaque ligne de gauche à
droite; cette façon de faire définit un vecteur
$a = (a_1, a_2, \dots, a_{mn})\in \mathbb{R}^{mn}$ par la relation
$a_k = A_{ij}$ ou $k = (i-1) m + j$.
L'application $\pi$ qui a la matrice $A$ associe le vecteur $a$ 
est une bijection entre les deux espaces $\mathbb{R}^{m \times n}$ et 
$\mathbb{R}^{mn}$, linéaire ainsi que sont inverse; on dira que
ces deux espaces vectoriels sont isomorphes, 
ce que l'on notera $\mathbb{R}^{m \times n} \simeq \mathbb{R}^{mn}$.
En toute rigueur, $\pi$ n'est pas une fonction, mais une famille de 
fonctions, paramétrisée par $m$ et $n$.

    >>> from numpy import *
    >>> A = array([[1,2,3], [4,5,6]])
    >>> A
    array([[1, 2, 3],
           [4, 5, 6]])
    >>> shape(A)
    (2, 3)
    >>> size(A)
    6
    >>> reshape(A, size(A))
    array([1, 2, 3, 4, 5, 6])
    >>> A = array([[1,2,3], [4,5,6]])
    >>> shape(A)
    (2, 3)
    >>> size(A)
    6
    >>> a = reshape(A, size(A))
    >>> a
    array([1, 2, 3, 4, 5, 6])
    >>> shape(a)
    (6,)
    >>> reshape(a, (2,3))
    array([[1, 2, 3],
          [4, 5, 6]])


Si $M$ est une telle matrice,
$M_{ij}$ ou $m_{ij}$ désigne le coefficient en ligne $i$ et colonne $j$.
Ces deux ensembles sont étroitement liés.

Les matrices $m \times n$ permettent de représenter des applications 
linéaires de $\mathbb{R}^{n}$ dans $\mathbb{R}^m$.

Soit $A$ une application linéaire de $\mathbb{R}^n$ dans $\mathbb{R}^m$.
On peut décomposer $A$ en $m$ composantes $A_i$, 
des applications de $\mathbb{R}^n$ dans $\mathbb{R}$ 
telles que pour tout $x$ dans $\mathbb{R}^n$, on ait
$A(x) = (A_1(x), A_2(x), \dots, A_m(x))$, ce que l'on note
simplement
$$
A = (A_1, A_2, \dots, A_m).
$$
Si l'on désigne maintenant par $e_j$ le $j$-ème vecteur de la base canonique de 
$\mathbb{R}^n$
$$
e_1 = (1, 0, 0, \dots, 0), \; e_2 = (0,1,0,\dots, 0), \; \dots \;, \;
e_n = (0,0,0,\dots, 1),
$$
il est possible d'associer à l'application linéaire 
$A: \mathbb{R}^n \to \mathbb{R}^m$ la matrice
$$
[A] := [A_{ij}]_{ij} :=
[A_i(e_j)]_{ij}=
\left[ 
\begin{array}{ccccc}
A_1(e_1) & A_1(e_2) & \cdots & A_1(e_n) \\
\vdots & \vdots & \vdots & \vdots\\
A_m(e_1) & A_m(e_2) & \cdots & A_m(e_n)
\end{array}
\right] \in \mathbb{R}^{m \times n}.
$$
Inversement, étant donné une matrice
$$
[a_{ij}]_{ij}=
\left[ 
\begin{array}{ccccc}
a_{11} & a_{12} & \cdots & a_{1n} \\
\vdots & \vdots & \vdots & \vdots\\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{array}
\right] \in \mathbb{R}^{m \times n},
$$
il est possible de définir une application linéaire 
$A: \mathbb{R}^n \to \mathbb{R}^m$ par la relation
$$
(A x)_i := \sum_{j} a_{ij} x_j.
$$
Cette deux construction sont inverses l'une de l'autre et établissent un
isomorphisme d'espaces vectoriels entre les applications linéaires de
$\mathbb{R}^n$ dans $\mathbb{R}^m$ et les matrices de taille $m \times n$
à coefficients réels.
$$
\mathbb{R}^m \stackrel{\ell}{\leftarrow} \mathbb{R}^n
\simeq 
\mathbb{R}^{m \times n} 
$$

L'intérêt central des représentations matricielles: la composition de fonctions
linéaires se traduit par une multiplication entre matrices. Si $A$ et $B$ 
désignent des applications linéaires de $\mathbb{R}^p$ dans $\mathbb{R}^n$
et de $\mathbb{R}^n$ dans $\mathbb{R}^m$ respectivement, 
l'application linéaire composée $C = B \circ A$ vérifie
  $$
  C_{ij} = \sum_{k} B_{ik} A_{kj}.
  $$
Dans la suite on évitera en général l'utilisation du symbole $\circ$ pour
désigner la composition d'applications linéaires, en lui préférant le
symbol $\cdot$. Le même symbole sera utilisé pour désigner le produit
entre deux matrices (on évitera dans la mesure du possible de désigner
le produit de deux matrices par simple juxtaposition des symboles; 
on réservera cette notation pour la multiplication d'un vecteur ou
d'une application linéaire par un scalaire).

------------------------------------------------

Dans le cadre du calcul matriciel, on associe en général à un vecteur 
$x=(x_1, \dots, x_n)$ de $\mathbb{R}^n$ le vecteur colonne
$$
\left[ 
\begin{array}{c}
x_1 \\
\vdots \\
x_n
\end{array}
\right] \in \mathbb{R}^{n \times 1}.
$$
Dans cette terminologie, un vecteur-colonne n'est pas un élément de
$\mathbb{R}^n$, mais une matrice. Formellement, on associé à $x$
une matrice
$X \in \mathbb{R}^{n\times 1}$, telle que $X_{i1} = x_i$.

**TODO:** refaire la présentation "à la main" sans mettre en correspondance
$x$ et l'application linéaire associée et mettre cette explication (qui
explique pourquoi $\cdot$ n'est pas une nouvelle notation et pourquoi
tous ces points sont associatifs) en exo ?

Cette matrice correspond à une application linéaire de $\mathbb{R}$ dans
$\mathbb{R}^n$.
Il n'est pas difficile de se convaincre que cette application est
tout simplement $\lambda \in \mathbb{R} \mapsto x \lambda \in \mathbb{R}^n$.
Le produit matrice-vecteur de $A$ et de $x$ représente donc la composée
de cette application et de $A$; on a "promu" $x$ du statut de vecteur
de $\mathbb{R}^n$ à celui d'application linéaire de $\mathbb{R}$ dans 
$\mathbb{R}^n$ et se faisant on lui a fourni une représentation matricielle.
On utilisera donc également la notation
$A \cdot x$ pour désigner l'image du vecteur $x$ par l'application linéaire
$A$, ou de façon équivalente le produit matrice-vecteur entre $A$ et $x$.

Notons qu'on peut également associer à un vecteur $x \in \mathbb{R}^n$ 
un vecteur-ligne; pour cela, on considère l'application linéaire
$x^t$ de $\mathbb{R}^n$ dans $\mathbb{R}$ définie par
$$
x^t \cdot y = \left< x, y \right> = \sum_i x_i y_i
$$
donc la matrice associée est un vecteur ligne.

Le produit matriciel étant associatif, tant que l'on manipule des matrices
et des vecteurs, il n'y a pas lieu de préciser si $A \cdot B \cdot C$ 
désigne $(A \cdot B) \cdot C$ (association à gauche) ou $A \cdot (B \cdot C)$
(association à droite).
Comme le produit matrice-vecteur est un produit matriciel classique,
quand $x$ est un vecteur, 
$A \cdot B \cdot x$ désigne indifféremment $(A \cdot B) \cdot x$ ou
$A \cdot (B \cdot x)$.

------------------------------------------------

**TODO:** préciser usage multiple du crochet: $[A]$ est une matrice quand
$A$ est une appli line, $[a_{ij}]_{ij}$ est une matrice, quand $x$ est un
vecteur, $x_i$ ou $[x]_i$ désigne son $i$-ème coefficient, etc.
A la limite, cela aurait du sens d'utiliser aussi $[x]$ pour un 
$n$-uplet, afin de le transformer en vecteur colonne (donc une matrice;
dans ce cadre, la notation $[x]^t$ a parfaitement du sens et les deux
"mondes", matriciels ou non, restent étanches ... mais les notations
deviennent potentiellement lourdes ...). NOTA: est-ce que j'ai envie
de parler de vecteur colonne ? Cela contribue à "figer" le crochet
au niveau matriciel et donc obère le niveau tensoriel ... Pas dramatique
sans doute, mais dommage parce qu'il est plus simple IMHO même si on se
limite aux matrices et vecteurs et se mappe mieux sur les projets num.





"Petit O" -- Notation de Bachmann-Landau
--------------------------------------------------------------------------------

**TODO:** changer, noter $\|h\|$ sous le petit o, sinon ça ne "passe pas"
aux ordres supérieurs. Grmph, ca pose aussi un certain nombre de problèmes
(l'expression finale ne dépend pas que de la norme). Résoudre ça.
Je me demande dans quelle mesure je ne suis pas à deux doigts d'oublier Landau
pour conserver la notation explicite $\varepsilon(h)\|h\|$.

La notation "$o$" est utilisée pour désigner une expression de la forme
$$
o(\phi(h)) := \varepsilon(h) \|\phi(h)\|
\; \mbox{ où } \;
\lim_{h \to 0} \varepsilon(h) = \varepsilon(0) = 0.
$$

**TODO:** "détails"
où $\varepsilon$ est une fonction 
-- scalaire ou vectorielle selon le contexte -- 
définie dans un voisinage de $0 \in \mathbb{R}^n$ et telle que ...

Expliquer aussi l'inverse: une équation avec un $o$ est vraie si on peut
trouver une fct dans la "classe" du o qui rend vraie l'équation.

--------------------------------------------------------------------------------

Par exemple, une fonction $f$ définie dans un voisinage de 
$x \in \mathbb{R}^n$ et à valeurs dans $\mathbb{R}^m$ est 
continue si et seulement si
$$
f(x+h) = f(x) + o(1).
$$
En effet, la fonction caractérisée par $\varepsilon(h) = f(x+h) - f(x)$
est définie dans un voisinage de $0 \in \mathbb{R}^n$ et c'est la seule
fonction telle que l'on ait $f(x+h) = f(x) + \varepsilon(h) \|1\|$.
Elle vérifie bien $\varepsilon(0) = 0$ et par ailleurs, il est clair
que $\varepsilon$ est continue en $0$ si et seulement si $f$ est continue
en $x$.

Différentielle
================================================================================

### Différentielle {.definition .theorem}

Soit $f: U \subset \mathbb{R}^n \to \mathbb{R}^m$ où $U$ est ouvert.
La fonction $f$ est *[différentiable]{.index}* en $x \in U$ s'il 
existe une application linéaire $L: \mathbb{R}^n \to \mathbb{R}^m$
telle que
$f(x+h) = f(x) + L \cdot h + o(h).$
Si c'est le cas, l'application $L$ est unique; nous la notons alors
$df(x)$ et l'appelons *[différentielle de $f$ en $x$]{.index}*.
Elle est donc caractérisée par:
$$
f(x+h) = f(x) + df(x) \cdot h + o(h).
$$
La fonction $f$ est *différentiable*
si elle est différentiable en tout point de $U$. 

### Note

On pourra parler de fonction $f$ différentiable *sur $U$* si le domaine de 
définition de la fonction n'est pas évident dans le contexte (cas particulier
des expressions, à suivre).

### TODO: pourquoi ouvert

(pas stricto sensu nécessaire mais plus simple; permet de se poser la question
de l'existence de la différentielle en tout point du domaine de définition. 
donner exemple avec branche de log définie
sur $\mathbb{C}^*$; on peut se poser la question de la différentiation
partout sauf sur $\mathbb{R}^-$.)

### TODO: lien avec dérivée

A faire dans le cas domaine de la dérivée ouvert d'abord. Puis, via l'extension,
montrer que cette restriction n'est pas limitative et permet aussi de traiter
le cas des dérivées à droite et à gauche si besoin. (et portée du système
d'extension assez général ...)

### Expressions

**NOTA:** expliquer que $df(x)$ est $d(f)(x)$, pas $d(f(x))$ ... donc pas
expression-friendly a priori ... Oui faire l'anatomie des "slots", comment
la notation se lit: symbole "d", puis trois slots: fonction, point, variation.

**TODO:** permetre d'écrire des choses comme

$$
d(x_1x_2) \cdot (h_1, h_2) = h_1 x_2 + x_1 h_2 
$$

Pfff ... A la fois pas aussi simple que
$$
d(xy) = xdy + y dx
$$
et en même temps plus ambigu, car dans la notation au-dessus, on n'a pas
d'info sur la position des divers arguments si l'on utilise les noms
$x$ et $y$: on ne peut pas savoir que $x$ correspond à $h_1$ et $y$ à $h_2$.
Mais l'interprétation avec les formes différentielles .... mmmm Nope.

Donc interpréter plutôt $d(xy)$ comme un raccourci pour
$$
df(x, y) \cdot (dx, dy)
\; \mbox{ où } \; 
f(x, y) = xy
$$
? Pas sans risque, le statut de $df$, $dx$ et $dy$ est différent ... Raaah.
Mais c'est le seul truc qui tient un peu la route sans introduire les formes
différentielles.

Ou alors, noter les fonctions de façon appropriée avec une notation infixe ?
Par exemple:
$$
d(+)(x, y) \cdot (h, k) = h y + x k 
$$
Horrible ... Oublier donc les expressions en première instance ?

$$
d(x y) = (\Delta x) y + x (\Delta y)
$$
bof. Confusoaire ...


### Note {.author}
Intégrer dès maintenant le pb de la différentiation des "expressions",
comme $x_1+x_2$. Possible ? Suppose aussi de parler dès maintenant de fcts
différentiables sur tout leur domaine puisque fondamentalement, ce
sont des notations de champs qui simplifient ici la vie ...
Mais on veut retarder la notion d'application différentielle ?
Numéro d'équilibriste ... ce que l'on veut éviter, c'est de raisonner
sur les espaces des valeurs associés (qui sont fonctionnels ... et peuvent
donner le vertige)

### Note {.author}
Même si la notation de la différentielle en $a$ donne un indice sur l'étape
suivante, il faut probablement retarder l'apparition de la notion d'application
différentielle et construire une familiarité avec la notion de différentielle 
en $a$ avant de passer à l'étape d'après.
La notion d'application différentielle ne devient nécessaire que pour parler
de fonction continûment différentiable et de différentielle d'ordre supérieur.


--------------------------------------------------------------------------------

**TODO:** différentielle d'une fonction à valeurs "tensorielles"
(vecteur, matrice).

--------------------------------------------------------------------------------

Dans le cas où $f$ est une fonction d'une unique variable réelle,
les deux concepts de dérivée et de différentielle coexistent et
sont étroitement liés.

### Différentielle et Dérivée {.theorem}

Soit $f: U \subset \mathbb{R} \to \mathbb{R}^m$ où $U$ est ouvert
et soit $a \in U$.
La fonction $f$ est différentiable en $a$ si et seulement si
elle est dérivable en $a$. Dérivée et différentielle de $f$ en 
$a$ se déduisent alors l'une de l'autre par les relations 
$$
f'(a) = df(a) \cdot 1
\; \mbox{ et } \;
df(a) = (h \in \mathbb{R} \mapsto f'(a) h).
$$

### Différentiation de Fonction Composée

Soit $f: U \subset \mathbb{R}^p \to \mathbb{R}^{n}$ et 
$g: V \subset \mathbb{R}^n \to \mathbb{R}^{m}$ deux fonctions définies
sur des ouverts $U$ et $V$ et telles que $f(U) \subset V$. 
Si $f$ est différentiable en $x \in U$ et $g$ est différentiable en $f(x) \in V$,
alors la composée $g \circ f$ est différentiable en $x$ et
$$
d(g \circ f)(x) = dg(f(x)) \circ df(x)
$$

### Remarque {.remark}

**TODO:** Inverser l'approche ? Donner dans le théorème le résultat avec la
variable intermédiaire, puis s'en passer en remarque, voire écrire
simplement $d(g\circ f) = (dg \circ f) df$, avec toutes
les ambiguités que cela peut engendrer ... 

En clair, la différentielle de $f$ et $g$ en $x$ est la composée des
différentielles de $f$ en $x$ et de $g$ en $y=f(x)$.
Il peut être utile pour se familiariser avec ce résultat d'expliciter
le rôle de la variable intermédiaire $y$ dans la formule ci-dessus:
$$
d(g\circ f)(x) = dg(y) \circ df(x) \; \mbox{ où } \; y = f(x).
$$
En complément, annoter les composants d'une formule avec les ensembles 
auquels ils appartiennent permet de s'assurer qu'elle n'est pas 
trivialement incorrecte. Ici par exemple:
$$
\stackrel{\mathbb{R}^m \leftarrow \mathbb{R}^p}{d(g\circ f)(x)} 
\, = \,  
\stackrel{\mathbb{R}^m \leftarrow \mathbb{R}^n}{dg(y)} 
\circ 
\stackrel{\mathbb{R}^n \leftarrow \mathbb{R}^p}{df(x)} \; \mbox{ où } \; y = f(x).
$$



### Preuve

L'objectif de la preuve est de montrer que
$$
g(f(x+h)) - g(f(x)) =  (dg(f(x)) \circ df(x)) \cdot h + o(h).
$$
La fonction $g$ étant différentiable en $f(x)$, il existe une fonction 
$\varepsilon_1$ définie sur un voisinage de $0$ et à valeurs dans $\mathbb{R}^m$
telle que $\varepsilon_1(k) \to \varepsilon_1(0)= 0$ quand $k$ tend vers $0$ et
$$
g(f(x)+k) - g(f(x)) = dg(f(x)) \cdot k + \varepsilon_1(k) \|k\|.
$$
Choisissons $k=f(x+h) - f(x)$ dans cette équation, de telle sorte que
$$
g(f(x)+k) = g(f(x) + (f(x+h) - f(x)) = g(f(x+h)).
$$
Nous obtenons donc
$$
g(f(x+h)) - g(f(x)) = dg(f(x)) \cdot (f(x+h)-f(x)) + \varepsilon_1(k) \|k\|.
$$

Notons que la fonction $\varepsilon_2(h) = \varepsilon_1(f(x+h) - f(x))$
est définie dans un voisinage de l'origine et que par continuité de $f$ en 
$x$, $f(x+h) - f(x)$ tend vers $0$ quand $h$ tend vers $0$, et par conséquent
$\varepsilon_2(h) \to \varepsilon_2(0) = 0$ quand $h\to 0$.
On a donc
$$
\begin{split}
g(f(x+h)) - g(f(x)) &= dg(f(x)) \cdot (f(x+h)-f(x)) \\
                    &\phantom{=} + \varepsilon_2(h) \|f(x+h)-f(x)\|.
\end{split}
$$


Comme $f$ est différentiable en $x$, il existe une fonction 
$\varepsilon_3$ définie sur un voisinage de $0$ et à valeurs dans $\mathbb{R}^n$
telle que $\varepsilon_3(h) \to \varepsilon_3(0)= 0$ quand $h$ tend vers $0$ et
$$
f(x+h) - f(x) = df(x) \cdot h + \varepsilon_3(h) \|h\|.
$$
En substituant cette relation dans la précédente, nous obtenons
$$
g(f(x+h)) - g(f(x)) = dg(f(x)) \cdot (df(x) \cdot h) + \varepsilon(h) \|h\|
$$
où $\varepsilon(0) = 0$ et dans le cas contraire,
$$
\varepsilon(h) = \varepsilon_2(h) \|df(x) \cdot (h / \|h\|) + \varepsilon_3(h) \| + dg(f(x)) \cdot \varepsilon_3(h).
$$
Il suffit pour conclure de prouver que $\varepsilon(h) \to 0$ quand $h \to 0$.
Or, 
$$
\begin{split}
\|\varepsilon(h)\| & \leq \|\varepsilon_2(h)\| \times \|df(x) \cdot (h / \|h\|) \| + \|\varepsilon_2(h)\| \times \|\varepsilon_3(h) \| + \|dg(f(x)) \cdot \varepsilon_3(h)\| \\
& \leq \|\varepsilon_2(h)\|  \times \|df(x)\| + \|\varepsilon_2(h)\| \times \|\varepsilon_3(h) \| + \|dg(f(x))\| \times \|\varepsilon_3(h)\|
\end{split}
$$
le résultat est donc acquis.



### Règles de la Somme et du Produit

Les applications somme $(x, y) \in \mathbb{R}^n \times \mathbb{R}^n \mapsto x + y$
et produit $(x, y) \in \mathbb{R}\times\mathbb{R} \to \mathbb{R}$ sont différentiables.
Leurs différentielles au point $(x, y)$ satisfont:
$$
d(x, y \mapsto x + y) \cdot (dx, dy) = dx + dy
$$
$$
d(x, y \mapsto x \times y) \cdot (dx, dy) = x dy + y dx 
$$

**TODO:** notation $d_{xy}$ pour alléger le reste ? (qui est par ailleurs
encore abusif malgré la lourdeur ... Rk: dans $df(x)$, on pourrait croire
que $d$ s'applique à l'expression $f(x)$, mais ça n'est pas l'esprit ...
donc rigoureusement plus haut je devrait écrire des choses comme:
$d(x, y \mapsto x + y)(x, y) \cdot (h_1, h_2)$. L'usage répété de $x$ et de
$y$ n'est qu'une "coincidence". Ici, l'écart avec ce que l'on a envie
d'écrire, à savoir $d(x+y) = dx + dy$ est particulièrement frappant.
Y'a-t'il une solution sans complexifier outre mesure de bénéficier de
ce niveau de simplicité des calculs ? Au moins accepter de différencier
des expressions ?)

### Preuve

**TODO**


**TODO:** (cas matriciel pour le produit ? A un moment ?)


Matrice Jacobienne
================================================================================

Quelle est la représentation matricielle $[df(x)]$ de la différentielle de
$f$ en $x$ quand celle-ci existe ? Il s'agit de calculer par définition de
calculer $[df(x) \cdot e_j]_i$. La relation
$f(x+h) = f(x) + df(x) \cdot h + o(\|h\|)$ établit l'existence d'une
fonction $\varepsilon$ définie dans un voisinage de $0$, nulle et continue
en $0$ et telle que $f(x+h) = f(x) + df(x) \cdot h + \varepsilon(h) \|h\|$.
Soit $t \neq  0$; en substituant $h = t e_j$, on obtient
$$
f(x+te_j) = f(x) + df(x) \cdot (t e_j) + \varepsilon(t e_j) \|t e_j\|.
$$
En exploitant la linéarité de la différentielle et en prenant la 
$i$-ème composante de cette équation vectorielle,
$$
[df(x) \cdot e_j]_i = \frac{f_i(x+te_j) - f_i(x)}{t} + \varepsilon_i(t e_j) (\|t\|/t).
$$
Par conséquent, en passant à la limite quand $t \to 0$, on obtient
$$
[df(x) \cdot e_j]_i = \lim_{t \to 0} \frac{f_i(x+t e_j) - f_i(x)}{t}.
$$
Quelques notations et définitions permettent de capturer ce résultat.

**TODO:** la décomposition en composant dès ce stade est un poil pénible
puisqu'elle n'est pas nécessaire au stade de la dérivée partielle ...
Oui on peut revenir en arrière et travailler ligne par ligne.

### Dérivée Partielle {.definition}

Soit $f: U \subset \mathbb{R}^n \to \mathbb{R}^m$ où $U$ est un ouvert.
Soit $x \in U$. Lorsque la limite existe, on appelle $i$-ème dérivée partielle
de $f$ en $x$ le vecteur $\partial_i f(x) \in \mathbb{R}^m$ défini par
$$
\partial_i f(x) = \lim_{t \to 0} \frac{f(x + t e_i) - f(x)}{t}
= \lim_{t \to 0} \frac{f(x_1, \dots, x_i + t, \dots, x_n) - f(x_1, \dots, x_n)}{t} 
$$
Lorsque $f$ est différentiable en $f$, toutes ses dérivées partielles existent
et vérifient
$$
\partial_i f(x) = df(x) \cdot e_i
$$
ou de façon équivalente, pour tout $h \in \mathbb{R}^n$
$$
df(x) \cdot h = \sum_{i=1}^n \partial_i f(x) h_i
$$

### Preuve 

**TODO:** finir, mais l'essentiel des arguments est dans l'intro.



### Matrice Jacobienne {.definition}


$$
Df(x) = [df(x)] = [\partial_j f_i(x)]_{ij}
=
\left[
\begin{array}{c}
\left[d f_1(x)\right] \\
\vdots \\
\left[d f_m(x)\right]
\end{array}
\right]
$$


**TODO.**


**TODO:** dumb down "différentielles" partielles en "dérivées partielles".
Et c'est une "découverte", on part de la représentation sous forme matricielle
des différentielles, les dérivée partielles ne sont pas considérées comme
un point de départ.

**TODO:** variables nommées, impact notation.

**TODO.** Eventuellement un mot sur le concept d'application partielle ?
Exploiter la chain rule plutôt que la construction élémentaire de l'introduction ?



### TODO

Fcts $C^1$ et réciproque partielle...

Inégalité des accroissement finis
================================================================================


### Différentielle et Intégrale

Pour comparer $f(a+h)$ et $f(a)$ de l'égalité, 
lorsque la fonction $f$ est continue en $a$, 
nous disposons de l'égalité $f(a + h) = f(a) + o(h)$,
mais cette relation est asymptotique. 
Pour maîtriser l'écart entre
$f(a+h)$ et $f(a)$ nous devons être mesure de faire tendre $h$ vers $0$. 
Si la grandeur $h$ est fixé, cette relation est inexploitable. 

Toutefois, dans cette situation, 
si $f$ est différentiable sur tout le segment $[a,b]$, il est possible
de relier $f(a+h)$ à $f(a)$.

### Théorème {.theorem}
Soit $f: U \subset \mathbb{R}^n \to \mathbb{R}^m$ où $U$ est ouvert,
soit $a \in U$ et $h \in \mathbb{R}^n$ tel que le segment $[a, a+h]$
  $$
  [a, a+h] = \{a + th \; | \; t \in [0,1]\}
  $$
soit inclus dans $U$. Si $f$ est différentiable en tout point de $[a, a+h]$,
$$
f(a + h) = f(a) + \int_0^1 df(a+th) \cdot h \, dt.
$$

### Preuve

Considérons la fonction $\phi: [0,1] \to \mathbb{R}^n$ définie par
$$
\phi(t) = f(a + th)
$$
La fonction $\phi$ est dérivable sur $[0,1]$ comme composée des fonction 
différentiables $f$ et $t \mapsto a + th$ et sa dérivée est donnée par
$$
\begin{split}
\phi'(t) &= d\phi(t) \cdot 1 \\
         &= (df(a+th) \circ d(t\mapsto a+th)) \cdot 1 \\
         &= df(a+th) \cdot (d(t\mapsto a+th) \cdot 1) \\
         &= df(a+th) \cdot (t \mapsto a+th)' \\
         &= df(a+th) \cdot h
\end{split}
$$
Par le théorème fondamental du calcul, on a donc
$$
f(a+h) - f(a) = \phi(1) - \phi(0) = \int_0^1 \phi'(t) \, dt 
                                  = \int_0^1 df(a+th) \cdot h \, dt.
$$




### Inégalité des accroissements finis (fonction d'une variable réelle) {.theorem}

Soit $f:[a, b] \to \mathbb{R}^m$ 
où $a \in \mathbb{R}$, $b \in \mathbb{R}$, $a \leq b$ et $m \in \mathbb{N}$.
Si $f$ est dérivable sur $[a,b]$ et $M$ est un majorant de $\|f'\|$,
c'est-à-dire si
$$
\mbox{pour tout } t \in [a, b], \;\|f'(t)\| \leq M.
$$
Alors 
$$
\|f(b) - f(a)\| \leq M (b-a)
$$

### Preuve {.proof}

Par définition, la fonction $f'$ est intégrable au sens de Newton et
$$
f(b) - f(a) = \int_a^b f'(t) \, dt.
$$
Elle est donc également intégrable au sens de Henstock-Kurzweil
**[TODO: référence]**;
en combinant la définition de l'intégrale de Henstock-Kurzweil 
et le lemme de Cousin, on peut trouver des approximations arbitrairement
précises de l'intégrale de $f'$ par des sommes de Riemann:
pour tout $\varepsilon > 0$, 
il existe une subdivision pointée $\mathcal{D}$
de l'intervalle $[a,b]$ telle que 
$$
\left\| f(b) - f(a) -  S(f', \mathcal{D}) \right\| 
=
\left\| \int_a^b f'(t) \, dt -  S(f', \mathcal{D}) \right\| 
\leq 
\varepsilon.
$$
En exploitant l'inégalité triangulaire, on obtient donc
$$
\|f(b) - f(a)\|
\leq 
\|S(f', \mathcal{D})\| + \varepsilon.
$$
Supposons que 
$\mathcal{D} = \{(t_i, [x_i, x_{i+1}]) \; | \; 0 \leq i \leq p-1 \}$.
En utilisant à nouveau l'inégalité triangulaire, 
on peut majorer en norme la somme de Riemann $S(f',\mathcal{D})$:
$$
\|S(f', \mathcal{D})\|
=
\left\|\sum_{i=0}^{p-1} f'(t_i) (x_{i+1} - x_i)\right\|
\leq 
\sum_{i=0}^{p-1} \|f'(t_i)\| |x_{i+1} - x_i|.
$$
Comme $\|f'(t_i)\| \leq M$ pour tout $i \in \{0,\dots,p-1\},$
$$
\sum_{i=0}^{p-1} \|f'(t_i)\| |x_{i+1} - x_i|
\leq
\sum_{i=0}^{p-1} M |x_{i+1} - x_i|
\leq M \sum_{i=0}^{p-1} |x_{i+1} - x_i|
$$
Finalement, comme $a=x_0 \leq x_1 \leq \dots x_p = b$,
$$
\sum_{i=0}^{p-1} |x_{i+1} - x_i| = \sum_{i=0}^{p-1} (x_{i+1} - x_i) =
x_p - x_0 = b - a
$$ 
et donc 
$\|S(f', \mathcal{D})\| \leq M (b - a).$
Par conséquent, $\|f(b) - f(a)\| \leq M(b-a) + \varepsilon$
et comme le choix de $\varepsilon > 0$ est arbitraire, on en déduit
le résultat cherché: $\|f(b) - f(a)\| \leq M(b-a).$


### Inégalité des accroissements finis {.theorem}

Soit $f: U \subset \mathbb{R}^n \to \mathbb{R}^m$ où $U$ est ouvert,
supposée différentiable en tout point d'un segment $[a, a+h]$ inclus 
dans $U$ et dont la différentielle est majorée en norme par $M$ sur $[a, a+h]$, 
c'est-à-dire telle que
$$
\mbox{pour tout } x \in [a, a+h], \;\|df(x)\| \leq M.
$$
Alors 
$$
\|f(a+h) - f(a)\| \leq M \|h\|
$$

### Preuve {.proof}

Steps: define $\phi: t \in [0,1] \mapsto f(a+th)$.
Deduce $\phi'(t) = df(a+th)(h)$ (chaine + rule + derivative/differential link).
Conclude with [above][Inégalité des accroissements finis (fonction d'une variable réelle)]

Points critiques
================================================================================

Différentielles d'ordre supérieur
================================================================================

Do's and don't {.note}
--------------------------------------------------------------------------------

Ne pas expliciter la correspondance avec les applis $n$-linéaires en général
(l'isomorphisme de trop). Une notation serait probablement la bienvenue,
mais la collection des $\cdot h \cdot h \dots$ en $(h, h, \dots)$ peut
être ambigu (pourrait être lue comme la décomposition d'un vecteur ...).
Trouver une solution ici. OK, on se contente de multiplier les dots,
avec convention association à gauche ("greedy")

Ce qui importe:

  - comprendre comment "passer à l'échelle" de la diff à la diff d'ordre 2,
    qu'il n'y a "rien de nouveau" si l'on a déja compris comment différencier
    une fonction à valeurs matricielle (/tensorielle).

  - donc dvlper en préambule le calcul diff appliqué aux fcts à valeurs 
    fonctionnelles/tensorielles. Ne pas faire l'équivalent pour les arguments,
    cela n'est pas nécessaire pour traiter du calcul différentiel d'ordre
    supérieur.

  - comprendre comment calculer $d^2f(x)\cdot k \cdot h$ quand on sait
    qu'il existe sans "monter dans les étages" (trick: différencier
    $df(x)\cdot h$).

  - comprendre quel terme représente $d^2f(x)\cdot k \cdot h$ en pratique,
    quelle approximation ce terme fait. (Nota: au passage 
    c'est crucial pour établir la symmétrie !).

  - représentation tensorielle, dérivées partielles. Application au Hessien.

  - Sommes de Taylor (avec o, avec reste intégral)

Nota: peut-être opportun de minimiser le coté diff par les valeurs matricielles.
Idées serait de caractériser $df$ en vérifiant la différentiabilité de
$x \mapsto df(x)\cdot h$ pour tout $h$: on ne "monte" pas en rang et
on peut définit $d^2f(x) \cdot k \cdot h := d(x \mapsto df(x)\cdot h)(x) \cdot k$

Différentielles d'ordre supérieur
--------------------------------------------------------------------------------

### Différentielle d'ordre 2 {.definition}

Soit $f: U \subset \mathbb{R}^n \to \mathbb{R}^m$ une fonction différentiable
dans un voisinage d'un point $x$ de $U$. On dira que $f$ est 
*deux fois différentiable en $x$* si pour tout vecteur $h$ de $\mathbb{R}^n$.
La fonction $x \mapsto df(x) \cdot h$ est différentiable en $x$.
La *différentielle d'ordre $2$ de $f$ en $x$*, notée $d^2f(x)$, 
est définie comme l'application linéaire telle que pour tout $h$ 
dans $\mathbb{R}^n$,
$$
d^2 f(x) \cdot h := d(x\mapsto df(x)\cdot h)(x),
$$
c'est-à-dire pour tout vecteur $k$ de $\mathbb{R}^n$,
$$
d^2f(x) \cdot h \cdot k = d(x\mapsto df(x)\cdot h)(x) \cdot k.
$$

### Remarques

  - On peut vérifier que le terme $d(x\mapsto df(x)\cdot h)(x)$ dépend 
    bien linéairement de $h$, ce qui justifie l'assertion que $d^2f(x)$
    est linéaire et la notation "$\cdot$" lorsqu'elle est appliquée à un
    argument $h$.

  - Par construction, le terme $d(x\mapsto df(x)\cdot h)(x)$ 
    est une application linéaire de $\mathbb{R}^n \to \mathbb{R}^m$, 
    donc la fonction $d^2f(x)$
    associe linéairement à un vecteur de $\mathbb{R}^n$ une application
    linéaire de $\mathbb{R}^n \to \mathbb{R}^m$. Autrement dit,
    $$
    d^2f(x) \in (\mathbb{R}^n \stackrel{\ell}{\to} (\mathbb{R}^n \stackrel{\ell}{\to} \mathbb{R}^m)),
    $$
    ce qui se décline successivement en
    $$
    d^2f(x) \cdot h \in (\mathbb{R}^n \stackrel{\ell}{\to} \mathbb{R}^m),
    \; \mbox{ et } \;
    (d^2f(x) \cdot h) \cdot k \in \mathbb{R}^m.
    $$

  - Pour alléger ces notations, on pourra considérer que dans les notations
    d'espace fonctionnels, le symbole "$\to$" associe à droite, par exemple:
    $$
    A \to B \to C := A \to (B \to C),
    $$
    $$    
    A \to B \to C \to D := A \to (B \to (C \to D))
    $$
    et inversement, lors de l'application d'une fonction linéaire,
    le symbole "$\cdot$" associe à gauche, par exemple:
    $$
    L \cdot h \cdot k :=  (L \cdot h) \cdot k,
    $$
    $$
    L \cdot h \cdot k \cdot l := ((L \cdot h) \cdot k) \cdot l.
    $$


### Variation de la différentielle {.theorem} 
Soit $f: U \subset \mathbb{R}^n \to \mathbb{R}^m$ une fonction 
deux fois différentiable en un point $x$ de $U$. On a
$$
df(x+k) = df(x) + d^2 f(x) \cdot \bullet \cdot k + o(\|k\|)
$$

**TODO:** en pratique, on combinera le résultat ci-dessus avec la symmétrie
de la différentielle d'ordre 2 pour mémoriser le résultat. Mais ce résultat
est lui-même utile dans la preuve de la symmétrie. Comment présenter les
résultat au final ? Se débrouiller pour minorer l'impact de la forme 
"temporaire" dans l'exposé oral c'est clair, mais dans le poly comment
faire pour casser la boucle ? Du coup, ce résultat serait un lemme,
et le "vrai" théorème simplifié suivra. OK.

### Remarque
Dans l'équation ci-dessus, le "$o(\|k\|)$" est inséré dans une équation
entre applications linéaires de $\mathbb{R}^n \to \mathbb{R}^m$.
Il doit donc être interprété comme
$$
o(\|k\|) = E(k) \|k\| \; \mbox{ où } \; 
\, E(k) \in \mathbb{R}^n \stackrel{\ell}{\to} \mathbb{R}^m, \,
\lim_{h \to 0} E(k) = E(0) = 0. 
$$


**TODO?**. "Sortir" les lemmes du théorème ? Voire les notation $\Delta f$ ?
Ce sont des résultats majeurs ? (ça éclaire des choses sur ce qu'est 
$d^2f$ et comment la calculer alors pourquoi pas ... ça pourrait aussi nous
éviter des lemmes "nestés" quoi qu'il en soit dans la preuve du théorème.
A la limite, le résultat sur la symmétrie de $\Delta f$ peut rester dedans,
c'est ça le coeur de la preuve. Et je sors l'autre sur l'approximation de
$d^2f$ par $\Delta^2 f$.)

### Preuve
Par définition de la différentielle d'ordre 2 en $x$, 
pour tout vecteur $h$ de $\mathbb{R}^n$ fixé, on a, 
pour tout vecteur $k$ de $\mathbb{R}^n$,
$$
df(x+k) \cdot h = df(x) \cdot h + d^2f(x) \cdot h \cdot k + o(\|k\|),
$$
c'est-à-dire qu'il existe pour tout $h$ une fonction $\varepsilon_h$, 
définie dans un voisinage de $0 \in \mathbb{R}^n$, nulle et continue
en $0$, telle que
$$
df(x+k) \cdot h 
= 
df(x) \cdot h + d^2f(x) \cdot h \cdot k + \varepsilon_{h}(k) \|k\|,
$$
Pour tout vecteur $k$ non nul, on a
$$
\varepsilon_{h}(k) = \frac{1}{\|k\|}\left(df(x+k) \cdot h - df(x) \cdot h - d^2f(x) \cdot h \cdot k \right),
$$
le terme $\varepsilon_{h}(k)$ est donc linéaire en $h$; 
notons $E(k)$ l'application linéaire de $\mathbb{R}^n$ dans $\mathbb{R}^m$
qui est nulle quand $k=0$ et définie dans le cas contraire
par $E(k) \cdot h = \varepsilon_h (k)$. On a donc pour tout $h$
$$
df(x+k) \cdot h 
= 
df(x) \cdot h + d^2f(x) \cdot h \cdot k + (E(k)\cdot h) \|k\|,
$$
soit 
$$
df(x+k)
= 
df(x) + d^2f(x) \cdot \bullet \cdot k + E(k) \|k\|,
$$
Par ailleurs, pour tout couple de 
vecteurs $h$ et $k$ de $\mathbb{R}^n$, on a
$$
\begin{split}
\|E(k) \cdot h\| &= \left\| E(k) \cdot \left(\sum_i h_i e_i \right) \right\| \\
&\leq \sum_i \|E(k) \cdot e_i\| |h_i| \\
&\leq \left(\sum_i \|E(k) \cdot e_i\|\right) \|h\| 
= \left(\sum_i \|\varepsilon_{e_i}(k)\|\right) \|h\|
\end{split},
$$
donc la norme d'opérateur de $E(k)$ vérifie
$$
\|E(k)\| \leq \sum_i \|\varepsilon_{e_i}(k)\| \to 0
\, \mbox{ quand } k \, \to 0,
$$
ce qui prouve le résultat cherché.

### Symmétrie de la différentielle d'ordre $2$ {.theorem}
Soit $f: U \subset \mathbb{R}^n \to \mathbb{R}^m$ une fonction 
deux fois différentiable en un point $x$ de $U$. Pour tout couple
de vecteur $h$ et $k$ de $\mathbb{R}^n$, on a
$$
d^2 f (x) \cdot h \cdot k = d^2 f(x) \cdot k \cdot h.
$$

### Preuve
Notons $\Delta f(x, h) = f(x+h) - f(x)$ la variation de $f$ en $x$ 
associée pour une variation $h$ de l'argument et $\Delta^2 f(x, h, k)$ 
la variation de $\Delta f(x, h)$ en $x$ pour une variation $k$ de l'argument:
$$
\Delta^2 f(x, h, k) = (f(x+k+h) - f(x+k)) - (f(x+h) - f(x)).
$$
Bien qu'elle soit technique, la preuve repose sur deux idées simples.
Tout d'abord, on peut constater directement que $\Delta^2 f(x, h, k)$ 
est symmétrique par rapport à ses arguments $h$ et $k$:

#### Symmétrie de la variation d'ordre 2
$$
\Delta^2 f(x, h, k) = \Delta^2 f(x, k, h). 
$$

--------------------------------------------------------------------------------

Ensuite, il nous faudra montrer que la meilleure approximation bilinéaire de
$\Delta^2 f(x, h, k)$ est donnée par $d^2f(x)\cdot h\cdot k$:

#### Approximation de la variation d'ordre deux {.lemma}
Pour tout $\varepsilon > 0$, il existe un $\eta > 0$ tel que si
$\|h\| \leq \eta$ et $\|k\| \leq \eta$, alors
$$
\left\|\Delta^2f(x, h, k) - d^2f(x)\cdot h\cdot k \right\| \leq \varepsilon (\|h\| + \|k\|)^2.
$$

--------------------------------------------------------------------------------

La conclusion s'imposera alors: en effet, si $h$ et $k$ sont des vecteurs
de $\mathbb{R}^n$ en exploitant la symmétrie de $\Delta^2f$, on obtient
\begin{multline*}
\|d^2f(x) \cdot h \cdot k - d^2f(x) \cdot k \cdot h \|
\leq \\
\|\Delta^2f(x, h, k) - d^2f(x)\cdot h\cdot k\| + \| \Delta^2f(x, k, h) - d^2f(x)\cdot h\cdot k\|.
\end{multline*}
En substituant $th$ à $h$ et $tk$ à $tk$ dans cette expression, 
puis en faisant tendre $t$ vers $0$, on peut rendre $th$ et $tk$ 
arbitrairement proches de $0$ et donc s'assurer que
pour tout $\varepsilon > 0$,
$$
\begin{split}
\|d^2f(x) \cdot h \cdot k - d^2f(x) \cdot k \cdot h \|
&=
\frac{1}{t^2}\|d^2f(x) \cdot th \cdot tk - d^2f(x) \cdot tk \cdot th \| \\
&\leq \frac{1}{t^2}2 \varepsilon (\|th\|+\|tk\|)^2 \\ 
&= 2\varepsilon (\|h\|+\|k\|)^2,
\end{split}
$$
ce qui nous assure que $d^2f(x) \cdot h \cdot k - d^2f(x) \cdot k \cdot h.$

#### Preuve (approximation de la variation d'ordre deux) {.preuve}

**TODO:** $h$ et $k$ assez petits pour que les expressions soient toutes
définies.

La différence $e$ entre $\Delta^2 f(x,h, k)$ et $d^2 f(x) \cdot h \cdot k$
vaut
$$
\begin{split}
e &= (f(x+h+k) - f(x+k)) - (f(x+h) - f(x))) - d^2f(x)\cdot h\cdot k \\
  &= (f(x+h+k) - f(x+h) - d^2f(x) \cdot h \cdot k) \\
  &\phantom{=} - (f(x+k) - f(x) - d^2f(x) \cdot 0 \cdot k)
\end{split}
$$
Par conséquent, si l'on définit $g$ par
$$
g(u) = f(x+u+k) - f(x+u) - d^2f(x) \cdot u \cdot k,
$$
la différence vaut $e = g(h) - g(0).$ Cette différence peut être majorée
par le théorème des accroissements finis: $g$ est différentiable sur
le segment $[0, h]$ et
$$
dg(u) = df(x+u+k) - df(x+u) - d^2f(x) \cdot \bullet \cdot k. 
$$
Comme
$$
\begin{split}
dg(u) &= (df(x+u+k) - df(x) - d^2f(x) \cdot \bullet \cdot (u+k) )\\
      &\phantom{=} - (df(x+u) - df(x) - d^2f(x) \cdot \bullet \cdot u),
\end{split}
$$
par le théorème controllant la [variation de la différentielle][Variation de la différentielle],
pour $\varepsilon > 0$ quelconque, comme
$\|u+k\| \leq \|h\| + \|k\|$ et $\|u\| \leq \|h\|$, 
on peut trouver un $\eta > 0$ tel que si $\|h\| < \eta$ et $\|k\| < \eta,$ 
alors 
$$
\|dg(u)\| \leq \frac{\varepsilon}{2} (\|h\| + \|k\|) + \frac{\varepsilon}{2} \|h\|.
$$
Par conséquent, le théorème des accroissement finis fournit
$$
\|e\| = \|dg(u) - dg(0)\| \leq  \left( \frac{\varepsilon}{2} (\|h\| + \|k\|) + \frac{\varepsilon}{2} \|h\|\right)\|h\| \leq \varepsilon (\|h\| + \|k\|)^2.
$$


--------------------------------------------------------------------------------



--------------------------------------------------------------------------------

La notion de différentielle d'ordre $2$ se généralise sans difficulté
à un ordre plus élevé, par induction sur l'ordre de la différentielle.

### Différentielle d'ordre $k$ {.definition}

Soit $f: U \subset \mathbb{R}^n \to \mathbb{R}^m$ une fonction différentiable
à l'ordre $k-1$ dans un voisinage d'un point $x$ de $U$. On dira que $f$ est 
*$k$ fois différentiable en $x$* si pour tous vecteurs $h_1, \dots, h_{k-1}$ 
de $\mathbb{R}^n$, 
la fonction 
$$x \mapsto d^{k-1}f(x) \cdot h_1 \cdot h_2 \cdots \cdot h_{k-1}$$ 
est différentiable en $x$.
La *différentielle d'ordre $k$ de $f$ en $x$*, notée $d^k f(x)$ 
est définie comme l'application linéaire telle que pour tout 
$h_1, \dots, h_{k-1}$ de $\mathbb{R}^n$,
$$
d^k f(x) \cdot h_1 \cdot h_2 \cdots \cdot h_{k-1} := d(x\mapsto d^{k-1}f(x) \cdot h_1 \cdot h_2 \cdots \cdot h_{k-1})(x)
$$
ou de façon équivalente
$$
d^k f(x) \cdot h_1 \cdot h_2 \cdots \cdot h_{k-1} \cdot h_k:= d(x\mapsto d^{k-1}f(x) \cdot h_1 \cdot h_2 \cdots \cdot h_{k-1})(x) \cdot h_k
$$

### Remarque

On a 
$$
d^kf(x) \in \overbrace{\mathbb{R}^n \to \mathbb{R}^n \to \cdots \to  \mathbb{R}^n}^{k \; \mathrm{termes}} \to \mathbb{R}^m
$$



Fonctions à valeurs matricielles/tensorielles
--------------------------------------------------------------------------------

Objectif: étendre les constructions du calcul différentielle aux fonctions
$f: U \subset \mathbb{R}^p \to \mathbb{R}^{m \times n}$ (après valeurs
scalaires et vectorielles, matricielles).

Etape 1: valeurs interprétée indifférement comme une matrice de taille
$m \times n$ ou comme une application linéaire de $\mathbb{R}^n$ dans
$\mathbb{R}^m$.

### Examples {#ex-vm .example}

On peut associer à tout vecteur $x$ non nul de $\mathbb{R}^n$ la projection 
orthogonale sur $x$; c'est une application linéaire $P(x)$ qui a tout vecteur
$y$ de $\mathbb{R}^n$ associe le vecteur 
$$
P(x) \cdot y = \left<\frac{x}{\|x\|}, y\right> \frac{x}{\|x\|}
= \frac{x}{\|x\|} \cdot \left(\frac{x}{\|x\|}\right)^t \cdot y
$$

Produit scalaire, exp matrice, etc ?

### Définition

**TODO:** motiver la nature de $dF$ quand $F$ est à valeurs fonctionnelles.


Si $F: U \subset \mathbb{R}^n \to \mathbb{R}^{p \times m}$, 
la différentielle de $F$ au point $x \in \mathbb{R}^n$ 
est l'application $dF(x)$ telle que $dF(x)\cdot h$ soit 
la meilleure approximation, linéaire en $h$, de $F(x+h) - F(x)$
pour de petites valeurs de $h$
$$
F(x+h) = F(x) + dF(x) \cdot h + o(h)
$$

L'application $dF(x)$ est donc une application linéaire de 
$\mathbb{R}^n$ dans les applications linéaires de 
$\mathbb{R}^m$ dans $\mathbb{R}^p$:
$$
dF(x): \mathbb{R}^n \stackrel{\ell}{\to} (\mathbb{R}^m \stackrel{\ell}{\to} \mathbb{R}^p)
$$
On peut associer à cette application un tenseur de rang 3, 
**TODO, def etc.**

$$
[dF(x) \cdot e_k \cdot e_j]_i
$$

**TODO** $\cdot$ désigne la contraction tensorielle, composition, etc.
Généraliser le cas matriciel, montrer les correspondances avec le cadre
fonctionnel. Isomorphisme

$$
\mathbb{R}^{m \times n \times n}
\; \simeq \;
\mathbb{R}^m \stackrel{\ell}{\leftarrow} \mathbb{R}^n \stackrel{\ell}{\leftarrow} \mathbb{R}^n
$$

**TODO:** régle du produit:

$H(x) = G(x) \cdot F(x)$,
$$
dH(x) \cdot h = (dG(x) \cdot h) F(x) + (dF(x) \cdot h) G(x)
$$







Misc.
--------------------------------------------------------------------------------
$f: U \subset \mathbb{R}^n \to \mathbb{R}^m$

$df: U \subset \mathbb{R}^n \to (\mathbb{R}^n \stackrel{\ell}{\to} \mathbb{R}^m)$

$$
d^2 f: 
U \subset \mathbb{R}^n 
\to 
(\mathbb{R}^n \stackrel{\ell}{\to} (\mathbb{R}^n \stackrel{\ell}{\to} \mathbb{R}^m))
$$



Tensor stuff


--------------------------------------------------------------------------------

**TODO:** définition. Il va falloir être malin ...


### Théorème 
Si $f: U \subset \mathbb{R}^n \to \mathbb{R}^m$ est deux fois différentiable
en $x$, pour tout $h \in \mathbb{R}^n$ et $k \in \mathbb{R}^n$,
$$
d^2 f(x) \cdot k \cdot h = d(x \mapsto df(x) \cdot k) \cdot h.
$$

### Preuve
**TODO**

### Théorème
**TODO:** approximation concrête de $d^2 f(x) \cdot h \cdot k$.

