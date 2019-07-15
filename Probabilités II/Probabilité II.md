% Probabilités II

\newcommand{\R}{\mathbb{R}}
\newcommand{\Q}{\mathbb{Q}}
\renewcommand{\P}{\mathbb{P}}
\renewcommand{\C}{\mathbb{C}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\A}{\mathcal{A}}
\newcommand{\E}{\mathcal{E}}
\newcommand{\B}{\mathcal{B}}
\newcommand{\E}{\mathcal{E}}
\renewcommand{\L}{\mathcal{L}}
\newcommand{\Esp}{\mathbb{E}}
\newcommand{\V}{\mathbb{V}}
\newcommand{\cov}{\text{Cov}}



**TODO : donner des exemples d'analogie avec le cas discret**

# Variables aléatoires réelles

En théorie moderne des probabilités, on préfère prendre un point de vue fonctionnel plutôt qu’ensembliste, et utiliser les variables aléatoires plutôt que les événements. Ce point de vue sera développé dans la suite du cours. Nous en donnons ici les idées de base.

Une variable aléatoire est une grandeur qui dépend du résultat de l’expérience. Par exemple,

 * le nombre de 6 obtenus dans un lancer de 3 dés,
 * le nombre d’appels dans un central téléphonique pendant une heure,
 * la distance du point d’atteinte d’une flèche au centre de la cible,
 * la valeur maximale d’un prix d’actif sur un intervalle de temps donné,
sont des variables aléatoires.

La définition formelle d'une variable aléatoire fait intervenir des éléments de la théorie de la mesure. On s'interessera dans un premier temps au cas d'une variable réelle **avec $\Omega = \R$ ou $\R^d$. ?? -> comment justifier d'introduire les v.a. si on travail sur le même espace** dont on donne une première définition : 

Soit $\Omega$ l'espace fondamental muni de sa tribu $\A$. Une *variable aléatoire* $X$ est une application de $(\Omega,\A)$ dans un ensemble $E$,
\begin{equation}
\omega \in \Omega \mapsto X(\omega) \in E
\end{equation}

En pratique, l’ensemble $E$ pourra être un ensemble fini ou dénombrable ou $\R$ ou $\R^d$ ou encore un espace plus sophistiqué tel que l’ensemble $C(\R_+ , \R^d)$ des fonctions continues de $\R_+$ dans $\R^d$.

