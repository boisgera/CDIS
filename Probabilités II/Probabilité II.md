% Probabilités II

\newcommand{\R}{\mathbb{R}}
\newcommand{\Q}{\mathbb{Q}}
\renewcommand{\P}{\mathbb{P}}
\renewcommand{\C}{\mathbb{C}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\A}{\mathcal{A}}
\newcommand{\B}{\mathcal{B}}


# Probabilité sur $\R$

## Fonction de répartition
Nous avons vu précédemment la définition générale d'une probabilité $\P$ sur un espace quelconque $\Omega$ muni d'une tribu $\A$. Un problème fondamental est de construire et de caractériser ces probabilités. La résolution de ca problème lorsque $\Omega$ est fini ou dénombrable est connu.
Le cas général fait l'objet de la théorie de la mesure et sera développé ultérieurement.

Nous allons ici nous contenter de résoudre, sans démonstrations complètes, le cas où $\Omega = \R$ (**$\R^d$ ?**) et où la tribu $\A$ est la tribu borélienne $\B_\R$ engendrée par les ouverts, ou par les fermés, ou  par les intervalles de la forme $]\-infty, a]$ pour $a \in \Q$ (cf CI II).

### Définition - fonction de répartition {.definition}
La *fonction de répartition* de la probabilité $\P$ sur $\R$ est la fonction
\begin{equation}
F(x) = \P(]-\infty, x]), x \in \R.
\end{equation}

### Exemple {.example}
**à développer** 
$\P$ mesure de Dirac -> $F$ fonction de Heavyside



### Proposition {.proposition #propfdr}
La fonction de répartition $F$ caractérise la probabilité $\P$ sur $\R$, et elle vérifie les trois conditions suivantes :
 * elle est croissante
 * elle est continue à droite
 * $\lim\limits_{x \to -\infty} = 0, \lim\limits_{x \to +\infty} = 1$.

### Démonstration {.proof}
 Se reporter à @Jacod pour la caractérisation.
 La première assertion est immédiate d'après sa définition. Pour la seconde, on remarque que si $x_n$ décroît vers $x$, alors $]\-infty,x_n]$ décroît vers $]\-infty,x]$ et donc $F(x_n)$ décroît vers $F(x)$ par le théorème de la continuité monotone. La troisième assertion se montre de manière analogue  en remarquant que $]\-infty,x]$ décroît vers $\varnothing$ (resp. croît vers $\R$) lorsque $x$ décroît vers $-\infty$ (resp. croît vers $+\infty$).

### Remarque {.remark}
 Comme $F$ est croissante, elle admet une limite à gauche en chaque point notée $F(x-)$. En remarquant que $]-\infty,y[ = \lim\limits_{n \to +\infty}$ si $y_n$ tend vers $y$ par valeurs décroissantes, on obtient pour $ x < y $: 

  * $\P(]x,y]) = F(y) - F(x)$
  * $\P(]x,y[) = F(y-) - F(x)$
  * $\P([x,y]) = F(y) - F(x-)$
  * $\P([x,y[) = F(y-) - F(x-)$

En particulier, $\P(\{x\}) = F(x) - F(x-)$ est le **saut** de la fonction $F$ au point $x$. On a donc $\P(\{x\}) = 0$ pour tout $x$ si et seulement si $F$ est continue en tout point.

La [proposition](#propfdr) admet une réciproque que nous admettrons. On se reportera à @Jacod pour une démonstration.

### Théorème {.theorem}
Si $F$ est une fonction réelle sur $\R$ qui vérifie les trois conditions de la [proposition](#propfdr), c'est la fonction de répartition d'une (unique) probabilité $\P$ sur $\R$ munie de la tribu borélienne $\B_\R$. On ne peut pas, en général, définir $\P$ sur la tribu $\mathcal{P)(\R)$ de toutes les parties de $\R$.

### Remarque {.remark}
Le théorème ci-dessus explique pourquoi, d’un point de vue strictement mathématique, il est nécessaire d’introduire les tribus en probabilités, malgré la complexité que cela engendre. Sinon, cela reviendrait à prendre (sans le dire) la tribu $\A = \mathcal{P)(\R)$ et il n'existerait que très peu de probabilités sur $\R$, à savoir les probabilités discrètes que l'on décrit rapidement ci-dessous :

### Exemple (à développer)

 1. Les masses de Dirac (ou **mesures** de Dirac)
 2. Les probabilités portées par $\N$
 3. Les probabilités discrètes

Il existe bien d’autres probabilités, non discrètes, sur \R. Le paragraphe suivant est consacré à un exemple très important, celui des probabilités avec densité.

## Densités de probabilités

# Variables aléatoires de loi à densité

# Moments d'une V.A. a densité

# Calculs de loi (cf Jacod - Garnier)

# Lois usuelles (annexe)

# Exercices