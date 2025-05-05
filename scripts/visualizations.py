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
    raise FileNotFoundError(f"No se encontró el archivo {INPUT_FILE}. Ejecuta 'data_cleaning.py' primero.")

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

# 2. Tasa de retención por Género
plt.figure(figsize=(10, 6))
retention_gender = df.groupby('Gender')['IsActiveMember'].mean() * 100
sns.barplot(x=retention_gender.index, y=retention_gender.values)
plt.title('Tasa de Retención por Género')
plt.xlabel('Género')
plt.ylabel('% Usuarios Activos')
plt.savefig(os.path.join(PLOTS_DIR, 'retention_by_gender.png'), bbox_inches='tight')
plt.close()

print(f"Nuevo gráfico guardado: {os.path.join(PLOTS_DIR, 'retention_by_gender.png')}")

# 3. Barras de retención por NumOfProducts
plt.figure(figsize=(10, 6))
retention_products = df.groupby('NumOfProducts')['IsActiveMember'].mean() * 100
sns.barplot(x=retention_products.index, y=retention_products.values)
plt.title('Tasa de Retención por Número de Productos')
plt.xlabel('Número de Productos')
plt.ylabel('% Usuarios Activos')
plt.savefig(os.path.join(PLOTS_DIR, 'retention_by_products.png'), bbox_inches='tight')
plt.close()

# 4. Heatmap de retención (Tenure vs. NumOfProducts)
plt.figure(figsize=(12, 8))
heatmap_data = df.pivot_table(values='IsActiveMember', index='Tenure', columns='NumOfProducts', aggfunc='mean') * 100
sns.heatmap(heatmap_data, annot=True, fmt='.1f', cmap='Blues')
plt.title('Retención (%) por Tenure y Número de Productos')
plt.xlabel('Número de Productos')
plt.ylabel('Tenure (Años)')
plt.savefig(os.path.join(PLOTS_DIR, 'retention_heatmap.png'), bbox_inches='tight')
plt.close()

# 5. Distribución de Balance por estado de actividad
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Balance', hue='IsActiveMember', multiple='stack', bins=30)
plt.title('Distribución de Balance por Estado de Actividad')
plt.xlabel('Balance ($)')
plt.ylabel('Frecuencia')
plt.savefig(os.path.join(PLOTS_DIR, 'balance_distribution.png'), bbox_inches='tight')
plt.close()

# 6. Tasa de retención por Geography
plt.figure(figsize=(10, 6))
retention_geography = df.groupby('Geography')['IsActiveMember'].mean() * 100
sns.barplot(x=retention_geography.index, y=retention_geography.values)
plt.title('Tasa de Retención por Geografía')
plt.xlabel('País')
plt.ylabel('% Usuarios Activos')
plt.savefig(os.path.join(PLOTS_DIR, 'retention_by_geography.png'), bbox_inches='tight')
plt.close()

# 7. Tasa de retención por rango de edad
bins = [18, 30, 45, 60, 100]  # Rangos: 18-30, 31-45, 46-60, >60
labels = ['18-30', '31-45', '46-60', '>60']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, include_lowest=True)
plt.figure(figsize=(10, 6))
retention_age = df.groupby('AgeGroup', observed=True)['IsActiveMember'].mean() * 100
sns.barplot(x=retention_age.index, y=retention_age.values)
plt.title('Tasa de Retención por Rango de Edad')
plt.xlabel('Rango de Edad')
plt.ylabel('% Usuarios Activos')
plt.savefig(os.path.join(PLOTS_DIR, 'retention_by_age_group.png'), bbox_inches='tight')
plt.close()

