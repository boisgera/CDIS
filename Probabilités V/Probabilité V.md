% Probabilités V

\newcommand{\R}{\mathbb{R}}
\newcommand{\Q}{\mathbb{Q}}
\renewcommand{\P}{\mathbb{P}}
\renewcommand{\C}{\mathbb{C}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\A}{\mathcal{A}}
\newcommand{\E}{\mathcal{E}}
\newcommand{\B}{\mathcal{B}}
\renewcommand{\L}{\mathcal{L}}
\newcommand{\Esp}{\mathbb{E}}
\newcommand{\V}{\mathbb{V}}
\newcommand{\cov}{\text{Cov}}
\renewcommand{\No}{\mathcal{N}}


# Intégrale de Monte-Carlo

Les méthodes de Monte-Carlo ont été développées initialement par des physiciens dans les années 1950 (voir les travaux de Metropolis, Ulam, Hastings et
Rosenbluth) pour calculer des intégrales (déterministes) à partir de méthodes probabilistes numériquement assez économiques. Le nom a été donné par référence
au célèbre casino du fait du caractère alétoire de ces méthodes.

Les méthodes de simulation sont basées sur la production de nombres aléatoires, distribués selon une certaine loi de probabilité. 
Dans de nombreuses applications, pour une certaine fonction $h$, on souhaite calculer, pour une variable aléatoire $X$ de loi $\P_X$
$$ \mathcal{I}=\Esp\left(h(X)\right)=\int_{\R^d} h(x) \P_X(dx),$$

En général, même si on sait évaluer $h$ en tout point, on ne peut pas calculer formellement l'intégrale $\mathcal{I}$, notamment quand $d$ est grand. Le calcul d'intégrale par la méthode Monte-Carlo consiste dans sa version la plus simple à générer $(X_1,\ldots,X_n) \sim_{i.i.d.}\P_X$, et à
approcher $\mathcal{I}$ par la moyenne empirique 
$$M_n(h)=\frac{1}{n}\sum_{i=1}^{n}h(x_i),$$
où i.i.d signifie indépendant et identiquement distribué. En effet, d'après la loi forte des grands nombres, si $h(x)$ est $\P_X$-intégrable, on a l'assurance que
$$M_n(h) \rightarrow \int h(x)\P_X(dx) \text{ p.s.}$$
Si de plus, $h(X)^4$ est intégrable la vitesse de convergence de $M_n(h)$ peut être évaluée,
puisque la variance
$$\V(M_n(h)) = \frac{1}{n} \int \left(h(x)-\mathcal{I}\right)^2 \P_X(dx)$$
peut également être estimée à partir de l'échantillon
$(X_1,\ldots,X_n)$ par la quantité
$$\sigma_n^2=\frac{1}{n}\sum_{i=1}^{n}\left( h(x_i)-M_n(h)\right)^2.$$
Le théorème central limite assure alors que pour $n$ grand,
$$\frac{M_n(h)-\mathcal{I}}{\sigma_n}$$
suit approximativement une loi $\No(0,1)$[^foot1]. Cette propriété conduit à la construction de tests de convergence et de bornes de
confiance asymptotiques pour $M_n(h)$. Par exemple, on aura
$$\P\left(\mathcal{I} \in \left[M_n(h) - 1.96 \sigma_n,M_n(h) + 1.96 \sigma_n\right]\right) \approx 0.95,$$
où on a $1.96 = \Phi^{-1}(0,975)$ avec $\Phi$ la fonction de répartition de la loi normale centrée réduite.

En outre, cette propriété indique que la vitesse de convergence de $M_n(h)$ est de l'ordre de $\sqrt{n}$ et ce indépendamment de la dimension du problème. Cela explique l'efficacité de cette méthode par rapport aux méthodes d'intégration numérique déterministes dont les vitesses de convergence décroissent rapidement avec la dimension du problème.

[^foot1]: ce résultat sera démontré dans le cours de science des données au second semestre.


# Génération de nombres pseudo-aléatoires

Les ordinateurs sont des machines déterministes. Il peut sembler paradoxal de leur demander de générer des nombres aléatoires. En réalité, les algorithmes de génération de nombres aléatoires vont générer des séquences de nombres déterministes qui vont avoir l'aspect de l'aléatoire. On s'intéresse ici à la génération de nombres uniformes sur $[0,1]$, puisque, comme on le verra dans la suite, il s'agit de l'ingrédient de base de toutes les méthodes de simulation stochastique.

