% Probabilité IV

\newcommand{\R}{\mathbb{R}}
\newcommand{\Q}{\mathbb{Q}}
\renewcommand{\P}{\mathbb{P}}
\renewcommand{\C}{\mathbb{C}}
\newcommand{\N}{\mathbb{N}}
\renewcommand{\No}{\mathcal{N}}
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
On considère une suite **infinie** $(X_n)_{n\in \N^\star}$ de variables aléatoires définies sur l'espace de probabilité $(\Omega, \A, \P)$.

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

# Convergences et loi des grands nombres

## Convergences de variables aléatoires
Dans ce paragraphe, nous allons étudier des modes de convergence impliquant la proximité des variables aléatoires elles-mêmes, contrairement au cas de la convergence en loi qui sera étudiée ultérieurement.

On considère une suite $(X_n)_{n\in \N^\star}$ de vecteurs aléatoires, définis sur un même espace de probabilité $(\Omega, \A, \P)$, et à valeurs dans $\R^d$. On considère également sur le même espace un vecteur "limite" $X$. On notera $|\cdot|$ la valeurs absolue dans $\R$ ou la norme dans $\R^d$.

### Définition {.definition}

 1. La suite $(X_n)_{n\in \N^\star}$ converge *presque sûrement* vers $X$, ce qui s'écrit $X_n \to X$ p.s., s'il existe un ensemble $N \in \A$ de probabilité nulle tel que
 $$ X_n (\omega) \xrightarrow[n \to \infty]{}  X(\omega) \forall \omega \notin N.$$
 2. La suite $(X_n)_{n\in \N^\star}$ converge *en probabilité* vers $X$, ce qui s'écrit $X_n \xrightarrow{\P} X$, si $\forall \epsilon >0$ on a
 $$ \P(|X_n-X| \geq \epsilon) \xrightarrow[n \to \infty]{}  0. $$
 3. La suite $(X_n)_{n\in \N^\star}$ converge *en moyenne* vers $X$, ce qui s'écrit $X_n \xrightarrow{\L^1} X$, si $X_n$ et $X$ sont dans $\L^1$ et si
 $$ \Esp(|X_n - X|) \xrightarrow[n \to \infty]{}  0 .$$

### Remarque {.remark}
La convergence presque sûre est la plus proche de la convergence simple des fonctions. Mais ici, nous permettons à certains $\omega$ de ne pas vérifier $X_n(\omega) \to X(\omega)$, si toutefois la probabilité de réalisation de l'ensemble de ces $\omega$ est nulle.

Ces convergences ne sont pas équivalentes comme le montre les exemples suivants.

### Exemples {.example}

 * Soit $(X_n)_{n\in \N^\star}$ une suite de variables aléatoires de Bernoulli à valeurs dans $\{0,1\}$ telles que
 $$ \P(X_n=1) = \frac{1}{n} ; \P(X_n = 0) = 1- \frac{1}{n}.$$
 Pour tout $\epsilon \in ]0,1[$, la probabilité $\P(|X_n|\geq 0) = \frac{1}{n}$ tend vers 0 quand $n tend vers l'infini. Ainsi, la suite $(X_n)_{n\in \N^\star}$ tend vers $X=0$ en probabilité. Comme $\Esp(\frac{1}{n}) = 0$, elle tend également en moyenne vers 0.
 Considérons maintenant une suite $(Y_n)_{n\in \N^\star}$ de variables aléatoires de Bernoulli ) valeurs dans $\{0,n^2\}$ telles que 
 $$ \P(Y_n=n^2) = \frac{1}{n} ; \P(Y_n = 0) = 1- \frac{1}{n}.$$
 Par le même argument que ci-dessus, nous voyons que la suite $(Y_n)_{n\in \N^\star}$ converge en probabilité vers 0, mais comme $\Esp(Y_n) = n$, la suite ne converge pas en moyenne vers 0 (ni vers aucune autre limite finie).
 * Soit $U$ une variable aléatoire uniforme sur $[0 , 1]$. Posons $Z_n = 1_{\{ U \leq \frac{1}{n}\} }$. Alors
 $$ \P(Z_n = 1)= \frac{1}{n} ; \P(Z_n = 0) = 1 - \frac{1}{n}$$
 Si $\omega \in \{U > 0\}$ est fixé, alors $\exists n_0 \in \N$ tel que $U(\omega) > \frac{1}{n_0}$, et donc tel que $Z_n(\omega) = 0$ pour tout $n \geq n_0$. Comme $\P(U>0)=1$, ceci montre que la suite $(Z_n)_{n\in \N^\star}$ converge presque sûrement vers 0.

Etudions maintenant les liens entre ces différentes convergences.

### Proposition {.proposition #propconv1}
La convergence p.s. et la convergence en moyenne entraînent la convergence en probabilité.

### Démonstration {.proof}
Soit $A_{n,\epsilon} = \{|X_n - X| > \epsilon \}$.

 * Supposons que $X_n \to X$ p.s. et soit $N$ l'ensemble de probabilité nulle en dehors duquel on a $X_n(\omega) \to X(\omega)$. Si $\omega \notin N$, on a $\omega \notin A_{n,\epsilon}$ pour tout $n \geq n_0$, où $n_0$ dépende de $\omega$ et de $\epsilon$, ce qui implique que les variables aléatoires $Y_{n,\epsilon} = 1_{N^c\cap A_{n,\epsilon}}$ tendent simplement vers 0 lorsque $n \to \infty$. Comme on a aussi $0 \leq Y_{n,\epsilon} \leq 1$ le théorème de convergence dominée implique que $\Esp(Y_{n,\epsilon}) \xrightarrow[n \to \infty]{} 0.$ Mais
 $$\P(A_{n,\epsilon}) \leq \P(N^c \cap A_{n,\epsilon}) + \P(N) = \P(N^c \cap A_{n,\epsilon}) = \Esp(Y_{n,\epsilon}) \xrightarrow[n \to \infty]{} 0.$$

 * Supposons que $X_n \xrightarrow{\L^1} X$. Pour $\epsilon >0$, on a $1_{A_{n,\epsilon}} \leq \frac{1}{\epsilon}|X_n - X|$, donc 
 $$ \P(A_{n,\epsilon}) \leq \frac{1}{\epsilon}\Esp(|X_n - X|) \to 0.$$


