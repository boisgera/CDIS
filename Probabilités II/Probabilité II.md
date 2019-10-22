% Probabilités II

\newcommand{\R}{\mathbb{R}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\Z}{\mathbb{Z}}
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

# Variables aléatoires réelles

En théorie moderne des probabilités, on préfère prendre un point de vue fonctionnel plutôt qu’ensembliste, et utiliser les variables aléatoires plutôt que les événements. Une variable aléatoire est une grandeur qui dépend du résultat de l’expérience. Par exemple,

 * le nombre de 6 obtenus dans un lancer de 3 dés,
 * le nombre d’appels dans un central téléphonique pendant une heure,
 * la distance du point d’atteinte d’une flèche au centre de la cible,
 * la valeur maximale d’un prix d’actif sur un intervalle de temps donné,
 
sont des variables aléatoires.

La définition formelle d'une variable aléatoire fait intervenir des éléments de la théorie de la mesure qui nous font pour l'instant défaut. On s'interessera dans un premier temps au cas d'une variable réelle dont on donne une définition partielle : 

Soit $\Omega$ l'espace fondamental muni de sa tribu $\A$. Une *variable aléatoire* $X$ est une application de $(\Omega,\A)$ dans un ensemble $E$,
\begin{equation*}
\omega \in \Omega \mapsto X(\omega) \in E
\end{equation*}

En pratique, l’ensemble $E$ pourra être un ensemble fini ou dénombrable ou $\R$ ou $\R^d$ ou encore un espace plus sophistiqué tel que l’ensemble $C(\R_+ , \R^d)$ des fonctions continues de $\R_+$ dans $\R^d$.

