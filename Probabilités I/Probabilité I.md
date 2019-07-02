% Probabilités I

<!-- LaTeX Macros -->
\newcommand{\R}{\mathbb{R}}
\renewcommand{\P}{\mathbb{P}}
\renewcommand{\C}{\mathbb{C}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\A}{\mathcal{A}}


# Introduction 

Le but de ce cours est de consolider et compléter les connaissances en théorie des probabilités acquises en CPGE mais surtout de permettre d’acquérir le raisonnement probabiliste. En effet, les probabilités peuvent être vues comme un outil de modélisation de phénomènes qui ont la caractéristique d'être aléatoires. Elles sont aussi un préalable indispensable pour aborder l'analyse statistique des données et les méthodes d'apprentissage automatique.

## Historique 

Avant que l'étude des probabilités soit considérée comme une science, l'observation du hasard dans les événements naturels a amené les philosophes et les scientifiques à réfléchir sur la notion de liens entre événements, causes et conséquences, et lois de la nature. Les jeux de hasard, les situations météorologiques ou les trajectoires des astres ont fait partie des domaines étudiés. Les explications données sont alors liées au destin, à une colère céleste ou à une présence divine.

Il est communément admis que le début de la science des probabilités se situe au XVIe siècle avec l'analyse de jeux de hasard par Jérôme Cardan et au XVIIe siècle avec les discussions entre Pierre de Fermat et Blaise Pascal au sujet de paradoxes issus de ces jeux, notamment posés par Antoine Gombaud, chevalier de Méré. Cette nouvelle théorie est nommée géométrie aléatoire par le chevalier de Méré en 1654, elle est appelée par la suite calcul conjectural, arithmétique politique et plus communément aujourd'hui théorie des probabilités. Cette théorie, dite des probabilités modernes, est alors étudiée par de nombreux penseurs jusqu'au XIXe siècle : Kepler, Galilée, Leibniz, Huygens, Halley, Buffon, les frères Bernoulli, Moivre, Euler, D'Alembert, Condorcet, Laplace, Fourier. Elle est principalement basée sur les événements discrets et la combinatoire.

Des considérations analytiques ont forcé l'introduction de variables aléatoires continues dans la théorie. Cette idée prend tout son essor dans la théorie moderne des probabilités, dont les fondations ont été posées par Andreï Nikolaevich Kolmogorov. Kolmogorov combina la notion d'univers, introduite par Richard von Mises et la théorie de la mesure pour présenter son système d'axiomes pour la théorie des probabilités en 1933. Très vite, son approche devint la base incontestée des probabilités modernes.

Le XXe siècle voit également le développement de l'application de la théorie des probabilités dans plusieurs sciences.

Avec la mécanique newtonienne, la théorie du champ électromagnétique ou la thermodynamique, la physique classique est la théorie utilisée jusqu'à la fin du XIXe siècle. En 1925, Erwin Schrödinger étudie l'équation qui détermine l'évolution d'une onde au cours du temps : l'équation de Schrödinger. Max Born utilise cette équation pour décrire une collision entre des particules telles que des électrons ou des atomes. Les observations de ces expériences l'amènent à supposer que la fonction d'onde est la probabilité que la particule soit détectée en un point de l'espace. C'est le début d'une nouvelle approche de la physique quantique.

En 1900, Louis Bachelier fut un des premiers mathématiciens à modéliser les variations de prix boursiers grâce à des variables aléatoiresa. « le marché n'obéit qu'à une seule loi : la loi du hasard ». Bachelier utilise alors le calcul stochastique pour étudier les variations boursières au cours du temps. En 1970, Fischer Black et Myron Scholes reprennent les idées de Bachelier pour modéliser les rendements d'une action.

L'utilisation des probabilités en biologie a pris un essor dans les années 1970, notamment dans l'étude de l'évolution des espèces. La reproduction des individus est modélisée par un choix aléatoire des gènes transmis ainsi que des mutations apparaissant de manière aléatoire sur les individus. L'extinction des espèces ou des gènes est alors étudiée en fonction des effets stochastiques.

