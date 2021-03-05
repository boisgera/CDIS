% Examen -- Corrigé


\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}
\renewcommand{\P}{\mathbb{P}}
\newcommand{\Esp}{\mathbb{E}}

\newcommand{\cC}{C}
\newcommand{\cD}{\mathcal{D}}

Calcul intégral
================================================================================

### Question 1 {.answer}

Si $\delta>0$ et $t \in [0, x_n]$, 
$\gamma(t) = \left]t-\delta/2, t+\delta/2\right[$ 
est un intervalle ouvert de $\R$ qui contient $t$. La fonction
$\gamma$ est donc une jauge sur $[0, x_n]$.


### Question 2 {.answer}
Le lemme de Cousin établit l'existence d'une telle jauge. Si l'on souhaite
une solution plus explicite, on peut par exemple rechercher une telle 
subdivision pointée $\mathcal{D}_m$ sous la forme 
$$
\left\{ 
  \left(\frac{k+1/2}{m}, \left[\frac{k}{m} x_n, \frac{k+1}{m} x_n \right]\right)\; \left| \vphantom{\int}\right. k \in \{0, \dots, m-1\}\; 
  \right\}
$$
(on vérifiera qu'il s'agit bien d'une subdivision pointée de $[0, x_n]$).
Pour tout $k \in \{0, \dots, m-1\}$, on a
$$
\gamma\left(\frac{k+1/2}{m}\right) 
=
\left]\frac{k+1/2}{m} - \frac{\delta}{2}, \frac{k+1/2}{m} + \frac{\delta}{2}\right[,
$$
donc si ${1}/{2m} < \delta / 2$ -- c'est-à-dire si $m>1/\delta$ -- on a
$$
\left[\frac{k}{m} x_n, \frac{k+1}{m} x_n \right] \subset \gamma\left(\frac{k+1/2}{m}\right)
$$
et $\mathcal{D}_m$ est subordonnée à $\gamma$. Il suffit donc de choisir un
entier $m$ strictement plus grand que $1/\delta$ pour que $\mathcal{D}_m$
fournisse l'exemple de subdivision recherché.

### Question 3 {.answer}
Pour tout entier $k$, la restriction de la fonction $f$ à l'intervalle 
$[x_k, x_{k+1}]$ est égale presque partout (sauf en $x_{k+1}$) 
à la fonction constante égale à $1$ si $k$ est pair et $-1$ sinon ;
cette restriction est donc intégrable et de même intégrale que la 
constante considérée. La fonction constante égale à $\lambda \in \{-1,1\}$ 
admet comme primitive la fonction $x \mapsto \pm \lambda x$ ; 
par le théorème fondamental du calcul, son intégrale sur
$[x_k, x_{k+1}]$ existe et vaut
$$
\int_{x_{k}}^{x_{k+1}} f(x) \, dx = [x \mapsto x]_{x_{k}}^{x_{k+1}} = x_{k+1} - x_{k} = 
a_{k/2} \; \mbox{ si $k$ est pair}
$$
et de même
$$
\int_{x_{k}}^{x_{k+1}} f(x) \, dx = [x \mapsto -x]_{x_{k}}^{x_{k+1}} = x_{k+1} - x_{k} = 
-b_{(k-1)/2} \; \mbox{ si $k$ est impair.}
$$
La fonction $f$ étant intégrable sur tous les intervalles $[x_k, x_{k+1}]$
tels que $0 \leq k \leq n-1$, elle est intégrable sur $[0, x_n]$ et
$$
\int_0^{x_n} f(x) \, dx = \sum_{k=0}^{n-1} \int_{x_k}^{x_{k+1}} f(x) \, dx
= \sum_{k\leq (n-1)/2} a_k - \sum_{k \leq (n-2)/2} b_k.
$$  

<!--
\left|
\begin{array}{ll}
a_0 - b_0 + a_1 + \dots - b_{(n-2)/2} & \mbox{si $n$ est pair,} \\
a_0 - b_0 + a_1 + \dots + a_{(n-1)/2} & \mbox{si $n$ est impair.}
\end{array}
\right.
-->

### Question 4 {.answer}
Soit $\mathcal{D}$ une subdivision pointé subordonnée à $\gamma$.
Si $(t, [a, b]) \in \mathcal{D}$ et l'intervalle $[a,b]$ ne contient aucun $x_k$, 
alors la restriction de $f$ à $[a, b]$ est constante.
On a donc dans ce cas
$$
\left|f(t) (b-a) - \int_a^b f(x) \, dx\right| = 0.
$$
En général, on note que $|f|$ est constante et égale à $1$ sur
$[0, x_n]$. Par conséquent, pour tout $(t, [a, b]) \in \mathcal{D}$,
$$|f(t)(b-a)| \leq |f(t)| |b-a| = (b-a)$$
et 
$$
\left|\int_a^b f(x) \, dx \right| \leq \int_a^b |f(x)| \, dx = (b-a),
$$
donc
$$
\left|f(t)(b-a) - \int_a^b f(x) \, dx \right| \leq 2 (b-a).
$$
Il y a au plus $(n+1)$ éléments $(t, J) \in \mathcal{D}$ tels que 
$\ell(J) > 0$ qui contiennent un $x_k$ avec $k \in \{0,\dots, n\}$
et pour tous ces intervalles $J$, comme $J\subset \gamma(t)$ et que
$\ell(\gamma(t)) = \delta$, on a $\ell(J) \leq \delta$.
Par conséquent,
$$
\begin{split}
\left|S(f, \mathcal{D}) - \int_0^{x_n} f(x) \, dx \right| 
&= \left|\sum_{(t,J) \in \mathcal{D}} f(t) \ell(J) - \int_J f(x) \, dx\right| \\
&\leq \sum_{(t, J) \in \mathcal{D}} \left|f(t) \ell(J) - \int_J f(x) \, dx\right| \\
&\leq 2 (n+1) \delta.
\end{split}
$$

### Question 5 {.answer}
Par récurrence, on peut établir que pour tout $k \in \N$, on a 
$x_k = 1 - 2^{-k}$. En effet, cette relation est vraie au rang $0$ ; si elle
est vraie pour $x_{2k}$ alors
$$
x_{2k+1} = x_{2k} + a_k = (1-2^{-2k}) + 2^{-2k-1} = 1 - 2^{-2k}(1 - 1/2)=
1 - 2^{-2k-1}
$$
et de même, si elle est vraie pour $x_{2k+1}$ alors
$$
x_{2k+2} = x_{2k+1} + b_k = (1 - 2^{-2k-1}) + 2^{-2k-2}
= 1 - 2^{-2k-1}(1 - 1/2)= 1 - 2^{-2k-2}.
$$
On a donc $S:=\lim_{k\to +\infty} 1 - 2^{-k} = 1$.

### Question 6 {.answer}
La fonction $f_n$ est intégrable car elle est l'extension par zéro 
à $\R$ de la restriction de $f$ à $[0, x_n]$, 
dont nous savons qu'elle est intégrable. 
Or $f$ est la limite simple des fonctions $f_n$ :

  - pour tout $x \in \left[0, S\right[$, $f_n(x) = f(x)$ à partir du moment
    où $x_n > x$, ce qui finit nécessairement par arriver puisque
    $\lim_{k \to +\infty} x_k = S$.

  - pour tout $x \not \in \left[0, S\right[$, $f_n(x) = f(x) =0$ pour tout
    entier $n$.

La fonction $f$ est donc mesurable comme limite simple de fonctions intégrables.

### Question 7 {.answer}
Soit $(a, b)$ une paire de réels telle que $0 \leq a \leq b \leq +\infty$.
On a
$$
\left[a, b\right[ = [a, b] \setminus \{b\}.
$$
Les ensembles $[a, b]$ et $\{b\}=[b, b]$ sont (des intervalles) fermés, donc mesurables. 
Le complémentaire $\left[a, b\right[$ de $\{b\}$ dans $[a, b]$ est donc mesurable.

Si $A$ est un sous-ensemble de $\mathbb{R}$, comme
$f(\R) = \{-1, 0, 1\}$, on a
$$
f^{-1}(A) = f^{-1}(A \cap \{-1, 0, 1\})
$$
Il suffit donc de déterminer l'image réciproque par $f$ des sous-ensembles 
de $\{-1, 0, 1\}$, qui sont en nombre fini. Or pour tout $A \subset \{-1,0,1\}$,
on a
$$
f^{-1}(A) = \bigcup_{a \in A} f^{-1}(a).
$$
Comme 
$$E_0 := f^{-1}(0) = \left]-\infty,0\right[ \cup \left[S, +\infty\right[=
\R \setminus \left[0, S\right[,$$
$$
E_1 := f^{-1}(1) = \bigcup_{k=0}^{+\infty} \left[x_{2k}, x_{2k+1}\right[
\; \mbox{ et } \;
E_{-1} := f^{-1}(-1) = 
\bigcup_{k=0}^{+\infty} \left[x_{2k+1}, x_{2k+2}\right[,
$$
l'ensemble $f^{-1}(A)$ peut être égal à $\varnothing$, 
$E_1$, $E_{-1}$, $E_0$, $E_1 \cup E_0$, $E_{-1} \cup E_0$ 
, $E_{-1}\cup E_1$ (c'est-à-dire $\left[0, S\right[$) ou bien $\R$.

Dans tous les cas, $f^{-1}(A)$ est un ensemble mesurable 
(comme union dénombrable d'ensembles mesurables ou complémentaire d'ensemble
mesurable) et ce quel que soit 
l'ensemble $A$ (il n'est même pas nécessaire de se restreindre aux ensembles
ouverts ou fermés). Par le critère de l'image réciproque, la fonction 
$f$ est donc mesurable.

### Question 8 {.answer}
Pour tout $n \in \N$, la fonction $f_n$ coïncide avec $f$ sur $[0, x_n]$ et
est nulle en dehors ce cet intervalle ; on a donc
$$
\int_{-\infty}^{+\infty} f_n(x) \, dx = \int_{0}^{x_n} f(x) \, dx
$$

Les fonction $f_n$ sont intégrables et convergent simplement vers $f$.
On a également $-h \leq f_n \leq h$ pour tout $n \in \N$ où la
fonction $h:\R \to \R$ définie par
$$
h(x) = \left\{
\begin{array}{rl}
1 & \mbox{si $0 \leq x < S$,} \\
0 & \mbox{sinon.}
\end{array}
\right.  
$$
est intégrable (ainsi que $-h$ par linéarité de l'intégrale). 
Par le théorème de convergence dominée,
$f$ est intégrable et 
$$
\int_{-\infty}^{+\infty} f(x) = 
\lim_{n \to +\infty} \int_0^{x_n} f(x) \, dx =
\lim_{n \to +\infty}
\sum_{k\leq (n-1)/2} a_k - \sum_{k \leq (n-2)/2} b_k.
$$
On a 
$$
\sum_{k=0}^p a_k = \sum_{k=0}^p 2^{-2k-1} = \frac{1}{2} \sum_{k=0}^p  \left(\frac{1}{4}\right)^k
=\frac{1}{2} \frac{1- (1/4)^{p+1}}{1 - 1/4}
$$
et 
$$
\sum_{k=0}^p b_k = \sum_{k=0}^p 2^{-2k-2} = \frac{1}{4} \sum_{k=0}^p  \left(\frac{1}{4}\right)^k
=\frac{1}{4} \frac{1- (1/4)^{p+1}}{1 - 1/4}
$$
Par conséquent,
$$
\int_{-\infty}^{+\infty} f(x) =
\lim_{n \to +\infty}
\sum_{k\leq (n-1)/2} a_k - \sum_{k \leq (n-2)/2} b_k
=\frac{1}{2} \frac{4}{3} - \frac{1}{4}  \frac{4}{3}  =\frac{1}{3}.
$$


### Question 9 {.answer}
La restriction de $f$ à l'intervalle $[0, S]$ est encadrée par les constantes
$-1$ et $1$. Elle est également continue en tout point $x \in [0, S]$ qui
n'appartient pas à l'ensemble
$\{x_k \; | \; k \in \N\}\cup \{S\},$ 
ensemble qui est dénombrable, donc négligeable ; 
la fonction $f$ est donc continue presque partout.
Par le critère d'intégrabilité de Lebesgue, elle est donc
Riemann-intégrable sur $[0, S]$.


<!--
Hors cadre
================================================================================


TODO -- Fonction distance
--------------------------------------------------------------------------------

Calcul intégral
--------------------------------------------------------------------------------

### Question 10 {.answer}
Comme la série $\sum_k a_k + b_k$ est non-bornée par hypothèse, 
$\lim_{k\to +\infty} x_k = +\infty$ et donc
$$
|f(x)| = \left| 
\begin{array}{rl}
0 & \mbox{si $x<0$,} \\
1 & \mbox{si $x \geq 0$.}
\end{array}
\right.
$$
La fonction $f$ n'est donc pas absolument intégrable.

Si nous supposons que $f$ est intégrable, alors par le théorème de Hake on
a en particulier 
$$
\lim_{n\to +\infty} \int_{-2^n}^{x_{2n}} f(x) \, dx = \int_{-\infty}^{+\infty} f(x) \, dx,
$$
or 
$$
\int_{-2^n}^{x_{2n}} f(x)\, dx = \int_0^{x_{2n}} f(x) \, dx = \sum_{k=0}^{n} a_k - b_k.
$$
Il est donc nécessaire que la série $\sum_k a_k - b_k$ soit convergente pour que 
$f$ soit intégrable et si $f$ est bien intégrable, on a alors
$$
\int_{-\infty}^{+\infty} f(x) \, dx = \sum_{k=0}^{+\infty} a_k - b_k.
$$
Comme il est également nécessaire que l'intégrale de $f$ sur $[0, x_{2n+1}]$
ait une limite quand $n \to +\infty$ pour que $f$ soit intégrable 
et que cette limite est à nouveau l'intégrale de $f$ sur $\R$, en utilisant
$$
\int_0^{x_{2n+1}} f(x) \, dx
=
\int_0^{x_{2n}} f(x)\, dx + a_n
$$
on en déduit qu'il est également nécessaire que $\lim_{n\to +\infty} a_n = 0$ ; 
on peut remarquer que lorsque la série $\sum_k a_k - b_k$ est convergente,
on a nécessairement $\lim_{n \to +\infty} a_n - b_n = 0$, donc ces deux
conditions impliquent également que $\lim_{n\to +\infty} b_n = 0$.

Réciproquement, supposons que 
$$\sum_{k} a_k - b_k \mbox{ est convergente et } 
\lim_{n\to +\infty} a_n = \lim_{n\to +\infty} b_n = 0.$$ 
Soit $c_n$ et 
$d_n$ deux suites de valeurs réelles telles que 
$\lim_{n\to +\infty} c_n = -\infty$ et $\lim_{n\to +\infty} d_n =+\infty$.
Notons $m_n$ le plus grand entier tel que $x_{2m_n} \leq d_n$. Dès que
$c_n \leq 0$, on a
$$
\int_{c_n}^{d_n} f(x) \,dx = \int_0^{d_n} f(x) \, dx = 
\sum_{k=0}^{m_n} a_k - b_k + \int_{x_{2m_n}}^{d_n} f(x) \, dx.
$$
Or comme $|f(x)| \leq 1$,
$$
\left|\int_{x_{2m_n}}^{d_n} f(x) \, dx\right| \leq d_n - x_{2m_n} \leq x_{2m_{n+1}} - x_{2m_n}
= a_{m_n} + b_{m_n}.
$$
Par conséquent, l'intégrale ci-dessus tend vers $0$ quand $n \to +\infty$ et par
conséquent,
$$
\lim_{n \to +\infty}  \int_{c_n}^{d_n} f(x) \,dx = \sum_{k=0}^{+\infty} a_k - b_k.
$$
Par le théorème de Hake, $f$ est donc intégrable.

-->


Calcul Différentiel
================================================================================

### Question 1 {.answer}

Si $x=(0,0)$ alors tout point de $C$ est à une distance de 1 de $x$, 
donc 
$$
d_\cC(x) = 1 \qquad , \qquad \Pi_\cC(x) = C \ .
$$

Supposons maintenant $x\neq (0,0)$. $x=(r\cos\theta,r\sin\theta)$ avec $r=\|x\|$ et $\theta\in[0,2\pi]$. Par ailleurs, un point $a\in C$ s'écrit $a=(\cos\rho,\sin \rho)$, $\rho\in[0,2\pi]$. On a donc
\begin{align*}
\|x-a\|^2 &= (r\cos\theta-\cos\rho)^2 + (r\sin\theta-\sin\rho)^2 \\
&= r^2 + 1 -2r(\cos\theta-\cos\rho+\sin\theta-\sin\rho) = r^2 + 1 -2r\cos(\theta-\rho)
\end{align*}
Donc le minimum est atteint pour $\cos(\theta-\alpha)=1$, i.e. $\theta=\rho$. On a alors
$$
\|x-a\|^2 = r^2 + 1 -2r = (r-1)^2 = (\|x\|-1)^2
$$
d'où $d_C(x)=\pm (\|x\|-1)$. De plus, le point $a\in C$ pour laquelle cette distance est atteinte est $(\cos\theta,\sin\theta)$, i.e., 
$$
\Pi_\cC(x) = \left\{\frac{x}{\|x\|} \right\} \ .
$$

<!--Commençons par étudier le cas où $x$ est de la forme $(x_1,0)$ avec $x_1 > 0$. Tout $a\in C$ s'écrit $a=(\cos t, \sin t)$, de sorte que
$$
\|x-a\|^2 = (\cos t -x_1)^2 + \sin^2 t = 1 -2x_1 \cos t + x_1^2 \ .
$$
Le minimum est atteint pour $t=0$ et on a alors $d_\cC(x) = \sqrt{(x_1-1)^2}$ atteint pour $a=(1,0)$.

Maintenant, prenons $x\neq (0,0)$ quelconque. Il s'écrit $\|x\|(\cos \rho, \sin \rho)$ où $\rho$ est son argument. Notons $R(\rho)$ la matrice de rotation d'angle $\rho$. On a donc $x = R(\rho)x_0$ avec $x_0 =(\|x\|,0)$ de la forme étudiée précédemment. Or pour tout $a\in \cC$,
$$
\|x-a\| = \|R(\rho)x_0-a\| = \|R(\rho)(x_0-R(-\rho) a)\| = \|x_0-a'\|
$$
avec $a' = R(-\rho) a$.
En observant que $R(-\rho)a$ décrit $\cC$ lorsque $a$ décrit $\cC$,
$$
d_\cC(x) =  \inf_{a'\in \cC} \|x_0-a'\| = d_\cC(x_0) = \sqrt{(\|x\|-1)^2}
$$
atteint pour $a' = (1,0)$ donc pour $a = R(\rho) a'= (\cos\rho,\sin\rho) = \frac{x}{\|x\|}$. Donc
$$
\Pi_\cC(x) = \left\{\frac{x}{\|x\|} \right\} \ .
$$
-->

<!-- Si $x\in \cC$, alors pour tout autre point $x'\in C$, $\|x-x'\| >0 = \|x-x\|$ donc $d_\cC(x) = 0$ et le seul projeté est $x$, i.e.
$$
\Pi_\cC(x) = \{x \} \ .
$$

Supposons maintenant que $x\notin C$ et $x\neq (0,0)$. 
Soit le point $M$ de coordonnées $x=(x_1,x_2)$ et le point $O=(0,0)$. Prenons $M_C$ un point sur le cercle. Alors les trois points $M,M_c,O$ définissent un triangle et on a
$$
MM_c^2 = MO^2 + M_cO^2 - 2 MO \times M_cO \cos(\gamma)
$$
où $\gamma$ est l'angle au sommet en $O$. Donc pour tout $M_c$ sur le cercle,
$$
MM_c^2 = \|x\|^2 + 1 - 2 \|x\| \cos(\gamma)
$$
qui est minimal pour $\gamma=0$, c'est-à-dire pour $M_c \in [OM)$. On a alors
$$
d_\cC(x)^2 = \|x\|^2 + 1 - 2 \|x\| = (\|x\|-1)^2
$$
et donc $d_\cC(x)=\pm (\|x\|-1)$ suivant si $x$ est à l'intérieur ou l'extérieur du cercle. De plus, le fait que $M_c \in [OM)$ et $M_c\in \cC$ détermine un unique $M_c$ qui a pour coordonnées $\frac{x}{\|x\|}$. Donc 
$$
\Pi_\cC(x) = \left\{\frac{x}{\|x\|} \right\} \ .
$$
-->

### Question 2 {.answer}
Au voisinage de $x=(0,0)$,
$$
d_\cC(x) = 1 - \|x\| = 1- \sqrt{x_1^2+x_2^2}  \ .
$$
La dérivée partielle par rapport à $x_1$ de $d_\cC$ en $x=0$, si elle existe, est donnée par
$$
\lim_{t\to 0} \frac{d_\cC(t,0)-d_\cC(0,0)}{t} = 
\lim_{t\to 0} \frac{1 - |t| -1}{t}  
=\lim_{t\to 0} -\frac{|t|}{t} \ .
$$
Mais cette limite n'existe pas car $-t/|t| = -1$ pour $t>0$ et $1$ pour $t<0$. 
Donc $d_\cC$ n'est pas différentiable en 0.

Prenons maintenant $x\in \cC$, c'est-à-dire tel que $\|x\|=1$. 
L'idée est de montrer que dans la direction donnée par le vecteur $x$, 
la différentielle n'existe pas. 
Supposons en effet que $d_\cC$ est différentiable en $x$. Alors pour tout $t\in \R$,
$$
d_\cC(x+tx) = d_\cC(x) + dd_\cC(x) \cdot tx + o(|t|) = dd_\cC(x) \cdot tx + o(|t|) \ ,
$$
donc
$$
\lim_{t\to 0} \frac{d_\cC(x+tx)}{t} = dd_\cC(x) \cdot x
$$
Mais pour $t$ petit, selon si $t>0$ ou $t<0$, $x+tx$ est à l'intérieur du cercle ou à l'extérieur et donc puisque $\|x\|=1$, soit
$$
d_\cC(x+tx) = \|x+t x\| -1 = (1+t)\|x\| -1 = t
$$
soit
$$
d_\cC(x+tx) = 1-\|x+t x\|  = 1- (1+t)\|x\| = -t.
$$
Donc ${d_\cC(x+tx)}/{t}$ n'admet pas de limite quand $t$ tend vers 0 et $d_\cC$ n'est pas différentiable en $x$.

### Question 3 {.answer}
De l'expression de $d_C(x)$ on déduit que pour tout $x \in \R^2$,
$$
f(x)=\|x\|-1 = \sqrt{x_1^2 +x_2^2}-1.
$$ 
Pour $(x_1,x_2)\neq (0,0)$, $f$ admet pour dérivées partielles
$$
\frac{\partial f}{\partial x_1}(x_1,x_2) = \frac{x_1}{\sqrt{x_1^2 +x_2^2}} 
\quad, \quad
\frac{\partial f}{\partial x_2}(x_1,x_2) = \frac{x_2}{\sqrt{x_1^2 +x_2^2}} 
$$
qui sont continues au voisinage de $x$. 
Donc $f$ est continûment différentiable sur $\R\setminus \{(0,0)\}$. 
On en déduit 
$$
\nabla f(x) = \left(
\begin{matrix}
\frac{x_1}{\sqrt{x_1^2 +x_2^2}}\\
\frac{x_2}{\sqrt{x_1^2 +x_2^2}}
\end{matrix}
\right)
= 
\frac{x}{\|x\|} \ .
$$
De même, $\nabla f$ est continûment différentiable sur $\R\setminus \{(0,0)\}$ donc $f$ est deux fois continûment différentiable de matrice Hessienne
$$
H_f(x) = \frac{1}{\sqrt{x_1^2 +x_2^2}} \left(
  \begin{matrix}
  1- \frac{x_1^2}{x_1^2 +x_2^2} & - \frac{x_1x_2}{x_1^2 +x_2^2} \\
  -\frac{x_1x_2}{x_1^2 +x_2^2} & 1- \frac{x_2^2}{x_1^2 +x_2^2}
  \end{matrix}
\right) = \frac{1}{\|x\|^3} 
\left(
\begin{matrix}
  x_2^2 & - x_1x_2 \\
  -x_1x_2 & x_1^2
  \end{matrix}
  \right)
$$
On note que $f$ est différentiable partout sauf en $x=(0,0)$, 
c'est-à-dire seulement là où $\Pi_\cC(x)$ est un singleton. 

### Question 4 {.answer}
Pour tout $x\in \R^2$, $\|\nabla f(x) \| = 1$. Par l'inégalité des accroissements finis, on déduit que pour tout $(x_a,x_b)$ tels que le segment $\left[ x_a,x_b \right]\subset\R\setminus \{ 0 \}$, $|f(x_a)-f(x_b)| \leq \|x_a-x_b\|$. Si maintenant $0 \in \left[ x_a,x_b \right]$, il existe une direction $v\in \R^2$ telle que $0 \notin \left[ x_a+tv,x_b +tv\right]$ pour tout $t>0$. Alors pour tout $t>0$,
$|f(x_a+tv)-f(x_b+tv)| \leq \|(x_a+tv)-(x_b+tv)\| = \|x_a-x_b\|$, et en passant à la limite lorsque $t$ tend vers 0, on obtient l'inégalité demandée car $f$ est continue sur $\R^2$.

### Question 5 {.answer}

<!-- Soit $x\in \R^n$. Puisque $A\subset \overline{A}$, on a $d_{\overline{A}}(x)\leq d_A(x)$. Mais $\overline{A}$ est fermé donc d'après la question précédente, $\Pi_{\overline{A}}$ est non vide, i.e. il existe $a^\star \in \overline{A}$ tel que $\|x-a^\star \| = d_{\overline{A}}(x)$. Par définition de l'adhérence, il existe une suite $(a_k)$ d'éléments de $A$ tels que 
$\lim_{k\to +\infty} a_k = a^\star$ et donc $\lim_{k\to +\infty} \|x-a_k \|= \|x-a^\star \| = d_{\overline{A}}(x)$. Par définition de $d_A$, il s'ensuit que $d_{A}(x)\leq d_{\overline{A}}(x)$. Finalement, on a donc bien $d_A = d_{\overline{A}}$.
-->

$d_A(x)=\inf_{a \in A} \|x - a\|=0$ implique qu'il existe une suite de point $a_n\in A$ tels que 
$$
\lim_{n\to \infty} \|x - a_n\| = 0 
$$
donc que $x$ est dans l'adhérence de $A$. Réciproquement, si une telle suite existe, $\inf_{a \in A} \|x - a\|\leq 0$ et donc nécessairement puisque $\|x - a\|\geq 0$ pour tout $a\in A$, $d_A(x)=0$.


### Question 6 {.answer}
Soit $x\in \R^n$. Fixons $a_0\in A$ et $r:=\|x-a_0\|$.
Soit $B$ la boule fermée centrée en $a_0$ et de rayon $r$. 
Comme $a_0\in A\cap B$, $A\cap B$ est non vide. 
De plus, $A\cap B$ est fermé comme intersection de fermés, et borné car $B$ est bornée. Donc $A\cap B$ est compact. L'application $a \mapsto \|x-a\|$ est continue sur $A\cap B$ donc elle admet un minimum atteint en $a^* \in A\cap B$. Par définition de $d_A$, on a donc $d_A(x) = \|x-a^*\|$
et $a^*\in \Pi_A(x)$.

Soit $x\in A$. Alors $d_A(x)=0$ et donc nécessairement $\Pi_A(x)=\{x\}$.

Soit $x\notin A$. Par définition, $\Pi_A(x) \subset A$, donc pour montrer le résultat il faut montrer que $\Pi_A(x) \cap \mathring{A}$ est vide.  Prenons donc un point $a_0\in \mathring{A}$ et montrons que $a_0\notin \Pi_A(x)$. Par définition de l'intérieur, il existe une boule $B$ centrée en $a_0$ et incluse dans $A$. L'idée est de montrer qu'il y aura forcément un point plus près de $x$ dans $B$. Prenons un point $a'$ sur le segment $[x,a_0]$ c'est-à-dire pour lequel il existe $\lambda\in [0,1]$ tel que
$$
a' = \lambda x + (1-\lambda) a_0 \ .
$$
On a alors
$$
\|a'-x\| = \|(1-\lambda)(a_0-x)\| = |1-\lambda|\|a_0-x\| <  \|a_0-x\|
$$
pour tout $\lambda \in \left]0,1\right]$. Or pour $\lambda$ suffisamment petit, $a'\in B\subset A$ et $a'$ est plus proche de $x$ que $a_0$. Donc $a_0 \notin \Pi_A(x)$ et $\Pi_A(x)\subset \partial A$.


### Question 7 {.answer}
Soit $x\in D_A$. On nous dit qu'alors $d_A^2$ est différentiable en $x$. Alors par définition du gradient, pour tout $v\in \R^n$, pour tout $t\in \R$,
$$
d_A(x+tv)^2 = d_A(x)^2 + \left<\nabla d_A^2 (x),tv\right> + o(t\|v\|)
$$
et donc 
$$
\lim_{t\to 0} \frac{d_A(x+tv)^2-d_A(x)^2}{t} = \left<\nabla d_A^2 (x),v\right> \ .
$$
D'après l'équation (1) de l'énoncé, 
<!-- on a 
$$
\lim_{t\to 0} \frac{d_A(x+tv)^2-d_A(x)^2}{t} = 2 \left<v, x-p_A(x)\right> \ .
$$ 
-->
on en déduit que
$$
\nabla d_A^2 (x) = 2(x-p_A(x)) \ .
$$

### Question 8 {.answer}
Tout d'abord $d_A$ est constante égale à zero sur l'ouvert $\mathring{A}$ donc elle y est différentiable de gradient $\nabla d_A =0$.

Ensuite, vu que $d_A = \sqrt{d_A^2}$, $d_A$ est différentiable en $x$ si $d_A^2$ est différentiable en $x$ et $d_A^2(x)\neq 0$, donc si $\Pi_A(x)\in D_A \setminus A$. Soit $g_1:\left]0, +\infty\right[ \to \left]0, +\infty\right[$ défini par $g_1(t)=\sqrt{t}$ et $g_2:D_A \setminus A \to \left]0, +\infty\right[$ défini par $g_2=d_A^2$. On a 
$$
d_A = g_1\circ g_2 
$$
et donc par la règle de différentiation en chaîne, pour tout $x\in D_A \setminus A$, 
$$
d d_A(x) \cdot h =  d g_1( g_2(x)) \cdot d g_2(x) \cdot h \ .
$$
Or pour $k\in \R$ et $t\in \left]0, +\infty\right[$, $d g_1( t)\cdot k = \frac{1}{2\sqrt{t}} k$, et pour $h\in \R^n$ et $x\in \R^n$, $d g_2(x) \cdot h = \left< \nabla d_A^2(x),h\right>$. Donc
$$
d d_A(x) \cdot h = \frac{1}{2\sqrt{d_A^2(x)}} \left< \nabla d_A^2(x),h\right>
$$
soit
$$
\nabla d_A(x) = \frac{1}{d_A(x)} (x-p_A(x)) = \frac{x-p_A(x)}{\|x-p_A(x)\|}  \ .
$$

On a donc la différentiabilité sur $(D_A \setminus A) \cup \mathring{A} = D_A\setminus \partial A$.

<!--Si $d_A$ était différentiable en un point $x\notin D_A$ admettant plusieurs projetés alors $d_A^2$ le serait aussi par différentiation en chaîne puisque $t\mapsto t^2$ est dérivable sur $\R$. C'est donc impossible. 

Supposons que $d_A$ différentiable en $x\in \partial A$. Alors 
$$
0\leq \lim_{t\to 0} \frac{d_A(x+tv)}{t} = \lim_{t\to 0} \frac{d_A(x+tv)-d_A(x)}{t} = \left<\nabla d_A(x),v\right> 
$$
et en l'appliquant à $-v$, nécessairement $\nabla d_A(x)=0$. Vu que le gradient à l'extérieur de $A$ (lorsqu'il existe) est de norme 1, il ne peut pas être continu sur la frontière. 
-->

### Question 9 {.answer}

Soient $v\in \R^n$, et $x\in \R^n$.

+ Soient $t>0$ et $p\in  \Pi_A(x)$. Pour tout $p_t\in \Pi_A(x+tv)$,
\begin{align*}
 \frac{d_A(x+tv)^2-d_A(x)^2}{t} &=   \frac{\|x+tv-p_t\|^2-\|x-p\|^2}{t}\\
 &\leq    \frac{\|x+tv-p\|^2-\|x-p\|^2}{t}\\
 &\leq 2 \left<v, x-p\right> + t\|v\|^2 \ .
\end{align*}
puisque $d_A(x+tv)$ minimise la distance à $A$ et $p_t\in A$.

+ Soit une suite $(t_k)_{k\in \N}$ de $\R^+$ telle que $\lim_{k\to +\infty} t_k = 0$, et $(p_{k})_{k\in \N}$ une suite de $A$ telle que $p_k\in \Pi_A(x+t_kv)$ pour tout $k\in \N$. On a 
\begin{align*}
|p_k| = |x+t_kv + p_k - (x+t_kv) |  &\leq |x+t_kv| + |x+t_kv - p_k|  \\
& \leq d_A(x+t_kv) + |x+t_kv| \\
& \leq d_A(x+t_kv) - d_A(x) +d_A(x) + |x+t_kv|
\end{align*}
Et d'après le point précédent, $\lim d_A(x+t_kv) - d_A(x) =0$ donc $(p_k)$ est bornée. $(p_k)$ est bornée dans le fermé $A$ donc elle vit dans un compact et on peut en extraire une sous-suite $(p_{\sigma(k)})$ qui converge vers $p_0 \in A$. Vu que $\lim \|x+t_{\sigma(k)}v - p_{\sigma(k)}\| = \|x-p_0\|$, et que $\|x+t_{\sigma(k)}v - p_{\sigma(k)}\|=d_A(x+t_\sigma(k)v)$, on en déduit $\|x-p_0\|=d_A(x)$ et donc que $p_0\in \Pi_A(x)$.

+ Finalement, puisque pour tout $k$, $d_A(x)\geq \|x- p_{\sigma(k)}\|$ par définition de la distance,
\begin{align*}
\frac{d_A(x+t_{\sigma(k)}v)^2-d_A(x)^2}{t_{\sigma(k)}} &= \frac{\|x+t_{\sigma(k)}v - p_{\sigma(k)}\|^2-\|x- p_{\sigma(k)}\|^2}{t_{\sigma(k)}} \\
&\geq 2 \left<v, x-p_{\sigma(k)}\right> + t_{\sigma(k)}\|v\|^2   \\
&\geq 2 \left<v, x-p_0\right> + 2 \left<v, p_0-p_{\sigma(k)}\right> + t_{\sigma(k)}\|v\|^2 \\
&\geq 2 \inf_{p\in \Pi_A(x)} \left<v, x-p\right> + \Delta_k
\end{align*}
avec $\lim_{k\to +\infty} \Delta_k=0$. Donc
$\liminf_{t\to 0}\frac{d_A(x+tv)^2-d_A(x)^2}{t} \geq 2 \inf_{p\in \Pi_A(x)} \left<v, x-p\right>$.
Par ailleurs, on sait par le premier point que $\frac{d_A(x+tv)^2-d_A(x)^2}{t}\leq 2\inf_{p\in \Pi_A(x)} \left<v, x-p\right> + \Delta(t)$ avec $\lim_{t\to0} \Delta(t)=0$. On en déduit que
$\limsup_{t\to 0}\frac{d_A(x+tv)^2-d_A(x)^2}{t}\geq 2\inf_{p\in \Pi_A(x)} \left<v, x-p\right>$.
Ceci montre donc que la limite existe et vaut nécessairement $2\inf_{p\in \Pi_A(x)} \left<v, x-p\right>$.


### Question 10 {.answer}

Supposons que $d_A^2$ est différentiable en $x$. Alors nécessairement, d'après la question précédente, pour tout $v\in \R^n$,
$$
\left< \nabla d_A^2(x), v \right> = 2\inf_{p\in \Pi_A(x)} \left<v, x-p\right> \ .
$$
Une idée est de montrer que la fonction à droite n'est pas linéaire si $\Pi_A(x)$ n'est pas un singleton. Soient donc $p_1,p_2 \in \Pi_A(x)$. Vu que pour tout $p\in \Pi_A(x)$, $\|x-p\|=d_A(x)$, en prenant $v_1=-(x-p_1)$, on obtient
$$
\left< \nabla d_A^2(x), v_1 \right> = 2\inf_{p\in \Pi_A(x)} -\left<x-p_1, x-p\right> = -2 \left<x-p_1, x-p_1\right>= -2d_A(x)^2 \ .
$$
De même, pour $v_2=-(x-p_2)$
$$
\left< \nabla d_A^2(x), v_2 \right> = -2 \left<x-p_2, x-p_2\right>= -2d_A(x)^2 \ .
$$
Par linéarité, on obtient donc
$$
\left< \nabla d_A^2(x), v_1+ v_2 \right> = -4 d_A(x)^2 \ .
$$
Mais par ailleurs,
$$
\left< \nabla d_A^2(x), v_1+ v_2 \right> = 2\inf_{p\in \Pi_A(x)} -\left<x-p_1, x-p\right>-\left<x-p_2, x-p\right>\ ,
$$
et le seul moyen d'obtenir $-4 d_A(x)^2$ est d'avoir simultanément
$$
-\left<x-p_1, x-p\right>= -d_A(x)^2 \qquad , \qquad -\left<x-p_2, x-p\right>= -d_A(x)^2 
$$
et donc $x-p_1= x-p=x-p_2$, soit $p_1=p_2$. Donc il faut que $\Pi_A(x)$ soit réduit à un singleton.

<!--
Pour tout $x\in A$, $d_A(x)=0$, et donc $b_A(x) = -d_{A^c}(x)\leq 0$. 
Pour tous les autres points $x$, c'est-à-dire pour tout $x\in A^c$, $d_{A^c}(x)=0$ et $b_A(x) = d_{A}(x) \geq 0$. Donc $b_A(x)=0$ si et seulement si $d_{A^c}(x)=d_{A}(x)=0$, 
donc si et seulement si $x\in \overline{A}\cap \overline{A^c}=\partial A$. 
En conclusion
$$
\partial A = \{ x\in \R^n , \ b_A(x)=0 \} \ .
$$
Ensuite, $\mathring{A}=A\setminus \partial A$ donc
$$
\mathring{A} = \{ x\in \R^n , \ b_A(x)<0 \} 
$$
Finalement, comme $A$ est fermé, $A^c$ est ouvert, donc $A^c \cap  \partial A =\emptyset$ et
$$
A^c = \{ x\in \R^n , \ b_A(x)>0 \} \ .
$$

Maintenant montrons que  $|b_A|=d_{\partial A}$. 
Pour $x\in A^c$, on a vu que $\Pi_A(x)\subset \partial A$ donc $b_A(x)=d_A(x)=d_{\partial A}(x)$. 

Maintenant, pour $x\in A$, $b_A(x)=-d_{A^c}(x)=-d_{\overline{A^c}}(x)$ et en appliquant le raisonnement précédent sur $\overline{A^c}$ qui est fermé, $d_{\overline{A^c}} = d_{\partial (\overline{A^c})} = d_{\partial A}$. Donc $b_A(x)=- d_{\partial A}(x)$, ce qui donne le résultat $|b_A|=d_{\partial A}$. 
-->

Probabilités
===================================================================================

## Préliminaires -- Espérance et fonction de répartition

### Question 1 {.answer}
 
Etudions la fonction $$g : (x,u) \in \R_+^2 \mapsto 1_{[x,+\infty[}(u)\,f(u) = \left|\begin{array}{ll} f(u) & \text{si } x \leq u,\\0 & \text{si } x > u. \end{array}\right.$$

   i. Remarquons d'abord que $f$ étant positive (c'est une densité), toutes les fonctions partielles de $g$ le sont aussi ; l'intégrabilité coïncide ici avec l'absolue intégrabilité.
    Soient $x,u \in\R_+$. 

   * D'après l'expression de $g$ on a $g_u(x) \leq f(u)\,1_{[0,u]}(x).$ La fonction partielle $g_u$ est donc positive et majorée par le produit d'une constante et de l'indicatrice d'un segment, qui est trivialement intégrable sur $\R_+$. Par le critère d'intégrabilité dominée, $g_u$ l'est donc aussi pour tout $u\in\R_+$.   
   * De même, $g_x(u) \leq f(u)$. La fonction partielle $g_x$ est donc positive et majorée par une densité, par définition (absolument) intégrable. Par le critère d'intégrabilité dominée, $g_x$ l'est donc aussi sur $\R_+$ pour tout $x\in\R_+$.
        
  ii. Comme $g_x$ est intégrable sur $\R_+$, on peut calculer son intégrale :
    \begin{align*}
    \int_{\R_+} g(x,u)\,du &= \int_{\R_+} 1_{[x,+\infty[}(u)\,f(u)\,du\\
    & = \int_{\R_+} (1 - 1_{[0,x[}(u))\,f(u)\,du\\
    & = \left(\int_{\R_+} f(u)\,du - \int_0^x f(u)\,du\right)\\
    &= 1 - F(x)
    \end{align*}
    car $X$ est une variable positive (sa densité est nulle sur $\R_-^\ast$).

  iii. Comme $g_u$ est intégrable sur $\R_+$, on peut calculer son intégrale :
    \begin{align*}
    \int_{\R_+} g(x,u) \,dx &= \int_{\R_+} 1_{[x,+\infty[}(u)\,f(u) \,dx = f(u)\,\int_{\R_+} 1_{[0,u]}(x)\,dx\\
    &= f(u)\,\int_0^u 1\, dx =  u\,f(u).
    \end{align*}

    
### Question 2 {.answer}

Nous allons montrer les deux sens de l'équivalence.

  * Commençons par supposer que $1-F$ est intégrable sur $\R_+$. D'après la question précédente, cela signifie que $x \in \R_+ \mapsto \int_{\R_+} g(x,u)\,du$ est (absolument) intégrable. D'après le théorème de Tonelli, $g$ est donc absolument intégrable sur $\R_+^2$. Le théorème de Fubini garantit alors que la fonction $u \in \R_+ \mapsto \int_{\R_+} g(x,u) \,dx = u\,f(u)$ est intégrable, ce qui signifie justement que $X \in \mathcal{L}^1$ pour $X$ une variable aléatoire positive.

  * Réciproquement, supposons que $X \in \mathcal{L}^1$, c'est-à-dire que $u \in \R_+ \mapsto u\,f(u) = \int_{\R_+} g(x,u) \,dx$ est (absolument) intégrable. Le théorème de Tonelli garantit alors que $g$ est absolument intégrable sur $\R_+^2$, puis celui de Fubini que la fonction $x \in \R_+ \mapsto \int_{\R_+} g(x,u)\,du = 1-F(x)$ l'est également.
  
  Nous avons donc montré l'équivalence $(E)$.
  
### Question 3 {.answer}

Par définition, puisque $X$ est positive nous avons d'abord
 $$\Esp\left(X\right) = \int_{\R_+} x\,f(x)\,dx.$$
 Or d'après la question 1, en utilisant à nouveau le théorème de Fubini :
 \begin{align*}
 \int_{\R_+} u\,f(u)\,du &= \int_{\R_+} \left(\int_{\R_+} g(x,u)\,dx\right)\,du = \int_{\R_+} \left(\int_{\R_+} g(x,u)\,du\right)\,dx\\
 & = \int_{\R_+} 1-F(x)\,dx.
 \end{align*}
 On peut donc écrire de manière équivalente $$\Esp(X) = \int_{\R_+} 1-F(x)\,dx.$$

## Etude du maximum -- Loi de Fréchet

### Question 4 {.answer}

La loi de $X^\alpha$ est déterminée par sa fonction de répartition que nous allons donc expliciter. Par définition, pour tout $x\in\R$ elle vaut $\P\left(X^\alpha \leq x \right)$. Or comme $X$ est positive ($F(0) = 0$), pour tout $x \in \R_-$ on a directement $\P\left(X^\alpha \leq x \right) = 0$. Pour tout $x \in \R_+^\ast$, l'application $x \in \R_+^\ast \mapsto x^\alpha$ étant bijective et croissante ($\alpha > 0$ par hypothèse), on obtient
$$\P\left(X^\alpha \leq x\right) = \P\left(X \leq x^{\frac{1}{\alpha}} \right)= F_{\frac{1}{\alpha}}(x).$$
Puisque $F_{\frac{1}{\alpha}}$ est nulle sur $\R_-$, on en déduit que l'égalité ci-dessus est vraie pour tout $x\in\R$. Ainsi, $X^\alpha$ suit une loi de Fréchet de paramètre $\dfrac{1}{\alpha}$.

### Question 5 {.answer}

 i. Comme $X$ est positive, d'après la première partie et la question précédente, $X^{\alpha} \in \mathcal{L}^1$ ssi $1-F_{\frac{1}{\alpha}}$ est intégrable sur $\R_+^\ast$ (inclure ou non $\{0\}$ ne change rien).
    
    La convexité de l'exponentielle nous assure que pour tout $x\in\R$, $$1 + x \leq e^x \leq 1 + x\,e^x.$$
    Ainsi, pour tout $x > 0$ on a
    $$x^{-\frac{1}{\alpha}}\,\exp\left\{-x^{-\frac{1}{\alpha}} \right\} \leq 1 - F_{\frac{1}{\alpha}}(x) \leq x^{-\frac{1}{\alpha}}.$$
    En outre, pour tout $x\in\R$ on a aussi
    \begin{equation}
    0 < 1 - F_{\frac{1}{\alpha}}(x) \leq 1. \tag{2}
    \end{equation}

    * Soit $\alpha < 1$. La fonction d'intérêt $1-F_{\frac{1}{\alpha}}$ est positive et majorée sur $\R_+^\ast$ par $$x\in\R_+^\ast \mapsto \left|\begin{array}{ll} x^{-\frac{1}{\alpha}} & \text{si } x > 1,\\ 1 & \text{si } 0< x \leq 1.\end{array}\right.$$ Or, quand $\alpha < 1$, cette dernière fonction est bien intégrable (par morceaux) sur $\R_+^\ast$. Par le critère d'intégrabilité dominée, $1-F_{\frac{1}{\alpha}}$ l'est donc également. On en conclut que le "si" de l'équivalence à démontrer est vrai.

    * Soit $\alpha \geq 1$. On a $\exp\left\{-x^{-\frac{1}{\alpha}}\right\} \to 1$ lorsque $x\to +\infty$ ; il existe donc $x_0 > 0$ tel que pour tout $x>x_0$ on a $\exp\left\{-x^{-\frac{1}{\alpha}}\right\} > \frac{1}{2}$. Or la fonction $x \mapsto \frac{1}{2}\,x^{-\frac{1}{\alpha}}$ n'est pas intégrable sur $]x_0, +\infty[$ pour $\alpha \geq 1$. Comme elle minore $1-F_{\frac{1}{\alpha}}$ sur ce même intervalle, $1-F_{\frac{1}{\alpha}}$ n'y est pas non plus intégrable. A fortiori, elle ne l'est donc pas non plus sur tout $\R_+^\ast$. On en conclut que le "seulement si" de l'équivalence recherchée est vrai lui aussi.  

    Finalement, nous avons bien $X^{\alpha} \in \mathcal{L}^1$ ssi $\alpha < 1$.

 ii. Soit $\alpha < 1$. Ici, il est plus facile d'utiliser la définition de $\Esp\left(X^\alpha\right)$ faisant intervenir la densité de $X^\alpha$. Puisque $F_{\frac{1}{\alpha}}$ est continue et dérivable partout, il en existe bien une, qui coïncide avec la dérivée de $F_{\frac{1}{\alpha}}$ :
 $$f_{\frac{1}{\alpha}} : x \in \R \mapsto \left|\begin{array}{ll} \frac{1}{\alpha}\,x^{-\frac{1}{\alpha}-1}\,\exp\left\{-x^{-\frac{1}{\alpha}} \right\} & \text{si } x > 0,\\ 0 & \text{sinon.}  \end{array}\right.$$
 Alors
 $$\Esp\left(X^\alpha\right) = \int_\R x\,f_{\frac{1}{\alpha}}(x)\,dx = \int_{0}^{+\infty} \dfrac{1}{\alpha}\,x^{-\frac{1}{\alpha}}\,\exp\left\{-x^{-\frac{1}{\alpha}} \right\}\,dx,$$
 et par le changement de variable $u = x^{-\frac{1}{\alpha}}$ on obtient directement
 $$\Esp\left(X^\alpha\right) = \int_0^{+\infty} u^{-\alpha}\,\exp\left\{-u\right\} \,du = \Gamma\left(1 - \alpha \right).$$

### Question 6 {.answer}

i. Lorsque $x\to+\infty$,
$$1-F(x) = 1-F_{\xi}(x) = 1 - \exp\left\{ -x^{-\xi}\right\} = 1 - \left( 1 - x^{-\xi} + o(x^{-\xi}) \right) \sim x^{-\xi}.$$
Par conséquent, pour tout $x>1$, lorsque $t\to+\infty$, on a
\begin{align*}
\P\left(X > xt \mid X > t \right) &= \dfrac{\P\left(X > xt\right)}{\P\left(X > t\right)} = \dfrac{1 - F(xt)}{1-F(t)} \sim \dfrac{x^{-\xi}\,t^{-\xi}}{t^{-\xi}} = x^{-\xi}.
\end{align*}

ii. D'après la question 5, $X$ a la même loi que $Y^{\frac{1}{\xi}}$, où $Y$ suit une loi de Fréchet standard. On a donc $X^\alpha\in\mathcal{L}^1$ ssi $Y^{\frac{\alpha}{\xi}} \in \mathcal{L}^1$, qui est équivalent, d'après la question 5.i, à $\alpha < \xi$. 

iii. Ces résultats illustrent pourquoi la loi de Fréchet est dite *à queue épaisse* : $1-F_\xi$ décroit lentement vers $0$, à la même vitesse que l'inverse d'une fonction puissance, et ce d'autant plus que $\xi$ est petit. Puisque pour tout $x\in\R$, $1-F_{\xi}(x) = \P\left(X > x\right)$, cela signifie que les événements extrêmes que sont les dépassements de très grandes hauteurs d'eau (qui auraient des conséquences environnementales, sociales, économiques dramatiques) ne sont pas si rares que ça. En particulier, lorsque $\xi \leq 1$, ils sont tellement fréquents que $X$ n'admet pas d'espérance ; cela n'a plus de sens de définir un comportement moyen lorsque la variabilité est trop grande. En outre, la convergence $\P(X>xt\mid X>t) \to x^{-\xi}$ quand $t\to+\infty$ et $x>1$ indique que sachant qu'une crue exceptionnelle a déjà eu lieu, la probabilité d'en observer une plus importante encore reste (relativement) élevée. Le choix de la loi de Fréchet pour modéliser la hauteur d'eau maximale de la Seine permet donc de se prémunir des risques dans le cadre du changement climatique.

**Remarque.** On se rend encore plus compte de l'aspect "queue épaisse" si on compare $1-F_\xi$ à $1-\Phi$, où $\Phi$ est la fonction de répartition d'une gaussienne centrée réduite, de densité $\varphi$. En effet, nous avons vu en TD que quand $x\to+\infty$, $$1-\Phi(x) \sim \dfrac{\varphi(x)}{x} = \dfrac{1}{\sqrt{2\pi}\,x}\,\exp\left\{-\dfrac{x^2}{2}\right\},$$
qui décroit exponentiellement vite vers $0$. Ainsi, pour $x\to+\infty$ on a
$$\dfrac{1-F_\xi(x)}{1-\Phi(x)} \sim \dfrac{x^{1-\xi}}{\sqrt{2\pi}}\,\exp\left\{\dfrac{x^2}{2}\right\},$$
qui tend d'autant plus vite vers $+\infty$ que $\xi$ est petit, c'est-à-dire que la queue de la distribution de $X$ est épaisse.
    
### Question 7 {.answer}

  i. Soit $x\in\R$, alors par indépendance et même distribution que $X$ des variables aléatoires $X_1,\dots,X_n$ on a
  \begin{align*}
  \P\left( M_n \leq x \right) &= \P\left( \max_{1\leq i \leq n} X_i \leq x \right) = \P\left( X_1\leq x,\dots, X_n \leq x \right)\\
  & = \prod_{i = 1}^n \P\left( X_i \leq x \right) = \P\left(X \leq x\right)^n= F_\xi(x)^n\\
  & = \exp\left\{ -n\,x^{-\xi}\right\} = \exp\left\{ -\left(n^{-\frac{1}{\xi}}\,x\right)^{-\xi} \right\}\\
  &= F_\xi\left( n^{-\frac{1}{\xi}}\,x \right).
  \end{align*}    
  Par conséquent, si l'on pose $a_n = n^{-\frac{1}{\xi}}$ on obtient bien
  $$\P\left(a_n\,M_n \leq x \right) = \P\left(n^{-\frac{1}{\xi}}\,M_n \leq x \right) = \P\left(M_n \leq n^{\frac{1}{\xi}}\,x \right) = F_\xi (x),$$
  ce qui signifie que $a_n\,M_n$ a la même loi que $X$.

  ii. En utilisant les questions 6.i et 7.i, quand $x\to+\infty$ on a directement
  \begin{align*}
  \dfrac{\P\left(M_n > x\right)}{n\,\P\left(X > x \right)} &= \dfrac{1}{n}\,\dfrac{1 - \P\left(M_n \leq x\right)}{1 - \P\left(X\leq x\right)} = \dfrac{1}{n}\,\dfrac{1 - F_\xi\left(n^{-\frac{1}{\xi}}\,x\right)}{1-F_\xi(x)} \\
  & \sim \dfrac{1}{n}\,\dfrac{\left(n^{-\frac{1}{\xi}}\,x\right)^{-\xi}}{x^{-\xi}} = 1.
  \end{align*}
  Ce résultat signifie que pour un seuil $x$ très grand, la hauteur d'eau maximale sur $n$ années a $n$ fois plus de chances de dépasser $x$ qu'en une seule année. Le risque de crue exceptionnelle croît de manière linéaire avec le nombre d'années écoulées.
    
### Question 8 {.answer}
    
Notons $\left(\mathcal{P}_n\right)$ l'équivalence à démontrer.

  * **Initialisation.**
    $\left(\mathcal{P}_1\right)$ est trivialement vraie.

  * **Hérédité.**
    Soit $n > 1$ et supposons que $\left(\mathcal{P}_{n-1}\right)$ est vraie. On fixe pour le moment $x>0$.

    On a l'inclusion des événements $$\Bigl(\{S_{n-1} > x\} \cup \{X_n > x\}\Bigr) \subset \{S_n > x\},$$
    qui combinée au caractère indépendant et identiquement distribué de $X_1,\dots,X_n$ donne
    \begin{align*}
    \P(S_n > x) &\geq \P\left( S_{n-1} > x \right) + \P\left(X_n > x \right) - \P\left(S_{n-1} > x, X_n > x \right)\\
    & = \P\left(S_{n-1} > x\right) + \P\left(S_{n-1} \leq x\right)\,\P\left(X > x \right).
    \end{align*}
    Ainsi, quand $x \to +\infty$, d'après $\left(\mathcal{P}_{n-1}\right)$ on a 
    \begin{align*}
    \dfrac{\P(S_n > x)}{n\,\P(X > x)} &\geq \dfrac{n-1}{n}\,\dfrac{\P\left(S_{n-1} > x\right)}{(n-1)\,\P\left(X > x\right)} + \dfrac{1}{n}\,\P\left(S_{n-1} \leq x\right)\\
    & \to \dfrac{n-1}{n} + \dfrac{1}{n} = 1.
    \end{align*}
    Par ailleurs, pour $\delta \in \left] 0, \frac{1}{2} \right[$ on a l'inclusion
    $$\{S_n > x\} \subset \{S_{n-1} > (1-\delta)x \} \cup \{X_n > (1-\delta)x \} \cup \{ S_{n-1} > \delta x, X_n > \delta x \},$$
    qui donne sous les hypothèses d'indépendance et de même loi de $X_1,\dots,X_n$
    \begin{align*}
    \P(S_n > x) &\leq \P\left(S_{n-1} > (1-\delta)x\right) + \P\left(X_n > (1-\delta)x\right)\\
    &\hspace*{2em} + \P\left(S_{n-1} > \delta x, X_n > \delta x\right)\\
    &= \P\left(S_{n-1} > (1-\delta)x\right) + \P\left(X_n > (1-\delta) x\right)\\
    &\hspace*{2em} + \P\left(S_{n-1} > \delta x\right)\,\P\left(X > \delta x\right).
    \end{align*}
    Par conséquent, quand $x\to+\infty$, d'après $\left(\mathcal{P}_{n-1}\right)$ et la question 6.i on a
    \begin{align*}
    \dfrac{\P(S_n > x)}{n\,\P(X>x)} &\leq \dfrac{\P\left(S_{n-1} > (1-\delta)x\right)}{n\,\P(X>x)} + \dfrac{\P\left(X > (1-\delta)x\right)}{n\,\P(X>x)}\\
    &\hspace{2em} + \dfrac{\P\left(X > \delta x\right)}{n\,\P(X>x)}\,\P\left(S_{n-1} > \delta x\right)\\
    & = (n-1)\dfrac{\P\left(S_{n-1} > (1-\delta)x\right)}{(n-1)\,\P(X> (1-\delta)x)}\,\dfrac{\P\left(X > (1-\delta)x\right)}{n\,\P(X>x)}\\
    &\hspace*{2em} + \dfrac{\P\left(X > (1-\delta)x\right)}{n\,\P(X>x)}\\
    &\hspace*{2em} + \dfrac{\P\left(X > \delta x\right)}{n\,\P(X>x)}\,\dfrac{\P\left(S_{n-1} > \delta x\right)}{(n-1)\,\P\left(X > \delta x\right)}\,(n-1)\,\P\left(X > \delta x\right)\\
    &\sim \left(\dfrac{n-1}{n} + \dfrac{1}{n}\right)\,(1-\delta)^{-\xi} + \dfrac{\delta^{-2\xi}}{n}\,(n-1)\,x^{-\xi} \\
    &\to (1-\delta)^{-\xi},
    \end{align*}
    qui tend vers $1$ lorsque $\delta \to 0$.

    Le théorème des gendarmes nous permet de conclure que $\left(\mathcal{P}_n\right)$ est vraie.

 * **Conclusion**. 
   La propriété $\left(\mathcal{P}_n\right)$ est vraie pour tout $n\in\mathbb{N}^\ast$.

   En combinant ce résultat avec celui de la question 7.ii on obtient $$\P\left(S_n > x\right) \sim \P\left(M_n > x\right)$$ quand $x\to+\infty$. Cela implique que la loi des excès du maximum domine celle de la somme. En d'autres termes, pour un très grand seuil $x >0$, l'événement extrême $\{S_n > x\}$ est essentiellement dû à l'événement $\{M_n > x\}$.
