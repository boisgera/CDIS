% Calcul Différentiel III

TODO, à trier, idées en vrac:

  - e.v.n fonctionnels ($C^k$, $L^1$, $L^2$, etc.), Hilbert, Banach.

  - opérateurs linéaires continus (bornés), adjoint (appli calcul diff, 
    par exemple pour calcul solution diff EDP sans recalcul ?)
   
  - différentielle (Fréchet), cas général

En fait va plus loin que le scope du calcul diff, 
contient un mini "topo en dim infinie" (qu'est-ce qui change ?
Compacité (en particulier ppté vraie sur les compacts ne donne plus
le semi-global, ppté de type Ascoli-Arzela pour caractériser la compacité
pour les fcts continues), non-équivalence des normes, dualité, 
topologie faible ?) 
et algèbre linéaire en dim infinie (opérateurs linéaires 
ne sont pas tous cont., pas de chance ... Hilbert, Banach, etc). 

Prérequis: Topo, Calcul Diff dim finie, sans doute l'intégrale
(les critères intégraux sont une grande motivation pour enseigner
le calcul diff en dim infinie), c'est aussi sans doute l'endroit
ou on veut parler de la complétude des espaces comme $L^1 / L^2$, 
etc.

Exemples à traiter: "interpolation" données non-paramétrique, 
calcul des variations, maximum entropie sous contrainte, 
diff. / chemin (ex: usage en analyse complexe), 
optimisation/gradient forme, etc. Autre exemple: quantif 
qui optimise le SNR ou l'entropie. Autre exemple: Pb de Dirichlet
variationel ? On peut faire ça ? Et lier ça au Laplacien ? 
Ou il il faut un cadre compliqué (trace & co) ?

Articulation avec Physique Fonda. et Appliquée (calc var, Hilb, etc.).
Volonté de permettre de comprendre des trucs comme la construction de
Fourier (prolgt opé lin con à partir d'un ensemble dense avec majoration),
ou typiquement, définition de la trace sur un bord régulier ...

  - Topo en dim infinie, Banach, Hilbert, opérateurs lin cont, 
    analyse spectrale

  - Calcul diff en dim infinie (acc. fini, cont df, inversion locale, 
    point critique et multiplicateurs de lagrange, etc.,
    tout ça revisité rapidement en se basant sur la familiarité
    avec la dim finie, déjà vue).

  - Equation de Poisson: intro Sobolev, pb "variationnel" en multivariable,
    trace, etc. Evocation schéma résolution numérique (élt finis) ?

  - Cadre Méca Q, opérateurs (non bornés) hermitien, semi-groupes (unitaires)
    fortement continus, etc?

<!-- LaTeX Macros -->
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}

--------------------------------------------------------------------------------

TODO -- Espaces de Hilbert/Banach
================================================================================

### Espace de Hilbert {.definition}
On appelle *espace de Hilbert* tout espace vectoriel muni d'un produit scalaire
qui soit complet.

### Espace de Banach {.definition}
On appelle *espace de Banach* tout espace vectoriel normé qui soit complet.

### Fonctions de class $C^k$ {.definition}
Soit $K$ un ensemble compact de $\R^n$ d'intérieur $V$, supposé *régulier*,
c'est-à-dire tel que $\overline{V} = K$.
On note $C^k(K, \R^m)$ l'espace des fonctions $f$ définies sur $K$, 
dont la restriction à $V$ est $k$-fois continûment différentiable et
dont les dérivées partielles $\partial^{\alpha} f$, $|\alpha| \leq k$ 
sont prolongeables en une fonction continue sur $K$ (toujours notée
$\partial^{\alpha} f$). Cet espace vectoriel est muni de la norme
$$
\|f\|^k_{\infty} = \sum_{|\alpha| \leq k} \|\partial^{\alpha} f\|_{\infty}
= \sum_{|\alpha| \leq k} \max_{x \in K} \|\partial^{\alpha} f(x)\|_{\R^m}.
$$

### TODO
Alternative avec fct définies uniquement sur l'intérieur + continuité uniforme ?
Bof (ou alors en exo, bon test pour la continuté uniforme). 
Mais on peut constater après coup que les objets dont on dispose sont 
uniformément continus (on a a besoin pour le calcul des variations).