La convergence en probabilité n’entraîne pas la convergence en moyenne, comme nous l’avons vu dans l’exemple ci-dessus, ne serait-ce que parce qu'elle n'implique pas l'appartenance de $X_n$ et $X$ à $\L^1$. Si les $X_n$ ne sont “pas trop grands”, il y a cependant équivalence entre les deux modes de convergence. En voici un exemple :

### Proposition {.proposition #propconv2}
S'il existe une constante $a$ telle que $|X_n| \leq a$ presque sûrement, il y a équivalence entre $X_n \xrightarrow{\P} X$ et $X_n \xrightarrow{\L^1} X$.

### Démonstration {.proof}
Etant donnée la [proposition précédente](#propconv1), dont on reprend les notations, il suffit de montrer que la convergence en probabilité implique la convergence en moyenne lorsque $|X_n| \leq a$.

Comme $|X_n| \leq a$, on a $\{|X| > a +\epsilon\} \subset A_{n,\epsilon}$, et donc $\P(|X| > a +\epsilon ) \leq \P(A_{n,\epsilon})$. En faisant $n \to \infty$, on en déduit que $\P(|X| > a + \epsilon) = 0$. Ceci est vrai pour tout $\epsilon$ et donc
$$\P(|X|> a) = 0.$$
Comme $|X_n| \leq a$, on a aussi
$$ |X_n -X| \leq \epsilon + (X_n + X) 1_{A_{n,\epsilon}} \leq \epsilon + 2a 1_{A_{n,\epsilon}}$$
sur l'ensemble $\{|X| \leq a \}$ qui est de probabilité 1. On a ainsi 
$$ \Esp(|X_n - X|) \leq \epsilon +2a \P(A_{n,\epsilon})$$
On en déduit que $\lim \sup_n \Esp(|X_n - X|) \leq \epsilon$, et comme $\epsilon$ est arbitrairement proche de 0, on a le résultat souhaité.

### {.anonymous}
Les rapports entre convergence presque-sûre et convergence en probabilité sont plus subtils. La première de ces deux convergences est plus forte que la seconde d’après la [proposition](#propconv2), mais “à peine plus”, comme le montre le résultat suivant.

### Proposition {.proposition #propconv3}
Si $X_n \xrightarrow{\P} X$, il existe une sous-suite $(n_k)$ telle que $X_{n_k} \to X$ p.s. quand $k \to \infty$.

### Démonstration {.proof}
Comme la suite $(X_n)_{n\in \N^\star}$ concerge en probabilité vers $X$, on peut définir une sous-suite de la manière suivante : posons $n_1 = 1$, et soit
$$ n_j = \inf \left\{ n > n_{j-1} ; \P \left(|X_r - X_s| > \frac{1}{2^j} \right) < \frac{1}{3^j}, \text{ pour } r,s \geq n \right\}.$$
Il résulte alors de 
$$\sum_j =\P \left(|X_{n_{j+1}} - X_{n_j}| > \frac{1}{2^j} \right) < \sum_j \frac{1}{3^j} < \infty$$
que la suite $(X_{n_j})_{j\in \N^\star}$ converge presque-sûrement. C'est en effet une conséquence du [lemme de Borel-Cantelli]() appliqué aux ensembles 
$$A_j =\left\{|X_{n_{j+1}} - X_{n_j}| > \frac{1}{2^j} \right\}.$$

### Exemple {.example}

Soient $\Omega = \R$ muni de sa tribu borélienne et $\P$ la probabilité uniforme sur [0, 1]. Soit $X_n = 1_{A_n}$ , où $A_n$ est un intervalle de [0, 1] de longueur $\frac{1}{n}$.
Ainsi, $\Esp(X_n) = \frac{1}{n}$, et la suite $X_n$ tend vers $X = 0$ en moyenne, et donc en probabilité. Supposons que les $A_n$ soient placés bout-à-bout, en recommençant en 0 chaque fois qu’on arrive au point 1. Il est clair que l’on parcourt indéfiniment l’intervalle [0, 1] (car la série de terme général 1/n diverge). Ainsi la suite numérique $X_n (\omega)$ ne converge pour aucun $\omega$, et on n’a pas $X_n \to X$ presque-sûrement ; cependant comme
la série $\sum_n 1/n^2$ converge, il s’en suit que $X_{n^2} \to X = 0$ presque-sûrement. Nous avons donc la convergence presque-sûre de la sous-suite $(X_{n^2})_{n\in \N^\star}$.

### Proposition {.proposition #propconv4}
Soit $f$ une fonction continue de $\R^d$ dans $\R$.

 1. Si $X_n \to X$ presque-sûrement, alors $f(X_n) \to f(X)$ presque-sûrement.
 2. Si $X_n \xrightarrow{\P} X$, alors $f(X_n) \xrightarrow{\P} f(X)$.

### Démonstration {.proof}
Le point 1. est évident. Pour 2., remarquons d'abord que si $K >0$ et $\epsilon >0$,
$$\{|f(X_n)-f(X)| \geq \epsilon\} \subset \{|X| > K\}\cup\{|X| \leq K, |f(X_n)-f(X)| \geq \epsilon\}.$$
La fonction $f$ est uniformément continue sur $\{x : |x| \leq K\}$, donc il existe $\eta > 0$ tel que $|x-y| <\epsilon$ et $|x| \leq K$ et $y\leq K$ impliquent 
$|f(x) - f(y)| <\epsilon$. On a donc
$$\{|f(X_n)-f(X)| \geq \epsilon\} \subset \{|X| > K\}\cup\{|X_n-X| \geq \eta\}$$
d'où
$$\P(|f(X_n)-f(X)| \geq \epsilon) \leq \P(|X| > K) + \P(|X_n-X| \geq \eta).$$
Par hypothèse, il vient
$$ \lim \sup_n \P(|f(X_n)-f(X)| \geq \epsilon) \leq \P(|X| > K) .$$
Enfin, $\lim_{K\to +\infty} \P(|X| > K) = 0$ (par convergence dominée) et donc la $\lim \sup$ ci-dessus est nulle. On a ainsi le résultat.

## La loi des grands nombres 

Dans ce paragraphe, on considère une suite $(X_n)_{n\in\N^\star}$ de variables aléatoires **indépendantes et de même loi** (ou indépendantes et identiquement distribuées, i.i.d. en abrégé). On considère la "moyenne" des $n$ premières variables aléatoires :
$$ M_n = \frac{X_1 + \ldots + X_n}{n},$$
et notre objectif est de montrer que $M_n$ converge vers l'espérance des $X_n$ lorsque celle-ci existe (comme les $X_n$ ont même loi, cette espérance est la
même pour tout $n$). Il s’agit là d’un des résultats essentiels de toute la théorie des probabilités, connu sous le nom de **loi des grands nombres**.

Nous allons démontrer dans un premier temps la loi des grands nombres pour des variables aléatoires de carré intégrable.

### Théorème {.theorem}
Soit $(X_n)_{n\in\N^\star}$ une suite de variables aléatoires indépendantes, de même loi et de **carré intégrable**, et $m = \Esp(X_n)$ leur moyenne. Alors la suite $(M_n)_{n\in\N^\star}$ définie par
$$M_n = \frac{X_1 + \ldots + X_n}{n}$$
converge vers $m$, **presque sûrement et en moyenne**, quand $n$ tend vers l'infini. Elle converge donc aussi en probabilité. On a même convergence en *moyenne quadratique*, à savoir que :
$$ \Esp((M_n - m)^2) \xrightarrow[n \to \infty]{} 0.$$

Le résultat sur la convergence en probabilité est appelé *loi faible des grands nombres*. Sa preuve est presque immédiate. Elle résulte de l’inégalité de Bienaymé-Chebyshev (exercice). Le résultat est peu informatif et permet d’obtenir certains contrôles d’erreurs. Le résultat prouvant la convergence presque-sûre est appelé *loi forte des grands nombres*. Sa preuve est plus délicate et utilise le lemme de Borel-Cantelli.

### Démonstration
Notons $\sigma^2$ la variance des variables $X_n$, bien définie puisqu'on les a supposées de carré intégrable. En vertu de la linéarité de l'espérance, on a
$$ \Esp(M_n) = m, \Esp((M_n-m)^2) = \V(M_n) = \frac{\sigma^2}{n},$$
d'où la convergence en moyenne quadratique.

Comme $\Esp(Y)^2 \leq \Esp(Y^2)$, on en déduit que $\Esp(|M_n -m|)\to 0$, donc on a aussi la convergence en moyenne.

La preuve de la convergence presque-sûre est plus délicate.

Quitte à remplacer $X_n$ par $X_n - m$ (et donc $M_n$ par $M_n - m$), nous pouvons supposer que $m = 0$.

Montrons tout d’abord que la sous-suite $(M_{n^2})_{n \in \N^\star}$ converge presque-sûrement vers 0.

D'après l'inégalité de Bienaymé-Chebyshev et ce qui précède, on a pour $q\in \N^\star$
$$\P(|M_n^2|\geq \frac{1}{q}) \leq \frac{\sigma^2 q^2}{n^2}$$

Donc si $A_{n,q} = \{|M_n^2|\geq \frac{1}{q}\}$, nous obtenons que $\sum_{n\geq 1} \P(A_{n,q}) < \infty$. Posons ensuite $B_{n,q} = \cup_{m\geq n} A_{m,q}$ et $C_q = \cap_{n \geq 1} B_{n,q} = \lim\sup_n A_{n,q}$. En appliquant le lemme de Borel-Cantelli, on obtient que $\P(C_q) = 0$. En conséquence, si on pose $N = \cup_{q \in \N^\star} C_q$, on obtient $\P(N) \leq \sum_{q\in\N^\star} = 0$.

Si $\omega \notin N$, alors $\omega \in \cap_{q \in \N^\star} (C_q)^c$. Ainsi, $\omega \notin C_q$ pour tout $q \geq 1$, et donc $\omega \notin B_{n,q}$ pour $n$ assez grand (car $B_{n,q}$ est décroissant en $n$). Cela siginfie que pour tout $\omega \notin N$, pour tout $q \geq 1$, il existe un $n$ assez grand tel que $M_{k^2} \leq \frac{1}{q}$ dès que $k \geq n$. Autrement dit, $M_{n^2} \to 0$ si $\omega \notin N$, avec $\P(N) = 0$, d'où
$$ M_{n^2} \xrightarrow[n \to \infty]{} 0 \text{ p.s.}$$

Montrons maintenant que la suite $(M_n)_{n\in\N^\star}$ tend presque-sûrement vers 0.

Pour tout entier $n$, notons $p(n)$, l'entier tel que $p(n)^2 \leq n \leq (p(n)+1)^2$. Alors, 
$$ M_n - \frac{p(n)^2}{n}M_{p(n)^2} = \frac{1}{n} \sum_{p = p(n)^2+1}^{n} X_p,$$
et puique les variables aléatoires de la somme sont indépendantes, il vient
\begin{align*}
\Esp\left(\left(M_n - \frac{p(n)^2}{n}M_{p(n)^2}\right)^2\right) & = \frac{n-p(n)^2}{n^2}\sigma^2 \\
                                                                 & \leq \frac{2p(n)+1}{n^2} \sigma^2 \leq \frac{2\sqrt{n}+1}{n^2} \sigma^2
\end{align*}

En appliquant de nouveau l'inégalité de Bienaymé-Chebyshev, on obtient
$$ \P(\left|M_n - \frac{p(n)^2}{n}M_{p(n)^2}\right|>a) \leq \frac{2\sqrt{n}+1}{n^2} \frac{\sigma^2}{a^2}$$
Comme la série $\sum_n \frac{2\sqrt{n}+1}{n^2}$ converge, le même raisonnement que pour $M_{n^2}$ décrit ci-dessus, montre que
$$ M_n - \frac{p(n)^2}{n}M_{p(n)^2} \to 0 \text{ p.s.}$$
Par ailleurs, on a déjà montré que $M_{p(n)^2} \to 0$ p.s. et $\frac{p(n)^2}{n} \to 1$. On en déduit que $M_n \to 0$ p.s.$

### {.anonymous}
Plus généralement, on a le résultat suivant (se référer par exemple à @Jacod pour la démonstration)

### Théorème {.theorem}
Soit $(X_n)_{n\in\N^\star}$ une suite de variables aléatoires indépendantes, de même loi et **intégrables**, et $m = \Esp(X_n)$ leur moyenne. Alors la suite $(M_n)_{n\in\N^\star}$ définie par
$$M_n = \frac{X_1 + \ldots + X_n}{n}$$
converge vers $m$, **presque sûrement et en moyenne**, quand $n$ tend vers l'infini.

### Exemple **TODO cf garnier** {.example}

# Convergence en loi --- fonction caractéristique --- théorème central limite
Nous allons introduire maintenant une nouvelle notion de convergence de suites de variables aléatoires. La convergence en loi définie dans ce paragraphe va concerner les lois des variables aléatoires. Elle signifiera que les lois sont asymptotiquement “proches”, sans que les variables aléatoires elles-mêmes le soient nécessairement. 

## Convergence en loi

On considère des vecteurs aléatoires $X_n$ et $X$, tous à valeurs dans le même espace $\R^d$, mais pouvant éventuellement être définis sur des espaces de probabilité différents.

### Définition {.definition #defconvloi}
On dit que la suite $(X_n)_{n\in \N^\star}$ *converge en loi* vers $X$ et on écrit $X_n \xrightarrow{\L} X$, si pour toute fonction $f$ continue bornée sur $\R^d$, 
$$\Esp(f(X_n)) \xrightarrow{\L} \Esp(f(X)).$$

### Exemple {.example}
Un cas très simple est celui où toutes les variables aléatoires $X_n$ prennent un nombre fini de valeurs $\{ x_i , 1 \leq i \leq N \}$. Alors, la suite $(X_n)_{n \in \N^\star}$ converge en loi vers $X$ si et seulement si 
$$\lim_{n \to +\infty} \P(X_n = x_i ) = \P(X = x_i), \forall 1 \leq i \leq N$$
Il suffit d’écrire pour $f$ continue bornée
$$ \Esp(f (X_n)) = \sum_{i=1}^N f (x_i ) P(X_n = x_i) $$

Dans l’exemple ci-dessus, $N$ est fini et fixé. Mais nous avons un résultat analogue (en faisant tendre $N$ vers l’infini) si les variables aléatoires ont un nombre dénombrable de valeurs. Le cas de la convergence de la loi binomiale vers la loi de Poisson est notamment traité en CPGE.

### Exemple {.example}
Soit $(X_n)_{n \in \N^\star}$ et $X$ des variables aléatoires de lois respectives $\No (0,\sigma^2_n)$ et $\No (0,\sigma^2)$. On suppose que la suite de réels positifs $(\sigma_n)_{n\in \N^\star}$ converge vers $\sigma > 0$ quand $n$ tend vers l'infini. Alors la suite $(X_n)_{n \in \N^\star}$ converge en loi vers $X$. En effet, soit $f$ une fonction continue bornée sur $\R$. On a
\begin{align*}
\Esp(f(X_n)) &= \int_\R f(y) \frac{1}{\sqrt{2\pi}\sigma_n} \exp\left(-\frac{y^2}{2\sigma^2_n}\right) dy \\
             &\to \int_\R f(y) \frac{1}{\sqrt{2\pi}\sigma} \exp\left(-\frac{y^2}{2\sigma^2}\right) dy
\end{align*}
où l'on a utilisée le théorème de convergence dominée.

La convergence en loi est plus faible que la convergence en probabilité et donc aussi que les convergences presque-sûre et en moyenne.

### Proposition {.proposition}
Si $X_n \xrightarrow{\P} X$, alors $X_n\xrightarrow{\L} X$.

### Démonstration {.proof}
Soit $f$ une fonction continue bornée. D'après la [proposition](#propconv4), on a $f(X_n) \xrightarrow{\P} f(X)$ et donc $f(X_n)$ converge aussi en moyenne vers $f(X)$ par la [proposition](#propconv2). Comme $|\Esp(Y)|\leq \Esp(|Y|)$ pour toute variable aléatoire réelle $Y$, on en déduit $\Esp(f(X_n)) \to \Esp(f(X))$.

### {.anonymous}
Un moyen efficace de caractériser la convergence en loi passe par l'étude de la suite des fonctions de répartition.

### Proposition {.proposition}
Soient $X_n$ et $X$ des variables aléatoires réelles de fonctions de répartition respectives $F_n$ et $F$. Pour que $X_n \xrightarrow{\L} X$, il faut et il suffit que $F_n(x) \xrightarrow[n\to \infty]{} F(x)$ pour tout $x$ en lequel $F$ est continue.

Notons que puisque la fonction $F$ est continue à droite et croissante, l’ensemble
des points où $F$ est continue est l’ensemble $D = \{x : F (x-) = F (x)\}$, et son
complémentaire est au plus dénombrable. Ainsi, $D$ est dense dans $R$.

### Démonstration {.proof}

 1. Supposons d'abord que $X_n \xrightarrow{\L} X$. Soit $a \in \R$ tel que $F(a-)=F(a)$. Pour tout $p \in \N^\star$ et tout $b \in \R$, il existe une fonction $f_{p,b}$ continue bornée sur $\R$ telle que 
 $$ 1_{]-\infty,b} \leq f_{p,b} \leq 1_{]-\infty,b + \frac{1}{p}}.$$
 Alors, par définition, $\Esp(f_{p,b}(X_n)) \to \Esp(f_{p,b}(X))$ quand $n$ tend vers l'infini.
 L'inégalité ci-dessus implique que $F_n(a) = \P(X_n \leq a) \leq \Esp(f_{p,a}(X_n))$ et $\Esp(f_{p,a}(X)) \leq F(a+1/p)$ ; 
 donc $\lim\sup_n F_n(a) \leq F(a+1/p)$ pour tout $p$ et donc on a aussi $\lim\sup_n F_n(a) \leq F(a)$.
 On a également que $F_n(a) \geq \Esp(f_{p,a-1/p}(X_n))$ et $\Esp(f_{p,a-1/p}(X)) \geq F(a-1/p)$ ; donc $\lim\inf_n F_n(a) \geq F(a-1/p)$ pour tout $p$ et donc aussi $\lim\inf_n F_n(a) \geq F(a)$, puique $F(a-)=F(a)$. Ces deux résultas impliquent que $F_n(a) \xrightarrow[n\to \infty]{} F(a)$.
 2. Inversement, supposons $F_n(x) \xrightarrow[n\to \infty]{} F(x)$ pour tout $x\in T$, où $T$ est une partie dense de $\R$. Soit $f$ une fonction continue bornée sur $\R$ et $\epsilon > 0$. Soient $a,b \in T$ avec $F(a) \leq \epsilon$ et $F(b) \geq 1-\epsilon$. Il existe $n_0$ tel que 
 $$ n\geq n_0 \Rightarrow \P(X_n\notin ]a,b]) = 1-F_n(b)+F_n(a) \leq 3\epsilon.$$
 La fonction $f$ est uniformément continue sur $[a,b]$, donc il existe un nombre fini de points $a_0 = a < a_1 < \ldots < a_k = b$ appartenant tous à $T$, et tels que $|f(x) - f(a_i)|\leq \epsilon$ si $a_{i-1} \leq x \leq a_i$. Donc
 $$ g(x) = \sum_{i=1}^k f(a_i)1_{]a_{i-1},a_i]}(x)$$
 vérifie $|f-g| \leq \epsilon$ sur $]a,b]$. Si $M = \sup_x |f(x)|$, il vient alors
 $$|\Esp(f(X_n))-\Esp(g(X_n))| \leq M \P(X_n \notin [a,b]) + \epsilon,$$
 de même pour $X$. Enfin, $\Esp(g(X_n)) = \sum_{i=1}^k f(a_i)(F_n(a_i) - F_n(a_{i-1})$, et de même pour $X$ par définition de $g$. Comme $(F_n(a_i))_{n \in \N^\star}$ converge vers $F(a_i)$ pour tout $i$, on en déduit l'existence de $n_1$ tel que 
 $$ n\geq n_1 \Rightarrow |\Esp(g(X_n)) - \Esp(g(X))|\leq \epsilon.$$
 Finalement, on a 
 $$ n \geq \sup(n_0,n_1) \Rightarrow |\Esp(f(X_n))-\Esp(f(X))|\leq 3\epsilon + 5 M \epsilon .$$ 
 Vu l'arbitraire sur $\epsilon$, on en déduit que $\Esp(f(X_n))$ converge vers $\Esp(f(X))$, d'où le résultat.

### Corollaire {.corollary}
Si la suite $(X_n)_{n\in\N^\star}$ de variables aléatoires réelles converge en loi vers $X$, et si la loi de $X$ admet une densité, alors pour tous $a< b$,
$$ \P(X_n \in ]a,b]) \xrightarrow[n\to \infty]{} \P(X\in]a,b]).$$

