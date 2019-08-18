% Equations Différentielles I

<!-- LaTeX Macros -->
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}

\newcommand{\cS}{\mathcal{S}}
\newcommand{\cC}{\mathcal{C}}


Notations à définir/uniformiser

- $C(I, \R)$
- boule ouverte/fermée

Un peu d'histoire
=========================== 



Cadre de l'étude
============================

Soit $n\in \N^*$. 

### Equation différentielle de degré $p$  {.definition}
Soient $p\in\N^*$, $U$ ouvert de $\R\times (\R^n)^p$ et $f:\R\times (\R^n)^p \to \R^n$ une application continue sur $U$. Une application $x:I\to \R^n$ de classe $C^p$ sur un intervalle $I$ de $\R$ est dite *solution* de *l'équation différentielle d'ordre $p$*
$$
x^{(p)} = f(t,x,\dot{x},\ldots, x^{(p-1)})
$$
si pour tout $t\in I$,

- $(t,x(t),\dot{x}(t),\ldots, x^{(p-1)}(t)) \in U$

- $x^{(p)}(t) = f(t,x(t),\dot{x}(t),\ldots, x^{(p-1)}(t))$.

On dira que l'équation différentielle est *autonome* si l'application $f$ ne dépend pas de $t$, i.e., $f: (\R^n)^p \to \R^n$.


### Exemples {.exemple}
quelques systèmes physiques vus en prépa (RLC, masse ressort, hamiltonien)


### Réduction à l'ordre 1
Etant donnés $p\in\N^*$, $U$ un ouvert de $\R\times (\R^n)^p$ et $f:\R\times (\R^n)^p \to \R^n$ une application continue sur $U$, définissons l'application $\underline{f} : \R \times (\R^n)^p \to (\R^n)^p$ par
$$
\underline{f}(t,x_0,x_1,\ldots,x_{p-1}) = (x_1,x_2,\ldots,x_{p-1},f(t,x_0,\ldots,x_{p-1})) \ .
$$
Alors $x\in C^p(I,\R^n)$ est solution de l'équation différentielle d'ordre $p$ définie par $f$ si et seulement si $(x,\dot{x},\ldots,x^{(p-1)})\in C^1(I,(\R^n)^p)$ est solution de l'équation différentielle d'ordre 1
$$
\dot{\underline{x}} = \underline{f}(t,\underline{x}) \ .
$$

*Démonstration* : \hfill $\blacksquare$

Nous déduisons que résoudre une équation différentielle d'ordre $p$ est en fait équivalent à résoudre une équation différentielle d'ordre 1, quitte à considérer comme inconnue la suite des dérivées $(x,\dot{x},\ldots,x^{(p-1)})\in C^1(I,\R^{\underline{n}})$ avec $\underline{n}=np$, au lieu de seulement $x\in C^p(I,\R^n)$.  Dans la suite de ce cours nous nous restreignons donc à $p=1$.


### Problème de Cauchy {.definition #def_cauchy}
Soient $U$ un ouvert de $\R\times \R^n$, $(t_0,x_0)\in U$ et $f\in C(U,\R^n)$. Le *problème de Cauchy* fait référence au système
$$
\dot{x}=f(t,x) \quad , \quad x(t_0)=x_0 \ .
$$
On dira donc que $x\in C(I,\R^n)$ résout le problème de Cauchy défini par $f$ et $(t_0,x_0)$ sur l'intervalle $I\subseteq \R$ si

- $t_0\in I$ et $x(t_0)=x_0$

- pour tout $t\in I$, $(t,x(t)) \in U$ et $\dot{x}(t)=f(t,x(t))$

On notera alors $x\in S_f(t_0,x_0)$.