### L'espace $C^k$ est complet {.proposition}
Soit $K$ un ensemble compact régulier de $\R^n$ ;
l'espace $C^k(K, \R^m)$ est complet.

### TODO -- Démonstration {.proof}

### Continuité uniforme {.definition}
Une fonction $f: X \to Y$, où $X$ et $Y$ sont des espaces métriques est 
*uniformément continue* si pour tout $\varepsilon > 0$, il existe un $r >0$
tel que, pour tous $x, y \in X$, si
$d(x, y) \leq r$, alors $d(f(x), f(y)) \leq \varepsilon.$

### {.ante}
De toute évidence, la continuité uniforme implique la continuité ; 
dans le cas de fonctions définies sur un ensemble compact, la réciproque
est valable:

### Continuité uniforme et compacité
Soient $X$ et $Y$ deux espaces métriques et $K \subset X$ un ensemble compact;
toute fonction $f: K \subset X \to Y$ qui est continue est uniformément continue.

### Démonstration 
Supposons au contraire qu'il existe un $\varepsilon>0$ 
tel que pour tout $k \in \N$ il existe $x_k$ et $y_k$ dans $K$ 
tels que $d(x_k, y_k) \leq 2^{-k}$, mais $d(f(x_k), f(y_k)) > \varepsilon$. 
Par compacité de $K$, la suite $x_k$ admet une suite extraite qui converge
vers un $\ell \in K$ ; la suite correspondante extraite de $y_k$ converge
également vers $\ell$. 
Comme $d(f(x_k), f(y_k)) \leq d(f(x_k), f(\ell)) + d(f(y_k), f(\ell))$,
la continuité de $f$ en $\ell$ impose qu'il existe un $k$ tel que
$d(f(x_k), f(y_k)) \leq \varepsilon$, ce qui contredit l'hypothèse initiale.



TODO -- Autres
--------------------------------------------------------------------------------

$L^1$, $L^2$, $L^{\infty}$ ($L^p$ ?)
Dans le cadre général ? (ens de départ ?)

$C^0$, $C^k$, etc. Hölder $C^{k,\alpha}$ ? 
Sur sous-ensemble compact de $\R^n$ ?

Sobolev (sur $\R^n$) ? Sur $\Omega$ par densité ? (ouch)

Espaces d'opérateurs: $E \stackrel{\ell}{\to } F$.


Exemple d'opérateurs bornés (ici et en exercice): les identités
($C^0 \to L^1$, $L^2 \to L^1$), l'intégrale ($L^1 \to \R^n$)

Technique de définition d'un opérateur borné par densité.

Liste de sous-ensembles denses (en particulier, 
fcts lisses à support compact ...)

Exemple techniques densité pour définir un truc ? et/ou étendre une
relation (exemple: IPP pour fcts avec dérivées faibles ? Fourier ?)

TODO -- Opérateurs Bornés
================================================================================

