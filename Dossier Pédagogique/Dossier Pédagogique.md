% Projet de Refonte IC
% GT UE 11 -- Mathématiques
% 16 mai 2019

Unité d'Enseignement: Document Pédagogique
================================================================================

---------------------------------------  ---------------------------------------
Année ou version du document             2019
Titre de l’UE                            Mathématiques
Identifiant                              UE 11
Préfigurateur / Responsable              Sébastien Boisgérault
Nombre d’ECTS                            4
Semestre                                 1
---------------------------------------  ---------------------------------------


Contexte, Enjeux et Objectifs
--------------------------------------------------------------------------------

L'unité d'enseignement (UE) est composée de 2 éléments constitutifs (EC) :

  - Calcul Différentiel, Intégral et Stochastique I (2 ECTS, 1er semestre),

  - Calcul Différentiel, Intégral et Stochastique II (2 ECTS, 1er semestre)

Comme l'indique l'intitulé "Calcul Différentiel, Intégral et Stochastique", 
le périmètre de l'UE correspond grossièrement dans le cycle de formation 2018 
aux enseignements:

  - Mathématiques 1: "Calcul Différentiel" (2 ECTS, 1er semestre),

  - Mathématiques 2: "Calcul Intégral" (3 ECTS, 2ème semestre),

  - Probabilités (2 ECTS, 2ème semestre),

  - Mathématiques 3: "Fonctions d'une variable complexe" 
    (2 ECTS, 3ème semestre),

  - Compléments de Mathématiques (1 ECTS, 1er semestre),

  - Soutien en Mathématiques (0 ECTS, 1er semestre).

