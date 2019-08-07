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
Soit $\Lambda_{n,\epsilon} = \{|X_n - X| > \epsilon \}$.

 * Supposons que $X_n \to X$ p.s. et soit $N$ l'ensemble de probabilité nulle en dehors duquel on a $X_n(\omega) \to X(\omega)$. Si $\omega \notin N$, on a $\omega \notin \Lambda_{n,\epsilon}$ pour tout $n \geq n_0$, où $n_0$ dépende de $\omega$ et de $\epsilon$, ce qui implique que les variables aléatoires $Y_{n,\epsilon} = 1_{N^c\cap \Lambda_{n,\epsilon}}$ tendent simplement vers 0 lorsque $n \to \infty$. Comme on a aussi $0 \leq Y_{n,\epsilon} \leq 1$ le théorème de convergence dominée implique que $\Esp(Y_{n,\epsilon}) \xrightarrow[n \to \infty]{} 0.$ Mais
 $$\P(\Lambda_{n,\epsilon}) \leq \P(N^c \cap \Lambda_{n,\epsilon}) + \P(N) = \P(N^c \cap \Lambda_{n,\epsilon}) = \Esp(Y_{n,\epsilon}) \xrightarrow[n \to \infty]{} 0.$$

 * Supposons que $X_n \xrightarrow{\L^1} X$. Pour $\epsilon >0$, on a $1_{\Lambda_{n,\epsilon}} \leq \frac{1}{\epsilon}|X_n - X|$, donc 
 $$ \P(\Lambda_{n,\epsilon}) \leq \frac{1}{\epsilon}\Esp(|X_n - X|) \to 0.$$


La convergence en probabilité n’entraîne pas la convergence en moyenne, comme nous l’avons vu dans l’exemple ci-dessus, ne serait-ce que parce qu'elle n'implique pas l'appartenance de $X_n$ et $X$ à $\L^1$. Si les $X_n$ ne sont “pas trop grands”, il y a cependant équivalence entre les deux modes de convergence. En voici un exemple :

### Proposition {.proposition #propconv2}
S'il existe une constante $a$ telle que $|X_n| \leq a$ presque sûrement, il y a équivalence entre $X_n \xrightarrow{\P} X$ et $X_n \xrightarrow{\L^1} X$.

### Démonstration {.proof}
Etant donnée la [proposition précédente](#propconv1), dont on reprend les notations, il suffit de montrer que la convergence en probabilité implique la convergence en moyenne lorsque $|X_n| \leq a$.

Comme $|X_n| \leq a$, on a $\{|X| > a +\epsilon\} \subset \Lambda_{n,\epsilon}$, et donc $\P(|X| > a +\epsilon ) \leq \P(\Lambda_{n,\epsilon})$. En faisant $n \to \infty$, on en déduit que $\P(|X| > a + \epsilon) = 0$. Ceci est vrai pour tout $\epsilon$ et donc
$$\P(|X|> a) = 0.$$
Comme $|X_n| \leq a$, on a aussi
$$ |X_n -X| \leq \epsilon + (X_n + X) 1_{\Lambda_{n,\epsilon}} \leq \epsilon + 2a 1_{\Lambda_{n,\epsilon}}$$
sur l'ensemble $\{|X| \leq a \}$ qui est de probabilité 1. On a ainsi 
$$ \Esp(|X_n - X|) \leq \epsilon +2a \P(\Lambda_{n,\epsilon})$$
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

On considère des vecteurs aléatoires $X_n$ et $X$, tous à valeurs dans le même espace $\R^d$, mais pouvant éventuellement être définis sur des espaces de probabilité différents.

### Définition {.definition}
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