### Equation intégrale {.theorem #theo_eq_integrale}
Soient $U$ un ouvert de $\R\times \R^n$, $f\in C(U,\R^n)$, $I$ un intervalle de $\R$, $(t_0,x_0)\in U$ tel que $t_0\in I$, et $x\in C(I,\R^n)$ telle que $(t,x(t))\subset U$ pour tout $t\in I$. Alors, $x\in S_f(t_0,x_0)$ si et seulement si $x$ est solution de l'équation intégrale
$$
x(t) = x_0 + \int_{t_0}^t f(s,x(s))ds \qquad \forall t\in I \ .
$$

*Démonstration* : Supposons $x\in S_f(t_0,x_0)$. Alors $x\in C^1(I,\R^n)$, and pour tout $t\in I$,
$$
x_0 + \int_{t_0}^t f(s,x(s))ds = x(t_0)  + \int_{t_0}^t \dot{x}(s) ds = x(t) \ .
$$
Réciproquement, si $x$ vérifie l'équation intégrale, $x(t_0)=x_0$, et puisque $f$ est continue sur $U$, on a $x\in C^1(I,\R^n)$ et par dérivation, $\dot{x}(t)=f(t,x(t))$ pour tout $t\in I$.$\hfill\blacksquare$

### Classe plus générale de solutions {.remark}
Relaxation de la continuité de $f$ et de la notion de solution de manière à ce que cette intégrale existe + ref à calcul intégral


Etude du problème de Cauchy
================================

Existence de solutions locales
--------------------------------

Le théorème suivant assure l'existence locale de solutions au [problème de Cauchy](#def_cauchy) sous une simple hypothèse de continuité de $f$.

### Théorème de Peano-Arzelà {.theorem  #theo_peano}
Soient $U$ un ouvert de $\R\times \R^n$ et $f\in C(U,\R^n)$. Pour tout $(t_0,x_0)\in U$, il existe $\epsilon >0$ et $x\in C^1([t_0-\epsilon,t_0+\epsilon],\R^n)$ tels que $x\in S_f(t_0,x_0)$.

*Démonstration*: La démonstration de ce résultat est hors-programme car elle fait appel au théorème d'Ascoli(-Arzelà) qui sera abordé dans les notions avancées de Calcul Différentiel III. Seule la connaissance et compréhension du résultat est exigible. Pour les curieux, preuve en appendice? $\hfill\blacksquare$

### Solution maximale {.definition #def_sol_max}
Soient $U$ un ouvert de $\R\times \R^n$, $f\in C(U,\R^n)$. On dit que $x\in C^1(I,\R^n)$ est une solution *maximale* de l'équation différentielle 
$$
\dot{x}=f(t,x)
$$
si pour toute autre solution $y\in C^1(J,\R^n)$ telle que $I\subseteq J$ et $x_{|I}\equiv y_{|I}$, on a nécessairement $I=J$ et $x\equiv y$. En d'autres termes, elle n'est pas *prolongeable*.

### Exemple
Considérons le problème de Cauchy
$$
\dot{x}=-\sqrt{|x|} \qquad , \qquad (t_0,x_0)=(0,0)
$$ 
permettant de modéliser l'écoulement d'un fluide dans un réservoir, selon la loi de *Torricelli*.
La fonction $f:(t,x)\mapsto -\sqrt{|x|}$ est continue sur $U=\R\times \R$, donc on sait que ce problème de Cauchy admet au moins une solution. Mais l'on montrera en exercice qu'il existe une infinité de solutions maximales.


Unicité des solutions
-------------------------------

Nous avons vu dans la partie précédente que des solutions locales au problème de Cauchy existent toujours si $f$ est continue mais qu'elles ne sont pas nécessairement uniques. Le théorème suivant montre que l'unicité des solutions est garantie si $f$ est de classe $C^1$ par rapport à la variable $x$.

### Théorème de Cauchy-Lipschitz (ou de Picard-Lindelöf) {.theorem #theo_lips}
Soient $U$ un ouvert de $\R\times \R^n$ et $f\in C(U,\R^n)$ telle que sa dérivée partielle $(t,x)\mapsto \frac{\partial f}{\partial x}(t,x)$ existe et est continue sur $U$ (on dira par la suite pour simplifier que $f$ est de classe $C^1$ par rapport à $x$).
Alors pour tout $(t_0,x_0)\in U$, il existe une unique solution maximale $x:I\to\R^n$ dans $S_f(t_0,x_0)$. De plus,  l'intervalle $I$ est ouvert.

