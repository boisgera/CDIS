% Probabilités IV

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

On s'est consacré jusqu'à présent à l'étude de (suites de) variables aléatoires indépendantes. En pratique cependant, on rencontre souvent des variables dépendantes les unes des autres. Dans le cas de la météo, les variables température, vitesse du vent et pression en fournissent un exemple. On va s'attacher dans ce chapitre à décrire les **lois conditionnelles** qui vont permettre de résumer l'information apportée par une variable (ou un vecteur) sur une autre et s'intéresser en particulier à l'**espérance conditionnelle** qui indiquera le comportement moyen d'une variable conditionnellement à une autre. Ce dernier cas pose le cadre probabiliste d'un des problèmes fondamentaux en apprentissage statistique : l'apprentissage supervisé, où on dispose d'un ensemble de réalisations d'une variable dont on cherche à prédire le comportement à partir d'un ensemble de variables dites explicatives (ou prédicteurs).

# Lois conditionnelles dans un couple

Soient deux variables aléatoire $X$ et $Y$ définies sur le même espace probabilisé $(\Omega, \A, \P)$. Dans le cas où $X$ et $Y$ sont indépendantes, on a vu que pour tous boréliens $B_1$ et $B_2$ de $\R$, on a 
$$\P(X\in B_1, Y\in B_2)= \P(X\in B_1)\P(Y\in B_2) = \P_X(B_1)\P_Y(B_2) = \int_{B_1}\P_Y(B_2)\P_X(dx),$$
où on a utilisé le théorème de Fubini (les mesures de probabiltés sont finies, donc $\sigma$-finies).

Du fait de l'indépendance, on a aussi $\P_Y(B_2) = \P(Y\in B_2) = \P(Y \in B_2 | X \in B_1) = \P_Y(B_2|X \in B_1)$ ce qui exprime que pour tout borélien $B_1$, la loi conditionnelle de $Y$ sachant $X\in B_1$ est identique à la loi de $Y$.

Dans le cas général, on va chercher une égalité de la forme
$$\P(X\in B_1, Y\in B_2) = \P_X(B_1)\P_Y(B_2 |X\in B_1) = \int_{B_1}\P_{Y|X=x}(B_2)\P_X(dx)$$
et s'intéresser à caractériser la *loi conditionnelle de $Y$ sachant $X=x$*, que l'on notera donc $\P_{Y|X=x}$.

De même, pour toute application $g : \R^2 \to \R$ borélienne telle que $g(X,Y)$ admette une espérance (relativement à la loi du couple $\P_{X,Y}$), on voudrait écrire :
$$\Esp(g(X,Y)) = \int_{\R} \left( \int_{\R} g(x,y) \P_{Y|X=x}(dy)\right) \P_X(dx)$$

Pour bien fixer les idées, on va décrire spécifiquement les cas où $X$ est discrète puis où le couple $(X,Y)$ admet une densité avant d'aborder le cas général.

## Cas où $X$ est discrète
Dans ce paragraphe, on suppose que la variable aléatoire réelle $X$ est discrète, c'est-à-dire que l'ensemble $X(\Omega) \subset \R$ des valeurs $x_k$ prises par $X$ est au plus dénombrable.

On peut imposer que $\forall x \in X(\Omega)$ on ait $\P(X=x) > 0$, quitte à modifier $X$ sur un ensemble de probabilité nulle. On va ainsi pouvoir utiliser la définition de la probabilité conditionnelle pour des événements de la forme $\{X =x\}$. Ceci permet d'écrire pour tous boréliens $B_1$ et $B_2$ de $\R$ :
\begin{align*}
\P(X \in B_1, Y \in B_2) &= \sum_{x \in X(\Omega)\cap B_1} \P(X=x, Y\in B_2)\\
                         &= \sum_{x \in X(\Omega)\cap B_1} \P(X=x) \P(Y \in B_2 | X=x)\\
                         &= \int_{B_1} \P(Y \in B_2 | X=x) \P_X(dx)
\end{align*}
puisque $\P_X = \sum_{x \in X(\Omega)} \P(X=x)\delta_x$. On obtient ainsi l'écriture souhaitée en posant
$$\P_{Y|X=x}(B_2) = \P(Y \in B_2 | X=x),\,\,\,\forall x \in X(\Omega), \forall B_2\in\B(\R).$$

