import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("operations_enrichies.csv", parse_dates=[1])

# VARIABLE QUALITATIVE
# Diagramme en secteurs

data["categ"].value_counts(normalize=True).plot(kind='pie')
# Cette ligne assure que le pie chart est un cercle plutôt qu'une éllipse
plt.axis('equal') 
plt.show() # Affiche le graphique

# Diagramme en tuyaux d'orgues
data["categ"].value_counts(normalize=True).plot(kind='bar')
plt.show()

# VARIABLE QUANTITATIVE
# Diagramme en bâtons
data["quart_mois"].value_counts(normalize=True).plot(kind='bar',width=0.1)
plt.show()

# Histogramme
data["montant"].hist(normed=True)
plt.show()

# Histogramme plus beau
data[data.montant.abs() < 100]["montant"].hist(normed=True,bins=20)
plt.show()