### Démonstration {.proof}
La fonction de répartition de $X$ est alors continue en tout point. (Mais pas nécessairement celles des variables aléatoires $X_n$.)

**Slutsky ???? voir avec CAA -> stat/ML**

## Fonction caractéristique

Dans ce paragraphe, nous introduisons un outil important en calcul des probabilités :
il s’agit de ce que l’on appelle *la fonction caractéristique* d’une variable aléatoire,
et qui dans d’autres branches des mathématiques s’appelle aussi *la transformée de Fourier*. Elle nous sera notamment très utile pour démontrer le théorème central limite.

On notera $< x, y >$ le produit scalaire de deux vecteurs de $\R^n$ . Si $u \in \R^n$ , la fonction (complexe) $x \mapsto e^{i < u,x>}$ est continue, de module 1. Donc si $X$ est un vecteur aléatoire à valeurs dans $\R^n$ , nous pouvons considérer $e^{i < u,x>}$ comme une variable aléatoire à valeurs complexes. Ses parties réelle $Y = \cos(< u, X>)$ et imaginaire $Z = \sin(< u, X>)$ sont des variables aléatoires réelles. Ces variables aléatoires réelles
sont de plus bornées par 1, donc elles admettent une espérance. Il est alors naturel d’écrire que l’espérance de $e^{i < u,x>}$ est
    $$\Esp(e^{i < u,x>}) = \Esp(Y) + i \Esp(Z) = \Esp(\cos< u, X>) + i\Esp(\sin< u, X>) $$

