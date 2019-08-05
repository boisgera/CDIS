% Probabilité IV

\newcommand{\R}{\mathbb{R}}
\newcommand{\Q}{\mathbb{Q}}
\renewcommand{\P}{\mathbb{P}}
\renewcommand{\C}{\mathbb{C}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\No}{\mathcal{N}}
\newcommand{\A}{\mathcal{A}}
\newcommand{\E}{\mathcal{E}}
\newcommand{\B}{\mathcal{B}}
\renewcommand{\L}{\mathcal{L}}
\newcommand{\Esp}{\mathbb{E}}
\newcommand{\V}{\mathbb{V}}
\newcommand{\cov}{\text{Cov}}


Nous allons présenter dans ce chapitre l’un des résultats essentiels de la théorie des probabilités. Ce résultat montre rigoureusement que, quand le nombre de répétitions de l’expérience tend vers l’infini, la fréquence de réalisation d’un événement converge vers la probabilité de réalisation de cet événement. Ce résultat, appelé **Loi des grands nombres**, a d’autres portées fondamentales. Philosophique tout d’abord, puisqu’il permet de voir le monde déterministe comme la limite macroscopique d’une accumulation de phénomènes élémentaires microscopiques aléatoires. Portée numérique aussi, car nous verrons que ce théorème est à l’origine de méthodes de calcul numérique appelées Méthodes de Monte-Carlo, qui sont extrêmement puissantes et robustes. Elles sont par exemple très utilisées en Physique ou en Mathématiques Financières.
Plus généralement, nous allons étudier les suites de variables aléatoires indépendantes et les notions de convergence de variables aléatoires. Nous verrons que plusieurs notions sont possibles, non équivalentes, ce qui enrichit mais complique aussi la description des comportements asymptotiques.

Nous nous plaçons dans le cadre général des variables aléatoires réelles qui n'admettent pas nécessairement de densité.

# Suites de variables aléatoires indépendantes 
On considère une suite **infinie** $(X_n)_{n\in \N^\star}$ de variables aléatoires définies sur l'espace probabilisé $(\Omega, \A, \P)$.

### Définition {.definition}
La suite $(X_n)_{n\in \N^\star}$ de variables aléatoires est dite *indépendante* si pour tout $n$, la famille finie $X_1,\ldots,X_n$ est indépendante.

Il est facile de vérifier que l’indépendance est préservée par certaines transformations.

### Proposition {.proposition}
L'indépendance de la suite $(X_n)_{n\in \N^\star}$ entraîne celle de 

 1. toute sous-suite $(X_{i_k})_{k\in \N^\star}$,
 2. toute suite de vecteurs issus de $X_n$,
 3. toute suite de la forme $(f_n(X_n))_{n\in \N^\star}$, où les fonctions $f_n$ sont des fonctions mesurables.

