CREATE DATABASE website_traffic_analysis;

USE website_traffic_analysis;
USE website_traffic_analysis;

CREATE TABLE website_traffic (
    Session_ID VARCHAR(20),
    User_ID VARCHAR(20),
    Date DATE,
    Traffic_Source VARCHAR(50),
    Page VARCHAR(100),
    Device VARCHAR(20),
    Country VARCHAR(50),
    New_or_Returning VARCHAR(20),
    Session_Duration_Min DECIMAL(8,2),
    Pages_Per_Session DECIMAL(8,2),
    Bounce_Rate DECIMAL(8,2),
    Goal_Completions INT,
    Conversion_Rate DECIMAL(8,2)
);
Select count(*) AS Total_records
From website_traffic;

SELECT*
from website_traffic
LIMIT 10;

SELECT 
    Traffic_Source,
    COUNT(DISTINCT Session_ID) AS Total_Sessions,
    COUNT(DISTINCT User_ID) AS Total_Users,
    ROUND(AVG(Bounce_Rate), 2) AS Average_Bounce_Rate,
    ROUND(AVG(Session_Duration_Min), 2) AS Average_Session_Duration,
    SUM(Goal_Completions) AS Total_Goal_Completions
FROM website_traffic
GROUP BY Traffic_Source
ORDER BY Total_Sessions DESC;

SELECT 
    Page,
    COUNT(DISTINCT Session_ID) AS Total_Sessions,
    ROUND(AVG(Bounce_Rate), 2) AS Average_Bounce_Rate,
    ROUND(AVG(Session_Duration_Min), 2) AS Average_Session_Duration,
    ROUND(AVG(Pages_Per_Session), 2) AS Average_Pages_Per_Session,
    SUM(Goal_Completions) AS Total_Goal_Completions
FROM website_traffic
GROUP BY Page
ORDER BY Total_Sessions DESC;


SELECT
    COUNT(DISTINCT Session_ID) AS Total_Sessions,
    SUM(Goal_Completions) AS Total_Goal_Completions,
    ROUND(
        SUM(Goal_Completions) * 100.0 /
        COUNT(DISTINCT Session_ID),
        2
    ) AS Conversion_Rate_Percentage
FROM website_traffic;

SELECT
    Date,
    COUNT(DISTINCT Session_ID) AS Total_Sessions,
    COUNT(DISTINCT User_ID) AS Total_Users,
    SUM(Goal_Completions) AS Goal_Completions
FROM website_traffic
GROUP BY Date
ORDER BY Date;