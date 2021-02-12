# %% [markdown]
# # UE 11 – Calcul Différentiel, Intégral et Stochastique 
# # Enquête 2020-2021, Elément Constitutif 1 
# %% [markdown]
# Compléments à [la synthèse automatique des données](https://boisgera.github.io/CDIS/Enquete/2020/report-2020-2021-EC1.html) fournie par Google forms.
# 
# Données brutes : [survey-2020-2021-EC1.csv](https://boisgera.github.io/CDIS/Enquete/2020/survey-2020-2021-EC1.csv)
# %% [markdown]
# ## Dépendances

# %%
# Python Standard Library
import re

# Third-Party Libraries
import matplotlib.pyplot as pp
from matplotlib import cm
pp.rcParams['figure.figsize'] = 16, 5

import numpy as np
import scipy.stats as st
import pandas as pd

from IPython.display import Markdown

# %% [markdown]
# ## Utilitaires

# %%
def barplot(df, key, answers, colormap="viridis", alpha=1.0, invert=False):
    data = df[key].dropna() # filter off empty answers
    data = [len(data[data==k])/len(data)*100 for k in answers]
    n = len(answers)
    index = list(range(n))
    pp.xticks(index, answers)
    pp.axis([-0.5, n-0.5, 0, 100]) 
    pp.grid(True) 
    pp.ylabel("Pourcentage")
    pp.yticks(np.linspace(0, 100, 11))
    colormap = cm.get_cmap(colormap)
    xrange = np.linspace(0.0, 1.0, n)
    if invert:
        xrange = 1.0 - xrange
    colors = [colormap(x) for x in xrange]
    _ = pp.bar(index, data, width=1.0, color=colors, alpha=alpha)
    pp.title(key)


# %%
blacklist = "Jean Auriol Chloé-Agathe Azencott Martin Bauw Pauline Bernard Samy Blusseau Sébastien Boisgérault Delphine Bresch-Pietri Mona Buisson Emilie Chautru Cyril Joly Hubert Ménou Silviu Niculescu Nicolescu Slawomir Pietrasz Thomas Romary Lev-Arcady Sellem Emilia Siviero Dilshad Surroop".split()

pattern = re.compile("|".join(f"({string})" for string in blacklist))

def filter_text(text):
    return pattern.sub(8 * "?", text)


# %%
def comments(df, number=0, label=None, filter=True):
    key = "Commentaires"
    if number:
        key += f".{number}"
    data = df[key]
    text = "### Commentaires"
    if label:
        text += f" – {label}\n\n"
    for item in df[key]:
        if isinstance(item, str) and item:
            text += f" - {item}\n\n"
    if filter:
        text = filter_text(text)
    return Markdown(text)


# %%
def hist_diff(df, label=None, color="black", kde=True):
    data = df["Difficulté"]
    m, s = np.nanmean(data), np.nanstd(data)
    n = len(data)
    try:
        label += f" ({n} élèves)"
    except:
        pass
    pp.hist(data, bins=np.linspace(0.0, 3.0001, 4*3 + 1), density=True, color=color, alpha=0.15,label=label)
    pp.legend()

    if len(data)>= 5:
        data.plot.kde(lw=2, color=color)
    bottom, top = pp.gca().get_ylim()
    pp.plot([m, m], [0.0, top], "-", color=color)
    if len(data) >= 5:
        pp.plot([m-s, m-s], [0.0, top], "--", color=color, alpha=0.5)
        pp.plot([m+s, m+s], [0.0, top], "--", color=color, alpha=0.5)
    pp.axis([0, 3, bottom, top])
  
    pp.xticks([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0], ["trop faible", "", "plutôt faible", "(moyenne)", "plutôt forte", "", "trop forte"])
    pp.yticks([])
    pp.title("Difficulté")

    pp.ylabel("Densité")


# %%
def hist_interest(df, label=None, color="black"):
    data = df["Intérêt"]
    m, s = np.nanmean(data), np.nanstd(data)
    n = len(data)
    try:
        label += f" ({n} élèves)"
    except:
        pass
    pp.hist(data, bins=np.linspace(0.0, 3.0001, 4*3 + 1), density=True, color=color, alpha=0.15,label=label)
    pp.legend()

    if len(data) >= 5:
        data.plot.kde(lw=2, color=color)
    bottom, top = pp.gca().get_ylim()
    pp.plot([m, m], [0.0, top], "-", color=color)
    if len(data) >= 5:
        pp.plot([m-s, m-s], [0.0, top], "--", color=color, alpha=0.5)
        pp.plot([m+s, m+s], [0.0, top], "--", color=color, alpha=0.5)
    pp.axis([0, 3, bottom, top])
  
    pp.xticks([0.0, 1.0, 1.5, 2.0, 3.0], ["Faible", "Plutôt faible", "", "Plutôt fort", "Fort"])
    pp.yticks([])
    pp.title("Intérêt/Utilité")

    pp.ylabel("Densité")