De nos jours, l’Ecole française de Probabilités est très active. La première Médaille Fields décernée à un probabiliste a été attribuée à Wendelin Werner en 2006. Les probabilités se développent de plus en plus, alimentées en particulier de manière essentielle par la physique, le développement des réseaux de télécommunications, la finance, la biologie, la médecine... Elles permettent de construire des modèles mathématiques, qui peuvent être validés par les données suivant la théorie statistique, et fournissent également des possibilités d’expérimentations fictives dans de multiples domaines d’applications.

## Plan du cours

Le cours est organisé en 5 amphis : 
Description des notions importantes du poly : variables aléatoires, conditionnement et indépendance, lois des grands nombres, simulation
Ouverture vers les stats

**TODO** à reprendre/développer

# Probabilités des évènements 

## Phénomènes aléatoires

L’objet de la théorie des probabilités est l’analyse mathématique de phénomènes dans lesquels le hasard intervient. Les phénomènes aléatoires résultent d'expériences dont le résultat ne peut être prédit à l'avance et qui peut varier si on répète l'expérience dans des conditions identiques.

Il est aisé de trouver des exemples de tels phénomènes.

### Exemples {.example}

 1. Jeu de Pile ou Face
 2. Lancé de dés
 3. Durée de vie d'une ampoule électrique
 4. Température demain à 12h au sommet de la tour Eiffel 
 5. Evolution du prix d'un actif financier sur un intervalle de temps $[t_1,t_2]$

La théorie des probabilités vise à fournir un modèle mathématiques pour décrire ces phénomènes. Elle repose sur trois ingrédients essentiels dont on donne ici les définitions.

### L'espace fondamental {.definition}

Noté habituellement $\Omega$, l'*espace fondamental* (ou encore l'*espace d'état* ou *univers*) contient l'ensemble de tous les résultats possibles d'un phénomène aléatoire. Un résultat possible d'une expérience sera noté $\omega \in \Omega$.

Si on reprend les exemples précédents, on peut facilement définir les univers associés :

