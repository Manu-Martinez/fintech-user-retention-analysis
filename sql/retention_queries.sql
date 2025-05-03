SELECT 
    Tenure AS Años_Desde_Registro,
    COUNT(DISTINCT CustomerId) AS Usuarios,
    COUNT(DISTINCT CASE WHEN IsActiveMember = 1 THEN CustomerId END) AS Usuarios_Activos,
    (COUNT(DISTINCT CASE WHEN IsActiveMember = 1 THEN CustomerId END) * 100.0 / COUNT(DISTINCT CustomerId)) AS Retencion
FROM churn_modelling_cleaned
GROUP BY Tenure;