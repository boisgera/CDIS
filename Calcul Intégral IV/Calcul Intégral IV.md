% Calcul Intégral IV

<!-- LaTeX Macros -->
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}

Mesure et intégrale
================================================================================

On rappelle:

### Tribu {.definition}
Une *tribu* ou *$\sigma$-algèbre* $\mathcal{A}$ sur un ensemble $X$ est une 
collection d'ensembles de $X$ contenant l'ensemble vide et stable par passage 
au complémentaire et à l'union dénombrable. 
Un ensemble de $\mathcal{A}$ est dit *mesurable* ; 
l'ensemble $X$ muni de $\mathcal{A}$ est un *espace mesurable*.

### Tribu engendrée par une collection {.definition}
Dans un ensemble $X$, on appelle *tribu engendrée* par une collection 
$\mathcal{C}$ d'ensembles de $X$ la plus petite (au sens de l'inclusion) 
tribu $\mathcal{A} = \sigma(\mathcal{C})$ de $X$ contenant $\mathcal{C}$.

### Démonstration de l'existence de la tribu engendrée {.proof}
Désignons par $\mathfrak{S}$ la (meta-)collection des tribus de 
$X$ incluant $\mathcal{C}$ (contenant $\mathcal{C}$ comme sous-ensemble). 
Elle n'est pas vide : elle contient la collection $\mathcal{P}(X)$
des ensembles de $X$ (qui de toute évidence est un sur-ensemble de $\mathcal{C}$
et une tribu de $X$). Montrons que la plus petite tribu $\sigma(\mathcal{C})$
de $X$ contenant $\mathcal{C}$ est l'intersection de $\mathfrak{S}$:
$$
\sigma(\mathcal{C}) := \bigcap \mathfrak{S} = \bigcap_{\mathcal{A} \in \mathfrak{S}} \mathcal{A},
$$
ou encore
$\sigma(\mathcal{C}) = \{A \subset X \, | \, A \in \mathcal{A} \mbox{ pour tout } \mathcal{A} \in \mathfrak{S}\}.$
Il est clair que si $\mathcal{A}$ est une tribu de $X$ contenant $\mathcal{C}$,
alors $\mathfrak{S} \subset \mathcal{A}$, car alors $\mathcal{A} \in \mathfrak{S}$.
Il nous suffit donc de montrer que $\cap \mathfrak{S}$ est une tribu de $X$
pour conclure ; on vérifiera aisément que comme chaque élément de $\mathfrak{S}$
est une tribu, cette intersection en est également une.

### Tribu de Lebesgue {.definition}
On appelle *tribu de Lebesgue* sur $\R^n$ la tribu composée des ensembles $E$
tels que pour tout pavé $P$ de $\R^n$, la fonction caractéristique 
de $E \cap P$ soit intégrable (au sens de Henstock-Kurzweil).

### {.post}
La tribu de Lebesgue est donc composée des ensembles mesurables au sens
du chapitre "Calcul Intégral III".

### TODO -- Référence
Lier au chapitre "Calcul Intégral III" en détail.

### Tribu de Borel {.definition}
On appelle *tribu de Borel* d'un espace topologique $X$ la plus petite tribu
contenant tous les fermés (ou tous les ouverts) de $X$.


### Mesure {.definition}
Une *mesure (positive)* $\mu$ sur un espace probabilisable $(X, \mathcal{A})$
est une fonction de $\mathcal{A}$ dans $[0, +\infty]$ telle que $\mu(\varnothing)= 0$
et pour toute collection dénombrable $\{A_1,\dots, A_k, \dots\}$ d'ensembles de
$\mathcal{A}$ disjoints deux à deux, on ait
$$
\mu \left( \bigcup_{k} A_k \right) = \sum_{k} \mu(A_k) ;
$$
on dit que $\mu$ est *$\sigma$-additive*.
L'ensemble $X$ muni de $\mathcal{A}$ et $\mu$ est un *espace mesuré*.

### Fonction mesurable
Une fonction $f: X \to Y$ associée aux espaces mesurables $(X, \mathcal{A})$
et $(Y,\mathcal{B})$ est *mesurable* si l'image réciproque $A =f^{-1}(B)$
de tout ensemble $B$ de $\mathcal{B}$ par $f$ appartient à $\mathcal{A}$.

### Conventions
Lorsque $Y = \R^m$, on supposera par défaut que la tribu associée est la
tribu de Borel, et lorsque $X = \R^n$, que la tribu associée est la tribu
de Lebesgue. Lorsque l'on souhaitera munir également $X$ de la tribu de Borel,
on parlera de fonctions *borélienne* (tribu de Borel au départ et à l'arrivée),
mais il existe une bonne raison pour ne pas prendre cette convention par 
défaut:

### Mesurable / mesurable
Une fonction $f:\R^n \to \R^m$ est mesurable au sens du chapitre III, 
c'est-à-dire limite simple de fonctions intégrables si et seulement si
elle est mesurable au sens de ce chapitre, quand $\R^n$ est muni de la
tribu de Borel et $\R^m$ de la tribu de Lebesgue.

### TODO -- Démonstration {.proof}

### Intégrale d'une fonction positive