### Exemple {.example}
Nous considérons l’ensemble $\Omega = [0, 1[$ muni de la tribu borélienne restreinte à cet ensemble, et de la mesure de Lebesgue. A chaque réel $\omega$, nous associons son développement dyadique (unique si l’on impose que les $\omega_i$ ne soient pas tous égaux à 1 à partir d’un certain rang) :
$$ \omega = \sum_{i\in \N^\star} \frac{\omega_i}{2^i}, \omega_i \in \{0,1\}$$.
L'application $X_i : \Omega \to \{0,1\}$, qui à $\omega$ associe $X_i(\omega) = \omega_i$ est une variable aléatoire sur $\Omega$. En effet, pour $x_i \in \{0,1\}$, $1\leq i \leq n$,
$$ \{X_i = x_i\} = \bigcup_{x_1,\ldots, x_{i-1} \in \{0,1\}} \left[ \sum_{j=1}^i \frac{x_j}{2^j}, \sum_{j=1}^i \frac{x_j}{2^j} + \frac{1}{2^i}\right[, $$
qui est bien un élément de la tribu borélienne de $\Omega = [0,1[$, et
$$\P(\{X_i = x_i\}) = \frac{1}{2^i} \sum_{x_1,\ldots, x_{i-1} = 0}^1 1 = \frac{1}{2}.$$
Montrons l'indépendance des variables aléatoires $(X_i)_{1\leq i \leq n}$. Nous avons 
$$ \bigcap_{1\leq i \leq n} \{X_i = x_i\} = \left[ \sum_{i=1}^n \frac{x_i}{2^i}, \sum_{i=1}^n \frac{x_i}{2^i} + \frac{1}{2^n}\right[ $$
si bien que 
$$ \P\left(\bigcap_{1\leq i \leq n} \{X_i = x_i\}\right) = \frac{1}{2^n} = \prod_{1\leq i \leq n} \P(\{X_i = x_i\}).$$
Cela démontre que les variables aléatoires $X_i$ sont indépendantes et de loi de Bernoulli de paramètre $\frac{1}{2}$ . Ainsi, nous venons de construire sur $\Omega$ une suite de variables aléatoires telle que toute sous-suite finie est constituée de variables aléatoires indépendantes. C’est donc une suite de
variables aléatoires indépendantes de loi de Bernoulli de paramètre $\frac{1}{2}$ .

# Inégalités de concentrations -> demi amphi théorie de la mesure (en lien avec l'espérance)

# Convergence de variables aléatoires

## Convergence en loi 
La convergence en loi définie dans ce paragraphe va concerner les lois des variables aléatoires. Elle signifiera que les lois sont asymptotiquement “proches”, sans que les variables aléatoires elles-mêmes le soient nécessairement. 

On considère des vecteurs aléatoires $X_n$ et $X$, tous à valeurs dans le même espace $\R^d$, mais pouvant éventuellement être définis sur des espaces de probabilité différents.

### Définition {.definition}
On dit que la suite $(X_n)_{n\in \N^\star}$ *converge en loi* vers $X$ et on écrit $X_n \xrightarrow{\L} X$, si pour toute fonction $f$ continue bornée sur $\R^d$, 
$$\Esp(f(X_n)) \xrightarrow{\L} \Esp(f(X)).$$

### Exemple {.example}
Un cas très simple est celui où toutes les variables aléatoires $X_n$ prennent un nombre fini de valeurs $\{ x_i , 1 \leq i \leq N \}$. Alors, la suite $(X_n)_{n \in \N^\star}$ converge en loi vers $X$ si et seulement si 
$$\lim_{n \to +\infty} \P(X_n = x_i ) = \P(X = x_i), \forall 1 \leq i \leq N$$
Il suffit d’écrire pour $f$ continue bornée
$$ \Esp(f (X_n)) = \sum_{i=1}^N f (x_i ) P(X_n = x_i)

Dans l’exemple ci-dessus, $N$ est fini et fixé. Mais nous avons un résultat analogue (en faisant tendre $N$ vers l’infini) si les variables aléatoires ont un nombre dénombrable de valeurs. Le cas de la convergence de la loi binomiale vers la loi de Poisson est notamment traité en CPGE.

### Exemple {.example}
Soit $(X_n)_{n \in \N^\star}$ et $X$ des variables aléatoires de lois respectives $\No (0,\sigma^2_n)$ et $\No (0,\sigma^2)$. On suppose que la suite de réels positifs $(\sigma_n)_{n\in \N^\star}$ converge vers $\sigma > 0$ quand $n$ tend vers l'infini. Alors la suite $(X_n)_{n \in \N^\star}$ converge en loi vers $X$. En effet, soit $f$ une fonction continue bornée sur $\R$. On a
\begin{align*}
\Esp(f(X_n)) &= \int_\R f(y) \frac{1}{\sqrt{2\pi}\sigma_n} \exp\left(-\frac{y^2}{2\sigma^2_n\right) dy \\
             &\to \int_\R f(y) \frac{1}{\sqrt{2\pi}\sigma} \exp\left(-\frac{y^2}{2\sigma^2\right) dy
\end{align*}
où l'on a utilisée le théorème de convergence dominée.


# Théorèmes limites

 * Loi des grands nombre - faible, forte
 * TCL (fonction caractéristique)