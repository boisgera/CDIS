% Probabilités I

<!-- LaTeX Macros -->
\newcommand{\R}{\mathbb{R}}
\newcommand{\Q}{\mathbb{Q}}
\renewcommand{\P}{\mathbb{P}}
\renewcommand{\C}{\mathbb{C}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\A}{\mathcal{A}}
\newcommand{\E}{\mathcal{E}}
\newcommand{\B}{\mathcal{B}}


# Introduction 

Le but de ce cours est de consolider et compléter les connaissances en théorie des probabilités acquises en CPGE mais surtout de permettre d’acquérir le raisonnement probabiliste. En effet, les probabilités peuvent être vues comme un outil de modélisation de phénomènes qui ont la caractéristique d'être aléatoires. L'aléatoire peut intervenir de différentes manières dans ces phénomènes.

 
 * Dans les cas d'école que sont les jeux de pile ou face ou de lancés de dés, la différence entre les résultats, si l’on réitère l’expérience, peut être liée à l’impulsion initiale communiquée au dé et à d'autres facteurs environnementaux comme le vent, la rugosité de la table, etc. Le hasard intervient du fait de la méconnaissance des conditions initiales, car la pièce ou le dé ont des trajectoires parfaitement définies par la mécanique classique.
 * Dans beaucoup de cas de figure, on fait intervenir l'aléatoire dans la modélisation du fait d'une connaissance incomplète des phénomènes. On parle alors de modélisation de l'incertitude. C'est le cas par exemple en sciences du climat, dont nous discutons ci-dessous.
 * Dans certains domaines, tels la physique quantique, l'aléatoire fait intrinsèquement partie de la théorie.

Elles sont aussi un préalable indispensable pour aborder l'analyse statistique des données et les méthodes d'apprentissage automatique.

En CPGE, les probabilités ont été vues dans le cadre de phénomènes aléatoires qui admettent un nombre au plus dénombrable de résultats possibles. Ce cadre restreint est supposé connu. On pourra se reporter au chapitre 3 de @polygarnier ou aux deux premiers chapitres de @polyponts pour une éventuelle mise à niveau.

## Exemple de la modélisation du climat

Les prédictions de la météo et les projections du climat proviennent généralement de modèle numériques qui simulent les différents processus physiques à l'oeuvre. Les incertitudes dans la construction et l'application de ces modèles sont variées et peuvent être réparties en quatre groupes : les conditions initiales (on ne connaît jamais parfaitement l'ensemble des variables climatiques en tout point du globe), les conditions aux limites (par exemple lorsqu'on travaille à l'échelle d'un continent ou d'un pays), les valeurs des paramètres intervenant dans les modèles (constantes issues d'observations diverses), les incertitudes structurelles enfin qui relèvent des choix de modélisation. Pour tenir compte de ces incertitudes, les climatologues effectuent des ensembles de simulations, où les différentes quantités incertaines sont échantillonnées selon des modèles probabilistes (voir en particulier @tebaldi).

L'incertitude sur les conditions initiales est particulièrement influente aux faibles échelles de temps. La météo est un système chaotique, les prévisions sont particulièrement sensibles aux variations des conditions initiales utilisées pour initialiser les modèles. Ces dernières sont en revanche connues de manière imparfaite. Il est ainsi nécessaire de tenir compte de cette incertitude. Ceci est rendu possible par la modélisation probabiliste. Les conditions aux limites font intervenir des **variables continues** (température, pression, vitesse du vent, etc.), ce qui représente la principale nouveauté par rapport au programme de CPGE, et il est nécessaire de caractériser leurs relations de **dépendance**. Il convient par ailleurs de tenir compte des observations (satellites, station de mesure, ...) en incluant cette information dans la modélisation probabiliste. On parle de **conditionnement** aux données. Il s'agit enfin d'en générer les valeurs via des algorithmes de **simulation stochastique**. La validité de l'approche est assurée par les **théorèmes limites**, qui garantissent la représentativité des ensembles générés.

## Plan du cours

Le cours est organisé en 5 amphis et abordera consécutivement les notions évoquées ci-dessus, à savoir les probabilités définies sur $\R$, les variables et vecteurs aléatoires réels, l'indépendance et le conditionnement de variables aléatoires, l'étude des suites de variables aléatoires et, enfin, les méthodes de simulation stochastique.


## Historique 

Avant que l'étude des probabilités soit considérée comme une science, l'observation du hasard dans les événements naturels a amené les philosophes et les scientifiques à réfléchir sur la notion de liens entre événements, causes et conséquences, et lois de la nature. Les jeux de hasard, les situations météorologiques ou les trajectoires des astres ont fait partie des domaines étudiés. Les explications données sont alors liées au destin, à une colère céleste ou à une présence divine.