*Démonstration* Nous donnons ici le principe de la preuve qu'il est important de comprendre. La preuve complète est donnée en appendice? L'essentiel est en fait de montrer que sous l'hypothèse de régularité de $f$ par rapport à $x$, il existe une unique solution locale au problème de Cauchy. De là on peut ensuite déduire qu'elle se prolonge en une unique solution maximale unique. L'ouverture de son intervalle de définition vient du fait qu'elle pourrait sinon être de nouveau prolongée *au bord* de l'intervalle puisque $U$ est ouvert, ce qui contradirait sa maximalité. La partie cruciale est donc le résultat local suivant qui constitue en fait le théorème initial de Cauchy-Lipschitz (sa généralisation aux solutions globales étant plutôt dûe à [Picard et Lindelöf](#rem_approx_succ)).

**Théorème de Cauchy-Lipschitz local** Soient $U$ un ouvert de $\R\times \R^n$, $f\in C(U,\R^n)$ de classe $C^1$ par rapport à $x$, et $(t_0,x_0)\in U$. Soient $\tau>0$ et $r>0$ tels que 
$$
\cC:=\left[t_0-\tau,t_0+\tau \right]\times \overline{B}_{r}(x_0)\subset U \ .
$$
Pour tout $\tau_m\in \left[0,\tau \right]$ tel que $\tau_m  \max_{\cC} |f| \leq r$,
<!--- $$
f_m := \max_{\cC} f \quad , \quad \tau_m := \min\left\{\tau,\frac{r}{f_m} \right\}
$$--->
il existe une unique fonction $x\in S_f(t_0,x_0)$ définie sur $[t_0-\tau_m,t_0+\tau_m]$. 

*Démonstration* Tout d'abord, $\cC$ étant fermé et borné en dimension finie, $\cC$ est  compact et par continuité de $f$, $\max_\cC |f|$ existe bien.  Rappelons nous que $E:=C([t_0-\tau_m,t_0+\tau_m],\R^n)$ (ref?) est un espace de Banach pour la norme uniforme $|\cdot|_\infty$, et définissons  
$$
F = \{x\in E \: : \: x(\left[t_0-\tau_m,t_0+\tau_m \right])\subseteq \overline{B}_{r}(x_0) \} \ .
$$
On peut montrer que[^Fferme] $F$ est un sous-ensemble fermé de $E$. $F$ est donc complet (ref?)  (toujours pour la norme uniforme $|\cdot|_\infty$). 
Pour tout $x\in F$, par définition, $(s,x(s))\in \cC\subset U$ pour tout $s\in \left[t_0-\tau_m,t_0+\tau_m \right]$ ; on peut donc définir l'opérateur $\Gamma : F\to E$ par
$$
\Gamma(x)(t) = x_0+\int_{t_0}^t f(s,x(s))ds \qquad \forall t\in \left[ t_0-\tau_m,t_0+\tau_m \right] \ .
$$
En fait, d'après la [représentation intégrale des solutions](#theo_eq_integrale), on sait qu'une fonction $x\in F$ est solution du problème de Cauchy sur $\left[ t_0-\tau_m,t_0+\tau_m \right]$ si et seulement si elle vérifie
$$
\Gamma(x)=x
$$
c'est-à-dire $x$ est un point fixe de $\Gamma$. Par ailleurs, on peut prouver[^solutionF]  que pour tout $x\in S_f(t_0,x_0)$ définie sur $\left[t_0-\tau_m,t_0+\tau_m \right]$, $x$ est dans $F$: c'est donc un point fixe $x^*$ de $\Gamma$ sur $F$. L'idée de la preuve est donc de montrer que $\Gamma$ (ou une de ses itérées) est contractante pour utiliser le théorème de point fixe sur un espace de Banach et en déduire l'existence et l'unicité de ce point fixe (REF?).