# %% [markdown]
# ## Données

# %%
df = pd.read_csv("survey-2020-2021-EC1.csv")

# %% [markdown]
# ### Calculs préalables
# %% [markdown]
# Nous calculons la difficulté globale avec la difficulté de chaque thème, pondérée par le nombre de sessions qu'il occupe. 

# %%
diff = {"Trop facile": 0 , "Plutôt facile": 1, "Plutôt difficile": 2, "Trop difficile": 3}
df["TO"] = df["Le thème X de l'enseignement vous a paru [Topologie]"].map(diff)
df["CD"] = df["Le thème X de l'enseignement vous a paru [Calcul différentiel]"].map(diff)
df["CI"] = df["Le thème X de l'enseignement vous a paru [Calcul intégral]"].map(diff)
df["PR"] = df["Le thème X de l'enseignement vous a paru [Probabilités]"].map(diff)
df["Difficulté"] = (df["TO"] + 2* df["CD"] + 3 * df["CI"] + 2 * df["PR"]) / 8


# %%
interest = {"Pas du tout": 0 , "Plutôt non": 1, "Plutôt oui": 2, "Tout à fait": 3}
df["TO.U"] = df["Le thème X de l'enseignement vous a semblé utile / pertinent / intéressant [Topologie]"].map(interest)
df["CD.U"] = df["Le thème X de l'enseignement vous a semblé utile / pertinent / intéressant [Calcul différentiel]"].map(interest)
df["CI.U"] = df["Le thème X de l'enseignement vous a semblé utile / pertinent / intéressant [Calcul intégral]"].map(interest)
df["PR.U"] = df["Le thème X de l'enseignement vous a semblé utile / pertinent / intéressant [Probabilités]"].map(interest)
df["Intérêt"] = (df["TO.U"] + 2* df["CD.U"] + 3 * df["CI.U"] + 2 * df["PR.U"]) / 8


# %%
df["Note Examen / 20"] = pd.to_numeric(df["Note Examen / 20"], downcast="float", errors="coerce")

# %% [markdown]
# ### Catégories
# %% [markdown]
# Filières d'origine :

# %%
MP = df[df["Filière d'origine"]=="MP/MP* : classe préparatoire Mathématiques-Physique"]
PSI = df[df["Filière d'origine"]=="PSI/PSI* : classe préparatoire Physique-Sciences de l'Ingénieur"]
PC = df[df["Filière d'origine"]=="PC/PC* : classe préparatoire Physique-Chimie"]
PT = df[df["Filière d'origine"]=="PT/PT* : classe préparatoire Physique-Technologie"]
TSI = df[df["Filière d'origine"]=="TSI : classe préparatoire Technologie et Sciences Industrielles"]
ATS = df[df["Filière d'origine"]=="ATS : classe préparatoire Adaptation Technicien Supérieur"]
AST_Fr = df[df["Filière d'origine"]=="AST Fr. : admis sur titres (France)"]
AST_Etr = df[df["Filière d'origine"]=="AST Etr. : admis sur titres (Etranger)"]


# %%
GS = df.loc[[5, 10, 19, 30, 39, 67, 91, 8]] # déterminé manuellement (les réponses sont parfois erronées).


# %%
labels = ["MP", "PSI", "PC", "PT", "TSI", "ATS", "AST_Fr", "AST_Etr"]
_ = pp.pie([len(eval(label)) for label in labels], labels=labels)

# %% [markdown]
# ## Satisfaction
# %% [markdown]
# L'enseignement est jugé globalement un peu mieux que "plutôt satisfaisant", avec aucune opinion "insatisfaite" exprimée et moins de 5 % d'opinions "plutôt insatisfaites" exprimées. Cette satisfaction est également assez peu sensible par rapport à la filière d'origine ; ce sont les MP qui préfèrent légèrement plus l'enseignement et les filières ATS, AST, TSI qui sont légèrement  moins satisfaites (en moyenne tout de même "plutôt satisfaites" avec 2.0 / 3.0 ; attention toutefois aux analyses les concernant car elle ne sont basées que sur 5 réponses). 

