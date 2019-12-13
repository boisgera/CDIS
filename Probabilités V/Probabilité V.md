% Probabilités V

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


# Intégrale de Monte-Carlo

Les méthodes de simulation sont basées sur la production de nombres aléatoires, distribués selon une certaine loi de probabilité. 
Dans de nombreuses applications, pour une certaine fonction $h$, on souhaite calculer, pour une variable aléatoire $X$ de loi $\P_X$
$$ \mathcal{I}=\E\left[h(X)\right]=\int_\R h(x) \P_X(dx),$$

<!-- En général, même si l'on sait évaluer $h$ en tout point, on ne peut pas calculer formellement l'intégrale $\mathcal{I}$. Le calcul
d'intégrale par la méthode Monte-Carlo consiste dans sa version la plus simple à générer $(X_1,\ldots,X_n) \sim_{i.i.d.}\P_X$, et à
approcher $\mathcal{I}$ par la moyenne empirique 
$$S_n(h)=\frac{1}{n}\sum_{i=1}^{n}h(x_i)$$
, où i.i.d signifie indépendant et identiquement distribué. En effet, d'après la loi forte des grands nombres, si $h(x)$ est $\P_X$ intégrable, on a l'assurance que
$$S_n(h) \rightarrow_{p.s.} \int h(x)\pi(x)\ud x$$
où p.s. signifie presque sûrement. Si de plus, $h(x)^2$ est $\P_X$ intégrable
la vitesse de convergence de $S_n(h)$ peut être évaluée,
puisque la variance
\begin{equation}
\V(S_n(h)) = \frac{1}{n} \int \left(
h(x)-\E_{\pi}\left[h(X)\right]\right)^2\pi(x)\ud x
\end{equation}
peut également être estimée à partir de l'échantillon
$(X_1,\ldots,X_n)$ par la quantité
\begin{equation}
\sigma_n^2=\frac{1}{n}\sum_{i=1}^{n}\left( h(x_i)-S_n(h)\right)^2.
\end{equation}
Le théorème de la limite centrale nous assure alors que pour $n$
grand,
\begin{equation}
\label{tcl1} \frac{\left( S_n(h)-\E_{\pi}\left[h(X)\right]\right)}{\sigma_n}
\end{equation}
suit approximativement une loi $\No(0,1)$. Cette propriété conduit
à la construction de tests de convergence et de bornes de
confiance asymptotiques pour $S_n(h)$. En outre, elle nous indique
que la vitesse de convergence de $S_n(h)$ est de l'ordre de
$\sqrt{n}$ et ce indépendamment de la dimension du problème. Cela
explique l'efficacité de cette méthode par rapport aux méthodes
d'intégration numérique déterministes dont les vitesses de
convergence décroissent
rapidement avec la dimension du problème.\\ -->


# Génération de nombres pseudo-aléatoires

Les ordinateurs sont des machines déterministes. Il peut sembler paradoxal de leur demander de générer des nombres aléatoires. En réalité, les algorithmes de génération de nombres aléatoires vont générer des séquences de nombres déterministes qui vont avoir l'aspect de l'aléatoire.

# Méthodes de simulation de v.a.
 * inversion
 * rejet
 * box-muller

# Simulation d'un vecteur Gaussien
 Cholesky

# Echantillonnage d'importance