### Remarque {.remark}
$\P_{Y|X=x}$ ainsi définie est simplement la probabilité sur $(\R,\B(\R))$ image par $Y$ de la probabilité conditionnelle $\P(\cdot|X=x)$ définie sur $(\Omega,\A)$, autrement dit, la **loi de $Y$ relative à $\P(\cdot|X=x)$** et non à $\P$.

La formule ci-dessus s'écrit $\P_{X,Y}(B_1 \times B_2) = \int_{B_1} \P(Y \in B_2 | X=x) \P_X(dx)$, où $\P_{X,Y}$ est la loi du couple. Elle se généralise à tout borélien $B$ de $\R^2$ de la manière suivante :

\begin{align*}
\P_{X,Y}(B) &= \P((X,Y)\in B) = \sum_{x \in X(\Omega)} \P(X=x, (x,Y) \in B) \\
      &= \sum_{x \in X(\Omega)} \P(X=x) \P((x,Y) \in B | X=x) \\
      &= \sum_{x \in X(\Omega)} \P(X=x) \P_{Y|X=x}(B_x),
\end{align*}

où $B_x = \{y\in \R, (x,y) \in B\}$. Ainsi, pour tout $B$ borélien de $\R^2$,

$$\Esp(1_B(X,Y)) = \int_{\R^2} 1_B(x,y)\P_{X,Y}(dx dy) = \int_\R \left(\int_\R 1_B(x,y) \P_Y(dy|X = x)\right)  \P_X(dx)$$

Par linéarité de l'espérance, on peut ainsi exprimer l'espérance d'une fonction étagée. Pour avoir le résultat pour une fonction positive, on exprime celle-ci comme limite simple d'une suite croissante de fonctions étagées, et on applique le théorème de convergence monotone. Enfin, on applique cette construction à $g_+$ et $g_-$ pour une fonction $g$ de signe quelconque $\P_{X,Y}$-intégrable. En d'autres termes, on reprend le procédé de construction de l'intégrale de Lebesgue. On obtient ainsi la formule souhaitée :
$$\Esp(g(X,Y)) = \int_{\R} \left( \int_{\R} g(x,y) \P_Y(dy|X = x)\right) \P_X(dx).$$

### Exemple {.example #ex1}

Soit $X \geq 0$ une variable aléatoire à valeurs dans $\N$ et $Y$ une variable aléatoire réelle positive telle que la loi du couple $\P_{X,Y}$ vérifie pour tout $n\in\N$ et tout borélien $B_2$ de $\R$ :
$$\P_{X,Y} (\{n\}\times B_2) = (1-\alpha)\alpha^n \int_{B_2 \cap \R_+^\star}e^{-t}\frac{t^n}{n!}dt,\,\,\, 0 < \alpha <1$$
$\P_{X,Y}$ est bien une probabilité sur $\R^2$ puisque par convergence monotone :
\begin{align*}
\P_{X,Y} (\R^2) &= \P_{X,Y}(\N \times \R) \\
                &= \sum_{n\in\N} \P_{X,Y} (\{n\}\times \R)\\
                &= \sum_{n\in\N} (1-\alpha)\alpha^n \int_{\R_+^\star}e^{-t}\frac{t^n}{n!}dt \\
                &= (1-\alpha)\int_{\R_+^\star}e^{-t} \sum_{n\in\N} \frac{\alpha t^n}{n!}dt \\
                &= (1-\alpha)\int_{\R_+^\star}e^{-(1-\alpha)t} dt = 1
\end{align*}               
où on aura reconnu la loi exponentielle de paramètre $(1-\alpha)$.
$\forall n \in \N$, 
$$ \int_{\R_+^\star}e^{-t}\frac{t^n}{n!}dt = \int_{\R_+^\star}e^{-t}\frac{t^{(n-1)}}{(n-1)!}dt = \ldots = \int_{\R_+^\star}e^{-t}dt =1$$
par intégration par parties itérée. la loi marginale de $X$ s'écrit donc :
$$\forall n \in \N, \P(X=n) = \P_{X,Y} (\{n\}\times \R_+^\star) = (1-\alpha)\alpha^n,$$ 
loi géométrique de paramètre $(1-\alpha)$. On en déduit la loi conditionnelle de $Y$ sachant $X = x$ :
$$\P_{Y|X=x}(B_2) = \P(Y \in B_2 | X=x) = \frac{\P_{X,Y} (\{n\}\times B_2)}{\P(X=n)} = \int_{B_2 \cap \R_+^\star} e^{-t}\frac{t^n}{n!}dt$$
et $\P_{Y|X=x}$ est la donc la loi gamma de paramètre $(n+1,1)$.


