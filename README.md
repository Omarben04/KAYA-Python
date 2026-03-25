# TP Équation de Kaya — Analyse de Données Mondiales

Ce projet a été réalisé dans le cadre du module de **Python appliqué à l'analyse de données** (L3 TRI — USMB). Il traite des données brutes de la **Banque Mondiale** pour illustrer graphiquement l'équation de **Yoichi Kaya**, qui relie les émissions mondiales de CO₂ à des facteurs démographiques, économiques et énergétiques.

---

## 📐 L'Équation de Kaya

$$CO_2 = \frac{CO_2}{TOE} \times \frac{TOE}{GDP} \times \frac{GDP}{POP} \times POP$$

| Terme | Signification |
|---|---|
| **CO₂** | Émissions totales de dioxyde de carbone |
| **TOE** | Consommation totale d'énergie (tonnes équivalent pétrole) |
| **GDP** | Produit Intérieur Brut mondial |
| **POP** | Population mondiale |

---

## 📁 Structure du projet

```
tp-kaya/
│
├── kaya.py                                                    # Script principal
├── API_EN.ATM.CO2E.KT_DS2_en_csv_v2_713263.csv               # Émissions de CO₂
├── API_NY.GDP.MKTP.CD_DS2_en_csv_v2_713242.csv               # PIB mondial (GDP)
├── API_SP.POP.TOTL_DS2_en_csv_v2_713131.csv                  # Population mondiale
└── API_EG.USE.PCAP.KG.OE_DS2_en_csv_v2_715552.csv            # Consommation d'énergie (TOE/POP)
```

---

## 🛠️ Prérequis

Python 3.x avec les bibliothèques suivantes :

```bash
pip install pandas matplotlib
```

| Bibliothèque | Rôle |
|---|---|
| `pandas` | Manipulation, filtrage et traitement des DataFrames |
| `matplotlib` | Tracé et mise en forme du graphique final |

---

## 🚀 Utilisation

1. Placez les **4 fichiers `.csv`** dans le même répertoire que `kaya.py`.
2. Ouvrez `kaya.py` dans votre IDE (ex : **Spyder**, VS Code).
3. Vérifiez que le **répertoire de travail** de l'IDE pointe bien vers ce dossier.
4. Exécutez le script.

Le programme va :
- Isoler les données mondiales (`Country Code == 'WLD'`) de **1960 à 2019**
- Calculer la variable `TOE` totale via `TOE/POP × POP`
- Ramener toutes les valeurs à une **base 100 en 1971**
- Calculer les ratios de l'équation de Kaya en base 100
- Générer un graphique d'évolution avec une **échelle logarithmique** sur l'axe Y

---

## 📊 Résultat attendu

Le graphique produit affiche l'évolution des 5 composantes de l'équation de Kaya entre 1960 et 2019, toutes normalisées à 100 en 1971 :

- `CO2_b100` — Émissions totales de CO₂
- `CO2/TOE_b100` — Intensité carbone de l'énergie
- `TOE/GDP_b100` — Intensité énergétique de l'économie
- `GDP/POP_b100` — PIB par habitant
- `POP_b100` — Population mondiale

> 📌 L'axe Y est en **échelle logarithmique** (`logy=True`) pour permettre une comparaison lisible entre des grandeurs d'ordres de magnitude très différents.

---

## 🧩 Détail du script `kaya.py`

### 1. Importation des données
```python
CO2df = pd.read_csv('...csv', header=2)  # header=2 ignore les métadonnées Banque Mondiale
```

### 2. Extraction des données mondiales
```python
CO2 = CO2df[CO2df['Country Code'] == 'WLD'][annees].squeeze()
```

### 3. Construction du DataFrame principal
```python
data = pd.DataFrame({'CO2': CO2, 'GDP': GDP, 'POP': POP})
data['TOE'] = TOE_over_POP * POP
```

### 4. Calcul en base 100 (référence : 1971)
```python
data['CO2_b100'] = 100 * data['CO2'] / data['CO2']['1971']
```

### 5. Visualisation
```python
extraction_kaya.plot(logy=True, figsize=(10, 6))
```

---

## 👨‍💻 Auteur

**Omar Benmansour** — L3 Télécommunications et Réseaux Informatiques (TRI)  
Université Savoie Mont Blanc (USMB)
