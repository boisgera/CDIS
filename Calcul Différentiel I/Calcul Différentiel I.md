% Calcul Différentiel I

<!-- LaTeX Macros -->
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}

\newcommand{\tr}{\operatorname{tr}}

<!--

Narratif & Notes & TODOsss
================================================================================

### Différentielle & Dérivée Directionnelle

La progression choisie est la suivante: 

  - la différentielle d'une fonction en un point est introduite directement,
    par analogie avec le concept et les propriétés de la dérivée, une fois
    présentés sous la bonne forme (meilleure approximation linéaire de la
    variation, forme avec $o$ plutôt que taux d'accroissement).

  - on exploite un peu cette définition, on finit de faire le lien
    avec la dérivée, on donne les règles de combi linéaires, du produit,
    de la différentation en chaîne.

  - sous hypothèse de différentiabilité, on donne le liens avec la dérivée
    partielle et les dérivée directionnnelles.

  - après coup, on examine la tentation (légitime) que l'on pourrait avoir
    de définir la différentielle en passant par les dérivée partielles:
    cette approche si elle était couronnée de succès, permettrait de 
    définir la différentielle en se ramenant à ce que l'on connaît déjà,
    à savoir la notion de dérivée. Et on se rend compte assez facilement
    que:

      - l'existence des dérivées partielles ne suffit pas à assurer 
        l'existence de la différentielle: un exemple très simple permet
        de montrer que cela n'assure même pas la continuité de la fonction
        au point d'intérêt. Plus grave si l'on veut: la règle de dérivation
        en chaîne ne marche pas non plus; en particulier, on ne peut pas
        calculer la dérivée partielle d'une fonction composée par ce biais.
        Note: suppose que l'on ait dérivé la chain rule très rapidement
        après la définition de la différentielle et c'est légitime:
        c'est un grand succès du concept.

      - examiner le contre-exemple standard (1 valeur sur les axes, une
        autre dans le reste du domaine), diagnostiquer ce qui ne va pas
        (à savoir, on est aveugle au comportement de la fonction en dehors
        de directions privilégiées), propose une solution en travaillant
        sur la dérivée directionnelle. Montrer par un nouveau contre-exemple,
        moins évident, que ça ne va toujours pas (ni continuité ni "chain rule").
        L'exemple en question travaille toujours avec deux valeurs distinctes,
        mais sur une parabole. 

      - le nouvelle exemple pour le coup met sur la piste d'une "bonne" solution
        alternative, la dérivée directionnelle au sens d'Hadamard. On peut
        la définir au moyens des chemins, simplifier sa caractérisation.
        Au final, elle vérifie bien la règle de dérivation en chaîne par 
        exemple, plus ou moins par construction, mais cela n'est pas surprenant
        car elle est équivalent à la notion de différentielle !
        A ce stade, pas évident que la démarche adoptée soit plus simple, 
        on peut se convaincre que le concept de différentielle est finalement
        pas si mal que ça ... d'autant plus qu'en dimension infinie, les
        deux notions divergent à nouveau et la différentielle de Fréchet 
        regagne des points.

    Une partie de ça à faire dans le cours, une partie en exo, 
    quelle frontière je ne sais pas encore exactement.

    - en parralèle, on montre que tout de même, on a le droit de travailler
      sur les dérivée partielles si l'on sait établir que le résultat est
      continu, car cela garantit l'existence de la différentielle (et sa
      continuité).

### Vecteurs / Matrices / Tenseurs

Sujet assez compliqué. Trois motivations sur ce sujet:

  - Le "tout-matrice" est assez ridicule quand on y pense;
    l'idée qu'il faille promouvoir des vecteurs de $\mathbb{R}^n$
    en matrice pour faire des calculs complique souvent les choses
    par rapport aux conventions tensorielles (où un vecteur est un
    tableau de dimension 1). C'est aussi assez incohérent avec les
    convention de NumPy qui pour le coup sont tensorielles par nature
    (contrairement à Matlab).

    Mais voilà, c'est la vision enseignée en prépa, difficile de tout
    déconstruire, d'autant que la démarche tensorielle vient avec ses
    propres problèmes de notation, conventions non partagées, etc.

    Donc on a vocation à rester compatible avec ce tout-matriciel;
    et à l'étendre mais de façon compatible quand nécessaire.
    Ainsi, "$\cdot$" interprété comme "application d'une fonction 
    linéaire", même quand la-dite fonction linéaire est à valeurs
    fonctionnelle (comme dans les diff d'ordre supérieur)

  - Il y a des problèmes qui supposent naturellement de considérer
    des fonctions avec des arguments matriciels. Par exemple, on
    comprend assez bien qu'on peut avoir besoin de différencier
    $\det A$ ou $A^{-1}$. Même si le problème final n'a que des
    paramètres vectoriels, on a envie de faire des "chain rules"
    avec des arguments matriciels.

  - Exemple pas trivial mais typique: calculer $d^2f \circ g$.
    A l'ordre $1$ on a $d f \circ g(x) = df(g(x)) \cdot df(x)$, 
    ce qui est (interprétable comme) un produit de matrices.

Positions aujourd'hui:

  - rester dans un premier temps compatible avec le conventions du 
    tout-matriciel, se contenter de noter l'écart avec les conventions
    NumPy, conserver une définition de $\cdot$ qui soit plus générale.

  - minimiser les présentations du tensoriel: on peut se contenter de
    montrer que $d^2f$ est représentable comme un tableau à trois dimensions
    et de faire les calculs avec les indices pour évaluer 
    $d^f(x) \cdot h_1 \cdot h_2$ par exemple; le cas différentielle d'ordre 
    $k$ n'est guère plus complexe.

  - regarder s'il y a des exemples éclairants à faire en TD sur 
    de la différentielle à argument matriciels et "bootstrapper" la
    définition de la différentielle à ce moment-là, en "mettant à plat"
    la matrice par exemple ? Ou exploiter la définition d'Hadamard pour
    éviter d'avoir à faire ça ?

### Normes

Ne rien mettre dans ce chapitre proprement dit, mais lister ce dont on
a besoin très concrètement pour inclure ces éléments dans le chapitre 
de topologie.

J'ai assez envie de noter par défaut $|x|$ les normes dans $\mathbb{R}^n$
et $\|L\|$ la norme d'opérateur et d'annoter ces normes par des symboles
(comme $|x|_2$, $\|A\|_{22}$) dans les contextes ou il faudrait être
plus précis.

Dans ce chapitre j'imagine que l'on peut (presque ?) toujours se limiter aux
normes euclidiennes et à la norme d'opérateur induite, sauf peut-être si
l'on en vient à montrer des choses comme le caractére intrinsèque de la
définition de différentielle ? Non, même là ça va marcher.

Donc concrêtement, définition de ces deux normes, pptés habituelles
(notamment $|Lx| \leq \|L\||x|$). Le coup de la norme d'opérateur
associé à la représentation matricielle (via SVD), utile ou pas ?
Si oui -- et on peut en douter -- alors il faut aussi parler de matrices
dans le chapitre sur la topo. Ouch, non, éviter. En fait, il faudra sans
peut-être "retarder" les rappels sur les opérateurs linéaires à ce chapitre,
car c'est un gros focus du chapitre (idée d'approximation linéaire est 
centrale ici, avant ça serait abstrait).

Auquel cas on parle de norme en topo, on montrer les exemple classiques en
dim finie et on parle d'équivalence des normes,
mais on attend ce chapitre pour parler d'opérateurs et de norme.
Donc un volet à rajouter ici ?

-->

Notations
================================================================================

Préambule
--------------------------------------------------------------------------------