### Définition {.definition}
Si $X$ est un vecteur aléatoire à valeurs dans $\R^n$, sa *fonction caractéristique* est la fonction $\phi_X$ de $\R^n$ dans $\C$ définie par
    $$ \phi_X(u) = \Esp(e^{i < u,x>}).$$

### Remarque {.remark}
La fonction caractéristique ne dépend en fait **que de la loi $\P_X$ de $X$** : c’est la “transformée de Fourier” de la loi $\P_X$.

Nous verrons que cette fonction porte bien son nom, au sens où elle caractérise la loi $\P_X$. C’est une notion qui, de ce point de vue, généralise la fonction génératrice $G$ qui a été vue en CPGE. Elle vérifie
    $$\phi_X(u) = G_X(e^{iu}) = \Esp(e^{iuX}) $$
pour une variable $X$ à valeurs dans $\N$.

### Proposition {.proposition}
$\phi_X$ est de module inférieur à 1, continue, avec
    $$ \phi(0) = 1 ; \phi_X(-u) = \overline{\phi_X(u)}.$$

### Démonstration {.proof}
$|z|$ désigne le module d'un nombre complexe $z$.

Comme $\Esp(Y)^2 \leq \Esp(Y^2)$ pour toute variable réelle $Y$, on a :
$$ |\phi_X(u)|^2 = \Esp(\cos< u, X>)^2 + \Esp(\sin< u, X>)^2 \leq \Esp(\cos^2< u, X> + \sin^2< u, X>) = 1.$$