Il est communément admis que le début de la science des probabilités se situe au XVIe siècle avec l'analyse de jeux de hasard par Jérôme Cardan et au XVIIe siècle avec les discussions entre Pierre de Fermat et Blaise Pascal au sujet de paradoxes issus de ces jeux, notamment posés par Antoine Gombaud, chevalier de Méré. Cette nouvelle théorie est nommée géométrie aléatoire par le chevalier de Méré en 1654, elle est appelée par la suite calcul conjectural, arithmétique politique et plus communément aujourd'hui théorie des probabilités. Cette théorie, dite des probabilités modernes, est alors étudiée par de nombreux penseurs jusqu'au XIXe siècle : Kepler, Galilée, Leibniz, Huygens, Halley, Buffon, les frères Bernoulli, Moivre, Euler, D'Alembert, Condorcet, Laplace, Fourier. Elle est principalement basée sur les événements discrets et la combinatoire.

Des considérations analytiques ont forcé l'introduction de variables aléatoires continues dans la théorie. Cette idée prend tout son essor dans la théorie moderne des probabilités, dont les fondations ont été posées par Andreï Nikolaevich Kolmogorov. Kolmogorov combina la notion d'univers, introduite par Richard von Mises et la théorie de la mesure pour présenter son système d'axiomes pour la théorie des probabilités en 1933. Très vite, son approche devint la base incontestée des probabilités modernes.

Le XXe siècle voit également le développement de l'application de la théorie des probabilités dans plusieurs sciences.

Avec la mécanique newtonienne, la théorie du champ électromagnétique ou la thermodynamique, la physique classique est la théorie utilisée jusqu'à la fin du XIXe siècle. En 1925, Erwin Schrödinger étudie l'équation qui détermine l'évolution d'une onde au cours du temps : l'équation de Schrödinger. Max Born utilise cette équation pour décrire une collision entre des particules telles que des électrons ou des atomes. Les observations de ces expériences l'amènent à supposer que la fonction d'onde est la probabilité que la particule soit détectée en un point de l'espace. C'est le début d'une nouvelle approche de la physique quantique.

En 1900, Louis Bachelier fut un des premiers mathématiciens à modéliser les variations de prix boursiers grâce à des variables aléatoires. « le marché n'obéit qu'à une seule loi : la loi du hasard ». Bachelier utilise alors le calcul stochastique pour étudier les variations boursières au cours du temps. En 1970, Fischer Black et Myron Scholes reprennent les idées de Bachelier pour modéliser les rendements d'une action.

L'utilisation des probabilités en biologie a pris un essor dans les années 1970, notamment dans l'étude de l'évolution des espèces. La reproduction des individus est modélisée par un choix aléatoire des gènes transmis ainsi que des mutations apparaissant de manière aléatoire sur les individus. L'extinction des espèces ou des gènes est alors étudiée en fonction des effets stochastiques.

De nos jours, l’Ecole française de Probabilités est très active. La première Médaille Fields décernée à un probabiliste a été attribuée à Wendelin Werner en 2006. Les probabilités se développent de plus en plus, alimentées en particulier de manière essentielle par la physique, le développement des réseaux de télécommunications, la finance, la biologie, la médecine... Elles permettent de construire des modèles mathématiques, qui peuvent être validés par les données suivant la théorie statistique, et fournissent également des possibilités d’expérimentations fictives dans de multiples domaines d’applications.

# Probabilités des événements 

## Phénomènes aléatoires et événements

L’objet de la théorie des probabilités est l’analyse mathématique de phénomènes dans lesquels le hasard intervient. Les phénomènes aléatoires résultent d'expériences dont le résultat ne peut être prédit à l'avance et qui **peut** varier si on répète l'expérience dans des conditions identiques. 

Il est aisé de trouver des exemples de tels phénomènes.

### Exemples {.example}

 1. Jeu de Pile ou Face
 2. Lancé de dés
 3. Durée de vie d'une ampoule électrique
 4. Température demain à 12h au sommet de la tour Eiffel 
 5. Evolution de la vitesse d’une molécule dans un gaz raréfié sur un intervalle de temps $[t_1,t_2]$

La théorie des probabilités vise à fournir un modèle mathématique pour décrire ces phénomènes. Elle repose sur trois ingrédients essentiels dont on donne ici les définitions.

### Définition -- L'espace fondamental {.definition}

Noté habituellement $\Omega$, l'*espace fondamental* (ou encore l'*espace d'état* ou *univers*) contient l'ensemble de tous les résultats possibles d'un phénomène aléatoire. Un résultat possible d'une expérience sera noté $\omega \in \Omega$.

Si on reprend les exemples précédents, on peut facilement définir les univers associés.

