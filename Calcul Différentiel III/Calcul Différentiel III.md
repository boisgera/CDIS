% Calcul Différentiel III

<!-- LaTeX Macros -->
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}

--------------------------------------------------------------------------------

TODO
================================================================================

  - Tenseur d'ordre (0, 1, 2 et) $3$. Structure d'espace vectoriel normé.
    Contraction tensorielle, lien avec les applis $n$-linéaires (ouch).

  - Différentielle et matrices (surtout à *valeurs* matricielles ; 
    il va s'agir de différencier $f'(x)$. Mais on peut en profiter pour
    avoir des variables matricielles aussi ... D'autant que si on veut
    utiliser la chain rule, pour avoir une "chain rule d'ordre 2", 
    on voudrait utilser la chain rule d'ordre 1 à travers le produit
    matriciel $(A, B) \to A \cdot B$ donc tout ça est lié.

  - Tenseur des dérivées d'ordre $3$.

  - Différentiabilité d'ordre 2, fct 2 fois continument différentiable.

  - Th fcts implicite version $C^n$, $C^n$ difféo ?

Exercices :

  - Fcts quadratique, Gaussienne, etc.

  - Courbure (dans le plan)

  - "bordered hessian" (optim.) 

  - formules d'analyse vectorielle (div de rot, $\mathrm{div} \, f \vec{u}$, etc.)

  - exemples calcul de DIFFERENTIAL CALCULUS, 
    TENSOR PRODUCTS AND THE IMPORTANCE OF NOTATION (JONATHAN H. MANTON).

Différentielle d'ordre $2$
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

### Tenseur d'ordre $3$ {.definition .one}
On appelera *tenseur d'ordre $3$* un élément de 
$\R^{m \times n \times p}$ où $(m, n, p) \in \N^{3}$, 
c'est-à-dire toute application $A$ de la forme
$$
(i,  j , k) \mapsto A_{ijk} \in \R
$$
où $(i, j, k) \in \{1,\dots,m\} \times \{1,\dots,n\}  \times \{1,\dots,p\}$.

### {.remark}
Un tenseur d'ordre $3$ n'est rien d'autre qu'un tableau de réels à 3 dimensions.
On peut considérer que c'est la suite logique de la progression scalaire
(tenseur d'ordre 0), vecteur (tenseur d'ordre 1), matrice (tenseur d'ordre 2).

### TODO.

Contraction, application bilinéaire, identification, etc.


### TODO

factor out dérivée partielle d'ordre 2.

### Tenseur des dérivées partielles d'ordre $2$ {.definition .one}
Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}^m$ et
$x$ un point de $U$. Soient $f_i$ les fonctions scalaires composant $f$.
Si toutes les dérivées partielles d'ordre $2$ des $f_i$ existent en $x$, 
on définit le *tenseur $f''(x) \in \R^{m \times n \times n}$ 
des dérivées partielles d'ordre $2$ de $f$ en $x$* par
$$
[f''(x)]_{ijk} = \partial_{kj} f_i(x).
$$

### Matrice hessienne {.definition .one}
Soient $U$ un ouvert de $\mathbb{R}^n$, $f: U \to \mathbb{R}$ et
$x$ un point de $U$. Soient $f_i$ les fonctions scalaires composant $f$, 
c'est-à-dire telles que
$f(x) = (f_1(x), \dots, f_m(x)).$
Si toutes les dérivées partielles d'ordre $2$ de $f$ en $x$ existent,
on définit *la matrice hessienne $\nabla^2 f(x)$* de $f$ en $x$ par
$$
[\nabla^2 f(x)]_{jk} = [f''(x)]_{1kj}  = \partial^2_{jk} f(x)
$$
c'est-à-dire
$$
\nabla^2 f(x) = \left[
\begin{array}{cccc}
\partial_{11} f (x) & \partial_{12} f (x) & \cdots & \partial_{1n} f (x) \\
\partial_{21} f (x) & \partial_{22} f (x) & \cdots & \partial_{2n} f (x) \\
\vdots & \vdots & \vdots & \vdots \\
\partial_{nn} f (x) & \partial_{n2} f (x) & \cdots & \partial_{nn} f (x) \\
\end{array}
\right].
$$

### Différentielle d'ordre 2 {.definition #d2 .two}
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


### Variation de la différentielle {.lemma #LVD} 
Si $f: U \subset \mathbb{R}^n \to \mathbb{R}^m$ est une fonction 
deux fois différentiable en $x \in U$,
$$
df(x+k) = df(x) + (h \mapsto d^2 f(x) \cdot h \cdot k) + E(k)\|k\|
$$
où $\lim_{k \to 0} E(k) = 0 \in \R^{m\times n}$.

### Démonstration {.proof}
Par [définition de la différentielle d'ordre 2 en $x$](#d2), 
pour tout vecteur $h$ de $\mathbb{R}^n$ fixé, 
pour tout vecteur $k$ de $\mathbb{R}^n$ dans un voisinage de $0$,
$$
df(x+k) \cdot h = df(x) \cdot h + d^2f(x) \cdot h \cdot k + \varepsilon_{h}(k)(\|k\|),
$$
où $\varepsilon_h$ vérifie $\lim_{k \to 0} \varepsilon_h(k) = 0$.
Si $k$ est non nul, on a donc
$$
\varepsilon_{h}(k) = \frac{1}{\|k\|}\left(df(x+k) \cdot h - df(x) \cdot h - d^2f(x) \cdot h \cdot k \right),
$$
le terme $\varepsilon_{h}(k)$ est donc linéaire en $h$ ; 
notons $E(k)$ l'application linéaire de $\mathbb{R}^n$ dans $\mathbb{R}^m$
qui est nulle quand $k=0$ et définie dans le cas contraire
par $E(k) \cdot h = \varepsilon_h (k)$. On a donc pour tout $h \in \R^n$
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
\|E(k) \cdot h\| &= \left\| E(k) \cdot \left(\sum_{i=1}^n h_i e_i \right) \right\| \\
&\leq \sum_{i=1}^n \|E(k) \cdot e_i\| |h_i| \\
&\leq \left(\sum_{i=1}^n \|E(k) \cdot e_i\|\right) \|h\| 
= \left(\sum_{i=1}^n \|\varepsilon_{e_i}(k)\|\right) \|h\|
\end{split}
$$
donc la norme d'opérateur de $E(k)$ vérifie
$$
\|E(k)\| \leq \sum_{i=1}^n \|\varepsilon_{e_i}(k)\| \to 0
\, \mbox{ quand } k \, \to 0,
$$
ce qui prouve le résultat cherché.

### TODO - Variation d'ordre 1 manquante

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

### Variation et différentielle d'ordre deux {.lemma #D2d2}
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

### Variation de la différentielle {.theorem} 
Si $f: U \subset \mathbb{R}^n \to \mathbb{R}^m$ est une fonction 
deux fois différentiable en $x \in U$,
$$
df(x+k) = df(x) + d^2 f(x) \cdot k + E(k)(\|k\|)
$$
où $\lim_{k \to 0} E(k) = 0 \in \R^{m\times n}$.

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
toute paire d'indice $i$ et $j$ la dérivée partielle $\partial^2_{ij} f(x)$
existe et 
$$
\partial^2_{ij} f(x) = \partial^2_{ji} f(x) = d^2 f(x) \cdot e_i \cdot e_j.
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




Différentielle d'ordre supérieur
================================================================================

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


Exercices
================================================================================

### TODO : diff du produit matriciel

### TODO : diff du déterminant.

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


Différentiation matricielle
--------------------------------------------------------------------------------

Source: [@Tao13]

\newcommand{\tr}{\mathrm{tr} \,}

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

Solutions
================================================================================


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