D'abord, pour tout $x\in F$, pour tout $t\in \left[t_0-\tau_m,t_0+\tau_m \right]$,
$$
|\Gamma(x)(t)-x_0| \leq \left|\int_{t_0}^t |f(s,x(s))| ds \right| \leq \tau_m \max_{\cC} |f| \leq r
$$
de sorte que $\Gamma(x)\in F$, i.e. $\Gamma:F\to F$. Ensuite, pour tout $(x_a,x_b)\in  F\times F$, pour tout $t\in \left[t_0-\tau_m,t_0+\tau_m \right]$,
$$
|\Gamma(x_a)(t)-\Gamma(x_b)(t)|\leq \left|\int_{t_0}^t |f(s,x_a(s))-f(s,x_b(s))| ds \right| \ .
$$
Soit $k=\max_\cC \left|\frac{\partial f}{\partial x} \right|$ (bien défini car $\cC$ est compact et $\frac{\partial f}{\partial x}$ est continue par hypothèse). Alors l'application du théorème des accroissement finis (REF) nous donne
$$
|\Gamma(x_a)(t)-\Gamma(x_b)(t)|\leq  \left|\int_{t_0}^t k|x_a(s)-x_b(s)| ds \right| \leq |t-t_0| k |x_a-x_b|_{\infty} 
$$
et donc $|\Gamma(x_a)-\Gamma(x_b)|_\infty \leq \tau_m k |x_a-x_b|_{\infty}$.
A ce stade, sauf si $\tau_m k<1$, $\Gamma$ n'est pas contractante. Cependant, on peut montrer par récurrence que pour tout $p\in \N$, et pour tout $t\in \left[t_0-\tau_m,t_0+\tau_m \right]$,
$$
|\Gamma^p(x_a)(t)-\Gamma^p(x_b)(t)|_\infty \leq \frac{(|t-t_0| k)^p}{p!} |x_a-x_b|_{\infty}
$$
en notant $\Gamma^p = \underbrace{\Gamma \circ \Gamma \circ \ldots \circ \Gamma}_{p \text{ fois }}$.
Donc pour tout $p\in \N$, $|\Gamma^p(x_a)-\Gamma^p(x_b)|_\infty \leq \frac{(\tau_m k)^p}{p!} ||x_a-x_b|_{\infty}$. Il existe donc $m$ tel que $\Gamma^{m}$ est contractante. D'après le théorème de point fixe de Banach (REF), $\Gamma$ admet un unique point fixe $x^*$ dans $F$. 
$\hfill\blacksquare$





### Relâchement à $f$ Lipschitzienne {.remark #rem_f_lips}
La première preuve d'existence et unicité locale de solutions sous l'hypothèse que $f$ est de classe $C^1$ par rapport à $x$ est dûe à Augustin Louis Cauchy (1820) et repose sur l'utilisation du théorème d'accroissements finis[^accfinis_Cauchy]. Mais on remarque dans notre preuve qu'il suffirait qu'il existe $k>0$ tel que
$$
|f(t,x_a)-f(t,x_b)|\leq k |x_a-x_b| \qquad \forall t\in \left[t_0-\tau_m,t_0+\tau_m \right], \forall (x_a,x_b)\in \overline{B}_r(x_0) \ ,
$$
c'est-à-dire que la fonction $f$ soit *lipschitzienne* par rapport à $x$ au voisinage de $(t_0,x_0)$. Cette propriété fut introduite par le mathématicien allemand Rudolf Lipschitz  quelques années plus tard (1868) pour prouver le même résultat de façon indépendante: d'où le nom de *théorème de Cauchy-Lipschitz*. Notons que cette dernière hypothèse est plus faible que celle de Cauchy car elle impose seulement que $x\mapsto f(t,x)$ soit lipschitzienne au voisinage de $(t_0,x_0)$, au lieu de différentiable. Par exemple, $x\mapsto |x|$ est lipschitzienne (mais pas $C^1$) et $\dot{x}=|x|$ admet donc une unique solution maximale quel que soit la condition initiale.

