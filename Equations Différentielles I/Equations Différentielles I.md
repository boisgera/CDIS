% Equations Différentielles I

<!-- LaTeX Macros -->
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}

\newcommand{\cS}{\mathcal{S}}

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

- $t_0\in I$ and $x(t_0)=x_0$

- for all $t\in I$, $(t,x(t)) \in U$ and $\dot{x}(t)=f(t,x(t))$

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

### Théorème de Peano {.theorem  #theo_peano}
Soient $U$ un ouvert de $\R\times \R^n$ et $f\in C(U,\R^n)$. Pour tout $(t_0,x_0)\in U$, il existe $\epsilon >0$ et $x\in C^1([t_0-\epsilon,t_0+\epsilon],\R^n)$ tels que $x\in S_f(t_0,x_0)$.

*Démonstration*: La démonstration de ce résultat est hors-programme car elle fait appel au théorème d'Ascoli qui sera abordé dans les notions avancées de Calcul Différentiel III. Seule la connaissance et compréhension du résultat est exigible. Pour les curieux, preuve en appendice? $\hfill\blacksquare$

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
La fonction $f:(t,x)\mapsto -\sqrt{|x|}$ est continue sur $U=\R\times \R$, donc on sait que ce problème de Cauchy admet au moins une solution. Mais pas unicité A FINIR




Unicité des solutions
-------------------------------

Nous avons vu dans la partie précédente que des solutions locales au problème de Cauchy existent toujours si $f$ est continue mais qu'elles ne sont pas nécessairement uniques. Le théorème suivant montre que l'unicité des solutions est garantie si $f$ est de classe $C^1$.

### Théorème de Cauchy-Lipschitz {.theorem #theo_lips}
Soient $U$ un ouvert de $\R\times \R^n$ et $f\in C(U,\R^n)$ telle que sa dérivée partielle $(t,x)\mapsto \frac{\partial f}{\partial x}(t,x)$ existe et est continue sur $U$ (on dira par la suite pour simplifier que $f$ est de classe $C^1$ en $x$).
Alors pour tout $(t_0,x_0)\in U$, il existe une unique solution maximale $x:I\to\R^n$ in $S_f(t_0,x_0)$. De plus,  l'intervalle $I$ est ouvert.

*Démonstration* Nous donnons ici le principe de la preuve qu'il est important de comprendre. La preuve complète est donnée en appendice? L'essentiel est en fait de montrer que sous l'hypothèse de régularité de $f$ par rapport à $x$, il existe une unique solution locale au problème de Cauchy. De là on peut ensuite déduire qu'elle se prolonge en une solution maximale unique et  définie sur $I$ ouvert : elle pourrait sinon être de nouveau prolongée *au bord* de l'intervalle, ce qui contradirait sa maximalité. La partie cruciale est donc le résultat suivant.

**Théorème**(Cauchy-Lipschitz local) Soient $U$ un ouvert de $\R\times \R^n$, $f\in C(U,\R^n)$ de classe $C^1$ en $x$, et $(t_0,x_0)\in U$. Soient $\tau>0$ et $r>0$ tels que 
$$
\mathcal{C}:=[t_0-\tau,t_0+\tau]\times \overline{B_{x_0}(r)}\subset U \ .
$$
Pour tout $\tau_m\in [0,\tau]$ tel que $\tau_m  \max_{\mathcal{C}} |f| \leq r$,
<!--- $$
f_m := \max_{\mathcal{C}} f \quad , \quad \tau_m := \min\left\{\tau,\frac{r}{f_m} \right\}
$$--->
il existe une unique fonction $x\in S_f(t_0,x_0)$ définie sur $[t_0-\tau_m,t_0+\tau_m]$. 

