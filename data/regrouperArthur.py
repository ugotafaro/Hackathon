import pandas as pd
import json


data=pd.read_excel('data\\crime\\2010.xlsx', sheet_name=2)
"""
# Création de données factices qui ressembleraient aux données chargées à partir d'une feuille Excel
data = {
    'Index de l\'Etat 4001': [
        'Règlements de compte entre malfaiteurs',
        'Homicides pour voler et à l\'occasion de vols',
        # ... autres crimes
    ],
    'Ain': [0, 0],
    'Aisne': [1, 2],
    # ... autres départements
}
"""

# Convertissons les données en DataFrame pour simuler la lecture à partir d'un fichier Excel.
df = pd.DataFrame(data)

# Initialisation de la structure de données JSON
data_json = {}

# Ajout des données de chaque département dans la structure JSON
for department in df.columns[1:]:  # On commence à 1 pour sauter 'Index de l\'Etat 4001'
    if department not in data_json:
        data_json[department] = {}

    data_json[department]["2010"] = {}
    data_json[department]["2010"]["Janvier"] = {}

    for row in df.itertuples():
        crime_type = row[1]  # La première colonne contient le type de crime
        crime_count = getattr(row, department)
        data_json[department]["2010"]["Janvier"][crime_type] = crime_count

# Conversion en JSON
json_output = json.dumps(data_json, indent=2, ensure_ascii=False)
print(json_output)

# Pour sauvegarder le JSON dans un fichier, vous utiliserez:
# with open('data.json', 'w', encoding='utf-8') as f:
#     json.dump(data_json, f, ensure_ascii=False, indent=2)
