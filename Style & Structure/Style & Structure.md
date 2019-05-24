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

3 niveau normalement assez.

"Atomes"

lvl 4

Exercices

Type/Propriétés des sections de niveau 3
--------------------------------------------------------------------------------


  - `theorem`, `proposition`, `corollary`, `lemma`.

  - `proof`

  - `exercise`, `questions`, `answers`

  - `remark`, `example`, `meta`, `anonymous`


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
