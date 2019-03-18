[![Build Status](https://travis-ci.org/boisgera/CDIS.svg?branch=master)](https://travis-ci.org/boisgera/CDIS)

Calcul Différentiel, Intégral et Stochastique
================================================================================

Accès aux Documents
--------------------------------------------------------------------------------

<https://github.com/boisgera/CDIS/tree/gh-pages/output>

Instructions
--------------------------------------------------------------------------------

### Outils 

  - Un client du système de gestion de version [git](https://git-scm.com/),

  - Une distribution [LaTeX](https://www.latex-project.org/),

  - Un éditeur de texte, explorateur de fichiers, terminal (bash), etc.
    ou un IDE comme  [Visual Studio Code](https://code.visualstudio.com/) 
    qui rassemble tous ces composants.

  - Le gestionnaire de paquetages et d'environnements [conda](https://conda.io/en/latest/).

Conda est particulièrement important puisqu'il est utilisé pour installer
de nombreux autres outils logiciels dont nous avons besoin, comme Python,
Pandoc, etc. Si vous n'avez pas déjà conda sur votre ordinateur,
vous pouvez installer [miniconda](https://docs.conda.io/en/latest/miniconda.html).

Produire les Documents
--------------------------------------------------------------------------------


Nos besoins supplémentaires sont décrites dans le fichier `environment.yml`.
Pour créer un environnement conda qui soit conforme à ces besoins,
exécuter dans le terminal la commande

    $ conda env create -f environment.yml -p env

Quand vous voudrez travaillez sur le projet, activez l'environnement par la
commande:

    $ conda activate ./env

Reference: [Conda/Managing environments](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

In the project directory: 

 1. Edit the Markdown version `document.md` of the document,
    its bibliography, etc.

 2. Then, execute the command

        $ ./build

    to create PDF, HTML and ODT versions of the document
    in the `output` directory.