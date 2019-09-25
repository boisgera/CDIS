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

La proposition suivante nous donne une nouvelle caractérisation de l'indépendance de deux variables aléatoire à densité :

### Proposition {.proposition}

Les variables aléatoires $X$ et $Y$ sont indépendantes si et seulement si la densité conditionnelle de $Y$ sachant $\{X = x\}$ ne dépend pas de $x$.

### Démonstration {.proof}

Si $X$ et $Y$ sont indépendantes, $f_{(X,Y)} (x,y) = f_X(x) f_Y(y)$, d'où $f_{Y|X=x}(y) = f_Y(y)$.

Inversement, si $f_{Y|X=x}(y) = f_Y(y)$ alors $f_{(X,Y)}(x,y) = f_{Y|X=x}(y) f_X(x) = f_Y(y)f_X(x)$ et $X$ et $Y$ sont indépendantes.

### {.anonymous}

Puisque $f_{Y|X=x}$ est une densité, on peut définir l'espérance qui lui est associée et introduire la notion d'espérance conditionnelle dans le cas où $Y$ est intégrable.

### Définition {.definition #defespcond}
Soit $Y$ une variable aléatoire intégrable.

 1. L'*espérance conditionnelle de $Y$ sachant $\{X=x\}* est définie par 
    $$\Esp(Y|X=x) = \int_\R y f_{Y|X=x} (y) dy.$$
 2. L'*espérance conditionnelle de $Y$ sachant $X$* est la **variable aléatoire** définie par :
    $$\Esp(Y|X) = \psi(X), \text{ avec } \psi(x) = \Esp(Y|X=x).$$

On peut étendre cette définition à toute variable de la forme $h(X,Y)$.

### Définition {.definition #defespcondh}
Soit $Y$ une variable aléatoire et $h$ une fonction continue par morceaux positive ou bornée sur $\R^2$.

 1. L'*espérance conditionnelle de $h(X,Y)$ sachant $\{X=x\}* est définie par 
    $$\Esp(h(X,Y)|X=x) = \int_\R y f_{h(x,y)|X=x} (y) dy.$$
 2. L'*espérance conditionnelle de $h(X,Y)$ sachant $X$* est la **variable aléatoire** définie par :
    $$\Esp(h(X,Y)|X) = \psi(X), \text{ avec } \psi(h(X,Y)) = \Esp(Y|X=x).$$

### Remarques {.remark}

 1. $\psi(x)$ n'est définie que pour $x \notin B = \{u, f_X(u)=0\}$, mais $\P(X\in B) = \int_B f_X(u)du =0.$ Par conséquent, la [définition](#defespcond) définit bien l'espérance conditionnelle $\psi(X) = \Esp(Y|X)$ avec probabilité 1.
 2. $\Esp(\Esp(|Y||X)) = \int_\R \left( \int_R |y|  \frac{f(x,y)}{f_X(x)} dy \right) f_X(x) dx = \Esp(|Y|)$ où nous avons utilisé le [théorème de Fubini](). L'espérance conditionnelle de $Y$ sachant $X$ est bien définie dès que $Y$ est intégrable. 
 3. Les rôles de $X$ et $Y$ peuvent évidemment être inversés dans tous les résultats. On a en particulier pour tout $x$ tel que $f_X(x) > 0$ et tout $y$ tel que $f_Y(y)) > 0$ :
    $$ f_{X|Y=y}(x) = \frac{f(x,y)}{f_Y(y)} = \frac{f_{Y|X=x}(y)f_X(x)}{f_Y(y)} .$$
 Ceci nous donne un équivalent de la *formule de Bayes pour les densités*.

### Théorème {.theorem} 
Si $Y$ est intégrable, alors $\psi(X) = \Esp(Y | X)$ est intégrable, et 
$$\Esp( \psi(X)) = E( Y ) .$$

### Démonstration {.proof} 
On a

\begin{align*}
\Esp(\psi(X)) & = \int_\R \psi(x)f_X(x) dx \\
& = \int_\R \left( \int_R y f_{Y|X=x} dy \right) f_X(x) dx \\
& = \int_\R \left( \int_R |y|  \frac{f(x,y)}{f_X(x)} dy \right) f_X(x) dx  \\
& = \Esp(Y).\\
\end{align*}

où avons utilisé ici le théorème de Fubini dont l'application est justifiée par la remarque ci-dessus.

### {.anonyomous}
Ce résultat permet de calculer $\Esp( Y )$ en conditionnant par une variable auxiliaire $X$ :
$$ \Esp( Y ) = \int_\R \Esp(Y | X = x) f_X(x) dx$$

Il généralise la [formule des probabilités totales](), qui correspond ici à $Y = 1_A$ , et $B_x = \{X = x\}$ où les $B_x$ forment cette fois une partition non dénombrable de $\R$. On l’écrit souvent sous forme
$$ \Esp \left( \Esp(Y | X) \right) = \Esp( Y )$$

L’espérance conditionnelle étant définie comme l’espérance de la loi conditionnelle,
elle hérite des propriétés usuelles de l’espérance :
 
 1. si $Y$ et $Z$ sont intégrables, $\Esp (aY + bZ | X) = a \Esp (Y | X) + b \Esp(Z | X)$,
 2. $\Esp (Y | X) \geq 0$ si $Y \geq 0$,
 3. $\Esp (1 | X) = 1$.
