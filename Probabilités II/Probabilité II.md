% Probabilités II

\newcommand{\R}{\mathbb{R}}
\newcommand{\Q}{\mathbb{Q}}
\renewcommand{\P}{\mathbb{P}}
\renewcommand{\C}{\mathbb{C}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\A}{\mathcal{A}}
\newcommand{\E}{\mathcal{E}}
\newcommand{\B}{\mathcal{B}}


## Loi d'une variable aléatoire

En théorie moderne des probabilités, on préfère prendre un point de vue fonctionnel plutôt qu’ensembliste, et utiliser les variables aléatoires plutôt que les événements. Ce point de vue sera développé dans la suite du cours. Nous en donnons ici uniquement les idées de base.

Une variable aléatoire est une grandeur qui dépend du résultat de l’expérience. Par exemple,

 * le nombre de 6 obtenus dans un lancer de 3 dés,
 * le nombre d’appels dans un central téléphonique pendant une heure,
 * la distance du point d’atteinte d’une flèche au centre de la cible,
 * la valeur maximale d’un prix d’actif sur un intervalle de temps donné,
sont des variables aléatoires.


La définition formelle d'une variable aléatoire fait intervenir des éléments de la théorie de la mesure. Dans un premier temps, on retiendra qu'étant donné un espace probabilisé $(\Omega, \A, \P)$, une variable aléatoire $X$ est une application de $(\Omega,\A)$ dans un ensemble $E$,
\begin{equation}
\omega \in \Omega \mapsto X(\omega) \in E
\end{equation}

En pratique, l’ensemble $E$ pourra être un ensemble fini ou dénombrable ou $R$ ou $R^d$ ou encore un espace plus sophistiqué tel que l’ensemble $C(\R_+ , \R^d)$ des fonctions continues de $\R_+$ dans $\R^d$.

### Remarque {.remark}
La terminologie, consacrée par l'usage, peut être trompeuse. Une variable aléatoire n'est pas une variable (au sens de l'analyse) mais une fonction. Cette terminologie est apparentée à la notion de variable en physique ou en sciences humaines où on désigne volontiers par "variable" la valeur prise par une fonction de l'état du système étudié.

L'intérêt principal de travailler avec des variables aléatoires est de pouvoir substituer à l'espace abstrait $\Omega$ des résultats de l'expérience l'espace $E$, mieux connu dans la pratique. Ainsi, grâce à une variable aléatoire $X$, nous pouvons transporter la structure abstraite du modèle probabiliste $(\Omega, \A, \P)$ sur l'espace d'arrivée $E$, en posant pour $B \in E$
\begin{equation}
\label{eq:loi_va}
\P_X (B ) = \P(X^{-1}(B)) = \P(\{\omega, X(\omega)\in B\})
\end{equation}
Cette formule défini une nouvelle probabilité, notée $\P_X$ et définie sur $E$, qui s'appelle la *loi de la variable* $X$.

Comme $\P(A)$ n'est définie que pour les $A$ de la tribu $\A$, la formule \eqref{eq:loi_va} ne permet de définir $\P_X(B)$ que pour les ensembles $B$ tels que $X^{-1}(B) \in \A$, d’où l’importance de la proposition suivante :

### Proposition {.proposition}

 a) La famille $\E$ des parties $B$ de $E$ telles que $X^{-1}(B) \in \A$ est une tribu de $E$.
 b) L'application $\P_X$ définie pour $B \in \E$ par 
 $$ \P_X (B ) = \P(X^{-1}(B)) $$ 
 définit une probabilité sur le couple $(E,\E)$.

### Démonstration {.proof}
Les 3 propriétés de la [définition d'une tribu](#deftribu) pour $\E$ ainsi que les deux propriétés de la [définition de la probabilité](#defproba) pour $\P_X$ découlent immédiatement des mêmes propriétés pour $\A$ et $\P$, une fois remarquées les propriétés élémentaires suivantes :
\begin{align*}
& X^{-1}(\varnothing) = \varnothing, X^{-1}(E) = \Omega, X^{-1}(B^c) = X^{-1}(B)^c \\
& X^{-1}(\cap_i A_i) = \cap_i X^{-1}(A_i), X^{-1}(\cup_i A_i) = \cup_i X^{-1}(A_i)
\end{align*}

### {.anonymous}

Les variables que nous rencontrerons dans ce cours seront soit à valeurs dans un ensemble dénombrable, soit à valeurs dans $\R$ ou dans $R^d$. Nous les appellerons respectivement des variables aléatoires discrètes, réelles ou des vecteurs aléatoires. Leurs lois seront alors des probabilités respectivement sur un ensemble dénombrable, sur $\R$ ou sur $R^d$. Les probabilités sur un espace fini ou dénombrable sont considérées connues. La description des probabilités sur $\R$ ou sur $R^d$ est plus délicate et fera l'objet de l'essentiel de ce cours.


# Variables aléatoires réelles

# Variables aléatoires de loi à densité

# Moments d'une V.A. a densité

# Calculs de loi (cf Jacod - Garnier)

# Lois usuelles (annexe)

# Exercices