# %%
barplot(
    df,
    "Globalement, cet enseignement vous a paru [Votre réponse]",
    ["Pas du tout satisfaisant", "Peu satisfaisant", "Plutôt satisfaisant", "Très satisfaisant"],
    colormap="plasma", alpha=0.75, invert=True
    )


# %%
mapping = {"Pas satisfaisant": 0, "Peu satisfaisant": 1, "Plutôt satisfaisant": 2, "Très satisfaisant": 3}
df["Satisfaction"] = df["Globalement, cet enseignement vous a paru [Votre réponse]"].map(mapping)
dfs = df.dropna(subset=["Satisfaction"])
print("Satisfaction moyenne:", np.round(np.nanmean(dfs["Satisfaction"]), 2), "/ 3.0")
dfs.groupby("Filière d'origine")["Satisfaction"].agg(["mean", "count"]).sort_values("count").style.format({"mean" : "{0:,.1f} / 3.0"}).bar(color='#FFA07A', align='zero', subset=["mean"]).bar(color='lightgreen', align='zero', subset=["count"]).set_caption("Satisfaction, par filière")


# %%
groupe_1 = df.loc[[5, 10, 19, 30, 39, 67, 91, 8]]

# %% [markdown]
# ## Difficulté perçue
# 
# L'enseignement est perçu en moyenne comme (un peu plus dur que) "moyennement difficile". Les variations d'une filière d'origine à l'autre sont assez faibles pour les PC, PSI et MP (les trois filières les plus importantes en volume), mais assez importante au sein de chaque filière. 

# %%
hist_diff(df, label="Tous")


# %%
hist_diff(MP, label="MP", color="green")


# %%
hist_diff(PSI, label="PSI", color="blue")


# %%
hist_diff(PC, label="PC", color="orange")


# %%
hist_diff(GS, label="Groupe de soutien", color="teal")


# %%
hist_diff(PT, label="PT", color="red")
hist_diff(AST_Fr, label="AST Fr.", color="purple")
hist_diff(TSI, label="TSI", color="magenta")
hist_diff(AST_Etr, label="AST Etr.", color="gold")
hist_diff(ATS, label="ATS", color="sienna")

# %% [markdown]
# ### Difficulté perçue et note à l'examen
# 
# La note à l'examen diminue en moyenne avec la difficulté (perçue) de l'enseignement. Toutefois, cette corrélation est plus forte pour les PC que les PSI et a fortiori pour les MP ; pour les MP la difficulté perçue de l'enseignement n'est plus un facteur explicatif significatif de la note à l'examen.

# %%
pp.scatter(df["Difficulté"], df["Note Examen / 20"], alpha=0.5, s=200)
pp.yticks([0.0, 5.0, 10.0, 15.0, 20.0])
pp.xticks([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0], ["Trop facile", "", "", "Difficulté Moyenne", "", "", "Trop difficle"])
pp.grid(True)
pp.axis([0.0, 3.0, 0.0, 20.0])

dfv = df[df["Note Examen / 20"].notnull() & df["Difficulté"].notnull()]
X, Y = dfv["Difficulté"], dfv["Note Examen / 20"]
print(f"corrélation Note / Difficulté : {X.corr(Y):.2g}")

Xs, Ys = dfv["Difficulté"].to_numpy().reshape((-1, 1)), dfv["Note Examen / 20"].to_numpy().reshape((-1, 1))
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(Xs, Ys)
m, M = lr.predict([[0.0], [3.0]])
_ = pp.plot([0, 3.0], [m, M], "r--")


# %%
pp.figure()
pp.xticks([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0], ["Trop facile", "", "", "Difficulté Moyenne", "", "", "Trop difficle"])
pp.yticks([0.0, 5.0, 10.0, 15.0, 20.0])

def s(df, label, color):
    dfv = df[df["Note Examen / 20"].notnull() & df["Difficulté"].notnull()]
    X, Y = dfv["Difficulté"], dfv["Note Examen / 20"]
    print(f"{label}: corrélation Note / Difficulté : {X.corr(Y):.2g}")

    Xs = df["Difficulté"].to_numpy().reshape((-1, 1))
    Ys = df["Note Examen / 20"].to_numpy().reshape((-1, 1))
    
    # Sklearn doesn't like nan
    is_ = [i for i in range(len(Xs)) if not np.isnan(Xs[i]) and not np.isnan(Ys[i])]
    lr = LinearRegression()
    lr.fit(Xs[is_], Ys[is_])
    pp.scatter(Xs, Ys, color=color, alpha=0.5, s=200, label=label)
    [m, M] = lr.predict([[0.0], [3.0]])
    pp.plot([0.0, 3.0], [m, M], "--", color=color)
    pp.xlabel("Difficulté")

