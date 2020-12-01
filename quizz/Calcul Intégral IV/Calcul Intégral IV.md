% Calcul Intégral IV

<!-- LaTeX Macros -->
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}
\newcommand{\tr}{\operatorname{tr}}

\newcommand{\zero}{$\mathord{\boldsymbol{\circ}}$}
\newcommand{\one}{$\mathord{\bullet}$}
\newcommand{\two}{$\mathord{\bullet}\mathord{\bullet}$}
\newcommand{\three}{$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$}
\newcommand{\four}{$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$}

#### Question 1 (réponses multiples)
Soit $X = \R^3$ et $\mathcal{A} = \mathcal{P}(X)$, l'ensemble des parties de $X$.
On définit pour tout $X \in \mathcal{A}$ la grandeur $\mu(A)$ comme le diamètre de $A$ :
$$
\mu(A) := \mathrm{diam}(A) := \sup \, \{\|x - y\| \; | \; (x, y) \in A \times A\} \in [0, +\infty].
$$
Est-ce que $\mu$ est une mesure sur $(X, \mathcal{A})$ ?

  - [ ] A : Non, car $\mathcal{A}$ n'est pas une tribu,

  - [ ] B : Non, car $\mu$ n'est pas nulle en 0,

  - [ ] C : Non, car $\mu$ n'est pas $\sigma$-additive,

  - [ ] D : Oui.


#### Question 2 (réponses multiples) 
Si $\mu$ et $\nu$ sont des mesures sur le même espace mesurable $(X, \mathcal{A})$,
$\alpha \in \R$ et $f: [0, +\infty] \to [0, +\infty]$ est continue, 
alors

  - [ ] A : $\mu + \nu$ est une mesure,

  - [ ] B : $\alpha \mu$ est une mesure,

  - [ ] C : $f\circ \mu$ est une mesure. 

#### Question 3
Soit $c$ la mesure de comptage sur $\R$ (muni de la tribu $\mathcal{P}(\R)$).
Deux fonctions $f:\R\to \R$ et $g:\R\to\R$ sont égales $c$-presque partout si
et seulement si :

  - [ ] A : $f$ et $g$ sont identiques,

  - [ ] B : $f$ et $g$ diffèrent au plus en un nombre fini de points,

  - [ ] C : la longueur de $\{x \in \R \; | \; f(x) \neq g(x)\}$ est nulle,

  - [ ] D : est vrai sans condition sur $f$ et $g$.
