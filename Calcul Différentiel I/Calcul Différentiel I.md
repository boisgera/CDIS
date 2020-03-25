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
    de définir la différentielle en passant par cles dérivée partielles:
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

<!--
TODO
================================================================================

Changelog :

  - Supression intégrale de Newton

  - Forme classique du théorème fondamental du calcul (avec hypothèse
    d'intégrabilité de $f'$).

TODO :

  - **Supression annexe intégrale de Newton. 
    Réviser résultat Théo fondamental du
    calcul et variation d'une fonction pour se limiter à des fonctions 
    "intégrables".** Préciser éventuellement dans une remarque (ou pas)
    que les résultats sont vrais sans hypothèse supplémentaire.
    Ca peut prendre la forme suivante : énoncer le résultat, PUIS expliquer
    qu'on peut comprendre "intégrable" comme "Riemann-intégrable" ou
    (ou même "continue par morceaux")
    ou "Lebesgue-intégrable" ou même HK-intégrable (hors-programme).  
    Le cas HK-intégrable est nécessaire pour prouver le théorème des
    accroissements finis et uniquement là ; la réference à "TFC vrai pour HK"
    pourrait même être locale et donc se limiter à cette preuve pour ne pas 
    compliquer le texte. A voir ...
    Bref, propager les conséquences de ce changement.

  - **Atténuer différence applis lin / matrices.** Dans les notations, etc.
    "Incarner" beaucoup plutôt les choses dans des matrices pour que 
    l'interprétation concrête soit toujours possible (tout est "calculable"
    à chaque étape), accepter en contrepartie qu'une notation soit (un peu) 
    ambigue dans son interprétation. Du coup, notation unique,
    par exemple $D f(x)$ pour désigner aussi bien la matrice jacobienne que
    la différentielle ? Y réfléchir, mais ça semble raisonnable ...
    Il est toujours possible de distinguer les objets en introduisant 
    $df(x)$ et $J_f(x)$ a posteriori  si besoin (mais si c'est vraiment le
    cas, c'est un échec non ?). De toute façon, il sera nécessaire d'expliquer
    pourquoi on peut écrire / comment interpréter $Dg(y) Df(x)$ vs
    $Dg(y) \cdot Df(x)$ vs $Dg(y) \circ Df(x)$.

    Ou conserver la notation $df(x)$ pour la matrice également ?
    On a envie de pouvoir conserver les identités comme $dx^2 = 2x dx$ ...

  - **Commencer par les dérivées partielles, insister sur le cadre $C^1$**.
    Passer de la dérivée aux dérivées partielles (sur un point intérieur du
    domaine), puis définir le gradient, la matrice jacobienne. 
    Dire qu'une fonction est différentiable en un point si la matrice 
    jacobienne de $f$ en $x$ fournit une approximation au 1er ordre de $f(x+h)$,
    c'est-à-dire si 
    $$
    f(x+h) = f(x) + Df(x) \cdot h + o(\|h\|)
    $$
    et qu'alors on appelle différentielle l'application de $f$ en $x$ 
    l'application linéaire $h \mapsto Df(x) \cdot h$ -- ou "$Df(x)$".
    (A noter que l'on peut faire l'impasse sur l'unicité de l'opérateur
    ainsi défini et que l'on n'a pas *a posteriori* à découvrir comment
    il est lié à la matrice jacobienne ; mais cela peut faire l'objet d'un
    exercice embarqué à cet endroit.)
    Exemples bien choisi pour montrer que ce développement au 1er ordre
    n'existe pas forcément même si la matrice jacobienne est bien définie. 

    La qualification de "continûment différentiable" est alors définie 
    comme la continuité de
    l'application $x \mapsto Df(x) \in \mathbb{R}^{n \times n}$.
    Que continûment différentiable implique différentiable est un théorème
    (facile à retenir avec la terminologie choisie).

  - Renvoyer en annexe les rappels d'algèbre linéaire (matrices,
    et applications linéaires, vecteurs, etc.). Puis la simplifier
    (notamment, les notations sur les applications linéaires).

  - TODO: renvoyer dérivée en annexe (y compris dérivée à droite et à gauche 
    dans un style extension sur ouvert ?)


\newpage
-->

Introduction
================================================================================

Objectifs d'apprentissage
--------------------------------------------------------------------------------

### Rappel dérivées ?

TODO

### Matrice jacobienne et différentielle

Dérivée permet de traiter fcts à valeurs scalaires ou vectorielles d'une variable.
L'objet généralisant la dérivée dans le cas multivariable

  - connaître définition dérivées partielles, Jacobien, gradient, etc. 

Toutefois, l'existence du Jacobien est en général insuffisante (? détailler ?) ;
elle ne suffit pas à garantir l'existence d'un dvlpt au 1er ordre. La façon
la plus simple de pallier à ça est de réquérir la continue diff

  - def continue diff, existence dvlpt 1er ordre

Dans le cas où l'on ne dispose pas de la cont diff, l'existence d'un dvlpt 
au 1er ordre peut suffire ; ce cas un peu plus subtil est suffisamment important
pour justifier une terminologie propre

  - def différentiabilité, lien avec continue diff.

### Calcul différentiel :

  - différentielle à partir des dérivées partielles

  - différentielle d'une application linéaire

  - règle de différentiation en chaîne

  - dérivées partielles et variables nommées

  - différentielles d'expression et de variables.

### Variation des fonctions :

TODO : savoir faire les preuves dans les cas simple continûment diff
(th fondam du calcul et inég acc finis ?)

  - théorème fondamental du calcul, forme monovariable
  
  - thé fond du calcul, forme multivariable. 
  
  - savoir la dériver et "adapter la preuve" le cas échéant.

  - connaitre i acc fini mono et multi-variable (cas euclidien)

  - savoir dériver l'inégalité des accroissements finis du théorème fondamental
    du calcul sous une hypothèse supplémentaire de régularité renforcée.

  - comprendre / savoir exploiter i acc fini avec autres normes que la norme
    euclidienne.


Conventions
--------------------------------------------------------------------------------

Un vecteur $x = (x_1, \dots, x_n) \in \R^n$
sera implicitement identifié, dans le contexte d'un calcul matriciel, 
au vecteur colonne
$$
\left[ \begin{array}{c}
x_1 \\
\vdots \\
x_n
\end{array}
\right] \in \R^{n \times 1}.
$$
Une application linéaire $A: \R^m \to \R^n$, sera quant à elle
implicitement identifiée avec la matrice à $m$ lignes et $n$ colonnes
représentant l'application linéaire dans les bases canoniques de 
$\R^m$ et $\R^n$
$$
\left[ 
\begin{array}{ccccc}
a_{11} & a_{12} & \cdots & a_{1n} \\
\vdots & \vdots & \vdots & \vdots\\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{array}
\right] \in \mathbb{R}^{m \times n}.
$$

Dans ce document, nous utiliserons le point "$\cdot$" pour 
désigner le produit entre matrices. Les identifications que nous venons
d'exposer nous incitent donc également à noter $A \cdot x$ l'image du vecteur $x$ 
par l'application linéaire $A$ et $A \cdot B$ la composition des 
applications linéaires $B$ par $A$. 

Sauf mention contraire, $\|x\|$ désignera
la norme euclidienne $\|x\|_2$ de $x$ dans $\R^n$ ;  
$\|A\|$ désignera la norme d'opérateur $\|A\|_{22}$ de $A$, 
induite par les normes euclidiennes sur $\R^m$ et sur $\R^n$.


Matrice jacobienne et différentielle
================================================================================

### Dérivée {.definition .zero}
Soient $U$ un ouvert de $\R$, $f: U \to \mathbb{R}^m$ et $x \in U$.
La fonction $f$ est *dérivable en $x$* si la limite du 
*taux d'accroissement* de $f$ en $x$ existe ; 
cette limite est appelée *dérivée de $f$ en $x$* 
et notée $f'(x)$ :
$$
f'(x) := \lim_{\substack{h \to 0 \\ h \neq 0}} \frac{f(x+h) - f(x)}{h}.
$$
La fonction $f$ est *dérivable (sur $U$)* si elle est dérivable en tout point
$x$ de $U$.

