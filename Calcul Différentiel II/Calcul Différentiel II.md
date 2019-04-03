% Calcul Différentiel II


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
    la physique (ex: thermo). Etudier un scope raisonnable. Cf Salamon
    sur scope géom diff ?

Analyse d'Erreur
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
est appelée; cet appel n'est donc pas tracé.
**OUCH, compliqué,** parce que ça va "réussir" et il faut la forcer à échouer,
et pour ce faire, ne *pas* dériver de `float`. Parfait, c'est le moment 
d'introduire `Node` !


Exercices
================================================================================

Déformations
--------------------------------------------------------------------------------

Usage IFT pour montrer que les formes de type $I+u$ sont des difféo pour 
$u petit. (le gradient de forme qui pourrait être sympa doit trouver
sa place dans la session 3)

Différentiation à pas complexe
--------------------------------------------------------------------------------

**TODO**