s(MP, "MP", "green")
s(PSI, "PSI", "blue")
s(PC, "PC", "orange")

pp.grid(True)
pp.axis([0.0, 3.0, 0.0, 20.0])
_ = pp.legend()

# %% [markdown]
# ## Intéret & Utilité de l'enseignement
# 
# L'intérêt/utilité perçu de l'enseignement est bonne (supérieure à "plutôt forte"). La variabilité selon la filière d'origine est relativement faible. Il ne semble pas y avoir de lien évident entre la difficulté perçue de l'enseignement et son intérêt/utilité.

# %%
print("Intérêt/utilité de l'enseignement :", round(np.nanmean(df["Intérêt"]), 2), "/ 3.0")
hist_interest(df, label="Tous")


# %%
hist_interest(MP, label="MP", color="green")


# %%
hist_interest(PSI, label="PSI", color="blue")


# %%
hist_interest(PC, label="PC", color="orange")


# %%
hist_interest(GS, label="groupe de soutien", color="teal")


# %%
hist_interest(PT, label="TSI", color="red")
hist_interest(AST_Fr, label="AST Fr.", color="purple")
hist_interest(TSI, label="TSI", color="magenta")
hist_interest(AST_Etr, label="AST Etr.", color="gold")
hist_interest(ATS, label="ATS", color="sienna")


# %%
df_ = df
color="black"

pp.scatter(df_["Difficulté"].to_numpy(), df_["Intérêt"].to_numpy(), alpha=0.5, s=500, c=color)
pp.axis([-0.1, 3.1, 0.9, 3.1])
pp.xlabel("Difficulté")
pp.ylabel("Intérêt/Utilité")
pp.xticks([0, 1, 2, 3],["Trop facile", "Plutôt facile", "Plutôt difficile", "Trop difficile"])
pp.yticks([1, 2, 3],["Peu intéressant", "Plutôt intéressant", "Tout à fait intéressant"])
pp.gcf().set_size_inches(16,16) 
pp.grid(True)

# %% [markdown]
# ## Groupe de soutien
# %% [markdown]
# Des étudiants se sont positionnés incorrectement comme appartenant au groupe de soutien (groupe 1). Les données corrigées manuellement, ci-dessous, montrent une satisfaction légèrement inférieure à la moyenne concernant l'enseignement (attendu compte tenu des filière d'origine des participants), mais le sentiment assez net d'avoir bénéficié de cette formule.

# %%
groupe_1 = df.loc[[5, 10, 19, 30, 39, 67, 91, 8]] # déterminé manuellement (les réponses sont parfois erronées).
groupe_1["Satisfaction"]


# %%
print("Satisfaction :",  np.mean(groupe_1["Satisfaction"]), "/ 3.0")


# %%
groupe_1['Vous êtes globalement satisfait des travaux dirigés [Votre réponse]']


# %%
groupe_1['Vous pensez avoir bénéficié du groupe de soutien (si vous en avez fait partie).']

# %% [markdown]
# ## Tutorats
# %% [markdown]
# #### Participation et satisfaction
# 
# **Tutorats classiques.**
# Approximativement la moitié des étudiants a participé régulièrement ou occasionnellement (au moins une fois sur trois) aux tutorats classiques. Parmi les étudiants assidus, on trouve 
# 
#   1. des étudiants des filières PT, AST, ATS et TSI pour un quart (plus du double de leur poids dans la promotion),
#   
#   2. des étudiants issus de MP, approximativement dans la même proportion que dans la promotion (!),
# 
#   3. des étudiants issus de PSI et PC, mais dans des proportions moindres que dans la promotion.
# 
# Les étudiants issus des filières PT, AST, ATS et TSI ou le poids des Mathématiques est en général plus faible, sont a priori en recherche d'un soutien/tutorat actif en Mathématiques. Les motivations des MPs sont probablement très différenciées avec sans doute la recherche d'un lieu d'étude et/ou l'envie d'aller plus loin. On retrouvera beaucoup plus de PSI et PC en participants occasionnels. On remarquera enfin que tous les étudiants issus de PT, AST, ATS et TSI semblent participer régulièrement ou occasionnellement aux tutorats classiques (les étudiants participant peu ou pas aux tutorats classiques sont tous issus des 3 filières MP, PSI, ou PC).
# 
# La satisfaction quant aux tutorats classique est bonne, avec ~ 85% de plutôt ou tout à fait satisfait. Mais cette proportion passe à 100% avec les PT, AST, ATS et TSI (dont une majorité de "tout à fait satisfait") ; ils sont donc actuellement les principaux bénéficiaires de la formule des tutorats classiques. La proportion de satisfaits retombe à moins de 80% pour les MPs qui ont participé aux tutorats classiques.
# 
# **Tutorats avancés.** Approximativement un tiers des étudiants a participé régulièrement ou occasionnellement aux tutorats avancés. C'est moins que pour les tutorats classiques, mais la satisfaction générale est meilleure que dans les tutorats classique. Pour l'ensemble des participants : ~ 90% de plutôt ou tout à fait satisfaits (dont ~ 55% de "tout à fait satisfaits"). Les participants sont presque au 3/4 issus de la filière MP et leur satisfaction est encore meilleure : ~ 95% de satisfaits, dont ~ 70% de "tout à fait satisfaits". Dans les catégories complémentaires présentes dans les participants assidus (PSI, PC, PT), la satisfaction reste élevée (~85 %), mais il n'y a plus que ~25 % d'étudiants "tout à fait satisfaits". 

