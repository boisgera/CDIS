[![Build Status](https://travis-ci.org/boisgera/CDIS.svg?branch=master)](https://travis-ci.org/boisgera/CDIS)

Calcul Différentiel, Intégral et Stochastique
================================================================================

Accès aux Documents
--------------------------------------------------------------------------------

<https://github.com/boisgera/CDIS/tree/gh-pages/output>


Produire les Documents
--------------------------------------------------------------------------------

### Préliminaire

Installez sur votre ordinateur:

  - un client du système de gestion de version [git](https://git-scm.com/), 

  - un terminal [bash](https://www.gnu.org/software/bash/),

  - une distribution [LaTeX](https://www.latex-project.org/),

  - le gestionnaire de paquetages et d'environnements [conda](https://conda.io/en/latest/).

  - optionnellement, pour modifier les sources du document, 
    [Visual Studio Code](https://code.visualstudio.com/).

### Environnement de travail

Conda est particulièrement important puisqu'il est utilisé pour installer
de nombreux autres outils logiciels dont nous avons besoin, comme Python,
Pandoc, etc. Nos besoins supplémentaires sont décrites dans le fichier 
`environment.yml`.
Pour créer un environnement conda qui soit conforme à ces besoins,
exécuter dans le terminal la commande

    $ conda env create -f environment.yml -p env

Quand vous voudrez travaillez sur le projet, activez l'environnement par la
commande:

    $ conda activate ./env

Reference: [Gestion des environnements Conda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

### Génération des documents

Exécutez la commande

    $ ./build

Les documents sont générés dans le répertoire `output`.