### Approximations successives {.remarque #rem_approx_succ}
Mise à part quelques formes particulières de $f$, il est très rare de savoir résoudre explicitement une équation différentielle. Cependant, la preuve (dans sa forme moderne donnée plus haut) caractérise la solution comme le point fixe de l'opérateur $\Gamma$. Or, on sait (REF) que ce point fixe est la limite uniforme de la suite des itérées de $\Gamma$. En pratique, on peut donc s'approcher arbitrairement proche  de la solution   sur l'intervalle $\left[t_0-\tau_m,t_0+\tau_m \right]$ (au sens de la norme uniforme), en calculant la suite $x_{p+1} = \Gamma(x_p)$ définie par
$$
x_{p+1}(t) =  x_0+\int_{t_0}^t f(s,x_p(s))ds  ,
$$
en notant ici de manière abusive $x_0$ la fonction constante égale à $x_0$. 
Cette méthode de recherche de point fixe porte le nom d'*approximations successives* et est introduite pour la première fois par le mathématicien français Emile Picard à la fin du XIXème siècle grâce aux progrès de l'analyse fonctionnelle.  C'est finalement le mathématicien finlandais Ernst Lindelöf qui donne à la preuve sa forme moderne en utilisant en 1894 la théorie des espaces de Banach. Pour les anglophones, ce théorème s'appelle d'ailleurs le *théorème de Picard-Lindelöf*. 


### Exemples {.example #ex_lips}
- Une équation différentielle *linéaire*, c'est-à-dire pour laquelle il existe $a\in C(\R,\R^{n\times n})$ et $b\in C(\R,\R^n)$ telles que
$$
f(t,x) = a(t) x + b(t) \ ,
$$
admet une unique solution maximale quelque-soit sa condition initiale $(t_0,x_0)\in \R\times \R^n$.
- 


Solutions globales
--------------------------------

Dans la section précédente, nous avons vu que lorsque $f$ est $C^1$ par rapport à $x$, la solution maximale au problème de Cauchy (qui est alors unique) est définie sur un intervalle ouvert. Mais cet intervalle n'est pas nécessairement $\R$ entier même si $U=\R \times \R^n$ et $f$ est de classe $C^\infty$. On dit dans ce cas que la solution n'est pas *globale*. 

### Example d'explosion en temps fini
L'intervalle de définition de la solution maximale du problème de Cauchy n'est pas nécessairement $\R$, même si $U=\R \times \R^n$ et $f$ est de classe $C^\infty$. Par exemple, considérons le problème de Cauchy
$$
\dot{x} = x^2 \quad , \qquad (t_0,x_0)\in \R^2 \ .
$$
La fonction $f:(t,x)\mapsto x^2$ est de classe $C^1$ sur $U=\R^2$, donc il existe une unique solution maximale. On peut vérifier par le calcul que celle-ci s'écrit  
$$
x(t)=\frac{x_0}{1-x_0(t-t_0)} \quad , \quad I=\left(-\infty,t_0+\frac{1}{x_0}\right) \ .
$$
Cette solution diverge au temps $t_0+\frac{1}{x_0}$, on dit qu'elle *explose en temps fini*. FIGURE

