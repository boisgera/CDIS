% Calcul Différentiel II

TODO, à trier, idées en vrac:

  - e.v.n fonctionnels ($C^k$, $L^1$, $L^2$, etc.), Hilbert, Banach.

  - opérateurs linéaires continus (bornés), adjoint (appli calcul diff, 
    par exemple pour calcul solution diff EDP sans recalcul ?)
   
  - différentielle (Fréchet), cas général

En fait va plus loin que le scope du calcul diff, 
contient un mini "topo en dim infinie" (qu'est-ce qui change ?
Compacité (en particulier ppté vraie sur les compacts ne donne plus
le semi-global, ppté de type Ascoli-Arzela pour caractériser la compacité
pour les fcts continues), non-équivalence des normes, dualité, 
topologie faible ?) 
et algèbre linéaire en dim infinie (opérateurs linéaires 
ne sont pas tous cont., pas de chance ... Hilbert, Banach, etc). 

Prérequis: Topo, Calcul Diff dim finie, sans doute l'intégrale
(les critères intégraux sont une grande motivation pour enseigner
le calcul diff en dim infinie), c'est aussi sans doute l'endroit
ou on veut parler de la complétude des espaces comme $L^1 / L^2$, 
etc.

Exemples à traiter: "interpolation" données non-paramétrique, 
calcul des variations, maximum entropie sous contrainte, 
diff. / chemin (ex: usage en analyse complexe), 
optimisation/gradient forme, etc. Autre exemple: quantif 
qui optimise le SNR ou l'entropie. Autre exemple: Pb de Dirichlet
variationel ? On peut faire ça ? Et lier ça au Laplacien ? 
Ou il il faut un cadre compliqué (trace & co) ?

Articulation avec Physique Fonda. et Appliquée (calc var, Hilb, etc.).
Volonté de permettre de comprendre des trucs comme la construction de
Fourier (prolgt opé lin con à partir d'un ensemble dense avec majoration),
ou typiquement, définition de la trace sur un bord régulier ...

  - Topo en dim infinie, Banach, Hilbert, opérateurs lin cont, 
    analyse spectrale

  - Calcul diff en dim infinie (acc. fini, cont df, inversion locale, 
    point critique et multiplicateurs de lagrange, etc.,
    tout ça revisité rapidement en se basant sur la familiarité
    avec la dim finie, déjà vue).

--------------------------------------------------------------------------------

### Différentielle de Fréchet {.definition}
Soient $E$ et $F$ deux espaces vectoriels normés et $U$ un ouvert de $E$.
La fonction $f: U \to F$ est *différentiable en $x \in U$* s'il existe
une application linéaire continue, notée $df(x)$ et appellée 
*différentielle de $f$ en $x$*, telle que
$$
f(x+h) = f(x) + df(x) \cdot h + o(\|h\|_E),
$$
c'est-à-dire si 
$$
\lim_{h \to O} \frac{f(x+h) - f(x) - df(x) \cdot h}{\|h\|_E} = 0.
$$


### TODO
 $F$ **et $G$ complets **? Ah ouais, conséquence de $\partial_2 f$
homéomorphisme linéaire. Mmmm au passage $u: E \to F$ linéaire cont
est un homéomorphisme ssi il est bijectif (théo de Banach)

### Théorème des Fonctions Implicites {.theorem #TFI-2}
Soient $E$, $F$ et $G$ trois espaces vectoriels normés, $F$ étant complet, 
et $f$ une fonction définie sur un ouvert $W$ de $E \times F$
$$
f: (x, y) \in W \subset \mathbb{R}^n \times \mathbb{R}^m \to f(x, y) \in \mathbb{R}^m
$$
qui soit continûment différentiable et telle que la différentielle partielle
$\partial_y f$ soit inversible en tout point de $W$.
Si le point $(x_0, y_0)$ de $W$ vérifie $f(x_0, y_0)= 0$,
alors il existe des voisinages ouverts $U$ de $x_0$ et $V$ de $y_0$ tels que
$U \times V \subset W$ et
une fonction implicite $\psi: U \to F$, continûment différentiable, 
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

Exercices
================================================================================

Gradient de Forme
--------------------------------------------------------------------------------

(dérivée une fonctionnelle dépendant de la géométrie en transportant la
géomtrie par $I+u$, puis dérivée par rapport à $u$ ?)

$Omega$ dans $U$ paramétrisé par une déformation $T = I + u$ avec $u$ petit
et une base $\Omega_0$ qui est un compact à bords $C^1$.
Différencier le volume de $\Omega$ par rapport $T$ (chgt de variable, etc), 
utiliser Stokes, montrer que la différentielle ne dépend que de 
$\left<V, n\right>$.


Théorème de Cauchy Intégral
--------------------------------------------------------------------------------

Montrer la version circulaire, sous l'hypothèse que $f$ est de différentielle
$\mathbb{C}$-linéaire et continue (en faisant une chain rule en dim infinie)
... mais est-ce vraiment nécessaire ? Ne peut-on pas calculer les dérivées
par rapport au centre et au rayon sans ça, avec uniquement la dérivation
"point par point" et les résultats de convergence dans les intégrales ?