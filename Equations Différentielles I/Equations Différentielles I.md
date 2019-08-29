% Equations Différentielles I

<!-- LaTeX Macros -->
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\Rgeq}{\R_{\geq 0}}
\renewcommand{\C}{\mathbb{C}}

\newcommand{\cS}{\mathcal{S}}
\newcommand{\cC}{\mathcal{C}}

\newcommand{\inter}{\mathop{\rm int}\nolimits}

Notations à définir/uniformiser

- $C^k(I, \R)$
- boule ouverte/fermée
- interieur 

Un peu d'histoire
=========================== 



Cadre de l'étude
============================

Soit $n\in \N^*$. 

### Equation différentielle de degré $p$  {.definition}
Soient $p\in\N^*$, $U$ ouvert de $\R\times (\R^n)^p$ et $f:U \to \R^n$ une application continue sur $U$. Une application $x:I\to \R^n$ continue sur un intervalle $I\subseteq \R$ non réduit[^intI] à un point, est dite *solution (sur[^solsurI] $I$)* de *l'équation différentielle d'ordre $p$* 
$$
x^{(p)} = f(t,x,\dot{x},\ldots, x^{(p-1)})
$$
si $x$ est de classe $C^p$ sur $I$ et pour tout $t\in I$,

- $(t,x(t),\dot{x}(t),\ldots, x^{(p-1)}(t)) \in U$

- $x^{(p)}(t) = f(t,x(t),\dot{x}(t),\ldots, x^{(p-1)}(t))$.

On dira que l'équation différentielle est *autonome* si l'application $f$ ne dépend pas de $t$. Dans ce cas, on pourrait définir $U$ directement comme un ouvert de $(\R^n)^p$ et $f: U\subseteq(\R^n)^p \to \R^n$.


### Exemples {.exemple}
quelques systèmes physiques vus en prépa (RLC, masse ressort, hamiltonien)


### Réduction à l'ordre 1
Etant donnés $p\in\N^*$, $U$ un ouvert de $\R\times (\R^n)^p$ et $f\in C^0(U,\R^n)$, définissons l'application $\underline{f} \in C^0(U,\R^n)$ par
$$
\underline{f}(t,x_0,x_1,\ldots,x_{p-1}) = (x_1,x_2,\ldots,x_{p-1},f(t,x_0,\ldots,x_{p-1})) \ .
$$
Alors $x\in C^p(I,\R^n)$ est solution de l'équation différentielle d'ordre $p$ définie par $f$ si et seulement si $(x,\dot{x},\ldots,x^{(p-1)})$ est solution de l'équation différentielle d'ordre 1
$$
\dot{\underline{x}} = \underline{f}(t,\underline{x}) \ .
$$

*Démonstration* : \hfill $\blacksquare$

Nous déduisons que résoudre une équation différentielle d'ordre $p$ est en fait équivalent à résoudre une équation différentielle d'ordre 1, quitte à considérer comme inconnue la suite des dérivées $(x,\dot{x},\ldots,x^{(p-1)})\in C^1(I,\R^{\underline{n}})$ avec $\underline{n}=np$, au lieu de $x\in C^p(I,\R^n)$.  Dans la suite de ce cours nous nous restreignons donc à $p=1$.


### Problème de Cauchy (*Initial Value Problem*) {.definition #def_cauchy}
Soient $U$ un ouvert de $\R\times \R^n$, $(t_0,x_0)\in U$ et $f\in C(U,\R^n)$. Le *problème de Cauchy* fait référence au système
$$
\dot{x}=f(t,x) \quad , \quad x(t_0)=x_0 \ .
$$
On dira donc que $x:I\to \R^n$ est solution du problème de Cauchy défini par $f$ et $(t_0,x_0)$ (sur un intervalle $I$ non réduit à un point) si

- $t_0\in I$ et $x(t_0)=x_0$

- $x$ est solution de l'équation différentielle $\dot{x}=f(t,x)$ sur $I$.
<!-- pour tout $t\in I$, $(t,x(t)) \in U$ et $\dot{x}(t)=f(t,x(t))$ -->

On notera alors $x\in S_f(t_0,x_0)$.