### Exemples {.example}

 1. Jeu de Pile ou Face, $\Omega = \{\text{p, f}\}$
 2. Lancé de dés,  $\Omega = \{1,2,3,4,5,6\}$
 3. Durée de vie d'une ampoule électrique, $\Omega = [0,+\infty [$ 
 4. Température demain à 12h au sommet de la tour Eiffel (en degrés Kelvin), $\Omega = [0,+\infty [$
 5. Evolution du prix d'un actif financier sur un intervalle de temps $[t_1,t_2]$, $\Omega = C ([t_1,t_2],\R^+)$, ensemble des application continues de $[t_1,t_2]$ dans $\R^+$


### Evènements {.definition}
Un *évènement* est une propriété qui est vérifiée ou non une fois l'expérience réalisée. On identifie un évènement $A$ à une partie de $\Omega$, i.e. $A = \{\omega \in \Omega, A \text{ est vérifiée pour } \omega \}$.

### Exemples {.example}

 1. Jeu de Pile ou Face, $A = \{p\}$ 
 2. Lancé de dés,  $A = \{1,3,5\}$
 3. Durée de vie d'une ampoule électrique, $A = [t_1,t_2]$ 
 4. Température demain à 12h au sommet de la tour Eiffel (en degrés Kelvin), $A = [T_1,T_2]\cup[T_3,T_4]$
 5. Evolution du prix d'un actif financier sur un intervalle de temps $[t_1,t_2]$, 
 $A = \{ f \in C([t_1,t_2], \R^+), \|f-g\|_{\infty} \leq a \}$, où
 $g \in C([t_1,t_2],\R^+)$, $a \in \R^+$ 

**TODO:** tableau d'équivalence opérations ensemblistes et logiques (cf poly maisonneuve)

On doit maintenant répondre à la question de savoir quels sont les évènements dont on va vouloir évaluer la probabilité d'occurence. On va ainsi regrouper les évènements en un ensemble $\A$ qui constitue une collection de sous-ensembles de $\Omega$. En particulier, si les évènements $A$ et $B$  Ceci conduit à la notion de *tribu de parties* de $\Omega$.

### Tribu {.definition}
Une *tribu* $\A$ est une collection de sous-ensembles de $\Omega$ tels que

 1. $\Omega \in \A$.
 2. $A \in \A \Rightarrow A^c \in \A$.
 3. $\forall n \in \N, A_n \in \A \Rightarrow \bigcup_n A_n \in \A$.
Le couple $(\Omega, \A)$ est appelé *espace probabilisable*.

### Exemples {.exemples}
 1. Dans le cas où $\Omega$ est au plus dénombrable, on le munit généralement de l'ensemble $\mathcal{P}(\Omega)$ des parties de $\Omega$
 2. Si $\Omega = \R$, on le munit de la *tribu borélienne* de $\R$, notée $\mathcal{B}(\R)$ **TODO voir si déjà vu en CI**
 3. On verra par la suite qu'il est aisé de définir une tribu sur tout espace topologique **plus tard ?** 

### Probabilité {.definition #defproba}
Une *probabilité* sur l'espace $(\Omega, \A)$ est une application $\P : \A \rightarrow [0,1]$, telle que :

 1. $\P(\Omega) = 1$,
 2. Pour toute suite (dénombrable) $(A_n)$ d'éléments de $\A$ **deux à deux disjoints**, on a 
 \begin{equation}
 \P(\bigcup_n A_n) = \sum_n A_n.
 \end{equation}

Le triplet $(\Omega, \A, \P)$ est appelé *espace probabilisé*. La modélisation probabiliste consiste ainsi à décrire une expérience
aléatoire par la donnée d’un espace probabilisé.

### Propriétés élémentaires 
 1. $\forall A \in \A, \P(A) \in [0,1]$ et $\P(A^c)= 1-\P(A)$
 2. $\forall A,B \in \A, A \subset B \Rightarrow \P(A) \leq \P(B)$
 3. $\forall A,B \in \A, \P(A \cup B ) = \P(A) + \P(B) - \P(A \cap B)$
 4. Inégalité de Boole, $\forall (A_i)_{1 \leq i \leq n} \in \A \P(\bigcup_{i=1}^n A_i) \leq \sum_{i=1}^n A_i$
 5. Formule de Poincaré $\forall (A_i)_{1 \leq i \leq n} \in \A$
 $$ \P(\bigcup_{i=1}^n A_i) = \sum_{i=1}^n \P(A_i) - \sum_{1 \leq i < j \leq n} \P(A_i \cap A_j) + \ldots + (-1)^n \P(\cap_{i=1}^n A_i)$$

### Demonstration {.proof}
Exercice

### Théorème de la continuité monotone
Dans le cas d'une suite $(A_n) \in \A$ croissante, on a 
$$ \P(\bigcup_n A_n) = \lim_{n \rightarrow \infty} \P(A_n)$$

### Demonstration {.proof}
Exercice

### Remarque {.remark}
Dans le cas d'une suite décroissante, on a 
$$ \P(\cap_{i=1}^n A_i) = \lim_{n \rightarrow \infty} \P(A_n)$$

### Lemme de Borel-Cantelli ??? ou alors à la fin 

## Probabilité conditionnelle 

### Probabilité conditionnelle {.definition}
Soient $(\Omega, \A, \P)$ un espace probabilisé, $A, B \in \A$ tels que $\P(B)>0$. La *probabilité conditionnelle* de $A$ sachant $B$, est le nombre 
\begin{equation}
\P(A|B) = \frac{\P(A\cap B)}{\P(B)}
\end{equation}

Cela définit une probabilité. En effet, on a :

### Proposition {.proposition}
 1. Soient $(\Omega, \A, \P)$ un espace probabilisé et $B \in A$ tel que $\P(B)>0$. Alors l’application de $\A$ dans $[0, 1]$ qui à $A$ associe $\P(A|B)$ définit une nouvelle probabilité sur $\Omega$, appelée probabilité conditionnelle sachant $B$.
 2. Si $\P(A) > 0$ et $\P(B) > 0$ , nous avons
$$P(A|B) P(B) = P(A \cap B) = P(B|A) P(A).$$

### Démonstration {.proof}
Il est clair que $0 \leq \P(A|B) \leq 1$. Par ailleurs, les deux propriétés de la [définition de la probabilité](#defproba)
pour $P(\cdot|B)$ proviennent des mêmes propriétés pour $\P$ et des remarques suivantes :
$\Omega \cap B = B$, et $(\bigcup_n A_n ) \cap B = \bigcup_n (A_n \cap B)$. De plus, si $A$ et $C$ sont disjoints, il en est
de même de $A \cap B$ et $C \cap B$. L’assertion 2. est évidente. d'après la définition de la [Probabilité conditionnelle].

### Formule des probabilités totales {.proposition}

Soit $(B_n)$ une partition finie ou dénombrable d’événements de $\Omega$ (i.e. telle que $\bigcup_n B_n = \Omega$ et les $B_n$ sont deux-à-deux disjoints), telle que $\P(B_n ) > 0$ pour tout n. Pour tout $A \in \A$, on a alors
\begin{equation}
P(A) = \sum_n P(A \bigcup_n B_n ) = \sum_n P(A|B_n) P(B_n).
\end{equation}

### Démonstration {.proof}
Nous avons $A = \bigcup_n (A\cap B_n)$. Par hypothèse, les ensembles $(A\cap B_n)$ sont deux-à-deux disjoints et de plus $\P(A\cap B_n) = \P(A|B_n)\P(B_n)$. Le résultat découle du deuxième point de la [définition de la probabilité](#defproba). 

### Formule de Bayes {.proposition}
Selon les mêmes hypothèses que ci-dessus et si $\P(A) > 0$, on a 
\begin{equation}
\forall i \P(B_i | A) = \frac{\P(A | B_i) \P(B_i)}{\sum_n \P(A | B_n) \P(A)}
\end{equation}

### Démonstration {.proof}
Le dénominateur vaut $\P(A)$ d'après la [Formule des probabilités totales]. La définition de la [probabilité conditionnelle] implique :
\begin{equation}
\P(B_i | A) = \frac{\P(A \cap B_i)}{\P(A)} = \frac{\P(A | B_i) \P(B_i)}{\P(A)}
\end{equation}

## Indépendance des évènements 
La notion d’indépendance est absolument fondamentale en probabilités et nous verrons
par la suite toutes ses implications dans la modélisation de l’aléatoire.

Intuitivement, deux événements $A$ et $B$ sont indépendants si le fait de savoir que $A$ est
réalisé ne donne aucune information sur la réalisation de $B$ et réciproquement.

### Indépendance de deux évènements {.definition}
Deux évènements $A$ et $B$ sont *indépendants* si et seulement si 
\begin{equation}
\P(A\cap B) = \P(A)\P(B)
\end{equation}

### Remarque {.remark}
 * La probabilité de voir $A$ réalisé ne dépend pas de la réalisation de $B$, et réciproquement.
 * Si $\P(A)>0$ et $\P(B)>0$, alors 
    \begin{equation}
    \P(A\cap B) = \P(A)\P(B) \Leftrightarrow \P(A) = \P(A|B) \Leftrightarrow \P(B) = \P(B|A)
    \end{equation}

## Proposition {.proposition}
Si les évènements $A$ et $B$ sont indépendants, alors il en est de même des couples $(A^c,B)$, $(A,B^c)$ et $(A^c,B^c)$.

# V.A. discretes

rappels rapides (complet avec lecture en autonomie ?) -> pas traité dans Bonnabel-Schmitt mais intéressant car analogies avec cas continu

# Définition d'une variable aléatoire réelle (cas $\Omega=\R$ ?)

# Variables aléatoires absolument continues -> plutôt en II

 * Fonction de répartition
 * Variables aléatoires à densité
 * Exemples
 * Lien avec la definition axiomatique ? (vérification de la $\sigma$-additivité dans le cas d'un univers réel, cf note SB)

aura-t-on le temps ? Sinon se limiter à une ouverture vers les v.a. à valeurs réelles

# Exercices
