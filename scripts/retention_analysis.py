import pandas as pd
import os

# Definir rutas relativas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
INPUT_FILE = os.path.join(DATA_DIR, 'Churn_Modelling_Cleaned.csv')

# Verificar que el archivo existe
if not os.path.exists(INPUT_FILE):
    raise FileNotFoundError(f"No se encontró el archivo {INPUT_FILE}. Ejecuta 'data_cleaning.py' primero.")

# Cargar dataset limpio
df = pd.read_csv(INPUT_FILE)

# Calcular retención por Tenure
retention_by_tenure = df.groupby('Tenure')['IsActiveMember'].mean() * 100
print("Retención por Tenure (%):")
print(retention_by_tenure)

# Calcular retención por NumOfProducts
retention_by_products = df.groupby('NumOfProducts')['IsActiveMember'].mean() * 100
print("\nRetención por NumOfProducts (%):")
print(retention_by_products)

# Guardar resultados (opcional)
OUTPUT_FILE = os.path.join(DATA_DIR, 'retention_results.csv')
retention_by_tenure.to_csv(OUTPUT_FILE, encoding='utf-8', float_format='%.2f')
print(f"Resultados guardados en: {OUTPUT_FILE}")