## Densités conditionnelles

On suppose maintenant que le couple $(X,Y)$ admet une densité $f_{X,Y}$ (par rapport à la mesure de Borel-Lebesgue). On note $f_X(x) = \int_\R f_{X,Y}(x,y)dy$ (respectivement $f_Y(y) = \int_\R f_{X,Y}(x,y)dx$) la loi marginale de $X$ (resp. de $Y$). On s'intéresse à caractériser la densité de la variable $Y$ connaissant la valeur prise par la variable $X$, c'est la *densité conditionnelle* de $Y$ sachant $\{X = x\}$ :

### Proposition {.proposition #defdenscond}
La formule suivante définit une densité sur $\R$, pour tout $x \in \R$ tel que $f_X(x) > 0$.
$$ f_{Y|X=x}(y) = \frac{f_{X,Y}(x,y)}{f_X(x)}.$$
Cette fonction s'appelle la *densité conditionnelle de $Y$ sachant $\{X = x\}$*.
La probabilité conditionnelle de $Y$ sachant $\{X = x\}$ s'écrit ainsi $\P_{Y|X=x} = f_{Y|X=x}l$, où $l$ représente la mesure de Borel-Lebesgue.

### Démonstration {.proof}
La preuve est immédiate puisque $f_{Y|X=x}$ est une fonction positive d'intégrale 1.

L’interprétation de cette définition est la suivante : la fonction $f(Y|X=x)$ est la densité de la “loi conditionnelle de $Y$ sachant que $X = x$”. Bien sûr, nous avons $\P(X = x) = 0$ puisque $X$ admet une densité, donc la phrase ci-dessus n’a pas réellement de sens, mais elle se justifie heuristiquement ainsi : $dx$ et $dy$ étant de “petits” accroissements des variables $x$ et $y$ et lorsque $f$ et $f_X$ sont continues et strictement positives respectivement en $(x,y)$ et $x$ :
\begin{align*}
f_X(x) dx & \approx \P(X \in [x, x+dx])\\
f_{X,Y}(x,y) dx dy & \approx \P(X \in [x, x+dx], Y \in [y, y+dy])\\
\end{align*}
Par suite 
\begin{align*}
f_{Y|X=x} (y) dy & \approx \frac{\P(X \in [x, x+dx], Y \in [y, y+dy])}{\P(X \in [x, x+dx])}\\
                 & \approx \P(Y \in [y, y+dy]|X \in [x, x+dx])\\
\end{align*}

On a alors le résultat suivant qui résout le problème posé en introduction :

### Proposition {.proposition}
Pour toute fonction $g : \R^2 \to \R$ telle que $g(X,Y)$ admette une espérance, on a :
$$\Esp(g(X,Y)) = \int_\R \left( \int_\R g(x,y)f_{Y|X=x}(y) dy \right) f_X(x) dx,$$ 
dont on déduit, en prenant $g=1_{B_1 \times B_2}$, que :
$$\P(X\in B_1, Y\in B_2) = \int_{B_1} \left( \int_{B_2}f_{Y|X=x}(y) dy \right) f_X(x) dx.$$

### Démonstration {.proof}
On a 
\begin{align*}
\Esp(g(X,Y)) &= \int_{\R^2} g(x,y) f_{X,Y}(x,y) dy dx \\
             &= \int_{\R^2} g(x,y) f_{Y|X=x}(y)f_X(x) dy dx \\
             &= \int_\R \left( \int_\R g(x,y)f_{Y|X=x}(y) dy \right) f_X(x)dx,
\end{align*}
les calculs étant licites par application du théorème de Fubini et du fait que l'application $x \mapsto \int_\R g(x,y)f_{Y|X=x}(y) dy$ est définie pour $f_X(x) >0$, soit presque partout relativement à la mesure $\P_X = f_X l$.

## Cas général
On peut établir le résultat suivant, qui complète le théorème de Fubini et le résultat d'existence et d'unicité des mesures produits, et que l'on admettra.

