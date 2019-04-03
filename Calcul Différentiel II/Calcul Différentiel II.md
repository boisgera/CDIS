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
    la physique (ex: [thermo](https://fr.m.wikipedia.org/wiki/Gaz_parfait)). 
    Etudier un scope raisonnable. Cf Salamon sur scope géom diff ?

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
    ...         cos_x = Node(cos_x_value, cos, x)
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

Puis, faisons en sorte qu'elle soit utilisée par défaut 
plutôt que la représentation standard des objets:

    >>> Node.__str__ = Node.__repr__ = node_repr

Nous somme prêts à faire notre vérification:

    >>> f = lambda x: 1.0 + cos(x)
    >>> end = trace(f, [pi])
    >>> print(end)
    Node(0.0, add, [Node(-1.0, cos, Node(3.141592653589793)), Node(1.0)])

Le résultat se lit de la façon suivante: le calcul de `f(pi)` produit 
la valeur `0.0`, issue de l'addition de `-1.0`, 
calculé comme `cos(3.141592653589793)` et de la constante `1.0`.
Cela semble donc correct !


Exercices
================================================================================

Déformations
--------------------------------------------------------------------------------

Usage IFT pour montrer que les formes de type $I+u$ sont des difféo pour 
$u petit. (le gradient de forme qui pourrait être sympa doit trouver
sa place dans la session 3)

Racines d'un Polynôme
--------------------------------------------------------------------------------

Si racine simple, variation continue (et plus) par rapport aux coefficients.

Différentielle de $X \mapsto X^{-1}$
--------------------------------------------------------------------------------

Différentiation à pas complexe
--------------------------------------------------------------------------------

**TODO**