De plus, si $g$ est continue par morceaux positive ou bornée,
$$ \Esp (Y g(X) | X) = g(X) \Esp (Y | X) $$

est une généralisation de l’égalité 1. ci-dessus, au cas où $a = g(X)$, qui doit être
considéré “comme une constante” dans le calcul de l’espérance conditionnelle sachant
$X$ ($X$ est fixée comme une donnée connue a priori).

### Exemple {.example} 
Soient $X$ et $Y$ de densité jointe $f_{X,Y}(x,y)= \frac{1}{x}1_T (x,y)$ où $T$ est le triangle $T = \{0< y< x < 1\}$

La densité marginale de $X$ est donnée par $f_X(x) = \int f_{X,Y}(x,y) dy = 1_{]0,1[}(x)$ et pour $x \in ]0,1[$,
$$ f_{Y|X=x} (y) = \frac{1}{x} 1_{]0,x[}(y) $$
Ainsi $X$ est uniformément distribué sur $]0,1[$, et la loi de $Y$ sachant $X =x$ est uniforme sur $]0,x[$ pour $(0 < x < 1)$. Pour un tel $x$, l'espérance conditionnelle $\Esp(Y|X=x)$ vaut ainsi $x/2$ et nous obtenons $\Esp(X|Y) = \frac{X}{2}$.

### note bofbof cet exemple...

# Vecteurs Gaussiens
Dans cette partie, on s'intéresse à l'exemple canonique des vecteurs gaussiens. Les vecteurs gaussiens (et leur extension que sont les fonctions aléatoires gaussiennes, qui, une fois discrétisées, se ramènent à des vecteurs) se rencontrent dans un grand nombre d'applications. L'ubiquité de la loi gaussienne se justifie également du fait du théorème central limite que nous verrons au prochain chapitre.




# Régression 
La régression est un ensemble de méthodes d'apprentissage statistique très utilisées pour analyser la relation d'une variable par rapport à une ou plusieurs autres. Ces méthodes visent notamment à décrire les liens de dépendance entre variable mais aussi de prédire au mieux la valeur d’une quantité non observée en fonction d'une ou plusieurs autres variables. On va en décrire ici le principe du point de vue probabiliste dans le cas particulier des variables de carré intégrable. On verra dans ce cadre, que l'on rencontre très fréquemment en pratique, une interprétation géométrique très éclairante de l'espérance conditionnelle.

## Régression linéaire
On considère deux variables aléatoires de carré intégrable dont on suppose connues les variances et la covariance. Nous souhaitons trouver la meilleure approximation de $Y$ par une fonction affine de $X$ de la forme $aX + b$, au sens des moindres carrés, c’est à dire qui minimise la quantité $\Esp((Y - (aX + b))^2)$. Il s’agit de déterminer les constantes $a$ et $b$ telles que $\Esp((Y - (aX + b))^2)$ soit minimale. Or, par linéarité,
$$\Esp((Y - (aX + b))^2) = \Esp(Y^2) -2a\Esp(XY) +a^2\Esp(X^2) +2ab\Esp(X) +b^2$$
L'annulation des dérivées partielles par rapport à $a$ et $b$ entraîne que les solutions sont

\begin{align*}
a & = \frac{\cov(X,Y)}{\V(X)} = \rho(X,Y)\frac{\sigma_Y}{\sigma_X} \\
b & = \E(Y)  - a \Esp(X)
\end{align*}

On vérifie aisément que ces valeurs donnent bien un minimum pour $\Esp((Y - (aX + b))^2)$, et déterminent ainsi la meilleure approximation linéaire de $Y$ basée sur $X$ au sens de la distance quadratique moyenne.

Cette approximation linéaire vaut
$$ \Esp(Y) + \rho(X,Y)\frac{\sigma_Y}{\sigma_X} (X -\Esp(X))$$
et l'erreur quadratique moyenne vaut alors
\begin{align*}
\Esp\left(\left(Y - \Esp(Y) - \rho(X,Y)\frac{\sigma_Y}{\sigma_X} (X -\Esp(X))\right)^2\right) & = \sigma_Y^2 + \rho^2(X,Y)\sigma^2_Y - 2\rho^2(X,Y)\sigma^2_Y\\
                        & = \sigma^2_Y(1-\rho^2(X,Y)).
\end{align*}

On voit ainsi que cette erreur est proche de 0 lorsque $|\rho(X,Y)| \approx 1$ tandis qu'elle est proche de $\V(Y) = \sigma^2_Y$ lorsque $\rho(X,Y) \approx 0$. 

Dans ce paragraphe, on s'est intéressé à caractériser la relation linéaire entre deux variables aléatoires de carré intégrable. On va montrer dans ce paragraphe que la meilleure approximation, au sens des l'erreur quadratique moyenne, de $Y$ par une fonction de $X$ est précisément donnée par $\Esp(Y|X)$. 

## Espace de Hilbert des variables aléatoires de carré intégrable
