% Style et Structure des Documents

Markdown
================================================================================

Les documents sources exploitent une variante du format [Markdown](https://en.wikipedia.org/wiki/Markdown).

Pour une introduction à Markdown, voir par exemple <https://commonmark.org/>.

La variante de Markdown utilisée est celle supportée par
l'outil [Pandoc](https://pandoc.org/); 
elle supporte à la fois des fonctionnalités indispensables à un cours de
Mathématiques (formules, bibliographie, etc.) et la production de 
documents dans une large gamme de formats. 
Se reporter à son [guide utilisateur](https://pandoc.org/MANUAL.html) 
pour les détails du format. 

Sections
================================================================================

Hiérarchie
--------------------------------------------------------------------------------

TODO:

  - 3 niveaux normalement assez (4 le cas échéant pour segmenter les longues
    preuves ?).

  - "Atomes", l'essentiel du contenu est au niveau 3

  - Structure des sections d'exercices ?

Type/Propriétés des sections de niveau 3
--------------------------------------------------------------------------------


  - `theorem`, `proposition`, `corollary`, `lemma`.

  - `proof`

  - `exercise` (?), `questions`, `answers` (pluriel ?)

  - `remark`, `example`, `meta`, `anonymous`


Mathématiques
================================================================================


  - Au moins à court terme, inclure les macros LaTeX nécessaires
    au début de chaque document (disons l'entête composée du titre, des auteurs 
    et de la date); comme Pandoc se charge lui-même de faire la substitution,
    a priori pas de risque de collision entre des conventions différentes
    d'un document à l'autre en cas de regroupement.
   
    Cf la section [Pandox -- LaTeX macros](https://pandoc.org/MANUAL.html#latex-macros) 
    pour lus de détails.

    usage des macros

  - usage libéral du "display style" si nécessaire plutôt que d'utiliser
    la commande `\displaystyle` dans des formules "inlines", ce qui casse 
    le [rythme vertical](https://zellwk.com/blog/why-vertical-rhythms/) 
    du document.

TODO:

  - ponctuation dans les formules (à terme), par exemple

        Dans le cas ou $a=1,$ la situation est identique.

    Sinon dans l'export HTML, Mathjax va faire des césures à des endroits
    inappropriés. Bonus de cette convention: c'est de toute façon ce qu'il
    faut faire en mode "display style", ça à le mérite de la cohérence.


Italique & Gras
================================================================================

L'italique sera utilisé pour désigner les nouveaux termes dans les
définitions, et éventuellement des termes en langue étrangère dans
le corps du texte.

Le gras sera utilisé pour mettre une emphase[^ptib].

Par exemple:

    **Attention**, dans ce qui suit, le terme *intervalle* désigne
    est un sous-ensemble connexe de la droite réelle; 
    un intervalle peut donc être non borné. 
   
[^ptib]: voir en particulier [la remarque de Mattew Butterick](https://practicaltypography.com/bold-or-italic.html) concernant le manque de visibilité de l'italique
dans les fontes sans sérif, qui fait pencher la balance en faveur du gras,
d'autant que l'italique à déjà un rôle qui lui est propre.