# %%
barplot(
    df,
    "Vous avez participé [aux tutorats classiques]",
    ["Moins de 1 fois sur 3", "Au moins 1 fois sur 3", "Au moins 2 fois sur 3"],
    colormap="plasma", alpha=0.75, invert=True
    )


# %%
origin = list(df["Filière d'origine"]) 
labels = list(set(origin)) # get all possible labels, exactly once
# sort them (largest category first)
labels = sorted(labels, key=lambda label: -len(df[df["Filière d'origine"]==label]))
_ = pp.pie([len([item for item in origin if item == label]) for label in labels], labels=labels)
_ = pp.gca().set_title("Filière d'origine (tous)", fontweight="bold", fontsize=18)


# %%
index = df["Vous avez participé [aux tutorats classiques]"] == "Au moins 2 fois sur 3"
dfi = df[index]
origin = list(dfi["Filière d'origine"]) 
_ = pp.pie([len([item for item in origin if item == label]) for label in labels], labels=labels)
_ = pp.gca().set_title("Tutorat classique : participants réguliers", fontweight="bold", fontsize=18)


# %%
index = df["Vous avez participé [aux tutorats classiques]"] == "Au moins 1 fois sur 3"
dfi = df[index]
origin = list(dfi["Filière d'origine"]) 
_ = pp.pie([len([item for item in origin if item == label]) for label in labels], labels=labels)
_ = pp.gca().set_title("Tutorat classique : participants occasionnels", fontweight="bold", fontsize=18)


# %%
index = df["Vous avez participé [aux tutorats classiques]"] == "Moins de 1 fois sur 3"
dfi = df[index]
origin = list(dfi["Filière d'origine"]) 
_ = pp.pie([len([item for item in origin if item == label]) for label in labels], labels=labels)
_ = pp.gca().set_title("Tutorat classique : participants rares et non-participants", fontweight="bold", fontsize=18)


# %%
barplot(
    df, 
    "Si vous y avez participé, vous avez apprécié / trouvé utile [les tutorats classiques]",
    ["Pas du tout", "Plutôt non", "Plutôt oui", "Tout à fait"],
    colormap="plasma", alpha=0.75, invert=True
)
_ = pp.gca().set_title("Tous : " + pp.gca().get_title())


# %%
l = ["PT/PT* : classe préparatoire Physique-Technologie", 
"TSI : classe préparatoire Technologie et Sciences Industrielles",
"ATS : classe préparatoire Adaptation Technicien Supérieur",
"AST Fr. : admis sur titres (France)",
"AST Etr. : admis sur titres (Etranger)"]
index = df["Filière d'origine"].isin(l)
dfi = df[index]
barplot(
    dfi, 
    "Si vous y avez participé, vous avez apprécié / trouvé utile [les tutorats classiques]",
    ["Pas du tout", "Plutôt non", "Plutôt oui", "Tout à fait"],
    colormap="plasma", alpha=0.75, invert=True
)
_ = pp.gca().set_title("PT, TSI, ATS, AST : " + pp.gca().get_title())


# %%
l = ["MP/MP* : classe préparatoire Mathématiques-Physique"]
#PSI = df[df["Filière d'origine"]=="PSI/PSI* : classe préparatoire Physique-Sciences de l'Ingénieur"]
#PC = df[df["Filière d'origine"]=="PC/PC* : classe préparatoire Physique-Chimie"]
index = df["Filière d'origine"].isin(l)
dfi = df[index]
barplot(
    dfi, 
    "Si vous y avez participé, vous avez apprécié / trouvé utile [les tutorats classiques]",
    ["Pas du tout", "Plutôt non", "Plutôt oui", "Tout à fait"],
    colormap="plasma", alpha=0.75, invert=True
)
_ = pp.gca().set_title("MP : " + pp.gca().get_title())