En fait, le théorème suivant montre que pour toute solution maximale, la paire $(t,x(t))$  quitte nécessairement n'importe quel compact de $U$ au bout d'un certain temps. Dans le cas usuel où $U=\R\times \R^n$, ceci implique donc que toute solution maximale non globale, i.e. définie sur $\left[0,\overline{t}\right[$ avec $\overline{t}<+\infty$, explose en temps fini, c'est-à-dire
$$
\lim_{t\to \overline{t}} \|x(t)\|=+\infty \ ,
$$
Dans le cas où $U$ ne serait pas l'espace entier, une solution non globale pourrait aussi tendre en temps fini vers le "bord" de $U$ sans nécessairement diverger.

### Théorème des bouts {.theorem #theo_bouts}
Soient $U$ un ouvert de $\R\times \R^n$ et $f\in C(U,\R^n)$ de classe $C^1$ par rapport à $x$. Soient $(t_0,x_0)\in U$ et $x:\left]\underline{t},\overline{t}\right[\to \R^n$ la solution maximale au problème de Cauchy correspondant, avec $\underline{t}\in \left[-\infty,t_0\right[$ et $\overline{t}\in \left]t_0,+\infty\right]$.  Alors pour tout compact $K\subset U$, il existe $t_K^+ \in \left[t_0,\overline{t}\right[$ and $t_K^-\in \left]\underline{t},t_0 \right]$) tels que
$$
(t,x(t))\notin K \qquad \forall t\in \left[t_K^+,\overline{t} \right[ \cup  \left]\underline{t},t_K^- \right] 
$$

*Démonstration* : Voir en [annexe](#pr_theo_bouts).  $\hfill\blacksquare$

### Critère d'existence globale {.theorem #theo_exist_glob}
Soient $I$ un intervalle ouvert de $\R$, $U=I\times\R^n$, $(t_0,x_0)\in U$ et $f\in C(U,\R^n)$ de classe $C^1$ par rapport à $x$. S'il existe $a,b:I\to \R$ telles que  
$$
|f(t,x)|\leq a(t) |x| + b(t) \quad \forall (t,x)\in I\times \R^n \ ,
$$
alors la solution maximale au problème de Cauchy associé est défini sur $I$ entier. On dit alors que $f$ a une *croissance au plus affine*.

*Démonstration* : Voir en [annexe](#pr_theo_exist_glob).  $\hfill\blacksquare$


### Exemples
- Reprenons l'exemple d'une équation différentielle *linéaire*, c'est-à-dire pour laquelle il existe $A\in C(I,\R^{n\times n})$ et $b\in C(I,\R^n)$ telles que
$$
f(t,x) = A(t) x + b(t) \ .
$$
D'après le théorème précédent, quelque-soit sa condition initiale $(t_0,x_0)\in I\times\R^n$, sa solution maximale est définie sur $I$ entier. Dans le cas où $A$ est constant, on en a même une formule explicite (obtenue par la méthode de *variation de la constante*)
$$
x(t) = e^{A(t-t_0)}x_0 + \int_{t_0}^t e^{A(t-s)} b(s)ds \ ,
$$
où $e^{A(t-s)}$ est l'exponentielle de matrice définie par
$$
e^{A(t-s)}=\sum^{+\infty}_{p=0} \frac{A^p(t-s)^p}{p!} \ .
$$
Attention, cette formule  ne fonctionne que si $A$ est constant.

- Un autre cas important d'une croissance au plus affine est lorsque $f$ est globalement bornée en $x$. Par exemple, 
$$
f(t,x)=c(t)\arctan(x) \qquad \text{ ou } \qquad 
f(t,x)=\frac{c(t)}{1+x^2}
$$
engendrent des problèmes de Cauchy aux solutions uniques et globales.

<!--- Bien sûr, la fonction $f:(t,x)\mapsto x^2$ ne satisfait pas la croissance au plus affine et [on a vu](#ex_lips) que les solutions associées explosent en temps fini. Par contre, si l'on prend $f(t,x)=-x|x|$ ou $f(t,x)=-x^3$ qui ne satisfont pas non plus cette condition, on peut montrer que les solutions maximales sont globales (et tendent vers 0). On en déduit donc que la croissance au plus affine est  suffisante mais pas nécessaire pour garantir la globalité des solutions.-->




Régularité et stabilité des solutions
==========================================

Depuis l'apparition de la mécanique Newtonienne au XVIIème sciècle, l'étude des équations différentielles a toujours été motivée par l'espoir de compréhension et la prédiction du comportement futur de systèmes physiques.
En particulier, une question ayant taraudé et divisé les scientifiques au cours des siècles est celle de la stabilité du système à trois corps (Terre-Lune-Soleil), ou plus généralement du système solaire.  Devant les avancées en mécanique céleste, Pierre-Simon Laplace écrit en 1814:

>Nous devons donc envisager l'état présent de l'univers comme l'effet de son état antérieur, et comme la cause de celui qui va suivre. Une intelligence qui pour un instant donné connaîtrait toutes les forces dont la nature est animée et la situation respective des êtres qui la composent, si d'ailleurs elle était assez vaste pour soumettre ses données à l'analyse, embrasserait dans la même formule les mouvements des plus grands corps de l'univers et ceux du plus léger atome : rien ne serait incertain pour elle, et l'avenir comme le passé serait présent à ses yeux.

Cette conviction *déterministe*, c'est-à-dire que les phénomènes physiques passés ou futurs sont entièrement déterminés par leur condition initiale, fut confirmée par le théorème de Cauchy-Lipschitz quelques années plus tard. Ce dernier suggère en effet que l'on peut prévoir l'évolution des systèmes physiques par la seule connaissance de leur condition initiale et de leur modèle physique. 

Cependant, à la fin du XIXème siècle, on se rend vite compte que la réalité est en fait toute autre:

- d'une part, la condition initiale et le modèle ne sont jamais parfaitement connus: quelle est alors la qualité de notre prédiction?  

- d'autre part, ne pouvant généralement pas calculer explicitement la solution, comment anticiper son comportement sur des temps longs, voire son comportement asymptotique?


Sensibilité aux conditions initiales et erreurs de modèle
--------------------------------------------------------

La première question fut soulevée par Henri Poincaré à la fin du XIXème siècle alors qu'il s'attelle à la question de la stabilité du système solaire. Il écrit:

>Si un cône repose sur sa pointe, nous savons bien qu'il va tomber, mais nous ne savons pas de quel côté ; il nous semble que le hasard seul va en décider. Si le cône était parfaitement symétrique, si son axe était parfaitement vertical, s'il n'était soumis à aucune autre force que la pesanteur, il ne tomberait pas du tout. Mais le moindre défaut de symétrie va le faire pencher légèrement d'un côté ou de l'autre, et dès qu'il penchera, si peu que ce soit, il tombera tout à fait de ce côté. Si même la symétrie est parfaite, une trépidation très légère, un souffle d'air pourra le faire incliner de quelques secondes d'arc ; ce sera assez pour déterminer sa chute et même le sens de sa chute qui sera celui de l'inclinaison initiale.

### Régularité en temps fini  {.theorem #theo_reg_CI}
Theo

## Exemples
- Considérons un système linéaire à paramètre et/ou condition initiale incertains
$$
\dot{x} = (p+\delta_p) x \qquad , \qquad x_0 = c +\delta_{c}
$$
Pour $\delta_p=0=\delta_c$, la solution est $x(t)=ce^{pt}$, et sinon $x_\delta(t)= (c+\delta_c)e^{(p+\delta_p)t}$. On a donc
$$
|x(t)-x_\delta(t)| = |c- (c+\delta_c)e^{\delta_p t}| e^{pt}
$$
A FINIR

### Chaos déterministe et exposant de Lyapunov {.remark #rem_chao}
Henri Poincaré continue:

> Une cause très petite, qui nous échappe, détermine un effet considérable que nous ne pouvons pas ne pas voir, et alors nous disons que cet effet est dû au hasard. Si nous connaissions exactement les lois de la nature et la situation de l'univers à l'instant initial, nous pourrions prédire exactement la situation de ce même univers à un instant ultérieur. Mais, lors même que les lois naturelles n'auraient plus de secret pour nous, nous ne pourrions connaître la situation qu'approximativement. Si cela nous permet de prévoir la situation ultérieure avec la même approximation, c'est tout ce qu'il nous faut, nous disons que le phénomène a été prévu, qu'il est régi par des lois ; mais il n'en est pas toujours ainsi, il peut arriver que de petites différences dans les conditions initiales en engendrent de très grandes dans les phénomènes finaux ; une petite erreur sur les premières produirait une erreur énorme sur les derniers. La prédiction devient impossible et nous avons le phénomène fortuit. 


## Exemple : l'attracteur de Lorenz


Propriétés asymptotiques
-----------------------------

### Point d'équilibre

### Stabilité, stabilité asymptotique

### Lyapunov

### Cas linéaire

### Cas du plan : théorème de Bendixon


Références
================================================================================

Exercices 
==============================================================================

### Non unicité de solutions
Fluide dans réservoir 
$\dot{x}==-k\sqrt(|x|)$

### Proie/prédateur
Cycle limite Bendixon

### Système linéaire


Annexes 
=========================================================================

### Preuve du théorème des bouts {.preuve #pr_theo_bouts}
Prouvons l'existence de $t_K^+$ (l'existence de $t_K^-$ se prouvant de la même façon). Pour cela, supposons le contraire c'est-à-dire qu'il existe un compact $K\subset U$ tel que
$$
 \forall t_K \in \left[t_0,\overline{t}\right[ \, , \, \exists t\in \left[t_K,\overline{t}\right[ \: : \: x(t)\in K
$$
En d'autres termes, on suppose que la solution revient de manière persistente dans $K$. Alors il existe une suite $(t_n)_{n\in \N}$ telle que 
$$
\overline{t}-\frac{1}{n}\leq  t_n < \overline{t} \quad \text{et} \quad (t_n,x(t_n))\in K \quad \forall n\in \N
$$
On a donc $\lim_{n\to+\infty} t_n = \overline{t}$, et par compacité de $K$, on peut extraire de $(t_n,(x(t_n))_{n\in \N}$ une sous-suite qui converge vers $(\overline{t},\overline{x})\in K$. Pour simplifier les notations, on suppose donc directement $\lim_{n\to+\infty} x(t_n) =\overline{x}$.

BESOIN de CL local pour avoir l'estimée du temps minimal d'existence de solution A compléter


### Preuve du théorème d'existence globale de solutions {.preuve #pr_theo_exist_glob}

<!-- Footnotes -->

[^Fferme]: 
Pour toute suite $(x_n)$ d'éléments de $F$ convergeant vers $x^*$, pour tout $t\in [t_0-\tau_m,t_0+\tau_m]$,
$$
|x_n(t)-x^*(t)|\leq |x_n-x^*|_{\infty} \quad \longrightarrow_{n\to \infty} 0
$$
donc la suite $(x_n(t))$ d'éléments du fermé $\overline{B}_{x_0}(r)$  converge dans $\R^n$ vers $x^*(t)$ qui est donc dans $\overline{B}_{x_0}(r)$. Ceci implique $x^*\in F$.

[^solutionF]:
Il suffit de montrer que $x([t_0-\tau_m,t_0+\tau_m])\subseteq \overline{B}_r(x_0)$. Supposons le contraire et sans perdre en généralité supposons que
$$
S := \{ t\in [t_0,t_0+\tau_m] \: : \: |x(t)-x_0|>r \} \neq \emptyset \ .
$$
Soit $t^*=\inf S$. Nécessairement $t_0 < t^* < t_0+\tau_m$. Donc par la [représentation intégrale](#theo_eq_integrale), 
$$
|x(t^*)-x_0|\leq (t^*-t_0) \max_{s\in [t_0,t^*]} f(s,x(s)) < \tau_m \max_\cC|f|< r \ .
$$
Par continuité de $x$, $|x(t)-x_0|\leq r$ pour un temps après $t^*$, ce qui contredit sa définition.

[^accfinis_Cauchy]
En l'absence d'outils d'analyse fonctionnelle à cette époque, la preuve de Cauchy consistait plutôt à discrétiser en temps l'intégrale de plus en plus finement et montrer la convergence vers une solution.