### Théorème {.theorem #fubinicond}
Soit un couple $(X,Y)$ de variables aléatoires réelles de loi jointe $\P_{X,Y}$, il existe une famille $\P_{Y|X=x}$ de probabilités sur $(\R,\B(\R))$, unique à une égalité $\P_X$-presque partout près[^footequi], qui vérifie pour tous $B_1, B_2$ boréliens de $\R$ :
$$ \P_{X,Y}(B_1 \times B_2) = \int_{B_1} \left( \int_{B_2} \P_{Y|X=x}(dy) \right) \P_X(dx).$$
Ces probabilités sont appelées *lois conditionnelles* de $Y$ sachant $X =x$. On a de plus pour toute application $g : \R^2 \to \R$ telle que $g(X,Y)$ admette une espérance :
$$\Esp(g(X,Y)) = \int_\R \left( \int_\R g(x,y)\P_{Y|X=x}(dy) \right) \P_X(dx).$$ 

[^footequi]: c'est-à-dire qu'on peut définir ces probabilités de la manière qu'on souhaite pour les boréliens $B$ tels que $\P_X(B)=0$.

### Remarques {.remark}

* Ce résultat peut être interprété comme un **théorème de Fubini conditionnel**, dans le sens où il permet une intégration séquentielle, mais ici la mesure de probabilité du couple $(X,Y)$ s'exprime comme un produit de mesures dont l'un des termes dépend de la variable d'intégration de l'autre. En particulier, si on change l'ordre d'intégration, on change les mesures qui interviennent.
* Fréquemment, dans les applications, la famille des lois conditionnelles est une donnée du modèle considéré, et leur existence ne pose donc pas de problème !
* On retrouve les cas vus précédemment en notant que pour tout borélien $B_1$ de $\R$ on a $\P_x(B_1) = \int_{B_1}\P_X(dx) = \sum_{x \in \B_1} \P(X=x)$ lorsque $X$ est discrète, et que pour tous boréliens $B_1$ et $B_2$ de $\R$ on a $\P_X(B_1) = \int_{B_1} f_X(x)dx$ et $\P_{X,Y}(B_1 \times B_2) = \int_{B_1 \times B_2}f_{X,Y}(x,y) dx dy$.
* Dans tout ce qui précède, les rôles de $X$ et $Y$ peuvent évidemment être inversés. 