# %%
barplot(
    df,
    "Vous avez participé [aux tutorats avancés]",
    ["Moins de 1 fois sur 3", "Au moins 1 fois sur 3", "Au moins 2 fois sur 3"],
    colormap="plasma", alpha=0.75, invert=True
    )


# %%
origin = list(df["Filière d'origine"]) 
labels = list(set(origin)) # get all possible labels, exactly once
# sort them (largest category first)
labels = sorted(labels, key=lambda label: -len(df[df["Filière d'origine"]==label]))
_ = pp.pie([len([item for item in origin if item == label]) for label in labels], labels=labels)
_ = pp.gca().set_title("Filière d'origine (tous)", fontweight="bold", fontsize=18)


# %%
index = df["Vous avez participé [aux tutorats avancés]"] == "Au moins 2 fois sur 3"
dfi = df[index]
origin = list(dfi["Filière d'origine"]) 
_ = pp.pie([len([item for item in origin if item == label]) for label in labels], labels=labels)
_ = pp.gca().set_title("Tutorat avancé : participants réguliers", fontweight="bold", fontsize=18)


# %%
barplot(
    df, 
    "Si vous y avez participé, vous avez apprécié / trouvé utile [les tutorats avancés]",
    ["Pas du tout", "Plutôt non", "Plutôt oui", "Tout à fait"],
    colormap="plasma", alpha=0.75, invert=True
)
_ = pp.gca().set_title("Tous : " + pp.gca().get_title())


# %%
l = ["MP/MP* : classe préparatoire Mathématiques-Physique"]
index = df["Filière d'origine"].isin(l)
dfi = df[index]
barplot(
    dfi, 
    "Si vous y avez participé, vous avez apprécié / trouvé utile [les tutorats avancés]",
    ["Pas du tout", "Plutôt non", "Plutôt oui", "Tout à fait"],
    colormap="plasma", alpha=0.75, invert=True
)
_ = pp.gca().set_title("MP : " + pp.gca().get_title())


# %%
l = ["PSI/PSI* : classe préparatoire Physique-Sciences de l'Ingénieur",
"PC/PC* : classe préparatoire Physique-Chimie",
"PT/PT* : classe préparatoire Physique-Technologie"]
index = df["Filière d'origine"].isin(l)
dfi = df[index]
barplot(
    dfi, 
    "Si vous y avez participé, vous avez apprécié / trouvé utile [les tutorats avancés]",
    ["Pas du tout", "Plutôt non", "Plutôt oui", "Tout à fait"],
    colormap="plasma", alpha=0.75, invert=True
)
_ = pp.gca().set_title("PSI, PC, PT : " + pp.gca().get_title())

# %% [markdown]
# Charge de travail
# --------------------
# %% [markdown]
#
# Les étudiants ont passé en moyenne : 
#
#   - 16h30 à étudier le cours,
# 
#   - 16h40 à faire des exercices,
# 
#   - 15h20 à travailler sur le projet numérique.
#   
# Si l'on affecte 50% du temps passé sur le projet numérique à l'enseignement informatique (comme annoncé), et que l'on rajoute aux heures déjà listées les 3 heures d'examen et les 20 minutes de soutenance de projet numérique, on obtient un temps de travail total moyen de **44 heures**, très proche de la moyenne théorique de 45 heures affectée par le cursus à l'enseignement. 
# 
# Ce volume de travail varie considérablement d'un étudiant à l'autre, avec un écart-type de ~10 heures. Le facteur explicatif principal est la filière d'origine, comme le montre la composition des populations ayant eu besoin de moins de 35h et celle ayant eu besoin de plus de 55h. Dans la première catégorie on trouve une très marge majorité de MP (presque 3/4), contre moins d'un quart dans la seconde catégorie. Inversement, aucun AST, ATS, TSI ou PT n'est présent dans la première catégorie, alors qu'ils sont surreprésentés dans la seconde (plus d'un quart de la population). Les proportions de PSI et de PC varient moins d'une catégorie à l'autre.
# 
#   

