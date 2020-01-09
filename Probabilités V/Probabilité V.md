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

Les méthodes de Monte-Carlo ont été développées initialement par des physiciens dans les années 1950 (notamment par les travaux de Metropolis, Ulam, Hastings,
Rosenbluth) pour calculer des intégrales (déterministes) à partir de méthodes probabilistes numériquement assez économiques. Le nom a été donné par référence
au célèbre casino du fait du caractère alétoire de ces méthodes.

Les méthodes de simulation sont basées sur la production de nombres aléatoires, distribués selon une certaine loi de probabilité. 
Dans de nombreuses applications, pour une certaine fonction $h$, on souhaite calculer, pour une variable aléatoire $X$ de loi $\P_X$
$$ \mathcal{I}=\Esp\left(h(X)\right)=\int_{\R^d} h(x) \P_X(dx),$$

En général, même si on sait évaluer $h$ en tout point, on ne peut pas calculer formellement l'intégrale $\mathcal{I}$, notamment quand $d$ est grand. Le calcul d'intégrale par la méthode Monte-Carlo consiste dans sa version la plus simple à générer un *échantillon* $(X_1,\ldots,X_n) \sim_{i.i.d.}\P_X$, et à
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

Les ordinateurs sont des machines déterministes. Il peut sembler paradoxal de leur demander de générer des nombres aléatoires[^vn]. En réalité, les algorithmes de génération de nombres aléatoires vont générer des séquences de nombres déterministes qui vont avoir l'aspect de l'aléatoire. On s'intéresse ici à la génération de nombres uniformes sur $[0,1]$, puisque, comme on le verra dans la suite, il s'agit de l'ingrédient de base de toutes les méthodes de simulation stochastique.

[^vn]:Von Neumann (1951) résume ce problème très clairement : "Any one who considers arithmetical methods of reproducing random digits is, of course, in
a state of sin. As has been pointed out several times, there is no such thing as a random number --- there are only methods of producing random numbers, and a
strict arithmetic procedure of course is not such a method. "

### Définition --- Générateur de nombres uniformes pseudo-aléatoires {.definition} 
Un *générateur de nombres uniformes pseudo-aléatoires* est un algorithme qui étant donné une valeur initiale $u_0$ et une transformation $T$ produit une séquence $u_i=T^i(u_0),\,\,\,i \in\N$ de valeurs dans [0,1]. Pour tout $n$, les valeurs $(u_1,\ldots,u_n)$ reproduisent le comportement d'une suite de variables aléatoires $(V_1,\ldots,V_n)$ i.i.d de loi uniforme sur [0,1], lorsqu'on les compare au travers d'un ensemble de tests statistiques[^diehard], par exemple que la corrélation entre deux nombres successifs soit suffisamment faible.

