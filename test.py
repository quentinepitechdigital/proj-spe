import pandas as pd

# Charger le fichier CSV d'origine
df = pd.read_csv('ventes_luxe_détaillées.csv', sep=';')

# Créer un pivot avec une colonne Montant_Ventes par Canal_Vente
df_pivot = df.pivot_table(index=['Date', 'Catégorie_Produit', 'Événement_Spécial', 'Mois', 'Année'],
                          columns='Canal_Vente', values='Montant_Ventes').reset_index()

# Renommer les colonnes pour avoir le format souhaité
df_pivot.columns = ['Date', 'Catégorie_Produit', 'Événement_Spécial', 'Mois', 'Année'] + \
                   ['Montant_Ventes_' + canal.replace(' ', '_') for canal in df_pivot.columns[5:]]

# Remplacer les valeurs manquantes par 0 (si certaines combinaisons de canaux sont absentes pour certaines dates)
df_pivot.fillna(0, inplace=True)

montant_cols = [col for col in df_pivot.columns if col.startswith('Montant_Ventes')]
df_pivot[montant_cols] = df_pivot[montant_cols].astype(int)

# Enregistrer le nouveau DataFrame dans un fichier CSV
df_pivot.to_csv('ventes_luxe_processed.csv', index=False, sep=';')

print("Le nouveau fichier CSV a été créé avec succès.")