### Définition --- Générateur de nombres uniformes pseudo-aléatoires {.definition} 
Un *générateur de nombres uniformes pseudo-aléatoires* est un algorithme qui étant donné une valeur initiale $u_0$ et une transformation $T$ produit une séquence $u_i=T^i(u_0),\,\,\,i \in\N$ de valeurs dans [0,1]. Pour tout $n$, les valeurs $(u_1,\ldots,u_n)$ reproduisent le comportement d'une suite de variables aléatoires $(V_1,\ldots,V_n)$ i.i.d de loi uniforme sur [0,1], lorsqu'on les compare au travers d'un ensemble de tests statistiques[^diehard], par exemple que la corrélation entre deux nombres successifs soit suffisamment faible.

[^diehard]: Par exemple, la suite de tests [Die Hard](https://en.wikipedia.org/wiki/Diehard_tests), due à Marsaglia.

### Exemple : la méthode des congruences {.example}
Cet alorithme, dû à Lehmer (@Lehmer) au début des années 50, est l'un des premiers à avoir été proposé et implémenté. Il est basé sur 2 paramètres :
 
 - le multiplicateur $a$
 - le modulo $m$

Etant donné $u_0\in ]0,1[$, la séquence de nombres est générée par la transformation suivante :
$$u_{n+1} = \frac{(m\,a\,u_{n}) \mathrm{\,mod\,} m}{m}$$

On peut remarquer que l'algorithme va produire une séquence de nombre qui sera périodique, c'est-à-dire qu'après un certain nombre d'itérations, la suite se répétera et qu'il pourra fournir au plus $m-1$ valeurs différentes. Ce trait est commun à tous les générateurs de nombre aléatoires et est lié aux limitations matérielles des ordinateurs (on ne peut représenter qu'un nombre fini de nombres). Le choix des valeurs de $a$ et $m$ est par conséquent crucial. Il existe des critères qui permettent de s'assurer du bon comportement de cette suite :

 * $m$ est un nombre premier (le plus grand possible)
 * $p = m-1 /2$ est un nombre premier
 * $a^p = -1 \mathrm{\,mod\,} m$

Ce critère assure une période pleine et donc que tous les nombres $(1/m,\ldots,(m-1)/m)$ seront générés. Cependant, les nombres générés ne sont pas indépendants, pas même non corrélés. On peut montrer que la corrélation entre 2 nombres successifs vaut approximativement $1/a$. Il convient donc de choisir $a$ suffisamment grand pour que celle-ci devienne négligeable. Par exemple, en prenant $a=1000$ et $m=2001179$, on obtient une période de $2001178$ et une corrélation de l'ordre de $10^{-3}$.

Ce générateur de nombres uniformes pseudo-aléatoires, bien que rudimentaire, a ouvert la voie à des générateurs plus sophistiqués, toujours basés sur des opérations arithmétiques. Le plus couramment utilisé est l'algorithme de [Mersenne-Twister](https://en.wikipedia.org/wiki/Mersenne_Twister) et est le générateur par défaut de la plupart des logiciels tels que Python, R, MATLAB, Julia, MS Excel,... Il passe notamment avec succès toute la batterie de tests Die Hard. En particulier, sa période vaut $2^19937 - 1$.

Pour certains usages, cet algorithme n'est cependant pas recommandé du fait de sa prédictibilité. C'est notamment un défaut rédhibitoire pour les applications en cryptographie. Il existe des variantes mieux adaptées à ce cas de figure. On notera enfin qu'il existe des générateurs de nombres aléatoires basés sur des phénomènes physiques comme un bruit électrique ou des phénomènes quantiques et donc parfaitement imprévisibles.


# Méthodes de simulation de v.a.
 * inversion
 * rejet
 * box-muller

# Simulation d'un vecteur gaussien à densité
La simulation d'un vecteur gaussien dont la matrice de covariance est inversible est extrêmement aisée. En effet, soit un vecteur gaussien $X = (X_1,\ldots,X_n)$ à valeurs dans $\R^n$ d'espérance $m$ et de matrice de covariance $C$ définie positive. 

Puisque la matrice $C$ est inversible, elle admet une racine carrée. En effet, on peut décomposer $C$ de la manière suivante :
$$C = V D V^t$$
où $V$ est une matrice orthogonale et $D$ est la matrice diagonale dont les termes diagonaux sont les valeurs propres (toutes strictement positives) de $C$.

Soit maintenant un autre vecteur gaussien $Y = (Y_1,\ldots,Y_n)$ à valeurs dans $\R^n$ et de matrice de covariance l'identité. Autrement dit, les $Y_i$ sont des variables aléatoires gaussiennes centrées, réduites et indépendantes.

# Echantillonnage d'importance