[^diehard]: Par exemple, la suite de tests [Die Hard](https://en.wikipedia.org/wiki/Diehard_tests), due à Marsaglia.

### Exemple : la méthode des congruences {.example}
Cet alorithme, dû à Lehmer (@Lehmer) au début des années 50, est l'un des premiers à avoir été proposé et implémenté. Il repose sur 2 paramètres :
 
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
La simulation d'un vecteur gaussien dont la matrice de covariance est inversible est extrêmement aisée. En effet, on souhaite simuler un vecteur gaussien $X = (X_1,\ldots,X_d)$ à valeurs dans $\R^d$ d'espérance $m$ et de matrice de covariance $C$ définie positive donnés. 

Puisque la matrice $C$ est inversible, elle admet une racine carrée, c'est-à-dire qu'il existe une matrice $N$ telle que $C = N\,N^t$. En effet, on peut décomposer $C$ de la manière suivante :
$$C = V\,D\,V^t$$
où $V$ est une matrice orthogonale et $D$ est la matrice diagonale dont les termes diagonaux sont les valeurs propres (toutes strictement positives) de $C$. Il suffit alors de prendre $N = V\,D^{1/2}$, où $D^{1/2}$ est la matrice diagonale dont les termes diagonaux sont les racines carrées des valeurs propres. En pratique, il est souvent coûteux numériquement d'effectuer le calcul des valeurs propres et des vecteurs propres de $C$. On va plutôt calculer sa [décomposition ou factorisation de Cholesky](https://fr.wikipedia.org/wiki/Factorisation_de_Cholesky) qui permet d'écrire
$$C = L\,L^t$$
avec $L$ une matrice triangulaire inférieure [^chol].

[^chol]: Cette décomposition est très utile dans la résolution de systèmes linéaires de la forme $A\,x = b$, où $b$ est connu, $x$ inconnu et $A$ est définie positive. Cela revient à résoudre $L\,L^t\,x = b$. On pose alors $y = L^t\,x$ et on résoud d'abord $Ly=b$, ce qui est très rapide puisque $L$ est triangulaire inférieure (on commence par $y_1 = b_1/L_{11}$, puis $y_2 = (b_2 - L{21}y_1)/L_{22}, etc. en descendant). On résoud ensuite $L^t\,x = y$, ce qui est aussi très rapide pour la même raison (on commence par $x_n = y_n/L_{nn}$ puis on remonte).

Soit maintenant un autre vecteur gaussien $Y = (Y_1,\ldots,Y_d)$ à valeurs dans $\R^d$ et de matrice de covariance l'identité. Autrement dit, les $Y_i$ sont des variables aléatoires gaussiennes centrées, réduites et indépendantes.

Alors, le vecteur $Z = m + L\,Y$ est gaussien, d'espérance $m$ et de matrice de covariance $C$. En effet, $Z$ est gaussien comme combinaison linéaire de variables aléatoires gaussiennes, $\Esp(Z) = \Esp(m + L\,Y) = m$ et $\V(Z) = \Esp((L\,Y)^2) = L I_d L^t = C$.

# Echantillonnage d'importance

On introduit dans cette section la méthode d'échantillonnage d'importance (importance sampling en anglais), que l'on appelle aussi, de manière plus intuitive, échantillonnage préférentiel. Pour ce faire, nous allons commencer par un exemple qui montre qu'il peut être plus efficace de simuler des valeurs selon une loi différente de celle d'intérêt, autrement dit de modifier la représentation de l'intégrale $\mathcal{I}$ sous la forme d'une espérance calculée selon une mesure donnée.

Supposons que l'on s'intéresse à calculer la probabilité $p$ qu'une variable $X$ de loi de Cauchy standard soit plus grande que 2 (on peut le calculer directement et p=0.15)
$$p = \int_2^{+\infty} \frac{1}{\pi(1+x^2)}dx$$
Si on estime $p$ directement à partir d'un échantillon $(X_1,\ldots,X_n)$ simulé selon la loi de Cauchy standard soit
$$\widehat{p}_1 = \frac{1}{n}\sum_{i=1}^n 1_{X_i > 2},$$
la *variance de l'estimateur* $\V(\widehat{p}_1) = p(1-p)/n = 0.127/n$, puisque $\widehat{p}_1$ suit une loi binomiale de paramètre $(n,p)$. On peut réduire cette variance (et donc améliorer la qualité de l'estimateur) en tirant parti de la symétrie de la densité de la loi de Cauchy, en formant un second estimateur
$$\widehat{p}_2 = \frac{1}{n}\sum_{i=1}^n 1_{|X_i| > 2},$$
dont la variance vaut $\V(\widehat{p}_2) = p(1-p/2)/2n = 0.052/n$.

La relative inefficacité de ces méthodes est due au fait que la majeure partie des valeurs simulées seront en dehors de la zone d'intérêt $]2,+\infty[$. En passant par le complémentaire, on peut réécrire $p$ comme
$$p = \frac{1}{2} - \int_0^2 \frac{1}{\pi(1+x^2)}dx,$$
dont le second terme peut être vu comme l'espérance de $h(U) = \frac{2}{\pi(1+U^2)}$ avec $U\sim \mathcal{U}_{[0,2]}$. Tirant un échantillon $(U_1,\ldots,U_n)$ i.i.d. de loi uniforme sur $[0,2]$, on obtient un troisième estimateur :
$$\widehat{p}_3 = \frac{1}{2} - \frac{1}{n}\sum_{i=1}^n \frac{2}{\pi(1+U_i^2)},$$
dont la variance vaut $\V(\widehat{p}_3) = (\Esp(h(X)^2) - \Esp(h(U))^2)/n = 0.0285/n$ (par intégration par parties). Enfin, on peut encore réécrire (voir @ripley)
$$p = \int_0^{1/2}\frac{y^{-2}}{\pi(1+y^{-2})}dy,$$
qui peut être vue comme $\Esp(\frac{V^{-2}}{2\pi(1+V^{-2})}$ avec $V\sim \mathcal{U}_{[0,1/2]}$. L'estimateur formé à partir de cette représentation et d'un échantillon $(V_1,\ldots,V_n)$ i.i.d. de loi uniforme sur $[0,1/2]$ a une variance de $0.95 10^{-4}/n$. Il est donc bien plus efficace que $\widehat{p}_1$ puisqu'il nécessite environ $\sqrt{10^3}=32$ fois moins de simulations pour parvenir à la même précision.

On a ainsi vu sur ce cas particulier que l'estimation d'une intégrale de la forme 
$$\mathcal{I}=\Esp\left(h(X)\right)=\int_{\R^d} h(x) \P_X(dx),$$
peut s'écrire de différentes manières, notamment en faisant varier $h$ et $\P_X$. Par conséquent, un estimateur "optimal" devrait tenir compte de l'ensemble de ces possibilités.