*Démonstration* Rappelons nous que $E:=C([t_0-\tau_m,t_0+\tau_m],\R^n)$ (ref?) est un espace de Banach pour la norme uniforme $|\cdot|_\infty$. Définissons  
$$
F = \{x\in E \: : \: x([t_0-\tau_m,t_0+\tau_m])\subseteq \overline{B_{x_0}(r)} \} \ .
$$
On peut montrer que\footnote{pour toute suite $(x_n)$ d'éléments de $F$ convergeant vers $x^*$, pour tout $t\in [t_0-\tau_m,t_0+\tau_m]$,
$$
|x_n(t)-x^*(t)|\leq |x_n-x^*|_{\infty} \quad \longrightarrow_{n\to \infty} 0
$$
donc la suite $(x_n(t))$ d'éléments du fermé $\overline{B_{x_0}(r)}$  converge dans $\R^n$ vers $x^*(t)$ qui est donc dans $\overline{B_{x_0}(r)}$. Ceci implique $x^*\in F$.} $F$ est un sous-ensemble fermé de $E$. $F$ est donc complet (ref?)  (toujours pour la norme uniforme $|\cdot|_\infty$). Définissons l'opérateur intégral $\Gamma : F\to E$ défini par
$$
\Gamma(x)(t) = x_0+\int_0^t f(s,x(s))ds
$$
$\hfill\blacksquare$


### Exemples {.example #ex_lips}
- Une équation différentielle *linéaire*, c'est-à-dire pour laquelle il existe $a\in C(\R,\R^{n\times n})$ et $b\in C(\R,\R^n)$ telles que
$$
f(t,x) = a(t) x + b(t) \ ,
$$
admet une unique solution maximale quelque-soit sa condition initiale $(t_0,x_0)\in \R\times \R^n$.

- L'intervalle de définition de la solution maximale du problème de Cauchy n'est pas nécessairement $\R$, même si $U=\R \times \R^n$ et $f$ est de classe $C^\infty$. Par exemple, considérons le problème de Cauchy
$$
\dot{x} = x^2 \quad , \qquad (t_0,x_0)\in \R^2 \ .
$$
La fonction $f:(t,x)\mapsto x^2$ est de classe $C^1$ sur $U=\R^2$, donc il existe une unique solution maximale. On peut vérifier par le calcul que celle-ci s'écrit  
$$
x(t)=\frac{x_0}{1-x_0(t-t_0)} \quad , \quad I=\left(-\infty,t_0+\frac{1}{x_0}\right) \ .
$$
Cette solution diverge au temps $t_0+\frac{1}{x_0}$, on dit qu'elle *explose en temps fini*.


### Relâchement à $f$ Lipschitzienne {.remark #rem_f_lips}
On remarque dans la preuve qu'il suffit que $f$ soit Lipschitzienne. A définir + exemple de fonction Lipschitzienne pas $C^1$ "variation bornée". 

C'est en fait Lipschitz lui-même qui a défini la notion de fonction Lipschitzienne pour faire marcher cette preuve et a montré le résultat parallèlement à Cauchy et de manière indépendente sous cette hypothèse plus faible, alors que Cauchy l'avait montré sous l'hypothèse $C^1$ en utilisant le théorème des accroissements finis.

### Approximations successives {.remarque #rem_approx_succ}
Il est rare de pouvoir calculer explicitement la solution au problème de Cauchy. Dans ce cas approximations successives de Picard


Solutions globales
--------------------------------

Dans la section précédente, nous avons vu que lorsque $f$ est $C^1$ en $x$, la solution maximale au problème de Cauchy (qui est alors unique) est définie sur un intervalle ouvert qui n'est pas nécessairement $\R$ entier, c'est-à-dire la solution n'est pas nécessairement globale. En fait, le théorème suivant montre que pour toute solution maximale, la paire $(t,x(t))$  quitte nécessairement n'importe quel compact de $U$ au bout d'un certain temps. Dans le cas usuel où $U=\R\times \R^n$, ceci implique donc que toute solution non globale explose en temps fini comme vu dans [l'exemple où $f(t,x)=x^2$](#ex_lips). Dans le cas où $U$ ne serait pas l'espace entier, une solution non globale pourrait aussi tendre en temps fini vers le "bord" de $U$ sans nécessairement diverger.

### Théorème des bouts {.theorem #theo_bouts}
Soient $U$ un ouvert de $\R\times \R^n$ et $f\in C(U,\R^n)$ de classe $C^1$ en $x$. Soient $(t_0,x_0)\in U$ et $x:(\underline{t},\overline{t})\to \R^n$ la solution maximale au problème de Cauchy correspondant, avec $\underline{t}\in [-\infty,t_0)$ et $\overline{t}\in (t_0,+\infty]$.  Alors pour tout compact $K\subset U$, il existe $t_K^+ \in [t_0,\overline{t})$ and $t_K^-\in (\underline{t},t_0]$) tels que
$$
(t,x(t))\notin K \qquad \forall t\in [t_K^+,\overline{t}) \cup  (\underline{t},t_K^-] 
$$