Cette comparaison met en évidence une nouvelle formule à la fois 
plus courte et plus compacte (avec 4 ECTS contre ~10 ECTS aujourd'hui, 
programmée sur 1 semestre contre 3 aujourd'hui), dans un contexte où la
formule actuelle est déjà considérée par de nombreux enseignants
comme disposant de trop peu de temps[^data-volume].

[^data-volume]: Pour apprécier cette position, des éléments de comparaison 
sont utiles. A titre d'exemple, le cours de tronc commun de 
Mathématiques 3, "Fonctions d'une variable complexe", dispose de 2 ECTS
(~20h de face-à-face pédagogique), quand le volume habituel pour
ce type de sujet se situe entre 4 et 12 ECTS. 
[Le cours d'Analyse Complexe de l'ENS (PSL)](https://www.math.ens.fr/enseignement/fiche_cours.html?cours=287#) se voit ainsi doté de 12 ECTS ;
son contenu semble couvert à 80% par le cours des MINES (un élève 
ayant déjà suivi ce type de cours à l'ENS Lyon, qualifie le cours 
des MINES de "complet").
Des exemples similaires peuvent être trouvés pour les autres enseignements
de Mathématiques de tronc commun ; 
l'analyse sur le peu de temps disponible pour ces enseignements 
-- à ambition constante -- semble donc largement fondée.

Ce constat ne traduit toutefois pas une diminution générale du poids des 
Mathématiques en tronc commun, mais la volonté de rééquilibrer 
la formation au profit des Mathématiques Appliquées à travers l'UE 21, 
au second semestre.

Dans le détail, toutefois, quelques nuances:

  - Une partie des contenus enseignés dans le périmètre actuel 
    seront transférés à l'unité d'enseignement UE 21 de 
    "Mathématiques Appliquées" au 2nd semestre[^transfert],
    quand cela améliore la cohérence globale de l'ensemble.

  - Certains éléments du périmètre actuel ne seront plus enseignés[^out] 
    pour préserver un volume suffisant sur les savoirs jugés prioritaires;
    compte tenu de la forte réduction du volume, une stratégie de 
    "coup de rabot" uniforme serait vouée à l'échec. 
    Les thématiques correspondantes pourront donner lieu à des enseignements
    électifs lors de la seconde année de formation.

  - Le périmètre actuel de l'UE est très cohérent, ses thématiques susceptibles
    d'être fortement intégrées.
    Compte tenu de la réduction du volume et de ce souci de synergie, 
    aucun nouveau champ général supplémentaire (Logique, Algèbre, etc.) 
    n'a été considéré dans cette nouvelle formule.
    Dans le périmètre actuel, tous les volets peuvent également être qualifiés 
    de fondamentaux dans la mesure où de très nombreux enseignements en 
    dépendent[^dep].


[^transfert]: Principalement: les éléments d'optimisation du calcul différentiel 
actuel sont naturellement transféré vers l'enseignement d'"Optimisation" 
et l'analyse harmonique (de Fourier) développée dans le calcul intégral 
actuel est intégrée au "Traitement du Signal".

[^out]: Ou bien de façon très partielle ; en particulier, sont concernées
l'analyse complexe et l'introduction aux équations aux dérivées partielles.

[^dep]: En particulier, la nécessité d'enseigner très tôt le volet probabilités
s'impose compte tenu des besoins des cours de Physique du 1er semestre comme
des enseignements de Mathématiques Appliquées du 2nd semestre.

Trois enjeux importants pour cette unité d'enseignement 
-- et qui seront traités dans ce document --
sont soulignés par la note de cadrage et rappelés ici.

**Hétérogénéité.** Selon la note de cadrage:

> La gestion de l’hétérogénéité croissante des niveaux et des attentes 
> des étudiants en Mathématiques à l’entrée du cycle ingénieur civil 
> est un enjeu majeur de cette UE. 
> L’UE devra répondre à cette attente en déterminant des acquis 
> d’apprentissage réalistes et en adaptant ses modalités pédagogiques 
> et d’évaluation. Il sera également nécessaire
> de développer pour les étudiants une offre d’accès à l’équipe pédagogique 
> en dehors des plages de face-à-face pédagogique pour proposer 
> un suivi personnalisé se substituant et amplifiant les politiques de 
> compléments et de soutien mises en œuvre jusqu’à présent.

La problématique des acquis d'apprentissages est évoquée 
dans la section "[Acquis d'Apprentissage]"; 
les réflexions associées sur le choix des contenus enseignés se trouvent
dans la sous-section "[Programme]" de la section "[Contenus et Activités]"
et les informations relatives aux modalités pédagogiques dans la
sous-section "[Principes]". La question des modalités d'évaluation est
traitée dans la section "[Modalités d'Evaluation]".

**Vision globale.** Selon la note de cadrage:

> Les interfaces entre cette UE, l’UE 12 (“Informatique”) d’une part 
> et l'UE 21  (“Mathématiques Appliquées”) d’autre part, 
> devront faire l’objet d’une étude menée par les préfigurateurs associés 
> pour assurer une cohérence d’ensemble à ce volet de la
> formation. Les besoins des cours de Physique devront également être 
> examinés.

Le bilan de ce travail, issu des échanges entre préfigurateurs 
et équipes pédagogiques, est restitué dans la section "[Prérequis]".

**Transformation Numérique.** Selon la note de cadrage:

> L’UE comportera un volet numérique conçu et valorisé et intégré 
> au même titre que les savoirs plus théoriques, même si son volume 
> sera plus modeste. Il couvrira l’étude des
> méthodes numériques les plus pertinentes pour la simulation des 
> solutions des équations différentielles, le calcul de différentielles 
> ainsi que le calcul d’intégrales. Dans
> ce contexte, le langage de programmation Python 
> (et l’écosystème associé pour l’ingénierie numérique) sera utilisé.

Cette problématique transverse s'invite naturellement dans presque toutes les
sections du document: les "[Prérequis]" pour le lien avec les enseignements
d'Informatique, la section "[Modalités d'Evaluation]" pour le poids du numérique
dans l'évaluation de l'UE, les sous-sections "[Programme]" et "[Principes]"
de "[Contenus et Activités]" concernant le détail des activités liées
au numérique et à leur intégration dans l'UE, 
la section "[Ressources Pédagogiques]" où la stratégie digitale associée
est détaillée et finalement la section 
"[Ressources Humaines, Matérielles, Financières]" où sont évoqués
l'organisation et les moyens particuliers que l'intégration du 
numérique suppose.





Organisation de l'UE
--------------------------------------------------------------------------------

--------------------------------------------------------------------------------
Éléments constitutifs (EC)                                Crédits
--------------------------------------------------------  ----------------------
1 -- Calcul Différentiel, 
Intégral et Stochastique I                                2

2 -- Calcul Différentiel, 
Intégral et Stochastique II                               2
--------------------------------------------------------------------------------

Prérequis
--------------------------------------------------------------------------------

L'UE, programmé au 1er semestre de la 1ere année de la scolarité, 
s'adresse à des étudiants issus pour l'essentiel des classes 
préparatoires aux grandes écoles (CPGE) via le concours commun Mines-Ponts. 
Plus de 85% des étudiants sont issus des filières MP, PSI et PC.
C'est donc le corpus des connaissances communes à ces trois filières 
et des compétences associées qui sert de référence à l'UE;
on pourra se reporter aux programmes de CPGE (cf. @UPS) 
issus de la réforme de 2013. 
C'est également cette population à laquelle s'adresse principalement l'UE; 
l'hétérogénéité des étudiants nécessite néanmoins d'étendre et de nuancer
cette première intention.

Au sein de cette population, les étudiants issus de MP sont les plus nombreux
(ils représentent plus de 40% de l'effectif total des étudiants). 
Dans ce projet, l'UE doit donc s'efforcer d'analyser et de limiter 
l'enseignement de contenus qui -- bien que nécessaires aux autres populations -- 
apparaîtraient aux élèves issus de MP comme au mieux des rappels et au pire des 
redites. 
C'est une problématique que ne connaissent pas les classes préparatoires.
La place consacrée dans l'UE à des contenus nouveaux, stimulants et 
susceptibles de susciter l'intérêt des étudiants les plus avancés 
en Mathématiques doit être significative; la capacité à les préparer,
s'ils le souhaitent, à intensifier la place des Mathématiques dans leur 
parcours en 2A, 3A ou au-delà, à travers des unités d'enseignement proposées
par MINES ParisTech ou des formations externes, doit être préservée.

A l'inverse, plus de 10% des étudiants à qui s'adresse l'UE 
ne satisfont pas l'hypothèse initiale: 
ils ne sont pas issu des filières MP/PSI/PC, n'offrent pas les
mêmes garanties en termes de prérequis, et ont souvent 
les plus grandes difficultés dans le cursus actuel
à valider les enseignements de Mathématiques
qui leur sont proposés.
Facteur aggravant,
cette population, très différente de la population générale, est elle-même
fortement hétérogène, car composée d'ATS, de TSI, d'admis sur titres variés, 
etc.
Ils sont pourtant admis de plein droit dans le cycle ingénieur civil,
ce qui nous donne l'obligation de rechercher des solutions 
ne les condamnant pas à un échec systématique.
L'impossibilité de concevoir un cours standard
qui soit adapté aux élèves les plus avancés et accessible à 
cette population minoritaire et fortement hétérogène, plaide
pour un recours important à l'accompagnement personnalisé;
il s'agira donc de concevoir un cours dont on sait pertinemment qu'il 
n'est pas totalement adapté ou accessible à une faible fraction de la 
population, ce qui supposera de leur part un travail important,
plus important que la moyenne, et que ce travail pourra être accompagné, 
en dehors des heures de face-à-face pédagogique,
par l'équipe pédagogique, dans des dispositifs de remédiation 
personnalisés.

**Informatique.** 
Pour un bon déroulement de son volet numérique, l'UE dépendra également 
des compétences introduites dans l'UE 12 d'Informatique: elle tirera parti
des sessions d'introduction au langage Python et de son usage dans un 
contexte scientifique, qu'il s'agisse des connaissances des constructions
du langage, de la familiarité avec les notebooks Jupyter qui se prêtent
au calcul interactif, des librairies comme NumPy pour le calcul numérique 
ou des outils de visualisation de données comme Matplotlib.

**Physique.** L'UE 13 de Physique (Statistique et Quantique) aura une
programmation a peu près simultanée avec l'UE 11; il ne sera donc pas
possible de garantir en général que l'UE 11 ou l'UE 13 introduise la
première telle ou telle notion exploitée dans les deux disciplines.
Il sera par contre nécessaire que ces évocations se renforcent et
se complètent intelligemment, d'autant plus que l'UE de Physique 
exploite un périmètre particulièrement large des Mathématiques.

Les échanges laissent penser que le programme de Mathématiques de l'UE offrira
des outils adaptés en ce qui concerne les probabilités[^oap], les notions
de mesure et de distributions, le calcul intégral, le calcul différentiel et 
les systèmes dynamiques[^oacdsd].
En particulier, une programmation plus précoce de l'enseignement 
des probabilités dans la formation, conforme au statut fondamental
(littéralement) de la discipline, serait un progrès par rapport à la
situation actuelle.
Les besoins en analyse fonctionnelle[^oaan], une thématique beaucoup plus 
difficile du point de vue des Mathématiques, ne sont que très 
partiellement couverts.
L'analyse harmonique (séries/transformée de Fourier) présente une difficulté 
particulière; indispensable en Physique, elle a totalement disparu des 
enseignements de Mathématiques de classes préparatoires 
dans la plupart des filières, 
et ne rentre pas dans le périmètre de l'UE 11 mais de l'UE 21, dans
l'EC de "Traitement du Signal". Des contacts ont été pris avec l'équipe en
charge pour tâcher de mitiger cette difficulté en fournissant par 
anticipation des ressources aux étudiants sur le sujet. 
Enfin, les notions algébriques qui pourraient être utiles à l'UE de
Physique[^oaa] sont hors du périmètre de l'UE 11.

[^oap]: Avec en particulier l'introduction des variables aléatoires à densité,
indispensable à la Physique Quantique.

[^oacdsd]: Il s'agit par exemple de permettre l'étude des systèmes 
hamiltoniens, qui relèvent à la fois des équations différentielles et
du calcul des variations.

[^oaan]: Les espaces de Hilbert seront introduits par exemple, mais tardivement
et de façon minimale ;
l'étude des opérateurs en dimension infinie (comme les opérateurs hermitiens
de la Physique Quantique), l'analyse spectrale associée, l'étude des problèmes
elliptiques, etc. dépassent très largement le cadre de ce qu'il nous semble
possible de faire dans l'UE 11.

[^oaa]: Telles que: groupe de Lie, algèbre de Lie, etc.

**Mathématiques Appliquées.** Une large partie des enseignements de l'UE 11
sert directement de fondation aux EC de l'UE 21:

- L'EC "Optimisation" repose très largement sur le calcul différentiel
  et prolonge ses enseignements,
  en particulier les sessions consacrées à la dimension finie et au 
  calcul numérique[^NBOC]. 

- L'EC "Sciences des Données" exploite principalement les 
  concepts et outils des Probabilités (ainsi que le calcul différentiel, 
  mais largement à travers l'enseignement d'Optimisation).

- L'EC "Traitement du Signal" requiert avant tout des
  concepts et outils relevant du calcul intégral, et dans une moindre 
  mesure de la dimension infinie et des probabilités.

[^NBOC]: L'UE 11 ne couvre toutefois pas l'intégralité des prérequis 
  "raisonnables" de l'EC d'Optimisation; en particulier, les notions
  de convexité nécessaires à l'Optimisation Convexe, par le passé
  acquises en classes préparatoires, 
  devront être prises en charge directement par l'UE 21.

Acquis d'Apprentissage
--------------------------------------------------------------------------------

Les objectifs de cette UE, située en tout début de scolarité, 
présentent bien des aspects similaires à ceux des classes préparatoires:
assurer une continuité avec les connaissances et pratiques pédagogiques
des classes préparatoires (là où les classes préparatoires 
se positionnent par rapport aux filières de lycée),
permettre l'acquisition d'un large panel de connaissances,
s'inscrire dans le projet de formation global
en s'interfaçant avec les enseignements de Mathématiques, Physique, etc.[^ocpge]

[^ocpge]: Le lecteur pourra lire avec profit les objectifs de formation des 
1ère et 2nde années des programmes de classe préparatoire aux grandes écoles 
[@UPS].
La description des compétences à développer est presque totalement 
indifférenciée en MP, PSI et PC, bien que les programmes diffèrent. 

Les acquis d'apprentissages qui en résultent 
nécessitent d'être décrits à différents niveaux: 
au niveau de l'UE ou de l'EC, puis des thématiques qui se déploient sur 
plusieurs sessions, de chaque session elle-même, voire de partie de session, etc. 
Cette organisation permet de limiter le nombre d'acquis d'apprentissage
décrits à chaque niveau, ce qui est une condition nécessaire pour une
bonne lisibilité des objectifs; on peut également, en considérant les
acquis des différents niveaux, s'assurer de la cohérence globale du projet
et, en allant au niveau le plus détaillé, s'assurer que les objectifs de
haut niveau sont bien transposés de façon opérationnelle.

Nous nous intéressons ici aux acquis d'apprentissage globaux de l'UE;
nous renvoyons le lecteur à la section "[Contenus et Activités]" pour
la description plus précise des attendus thématique par thématique.
Pour ce qui est du niveau de détail le plus fin nous renvoyons
aux ressources pédagogiques elles-mêmes: un effort sera entrepris[^en-cours] 
pour annoter les ressources pédagogiques afin d'expliciter 
les raisons d'être des concepts, notations, méthodes, etc. introduits
ainsi que les attentes associées dans le cadre du projet de formation 
de l'UE. 
Rendre ces informations disponibles doit permettre une 
meilleure compréhension de la place de l'UE dans le projet de formation 
global, favoriser la communication au sein de l'équipe pédagogique et 
préciser le contrat didactique avec les étudiants.

[^en-cours]: Il s'agit pour cette première année d'initier cet effort, 
qui nécessite de transformer en profondeur le processus de conception 
des ressources pédagogiques.
Compte tenu de son ampleur, cette transformation ne sera vraisemblablement
pas achevée pour la première année de l'UE et sa visibilité pourrait 
initialement être limitée.

A l'issue de cette UE, les étudiants auront

  - découvert et assimilé un large panel de nouvelles connaissances
    fondamentales dans les domaines du calcul différentiel, intégral 
    et stochastique, prolongeant les connaissances acquises antérieurement 
    (cf. [Programme]).

  - renforcé et élargi les compétences associées au spectre
    varié des pratiques mathématiques actuelles, 
    qui supposent de savoir comprendre, deviner, raisonner, démontrer, 
    expérimenter, calculer, communiquer.[^pratiques]

  - développé des aptitudes clés facilitant la poursuite de leurs 
    études[^champs], aussi bien les enseignements de tronc commun 
    qu'ultérieurement, une large gamme de parcours 
    de formation individualisés. 

[^pratiques]: Il s'agit aussi bien ici de savoir s'approprier 
un nouveau concept (avoir des intuitions pertinentes le concernant, 
cerner son applicabilité, etc.), que de savoir 
formaliser complétement un raisonnement déductif (rédiger une 
démonstration) ou encore d'interfacer les aspects théoriques
avec les outils numériques. Les besoins en la matière sont variés,
et posent des défis importants en terme de modalités pédagogiques
et notamment de modalités d'évaluation. Les profils et les attentes
des étudiants sont également plus variés que dans les filières 
plus "pures" des classes préparatoires. Il est inutile d'espérer
compenser intégralement en quelques dizaines d'heures les différences 
importantes qui se sont formées dans les deux ans des filières préparatoires,
d'autant que les objectifs en termes d'acquisition de nouvelles
connaissances sont ambitieux; il sera donc nécessaire d'œuvrer pour ne pas 
évaluer systématiquement les étudiants à l'aune d'un "profil type" 
étroit et rigide, mais par rapport à un large panel de compétences 
mathématiques utiles, panel qui sera probablement maîtrisé de 
façon lacunaire.

[^champs]: En Mathématiques bien sûr, mais aussi Physique, Informatique, 
Sciences Economiques et Sociales, etc. 
Si les Mathématiques ne sont pas "une discipline serve", 
et qu'il est légitime qu'une partie des objectifs consiste à préparer
les étudiants à des Mathématiques plus avancées,
les Mathématiques *du tronc commun* du cycle ingénieur civil 
ne peuvent pas être sourdes aux besoins exprimés 
par les autres champs disciplinaires.

<!--

**TODO:** renforcer la place du numérique, dvlper l'autonomie.
 
Des différences de contexte sont toutefois marquées:

  - Le projet de formation consacre à cette UE un volume limité à 4 ECTS, 
    ce qui est sans commune mesure avec le temps disponible en
    classe préparatoire pour atteindre les objectifs de formation. 
    Le périmètre concerné -- calcul différentiel, intégral et stochastique 
    -- est pourtant très vaste (plus du double de
    ce volume y était consacré dans l'ancienne maquette) et doit de plus
    tenir compte des allégements dans ce domaine 
    de la réforme de 2013 des classes préparatoires. 
    Il est donc nécessaire d'avoir une ambition réaliste quant à notre capacité 
    à compléter et infléchir les acquis de classe préparatoire, notamment dans 
    les compétences de base associées à la pratique des Mathématiques. 

  - L'hétérogénéité croissante des élèves, issus de filières variées et
    aux objectifs de parcours diversifiés,
    est une problématique qui épargne largement les classes préparatoires. 
    Le modèle qui a pu prévaloir implicitement jusqu'à présent
    pour gérer cette hétérogénéité -- remettre les étudiants à niveau 
    pour les re-homogénéiser -- montre ses limites. Il est donc nécessaire
    d'accepter en partie et de prendre en compte cette hétérogénéité 
    plutôt que de chercher à tout prix à la réduire.

  - La première année du cycle ingénieur civil est la dernière année 
    du premier cycle d'étude supérieures (L3, undergraduate) et 
    doit préparer les élèves qui souhaiteraient faire une partie
    de leur formation en seconde année à l'extérieur aux standards
    du 2nd cycle d'étude supérieure en Mathématiques.

    ... aussi: maturation, autonomie, etc? 

-->

<!--



Donc

  - L'analyse du tableau des compétences variées attachées à la pratique
    des Mathématiques est toujours pertinente (raisonner, démontrer, calculer, 
    communiquer). Compliqué, j'aimerai expliquer qu'il nous faudra être en
    mesure de relever des compétences "une par une" sans qu'aucune ne soit
    "bloquante" (en écho à la multiplicité des profils en entrée et des
    besoins en sortie). Ex: statut/intérêt de la preuve pour la plupart des
    élèves ?

  - Compétences ? Largement "gelées" dans leur équilibre à l'issue de la prépa?

  - Périmètre large, Volume restreint, 
    
  - Continuité: autonomie de l'élève à développer, mais possibilité d'un
    suivi important (comme en prépa).

  - Hétérogénéité (conséquences pour compétences).
    Construction de objets mathématiques, "calcul", statut de la démonstration, etc.


  - Interface, position ? Projet "complexe", multidisciplinaires, non.
    (pas le temps, y'a la 2A, etc.). Besoins communs, etc.

-->

<!--
Les
objectifs d'apprentissage que nous décrivons ci-dessous mettent l'accent sur
les évolutions par rapport à la doctrine des classes préparatoires, que
nous résumons brièvement en deux points:

  - Les Mathématiques dans une démarche globale.

    Les programmes de classe préparatoire encourage le développement 
    d'un équilibre entre les exercices d'entraînement, contribuant à
    l'acquisition de savoir et capacités très ciblés, et la confrontation à
    des problèmes plus complexes, éventuellement ouverts, nécessitant 
    un travail de recherche individuel ou collectif et d'un large 
    éventail des connaissances et capacité. Sont en ligne de mire:
    le développement de l'autonomie, le développement d'une large
    gamme de stratégies de résolution de problème, l'interaction
    des Mathématiques avec d'autres champs disciplinaires.

  - Raisonner, Démontrer, Calculer, Communiquer.

    Le programmes de classe préparatoire tendent à organiser ces éléments
    autour de trois pôles: raisonner pour produire des démonstrations
    (le cœur de l'activité mathématique); calculer, manipuler des symboles, 
    maîtriser un formalisme; et enfin communiquer à l'écrit et à l'oral.
    La construction d'objets comme une part de l'activité mathématique
    n'est évoquée que pour la filière MP.

-->

<!--

TODO / hétérogénéité: compétences: "construction" juste MP. Statut de la preuve,
niveau de "rigueur", différences dans les pratiques disciplinaires: donner les
standards des Maths du 20ème siècle comme "direction", mais reconnaitre les
compétences "partielles" (intuition, inductif, etc.) même si maitrise formelle
pas totale. Nécessaire de mieux discriminer les spectre des compétences
et la maitrise partielle.
Reprendre compétences listées en prépa, réorganiser et dire nos attendus?
Lister attendus ? Quid mémorisation, quid assimilation/intuition ?
Capacité à formaliser vs "calcul formel" ? Calcul / preuve ?
Lister ce qu'on attend ici dans ces domaines, en parallèle avec une
vision des différents profils (raisonner, communiquer/convaincre, etc.).


  - Intégration composants, périmètre, unité, interactions disciplinaires.

  - Narratif, matrice, compréhension à différents niveaux.
    Simple avant complexe, démarche inductive.
    Proposer des solutions à des problèmes, inscrire les notions
    dans une trame; ne pas chercher le cas le plus général / conceptuel
    comme première étape.

  - Construction objets, cadres mathématiques, démonstration et pas calcul formel.
    Pratique de référence complète, modèle (pb, idée, démo, formalisation),
    mais reconnaissance / valorisation maitrise partielle (suffisant pour
    des gammes d'applications).
    Valoriser différents volets de l'activité, même au niveau du raisonnement:
    connaître / avoir assimilé notions, avoir intuitions, savoir formaliser,
    etc.

  - Numérique ...

  - en prépa: Architecture des filières fortement différenciées, 
    liste et description des compétences non ... 

-->

Compétences
--------------------------------------------------------------------------------

Vis-à-vis du référentiel générique de la CTI, 
l'UE participe principalement aux compétences relatives à
"l'acquisition des connaissances scientifiques et techniques 
et la maîtrise de leur mise en œuvre" :

 1. La connaissance et la compréhension d’un large champ de sciences 
    fondamentales et la capacité d’analyse et de synthèse qui leur est associée.

    **Totalement.**

 2. L’aptitude à mobiliser les ressources d’un champ scientifique et technique 
    spécifique.

    **Totalement.**

 3. La maitrise des méthodes et des outils de l’ingénieur :
    identification, modélisation et résolution de problèmes même non familiers 
    et incomplètement définis, l’utilisation des outils informatiques, 
    l’analyse et la conception de systèmes.

    **Partiellement. ** A ce stade de la formation, et dans la perspective des
    problèmes auxquels peut être confronté un ingénieur, 
    l'UE confronte les étudiants à la résolution de problèmes simples
    (par opposition à "composés" ou "complexes", 
    mais pas dans le sens de "aisé") et bien définis.
    L'utilisation de l'outil informatique est également une compétence que 
    l'UE contribue à développer.

 4. La capacité à concevoir, concrétiser, tester et valider des solutions, 
    des méthodes, produits, systèmes et services innovants.

    **Partiellement.** La conception, le test et la validation de solutions
    et de méthodes, dans le domaine des Mathématiques.

 5. La capacité à effectuer des activités de recherche, fondamentale 
    ou appliquée, à mettre en place des dispositifs expérimentaux, 
    à s’ouvrir à la pratique du travail collaboratif.

    **Partiellement.** L'UE est plutôt un précurseur pour ce type
    d'activité, qui arrivera plus tard dans le cursus.
    Des pratiques collaboratives pourraient être exploitées dans
    le cadre de l'UE, sans pour autant constituer un objectif de formation.

 6. La capacité à trouver l’information pertinente, à l’évaluer et à 
    l’exploiter : compétence informationnelle.

    **Partiellement.** Oui, à ceci près que la recherche de l'information
    pertinente va être principalement cantonnée aux ressources pédagogiques
    conçues spécifiquement pour l'UE pour des raisons d'efficacité[^eff].
    Les projets numériques, et peut-être les modalités d'évaluations
    du second EC, pourraient être l'occasion d'élargir le champ des 
    recherches (à des corpus pré-selectionnés de ressources extérieures,
    ou même sans ce type d'assistance).
    
[^eff]: Le périmètre de l'UE est large et le rythme ambitieux; 
accomoder fortement les ressources pédagogiques est un des 
leviers principaux dont nous disposons pour répondre à ce défi.

Aucune compétence n'est spécifiquement développée qui soit relative
à "l'adaptation aux exigences propres de l'entreprise et de la société" :

 7. --

 8. --

 9. --

 10. --

La "prise en compte de la dimension organisationnelle, personnelle et culturelle"
est partiellement concernée:

 11. --

 12. --

 13. --

 14. La capacité à se connaitre, à s’autoévaluer, à gérer ses compétences 
     (notamment dans une perspective de formation tout au long de la vie), 
     à opérer ses choix professionnels.

     **Partiellement.** Pas dans une perspective globale, mais localement,
     concernant le niveau de maîtrise des acquis d'apprentissage associés
     à l'UE. Cette compétence est importante dans la mesure où elle
     conditionne le recours que les étudiants peuvent avoir aux dispositifs
     de remédiation.



Modalités d'Evaluation
--------------------------------------------------------------------------------

L'évaluation de l'EC 1 sera principalement basée sur un examen écrit.
Cette modalité, standard et familière pour les étudiants, 
à l'inconvénient d'être peu personnalisable et fournit en cas de 
note insuffisante très peu d'explications aux enseignants sur les 
raisons de l'échec. Elle répond pourtant de façon simple à 
l'organisation globale de l'UE, qui concentre une grande partie 
des acquis d'apprentissage les plus simples et les plus importants 
dans son premier volet, pour lesquels une évaluation normalisée 
devrait convenir. A défaut de fournir des informations précises sur la 
nature des difficultés rencontrées par les étudiants -- 
difficultés qui n'auraient pas été détectées dans le cadre du dispositif 
d'accompagnement personnalisé, auquel les étudiants ne sont pas tenus
d'avoir recours -- elle a le mérite de donner l'alerte de façon claire
et clinique, puisqu'elle situe les résultats des étudiants 
les uns par rapport aux autres, dans un dispositif standard.
Cette information doit être alors prise en compte dans le second 
EC de l'UE pour définir de façon plus personnalisée des objectifs 
adaptés et orienter si nécessaire les étudiants vers le dispositif
d'accompagnement personnalisé du second EC.

Les modalités d'évaluations du second EC ne sont pas définies dans le détail
à ce stade; plusieurs modalités ont été évoquées par le groupe de travail
(oraux, mémoires, devoirs en temps libre, etc.) pour ne pas cantonner
l'évaluation aux examens écrits qui ne permettent pas de mettre en valeur
toutes les compétences des étudiants et sont globalement assez peu informatifs.
Une certaine liberté peut également être envisagée dans la personnalisation
de l'évaluation dans la mesure où certains acquis d'apprentissage plus avancés 
du second EC sont un peu moins critiques pour l'ensemble des étudiants 
et que leur intérêt pour chacun va dépendre de leur projet personnel de formation.
En particulier, lorsque ces acquis dépendent explicitement d'acquis
du premier EC qui ne sont pas maîtrisés, les étudiants -- conseillés par
l'équipe pédagogique -- devront pouvoir consacrer à nouveau du temps sur les 
acquis de base, afin de valider à nouveau les acquis du premier EC, 
quitte à abandonner explicitement une partie des acquis du second EC[^exp-choix]. 
Il faudra donc distinguer dans ce second EC les nouveaux 
acquis fondamentaux d'acquis plus avancés qui prolongent le premier EC[^ex-distinction].

[^exp-choix]: Avec pour conséquence mécanique de perdre des points à coup sûr 
sur le second EC -- 
mais des points qu'il aurait été très difficile de gagner quoi qu'il en soit
-- et avec une nouvelle chance de gagner des points au titre du premier EC.


[^ex-distinction]: A titre d'exemple: les équations différentielles n'apparaissent
que dans le second EC et les savoirs de CPGE dans ce domaine sont trop limités pour
les besoins de l'ingénieur, il est donc nécessaire d'exiger de tous l'acquisition 
de compétences dans ce domaine; par contre,
il est contre-productif de chercher à valider des acquis de calcul 
différentiel en dimension infinie tant que le calcul différentiel en dimension 
finie n'est pas un minimum maîtrisé.


Le volet algorithmique et numérique, transverse à l'UE, 
représente environ 25% du travail total des étudiants[^detail-num]. 
Le même poids lui est donc affecté dans l'évaluation de l'UE. 
Un tiers de cette activité est programmée dans l'EC 1, 
pour un poids de 1/6 de la note de l'EC, 
et les deux tiers restant dans l'EC 2, pour 1/3 de la note de l'EC.

[^detail-num]: Chacun des trois thèmes numériques comporte une session de
cours magistral, une session de travaux dirigés, une session de travail
personnel associée et deux sessions dédiées au projet numérique, pour un
total de $3 \times 5 = 15$ sessions, soit 22h30 sur les 90h de travail
total affectées à l'UE.

Contenus et Activités
--------------------------------------------------------------------------------

### Programme

Le programme de l'UE est organisé ci-dessous en 5 thématiques, 
dont la plupart sont réparties sur les deux EC.
Cette présentation a vocation à fournir une grille de lecture simple 
des contenus et équilibres de l'UE, mais dans le détail, 
ces volets thématiques sont tout sauf étanches[^ex]; 
ce découpage ne doit donc pas être pris au pied de la lettre.
Chaque item listé et numéroté fait référence à une session de cours magistral (1h30).

[^ex]: Par exemple, la problématique de l'intégration apparaîtra
dès la 1ere session de calcul différentiel, des considérations de 
topologie seront à nouveau évoquées dans la session de 
calcul différentiel en dimension infinie, 
les probabilités feront partie intégrante de la session "application" 
de la théorie de la mesure, la session de probabilités consacrée aux
méthodes de Monte-Carlo fournit des outils pour le calcul d'intégrales, 
etc.

#### Topologie

 1. Topologie pour l'Analyse

Une introduction nécessairement minimaliste compte tenu du très faible
volume dédié[^intro] et dictée par les besoins variés des sessions 
qui suivent. Malheureusement, les contenus des programmes des classes
préparatoires dans ce domaine sont très réduits[^CPGE-topo].
En conséquence, le contenu programmé se limite à la topologie des
sous-ensembles d'espaces vectoriels normés (dimension finie ou infinie), 
avec notamment l'étude des notions de complétude et de compacité 
dans ce cadre; ce positionnement est suffisant pour les besoins de l'UE[^Kura].
Une partie des éléments techniques spécifiques à la dimension infinie
(opérateurs linéaires bornés, etc.)
ne sera introduite que dans la 3ème session de Calcul Différentiel, 
quand le besoin s'en fera sentir.
En perspective, on peut envisager de compléter l'exposé oral
par des éléments de topologie générale, selon des approches susceptibles
d'être pédagogiquement efficaces[^nearness], mais ces compléments 
destinés aux étudiants les plus curieux ne sauraient constituer des 
compétences exigibles de tous.

[^nearness]: En particulier, en prenant comme objet primitif la 
notion de "proximité" entre deux points 
plutôt que le concept d'ouvert (cf. par exemple [@Gau78]).
Très différentes dans la présentation, les deux approches sont pourtant 
strictement équivalentes mathématiquement.

[^intro]: Cette session qui sera la première de l'UE occupera vraisemblablement
moins de 1h30 de cours magistral s'il est nécessaire de présenter la logique
et les modalités de l'UE dans cette même session.

[^CPGE-topo]: Cette situation est antérieure à la réforme de 2013.
Le cadre le plus général abordé aujourd'hui est celui des espaces vectoriels 
normés, et de façon assez large uniquement en MP; en PSI comme en PC, 
l'emphase est mise sur les espaces vectoriels normés de dimension finie.
La notion d'espace métrique n'est abordée dans aucune filière, sans parler de 
la notion d'espace topologique. La notion de suite de Cauchy, de complétude,
de point fixe sont hors-programme pour tous. La notion d'ensemble compact
n'est abordée qu'en MP (et via la notion de compacité séquentielle).

[^Kura]: Par le [théorème de plongement de Kuratowski](https://en.wikipedia.org/wiki/Kuratowski_embedding),
ce cadre simple, qui est le prolongement naturel après les enseignements 
de classes préparatoires est "exactement aussi puissant" que le cadre des 
espaces métriques qui est enseigné aujourd'hui. Il s'agit donc principalement
d'une modification de nature didactique.


#### Calcul Différentiel 

 1. Fonctions de plusieurs variables,

 2. Méthodes numériques de calcul,

 3. Calcul différentiel en dimension infinie.

Le volet "Calcul Différentiel" est organisé pour prendre le relais 
des contenus actuels de CPGE dans le domaine, réduits par la réforme
de 2013[^CPGE-CD], en introduisant une démarche par étapes.

La première session (1er EC) introduit la notion de différentielle 
dans un cadre limité aux fonctions de plusieurs variables réelles[^ni], 
puis dans ce même cadre la différentiation en chaîne, 
les différentielles d'ordre supérieur, ainsi que le lien avec 
la représentation de la différentielle par une matrice, 
qui est propre à la dimension finie.

La seconde session (1er EC) est un volet algorithmique et numérique.
Elle introduira le théorème des fonctions implicites,
en insistant sur l'aspect constructif de la solution 
(méthode de Newton, recherche d'un point fixe, etc.);
elle fournira également aux étudiants des clés pour 
évaluer numériquement les différentielles lorsque le calcul d'une 
solution symbolique ou analytique n'est pas une option.
L'accent -- notamment au travers du projet -- 
sera mis sur les techniques de différentiation automatique dont l'usage s'est 
rapidement (re-)développé en optimisation et machine learning.
Pour situer l'intérêt de cette méthode parmi le panel des options
existantes (comme le calcul de différences finies), 
des éléments d'analyse numérique (analyse des erreurs
asymptotiques comme des erreurs d'arrondi) seront introduits.

La troisième et dernière session (2nd EC) ne sera dispensée qu'une
fois que l'UE aura motivé l'étude de "fonctions de fonctions",
le cas d'usage central pour le calcul différentiel en dimension infinie.
La différentielle de Fréchet dans les espaces de Hilbert/Banach et ses
applications sera alors considérée, avec les concepts dont elle dépend.


[^ni]: C'est-à-dire "de dimension finie", mais sans mettre l'accent sur
le caractère intrinsèque de la différentielle.

 [^CPGE-CD]: Même dans la filière MP, la notion de différentielle n'est
 introduite que dans le cadre les espaces vectoriels normés de dimension finie;
 la différentielle d'ordre 2 n'est pas définie; théorème des fonctions
 implicites et d'inversion locale sont absents. Dans les filières PSI et PC,
 le caractère intrinsèque de la différentielle disparaît: il s'agit
 désormais d'étudier des fonctions de plusieurs variables réelles -- plus
 précisément, "en pratique", de fonctions réelles dépendant d'au plus
 3 variables réelles.
 Stricto sensu, la notion de fonction différentiable n'est pas présente:
 l'objet "différentielle" est défini a posteriori,
 à partir des dérivées partielles; de même
 la règle de différentiation en chaîne est abordée à travers le calcul des 
 dérivées partielles.

#### Calcul Intégral 

  1. Intégrale de Riemann généralisée,

  2. Intégrabilité absolue & mesurabilité,

  3. Théorèmes de convergence & intégrales multiples,

  4. Théorie abstraite de la mesure,

  5. Applications de la théorie de la mesure.

L'organisation de ce volet est motivée par la volonté d'arriver rapidement et
avec aussi peu de technicité que possible à une intégrale "moderne" 
-- suffisamment générale et accompagnée d'outils efficaces -- 
dans $\mathbb{R}$ et $\mathbb{R}^n$ 
(3 sessions, 1er EC), 
à la fois susceptible de couvrir les besoins d'une large majorité des étudiants
et de correspondre aux capacités du plus grand nombre.
Les étudiants pourront ensuite s'appuyer sur leur compréhension de ce
premier volet[^step] pour aborder le second volet (2 sessions, 2nd EC), 
sensiblement plus technique et plus abstrait, 
consacré à la théorie de la mesure.
Posant plus de difficultés aux étudiants, dotée d'un volume restreint,
cette seconde partie n'est donc plus sur le chemin critique;
seules certaines des applications les 
plus avancées (telles que: fonctions généralisées, 
probabilités dans le cadre général, etc.) requièrent sa maîtrise. 

Cette stratégie permet de se consacrer dans un premier temps
à l'intégrale de Riemann généralisée[^HK] comme le plus court chemin
pour définir l'intégrale "de Lebesgue" dans $\mathbb{R}$ et $\mathbb{R}^n$, 
sans avoir recours à la théorie de la mesure. Plus récente, mieux intégrée avec
le calcul différentiel, plus simple à comprendre, les bénéfices de cette 
approche par l'intégrale de Riemann généralisée sont bien documentés 
(voir par exemple @Bar96).
Cette étape doit être comprise dans le contexte où plus aucune construction 
spécifique de l'intégrale n'est au programme des classes 
préparatoires[^CPGE-int]; il faut par conséquent s'attendre à ce que même 
cette approche simplifiée, dans le prolongement des notions de CPGE, 
présente son lot de défis pour certains étudiants.

[^step]: Une grande partie de ce qui constitue l'"outillage axiomatique" 
de la théorie de mesure -- notion d'ensemble et de fonction mesurable,
mesure $\sigma$-additive, etc. -- peut être découvert, plutôt que postulé,
dans le cadre du premier volet. Les solutions que la théorie générale
apporte doivent être dans la mesure du possible mises en rapport avec 
des problèmes auquels on aura été confronté au préalable -- 
comme par exemple l'impossibilité de définir une mesure de volume 
aux propriétés satisfaisantes applicable à tous les ensembles de 
$\mathbb{R}^3$ -- avant d'axiomatiser la notion d'ensemble mesurable. 
Les résultats majeurs de la théorie générale feront
de plus écho à des résultats déjà énoncés et manipulés dans un cadre
plus simple.

[^HK]: Ou plus précisement, à l'intégrale de Henstock-Kurzweil, 
puisqu'il y a plusieurs intégrales de Riemann généralisées 
(McShane, Mawhin, etc.).

[^CPGE-int]: L'intégrale considérée concerne les fonctions continues par 
morceaux sur un intervalle de $\mathbb{R}$. Même dans ce périmètre étroit
concernant l'intégration, "aucune construction n’est exigible". 
Toutefois, si les sommes de Riemann ne sont pas (nécessairement) 
utilisées pour *construire* l'intégrale, elles sont vues par tous dans le cas
des subdivisions régulières, et utilisées pour les *calculer*:
les méthodes des rectangles et des trapèzes sont au programme 
d'Informatique.

#### Equations Différentielles

   1. Equations non-linéaires,
      problème bien posé, 
      comportement asymptotique.

   2. Méthodes numériques de résolution.

Le volet consacré aux équations différentielles, qui nécessite à la fois
des résultats du calcul différentiel et intégral, est programmé dans le
2nd EC. Il s'inscrit dans le prolongement des contenus enseignés en 
classes préparatoires[^CPGE-ODEs]; en particulier, les équations
différentielles étudiées ne sont plus nécessairement linéaires et n'ont
plus nécessairement de solution analytique connue. 
L'accent est donc mis sur la présentation d'un cadre général définissant 
un problème bien posé, le comportement qualitatif des solutions 
(en temps fini et asymptotiquement) 
et l'usage de méthodes numériques pour la détermination de solutions 
approchées; cet effort se prolonge dans un projet numérique.

[^CPGE-ODEs]: Le programme de CPGE consacré aux équations différentielles
se limite au cadre linéaire pour toutes les filières. Les résultats
d'existence et d'unicité (mais pas la continuité par rapport aux conditions
initiales) sont présentés dans ce cadre étroit; la problématique des solutions
locales (maximales) par exemple est donc occultée. Le volet numérique,
en lien avec l'enseignement d'informatique, se limite au schéma d'Euler
explicite; l'étude de l'influence du pas de discrétisation sur la 
qualité de la solution est évoquée, mais de façon purement qualitative.

#### Probabilités 

   1. Introduction,

   2. Variables aléatoires réelles à densité,

   3. Vecteurs aléatoires ($\mathbb{R}^n$) & conditionnement,

   4. Théorie asymptotique & inégalités de concentration,

   5. Méthodes de Monte-Carlo.

Comme les volets consacrés au calcul différentiel et au calcul intégral,
l'enseignement de Probabilité est décomposé en deux parties, pour 
introduire par étapes de difficulté croissante un nombre important 
d'éléments nouveaux.

Les enseignements de classes préparatoires en Probabilités sont consacrés
aux variables aléatoires réelles finies ou discrètes[^restr], ce qui permet d'aborder un
périmètre de notions assez large et les calculs associés[^CPGE-Proba]
tout en maintenant un niveau de technicité relativement limité, un luxe dont nous
ne disposerons malheureusement plus dans cette UE.
La problématique de simulation de systèmes aléatoires est présente 
mais de façon limitée dans les programmes. La modélisation 
de systèmes aléatoires fait en théorie partie des compétences
attendues, mais semble en pratique peu présente. 
Or ces deux compétences, importantes pour l'ingénieur, 
doivent être développées.

[^restr]: Dans les filières MP, PSI, PC, etc; dans d'autres filières
comme B/L, ECE, ECS, certaines variables aléatoires réelles continues sont introduites.

La première partie (2 sessions, 1er EC) commence par des rappels des résultats 
de classes préparatoires (cadre discret), mis en perspective relativement aux 
besoins de modélisation du réel et à l'histoire des probabilités. 
On sensibilise ainsi d'emblée les élèves à l'un des points les moins exploités 
en CPGE et utile (entre autres) à l'UE 21 : la modélisation probabiliste. 
L'accent est ensuite mis sur la rupture qu'est l'introduction des variables 
aléatoires réelles 
continues (à densité), avec une relative économie de moyens techniques
(en exploitant la théorie intégrale développée dans le 1er EC).

La seconde partie (3 sessions, 2nd EC) introduit les notions plus complexes
de vecteurs aléatoires, de conditionnement, etc. Elle fera également la jonction
avec les éléments de théorie abstraite de la mesure et du calcul intégral pour
développer les résultats (notamment asymptotiques) qui nécessitent le cadre
le plus général. Le volet de simulation sera consacré aux méthodes de Monte-Carlo,
à la fois comme méthode de simulation de phénomènes aléatoires et comme
technique d'intégration numérique; il sera prolongé par un projet numérique.

[^CPGE-Proba]: Le programme de 1ere année est consacré aux
probabilités dans des univers finis; en seconde année sont étudiées
les variables aléatoires discrètes. Sur les filières MP/PSI/PC, le
périmètre est relativement large: univers, événements, variables aléatoires,
fonction de répartition, lois conditionnelles, espérance, variance, 
etc. jusqu'à une introduction aux séries génératrices et aux résultats
asymptotiques. Cependant, le poids des probabilités dans la formation des CPGE
-- qui pourrait sembler significatif à la lecture des programmes -- 
ne représente en fait que quelques semaines de la formation. 
Une grande variabilité semble exister entre
filières (MP / PSI-PC) et également d'un enseignant à l'autre, la place
des probabilités dans les programmes de Mathématiques des CPGE ne faisant 
pas l'unanimité et les professeurs étant inégalement formés à la discipline.

### Principes

  - **Durée (6-9 semaines par EC).** 
    Le programme de référence de l'UE ci-après 
    associe à chaque EC une plage de 6 semaines. 
    Cette durée n'est pas une recommandation, mais un seuil plancher,
    à partir duquel on peut sans difficulté construire un programme sur
    7, 8 ou 9 semaines par EC, 9 semaines étant probablement 
    ce qui serait préférable[^recomm-durée].

  - **Cours Magistral "Classique".** Un consensus se dégage pour souhaiter
    l'adoption de modalités relativement classiques, c'est-à-dire 
    l'usage de la craie et du tableau noir[^em]
    plutôt que l'usage de transparents. Cette modalité répond à plusieurs
    objectifs: plus familière des étudiants des classes préparatoires qui
    savent l'exploiter de façon efficace, elle facilite également une
    attitude plus active. Enfin, dans un contexte où la tentation est grande
    de balayer un grand nombre de notions en très peu de temps, obliger
    l'enseignant à écrire les choses agit comme un "limiteur de vitesse"
    qui est le bienvenu. Il apparaît alors comme indispensable de faire
    des choix en amont sur les notions à enseigner et de travailler sur 
    une scénarisation cohérente et réaliste des sessions de cours, 
    et l'articulation avec les ressources pédagogiques mises à
    disposition. 

    A noter que l'enseignement "Mathématiques 3" a introduit puis développé
    des sessions tutorées d'étude des ressources pédagogiques en substitution
    des cours magistraux, sur la base du choix des étudiants. 
    Si les cours magistraux sont encore choisis
    majoritairement, les étudiants qui optent pour la
    formule tutorée font état d'une satisfaction plus élevée que ceux
    ayant choisi les cours magistraux[^data-M3].
    Nous n'avons pas opté pour ce type de modalité pour la rentrée 2019
    compte tenu des défis majeurs que présente déjà la formule classique,
    mais il conviendra de reconsidérer la question dans le futur.

[^data-M3]: avec en 2018 des satisfactions de 3.68/4, 3.90/4 et 3.94/4 pour les 
trois sessions de tutorats quand les cours magistraux classiques sont à 
3.14/4 et 3.29/4.

[^em]: ou équivalent: marqueurs et tableaux blancs ou stylet et tablettes 
       graphiques et vidéoprojecteur, etc. remplissent le même rôle.

  - **Cours Magistral et Pédagogie active.** 
    Le groupe de travail souligne 
    les potentielles difficultés liées à l'organisation de cours magistraux aussi 
    longs que 1h30, une durée qui est susceptible d'être peu efficace et de
    démotiver les étudiants si aucune adaptation n'est envisagée.
    Les solutions évoquées reposent soit sur une diminution de la
    durée du cours -- par exemple 1h de cours puis 2h de travaux
    dirigées au sein d'une plage de 2 $\times$ 1h30 -- un schéma 
    probablement complexe à mettre en œuvre dans l'organisation 
    de la scolarité envisagée -- 
    ou -- ce que nous envisageons pour la rentrée 2019 -- 
    sur la nécessité de ponctuer l'enseignement 
    magistral de plages où les étudiants sont actifs 
    (qu'il s'agisse de plages de questions, 
    de courtes sessions d'exercices, d'expérimentations numériques, 
    etc.). Les enseignements de Physique Quantique et Statistique
    (UE 13 dans la nouvelle maquette) disposent d'expériences 
    très positives avec ce type de modalité.



  - **Equilibre Cours/Travaux Dirigés/Travail Personnel.** 
    Chaque session de cours est associée à une session de travaux dirigés 
    et complétée par une session de travail personnel dédiée,
    ce qui fournit un schéma lisible garantissant aux étudiants un
    temps minimum pour chaque phase d'apprentissage.
    Quelques jours devront séparer chaque session de cours 
    de la session de travaux dirigés correspondante pour laisser
    aux étudiants le temps d'assimiler. À l'inverse, les séances
    de travail personnel seront programmées immédiatemment après
    les séances de travaux dirigés pour faciliter la mise en œuvre
    des tutorats.

  - **Travail Personnel: Autonomie Totale et Tutorats.** 
    Les étudiants doivent consacrer en moyenne 24 sessions de 1h30 de travail 
    personnel à l'unité d'enseignement. 
    Ces sessions auront une programmation de référence à l'emploi du temps 
    et un contenu de référence, dans une double logique: fournir à la plupart
    des élèves un guide -- purement indicatif -- sur l'organisation "standard"
    de leur temps de travail et permettre pour les autres un accès élargi
    aux équipes pédagogiques à travers un tutorat.

    Le tutorat se distingue des autres modalités pédagogiques par son coté 
    individualisé et flexible; il s'agit d'accompagner des étudiants dans
    leur démarche d'apprentissage si ceux-ci en font la demande, 
    en s'adaptant à leurs besoins, et de favoriser le développement de leur 
    autonomie.

    Optionnel, voire ponctuel ou temporaire, 
    il ne concerne donc pas l'ensemble des étudiants; d'autres profiteront de
    ces sessions pour travailler en totale autonomie. 
    Il se veut l'outil principal de soutien et de 
    remédiation pour les élèves en difficulté, 
    ne disposant pas des prérequis souhaités,
    ayant des problèmes de méthodologie, etc.
    Il peut également être exploité par les étudiants les plus avancés
    -- à leur demande -- pour aller au-delà des objectifs d'apprentissage de 
    l'enseignement proposé.
    Dans les deux cas, il s'adresse à des étudiants qui vont devoir travailler 
    plus que la moyenne sur l'UE, qu'il s'agisse d'un besoin pour atteindre
    les objectifs de l'UE ou d'un projet personnel d'aller plus loin; 
    il ne se substitue donc pas intégralement
    au travail en totale autonomie.

  - **Examen de Mi-Parcours.**
    Se reporter à la section "[Modalités d'Evaluation]" pour le contexte.
    Le projet de l'UE nécessite que l'évaluation du premier EC soit
    programmée juste avant une pause dans les enseignements de l'UE 
    pour que l'équipe pédagogique puisse corriger les examens, analyser
    les prestations des étudiants et le cas échéant individualiser la
    prise en charge et les objectifs de certains étudiants dans le cadre
    du second EC.


  - **Projets Numériques.** 
    Les deux EC comportent au total trois projets numériques qui complètent 
    les cours et travaux dirigés par un volet applicatif/concret/expérimental,
    pour un total de 9h de travail personnel.
    Ces projets, bien que préparés par des sessions des cours et/ou TDs,
    ne sont pas conçus comme des travaux pratiques en face-à-face pédagogique, 
    mais affectés au temps de travail personnel des étudiants pour une plus
    grande flexibilité et efficacité des apprentissages.
    Comme le reste des activités de travail personnel, ils feront l'objet
    de séances de tutorat optionnelles programmées à l'emploi du temps;
    typiquement une plage de 3h consécutives, programmée hors-horaire.

[^recomm-durée]: 9 semaines par EC correspond à 3h (2 sessions de 1h30) 
  de face-à-face pédagogique, et 5h de charge de travail totale par semaine.

Chaque item listé fait référence à une session de 1h30; 
les sessions de travail personnel (autonomie ou tutoré) sont listées en italique.

**Modalités:**

  - C: cours, 
  
  - TD: travaux dirigés, 

  - EX: examen,

  - TL: travail libre,

  - PN: projet numérique.

### Calcul Différentiel, Intégral et Stochastique I

Semaine 1:

  - Jour 1:
  
    - Topologie (C)

  - Jour 2:
  
    - Calc. Diff. 1 (C)
    
    - Topologie (TD) *+ Topologie (TL)*

  - Jour 3:
  
    - Calc. Diff. 1 (TD) *+ Calc. Diff. 1 (TL)* 

Semaine 2: 

  - Jour 1:
  
    - Calc. Diff. 2 (C)

  - Jour 2:
  
    - Calc. Int. 1 (C) 
    
    - Calc. Diff. 2 (TD) *+ Calc. Diff. 2 (TL)*

Semaine 3:

  - Jour 1:
  
    - Calc. Int. 1 (TD) *+ Calc. Int. 1 (TL)*

  - Jour 2:
  
    - Calc. Int. 2 (C) 
    
    - *Calc. Diff. 2 (PN) + Calc. Diff. 2 (PN)*

Semaine 4: 

  - Jour 1:

    - Proba 1 (C)

    - Calc. Int. 2 (TD) *+ Calc. Int. 2 (TL)*


  - Jour 2:
  
    - Proba 1 (TD) *+ Proba 1 (TL) *
  
  - Jour 3:
  
    - Proba 2 (C)

Semaine 5: 

  - Jour 1:
  
    - Calc. Int. 3 (C)

    - Proba 2 (TD) *+ Proba 2 (TL)*
  
  - Jour 2:
  
    - Calc. Int. 3 (TD) *+ Calc. Int. 3 (TL)*  

Semaine 6:

  - Jour 1:
  
    - *Révisions (TL) + Révisions (TL)*
  
  - Jour 2:
  
    - Examen (EX) + Examen (EX)


### Calcul Différentiel, Intégral et Stochastique II


Semaine 1:

  - Jour 1:
  
    - Calc. Int. 4 (C)

  - Jour 2:
  
    - Equa. Diff. 1 (C)
    
    - Calc. Int. 4 (TD) *+ Calc. Int. 4 (TL)*

Semaine 2: 

  - Jour 1:
  
    - Calc. Int. 5 (C)

    - Equa. Diff. 1 (TD) *+ Equa. Diff. 1 (TL)*

  - Jour 2:
  
    - Equa. Diff. 2 (C) 
    
    - Calc. Int. 5 (TD) *+ Calc. Int. 5 (TL)*

Semaine 3:

  - Jour 1:
  
    - Proba. 3 (C) 
    
    - Equa. Diff 2 (TD) *+ Equa. Diff. 2 (TL)*

  - Jour 2:
  
    - Calc. Diff. 3 (C) 
    
    - Proba. 3 (TD) *+ Proba. 3 (TL)*

  - Jour 3:

    - *Equa. Diff. (PN) + Equa. Diff. (PN)*

Semaine 4: 

  - Jour 1:

    - Proba. 4 (C)

    - Calc. Diff. 3 (TD) *+ Calc. Diff. 3 (TL)* 

  - Jour 2:
  
    - Proba. 4 (TD) *+ Proba. 4 (TL)*

 
Semaine 5: 

  - Jour 1:
  
    - Proba. 5 (C)
 
  - Jour 2:

    - Proba. 5 (TD) *+ Proba. 5 (TL)*

  - Jour 3:

    - *Proba. 5 (PN) + Proba. 5 (PN)*

Semaine 6:

  - Jour 1:
  
    - Examen (EX) + Examen (EX)


Ressources Pédagogiques
--------------------------------------------------------------------------------

Un ensemble de documents comprenant les supports des cours, travaux dirigés et
projets numériques sera développé en suivant les trois principes suivants.

  - **Accès libre.**
    Les documents associés à l'UE sont mis à disposition sans formalité et
    sous forme digitale à toute personne souhaitant y avoir accès.
    Cette mise à disposition se fait dans le cadre d'une licence
    de type Creative Commons CC-BY-NC-SA, qui offre une grande liberté
    dans l'usage et la redistribution des documents.
    Le développement et l'évolution des ressources se
    déroulera de façon publique et transparente, 
    ce qui facilite des schémas collaboratifs et participatifs.
    
  - **Reproductibilité.** 
    La politique d'accès libre et public aux ressources pédagogiques
    ne se limite pas aux documents eux-mêmes, mais s'étend à tous les
    fichiers nécessaires à leur (re-)production.
    Afin de faciliter leur modification et leur usage,
    les documents sont produits
    au moyen de technologies *open-source* et exploitent des formats
    ouverts et adaptés; un effort spécifique est également entrepris pour 
    simplifier la reproduction de l'environnement logiciel nécessaire à 
    cette démarche[^reprod].    

  - **Formes Digitales.** La production de documents papiers et e-books au
    format PDF est prévue, mais le processus et les outils de développements 
    utilisés intègrent en amont la nécessité d'évoluer à brève échéance
    vers d'autres formats plus riches en fonctionnalités et plus adaptés au 
    monde digital (HTML, notebooks, etc).

[^reprod]: en explicitant les dépendances logicielles, 
en facilitant leur installation au sein d'environnements virtuels 
et en mettant en œuvre une démarche d'[intégration continue](https://fr.wikipedia.org/wiki/Int%C3%A9gration_continue)
pour produire automatiquement les ressources pédagogiques.

De ces principes généraux, qui ont une composante idéologique, 
découlent également de bénéfices très concrets, comme ceux listés ci-après.

  - **Développement durable.** Les évolutions des contenus enseignés
    en lycée et classes préparatoires et du projet de formation du cycle au cours
    du temps, les changements d'équipe pédagogique mettant en œuvre le projet,
    etc. sont autant de facteurs qui nécessitent l'adaptation régulière 
    des ressources pédagogiques. Aujourd'hui, le modèle de production et
    de propriété intellectuelle peut être fermé, et tend à encourager 
    la production de ressources de qualité[^publiables] 
    mais également largement immuables.
    La réutilisation de l'existant est faible; les évolutions se font 
    principalement par à-coup, sans réelle continuité, et chaque itération
    a un coût important. 
    Le modèle que nous mettrons en œuvre promet au contraire 
    une forme de "développement durable" où les ressources sont vivantes,
    en évolution, et les investissements initiaux peuvent être mieux 
    réutilisés.

  - **Agilité.** Il est difficile d'anticiper aujourd'hui la forme 
    et la configuration dans lesquelles les ressources pédagogiques 
    devraient être consommées.  Il peut ainsi être nécessaire de produire 
    des ressources pédagogiques avec et sans annotations 
    (cf. section "[Acquis d'Apprentissage]"), organisées par thématique
    ou regroupant toutes les ressources de l'UE, 
    adaptées à un public malvoyant, destinées à l'impression ou à
    des formats électroniques variés (PDF, HTML, etc.), 
    réutilisables dans des cours en ligne, etc.
    Ce qui est certain c'est qu'une forme unique ne va pas convenir 
    à tous les usages et qu'il faut donc prévoir en amont une chaîne 
    d'outils permettant une grande flexibilité. 
    Le système de préparation de documents LaTeX, 
    très majoritairement utilisé pour élaborer des documents en Mathématiques,
    est malgré son grand âge, encore très novateur et de grande qualité
    sur de multiples aspects. Néanmoins, il est dévenu également très insuffisant 
    à bien des égards et doit donc faire partie d'une solution plus globale.
    
<!--

  - Communication, DOI, etc.

  - Appropriation (élèves, etc.), 

-->


[^publiables]: au sens de "publiable par un éditeur scientifique".


Processus Qualité
--------------------------------------------------------------------------------

**Groupe de Travail.** Ont été associés au groupe de travail au fur et à mesure 
du projet:

  - Paul-Adrien Blancquart, Marin Boyet, Alexandre Himmelein, 
    étudiants ou jeunes diplômés du cycle ingénieur civil, qui
    se sont portés volontaires pour participer à la réflexion 
    portant sur l'UE 11. Marin Boyet s'est impliqué plus largement
    dans la réflexion sur la refonte du cycle IC dans son ensemble
    depuis son commencement.
 
  - Silviu Niculescu (Centrale-Supélec), 
    Michel Schmitt (Ministère de l'Economie et des Finances), 
    Gabriel Stoltz (Ecole des Ponts ParisTech), comme experts.
    Il s'agit d'experts disciplinaires et/ou de formation, 
    qui bien qu'apportant un point de vue extérieur à MINES ParisTech 
    ont une très bonne connaissance de notre formation 
    (responsabilité de direction, participation aux réformes précédentes
    de l'enseignement des Mathématiques, etc.)
    et ont tous des expériences concrètes d'enseignement dans le cycle
    ingénieur civil.

  - Sébastien Giraud (Lycée Kléber), un enseignant de classes préparatoires aux 
    grandes écoles (CPGE) et connaisseur du large spectre des filières de CPGE 
    au sein desquelles nous recrutons. 
    Deux autres entretiens ont été menés à ce stade avec des enseignants 
    en CPGE à Paris et en région parisienne. 
    C'est un dialogue que nous souhaitons maintenir dans la durée ; 
    la réforme actuelle du lycée aura sans doute des répercussions importantes 
    et les enseignants de CPGE seront alors aux avant-postes pour percevoir 
    ces changements.

  - La cellule TICE (Technologies de l'Information et de la Communication
    pour l'Enseignement) de MINES ParisTech -- à travers Willy Morscheidt et 
    Marie-Françoise Curto -- associés notamment sur les questions d'ingénierie
    pédagogique.

  - Au titre de l'équipe pédagogique, Emilie Chautru (GEOSCIENCES),
    Pauline Bernard (CAS), Thomas Romary (GEOSIENCES) et Sébastien 
    Boisgérault (CAOR), également préfigurateur de l'UE, dont les
    compétences disciplinaires correspondent au périmètre de l'UE.
    Des échanges nombreux ont également eu lieu avec les préfigurateurs et les 
    équipes pédagogiques
    des UE 12 -- Informatique -- 13 -- Physique -- et 21 -- Mathématiques Appliquées --
    sans que les interlocuteurs soient formellement associés au groupe de 
    travail.

**Déclinaison du processus qualité.**
L'amélioration continue de l'enseignement passe par un processus
"data-driven" de recueil de données généralisé sur le terrain,
s'inscrivant dans une démarche expérimentale plus explicite
(analyse, décision, mise en œuvre puis évaluation).
Les sources de données seront à la fois informelles, qualitatives,
fournies par les échanges avec les étudiants, échanges qui seront 
renforcés par l'accompagnement personnalisé, et l'usage de questionnaires
dédiés à l'UE, plus précis et quantitatifs. 
Conformément aux expériences menées dans le cours
de Mathématiques 3, nous avons l'intention de recueillir des données
détaillées -- session par session, ressource par ressource, 
intervenant par intervenant, dispositif pédagogique par dispositif pédagogique 
-- sans quoi il est très difficile de mettre en œuvre des actions correctives 
efficaces, et de garantir une totale transparence sur ces informations 
et les actions qui pourront en découler.
Des dispositifs complémentaires -- comme la participation d'observateurs aux
sessions de l'enseignement, au titre de l'expertise disciplinaire
et/ou pédagogique, dégagés de la charge d'encadrement -- auraient également 
un intérêt certain.


Ressources Humaines, Matérielles, Financières
--------------------------------------------------------------------------------

La réalisation du projet de l'UE sera confiée à
Emilie Chautru (GEOSCIENCES), Pauline Bernard (CAS), 
Thomas Romary (GEOSIENCES) et Sébastien Boisgérault (CAOR) 
à travers l'élaboration collaborative des ressources
pédagogiques, la prise en charge des cours magistraux et une
implication dans les autres activités de l'UE (travaux dirigés,
tutorats, évaluation, etc.). 
Une attention particulière sera apportée à la recherche au sein de 
MINES ParisTech de doctorants ou de jeunes enseignants-chercheurs 
susceptibles de compléter l'équipe pédagogique, pour les activités
nécessitant des effectifs plus importants; l'expérience
montre que bien accompagnée, cette implication peut être très bénéfique
pour les deux parties. 
En plus de l'expertise disciplinaire en Mathématiques, 
qui est un prérequis évident pour ces enseignants-chercheurs, 
il conviendra de tenir compte des profils 
ayant une expérience et une motivation forte pour l'enseignement et la 
pédagogie, pouvant contribuer à améliorer la cohérence interne ou externe de l'UE, 
disposant d'une culture numérique forte et/ou d'une bonne 
connaissance du profil des étudiants et du projet de formation.

Les effectifs d'enseignants responsables des sessions en présentiel 
(face-à-face pédagogique ou tutorat) suivent la répartition suivante:

  - Cours magistraux: 1 intervenant ($\times$ 24h).  
    Un intervenant à chaque session dans les modalités actuelles.

  - Travaux dirigés: 6 intervenants ($\times$ 24h).  
    En prévision d'un effectif maximal de 130 étudiants,
    6 groupes de travaux dirigés seront constitués.

  - Tutorats (classique et projet): 6 intervenants ($\times$ 33h).  
    Destinés à des effectifs plus restreints que les travaux dirigés 
    en raison de leur caractère optionnel,
    les tutorats s'inscrivent néanmoins dans une logique d'accompagnement 
    personnalisé et supposent donc un encadrement renforcé. 
    Dans cette optique, et pour assurer une continuité dans l'accompagnement, 
    l'effectif de 6 personnes en charge des travaux dirigés sera maintenue.

Ce découpage ne concerne que les activités en présence des étudiants, 
et laisse de coté des activités et des rôles moins visibles ou
"nobles" mais coûteux en temps et tout aussi importants[^exr], 
qu'il sera intéressant de documenter plus précisément.
Les titres décrivant aujourd'hui officiellement les rôles possibles des 
enseignants-chercheurs dans une UE -- "responsable", "intervenant", 
"chargé d'enseignement" -- sont trop grossiers pour avoir cette 
fonction[^fc].

[^exr]: Tels que: la gestion de l'infrastructure numérique 
pour les ressources pédagogiques, l'accompagnement des doctorants 
dans leur activité d'enseignement, la mise en place d'expérimentations 
pédagogiques, etc. 

[^fc]: Ces catégories classiques ne permettent par exemple pas
de distinguer les contributions à la définition et l'amélioration 
continue du projet, des contributions dans le développement des 
ressources pédagogiques, ou encore du temps passé en face-à-face 
pédagogique ou dans les activités d'accompagnement.

On constatera que les modalités pédagogiques envisagées,
notamment les sessions tutorées, classiques ou numériques, ne s'inscrivent 
pas spontanément dans les dénominations "classiques" servant de base au calcul 
du taux de rémunération horaire pour les enseignants extérieurs (à savoir
"Cours ou Conférences", "Petite Classe", "Travaux Pratiques", 
"Soutien Technique"). Il serait pertinent de revisiter ces catégories en
mettant clairement en évidence quelle différence de travail ou de niveau
d'expertise fonde les écarts importants de rémunération entre les 
différentes catégories[^dPCTP]. En particulier, la place des activités
numériques -- qui sont stratégiques -- dans cette hiérarchie devrait être 
précisées.

[^dPCTP]: Le ratio entre la rémunération horaire des travaux dirigés 
("Petite Classe") et des travaux pratiques est supérieur à 2.

Concernant les problématiques matérielles ou d'infrastructure:

  - Les cours magistraux -- à la forme essentiellement classique --
    nécessitent principalement des amphithéatres dotés de tableaux
    suffisamment grands, à plusieurs volets.
    Des dispositifs technologiques facilitant les interactions pourraient 
    également être envisagés
    (tels que boitiers de vote, tablette graphique, etc.), mais aucune
    solution précise de ce type n'est prévue à ce stade (l'interaction
    pouvant être introduite dans un premier temps de façon plus classique).

  - Concernant les ressources pédagogiques, la transition numérique
    a été prise en compte depuis le départ dans ce projet d'UE avec
    une modernisation des processus.
    Mais cet aspect ne sera mis en œuvre initialement que de façon partielle,
    compte tenu des efforts importants nécessaires qui reposent aujourd'hui
    intégralement sur l'équipe pédagogique.
    Exploiter pleinement ce potentiel numérique supposera un engagement
    et des moyens (développement, valorisation, etc.) conséquents, impliquant
    une gamme plus large d'acteurs.
    
  - Les besoins en terme d'infrastructure informatique
    nécessaires au bon déroulement des projets numériques sont en ligne 
    avec ceux exprimés par l'UE 12 d'Informatique pour son volet
    "Python Numérique".

Annexe -- Référentiel de Base des Compétences CTI
--------------------------------------------------------------------------------

Source CTI: <https://www.cti-commission.fr/fonds-documentaire/document/15/chapitre/1125>

L'acquisition des connaissances scientifiques et techniques et la maîtrise de leur mise en œuvre :

 1. la connaissance et la compréhension d’un large champ de sciences 
    fondamentales et la capacité d’analyse et de synthèse qui leur est associée,

 2. l’aptitude à mobiliser les ressources d’un champ scientifique et technique 
    spécifique,

 3. la maitrise des méthodes et des outils de l’ingénieur :
    identification, modélisation et résolution de problèmes même non familiers 
    et incomplètement définis, l’utilisation des outils informatiques, 
    l’analyse et la conception de systèmes,

 4. la capacité à concevoir, concrétiser, tester et valider des solutions, 
    des méthodes, produits, systèmes et services innovants,

 5. la capacité à effectuer des activités de recherche, fondamentale 
    ou appliquée, à mettre en place des dispositifs expérimentaux, 
    à s’ouvrir à la pratique du travail collaboratif,

 6. la capacité à trouver l’information pertinente, à l’évaluer et à 
    l’exploiter : compétence informationnelle.

L'adaptation aux exigences propres de l'entreprise et de la société :

 7. l’aptitude à prendre en compte les enjeux de l’entreprise 
    (dimension économique, respect de la qualité, compétitivité et productivité, 
    exigences commerciales, intelligence économique),

 8. l’aptitude à prendre en compte les enjeux des relations au travail, 
    d’éthique, de responsabilité, de sécurité et de santé au travail,

 9. l’aptitude à prendre en compte les enjeux environnementaux, 
    notamment par application des principes du développement durable,

10. l’aptitude à prendre en compte les enjeux et les besoins de la société.

La prise en compte de la dimension organisationnelle, personnelle et culturelle :

 11. la capacité à s’insérer dans la vie professionnelle, à s’intégrer 
     dans une organisation, à l’animer et à la faire évoluer 
     (exercice de la responsabilité, esprit d’équipe, engagement et leadership, 
     management de projets, maitrise d’ouvrage, communication avec des 
     spécialistes comme avec des non-spécialistes),

 12. la capacité à entreprendre et innover, dans le cadre de projets personnels 
     ou par l’initiative et l’implication au sein de l’entreprise dans des 
     projets entrepreneuriaux,

 13. l’aptitude à travailler en contexte international  
     (maitrise d’une ou plusieurs langues étrangères et ouverture culturelle 
     associée, capacité d’adaptation aux contextes internationaux),

 14. la capacité à se connaitre, à s’autoévaluer, à gérer ses compétences 
     (notamment dans une perspective de formation tout au long de la vie), 
     à opérer ses choix professionnels.

Références
--------------------------------------------------------------------------------