### {.post .remark}
Cette définition couvre le cas où la fonction $f$ est définie est sur un 
intervalle ouvert $\left]a, b\right[$, mais pas sur un intervalle fermé et 
borné $[a, b]$. Pour traiter ce cas, on peut introduire les notions de dérivées 
à gauche et à droite.

### Dérivée sur un intervalle fermé et borné {.definition .zero}
Soient $a, b \in \R$ avec $a < b$ et $f: [a, b] \to \mathbb{R}^m$.
La fonction $f$ est *dérivable sur $[a, b]$* 
si elle est dérivable sur l'intervalle ouvert $\left]a, b\right[$ 
et que les dérivées de $f$ à droite en $a$ et à gauche en $b$ existent.
On pose alors
$$
f'(a) := \lim_{\substack{h \to 0 \\ h > 0}} \frac{f(a+h) - f(a)}{h}
\; \mbox{ et } \;
f'(b) := \lim_{\substack{h \to 0 \\ h < 0}} \frac{f(b+h) - f(b)}{h}.
$$

### {.remark}
Il est aussi possible d'utiliser une pirouette pour se ramener à un domaine
de définition ouvert. Cela nous sera utile pour intégrer les dérivées 
au calcul différentiel multivariable qui ne sera développé que 
pour des domaine de définition ouverts.

### Dérivée et prolongement {.proposition .one}
Soient $a, b \in \R$ avec $a < b$ et $f: [a, b] \to \mathbb{R}^m$.
La fonction $f$ est dérivable sur $[a, b]$ si et seulement si elle admet un 
prolongement $g$ à un ensemble ouvert $U$ de $\R$ contenant $[a, b]$ qui soit 
dérivable. Si c'est le cas, sa dérivée $f'$ est égale à la restriction 
de la fonction $g'$ à $[a, b]$.

\newcommand{\lb}{\left]}
\newcommand{\rb}{\right[}

![Un prolongement dérivable de $f:x \in [0,1] \mapsto e^{-x}$ à $\lb-0.5, 1.5 \rb$.
Ce prolongement $g$ est défini par 
$g(x) = 1 - x$ si $x < 0$ et $g(x) = (2-x)/e$ si $x>1$.](images/prolongement.tex)

### Dérivées à gauche et à droite {.exercise .question}
Montrer que la ... **TODO** Exo démo résult précédent


### Dérivée et développement limité  {.proposition .zero}
Soient $U$ un ouvert de $\R$, $f: U \to \mathbb{R}^m$ et $x \in U$.
Si la fonction $f$ est dérivable en $x$, alors dans un voisinage de $x$
on a
$$
f(x+h) = f(x) + f'(x) h + \varepsilon(h)|h|
$$
où la fonction $\varepsilon$, définie dans un voisinage de $h=0$, 
est telle que 
$$
\lim_{h \to 0}\varepsilon(h) = 0.
$$

###  Dérivée et développement limité (réciproque)  {.proposition .one}
Soient $U$ un ouvert de $\R$, $f: U \to \mathbb{R}^m$ et $x \in U$.
S'il existe un $\ell \in \R^m$ tel que
$$
f(x+h) = f(x) + \ell h + \varepsilon(h)|h|
$$
alors $f$ est dérivable en $x$ et $f'(x) = \ell$.

### Dérivées partielles {.definition .one}
Soient $U$ un ouvert de $\R^n$, $f: U \to \mathbb{R}^m$ et 
$x=(x_1, \cdots, x_n) \in U$. Lorsque la $j$-ème fonction partielle de $f$
$$
y_j \mapsto f(x_1, \cdots, x_{j-1}, y_j, x_{j+1}, \cdots, x_n)
$$
est dérivable en $y_j = x_j$, on appelle $j$-ème *dérivée partielle
de $f$ en $x$*
et on note $\partial_j f(x) \in \mathbb{R}^m$ sa dérivée.
$$
\partial_j f(x) := \left(y_j \mapsto f(x_1, \cdots, x_{j-1}, y_j, x_{j+1}, \cdots, x_n)\right)'(x_j)
$$
Alternativement,
$$
\begin{split}
\partial_j f(x)
&:= \lim_{t \to 0} \frac{f(x + t e_j) - f(x)}{t} \\
&\phantom{:}= \lim_{t \to 0} \frac{f(x_1, \dots, x_j + t, \dots, x_n) - f(x_1, \dots, x_n)}{t}. 
\end{split}
$$

### Matrice jacobienne {.definition .one}
Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}^m$ et
$x$ un point de $U$. Soient $f_i$ les fonctions scalaires composant $f$, 
c'est-à-dire telles que
$f(x) = (f_1(x), \dots, f_m(x)).$
Si toutes les dérivées partielles des fonctions $f_i$ existent en $x$,
on définit la *matrice jacobienne de $f$ en $x$*, notée $f'(x)$, comme
la matrice de $\R^{m \times n}$ telle que
$$
[J_f(x)]_{ij} = \partial_{j} f_i(x),
$$
c'est-à-dire
$$
J_f(x) =
\left[
\begin{array}{cccc}
\partial_1 f_1 (x) & \partial_2 f_1 (x) & \cdots & \partial_n f_1 (x) \\
\partial_1 f_2 (x) & \partial_2 f_2 (x) & \cdots & \partial_n f_2 (x) \\
\vdots & \vdots & \vdots & \vdots \\
\partial_1 f_m (x) & \partial_2 f_m (x) & \cdots & \partial_n f_m (x) \\
\end{array}
\right]
$$

### TODO

$J_f(x)$ en fonction des vecteurs $\partial_i f(x)$ (exo).

### Gradient {.definition .one}
Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}$ et
$x$ un point de $U$. Si toutes les dérivées partielles de $f$ existent en $x$,
on appelle *gradient de $f$ en $x$* et l'on note $\nabla f(x)$ le vecteur
de $\R^n$ défini comme la transposée de la matrice jacobienne de $f$ en $x$ :
$$
\nabla f(x) := J_f(x)^{\top} = 
\left[ 
\begin{array}{c}
\partial_1 f(x) \\
\partial_2 f(x) \\
\vdots \\
\partial_n f(x)
\end{array}
\right].
$$


### TODO. Calcul élémentaires mat jac & gradient.

### TODO 

mat jacobienne à partir des gradients de $f_i$

<!--
### Petit o de Landau {.definition .three}
Dans ce document, la notation $o(g(h))$ désigne une expression 
de la forme
$$
o(g(h)) := \varepsilon(h) g(h) \in \R^m
$$
où $g et $\varepsilon$ sont des fonctions définies dans un voisinage $V$ 
de $h=0$, $g$ est scalaire, $\varepsilon$ est à valeurs dans $\R^m$ et
$$
\lim_{h \to 0} \varepsilon(h) = \varepsilon(0) = 0.
$$
En particulier, un "petit o de $1$" désigne une expression de la forme
$$
o(1) := \varepsilon(h)
$$
et un "petit o de $\|h\|$" fait référence à
$$
o(\|h\|) := \varepsilon(h) \|h\| = o(1) \|h\|.
$$
-->

### {.remark}
En l'absence d'information supplémentaire, l'existence de la matrice jacobienne
en $x$ offre très peu de garanties de régularité sur $f$ en $x$. 
Il est ainsi possible que la fonction $f$ ne soit pas même pas continue en $x$. 
(On rappelle que pour les fonctions d'une variable, l'existence de
la dérivée en un point implique la continuité en ce point.)

### Fonction discontinue {.exercise .one #discont}
Exhiber une fonction $f: \R^2 \to \R$ dont le gradient existe en $(0,0)$
mais qui soit discontinue en $(0,0)$.

### {.remark}
Une façon simple de renforcer la régularité de la fonction $f$ est d'exiger
qu'elle soit continûment différentiable :

### Continue différentiabilité {.definition .one #cdiff}
Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}^m$ et
$x$ un point de $U$.
La fonction $f$ est *continûment différentiable*
si pour tout $i \in \{1,\dots, m\}$
et $j \in \{1,\dots, n\}$, la dérivée partielle
$$
x \in U \mapsto \partial_j f_i(x) \in \R
$$
est définie et continue en tout point de $U$.

### Continue différentiabilité -- définitions équivalentes {.post .two .remark}
Cette définition de la continue différentiabilité est probablement la plus 
élémentaire. 
Mais de façon équivalente, la fonction $f$ est continûment différentiable si 
(et seulement si) les dérivées partielles
$x \in U \mapsto \partial_j f(x) \in \R^m$
sont définies et continues pour tout $i \in \{1, \dots, m\}$
ou encore si la fonction $x \in U \mapsto J_f(x) \in \R^{m \times n}$
est définie et continue.

### {.remark}
La continue différentiabilité implique l'existence d'un développement au
premier ordre en tout point :

### Existence d'un développement limité au 1er ordre {.proposition .two #dl1}
Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}^m$ et
$x$ un point de $U$.
Si $f$ est continûment différentiable alors $f(x+h)$ admet le développement 
limité au 1er ordre $h \mapsto f(x) + f'(x) \cdot h$, c'est-à-dire qu'il
existe sur un voisinage de $h=0$ une fonction
$\varepsilon$ à valeurs dans $\R^m$ vérifiant
$\lim_{h \to 0} \varepsilon(h) = 0$
telle que 
$$
f(x+h) = f(x) + f'(x) \cdot h + \varepsilon(h) \|h\|.
$$

### Démonstration {.proof} 
Supposons $f: U \subset \R^m \to \R^n$ continûment différentiable.
Soit $x \in U$ et $r>0$ telle que la boule fermée centrée en $x$ 
et de rayon $r$ soit incluse dans $U$
$$
\overline{B}(x, r) =
\{y \in \R^n \; | \; \|y - x\| \leq r\} \subset U
$$
et soit $h \in \R^n$ tel que $\|h\| \leq r$. 
La variation de $f$ entre $x$ et $x+h$ satisfait
\begin{multline*}
f(x+h) - f(x) = \\ 
\sum_{i=1}^n f(x+(h_1, \dots,h_{i-1}, h_i, 0, \dots)) - f(x + (h_1, \dots, h_{i-1}, 0, 0, \dots)). 
\end{multline*}

