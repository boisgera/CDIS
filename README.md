[![Build Status](https://travis-ci.org/boisgera/CDIS.svg?branch=master)](https://travis-ci.org/boisgera/CDIS)

Calcul Différentiel, Intégral et Stochastique
================================================================================


:book: Documents
--------------------------------------------------------------------------------

| Chapitre      | PDF (e-book) | PDF (print) |
| ------------- | ------------- | --------------------- |
| Topologie 1/1  | [Topologie.pdf](https://boisgera.github.io/CDIS/output/Topologie.pdf) | [Topologie (a4, recto-verso).pdf](https://boisgera.github.io/CDIS/output/Topologie.pdf) |
| Calcul Différentiel 1/3 | [Calcul Différentiel I.pdf](https://boisgera.github.io/CDIS/output/Calcul%20Différentiel%20I.pdf) | [Calcul Différentiel I (a4, recto-verso).pdf](https://boisgera.github.io/CDIS/output/Calcul%20Différentiel%20I.pdf) |
| ... | ... | ... |




  - [Tous les documents (PDF, LaTeX)](https://github.com/boisgera/CDIS/tree/gh-pages/output) (travail en cours)

:calendar: Calendrier 2019 
--------------------------------------------------------------------------------

  - [en ligne (Google Calendar)](https://calendar.google.com/calendar/embed?src=ecqbbg9bbqgaqh0rgnsjt4ppvk%40group.calendar.google.com&ctz=Europe%2FParis)

  - [au format iCalendar (.ICS)](https://calendar.google.com/calendar/ical/ecqbbg9bbqgaqh0rgnsjt4ppvk%40group.calendar.google.com/public/basic.ics)

  - [en version texte](https://github.com/boisgera/CDIS/tree/gh-pages/Calendrier/calendrier.txt)


:speech_balloon: Forum
--------------------------------------------------------------------------------

  - [Discourse Mines ParisTech](https://discourse.mines-paristech.fr) (privé)

:pencil: Développeurs & Contributeurs
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
Pandoc, etc. Nos besoins supplémentaires sont décrits dans le fichier 
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

--------------------------------------------------------------------------------

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Licence Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />Cette œuvre est mise à disposition selon les termes de la <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Licence Creative Commons Attribution - Pas d’Utilisation Commerciale - Partage dans les Mêmes Conditions 4.0 International</a>.