# %%
nan = np.nan
li = df["Temps total consacré à l'étude du cours (en présence des enseignants ou non)"]
l =  ['10',
 nan,
 '15',
 '12',
 '12',
 '18',
 '10',
 '24',
 '24',
 nan,
 'Je ne sais pas, mais je passe beaucoup de temps à relire le cours et à le ficher',
 '15',
 "24",
 '18',
 '16',
 '24',
 '15',
 '16',
 '12',
 '13',
 '16',
 '20',
 '12',
 '22',
 nan,
 '15',
 '15',
 "10",
 '12',
 nan,
 '27.5',
 '4',
 '12',
 '14',
 '21',
 '20',
 '26',
 '10',
 '16',
 '24',
 '15',
 '9',
 nan,
 '10',
 '10',
 '15',
 "13.5",
 '10',
 '20',
 "20",
 nan,
 '18',
 '19',
 '20',
 '12',
 '18',
 '20',
 '24',
 "20",
 '12 ',
 '11',
 '18',
 '30',
 '10',
 '12',
 '20',
 'Non mesuré : probablement dans la moyenne conseillée',
 '25',
 'Je ne saurais donner de temps...',
 '9',
 '17',
 '13',
 '25',
 '12',
 '17',
 '15',
 "20",
 '15',
 '24',
 '20',
 '12',
 '18',
 '24',
 '16',
 "20",
 '24',
 '20',
 '13',
 '15',
 '16',
 '22',
 '16',
 '12',
 '16',
 '10.5',
 nan,
 '10',
 '15',
 '20',
 '15',
 '12',
 '14',
 '15.5',
 '24',
 '14',
 '20',
 '20']
time_old_new = []
for i, x in enumerate(l):
    try:
        l[i] = float(x)
    except:
        l[i] = np.nan
    time_old_new.append([li[i], l[i]])
df["Temps total consacré à l'étude du cours (en présence des enseignants ou non)"] = l

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    display(pd.DataFrame(time_old_new, columns=["Original", "Transcrit"]))


# %%
np.nanmean(l)


# %%
t1 = data = df["Temps total consacré à l'étude du cours (en présence des enseignants ou non)"] 
color="black"
label=None
data.plot.kde(color=color)
m, s = np.nanmean(data), np.nanstd(data)
bottom, top = pp.gca().get_ylim()
pp.plot([m, m], [0.0, top], "--", color=color, alpha=0.5)
pp.plot([m-s, m-s], [0.0, top], "--", color=color, alpha=0.5)
pp.plot([m+s, m+s], [0.0, top], "--", color=color, alpha=0.5)
pp.title("Temps total consacré à l'étude du cours")

# %%
li = df["Temps total consacré aux exercices (en présence des enseignants ou non)"].tolist()
l = ['12',
'13',
'24',
'12',
'16',
'15',
'14',
'20',
'22',
nan,
"En fichant je fais tous les exercices essentiels, je fais les avancés lorsque j'ai relu mon cours et que je pense le maîtriser",
'12',
'15',
'20',
'24',
'15',
'12',
'12',
'15',
'12',
'14',
'16',
'17',
'22',
nan,
'12',
'20',
'15',
'12',
nan,
'27.5',
'17',
'20',
'12',
'18',
'16',
'18',
'14',
'12',
'24',
'13',
'3',
nan,
'17',
'10',
'15',
'14.5',
'12',
'18',
'16.5 ',
nan,
'12',
'13.5',
'24',
'12',
'14',
'14',
'26',
"15",
'12',
'15',
'16',
'24',
'14',
"12",
'23',
"Non mesuré  probablement dans la moyenne conseillée (un peu de préparation à l'avance)",
'30',
'Idem',
'12',
'17',
'16',
'20',
'12',
'24',
'25',
"15",
'12',
'14',
'20',
'12',
'18',
'24',
'13',
'24',
nan,
'20',
'30',
'12',
'18',
'20',
'24',
'12',
'12',
'12',
nan,
'20',
nan,
'12',
'17',
'15',
'16',
'13.5',
'16',
"18",
'12',
'30']
time_old_new = []
for i, x in enumerate(l):
   try:
       l[i] = float(x)
   except:
       l[i] = np.nan
   time_old_new.append([li[i], l[i]])

t2 = df["Temps total consacré aux exercices (en présence des enseignants ou non)"] = l
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
   display(pd.DataFrame(time_old_new, columns=["Original", "Transcrit"]))


# %%
np.nanmean(l)


# %%
t2 = data = df["Temps total consacré aux exercices (en présence des enseignants ou non)"]
color="black"
label=None
data.plot.kde(color=color)
m, s = np.nanmean(data), np.nanstd(data)
bottom, top = pp.gca().get_ylim()
pp.plot([m, m], [0.0, top], "--", color=color, alpha=0.5)
pp.plot([m-s, m-s], [0.0, top], "--", color=color, alpha=0.5)
pp.plot([m+s, m+s], [0.0, top], "--", color=color, alpha=0.5)
pp.title("Temps total consacré aux exercices")