## Conséquences
Le [théorème précédent](#fubinicond) a deux conséquences majeures. Il fournit d'une part un moyen efficace d'identifier la loi marginale de $Y$ connaissant la loi marginale de $X$ et la loi de $Y$ sachant $X$. En effet, en notant que pour tout borélien $B$ de $\R$, $\P_Y(B) = \P_{X,Y}(\R \times B)$ et en appliquant ce théorème, on a la proposition suivante :

### Proposition {.proposition #balcond}

* La loi marginale $\P_Y$ de $Y$ s’exprime comme la moyenne des lois conditionnelles $\P_{Y|X=x}$ pondérée par la loi de $X$. Pour tout $B$ borélien de $\R$
$$\P_Y(B) = \int_\R \left( \int_{B} \P_{Y|X=x}(dy) \right) \P_X(dx) = \int_\R \P_{Y|X=x}(B) \P_X(dx)$$
* Dans le cas où $X$ est discrète (à valeurs dans $I$ dénombrable), on retrouve une expression de la formule des probabilités totales et composées :
$$\P_Y(B) = \P(Y\in B) = \sum_{x \in I} \P(Y \in B | X = x)\P(X=x)$$
* Dans le cas où le couple $(X,Y)$ admet une densité, puisqu'on a $f_{X,Y}(x,y) = f_{Y | X=x}(y)f_X(x)$, on obtient l'expression suivante pour la densité marginale :
$$f_Y(y) = \int_\R f_{X,Y}(x,y)dx = \int_\R f_{Y | X=x}(y)f_X(x) dx.$$
 On a en particulier la *formule de Bayes pour les densités* : pour tout $x$ tel que $f_X(x) > 0$ et tout $y$ tel que $f_Y(y) > 0$ :
    $$ f_{X|Y=y}(x) = \frac{f_{X,Y}(x,y)}{f_Y(y)} = \frac{f_{Y|X=x}(y)f_X(x)}{f_Y(y)} .$$


### Exemple {.example}
Poursuivons [l'exemple vu ci-dessus](#ex1). On rappelle qu'on a déjà identifié la loi marginale de $X$ ainsi que la loi conditionnelle de $Y$ sachant $X=n$ pour $n\in\N$ que l'on rappelle ici :
$$\P(X=n) = (1-\alpha)\alpha^n,\,n\in\N \text{ et }\forall  B \in \B(\R), \, \P_{Y|X=x}(B) = \int_{B \cap \R_+^\star} e^{-t}\frac{t^n}{n!}dt$$
On peut en déduire la loi marginale de $Y$ en utilisant la [proposition ci-dessus](#balcond) et le théorème de convergence monotone :
\begin{align*}
\P_Y(B)  &= \sum_{n \in \N} (1-\alpha)\alpha^n \int_{B \cap \R_+^\star} e^{-t}\frac{t^n}{n!} dt\\
         &= (1-\alpha) \int_{B \cap \R_+^\star} e^{-t} \sum_{n \in \N} \frac{(\alpha t)^n}{n!} dt \\
         &= \int_B 1_{\R_+}(t)(1-\alpha) e^{-(1-\alpha)t} dt,
\end{align*}
de sorte que $Y$ suit une loi exponentielle de paramètre $(1-\alpha)$.

En inversant les rôles, on va pouvoir identifier la loi de $X$ sachant $Y \in B$ en notant que
\begin{align*}
\P_{X,Y}(\{n\} \times B) &= \P_X(\{n\})\P_{Y|X=n}(B) \\
                         &= \int_B \frac{(\alpha t)^n}{n!} e^{-\alpha t} \P_Y(dt)\\
                         &= \int_B \P_{X = n | Y =t}(\{n\}) \P_Y(dt)
\end{align*}
où l'on reconnaît que $\P_{X =n | Y =t}(\{n\}) = \frac{(\alpha t)^n}{n!} e^{-\alpha t}$, c'est-à-dire que $X$ sachant $Y = t$ suit une loi de Poisson de paramètre $\alpha t$ pour $\P_Y$-presque tout $t$.

En utilisant, le [théorème précédent](#fubinicond), on obtient une nouvelle caractérisation de l'indépendance de deux variables aléatoires faisant intervenir les lois conditionnelles.

### Proposition (critère d'indépendance) {.proposition}

1. $X$ et $Y$ sont indépendantes si et seulement si, pour $\P_X$-presque tout $x$, $\P_{Y |X = x}$ ne dépend pas de $x$ et dans ce cas, on a $\P_{Y |X = x} = \P_Y$, c'est-à-dire que la loi conditionnelle est identique à la loi marginale.

2. Dans le cas où $(X,Y)$ admet une densité, $X$ et $Y$ sont indépendantes si et seulement si la densité conditionnelle de $Y$ sachant $\{X = x\}$ ne dépend pas de $x$.

### Démonstration {.proof}

1. Si $X$ et $Y$ sont indépendantes, pour tous $B_1$, $B_2$ boréliens de $\R$, $\P_{X,Y} (B_1 \times B_2) = \P_X(B_1)\P_Y(B_2) = \int_{B_1}\P_Y(B_2)\P_X(dx) = \int_{B_2}\P_X(B_1) \P_Y(dy)$. Le résultat d'unicité du [théorème ci-dessus](#fubinicond) (à une égalité $\P_X$-presque sûre près), nous indique alors que $\P_{Y|X=x}(B_2) = \P_Y(B_2)$.

   Inversement, si $\P_{Y |X = x} = \P_Y$, alors $\P_{X,Y} (B_1 \times B_2) = \int_{B_1}\P_{Y|X=x}(B_2)\P_X(dx) = \int_{B_1}\P_Y(B_2)\P_X(dx) = \P_X(B_1)\P_Y(B_2)$.

2. Si $X$ et $Y$ sont indépendantes, $f_{X,Y} (x,y) = f_X(x) f_Y(y)$, d'où $f_{Y|X=x}(y) = f_Y(y)$.

   Inversement, si $f_{Y|X=x}(y) = f_Y(y)$ alors $f_{X,Y}(x,y) = f_{Y|X=x}(y) f_X(x) = f_Y(y)f_X(x)$ et $X$ et $Y$ sont indépendantes.

### {.anonymous}

# Espérance conditionnelle

Puisque $\P_{Y|X=x}$ est la loi d'une variable aléatoire, on peut définir l'espérance qui lui est associée et introduire la notion d'espérance conditionnelle dans le cas où $Y$ est intégrable.

### Définition {.definition #defespcond}
Soit $Y$ une variable aléatoire intégrable.

 1. L'*espérance conditionnelle de $Y$ sachant $\{X=x\}$* est définie par 
    $$\Esp(Y|X=x) = \int_\R y \P_{Y|X=x} (dy).$$
 2. L'*espérance conditionnelle de $Y$ sachant $X$* est la **variable aléatoire** définie par :
    $$\Esp(Y|X) = \psi(X), \text{ avec } \psi(x) = \Esp(Y|X=x).$$

### Remarques {.remark}

 1. $\psi(x)$ n'est définie que pour $x \notin B$, avec $\P(X\in B) = 0$. Par conséquent, la [définition](#defespcond) définit bien l'espérance conditionnelle $\psi(X) = \Esp(Y|X)$ $\P_X$-presque partout, autrement dit avec probabilité 1, ou encore presque sûrement.
 2. $\Esp(\Esp(|Y||X)) = \Esp(|Y|)$ comme conséquence directe du [théorème de Fubini conditionnel](#fubinicond). L'espérance conditionnelle de $Y$ sachant $X$ est bien définie dès que $Y$ est intégrable. 
 3. Lorsque $(X,Y)$ admet une densité, l'espérance conditionnelle de $Y$ sachant $\{X=x\}$ s'écrit
 $$\Esp(Y|X=x) = \int_\R y f_{Y|X=x}(y) dy.$$

On peut étendre cette définition aux variables de la forme $g(X,Y)$.

### Définition {.definition #defespcondh}
Soit $Y$ une variable aléatoire et $g$ une fonction mesurable positive ou $\P_{X,Y}$-intégrable sur $\R^2$.

 1. L'*espérance conditionnelle de $g(X,Y)$ sachant $\{X=x\}$* est définie par 
    $$\Esp(g(X,Y)|X=x) = \int_\R g(x,y) f_{Y|X=x} (y) dy.$$
 2. L'*espérance conditionnelle de $g(X,Y)$ sachant $X$* est la **variable aléatoire** définie par :
    $$\Esp(g(X,Y)|X) = \psi(X), \text{ avec } \psi(x) = \Esp(g(X,Y)|X=x).$$


### Théorème {.theorem} 
Si $Y$ est intégrable, alors $\psi(X) = \Esp(Y | X)$ est intégrable, et 
$$\Esp( \psi(X)) = E( Y ) .$$

### Démonstration {.proof} 
C'est une conséquence directe du [théorème de Fubini conditionnel](#fubinicond).

### {.anonyomous}
Ce résultat permet de calculer $\Esp( Y )$ en conditionnant par une variable auxiliaire $X$ :
$$ \Esp( Y ) = \int_\R \Esp(Y | X = x) \P_X(dx) dx$$

Il généralise la [formule des probabilités totales](Probabilité I.pdf #formprobatot), qui correspond ici à $Y = 1_A$ , et $B_x = \{X = x\}$ où les $B_x$ forment cette fois une partition non dénombrable de $\R$. On l’écrit souvent sous la forme
$$ \Esp \left( \Esp(Y | X) \right) = \Esp( Y )$$
et on l'appelle la *formule de l'espérance totale*.

L’espérance conditionnelle étant définie comme l’espérance de la loi conditionnelle,
elle hérite des propriétés usuelles de l’espérance :
 
 1. si $Y$ et $Z$ sont intégrables, $\Esp (aY + bZ | X) = a \Esp (Y | X) + b \Esp(Z | X)$,
 2. $\Esp (Y | X) \geq 0$ si $Y \geq 0$,
 3. $\Esp (1 | X) = 1$.
De plus, si $g$ est mesurable positive ou $\P_X$-intégrable,
$$ \Esp (Y g(X) | X) = g(X) \Esp (Y | X) $$

est une généralisation de l’égalité 1. ci-dessus, au cas où $a = g(X)$, qui doit être considéré “comme une constante” dans le calcul de l’espérance conditionnelle sachant $X$ ($X$ est fixée comme une donnée connue a priori). En effet, on a alors $\Esp(g(x)Y|X=x) = g(x)\psi(x)$.


## Vecteurs Gaussiens à densité
Dans le cas des vecteurs gaussiens à densité, c'est-à-dire dont la matrice de covariance est définie positive, et donc inversible, le calcul des lois conditionnelles de certaines composantes par rapport aux autres est particulièrement aisé. On va voir en particulier que les lois conditionnelles ont le bon goût d'être elles-mêmes gaussiennes, ce qui explique (en partie) le succès de ces modèles dans les applications.

On considère un vecteur gaussien $X = (X_1,\ldots,X_n)$ à valeurs dans $\R^n$ d'espérance $m$ et de matrice de covariance $C$ définie positive. On a vu au chapitre 2 que la densité du vecteur $X$ s'écrit pour $x\in\R^d$ :
$$f_X(x) = \frac{1}{(2\pi)^{n/2}\sqrt{\det (C)}}\exp \left(-\frac{1}{2}(x-m)^t C^{-1}(x-m)\right)$$

Soit $1 \leq k \leq n$ un entier. On souhaite exprimer $f_{Y|Z=z}$, la densité conditionnelle de $Y = (X_1,\ldots,X_{k-1})$ sachant $Z = (X_k,\ldots,X_n) = (x_k,\ldots,x_n) = z$. On a vu que 
$$f_X = f_{Y|Z=z} f_Z,$$
où $f_Z$ est la densité marginale de $Z$. On cherche donc à décomposer $f_X$ de la sorte. On note $m = (m_Y,m_Z)$ et on remarque que $C$ peut se décomposer en blocs :
\begin{equation*}
C = \left(\begin{array}{cc} C_Y & C_{Y,Z} \\ C_{Z,Y} & C_Z \end{array}\right)
\end{equation*}
où $C_Y = \cov(Y,Y)$, $C_Z = \cov(Z,Z)$ et $C_{Y,Z} = \cov(Y,Z)$. Le *complément de Schur*[^mckbk] du bloc $C_Y$ est la matrice 
$$CS_Y = C_Y - C_{Y,Z}C_Z^{-1}C_{Z,Y}$$
et permet d'exprimer l'inverse de $C$ comme :
\begin{equation*}
C^{-1} = \left(\begin{array}{cc} CS_Y^{-1} & -CS_Y^{-1}C_{Y,Z}C_Z^{-1} \\ -C_Z^{-1}C_{Z,Y}CS_Y^{-1}  & C_Z^{-1} + C_Z^{-1}C_{Z,Y}CS_Y^{-1}C_{Y,Z}C_Z^{-1} \end{array}\right)
\end{equation*}
On peut alors réarranger les termes de la forme quadratique dans $f_X$ et on obtient :
\begin{align*}
(x-m)^t C^{-1}(x-m) =& \left(y - (m_Y - C_{Y,Z}C_Z^{-1}(z-m_Z))\right)^t CS_Y^{-1}\left(y - (m_Y - C_{Y,Z}C_Z^{-1}(z-m_Z))\right)\\
 &+ (z-m_Z)^t C_Z^{-1}(z-m_Z)
\end{align*}
Pour la constante, on peut remarquer que :
$$ \det (C) = \det(CS_Y)\det(C_Z).$$
On en déduit ainsi que 
<!-- \begin{align*}
f_{Y|Z=z}(y) =& \frac{1}{(2\pi)^{n/2}\sqrt{\det (CS_Y)}}\\
&\exp \left(-\frac{1}{2}\left(y - \psi(z)\right)^t CS_Y^{-1}\left(y - \psi(z))\right)\right)
\end{align*} -->
$$f_{Y|Z=z}(y) = \frac{1}{(2\pi)^{k/2}\sqrt{\det (CS_Y)}}\exp \left(-\frac{1}{2}\left(y - \psi(z)\right)^t CS_Y^{-1}\left(y - \psi(z))\right)\right)$$


C'est-à-dire que la variable aléatoire $Y|Z=z$ est gaussienne d'espérance $m_{Y|Z=z} = \psi(z) = m_Y - C_{Y,Z}C_Z^{-1}(z-m_Z)$ et de matrice de covariance $CS_Y = C_Y - C_{Y,Z}C_Z^{-1}C_{Z,Y}$. Autrement dit, l'espérance conditionnelle de $Y$ sachant $Z$ est la variable aléatoire $\Esp(Y|Z) = \psi(Z) =(m_Y - C_{Y,Z}C_Z^{-1}(Z-m_Z))$. On notera que la covariance conditionnelle donnée par $CS_Y$ ne dépend pas de la valeur prise par $Z$.

[^mckbk]: voir par exemple l'excellent [matrix cookbook](https://www.ics.uci.edu/~welling/teaching/KernelsICS273B/MatrixCookBook.pdf).



# Régression et espérance conditionnelle des variables de carré intégrable
La régression est un ensemble de méthodes d'apprentissage statistique très utilisées pour analyser la relation d'une variable par rapport à une ou plusieurs autres. Ces méthodes visent notamment à décrire les liens de dépendance entre variables mais aussi de prédire au mieux la valeur d’une quantité non observée en fonction d'une ou plusieurs autres variables. On va en décrire ici le principe du point de vue probabiliste dans le cas particulier des variables de carré intégrable. On verra dans ce cadre, que l'on rencontre très fréquemment en pratique, une interprétation géométrique très éclairante de l'espérance conditionnelle.

## Régression linéaire
On considère deux variables aléatoires de carré intégrable dont on suppose connues les variances et la covariance. Nous souhaitons trouver la meilleure approximation de $Y$ par une fonction affine de $X$ de la forme $aX + b$, au sens des moindres carrés, c’est-à-dire qui minimise la quantité $\Esp((Y - (aX + b))^2)$. Il s’agit de déterminer les constantes $a$ et $b$ telles que $\Esp((Y - (aX + b))^2)$ soit minimale. Or, par linéarité,
$$\Esp((Y - (aX + b))^2) = \Esp(Y^2) -2a\Esp(XY) +a^2\Esp(X^2) +2ab\Esp(X) +b^2.$$
L'annulation de ses dérivées partielles en à $a$ et $b$ entraîne que les solutions sont

\begin{align*}
a & = \frac{\cov(X,Y)}{\V(X)} = \rho(X,Y)\frac{\sigma_Y}{\sigma_X} \\
b & = \Esp(Y)  - a \Esp(X)
\end{align*}

On vérifie aisément que ces valeurs donnent bien un minimum pour $\Esp((Y - (aX + b))^2)$ qui est convexe, et déterminent ainsi la meilleure approximation linéaire de $Y$ basée sur $X$ au sens de l'erreur quadratique moyenne.

Cette approximation linéaire vaut
$$ \Esp(Y) + \rho(X,Y)\frac{\sigma_Y}{\sigma_X} (X -\Esp(X))$$
et l'erreur quadratique moyenne vaut alors
\begin{align*}
\Esp\left(\left(Y - \Esp(Y) - \rho(X,Y)\frac{\sigma_Y}{\sigma_X} (X -\Esp(X))\right)^2\right) & = \sigma_Y^2 + \rho^2(X,Y)\sigma^2_Y - 2\rho^2(X,Y)\sigma^2_Y\\
                        & = \sigma^2_Y(1-\rho^2(X,Y)).
\end{align*}

On voit ainsi que cette erreur est proche de 0 lorsque $|\rho(X,Y)| \approx 1$ tandis qu'elle est proche de $\V(Y) = \sigma^2_Y$ lorsque $\rho(X,Y) \approx 0$. 


## Espace de Hilbert des variables aléatoires de carré intégrable

Dans le paragraphe précédent, on s'est intéressé à approximer linéairement une variable aléatoire $Y$ de carré intégrable par une autre variable $X$ également de carré intégrable.  On va montrer dans ce paragraphe que la meilleure approximation, au sens des l'erreur quadratique moyenne, de $Y$ par une fonction de $X$ est précisément donnée par $\Esp(Y|X)$. 


Exercices
===============================================================================

## Un exercice tout bête {.question #etb} 
Soient $X$ et $Y$ de densité jointe $f_{X,Y}(x,y)= \frac{1}{x}1_T (x,y)$ où $T$ est le triangle $T = \{0< y< x < 1\}$.

1. Calculer la densité marginale de $X$
2. Calculer la densité conditionnelle de $Y$ sachant $X=x$.
3. En déduire l'espérance conditionnelle de $Y$ sachant $X$.

## Mélanges de loi
mélanges de gaussienne, cf silvere-schmidt

## Variance et covariance totales

## Lois conjuguées
exemples utiles en bayésien : gauss-gauss, gauss-gamma,...

## Randomisation
exemple de somme aléatoire de v.a.r.

## Modèle graphique --- indépendance conditionnelle

-----------------------------------------------------------


Solutions
===============================================================================


## Un exercice tout bête {.answer #etb} 
La densité marginale de $X$ est donnée par $f_X(x) = \int f_{X,Y}(x,y) dy = 1_{]0,1[}(x)$ et pour $x \in ]0,1[$,
$$ f_{Y|X=x} (y) = \frac{1}{x} 1_{]0,x[}(y) $$
Ainsi $X$ est uniformément distribué sur $]0,1[$, et la loi de $Y$ sachant $X =x$ est uniforme sur $]0,x[$ pour $(0 < x < 1)$. Pour un tel $x$, l'espérance conditionnelle $\Esp(Y|X=x)$ vaut ainsi $x/2$ et nous obtenons $\Esp(Y|X) = \frac{X}{2}$.