Pour montrer la continuité, considérons une suite $u_p \xrightarrow[p \to \infty]{} u$. Il y a convergence simple de $e^{i < u_p,X>}$ vers $e^{i < u,X>}$. Comme ces variables aléatoires sont de module borné par 1, le théorème de convergence dominée assure que $\phi_X(u_p) \xrightarrow[p \to \infty]{} \phi_X(u)$. $\phi_X$ est donc continue.

### Proposition {.proposition #fct_carac_vec}
Si $X$ est un vecteur aléatoire à valeurs dans $\R^n$, si $a \in \R^m$ et $A$ est une matrice réelle de taille $m \times n$, alors 
    $$ \phi{a+AX}(u) = e^{i < u,a>} \phi_X (A^t u), \forall u \in \R^m$$

### Démonstration {.proof}
Nous avons $e^{i< u, a + AX>} = e^{i < u,a>}e^{i <A^tu, X>}$. En effet, $< u, A X> = < A^t u, X>$. On prend ensuite les espérances pour obtenir le résultat.

### Exemples {.example #ex}

 1. $X$ suit une loi binomiale $\mathcal{B}(n,p)$ : $\phi_X(u) = (p e^{iu}+ 1- p)^n$.
 2. $X$ suit une loi de Poisson $\mathcal{P}(\theta)$ : $\phi_X(u) = e^{\theta (e^{iu}-1)}$.
 3. $X$ suit une loi uniforme $\mathcal{U}_{[a,b]}$ :$\phi_X(u) = \frac{e^{iua} - e^{iub}}{iu(b-a)}$.
 4. $X$ suit une loi exponentielle $\mathcal{E}(\lambda)$, $\lambda > 0$ : $\phi_X(u) = \frac{\lambda}{\lambda - iu}$.
 5. $X$ suit une loi normale $\No(0,1)$ : $\phi_X(u) = e^{-u^2/2}$.
 6. $X$ suit une loi normale $\No(\mu,\sigma^2)$ : $\phi_X(u) = e^{iu\mu -u^2\sigma^2/2}$.