### Exemples {.example}

 1. Jeu de Pile ou Face, $\Omega = \{\text{pile}, \text{face}\}$
 2. Lancé de dés,  $\Omega = \{1,2,3,4,5,6\}$
 3. Durée de vie d'une ampoule électrique, $\Omega = [0,+\infty [$ 
 4. Température demain à 12h au sommet de la tour Eiffel (en degrés Kelvin), $\Omega = [0,+\infty [$
 5. Evolution de la vitesse d’une molécule dans un gaz raréfié sur un intervalle de temps $[t_1,t_2]$, $\Omega$ : ensemble des application continues sur $[t_1,t_2]$ à valeurs dans $\R^3$

Cette liste d’exemples montre que l’espace $\Omega$ peut varier énormément dans sa structure, d’une expérience à l’autre. Cela permet de réaliser la richesse de la théorie qu’il faut mettre en place, pour créer un modèle qui englobe tous ces cas. Nous verrons également ultérieurement que le modèle abstrait que nous allons construire permettra de s’affranchir du fait que $\Omega$ décrit précisément tous les résultats possibles de l’expérience.


### Définition -- Evénement {.definition}
Un *événement* est une propriété qui est vérifiée ou non une fois l'expérience réalisée. On identifie un événement $A$ à un sous-ensemble ou  *partie* de $\Omega$, i.e. $A = \{\omega \in \Omega : A \text{ est vérifiée pour } \omega \}$.

### Exemples {.example}

 1. Jeu de Pile ou Face : $A = \{\text{pile}\}$. 
 2. Lancé de dés :  $A = \{1,3,5\}$.
 3. Durée de vie d'une ampoule électrique : $A = [t_1,t_2] \subset \R^+$.
 4. Température demain à 12h au sommet de la tour Eiffel (en degrés Kelvin) : $A = [T_1,T_2]\cup[T_3,T_4] \subset \R^+$.
 5. Evolution de la vitesse d’une molécule dans un gaz raréfié sur un intervalle de temps $[t_1,t_2] \subset \R^+$ : 
 $A = \{ f \in C([t_1,t_2], \R^3) : \|f-g\|_{\infty} \leq a \}$, où
 $g \in C([t_1,t_2],\R^3)$ et $a \in \R^+$.


Les événements étant des ensembles, les opérations ensemblistes classiques admettent une interprétation probabiliste.

### Correspondance entre opérations logiques et ensemblistes

| Terminologie probabiliste | Terminologie ensembliste | Notation |
|:-:|:-:|:-:|
| événement certain  | ensemble entier  | $\Omega$  |
| événement impossible  |  ensemble vide  | $\varnothing$  |
| événement contraire | complémentaire | $A^c$  |
| événement atomique  |  singleton | $\{\omega\}$  |
| implication | inclusion | $\subset$  |
| et  | intersection  | $\cap$  |
| ou  | réunion | $\cup$ |
| événements incompatibles | ensembles disjoints | $A_1\cap A_2 = \varnothing$  |

On doit maintenant répondre à la question de savoir quels sont les événements dont on va vouloir évaluer la probabilité d'occurence. On va ainsi regrouper les événements en un ensemble $\A$ qui constitue une collection de sous-ensembles de $\Omega$. On va souhaiter en particulier pouvoir combiner des événements au sein de $\A$ par les opérations ensemblistes courantes. 

Ceci conduit à la notion de *tribu de parties* de $\Omega$.

### Définition -- Tribu {.definition #deftribu}
Une *tribu* (ou *$\sigma$-algèbre*) $\A$ est une collection de sous-ensembles de $\Omega$ tels que :

 1. $\Omega \in \A$,
 2. $A \in \A \Rightarrow A^c \in \A$,
 3. $\forall\, n \in \N, A_n \in \A \Rightarrow \bigcup_n A_n \in \A$.

Le couple $(\Omega, \A)$ est appelé *espace probabilisable*.

### Exemples {.example}
 1. $\A = \{\varnothing,\Omega\}$ est la tribu *grossière* ou *triviale* : c'est la plus petite tribu de $\Omega$.
 2. Dans le cas où $\Omega$ est au plus dénombrable, on choisit systématiquement l'ensemble $\mathcal{P}(\Omega)$ des parties de $\Omega$ dont on vérifie aisément qu'il s'agit d'une tribu ; c'est le cadre étudié en CPGE. On verra ultérieurement que cette tribu est trop grande dans le cas où $\Omega$ est infini non dénombrable.
 3. Si $\Omega = \R$, on peut le munir de la tribu formée des ensembles mesurables de $\R$, dite *tribu de Lebesgue*.
 4. On verra par la suite qu'il est aisé de définir une tribu sur tout espace topologique.

## Notion de densité de probabilité

Une des nouveautés majeures de ce cours par rapport au programme de CPGE est le cas où l'espace fondamental n'est plus fini ni dénombrable. On va voir ici que les outils développés dans le cours de calcul intégral vont nous permettre de définir une probabilité sur $\R$ muni de la tribu de ses ensembles mesurables.

<!-- ### Densité de Probabilité {.definition} -->
Soit $\Omega = \R$ et $f : \Omega \to \R^+$ une fonction absolument intégrable telle que 
$$ \int_\Omega f(x)\, dx =1. $$

<!-- voir aussi issue #34 -->
Soit $\A$ la collection des ensembles mesurables sur $\Omega$ ;
[les propriétés élémentaires des ensembles mesurables (cf. "Calcul Intégral II")](Calcul Intégral II.pdf#pptés-tribu) établissent que $\mathcal{A}$ est une tribu, 
sur laquelle on peut définir

$$ \P(A) = \int_\Omega 1_{A}\, f(x)\, dx = \int_A f(x)\, dx. $$

On vérifie aisément que $\P$ vérifie les 3 propriétés suivantes :

 1. $\forall\, A \in \A$, $\P(A) \in [0,1]$.

 2. $\P(\Omega) = \int_\Omega f(x) dx = 1$.

 3. Si $A_n$ désigne une suite (dénombrable) d'événements **disjoints** de $\A$, on a, en appliquant le théorème de convergence dominée à la suite de fonctions $f(x) 1_{\left\{\bigcup_{n=0}^m A_n\right\}}(x) = \sum_{n=0}^m f(x) 1_{A_n}(x)$ ($m \in \N^\ast$), majorée trivialement par $f$ intégrable :
    \begin{align*}
        \P\left(\bigcup_{n=0}^m A_n\right) &= \int_\Omega 1_{\left\{\bigcup_{n=0}^m A_n\right\}}\, f(x)\, dx\\
                          &= \lim_{m \to +\infty} \int_\Omega \sum_{n=0}^m 1_{A_n}\, f(x)\, dx\\
                          &= \lim_{m \to +\infty} \sum_{n=0}^m \int_\Omega 1_{A_n}\, f(x)\, dx\\
                          &= \lim_{m \to +\infty} \sum_{n=0}^m \P(A_n) \\
                          &= \sum_{n=0}^{+\infty} \P(A_n).                        
    \end{align*}


Ces trois propriétés correspondent aux [axiomes de Kolmogorov](#defproba) qui définissent une probabilité sur un espace probabilisable général. La fonction $f$ est appelée *densité de probabilité*. On verra plus loin que l'on ne peut pas caractériser toutes les probabilités sur $\R$ via cette notion. Celle-ci constitue néanmoins un exemple fondamental que l'on approfondira dans la suite du cours, notamment dans le cadre de l'étude des variables aléatoires.

### Remarque {.remark}

On pourra faire l'analogie entre la densité de probabilité et la loi de probabilité sur un univers discret, dans le sens où elle va "pondérer" les valeurs réelles, en remarquant cependant que :

 * $f(x)$ n'est pas nécessairement inférieur à 1,

 * $\P(\{x\}) = \int_{\{x\}} f(x)\, dx = 0$ et plus généralement, $\P(A) = 0$ si $A$ est négligeable.

## Probabilité

### Définition -- Probabilité {.definition #defproba}
Une *probabilité* sur l'espace $(\Omega, \A)$ est une application $\P : \A \rightarrow [0,1]$, telle que :

 1. $\P(\Omega) = 1$,
 2. pour toute suite (dénombrable) $(A_n)_{n\in\N^\star}$ d'éléments de $\A$ **deux à deux disjoints**, on a 
 \begin{equation}
 \P\left(\bigcup_{n\in\N^\star} A_n\right) = \sum_{n\in\N^\star} \P(A_n).
 \end{equation}

Le triplet $(\Omega, \A, \P)$ est appelé *espace probabilisé*. La modélisation probabiliste consiste ainsi à décrire une expérience
aléatoire par la donnée d’un espace probabilisé.

La définition suivante est fondamentale en théorie des probabilités. Elle introduit une
notion de “vrai ou faux” qui dépend de la probabilité choisie sur l’espace fondamental.

### Définition -- Propriété presque-sûre {.definition}
Soit $(\Omega, \A, \P)$ un espace probabilisé.

Une propriété est vraie $\P$-*presque-sûrement* (en abrégé $\P$-p.s.), si l'ensemble des $\omega \in \Omega$ pour lesquels elle est vraie est de probabilité égale à 1.

### Proposition -- Propriétés élémentaires {.proposition #elemprop} 
 1. $\forall\, A \in \A$, $\P(A) \in [0,1]$ et $\P(A^c)= 1-\P(A)$.
 2. $\forall\, A,B \in \A$, $A \subset B \Rightarrow \P(A) \leq \P(B)$.
 3. $\forall\, A,B \in \A$, $\P(A \cup B ) = \P(A) + \P(B) - \P(A \cap B)$.
 4. Inégalité de Boole : $\forall\, n \in \N^\ast$, $\forall\, (A_i)_{1 \leq i \leq n} \in \A, \P\left(\bigcup_{i=1}^n A_i\right) \leq \sum_{i=1}^n \P(A_i)$.
 5. Formule de Poincaré : $\forall\, n \in \N^\ast$, $\forall\, (A_i)_{1 \leq i \leq n} \in \A$
 $$ \P\left(\bigcup_{i=1}^n A_i\right) = \sum_{i=1}^n \P(A_i) - \sum_{1 \leq i < j \leq n} \P(A_i \cap A_j) + \ldots + (-1)^n \P\left(\bigcap_{i=1}^n A_i\right).$$

### Demonstration {.proof}
Exercice

### Théorème de la continuité monotone {.theorem #continuitemonotone}
Dans le cas d'une suite $(A_n)_{n\in\N}$ d'éléments de $\A$ croissante, on a 
$$ \P\left(\bigcup_{n\in\N} A_n\right) = \lim_{n \rightarrow \infty} \P(A_n).$$

### Demonstration {.proof}
Exercice

### Remarque {.remark}
Dans le cas d'une suite décroissante, on a 
$$ \P\left(\bigcap_{n \in \N} A_n\right) = \lim_{n \rightarrow \infty} \P(A_n).$$

**ou version plus complète avec l'équivalence de la $\sigma$-additivité??? - *Dans les compléments***

**Lemme de Borel-Cantelli ??? ou alors à la fin - *Dans les suites de va***

## Probabilité conditionnelle 

La construction d’un modèle probabiliste repose sur l’information connue **a priori** sur l’expérience aléatoire. Ce modèle permet de quantifier les probabilités de réalisation de certains résultats de l’expérience. Il est fondamental de remarquer que si l’information change, les probabilités de réalisation changent. L'outil qui va nous permettre d'introduire cette information est la probabilité conditionnelle dont nous donnons ici la définition.

### Définition -- Probabilité conditionnelle {.definition}
Soient $(\Omega, \A, \P)$ un espace probabilisé, $A, B \in \A$ tels que $\P(B)>0$. La *probabilité conditionnelle* de $A$ sachant $B$ est le nombre 
\begin{equation}
\P(A|B) = \frac{\P(A\cap B)}{\P(B)}.
\end{equation}

Cela définit une probabilité. 

### Proposition {.proposition}
 1. Soient $(\Omega, \A, \P)$ un espace probabilisé et $B \in \A$ tel que $\P(B)>0$. Alors l’application de $\A$ dans $[0, 1]$ qui à $A$ associe $\P(A|B)$ définit une nouvelle probabilité sur $\Omega$, appelée probabilité conditionnelle sachant $B$.
 2. Si $\P(A) > 0$ et $\P(B) > 0$ , nous avons
$$\P(A|B)\, \P(B) = \P(A \cap B) = \P(B|A)\, \P(A).$$

### Démonstration {.proof}
Il est clair que $0 \leq \P(A|B) \leq 1$. Par ailleurs, les deux propriétés de la [définition de la probabilité](#defproba)
pour $\P(\cdot|B)$ proviennent des mêmes propriétés pour $\P$ et des remarques suivantes :
$\Omega \cap B = B$, et $(\bigcup_{n\in\N} A_n ) \cap B = \bigcup_{n\in\N} (A_n \cap B)$. De plus, si $A$ et $C$ sont disjoints, il en est
de même de $A \cap B$ et $C \cap B$. L’assertion 2 est évidente, d'après la définition de la [Probabilité conditionnelle].

### Exemple : approche bayésienne (subjective)


### Formule des probabilités totales {.proposition}

Soit $(B_n)_{n\in\N}$ une partition finie ou dénombrable d’événements de $\Omega$ (i.e. telle que $\bigcup_{n\in\N} B_n = \Omega$ et les $B_n$ sont deux-à-deux disjoints), telle que $\P(B_n ) > 0$ pour tout $n\in\N$. Pour tout $A \in \A$, on a alors
\begin{equation}
P(A) = \sum_{n\in\N} P(A \cap B_n ) = \sum_{n\in\N} P(A|B_n)\, P(B_n).
\end{equation}

### Démonstration {.proof}
Nous avons $A = \bigcup_{n\in\N} (A\cap B_n)$. Par hypothèse, les ensembles $(A\cap B_n)$ sont deux-à-deux disjoints et de plus $\P(A\cap B_n) = \P(A|B_n)\,\P(B_n)$. Le résultat découle du deuxième point de la [définition de la probabilité](#defproba). 

### Formule de Bayes {.proposition}
Selon les mêmes hypothèses que ci-dessus et si $\P(A) > 0$, on a 
\begin{equation}
\forall\, i \in \{1,\dots,n\},\  \P(B_i | A) = \dfrac{\P(A | B_i)\, \P(B_i)}{\sum_{n\in\N} \P(A | B_n)\, \P(A)}.
\end{equation}

### Démonstration {.proof}
Le dénominateur vaut $\P(A)$ d'après la [Formule des probabilités totales]. La définition de la [probabilité conditionnelle] implique :
\begin{equation}
\P(B_i | A) = \dfrac{\P(A \cap B_i)}{\P(A)} = \dfrac{\P(A | B_i) \P(B_i)}{\P(A)}.
\end{equation}

### Exemple d'application **TODO**

## Indépendance des événements 
La notion d’indépendance est absolument fondamentale en probabilités et nous verrons
par la suite toutes ses implications dans la modélisation de l’aléatoire.

Intuitivement, deux événements $A$ et $B$ sont indépendants si le fait de savoir que $A$ est
réalisé ne donne aucune information sur la réalisation de $B$ et réciproquement.

### Définition -- Indépendance de deux événements {.definition}
Deux événements $A$ et $B$ sont *indépendants* si et seulement si 
\begin{equation}
\P(A\cap B) = \P(A)\, \P(B).
\end{equation}

### Remarques {.remark}

 * La probabilité de voir $A$ réalisé ne dépend pas de la réalisation de $B$, et réciproquement.
 * Si $\P(A)>0$ et $\P(B)>0$, alors 
    \begin{equation}
    \P(A\cap B) = \P(A)\, \P(B) \Leftrightarrow \P(A) = \P(A|B) \Leftrightarrow \P(B) = \P(B|A).
    \end{equation}

### Proposition {.proposition}
Si les événements $A$ et $B$ sont indépendants, alors il en est de même des couples $(A^c,B)$, $(A,B^c)$ et $(A^c,B^c)$.

# Probabilité sur $\R$

## Fonction de répartition
Nous avons vu précédemment la définition générale d'une probabilité $\P$ sur un espace quelconque $\Omega$ muni d'une tribu $\A$. Un problème fondamental est de construire et de caractériser ces probabilités. La résolution de ce problème lorsque $\Omega$ est fini ou dénombrable est connu.
Le cas général fait l'objet de la théorie de la mesure et sera développé ultérieurement.

Nous allons ici nous contenter de résoudre, sans démonstrations complètes, le cas où $\Omega = \R$ et où la tribu $\A$ est la tribu formée des ensembles mesurables.

### Définition -- fonction de répartition {.definition #deffdr}
La *fonction de répartition* de la probabilité $\P$ sur $\R$ est la fonction
\begin{equation}
F(x) = \P(\left]-\infty, x\right]),\ x \in \R.
\end{equation}

### Théorème {.theorem}
La fonction de répartition $F$ caractérise la probabilité.

### {.anonymous}
Nous démontrerons ce résultat ultérieurement.

### Théorème {.theorem #theofdr}
Une fonction $F$ est la fonction de répartition d'une unique probabilité $\P$ sur $\R$ muni de la tribu des ensembles mesurables si et seulement si elle vérifie les trois conditions suivantes :

 1. elle est croissante,
 2. elle est continue à droite,
 3. $\lim\limits_{x \to -\infty} F(x) = 0, \lim\limits_{x \to +\infty} F(x) = 1$.

### Démonstration {.proof}

La première assertion est immédiate d'après la [définition](#deffdr). Pour la seconde, on remarque que si $x_n$ décroît vers $x$, alors $]-\infty,x_n]$ décroît vers $]-\infty,x]$ et donc $F(x_n)$ décroît vers $F(x)$ par le théorème de la continuité monotone. La troisième assertion se montre de manière analogue  en remarquant que $]-\infty,x]$ décroît vers $\varnothing$ (resp. croît vers $\R$) lorsque $x$ décroît vers $-\infty$ (resp. croît vers $+\infty$).

La réciproque est plus difficile à obtenir et nécessite des éléments de théorie de la mesure qui nous font pour l'instant défaut. Nous renvoyons donc sa démonstration à plus tard.

### Remarque {.remark}
 Comme $F$ est croissante, elle admet une limite à gauche en chaque point notée $F(x^-)$. En remarquant que $]-\infty,y[\, = \lim\limits_{n \to +\infty}]-\infty,y_n[$ si $y_n$ tend vers $y$ par valeurs décroissantes, on obtient pour $x < y$ : 

  * $\P(]x,y]) = F(y) - F(x)$
  * $\P(]x,y[) = F(y-) - F(x)$
  * $\P([x,y]) = F(y) - F(x^-)$
  * $\P([x,y[) = F(y-) - F(x^-)$

En particulier, $\P(\{x\}) = F(x) - F(x^-)$ est le **saut** de la fonction $F$ au point $x$. On a donc $\P(\{x\}) = 0$ pour tout $x$ si et seulement si $F$ est continue en tout point.

### Remarque {.remark} 
<!-- cf #32 -->
Le théorème ci-dessus explique pourquoi, d’un point de vue strictement mathématique, il est nécessaire d’introduire les tribus en probabilités, malgré la complexité que cela engendre. Plus concrètement, considérons l'exemple suivant : soit $\Omega = [0,1]$ et $\P$ telle que $\P(]a,b]) = b-a$ pour $0\leq a\leq b\leq 1$ (il s'agit de la loi uniforme sur [0,1]). C'est une probabilité naturelle qui assigne à tout intervalle sa longueur comme probabilité. Supposons maintenant que l'on souhaite étendre de manière unique $\P$ au $2^{[0,1]}$ éléments de $\mathcal{P}(\R)$ de manière à ce que $\P(\Omega) =1$ et $\P\left(\cup_{n\in\N^\star} A_n\right) = \sum_{n\in\N^\star} \P(A_n)$ pour toute suite $(A_n)_{n\in\N^\star}$ tels que $\A_n\cap A_m = \varnothing$ pour $n \neq m$. On peut prouver qu'un tel $\P$ n'existe pas. $\mathcal{P}(\R)$ est trop "grand" pour définir un tel $\P$. Il contient en particulier des ensembles non mesurables.

Si l'on voulait travailler avec la tribu $\A = \mathcal{P}(\R)$, il n'existerait que très peu de probabilités sur $\R$, à savoir les probabilités discrètes que l'on décrit rapidement ci-dessous.

### Exemple {.example #ex.discret}

 1. Les masses de Dirac (ou **mesures** de Dirac). 
 
    Soit $a \in \R$, on appelle mesure de Dirac en $a$, la probabilité $\P$ sur $\R$ qui vérifie pour $A \in \B_\R$
    \begin{equation}
        \P(A) = \left\{ \begin{array}{ll}
        1  &\text{si } a \in A, \\
        0 &\text{sinon.}
        \end{array}
        \right.
    \end{equation}
    Sa fonction de répartition est $F(x) = 1_{[a,+\infty[}(x)$.

 2. Les probabilités portées par $\N$.

    Comme $\N$ est une partie de $\R$, toute probabilité sur $\N$ peut être considérée comme une probabilité sur $\R$ qui ne "charge" que $\N$. Plus précisément, si $Q$ est une probabilité sur $\N$, on définit son "extension" $\P$ à $\R$ en posant $\P(A) = Q(A\cap \N)$. Si $q_n = Q(\{n\})$ pour $n \in \N$, la fonction de répartition $F$ de $\P$ est 
    \begin{equation}
    F(x) = \left\{ \begin{array}{ll}
    0  &\text{si } x <0, \\
    \sum_{i=0}^{\lfloor x \rfloor} q_i &\text{sinon,}
    \end{array}
    \right.
    \end{equation}
    où $\lfloor \cdot \rfloor$ désigne la partie entière.

 3. Les probabilités discrètes.

    Plus généralement, si $E$ est une partie finie ou dénombrable de $\R$, toute probabilité $Q$ sur $E$ peut être considérée comme une probabilité $\P$ sur $\R$, via la formule $\P(A) = Q(A\cap E)$. Si pour tout $i \in E$, on pose $q_i = Q(\{i\})$, la fonction de répartition $F$ de $\P$ est alors 
    $$F(x) = \sum_{\substack{i \in E \\ i \leq x}} q_i,$$
    avec la convention qu'une somme "vide" vaut 0. On retrouve bien l'exemple 2 si $E = \N$. On voit que $F$ est **purement discontinue** au sens où elle est complètement caractérisée par ses sauts $\triangle F(x) = F(x) - F(x^-)$ :
    $$F(x) = \sum_{\substack{y \in E \\ y\leq x}} q_i.$$
    Notons aussi que l'ensemble $E$, bien qu'au plus dénombrable, peut tout à fait être partout dense dans $\R$, par exemple $E = \Q$ : si alors $q_i >0$ pour tout $i \in \Q$, la fonction $F$ est discontinue en tout rationnel.

<!-- Nota SB: concept d'ensemble dense pas vu en Topo à ce stade, peut-être en 
Calcul Diff 3, tard (et sans doute pas en CPGE) -->    

Il existe bien d’autres probabilités, non discrètes, sur $\R$. Le paragraphe suivant est consacré à un exemple très important, celui des probabilités avec densité.

## Densités de probabilités

### Définition -- densité de probabilité {.definition}
Une fonction réelle $f$ sur $\R$ est une *densité de probabilité* (ou plus simplement *densité*) si elle est positive, intégrable et vérifie 
$$\int_\R f(x)\, dx = 1.$$ 

Si $f$ est une densité, la fonction 
   $$F(x) =\int_{-\infty}^x f(y)\, dy$$ 
est la fonction de répartition d'une probabilité $\P$ sur $\R$. On dit que $f$ est la densité de $\P$ ou que $\P$ admet la densité $f$.
Dans ce cas, $F$ est continue, de sorte que $\P(\{x\}) = 0$ pour tout $x$, et elle est même dérivable et de dérivée $f$ en tout point ou $f$ est continue. A l'inverse, si la fonction de répartition d'une probabilité $\P$ est dérivable, ou seulement continue partout et dérivable par morceaux, alors $\P$ admet une densité.

Il existe bien sûr des fonctions de répartitions qui n'ont pas de densité : c'est le cas des probabilités discrètes données en exemple [ci-dessus]{#ex.discret}. Il existe des cas "mixtes" : soient d'une part $f$ une fonction positive intégrable et d'autre part une partie finie ou dénombrable $E$ de $\R$ et des poids $p_i>0$ indexés par $i \in E$, tels que :
    $$ \int_\R f(x)\, dx + \sum_{i\in E} p_i = 1.$$
Alors la fonction 
    $$ F(x) = \int_{-\infty}^x f(x)\, dx + \sum_{\substack{i\in E \\ i \leq x}} p_i$$
est une fonction de répartition, et la probabilité associée $\P$ n'admet pas de densité et n'est pas non plus discrète.

### Remarques {.remark}

<!-- le "f(x) +1" me perturbe un peu ... comme si ce choix particulier avait un
     rôle spécial ; bien sûr ça n'est pas le cas ! Est-ce qu'on peut éviter ce
     "red herring" ? 
  -->

 1. La fonction de répartition est entièrement déterminée par la probabilité $\P$. Il n'en est pas de même de la densité lorsqu'elle existe : si en effet on a $F(x) =\int_{-\infty}^x f(y)\, dy$ et si on pose $g(x) = f(x)$ si $x \notin E$ et $g(x) =f(x)+1$ (par exemple) si $x\in E$, où $E$ est un ensemble négligeable, alors $g$ est encore une densité de $\P$.

 2. Une interprétation intuitive de la densité $f$ de $\P$ : si $dx$ est un petit accroissement de la variable $x$, on a (si du moins $f$ est continue en $x$) :
 $$ f(x) \sim \frac{\P([x,x+dx])}{dx}.$$   


### Exemples de lois à densités {.example}

 1. La *loi uniforme* sur $[a,b]$, avec $a,b \in \R$ tels que $ a < b $, notée $\mathcal{U}_{[a,b]}$, est la probabilité $\P$ qui admet la densité
    $$f(x) = \left\{\begin{array}{ll}
            \frac{1}{b-a} & \text{si } a \leq x \leq b,\\
            0 & \text{sinon}.
            \end{array}\right.$$
    En vertu de la remarque 1. ci-dessus, on aurait pu choisir $f(a) = f(b) = 0$. Au vu de l'interprétation 2. ci-dessus, le fait que $f$ soit constante sur $[a, b]$ exprime que si on choisit un point selon la probabilité uniforme, nous avons “autant de chances” de tomber au voisinage de chaque point de l’intervalle $[a, b]$. Cela explique le nom “uniforme”. On remarque aussi que $\P(\{x\}) = 0$ pour tout $x$ (comme pour toutes les probabilités à densité). Nous avons donc une probabilité nulle de tomber exactement en un point $x$ fixé à l’avance.
    On vérifie aisément que sa fonction de répartition est
    $$F(x) = \left\{\begin{array}{ll}
            0 & \text{si } x < a,\\
            \frac{x-a}{b-a} & \text{si } a \leq x \leq b,\\
            1 & \text{si } x > b.
            \end{array}\right.$$

 2. La *loi exponentielle* de paramètre $\theta$, notée $\mathcal{E}_\theta$, est la loi de densité
    $$f(x) = \left\{\begin{array}{ll}
            0 & \text{si } x < 0,\\
            \theta e^{-\theta x} & \text{sinon}.
            \end{array}\right.$$
    et de fonction de répartition 
    $$F(x) = \left\{\begin{array}{ll}
            0 & \text{si } x < 0,\\
            1 - e^{-\theta x} & \text{sinon}.
            \end{array}\right.$$
    Dans la pratique, on utilise fréquemment la loi exponentielle pour modéliser une durée de vie ou le temps d’attente avant l’arrivée d’un événement spécifique. Par exemple la durée de vie d’une bactérie, d'un composant électronique, la durée d’une conversation téléphonique ou le temps qui nous sépare du prochain tremblement de terre peuvent être considérées comme des variables aléatoires de loi exponentielle.
    
 3. La *loi normale* (ou de *Gauss* ou encore *gaussienne*) de paramètres $\mu$ et $\sigma^2$, notée $\mathcal{N}(\mu,\sigma^2)$, est la loi de densité
    $$f(x) = \frac{1}{\sqrt{2\pi}\sigma}\exp(-\frac{(x-\mu)^2}{2\sigma^2})$$
    Lorsque $\mu = 0$ et $\sigma^2$, on l'appelle la loi normale *centrée réduite* pour des raisons que nous expliciterons au prochain chapitre.

    La distribution normale fut introduite par De Moivre en 1733. Celui-ci l’utilisa pour approximer une variable aléatoire binomiale quand le paramètre $n$ de celle-ci était grand. Ce résultat fut ensuite progressivement généralisé par Laplace et d’autres confrères pour devenir le théorème connu sous le nom de théorème de la limite centrale, qui sera démontré au Chapitre 4. Ce théorème est l’un des plus importants de la théorie des probabilités et prouve que de très nombreux phénomènes aléatoires suivent approximativement une loi normale. Nous pouvons citer à titre d’exemple la taille d’un individu choisi au hasard, les composantes de la vitesse d’une molécule de gaz ou l’erreur de mesure d’une quantité physique.   

Nous aurons l'occasion de voir par la suite un grand nombre d'autres exemples de probabilités avec densité.

# Exercices


