-- ============================================================
-- CUSTOMER CHURN ANALYSIS
-- SQL ANALYSIS
-- ============================================================

-- 1. Total customers
SELECT
    COUNT(*) AS total_customers
FROM telco_churn;


-- 2. Total churned customers
SELECT
    COUNT(*) AS churned_customers
FROM telco_churn
WHERE Churn_Label = 'Yes';


-- 3. Overall churn rate
SELECT
    ROUND(
        SUM(CASE WHEN Churn_Label = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM telco_churn;


-- 4. Churn rate by contract type
SELECT
    Contract,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn_Label = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        SUM(CASE WHEN Churn_Label = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM telco_churn
GROUP BY Contract
ORDER BY churn_rate DESC;


-- 5. Churn rate by internet service
SELECT
    Internet_Service,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn_Label = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        SUM(CASE WHEN Churn_Label = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM telco_churn
GROUP BY Internet_Service
ORDER BY churn_rate DESC;


-- 6. Churn rate by payment method
SELECT
    Payment_Method,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn_Label = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        SUM(CASE WHEN Churn_Label = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM telco_churn
GROUP BY Payment_Method
ORDER BY churn_rate DESC;


-- 7. Average monthly charges by churn status
SELECT
    Churn_Label,
    ROUND(AVG(Monthly_Charges), 2) AS avg_monthly_charges
FROM telco_churn
GROUP BY Churn_Label;


-- 8. Average total charges by churn status
SELECT
    Churn_Label,
    ROUND(AVG(Total_Charges), 2) AS avg_total_charges
FROM telco_churn
GROUP BY Churn_Label;


-- 9. Churn rate by senior citizen status
SELECT
    Senior_Citizen,
    COUNT(*) AS total_customers,
    ROUND(
        SUM(CASE WHEN Churn_Label = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM telco_churn
GROUP BY Senior_Citizen
ORDER BY churn_rate DESC;


-- 10. Churn rate by partner status
SELECT
    Partner,
    COUNT(*) AS total_customers,
    ROUND(
        SUM(CASE WHEN Churn_Label = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM telco_churn
GROUP BY Partner
ORDER BY churn_rate DESC;


-- 11. Churn rate by dependents
SELECT
    Dependents,
    COUNT(*) AS total_customers,
    ROUND(
        SUM(CASE WHEN Churn_Label = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM telco_churn
GROUP BY Dependents
ORDER BY churn_rate DESC;


-- 12. Churn rate by tenure group
SELECT
    CASE
        WHEN Tenure_Months <= 12 THEN '0-12 Months'
        WHEN Tenure_Months <= 24 THEN '13-24 Months'
        WHEN Tenure_Months <= 48 THEN '25-48 Months'
        ELSE '49-72 Months'
    END AS tenure_group,
    COUNT(*) AS total_customers,
    ROUND(
        SUM(CASE WHEN Churn_Label = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM telco_churn
GROUP BY
    CASE
        WHEN Tenure_Months <= 12 THEN '0-12 Months'
        WHEN Tenure_Months <= 24 THEN '13-24 Months'
        WHEN Tenure_Months <= 48 THEN '25-48 Months'
        ELSE '49-72 Months'
    END
ORDER BY churn_rate DESC;


-- 13. Churn by online security
SELECT
    Online_Security,
    COUNT(*) AS total_customers,
    ROUND(
        SUM(CASE WHEN Churn_Label = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM telco_churn
GROUP BY Online_Security
ORDER BY churn_rate DESC;


-- 14. Churn by technical support
SELECT
    Tech_Support,
    COUNT(*) AS total_customers,
    ROUND(
        SUM(CASE WHEN Churn_Label = 'Yes' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM telco_churn
GROUP BY Tech_Support
ORDER BY churn_rate DESC;


-- 15. High-value churned customers
SELECT
    CustomerID,
    Tenure_Months,
    Contract,
    Internet_Service,
    Monthly_Charges,
    Total_Charges,
    CLTV
FROM telco_churn
WHERE Churn_Label = 'Yes'
ORDER BY CLTV DESC
LIMIT 20;