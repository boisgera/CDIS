% Topologie

\newcommand{\R}{\mathbb{R}}

Structures Topologiques
================================================================================

### TODO

Remarque scalaires réels, extension plus tard au cas complexe.

### Norme {.definition}
Une *norme* sur un espace vectoriel $E$ est une application
$$\| \cdot \|: E \to \left[0, +\infty\right[$$
qui vérifie les trois axiomes suivants:

  - Séparation: $\|x\| = 0$ si et seulement si $x=0$,

  - Homogénéité: $\|\lambda x\| = |\lambda| \|x\|$ pour tous $\lambda \in \mathbb{R}$ et $x \in E$,

  - Inégalité triangulaire: $\|x+y\| \leq \|x\| + \|y\|$ pour tous $x \in E$ et $y \in E$.

### Produit scalaire {.definition}
Un *produit scalaire* sur un espace vectoriel $E$ est une application
$$\left< \cdot , \cdot \right>: E \times E \to \mathbb{R}$$
qui est

  - Bilinéaire symmétrique: pour tous $\lambda \in \mathbb{R}$ et $x, y, z \in E$:
    
      - $\left<x, y\right> = \left<y, x\right>$,

      - $\left<x, \lambda y\right> = \lambda \left<x, y\right>$

      - $\left<x, y + z\right> = \left<x, y\right> + \left<x, z\right>$.


  - Définie positive: pour tout $x \in E$, 
  
    - $\left<x, x \right> \geq 0$,

    - $\left<x, x \right> = 0$ si et seulement si $x=0$.

### TODO

Mq produit scalaire définit une norme.

### L'espace euclidien $\mathbb{R}^n$ {.remark}
L'ensemble $\mathbb{R}^n$ est un espace vectoriel de dimension finie
qui muni du produit scalaire
$$
\left<x,y\right> = x_1 y_1 + \dots + x_n y_n
$$
devient un *espace euclien*; la norme associée vérifie
$$
\|x\| = \sqrt{x_1^2 +\dots + x_n^2}.
$$


### Remarque

Terminologie evn, espace métriques regroupées après coup ? Et référence
au cas plus général en annexe ?

**TODO:** limitation des evn, sous-ensembles d'evn, nouvelle
structure, et plus tard (?) comment espace métrique n'est pas plus
général (à une isométrie près). Convention (légèrement abusive)
qui consiste à appeler espace métrique sous-ensembles d'un evn.

Continuité et Limite
================================================================================

### TODO 

(que dire sur limite ? Cadre général exclu ici ...
Au minimum, indispensable limite de suite. 
Qui du reste ? fonctions $X \to Y$, etc ? 
Montrer en exercice que des cas "limite en $\infty$" se ramènent à ça ?
L'idée que la notion de limite peut tjs être ramenée à une limite de
type limite quand on tend vers un point est intéressante.)

### Limite d'une suite {.definition}
Une suite $x_k$ de valeurs d'un espace métrique $X$ est *convergente*
si elle a une *limite*, c'est-à-dire un élement de $x$ de $X$
dont $x_{k}$ soit arbitrairement proche à partir d'un certain rang,
c'est-à-dire vérifiant: pour tout $\varepsilon > 0$, il existe un entier $n$ 
tel que pour tout $k \geq n$, on ait $\|x_k - x\| \leq \varepsilon$.

### Unicité de la limite {.proposition}
Si une suite $x_k$ admet une limite, celle-ci est unique.

### Démonstration {.proof}
Par l'inégalité triangulaire, pour tout entier $k$ on a
$$
\|x - x'\| \leq \|x - x_k\| + \|x' - x_k\|.
$$
Les points $x$ et $x'$ étant deux limites de $x_k$, 
pour tout $\varepsilon > 0$, il existe des rangs $n$ et $n'$ tels que
lorsque $k \geq n$ et $k\geq n'$, on a $\|x - x_k\| \leq \varepsilon /2$
et $\|x' - x_k\| \leq \varepsilon /2$. Par conséquent, pour 
$k = \max(n, n')$, on a
$\|x - x'\| \leq \varepsilon$. La valeur $\varepsilon > 0$ étant arbitraire,
on en déduit que $\|x - x'\|= 0$, soit par séparation, $x=x'$.

### TODO

Continuité cadre métrique/métrique.

Bestiaire
================================================================================

**TODO**

  - ouvert, fermé, voisinage, compact (?), adhérence, intérieur, frontière

  - point isolé, d'accumulation, ensemble dense, etc.

**TODO.** Partir de la notion de limite, définir l'adhérence, et le reste
à partir de ça, puis "découvrir" les définitions "directes"/séquentielles.

### Définitions séquentielles

  - Un ensemble $F$ est *fermé* si la limite de toute suite convergente de $F$
    appartient à $F$.

  - Un ensemble $V$ est un *voisinage* d'un point $x$ de $X$ si toute
    suite convergeant vers $x$ appartient à $V$ à partir d'un certain rang.

  - Un ensemble $O$ est *ouvert* si tout suite convergeant vers une
    limite appartenant à $O$ appartient à $O$ à partir d'un certain rang.

  - Un ensemble $K$ est *compact* si toute suite de $K$ admet une sous-suite
    convergente.

  

Complétude
================================================================================

### TODO:

  - evn, espace métrique (comme sous-ensemble d'un e.v.n.), 
    suite de Cauchy, complétude

  - application lipschitzienne, (et lip est cont) contractante, 
    $\kappa$-contractante

### Suite de Cauchy {.definition}
Une suite de points $x_k$ est *de Cauchy* si pour tout
$\varepsilon > 0$, 
il existe un rang $m$ tel que pour tous les entiers $n \geq m$ et $p \geq m$, 
$\|x_n - x_p\| \leq \varepsilon$. 

### Diamètre {.definition}
Le diamètre d'un sous-ensemble $A$ d'un espace vectoriel normé est donné par:
$$
\mbox{diam}(A) = \sup \, \{\|x - y \| \, | \, x \in A, \, y \in A\}
$$

### Suite de Cauchy et diamètre {.proposition}
Une suite de points $x_k$ est de Cauchy si et seulement si
$$
\lim_{k \to + \infty} \mbox{diam}(\{x_n \, | \, n \geq k \}) = 0.
$$

### Complétude {.definition}
Un espace métrique $X$ est *complet* si et seulement si tout suite de Cauchy
est convergente.

### Application contractante {.definition}
Une fonction $f: X \to X$ est *$\kappa$-contractante*, 
où $\kappa \in \left[0, 1\right[$,
si pour tout couple de points $x$ et $y$ de $X$, on a 
$$
\|f(x) - f(y)\| \leq \kappa \|x - y\|.
$$
Une telle application est *contractante* si elle est 
$\kappa$-contractante pour un $\kappa \in \left[0, 1\right[$.

### Théorème de Point Fixe de Banach {.definition .theorem #T-TPFB}

Soit $f: E \to E$ une application contractante dans un espace métrique $E$.
Si l'espace $E$ est complet, l'application $f$ admet un unique *point fixe* $x$,
c'est-à-dire une unique solution $x \in E$ à l'équation
  $$
  x = f(x).
  $$

### Démonstration {.proof}

L'unicité du point fixe (l'existence d'au plus une solution à $x=f(x)$) est
simple à établir: si $x$ et $y$ sont deux points fixes de $f$, c'est-à-dire 
si $x=f(x)$ et $y=f(y)$, alors $\|x - y\| = \|f(x) - f(y)\|$. 
L'application $f$ étant $\kappa$-contractante, on a donc
$$
\|x - y\| = \|f(x) - f(y)\| \leq \kappa \|x - y\|;
$$
et puisque $0\leq \kappa < 1$, cette inégalité entraîne $\|x - y\| = 0$, 
soit $x=y$.

Quant à l'existence du point fixe, sa preuve est constructive: 
nous allons établir que quel que soit le choix de $x_0 \in E$, 
la suite de valeurs définie par
$$
x_{n+1} = f(x_n)
$$
converge vers le point fixe. 
Le point crucial est d'établir que cette suite
admet une limite $x_{\infty}$; en effet, si ce résultat est acquis, 
en passant à la limite sur $n$ dans la relation de récurrence, 
et exploitant la continuité de l'application $f$, on obtient
$$
x_{\infty} = \lim_{n \to +\infty} x_{n+1} = \lim_{n \to +\infty}f(x_n) = f(x_{\infty}).
$$
A cette fin, nous allons prouver que la suite des $x_n$ est de Cauchy; 
l'existence d'une limite se déduira alors de la complétude de $E$. 
On remarque tout d'abord que pour tout entier $n$, 
$$
\|x_{n+2} - x_{n+1}\| = \|f(x_{n+1}) - f(x_n)\| \leq \kappa \|x_{n+1} - x_n\|,
$$
ce qui par récurrence fournit pour tout $n$
$$
\|x_{n+1} - x_n\| \leq \kappa^n \|x_1 - x_0\|.
$$
Par conséquent, pour tout couple d'entiers $n$ et $p$, on a
$$
\|x_{n+p} - x_n\| 
\leq \sum_{k=0}^{p-1} \|x_{n+k+1} - x_{n+k}\|
\leq \sum_{k=0}^{p-1} \kappa^{n+k} \|x_{1} - x_{0}\|.
$$
Dans le second membre apparaît une somme de termes d'une suite géométrique:
$$
\sum_{k=0}^{p-1} \kappa^{n+k} = \kappa^n \frac{1 - \kappa^{p}}{1 - \kappa}
\leq \frac{\kappa^n}{1 - \kappa};
$$
on en déduit
$$
\|x_{n+p} - x_n\| 
\leq  
\frac{\kappa^n}{1 - \kappa} \|x_{1} - x_{0}\|.
$$
Le second membre de cette inégalité tendant vers $0$ indépendamment de $p$
quand $n$ tend vers $+\infty$, la suite des $x_n$ est bien de Cauchy, ce
qui conclut la preuve.

Compacité
================================================================================

### Compacité {.definition}
Un ensemble $E$ est *compact* si toute suite de valeurs de 
$E$ admet une sous-suite convergeant dans $E$.

### Image d'un compact {.theorem}
L'image d'un ensemble compact par une application continue est un ensemble
compact.

### Existence d'un minimum {.corollary #T-EM}
Une fonction continue $f: K \to \mathbb{R}$ définie sur un ensemble compact 
$K$ admet un minimum global.

### Théorème de Heine-Borel {.theorem}
Un ensemble $E$ de $\R^n$ est compact 
si et seulement si il est fermé et borné.

Annexe
================================================================================

### Remarque {.anonymous}

**TODO.** quantitatif contre qualitatif
$$
d(x, A) = 0
$$



### Topologie {.definition}

Une relation de *proximité* sur un ensemble $E$ est une relation 
entre points de $E$ et ensembles de $E$ vérifiant les axiomes 
suivants:

 1. Aucun point n'est proche de l'ensemble vide,

 2. Tout point d'un ensemble est proche de cet ensemble,

 3. Un point est proche de l'union de deux ensembles 
    si et seulement s'il est proche d'au moins l'un 
    des deux ensembles,

 4. Un point proche de l'ensemble des points proches d'un ensemble
    est adhérent à l'ensemble.

L'ensemble $E$ muni d'une relation de proximité est un *espace topologique*.
    
### Adhérence {.definition}

On appelle *adhérence* d'un ensemble $A$
l'ensemble $\overline{A}$ des points adhérents à $A$.



### Calcul Topologique
Une fonction $\overline{\, \cdot \,}: \mathcal{P}(E) \to \mathcal{P}(E)$ est 

 1. $\overline{\varnothing} = \varnothing$,

 2. $A \subset \overline{A}$,

 3. $\overline{A \cup B} = \overline{A} \cup \overline{B}$,

 4. $\overline{\overline{A}} = \overline{A}$.



Exercices
================================================================================

Comparaison des normes
--------------------------------------------------------------------------------

TODO: comparaison manuelle, meilleure bornes

Plongement de Kuratowski
--------------------------------------------------------------------------------

Nous souhaitons établir le résulat suivant: tout espace métrique peut être
identifié à un sous-ensemble d'un espace vectoriel normé tout en préservant 
sa distance.

Soit $X$ un espace métrique et $x_0$ un point de $X$. 
On associe à l'élément $x$ de $X$ la fonction $f_x: X \to \R$ définie
par
$$
f_x(y) = d(x, y) - d(x_0, y).
$$

 1. Montrer que la fonction $x \mapsto f_x$ est injective.

 2. Montrer que pour tout point $x$ la fonction $f_x$ est bornée.

 3. Montrer que l'espace vectoriel $E$ des fonctions bornées de $X$ dans 
    $\mathbb{R}$ est un espace vectoriel qui peut être muni de la norme 
    $\| \cdot \|_{\infty}$ définie par
    $$
    \|f\|_{\infty} = \sup \, \{|f(y)| \, | \, y \in X\}.
    $$

 4. Montrer que $x \mapsto f_x$ est une isométrie, 
    c'est-à-dire que pour tout $x$ et
    $y$ dans $X$, on a 
    $$
    d(x, y) = \|f_x - f_y\|_{\infty}.
    $$

Point fixe
--------------------------------------------------------------------------------

Soit $f: E \to E$ une fonction définie et à valeurs dans un espace métrique 
complet $E$ pour laquelle il existe un entier $n \geq 1$ tel que la composée 
$n$ fois de $f$ avec elle-même, notée $f^n$, est contractante. 

On souhaite montrer que sous ces hypothèses 
-- qui généralisent celles du [théorème de point fixe de Banach](#T-TPFB) -- 
$f$ admet encore un unique point fixe.

 1. Montrer que tout point fixe éventuel de $f$ est également 
    un point fixe de $f^n$.

 2. Montrer que $f^n$ admet un unique point fixe et qu'il est également
    un point fixe de $f$.

 3. Montrer que le procédé habituel pour construire un point 
    fixe de $f$ est toujours valable quand $f^n$ est contractante.


Normes d'opérateurs
--------------------------------------------------------------------------------

Changer les normes au départ et à l'arrivée, calculer les normes d'opérateurs
associées sur la base d'une représentation matricielle (ex: norme sup au 
départ et à l'arrivée)

En lien avec les résolutions itératives de systèmes linéaires,
utiliser / montrer que pour tout $A \in \R^{n\times n}$
et tout $\varepsilon > 0$, il existe une norme matricielle 
$\|\, \cdot \, \|$ telle que $\|A\| \leq \rho(A) + \varepsilon$.

Voir aussi <https://math.stackexchange.com/questions/126460/iteration-convergence>

Fonctions définies par un recouvrement
--------------------------------------------------------------------------------

Soit une fonction définie par la donnée de 
ses restrictions $f_A$ aux ensembles $A \in \mathcal{A}$.
Ce procédé permet de définir uniquement la fonction $f$ sur l'ensemble
$$
\mbox{dom}(f) = \bigcup_{A \in \mathcal{A}} A
$$
à condition que les restrictions soient compatibles
$$
x\in A \cap B, \, A \in \mathcal{A}, \, B \in \mathcal{A}
\, \Rightarrow \, 
f_A(x) = f_B(x).
$$

  1. On suppose que les fonctions $f_A$, $A \in \mathcal{A}$ sont continues.
     Est-ce que la fonction $f$ est nécessairement continue ?
     Dans le cas contraire, quelle condition "raisonnable" portant sur
     la collection $\mathcal{A}$ peut-on ajouter pour s'assurer du résultat ?

  2. Application angle sur l'hélice et $\arctan$ ...


Equations Linéaires et Point Fixes
--------------------------------------------------------------------------------

Préparer et résoudre numériquement des systèmes de la forme $A x = b$ dans
des cas simples (ex: Jacobi, Gauss-Seidel, cas diagonally dominant ?).

Exemples concrets (ex: Poisson Image editing) et exemples ou "ça ne marche pas"
en itérant sans s'assurer du caractère contractant. 

Prendre un exemple de petite dimension associé au PIE; admettre le résultat
que $\|A^k\| \to 0 \Leftrightarrow \rho(A) < 1$ et tester algo de Jacobi
(Au préalable, calculer norme de l'opérateur via la svd ?).

Lien norme d'opérateur et rayon spectral ??? Cf supra sur rayon spectral
et lien avec norme.


Nombres Réels de Bishop ?
--------------------------------------------------------------------------------

(illustration des suites de Cauchy ?)

"Localement"
--------------------------------------------------------------------------------

Etude des pptés "localement X" pour X=bornée, positive (ex: distance), 
coup de la stabilité asympt (localt equi-convergente ?), 
localement unift continue, etc.
et comment elle s'étendent à un ensemble d'adhérence compacte 
("compactement inclus" dans l'espace de référence).

"Contre-exemples" ? Avec "localement constant", "localement polynomial", 
"localement lipschitz" etc., opérations qui ne sont pas stables par union 
finie. 

Compacité et Continuité
--------------------------------------------------------------------------------

Montrer la réciproque du [résultat d'existence d'un minimum pour une fonction
numérique continue définie sur un compact](#T-EM):
si l'ensemble $E \subset \mathbb{R}^n$ n'est pas compact, 
il existe une fonction continue $f: E \to \mathbb{R}$ 
n'ayant pas de minimum.



Fonctions propres
--------------------------------------------------------------------------------

Soit $f: \mathbb{R}^n \to \mathbb{R}$ une fonction continue et propre,
c'est-à-dire telle que
$$
f(x) \to +\infty \mbox{ quand } \|x\| \to +\infty.
$$

Montrer que les ensembles de sous-niveaux de $f$, de la forme
$$
\{x \in \mathbb{R}^n \, | \, f(x) \leq c\} \, \mbox{ où } \, c \in \mathbb{R}
$$
sont compacts.

Solutions aux Exercices
================================================================================

Solution -- [Point fixe]
--------------------------------------------------------------------------------

 1. Si $x$ est un point fixe de $f$, $f(x) = x$, par conséquent
    $$
    f^2(x) = f(f(x)) = f(x) = x, 
    $$
    puis
    $$
    f^3(x) = f(f^2(x)) = f(x) = x,
    $$
    etc. Par récurrence, il est clair que l'on peut établir que pour tout
    $n \geq 1$, on a $f^n(x) = x$: $x$ est un point fixe de $f^n$.

 2. La fonction itérée $f^n$ satisfait les hypothèses du 
    [théorème du point fixe de Banach](#T-TPFB), par conséquent elle
    admet un point fixe $x$. Comme $f^n(x) = x$, en applicant $f$ aux
    deux membres de cette équation, on obtient 
    $$
    f(f^n(x)) = f^n(f(x)) = f(x).
    $$
    Par conséquent, $f(x)$ est un point fixe de $f^n$. 
    C'est donc l'unique point fixe $x$ de $f^n$; on a donc $f(x) = x$,
    c'est-à-dire que $x$ est un point fixe de $f$. 

 3. Le "procédé habituel pour construire un point fixe de $f$" 
    consiste à prendre un $x_0 \in E$ quelconque et à construire 
    par récurrence la suite des $x_{k+1} = f(x_k)$. 
    On souhaite donc montrer que cette suite converge vers l'unique point fixe 
    $x$ de $f$. 
    La fonction $f^n$ satisfaisant les hypothèses du
    [théorème du point fixe de Banach](#T-TPFB), 
    on sait que la suite extraite
    $(x_{kn})_k$ converge vers $x$, car $x_{(k+1)n} = f^n(x_{kn})$.
    Il en est de même pour la suite extraite $(x_{kn+1})_k$, construite
    à partir du même procédé mais en initialisant la séquence avec 
    la valeur $x_1$, pour la suite $(x_{kn+2})_k$, ..., jusqu'à 
    $(x_{kn + (n-1)})_k$. Ces $n$ suites convergent toutes vers $x$,
    donc la suite des $(x_k)_k$ converge également vers le point fixe $x$, 
    comme sous les hypothèses du [théorème du point fixe de Banach](#T-TPFB).