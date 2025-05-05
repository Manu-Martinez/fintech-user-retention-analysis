# scripts/data_cleaning.py
import pandas as pd
import os

# Definir rutas relativas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
INPUT_FILE = os.path.join(DATA_DIR, 'Churn_Modelling.csv')
OUTPUT_FILE = os.path.join(DATA_DIR, 'Churn_Modelling_Cleaned.csv')

# Verificar que el archivo existe
if not os.path.exists(INPUT_FILE):
    raise FileNotFoundError(f"No se encontró el archivo {INPUT_FILE}. Asegúrate de que esté en la carpeta 'data/'.")

# Cargar dataset
df = pd.read_csv(INPUT_FILE)

# Verificar nulos
print("Valores nulos por columna:")
print(df[['Geography', 'Age', 'HasCrCard', 'IsActiveMember']].isnull().sum())

# Filtrar nulos en Geography y IsActiveMember
df = df[df['Geography'].notnull() & df['IsActiveMember'].notnull()]

# Imputar nulos en Age y HasCrCard
df['Age'] = df['Age'].fillna(df['Age'].median()).astype(int)  # Convertir a entero
df['HasCrCard'] = df['HasCrCard'].fillna(df['HasCrCard'].mode()[0]).astype(int)  # Convertir a entero

# Asegurar tipos numéricos para otras columnas
numeric_columns = {
    'CreditScore': int,
    'Tenure': int,
    'Balance': float,
    'NumOfProducts': int,
    'IsActiveMember': int,
    'EstimatedSalary': float,
    'Exited': int
}

for col, dtype in numeric_columns.items():
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(df[col].median()).astype(dtype)

# Verificar nulos después de limpieza
print("\nValores nulos después de limpieza:")
print(df[['Geography', 'Age', 'HasCrCard', 'IsActiveMember']].isnull().sum())

# Verificar tipos de datos
print("\nTipos de datos:")
print(df.dtypes)

# Guardar dataset limpio en formato compatible con Tableau
df.to_csv(OUTPUT_FILE, encoding='utf-8', float_format='%.2f', index=False )
print(f"Dataset limpio guardado en: {OUTPUT_FILE}")