L’intérêt majeur de la fonction caractéristique réside dans le fait qu’elle caractérise la
loi de la variable aléatoire (d'où son nom).

### Théorème {.theorem #caracfc}
La fonction caractéristique $\phi_X$ caractérise la loi du vecteur aléatoire $X$. Ainsi, si deux vecteurs aléatoires $X$ et $Y$ ont même fonction caractéristique, ils ont même loi.

### Démonstration {.proof}
Soient les fonctions suivantes avec $\sigma > 0$ :
    $$ f_\sigma (x) = \frac{1}{(2\pi \sigma^2)^{n/2}}\exp\left(-\frac{|x|^2}{2\sigma^2}\right) \text{ et } \widehat{f}_\sigma (u)= \exp\left(-\frac{|u|^2}{2\sigma^2}\right).$$
On a 
\begin{align*}
\int f_\sigma (x) e^{i < u,x>} dx &= \int{\R^n} \prod_{j=1}^n \frac{1}{\sqrt{2\pi \sigma^2}}\exp\left(-\frac{x_j^2}{2\sigma^2}+iu_j x_j\right) dx_1\ldots dx_n \\
                                  &= \prod_{j=1}^n \int{\R} \frac{1}{\sqrt{2\pi \sigma^2}}\exp\left(-\frac{t^2}{2\sigma^2}+iu_j t\right) dt = \widehat{f}_\sigma(u)
\end{align*}
d'après l'exemple 5 [ci-dessus](ex) et en utilisant le théorème de Fubini. On remarque ainsi que
$$ f_\sigma (u-v) = \frac{1}{(2\pi \sigma^2)^{n/2}} \widehat{f}_\sigma(\frac{u-v}{\sigma^2}) = \frac{1}{(2\pi \sigma^2)^{n/2}} \int f_\sigma (x) e^{i < u -v ,x>/\sigma^2} dx.$$

Supposons que $X$ et $X'$ admettent la même fonction caractéristique $\phi_X = \phi_{X'}$. En utilisant le théorème de Fubini, on a 
\begin{align*}
\int f_\sigma (u-v) \P_X (du) &= \int_{\R^n} \frac{1}{(2\pi \sigma^2)^{n/2}} \left( \int_{\R^n} f_\sigma (x) e^{i < u -v ,x>/\sigma^2} dx \right) \P_X (du)\\
                              &= \int_{\R^n} f_\sigma (x) \frac{1}{(2\pi \sigma^2)^{n/2}} \phi_X(\frac{x}{\sigma^2}) e^{-i < v ,x>/\sigma^2} dx,
\end{align*}