Les fragments de code de ce document utilisent le langage Python 3.
La bibliothèque [NumPy](http://www.numpy.org/) est exploitée:

    >>> from numpy import *

Ensembles et fonctions
--------------------------------------------------------------------------------

La notation classique $f: A \to B$ pour désigner une fonction $f$ d'un
ensemble $A$ dans un ensemble $B$ suggère d'utiliser $A \to B$ 
pour désigner l'ensemble des fonctions de $A$ dans $B$.
Avec cette convention, $f: A \to B$ signifie la
même chose que $f \in A \to B$.

La convention que nous adoptons a vocation à simplifier la manipulation
de fonctions dont les valeurs sont des fonctions, un schéma très fréquent
en calcul différentiel.
Si $f: A \to B$ et $g: B \to C$, la composée des fonctions $f$ et $g$,
notée $g \circ f$, appartient à $A \to C$ et est définie par
$$
(g \circ f) (x) = g(f(x)).
$$
Si l'on applique bien $f$ à $x$, puis $g$ au résultat, il est néanmoins
naturel d'inverser l'ordre d'apparition des fonctions dans la notation $g \circ f$;
il faut en effet s'adapter à la notation classique (infixe ou polonaise) 
qui désigne par $f(x)$ l'image de $x$ par $f$. 
Pour cette même raison, il pourra être utile de
d'utiliser $B \leftarrow A$ comme une variante de la notation $A \to B$.
On pourra alors utiliser la règle
$$
g: C \leftarrow B, \; f: B \leftarrow A \; \implies \; g \circ f: C \leftarrow A
$$
où les notations des ensembles et fonctions $g$, $f$, $A$, $B$ et $C$
restent dans le même ordre d'apparition et les deux occurrences de 
l'ensemble intermédiaire $B$ se touchent.

Applications linéaires et calcul matriciel
--------------------------------------------------------------------------------

### Multiplication scalaire-vecteur
Pour tout scalaire $\lambda \in \mathbb{R}$ et vecteur $x \in \mathbb{R}^n$,
on notera $\lambda x$ ou parfois $x \lambda$ la multiplication du vecteur $x$ 
par le scalaire $\lambda$. Lorsque $\lambda$ est non nul, on
notera également $x / \lambda$ le vecteur $(1 / \lambda) x$.

Un vecteur de $\mathbb{R}^n$ est représenté dans NumPy par un tableau à une
dimension :

    >>> x = array([1, 2, 3])
    >>> x.ndim
    1
    >>> shape(x)
    (3,)
    >>> size(x)
    3

La multiplication d'un scalaire et d'un vecteur est désignée par le symbole
`*`:

    >>> 2 * x
    array([2, 4, 6])

### Matrices

Nous noterons $\mathbb{R}^{m \times n}$ l'ensemble des matrices à 
$m$ lignes et $n$ colonnes à coefficients réels. 
Une matrice telle que

$$
\left[
\begin{array}{ccc}
1 & 2 & 3 \\
4 & 5 & 6
\end{array}
\right] \in \mathbb{R}^{2 \times 3}
$$

sera représentée avec NumPy par un tableau bi-dimensionnel:

    >>> A = array([[1, 2, 3], [4, 5, 6]])
    >>> A
    array([[1, 2, 3],
           [4, 5, 6]])
    >>> A.ndim
    2
    >>> shape(A)
    (2, 3)
    >>> size(A)
    6

### Mise à plat des matrices {.warning #flatten}
Dans la notation $\mathbb{R}^{m \times n}$, 
$\times$ est un symbole de séparation, purement syntactique : 
$\mathbb{R}^{2 \times 3}$ désigne ainsi 
l'ensemble des matrices à 2 lignes et 3 colonnes à coefficients réels 
et diffère de $\mathbb{R}^6$ qui
désigne l'ensemble des $6$-uplets à coefficients réels. 

Ces deux ensembles sont toutefois similaires: pour toute matrice 
$A \in \mathbb{R}^{m\times n}$, on peut construire un $mn$-uplet en 
listant tous les coefficients de la matrices en parcourant l'ensemble 
des lignes de la matrice de haut en bas et chaque ligne de gauche à
droite; cette façon de faire définit un vecteur de $\mathbb{R}^{mn}$.
L'opération ainsi définie sera notée $\pi_{m\times n}$ (voire $\pi$
s'il n'y a pas d'ambiguité).
Par exemple :

$$
\pi_{2 \times 3}: 
\left[
\begin{array}{ccc}
1 & 2 & 3 \\
4 & 5 & 6
\end{array}
\right] \in \mathbb{R}^{2 \times 3}
\; \mapsto \;
(1,2,3,4,5,6) \in \mathbb{R}^6
$$

Cette opération est bijective ; elle-même ainsi que son inverse sont linéaires.
$\mathbb{R}^{m \times n}$ et $\mathbb{R}^{m n}$ sont donc isomorphes (en tant
qu'espace vectoriels), ce que l'on notera :

$$
\mathbb{R}^{m \times n} \, \cong \, \mathbb{R}^{mn}
$$

Le passage de la forme matrice à la forme vecteur se fait de la façon suivante
avec NumPy:

    >>> A
    array([[1, 2, 3],
           [4, 5, 6]])
    >>> a = reshape(A, (6,))
    >>> a
    array([1, 2, 3, 4, 5, 6])
    >>> reshape(a, (2, 3))
    array([[1, 2, 3],
           [4, 5, 6]])

### Applications linéaires

Notons
$$
\mathbb{R}^n \stackrel{\ell}{\to} \mathbb{R}^m
\; \mbox{ ou } \;
\mathbb{R}^m \stackrel{\ell}{\leftarrow} \mathbb{R}^n
$$ 
l'ensemble des applications linéaires de $\mathbb{R}^n$ dans $\mathbb{R}^m$.
La raison d'être des matrices $\mathbb{R}^{m \times n}$ est de représenter
ces applications linéaires.

Si $A$ désigne  une application linéaire de $\mathbb{R}^n$ dans $\mathbb{R}^m$,
on peut la décomposer en $m$ composantes $A_i$, 
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
[A] :=
[A_i(e_j)]_{ij}=
\left[ 
\begin{array}{ccccc}
A_1(e_1) & A_1(e_2) & \cdots & A_1(e_n) \\
\vdots & \vdots & \vdots & \vdots\\
A_m(e_1) & A_m(e_2) & \cdots & A_m(e_n)
\end{array}
\right] \in \mathbb{R}^{m \times n}.
$$
Réciproquement, étant donné une matrice
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
(A x)_i := \sum_{j} a_{ij} x_j
$$
et cette opération est l'inverse de la précédente.

Cette correspondance établit un isomorphisme d'espaces vectoriels entre 
les applications linéaires de $\mathbb{R}^n$ dans $\mathbb{R}^m$ et 
les matrices de taille $m \times n$ à coefficients réels :
$$
\mathbb{R}^m \stackrel{\ell}{\leftarrow} \mathbb{R}^n
\, \cong \,
\mathbb{R}^{m \times n} 
$$

### Composition d'applications linéaires
 
Si $A$ et $B$ désignent des applications linéaires de 
$\mathbb{R}^p$ dans $\mathbb{R}^n$ et de $\mathbb{R}^n$ dans $\mathbb{R}^m$ 
respectivement, la fonction composée $C = B \circ A$ est une application
linéaire qui vérifie
  $$
  C_{ij} = \sum_{k} B_{ik} A_{kj}.
  $$
Autrement dit, la composition de fonction linéaires se traduit par la
multiplication des matrices associées.

Dans la suite on évitera en général l'utilisation du symbole $\circ$ pour
désigner la composition d'applications linéaires, en lui préférant le
symbole $\cdot$ ("point"). 
<!--
Le même symbole sera utilisé pour désigner le produit
entre deux matrices (on évitera dans la mesure du possible de désigner
le produit de deux matrices par simple juxtaposition des symboles).
-->

La méthode `dot` des tableaux NumPy permet de calculer ce produit matriciel :

    >>> A = array([[1, 2, 3], [4, 5, 6]])
    >>> B = array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    >>> A.dot(B)
    array([[1, 2, 3],
           [4, 5, 6]])

### Adjoint d'un opérateur {.definition}
Lorsque $A: \R^n \to \R^m$ est un opérateur linéaire, on peut définir de
façon unique l'opérateur *adjoint* $A^* : \R^m \to \R^n$ comme l'unique
opérateur tel que pour tout $x \in \R^n$ et tout $y \in \R^m$, on ait
$$
\left<y, A \cdot x \right> = \left<A^* \cdot y, x \right>.
$$
La matrice représentant $A^*$ est la transposée de la matrice représentant $A$ :

    >>> A
    array([[1, 2, 3],
           [4, 5, 6]])
    >>> transpose(A)
    array([[1, 4],
           [2, 5],
           [3, 6]])


### Vecteurs colonnes et vecteur lignes
Dans le cadre du calcul matriciel, on associe souvent à un vecteur 
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
Dans cette terminologie, un vecteur colonne n'est pas, 
malgré son nom, un vecteur de $\mathbb{R}^n$, mais bien 
une matrice de taille $n \times 1$. 
Formellement, on a associé à $x$
une matrice
$X \in \mathbb{R}^{n\times 1}$, telle que $X_{i1} = x_i$.
Le produit entre une matrice et un vecteur colonne de taille compatible
n'est rien d'autre qu'un produit matriciel classique. 

Le vecteur $x$ étant associé à une matrice, on peut se demander quel
opérateur linéaire est associé à cette matrice. La réponse est simple:
il s'agit de l'application
$$
\lambda \in \R \mapsto \lambda x \in \R^n.
$$
Identifier un vecteur et son opérateur linéaire de $\R \to \R^n$
permet par exemple de disposer "gratuitement" de la définition 
$x^*$ (l'adjoint de l'opérateur associé à $x$) : il s'agit
de l'application linéaire de $\R^n$ dans $\R$ dont la matrice
est la transposée du vecteur colonne associé à $x$, autrement dit,
la représentation de $x$ comme vecteur ligne.

L'intérêt de la représentation des vecteurs comme vecteurs colonnes : 
si $A$ est une application linéaire de $\mathbb{R}^n$ dans
$\mathbb{R}^m$ et $x$ un vecteur de $\mathbb{R}^n$, le vecteur
image $y=A \cdot x \in \mathbb{R}^m$ de $x$ par $A$ est représenté par 
le vecteur colonne qui est le produit entre 
la représentation de $A$ comme matrice et la représentation de
$x$ comme vecteur colonne.

Concrêtement, NumPy ne nécessite pas qu'un vecteur soit d'abord 
transformé en matrice pour réaliser un produit matrice-vecteur.
La méthode `dot` des tableaux peut être utilisée ici aussi 
pour réaliser cette opération:

    >>> A = array([[1, 2, 3], [4, 5, 6]])
    >>> x = array([7, 8, 9])
    >>> A.dot(x)
    array([ 50, 122])

Le produit matriciel étant associatif, tant que l'on manipule des matrices
et des vecteurs, il n'y a pas lieu de préciser si $A \cdot B \cdot C$ 
désigne $(A \cdot B) \cdot C$ (association à gauche) ou $A \cdot (B \cdot C)$
(association à droite).
Comme le produit matrice-vecteur est un produit matriciel classique,
quand $x$ est un vecteur, 
$A \cdot B \cdot x$ désigne indifféremment $(A \cdot B) \cdot x$ ou
$A \cdot (B \cdot x)$.

Notation de Landau
--------------------------------------------------------------------------------

<!--
### Objectif {.meta}

Présenté volontairement dans le cadre le plus étroit possible qui satisfasse
nos besoins (notamment, comparaison par rapport $\|h\|^k$) suffit, ce qui 
évite un grand nombre de subtilités. Pas jugé d'un grand intérêt en tant que
tel, nous ne développons absolument pas le "calcul des o"; il s'agit juste
d'avoir une notation pratique pour noter des résultats, dans le cadre bien
précis du calcul différentiel et des propriétés des restes dans les 
développements limités. 
Toutes les démonstrations commencent par la traduction des $o$ en fonctions;
on est donc presque dans la situation ou l'on pourrait se passer de la 
notation; on aurait en contrepartie des résultats un peu plus lourd à énoncer,
les conséquences seraient limitées à ça.

**TODO:** remarque sur rôle du $o(1)$ et comment on pourrait tout ramener à
ça ... retenir au moins que $o(\|h\|) = o(1) \|h\|$ ? La notation $o(1)$
est pratique pour désigner $\varepsilon$ directement, sans avoir à rappeler
les hypothèses en détail.
-->

### Petit o de Landau
La notation $o(\|h\|^k)$, 
où $h \in \mathbb{R}^n$ et $k \in \mathbb{N}$,
désigne une expression de la forme
$$
o(\|h\|^k) := \varepsilon(h) \|h\|^k
$$
où $\varepsilon$ est une fonction définie dans un voisinage de $0$ 
et telle que 
$$
\lim_{h \to 0} \varepsilon(h) = \varepsilon(0) = 0.
$$
En particulier, dans le cas $k=0$, la notation $o(1)$
désigne un terme de la forme $\varepsilon(h)$
où $\varepsilon$ est une fonction du type défini ci-dessus.
Le cas général peut toujours être réduit à ce cas particulier
puisque l'on a $o(\|h\|^k) = o(1)\|h\|^k$.

En dehors de tout contexte, cette notation est très ambiguë puisque l'on ne
précise même pas à quel ensemble appartiennent les valeurs de $\varepsilon$.
Les choses se précisent lorsqu'elle est utilisée dans une équation donnée,
comme
$$
\phi(h) = o(\|h\|^k)
$$
où la fonction $\phi$ est connue.
Cette relation signifie alors: la fonction $\phi$ est définie dans un
voisinage de $0$ et vérifie:
$$
\lim_{h \to 0} \frac{\phi(h)}{\|h\|^k} = 0.
$$
La fonction $\varepsilon$ est alors définie de façon unique 
sur ce voisinage de $0$ par la relation
$$
\varepsilon(h) 
= 
\frac{\phi(h)}{\|h\|^k} \, \mbox{ si } \, h \neq 0
\, \mbox{ et } \,
\varepsilon(0) = 0.
$$

### Continuité {.example}

Si $f$ est une fonction définie d'un sous-ensemble de $\mathbb{R}^n$
et que $x \in \mathbb{R}^n$, la notation
$$
f(x+h) = f(x) + o(1)
$$
signifie donc que $f$ définie dans un voisinage de $x$ et que
$$
\lim_{h \to 0} f(x + h) = f(x),
$$
autrement dit que $x$ appartient à l'intérieur du domaine de définition de
$f$ et que $f$ est continue en ce point.


Différentielle
================================================================================

### Dérivée

Soient $U$ un ouvert de $\mathbb{R}$ et $f: U \to \mathbb{R}^m$.
La fonction $f$ est *dérivable* en $x \in U$ s'il existe une
limite $\ell \in \mathbb{R}^n$ au *taux d'accroissement* de
$f$ en $x$:
$$
\ell = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
$$
Cette limite quand elle existe est unique ; 
elle est appelée *dérivée de $f$ en $x$* et notée $f'(x)$:
$$
f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}.
$$

### Valeurs scalaires ou vectorielles {.remark}

La formation d'un taux d'accroissement dans cette définition 
nécessite que l'on divise par $h$
et par conséquent que $h$ soit scalaire ; 
la dérivée ne peut donc être définie que si $f$ est une fonction 
d'une unique variable (scalaire).
En revanche, la fonction peut être à valeurs scalaires ou vectorielles sans
qu'il soit nécessaire de changer cette définition. 
Précisement, une fonction vectorielle $f=(f_1, \cdots, f_m)$ sera dite 
dérivable en $x$ si et seulement si toutes ses composantes 
-- qui sont des fonctions scalaires -- sont dérivables; 
on a alors
  $$
  (f'(x))_i = f_i'(x).
  $$
Autrement dit, on peut dériver composante par composante. 
Cette approche se généralise de façon directe au cas des fonctions
à valeurs matricielles.

### Développement limité au premier ordre {.theorem}
Soient $U$ un ouvert de $\mathbb{R}$ et $f: U \to \mathbb{R}^m$.
La fonction $f$ est *dérivable* en $x \in U$ si et seulement si il 
existe un vecteur $\ell \in \mathbb{R}^m$ tel que
$$
f(x+h) = f(x) + \ell h + o(|h|).
$$
Le vecteur $\ell$ est alors égal à $f'(x)$.

### Démonstration {.proof}
Supposons que le taux d'accroissement de $f$ 
ait une limite $\ell$ en $x$ et considérons la fonction $\varepsilon$,
à valeurs dans $\mathbb{R}^m$, définie quand $x+h \in U$ par 
$\varepsilon(0) = 0$ et si $h \neq 0$ par
$$
\varepsilon(h) = \frac{f(x+h) - f(x)}{|h|} - \ell \frac{h}{|h|}.
$$
Puisque $U$ est ouvert, la fonction $\varepsilon$ est définie dans un voisinage 
de $h=0$ ;  
par construction, pour tout $h$ on a $f(x+h) = f(x) + \ell h + \varepsilon(h) |h|$.
Finalement, $f$ étant dérivable en $x$ de dérivée $\ell$, comme
pour $h \neq 0$,
$$
\varepsilon(h) = \left(\frac{f(x+h) - f(x)}{h} - \ell h \right) \frac{h}{|h|}
$$
on a bien $\lim_{h \to 0} \varepsilon(h) = 0$.
Par conséquent, avec la notation de Landau,
$$
f(x+h) = f(x) + \ell h + o(|h|).
$$
Réciproquement, si l'égalité $f(x+h) = f(x) + \ell h + \varepsilon(h) |h|$
est satisfaite avec un $\varepsilon(h)$ qui soit un $o(1)$, comme
$$
\frac{f(x+h) - f(x)}{h} = \ell + \varepsilon(h) \frac{h}{|h|}
$$
le taux d'accroissement de $f$ en $x$ tend bien vers
$\ell$ quand $h$ tend vers $0$.

### Fonctions linéaires d'une variable scalaire {.note}
Le terme $\ell h$ dans le développement limité au premier ordre de $f$ en
$x$ est une fonction linéaire de $h$.
Cette remarque n'est pas anodine car toutes les applications 
linéaires
de $\mathbb{R}$ dans $\mathbb{R}^m$ sont de cette forme.
En effet, pour une telle fonction $L$ et pour tout $h \in \mathbb{R}$, 
$$L\cdot h = L \cdot (h \times 1) = h (L \cdot 1) = (L \cdot 1) h,$$
le vecteur $\ell = L \cdot 1$ convient donc. 
On  peut donc caractériser la dérivabilité de $f$ en $x$
par l'existence d'une fonction linéaire de $\mathbb{R}^m$ dans $\mathbb{R}$
telle que
$$
f(x) = f(x+h) + L \cdot h + o(|h|).
$$
Cette caractérisation de la dérivée est directement généralisable au cas
de fonctions à $n$ variables.

### Différentielle de Fréchet {.definition .theorem}

Soient $U$ un ouvert de $\mathbb{R}^n$ et $f: U \to \mathbb{R}^m$.
La fonction $f$ est *[différentiable]{.index}* en $x \in U$ 
s'il existe une application linéaire $L: \mathbb{R}^n \to \mathbb{R}^m$
telle que
$f(x+h) = f(x) + L \cdot h + o(\|h\|).$
Si c'est le cas, l'application $L$ est unique ; 
nous la notons alors $df(x)$ et l'appelons *[différentielle de $f$ en $x$]{.index}*.
Elle est donc caractérisée par :
$$
f(x+h) = f(x) + df(x) \cdot h + o(\|h\|).
$$
La fonction $f$ est *différentiable*
(ou *différentiable sur $U$*)
si elle est différentiable en tout point de $U$. 

### Variation d'une fonction {.definition} 
On appelle *variation de $f$ en $x$*, 
pour la variation $h$ de l'argument, 
la grandeur
$$
\Delta f(x, h) := f(x+h) - f(x),
$$

### Variation et différentielle {.remark .ante}
La différentielle de $f$ en $x$, quand elle existe, 
constitue la "meilleure" approximation linéaire de la
variation de $f$ en $x$, car c'est la seule telle que
$$
\Delta f(x, h) = df(x) \cdot h + o(\|h\|).
$$
En particulier, quand la fonction $f$ est affine, 
la fonction linéaire associée est sa différentielle.

### Différentielle d'une fonction affine
Toute fonction $f: \R^n \to \R^m$ de la forme 
$f(x) = A \cdot x + b$
où $A: \R^n \to \R^m$ est linéaire et $b \in \R^m$,
est différentiable en tout point $x$ de $\R^n$ et
$df(x) = A.$

### Démonstration {.proof}
Il suffit de constater que 
$$\Delta f(x, h) = f(x+h) - f(x) = A \cdot (x+h) + b - A \cdot x -b = A \cdot h$$
et que par conséquent
$\Delta f(x, h) = A \cdot h + o(\|h\|)$.

### {.ante}
Résumons les liens entre dérivée et différentielle à ce stade :

### Différentielle et dérivée {.theorem}
Soient $U$ un ouvert de $\mathbb{R}$, $f: U \to \mathbb{R}^m$
et $x \in U$.
La fonction $f$ est différentiable en $x$ si et seulement si
elle est dérivable en $x$. Dérivée et différentielle de $f$ en 
$x$ se déduisent alors l'une de l'autre par les relations 
$$
f'(x) = df(x) \cdot 1
\; \mbox{ et } \;
df(x) = (h \in \mathbb{R} \mapsto f'(x) h).
$$

### Démonstration {.proof}
Une conséquence de la caractérisation de la dérivabilité des fonctions
par l'existence de [développement limité au premier ordre][Développement limité au premier ordre]
et de la caractérisation des [fonctions linéaires d'une variable scalaire][Fonctions linéaires d'une variable scalaire].

### Gradient {.definition}
Soient $U$ un ouvert de $\mathbb{R}^n$ et $f: U \to \mathbb{R}$ 
différentiable en $x \in U$. Le *gradient de $f$ en $x$* noté $\nabla f(x)$
est l'unique vecteur de $\R^n$ tel que pour tout $h \in \R^n$,
$$
df(x) \cdot h = \left<\nabla f(x), h \right>.
$$

### Démonstration (existence et unicité) {.proof}
La différentielle de $f$ en $x$ est une forme linéaire sur $\mathbb{R}^n$,
c'est-à-dire une application linéaire de $\mathbb{R}^n$ dans $\mathbb{R}$.
Or pour toute application $A$ de ce type, si un vecteur $a \in \R^n$
est tel que $A \cdot h = \left<a, h\right>$ pour tout $h \in \R^n$, 
alors sélectionner successivement $h = e_i$ pour $i=1, \dots, n$
fournit nécessairement $a = (A(e_1), \dots, A(e_n))$ ; 
il existe donc au plus un vecteur $a$ satisfaisant ces égalités. 
Réciproquement, pour ce vecteur
$a$, on a bien
$$
A \cdot h = A \cdot (h_1 e_1 + \dots + h_n e_n) = \sum_i h_i A(e_i) = \sum_i a_i h_i
= \left<a, h\right>.
$$
Dans notre contexte où $A = df(x)$, le gradient est donc défini de façon unique
par $\nabla f(x) = (df(x)\cdot e_1, \dots, df(x)\cdot e_n)$.

### Point critique
Soient $U$ un ouvert de $\mathbb{R}^n$ et $f: U \to \mathbb{R}$,
une fonction différentiable. Le point $x$ est un *point critique
de $f$* si $df(x) = 0$.

### Point critique et extrema
Soient $U$ un ouvert de $\mathbb{R}^n$ et $f: U \to \mathbb{R}$
une fonction différentiable. Si $f$ admet un minimum ou un maximum
local en $x \in U$, alors $x$ est un point critique de $f$.

### Démonstration {.proof}
Supposons que $f$ admette un minimum local en $x$ (le cas du maximum peut
s'en déduire en considérant la fonction $-f$). Soit $r > 0$ tel que 
pour tout $y \in \R^n$ satisfaisant $\|y - x\| \leq r$ on ait $y \in U$ 
et $f(x) \leq f(y)$. Soit $h \in \mathbb{R}^n$ et $t$ un réel non nul
suffisamment petit pour que $\left\|th \right\| \leq r$. Comme $f$
est différentiable en $x$, il existe une fonction $\varepsilon$ qui soit
un petit o de $1$ telle que
$$
f(x+th) - f(x) = df(x) \cdot (th) + \varepsilon(th) \|th\|.
$$
Soit par linéarité de la différentielle,
$$
df(x) \cdot h = \frac{f(x+th) - f(x)}{t} - \varepsilon(th) \frac{|t|}{t} \|h\|. 
$$
En faisant tendre $t$ vers $0$ dans le membre de droite de cette équation
(la limite existe puisque le membre de droite est indépendant de $t$),
on obtient un nombre positif ou nul. 
Le même raisonnement pouvant être appliqué pour calculer 
$df(x) \cdot (-h) = -df(x) \cdot h$, on en déduit
que $df(x) \cdot h = 0$.

### Différentiation composante par composante {#dcpc}
Soient $U$ un ouvert de $\mathbb{R}^n$ et $f: U \to \mathbb{R}^m$.
La fonction $f=(f_1, \cdots, f_m)$ est différentiable en $x \in U$ 
si et seulement si chacune de ses composantes $f_i$ est différentiable
en $x$. On a alors pour tout $h \in \mathbb{R}^n$
$$
(df(x) \cdot h)_i = d f_i(x) \cdot h.
$$

### Démonstration {.proof}
Supposons $f$ différentiable en $x$ ; soit $\varepsilon$ un $o(1)$ tel que
$$
f(x + h) = f(x) + df(x)\cdot h + \varepsilon(h) \|h\|.
$$
En prenant la $i$-ème composante de cette equation, on obtient
$$
f_i(x + h) = f_i(x) + (df(x)\cdot h)_i + \varepsilon_i(h) \|h\|.
$$
On constate alors que l'application $h \mapsto (df(x) \cdot h)_i$ est linéaire
(l'application "prendre la $i$-ème composante d'un vecteur de $\mathbb{R}^m$" 
étant linéaire)
et que $\varepsilon_i$ est un $o(1)$. 
La $i$-ème composante $i$ de $f$ est donc différentiable et 
$df_i(x) \cdot h = (df(x) \cdot h)_i$.

Réciproquement, si toutes les composantes de $f$ sont 
différentables en $x$, c'est-à-dire si il existe pour chaque $i$ une
fonction $\varepsilon_i$ qui soit un $o(1)$ et telle que
$$
f_i(x + h) = f_i(x) + df_i(x)\cdot h + \varepsilon_i(h) \|h\|,
$$
on a
$$
f(x + h) = f(x) + (df_1(x)\cdot h, \dots, df_m(x)\cdot h) + 
\varepsilon(h) \|h\|,
$$ 
et $\varepsilon := (\varepsilon_1, \dots, \varepsilon_m)$ est bien un $o(1)$.
Comme la fonction $h \mapsto (df_1(x)\cdot h, \dots, df_m(x)\cdot h)$ est 
linéaire en $h$, on en déduit que $f$ est différentiable en $x$.

### Valeurs et variables matricielles {.remark}
On peut de façon très simple définir la différentielle d'une fonction $F$
d'une ou de plusieurs variables scalaires et dont la valeur est matricielle, 
c'est-à-dire telle que
$$
F : U \subset \mathbb{R}^n \to \R^{m \times p}.
$$
Il suffit en effet d'exiger que chaque composante $F_{ij}$ soit différentiable,
puis de définir $dF(x)$ composante par composante, de façon similaire au cas
vectoriel:
$$
(dF(x) \cdot h)_{ij} = d F_{ij}(x) \cdot h.
$$
Mais le traitement des fonctions dont les arguments sont matriciels --
par exemple l'application trace $\mathrm{tr}: \R^{n\times n} \to \mathbb{R}$ --
demande une autre approche. Dans le cas d'une unique variable matricielle[^ext],
donc d'une fonction de la forme
$$
f : U \subset \mathbb{R}^{n \times m} \to \R^p,
$$
on utilisera la fonction auxiliaire $f^*$ dont l'argument est un vecteur
de $\R^{m\times n}$, argument qu'on "remettra sous forme matricielle"
(cf. section "[Mise à plat des matrices]") avant de le fournir comme argument à $f$.
C'est-à-dire que la fonction auxiliaire $f^*$ est définie à partir de 
$\pi := \pi_{m \times n}$ comme
$$
f^* = f \circ \pi^{-1}
$$
On dira alors que $f$ est différentiable en $X$ si et seulement si $f^*$
est différentiable en $x=\pi(X)$ et si c'est le cas, on définira la
fonction $df(X): \mathbb{R}^{m\times n} \to \mathbb{R}^p$ par
$$
df(X) = df^*(x) \circ \pi.
$$
Ces deux façons d'étendre la notion de la différentielle -- 
aux fonction à valeurs matricielles et à arguments matriciels -- 
peuvent être combinées.

Prenons un exemple du second cas; la fonction
$$
\mathrm{tr}: 
A = \left[ 
\begin{array}{cc}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{array}
\right] \in \R^{2 \times 2}
\mapsto 
a_{11} + a_{22} \in \mathbb{R}.
$$
a pour fonction auxiliaire 
$$
\mathrm{tr}^*: 
a=(a_{11}, a_{12}, a_{21}, a_{22}) \in \R^{4}
\mapsto 
a_{11} + a_{22} \in \mathbb{R}.
$$
Pour tout $h=(h_1, h_2, h_3, h_4) \in \mathbb{R}^4$, on a 
$$
\mathrm{tr}^*(a + h) = 
\mathrm{tr}^*(a) + h_{11} + h_{22}.
$$
L'application $h \mapsto h_{11} + h_{22}$ étant linéaire, $\mathrm{tr}^*$
est différentiable en $a$, de différentielle
$d\mathrm{tr}^*(a) \cdot h = h_{11} + h_{22}$.
L'application $\mathrm{tr}$ est donc différentiable en $A$ et
$$
d\mathrm{tr}(A) \cdot H  = h_{11} + h_{22}
\; \mbox{ avec } \;
H = \left[ 
\begin{array}{cc}
h_{11} & h_{12} \\
h_{21} & h_{22}
\end{array}
\right],
$$
c'est-à-dire $d\mathrm{tr}(A)  = \mathrm{tr}$.


[^ext]: Si la fonction $f$ a plusieurs arguments matriciels
$$
A_1 \in \R^{m_1 \times n_1}, \, \dots, A_k \in \R^{m_k \times n_k},
$$
on pourra définir une fonction auxiliaire $f^*$ qui reconstruit ces matrices 
à partir des éléments d'un unique vecteur de $\R^n$ où $n = m_1 n_1 + \dots + m_k n_k$,
en procédant par exemple de gauche à droite, de haut en bas, 
et de la première à la dernière matrice.

### Domaine de définition non ouvert {.remark}

La définition de la différentielle de $f$ suppose que le domaine de définition
de $f$ soit un ensemble ouvert. Cette restriction permet de garantir qu'en
tout point $x$ considéré du domaine de définition, on puisse examiner la
variation de $f$ en $x$ dans "toutes les directions" pour voir s'il existe
une approximation linéaire.

Il y a néanmoins des façons de s'adapter quand le domaine de définition de 
$f$ n'est pas ouvert :

  - Si $x$ est un point de l'intérieur de ce domaine, 
    on peut alors considérer la 
    restriction de $f$ à un voisinage ouvert de $x$ et étudier la 
    différentiabilité de cette restriction. Le résultat (existence
    de la différentielle et valeur le cas échéant) est indépendant
    du voisinage ouvert choisi.

  - Si $x$ est un point de la frontière de ce domaine,
    on peut à l'inverse chercher s'il existe une extension de $f$
    à un voisinage ouvert de $x$ qui soit différentiable en $x$.
    En général cette approche ne garantit pas une définition unique
    de la différentielle de $f$ en $x$, mais est suffisante dans
    des cas importants. Par exemple, elle permet d'étudier la
    [différentiabilité (ou dérivabilité) de fonctions d'une variable 
    scalaire sur des intervalles fermés de $\mathbb{R}$](#intervalle-fermé).

### Différencier une expression
L'expression $df(x) \cdot h$ dépend de trois éléments : la fonction $f$,
le point de référence $x$ et la variation de l'argument $h$. Cette notation
est sans ambiguité mais peut parfois être lourde à manipuler.
Dans le calcul des dérivées, nous avons l'habitude, pour signifier que
la dérivée de la fonction $x \mapsto x^2$ en tout point $x$ de $\mathbb{R}$
est $2x$, d'écrire simplement
  $$
  (x^2)' = 2x.
  $$
Le membre de gauche désigne la dérivée de la fonction $x \mapsto x^2$, 
évaluée en $x$.
Avec notre notation pour la différentielle, à ce stade 
il nous faudrait écrire:
$$
d (x \in \mathbb{R} \to x^2)(x) \cdot h = 2 x h.
$$
Si l'on accepte de regrouper la fonction à différencier et le point où
elle est calculée en un terme unique dans cette notation, qui est une
expression de $x$, on peut alors écrire:
$$
d x^2 \cdot h = 2 x h,
$$
ce qui est un progrès, même si la notation n'est pas totalement dénuée 
d'ambiguité[^amb].
On remarque alors qu'en exploitant cette convention, le terme $dx$
vient à désigner $d(x \mapsto x)(x)$; comme $(x)' = 1$,
on a donc $dx \cdot h = 1 \times h = h$. 
Par conséquent, on peut réécrire l'équation ci-dessus sous la forme
mémorable
$$
dx^2 = 2 x dx.
$$

[^amb]: par exemple: est-ce que $df(x^2)$ désigne désormais la différentielle
de la fonction $f$ évaluée en $x^2$ ou la différentielle de la fonction 
$x \mapsto f(x^2)$ évaluée en $x$ ? Les deux grandeurs ne sont pas égales ...
Il faut donc savoir si l'on différencie une fonction en un point ou bien
une expression par rapport à une variable. On pourra rajouter des parenthèses
pour lever l'ambiguité si nécessaire, avec $d(f)(x^2)$ dans le premier cas
et $d(f(x^2))$ dans le second. Par défaut, nous supposerons dans la suite
que $df(x^2)$ désigne la notation "stricte" $d(f)(x^2)$.


<!--
### Note {.meta}
Même si la notation de la différentielle en $x$ donne un indice sur l'étape
suivante, il faut probablement retarder l'apparition de la notion d'application
différentielle et construire une familiarité avec la notion de différentielle 
en $a$ avant de passer à l'étape d'après.
La notion d'application différentielle ne devient nécessaire que pour parler
de fonction continûment différentiable et de différentielle d'ordre supérieur.
-->

# {.ante .remark}

Sous les hypothèses ad hoc, la différentielle de $f$ et $g$ en $x$ 
est la composée des différentielles de $f$ en $x$ et de $g$ en $y=f(x)$.

### Règle de différentiation en chaîne {#chain-rule}

Soit $f: U \subset \mathbb{R}^p \to \mathbb{R}^{n}$ et 
$g: V \subset \mathbb{R}^n \to \mathbb{R}^{m}$ deux fonctions définies
sur des ouverts $U$ et $V$ et telles que $f(U) \subset V$. 
Si $f$ est différentiable en $x \in U$ et $g$ est différentiable en $f(x) \in V$,
alors la composée $g \circ f$ est différentiable en $x$ et
$$
d(g \circ f)(x) = dg(y) \cdot df(x) \; \mbox{ où } \; y = f(x).
$$

### Notations {.note}

La formule précédente peut s'écrire de façon plus compacte sans
la variable intermédiaire $y$ :
$$
d(g \circ f)(x) = dg(f(x)) \cdot df(x).
$$
Le terme $dg(f(x))$ y désigne la différentielle de $g$ en $f(x)$
et non la différentielle de l'expression $g(f(x))$ (qui est le terme
que l'on souhaite calculer).

Comment souvent, annoter les composants d'une formule avec les ensembles 
auquels ils appartiennent permet de s'assurer qu'elle n'est pas 
de toute évidence incorrecte. Ici par exemple :
$$
\stackrel{\mathbb{R}^m \leftarrow \mathbb{R}^p}{d(g\circ f)(x)} 
\, = \,  
\stackrel{\mathbb{R}^m \leftarrow \mathbb{R}^n}{dg(y)} 
\cdot
\stackrel{\mathbb{R}^n \leftarrow \mathbb{R}^p}{df(x)} \; \mbox{ où } \; y = f(x).
$$

### Démonstration {.proof}
L'objectif de la preuve est de montrer que
$$
g(f(x+h)) - g(f(x)) =  (dg(f(x)) \cdot df(x)) \cdot h + o(\|h\|).
$$
La fonction $g$ étant différentiable en $f(x)$, il existe une fonction
$\varepsilon_1$ qui soit un $o(1)$ et telle que
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

Notons que la fonction $\varepsilon_2(h) := \varepsilon_1(f(x+h) - f(x))$
est définie dans un voisinage de l'origine et que par continuité de $f$ en 
$x$, $f(x+h) - f(x)$ tend vers $0$ quand $h$ tend vers $0$, et par conséquent
$\varepsilon_2(h) \to \varepsilon_2(0) = 0$ quand $h\to 0$ ; 
la fonction $\varepsilon_2$ est donc un $o(1)$.
Avec cette notation, on a
$$
\begin{split}
g(f(x+h)) - g(f(x)) &= dg(f(x)) \cdot (f(x+h)-f(x)) \\
                    &\phantom{=} + \varepsilon_2(h) \|f(x+h)-f(x)\|.
\end{split}
$$
Comme $f$ est également différentiable en $x$, il existe une fonction 
$\varepsilon_3$ qui soit un $o(1)$ et telle que
$$
f(x+h) - f(x) = df(x) \cdot h + \varepsilon_3(h) \|h\|.
$$
En substituant cette relation dans la précédente, nous obtenons
$$
g(f(x+h)) - g(f(x)) = dg(f(x)) \cdot (df(x) \cdot h) + \varepsilon(h) \|h\|
$$
où $\varepsilon(0) = 0$ et dans le cas contraire,
$$
\varepsilon(h) =  dg(f(x)) \cdot \varepsilon_3(h) + \varepsilon_2(h) 
\left\|df(x) \cdot \frac{h}{\|h\|} + \varepsilon_3(h) \right\|.
$$
Il suffit pour conclure de prouver que $\varepsilon(h) \to 0$ quand $h \to 0$.
Or, 
$$
\begin{split}
\|\varepsilon(h)\| & \leq \|dg(f(x)) \cdot \varepsilon_3(h)\| + \|\varepsilon_2(h)\| \times \|df(x) \cdot (h / \|h\|) \| + \|\varepsilon_2(h)\| \times \|\varepsilon_3(h) \|   \\
& \leq \|dg(f(x))\| \times \|\varepsilon_3(h)\| + \|\varepsilon_2(h)\|  \times \|df(x)\| + \|\varepsilon_2(h)\| \times \|\varepsilon_3(h) \|,  
\end{split}
$$
le résultat est donc acquis.


### Règle de la somme {.theorem #sum-rule}
La somme
$(x, y) \in \mathbb{R}^2 \mapsto x + y \in \mathbb{R}$ 
est différentiable en tout point et
$$
d(x+y) = dx + dy.
$$

### Démonstration {.proof}
Pour tout $(x, y) \in \mathbb{R}^2$ et tout $(h_1, h_2) \in \mathbb{R}^2$, on a
$$
(x + h_1) + (y + h_2) = (x + y) + (h_1 + h_2).
$$
L'application somme est donc différentiable et sa différentielle
est l'application $(h_1, h_2) \to h_1 + h_2$, c'est-à-dire 
$dx + dy$.

### Règle du produit {.theorem #product-rule}
L'application produit 
$(x, y) \in \mathbb{R}^2 \mapsto xy  \in \mathbb{R}$
est différentiable en tout point et
$$
d xy = x dy + y dx
$$

### Démonstration {.proof}
Soit $(x, y) \in \mathbb{R}^2$. Pour tout $h = (h_1, h_2) \in \mathbb{R}^2$,
on a 
$$
(x+h_1) (y+h_2) = x y + x h_2 + y h_1 + h_1 h_2.
$$
Comme $|h_1 h_2| \leq \|h\|^2$, le produit $h_1 h_2$ est un $o(h)$.
Par conséquent, l'application produit
est différentiable en tout point $(x, y)$ de $\mathbb{R}^2$ 
et sa différentielle est l'application
$(h_1, h_2) \to x h_2 + y h_1,$
c'est-à-dire $x dy + y dx$.

### Linéarité de la différentielle {.corollary}
Soit $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}^m$ et 
$g: U \to \mathbb{R}^m$, différentiables en $x \in U$. 
Pour tous réels $\lambda$ et $\mu$, l'application 
$\lambda f + \mu g$ est différentiable en $x$ et
$$
d(\lambda f + \mu g)(x) = \lambda df(x) + \mu dg(x).
$$

### Démonstration {.proof}
Compte tenu du résultat concernant [la différentiation composante par composante](#dcpc),
il suffit d'établir le résultat pour $f$ et $g$ à valeurs réelles.
Or, l'application $x \in \mathbb{R}^n \mapsto (\lambda, f(x))$ est différentiable
en $x$ car ses composantes sont différentiables ; 
sa différentielle -- calculée composante par composante -- 
est l'application $h \mapsto (0, df(x) \cdot h)$.
L'application $\lambda f$ étant le produit de $\lambda$ et $f$,
par [la règle de différentiation en chaîne](#chain-rule), 
elle est différentiable en $x$ et 
$$
d (\lambda f)(x) = \lambda df(x) + f(x) \times (h \to 0) = \lambda df(x).
$$
De même, $\mu g$ est différentiable en $x$ et $d(\mu g)(x) = \mu dg(x)$.
Par la règle de la somme, la combinaison linéaire $\lambda f + \mu g$ est
donc différentiable en $x$ et 
$d(\lambda f + \mu g)(x) = \lambda df(x) + \mu dg(x)$.

Jacobienne, dérivées partielles et directionnelles 
================================================================================

<!--
### Objectifs {.meta}

TODO: à l'oral, insister sur différentielle comme point de départ et
le reste (dérivées partielles, directionnelle, etc) s'ensuivent.
Montrer que la démarche inverse ne marche pas (bien que la jacobienne
puisse être formellement définie, la chain rule ne marche pas, donc
on ne peut pas les multiplier)
-->

### Matrice jacobienne {.definition}
Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}^m$ et
$x$ un point de $U$. Quand $f$ est différentiable en $x$, 
on appelle *matrice jacobienne* de $f$ en $x$ et l'on note 
$J_f(x)$ la matrice $\mathbb{R}^{m \times n}$ associée à la 
différentielle $df(x): \mathbb{R}^n \to \mathbb{R}^m$ de $f$ en $x$.

### Dérivées partielles {.definition}
Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}^m$ et $x \in U$. 
Lorsque la $i$-ème fonction partielle de $f$ en $x$
$$
y_i \mapsto f(x_1, \cdots, x_{i-1}, y_i, x_{i+1}, \cdots, x_n)
$$
est dérivable en $y_i = x_i$, on appelle $i$-ème *dérivée partielle*
de $f$ en $x$ et on note $\partial_i f(x) \in \mathbb{R}^m$ sa dérivée.
Alternativement,
$$
\begin{split}
\partial_i f(x)
&= \lim_{t \to 0} \frac{f(x + t e_i) - f(x)}{t} \\
&= \lim_{t \to 0} \frac{f(x_1, \dots, x_i + t, \dots, x_n) - f(x_1, \dots, x_n)}{t} 
\end{split}
$$
quand le second membre existe.

### Différentielles partielles {.remark .definition}
La dérivée partielle permet d'étudier séparement l'influence de chaque 
variable scalaire de $f$ sur sa variation. 
Mais dans certaine situations il est plus naturel de regrouper 
les variables dont dépend $f$ en plusieurs variables vectorielles. 
Ainsi, pour étudier l'application produit scalaire dans $\mathbb{R}^n$
$$
\left<\cdot, \cdot \right>: 
(x_1,\dots, x_n, y_1, \dots, y_n) \in \R^{2n}
\mapsto \sum_{k=1}^n x_k y_k \in \R,
$$
il est raisonnable de partitionner la variable en 
$x = (x_1, \dots, x_n) \in \mathbb{R}^n$ d'une part et
$y = (y_1, \dots, y_n) \in \mathbb{R}^n$ d'autre part.
Pour gérer ce type de situation, la *différentielle partielle* par rapport au 
$i$-ème argument d'une fonction
$$
f: U \subset \R^{n_1} \times \dots \times \R^{n_k} \to \R^m
$$
est définie comme la différentielle de la $i$-ème fonction partielle de $f$ en 
$x = (x_1, \dots, x_k)$
$$
y_i \in \R^{n_i} \mapsto f(x_1, \cdots, x_{i-1}, y_i, x_{i+1}, \cdots, x_k)
$$
quand celle-ci existe. Elle est notée $\partial_i f(x)$, comme la dérivée
partielle, ce qui n'est pas trop ambigu tant que l'on explicite
comment l'argument de $f$ est décomposé.

### Arguments nommés
Les conventions attribuant un nom aux arguments d'une fonction
permettent parfois de rendre les dérivées et différentielles partielles
plus intelligibles. Si le $i$-ème argument 
d'une fonction $f$ est désigné par un symbole $x$, 
on pourra noter 
$\partial_{x} f$ (ou ${\partial f}/{\partial x}$)
sa dérivée partielle 
(ou différentielle partielle selon le cas)
au lieu de $\partial_i f$.

Si l'on considère par exemple la fonction $m$ définie par
$$
m: (x, y, z, t) \in \R^4 \to x^2 + y^2 + z^2 - c^2 t^2,
$$
comme dans la théorie de la relativité,
les dérivées partielles par rapport aux variables d'espace $x$, $y$, $z$ 
sont données par 
$\partial_x m(x, y, z, t) = 2 x$,
$\partial_y m(x, y, z, t) = 2 y$,
$\partial_z m(x, y, z, t) = 2 z$
et par rapport à la variable de temps $t$ par
$\partial_{t} m(x, y, z, t) = -2c^2t.$
Si l'on préfère regrouper les trois premiers arguments en un 
vecteur d'espace $\mathbf{x} = (x, y, z)$, on a alors
$$
m: (\mathbf{x}, t) \in \R^3 \times \R \to \|\mathbf{x}\|^2 - c^2 t^2,
$$
et la différentielle partielle
$$
\partial_{\mathbf{x}}m(\mathbf{x}, t) = 2 (xdx + y dy + z dz).
$$

### Différentielle et dérivées partielles {.proposition}
Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}^m$ et
$x$ un point de $U$. 
Lorsque $f$ est différentiable en $x$, 
toutes ses dérivées partielles existent et vérifient
$$
\partial_i f(x) = df(x) \cdot e_i,
$$
ou de façon équivalente, pour tout $h \in \mathbb{R}^n$
$$
df(x) \cdot h = \sum_{i=1}^n \partial_i f(x) h_i.
$$

### Différentielle et différentielles partielles {.post}
Sous les même hypothèses, si l'on considère désormais $f$ comme une
fonction
$f: U \subset \R^{n_1} \times \dots \times \R^{n_k} \to \R^m$
(avec $n_1 + \dots + n_k = n$),
toutes les différentielles partielles de $f$ en $x$ existent et
pour tout $h=(h_1, \dots, h_k) \in \R^{n_1} \times \dots \times \R^{n_k}$,
$$
df(x) \cdot h = \sum_{i=1}^n \partial_i f(x) \cdot h_i.
$$

### Démonstration {.proof}
La différentiabilité de $f$ en $x$ établit l'existence d'une
fonction $\varepsilon$ qui soit un $o(1)$ et telle que 
$$
f(x+h) = f(x) + df(x) \cdot h + \varepsilon(h) \|h\|.
$$
Soit $t$ un réel non nul ; substituer $h := t e_i$ dans cette relation fournit
$$
f(x+te_i) = f(x) + df(x) \cdot (t e_i) + \varepsilon(t e_i) \|t e_i\|.
$$
En exploitant la linéarité de la différentielle, on obtient donc
$$
df(x) \cdot e_i = \frac{f(x+te_i) - f(x)}{t} + \varepsilon(t e_i) \frac{|t|}{t}.
$$
Par conséquent, en passant à la limite quand $t \to 0$, on obtient
$$
df(x) \cdot e_i = \lim_{t \to 0} \frac{f(x+t e_i) - f_i(x)}{t} =: \partial_i f(x)
$$
Pour obtenir la seconde forme de cette relation, il suffit de décomposer un
vecteur $h=(h_1, \dots, h_n)$ sous la forme
$$
h = h_1 e_1 + \dots + h_n e_n
$$
et d'exploiter la linéarité de la différentielle ; on obtient
$$
df(x) \cdot h 
= df(x) \cdot \left( h_1 e_1 + \dots + h_n e_n\right)
= \sum_i (df(x) \cdot e_i) h_i 
= \sum_i \partial_i f(x) h_i,
$$
comme attendu.

### Matrice jacobienne et dérivées partielles {.corollary}
Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}^m$ et
$x$ un point de $U$. 
Si $f$ est différentiable en $x$, on a 
$$
[J_f(x)]_{ij} = \partial_{j} f_i(x),
$$
c'est-à-dire
$$
J_f(x) = \left[
\begin{array}{cccc}
\partial_1 f_1 (x) & \partial_2 f_1 (x) & \cdots & \partial_n f_1 (x) \\
\partial_1 f_2 (x) & \partial_2 f_2 (x) & \cdots & \partial_n f_2 (x) \\
\vdots & \vdots & \vdots & \vdots \\
\partial_1 f_m (x) & \partial_2 f_m (x) & \cdots & \partial_n f_m (x) \\
\end{array}
\right]
$$

### Démonstration {.proof}
Par définition, la matrice jacobienne de $f$ en $x$ se déduit de la 
différentielle par
$[J_f(x)]_{ij} = (df(x) \cdot e_j)_i.$
Comme $\partial_j f(x) = df(x) \cdot e_j,$ on a
$[J_f(x)]_{ij} = (\partial_j f(x))_i.$ 
Les fonctions vectorielles se dérivant composante par composante, 
on en déduit que $[J_f(x)]_{ij} = \partial_j f_i(x)$. 

### Gradient et dérivées partielles
Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}$ et $x$ un point de $U$. 
Si $f$ est différentiable en $x$, on a 
$$
\nabla f(x) = (\partial_1 f(x), \dots, \partial_n f(x)).
$$

### Démonstration {.proof}
Pour tout $h \in \R^n$, on a
$$
\left<\nabla f(x), h\right> 
= df(x) \cdot h
= \sum_i \partial_i f(x) \cdot h_i 
= 
\left<(\partial_1 f(x), \dots, \partial_n f(x)), h \right>, 
$$
ce qui établit le résultat.


### Matrice jacobienne, gradient et dérivées partielles {.remark #mjgdp}
On remarquera qu'avec les résultats ci-dessus, il est techniquement possible de 
définir le gradient $\nabla f(x)$ ou la matrice jacobienne $J_f(x)$ en supposant 
uniquement que les dérivées partielles de $f$ en $x$ existent, 
ce qui peut arriver alors que $f$ n'est pas différentiable en $x$. 
Mais cette extension est à prendre avec précaution. 
En effet, dans ce cadre étendu, 
on ne peut plus transposer aux gradients et matrices jacobiennes 
tous les résultats valides pour les différentielles. 
Par exemple, si $J_g(f(x))$ et $J_f(x)$ existent
(au sens où toutes les dérivées partielles concernées existent), on peut
former le produit matriciel $J_g(f(x)) J_f(x)$, mais sans aucune garantie que 
$J_{g \circ f}(x)$ existe et/ou soit égal à ce produit, 
car [la règle de différentiation en chaîne](#chain-rule) requiert l'existence 
des différentielles.

### Fonction continûment différentiable {.proposition}
Soit $U$ un ouvert de $\mathbb{R}^n$. 
Une fonction $f: U \to \mathbb{R}^m$ 
est *continûment différentiable* si elle est différentiable et si 
l'application différentielle
$$
df: x \in U \subset \R^n \mapsto df(x) \in (\R^n \stackrel{\ell}{\to} \R^m)
$$
est continue.

### {.ante}
Cette définition constitue un moyen de vérifier l'existence de
la différentielle (et sa continuité) en passant par les dérivées partielles :

### Dérivées partielles continues {.proposition}
Soit $U$ un ouvert de $\mathbb{R}^n$.
Une fonction $f: U \to \mathbb{R}^m$ 
est continûment différentiable si et seulement si toutes ses dérivées
partielles existent et sont continues.

### Démonstration {.proof}
Si $f$ est différentiable de différentielle continue, ses dérivées partielles
sont définies et $\partial_i f(x) = df(x) \cdot e_i$. Le second membre de 
cette relation est une fonction continue de $x$, donc les dérivées partielles
sont continues.

Réciproquement, soit $f: U \subset \R^n \to \R$ une fonction 
dont les dérivées partielles existent et sont continues
(la preuve dans le cas d'une fonction à valeurs vectorielles se déduit 
du résultat dans le cas scalaire).
Soit $a \in U$ et $r>0$ telle que la boule fermée centrée en $a$ et de rayon
$r$ soit dans $U$ ; soit $h \in \R^n$ tel que $\|h\| \leq r$. 
La variation de $f$ entre $a$ et $a+h$ satisfait
$$
f(a+h) - f(a) = \sum_{i=1}^n f(a+(h_1, \dots, h_i, 0, \dots)) - f(a + (h_1, \dots, h_{i-1}, 0, \dots)). 
$$
Or, par [le théorème fondamental du calcul](#TFC), 
comme pour tout $i$ la fonction
$$t \in [0,1] \mapsto f(a+(h_1, \dots, th_i, 0, \dots))$$
est dérivable de dérivée
$\partial_i f(a+(h_1, \dots, th_i, 0, \dots)) h_i$, on a
\begin{multline*}
f(a+(h_1, \dots, h_i, 0, \dots)) - f(a + (h_1, \dots, h_{i-1}, 0, \dots)) = \\
h_i \int_0^1 \partial_i f(a+(h_1, \dots, th_i, 0, \dots)) \, dt.
\end{multline*}
Par ailleurs, comme
$$
\partial_i f(a) h_i
=
h_i \int_0^1 \partial_i f(a) \, dt,
$$
on a 
\begin{multline*}
f(a+h) - f(a) - \sum_i \partial_i f(a) h_i = \\
\sum_{i=1}^n h_i \int_0^1 \left[\partial_i f(a+(h_1, \dots, th_i, 0, \dots)) - \partial_i f(a) \right] \, dt. 
\end{multline*}
Par continuité des dérivées partielles en $a$, si $r$ est choisi de telle sorte
que $|\partial_i f(b) - \partial_i f(a)| \leq \varepsilon / n$ 
quand $|b-a| \leq r$, alors l'inégalité triangulaire et 
[la majoration des intégrales](#ML-memma) ci-dessus
conduisent à
$$
\left|f(a+h) - f(a) - \sum_i \partial_i f(a) h_i \right|
\leq
\sum_{i=1}^n |h_i| {\varepsilon}/{n}
\leq \varepsilon \|h\|.
$$
La fonction $f$ est donc différentiable en $a$, de différentielle
$h \mapsto \sum_i \partial_i f(a) h_i$. La matrice (jacobienne) 
représentant $df(x)$ ayant pour coefficients les dérivées partielles
de $f$ en $x$, elle est une fonction continue de $x$, comme $df(x)$.

### Matrice jacobienne continue {.remark}
S'il l'on adopte la définition étendue de jacobien de la remarque
"[Matrice jacobienne, gradient et dérivées partielles]", la définition de 
continûment différentiable peut être reformulée comme
"la matrice jacobienne existe et est continue".


Variation des fonctions
================================================================================

### Différentielle et intégrale

Pour comparer $f(a+h)$ et $f(a)$, 
lorsque la fonction $f$ est continue en $a$, 
nous disposons de l'égalité $f(a + h) = f(a) + o(1)$,
mais cette relation est asymptotique. 
Pour maîtriser l'écart entre
$f(a+h)$ et $f(a)$ au moyen de cette formule, 
nous devons être en mesure de faire tendre $h$ vers $0$. 
Si la grandeur $h$ est fixée, cette relation est inexploitable. 

Toutefois, dans cette situation, 
si $f$ est différentiable sur tout le segment $[a,a+h]$, il est possible
de relier $f(a+h)$ à $f(a)$ en intégrant les variations infinitésimales 
de $f$ le long de $[a, a+h]$. 
La seule notion d'intégrale dont nous avons besoin,
minimaliste et construite exclusivement au service du calcul différentiel,
est l'intégrale de Newton, présentée [en annexe](#intégrale-Newton) ;
dans de ce chapitre, c'est toujours cette intégrale dont nous ferons
usage implicitement.

### Théorème fondamental du calcul {.theorem #TFC}
Si $f: [a, b] \to \R$ est dérivable, alors $f'$ est intégrable et
$$
f(b) - f(a)  = \int_a^b f'(x) \, dx.
$$

### Démonstration {.proof}
Cf. [l'annexe consacrée à l'intégrale de Newton](#intégrale-Newton).

### Variation d'une fonction {.theorem}
Soient $U$ un ouvert de $\mathbb{R}^n$ et $f: U \to \mathbb{R}^m$,
soient $a \in U$ et $h \in \mathbb{R}^n$ tels que le segment
  $$
  [a, a+h] = \{a + th \; | \; t \in [0,1]\}
  $$
soit inclus dans $U$. Si $f$ est différentiable en tout point de $[a, a+h]$,
$$
f(a + h) = f(a) + \int_0^1 df(a+th) \cdot h \, dt.
$$

### Démonstration
Considérons la fonction $\phi: [0,1] \to \mathbb{R}^n$ définie par
$$
\phi(t) = f(a + th)
$$
La fonction $\phi$ est dérivable sur $[0,1]$ comme composée des fonctions 
différentiables $f$ et $t \mapsto a + th$ ; sa dérivée est donnée par
$$
\begin{split}
\phi'(t) &= d\phi(t) \cdot 1 \\
         &= (df(a+th) \cdot d(t\mapsto a+th)) \cdot 1 \\
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

### Inégalité des accroissements finis I {.theorem #TAFS}
Soit $f:[a, a+h] \to \mathbb{R}^m$ où $a \in \mathbb{R}$, 
$h \in \left[0, +\infty\right[$.
Si $f$ est dérivable sur $[a,a+h]$ et $M$ est un majorant de $\|f'\|$,
c'est-à-dire si
$$
\mbox{pour tout } t \in [a, b], \;\|f'(t)\| \leq M.
$$
Alors 
$$
\|f(a+h) - f(a)\| \leq M h.
$$

### Démonstration {.proof}
Par construction, la fonction $f'$ est intégrable au sens de Newton et
$$
f(a+h) - f(a) = \int_a^b f'(t) \, dt.
$$
Elle est donc également intégrable au sens de Henstock-Kurzweil
(cf. [chapitre "Calcul Intégral I"](Calcul Intégral I.pdf)) ;
en combinant [la définition de l'intégrale de Henstock-Kurzweil](Calcul Intégral I.pdf#HK) 
et [le lemme de Cousin](Calcul Intégral I.pdf#cousin), 
on peut trouver des approximations arbitrairement
précises de l'intégrale de $f'$ par des sommes de Riemann[^hklc] :
pour tout $\varepsilon > 0$, 
il existe une subdivision pointée $\mathcal{D}$
de l'intervalle $[a,b]$ telle que 
$$
\left\| f(a+h) - f(a) -  S(f', \mathcal{D}) \right\| 
=
\left\| \int_a^{a+h} f'(t) \, dt -  S(f', \mathcal{D}) \right\| 
\leq 
\varepsilon.
$$
En exploitant l'inégalité triangulaire, on obtient donc
$$
\|f(a+h) - f(a)\|
\leq 
\|S(f', \mathcal{D})\| + \varepsilon.
$$
Supposons que 
$\mathcal{D} = \{(t_i, [x_i, x_{i+1}]) \; | \; 0 \leq i \leq k-1 \}$.
En utilisant à nouveau l'inégalité triangulaire, 
on peut majorer en norme la somme de Riemann $S(f',\mathcal{D})$:
$$
\|S(f', \mathcal{D})\|
=
\left\|\sum_{i=0}^{k-1} f'(t_i) (x_{i+1} - x_i)\right\|
\leq 
\sum_{i=0}^{k-1} \|f'(t_i)\| |x_{i+1} - x_i|.
$$
Comme $\|f'(t_i)\| \leq M$ pour tout $i \in \{0,\dots,k-1\},$
$$
\sum_{i=0}^{k-1} \|f'(t_i)\| |x_{i+1} - x_i|
\leq
\sum_{i=0}^{k-1} M |x_{i+1} - x_i|
\leq M \sum_{i=0}^{k-1} |x_{i+1} - x_i|
$$
Finalement, comme $a=x_0 \leq x_1 \leq \dots x_k = a+h$,
$$
\sum_{i=0}^{k-1} |x_{i+1} - x_i| = \sum_{i=0}^{k-1} (x_{i+1} - x_i) =
x_p - x_0 = (a+h) - a = h
$$ 
et donc 
$\|S(f', \mathcal{D})\| \leq Mh.$
Par conséquent, $\|f(a+h) - f(a)\| \leq M h + \varepsilon$
et comme le choix de $\varepsilon > 0$ est arbitraire, on en déduit
le résultat cherché : $\|f(a+h) - f(a)\| \leq M h.$

[^hklc]: l'intégrabilité de $f'$ signifie que quelle que soit la
précision $\varepsilon>0$ cherchée on pourra trouver une jauge telle que
pour toute subdvision pointée subordonnée à cette jauge, l'écart entre
la somme de Riemann et l'intégrale est au plus $\varepsilon$. 
Le lemme de Cousin affirme que pour toute jauge il existe effectivement 
une subdivision pointée qui y soit subordonnée.

### Inégalité des accroissements finis II {.theorem #TAF}

Soient $U$ un ouvert de $\mathbb{R}^n$, et $f: U \to \mathbb{R}^m$
supposée différentiable en tout point d'un segment $[a, a+h]$ inclus 
dans $U$ et dont la différentielle est majorée en norme par $M$ sur $[a, a+h]$, 
c'est-à-dire telle que
$$
\mbox{pour tout } x \in [a, a+h], \;\|df(x)\| \leq M.
$$
Alors 
$$
\|f(a+h) - f(a)\| \leq M \|h\|.
$$

### Démonstration {.proof}
Considérons la fonction $\phi: t \in [0,1] \mapsto f(a+th)$.
Nous avons déjà montré dans la démonstration de "[Variation d'une fonction]"
que cette fonction est dérivable, de dérivée $\phi'(t) = df(a+th) \cdot h$.
De plus, 
$$
\|\phi'(t)\| = \| df(a+th) \cdot h \| \leq \| df(a+th) \|\|h\| \leq M \|h\|.
$$
Par [l'inégalité des accroissements finis dans le cas d'une variable réelle](#TAFS), 
$$
\|f(a+h) - f(a)\| = \|\phi(1) - \phi(0)\|
\leq M \|h\| \times 1 = M \|h\|.
$$


Différentielles d'ordre supérieur
================================================================================

<!--

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
    c'est crucial pour établir la symétrie !).

  - représentation tensorielle, dérivées partielles. Application au Hessien.

  - Sommes de Taylor (avec o, avec reste intégral)

Nota: peut-être opportun de minimiser le coté diff par les valeurs matricielles.
Idées serait de caractériser $df$ en vérifiant la différentiabilité de
$x \mapsto df(x)\cdot h$ pour tout $h$: on ne "monte" pas en rang et
on peut définit $d^2f(x) \cdot k \cdot h := d(x \mapsto df(x)\cdot h)(x) \cdot k$

Différentielles d'ordre supérieur
--------------------------------------------------------------------------------

### Note {.speaker-note}

La démarche pour présenter les différentielles d'ordre supérieur a été
simplifié, mais le narratif peut profiter des "échecs" qui mène à notre
solution finale:

  1. On a envie de définir $d^2f(x)$ comme $d(x \mapsto df(x))(x)$.
     C'est *exactement* la même démarche que la dérivée, et c'est
     une démarche légitime que l'on adoptera pour le cadre de la dimension
     infinie. Seul "problème", l'objet $df(x)$ appartient aux applis
     linéaire de $\mathbb{R}^n$ dans $\mathbb{R}^m$ et à ce stade on ne
     sait différencier que des fonctions à valeurs dans $\mathbb{R}^p$.

  2. On "patche" la démarche précédente: ok, $df(x)$ est linéaire de
     $\mathbb{R}^n$ dans $\mathbb{R}^m$, mais c'est isomorphe (via les
    matrices, plus la "mise à plat") à $\mathbb{R}^p$ pour $p=mn$.
    Si on note $\pi$ cette correspondance, on peut étudier la diff
    de $\pi \circ df$ et quand ça existe, le seul pb est que l'objet
    associé produit des valeurs dans $\mathbb{R}^p$ au lieu de
    trucs dans $\mathbb{R}^n \stackrel{\ell}{\to} \mathbb{R}^m$, 
    mais c'est pas grave, on peut inverser la transformation, ce qui
    donne comme définition
    $$
    d^2 f(x) = \pi^{-1} \circ d(\pi \circ df)(x).
    $$
    c'est-à-dire
    $$
    d^2 f(x) \cdot h \cdot k = (\pi^{-1} (d(\pi \circ df)(x) \cdot h)) \cdot k
    $$
    (attention ici, "$\cdot$" ou "$\circ$" deviennent dangereux à utiliser
    sans parenthèse, on a basculé dans du higher-order avec $\pi$; et la
    convention que je pensais utiliser en remplaçant $\circ$ par
    $\cdot$ quand l'application est linéaire déconne avec $\pi$ parce
    qu'il y a des applications non-linéaire "plus bas"; le cadre ou 
    "$\cdot$" fait le job sans ambiguité serait à restreindre/préciser ...).
    Bon, voilà pourquoi je crois que même si c'est tentant sur le principe, 
    il ne faut pas présenter les choses comme ça au final.
    Mais ça peut faire l'objet d'exercices intéressants.

  3. La version final, hyper simple: on se refuse à différencier un objet
     fonctionnel, on l'évalue sur une direction / variation de l'argument
     et là on s'est ramené au cadre usuel, donc on requière la diff et on
     constate que le résultat est linéaire par rapport à la première 
     variation choisie, et on en déduit l'"anatomie" de la différentielle
     d'ordre 2 (c'est donc moins une construction qu'une découverte ...).
     Au passage, par linéarité, on peut se convaincre facilement que notre
     définition de la différentielle d'ordre 2 revient à vérifier que 
     chaque dérivée partielle (d'une fonction différentiable)
     est différentiable. Donc on vérifie l'existence avec la différentielle,
     mais on peut utiliser les dérivées partielles pour les calculs
     intermédiaires.


### Note {.design-note}

Notre définition simplifie la vie en dimension finie en se ramenant 
directement à chaque étape de la façon la plus simple au cadre de la 
différentielle de fonctions de $\mathbb{R}^n$ dans $\mathbb{R}^m$.
Mais elle n'est probablement pas adapté au cadre de la dimension
finie; l'adaptation la plus simple consisterait à écrire l'expression
qui fait que $df(x) \cdot h$ existe en terme de limite par rapport
à un terme $k$, mais à requérir en plus que cette limite existe
uniformément par rapport à l'argument $h$ tant que $h$ reste borné
(voir par exemple [ici](https://en.wikipedia.org/wiki/Fr%C3%A9chet_derivative#Higher_derivatives)).

A ce stade, le cadre abstrait classique devient probablement préférable,
car simplificateur, mais

  - un contre-exemple qui montre que notre définition ne "marche pas"
    en dimension infinie (absence d'équivalence avec la classique)
    serait intéressant

  - une note / un exercice sur cette définition alternative au cadre
    abstrait, plus proche de la démarche que nous avons choisi pour 
    la dimension finie pourrait être intéressant

-->

### Différentielle d'ordre 2 {.definition #d2}
Soit $f: U \subset \mathbb{R}^n \to \mathbb{R}^m$ une fonction différentiable
dans un voisinage d'un point $x$ de $U$. 
On dira que $f$ est *deux fois différentiable en $x$* 
si pour tout vecteur $h$ de $\mathbb{R}^n$,
la fonction $x \mapsto df(x) \cdot h$ est différentiable en $x$.
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
    A \to B \to C \to D := A \to (B \to (C \to D)).
    $$
    La convention associée -- utilisée dans la définition de la différentielle
    d'ordre 2 -- veut que lors de l'application d'une fonction linéaire,
    le symbole "$\cdot$" associe à gauche, par exemple:
    $$
    L \cdot h \cdot k :=  (L \cdot h) \cdot k,
    $$
    $$
    L \cdot h \cdot k \cdot l := ((L \cdot h) \cdot k) \cdot l.
    $$


### Variation de la différentielle I {.proposition #LVD} 
Si $f: U \subset \mathbb{R}^n \to \mathbb{R}^m$ est une fonction 
deux fois différentiable en $x \in U$,
$$
df(x+k) = df(x) + (h \mapsto d^2 f(x) \cdot h \cdot k) + o(\|k\|).
$$

### Interprétation du $o(\|k\|)$ {.remark}
L'équation ci-dessus s'applique à des fonctions linéaires de $\R^n$
dans $\R^m$. Elle doit donc être interprétée comme l'existence
d'une fonction $E$, définie dans un voisinage de $0$ dans $\R^n$, 
vérifiant
$$
E(k) \in \R^n \stackrel{\ell}{\to} \R^m \; \mbox{ et } \;
\lim_{h \to 0} E(k) = E(0) = 0,
$$
telle que
$$
df(x+k) = df(x) + (h \mapsto d^2 f(x) \cdot h \cdot k) + E(k) \|k\|.
$$

### Démonstration {.proof}
Par [définition de la différentielle d'ordre 2 en $x$](#d2), 
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
le terme $\varepsilon_{h}(k)$ est donc linéaire en $h$ ; 
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
df(x) + (h \mapsto d^2f(x) \cdot h \cdot k) + E(k) \|k\|,
$$
Par ailleurs, pour tout couple de 
vecteurs $h$ et $k$ de $\mathbb{R}^n$, on a
$$
\begin{split}
\|E(k) \cdot h\| &= \left\| E(k) \cdot \left(\sum_i h_i e_i \right) \right\| \\
&\leq \sum_i \|E(k) \cdot e_i\| |h_i| \\
&\leq \left(\sum_i \|E(k) \cdot e_i\|\right) \|h\| 
= \left(\sum_i \|\varepsilon_{e_i}(k)\|\right) \|h\|
\end{split}
$$
donc la norme d'opérateur de $E(k)$ vérifie
$$
\|E(k)\| \leq \sum_i \|\varepsilon_{e_i}(k)\| \to 0
\, \mbox{ quand } k \, \to 0,
$$
ce qui prouve le résultat cherché.

### Variation d'ordre $2$
Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}^m$ et $x \in U$.
Quand cette expression est définie, on appelle *variation d'ordre 2*
de $f$ en $x$, associée aux variations $h$ et $k$ de l'argument,
la grandeur
$$
\begin{split}
\Delta^2 f(x, h, k) &=\Delta(x \mapsto \Delta f(x, h))(x, k) \\
&= \Delta f(x+k, h) - \Delta f(x, h).
\end{split}
$$

### Variation et différentielle d'ordre deux {.theorem #D2d2}
Pour tout $\varepsilon > 0$, il existe un $\eta > 0$ tel que si
$\|h\| \leq \eta$ et $\|k\| \leq \eta$, alors
$$
\left\|\Delta^2f(x, h, k) - d^2f(x)\cdot h\cdot k \right\| \leq \varepsilon (\|h\| + \|k\|)^2.
$$

### Démonstration  {.proof}
Considérons des vecteurs $h$ et $k$ tels que $x+h$, $x+k$ et $x+h+k$ soient
dans le domaine de définition de $f$.
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
la différence vaut $e = g(h) - g(0)$. 
Cette différence peut être majorée par [l'inégalité des accroissements finis](#TAF) : 
$g$ est différentiable sur le segment $[0, h]$ et
$$
dg(u) = df(x+u+k) - df(x+u) - (h \mapsto d^2f(x) \cdot h \cdot k). 
$$
Comme
$$
\begin{split}
dg(u) &= (df(x+u+k) - df(x) - (h \mapsto d^2f(x) \cdot h \cdot (u+k)) )\\
      &\phantom{=} - (df(x+u) - df(x) - (h \mapsto d^2f(x) \cdot h \cdot u)),
\end{split}
$$
par le théorème controllant la [variation de la différentielle][Variation de la différentielle I],
pour $\varepsilon > 0$ quelconque, comme
$\|u+k\| \leq \|h\| + \|k\|$ et $\|u\| \leq \|h\|$, 
on peut trouver un $\eta > 0$ tel que si $\|h\| < \eta$ et $\|k\| < \eta,$ 
alors 
$$
\|dg(u)\| \leq \frac{\varepsilon}{2} (\|h\| + \|k\|) + \frac{\varepsilon}{2} \|h\|.
$$
Par conséquent, [le théorème des accroissements finis](#TAF) fournit
$$
\|e\| = \|dg(u) - dg(0)\| \leq  \left( \frac{\varepsilon}{2} (\|h\| + \|k\|) + \frac{\varepsilon}{2} \|h\|\right)\|h\| \leq \varepsilon (\|h\| + \|k\|)^2.
$$

### Symétrie de la différentielle d'ordre $2$ {#SD2 .theorem}
Soit $f: U \subset \mathbb{R}^n \to \mathbb{R}^m$ une fonction 
deux fois différentiable en un point $x$ de $U$. Pour tout couple
de vecteur $h$ et $k$ de $\mathbb{R}^n$, on a
$$
d^2 f (x) \cdot h \cdot k = d^2 f(x) \cdot k \cdot h.
$$

### Démonstration {.proof}
Notons au préalable que
$$
\begin{split}
\Delta^2 f(x, h, k) &= (f(x+k+h) - f(x+k)) - (f(x+h) - f(x)) \\
&= f(x+h+k) - f(x+h) - f(x+k) + f(x) \\
&= (f(x+k+h) - f(x+h)) - (f(x+k) - f(x)) \\
&= \Delta^2 f(x, k, h).
\end{split}
$$
La variation d'ordre $2$ de $f$ en $x$ est donc
symétrique par rapport à ses arguments $h$ et $k$.
On peut alors exploiter [la relation entre variation d'ordre $2$ et 
différentielle d'ordre 2](#D2d2) en notant que
\begin{multline*}
\|d^2f(x) \cdot h \cdot k - d^2f(x) \cdot k \cdot h \|
\leq \\
\|\Delta^2f(x, h, k) - d^2f(x)\cdot h\cdot k\| + \| \Delta^2f(x, k, h) - d^2f(x)\cdot h\cdot k\|.
\end{multline*}
On obtient pour tout $\varepsilon > 0$ et quand $h$ et $k$ sont suffisamment petits,
$$
\begin{split}
\|d^2f(x) \cdot h \cdot k - d^2f(x) \cdot k \cdot h \| 
\leq 2\varepsilon (\|h\|+\|k\|)^2.
\end{split}
$$
Si $h$ et $k$ sont arbitraires, en substituant $th$ à $h$ et $tk$ à $k$
pour un $t>0$ suffisamment petit pour que l'inégalité ci-dessus soit valable,
comme 
$$
d^2f(x) \cdot th \cdot tk - d^2f(x) \cdot tk \cdot th
=t^2 \times (d^2f(x) \cdot h \cdot k - d^2f(x) \cdot k \cdot h)
$$
et 
$$
2 \varepsilon (\|th\|+\|tk\|)^2 = t^2 \times 2 (\|h\|+\|k\|)^2,
$$
on voit que l'inégalité est en fait valable pour des $h$ et $k$ arbitraires.
On en déduit que $d^2f(x) \cdot h \cdot k - d^2f(x) \cdot k \cdot h = 0.$

### Variation de la différentielle II {.theorem} 
Si $f: U \subset \mathbb{R}^n \to \mathbb{R}^m$ est une fonction 
deux fois différentiable en $x \in U$,
$$
df(x+k) = df(x) + d^2 f(x) \cdot k + o(\|k\|)
$$

### Démonstration {.proof}
Par le [lemme sur la variation de la différentielle](#LVD), on sait que
$$
df(x+k) = df(x) + (h \mapsto d^2 f(x) \cdot h \cdot k) + o(\|k\|).
$$
La [différentielle d'ordre 2 étant symétrique](#SD2), 
$$
d^2 f(x) \cdot h \cdot k = d^2 f(x) \cdot k \cdot h = (d^2 f(x) \cdot k) \cdot h,
$$
ce qui fournit l'égalité cherchée.

### Dérivées partielles d'ordre 2 {.definition}
Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}^m$ et
$x \in U$. Soient $i$ et $j$ deux indices dans $\{1,\dots, n\}$.
Lorsque la $j$-ème dérivée partielle de $f$ est définie sur $U$ et
admet en $x$ une $i$-ème dérivée partielle, on l'appelle 
*dérivée partielle d'ordre 2* de $f$ en $x$ par rapport aux $j$-ème 
et $i$-ème variables et on la note $\partial^2_{ij} f(x)$:
$$
\partial^2_{ij} f(x) := \partial_i (x \mapsto \partial_j f(x))(x).
$$

### Symétrie des dérivées partielles d'ordre 2 {.proposition #sdp2}
Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}^m$ et
$x \in U$. Si $f$ est deux fois différentiable en $x$, alors pour
toute paire d'indice $i$ et $j$ la dérivée partielle $\partial_{ij} f(x)$
existe et 
$$
\partial_{ij} f(x) = \partial_{ji} f(x) = d^2 f(x) \cdot e_i \cdot e_j.
$$

### Démonstration {.proof}
Si $f$ est deux fois différentiable, on a $\partial_j f(x) = d(f(x)) \cdot e_j$,
puis $\partial^2_{ij} f(x) = d(d(f(x)) \cdot e_j) \cdot e_i$. 
Par [définition de la différentielle d'ordre 2](#d2),
$$d^2f(x) \cdot e_j \cdot e_i = d(d(f(x)) \cdot e_j) \cdot e_i,$$
on en déduit donc que $\partial^2_{ij} f(x) = d^2f(x) \cdot e_j \cdot e_i$.
Par [symétrie de la différentielle d'ordre 2](#SD2), 
$\partial^2_{ij} f(x) = \partial^2_{ji} f(x)$.

### Hessienne {.definition}
Soit $f: U \subset \R^n \to \R$ une fonction deux fois différentiable en 
$x \in U$. On appelle *Hessienne* de $f$ et $x$ et l'on note
$\nabla^2f(x)$ l'application linéaire $\R^n \to \R^n$ telle 
que pour tout couple de vecteurs $h$ et $k$ de $\R^n$
$$
d^2f(x) \cdot h \cdot k = \left<\nabla^2f(x) \cdot h, k \right>.
$$
La *matrice hessienne $H_f(x)$* est la matrice associée à cette application
linéaire ; elle est donnée par 
$$
(H_f(x))_{ij} = \partial^2_{ij} f(x).
$$

### Démonstration (expression de la matrice hessienne) {.proof}
Elle résulte directement de la définition de $\nabla^2 f(x)$ et des liens entre
$d^2f(x)$ et $\partial^2_{ij} f(x)$ établis par la proposition 
["Symétrie des dérivées partielles d'ordre 2"](#sdp2).


### {.ante}
La notion de différentielle d'ordre $2$ se généralise sans difficulté
à un ordre plus élevé, par induction sur l'ordre de la différentielle.

### Différentielle d'ordre $k$ {.definition #dos}

Soit $f: U \subset \mathbb{R}^n \to \mathbb{R}^m$ une fonction différentiable
à l'ordre $k-1$ dans un voisinage d'un point $x$ de $U$. On dira que $f$ est 
*$k$ fois différentiable en $x$* si pour tous vecteurs $h_1, \dots, h_{k-1}$ 
de $\mathbb{R}^n$, 
la fonction 
$$x \mapsto d^{k-1}f(x) \cdot h_1 \cdot h_2 \cdot \hdots \cdot h_{k-1}$$ 
est différentiable en $x$.
La *différentielle d'ordre $k$ de $f$ en $x$*, notée $d^k f(x)$ 
est définie comme l'application linéaire telle que pour tout 
$h_1, \dots, h_{k-1}$ de $\mathbb{R}^n$,
$$
d^k f(x) \cdot h_1 \cdot h_2 \cdot \hdots \cdot h_{k-1} := d(x\mapsto d^{k-1}f(x) \cdot h_1 \cdot h_2 \cdot \hdots \cdot h_{k-1})(x)
$$
ou de façon équivalente
$$
d^k f(x) \cdot h_1 \cdot h_2 \hdots \cdot h_{k-1} \cdot h_k:= d(x\mapsto d^{k-1}f(x) \cdot h_1 \cdot h_2 \cdot \hdots \cdot h_{k-1})(x) \cdot h_k
$$

### Remarque
On a 
$$
d^kf(x) \in \overbrace{\mathbb{R}^n \to \mathbb{R}^n \to \cdots \to  \mathbb{R}^n}^{k \; \mathrm{termes}} \to \mathbb{R}^m
$$


### Stratification {.lemma #stratification}
Si $f: U \subset \mathbb{R}^n \to \mathbb{R}^m$ est une fonction 
$k$ fois différentiable en un point $x$ de $U$, pour tous vecteurs 
$h_1$, $h_2$, $\dots$, $h_k$ de $\R^n$, et tout $p \in \{0,\dots, k\}$,
on a
$$
d^k f(x) \cdot h_1 \cdot \hdots \cdot h_k
=
d^{k-p} (x \mapsto d^p f(x) \cdot h_1 \cdot \hdots \cdot h_{p})(x) \cdot h_{p+1} \cdot \hdots \cdot h_k.
$$

### Démonstration {.proof}
Faisons l'hypothèse que le théorème est satisfait lorsque la fonction est $j$
fois différentiable pour tout $j \leq k$. C'est de toute évidence le cas
pour $k=0, 1, 2$ ; montrons qu'il est encore vrai pour $j=k+1$.

Notons tout d'abord que si $p=0$, le résultat est évident ; on supposera
donc dans la suite que $p \in \{1,\dots,k+1\}$.
Par [définition des différentielles d'ordre supérieur](#dos),
$$
d^{k+1} f(x) \cdot h_1 \cdot \hdots \cdot h_{k+1}
= d (d^k f(x) \cdot h_1 \cdot \hdots \cdot h_{k}) \cdot h_{k+1}.
$$
Or, par l'hypothèse de récurrence à l'ordre $k$,
$$
d^k f(x) \cdot h_1 \cdot \hdots \cdot h_{k}
= d^{k-p} (d^p f(x) \cdot h_1 \cdot \hdots \cdot h_p) \cdot h_{p+1} \cdot \hdots \cdot h_k
$$
donc si l'on pose $g(x) = d^p f(x) \cdot h_1 \cdot \hdots \cdot h_p$ et 
que l'on applique l'hypothèse de récurrence à l'ordre $k+1-p$
(un nombre compris entre $0$ et $k$), on obtient
$$
\begin{split}
d^{k+1} f(x) \cdot h_1 \cdot \hdots \cdot h_{k+1}
&=
d(d^{k-p} g(x) \cdot h_{p+1} \cdot \hdots \cdot h_k)\cdot h_{k+1} \\
&=
d^{k+1-p} g(x) \cdot h_{p+1} \cdot \hdots \cdot h_k \cdot h_{k+1}
\end{split}
$$
et donc au final
$$
d^{k+1} f(x) \cdot h_1 \cdot \hdots \cdot h_{k+1}
=
d^{k+1-p} (d^p f(x) \cdot h_1 \cdot \hdots \cdot h_p) \cdot h_{p+1} \cdot \hdots \cdot h_k \cdot h_{k+1}.
$$
L'hypothèse de récurrence est donc prouvée au rang $k+1$, 
ce qui établit le résultat.

### Symétrie des différentielles d'ordre supérieur {.proposition #sdos}
Soit $f: U \subset \mathbb{R}^n \to \mathbb{R}^m$ une fonction 
$k$ fois différentiable en un point $x$ de $U$. Pour toute permutation
$\sigma$ de $\{1,\dots, n\}$
et pour tous vecteurs 
$h_1$, $h_2$, $\dots$, $h_k$ de $\R^n$, on a:
$$
d^k f(x) \cdot h_{\sigma(1)} \cdot \hdots \cdot h_{\sigma(i)} \cdot \hdots \cdot h_{\sigma(k)}
=
d^k f(x) \cdot h_{1} \cdot \hdots \cdot h_{i} \cdot \hdots \cdot h_{k}.
$$

### Démonstration {.proof}
Toute permutation peut être décomposée en une succession de transpositions
$\tau_{ij}$, où $\tau_{ij}(i) = j$, $\tau_{ij}(j)=i$ et $\tau_{ij}(k) = k$
si $k$ diffère de $i$ et de $j$.
Il suffit donc d'établir le résultat quand $\sigma$ est une transposition.
Nous procédons par récurrence sur $k$. Le résultat dans le cas $k=2$ résulte
de [la symétrie de la différentielle d'ordre 2](#SD2). Supposons désormais 
le résultat établi au rang $k \geq 2$. 
En utilisant [la stratification de
$d^{k+1} f(x) \cdot h_1 \cdot \hdots \cdot h_k \cdot h_{k+1}$
pour $p=1$ et $p=k$](#stratification), on peut établir le résultat si $i$ et $j$
appartiennent tous les deux à $\{2,\dots, k+1\}$ ou à $\{1,\dots, k\}$.
Dans l'unique cas restant, on peut décomposer $\tau_{1(k+1)}$ en
$\tau_{2(k+1)} \circ \tau_{12} \circ \tau_{2(k+1)}$ et se ramener 
au cas précédent.

### Dérivées partielles d'ordre supérieur et multi-indices {.remark}
Les dérivées partielles d'ordre supérieur se définissent par récurrence,
de manière similaire aux dérivées partielles d'ordre $2$. Pour simplifier
la notation $\partial^k_{i_1 \dots i_k} f(x)$, on exploite le fait que
si $f$ est $k$ fois différentiable en $x$,
$$
\partial^k_{i_1 \dots i_k} f(x) = d^k f(x) \cdot e_{i_1} \cdot \hdots \cdot e_{i_k}.
$$
Compte tenu de la symétrie de $d^k f(x)$, peu importe l'ordre de $i_1$, $\dots$, $i_k$, 
seul le nombre de fois où un indice apparaît compte. 
Cette remarque fonde une notation basée sur les multi-indices 
$\alpha=(\alpha_1, \dots, \alpha_n) \in \N^n$ où $\alpha_i$ détermine le
nombre de fois où l'indice $i$ apparait. 
Formellement, le symbole $\partial^{\alpha} f(x)$ désigne $f(x)$ si 
$\alpha = (0, \dots, 0)$ et dans le cas contraire:
$$
\partial^{(\alpha_1, \cdots, \alpha_i + 1, \cdots, \alpha_n)} f(x) = \partial_i (\partial^{\alpha} f)(x).
$$


<!--

Fonctions à valeurs matricielles/tensorielles
--------------------------------------------------------------------------------

+1Objectif: étendre les constructions du calcul différentielle aux fonctions
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
= \frac{x}{\|x\|} \cdot \left(\frac{x}{\|x\|}\right)^* \cdot y
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

-->

### Puissance symbolique
Comme les différentielles d'ordre supérieure sont fréquemment évaluées 
lorsque les termes $h_1$, $h_2$, $\dots$, sont égaux, on adoptera la notation
(purement syntaxique) suivante :
$$
(\cdot \, h)^k := \overbrace{\cdot h \cdot \hdots \cdot h}^{k \; \mathrm{termes}}.
$$

### Développement limité d'ordre supérieur {.theorem #dl}
Soit $f: U \subset \R^n \to \R^m$ une fonction $j$ fois différentiable au point
$x \in U$. Alors
$$
f(x+h) = \sum_{i=0}^{j}  \frac{d^i f(x)}{i!} (\cdot \, h)^i
+ o(\|h\|^j).
$$

### Démonstration {.proof}
Le résultat est clair pour $j=0$. Supposons le vrai à un rang $j-1$ arbitraire
pour toute fonction $j-1$ fois différentiable
et supposons que $f$ est $j$ fois différentiable. Formons le reste 
d'ordre $j$ associé à $f$:
$$
r(h) = f(x+h) - \sum_{i=0}^{j} \frac{d^i f(x)}{i!} (\cdot \, h)^i.
$$
Il nous faut montrer que $r(h)$ est un $o(\|h\|^j)$, ce qui 
nous allons accomplir en établissant que $\|dr(h)\| = o(\|h\|^{j-1})$.
En effet, si $dr(h) = E(h) \|h\|^{j-1}$ où l'application linéaire $E$
est un $o(1)$, alors pour tout $\varepsilon > 0$ et $h$ assez proche de $0$ 
on a $\|E(h)\| \leq \varepsilon$ et donc par [le théorème des accroissements
finis](#TAF),
$$
\|r(h)\| = \|r(h) - r(0)\| \leq \varepsilon \|h\|^{j-1} \times \|h\|
= \varepsilon \|h\|^j,
$$
ce qui établit que $r(h) = o(\|h\|^j)$.

Etablissons donc que $r(h)$ est un $o(\|h\|^j)$.
Les termes $d^i f(x)\cdot h_1 \cdot \hdots \cdot h_i$ 
sont linéaires par rapport à chacun des $h_j$, donc pour tout vecteur 
$k$, compte tenu de la symétrie de $d^i f(x)$,
$$
d^i f(x) (\cdot \, (h+k))^i
= 
d^i f(x) (\cdot \, h)^i
+ i d^i f(x) (\cdot \, h)^{i-1} \cdot k
+ o(\|k\|).
$$
La différentielle de 
$h \mapsto {d^i f(x)} (\cdot \, h)^i$
vaut donc $id^i f(x) (\cdot \, h)^{i-1}$ et
$$
d r(h) \cdot k = df(x+h) \cdot k - d f(x) \cdot k - 
d^2f(x) \cdot h\cdot k - \dots -
\frac{d^i f(x)}{(i-1)!} (\cdot \, h)^{i-1} \cdot k.
$$
Par [le lemme de stratification](#stratification) et 
[la symétrie des différentielles d'ordre supérieur](#sdos), on obtient 
\begin{multline*}
d r(h) \cdot k = df(x+h) \cdot k - d f(x) \cdot k  \\ 
- d(x \mapsto df(x) \cdot k)(x) \cdot h - \dots -
\frac{d^{i-1} (x \mapsto df(x) \cdot k)(x)}{(i-1)!} (\cdot \, h)^{i-1}.
\end{multline*}
soit en posant $\phi(x) = df(x) \cdot k$,
$$
d r(h) \cdot k = \phi(x+h) - \phi(x) - 
d \phi(x) \cdot h - \dots -
\frac{d^{i-1} \phi(x)}{(i-1)!} (\cdot h)^{i-1}.
$$
L'hypothèse de récurrence nous garantit donc que 
$d r(h) \cdot k = o(\|h\|^{j-1})$ à $k$ fixé, ce qui, 
combiné avec la linéarité de $d r(h)$, fournit
$\|dr(h)\| = o(\|h\|^{j-1})$.



### Développement de Taylor avec reste intégral I {#DTRI-I}
Soit $f:[a, a+h] \to \mathbb{R}^m$ où $a \in \mathbb{R}$, 
$h \in \left[0, +\infty\right[$.
Si $f$ est $j+1$ fois dérivable sur $[a,a+h]$,
$$
f(a+h)  = \sum_{i=0}^n \frac{f^{(i)}(a)}{i!} h^i + \int_a^{a+h} \frac{f^{(j+1)}(t)}{j!} (a+h-t)^j \, dt.
$$

### Démonstration {.proof}
A l'ordre $j=0$, la relation à prouver est
$$
f(a+h) = f(a) + \int_a^{a+h} f'(t) \, dt
$$
qui n'est autre que [le théorème fondamental du calcul](#TFC).
Si l'on suppose la relation vérifiée à l'ordre $j$, et $f$ $j+2$ fois dérivable,
par [intégration par parties](#IPP), on obtient
\begin{multline*}
\int_a^{a+h} f^{(j+1)}(t) \frac{(a+h-t)^j}{j!} \, dt
= \\
\left[ f^{(j+1)}(t) \times \left( -\frac{(a+h-t)^{j+1}}{(j+1)!} \right) \right]_a^{a+h} \\
- 
\int_a^{a+h} f^{(j+2)}(t) \left( -\frac{(a+h-t)^{j+1}}{(j+1)!} \right) \, dt,
\end{multline*}
soit 
\begin{multline*}
\int_a^{a+h} f^{(j+1)}(t) \frac{(a+h-t)^j}{j!} \, dt
= \\
f^{(j+1)}(a) \times \frac{h^{j+1}}{(j+1)!}
+ 
\int_a^{a+h} f^{(j+2)}(t) \frac{(a+h-t)^{j+1}}{(j+1)!} \, dt,
\end{multline*}
ce qui achève la preuve par récurrence.

### Développement de Taylor avec reste intégral II {#DTRI-II}
Si $f: U \subset \R^n \to \R^m$ est $j+1$ fois différentiable et $[a, a+h] \subset U$,
$$
f(a+h)  = \sum_{i=0}^{j} \frac{df^{(i)}(a)}{i!} (\cdot \, h)^i
+ \int_0^{1} \frac{df^{(j+1)}(a+th)}{j!} (\cdot \, h)^{j+1} (1-t)^j\, dt.
$$

### Démonstration {.proof}
La démonstration découle directement du [développement de 
Taylor avec reste intégral dans le cas d'une fonction d'une variable réelle](#DTRI-I),
appliqué à la fonction $\phi: t \in [0, 1] \mapsto f(a+th) \in \R^m$.
Il nous suffit de montrer que $\phi$ est $j+1$ fois différentiable 
et que pour tout entier $i$ inférieur ou égal à $j+1$,
$\phi^{(i)}(t) = df^{(i)}(a+th) (\cdot \, h)^i$. 

Cette relation est évidemment satisfaite pour 
$i=0$. Supposons qu'elle soit vérifiée au rang $i \leq j$. 
La fonction $f$ étant $i+1$ fois différentiable, la fonction
$g:x \in U \mapsto df^{(i)}(x) (\cdot \, h)^i$ est différentiable, et
$$
dg(x) \cdot h = df^{(i+1)}(x) (\cdot \, h)^{i+1}.
$$
Par dérivation en chaîne, la fonction 
$t \mapsto df^{(i)}(a+th) (\cdot \, h)^i$
est donc dérivable, de dérivée $dg(a+th) \cdot h$, soit
$df^{(i+1)}(a+th) (\cdot \, h)^{i+1}.$


Annexe -- Intégrale de Newton {#intégrale-Newton}
================================================================================

### Intégrale de Newton {.definition}
Soit $f:[a, b] \to \mathbb{R}^m$. On dit que $f$ 
est *intégrable au sens de Newton* si elle admet une primitive 
$F: [a, b] \to \mathbb{R}^m$. L'intégrale de $f$ entre $a$ et $b$ est
alors définie par
$$
\int_a^b f(x) \, dx = F(b) - F(a).
$$
La primitive $F$ de $f$ quand elle existe étant déterminée à une constante près,
cette définition est non-ambiguë.

### {.remark}
Une autre façon de voir les choses : l'intégrale de Newton est définie de telle
sorte que [le théorème fondamental du calcul](#TFC) soit trivialement satisfait, 
en toute généralité.
Pour d'autres intégrales, comme l'intégrale de Riemann ou l'intégrale
de Lebesgue, il sera nécessaire de faire des hypothèses supplémentaires
sur la fonction $f'$ (par exemple, $f'$ continue) pour que ce résultat 
soit valable. L'intégrale de Henstock-Kurzweil, qui sera exposée dans
le cours de calcul intégral, vérifie bien le théorème fondamental du
calcul en toute généralité : elle étend donc l'intégrale de Newton
(et celle de Riemann, ainsi que celle de Lebesgue).

### {.ante}
L'intégrale de Newton est un outil assez primitif[^smjm] et difficile 
à exploiter ; elle vérifie tout de même quelques propriétés bien utiles.

[^smjm]: sans mauvais jeu de mots ...

### Linéarité {.proposition}
Soit $f:[a, b] \to \mathbb{R}^m$, $g:[a, b] \to \mathbb{R}^m$, et 
$\lambda$, $\mu$ deux constantes réelles. Si $f$ et $g$ sont intégrables
au sens de Newton, $\lambda f + \mu g$ également et
$$
\int_a^b \lambda f(x) + \mu g(x) \, dx
=
\lambda \int_a^b f(x) \, dx + \mu \int_a^b g(x) \, dx.
$$

### Démonstration {.proof}
Par hypothèse, $f$ a une primitive $F$, $g$ a une primitive $G$,
$$
\int_a^b f(x) \, dx = F(b) - F(a)
\; \mbox{ et } \; 
\int_a^b g(x) \, dx = G(b) - G(a).
$$
La fonction $\lambda F + \mu G$ est une primitive de $\lambda f + \mu g$
et donc
$$
\begin{split}
\int_a^b \lambda f(x) + \mu g(x) \, dx
&=
(\lambda F(b) + \mu G(b)) - (\lambda F(a) + \mu G(a))\\
&=
\lambda (F(b) - F(a)) + \mu (G(b) - G(a)) \\
&=
\lambda \int_a^b f(x) \, dx + \mu \int_a^b g(x) \, dx.
\end{split}
$$

### Majoration {.theorem #ML-lemma}
Si $f:[a, b] \to \mathbb{R}$ est une fonction intégrable au sens de Newton 
telle que $|f| \leq M,$
$$
\left| \int_a^b f(x) \, dx \right| \leq M (b-a).
$$

### Démonstration {.proof}
La fonction $g: x \in [a, b] \mapsto f(x) - M$ est intégrable au sens de Newton
et négative. Si $G$ est une primitive de $g$, elle est donc décroissante.
Par conséquent,
$$
\int_a^b (f(x) - M) \, dx = \int_a^b f(x) \, dx - M(b-a) = G(b) - G(0) \leq 0.
$$
On peut de même montrer en intégrant la fonction $x \in [a, b] \to f(x) + M$ 
que 
$$
\int_a^b f(x) \, dx + M(b-a) \geq 0,
$$
ce qui fournit le résultat cherché.

### Intégration par parties {.theorem #IPP}
Soit $f:[a, b] \to \mathbb{R}$ et $g:[a, b] \to \mathbb{R}$ deux fonctions
dérivables. Si la fonction $f g'$ est intégrable au sens de Newton, 
la fonction $f' g$ également et
$$
\int_a^b f'(x) g(x) \, dx = (f(b) g(b) - f(a) g(a)) -\int_a^b f(x) g'(x) \, dx.
$$

### Démonstration {.proof}
Comme $(fg)' = f'g + fg'$, on a $f'g = (fg)' - fg'$. 
Or, $(fg)'$ est intégrable au sens de Newton ($fg$ est une de ses primitives), 
$fg'$ est intégrable au sens de Newton par hypothèse, 
donc $f'g$ est intégrable comme combinaison linéaire de fonctions intégrables. 
De plus, 
$$
\begin{split}
\int_a^b f'(x) g(x) \,dx 
&= 
\int_a^b (fg)'(x) \, dx - \int_a^b f(x) g'(x) \, dx \\
&= (f(b) g(b) - f(a) g(a)) - \int_a^b f(x) g'(x) \, dx.
\end{split}
$$

Exercices
================================================================================

<!--
Vecteurs, vecteurs colonnes, vecteurs lignes
--------------------------------------------------------------------------------

Soit $x = (x_1, \cdots, x_n)$ un vecteur de $\mathbb{R}^n$.

### Question 1
Le vecteur colonne $X$ associé à $x$
$$
X = \left[ 
\begin{array}{c}
x_1 \\
\vdots \\
x_n
\end{array}
\right] \in \mathbb{R}^{n \times 1}.
$$
est une matrice et représente donc une application linéaire. Laquelle ?

$\to$ [Solution](#sol-vvcvl-1)

### Question 2
Le vecteur colonne ligne $X^*$ associé à $x$
$$
X^* = \left[ 
\begin{array}{ccc}
x_1 & \cdots & x_n
\end{array}
\right] \in \mathbb{R}^{1 \times n}.
$$
représente également une application linéaire. Laquelle ?

$\to$ [Solution](#sol-vvcvl-2)

-->

Dérivée sur un intervalle fermé {.question #dif}
--------------------------------------------------------------------------------

Montrer qu'une fonction $f$ est dérivable sur l'intervalle fermé $[a, b]$
-- $f'(a)$ et $f'(b)$ désignant alors les dérivées à droite de $f$ en $a$
et à gauche de $f$ en $b$ --
si et seulement si il existe un $\varepsilon > 0$ et une extension $g$ de
$f$ sur $\left]a-\varepsilon, b+\varepsilon\right[$ tel que $g$ soit dérivable
et qu'alors, $f' = g'|_{[a, b]}$.


Différentiation en chaîne {#dec}
--------------------------------------------------------------------------------

[La règle générale de différentiation en chaîne](#chain-rule)
s'applique à la composée de deux fonctions différentiables 
$f: U \subset \R^p \to \R^n$ et $g: V \subset \R^n \to \R^m$.

### Question 1 {.question #dec-1}
Calculer $d(g \circ f)$ quand $p = n = 1$ (on utilisera les dérivées
de $f$ et $g$).

### Question 2 {.question #dec-2}
Calculer $d(g \circ f)$ quand $p = m = 1$ (on utilisera les dérivées 
et/ou gradients de $f$ et $g$).

<!--
Soit $f: U \subset \mathbb{R} \to \mathbb{R}$ et 
$g: V \subset \mathbb{R} \to \mathbb{R}$ deux fonctions définies
sur des ouverts $U$ et $V$ et telles que $f(U) \subset V$. 
Si $f$ est dérivable en $x \in U$ et $g$ est dérivable en $f(x) \in V$,
alors la composée $g \circ f$ est dérivable en $x$ et
$$
(g \circ f)'(x) = g'(f(x)) f'(x).
$$
-->

Fonction quadratique 
--------------------------------------------------------------------------------
Soit $A: \R^n \to \R^n$ un opérateur linéaire, $b$ un vecteur de $\R^n$ et
$c \in \R$. On considère la fonction $f:\R^n \to \R$ définie par
$$
f(x) = \frac{1}{2} \left<x, A \cdot x \right> + \left<b, x\right> + c. 
$$

### Question 1 {.question #fq-1}
Montrer que $f$ est 2 fois différentiable en tout point $x$ de $\R^n$ ; 
calculer $\nabla f(x)$ et $\nabla^2 f(x)$.

### Question 2 {.question #fq-2}
Soit $x \in \R^n$ ; on suppose que $\nabla^2 f(x)$ est inversible. 
Montrer que la fonction $f$ admet un unique point critique $x_0$ et le 
calculer en fonction de $x$, $\nabla f(x)$ et $\nabla^2 f(x)$.

Vecteur gaussien
--------------------------------------------------------------------------------

La densité de probabilité associé à un vecteur gaussien $X \in \R^d$ 
est proportionnelle à la fonction
$$
f: x \in \R^d \mapsto \exp\left( -\frac{1}{2} \left<x, \Sigma^{-1} \cdot x \right> \right)
$$
où $\Sigma : \R^d \to \R^d$ est un opérateur linéaire autoadjoint 
(c'est-à-dire que $\Sigma^* = \Sigma$) 
tel que $\left<x, \Sigma \cdot x \right> > 0$ quand $x\neq 0$.

### Question 1 {.question #vg-1}
Montrer que la fonction $f$ est différentiable et calculer son gradient.

### Question 2 {.question #vg-2}
Montrer que la fonction $f$ est deux différentiable et calculer sa 
hessienne.

Robot manipulateur {.question #rm}
--------------------------------------------------------------------------------

Les coordonnées cartésiennes $x$ et $y$ de l'effecteur final 
d'un robot dans le plan, composé de deux corps rigides de longueur
$\ell_1$ et $\ell_2$ et d'articulation rotoïdes sont données
par
$$
\left|
\begin{array}{rcl}
x &=& \ell_1 \cos \theta_1 + \ell_2 \cos (\theta_1 + \theta_2) \\
y &=& \ell_1 \sin \theta_1 + \ell_2 \sin (\theta_1 + \theta_2) \\
\end{array}
\right.
$$
où $\theta_1$ et $\theta_2$ sont les coordonnées articulaires du robot.

Montrer que l'application 
$f: (\theta_1, \theta_2) \in \R^2 \mapsto (x, y) \in \R^2$ 
est différentiable et déterminer sa matrice jacobienne.

Différentiation matricielle
--------------------------------------------------------------------------------

Source: [@Tao13]

### Question 1 {.question #dm-1}
Montrer que l'application $\det: A \in \R^{n \times n} \to \det A \in \R$ est 
différentiable en l'identité ($A = I$) et calculer cette différentielle.

### Question 2 {.question #dm-2}
L'identité de Weinstein–Aronszajn $\det (I + AB) = \det (I + BA)$
vaut pour toutes les matrices carrées $A$ et $B$ de même dimension.
En déduire une identité concernant $\tr A B$ et $\tr BA$.

### Question 3 {.question #dm-3}
Montrer que l'application $A \mapsto A^{-1}$ est définie dans un voisinage
ouvert de l'identité, est différentiable en ce point et calculer cette
différentielle.

Dérivée partielles, directionnelles et différentielle
--------------------------------------------------------------------------------

### Question 1 {.question #dpdd-1}
Construire une fonction $f:\R^2 \to \R$ dont les dérivées partielles
existent en $(0,0)$ mais qui ne soit pas différentiable en ce point.

### Question 2 {.question #dpdd-2}
Construire une fonction $f:\R^2 \to \R$ dont la dérivée dans la direction
$h \in \R^2$
$$
f'(x, h) := \lim_{t \to 0} \frac{f(x+th) - f(x)}{t}
$$
existe en $x=(0,0)$ pour tout $h \in \R^2$,
mais qui ne soit pas différentiable en ce point.


Dérivée directionnelle d'Hadamard
--------------------------------------------------------------------------------

Source: [@Sha90]

Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}^m$ et $x \in U$. 
La fonction $f$ est *directionnellement dérivable* si pour tout
vecteur $h \in \mathbb{R}^n$, la dérivée directionnelle
$$
f'(x, h) := (t \mapsto f(x+ th))'(0) = \lim_{t \to 0} \frac{f(x+th) - f(x)}{t}
$$
est bien définie.

On introduit une variante à cette définition:
la fonction $f$ est *directionnellement dérivable au sens de Hadamard* 
en $x$ si pour tout chemin $\gamma: I \subset \mathbb{R} \to \mathbb{R}^n$,
défini sur un intervalle ouvert $I$ contenant $0$, tel que
$\gamma(I) \subset U$,  $\gamma(0) = x$ et $\gamma'(0)$ existe,
la dérivée $(f \circ \gamma)'(0)$ existe. 

### Question 1 {.question #ddh-1}
Montrer que si $f$ est directionnellement dérivable au sens de Hadamard 
en $x$, alors $f$ est directionnellement dérivable au sens classique.

### Question 2 {.question #ddh-2}
Montrer que si $f$ est directionnellement dérivable au sens de Hadamard
en $x$, la grandeur $(f \circ \gamma)'(0)$ ne dépend de $\gamma$
qu'à travers $\gamma'(0)$ et que par conséquent
$$
(f\circ \gamma)'(0) = f'(x, \gamma'(0)).
$$

### Question 3 -- Dérivation en chaîne {.question #ddh-3}
Soit $f: U \subset \mathbb{R}^p \to \mathbb{R}^{n}$ et 
$g: V \subset \mathbb{R}^n \to \mathbb{R}^{m}$ deux fonctions définies
sur des ouverts $U$ et $V$ et telles que $f(U) \subset V$. 
Montrer que si $f$ est directionnellement dérivable au sens de Hadamard 
en $x \in U$ et que $g$ est directionnellement dérivable au sens de Hadamard 
en $f(x) \in V$, alors la composée $g \circ f$ est directionnellement 
dérivable au sens de Hadamard en en $x$ et
$$
(g\circ f)'(x, h) = g'(f(x), f'(x, h)).
$$

### Question 4 {.question #ddh-4}
Montrer que $f$ est directionnellement dérivable au sens de Hadamard en $x$ 
si et seulement si la limite
$$
\lim_{(t, k) \to (0, h)} \frac{f(x+ t k) - f(x)}{t}
$$
existe et que la limite est alors égale à $f'(x, h)$.

### Question 5 {.question #ddh-5}
Une fonction dérivable directionnellement au sens de Hadamard en $x$ est 
*différentiable au sens de Hadamard* en $x$ si de plus $f'(x, h)$ 
est une fonction linéaire de $h$.
Montrer que $f$ est différentiable en $x$ au sens de Hadamard 
si et seulement si elle est différentiable en $x$ au sens de Fréchet.

Inégalité de la valeur moyenne {.question #ivm}
--------------------------------------------------------------------------------
Soit $f:[a, b] \subset \R \to \R^m$ une fonction intégrable au sens de Newton;
on appelle *valeur moyenne de $f$* la grandeur
$$
\left<f\right> := \frac{1}{b-a} \int_a^b f(x) \, dx.
$$
Quel est le lien entre $\left<f\right>$ et la grandeur 
$\sup_{x \in [a, b]} \|f(x)\|$ ?

Egalité des accroissements finis ? {.question #eaf}
--------------------------------------------------------------------------------
Soit $f:[0, 2\pi] \to \mathbb{R}^2$ la fonction définie par
$$
f(t) = (\cos t, \sin t)
$$
Peut-on trouver un $t \in [0, 2\pi]$ tel que $f(2\pi) - f(0) = f'(t) \times 2\pi$ ?

Convexité
--------------------------------------------------------------------------------

Soit $U$ un ensemble ouvert et convexe de $\R^n$ et $f: U \to \R$ une fonction
deux fois différentiable. 

### Question 0 {.question #c-0}
Calculer le développement limité à l'ordre 2 de 
$f(x+2h) - 2f(x+h) + f(x)$.

### Question 1 {.question #c-1}
Montrer que si $f$ est convexe, c'est-à-dire si
pour tous $x, y \in U$ et $\lambda\in[0,1]$,
$$
f((1-\lambda) x + \lambda y) \leq (1 - \lambda) f(x) + \lambda f(y),
$$
alors pour tout $x \in U$ et $h \in \R^n$,
$$
d^2f(x) (\cdot h)^2 = \left<\nabla^2 f(x) \cdot h, h\right> \geq 0.
$$

### Question 2 {.question #c-2}
Montrer la réciproque de ce résultat.

<!--
TODO -- Analycité
--------------------------------------------------------------------------------

Borne sur $f^{(n)}$ et analycité ?

-->

<!--
TODO -- Oloid
--------------------------------------------------------------------------------

Source: [@DS97]

cf <http://www.heldermann-verlag.de/jgg/jgg01_05/jgg0113.pdf>, par exemple
calcul plan tangent ?

-->

Solutions
================================================================================

<!--
Vecteurs, vecteurs colonnes, vecteurs lignes
--------------------------------------------------------------------------------

### Question 1 {#sol-vvcvl-1}
Par définition, le vecteur colonne associé à $x$ représente l'application
linéaire $A$ de $\mathbb{R}$ dans $\mathbb{R}^n$ telle que pour tout
$h \in \mathbb{R}$ et tout $i=1,\dots, n$, 
$$
(A h)_i = \sum_{k=1}^1 X_{ik} h = x_i h,
$$
soit $A h = h$.

### Question 2 {#sol-vvcvl-2}
Par définition, le vecteur ligne associé à $x$ représente l'application
linéaire $B$ de $\mathbb{R}^n$ dans $\mathbb{R}$ telle que pour tout
$h=(h_1, \dots, h_n) \in \mathbb{R}^n$ 
$$
B h = \sum_k x_i h_i,
$$
soit $B h = \left< x, h \right>$ ou $\left<\cdot, \cdot\right>$
désigne le produit scalaire dans $\mathbb{R}^n$. 

-->

Dérivée sur un intervalle fermé {.answer #answer-dif}
--------------------------------------------------------------------------------

Si une fonction $g$ dérivable sur $\left]a-\varepsilon, b+\varepsilon \right[$
étend la fonction $f$ définie sur $[a, b]$,
il est clair que $f$ est dérivable en tout point de $[a, b]$ et que
$g'|_{[a, b]} = f'$.

Réciproquement, si $f$ est dérivable sur $[a, b]$ (à droite en $a$ et à gauche
en $b$), alors la fonction $g: \left]a-1, b+1 \right[$ définie par 
$$
g(x) = \left|
\begin{array}{rl}
f(a) + f'(a) \times (x-a) & \mbox{si } x < a \\
f(x) & \mbox{si } x \in [a, b] \\
f(b) + f'(b) \times (x-b) & \mbox{si } x > b
\end{array}
\right.
$$
étend $f$ et est dérivable par construction.

Différentiation en chaîne 
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-dec-1}
Les fonction $f$ et $g$ sont différentiables  donc dérivables
(cf. [Différentielle et dérivée]).
Comme fonctions d'une variable, en raison du
[lien entre différentielle et dérivée][Différentielle et dérivée],
on a $df(x) \cdot h = f'(x) h$ et $dg(x) \cdot h = g'(x)h$.
Par la [règle de différentiation en chaîne](#chain-rule),
on obtient
$$
d(g \circ f)(x)= dg(f(x)) \cdot df(x).
$$
On en déduit
$$
\begin{split}
d(g \circ f)(x) \cdot h 
&= (dg(f(x)) \cdot df(x) )\cdot h \\
&=dg(f(x)) \cdot (df(x) \cdot h) \\
&= dg(f(x)) \cdot (f'(x) h) \\
&= g'(f(x)) (f'(x) h) \\
&= (g'(f(x)) f'(x)) h.
\end{split}
$$

### Question 2 {.answer #answer-dec-2}
La fonction $f$ dépendant d'une variable scalaire, elle est dérivable et 
$df(x) \cdot h = f'(x) h$. Quant à $g$ qui est à valeur scalaire, sa
différentielle en $x$ est reliée à son gradient par 
$dg(x) \cdot h =\left<\nabla g(x), h\right>$.
La [règle de différentiation en chaîne](#chain-rule),
$d(g \circ f)(x)= dg(f(x)) \cdot df(x)$ se décline donc en
$$
\begin{split}
d(g \circ f)(x) \cdot h 
&= dg(f(x)) \cdot (df(x) \cdot h) \\
&= dg(f(x)) \cdot (f'(x) h) \\
&= \left<\nabla g(f(x), f'(x)h \right>  \\
&= \left<\nabla g(f(x)), f'(x) \right> h.
\end{split}
$$ 

Fonction quadratique 
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-fq-1}
Pour tout $x \in \R^n$ et tout $h \in \R^n$, on a 
$$
\begin{split}
f(x+h) - f(x) &= \frac{1}{2} \left<(x+h), A \cdot (x+h) \right> + \left<b, x+h\right> + c
- \frac{1}{2} \left<x, A \cdot x \right> - \left<b, x\right> - c \\
& =
\frac{1}{2} \left<x, A \cdot h \right> + \frac{1}{2} \left<h, A \cdot x \right> +
\left<b, h\right> + \frac{1}{2} \left<h, A \cdot h \right> \\
&=
\frac{1}{2} \left<A^* \cdot x, h \right> + \frac{1}{2} \left<A \cdot x, h \right> +
\left<b, h\right> + \frac{1}{2} \left<h, A \cdot h \right>.
\end{split}
$$
Comme $|\left<h, A \cdot h \right>| \leq \|h\| \times \|A\| \|h\|$, ce terme
est un $o(\|h\|)$. On en conclut que
$$
f(x+h) - f(x)
= \left<\frac{1}{2}(A + A^*) \cdot x + b, h\right> + o(\|h\|).
$$
La fonction $f$ est donc différentiable en $x$, de gradient
$$
\nabla f(x) = \frac{1}{2}(A + A^*) \cdot x + b.
$$
Pour tout $h \in \R^n$, la fonction $x \mapsto \left<\nabla f(x), h\right>$
vérifie
$$
\left<\nabla f(x+k), h\right> - \left<\nabla f(x), h\right>
= \left<\frac{1}{2}(A + A^*) \cdot k, h\right>.
$$
Elle est donc différentiable et 
$$
d^2 f(x) \cdot h \cdot k = \left<\frac{1}{2}(A + A^*) \cdot k, h\right>.
$$
Par symétrie de la différentielle d'ordre $2$,
$$
d^2 f(x) \cdot h \cdot k = \left<\frac{1}{2}(A + A^*) \cdot h, k\right>,
$$
donc 
$$
\nabla^2 f(x) = \frac{1}{2}(A + A^*).
$$

### Question 2 {.answer #answer-fq-2}
Si $\nabla^2 f(x)$ est inversible (cet opérateur est constant), comme
$$
\nabla f(y) = \frac{1}{2}(A + A^*) \cdot y + b = \nabla^2 f(x) \cdot y + b,
$$
résoudre $\nabla f(y) = 0$ revient à rechercher les solutions de
$$
\nabla^2 f(x) \cdot y + b = \nabla^2 f(x) \cdot y + (\nabla f(x) - \nabla^2 f(x) \cdot x) = 0.
$$
Il existe donc un unique point critique pour $f$, donné par
$$
y = x - (\nabla^2 f(x))^{-1} \nabla f(x).
$$

Vecteur gaussien
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-vg-1}
La fonction 
$$
f: x \in \R^d \mapsto \exp\left( -\frac{1}{2} \left<x, \Sigma^{-1} \cdot x \right> \right)
$$
apparaît comme la composée des fonctions
$$
x \in \R^d \mapsto -\frac{1}{2} \left<x, \Sigma^{-1} \cdot x \right>
\; \mbox{ et } \; \exp:\R \to \R.
$$ 
La fonction $\exp$ est dérivable, et donc différentiable 
sur tout $\R$ avec $d (\exp(y)) = \exp'(y) dx = \exp(y) dy$, c'est-à-dire
$$
d\exp(y) \cdot h = \exp(y) \times h.
$$ 
Quand à la première fonction, pour tout $h \in \R^d$, on a
\begin{multline*}
-\frac{1}{2} \left<x+h, \Sigma^{-1} \cdot (x+h) \right>
=  \\
-\frac{1}{2} \left(\left<x, \Sigma^{-1} \cdot x \right>
+ <x, \Sigma^{-1} h> + <h, \Sigma^{-1} \cdot x> + \left<h, \Sigma^{-1} \cdot h \right>
\right). 
\end{multline*}
D'une part, comme $\Sigma$ est autoadjoint (et inversible), $\Sigma^{-1}$ également et
$$
<x, \Sigma^{-1} \cdot h> + <h, \Sigma^{-1} \cdot x> = 2 \left<\Sigma^{-1} \cdot x, h \right>,
$$
d'autre part
$$
\left| \left<h, \Sigma^{-1} \cdot h \right> \right|
\leq \|h\| \times \|\Sigma^{-1} \cdot h\| \leq \|h\| \times \|\Sigma^{-1}\| \times \|h\| = o(\|h\|).
$$
La fonction est donc différentiable sur $\R^n$, avec
$$
d \left( -\frac{1}{2} \left(\left<x, \Sigma^{-1} \cdot x \right>\right) \right) \cdot h
= - \left<\Sigma^{-1} \cdot x, h \right>.
$$
La fonction $f$ est donc différentiable sur $\R^d$ comme composée
de fonctions différentiables et l'on a
$$
d f(x) \cdot h = - \exp \left( -\frac{1}{2} \left(\left<x, \Sigma^{-1} \cdot x \right>\right) \right)
\left<\Sigma^{-1} \cdot x, h \right>
= \left<-f(x) \times \Sigma^{-1} \cdot x, h \right>,
$$
le gradient de $f$ vaut donc
$$
\nabla f(x) = -f(x) \times \Sigma^{-1} \cdot x.
$$

### Question 2 {.answer #answer-vg-2}
De l'équation
$$
d f(x) \cdot h 
= \left<-f(x) \times \Sigma^{-1} \cdot x, h \right>
= -f(x) \left<\Sigma^{-1} \cdot h, x \right>
$$
on déduit que $x \mapsto d f(x) \cdot h$ est différentiable comme produit
de fonctions scalaires différentiables (la fonction 
$x \mapsto \left<\Sigma^{-1} \cdot h, x \right>$ étant linéaire). 
On a de plus
$$
\begin{split}
d (x \mapsto d f(x) \cdot h) \cdot k
&=
- (df(x) \cdot k) \times \left<\Sigma^{-1} \cdot x, h \right>
- f(x) \times \left<\Sigma^{-1} \cdot h, k \right> \\
&= 
\left<-f(x) \times \Sigma^{-1} \cdot x, k \right> \left<\Sigma^{-1} \cdot x, h \right>+
\left<-f(x) \times \Sigma^{-1} \cdot h, k\right>
\end{split}
$$

Pour des vecteurs arbitraires $u$ et $v$ dans $\R^n$, on a
$$
\left<u, k \right> \left<v, h \right>
=
\left<k, u \right> \left<v, h \right>
= k^* \cdot u  \times v^* \cdot h = (v \cdot u^* \cdot k)^* \cdot h = \left<(v \cdot u^*) \cdot k, h \right>,
$$
par conséquent
$$
d (x \mapsto d f(x) \cdot h) \cdot k
= 
-f(x) \left<(\Sigma^{-1} \cdot x \cdot x^* \cdot \Sigma^{-1} + \Sigma^{-1}) h, k\right>.
$$
La Hessienne de $f$ en $x$ est donc donnée par
$$
\nabla^2 f(x) = - f(x) (\Sigma^{-1} \cdot x \cdot x^* \cdot \Sigma^{-1} + \Sigma^{-1}).
$$


Robot manipulateur {.answer #answer-rm}
--------------------------------------------------------------------------------

Des équations
$$
\left|
\begin{array}{rcr}
x &=& \ell_1 \cos \theta_1 + \ell_2 \cos (\theta_1 + \theta_2) \\
y &=& \ell_1 \sin \theta_1 + \ell_2 \sin (\theta_1 + \theta_2) \\
\end{array}
\right.
$$
on déduit que les dérivées partielles de $x$ et de $y$ par rapport
à $\theta_1$ et $\theta_2$ existent et vérifient
$$
\begin{array}{rcl}
\partial_1 x(\theta_1, \theta_2)
&=& -\ell_1 \sin \theta_1 - \ell_2 \sin (\theta_1 + \theta_2), \\
\partial_2 x(\theta_1, \theta_2)
&=& - \ell_2 \sin (\theta_1 + \theta_2), \\
\partial_1 y(\theta_1, \theta_2)
&=& \ell_1 \cos \theta_1 + \ell_2 \cos (\theta_1 + \theta_2), \\
\partial_2 y(\theta_1, \theta_2)
&=& \ell_2 \cos (\theta_1 + \theta_2).
\end{array}
$$
Ces grandeurs étant continues, la fonction $f=(x, y)$ est continûment
différentiable et donc différentiable. Si l'on note $s_1 = \sin \theta_1$,
$s_{12}= \sin(\theta_1+\theta_2)$, $c_1 = \cos \theta_1$ et
$c_{12}= \cos(\theta_1+\theta_2)$, on obtient donc
$$
J_f(\theta_1, \theta_2)
=
\left[
\begin{array}{rr}
-\ell_1 s_1 -\ell_2 s_{12} & -\ell_2 s_{12} \\
\ell_1 c_1 + \ell_2 c_{12} & \ell_2 c_{12} 
\end{array}
\right].
$$

Différentiation matricielle
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-dm-1}
Soit $H \in \R^{n\times n}$, telle que
$$
H = 
\left[
\begin{array}{cccc}
h_{11} & h_{12} & \hdots & h_{1n} \\
h_{21} & h_{22} & \hdots & h_{2n} \\
\vdots & \vdots & \vdots & \vdots \\
h_{n1} & h_{n2} & \hdots & h_{nn} \\
\end{array} 
\right].
$$
En développant le déterminant selon la première colonne, on constate
que
$$
\begin{split}
\det (I+H) &= 
\left|
\begin{array}{cccc}
1+h_{11} & h_{12} & \hdots & h_{1n} \\
h_{21} & 1+h_{22} & \hdots & h_{2n} \\
\vdots & \vdots & \vdots & \vdots \\
h_{n1} & h_{n2} & \hdots & 1+h_{nn} \\
\end{array} 
\right| \\
&=(1 + h_{11}) 
\left| \begin{array}{ccc}
1+h_{22} & \hdots & h_{2n} \\
\vdots & \vdots & \vdots \\
h_{n2} & \hdots & 1+h_{nn} \\
\end{array} \right| 
+ o(\|H\|), \\
\end{split}
$$
une relation dont on tire par récurrence que
$$
\begin{split}
\det (I+H) 
&= \prod_{i = 1}^n (1 + h_{ii}) + o(\|H\|)
=\det I + \sum_{i=1}^n h_{ii} + o(\|H\|) \\
&= \det I + \tr H + o(\|H\|).
\end{split}
$$
La différentiel du déterminant existe donc en l'identité et 
$d\det(I) \cdot H = \tr H$.

### Question 2 {.answer #answer-dm-2}
Pour tout réel $\varepsilon$ et $A$, $B$ matrices carrées de même taille, on a
$$
\det (I + \varepsilon A B) = \det (I + \varepsilon B A).
$$
Les deux membres de cette équations sont dérivables par rapport à
$\varepsilon$ en $0$ par la règle de différentiation en chaîne 
et l'égalité de ces dérivées fournit
$$
\tr A B = \tr B A.
$$

### Question 3 {.answer #answer-dm-3}
Le déterminant étant une application continue, si $A \in \R^{n\times n}$ 
est suffisamment proche de l'identité -- dont le déterminant vaut $1$ --
son déterminant est positif ; la matrice $A$ est alors inversible.

Quand la matrice $A \in \R^{n \times n}$ est suffisamment proche de l'identité 
pour être inversible, la formule de Cramer établit
$$
A^{-1} = \frac{1}{\det A} \mathrm{co}(A)^t.
$$
Chaque coefficient de $\mathrm{co}(A)^t$ (la transposée de la comatrice
de $A$) est une fonction polynomiale
des coefficients $a_{ij}$ de $A$ ; chaque coefficient de $\mathrm{co}(A)^t$
est donc une fonction continûment différentiable des coefficients de $A$
et donc différentiable en $A=I$.
Par la règle du produit, chaque coefficient de $A^{-1}$ est 
donc différentiable en $A=I$ ; l'application $A \mapsto A^{-1}$ est donc
différentiable en $A=I$.

Notons $\mathrm{inv}(A) = A^{-1}$ ; comme 
$\mathrm{inv}(I+H) = I + d \, \mathrm{inv}(I) \cdot H + o(\|H\|),$
l'identité $(I+ H) (I + H)^{-1} = I$ fournit :
$$
(I+H)(I + d\,\mathrm{inv}(I) \cdot H + o(\|H\|)) 
= I + H + d\,\mathrm{inv}(I) \cdot H + o(\|H\|)
= I,
$$
et donc
$$d \,\mathrm{inv} (I) \cdot H= - H.$$

Dérivée partielles, directionnelles et différentielle
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-dpdd-1}

Les dérivées partielles de la fonction $f:\R^2 \to \R$ définie par
$$
f(x,y) 
= \left|
\begin{array}{cl}
0 & \mbox{si } x=0 \mbox{ ou } y=0, \\
1 & \mbox{sinon.}
\end{array}
\right.
$$
existent en $(0,0)$ et sont nulles, puisque les fonctions partielles associées
sont nulles. Mais $f$ n'est pas continue en l'origine ; 
elle n'y est donc a fortiori pas différentiable.

### Question 2 {.answer #answer-dpdd-2}
Les dérivées directionnelles de la fonction $f:\R^2 \to \R$ définie par
$$
f(x,y) 
= \left|
\begin{array}{cl}
1 & \mbox{si } x > 0 \mbox{ et } y=x^2, \\
0 & \mbox{sinon.}
\end{array}
\right.
$$
existent en $(0,0)$ et sont nulles pour tout $h \in \R^2$, 
puisque les fonctions associées $t \in \R \mapsto f(t h)$
sont nulles pour $|t|$ suffisamment petit.
Mais $f$ n'est pas continue en l'origine ; 
elle n'y est donc a fortiori pas différentiable.

Dérivée directionnelle d'Hadamard
--------------------------------------------------------------------------------

### Question 1 {.answer #answer-ddh-1}
Supposons que $f$ soit directionnellement dérivable au sens de Hadamard
en $x$. Pour tout $h \in \mathbb{R}^n$, par continuité de l'application
$t \in \mathbb{R} \mapsto x + th$, pour $\varepsilon > 0$ assez petit,
et parce que le domaine de définition de $f$ est ouvert,
l'image de la fonction 
$$
\gamma: t \in \left]-\varepsilon, \varepsilon \right[ \mapsto x + th
$$
est incluse dans le domaine de définition de $f$, est telle que
$\gamma(0) = x$, $\gamma'(0) = h$. Par conséquent, la dérivée
de $f\circ \gamma$ en $0$ existe, et c'est par construction la
dérivée directionnelle de $f$ en $x$ dans la direction $h$.
La fonction $f$ est donc directionnellement dérivable en $x$ 
au sens classique.

### Question 2 {.answer #answer-ddh-2}
Supposons que $f$ soit directionnellement dérivable au sens de Hadamard
en $x$. Pour montrer que l'expression $(f \circ \gamma)'(0)$ ne dépend
de $\gamma$ qu'à travers $\gamma'(0)$, nous allons considérer un
second chemin arbitraire $\beta: J \to \mathbb{R}^n$, 
où $J$ est un intervalle ouvert de $\mathbb{R}$ contenant $0$, 
tel que $\beta(0) = x$,
$\beta'(0)=\gamma'(0)$ et montrer que 
$$
(f \circ \gamma)'(0) = (f \circ \beta)'(0).
$$
L'idée de la démonstration consiste à construire un troisième chemin 
$\alpha$ qui en "mélangeant" les chemins $\beta$ et $\gamma$, 
satisfait les hypothèses de la définition de "directionnellement 
dérivable au sens de Hadamard",
est tel que $\alpha'(0) = \beta'(0) = \gamma'(0)$
et également tel que
d'une part $(f \circ \alpha)'(0)= (f \circ \beta)'(0)$ et d'autre 
part $(f \circ \alpha)'(0)=(f \circ \gamma)'(0)$.

Un chemin qui permette de tenir ce raisonnement est le suivant. 
Tout d'abord, choisissons
$\varepsilon > 0$ tel que 
$\left]-\varepsilon, \varepsilon\right[ \subset I \cap J$,
puis définissons $\alpha: \left]-\varepsilon,\varepsilon\right[ \to \mathbb{R}^n$
par
$$
\alpha(t) = \left|
\begin{array}{cl}
x & \mbox{si } \, t=0, \\
\beta(t) & \mbox{si } \, \varepsilon /2^{2k+1} \leq |t| < \varepsilon / 2^{2k}, \, \mbox{pour un entier } \, k \in \mathbb{N}, \\
\gamma(t) & \mbox{si } \, \varepsilon / 2^{2k+2} \leq |t| < \varepsilon / 2^{2k+1},  \, \mbox{pour un entier } \, k \in \mathbb{N}.
\end{array}
\right.
$$
Les hypothèses de la définition sont facilement vérifiées, 
ainsi que la preuve que $\alpha'(0) = \beta'(0) = \gamma'(0)$.
Avec l'hypothèse de différentiabilité au sens de Hadamard, nous
savons donc que la dérivée $(f\circ \alpha)'(0)$ existe.
On peut la calculer comme la limite de
$$
(f \circ \alpha)'(0) = \lim_{k \to +\infty} \frac{f(\alpha(t_k)) - f(x)}{t_n}
$$
où $t_k$ est une suite arbitraire de valeurs non nulles tendant vers $0$.
Or, si l'on choisit $t_k = \varepsilon/2^{2k+1}$, on trouve
$$
\lim_{k \to +\infty} \frac{f(\alpha(t_k)) - f(x)}{t_k}
=
\lim_{k \to +\infty} \frac{f(\beta(t_k)) - f(x)}{t_k}
= (f \circ \beta)'(0)
$$
et si l'on choisit $t_k = \varepsilon/2^{2k+2}$, on trouve
$$
\lim_{k \to +\infty} \frac{f(\alpha(t_k)) - f(x)}{t_k}
=
\lim_{k \to +\infty} \frac{f(\gamma(t_k)) - f(x)}{t_k}
= (f \circ \gamma)'(0),
$$
ce qui prouve le résultat d'indépendance souhaité.
Pour prouver que $(f\circ \gamma)'(0) = f'(x, \gamma'(0))$, 
il suffit d'associer à un chemin quelconque $\gamma$ le
chemin "canonique" $\beta: t \mapsto x+ t\gamma'(0)$ de la question 1,
qui est tel que $\beta'(0) = \gamma'(0)$ d'une part et d'autre part
$(f \circ \beta)'(0) = f'(x, \beta'(0))$ par construction.
On en déduit que
$$
(f \circ \gamma)'(0) = (f \circ \beta)'(0) = f'(x, \beta'(0)) = f'(x, \gamma'(0)).
$$

### Question 3 {.answer #answer-ddh-3}
Soit $\gamma: I \subset \mathbb{R} \to \mathbb{R}^n$,
un chemin défini sur un intervalle ouvert $I$ contenant $0$, 
tel que $\gamma(I) \subset U$,  $\gamma(0) = x$ et $\gamma'(0)$ existe.
Alors, sous les hypothèses du théorème de dérivée en chaîne que nous
souhaitons montrer, le chemin $\beta = f \circ \gamma$ est 
défini sur $I$, vérifie $\beta(I) \subset V$, $\beta(0) = f(x)$ 
et par hypothèse de dérivabilité directionnelle au sens de
Hadamard sur $f$ en $x$,
$\beta'(0) = f'(x, \gamma'(0))$.
Par hypothèse de dérivabilité directionnelle au sens de
Hadamard sur $g$ en $f(x)$, 
$$
((g\circ f) \circ \gamma)'(0) = 
(g \circ \beta)'(0) = g'(f(x), \beta'(0)) = g'(f(x), f'(x, \gamma'(0))),
$$
ce qui prouve la dérivabilité directionnelle au sens de Hadamard pour
la composée $g \circ f$ en $x$. Il suffit d'associer à un vecteur $h$
le chemin canonique $t \mapsto x + th$ pour obtenir la relation
$$
(g \circ f)'(x, h) = g'(f(x), f'(x, h)).
$$

### Question 4 {.answer #answer-ddh-4}
Tout d'abord, si la limite 
$$
\lim_{(t, k) \to (0, h)} \frac{f(x+ t k) - f(x)}{t}
$$
existe, elle est égale à la limite obtenue en fixant $k=h$ 
$$
\lim_{t \to 0} \frac{f(x+ t h) - f(x)}{t}
$$
qui est par définition $f'(x, h)$.

Supposons que cette limite existe et montrons que $f$ a une dérivée
directionnelle au sens de Hadamard.
Soit $\gamma$ un chemin satisfaisant les hypothèses de cette définition.
La fonction $f\circ \gamma$ est dérivable en $0$ si et seulement si
le taux d'accroissement associé converge en $0$. Or, ce taux
d'accroissement peut s'écrire sous la forme
$$
\frac{f(\gamma(t)) - f(\gamma(0))}{t}
=
\frac{f\left(x + t \frac{\gamma(t) - \gamma(0)}{t}\right) - x}{t}.
$$ 
Le chemin $\gamma$ étant dérivable en $0$,
$$
k(t) :=  \frac{\gamma(t) - \gamma(0)}{t} \to \gamma'(0)
\, \mbox{ quand } \, t \to 0
$$
donc par hypothèse, le taux d'accroissement de $f\circ \gamma$ a une
limite en $0$.

Réciproquement, suppose que $f$ soit directionnellement dérivable au
sens de Hadamard en $0$. Pour montrer que la limite 
$$
\lim_{(t, k) \to (0, h)} \frac{f(x+ t k) - f(x)}{t}
$$
existe, il nous suffit de montrer que pour toute suite $t_i$ de valeurs
non nulles tendant vers $0$ et toute suite de vecteurs $k_i$ convergeant
vers $h$, la limite
$$
\lim_{i \to +\infty} \frac{f(x+ t_i k_i) - f(x)}{t_i}
$$
existe. On peut imposer la restriction que la suite $|t_i|$ soit 
strictement décroissante et le résultat reste valable.

Pour tout $t \in \mathbb{R}^*$ notons $j(t)$ le plus
petit parmi les entiers $j$ satisfaisant
$$
|t - t_j| = \min_{i \in \mathbb{N}} |t - t_i|,
$$
puis définissons $\gamma(t)$ par $\gamma(0) = x$ et si $t \neq 0$,
$$
\gamma(t) = x + t k_{j(t)}.
$$
S'il est défini sur un intervalle $\left]-\varepsilon, \varepsilon\right[$
assez petit, $\gamma$ satisfait les hypothèses de la dérivabilité 
directionnelle. Le point critique à vérifier est que $\gamma$ est dérivable
en $0$. Mais par construction
$$
\frac{\gamma(t) - \gamma(0)}{t} = k_{j(t)}
$$
et $j(t)$ tend vers $+\infty$ quand $t$ tend vers $0$; 
par conséquent la limite existe et
$$
\lim_{t \to 0} \frac{\gamma(t) - \gamma(0)}{t} = h.
$$
Par construction
$$
\frac{f(\gamma(t_i)) - f(\gamma(0))}{t_i} = \frac{f(x+ t_i k_i) - f(x)}{t_i}.
$$
Comme la fonction est dérivable directionnellement au sens de 
Hadamard, 
$$
\lim_{i \to +\infty} \frac{f(x+ t_i k_i) - f(x)}{t_i}
$$
existe.

### Question 5 {.answer #answer-ddh-5}
Si $f$ est différentiable au sens de Fréchet, notons $\varepsilon$
la fonction définie dans un voisinage de $0$, continue et nulle en $0$,
telle que
$$
f(x+h) = f(x) + df(x) \cdot h + \varepsilon(h)\|h\|.
$$
On a alors pour tout $t\in \mathbb{R}$ non nul et tout vecteur
$k \in \mathbb{R}^n$ suffisamment petits, en posant $h=tk$, 
$$
\begin{split}
\frac{f(x+ t k) - f(x)}{t}
&= \frac{1}{t}df(x) \cdot tk + \frac{1}{t}\varepsilon(tk) \|tk\| \\
&= df(x) \cdot k + \varepsilon(t k) \frac{|t|}{t} \|k\|.
\end{split}
$$
Le terme $df(x) \cdot k$ tend vers $df(x)\cdot h$ quand $k \to h$
et le second terme du membre de droite tend vers $0$ quand 
$t$ et $k$ tendent vers $0$, donc
$$
\lim_{(t, k) \to (0, h)} \frac{f(x+ t k) - f(x)}{t} = df(x) \cdot h.
$$
Par conséquent la fonction $f$
est directionnellement dérivable au sens de Hadamard.
Le membre de droite, égal à $f'(x, h)$, est linéaire en $h$ ;
la fonction $f$ est donc différentiable au sens de Hadamard.

Réciproquement, supposons que $f$ est différentiable au sens de Hadamard.
Pour montrer que $f$ est différentiable au sens de Fréchet, 
de différentielle $f'(x, h)$, montrons que
$$
\frac{\|f(x+h) - f(x) - f'(x, h)\|}{\|h\|} \to 0 \, \mbox{ quand } \, h \to 0,
$$
ou de façon équivalente, que
$$
\frac{f\left(x+ \|h\|\frac{h}{\|h\|} \right) - f(x)}{\|h\|} - f'\left(x, \frac{h}{\|h\|} \right) \to 0
\, \mbox{ quand } \, h \to 0.
$$
Il nous suffit de montrer que pour toute suite $t_i > 0$ telle
que $t_i \to 0$ quand $i \to +\infty$ et 
$k_i \in \mathbb{R}^n$ telle que $\|k_i\| = 1$,
$$
\frac{f\left(x+ t_i k_i \right) - f(x)}{t_i} - f'\left(x, k_i \right) \to 0
\, \mbox{ quand } \, i \to +\infty.
$$
Imaginons au contraire que cette expression ne tende pas vers $0$.
Alors on pourrait trouver un $\varepsilon > 0$ et une sous-suite de 
$(t_i, k_i)$, notée de $(t'_i, k'_i)$, telle que pour tout $i$,
$$
\left\|
\frac{f \left(x+ t'_i k'_i \right) - f(x)}{t'_i} - f'\left(x, k'_i \right)
\right\| \geq \varepsilon.
$$
Mais la suite des $k'_i$ est de norme égale à $1$ ;
la sphère fermée de centre $1$ étant compacte, il existe des sous-suites
$t''_i$ et $k''_i$ de $t'_i$ et $k'_i$ et un $h \in \mathbb{R}^n$ tels que
$\|h\| = 1$ et
$k''_i \to h$. 
Par hypothèse de dérivabilité au sens de Hadamard,
on aurait
$$
\frac{f\left(x+ t''_i k''_i \right) - f(x)}{t''_i} \to f'\left(x, h\right)
\, \mbox{ quand } \, i \to +\infty
$$
ce qui contredit l'inégalité ci-dessus et prouve la contradiction.
Par conséquent, $f$ est bien différentiable au sens de Fréchet.

Inégalité de la valeur moyenne {.answer #answer-ivm}
--------------------------------------------------------------------------------

Soit $F:[a, b] \to \R^m$ une primitive de $f$. 
Par [définition de l'intégrale de Newton](#intégrale-Newton),
$$
\left<f\right> = \frac{1}{b-a} \int_a^b f(x) \, dx
= \frac{F(b) - F(a)}{b-a}.
$$
Or si $\|F'\| = \|f\|$ est borné sur $[a, b]$, par 
[le théorème des accroissements finis](#TAFS),
$$
\|F(b) - F(a)\| \leq \sup_{x \in [a, b]} \|f(x)\| \times  (b-a),
$$
et donc
$$
\left\|\left<f\right>\right\| \leq  \sup_{x \in [a, b]} \|f(x)\|.
$$
Il va de soi que cette inégalité reste vérifiée si $\|f\|$ est non-bornée,
c'est-à-dire si $\sup_{x \in [a, b]} \|f(x)\| = +\infty$.

Egalité des accroissements finis ? {.answer #answer-eaf}
--------------------------------------------------------------------------------

La dérivée de $f$ est donnée par $f'(t) = (-\sin t, \cos t)$; 
en particulier pour tout $t \in [0, 2\pi]$, $\|f'(t)\| = 1$.
Or $f(2\pi) - f(0) = 0$, donc il est impossible de trouver un 
$t$ tel que $f(2\pi) - f(0) = f'(t) \times 2\pi$.

Convexité
--------------------------------------------------------------------------------

### Question 0 {.answer #answer-c-0}
[Le développement limité à l'ordre 2 de $f$ en $x$](#dl) fournit
$$
f(x+h) = f(x) + df(x) \cdot h + \frac{d^2f(x)}{2} (\cdot h)^2 + o(\|h\|^2)
$$
et donc
$$
f(x+2h) = f(x) + 2 df(x) \cdot h + 4 \frac{d^2f(x)}{2} (\cdot h)^2 + o(\|h\|^2).
$$
Par conséquent,
$$
f(x+2h) - 2 f(x+h) + f(x) = d^2 f(x) (\cdot h)^2 + o(\|h\|^2).
$$

### Question 1 {.answer #answer-c-1}
En considérant $y = x+2h$ et $\lambda = 1/2$, on voit que l'hypothèse
de convexité de $f$ entraîne 
$$
f(x+h) \leq \frac{1}{2} f(x) + \frac{1}{2} f(x+2h),
$$
soit $$f(x+2h) - 2 f(x+h) - f(x) \geq 0.$$
En utilisant le résultat de la question précédente,
on obtient
$$d^2 f(x) (\cdot h)^2 + o(\|h\|^2) \geq 0$$ et donc, en substituant 
$th$ à $h$ et en faisant tendre $t$ vers $0$, 
$d^2 f(x) (\cdot h)^2 \geq 0.$

### Question 2 {.answer #answer-c-2}
Comme $f((1-\lambda) x + \lambda y) = f(x + \lambda (y-x))$,
l'inégalité de Taylor avec reste intégral fournit 
$$
\begin{split}
f((1-\lambda) x + \lambda y)
&= f(x) + df(x) \cdot \lambda (y-x) \\
&\phantom{=} + \int_0^1 d^2f(x+ t\lambda (y-x)) (\cdot \lambda(y-x))^2 (1- t) \, dt.
\end{split}
$$
L'intégrale ci-dessus étant égale à 
$$
\lambda \int_0^1 d^2f(x+ t\lambda (y-x)) (\cdot (y-x))^2 
\left(1- \frac{ \lambda t}{\lambda} \right) \, \ \lambda dt,
$$
par le changement de variable $t \lambda \to t$ elle est égale à
$$
\lambda \int_0^{\lambda} d^2f(x+ t (y-x)) (\cdot (y-x))^2 
\left(1 - \frac{t}{\lambda} \right)\, dt.
$$
En utilisant le développement de Taylor avec reste intégral pour
$\lambda \in \left]0, 1\right]$ et $\lambda=1$, on obtient donc
$$
\begin{split}
f((1-\lambda) x + \lambda y) - \lambda f(y)
&= f(x) - \lambda f(x) + df(x) \cdot \lambda (y-x) - \lambda df(x) \cdot (y-x) \\
&\phantom{=} + \lambda \int_0^{\lambda} d^2f(x+ t (y-x)) (\cdot (y-x))^2  \left(1 - \frac{t}{\lambda} \right)\, dt
\\
&\phantom{=} - \lambda \int_0^{1} d^2f(x+ t (y-x)) (\cdot (y-x))^2 
\left(1 - t \right)\, dt,
\end{split}
$$
soit 
$$
f((1-\lambda) x + \lambda y) - \lambda f(y)
- (1 - \lambda) f(x) 
=\lambda \int_0^1 \phi_f(t) \psi_{\lambda} (t) \, dt
$$
où
$\phi_f(t) := d^2f(x+ t (y-x)) (\cdot (y-x))^2$ est positive par hypothèse et 
$$
\psi_{\lambda}(t) :=
\left|
\begin{array}{cc}
t(1 - 1/\lambda) & \mbox{si } t \leq \lambda\\
(t - 1) & \mbox{sinon.}
\end{array}
\right.
$$
La fonction $\psi_{\lambda}$ étant négative, on en conclut que
$f((1-\lambda) x + \lambda y) - \lambda f(y) - f(x)$ est négative pour tout
$\lambda \in \left]0, 1\right]$ ; cette inégalité est également trivialement
satisfaite si $\lambda=0$. La fonction $f$ est donc convexe.

<!--
TODO -- Analycité
--------------------------------------------------------------------------------
-->


<!--

TODO -- Oloid
--------------------------------------------------------------------------------
-->

Références
================================================================================