![Ligne brisée joignant $x$ et $x+h$.](images/cont-diff.tex){#cont-diff}

Or comme pour tout $i$ la fonction
$$t \in [0,1] \mapsto f(x+(h_1, \dots, th_i, 0, \dots))$$
est dérivable de dérivée
$\partial_i f(x+(h_1, \dots, th_i, 0, \dots)) h_i$ et que cette expression
est une fonction continue -- et donc intégrable -- de la variable $t$, 
par [le théorème fondamental du calcul](#TFC), on obtient
\begin{multline*}
f(x+(h_1, \dots, h_{i-1},h_i, 0, \dots)) - f(x + (h_1, \dots, h_{i-1}, 0, 0, \dots)) = \\
h_i \int_0^1 \partial_i f(x+(h_1, \dots, h_{i-1}, th_i, 0, \dots)) \, dt.
\end{multline*}
Par ailleurs, comme
$$
f'(x) \cdot h =
\sum_{i=1}^n \partial_i f(x) h_i
=
\sum_{i=1}^n h_i \int_0^1 \partial_i f(x) \, dt,
$$
on a 
\begin{multline*}
f(x+h) - f(x) - \sum_i \partial_i f(x) h_i = \\
\sum_{i=1}^n h_i \int_0^1 \left[\partial_i f(x+(h_1, \dots, h_{i-1}, th_i, 0, \dots)) - \partial_i f(x) \right] \, dt. 
\end{multline*}
Par continuité des dérivées partielles en $x$, si $r$ est choisi suffisamment 
petit pour que $\|\partial_i f(y) - \partial_i f(x)\| \leq \varepsilon / n$ 
quand $\|y-x\| \leq r$, alors l'inégalité triangulaire
fournit
\begin{multline*}
\left\|\int_0^1 \left[\partial_i f(x+(h_1, \dots, h_{i-1}, th_i, 0, \dots)) - \partial_i f(x) \right] \, dt \right\| \leq \\
\int_0^1 \left\|\partial_i f(x+(h_1, \dots, h_{i-1}, th_i, 0, \dots)) - \partial_i f(x) \right\| \, dt \leq \varepsilon/n
\end{multline*}
et donc, toujours par inégalité triangulaire, comme $|h_i| \leq \|h\|$,
$$
\left\|f(x+h) - f(x) - \sum_{i=1}^n \partial_i f(x) h_i \right\|
\leq
\sum_{i=1}^n |h_i| {\varepsilon}/{n}
\leq \varepsilon \|h\|.
$$
La fonction $f$ admet donc un dévelopement limité au 1er ordre en $x$.

### {.remark}
On qualifiera *différentiable* une fonction admettant ce développement 
au premier ordre. La différentiabilité est la transposition naturelle 
du concept de dérivabilité aux fonctions de plusieurs variables :
pour jouer ce rôle, l'existence du jacobien est une propriété trop faible 
et la continue différentiabilité est une propriété trop forte.

### Différentiabilité {.definition .three}
Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}^m$ et
$x$ un point de $U$. 
On dit que $f$ est *différentiable en $x$* si la matrice jacobienne de $f$ en
$x$ existe et que $f(x+h)$ admet le développement limité
au 1er ordre $h \mapsto f(x) + J_f(x) \cdot h$ : il existe
sur un voisinage de $h=0$ une fonction
$\varepsilon$ à valeurs dans $\R^m$ vérifiant $\lim_{h \to 0} \varepsilon(h) = 0$
telle que 
$$
f(x+h) = f(x) + J_f(x) \cdot h + \varepsilon(h) \|h\|.
$$
On dit que $f$ est *différentiable* (ou *différentiable sur $U$*)
si elle est différentiable en tout point $x$ de $U$.

### {.remark}
[L'existence d'un développement limité au 1er ordre pour les fonctions continûment
différentiables](#dl1) se reformule alors comme suit : 

### Continue différentiabilité implique différentiabilité {.proposition .one #cdid}
Soient $U$ un ouvert de $\mathbb{R}^n$ et $f: U \to \mathbb{R}^m$.
Si $f$ est continûment différentiable, $f$ est différentiable.

**TODO.** diff implique cont

**TODO** dérivées directionnelles ?

<!--
### Convention de Landau {.definition .four}
Toute fonction $\varepsilon : V \subset \R^n \mapsto \R^m$ définie sur 
un voisinage de $0 \in \R^n$ telle que 
$$
\lim_{h \to 0} \varepsilon(h) = \varepsilon(0) = 0
$$
est appelée "un $o(1)$", ce que l'on note $\varepsilon(h)  = o(1)$.
La fonction $h \in V \mapsto \varepsilon(h)\|h\|$ est un $o(h)$
$\varepsilon(h)\|h\| = o(h)$.
-->

### TODO -- cas monovariable (dérivabilité équiv diff)

### Fonctions affines {.exercise .question #fa .one}
Soit $A \in \R^{m\times n}$ et $b \in \R^m$. 
Calculer la matrice jacobienne de la fonction $f:\R^n \to \R^m$ définie par 
$f(x) = A \cdot x + b$ et montrer que cette fonction est différentiable.

### {.remark}
L'existence de la matrice jacobienne de $f$ en $x$ ne garantit pas
l'existence d'un développement au premier ordre de $f$ en $x$.
Par contre, si un tel développement existe, il est nécessairement
obtenu à partir de la matrice jacobienne comme le montre l'exercice suivant.

### Développement limité au premier ordre {.exercise .question #dlmj .two}
Montrer que si 
$A \in \R^{m \times n}$ vérifie dans un voisinage de $h=0$
$$
f(x+h) = f(x) + A \cdot h + \varepsilon(h) \|h\|
$$
avec $\lim_{h \to 0} \varepsilon(h) =  0$
alors la matrice jacobienne $J_f(x)$ est bien définie et $J_f(x) = A$.

### Différentielle {.definition .two}
Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}^m$ et
$x$ un point de $U$. 
Si $f$ est différentiable en $x$ on appelle alors *différentielle de $f$ en $x$* 
l'application linéaire 
$df(x)$ associée à la matrice jacobienne 
$$
df(x) := \left(h \in \R^n \mapsto J_f(x) \cdot h \in \R^m \right)
$$
soit l'application caractérisée pour tout $h \in \R^n$ par
$$
df(x) \cdot h = \sum_{i=1}^n \partial_i f(x) h_i.
$$
Si l'on identifie applications linéaires et matrices, la différentielle
en vient à désigner la matrice jacobienne elle-même :
$$
df(x) = J_f(x).
$$

### TODO

Un mot sur ce que le terme $df(x) \cdot h$ (et ses composants) *représente* :
un approximation (au premier ordre) de la variation de $f$ en $x$ quand 
l'argument varie de $h$.

### Différentiabilité {.two .exercise}
Montrer que $f$ est différentiable en $x$ si et seulement si $J_f(x)$ est bien
définie et que
$$
\lim_{\substack{h \to 0 \\ h\neq 0}} \left(\frac{f(x+h) - f(x)}{\|h\|} - J_f(x) \cdot \frac{h}{\|h\|}\right) = 0.
$$



### TODO
Diff implique cont, existence des dérivées directionnelles et expression.




### Fonction quadratique {.question #fq .exercise .two}
Soit $A \in \R^{n \times n}$. En utilisant les liens entre continue 
différentiabilité et différentiabilité, montrer que la fonction 
$$
f : x \in \R^n \mapsto x^{\top} \cdot A \cdot x
$$
est différentiable et déterminer l'application $df(x)$.

### TODO : exo diff produit scalaire

Calcul Différentiel
================================================================================

### Différentielle d'une application linéaire {.theorem #dal .one}
Toute application linéaire $A: \R^n \to \R^m$ est
différentiable et pour tout $x \in \R^n$,
$$
dA(x) = A.
$$

### Démonstration {.proof}
Pour tout $x \in \R^n$, la $i$-ème composante de la fonction $A$ en $x$ est 
donnée par 
$(A \cdot x)_i = \sum_{k=1}^n A_{ik} x_k$,
donc sa $j$-ème dérivée partielle existe et
$$
\partial_j (x \mapsto A \cdot x)_i(x) = \partial_j \left(x \mapsto \sum_{k=1}^n A_{ik} x_k \right)(x)
= A_{ij}.
$$
La matrice jacobienne $J_A(x)$ est donc définie et $J_A(x) = A$.
Chaque coefficient de $J_A$ est une constante et donc une fonction continue de
$x$ : la fonction $A$ est [continûment différentiable -- et donc
différentiable](#cdid) -- et $dA(x) = J_A(x) = A$.

### TODO
Expliquer que fondamentalement, calcul = composition de fonctions.

### Règle de différentiation en chaîne {.theorem #chain-rule .two}
Soit $f: U \subset \mathbb{R}^p \to \mathbb{R}^{n}$ et 
$g: V \subset \mathbb{R}^n \to \mathbb{R}^{m}$ deux fonctions définies
sur des ouverts $U$ et $V$ et telles que $f(U) \subset V$. 
Si $f$ est différentiable en $x \in U$ et $g$ est différentiable en $f(x) \in V$,
alors la composée $g \circ f$ est différentiable en $x$ et
$$
d(g \circ f)(x) = dg(y) \cdot df(x) \; \mbox{ où } \; y = f(x).
$$

### Démonstration {.proof}
L'objectif de la preuve est de montrer que dans un voisinage de $h=0$,
$$
g(f(x+h)) - g(f(x)) =  (dg(f(x)) \cdot df(x)) \cdot h + \varepsilon(h)\|h\|
$$
où $\lim_{h \to 0} \varepsilon(h) = 0$.
La fonction $g$ étant différentiable en $f(x)$, il existe une fonction
$\varepsilon_1$ définie dans un voisinage de $0$ et telle que
$\lim_{h \to 0} \varepsilon_1(h) = 0$, 
vérifiant
$$
g(f(x)+k) - g(f(x)) = dg(f(x)) \cdot k + \varepsilon_1(k) \|k\|.
$$
Choisissons $k=f(x+h) - f(x)$ dans cette équation, de telle sorte que
$$
g(f(x)+k) = g\left(f(x) + (f(x+h) - f(x))\right) = g(f(x+h)).
$$
Nous obtenons donc
$$
g(f(x+h)) - g(f(x)) = dg(f(x)) \cdot (f(x+h)-f(x)) + \varepsilon_1(k) \|k\|.
$$

Notons que la fonction $\varepsilon_2(h) := \varepsilon_1(f(x+h) - f(x))$
est définie dans un voisinage de $0$ et que par continuité de $f$ en 
$x$, $f(x+h) - f(x)$ tend vers $0$ quand $h$ tend vers $0$, et par conséquent
$\varepsilon_2(h) \to 0$ quand $h\to 0$.
Avec cette notation, on a
$$
\begin{split}
g(f(x+h)) - g(f(x)) &= dg(f(x)) \cdot (f(x+h)-f(x)) \\
                    &\phantom{=} + \varepsilon_2(h) \|f(x+h)-f(x)\|.
\end{split}
$$
Comme $f$ est également différentiable en $x$, il existe une fonction 
$\varepsilon_3$ définie dans un voisinage de $0$ et telle que
$\lim_{h \to 0} \varepsilon(h) = 0$ vérifiant
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

### Composition de fonctions continûment différentiables {.exercise #cfcd .question .one}
Montrer que si dans [l'énoncé de la règle de différentiation en chaîne](#chain-rule) 
les fonctions $f$ et $g$ sont continûment différentiables, alors $g \circ f$
l'est également.

### TODO -- Existence d'une dérivée directionnelle (exo)

Notations compactes
--------------------------------------------------------------------------------

En tant que client du calcul différentiel (comme physicien par exemple) 
vous avez peut-être été exposé à des notations assez éloignées de celles 
que nous avons pratiqué jusqu'à présent. Au coeur de ces notations,
on trouve une formule du type
$$
d (f(x_1, \dots, x_n)) = \frac{\partial f(x_1,\dots, x_n)}{\partial x_1} d x_1 + \dots + \frac{\partial f(x_1,\dots, x_n)}{\partial x_n} dx_n.
$$
Bien utilisées, ces notations ont le potentiel de simplifier significativement
le calcul différentiel ; elle recèlent toutefois un potentiel d'ambiguité
-- et donc des risques d'erreurs -- contre lequel il faut se prémunir. 
Nous allons donc les détailler sur un exemple et les interpréter à la lumière 
des concepts déjà introduits.

#### Différentielle d'expressions
L'idée clé est d'étendre le calcul différentiel des fonctions 
à des formules mathématiques ou expressions, 
composées de symboles de fonctions, d'opérateurs, de constantes et de variables. 
Considérons par exemple, l'expression $$e := ``x^2 - c^2 t^2".$$ 
Nous allons rapidement omettre les guillemets pour simplifier les notations ; 
mais pour le moment ils soulignent que nous avons affaire à une formule 
(à une suite de symboles) et pas à un nombre réel.
Cette expression exploite les opérateurs d'addition 
et d'exponentiation ; le symbole "$2$" désigne une
constante numérique ainsi que "$c$" (ici, la vitesse de la lumière 
dans le vide) ;
les symboles "$x$" et "$t$" font référence à des variables (de position et de 
temps respectivement). 
La valeur numérique que désigne $e$ est définie pour toute valeur réelle des
variables $x$ et $t$ ;
on peut donc lui associer la fonction
$$
f: (x,t) \in \R \times \R \mapsto x^2 - c^2 t^2 \in \R
$$
et utiliser ensuite les expressions $e$ et "$f(x, t)$" de façon interchangeable.
La fonction $f$ étant différentiable, on définit la différentielle
de l'expression $e$ comme
$$
d e := d(f(x, t)) := df (x, t).
$$

#### Dérivées partielles et arguments nommés
Pour ce qui est des dérivées partielles, on a intérêt à adopter une notation
qui tient compte du nom des variables plutôt que de leur position dans la liste
des arguments de la fonction ; on définit donc
$$
\frac{\partial e}{\partial x} := \frac{\partial \, f(x, t)}{\partial x} := \partial_1 f(x, t)
\; \mbox{ et } \;
\frac{\partial e}{\partial t} := \frac{\partial \, f(x, t)}{\partial t} := \partial_2 f(x, t).
$$
Compte tenu de l'expression $e$, on a ici
$$
\frac{\partial e}{\partial x} = 2x 
\; \mbox{ et } \;
\frac{\partial e}{\partial t} = -2c^2 t. 
$$

#### Différentielle des variables
Remarquons que les symboles de variables "$x$" et "$t$" sont aussi des 
expressions à part entière. Elles peuvent donc être associées aux fonctions
linéaires
$(x,t) \in \R \times \R \mapsto x \in \R$ et 
$(x,t) \in \R \times \R \mapsto t \in \R$ ; leur différentielle satisfait donc
$$
dx\cdot (h_x, h_t) = h_x \; \mbox{ et } \; dt \cdot (h_x, h_t) = h_t. 
$$
Les fonctions $dx$ et $dt$ -- il s'agit bien de fonctions et pas de nombres -- 
prélèvent donc dans le vecteur de variation des arguments $(h_x, h_t)$ la 
composante associée à la variable $x$ et $t$ respectivement.

La différentielle de $e$ satisfait
$d e \cdot (h_x, h_t) = ({\partial e}/{\partial x}) h_x + ({\partial e}/{\partial t}) h_t$
pour toute variation $(h_x, h_t)$. On peut donc réécrire cette relation sous la forme
$$
d e = \frac{\partial e}{\partial x} dx + \frac{\partial e}{\partial t} dt,
$$
et donc ici
$$
d (x^2 - c^2 t^2) = 2x \, dx - 2 c^2 t \, dt.
$$

### Nouveau jeu de variables {.exercise .one .question}
On considère successivement l'expression $x^2 - c^2 t^2$ comme une fonction 
non plus de $(x, t)$, mais de $(t,x)$ puis de $(t, x, y)$. 
Comment interpréter les termes
$dt$ et $dx$ dans chacun de ces cas ?
La relation $d (x^2 - c^2 t^2) = 2x \, dx - 2 c^2 t \, dt$ est-elle
toujours valable ?


### Différentielle d'une application linéaire {.exercise .one .question}
Soit $A \in \mathbb{R}^{m\times n}$. Interpréter puis démontrer la relation
$$
d (A \cdot x) = A  \cdot dx.
$$
En déduire ... $d(x+y)$ ... $d(\lambda x)$ ... Puis linéarité diff ?

### TODO
Déduire régle de la somme et linéarité de l'identité 
$$d(A \cdot x) = A  \cdot dx$$ ? 
Déduire la régle du produit de
$$
d(x^{\top} \cdot A \cdot y) =  x^{\top} \cdot A \cdot dy + y^{\top} \cdot A^{\top} \cdot dx
$$
(csq exo : difff $\left<x, y\right>$ et $\|x\|$ (si $x \neq 0$))

### TODO: diff fct bilin

### Différentielle et norme euclidienne {.exercice .question #diff-norm}
En exploitant la règle de différentiation en chaîne, montrer que le
carré de la norme euclidienne
$$
f: x \in \R^n \mapsto \|x\|^2 \in \R
$$ 
est différentiable, puis calculer son gradient $\nabla f$.

### Différentiabilité et norme euclidienne {.answer #answer-diff-norm}
Pour tout $x \in \R^n$ on a
$$
\|x\|^2 = x^{\top} \cdot I \cdot x,
$$
La fonction $x \in \R^n$ peut donc s'écrire comme la composée
des fonctions
\begin{align*}
f &: x \in \R^n  \mapsto (x, x) \in \R^{n} \times \R^n \\
g &: (x, y) \in \R^n \times \R^n \mapsto x^{\top} \cdot y \in \R \\
\end{align*}

**TODO**




### TODO - adapter. Linéarité de la différentielle {.corollary}
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


Variation des fonctions
================================================================================

### {.remark}
Lorsque la fonction $f$ est différentiable en $x$, 
nous disposons de l'égalité 
$$
f(x + h) - f(x) = df(x) \cdot h + \varepsilon(h) \|h\|
$$
avec $\lim_{h \to 0}\varepsilon(h) = 0$. 
Cette égalité est de nature asymptotique, ce qui veut dire que
pour maîtriser l'écart entre
$f(x+h)$ et $f(x)$, 
nous devons être en mesure de faire tendre $h$ vers $0$ ;
si la grandeur $h$ est fixée cette relation ne
nous fournit aucune information, même si $h$ est "très petit". 

Mais tout n'est pas perdu : si nous savons que $f$ est différentiable 
non pas uniquement en $x$ mais sur tout le segment $[x,x+h]$, 
il est possible de calculer la différence entre $f(x+h)$ et $f(x)$ 
en intégrant les variations infinitésimales 
de $f$ le long de $[x, x+h]$. 

### Théorème fondamental du calcul (monovariable) {.theorem #TFC .one}
Si $f: [a, b] \subset \R \to \R^m$ est dérivable et que $f'$ est intégrable alors
$$
f(b) - f(a)  = \int_a^b f'(x) \, dx.
$$

### Démonstration {.proof}
Voir l'enseignement de calcul intégral.

### A propos du terme "intégrable" {.remark .three}
A ce stade, vous pouvez retenir que si $f'$ est continue, 
continue par morceaux ou même intégrable au sens de Riemann, 
elle est "intégrable" comme le demandent les hypothèses du théorème.

Dans ce chapitre, sauf précision contraire, le terme "intégrable" 
doit être compris comme "intégrable au sens de Lebesgue". 
La définition de ce concept 
-- ainsi que la preuve du théorème fondamental du calcul -- 
seront fournies dans le volet calcul intégral de l'enseignement.  


### Forme générale du théorème fondamental du calcul {.remark .four #TFCE}
Si l'on adopte au lieu de l'intégrale de Lebesgue l'intégrale encore
plus générale de Henstock-Kurzweil (cf. calcul intégral), 
alors toute fonction dérivée est automatiquement 
intégrable. 
Le théorème fondamental du calcul est alors valable en toute généralité ; 
il prend la forme suivante :
si $f: [a, b] \to \R^m$ est dérivable, alors $f'$ est intégrable 
(au sens de Henstock-Kurzweil) et
$$
f(b) - f(a)  = \int_a^b f'(x) \, dx.
$$
Cette forme avancée du théorème est toutefois rarement nécessaire ; 
elle est néanmoins utile pour prouver 
[l'inégalité des accroissements finis](#TAFS) en toute généralité.
Cette extension est aussi applicable à 
[la version multivariable du théorème fondamental du calcul](#VF) : 
si l'on utilise l'intégrale de Henstock-Kurzweil, il sera inutile
de vérifier que l'application 
$t \mapsto df(a+th)  \cdot h$ est intégrable pour appliquer le théorème ;
comme dérivée de l'application $t \mapsto f(a+th)$, 
cette fonction l'est automatiquement.

### Théorème fondamental du calcul (multivariable) {.theorem #VF .two}
Soient $U$ un ouvert de $\mathbb{R}^n$ et $f: U \to \mathbb{R}^m$,
soient $a \in U$ et $h \in \mathbb{R}^n$ tels que le segment
  $$
  [a, a+h] = \{a + th \; | \; t \in [0,1]\}
  $$
soit inclus dans $U$. Si $f$ est différentiable en tout point de $[a, a+h]$
et que l'application $t \in [0,1] \mapsto df(a+th) \cdot h \in \R^m$ 
est intégrable, alors
$$
f(a + h) - f(a) = \int_0^1 df(a+th) \cdot h \, dt.
$$

![Géométrie [du théorème du calcul multivariable](#VF)](images/peanut.tex)

### Démonstration {.proof}
L'ensemble $U$ étant ouvert, il existe un $\varepsilon > 0$ tel que
l'intervalle ouvert $I := \left]-\varepsilon, 1+\varepsilon \right[$ 
soit inclus dans $U$. 
On note $\phi$ la fonction $I \to \mathbb{R}^n$ 
définie par
$$
\phi(t) = f(a + th)
$$
La fonction $\phi$ est différentiable -- et donc dérivable -- 
en tout point de $[0,1]$ [comme composée des fonctions 
différentiables $f$ et $t \mapsto a + th$](#chain-rule) ; 
sa dérivée est donnée par
$$
\begin{split}
\phi'(t) &= d\phi(t) \\
         &= df(a+th) \cdot d(t\mapsto a+th) \\
         &= df(a+th) \cdot (t \mapsto a+th)' \\
         &= df(a+th) \cdot h
\end{split}
$$
Par [le théorème fondamental du calcul](#TFC), comme par hypothèse $\phi'$ 
est intégrable sur $[0, 1]$, on a donc
$$
f(a+h) - f(a) = \phi(1) - \phi(0) = \int_0^1 \phi'(t) \, dt 
                                  = \int_0^1 df(a+th) \cdot h \, dt.
$$

### Cas des fonctions continûment différentiables {.exercise .one .question #cfcd3}
Soient $U$ un ouvert de $\mathbb{R}^n$ et $f: U \to \mathbb{R}^m$,
soient $a \in U$ et $h \in \mathbb{R}^n$ tels que le segment
$[a, a+h] = \{a + th \; | \; t \in [0,1]\}$
soit inclus dans $U$. 
Montrer que si $f$ est continûment différentiable sur $U$, 
[le théorème fondamental du calcul](#VF) est applicable.

### Inégalité des accroissements finis (monovariable) {.theorem #TAFS .two}
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
Par [la forme générale du théorème fondamental du calcul](#TFCE),
la fonction $f'$ est intégrable au sens de Henstock-Kurzweil et
$$
f(a+h) - f(a) = \int_a^{a+h} f'(t) \, dt.
$$
La théorie de l'intégrale de Henstock-Kurzweil nous garantit qu'il est possible 
d'obtenir des approximations arbitrairement précises de cette intégrale au moyen de 
sommes de Riemman[^aci]. Cela signifie que pour tout $\varepsilon > 0$, 
il existe des réels $x_0, \dots, x_k, t_0, \dots, t_{k-1}$ vérifiant
$$
a = x_0 \leq t_0 \leq x_1 \leq t_1 \leq  \dots \leq x_{k-1} \leq t_{k-1} \leq x_{k} = a+h
$$
telle que la somme
$$
S = \sum_{i=0}^{k-1} f'(t_i)(x_{i+1} - x_i)
$$
satisfasse
$$
\left\| \int_a^{a+h} f'(t) \, dt -  S \right\| 
\leq 
\varepsilon.
$$

[^aci]:  en combinant la définition de l'intégrabilité de $f'$ 
au sens de Henstock-Kurzweil et 
[le lemme de Cousin](Calcul Intégral I.pdf#cousin) du calcul intégral.

En exploitant deux fois l'inégalité triangulaire, on obtient donc
$$
\|f(a+h) - f(a)\|
\leq 
\|S\| + \varepsilon \leq \sum_{i=0}^{k-1} \|f'(t_i)\| |x_{i+1} - x_i| +\varepsilon.
$$
Comme $\|f'(t_i)\| \leq M$ pour tout $i \in \{0,\dots,k-1\},$
$$
\sum_{i=0}^{k-1} \|f'(t_i)\| |x_{i+1} - x_i|
\leq
\sum_{i=0}^{k-1} M |x_{i+1} - x_i|
\leq M \sum_{i=0}^{k-1} |x_{i+1} - x_i|
$$
et comme $a=x_0 \leq x_1 \leq \dots \leq x_k = a+h$,
$$
\sum_{i=0}^{k-1} |x_{i+1} - x_i| = \sum_{i=0}^{k-1} (x_{i+1} - x_i) =
x_p - x_0 = (a+h) - a = h.
$$ 
On a donc $\|S\| \leq Mh$  et
par conséquent $\|f(a+h) - f(a)\| \leq M h + \varepsilon$ ;
le choix de $\varepsilon > 0$ étant arbitraire, on en déduit
le résultat cherché.


### {.remark}
L'énoncé de l'inégalité des accroissements finis ne fait aucune hypothèse sur 
la régularité de la fonction $f'$ ; c'est cette généralité qui rend sa 
démonstration technique. Si l'on accepte des hypothèses un peu plus 
contraignantes, elle peut être simplifiée de façon significative.

### Cas des fonctions continûment différentiables {.exercise .question .one #cfcd2}
Trouver une démonstration simple de [l'inégalité des accroissement finis](#TAFS)
reposant sur [le théorème fondamental du calcul](#TFC)
dans le cas où la fonction $f'$ est continue (ou continue par morceaux,
ou intégrable au sens de Riemann, ou intégrable au sens de Lebesgue, 
selon la théorie de l'intégration que vous connaissez à ce stade).

### {.remark}
Il existe également une démonstration alternative
de l'inégalité des accroissements finis qui ne repose pas sur le calcul intégral, 
mais sur les identités associées à la norme euclidienne et sur le théorème des
valeurs intermédiaires :

### Inégalité des accroissements finis (version euclidienne)  {.exercise #mitch .question .two}
Soit $\phi: t \in [a, a+h] \to \R$ la fonction définie par
$$
\phi(t) = \left<f(a+h) - f(a), f(t) \right>.
$$
En appliquant le théorème des valeurs intermédiaires à $\phi$, 
prouver [l'inégalité des accroissements finis](#TAFS).





### Inégalité des accroissements finis (multivariable) {.theorem #TAF .two}

Soient $U$ un ouvert de $\mathbb{R}^n$, et $f: U \to \mathbb{R}^m$
supposée différentiable en tout point d'un segment $[a, a+h]$ inclus 
dans $U$ et dont la différentielle est majorée en norme par $M$ sur $[a, a+h]$, 
c'est-à-dire telle que
$$
\mbox{pour tout } x \in [a, a+h], \;\|f'(x)\| \leq M.
$$
Alors 
$$
\|f(a+h) - f(a)\| \leq M \|h\|.
$$


### Démonstration {.proof}
Considérons la fonction $\phi: t \mapsto f(a+th)$ déjà exploitée 
dans la démonstration de la proposition ["Variation d'une fonction"](#VF) ;
cette fonction est dérivable sur $[0,1]$, de dérivée $\phi'(t) = df(a+th) \cdot h$.
De plus, 
$$
\|\phi'(t)\| = \| df(a+th) \cdot h \| \leq \| df(a+th) \|\|h\| \leq M \|h\|.
$$
Par [l'inégalité des accroissements finis dans le cas d'une variable réelle](#TAFS), 
$$
\|f(a+h) - f(a)\| = \|\phi(1) - \phi(0)\|
\leq M \|h\| \times 1 = M \|h\|.
$$

### Variation du logarithme {.exercice .two .question #log}
Il est possible de définir une version multivariable et vectorielle 
de la fonction logarithme, définie sur le *plan coupé*
$$U = \R^2 \setminus \{(x, 0) \; | \;  x \leq 0\}$$ et à valeurs dans $\R^2$. 
Cette fonction est différentiable et vérifie en tout point
$$\|d \log (x, y)\| = \frac{1}{\sqrt{x^2 + y^2}}.$$ 
Montrer que pour tout $(x, y) \in U$, on a 
$$
\|\log (x, y) - \log (x, -y)\| \leq 2 \pi.
$$

### TODO
revoir nom des variables ($a$, $h$, $x$, etc.) en cohérence avec ce qui précède.

### Normes non euclidiennes {.remark .four}

Les versions [monovariable](#TAFS) et [multivariable](#TAF) de l'inégalité des 
accroissements finis peuvent être généralisées à d'autres normes que la 
norme euclidienne. Dans le cas monovariable, si $\|\cdot\|_{\R^m}$ est
une norme arbitraire sur $\R^m$ et que l'on dispose de la borne $\|f'(y)\|_{\R^m} \leq M$
sur $[x, x+h]$,
alors on peut conclure que $$\|f(x+h) - f(x)\|_{\R^m} \leq Mh.$$ 
Dans le cas multivariable, si de plus $\|\cdot\|_{\R^n}$ est une norme arbitraire 
sur $\R^n$ et que l'on définit pour tout $A \in \R^{m\times n}$ la norme d'opérateur
associée
$$
\|A\|_{\R^{m\times n}} := \sup_{x \neq 0} \frac{\|A \cdot x\|_{\R^m}}{\|x\|_{\R^n}},
$$
alors on peut déduire de la borne $\|df(y)\|_{\R^{m\times n}} \leq M$ sur $[x, x+h]$ 
que $$\|f(x+h) - f(x)\|_{\R^m} \leq M \|h\|_{\R^n}.$$
Seules des modifications mineures des démonstrations déjà présentées sont 
nécessaires pour établir ces résultats.

Annexe -- Algèbre linéaire
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

Exercices complémentaires
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

### TODO

Pt spline / point de contôle. Avec dessin. 

Question / "contrôle de la direction" d'un point / mouvement point de contrôle ?

Différentiation en chaîne {#dec}
--------------------------------------------------------------------------------

[La règle générale de différentiation en chaîne](#chain-rule)
s'applique à la composée de deux fonctions différentiables 
$f: U \subset \R^p \to \R^n$ et $g: V \subset \R^n \to \R^m$.

### Question 1 {.question #dec-1 .one}
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

Robot manipulateur
--------------------------------------------------------------------------------

Les coordonnées cartésiennes $x$ et $y$ de l'effecteur final 
d'un robot dans le plan, composé de deux barres rigides de longueur
$\ell_1$ et $\ell_2$ et d'articulations rotoïdes sont données
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

![$\ell_1 = 3$, $\ell_2 = 2$, $\theta_1 = \pi/4$, $\theta_2 = - \pi/4$.](images/robot.tex){#robot}

On souhaite quantifier quel impact un jeu au niveau des articulations affecte
la précision du positionnement de l'effecteur final.

### Question 1  {.question #rm-1 .one}
Montrer que l'application 
$f: (\theta_1, \theta_2) \in \R^2 \mapsto (x, y) \in \R^2$ 
est différentiable et déterminer sa matrice jacobienne.

### Question 2  {.question #rm-2 .two}

Soit $(\theta_{10}, \theta_{20}) \in \R^2$ et 
$(x_0, y_0) = f(\theta_{10}, \theta_{20})$.
Montrer que si 
$$|\theta_1 - \theta_{10}| \leq \varepsilon \; \mbox{ et } \; 
|\theta_2 - \theta_{20}| \leq \varepsilon$$ alors $(x, y) = f(\theta_1, \theta_2)$
appartient au carré centré en $(x_0, y_0)$ d'arête de longueur 
$(\ell_1/2 + \ell_2) \varepsilon$.


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

### Question 1 {.question #ddh-1 .one}
Montrer que si $f$ est directionnellement dérivable au sens de Hadamard 
en $x$, alors $f$ est directionnellement dérivable au sens classique.

### Question 2 {.question #ddh-2 .three}
Montrer que si $f$ est directionnellement dérivable au sens de Hadamard
en $x$, la grandeur $(f \circ \gamma)'(0)$ ne dépend de $\gamma$
qu'à travers $\gamma'(0)$ et que par conséquent
$$
(f\circ \gamma)'(0) = f'(x, \gamma'(0)).
$$

### Question 3 -- Dérivation en chaîne {.question #ddh-3 .two}
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

### Question 4 {.question #ddh-4 .four}
Montrer que $f$ est directionnellement dérivable au sens de Hadamard en $x$ 
si et seulement si la limite
$$
\lim_{(t, k) \to (0, h)} \frac{f(x+ t k) - f(x)}{t}
$$
existe et que la limite est alors égale à $f'(x, h)$.

### Question 5 {.question #ddh-5 .four}
Une fonction dérivable directionnellement au sens de Hadamard en $x$ est 
*différentiable au sens de Hadamard* en $x$ si de plus $f'(x, h)$ 
est une fonction linéaire de $h$.
Montrer que $f$ est différentiable en $x$ au sens de Hadamard 
si et seulement si elle est différentiable en $x$.


Thermodynamique
--------------------------------------------------------------------------------

Pour un gaz parfait, la pression $P$, le volume $V$, le nombre de particules 
$N$ et la température $T$ sont reliés par la relation
$$
PV = N k_B T
$$
où $k_B$ est la constante de Boltzmann. Si en outre le gaz est mono-atomique, 
son entropie $S$ est donnée par l'expression[^gibbs]
$$
S = N k_B \left[\frac{5}{2} + \ln \left(\frac{V}{N} \frac{(2\pi m k_B T)^{3/2}}{h^3} \right)\right]
$$
où $h$ est la constante de Planck et $m$ la masse d'un atome de gaz.
On s'intéresse dans la suite à une quantité fixe d'un gaz donné de ce type.

[^gibbs]: cf. par exemple [l'article consacré au "Paradoxe de Gibbs" sur Wikipédia](https://fr.wikipedia.org/wiki/Paradoxe_de_Gibbs).

### Question 0 {.question #th-0 .one}
Quelles sont les grandeurs variables ("variables d'état") associées à 
cette expression de l'entropie $S$ ? Quelle intervalle de valeurs peuvent
prendre ces variables ? (On souhaite que l'entropie soit toujours définie.)

### Question 1 {.question #th-1 .one}
Montrer que la différentielle $dS$ est bien définie et la calculer
en utilisant les notations les plus appropriées.

### Question 2 {.question #th-2 .three}
L'énergie interne $U$ du gaz est une fonction des variables d'état 
(une "fonction d'état") ;
sa variation infinitésimale est reliée à celle de l'entropie et 
du volume par la relation
$$
dU = T dS - P dV.
$$
Quel sens donnez-vous à cette relation mathématiquement ? 
Pouvez-vous la réécrire en utilisant les variations associées aux variables
d'état utilisées précédemment ? 

### Question 3 {.question #th-3 .two}
Déduire de la question précédente une expression de l'énergie interne 
(définie à une constante près).

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

Exercices essentiels
--------------------------------------------------------------------------------

### Dérivée sur un intervalle fermé {.answer #answer-dif}

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


### Fonction discontinue {.answer #answer-discont}
La fonction $f: \R^2 \to \R$ définie par :
$$
f(x,y) = \left|
\begin{array}{rl}
0 & \mbox{si $x=0$ ou $y=0$,} \\
1 & \mbox{sinon.}
\end{array}
\right.
$$
est discontinue en $(0,0)$, car $f(2^{-n}, 2^{-n}) = 1$ pour tout $n \in \N$,
donc
$$
\lim_{n \to +\infty} f(2^{-n}, 2^{-n}) = 1 \neq 0 = f(0,0).
$$
Par contre, les deux fonctions partielles de $f$ en $(0,0)$
$$
x_1 \mapsto f(x_1, 0) \; \mbox{ et } \; x_2 \mapsto f(0, x_2)
$$
sont constantes et égales à $0$. Les dérivées partielles $\partial_1 f(0,0)$
et $\partial_2 f(0,0)$ existent donc et sont nulles. Le gradient de $f$ en
$(0,0)$ est donc définie (et nul).

### Fonctions affines {.answer #answer-fa}
Comme $f(x) = A \cdot x + b$, la $i$-ème composante de $f$ satisfait
$$
f_i(x) = \sum_{k=1}^n A_{ik} x_k + b_i
$$
et donc la $j$-ème fonction partielle de $f_i$ en $x$ est la fonction 
de la variable $y_j$ dont la valeur est
\begin{multline*}
f_i(x_1, \dots, x_{j-1}, y_i, x_{j+1}, \dots, x_n) = \\
A_{i1} x_1 + \dots + A_{i,j-1} x_{j-1} + A_{ij} y_j + A_{i,j+1} x_{j+1} + b_i.
\end{multline*}
C'est une fonction affine de $y_j$ qui est dérivable, de dérivée
$A_{ij}$. On a donc
$\partial_j f_i(x) = A_{ij}$ ; la matrice jacobienne $J_f(x)$ existe en tout
point $x \in \R^n$ et vérifie $J_f(x) = A$.

Pour tout $x \in \R^n$ et $h \in \R^n$, on a donc
$$
f(x+h) -  f(x) - J_f(x) \cdot h = A \cdot (x+h) - A \cdot x - A\cdot h = 0,
$$
ce que l'on peut écrire sous la forme
$$
f(x+h) = f(x) + J_f(x) \cdot h + \varepsilon(h) \|h\|
$$
en prenant pour fonction $\varepsilon$ la fonction de $\R^n$ dans $\R^m$ 
identiquement nulle. La fonction $f$ est donc différentiable sur $\R^n$.

### Développement limité au premier ordre {.answer #answer-dlmj}
De l'hypothèse 
$$
f(x+h) = f(x) + A \cdot h + \varepsilon(h) \|h\|
$$
on peut déduire que pour tout $i \in \{1,\dots, n\}$, on a 
$$f_i(x+h) = f_i(x) + [A \cdot h]_i + \varepsilon_i(h) \|h\|$$ et donc
\begin{align*}
\frac{f_i(x + t e_j) - f_i(x)}{t} 
&= \frac{f_i(x) + [A \cdot te_j]_i + \varepsilon_i(te_j) \|te_j\| - f_i(x)}{t} \\
&= [A \cdot e_j]_i + \varepsilon_i(t e_j) \\
&= A_{ij} + \varepsilon_i(t e_j).
\end{align*}
Comme $\lim_{h \to 0}\varepsilon(h) = \varepsilon(0) = 0$,
cette expression a une limite quand $t \to 0$, donc
$\partial_j f_i(x)$ existe et vérifie
$$
\partial_j f_i(x) = \lim_{t \to 0} \frac{f_i(x + t e_j) - f_i(x)}{t} = A_{ij}.
$$
La matrice jacobienne $J_f(x)$ de $f$ en $x$ existe donc et est égale à $A$.

### Fonction quadratique {#answer-fq .answer}
Comme
$$
f(x) = x^{\top} \cdot A \cdot x = \sum_{i=1}^{n} \sum_{k=1}^n x_i A_{ik} x_k,
$$
pour tout $j \in \{1,\dots, n\}$ on a 
$$
f(x) = x_j A_{jj} x_j + \sum_{\substack{k=1 \\ k\neq j}}^n x_j  A_{jk} x_k +  \sum_{\substack{i=1\\i\neq j}}^n x_i A_{ij} x_j
+ \sum_{\substack{i=1\\i\neq j}}^{n} \sum_{\substack{k=1\\k\neq j}}^n x_i A_{ik} x_k.
$$
Par conséquent, la dérivée partielle $\partial_j f(x)$ existe et vérifie
\begin{align*}
\partial_j f(x) &= 2 A_{jj} x_{j} + \sum_{\substack{k=1 \\ k\neq j}}^n A_{jk} x_k + \sum_{\substack{i=1\\i\neq j}}^n x_i A_{ij} \\
&= \sum_{k=1}^n A_{jk} x_k + \sum_{i=1}^n x_i A_{ij} \\
&= [A \cdot x]_j + [A^{\top} \cdot x]_j \\
&= [(A + A^{\top}) \cdot x]_j.
\end{align*}
Toute ces dérivées partielles sont des fonctions linéaires de $x$, 
elles sont donc continues et la fonction $f$ est continûment différentiable ;
[elle est donc différentiable](#cdid).
De plus, l'égalité ci-dessus nous fournit
$$
J_f(x)^{\top} = \nabla f(x) = (A + A^{\top}) \cdot x,
$$
et donc la différentielle de $f$ en $x$ est l'application déterminée par
$$
df(x) \cdot h = J_f(x) \cdot h = ((A + A^{\top}) \cdot x)^{\top} \cdot h
= x^{\top} \cdot (A + A^{\top}) \cdot h.
$$

### Composition de fonctions continûment différentiables {.answer #answer-cfcd}
D'après [la règle de différentiation en chaîne](#chain-rule), $d (g\circ f)(x)= dg(f(x)) \cdot df(x)$.
Donc pour tout $i \in \{1, \dots, m\}$ et $j \in \{1,\dots, p\}$,
\begin{align*}
[d (g\circ f)(x)]_{ij} &= 
[dg(f(x)) \cdot df(x)]_{ij} \\
&= \sum_{k=1}^n [dg(f(x))]_{ik} [df(x)]_{kj} \\
&= \sum_{k=1}^n \partial_k g_i(f(x)) \partial_j f_k(x).
\end{align*}
Chaque coefficient $\partial_j (g\circ f)_i$ est une somme de produit de 
fonctions continues et est donc continu. Par conséquent, $g\circ f$ est
continûment différentiable.

### Cas des fonctions continûment différentiables {.answer #answer-cfcd3}
Si $f$ est continûment différentiable sur $U$, elle est en particulier
différentiable sur $[a, a+h]$. De plus, 
$$
df(a+th) \cdot h = \sum_{i=1}^{n} \partial_j f(a+th) h_j,
$$
donc la fonction $t \in [0,1] \mapsto df(a+th) \cdot h$ est continue
et par conséquent intégrable. [Le théorème fondamental du calcul](#VF)
est donc applicable.

### Cas des fonctions continûment différentiables {.answer #answer-cfcd2}
Si la fonction $f'$ est continue (ou intégrable au sens de
Riemann, ou intégrable au sens de Lebesgue), 
[le théorème fondamental du calcul](#TAFS) est applicable, donc 
$$
f(a+h) - f(a) = \int_a^{a+h} f'(t) \, dt.
$$
L'inégalité triangulaire appliquée à l'intégrale du membre de droite fournit
alors
$$
\left\|f(a+h) - f(a)\right\| = \left\|\int_a^{a+h} f'(t) \, dt\right\|
\leq \int_a^{a+h} \|f'(t)\| \, dt \leq \int_a^{a+h} M \, dt = M h.
$$

### Inégalité des accroissements finis (version euclidienne) {.answer #answer-mitch}
**TODO.** adopter convention $\phi$ déf sur $[0,1]$ plus proche de ce qui
précède et qui suit ?
Comme
$$
\frac{\phi(t+s) - \phi(t)}{s} 
= 
\left<f(a+h) - f(a), \frac{f(t+s) - f(t)}{s}\right>,
$$
la fonction $\phi$ est dérivable en tout point $t\in [a,a+h]$ et
$$
\phi'(t) = \left<f(a+h) - f(a), f'(t) \right>.
$$
La fonction $f$ étant à valeurs réelles, 
le théorème des valeurs intermédiaires est applicable : il existe un 
$\tau \in [a,a+h]$ tel que
$$
\phi(a+h) - \phi(a) = \phi'(\tau) h = \left<f(a+h) - f(a), f'(\tau) \right> h.
$$
Comme par ailleurs
\begin{align*}
\phi(a+h) - \phi(a) &= 
\left<f(a+h) - f(a), f(a+h) \right> - \left<f(a+h) - f(a), f(a) \right>  \\
&= \|f(a+h) - f(a)\|^2,
\end{align*}
on a 
$$
\|f(a+h) - f(a)\|^2 = \left<f(a+h) - f(a), f'(\tau) \right> h \leq \|f(b) - f(a)\| \|f'(\tau)\| h.
$$
Puisque $\|f'(\tau)\| \leq M$, on en déduit que $\|f(a+h) - f(a)\| \leq M h.$




### Variation du logarithme {.answer #answer-log}
En premier lieu, on peut noter qu'en général, 
le segment d'extrémités $(x, y)$ et $(x, -y)$ 
n'est pas inclus dans le plan coupé $U$.
On ne peut donc pas appliquer directement [la version multivariable de 
l'inégalité des accroissements finis](#VF).
Nous allons donc adapter la technique utilisée dans la démonstration de ce 
théorème en introduisant un chemin $\phi: [0, 1] \to \R^2$ qui joint $(x, y)$ et 
$(x, -y)$ et dont l'image est incluse dans $U$.

![Représentation du chemin $\phi$ quand $(x, y)=(-1, -1)$.](images/log.tex)

On note $\theta$ l'unique détermination de l'angle polaire de $(x, y)$ comprise
dans l'intervalle $\left]-\pi, \pi\right[$ et on pose
$$
\phi(t) := \left(r\cos ((1 - 2 t)\theta), r\sin ((1-2t)\theta) \right)
\; \mbox{ où } \; r := \sqrt{x^2 + y^2}.
$$
On remarque que $\phi(t) \in U$ pour tout $t$, que $\phi(0) = (x, y)$
et que $\phi(1) = (x, -y)$. La fonction $\phi$ est dérivable et 
$$
\phi'(t) = \left(2 \theta r\sin ((1 - 2 t)\theta), -2 \theta r\cos ((1-2t)\theta) \right) ;
$$
la fonction $\log \circ  \, \phi$ est donc définie et dérivable et 
$$
d (\log \circ \, \phi) (t) = d \log (\phi(t)) \cdot d \phi(t)=
d \log(\phi(t)) \cdot \phi'(t).
$$
Par conséquent,
$$
\|d (\log \circ \, \phi) (t)\| \leq \|d \log (\phi(t))\| \|\phi'(t)\|
\leq \frac{1}{r} \times 2 |\theta| r = 2 |\theta| \leq 2 \pi.
$$
L'application de 
[l'inégalité des accroissement finis (monovariable)](#TAFS) à la fonction 
$\log \circ \, \phi$ fournit donc l'inégalité
$$
\|\log (x, y) - \log (x, -y)\| \leq 2 \pi.
$$

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


Robot manipulateur
--------------------------------------------------------------------------------

### Question 1  {.answer #answer-rm-1}

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
\partial x/ \partial \theta_1
&=& -\ell_1 \sin \theta_1 - \ell_2 \sin (\theta_1 + \theta_2), \\
\partial x / \partial \theta_2
&=& - \ell_2 \sin (\theta_1 + \theta_2), \\
\partial y / \partial \theta_1
&=& \ell_1 \cos \theta_1 + \ell_2 \cos (\theta_1 + \theta_2), \\
\partial y / \partial \theta_2
&=& \ell_2 \cos (\theta_1 + \theta_2).
\end{array}
$$
Ces grandeurs étant continues, la fonction $f$ est continûment
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

### Question 1  {.answer #answer-rm-2}
Soient $\delta \theta_1 := \theta_1 - \theta_{10}$
et $\delta \theta_2 := \theta_2 - \theta_{20}$. La fonction
$$
\phi : t \in [0, 1]  
\mapsto
f(\theta_{10} + t\delta \theta_1, \theta_{12} + t\delta \theta_2)
$$
est continûment dérivable, de dérivée
$$
\phi'(t)=
df(\theta_{10} +t \delta \theta_1, \theta_{20} +t \delta \theta_2) 
\cdot (\delta \theta_1 , \delta \theta_2)
$$
Si l'on note $s_1(t) = \sin (\theta_{10} + t\delta \theta_1)$,
$c_1(t) = \cos (\theta_{10} + t\delta \theta_1)$, ...,
le [théorème fondamental du calcul](#TFC) et l'expression de la matrice
jacobienne de $f$ nous fournissent donc
\begin{multline*}
f(\theta_1, \theta_2) - f(\theta_{10}, \theta_{20})
=
\int_0^1 \, \phi'(t) \, dt 
= \\
\int_0^1
\left[
\begin{array}{c}
(-\ell_1 s_1(t) -\ell_2 s_{12}(t)) \delta \theta_1  -\ell_2 s_{12}(t) \delta \theta_2 \\
(\ell_1 c_1(t) + \ell_2 c_{12}(t)) \delta \theta_1 + \ell_2 c_{12}(t) \delta \theta_2
\end{array}
\right] dt
\end{multline*}
et donc par inégalité triangulaire et majoration de l'intégrande,
$$
|x- x_0| = |f_1(\theta_1,\theta_2) - f_1(\theta_{10}, \theta_{20})| \leq (\ell_1 + \ell_2) |\delta \theta_1| + \ell_2 |\delta \theta_2|
$$
ainsi que 
$$
|y - y_0| = |f_2(\theta_1,\theta_2) - f_2(\theta_{10}, \theta_{20})|
\leq (\ell_1 + \ell_2) |\delta \theta_1| + \ell_2 |\delta \theta_2|.
$$
Si $|\delta \theta_1| \leq  \varepsilon$ et $|\delta \theta_2| \leq  \varepsilon$,
on en déduit
$$
|x - x_0| \leq (\ell_1 + 2\ell_2) \varepsilon \; \mbox{ et } \;
|y - y_0| \leq (\ell_1 + 2\ell_2) \varepsilon.
$$
Le point $(x, y) = f(\theta_1, \theta_2)$ appartient donc au carré centré 
en $(x_0, y_0)$ d'arête de longueur $(\ell_1/2 + \ell_2=\varepsilon$. 


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
Si $f$ est différentiable, notons $\varepsilon$
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
Pour montrer que $f$ est différentiable, 
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
Par conséquent, $f$ est bien différentiable.


Thermodynamique
--------------------------------------------------------------------------------

### Question 0 {.answer #answer-th-0}
Les variables associées à l'expression fournie de l'entropie $S$ sont le volume
$V$ et la température $T$. Pour que l'expression définissant l'entropie soit 
toujours définie, il suffit d'exiger que $V$ et $T$ soient strictement positives.

### Question 1 {.answer #answer-th-1}
L'entropie, en tant que fonction de $(V, T) \in \left]0,+\infty\right[^2$, 
est une fonction (continûment) différentiable. En effet, les dérivées partielles
de $S(V,T)$ sont définies en tout point et vérifient
$$
\frac{\partial S(V, T)}{\partial V} = N k_B \frac{1}{V} 
\; \mbox{ et } \;
\frac{\partial S(V,T)}{\partial T} = \frac{3}{2}N k_B \frac{1}{T},
$$
deux expressions dépendant continûment de $(V, T)$. 
On a par conséquent
$$
d S = \frac{\partial S(V, T)}{\partial V} d V + \frac{\partial S(V,T)}{\partial T} dT = N k_B \left[\frac{dV}{V} + \frac{3}{2} \frac{dT}{T}\right].
$$

### Question 2 {.answer #answer-th-2}
Si $U$ est une fonction (différentiable) de $(V, T)$, 
on peut interpréter mathématiquement la relation $dU = T dS - P dV$ comme
$$
d(U(V, T)) = T d(S(V, T)) - P(V, T) dV
$$
où $P(V, T) := N k_B T / V$ résulte de la loi des gaz parfaits $PV = N k_B T$.
En exploitant la différentielle $dS(V, T)$ déjà calculée, on en déduit 
$$
d(U(V, T)) =  T N k_B \left[\frac{dV}{V} + \frac{3}{2} \frac{dT}{T}\right] - N k_B T \frac{dV}{V}
= \frac{3}{2} N k_B dT.
$$

### Question 3 {.answer #answer-th-3}
Soit $(V_0, T_0) \in \left]0, +\infty\right[^2$ et 
$(V, T) \in \left]0, +\infty\right[^2$. Le segment reliant $(V_0, T_0)$
et $(V, T)$ est inclus tout entier dans $\left]0, +\infty\right[^2$
qui est convexe. Pour tout $t \in [0, 1]$, on a 
\begin{align*}
\phi(t) & :=
dU(V_0 + t(V - V_0), T_0 + t(T - T_0)) \cdot (V - V_0, T - T_0) \\ 
&\phantom{:}= \frac{3}{2}  N k_B dT \cdot (V - V_0, T - T_0) \\
&\phantom{:}= \frac{3}{2}  N k_B (T - T_0).
\end{align*}
La fonction $\phi$ est constante, donc intégrable sur $[0, 1]$.
Par [le théorème fondamental du calcul multivariable](#VF), on a
$$
U(V, T) = U(V_0, T_0) + \int_0^1 \phi(t) \, dt
= \left[U(V_0, T_0) - \frac{3}{2}  N k_B T_0\right] + \frac{3}{2}  N k_B T,
$$
ce qui démontre qu'à une constante près, on a $$U(V, T) =  \frac{3}{2} Nk_B T.$$

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

