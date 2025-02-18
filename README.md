# Option Pricing Model (Black-Scholes)

Ce projet implémente le modèle de **Black-Scholes** pour calculer le prix des options européennes (call et put) en Python.

## Description

Le modèle de Black-Scholes est une méthode bien connue pour évaluer les options financières en fonction des variables suivantes :
- Le prix actuel du sous-jacent
- Le prix d'exercice de l'option (strike price)
- Le temps jusqu'à l'échéance
- Le taux d'intérêt sans risque
- La volatilité du sous-jacent

Ce script utilise la bibliothèque `numpy` pour les calculs numériques et `scipy.stats` pour la fonction de distribution normale.

## Prérequis

Avant d'exécuter le script, assurez-vous d'avoir **Python 3.x** installé ainsi que les bibliothèques suivantes :

```bash
pip install numpy scipy
```

## Utilisation

### Exécution du script

Pour exécuter le script avec les paramètres définis, lancez la commande suivante :

```bash
python option_pricing_modelBS.py
```

### Fonction principale

La fonction `pricing()` calcule le prix d'une option call ou put.

#### Paramètres :
- `s` : Prix actuel du sous-jacent
- `k` : Prix d'exercice de l'option
- `t` : Temps à l'échéance (en années)
- `r` : Taux d'intérêt sans risque
- `vol` : Volatilité annuelle du sous-jacent
- `type` : Type d'option, soit **"c"** pour **call**, soit **"p"** pour **put**

#### Exemple d'utilisation :

```python
from option_pricing_modelBS import pricing

# Définition des paramètres
s = 100      # Prix du sous-jacent
k = 102      # Prix d'exercice
t = 0.66     # Temps à l'échéance en années
r = 0.05     # Taux d'intérêt sans risque
vol = 0.07   # Volatilité annuelle

# Calcul du prix de l'option call
call_price = pricing(s, k, t, r, vol, type="c")
print(f'Call price: {call_price:.2f}')

# Calcul du prix de l'option put
put_price = pricing(s, k, t, r, vol, type="p")
print(f'Put price: {put_price:.2f}')
```

## Exemple de sortie

Pour les paramètres définis ci-dessus, le script affiche :

```
Call price: 4.76
Put price: 3.21
```
