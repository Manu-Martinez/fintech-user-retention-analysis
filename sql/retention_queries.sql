-- Retención por Tenure
SELECT 
    Tenure AS Años_Desde_Registro,
    COUNT(DISTINCT CustomerId) AS Usuarios,
    COUNT(DISTINCT CASE WHEN IsActiveMember = 1 THEN CustomerId END) AS Usuarios_Activos,
    (COUNT(DISTINCT CASE WHEN IsActiveMember = 1 THEN CustomerId END) * 100.0 / COUNT(DISTINCT CustomerId)) AS Retencion
FROM churn_modelling_cleaned
GROUP BY Tenure;

-- Retención por Tenure
SELECT 
    Tenure,
    ROUND(AVG(CAST(IsActiveMember AS FLOAT)) * 100, 2) AS RetentionRate
FROM bank_customers
GROUP BY Tenure
ORDER BY Tenure;

-- Retención por Gender
SELECT 
    Gender,
    ROUND(AVG(CAST(IsActiveMember AS FLOAT)) * 100, 2) AS RetentionRate
FROM bank_customers
GROUP BY Gender;

-- Tasa de abandono por Tenure y NumOfProducts
SELECT 
    Tenure,
    NumOfProducts,
    ROUND(AVG(CAST(Exited AS FLOAT)) * 100, 2) AS ChurnRate
FROM bank_customers
GROUP BY Tenure, NumOfProducts
ORDER BY Tenure, NumOfProducts;

-- Balance promedio por estado de actividad
SELECT 
    IsActiveMember,
    ROUND(AVG(Balance), 2) AS AvgBalance
FROM bank_customers
GROUP BY IsActiveMember;

-- Retención por HasCrCard y Gender
SELECT 
    HasCrCard,
    Gender,
    ROUND(AVG(CAST(IsActiveMember AS FLOAT)) * 100, 2) AS RetentionRate
FROM bank_customers
GROUP BY HasCrCard, Gender
ORDER BY HasCrCard, Gender;