import pandas as pd

# Importation des données brutes avec header=2 pour ignorer les 2 premières lignes de métadonnées
CO2df = pd.read_csv('API_EN.ATM.CO2E.KT_DS2_en_csv_v2_713263.csv', header=2)
GDPdf = pd.read_csv('API_NY.GDP.MKTP.CD_DS2_en_csv_v2_713242.csv', header=2)
POPdf = pd.read_csv('API_SP.POP.TOTL_DS2_en_csv_v2_713131.csv', header=2)
TOE_over_POPdf = pd.read_csv('API_EG.USE.PCAP.KG.OE_DS2_en_csv_v2_715552.csv', header=2)
# 1. On crée d'abord une liste contenant les années de '1960' à '2019' en format texte (car les noms de colonnes sont du texte)
annees = [str(annee) for annee in range(1960, 2020)]

# 2. On filtre pour garder la ligne du monde ('WLD'), on sélectionne les colonnes des années, et .squeeze() transforme la ligne en Série
CO2 = CO2df[CO2df['Country Code'] == 'WLD'][annees].squeeze()
# 1. On crée une liste des années de '1960' à '2019' en texte
annees = [str(annee) for annee in range(1960, 2020)]

# 2. On extrait les données pour le monde ('WLD') pour chaque variable
CO2 = CO2df[CO2df['Country Code'] == 'WLD'][annees].squeeze()
GDP = GDPdf[GDPdf['Country Code'] == 'WLD'][annees].squeeze()
POP = POPdf[POPdf['Country Code'] == 'WLD'][annees].squeeze()
TOE_over_POP = TOE_over_POPdf[TOE_over_POPdf['Country Code'] == 'WLD'][annees].squeeze()

# 3. On crée le nouveau tableau de données 'data' demandé dans le TP
data = pd.DataFrame({
    'CO2': CO2,
    'GDP': GDP,
    'POP': POP
})

# 4. On ajoute la colonne TOE en multipliant TOE_over_POP par POP
data['TOE'] = TOE_over_POP * POP
# 1. On définit l'année de base (première année où on a toutes les données)
annee_base = '1971'

# 2. On calcule les indices base 100 pour chaque variable
data['CO2_b100'] = 100 * data['CO2'] / data['CO2'][annee_base]
data['TOE_b100'] = 100 * data['TOE'] / data['TOE'][annee_base]
data['GDP_b100'] = 100 * data['GDP'] / data['GDP'][annee_base]
data['POP_b100'] = 100 * data['POP'] / data['POP'][annee_base]

# 3. On calcule les ratios de l'équation de Kaya en base 100
data['CO2/TOE_b100'] = 100 * data['CO2_b100'] / data['TOE_b100']
data['TOE/GDP_b100'] = 100 * data['TOE_b100'] / data['GDP_b100']
data['GDP/POP_b100'] = 100 * data['GDP_b100'] / data['POP_b100']

import matplotlib.pyplot as plt

# 45.4 Extract relevant data 
# On sélectionne uniquement les 5 colonnes d'indices en base 100 pour l'équation de Kaya
extraction_kaya = data[['CO2_b100', 'CO2/TOE_b100', 'TOE/GDP_b100', 'GDP/POP_b100', 'POP_b100']]

# 45.5 Plot data 
# On trace le graphique. 'logy=True' permet de mettre l'axe Y en échelle logarithmique, tandis que l'axe X reste linéaire.
extraction_kaya.plot(logy=True, figsize=(10, 6))

# On ajoute un peu de décoration pour que le graphique soit propre
plt.title("Équation de Kaya (Base 100 en 1971)")
plt.xlabel("Années")
plt.ylabel("Indices (échelle logarithmique)")
plt.grid(True, which="both", ls="--", linewidth=0.5) # Ajoute une grille pour mieux lire l'échelle log
plt.show()