Opérateurs définis sur un domaine $D(A)$ dense 
(certains bornés, d'autres non). Applis méca Q ?

Opérateurs bornés, cas particulier des "inclusions"
(fonction identité, différente norme au départ et à l'arrivée)


Différentielle
================================================================================

### Différentielle de Fréchet {.definition}
Soient $E$ et $F$ deux espaces vectoriels normés et $U$ un ouvert de $E$.
La fonction $f: U \to F$ est *différentiable en $x \in U$* s'il existe
une application linéaire continue, notée $df(x)$ et appellée 
*différentielle de $f$ en $x$*, telle que
$$
f(x+h) = f(x) + df(x) \cdot h + o(\|h\|_E),
$$
c'est-à-dire si 
$$
\lim_{h \to 0} \frac{\|f(x+h) - f(x) - df(x) \cdot h\|_F}{\|h\|_E} = 0.
$$

### TODO

Reprendre les règles de calcul de la dimension finie

### TODO -- Règle de différentiation en chaîne {#rdc}

### TODO -- Pt critique et minimum {#rdc}

### Théorème des Fonctions Implicites {.theorem #TFI-2}
Soient $E$, $F$ et $G$ trois espaces vectoriels normés, $F$ étant complet, 
et $f$ une fonction définie sur un ouvert $W$ de $E \times F$
$$
f: (x, y) \in W \subset \mathbb{R}^n \times \mathbb{R}^m \to f(x, y) \in \mathbb{R}^m
$$
qui soit continûment différentiable et telle que la différentielle partielle
$\partial_y f$ soit inversible et d'inverse continu en tout point de $W$.
Si le point $(x_0, y_0)$ de $W$ vérifie $f(x_0, y_0)= 0$,
alors il existe des voisinages ouverts $U$ de $x_0$ et $V$ de $y_0$ tels que
$U \times V \subset W$ et
une fonction implicite $\psi: U \to F$, continûment différentiable, 
telle que pour tous $x \in  U$ et $y \in V$,
$$
f(x, y) = 0
\; \Leftrightarrow \; 
y = \psi(x).
$$
De plus, la différentielle de $\psi$ est donnée pour tout $x \in U$ par
$$
d \psi(x) = - (\partial_y f(x, y))^{-1} \cdot \partial_x f(x, y) \, \mbox{ où } \, y=\psi(x).
$$

### Démonstration (esquisse) {.proof}
La démonstration est similaire au cas de la dimension finie: 
la construction de la solution $f(x, y) = 0$ en $y$ est
toujours basée sur la construction d'une suite d'approximations $y_k$ par 
la méthode (modifiée) de Newton. 
L'existence d'un point fixe à cette méthode repose sur le point fixe de Banach 
-- d'où l'hypothèse de complétude de $F$ -- 
et la caractère contractant de la fonction de Newton,
qui exploite la norme d'opérateur $\|(\partial_y f(x_0, y_0))^{-1}\|$
et donc la continuité de cet inverse.

### Formulation alternative {.remark}
On remarque que sous les hypothèses du théorème des fonctions implicites,
l'espace vectoriel normé $G$ est nécessairement complet. En effet, pour
toute suite de Cauchy $z_k$ dans $G$, comme $Q := \partial_y f(x_0, y_0)$
est inversible et d'inverse continu, $y_k := Q^{-1} \cdot z_k$ est de 
Cauchy dans $F$, complet par hypothèse; si $\ell$ désigne la limite de
cette suite, $Q \cdot \ell$ fournit une limite à la suite des $z_k$ dans
$G$.

Si l'on ajoute cette hypothèse 
-- inutile à ce stade, mais le plus souvent très simple à vérifier -- 
au théorème, on peut en retirer une autre, en général plus technique. 
En effet, un théorème dû à Stefan Banach affirme que toute fonction 
linéaire continue entre deux espaces de Banach qui est inversible
à un inverse continue.
Compte tenu de ce résultat, on peut reformuler l'énoncé du théorème
des fonctions implicites en omettant la vérification de l'inversibilité
de $\partial_y f$:


### Théorème des Fonctions Implicites {.theorem #TFI-2-alt}
Soient $E$, $F$ et $G$ trois espaces vectoriels normés, 
$F$ et $G$ étant complets, 
et $f$ une fonction définie sur un ouvert $W$ de $E \times F$
$$
f: (x, y) \in W \subset \mathbb{R}^n \times \mathbb{R}^m \to f(x, y) \in \mathbb{R}^m
$$
qui soit continûment différentiable et dont la différentielle partielle
$\partial_y f$ est inversible en tout point de $W$.
Si le point $(x_0, y_0)$ de $W$ vérifie $f(x_0, y_0)= 0$,
alors il existe des voisinages ouverts $U$ de $x_0$ et $V$ de $y_0$ tels que
$U \times V \subset W$ et
une fonction implicite $\psi: U \to F$, continûment différentiable, 
telle que pour tous $x \in  U$ et $y \in V$,
$$
f(x, y) = 0
\; \Leftrightarrow \; 
y = \psi(x).
$$
De plus, la différentielle de $\psi$ est donnée pour tout $x \in U$ par
$$
d \psi(x) = - (\partial_y f(x, y))^{-1} \cdot \partial_x f(x, y) \, \mbox{ où } \, y=\psi(x).
$$

### TODO

Nouvelle définition de la différentielle d'ordre supérieur, compatibilité avec
la dimension finie

### TODO

Développement de Taylor, Taylor avec reste intégral, etc.

Calcul des variations
================================================================================

<!--
 Notons $C^1(K,U)$ l'ensemble
$$
C^1(K,U) = \{f \in C^1(K, \R^m) \, | \, f(K) \subset U\}.
$$
-->

### Différentiation d'une composition {.lemma #duc}
Soit $K \subset \R^n$ un ensemble compact et $U \subset \R^m$ un ensemble
ouvert. Soit
$C^0(K,U) = \{f \in C^0(K, \R^m) \, | \, f(K) \subset U\}.$
Si la fonction $g: U \subset \R^m \to \R^p$ est continûment différentiable,
alors l'application
$$
G: f \in C^0(K,U) \mapsto g \circ f \in C^0(K,\R^p)
$$
est différentiable et
$$
d G(f) \cdot h = d (f \mapsto g \circ f)(f) \cdot h
=
(x \mapsto dg(f(x)) \cdot h(x)).
$$

### Expression de la différentielle {.remark}
Si l'on admet (temporairement) que l'application $G$ est différentiable,
il est possible de deviner quelle sera nécessairement son expression 
en se ramenant à du calcul différentiel en dimension finie.
Fixons pour cela un $x \in K$ arbitraire et définissons pour $k=m$ ou $n$
l'opérateur linéaire continu
$$
X: \phi \in C^0(K, \R^k) \to \phi(x) \in \R^k.
$$
Par définition de $G$, pour toute fonction $f$ on a 
$G(f)(x) = (g \circ f)(x) = g(f(x))$, soit $X(G(f)) = g(X(f))$, ou encore
$X \circ G = g \circ X$. Différencier cette dernière équation en $f$ 
pour la variation $h$, fournit
$$
d(X \circ G)(f)\cdot h = d(g \circ X)(f) \cdot h.
$$
Par la règle de différentiation en chaîne, comme $dX(\phi) = X$, on a donc
$$
X \cdot dG(f) \cdot h = dg(X(f)) \cdot X \cdot h,
$$
soit $(dG(f) \cdot h)(x) = dg(f(x)) \cdot h(x)$, 
ce qui est bien le résultat cherché.

### Démonstration {.proof}
Remarquons tout d'abord que le domaine de définition $C^1(K, U)$ de $G$ est bien un
sous-ensemble ouvert de l'espace vectoriel normé $C^1(K, \R^m)$,
il est donc possible d'envisager sa différentiabilité.
En effet, si $f \in C^1(K, U)$, l'image $f(K)$ est un sous-ensemble
compact de $U$ ; par conséquent, $\varepsilon := d(f(K), \R^m \setminus U) > 0$.
Si $h \in C^1(K, \R^m)$ et que $\|h\|^1_{\infty} < \varepsilon$, alors
$\|h\|_{\infty} < \varepsilon$ et par conséquent pour tout $x \in K$,
$\|h(x)\| < \varepsilon$. On a donc $(f + h)(x) \in U$ pour tout $x \in K$:
la boule ouverte centrée en $f$ et de rayon $\varepsilon$ dans $C^1(K, \R^m)$
est incluse dans $C^1(K, U)$.

Notons ensuite que $dg(f(x)) \cdot h(x)$ appartient à $C^0(K,\R^p)$
et que l'application $h \in C^0(K,\R^m) \mapsto dg(f(x)) \cdot h(x)$
est linéaire et continue ; on a en effet
$$
\begin{split}
\|dg(f(x)) \cdot h(x)\|_{\infty} 
&= \left\|\sum_{i} \partial_i g(f(x)) h_i(x)\right\| \\
&\leq \sum_{i} \|\partial_i g(f(x))\| \|h_i(x)\| \\
&\leq \left(\sum_i \|\partial_i g(f(x))\|\right) \|h(x)\| \\
& \leq \left(\max_{x \in K} \sum_i \|\partial_i g(f(x))\|\right) \|h\|_{\infty}.
\end{split}
$$

Soit $x \in K$ et $r>0$ (à déterminer) tel que $d(f(K), \R^m \setminus U) > r$.
La fonction
$$
h \in B(0, r) \subset \R^n \mapsto g (f(x)+ h) - g(f(x)) - dg(f(x)) \cdot h
$$
est alors bien définie, de différentielle $dg(f(x)+h) - dg(f(x))$.
Cette expression est une fonction continue
de $x \in K$ et de $h \in \overline{B(0, r)}$ ; elle est donc 
uniformément continue. Pour tout $\varepsilon > 0$, si $r$ est suffisamment
petit, $x \in K$ et $h \in B(0, r)$, 
$$
\|dg(f(x)+h) - dg(f(x))\| \leq \varepsilon.
$$
Par le théorème des accroissements finis, comme 
$$
g (f(x)+ 0) - g(f(x)) - dg(f(x)) \cdot 0 = 0
$$
on a donc
$$
\|g (f(x)+ h) - g(f(x)) - dg(f(x)) \cdot h\| \leq \varepsilon \|h\|.
$$
ce qui donne en substituant $h(x)$ à $h$ 
(où $h:K \to \R^m$ est désormais une fonction continue telle que
$\|h\|_{\infty} < r$)
$$
\begin{split}
\|g\circ (f+h) - g \circ f + (x \mapsto dg(f(x)) \cdot h(x)) \|_{\infty} &= \\
\|x \mapsto g (f(x)+ h(x)) - g(f(x)) + dg(f(x)) \cdot h(x) \|_{\infty} &\leq \varepsilon \|h\|_{\infty}
\end{split}
$$
ce qui prouve la différentiabilité de $f \mapsto g \circ f$ et la valeur de 
sa différentielle.

### Lagrangien {.definition}
On appelle *lagrangien* toute fonction continûment différentiable
$$
L: (t, y, \dot{y}) \in \R \times \R^n \times \R^n \to \R
$$
et *action* associée toute intégrale de la forme
$$
A(y) = \int_a^b L(t, y(t), \dot{y}(t)) \, dt
$$
où $a \leq b \in \R$ et $y \in C^1([a, b],\R^n)$.

### Différentielle de l'action {#da}
L'action $A: y \in C^1([a, b], \R^n) \to  \R$ 
est une fonction différentiable et
$$
dA(y) \cdot h = \int_a^b \partial_{y} L(t, y(t), \dot{y}(t)) \cdot h(t)+
\partial_{\dot{y}}  L(t, y(t), \dot{y}(t)) \cdot \dot{h}(t)
\, dt
$$

### Démonstration {.proof}
L'application
$$
y \in C^1([a, b], \R^n) \mapsto (t\mapsto t, y, \dot{y}) \in C^0([a, b], \R^{2n+1})
$$
est différentiable (car affine et continue), de différentielle
$$
h \in C^1([a, b], \R^n) \mapsto (0, h, \dot{h}) \in C^0([a, b], \R^{2n+1}).
$$
Le langrangien $L$ étant continûment différentiable, 
par [différentiation d'une composition](#duc), l'application
$$
\phi \in C^0([a, b], \R^{2n+1}) \mapsto L \circ \phi \in C^0([a, b], \R) 
$$
est différentiable, de différentielle
$$
\psi \in C^0([a, b], \R^{2n+1}) \mapsto (t \mapsto dL(\phi(t)) \cdot \psi(t)) \in C^0([a, b], \R).
$$
Par [la règle de différentiation en chaîne]{#rdc}, l'application
$y \in C^1([a, b], \R^n) \mapsto L \circ (t\mapsto t, y, \dot{y}) \in C^0([a, b], \R)$
est donc différentiable, de différentielle
$$
\partial_t L(t, y(t), \dot{y}(t)) \cdot 0 + 
\partial_y L(t, y(t), \dot{y}(t)) \cdot h(t) +
\partial_{\dot{y}} L(t, y(t), \dot{y}(t)) \cdot \dot{h}(t).
$$
L'application 
$$
f \in C^0([a, b], \R) \mapsto \int_a^b f(t) \, dt \in \R
$$
étant linéaire continue, à nouveau par application de 
[la règle de différentiation en chaîne]{#rdc}, l'action est différentiable, de différentielle
$$
dA(y) \cdot h = \int_a^b \partial_y L(t, y(t), \dot{y}(t)) \cdot h(t) +
\partial_{\dot{y}} L(t, y(t), \dot{y}(t)) \cdot \dot{h}(t) \, dt.
$$

### Points critiques de l'action {.théorème #theo-EL}
Supposons la fonction $\nabla_{\dot{y}} L$ continûment différentiable ;
soit $\alpha, \beta \in \R^n$. Si la trajectoire $y$ minimise 
(localement) l'action 
$$
A(z) = \int_a^b L(t, z(t),\dot{z}(t)) \, dt
$$
parmi les fonctions $z \in C^1([a, b], \R^n)$ telles que 
$z(a) = \alpha$ et $z(b) = \beta$, alors elle satisfait
pour tout $t \in [a, b]$ l'*équation d'Euler-Lagrange*
[$$
\frac{d}{dt} \left(\nabla_{\dot{y}} L(t, y(t), \dot{y}(t)) \right) - \nabla_y L(t, y(t), \dot{y}(t)) = 0.
$$]{#EL}

### Démonstration {.proof}
Soit $y$ une fonction minimisant l'action localement, sur la boule ouverte 
$B(y, r)$ de rayon $r>0$ (dans l'espace affine des fonctions $z$ de $C^1([a, b], \R^n)$ 
telles que $z(a) =\alpha$ et $z(b)=\beta$). 
La fonction
$$
h \in B(0,r) \mapsto A(y+h) \in \R,
$$
où $B(0,r)$ désigne le sous-ensemble ouvert des fonctions de l'espace
vectoriel normé $$E = \{h \in C^1([a, b],\R) \, | \, h(a) = h(b) = 0\}$$
telles que $\|h\|_{\infty}^1 < r$,
admet donc un minimum en $h=0$ ;
cela nécessite que $d A(y) \cdot h$ pour 
tout $h \in E$.
Notons $\phi(t) = (t, y(t), \dot{y}(t))$ ; [la différentielle de l'action](#da)
peut être exprimée en fonction des gradients (partiels) de $L$ comme
$$
dA(y) \cdot h = \int_a^b \left<\nabla_y L(\phi(t)), h(t)\right> +
\left<\nabla_{\dot{y}} L(\phi(t)), \dot{h}(t) \right> \, dt.
$$
Sous l'hypothèse de régularité du théorème, 
si $h \in C^1([a, b], \R)$ est telle que $h(a) = h(b) = 0$,
une intégration par parties fournit
$$
\begin{split}
dA(y) \cdot h &= \int_a^b \left<\nabla_y L(\phi(t)), h(t)\right> 
- \left<\frac{d}{dt}\nabla_{\dot{y}} L(\phi(t)), h(t) \right> \, dt \\
&= - \int_a^b \left<\frac{d}{dt}\nabla_{\dot{y}} L(\phi(t)) - \nabla_y L(\phi(t)), h(t) \right> \, dt.
\end{split}.
$$
Compte tenu de la continuité en $t$ de  $\frac{d}{dt}\nabla_{\dot{y}} L(\phi(t)) - \nabla_y L(\phi(t))$
et du caractère arbitraire de $h$, $dA(y) \cdot h =0$ implique que pour tout $t$,
[l'équation d'Euler-Lagrange](#EL) est satisfaite.



TODO -- Exercices
================================================================================

TODO -- Théorème de Banach
--------------------------------------------------------------------------------

TODO -- Complétude
--------------------------------------------------------------------------------
Montrer que l'espace des fonctions continues de $[0,1]$ dans $\R$
n'est pas complet pour la norme
$$
\|f\|_1 = \int_0^1 |f(x)| \, dx.
$$

Différentiation d'une composition {.question #dc}
--------------------------------------------------------------------------------

Soit $J$ un ensemble compact de $\R^n$, $f \in C^0(J, \R^n)$ et $K$
un ensemble compact de $\R^n$ contenant $f(J)$.
On note $F$ l'application
$$
F: g \in C^0(K, \R^p) \mapsto g \circ f \in C^0(J ,\R^p).
$$
Montrer que $F$ est différentiable et calculer sa différentielle.

TODO -- Gradient de Forme {.question #gf}
--------------------------------------------------------------------------------

**TODO.** Préciser cadre des perturbations, matcher avec ce qui vient avant
(Calcul Intégral III) si nécessaire, adapter et rédiger les "détails techniques" 
du corrigé ensuite.

Soit $K_0$ un compact à bord $C^1$ de $\R^3$ et $T:K_0 \to \R^3$ une 
application continûment différentiable. On s'intéresse au volume 
de $K= T(K_0)$, vu comme une fonction de $T$.
$$
V = \int_{K} \, dx.
$$

Montrer que si $T est suffisamment proche de l'identité dans $C^1(K_0, \R^3)$,
il admet une extension comme un $C^1$-diffeomorphisme (global) de $\R^3$ dans
lui-même.

Montrer que $V$ est une fonction différentiable de $T$ au point $T=I$ 
dans $C^1(K, \R^3)$ et calculer sa différentielle $dV(I) \cdot H$.

**TODO:** ajouter check dépendance en $H$ uniquement sur le bord, et via
la composante normale.


Théorème de Cauchy Intégral
--------------------------------------------------------------------------------

Montrer la version circulaire, sous l'hypothèse que $f$ est de différentielle
$\mathbb{C}$-linéaire et continue (en faisant une chain rule en dim infinie)
... mais est-ce vraiment nécessaire ? Ne peut-on pas calculer les dérivées
par rapport au centre et au rayon sans ça, avec uniquement la dérivation
"point par point" et les résultats de convergence dans les intégrales ?

Solutions
================================================================================

Différentiation d'une composition {.answer #answer-dc}
--------------------------------------------------------------------------------

Soit $g, h \in C^0(K, \R^p)$ ; on a 
$(g+h) \circ f - g \circ f = h \circ f,$ soit
$$F(g+h) - F(g) - h \circ f = 0.$$
De plus, la fonction $h \in C^0(K, \R^p) \mapsto h \circ f \in C^0(J, \R^p)$ 
est linéaire (évident) et continue, car 
$$
\|h\circ f\|_{\infty} = \max_{x \in J} \|(h \circ f)(x)\| \leq 
\max_{y \in K} \|h(y)\| = \|h\|_{\infty}.
$$
La fonction $F$ est donc différentiable en $g$ et
$dF(g) \cdot h = h \circ f.$

TODO -- Gradient de Forme {.answer #answer-gf}
--------------------------------------------------------------------------------

Par changement de variable, $T$ étant un $C^1$-difféomorphisme, 
$$
V = \int_{T(K)} dx = \int_{K} |\det J_T(x)| \, dx.
$$
Quand $T$ est suffisamment proche de l'identé, $\det J_T(x) > 0$.
L'application $\det$ est continûment différentable dans un voisinage
de l'identité, de différentielle
$$
d\det(I) \cdot H = \mathrm{tr}(H).
$$
L'application 
$$
T \in C^1(K,\R^3) \mapsto J_T \in C^0(K, \R^{3\times 3})
$$
est également continûment différentiable (car linéaire continue entre ces
espaces). 
La fonction 
$$
T \in C^1(K, \R^3) \mapsto \det J_T \in C^0(K,\R^3)
$$
est donc différentiable en $I$ comme différentielle d'une composition et
$$
d(T \mapsto \det J_T) \cdot H = \mathrm{tr}(J_H) = \sum_{i=1}^3 \partial_i H_i
= \mathrm{div} \, H.
$$
L'application
$$
f \in C^0(K,\R^3) \mapsto \int_{K} f dx \in \R
$$
étant linéaire continue, le volume est une fonction différentiable de $T$
en l'identité et vérifie
$$
d V(T) \cdot H = \int_K \mathrm{div} \, H(x) \, dx,
$$
soit encore par le théorème de la divergence,
$$
d V(T) \cdot H = \int_{\partial K} \left<H(x), n(x) \right> \, \sigma(dx).
$$
