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