### Représentation intégrale des solutions {.theorem #theo_eq_integrale}
Soient $U$ un ouvert de $\R\times \R^n$, $f\in C(U,\R^n)$, $I$ un intervalle de $\R$ d'intérieur non vide, $(t_0,x_0)\in U$ tel que $t_0\in I$, et $x\in C(I,\R^n)$ telle que $(t,x(t))\in U$ pour tout $t\in I$. Alors, $x\in S_f(t_0,x_0)$ si et seulement si $x$ est solution de l'équation intégrale
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
La fonction $f:(t,x)\mapsto -\sqrt{|x|}$ est continue sur $U=\R\times \R$, donc on sait que ce problème de Cauchy admet au moins une solution. En fait, on montrera en [exercice](#exo_Torricelli) qu'il existe une infinité de solutions maximales.


Unicité des solutions
-------------------------------

Nous avons vu dans la partie précédente que des solutions locales au problème de Cauchy existent toujours si $f$ est continue mais qu'elles ne sont pas nécessairement uniques. Le théorème suivant montre que l'unicité des solutions est garantie si $f$ est de classe $C^1$ par rapport à la variable $x$.

### Théorème de Cauchy-Lipschitz (ou de Picard-Lindelöf) {.theorem #theo_lips}
Soient $U$ un ouvert de $\R\times \R^n$ et $f\in C^0(U,\R^n)$ telle que sa dérivée partielle $(t,x)\mapsto \frac{\partial f}{\partial x}(t,x)$ existe et est continue sur $U$ (on dira que $f$ est de classe $C^1$ par rapport à $x$).
Alors pour tout $(t_0,x_0)\in U$, il existe une unique solution maximale $x:I\to\R^n$ dans $S_f(t_0,x_0)$. De plus,  l'intervalle $I$ est ouvert et contient un voisinage de $t_0$.

*Démonstration* Nous donnons ici le principe de la preuve qu'il est important de comprendre. La preuve complète est donnée en appendice? L'essentiel est en fait de montrer que sous l'hypothèse de régularité de $f$ par rapport à $x$, il existe une unique solution locale au problème de Cauchy. De là on peut ensuite déduire qu'elle se prolonge en une unique solution maximale unique. L'ouverture de son intervalle de définition vient du fait qu'elle pourrait sinon être de nouveau prolongée *au bord* de l'intervalle puisque $U$ est ouvert, ce qui contradirait sa maximalité. La partie cruciale est donc le résultat local suivant qui constitue en fait le théorème initial de Cauchy-Lipschitz (sa généralisation aux solutions globales étant plutôt dûe à [Picard et Lindelöf](#rem_approx_succ)).

**Théorème de Cauchy-Lipschitz local** Soient $U$ un ouvert de $\R\times \R^n$, $f\in C^0(U,\R^n)$ de classe $C^1$ par rapport à $x$, et $(t_0,x_0)\in U$. Soient $\tau>0$ et $r>0$ tels que 
$$
\cC:=\left[t_0-\tau,t_0+\tau \right]\times \overline{B}_{r}(x_0)\subset U \ .
$$
Pour tout $\tau_m\in \left[0,\tau \right]$ tel que $\tau_m  \max_{\cC} \|f\| \leq r$,
<!--- $$
f_m := \max_{\cC} f \quad , \quad \tau_m := \min\left\{\tau,\frac{r}{f_m} \right\}
$$--->
il existe une unique fonction $x\in S_f(t_0,x_0)$ définie sur $[t_0-\tau_m,t_0+\tau_m]$. 

*Démonstration* Tout d'abord, $\cC$ étant fermé et borné en dimension finie, $\cC$ est  compact et par continuité de $f$, $\max_\cC \|f\|$ existe bien.  Rappelons nous que $E:=C^0([t_0-\tau_m,t_0+\tau_m],\R^n)$ (ref?) est un espace de Banach pour la norme uniforme $\|\cdot\|_\infty$, et définissons  
$$
F = \{x\in E \: : \: x(\left[t_0-\tau_m,t_0+\tau_m \right])\subseteq \overline{B}_{r}(x_0) \} \ .
$$
On peut montrer que[^Fferme] $F$ est un sous-ensemble fermé de $E$. $F$ est donc complet (ref?)  (toujours pour la norme uniforme $\|\cdot\|_\infty$). 
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
\|\Gamma(x)(t)-x_0\| \leq \left|\int_{t_0}^t \|f(s,x(s))\| ds \right| \leq \tau_m \max_{\cC} \|f\| \leq r
$$
de sorte que $\Gamma(x)\in F$, i.e. $\Gamma:F\to F$. Ensuite, pour tout $(x_a,x_b)\in  F\times F$, pour tout $t\in \left[t_0-\tau_m,t_0+\tau_m \right]$,
$$
\|\Gamma(x_a)(t)-\Gamma(x_b)(t)\|\leq \left|\int_{t_0}^t \|f(s,x_a(s))-f(s,x_b(s))\| ds \right| \ .
$$
Soit $k=\max_\cC \left\|\frac{\partial f}{\partial x} \right\|$ (bien défini car $\cC$ est compact et $\frac{\partial f}{\partial x}$ est continue par hypothèse). Alors l'application du théorème des accroissement finis (REF) nous donne
$$
\|\Gamma(x_a)(t)-\Gamma(x_b)(t)\|\leq  \left|\int_{t_0}^t k\|x_a(s)-x_b(s)\| ds \right| \leq |t-t_0| k \|x_a-x_b\|_{\infty} 
$$
et donc $\|\Gamma(x_a)-\Gamma(x_b)\|_\infty \leq \tau_m k \|x_a-x_b\|_{\infty}$.
A ce stade, sauf si $\tau_m k<1$, $\Gamma$ n'est pas contractante. Cependant, on peut montrer par récurrence que pour tout $p\in \N$, et pour tout $t\in \left[t_0-\tau_m,t_0+\tau_m \right]$,
$$
\|\Gamma^p(x_a)(t)-\Gamma^p(x_b)(t)\|_\infty \leq \frac{(|t-t_0| k)^p}{p!} \|x_a-x_b\|_{\infty}
$$
en notant $\Gamma^p = \underbrace{\Gamma \circ \Gamma \circ \ldots \circ \Gamma}_{p \text{ fois }}$.
Donc pour tout $p\in \N$, $\|\Gamma^p(x_a)-\Gamma^p(x_b)\|_\infty \leq \frac{(\tau_m k)^p}{p!} \|x_a-x_b\|_{\infty}$. Il existe donc $m$ tel que $\Gamma^{m}$ est contractante. D'après le théorème de point fixe de Banach (REF), $\Gamma$ admet un unique point fixe $x^*$ dans $F$. 
$\hfill\blacksquare$





### Relâchement à $f$ Lipschitzienne {.remark #rem_f_lips}
La première preuve d'existence et unicité locale de solutions sous l'hypothèse que $f$ est de classe $C^1$ par rapport à $x$ est dûe à Augustin Louis Cauchy (1820) et repose sur l'utilisation du théorème d'accroissements finis[^accfinis_Cauchy]. Mais on remarque dans notre preuve qu'il suffirait qu'il existe $k>0$ tel que
$$
\|f(t,x_a)-f(t,x_b)\|\leq k \|x_a-x_b\| \qquad \forall t\in \left[t_0-\tau_m,t_0+\tau_m \right], \forall (x_a,x_b)\in \overline{B}_r(x_0) \ ,
$$
c'est-à-dire que la fonction $f$ soit *lipschitzienne* par rapport à $x$ au voisinage de $(t_0,x_0)$. Cette propriété fut introduite par le mathématicien allemand Rudolf Lipschitz  quelques années plus tard (1868) pour prouver le même résultat de façon indépendante: d'où le nom de *théorème de Cauchy-Lipschitz*. Notons que cette dernière hypothèse est plus faible que celle de Cauchy car elle impose seulement que $x\mapsto f(t,x)$ soit lipschitzienne au voisinage de $(t_0,x_0)$, au lieu de différentiable. Par exemple, $x\mapsto \|x\|$ est lipschitzienne (mais pas $C^1$) et $\dot{x}=\|x\|$ admet donc une unique solution maximale quel que soit la condition initiale.

### Approximations successives {.remarque #rem_approx_succ}
Mise à part quelques formes particulières de $f$, il est très rare de savoir résoudre explicitement une équation différentielle. Cependant, la preuve (dans sa forme moderne donnée plus haut) caractérise la solution comme le point fixe de l'opérateur $\Gamma$. Or, on sait (REF) que ce point fixe est la limite uniforme de la suite des itérées de $\Gamma$. En pratique, on peut donc s'approcher arbitrairement proche  de la solution   sur l'intervalle $\left[t_0-\tau_m,t_0+\tau_m \right]$ (au sens de la norme uniforme), en calculant la suite $x_{p+1} = \Gamma(x_p)$ définie par
$$
x_{p+1}(t) =  x_0+\int_{t_0}^t f(s,x_p(s))ds  ,
$$
en notant ici de manière abusive $x_0$ la fonction constante égale à $x_0$. 
Cette méthode de recherche de point fixe porte le nom d'*approximations successives* et est introduite pour la première fois par le mathématicien français Emile Picard à la fin du XIXème siècle grâce aux progrès de l'analyse fonctionnelle.  C'est finalement le mathématicien finlandais Ernst Lindelöf qui donne à la preuve sa forme moderne en utilisant en 1894 la théorie des espaces de Banach. Pour les anglophones, ce théorème s'appelle d'ailleurs le *théorème de Picard-Lindelöf*. 


### Exemples {.example #ex_lips}
- Une équation différentielle *linéaire*, c'est-à-dire pour laquelle il existe $a\in C^0(\R,\R^{n\times n})$ et $b\in C^0(\R,\R^n)$ telles que
$$
f(t,x) = a(t) x + b(t) \ ,
$$
admet une unique solution maximale quelque-soit sa condition initiale $(t_0,x_0)\in \R\times \R^n$.
- 


Solutions globales
--------------------------------

Dans la section précédente, nous avons vu que lorsque $f$ est $C^1$ par rapport à $x$, la solution maximale au problème de Cauchy (qui est alors unique) est définie sur un intervalle ouvert. Mais cet intervalle n'est pas nécessairement $\R$ entier même si $U=\R \times \R^n$ et $f$ est de classe $C^\infty$. On dit dans ce cas que la solution n'est pas *globale*. 

### Example d'explosion en temps fini
Par exemple, considérons le problème de Cauchy
$$
\dot{x} = x^2 \quad , \qquad (t_0,x_0)\in \R^2 \ .
$$
La fonction $f:(t,x)\mapsto x^2$ est de classe $C^1$ sur $U=\R^2$, donc il existe une unique solution maximale. On peut vérifier par le calcul que celle-ci s'écrit  
$$
x(t)=\frac{x_0}{1-x_0(t-t_0)} \quad , \quad I=\left(-\infty,t_0+\frac{1}{x_0}\right) \ .
$$
Cette solution diverge au temps $t_0+\frac{1}{x_0}$, on dit qu'elle *explose en temps fini*. 

![Solutions à $\dot{x} = x^2$ pour $t_0=0$ et différentes valeurs de $x_0$](images/explosion_temps_fini.py){#fig_explo_temps_fini}

En fait, le théorème suivant montre que pour toute solution maximale, la paire $(t,x(t))$  quitte nécessairement n'importe quel compact de $U$ au bout d'un certain temps. Dans le cas usuel où $U=\R\times \R^n$, ceci implique donc que toute solution maximale non globale, i.e. définie sur $\left[0,\overline{t}\right[$ avec $\overline{t}<+\infty$, explose en temps fini, c'est-à-dire
$$
\lim_{t\to \overline{t}} \|x(t)\|=+\infty \ ,
$$
Dans le cas où $U$ ne serait pas l'espace entier, une solution non globale pourrait aussi tendre en temps fini vers le "bord" de $U$ sans nécessairement diverger.

### Théorème des bouts {.theorem #theo_bouts}
Soient $U$ un ouvert de $\R\times \R^n$ et $f\in C^0(U,\R^n)$ de classe $C^1$ par rapport à $x$. Soient $(t_0,x_0)\in U$ et $x:\left]\underline{t},\overline{t}\right[\to \R^n$ la solution maximale au problème de Cauchy correspondant, avec $\underline{t}\in \left[-\infty,t_0\right[$ et $\overline{t}\in \left]t_0,+\infty\right]$.  Alors pour tout compact $K\subset U$, il existe $t_K^+ \in \left[t_0,\overline{t}\right[$ and $t_K^-\in \left]\underline{t},t_0 \right]$) tels que
$$
(t,x(t))\notin K \qquad \forall t\in \left[t_K^+,\overline{t} \right[ \cup  \left]\underline{t},t_K^- \right] 
$$

*Démonstration* : Voir en [annexe](#pr_theo_bouts).  $\hfill\blacksquare$

### Critère d'existence globale {.theorem #theo_exist_glob}
Soient $I$ un intervalle ouvert de $\R$, $U=I\times\R^n$, $(t_0,x_0)\in U$ et $f\in C^0(U,\R^n)$. S'il existe $a,b:I\to \R$ telles que  
$$
\|f(t,x)\|\leq a(t) \|x\| + b(t) \quad \forall (t,x)\in I\times \R^n \ ,
$$
alors toute[^uniCritExGlob] solution maximale au problème de Cauchy associé est définie sur $I$ entier. On dit alors que $f$ a une *croissance au plus affine*.

*Démonstration* : Prouvé dans l'exercice [*Autour du Lemme de Grönwall*](#exo_gronwall).  $\hfill\blacksquare$


### Exemples
- Reprenons l'exemple d'une équation différentielle *linéaire*, c'est-à-dire pour laquelle il existe $A\in C^0(I,\R^{n\times n})$ et $b\in C^0(I,\R^n)$ telles que
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

Depuis l'apparition de la mécanique Newtonienne au XVIIème sciècle, l'étude des équations différentielles a toujours été motivée par l'espoir de compréhension et de prédiction du comportement futur ou passé de systèmes physiques.
En particulier, une question ayant taraudé et divisé les scientifiques au cours des siècles est celle de la stabilité du système à trois corps (Terre-Lune-Soleil), ou plus généralement du système solaire.  Enchanté devant les avancées de la mécanique céleste, Pierre-Simon Laplace écrit en 1814:

>Nous devons donc envisager l'état présent de l'univers comme l'effet de son état antérieur, et comme la cause de celui qui va suivre. Une intelligence qui pour un instant donné connaîtrait toutes les forces dont la nature est animée et la situation respective des êtres qui la composent, si d'ailleurs elle était assez vaste pour soumettre ses données à l'analyse, embrasserait dans la même formule les mouvements des plus grands corps de l'univers et ceux du plus léger atome : rien ne serait incertain pour elle, et l'avenir comme le passé serait présent à ses yeux.

Cette conviction *déterministe*, c'est-à-dire que les phénomènes physiques passés ou futurs sont entièrement déterminés par leur condition initiale, fut confirmée par le théorème de Cauchy-Lipschitz quelques années plus tard. Ce dernier suggère en effet que l'on peut prévoir l'évolution des systèmes physiques par la seule connaissance de leur condition initiale et de leur modèle physique. 

Cependant, à la fin du XIXème siècle, on se rend vite compte que la réalité est en fait toute autre:

- d'une part, la condition initiale et le modèle ne sont jamais parfaitement connus: quelle est alors la qualité de notre prédiction?  

- d'autre part, ne pouvant généralement pas calculer explicitement la solution, comment anticiper son comportement sur des temps longs, voire son comportement asymptotique?


Sensibilité aux conditions initiales et erreurs de modèle
--------------------------------------------------------

La première question fut soulevée par Henri Poincaré à la fin du XIXème siècle alors qu'il s'attelle à la question de la stabilité du système solaire. Il écrit:

>Si un cône repose sur sa pointe, nous savons bien qu'il va tomber, mais nous ne savons pas de quel côté [...]. Si le cône était parfaitement symétrique, si son axe était parfaitement vertical, s'il n'était soumis à aucune autre force que la pesanteur, il ne tomberait pas du tout. Mais le moindre défaut de symétrie va le faire pencher légèrement d'un côté ou de l'autre, et dès qu'il penchera, si peu que ce soit, il tombera tout à fait de ce côté. Si même la symétrie est parfaite, une trépidation très légère, un souffle d'air pourra le faire incliner de quelques secondes d'arc [...]. 

Le théorème suivant nous montre que pour un horizon de temps fini donné, on peut obtenir une solution arbitrairement précise si le système est initialisé suffisamment précisément et si les perturbations (ou erreurs de modèle) sont suffisamment faibles. En d'autres termes, la solution est *régulière* par rapport aux perturbations en temps fini. Ceci est crucial en physique puisque l'on ne peut jamais tout modéliser parfaitement.

### Régularité en temps fini  {.theorem #theo_reg_CI}
Soient $U$ un ouvert de $\R\times \R^n$, $f\in C^0(U,\R^n)$ de classe $C^1$ par rapport à $x$, $(t_0,x_0)\in U$, et $x:I\to\R^n$ la solution maximale dans $S_f(t_0,x_0)$. Pour tout $\overline{t}$ tel que $[t_0,\overline{t}]\subset I$, il existe $\delta_m>0$ et $\lambda\in \R$ tels que pour $\delta\in \R^n$ tel que $|\delta|\leq \delta_m$, la solution maximale $x_\delta$ dans $S_f(t_0,x_0+\delta)$ est définie sur $[t_0,\overline{t}]$ et vérifie
$$
|x(t)-x_{\delta}(t)| \leq e^{\lambda (t-t_0)} |\delta| \qquad \forall t\in [t_0,\overline{t}] \ .
$$
On dit alors que la solution du problème de Cauchy est continue par rapport à la condition initiale à horizon de temps fini : plus l'erreur de condition initiale $\delta$ est petite, plus l'erreur sur la trajectoire à horizon $\overline{t}$ est petite. Attention, l'hypothèse ``$C^1$ par rapport à $x$'' est importante encore ici, comme illustré dans l'exercice *[Ecoulement dans un réservoir](#exo_Torricelli)*.

*Démonstration* Prouvé dans l'exercice [*Autour du Lemme de Grönwall*](#exo_gronwall) \hfill $\blacksquare$

### Exemples
- Si $\lambda<0$, l'erreur commise sur la condition initiale disparait au cours du temps dans les solutions : on dit qu'elles ``oublient'' leur condition initiales et que le système est *contractant*. 

- On peut aussi déduire de ce résultat la continuité des solutions par rapport à des paramètres $p$ intervenant dans la fonction $f$. En effet, il suffit de considérer le système étendu
\begin{align*}
\dot{y} &= f(t,y,p)\\
\dot{p} &= 0
\end{align*}
pour lequel l'incertitude de paramètre se ramène à une incertitude de condition initiale.

- Considérons un système linéaire à paramètre et/ou condition initiale incertains
$$
\dot{x} = (a+\delta_a) x \qquad , \qquad x_0 = c +\delta_{c}
$$
Pour $\delta_a=0=\delta_c$, la solution est $x(t)=ce^{at}$, et sinon 
$$
x_\delta(t)= (c+\delta_c)e^{(a+\delta_a)t} \ .
$$ 
On a donc pour tout $t$,
$$
\|x(t)-x_\delta(t)\| = \|c- (c+\delta_c)e^{\delta_a t}\| e^{at} \leq \left(|\delta_c|e^{\delta_a t} + |1-e^{\delta_a t}| |c| \right) e^{at} 
$$
et pour tout $\overline{t}>0$ et $|\delta_a| \leq \frac{1}{\overline{t}}$
$$
\sup_{t\in [0,\overline{t}] } \|x(t)-x_\delta(t)\| \leq \left( |\delta_c|e^{\delta_a\overline{t}} + |\delta_a|  |c| \overline{t}\right) e^{a\overline{t}}
$$
qui peut être rendu aussi faible que voulu si $\delta_a$ et $\delta_c$ sont suffisamment petits. On voit bien ici que cette différence est bornée en temps fini, mais pas forcément aymptotiquement en particulier si $a>0$.

- L'outil [Fibre](https://portsmouth.github.io/fibre/)[^linkFibre] permet d'observer en dimension 3 cette continuité des solutions par rapport aux conditions initiales : à "Integration Time" fixé, plus on réduit la boîte de condition initiales, plus les solutions restent proches. Par contre, lorsqu'on augmente le "Integration Time" les solutions s'écartent.

### Chaos déterministe et exposant de Lyapunov {.remark #rem_chao}
Même si la continuité des solutions par rapport aux paramètres et conditions initiales est une bonne nouvelle qui donne espoir de pouvoir simuler et prédire des systèmes physiques, elle est malheureusement parfois insuffisante. 
Henri Poincaré continue:

<!-- Une cause très petite, qui nous échappe, détermine un effet considérable que nous ne pouvons pas ne pas voir, et alors nous disons que cet effet est dû au hasard. -->
> Si nous connaissions exactement les lois de la nature et la situation de l'univers à l'instant initial, nous pourrions prédire exactement la situation de ce même univers à un instant ultérieur. Mais, lors même que les lois naturelles n'auraient plus de secret pour nous, nous ne pourrions connaître la situation qu'approximativement. Si cela nous permet de prévoir la situation ultérieure avec la même approximation, c'est tout ce qu'il nous faut, nous disons que le phénomène a été prévu, qu'il est régi par des lois ; mais il n'en est pas toujours ainsi, il peut arriver que de petites différences dans les conditions initiales en engendrent de très grandes dans les phénomènes finaux ; une petite erreur sur les premières produirait une erreur énorme sur les derniers. La prédiction devient impossible et nous avons le phénomène fortuit. 

En fait, A FINIR + insister sur determinisme + anecdote poincaré, fin de l'espoir de Laplace
chaos que pour borné

### Exemples 

- 1963 : l'attracteur de Lorenz, météo

- 1992 : Sussman\& Wisdom système solaire chaotique avec horizon de Lyapunov 200 million d'années

- electricité, pendule forcé


Propriétés asymptotiques
-----------------------------

Dans la section précédente nous avons répondu à la première question qui était la sensibilité des solutions aux erreurs de condition initiale et de modèle. Mais cette étude était en temps fini et nous nous intéressons maintenant à la seconde question qui est le comportement asymptotique des solutions. Nous voulons des critères sur la fonction $f$ qui nous permettent de prédire ce comportement: est-ce qu'il diverge ? est-ce qu'il tend vers un point en particulier ? vers un cycle limite ?

Dans la suite, pour simplifier, nous étudions les équations différentielles dites *autonomes*, c'est-à-dire dont la fonction $f$ est indépendente du temps. On se donne donc un ouvert $\Omega$ de $\R^n$ et une fonction continue $f:\Omega\to \R^n$. Dans ce cas, on prend par défaut $t_0=0$. Puisque l'on souhaite étudir plus particulièrement le comportement *asymptotique* des solutions de $\dot{x}=f(x)$, on se restreint aux solutions *complètes*, c'est-à-dire définies sur $\Rgeq = [0,+\infty)$.

### Point d'équilibre
On appelle *point d'équilibre* un point $a\in \R^n$ tel que
$$
f(a) = 0  \ .
$$
En d'autres termes, la fonction constante $x\equiv a$ est solution.

### Stabilité, stabilité asymptotique
Un point d'équilibre $a$ est dit:

- *stable* si l'*on peut rester arbitrairement proche de $a$ quitte à initialiser les solutions suffisamment proche de $a$*, c'est-à-dire pour tout $\varepsilon >0$, il existe $\eta>0$ tel que toute solution $x: \Rgeq\to \R$ vérifie
$$
|x(0)-a|\leq \eta \qquad \Longrightarrow \qquad |x(t)-a|\leq \varepsilon \quad \forall t\in I \ .
$$

- *instable* s'il n'est pas stable.

- *localement attractif* si *toutes les solutions initialisées suffisamment proche de $a$ convergent vers $a$*, c'est-à-dire s'il existe $\eta>0$ tel que toute solution $x: \Rgeq\to \R$ vérifie
$$
|x(0)-a|\leq \eta \qquad \Longrightarrow \qquad \lim_{t\to+\infty} x(t)=a \ .
$$

- *globalement attractif* si *toutes les solutions convergent vers $a$*.

- *localement (resp. globalement) asymptotiquement stable* s'il est à la fois stable et localement (resp. globalement) attractif. 


### Exemples


### Caractérisation par Lyapunov


### Cas d'un système linéaire
Soit $A\in \R^{n\times n}$. Le point d'équilibre 0 est  asymptotiquement stable pour le système
$$
\dot{x} = Ax
$$
si et seulement si les valeurs propres de $A$ sont toutes à partie réelle strictement négative.

*Démonstration* La notion d'*asymptotiquement stable* contient deux propriétés : la stabilité et l'attractivité. On montrera en [exercice](#exo_attrac_stab) que pour un système linéaire, la stabilité asymptotique est équivalente à l'attractivité, c'est-à-dire que la stabilité vient gratuitement avec l'attractivité. C'est une propriété propre aux systèmes linéaires. Il suffit donc de trouver un critère caractérisant l'attrictivité de 0. On a vu que les solutions s'écrivent
$$
x(t)= e^{At} x_0 \ .
$$
Si $A$ était diagonale (réelle), on aurait $x_i(t)=e^{\lambda_i t}x_{0,i}$, où $\lambda_i$ sont les valeurs propres et l'on voit bien que la convergence des solutions vers 0 est équivalente à avoir $\lambda_i<0$. Maintenant, si $A$ est diagonalisable, i.e., il existe $P\in \R^{n\times n}$ telle que $P^{-1} A P$ est diagonale, on a $P^{-1} x(t) P =  e^{P^{-1} A P t} P^{-1} x_0 P$, et reproduisant le même argument, $P^{-1} x P$ (et donc $x$) converge vers 0 si et seulement si les entrées diagonales de $P^{-1} A P$, qui sont les valeurs propres de $A$, sont à partie réelle strictement négative. Ceci dit toute matrice $A$ n'est pas diagonalisable. Par contre, toute matrice est triangularisable. 
\hfill $\blacksquare$

Attention ce critère n'est valable que pour $A$ constant. Le fait que $A\in C^0(I,\R^{n\times n})$ ait des valeurs propres à partie réelle strictement négative pour tout $t$ n'implique pas que le système
$$
\dot{x} = A(t) x 
$$
soit asymptotiquement stable. EXEMPLE ?

### Cas du plan : portrait de phase et théorème de Bendixon


Références
================================================================================

Exercices 
==============================================================================

### Ecoulement dans un réservoir {.exercice #exo_Torricelli}
Considérons un réservoir cylindrique de section $S$ qui se vide par une ouverture de section $s$ située à sa base. On note $x$ la hauteur de liquide dans le réservoir. D'après la *loi de Torricelli*[^Torricelli], l'équation d'évolution de $x$ est donnée par 
$$
\dot{x}=-k\sqrt{|x|} \qquad k = \frac{s}{S}\sqrt{2g}
$$
où $g$ est la pesanteur.

1. Etant donné un temps initial $t_0$ et une hauteur initiale $x_0$, résoudre le problème de Cauchy associé.

2. Comment expliquer physiquement la multitude de solutions ? 

3. Les solutions sont-elles continues par rapport aux conditions initiales au sens du [théorème de régularité des solutions](#theo_regCondInit) donné plus haut ? Pourquoi ?

-> [*Correction*](#correc_Torricelli)

### Autour du Lemme de Grönwall {.exercice #exo_gronwall}

1. (Lemme de Grönwall) Soient $t^-, t^+\in \R$, $u,\alpha, \beta\in C^0([t^-,t^+],\Rgeq)$, tels que
$$
u(t) \leq \alpha(t) + \int_{t_0}^{t}\beta(s) u(s)ds \qquad \forall t\in [t^-,t^+] \ .
$$
Montrer qu'alors
$$
u(t) \leq \alpha(t) +  \int_{t_0}^{t} \alpha(s)\beta(s) \exp\left(\int_{s}^t\beta(r)dr \right) ds\qquad \forall t\in [t^-,t^+]\ .
$$
En déduire que si $\alpha$ est constant,
$$
u(t) \leq \alpha \exp\left(\int_{t_0}^t\beta(r)dr \right) \qquad \forall t\in [t^-,t^+] \ .
$$
*Indice : poser $v(t)=\int_{t_0}^t\beta(s)u(s)ds$ et étudier la dérivée de $v(t)\exp\left(-\int_{t_0}^t\beta(r)dr\right)$*.

2. Utiliser le Lemme de Grönwall pour montrer le [théorème d'existence globale de solutions](#theo_exist_glob). 
*Indice : utiliser la [représentation intégrale des solutions](#theo_eq_integrale)*.

3. Utiliser le Lemme de Grönwall pour montrer le [théorème de continuité par rapport aux conditions initiales](#theo_reg_CI).
*Indice : utiliser la [représentation intégrale des solutions](#theo_eq_integrale)*.

-> [*Correction*](#correc_gronwall)

### Proie/prédateur
Cycle limite Bendixon ou exo cercle attractif

### Masse/ressort {.exercice #exo_masse_ressort}
Considérons une masse $m$ accrochée à un ressort de raideur $k$, lui-même fixé à un mur. 

1. Montrer que l'évolution de la position de la masse peut être décrite par  
$$
m\ddot{x} = - \lambda \dot{x} -k x \ ,
$$
où $\lambda$ est un coefficient de frottement. Que représente $x$ ?

2. Réduire l'équation différentielle à l'ordre $1$.

3. Déterminer les points d'équilibre.

4. Etudier leur stabilité et le comportement des solutions pour $\lambda=0$ et $\lambda>0$. Les dessiner sur un portrait de phase.

-> [*Correction*](#correc_masse_ressort)

### Attractivité locale implique stabilité asymptotique globale pour un système linéaire {.exercice #exo_attrac_stab}
Soit $A\in \R^{n\times n}$. Montrer que si 0 est localement attractif pour 
$$
\dot{x} = Ax
$$
alors il l'est globalement et 0 est stable.

-> [*Correction*](#correc_attrac_stab)


### Contrôle d'un système linéaire {.exercice #exo_cont_lin}
Soit le système décrit par
$$
\dot{x} = x + u(t)
$$
où $t\mapsto u(t)$ est une entrée à choisir.

1. Comment se comporte le système si $u\equiv 0$ ?

2. Si on mesure $t\mapsto x(t)$, comment choisir $u$ pour le rendre asymptotiquement stable ?

-> [*Correction*](#correc_cont_lin)


Correction des exercices
===============================

### Ecoulement dans un réservoir {.correction #correc_Torricelli}


### Autour du Lemme de Grönwall {.correction #correc_gronwall}

1. Soit $v$ l'application définie par $v(t)=\int_{t_0}^t\beta(s)u(s)ds$ sur $[t^-,t^+]$. Elle vérifie
$$
\dot{v}(t) = \beta(t)u(t) \quad , \quad u(t) \leq \alpha(t)+v(t) \ ,
$$
et donc puisque $\beta$ est à valeurs positives,
$$
\dot{v}(t) \leq \alpha(t)\beta(t)+\beta(t)v(t) \ .
$$
Soit maintenant $w$ l'application définie par $w(t)=v(t)\exp\left(-\int_{t_0}^t\beta(r)dr\right)$. $w$ est dérivable sur $[t^-,t^+]$ et 
\begin{align*}
\dot{w}(t) &= (\dot{v}(t)-\beta(t)v(t))\exp\left(-\int_{t_0}^t\beta(r)dr\right)\\
&\leq \alpha(t)\beta(t)\exp\left(-\int_{t_0}^t\beta(r)dr\right)
\end{align*}
En intégrant des deux côté entre $t_0$ et $t$, on obtient
$$
w(t)-w(t_0)\leq \int_{t_0}^t \alpha(s)\beta(s)\exp\left(-\int_{t_0}^s\beta(r)dr\right)ds
$$
et en remplaçant $w$ par son expression,
$$
v(t)\leq \int_{t_0}^t \alpha(s)\beta(s)\exp\left(\int_{t_0}^t\beta(r)dr\right)ds \ ,
$$
ce qui donne le résultat.
Finalement, si $\alpha$ est constant alors
\begin{align*}
u(t) &\leq \alpha +\alpha \left[-\exp\left(\int_s^t\beta(r)dr \right) \right]_{t_0}^t \\
& \leq \alpha -\alpha +\alpha \exp\left(\int_{t_0}^t\beta(r)dr \right)
\end{align*}
ce qui donne le résultat.

2. Soit $x:]\underline{t},\overline{t}[\subseteq I\to \R^n$ une solution au problème de Cauchy. Par le théorème de [représentation intégrale des solutions](#theo_eq_integrale), 
$$
x(t)=x_0 + \int_{t_0}^t f(s,x(s))ds \ ,
$$
et donc, utilisant l'hypothèse de borne au plus affine de $f$, 
$$
\|x(t)\| \leq \|x_0\| + \int_{t_0}^t |b(s)| + |a(s)|\|x(s)\|ds \ .
$$
Sur tout segment $[t^-,t^+]\subset ]\underline{t},\overline{t}[$, on peut donc appliquer le Lemme de Grönwall, ce qui donne
$$
\|x(t)\| \leq \alpha(t) +  \int_{t_0}^{t} \alpha(s)\beta(s) \exp\left(\int_{s}^t\beta(r)dr \right)
$$
avec $\alpha(t)=\|x_0\| + \int_{t_0}^t |b(s)|$ et $\beta(t)= |a(t)|$ qui sont continues sur $I$. D'après le [théoreme des bouts](#theo_bouts), nécessairement $]\underline{t},\overline{t}[=I$.

3. Soient $x:I\to \R^n$ et $x_\delta:I_\delta\to \R^n$ les solutions maximales associées à $(t_0,x_0)$ et $(t_0,x_0+\delta)$ respectivement, et $\overline{t}$ tel que $[t_0,\overline{t}]\subset I$. On sait que
\begin{align*}
x(t)&=x_0  + \int_{t_0}^t f(s,x(s))ds & \forall t\in I\\
x_\delta(t)&=x_0 +\delta  + \int_{t_0}^t f(s,x_\delta(s))ds &\forall t\in I_\delta
\end{align*}
ce qui donne
$$
|x(t)-x_\delta(t)|\leq |\delta| + \int_{t_0}^t |f(s,x(s))-f(s,x_\delta(s))|ds \qquad \forall t\in I\cap I_\delta
$$
Si $[t_0,\overline{t}]\subset I\cap I_\delta$, définissont le compact $\cC := x([t_0,\overline{t}])\cup x_\delta([t_0,\overline{t}])$. Puisque $\frac{\partial f}{\partial x}$ est continue sur $U$ par hypothèse, $M=\max_{[t_0,\overline{t}]\times \cC} \frac{\partial f}{\partial x}$ est bien défini. On a donc par le théorème des accroissements finis
$$
|x(t)-x_\delta(t)|\leq |\delta| + \int_{t_0}^t M |x(s)-x_\delta(s)|ds \qquad \forall t\in [t_0,\overline{t}] \ .
$$
Donc par le Lemme de Grönwall, 
$$
|x(t)-x_\delta(t)|\leq |\delta|e^{M(t-t_0)} \qquad \forall t\in [t_0,\overline{t}] \ .
$$
Il suffit donc de montrer que $[t_0,\overline{t}]\subset I\cap I_\delta$. A FINIR !!!

### Proie/prédateur {.correction #correc_proiePreda}


### Masse/ressort {.correction #correc_masse_ressort}

### Attractivité locale implique stabilité asymptotique globale pour un système linéaire {.correction #corr_attrac_stab}

Tout d'abord, montrons que l'attractivité locale de 0 implique l'attractivité globale. Ceci est dû à la propriété d'*homogénéité* des systèmes linéaires: si $x$ une solution initialisée à $x_0\in\R$, alors $\lambda x$ est solution initialisée à $\lambda x_0$ puisque 
$$
\lambda x(t) = \lambda e^{At} x_0 = e^{At} (\lambda x_0) \ .
$$
Donc soit $\eta>0$ tel que toute solution initialisée dans $B_\eta(0)$ converge vers 0. Soit $x$ une solution initialisée à $x_0\in\R$. Alors $\lambda x$ avec $\lambda < \eta / |x_0|$ est solution initialisée dans $B_\eta(0)$ et converge vers 0. Donc $x$ converge vers 0.

Maintenant, montrons la stabilité. Soit $\varepsilon >0$. Notons $(x_i)_{i=1...n}$ une base orthonormale de $\R^n$. Soit alors $M>0$ tel que 
$$
|e^{At} x_i | \leq M \quad \forall t \in \Rgeq \quad \forall i\in \{1,...,n\}
$$
qui existe bien puisque toutes les solutions convergent vers 0 et $n$ est fini. 
Soit maintenant $\eta >0$. Pour tout $x_0 \in B_\eta(0)$ dont la décomposition dans la base s'écrit
$$
x_0 = \sum_{i=1}^n \alpha_i x_i
$$
on a $|\alpha_i|\leq \eta$ et donc pour tout $t \in \Rgeq$,
$$
\left| e^{At} x_0 \right| \leq \left| \sum_{i=1}^n  e^{At} \alpha_i x_i\right|  \leq  n \eta M 
$$
On conclut que pour des conditions initiales suffisamment petites ($\eta <\frac{\varepsilon}{nM}$), les solutions restent inférieures à $\varepsilon$ en norme. Donc le système est stable.

### Contrôle d'un système linéaire {.correction #correc_cont_lin}
Si $u\equiv 0$, les solutions sont $x(t) = e^t x_0$ donc le point d'équilibre 0 est instable et les solutions divergent. Si l'on mesure $x(t)$, on peut prendre $u(t) = - kx(t)$, ce qui donne
$$
\dot{x} = -(k-1) x
$$
qui est donc asymptotiquement stable si $k>1$.

Annexes 
=========================================================================

### Preuve du théorème des bouts {.preuve #pr_theo_bouts}
Prouvons l'existence de $t_K^+$ (l'existence de $t_K^-$ se prouvant de la même façon). Pour cela, supposons le contraire c'est-à-dire qu'il existe un compact $K\subset U$ tel que
$$
 \forall t_K \in \left[t_0,\overline{t}\right[ \, , \, \exists t\in \left[t_K,\overline{t}\right[ \: : \: x(t)\in K
$$
En d'autres termes, on suppose que la solution revient de manière persistente dans $K$. Alors il existe une suite $(t_p)_{p\in \N}$ telle que 
$$
\overline{t}-\frac{1}{p}\leq  t_p < \overline{t} \quad \text{et} \quad (t_p,x(t_p))\in K \quad \forall p\in \N
$$
On a donc $\lim_{p\to+\infty} t_p = \overline{t}$, et par compacité de $K$, on peut extraire de $(t_p,(x(t_p))_{p\in \N}$ une sous-suite qui converge vers $(\overline{t},\overline{x})\in K$. Pour simplifier les notations, on suppose donc directement $\lim_{p\to+\infty} x(t_p) =\overline{x}$.

Soient $\tau>0$, $r>0$ et $\tau_m\in \left(0,\tau \right]$ tels que 
$$
\cC:=\left[\overline{t}-2\tau,\overline{t}+2\tau \right]\times \overline{B}_{2r}(\overline{x})\subset U \quad , \quad \tau_m  \max_{\cC} \|f\| \leq r\ .
$$
Soit $p\in \N$ tel que $|t_p-\overline{t}|< \tau_m$ et $\|x(t_p)-\overline{t}\|< r$. Alors $\left[t_p-\tau,t_p+\tau \right]\times \overline{B}_{r}(x(t_p))\subset U$ et le théorème de Cauchy Lipschitz nous dit qu'il existe une solution $y:[t_p-\tau_m,t_p+\tau_m]\to \R^n$ au problème de Cauchy $\dot{y}=f(t,y)$, $y(t_n)=x(t_n)$. On a alors $t_p+\tau_m>\overline{t}$, et par unicité, $x\equiv y$ sur $[t_p,\overline{t})$. Donc $x$ peut être prolongée, ce qui contredit sa maximalité.



<!-- Footnotes -->

[^intI]:
Certaines références autorisent les  solutions définies sur un intervalle d'intérieur vide, c'est-à-dire réduit à un point, qui sont dîtes "triviales". Mais cela n'a pas grand intérêt ici et nous supposons donc que les solutions sont définies au moins "pendant un certain temps".

[^solsurI]:
On pourra omettre de préciser l'intervalle $I$ sur lequel $x$ est solution lorsque $I$ est l'ensemble de définition naturel (ou clairement défini) de $x$. Lorsque celui-ci est ambigue ou bien lorsque l'on veut insister sur l'intervalle de définition, on dira *solution sur $I$*.

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

[^accfinis_Cauchy]:
En l'absence d'outils d'analyse fonctionnelle à cette époque, la preuve de Cauchy consistait plutôt à discrétiser en temps l'intégrale de plus en plus finement et montrer la convergence vers une solution.

[^uniCritExGlob]:
Si $f$ est de classe $C^1$ par rapport à $x$, cette solution est unique. Mais ce théorème est aussi valable pour $f$ seulement continue.

[^linkFibre]:
https://portsmouth.github.io/fibre/ + details

[^Torricelli]:
Sous l'hypothèse d'incompressibilité du fluide, la loi de Bernoulli dit que 
$$
p_s + \rho g h_s + \rho \frac{v_s^2}{2}=p_o + \rho g h_o + \rho \frac{v_o^2}{2}
$$ 
où $s$ fait référence aux quantités à la surface et $o$ à l'ouverture.  On a $p_s=p_o$ égales à la pression atmosphérique, $h_s-h_o=x$, $v_s=\frac{s}{S}v_o$ par conservation du débit, et $\dot{x} = - v_s$. On obtient donc
$$
\dot{x} = - \frac{1}{\sqrt{\left(\frac{S}{s}\right)^2-1}} \sqrt{2gx} \approx -\frac{s}{S} \sqrt{2gx}
$$
en supposant que $s\ll S$.