*Démonstration* : Prouvons l'existence de $t_K^+$ (l'existence de $t_K^-$ se prouvant de la même façon). Pour cela, supposons le contraire c'est-à-dire qu'il existe un compact $K\subset U$ tel que
$$
 \forall t_K \in [t_0,\overline{t}) \, , \, \exists t\in [t_K,\overline{t}) \: : \: x(t)\in K
$$
En d'autres termes, on suppose que la solution revient de manière persistente dans $K$. Alors il existe une suite $(t_n)_{n\in \N}$ telle que 
$$
\overline{t}-\frac{1}{n}\leq  t_n < \overline{t} \quad \text{et} \quad (t_n,x(t_n))\in K \quad \forall n\in \N
$$
On a donc $\lim_{n\to+\infty} t_n = \overline{t}$, et par compacité de $K$, on peut extraire de $t_n,(x(t_n))_{n\in \N}$ une sous-suite qui converge vers $(\overline{t},\overline{x})\in K$. Pour simplifier les notations, on suppose donc directement $\lim_{n\to+\infty} x(t_n) =\overline{x}$.

BESOIN de CL local pour avoir l'estimée du temps minimal d'existence de solution 

$\hfill\blacksquare$

### Critère d'existence globale {.theorem #theo_exist_glob}
Soient $I$ un intervalle ouvert de $\R$, $U=I\times\R^n$, $(t_0,x_0)\in U$ et $f\in C(U,\R^n)$ de classe $C^1$ en x. S'il existe $a,b:I\to \R$ telles que  
$$
|f(t,x)|\leq a(t) |x| + b(t) \quad \forall (t,x)\in I\times \R^n \ ,
$$
alors la solution maximale au problème de Cauchy associé est défini sur $I$ entier. On dit alors que $f$ a une *croissance au plus affine*.

*Démonstration* : 
\hfill$\blacksquare$


### Exemples
- Reprenons l'exemple d'une équation différentielle *linéaire*, c'est-à-dire pour laquelle il existe $a\in C(I,\R^{n\times n})$ et $b\in C(I,\R^n)$ telles que
$$
f(t,x) = a(t) x + b(t) \ .
$$
D'après le théorème précédent, quelque-soit sa condition initiale $(t_0,x_0)\in I\times\R^n$, sa solution maximale est définie sur $I$ entier.

- Un autre cas important d'une croissance au plus affine est lorsque $f$ est globalement bornée en $x$, par exemple de la forme $f(t,x)=c(t)\arctan(x)$ ou $f(t,x)=\frac{c(t)}{1+x^2}$. Dans ce cas, le théorème s'applique avec $a(t)=0$.

<!--- Bien sûr, la fonction $f:(t,x)\mapsto x^2$ ne satisfait pas la croissance au plus affine et [on a vu](#ex_lips) que les solutions associées explosent en temps fini. Par contre, si l'on prend $f(t,x)=-x|x|$ ou $f(t,x)=-x^3$ qui ne satisfont pas non plus cette condition, on peut montrer que les solutions maximales sont globales (et tendent vers 0). On en déduit donc que la croissance au plus affine est  suffisante mais pas nécessaire pour garantir la globalité des solutions.-->




Régularité et stabilité des solutions
==========================================

Régularité en temps fini
-----------------------------

### Régularité par rapport à la condition initiale  {.theorem #theo_reg_CI}


### Chaos et exposant de Lyapunov {.remark #rem_chao}



Propriétés asymptotiques
-----------------------------

### Point d'équilibre

### Stabilité, stabilité asymptotique

### Lyapunov

### Cas linéaire

### Cas du plan : théorème de Bendixon


Références
================================================================================