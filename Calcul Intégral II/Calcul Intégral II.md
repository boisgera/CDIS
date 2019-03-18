% Calcul Intégral II
% Sébastien Boisgérault

Perspective:

  - le théorème de convergence dominé est requis techniquement dans certaines
    preuves et également pour donner une perspective sur la démarche.
    Mais sa preuve, ses conséquences, variantes, etc. non, ce qui peut
    suggérer une "preview" de ce résultat et un développement plus complet
    ultérieurement. On a "besoin" du DCT et de son corollaire qu'une fct
    est intégrable ssi elle est bornée par des fcts intégrables et mesurable.

  - Justifier l'introduction des ensembles mesurables ... par la recherche
    d'une notion de "volume" (longueur/aire/...) suffisamment générale ?
    Oui, en généralisant ce qui se passe pour les intervalles.
    Et les ensembles mesurables sont ceux dont la mesure ne pose pas de pb
    à part qu'ils sont "trop grands".
    Introduire mesure de Lebesgue à ce stade, est possible, 
    $\sigma$-algèbres, etc. Nécessaire dans la manip des fcts mesurables.

    Cross-justifier la notion de fonction absolument mesurable 
    (concept "stable" par multiplication par la fonction caractéristique
    d'un ensemble mesurable.)

    Probablement inclure plus généralement la pbmatique des fcts 
    absoluments continues ici. Deux axes: intégrer sur des sous-ensembles
    "plus généraux" et de façon général, meilleur comportement par rapport
    aux opération usuelles: le produit borné abs int et abs int est abs int;
    ça n'est pas le cas pour les fcts simplement intégrables, ce qui est
    compliqué! Le pb du "multiplier" de fcts intégrable (égal pp à une fct
    de variation bornée), c'est too much ...

  - Justifier l'introduction des fonctions mesurables. Elle contribuent
    à résoudre le problème suivant: comment montrer qu'une fonction est
    intégrable ? On décompose cette question en deux parties indépendentes: 
    montrer que la fonction est "bornée" et est "assez régulière".
    Des exemples bien choisis doivent être utilisés pour mesurer les
    progrès dans cette direction (avant/après). Etudier en conjonction
    le pb des "multipliers" (Swartz) ?

  - Mener toute la présentation dans $\mathbb{R}$.
   
Ensembles mesurables
================================================================================

### Ensemble mesurable {.definition}

Un ensemble $E$ de $\mathbb{R}$ est *mesurable* si pour tout intervalle
$[a, b]$ compact de $\mathbb{R}$, la fonction caractéristique de 
l'intersection de $E$ et de $[a, b]$ 
$$
x \in \mathbb{R} \mapsto \{x \in E \mbox{ et } x \in [a, b]\}
$$
est intégrable.

--------------------------------------------------------------------------------

(expliquer ensembles infinis, problématique de régularité mais pas de taille)


### Propriétés des ensembles mesurables {.theorem}

 1. L'ensemble vide est mesurable.

 2. L'ensemble des points n'appartenant pas à un ensemble mesurable est mesurable.

 3. L'union d'une collection finie ou dénombrable d'ensembles mesurables,
    est mesurable.

 4. Tout ensemble ouvert est mesurable.

### Preuve {.proof}

**TODO.**

--------------------------------------------------------------------------------

### Tribu / $\sigma$-algèbre {.definition}

**TODO:** $\sigma$-algèbre, "calculs"/notations associées, Boréliens, 
perspective par rapport à supra.


Fonctions mesurables
================================================================================

Perspective: "relâcher" la contrainte sur le caractère "borné" des fonctions
intégrables. D'où la définition (à préciser dans le contexte de la conséquence
du DCT ? Préciser ...)

### Fonction mesurable {.definition}
Une fonction $f:\mathbb{R} \mapsto \mathbb{R}$ est *mesurable* 
si elle est la limite simple d'une suite de fonctions intégrables 
$f_k:\mathbb{R} \mapsto \mathbb{R}$.

**TODO:** (définir puis) montrer que "localement intégrable" n'est pas le
bon/même concept? Mais que localement intégrable est mesurable ?

### Les fonctions intégrables sont mesurables

... trivial

### Les limites simples de fonction mesurables sont mesurables.

... facile, en diagonalisant.

### Les fonctions continues sont mesurables

... car elle sont localement intégrables.

### Composition par fonction continue

Super important pour applications ($\lambda f+ \mu g$, $f \times g$,
$f \wedge g$, etc.). Peut se montrer dès maintenant ou nécessite
carac par les image réciproques ? (pour le moment, par les images 
réciproques (NOTE: nécessite le cas $n$-dimensionnel pour les
fcts réciproques, mais ça n'est pas méchant si? Non.) donc à mettre après; 
je ne sais pas si on peut y arriver
directement -- en utilisant le critère de Cauchy ?)

### Carac par les images réciproques {.theorem}

**TODO:** différents "niveaux" de l'ascenseur. De $\leftrightarrow$ à la 
version minimaliste $\{x \in \mathbb{R} \; | \; f(x) \leq c\}$ mesurable
pour tout $c \in \mathbb{R}$ à l'image réciproque de tout Borélien est 
mesurable ("nécessaire" ?).

### Preuve. 

Ouch. Un coté se fait bien et la technique est intéressante 
(mq si les images réciproques sont mesurables, on peut exhiber une approx
simple de fcts intégrables, et même "étagées", qui se prête bien à des
desseins et servira pour la construction abstraite de l'intégrale de 
Lebesgue.)

Au passage, la construction permettra de montrer que les fcts mesurables
sont des limites de fonctions absolument intégrables.

L'autre coté -- sauf si une voie plus facile existe -- suppose de nombreux
résutats techniques, certains intéressants en soi. Il s'agit de combiner:
l'existence p.p. d'une dérivée pour une fonction intégrables (intéressant
mais compliqué: nécessite recouv de Vitali a priori), ce qui permet de 
montrer que tout fct intégrable est limite p.p. de fonctions continues,
ce qui est la clé (puisque -- à montrer -- la carac par les image réciproque
est robuste / à p.p., englobe les fcts continues et est stable par passage
à la limite. Beacoup de "redites" nécessaires par rapport aux notions dvlpées
plus haut, mais avec une def alternative ...).