et la même égalité reste vraie pour $\P_{X'}$. Par suite $\Esp(g(X)) = \Esp(g(X'))$ pour toute fonction $g$ de l'espace vectoriel de fonction engendrées par $u \mapsto f_\sigma (u-v)$. D'après le théorème de Stone-Weiertrass, cet espace est dense dans l'ensemble $C_0$ des fonctions continues sur $\R^n$ et ayant une limite nulle à l'infini, pour la topologie de la convergence uniforme. Par suite, $\Esp(g(X)) = \Esp(g(X'))$ pour toute fonction $g \in C_0$. Comme l'indicatrice de tout ouvert est limite croissante de fonctions de $C_0$, on en déduit que $\P_X(A) = \Esp(1_A (X))$ est égal à $\P_{X'}(A) = \Esp(1_A (X'))$ pour tout ouvert $A$, ce qui implique $P_X = P_{X'}$.

### {.anonymous}
La fonction caractéristique offre également un moyen commode de caractériser l'indépendance.

### Corollaire {.corollary}
Soit $X = (X_1,\ldots,X_n)$ un vecteur aléatoire à valeurs dans $\R^n$. Ses composantes $X_i$ sont indépendantes si et seulement si pour tous $u_1, \ldots, u_n \in \R$, 
    $$ \phi_X(u_1,\ldots,u_n) = \prod_{j=1}^n \phi_{X_j}(u_j) $$
où $\phi_X$ désigne la fonction caractéristique du vecteur aléatoire $X$, et $\phi_{X_j}$ celle de la composante $X_j$ opur chaque $j$.

### Démonstration {.proof}
On a $< u,X> = \sum_{j=1}^n u_j X_j$. Si les $X_i$ sont indépendantes, et comme $e^{i < u,x>} = \prod_j e^{i u_j x_j}$, nous obtenons directement le résultat en utilisant la [proposition](Probabilité II.pdf #indep_fct).

Supposons inversement qu'on ait $\phi_X (u_1,\ldots,u_n) = \prod_{j=1}^n \phi_{X_j}(u_j)$. On peut alors construire des variables aléatoires $X'_j$ indépendantes, telles que $X'_j$ et $X_j$ aient même loi pour tout $j$ et donc telles que $\phi_{X'_j} = \phi_{X_j}$. Si $X' = (X'_1,\ldots,X'_n)$, on a donc $\phi_{X'} = \phi_X$. Donc $X$ et $X'$ ont même loi, ce qui entraîne que pour tous boréliens $A_j$, on ait
$$ \P(\bigcap_j \{X_j \in A_j\}) = \P(\bigcap_j \{X'_j \in A_j\}) = \prod_j \P(\{X'_j \in A_j\}) = \prod_j \P(\{X_j \in A_j\})$$
d'où l'indépendance.

### Proposition {.proposition #fct_carac_sum}
Si $X$ et $Y$ sont deux vecteurs aléatoires indépendants à valeurs dans $\R^n$, la fonction caractéristique de la somme $X+Y$ est donnée par
    $$ \phi_{X+Y} = \phi_X\phi_Y$$

### Démonstration {.proof}
Comme $e^{i< u, X+Y>}=e^{i< u, X>}e^{i< u, Y>}$, il suffit d'appliquer la [proposition](Probabilité II.pdf #indep_fct).

### Exemples :
Soient $X$ et $Y deux variables aléatoires réelles indépendantes et $Z = X+Y$ :

 1. Si $X$ suit la loi normale $\No(m,\sigma^2)$ et $Y$ suit $\No(m',\sigma'^2)$, alors $Z$ suit une loi $\No(m+m',\sigma^2+\sigma'^2)$, d'après l'[exemple](#ex) point 6. et la [proposition](#fct_carac_sum).
 2. Si $X$ et $Y$ suivent des lois de Poisson de paramètres $\theta$ et $\theta'$, alors $Z$ suit une loi de Poisson de paramètre $\theta + \theta'$, d'après l'[exemple](#ex) point 2. et la [proposition](#fct_carac_sum).
 3. Si $X$ suit une loi binomiale $\mathcal{B}(n,p)$ et $Y$ la loi biomiale $\mathcal{B}(m,p)$, alors $Z$ suit une loi binomiale $\mathcal{B}(n+m,p)$, d'après l'[exemple](#ex) point 1. et la [proposition](#fct_carac_sum).

### Proposition {.proposition #fct_carac_deriv}
Soit $X$ un vecteur aléatoire de $\R^n$. Si la variable $|X|^m$ (ou $|\cdot|$ désigne la norme euclidienne) est intégrable pour un entier $m$, la fonction $\phi_X$ est $m$ fois continûment différentiable sur $\R^n$ et pour tout choix des indices $i_1,\ldots, i_m$, 
    $$ \frac{\partial^m}{\partial u_{i_1}\ldots \partial u_{i_m}} \phi_X(u) = i^m \Esp (e^{i < u,X >}X_{i_1}\ldots X_{i_m}),$$
où les $X_j$ sont les composantes de $X$.

### Démonstration {.proof}
Le résultat se démontre par application itérée du théorème de dérivation sous le signe somme.

### Remarque {.remark}
En prenant $u=0$ dans la [proposition](#fct_carac_sum), la formule permet de calculer $\Esp(X_{i_1}\ldots X_{i_m})$ en fonction des dérivées à l'origine de $\phi_X$, autrement dit de calculer tous les moments du vecteur $X$, s'ils existent. Par exemple, si $X$ est à valeurs réelles et est intégrable (respectivement de carré intégrable), nous avons
    $$ \Esp(X) = i \phi'_X(0), (\text{resp.} \Esp(X^2) = \phi"_X(0))$$

### Théorème {.theorem #fct_carac_gauss}
$X$ est un vecteur gaussien si et seulement si sa fonction caractéristique s'écrit
    $$\phi_X(u) = e^{i< u,m> - \frac{1}{2}< u,Cu>}$$
où $m = \Esp(X) \in \R^n$ et $C$ est la matrice de covariance de $X$.

### Démonstration {.proof}

 1. Supposons $\phi_X(u) = e^{i< u,m> - \frac{1}{2}< u,Cu>}$. Pour toute combinaison linéaire $Y = \sum_j a_j X_j = < a, X >$, et pour tout $v \in \R$, on a 
    $$ \phi_Y(v) = \phi_X(va) = e^{iv< a ,m> - \frac{v^2}{2}< a,Ca>}$$
    donc $Y$ suit la loi $\No(< a, m>, < a, Ca>)$.
 2. Inversement, soit $C$ la matrice de covariance de $X$ et $m$ son vecteur moyenne. Si $Y = < a, X > = \sum_{j=1}^n a_j X_j$ avec $a\in\R^n$, un calcul simple montre
        $$ \Esp(Y) = < a, m >, \V(Y) = < a, Ca> $$
    Par hypothèse, $Y$ suit une loi normale donc vu le point 6. de l'[exemple plus haut](#ex), sa fonction caractéristique est
        $$ \phi_Y(v) = e^{iv< a ,m> - \frac{v^2}{2}< a,Ca>} $$
    Mais $\phi_Y(1) = \phi_{< a,X>} (1) = \Esp (e^{i < a, X>}) = \phi_X(a)$, d'où le résultat.

Le théorème suivant caractérise la convergence en loi à l’aide des fonctions caractéristiques. C’est un critère extrêmement utile dans la pratique.

### Théorème de Lévy {.theorem #levytheorem}
Soit $(X_n)_{n \in \N^\star}$ une suite de vecteurs aléatoires à valeurs dans $\R^d$.

 1. Si la suite $(X_n)_{n \in \N^\star}$ converge en loi vers $X$, alors $\phi_{X_n}$ converge simplement vers $\phi_X$.

 2. Si les $\phi_{X_n}$ convergent simplement vers une fonction (complexe) $\phi$ sur $\R^d$ et si cette fonction est **continue** en 0, alors c'est la fonction caractéristique d'une variable aléatoire $X$ et $X_n \xrightarrow{\L} X$.

### Démonstration {.proof}

 1. On remarque que $\phi_{X_n}(u) = \Esp(g_u(X_n))$ et $\phi_X(u) = \Esp(g_u(X))$ où $g_u$ est la fonction continue bornée $g_u(x) = e^{i < u,x>}$. On applique alors la [définition](#defconvloi).
 2. Admis.

## Théorème central limite
Ce théorème est aussi connu sous le nom de théorème de la limite centrale. Plus simplement, il apparaît souvent sous l’abréviation TCL.

On considère une suite de variables aléatoire $(X_n)_{n \in \N^\star}$ indépendantes, de même loi et de carré intégrable. On note $m$ et $\sigma^2$ la moyenne et la variance commune aux variables $X_n$, et
    $$S_n = X_1 + \ldots X_n$$
ainsi ($S_n = n M_n$). On a vu que la loi des grands nombres assure que $M_n$ converge vers $m$ presque-sûrement et en moyenne. On va s'intéresser a la vitesse à laquelle cette convergence a lieu.

Pour évaluer cette vitesse, c’est-à-dire trouver un équivalent de $\frac{S_n}{n} - m$, on est amenés à étudier la limite éventuelle de la suite $n^\alpha (\frac{S_n}{n} - m)$ pour différentes valeurs de $\alpha$ : si $\alpha$ est “petit” cette suite va encore tendre vers 0, et elle va “exploser” si $\alpha$est “grand”. On peut espérer que pour une (et alors nécessairement une seule) valeur de $\alpha$, cette suite converge vers une limite qui n’est ni infinie ni nulle.

Il se trouve que la réponse à cette question a un aspect “négatif” : la suite $n^\alpha (\frac{S_n}{n} - m)$ ne converge au sens presque-sûr, ou même en probabilité, pour aucune valeur de $\alpha$. Elle a aussi un aspect “positif” : cette suite converge, au sens de la convergence en loi, pour la même valeur $\alpha = 1/2$ quelle que soit la loi des $X_n$, et toujours vers une loi normale.

Ce résultat, qui peut sembler miraculeux, a été énoncé par Laplace (1749-1827) et démontré beaucoup plus tard par Lyapounov (1901). Il montre le caractère universel de la loi normal en probabilités (d'où son nom). Il fait l’objet du théorème suivant, appelé théorème central limite (TCL), ou de la limite centrale.

### Théorème central limite {.theorem #TCL}
Si les $X_n$ sont des variables aléatoires réelles, indépendantes et de même loi, de carré intégrable, de moyenne $m$ et de variance $\sigma^2 >0$, alors les variables
    $$ \frac{S_n -nm}{\sigma \sqrt{n}}$$
convergent en loi vers une variable aléatoire de loi $\No(0,1)$.

En d'autres termes, $\sqrt{n}(M_n - m)$ converge vers une variable normale de loi $\No(0,\sigma^2)$.

### Démonstration {.proof}
Soit $\phi$ la fonction caractéristique de $X_n - m $, et $Y_n = \frac{S_n -nm}{\sigma \sqrt{n}}$. D'après la [proposition](#fct_carac_vec) et la [proposition](#fct_carac_sum), la fonction caractéristique de $Y_n$ est 
    $$\phi_n(u) = \phi\left(\frac{u}{\sigma\sqrt{n}}\right)^n .$$
Comme $\Esp(X_n -m) = 0$ et $\Esp((X_n-m)^2) = \sigma^2$, la [proposition](#fct_carac_deriv) entraîne 
    $$\phi(u) = 1 - \frac{u^2\sigma^2}{2} + u^2 o (|u|) \text{ quand } u \rightarrow 0.$$
Comme $\phi(0) = 1$ et que $\phi$ est continue en 0, on a  que pour $u$ fixé et $n$ assez grand,
    $$ \left| \phi\left(\frac{u}{\sigma\sqrt{n}}\right)-1\right| \leq 1/2. $$
Il est possible de généraliser la notion de logarithme aux complexes $z$ tels que $|z  -1| \leq 1/2$. La fonction $\log z$ définie sur le disque $\{z\in \C; |z  -1| \leq 1/2\}$ admet le même développement limité au voisinage de $z = 1$ que le logarithme réel. Ainsi
    $$ \phi_n(u) = \exp \left( n \log\left(1 - \frac{u^2}{2n} + \frac{1}{n}\epsilon_n(u) \right)\right),$$
où $\epsilon_n(u)$ tend vers 0 quand $n$ tend vers l'infini, et on en déduit que $\phi_n(u)$ tend vers $\exp(-u^2/2)$. Le résultat découle alors du [théorème de Lévy](#levytheorem).

### Remarque {.remark}

On peut déduire de ce résultat que $n^\alpha (\frac{S_n}{n} - m)$ converge vers 0 (resp. $+\infty$) en probabilité lorsque $\alpha < 1/2$ (resp. $\alpha > 1/2$).

### Exemple : convergence des lois binomiales
Supposons que $S_n$ suive une loi binomiale $\mathcal{B}(p,n)$. Cela revient à dire que $S_n$ a la même loi qu'une somme $X_1+\ldots+X_n$ de $n$ variables aléatoires $X_i$ indépendantes de loi $\mathcal{B}(p,1)$, i.e. $\P(X_i= 1) = p$ et $\P(X_i= 0) = 1- p$. On a alors $m=p$ et $\sigma^2= p(1-p)$.

On veut calculer $\P(S_n \leq x)$ pour $x$ fixé et $n$ grand.

Si $p$ est petit de sorte que $\theta = np$ ne soit pas trop grand (en pratique, $\theta \leq 5$ convient), on peut utiliser l’approximation par une loi de Poisson, vue en CPGE. Si $p$ est très proche de 1, de sorte que $\theta = n(1 - p)$ soit comme ci-dessus, alors $n - S_n$ suit à son tour une loi proche de la loi de Poisson de paramètre $\theta$.

Dans les autres cas, on utilise la loi des grands nombres et le théorème central limite :
\begin{align*}
\frac{S_n}{n} & \xrightarrow{\P} p,\\
\frac{S_n - np}{\sqrt{n p(1-p)}} & \xrightarrow{\L} \No(0,1)
\end{align*}

Si on désigne par $\Phi$ la fonction de répartition de la loi $\No(0,1)$, il vient 
    $$\P(S_n \leq x) \approx \Phi \left(\frac{x - np}{\sqrt{n p(1-p)}}\right)$$

Imaginons que l'on lance 1000 fois une pièce (non truquée). On cherche la probabilité d’obtenir plus de 545 fois le côté Face. Le calcul exact utilisant les lois binomiales est extrêmement lourd. Le résultat ci-dessus nous donne une très bonne approximation. On a
    $$ \P(S_{1000} > 545) = \P\left(\frac{S_{1000} - 500}{\sqrt{250}} > \frac{45}{\sqrt{250}}\right) \approx \int_{\frac{45}{\sqrt{250}}}^{+\infty} \frac{1}{\sqrt{2\pi}} e^{-x^2/2} dx.$$

Cette dernière intégrale se calcule numériquement (on trouve encore des abaques où les valeurs de $\Phi$ sont tabulées) et on obtient
    $$ \P(S_{1000} > 545) \approx 1 - \Phi(2,84) \approx 0,0023.$$

Le [théorème](#TCL) admet une version multidimensionnelle, de preuve similaire. On considère des vecteurs aléatoires $X_n$ à valeurs dans $\R^d$, indépendants et de même loi, dont les composantes sont de carré intégrable. On a un vecteur moyenne $m = E(X_n)$, et une matrice de covariance $C = (c_{ij} )_{i,j=1,\ldots,d}$ avec $c_ij = \cov(X_i,X_j)$. On peut alors énoncer le TCL multi-dimensionnel.

### Théorème central limite multi-dimensionnel {.theorem}
Les vecteurs aléatoires $\frac{S_n-nm}{\sqrt{n}}$ convergent en loi vers un vecteur aléatoire gaussien centré (i.e. de moyenne nulle), de matrice $C$.