# 8. Correlación entre CreditScore y retención
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='CreditScore', y='IsActiveMember', alpha=0.5)
plt.title('Relación entre CreditScore e IsActiveMember')
plt.xlabel('Puntaje Crediticio')
plt.ylabel('Estado de Actividad (0 = Inactivo, 1 = Activo)')
plt.savefig(os.path.join(PLOTS_DIR, 'creditscore_vs_retention.png'), bbox_inches='tight')
plt.close()
correlation = df['CreditScore'].corr(df['IsActiveMember'])
print(f"Correlación entre CreditScore e IsActiveMember: {correlation:.2f}")

# 9. Retención por HasCrCard
plt.figure(figsize=(10, 6))
retention_hascrcard = df.groupby('HasCrCard')['IsActiveMember'].mean() * 100
sns.barplot(x=retention_hascrcard.index, y=retention_hascrcard.values)
plt.title('Tasa de Retención por Posesión de Tarjeta de Crédito')
plt.xlabel('Tiene Tarjeta de Crédito (0 = No, 1 = Sí)')
plt.ylabel('% Usuarios Activos')
plt.savefig(os.path.join(PLOTS_DIR, 'retention_by_hascrcard.png'), bbox_inches='tight')
plt.close()

# 10. Retención por rango de salario
bins_salary = [0, 50000, 100000, 150000, 200000]
labels_salary = ['0-50k', '50k-100k', '100k-150k', '150k-200k']
df['SalaryRange'] = pd.cut(df['EstimatedSalary'], bins=bins_salary, labels=labels_salary, include_lowest=True)
plt.figure(figsize=(10, 6))
retention_salary = df.groupby('SalaryRange', observed=True)['IsActiveMember'].mean() * 100
sns.barplot(x=retention_salary.index, y=retention_salary.values)
plt.title('Tasa de Retención por Rango de Salario Estimado')
plt.xlabel('Rango de Salario ($)')
plt.ylabel('% Usuarios Activos')
plt.savefig(os.path.join(PLOTS_DIR, 'retention_by_salary_range.png'), bbox_inches='tight')
plt.close()

# 11. Heatmap de tasa de abandono (Exited) por Tenure y NumOfProducts
plt.figure(figsize=(12, 8))
churn_heatmap_data = df.pivot_table(values='Exited', index='Tenure', columns='NumOfProducts', aggfunc='mean') * 100
sns.heatmap(churn_heatmap_data, annot=True, fmt='.1f', cmap='Reds')
plt.title('Tasa de Abandono (%) por Tenure y Número de Productos')
plt.xlabel('Número de Productos')
plt.ylabel('Tenure (Años)')
plt.savefig(os.path.join(PLOTS_DIR, 'churn_heatmap.png'), bbox_inches='tight')
plt.close()

# 12. Balance promedio por estado de actividad
plt.figure(figsize=(10, 6))
avg_balance = df.groupby('IsActiveMember')['Balance'].mean()
sns.barplot(x=avg_balance.index, y=avg_balance.values)
plt.title('Balance Promedio por Estado de Actividad')
plt.xlabel('Estado de Actividad (0 = Inactivo, 1 = Activo)')
plt.ylabel('Balance Promedio ($)')
plt.savefig(os.path.join(PLOTS_DIR, 'avg_balance_by_activity.png'), bbox_inches='tight')
plt.close()

# 13. Retención por HasCrCard y Gender
plt.figure(figsize=(10, 6))
retention_hascrcard_gender = df.groupby(['HasCrCard', 'Gender'])['IsActiveMember'].mean() * 100
retention_hascrcard_gender = retention_hascrcard_gender.reset_index()
sns.barplot(x='HasCrCard', y='IsActiveMember', hue='Gender', data=retention_hascrcard_gender)
plt.title('Tasa de Retención por Tarjeta de Crédito y Género')
plt.xlabel('Tiene Tarjeta de Crédito (0 = No, 1 = Sí)')
plt.ylabel('% Usuarios Activos')
plt.savefig(os.path.join(PLOTS_DIR, 'retention_by_hascrcard_gender.png'), bbox_inches='tight')
plt.close()

print(f"Todos los gráficos guardados en: {PLOTS_DIR}")