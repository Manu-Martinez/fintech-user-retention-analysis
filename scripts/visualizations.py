# scripts/visualizations.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Configurar estilo de gráficos
sns.set_style("whitegrid")

# Definir rutas relativas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
PLOTS_DIR = os.path.join(BASE_DIR, 'plots')
INPUT_FILE = os.path.join(DATA_DIR, 'Churn_Modelling_Cleaned.csv')

# Crear carpeta plots si no existe
if not os.path.exists(PLOTS_DIR):
    os.makedirs(PLOTS_DIR)

# Verificar que el archivo existe
if not os.path.exists(INPUT_FILE):
    raise FileNotFoundError(f"{INPUT_FILE} Not found. Run 'data_cleaning.py' first.")

# Cargar dataset limpio (sin modificarlo)
df = pd.read_csv(INPUT_FILE)

# 1. Curva de retención por Tenure
plt.figure(figsize=(10, 6))
retention_tenure = df.groupby('Tenure')['IsActiveMember'].mean() * 100
sns.lineplot(x=retention_tenure.index, y=retention_tenure.values)
plt.title('Tasa de Retención por Tenure')
plt.xlabel('Tenure (Años)')
plt.ylabel('% Usuarios Activos')
plt.savefig(os.path.join(PLOTS_DIR, 'retention_by_tenure.png'), bbox_inches='tight')
plt.close()

# 2. Barras de retención por NumOfProducts
plt.figure(figsize=(10, 6))
retention_products = df.groupby('NumOfProducts')['IsActiveMember'].mean() * 100
sns.barplot(x=retention_products.index, y=retention_products.values)
plt.title('Tasa de Retención por Número de Productos')
plt.xlabel('Número de Productos')
plt.ylabel('% Usuarios Activos')
plt.savefig(os.path.join(PLOTS_DIR, 'retention_by_products.png'), bbox_inches='tight')
plt.close()

# 3. Heatmap de retención (Tenure vs. NumOfProducts)
plt.figure(figsize=(12, 8))
heatmap_data = df.pivot_table(values='IsActiveMember', index='Tenure', columns='NumOfProducts', aggfunc='mean') * 100
sns.heatmap(heatmap_data, annot=True, fmt='.1f', cmap='Blues')
plt.title('Retención (%) por Tenure y Número de Productos')
plt.xlabel('Número de Productos')
plt.ylabel('Tenure (Años)')
plt.savefig(os.path.join(PLOTS_DIR, 'retention_heatmap.png'), bbox_inches='tight')
plt.close()

# 4. Distribución de Balance por estado de actividad
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Balance', hue='IsActiveMember', multiple='stack', bins=30)
plt.title('Distribución de Balance por Estado de Actividad')
plt.xlabel('Balance ($)')
plt.ylabel('Frecuencia')
plt.savefig(os.path.join(PLOTS_DIR, 'balance_distribution.png'), bbox_inches='tight')
plt.close()

print(f"Plots stored in: {PLOTS_DIR}")