% Calcul Différentiel III

<!-- LaTeX Macros -->
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\renewcommand{\C}{\mathbb{C}}
\newcommand{\tr}{\operatorname{tr}}

\newcommand{\zero}{$\mathord{\boldsymbol{\circ}}$}
\newcommand{\one}{$\mathord{\bullet}$}
\newcommand{\two}{$\mathord{\bullet}\mathord{\bullet}$}
\newcommand{\three}{$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$}
\newcommand{\four}{$\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}\mathord{\bullet}$}

#### Question 1 (réponse multiple)
Soit $f: (x_1, x_2) \in \R^2 \mapsto x_1 x_2 \in \R$. On a

 - [ ] A: $$H_f(x) = \left[\begin{array}{cc} 0 & 1 \\ 1 & 0 \end{array} \right]$$

 - [ ] B: Si $h_1 = (h_{11}, h_{12}) \in \R^2$ et $h_2 = (h_{21}, h_{22}) \in \R^2$,
   $$d^2 f(x_1, x_2) \cdot h_1 \cdot h_2 = h_{11}h_{22} - h_{21}h_{12}$$


 - [ ] C: Pour tout $x \in \R^2$ 
          $$\nabla f(x+h) = \nabla f(x) + \frac{1}{2} \left< h, H_f(x) \cdot h\right> + \varepsilon(h) \|h\|^2$$
          où $\varepsilon(h) \to 0$ quand $h \to 0$.

#### Question 2
Si $f: \R^n \to \R$ est deux fois différentiable en $x \in U$
et que $df(x) \cdot h \cdot h$ est connu pour tout $h \in \R^n$, 
peut-on déterminer $df(x) \cdot h_1 \cdot h_2$ pour tout $h_1, h_2 \in \R^n$ ?

  - [ ] Non.

  - [ ] Oui.

#### Question 3
Le tenseur de type $(1,1,1)$ défini par par $t_{ijk} = 1.0$ :

  - [ ] est d'ordre $1$,

  - [ ] est décrit en NumPy par le tableau `np.array([1.0])`,

  - [ ] représente l'application linéaire
    $x \in \R \to y \in \R \to xy \in \R$


#### Question 5
Si $f: \R^2 \to \R^4$ est trois fois différentiable, quel est le type du tenseur
représentant $d^3f(x)$ ?

 - [ ] A: (4, 2, 2, 2)

 - [ ] B: (3, 4, 2)

 - [ ] C: (4, 2, 1)

#### Question 6
Si $f: \R^3 \to \R^3$ est deux fois différentiable, combien y'a-t'il au plus
de coefficients différents dans le tenseur représentant $d^2f(x)$ ?

  - [ ] A: 9

  - [ ] B: 18

  - [ ] C: 27