### Remarque {.remark}
La terminologie, consacrée par l'usage, peut être trompeuse. Une variable aléatoire n'est pas une variable (au sens de l'analyse) mais une fonction. Cette terminologie est apparentée à la notion de variable en physique ou en sciences humaines où on désigne volontiers par "variable" la valeur prise par une fonction de l'état du système étudié.

L'intérêt principal de travailler avec des variables aléatoires est de pouvoir substituer à l'espace abstrait $\Omega$ des résultats de l'expérience l'espace $E$, mieux connu dans la pratique. Ainsi, grâce à une variable aléatoire $X$, nous pouvons transporter la structure abstraite du modèle probabiliste $(\Omega, \A, \P)$ sur l'espace d'arrivée $E$, en posant pour $B \subset E$
$$\P_X (B) = \P(X^{-1}(B)) = \P(\{\omega, X(\omega)\in B\})$$

Cette formule définit une nouvelle probabilité, notée $\P_X$ et définie sur $E$, qui s'appelle la *loi de la variable* $X$.

### Notation {.remark}
Il est usuel de noter l'ensemble $X^{-1}(B) = \{\omega \in \Omega, X(\omega) \in B\}$ par $\{X \in B\}$, ce qui allège les écritures. On se rappelera néanmoins que cette notation désigne un sous-ensemble de $\Omega$.

Comme $\P(A)$ n'est définie que pour les $A$ de la tribu $\A$, la formule ci-dessus ne permet de définir $\P_X(B)$ que pour les ensembles $B$ tels que $X^{-1}(B) \in \A$, d’où l’importance de la proposition suivante :

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

$\P_X$ sera plus facile à caractériser que $\P$ puisque $E$ est un ensemble connu (on pourra en particulier utiliser ses propriétés topologiques) alors que $\Omega$ est un espace abstrait. Les variables que nous rencontrerons dans ce cours seront soit à valeurs dans un ensemble dénombrable, soit à valeurs dans $\R$ ou dans $\R^d$. Nous les appellerons respectivement des variables aléatoires discrètes, réelles ou des vecteurs aléatoires. Leurs lois seront alors des probabilités respectivement sur un ensemble dénombrable, sur $\R$ ou sur $\R^d$. Le cas discret est considéré connu. 

La [proposition ci-dessus](#propva.tribu) implique que l'ensemble $X^{-1}(B)$ soit un évènement, pour tout $B$ dans $\E$. Dans le cas où $E = \R$, on notera $\E_\R$ la tribu associée[^NB]. Cela nous conduit à poser :


### Définition -- variable aléatoire réelle {.definition #defvar}
Soit l'espace d'état $\Omega$ muni de la tribu $\A$ des évènements. Une application $X$ de $\Omega$ dans $\R$ est une *variable aléatoire réelle* si $X^{-1}(B) \in \A$ pour tout $B \in \E_{\R}$.

### Définition -- loi d'une variable aléatoire réelle {.definition #defloivar}
La probabilité $\P_X$, définie sur $(\R,\E_{\R})$ par $\P_X (B) = \P(X^{-1}(B))$ pour $B \in \E_{\R}$ est appelée *loi de la variable $X$*, ou *distribution* de $X$.

[^NB]: Nous n'avons pas les outils permettant de caractériser cette tribu pour le moment. On verra par la suite que, dans le cas des variables aléatoires réelles à densité, elle est très similaire à la tribu des ensembles mesurables de $\R$, à une collection d'ensembles négligeables près.


On a alors le résultat très utile suivant :

### Proposition {.proposition #composition}
Si $X_1, \ldots, X_n$ sont des variables aléatoires réelles et si $g$ est une fonction mesurable de $\R^n$ dans $\R$, alors $Y = g(X_1,\ldots,X_n)$ est une variable aléatoire réelle.

### Démonstration (idée) {#proof}
Puisque $g$ est mesurable, le critère de l'image réciproque implique que $\forall A \in \E_{\R}$, $g^{-1}(A) \in \E_{\R^n}$. Par composition, on en déduit que $Y = g(X_1,\ldots,X_n)$ est une variable aléatoire.

Comme application de ce résultat, on a les propriétés suivantes :

### Proposition {.proposition}

Soient $X$, $Y$ et $(X_n)_{n \in \N^\star}$ des variables aléatoires réelles. On a 

 1. $X + Y$, $XY$, $\frac{X}{Y}$ si $Y \neq O$, sont des variables aléatoires.
 
 2. $\sup_{1\leq p \leq n} X_p$, $\inf_{1\leq p \leq n} X_p$, sont des variables aléatoires.

 3. $\sup_{n\geq 1} X_n$, $\inf_{n\geq 1} X_n$, sont des variables aléatoires.
        
 4. Si $X_n(\omega) \xrightarrow[n \to \infty]{} Z(\omega)$, $\forall \omega$, alors la limite $Z$ est une variable aléatoire.

 5. $Z = 1_A$ est une variable aléatoire $\Leftrightarrow$ $A \in \A$.

### Définition -- variable aléatoire réelle à densité {.definition #va.densité}
Soit $X$ une variable aléatoire. On dit que $X$ a une *loi de densité $f$* (ou par abus de language "est de densité $f$"), si $\P_X$ admet la densité $f$ et donc si pour tout réel $x$, 
$$ \P(X\leq x) = \int_{-\infty}^x f(y) dy.$$

### Exemple {.example #ex.expo}

La durée de fonctionnement, en heures, d'un ordinateur avant sa première panne est une variable aléatoire positive de loi exponentielle de paramètre 1/100, de densité donnée par 

$$f(x) = \left\{ \begin{array}{ll}
        \frac{1}{100}\exp\left(-\frac{x}{100}\right) & x \geq 0, \\
        0 & x < 0.
        \end{array}
        \right.$$

Calculons la probabilité que cette durée de fonctionnement $X$ soit comprise entre 50 et 150 heures, elle vaut 
$$ \P(X \in [50,150]) = \int_{50}^{150} \frac{1}{100}\exp\left(-\frac{x}{100}\right) dx = \exp(-1/2)-\exp(-3/2) \approx 0,38.$$
Calculons la probabilité que l'ordinateur fonctionne moins de 100 heures :
$$ \P(X \leq 100) = \int_{0}^{100} \frac{1}{100}\exp\left(-\frac{x}{100}\right) dx = 1-e^{-1} \approx 0,63.$$


# Moments d'une variable aléatoire à densité
 
La densité de probabilité d'une variable aléatoire va nous permettre de calculer aisément des grandeurs caractéristiques telles que sa valeur moyenne et sa variance définies ci-dessous :

### Définition {.definition #defesp}
La variable aléatoire $X : \Omega \to \R$ de densité $f$ est dite  *intégrable* si l'intégrale $\int_\R |x|f(x) dx$ est définie, autrement dit si le produit $x f(x)$ est absolument intégrable[^noteesp]. On définit alors son *espérance* par 
        $$\Esp(X) = \int_\R x f(x)dx$$

[^noteesp]: Comme $f$ est positive, on peut en fait se convaincre que $xf(x)$ intégrable équivaut à $xf(x)$ absolument intégrable : si $x f(x)$ est intégrable, ses "restrictions" $g(x) = xf(x) 1_{\R_-}(x)$ et $h(x)=x f(x) 1_{\R_+}(x)$ sont intégrables (passer par la restriction aux intervalles $\R_-$ et $\R_+$ puis par le critère qui étend par 0 à $\R$ ; les deux opérations préservent l'intégrabilité). Or $|x|f(x) = h(x) - g(x)$ (sauf en 0), donc elle est intégrable.
<!-- **note : pour introduire proprement l'espérance d'une variable aléatoire réelle, on a besoin de l'intégrale de Lebesgue -> CI 5** -->

### Remarque {.remark} 
$\Esp(X)$ est un nombre réel qui donne une valeur moyenne résumant la variable aléatoire $X$.

L’espérance mathématique d’une variable aléatoire est un concept fondamental de la théorie des probabilités. La dénomination d’espérance pour cette quantité fait référence aux problèmes de jeux et d’espérance de gain. Cette terminologie imagée a été introduite par Pascal.

On note $\L^1$ l'ensemble de toutes les variables réelles $X$ à densité intégrables. Les propriétés suivantes découlent directement des propriétés de l'intégrale.

### Proposition {.proposition #propl1}
 * $\L^1$ est un espace vectoriel et $\forall X,Y \in \L^1$, $\forall a,b \in \R$ 
        $$\Esp(aX + bY) = a\Esp(X) + b\Esp(Y).$$
 * $X \in \L^1 \Leftrightarrow |X| \in \L^1$, et dans ce cas $$|\Esp(X)| \leq \Esp(|X|).$$
 * Si $X \geq 0$ et $X \in \L^1$, alors $\Esp(X) \geq 0.$
 * Si $X,Y \in \L^1$ sont telles que $X \leq Y$, alors
        $$ \Esp(X) \leq \Esp(Y).$$
 * L'espérance d'une variable presque-sûrement constante est égale à cette constante :
 $$ \text{Si } \P(X(\omega) = a ) = 1, \text{ alors } \Esp(X) = a.$$
 * Si $\exists b \in \R_+$ tel que $|X| \leq b$, alors $X \in \L^1$ et $\Esp(X) \leq b$.

### Rappel : cas discret {.remark}
Dans le cas d'une variable aléatoire discrète $Y$ à valeurs dans $\N^\ast$, son espérance est définie par la quantité $\Esp(Y) = \sum_{i\in\N^\ast} i\P(Y=i)$, pourvu que celle-ci soit finie. On voit immédiatement que les propriétés ci-dessus sont également vérifiées.

Outre l'espace $\L^1$, nous pouvons définir l'espace $\L^2$ des variables aléatoires réelles dont le carré $X^2$ est dans $\L^1$.

### Définition {.definition #defvar}
La variable aléatoire $X : \Omega \to \R$ de densité $f$ est dite *de carré intégrable* si $\Esp(X^2) = \int_\R x^2 f(x)dx$ est définie, autrement dit si le produit $x^2 f(x)$ est intégrable. Sa *variance* est définie par
        $$\V(X) = \Esp((X-\Esp(X))^2)$$


### Proposition {.proposition #propl2}
$\L^2$ est un sous-espace vectoriel de $\L^1$, et si $X \in \L^2$,
$$|\Esp(X)| \leq \Esp(|X|) \leq \sqrt{\Esp(X^2)}$$


### Démonstration {.proof}
Soient $X$ et $Y$ deux variables aléatoires réelles de $\L^2$ et $a \in \R$. Comme $(aX+ Y)^2 \leq 2 a^2 X^2 + 2 Y^2$, alors $aX + Y \in \L^2$. Ainsi, $\L^2$ est un espace vectoriel.

L'inclusion $\L^2 \subset \L^1$ découle de $|X| \leq 1 + X^2$ et de la [proposition précédente](#propl1) (linéarité).

La première inégalité a déjà été vue [ci-dessus](#propl1). Pour la seconde, nous pouvons nous limiter au cas où $X$ est positive. Soit alors $a = \Esp(X)$ et $Y = X-a$. Par linéarité, on a 
        $$ \Esp(Y^2) = \Esp(X^2) - 2a \Esp(X) + a^2 = \Esp(X^2)-a^2.$$
Et $\Esp(Y^2) \geq 0$ par le troisième point de la [proposition ci-dessus](#propl1). Par conséquent, $\Esp(X)^2 = a \leq \Esp(X^2)$ ce qui est le résultat recherché.

### Remarque {.remark}
En vertu de cette [proposition](#propl2), $\V(X)$ est **positive** et sa racine carrée $\sigma_X$ s'appelle l'*écart-type* de $X$. L’écart-type est une grandeur qui mesure la moyenne (en un certain sens) de l’écart des valeurs de $X$ à sa moyenne, d’où son nom.

On a également 
        $$\V(X) = \Esp(X^2)-\Esp(X)^2$$
que l'on obtient en développant $(X-\Esp(X))^2$. Cette manipulation anodine est fort utile dans la pratique. On retiendra que "La variance est égale à la moyenne des carrés moins le carré de la moyenne". On désigne le terme $\Esp(X^2)$ par l'expression *moment d'ordre deux* tandis que la variance est parfois appelée *moment centré d'ordre deux*.

### Remarque {.remark}
D'après ce qui précède, si $X$ est une variable aléatoire de carré intégrable, d'espérance $\Esp(X)$ et d'écart-type $\sigma_X >0$, alors la variable aléatoire $$\frac{X-\Esp(X)}{\sigma_X}$$
est d'espérance nulle et de variance 1. On dira qu'une telle variable aléatoire est *centrée et réduite*.

On peut remarquer que si $X$ et $Y$ sont dans $\L^2$, la variable aléatoire $XY$ est dans $\L^1$, puisque $|XY| \leq \frac{1}{2}(X^2+Y^2)$. On peut ainsi définir la *covariance* de deux variables aléatoires :

### Définition {.definition #defcov}
Si $X$ et $Y$ sont dans $\L^2$, la variable aléatoire $(X-\Esp(X))(Y-\Esp(Y))$ est intégrable. On appelle la *covariance* de $X$ et $Y$ l'espérance de cette variable aléatoire et on la note :
        $$\cov (X,Y) = \Esp((X-\Esp(X))(Y-\Esp(Y))).$$
Le *coefficient de corrélation* des variables aléatoires $X$ et $Y$ est le nombre 
        $$\rho(X,Y) = \frac{\cov (X,Y)}{\sqrt{\V(X)}\sqrt{\V(Y)}}$$
qui est bien défini lorsque $\V(X)>0$ et $\V(Y)>0$.

Du fait de la linéarité de l'espérance, on a 
$$\cov(X,Y) = \Esp(XY) - \Esp(X)\Esp(Y)$$
et d'ailleurs, on voit que la formule de calcul de la variance donnée plus haut est un cas particulier de cette formulation car $\V(X) = \cov(X,X)$. La linéarité de l'espérance nous donne encore pour $a,a',b,b' \in \R$
\begin{align*} 
\Esp((aX+b)(a'Y+b')) &= aa'\Esp(XY) + ab'\Esp(X) +a'b\Esp(Y) + bb'\\
\Esp(aX+b)\Esp(a'Y+b') &= aa'\Esp(X)\Esp(Y) + ab'\Esp(X) +a'b\Esp(Y) + bb'
\end{align*}
On en déduit que la covariance est une forme bilinéaire sur l'espace vectoriel des variables aléatoires de carré intégrable, et nous avons
$$\cov(aX+b,a'Y+b') = aa'\cov(X,Y)$$
En particulier, on a
$$ \V(aX) = a^2\V(X)$$
On en déduit que les coefficients de corrélation de $X$ et $Y$ et de $aX+b$ et $a'Y+b'$ sont égaux lorsque $aa' >0$.


### Inégalité de Cauchy-Schwarz {.proposition #CS}
Soit $X$ et $Y$ deux variables aléatoires de carré intégrable, alors on a *l'inégalité de Cauchy-Schwarz* :
        $$|\Esp(XY)| \leq \Esp(|XY|) \leq \sqrt{\Esp(X^2)\Esp(Y^2)}$$
avec égalité si et seulement si $X$ et $Y$ sont presque-sûrement proportionnelles.

### Démonstration {.proof}
La première inégalité a été démontrée plus haut. Pour la seconde, on a $\forall x \in \R$ d'après la linéarité de l'espérance :
$$x^2\Esp(X^2) + 2x\Esp(XY)+ \Esp(Y^2) = \Esp((xX+Y)^2) \geq 0.$$
Mais ceci n'est possible que si ce trinôme en $x$ n'a au plus qu'une seul racine réelle ; son discriminant 
        $$4\left((\Esp(XY))^2 - \Esp(X^2)\Esp(Y^2)\right)$$
doit donc être négatif ou nul ce qui donne le résultat.

Le discriminant est nul si et seulement si le trinôme admet une racine double $x_0$ et dans ce cas, $Y(\omega) = -x_0 X(\omega)$ pour presque tout $\omega$.

### Remarque {.remark}
On déduit de l'inégalité de [Cauchy-Schwarz](#CS) que le coefficient de corrélation de $X$ et $Y$ vérifie
$$-1\leq \rho(X,Y) \leq 1.$$

Enfin, il peut être intéressant de pouvoir calculer l'espérance d'une fonction mesurable d'une variable aléatoire réelle à densité qui est une variable aléatoire en vertu de la [proposition vue plus haut](#composition).

### Proposition {.proposition #esperanceg}
Soit $X$ une variable aléatoire réelle admettant la densité $f$, et $g$ une fonction mesurable de $\R$ dans $\R$. Alors $g(X)$ est intégrable si et seulement si l'intégrale
$$\int_\R |g(x)|f(x) dx,$$
est définie et dans ce cas
$$\Esp(g(X)) = \int_R g(x)f(x) dx.$$

Nous n'avons pas tous les éléments permettant de démontrer ce résultat, mais l'argument heuristique suivant permet de comprendre pourquoi il est vrai : supposons $g$ continue telle que $|g|f$ soit intégrable. Alors il existe une jauge $\gamma(t)$, sur $[-\infty, +\infty]$ telle que, si la subdivision pointée (totale ou partielle) $\mathcal{D} =\{(t_i, I_i)\}_i$ est subordonnée à $\gamma$, on a
$$
S(|g|f, \mathcal{D}) = \left|S(|g|f, \mathcal{D}) - \int _\R |g(x)|f(x) dx \right| 
\leq 
\varepsilon.
$$ 
Posons $X_i = t_i$ si $X \in I_i$, pour $i \in \{0,\ldots,n-1\}$. Ainsi, pour tout $\omega$, $X_n(\omega) \xrightarrow{n \to \infty} X(\omega)$ et par continuité de $g$, on a $g(X_n) \xrightarrow[n \to \infty]{} g(X)$. Comme $X_n$ est une variable aléatoire discrète, on a
$$\Esp(g(X_n)) = \sum_{i=0}^{n-1}g(t_i)\P(X\in I_i)l(I_i) \approx \sum_{i=0}^{n-1}g(t_i)f(t_i)$$
et ce dernier terme permet une apprximation de $\int _\R |g(x)|f(x) dx$ à une précision $\varepsilon$ près.

### Remarque {.remark}
L'espérance et la variance sont des cas particulier de ce résultat. On de plus pour $A \in \E_\R$ :
$$\Esp(1_A(X)) = \int_A f(x)dx = \P(X\in A)$$

## Exemples

Nous donnons ici quelques exemples de densités de probabilité. Nous reprenons en particulier les [trois exemples de densités donnés au premier cours](Probabilité I.pdf #exampledens) :

### *Loi uniforme*

sur $[a,b]$, où $a < b$ et on note $X \sim \mathcal{U}_{[a,b]}$ si $X$ est de densité
    $$ f(x) = \frac{1}{b-a} 1_{[a,b]} (x).$$
Son espérance vaut
        $$ \Esp(X) = \int_a^b \frac{x}{b-a} dx = \frac{a+b}{2}$$
et puisque
        $$ \Esp(X^2) = \int_a^b \frac{x^2}{b-a} dx = \frac{a^2 + ab +b^2}{3},$$
alors sa variance vaut
        $$ \V(X) = \Esp(X^2) - \Esp(X)^2 = \frac{(b-a)^2}{12}.$$

### *Loi exponentielle*

de paramètre $\theta > 0$ et on note $X \sim \mathcal{E}(\theta)$ si $X$ est de densité
        $$ f(x) = \theta e^{-\theta x} 1_{\{x>0\}}.$$
Son espérance et sa variance se calculent aisément et valent
        $$ \Esp(X) = \frac{1}{\theta} \text{ et } \V(X) = \frac{1}{\theta^2}$$

### *Loi gamma*

On rappelle tout d'abord que la fonction gamma est définie pour $\alpha \in \left] 0, + \infty \right[$ par 
        $$\Gamma(\alpha) = \int_0^{+\infty} x^{\alpha-1}e^{-x} dx.$$
En intégrant par partie, on obtient la relation $\Gamma(\alpha+1) = \alpha \Gamma(\alpha)$, et on a $\Gamma(1) = 1$. On en déduit que $\Gamma(n) = (n-1)!$.

Une variable aléatoire $X$ suit une loi gamma de paramètre d'échelle $\theta$ et d'indice $\alpha$ et on note $X \sim \Gamma(\alpha,\theta)$, si sa loi admet la densité
        $$f(x) = \frac{1}{\Gamma(\alpha)}\theta^\alpha x^{\alpha -1} e^{-\theta x}.$$
Son espérance et sa variance s'obtiennent en utilisant le changement de variable $x \mapsto \theta x$ et la définition de la fonction gamma :
        $$\Esp(X) = \frac{\alpha}{\theta} \text{ et } \V(X) = \frac{\alpha}{\theta^2}.$$
On remarquera que $\Gamma(1,\theta)$ est la loi exponentielle de paramètre $\theta$. 

Lorsque $\alpha$ est entier, la loi gamma permet de modéliser le temps d'attente avant la $n$-ième occurence d'événements indépendants de loi exponentielle de paramètre $\theta$.

### *Loi normale*

de paramètres $\mu$ et $\sigma^2$ et on note $X \sim \mathcal{N}(\mu,\sigma^2)$ si $X$ est de densité[^verif]
        $$f(x) = \frac{1}{\sqrt{2\pi}\sigma}\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$
Son espérance et sa variance valent
        $$\Esp(X) =  \mu \text{ et } \V(X) = \sigma^2$$
Pour le voir, on fait d'abord le calcul dans le cas centré réduit ($\mu = 0$ et $\sigma^2 =1$) puis on s'y ramène par le changement de variable $x \mapsto \frac{x-\mu}{\sigma}$.

[^verif]: Pour s'assurer qu'il s'agit bien d'une densité, on remarque que  $I = \int_{-\infty}^{+\infty} f(x) dx$ vérifie 
$$ I^2 = \int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} f(x) f(y) dxdy = \int_{0}^{2\pi} d\theta\int_{0}^{+\infty}\frac{1}{2\pi} \rho e^{-\rho^2/2}d\rho $$
(en passant en coordonnées polaires dans l'intégrale double). Le calcul est ensuite aisé et on obtient $I = 1$.

### Remarque {.remark}
Dans les exemples ci-dessus, on peut remarquer que les densités sont paramétrées par des nombres réels qui sont liés directement aux valeurs de l’espérance et de la variance de la variable. C’est très utile en statistique où l'on cherchera à estimer la valeur de ces paramètres à partir des observations disponibles. Dans le cas de la loi normale, la moyenne et la variance (empiriques) des échantillons fourniront ainsi directement des estimateurs des paramètres.

Il existe des variables aléatoires qui n’ont pas d’espérance, comme le montre l’exemple suivant.

### *loi de Cauchy*

Un gyrophare envoie un flash lumineux dans une direction aléatoire uniforme d’angle $\theta$. On cherche la distribution de l'abscisse $X$ du point d'impact du rayon lumineux sur un écran plan infini situé à distance 1 du gyrophare.

L'angle $\theta$ est une variable aléatoire uniforme sur $[-\pi/2,\pi/2]$, de densité $g(\theta) = \frac{1}{\pi}1_{[ -\pi/2,\pi/2 ]}(\theta)$. L'abscisse $X$ est donnée par $X = \tan \theta$, c'est donc une variable aléatoire, de fonction de répartition
\begin{align*}        
F(x) & = \P(X \leq x) \\
     & = \P(\theta \leq \arctan x) \\
     & = \int_{-\infty}^{\arctan x} \frac{1}{\pi}1_{[ -\pi/2,\pi/2 ]}(\theta) d\theta \\
     & = \frac{1}{\pi} \arctan x + \frac{1}{2}.
\end{align*}

$F$ est de classe $C^1$ de dérivée
        $$f(x) = \frac{1}{\pi(1+x^2)}, x \in \R$$

C'est la densité de la loi de Cauchy. Une variable aléatoire $X$ de loi de Cauchy n'admet pas d'espérance. En effet, $\frac{x}{\pi(1+x^2)} \sim_{x\to \infty} \frac{1}{x}$ n'est pas intégrable.

# Vecteurs aléatoires à densité
Nous allons généraliser ici la notion de variable aléatoire en considérant qu'elle peut prendre ses valeurs dans $\R^n$. Les vecteurs aléatoires se rencontrent naturellement lorsqu'on s'intéresse à plusieurs quantités conjointement, par exemple dans le cas de la météo, la température, la pluviométrie et la vitesse et la direction du vent.

## Définitions

Une variable aléatoire $X$ à valeurs dans $\R^n$ (ou vecteur aléatoire) est simplement une collection de $n$ variables réelles définies sur le même espace probabilisé $(\Omega, \A, \P)$, qui sont les *composantes* de $X$. On écrit $X = (X_1,\ldots,X_n)$.

De même qu'en dimension 1, la loi de $X$ est caractérisée par la fonction de répartition multi-dimensionnelle $F : \R^n \to \R$ définie par 
$$F(x_1,\ldots,x_n) = \P_X(X_1\leq x_1,\ldots,X_n\leq x_n)$$
Mais caractériser les fonctions de répartition sur $\R^n$ est délicat, de sorte que cette notion est rarement utilisée. Nous allons plus particulièrement nous intéresser aux vecteurs aléatoires à densité.

### Définition {.definition #defvect}
On dit que $X$ admet la densité $f$ si la fonction réelle $f$ sur $\R^n$ est positive, intégrable et vérifie 
$$\int_{\R^n} f(x) dx = \int_{-\infty}^{+\infty} \ldots \int_{-\infty}^{+\infty} f(x_1,\ldots,x_n) dx_1 \ldots dx_n= 1$$
et si
$$\P_X(X_1\leq x_1,\ldots,X_n\leq x_n) = \int_{-\infty}^{x_1} \ldots \int_{-\infty}^{x_n} f(x_1,\ldots,x_n) dx_1 \ldots dx_n$$

De la même manière que dans la [proposition vue plus haut](#esperanceg), on a :

### Proposition {.proposition #esperancegvect}
Soit $X$ un vecteur aléatoire de densité $f$, et soit $g$ une fonction de $\R^n$ dans $\R$, mesurable. On a alors $g(X)\in \L^1$ si et seulement si 
$$\int_{-\infty}^{+\infty} \ldots \int_{-\infty}^{+\infty} |g(x_1,\ldots,x_n)|f(x_1,\ldots,x_n) dx_1 \ldots dx_n,$$
est définie et dans ce cas, on a 
$$\Esp(g(X)) = \int_{-\infty}^{+\infty} \ldots \int_{-\infty}^{+\infty} g(x_1,\ldots,x_n)f(x_1,\ldots,x_n) dx_1 \ldots dx_n.$$

Pour revenir à la densité d'une composante d'un vecteur aléatoire, on intègre par rapport aux autres variables. On le présente ici dans le cas d'un couple $Z=(X,Y)$ de variables aléatoires. On généralise aisément à une dimension supérieure.

### Proposition {.proposition}
Supposons que $Z$ admette une densité $f$. Alors $X$ et $Y$ admettent les densités $f_X$ et $f_Y$ données par
$$f_X(x) = \int_\R f(x,y) dy, f_Y(y) = \int_\R f(x,y) dx.$$
Les fonctions $f_X$ et $f_Y$ s'appellent les *densités marginales* de $f$.

### Démonstration {.prooof}
Pour tout $x \in \R$, on a par définition
$$ \P(X \leq x) = \P(Z \in ]-\infty,x] \times \R) = \int_{-\infty}^x du \left(\int_\R f(u,v) dv\right).$$
Donc si $f_X$ est définie par $f_X(x) = \int_\R f(x,y) dy$, nous obtenons que $\P(X \leq x) = \int_{-\infty}^x f_X(u) du$, ce qui montre que $f_X$ est la densité de $X$. Le raisonnement est analogue pour $Y$.

### Remarque {.remark}
La réciproque de cette proposition est fausse en revanche : les variables aléatoires $X$ et $Y$ peuvent avoir des densités sans que le couple $Z = (X, Y )$ en ait une.

Supposons par exemple que $X = Y$. Si $\Delta = \{(x,x) ; x\in \R\}$ est la diagonale de $\R^2$, nous avons évidemment $\P_Z(\Delta) = 1$ mais si la [proposition précédente](#esperancegvect) était valide pour $\P_Z$, on aurait $\P_Z(\Delta) = \Esp(1_\Delta) = \int_{\R^2} 1_\Delta f_Z(z)dz = 0$ car $\Delta$ est de volume nul dans $\R^2$.

En particulier, il faut faire attention au fait que dans le cas général, la densité d'un couple de variables aléatoires n'est pas le produit des densités.

### Exemple
On lance une fléchette sur une cible circulaire de rayon unité. Le joueur est suffisamment maladroit pour que le point $M$ d’impact de la fléchette
soit supposé uniformément distribué sur la cible (On décide de n’observer que les lancés qui atteignent la cible).

Les coordonnées cartésiennes de $M \in D = \{(x,y) \in \R^2 , x^2+y^2 \leq 1\}$ constituent un couple de variables aléatoires de densité
$$f_{(X,Y)}(x,y) = \frac{1}{\pi}1_{D} (x,y)$$
uniforme sur le disque, par hypothèse. L'abscisse de $X$ est distribuée selon la densité marginale
$$f_X(x) = \int f_{(X,Y)}(x,y) dy = \frac{2}{\pi} (1-x^2) 1_{[-1,1]}(x).$$
La loi de $Y$ a la même densité.


## Moments d'un vecteur aléatoire

### Définition {.definition}
Si les composantes $X_i$ du vecteur aléatoire $X = (X_1,\ldots,X_n)$ sont intégrables, on peut définir le *vecteur espérance* 
        $$\Esp(X) = (\Esp(X_1),\ldots,\Esp(X_n))$$
Si les composantes $X_i$ du vecteur aléatoire $X = (X_1,\ldots,X_n)$ sont de carré intégrable, la *matrice de covariance* de $X$ est la matrice $C_X = (c_{i,j})_{1 \leq i \leq n , 1 \leq j \leq n}$ de taille $n \times n$ et dont les éléments valent
        $$c_{i,j} = \cov (X_i,X_j)$$

### Proposition {.proposition}
La matrice de covariance est symétrique non-négative (ou encore semi-définie positive).

### Démonstration {.proof}
La symétrie est évidente. Non-négative signifie que pour tous réels $a_1,\ldots,a_n$, on a $\sum_{i=1}^n \sum_{j=1}^n a_i a_j c_{i,j} \geq 0$. Un calcul simple montre que
$$ \sum_{i=1}^n \sum_{j=1}^n a_i a_j c_{i,j} = \V(\sum_{i=1}^n a_i X_i).$$

### Exemple : Vecteur Gaussien $n$-dimensionel {.example}
Un exemple de vecteurs aléatoires est celui des vecteurs gaussiens, que nous étudierons en détail au chapitre suivant. Soient $m \in \R^n$ et $C$ une matrice symétrique définie positive (c'est-à-dire telle que pour tout $x \in \R^n$ non identiquement nul $x^tCx > 0$ où $^t$ désigne la transposée). Le vecteur $X \in \R^n$ est un vecteur aléatoire gaussien d’espérance $m$ et de matrice de covariance $C$ si sa densité s’écrit
$$ f(x) = \frac{1}{(2\pi)^{n/2}\sqrt{\det (C)}}\exp (-\frac{1}{2}(x-m)^tC^{-1}(x-m)) $$
On a alors $\Esp(X) = m$ et $C_X =C$.

**TODO** figure densité Gaussienne

## Variables aléatoires indépendantes
<!-- Lorsque l'on modélise plusieurs variables conjointement, une hypothèse importante est celle de l'indépendance. Ce caractère traduit l'absence de lien de causalité entre les variables. Par exemple, on fait naturellement l'hypothèse d'indépendance lorsque l'on considère une répétition d'une même expérience dans les mêmes conditions. ??? -->
Dans ce paragraphe, on considère un couple $(X,Y)$ de vecteurs aléatoires respectivement à valeurs dans $\R^m$ et $\R^n$. Les résultats s'étendent sans peine à une famille finie quelconque. 


On peut se ramener aux évènements pour caractériser l'indépendance de deux vecteurs aléatoires. En effet, considérons le vecteur aléatoire $Z = (X,Y)$, $A$ et $B$ deux ensembles dans $\E_{\R^m}$ et $\E_{\R^n}$. On a vu que les évènements $X\in A$ et $Y \in B$ sont indépendants si et seulement si $\P_Z(X \in A, Y \in B) = \P(X^{-1}(A) \cap Y^{-1}(B)) = \P(X^{-1}(A))\P(Y^{-1}(B)) = \P_X(X \in A)\P_Y(Y \in B)$. Pour que deux vecteurs aléatoires soient indépendants, on va donc demander que ceci soit valable quelques soient $A$ et $B$.

### Définition {.definition #defvai}
Les vecteurs aléatoires $X$ et $Y$ sont *indépendants* si pour tous ensembles $A$ et $B$ des tribus correspondantes, 
$$\P(X \in A, Y \in B) = \P(X \in A)\P(Y \in B)$$

Cette définition se traduit en termes de densités dans la proposition suivante que l'on énonce sans perte de généralité pour un couple de variables aléatoires.

### Proposition {.proposition}
Soient $X$ et $Y$ deux variables aléatoires réelles de densités $f_X$ et $f_Y$. $X$ et $Y$ sont indépendantes si et seulement si 
le couple $Z = (X,Y)$ a pour densité (sur $\R^2$) :
$$f_Z(x,y) = f_X(x)f_Y(y).$$

### Démonstration {.proof}
S'il y a indépendance, la [définition](#defvai) implique 
$$P(X\leq x, Y\leq y) = P(X\leq x) \P(Y\leq y) = \int_{-\infty}^x f_X(u) du \int_{-\infty}^y f_Y(v) dv$$
ce qui montre que $\P_Z$ vérifie la [définition d'un vecteur aléatoire à densité](#defvect) avec $f_Z=f_X f_Y$.

Inversement, si $f_Z=f_X f_Y$, on a pour tous $A$, $B$ de $\E_{\R}$
$$\P(X\in A, Y\in B) = \int_A \int_B f_X(x) f_Y(y) dxdy = \P(X \in A)\P(Y \in B)$$ 
où on a utilisé le théorème de Fubini.

### {.anonymous}

Considérons maintenant deux fonctions $g$ et $h$ définies sur $\R^m$ et $\R^n$ telles que $g(X)$ et $h(Y)$ soient aussi des variables aléatoires. 

### Proposition {.proposition #indep_fct}
Avec les notations précédentes, si $X$ et $Y$ sont indépendantes de densités respectives $f_X$ et $f_Y$, les variables aléatoires $g(X)$ et $h(Y)$ sont aussi indépendantes. Si de plus $g(X)$ et $h(Y)$ sont intégrables, alors le produit $g(X)h(Y)$ est aussi intégrable, et on a 
$$ \Esp(g(X)h(Y)) = \Esp(g(X))\Esp(h(Y))$$ 

### Démonstration {.proof}
La première assertion est évidente par définition de l'indépendance. Par ailleurs, si $g(X)$ et $h(Y)$ sont intégrables, en notant $f_{(X,Y)}$ la densité du couple $(X,Y)$, et en utilisant le théorème de Fubini, on a
\begin{align*}
\Esp(g(X)h(Y))  & = \int_{\R^{m+n}} g(x)h(y) f_{(X,Y)}(x,y) dx dy \\
                & = \int_{\R^m} \int_{\R^n} g(x)h(y)f_X(x) f_Y(y) dx dy \\
                & = \left(\int_{\R^m}  g(x) f_X(x) dx \right) \left(\int_{\R^n} h(y) f_Y(y) dy\right)\\
                & = \Esp(g(X))\Esp(h(Y))
\end{align*}

### Remarque {.remark}
Ce résultat est encore valable si $X$ et $Y$ n'admettent pas de densité mais nous ne disposons pas encore des outils de théorie de la mesure nécessaires à sa démonstration.

On déduit de ce résultat et de la [définition de la covariance](#defcov) que :

### Corollaire {.corollary}
Si les variables aléatoires réelles $X$ et $Y$ sont indépendantes et de carré intégrable, alors
$\cov(X,Y) = 0$ et $\rho(X,Y) = 0$.

### Remarque
Attention, la réciproque est fausse. Par exemple, si $X \sim \mathcal{U}_{[-1,1]}$ et $Y = X^2$. $X$ et $Y$ ne sont clairement pas indépendantes mais on a

$$\cov(X,Y) = \cov(X,X^2) = \Esp(X^3) - \Esp(X)\Esp(X^2) = 0$$

# Identification de densité

Un problème important est le suivant. Soit $X$ une variable aléatoire réel, admettant la densité $f_X$. Soit $g$ une fonction mesurable, de sorte que $Y = g(X)$ soit aussi une variable aléatoire. Est-ce que $Y$ admet une densité, et si oui, comment la calculer ?

On peut déjà remarquer que cette densité n’existe pas toujours. Si par exemple $g(x) = a$ pour tout $x$, la loi de $Y$ est la masse de Dirac en $a$, qui n’a
pas de densité.

Pour résoudre ce problème, l’idée consiste à essayer de mettre $E(h(Y )) = E(h \circ g(X))$ sous la forme $\int h(y)f_Y (y)dy$ pour une fonction convenable 
$f_Y$, et une classe de fonctions $h$ suffisamment grande. La fonction $f_Y$ sera alors la densité cherchée.

La [proposition](#esperanceg) implique
$$ \Esp(h(Y)) = \Esp(h \circ g (X)) = \int_{\R} h \circ g(x) f_X(x) dx$$

et on fait le changement de variable $y = g(x)$ dans cette intégrale. Cela nécessite que $g$ soit dérivable et bijective “par morceaux”, et il faut faire très attention aux domaines où $g$ est croissante ou décroissante. Puisque la fonction $h$ est arbitraire, on appelle couramment cette technique la *méthode de la fonction muette*. Cette approche résulte en fait de la proposition suivante que nous ne démontrerons pas :

### Proposition {.proposition}
Si il existe une fonction $f$ telle que pour toute fonction mesurable $h$ telle que $h(x) f(x)$ soit absolument intégrable, 
$$\Esp(h(X)) = \int_\R h(x) f(x) dx$$
alors la loi de $X$ admet la densité $f$.

L’idée de la preuve repose sur le fait que parmi ces fonctions se trouvent les $h = 1_{]-\infty,y]}$, pour laquelle la formule précédente donne la fonction de répartition de $f$.

Nous donnons ici quelques exemples d'application de cette méthode :

 * Soit $Y = aX + b$, où $a$ et $b$ sont des constantes. Si $a=0$, alors $Y = b$ et la loi de $Y$ est la masse de Dirac en $b$ (sans densité). Si $a \neq 0$, on fait le changement de variable $y = ax+b$, ce qui donne
        $$ \Esp(h(Y)) = \int_\R h(ax+b) f_X(x) dx = \int_\R h(y) f_X(\frac{y-b}{a})\frac{1}{|a|} dy $$
 Donc 
        $$ f_Y(y) = f_X(\frac{y-b}{a})\frac{1}{|a|} $$
 * Soit $Y =X^2$. La fonction $g$ est décroissante sur $\R_-$ et croissante sur $\R_+$. Le changement de variable $y = x^2$ donne alors
        \begin{align*}
        \Esp(h(Y)) &= \int_{-\infty}^0 h(x^2) f_X(x) dx + \int_0^{+\infty} h(x^2) f_X(x) dx\\
                   &= \int_0^{+\infty} h(y) f_X(-\sqrt{y})\frac{1}{2\sqrt{y}} dy + \int_0^{+\infty} h(y) f_X(\sqrt{y})\frac{1}{2\sqrt{y}}dy
        \end{align*}
   et on en déduit
        $$f_Y(y) = (f_X(-\sqrt{y})+f_X(\sqrt{y}))\frac{1}{2\sqrt{y}}1_{\left]0,+\infty\right[}$$

Dans le cas des vecteurs aléatoires, l'idée est la même. Soit $X = (X_1,\ldots,X_n)$, un vecteur aléatoire de densité $f_X$ sur $\R^n$, $g$ une fonction de $\R^n$ dans $\R^m$ et $Y = g(X)$. Plusieurs cas sont à considérer :

 1. $m > n$, le vecteur $Y$ n'admet pas de densité.
 2. $m=n$, on utilise comme dans le cas unidimensionel le changement de variable $y = g(x)$ dans 
        $$ \Esp(h(Y)) = \Esp(h \circ g (X)) = \int_{\R^n} h \circ g(x) f_X(x) dx $$
    Supposons d'abord que $g$ soit une bijection continûment différentiable de $A$ dans $B$, ouverts de $\R^n$. Sous l'hypothèse que $h \circ g(x) f_X(x)$ soit absolument intégrable, le [théorème de changement de variable](Calcul Intégral III.pdf) nous assure :
        $$ \int_A h\circ g f_X(x) dx = \int_B h(y) f_X \circ g^{-1}(y) \frac{1}{|\det J_g (y)|} dy,$$ 
    où $J_g$ désigne la matrice de Jacobi associée à la différentielle de $g$. Dans le cas où $f_X(x) = 0$ en dehors de $A$, on obtient que $Y$ admet la densité
        $$ f_Y(y) = 1_B(y)f_X \circ g^{-1}(y)\frac{1}{|\det Dg (y)|}.$$
    Lorsque $g$ est simplement continûment différentiable, il existe souvent une partition finie $(A_i)_{1\leq i \leq n}$ de l'ensemble $\{x ; f(x) >0\}$, telle que $g$ soit injective sur chaque $A_i$. On note alors $B_i = g(A_i)$ l'image de $A_i$ par $g$. On découpe alors l'intégrale selon les $A_i$, on applique la formule précédente à chaque morceau et on somme pour obtenir :
        $$ f_Y(y) = \sum_{i=1}^n 1_{B_i}(y)f_X \circ g^{-1}(y) \frac{1}{|\det J_g (y)|},$$
    où $g^{-1}$ est bien définie sur chaque $B_i$ comme image réciproque de la restriction de g à $A_i$.
 3. $m < n$, on commence par "compléter" $Y$, en essayant de construire une application $g'$ de $\R^n$ dans $\R^n$ dont les $m$ premières composantes coïncident avec les composantes de $g$ et pour laquelle on peut appliquer l'une des deux formules précédentes. On obtient ainsi la densité $f_Y'$ de $Y' = g'(X)$ puis     on obtient la densité de $Y$ en calculant sa *loi marginale* :
        $$f_Y(y_1,\ldots,y_m) = \int_{\R^{n-m}} f_{Y'}(y_1,\ldots,y_m,y_{m+1},\ldots y_n) dy_{m+1}\ldots dy_n.$$
    Nous reviendrons sur cette notion au chapitre suivant.

### Exemples

 1. **Coordonnées polaires**
    Soit $X = (U,V)$ un vecteur aléatoire de $\R^2$, et $Y = (R,\Theta)$ ses coordonnées polaires. La transformation $g$ est un difféomorphisme de $A = \R^2\setminus\{0\}$ dans $B = \left]0,+\infty\right[\times \left]0,2\pi\right]$, et son inverse $g^{-1}$ s'écrit : $u = r\cos \theta,\, v= r\sin \theta$.
    Le Jacobien de $g^{-1}$ au point $(r,\theta)$ vaut $r$, donc le point 2. ci-dessus entraîne que 
        $$ f_Y(r,\theta) = r f_X(r\cos\theta,r\sin\theta)1_B(r,\theta)$$
    Par exemple, si $U$ et $V$ sont indépendantes et de loi $\No(0,1)$, on a $f_X(u,v) = \frac{1}{2\pi}\exp\left(-\frac{u^2+v^2}{2}\right)$ et donc
        $$ f_Y(r,\theta) = \frac{1}{2\pi} r\left(-\frac{r^2}{2}\right)1_{\left]0,+\infty\right[ }(r)1_{\left]0,2\pi\right]}(\theta).$$
    En particulier, on remarque que $R$ et $\Theta$ sont indépendantes de densités respectives $r\exp\left(-\frac{r^2}{2}\right)1_{\left]0,+\infty\right[}(r)$ et $1_{\left]0,2\pi\right]}(\theta)$.
 2. **Somme de deux variables aléatoires indépendantes**
    Soient $U$ et $V$ indépendantes et admettant les densités $f_U$ et $f_V$, on cherche la densité de la somme $Z = U+V$. On commence par compléter $Z$ en le couple $T = (U,Z)$ (par exemple), correspondant à la bijection $g(u,v) = (u, u+v)$ sur $\R^2$ dont le jacobien est 1 et d'inverse $g^{-1}(x,y) = (x,x-y)$. Appliquant le point 3. ci-dessus, on obtient :
        $$f_Z(z) = \int_{\R}f_U(u)f_V(z-u) du = \int_{\R}f_U(z-v)f_V(v)dv.$$
    La fonction $f_Z$ est appelée *le produit de convolution* des des fonctions $f_U$ et $f_V$.


# Exercices

## Loi de vie et de mort 

La durée de vie d'un être vivant ou d'un matériel peut-être assimilée à une variable aléatoire strictement positive $T$.
Dans ce cadre, on peut définir les notions suivantes :

* Loi de vie a priori : il s'agit de la loi du temps $T$ caractérisée par fonction de répartition complémentaire
        $$G(t) = \P(T>t)$$
* Loi de survie après $t_0 \geq 0$ : il s'agit de la loi du temps $T-t_0$ qu'il lui reste à vivre, sachant qu'il était encore en vie à t_0, de fonction de répartition complémentaire
        $$G_{t_0}(t) =\P(T>t+t_0|T>t_0)$$

On dira que la loi de vie satisfait la propriété de non vieillissement (ou d'absence de mémoire) si la loi de survie et la loi de vie sont égales :
        $$\forall t \geq 0 \text{ et } \forall t_0 \geq 0, G_{t_0}(t) = G(t)$$

### Question 1 {.question #viemort1}

Exprimer la loi de survie à partir de la loi a priori

### Question 2 {.question #viemort2}

Montrer qu'une variable aléatoire $T$ satisfait la propriété de non-vieillissement si et seulement si elle est de loi exponentielle.

### Question 3 {.question #viemort3}
On suppose que $T$ admet une densité continue sur $\R_+^\ast$. Montrer que l'on peut définir le taux de mort à l'instant $t$ par 
        $$D(t) = \lim_{\Delta t \to 0} \frac{1}{\Delta t}\P(t < T \leq t + \Delta t | T >t)$$
et exprimer $G$ en fonction de $D$.

Quelles lois correspondent-elles à $D$ constant ?


## Loi bêta {.question #loibeta}

Soit $X = (U,V)$ un vecteur aléatoire de $\R^2$, avec $U$ et $V$ indépendantes de lois $\Gamma(\alpha,\theta)$ et $\Gamma(\beta,\theta)$. Identifier la densité de $\frac{U}{U+V}$.

## Crues centennales de la Seine
On suppose que la hauteur d’eau maximale au cours de l’année $n$ est décrite par une variable aléatoire $X_n$ de densité $f(x)$ et de fonction de répartition $F(x)$, identique pour toutes les $X_n$, que l'on suppose également indépendantes.

### Question 1 {.question #crue1}
Calculer la fonction de répartition du maximum sur $n$ années $Y = \max(X_1,\ldots,X_n)$.

### Question 2 {.question #crue2}
En déduire la densité de $Y$.

### Question 3 {.question #crue3}
Expliciter la densité de $Y$ lorsque les $X_i$ sont de loi uniforme sur $[0,1]$. 

### Question 4 {.question #crue4}
Selon mêmes hypothèses, calculer la hauteur minimale des quais pour que la probabilité de voir la Seine déborder sur une période de $n$ années soit inférieure à 1/1000.

### Question 5 {.question #crue5}
Toujours selon les mêmes hypothèses, calculer la médiane de $Y$. La comparer avec celle des $X_i$. Commenter.



# Solutions

## Loi de vie et de mort 

### Question 1 {.answer #answer-viemort1}

Par définition, on a 
$$ G_{t_0}(t) = \P(T>t+t_0|T>t_0) = \frac{\P(T>t+t_0,T>t)}{\P(T>t)} = \frac{G(t+t_0)}{G(t)}$$

### Question 2 {.answer #answer-viemort2}

D'après la question précédente, $G$ vérifie alors $G(t_0+t) = G(t)G(t_0)$ pour tous $t, t_0 > 0$. Comme $G$ est décroissante, continue à gauche et tend vers 0 à l'infini, on en déduit que $G(t) = e ^{-\theta t}$, pour un $\theta > 0$. On reconnaît la fonction de répartition complémentaire d'une loi exponentielle de paramètre $\theta$.

### Question 3 {.answer #answer-viemort3}
\begin{align*}
D(t) &= \lim_{\Delta t \to 0} \frac{1}{\Delta t}\P(t < T \leq t + \Delta t | T >t)\\
     &= \lim_{\Delta t \to 0} \frac{1}{\Delta t}\frac{\P(t < T \leq t + \Delta t)}{\P(T >t)}\\
     &= \frac{1}{G(t)} \lim_{\Delta t \to 0} \frac{G(t) - G(t + \Delta t)}{\Delta t}\\
     &= -\frac{g(t)}{G(t)}
\end{align*}
Ainsi, $D(t) = \frac{d}{dt}(-\ln G(t))$ et comme $G(0) = 1$, alors on a pour $t >0$
        $$G(t) = \exp\left(-\int_0^tD(s) ds\right)$$
Si $D$ est constant, on retrouve une loi exponentielle.


## Loi bêta {.answer #answer-loibeta}
On note d'abord que la dimension de $Y$ est plus petite que celle de $X$. On va donc compléter $Y$ en prenant par exemple $Y' = (Y,Z)$, avec $Z=U+V$, ce qui correspond à $g(u,v) = \left(\frac{u}{u+v},u+v\right)$. Cette application est bijective de $A = \left]0,+\infty\right[^2$ dans $B = \left]0,1\right[ \times \left]0,+\infty\right[$, d'inverse $g^{-1}(y,z) = (yz,z(1-y))$, qui a pour jacobien $z$.

Comme $f_X(u,v) = \frac{\theta^{\alpha+\beta}}{\Gamma(\alpha)\Gamma(\beta)}u^{\alpha-1}v^{\beta-1}e^{-\theta(u+v)}1_A(u,v)$, on a 
        $$f_{Y'}(y,z) = \frac{\theta^{\alpha+\beta}}{\Gamma(\alpha)\Gamma(\beta)}z^{\alpha+\beta -1}y^{\alpha-1}(1-y)^{\beta-1}e^{-\theta z}1_B(y,z).$$
On obtient alors la densité de Y en intégrant $f_{Y'}(y,z)$ par rapport à $z\in \left]0,+\infty\right[$ :
\begin{align*}
f_Y(y) &= \int_0^{+\infty} f_{Y'}(y,z) dz\\
       &= \frac{\theta^{\alpha+\beta}}{\Gamma(\alpha)\Gamma(\beta)}y^{\alpha-1}(1-y)^{\beta-1}1_{\left]0,1\right[}(y)\int_0^{+\infty}z^{\alpha+\beta -1}e^{-\theta(z)}dz\\
       &= \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}y^{\alpha-1}(1-y)^{\beta-1}1_{\left]0,1\right[}(y),
\end{align*}
où on a utilisé la définition de la fonction gamma et le changement de variable linéaire $z \mapsto \theta z$.
On appelle loi bêta de paramètres $\alpha$ et $\beta$ la loi admettant cette densité. Admettant une grande variété de formes, elle permet de modéliser de nombreuses distributions à support fini.

La loi bêta apparaît naturellement dans une expérience d'urnes, donnée par George Pólya dans un article de 1930, [*Sur quelques points de la théorie des probabilités*](http://www.numdam.org/article/AIHP_1930__1_2_117_0.pdf). Il décrit l'expérience suivante : on se donne une urne contenant initialement $r$ boules rouges et $b$ boules bleues, on tire une boule dans l'urne, puis on la remet dans l'urne avec une deuxième boule de même couleur. Alors la proportion de boules rouges tend vers une variable aléatoire de loi Beta$(r,b)$, et, inversement, la proportion de boules bleues tend vers une variable aléatoire de loi Beta$(b,r)$. 

Nous obtenons aussi facilement la densité de $Z$. En effet, on a $f_{Y'}(y,z) = f_Y(y)f_Z(z)$ ($Y$ et $Z$ sont donc indépendantes), où
$$f_Z(z) = \frac{\theta^{\alpha+\beta}}{\Gamma(\alpha+\beta)}z^{\alpha+\beta -1}e^{-\theta z}1_{\left]0,+\infty\right[}$$
On a ainsi démontré que si $U$ et $V$ sont deux variables aléatoires indépendantes de lois respectives $\Gamma(\alpha,\theta)$ et $\Gamma(\beta,\theta)$, alors $U+V$ suit la loi $\Gamma(\alpha+\beta,\theta)$ et est indépendante de $\frac{U}{U+V}$ qui suit une loi bêta de paramètres $(\alpha,\beta)$.

## Crues centennales de la Seine

### Question 1 {.answer #answer-crue1}
Soit $x\in \R$
\begin{align*}
F_Y(x) = F(Y\leq x) &= F(X_1\leq x,\ldots,X_n\leq x)\\
           &= \prod_{i=1}^n F(X_i\leq x) \\
           &= F(x)^n
\end{align*}
puisque les $X_i$ sont indépendantes et de même loi

### Question 2 {.answer #answer-crue2}
Soit $x\in \R$
\begin{align*}
f_Y(x) &= \frac{\partial}{\partial x} F_Y(x)\\
       &= \frac{\partial}{\partial x} F(x)^n\\
       &= nf(x)F(x)^{n-1}
\end{align*}

### Question 3 {.answer #answer-crue3}
On a alors $f(x) = 1_{[0,1]}(x)$ et $F(x) = x 1_{[0,1]}(x)$. On en déduit
$$ f_Y(x) = n x^{n-1}1_{[0,1]} $$

### Question 4 {.answer #answer-crue4}

On cherche à déterminer $x$ tel que $\P(Y > x) \leq \frac{1}{1000}$. Or,
$$ \P(Y > x) = 1-\P(Y \leq x) = 1 - F_Y(x) = 1 - F(x)^n = 1-x^n $$
Ainsi
$$ 1-x^n \leq \frac{1}{1000} \Leftrightarrow (1-\frac{1}{1000})^{1/n} \leq x $$

### Question 5 {.answer #answer-crue5}
On rappelle que la médiane est le réel $m$ tel que $\frac{1}{2} = \P(Y \leq m) = F_Y(m)$.

On cherche donc $m$ tel que $m^n = \frac{1}{2}$, soit $m = \frac{1}{2^{1/n}}$.

On voit que cette valeur est plus élevée que la médiane des $X_i$ qui vaut $\frac{1}{2}$. Elle tend même vers 1 lorsque $n$ tend vers l'infini.



Références
================================================================================