# %%
t3 = data = l = df["Temps total consacré au projet numérique (en présence des enseignants ou non)"]
color="black"
label=None
data.plot.kde(color=color)
m, s = np.nanmean(data), np.nanstd(data)
bottom, top = pp.gca().get_ylim()
pp.plot([m, m], [0.0, top], "--", color=color, alpha=0.5)
pp.plot([m-s, m-s], [0.0, top], "--", color=color, alpha=0.5)
pp.plot([m+s, m+s], [0.0, top], "--", color=color, alpha=0.5)
pp.xticks([0, 10, 20, 30, 40])
pp.title("Temps total consacré au projet numérique")


# %%
np.nanmean(l)


# %%
t = t1 + t2 + 0.5 * t3 + 3.0 + 1/3 # added exams, substracted CS part in project (half)
#t.plot.kde(color=color)
t = t[t.notnull()]
k = st.gaussian_kde(t)
h = np.linspace(0, 100, 1000)
color = "black"
pp.plot(h, k(h), color)
pp.fill_between(h, np.zeros_like(h), k(h), color=color, alpha=0.15)
m, s = np.nanmean(t), np.nanstd(t)
print("moyenne :", m, ", écart-type :", s)
bottom, top = pp.gca().get_ylim()
left, right = pp.gca().get_xlim()
pp.plot([m, m], [bottom, top], "--", color=color)
pp.plot([m-s, m-s], [bottom, top], "--", color=color, alpha=0.5)
pp.plot([m+s, m+s], [bottom, top], "--", color=color, alpha=0.5)
pp.axis([left, right, bottom, top])
ticks = np.r_[0:100:10]
pp.title("Temps de travail total")
pp.xlabel("Temps (en heures)")
pp.ylabel("Densité")
_ = pp.xticks(ticks)


# %%
dfi = df.loc[t[t <= 35].index]
origin = dfi["Filière d'origine"]
_ = pp.pie([len([item for item in origin if item == label]) for label in labels], labels=labels)
_ = pp.gca().set_title("Temps de travail total : moins de 35 h", fontweight="bold", fontsize=18)


# %%
dfi = df.loc[t[t >= 55].index]
origin = dfi["Filière d'origine"]
_ = pp.pie([len([item for item in origin if item == label]) for label in labels], labels=labels)
_ = pp.gca().set_title("Temps de travail total : plus de 55 h", fontweight="bold", fontsize=18)

# %% [markdown]
# ## Equipe pédagogique
# %% [markdown]
# **Satisfaction moyenne vis-à-vis du travail des enseignants.** Le calcul n'est **pas** explicitement pondéré par le nombre d'heures fait par les enseignants (chaque appréciation donnée ayant le même poids). Mais les enseignants ayant vu le plus souvent les élèves et surtout un nombre d'élèves plus grand sont susceptibles d'avoir plus d'appréciations de leur part, et donc indirectement un poids plus important dans le calcul.
# 
# Au final, avec ce mode de calcul, 90% des étudiants apparaissent comme plutôt ou tout à fait satisfaits du travail de l'équipe pédagogique, contre 10% des étudiants qui semblent peu ou pas satisfaits. 

# %%
teachers = "Toutes modalités confondues, êtes-vous satisfait du travail des enseignants" 
all_teachers = [key for key in df.columns.values if key.startswith(teachers)]
#a = df[all_teachers].value_counts()
results = df[all_teachers].apply(pd.value_counts).sum(axis=1) # series
total = results.sum()
percentage = pd.DataFrame({"Satisfaction" : results.apply(lambda s: round(s / total * 100, 2))})
answers = ["Non, pas du tout", "Plutôt non", "Plutôt oui", "Oui, tout à fait"]
percentage = percentage.reindex(answers)
display(percentage)

colormap="viridis"
alpha=0.75
invert=True
n = len(answers)
index = list(range(n))
pp.xticks(index, answers)
pp.axis([-0.5, n-0.5, 0, 100]) 
pp.grid(True) 
pp.ylabel("Pourcentage")
pp.yticks(np.linspace(0, 100, 11))
colormap = cm.get_cmap(colormap)
xrange = np.linspace(0.0, 1.0, n)
if invert:
    xrange = 1.0 - xrange
colors = [colormap(x) for x in xrange]
_ = pp.bar(index, percentage["Satisfaction"], width=1.0, color=colors, alpha=alpha)
_ = pp.title("Etes vous satisfait du travail des enseignants ?")