### Remarque {.remark}
La terminologie, consacrée par l'usage, peut être trompeuse. Une variable aléatoire n'est pas une variable (au sens de l'analyse) mais une fonction. Cette terminologie est apparentée à la notion de variable en physique ou en sciences humaines où on désigne volontiers par "variable" la valeur prise par une fonction de l'état du système étudié.

L'intérêt principal de travailler avec des variables aléatoires est de pouvoir substituer à l'espace abstrait $\Omega$ des résultats de l'expérience l'espace $E$, mieux connu dans la pratique. Ainsi, grâce à une variable aléatoire $X$, nous pouvons transporter la structure abstraite du modèle probabiliste $(\Omega, \A, \P)$ sur l'espace d'arrivée $E$, en posant pour $B \in E$
\begin{equation}
\label{eq:loi_va}
\P_X (B) = \P(X^{-1}(B)) = \P(\{\omega, X(\omega)\in B\})
\end{equation}
Cette formule défini une nouvelle probabilité, notée $\P_X$ et définie sur $E$, qui s'appelle la *loi de la variable* $X$.

Comme $\P(A)$ n'est définie que pour les $A$ de la tribu $\A$, la formule \eqref{eq:loi_va} ne permet de définir $\P_X(B)$ que pour les ensembles $B$ tels que $X^{-1}(B) \in \A$, d’où l’importance de la proposition suivante :

### Proposition {.proposition #propva.tribu}

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

Les variables que nous rencontrerons dans ce cours seront soit à valeurs dans un ensemble dénombrable, soit à valeurs dans $\R$ ou dans $R^d$. Nous les appellerons respectivement des variables aléatoires discrètes, réelles ou des vecteurs aléatoires. Leurs lois seront alors des probabilités respectivement sur un ensemble dénombrable, sur $\R$ ou sur $R^d$. Les probabilités sur un espace fini ou dénombrable sont considérées connues. 

La [proposition ci-dessus](#propva.tribu) implique que l'ensemble $X^{-1}(B)$ soit un évènement, pour tout $B$ dans $\E$. Cela nous conduit à poser

### Définition {.definition #defvar}
Soit l'espace d'état $\Omega$ munit de la tribu $\A$ des évènements. Une application $X$ de $\Omega$ dans $\R$ est une *variable aléatoire réelle* si $X^{-1}(B) \in \A$ pour tout $B$ dans $\B_\R$. (ou tribu de Lebesgue, à trancher)

On a alors le résultat très utile suivant que nous admettrons dans un premier temps.

### Proposition {.proposition}
Si $X_1, \ldots, X_n$ sont des variables aléatoires réelles et si $f$ est une fonction continue de $\R^n$ dans $\R$, alors $Y = f(X_1,\ldots,X_n)$ est une variable aléatoire réelle.

Comme application de ce résultat, on a les propriétés suivantes :

### Proposition {.proposition}

Soient $X$, $Y$ et $(X_n)_{n \in \N^\star}$ des variables aléatoires réelles. On a 

 1. $X + Y$, $XY$, $\frac{X}{Y}$ si $Y \neq O$, sont des variables aléatoires.
 
 2. $\sup_{1\leq p} X_n$, $\inf_{1\leq p} X_n$, sont des variables aléatoires.

 3. $\sup_{n\geq 1} X_n$, $\inf_{n\geq 1} X_n$, sont des variables aléatoires.

 4. Si $X_n(\omega) \xrightarrow{n \to \infty} Z(\omega)$, $\forall \omega$, alors la limite $Z$ est une variable aléatoire.

 5. $Z = 1_A$ est une variable aléatoire $\Leftrightarrow$ $A \in \A$

**Note : la démonstration n'a aucun intérêt si $\Omega = \R$ ou $\R^n$. C'est d'ailleurs difficile de justifier l'introduction des v.a. dans ce cas. Renvoyer ça au CI 5. L'idée à partir d'ici est de donner des résultats uniquement dans le cas à densité**

### Définition {.definition #va.densité}
Soit $X$ une variable aléatoire. On dit que $X$ a une *loi de densité $f$* (ou par abus de language "est de densité $f$"), si $\P_X$ admet la densité $f$ et donc si pour tout réel $x$, 
$$ \P(X\leq x) = \int_{-\infty}^x f(y) dy.$$

### Exemple {.example #ex.expo}
La durée de fonctionnement d'un ordinateur avant sa première panne est une variable aléatoire positive de densité donnée par 

$$f(x) = \left\{ \begin{array}{ll}
        \frac{1}{100}\exp\left(-\frac{x}{100}\right) & x \geq 0, \\
        0 & x < 0.
        \end{array}
        \right.$$

Calculons la probabilité que cette durée de fonctionnement $X$ soit comprise entre 50 et 150 heures, elle vaut 
$$ \P(X \in [50,150]) = \int_50^150 \frac{1}{100}\exp\left(-\frac{x}{100}\right) dx = \exp(-1/2)-\exp(-3/2) \approx 0,38.$$
Calculons la probabilité que l'ordinateur fonctionne moins de 100 heures :
$$ \P(X \leq 100) = \int_{0}^100 frac{1}{100}\exp\left(-\frac{x}{100}\right) dx = 1-e^{-1} \approx 0,63.$$

### Densités réelles usuelles
Nous donnons ici quelques exemples de densités de probabilité. On dit que $X$ suit la 

 * *loi uniforme* sur $[a,b]$, où $a < b$ et on note $X \sim \mathcal{U}_[a,b]$ si $X$ admet la densité
        $$ \frac{1}{b-a} 1_{[a,b]} (x).$$
 * *loi exponentielle* de paramètre $\lambda > 0$ et on note $X \sim \mathcal{E}(\lambda)$ si $X$ admet la densité
        $$ \lambda e^{-\lambda x} 1_{\{x>0\}}.$$
 * *loi gaussienne*
 * *loi de Cauchy*
 * *loi Gamma*

**note : ajouter de jolies figures**

# Moments d'une variable aléatoire à densité
 
La densité de probabilité d'une variable aléatoire va nous permettre de calculer aisément des grandeurs caractéristiques telles que sa valeur moyenne et sa variance définies ci-dessous :

### Définition {.definition #defesp}
La variable aléatoire $X : \Omega \to \R$ de densité $f$ est dite  *intégrable* si $\int_\R |x|f(x) dx < +\infty$, autrement dit si le produit $x f(x)$ est absolument intégrable. On définit alors son *espérance* par 
        $$\Esp(X) = \int_\R x f(x)dx$$

**note : pour introduire proprement l'espérance d'une variable aléatoire réelle, on a besoin de l'intégrale de Lebesgue -> CI 5**

On note $\L^1$ l'ensemble de toutes les variables réelles $X$ à densité intégrables. Les propriétés suivantes découlent directement des propriétés de l'intégrale.

### Proposition {.proposition #propl1}
 * $\L^1$ est un espace vectoriel et $\forall X,Y \in \L^1$, $\forall a,b \in \R$ 
        $$\Esp(aX + bY) = a\Esp(X) + b\Esp(Y).$$
 * $X \in \L^1 \leftrightarrow |X| \in \L^1$, et dans ce cas $$|\Esp(X)| \leq \Esp(|X|).$$
 * Si $X \geq 0$ et $X \in \L^1$, alors $\Esp(x) \geq 0.$
 * Si $X,Y \in \L^1$ sont telles que $X \leq Y$, alors
        $$ \Esp(X) \leq \Esp(Y).$$
 * Si $\exists b \in \R$ tel que $|X| \leq b$, alors $X \in \L^1$ et $\Esp(X) \leq b$.

### Remarque : analogie avec le cas discret **TODO**

Outre l'espace $\L^1$, nous pouvons définir l'espace $\L^2$ des variables aléatoires réelles dont le carré $X^2$ est dans $\L^1$.

### Définition {.definition #defvar}
La variable aléatoire $X : \Omega \to \R$ de densité $f$ est dite *de carré intégrable* si $\Esp(X^2) = \int_\R x^2 f(x)dx < +\infty$, autrement dit si le produit $x^2 f(x)$ est intégrable. Sa *variance* est définie par
        $$\V(X) = \Esp((X-\Esp(X))^2)$$


### Proposition {.proposition #propl2}
$\L^2$ est un sous-espace vectoriel de $\L^1$, et si $X \in \L^2$,
$$|\Esp(X)| \leq \Esp(|X|) \leq \sqrt{\Esp(X^2)}$$


### Démonstration {.proof}
Soient $X$ et $Y$ deux variables aléatoires réelles de $\L^2$ et $a \in \R$. Comme $(aX+ Y)^2 \leq 2 a^2 X^2 + 2 Y^2$, alors $aX + Y \in \L^2$. Ainsi, $\L^2$ est un espace vectoriel.

L'inclusion $\L^2 \in \L^1$ découle de $|X| \leq 1 + |X^2|$ et de la [proposition précédente](#propl1).

La première inégalité a déjà été vue ci-dessus. Pour la seconde, nous pouvons nous limiter au cas où $X$ est positive. Soit alors $a = \Esp(X)$ et $Y = X-a$. Par linéarité, on a 
        $$ \Esp(Y^2) = \Esp(X^2) - 2a \Esp(X) + a^2 = \Esp(X^2)-a^2.$$
Et $\Esp(Y^2) \geq 0$ par le troisième point de la [proposition ci-dessus](#propl1). Par conséquent, $\Esp(X)^2 = a \leq \Esp(X^2)$ ce qui est le résultat recherché.

### Remarque {.remark}
En vertu de cette [proposition](#propl2), $\V(X)$ est **positive** et sa racine carrée $\sigma_X$ s'appelle l'*écart-type* de $X$. L’écart-type est une grandeur qui mesure la moyenne (en un certain sens) de l’écart des valeurs de $X$ à sa moyenne, d’où son nom. 



### Exemple : **TODO illustration écart type**

On peut remarquer que si $X$ et $Y$ sont dans $\L^2$, la variable aléatoire $XY$ est dans $\L^1$. En effet, on a $|XY| \leq \frac{1}{2}(X^2+Y^2)$. On peut ainsi définir la *covariance* de deux variables aléatoires.

### Définition {.definition #defcov}
Si $X$ et $Y$ sont dans $\L^2$, la variable aléatoire $(X-\Esp(X))(Y-\Esp(Y))$ est intégrable. On appelle la *covariance* de $X$ et $Y$ l'espérance de cette variable aléatoire et on la note :
        $$\cov (X,Y) = \Esp((X-\Esp(X))(Y-\Esp(Y))).$$
Le *coefficient de corrélation* des variables aléatoires $X$ et $Y$ est le nombre 
        $$\rho(X,Y) = \frac{\cov (X,Y)}{\sqrt{\V(X)}\sqrt{\V(Y)}}$$
qui est bien défini lorsque $\V(X)>0$ et $\V(Y)>0$.



# Vecteurs aléatoires à densité

# Variables aléatoires indépendantes

# Calculs de loi (cf Jacod - Garnier)


# Exercices

