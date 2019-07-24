% Probabilités III

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

# Densités marginales et conditionnelles

Nous étudié précédemment l'indépendance des variables aléatoires. Nous allons nous intéresser ici à caractériser la dépendance entre variables aléatoires et en particulier le conditionnement.

On se limite pour simplifier à énoncer les résultats pour un couple $Z=(X,Y)$ de variables aléatoires. Ils se généralisent aisément à une dimension supérieure.

### Proposition {.proposition}
Supposons que $Z$ admette une densité $f$. Alors $X$ et $Y$ admettent les densités $f_x$ et $f_Y$ données par
$$f_X(x) = \int_\R f(x,y) dy, f_Y(y) = \int_\R f(x,y) dx.$$
Les fonctions $f_X$ et $f_Y$ s'appellent les *densités marginales* de $f$.

### Démonstration {.prooof}
Pour tout $x \in \R$, on a par définition
$$ \P(X \leq x) = \P(Z \in ]-\infty,x] \times \R) = \int_{-\infty}^x du \left(\int_\R f(u,v) dv\right).$$
Donc si $f_X$ est définie par $f_X(x) = \int_\R f(x,y) dy$, nous obtenons que $\P(X \leq x) = \int_{-\infty}^x f_X(u) du$, ce qui montre que $f_X$ est la densité de $X$. Le raisonnement est analogue pour $Y$.

### Remarque {.remark}
La réciproque de cette proposition est fausse en revanche : les variables aléatoires $X$ et $Y$ peuvent avoir des densités sans que le couple $Z = (X, Y )$ en ait une.

Supposons par exemple que $X = Y$. Si $\Delta = \{(x,x) ; x\in \R\}$ est la diagonale de $\R^2$, nous avons évidemment $\P_Z(\Delta) = 1$ mais si la [proposition](Probabilité II.pdf #esperancegvect) était valide pour $\P_Z$, on aurait $\P_Z(\Delta) = \Esp(1_\Delta) = \int_{\R^2} 1_\Delta f_Z(z)dz = 0$ car $\Delta$ est de volume nul dans $\R^2$.

En particulier, il faut faire attention au fait que dans le cas général, la densité d'un couple de variables aléatoires n'est pas le produit des densités.

### Exemple
On lance une fléchette sur une cible circulaire de rayon unité. Le joueur est suffisamment maladroit pour que le point $M$ d’impact de la fléchette
soit supposé uniformément distribué sur la cible (On décide de n’observer que les lancés qui atteignent la cible).

Les coordonnées cartésiennes de $M \in D = \{(x,y) \in \R^2 , x^2+y^2 \leq 1\}$ constituent un couple de variables aléatoires de densité
$$f_{(X,Y)}(x,y) = \frac{1}{\pi}1_{D} (x,y)$$
uniforme sur le disque, par hypothèse. L'abscisse de $X$ est distribuée selon la densité marginale
$$f_X(x) = \int f_{(X,Y)}(x,y) dy = \frac{2}{\pi} (1-x^2) 1_{[-1,1]}(x).$$
La loi de $Y$ a la même densité.

On peut maintenant s'intéresser à caractériser la densité de la variable $Y$ connaissant la valeur prise par la variable $X$, c'est la *densité conditionnelle* de $Y$ sachant $\{X = x\}$ :

### Proposition {.proposition #defdenscond}
La formule suivante définit une densité sur $\R$, pour tout $x$ tel que $f_X(x) > 0$ :
$$ f_{Y|X=x}(y) = \frac{f(x,y)}{f_X(x)}.$$
Cette fonction s'appelle la *densité conditionnelle de $Y$ sachant $\{X = x\}$*.

La preuve est immédiate puisque $f_{Y|X=x}$ est une fonction positive d'intégrale 1.

L’interprétation de cette définition est la suivante : la fonction $f(Y|X=x)$ est la densité de la “loi conditionnelle de Y sachant que X = x”. Bien sûr, nous avons $\P(X = x) = 0$ puisque $X$ admet une densité, donc la phrase ci-dessus n’a pas réellement de sens, mais elle se justifie heuristiquement ainsi : $dx$ et $dy$ étant de “petits” accroissements des variables $x$ et $y$ et lorsque $f$ est continue :
\begin{align*}
f_X(x) dx & \approx \P(X \in [x, x+dx])\\
f_(x,y) dx dy & \approx \P(X \in [x, x+dx], Y \in [y, y+dy])\\
\end{align*}
Par suite 
\begin{align*}
f_{Y|X=x} (y) dy & \approx \frac{\P(X \in [x, x+dx], Y \in [y, y+dy])}{\P(X \in [x, x+dx])}\\
                 & \approx \P(Y \in [y, y+dy]|X \in [x, x+dx])\\
\end{align*}

En intervertissant les rôles de $X$ et $Y$ dans la [proposition ci-dessus](#defdenscond), on a pour tout $x$ tel que $f_X(x) > 0$ et tout $y$ tel que $f_Y(y)) > 0$ :
$$ f_{X|Y=y}(x) = \frac{f(x,y)}{f_Y(y)} = \frac{f_{Y|X=x}(y)f_X(x)}{f_Y(y)} .$$
Ceci nous donne un équivalent de la formule de Bayes pour les densités.

La proposition suivante nous donne une nouvelle caractérisation de l'indépendance de deux variables aléatoire à densité :

### Proposition {.proposition}

Les variables aléatoires $X$ et $Y$ sont indépendantes si et seulement si la densité conditionnelle de $Y$ sachant $\{X = x\}$ ne dépend pas de $x$.

### Démonstration {.proof}

Si $X$ et $Y$ sont indépendantes, $f_{(X,Y)} (x,y) = f_X(x) f_Y(y)$, d'où $f_{Y|X=x}(y) = f_Y(y)$.

Inversement, si $f_{Y|X=x}(y) = f_Y(y)$ alors $f_{(X,Y)}(x,y) = f_{Y|X=x}(y) f_X(x) = f_Y(y)f_X(x)$ et $X$ et $Y$ sont indépendantes.

### {.anonymous}

Puisque $f_{Y|X=x}$ est une densité, on peut définir l'espérance qui lui est associée et introduire la notion d'espérance conditionnelle dans le cas où $Y$ est intégrable.

### Définition {.definition}
Soit $Y$ une variable aléatoire intégrable.

 1. L'*espérance conditionnelle de $Y$ sachant $\{X=x\}* est définie par 
    $$\Esp(Y|X=x) = \int_\R y f_{Y|X=x} (y) dy.$$
 2. L'*espérance conditionnelle de $Y$ sachant $X$* est la **variable aléatoire** définie par :
    $$\Esp(Y|X) = \psi(X), \text{ avec } \psi(x) = \Esp(Y|X=x).$$

On peut étendre cette définition à toute variable de la forme $h(X,Y)$.

### Définition {.definition}
Soit $Y$ une variable aléatoire et $h$ une fonction continue par morceaux positive ou bornée sur $\R^2$.

 1. L'*espérance conditionnelle de $Y$ sachant $\{X=x\}* est définie par 
    $$\Esp(Y|X=x) = \int_\R y f_{Y|X=x} (y) dy.$$
 2. L'*espérance conditionnelle de $Y$ sachant $X$* est la **variable aléatoire** définie par :
    $$\Esp(Y|X) = \psi(X), \text{ avec } \psi(x) = \Esp(Y|X=x).$$


# Vecteurs Gaussiens