import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("../Dataset/Website_Traffic_Analysis.csv")

print("Dataset loaded successfully!")
print("Shape:", df.shape)

# -----------------------------
# 1. Basic Data Inspection
# -----------------------------

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:", df.duplicated().sum())

# -----------------------------
# 2. Data Preprocessing
# -----------------------------

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Remove duplicate records
df = df.drop_duplicates()

# Fill missing numeric values with median
numeric_columns = df.select_dtypes(include=np.number).columns

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

# Fill missing categorical values with mode
categorical_columns = df.select_dtypes(include="object").columns

for column in categorical_columns:
    if df[column].isnull().any():
        df[column] = df[column].fillna(df[column].mode()[0])

print("\nPreprocessing completed.")

# -----------------------------
# 3. Overall Website Analysis
# -----------------------------

total_sessions = df["Session_ID"].nunique()
total_users = df["User_ID"].nunique()
average_bounce_rate = df["Bounce_Rate"].mean()
average_session_duration = df["Session_Duration_Min"].mean()
average_pages_per_session = df["Pages_Per_Session"].mean()
total_goal_completions = df["Goal_Completions"].sum()

print("\n----- Overall Website Metrics -----")
print("Total Sessions:", total_sessions)
print("Total Users:", total_users)
print("Average Bounce Rate:", round(average_bounce_rate, 2), "%")
print("Average Session Duration:",
      round(average_session_duration, 2), "minutes")
print("Average Pages per Session:",
      round(average_pages_per_session, 2))
print("Total Goal Completions:", total_goal_completions)

# -----------------------------
# 4. Traffic Source Analysis
# -----------------------------

traffic_source = df.groupby("Traffic_Source").agg(
    Sessions=("Session_ID", "nunique"),
    Users=("User_ID", "nunique"),
    Average_Bounce_Rate=("Bounce_Rate", "mean"),
    Average_Session_Duration=("Session_Duration_Min", "mean"),
    Goal_Completions=("Goal_Completions", "sum")
).reset_index()

print("\n----- Traffic Source Analysis -----")
print(traffic_source.round(2))

# -----------------------------
# 5. Page Performance Analysis
# -----------------------------

page_analysis = df.groupby("Page").agg(
    Sessions=("Session_ID", "nunique"),
    Average_Bounce_Rate=("Bounce_Rate", "mean"),
    Average_Session_Duration=("Session_Duration_Min", "mean"),
    Average_Pages_Per_Session=("Pages_Per_Session", "mean"),
    Goal_Completions=("Goal_Completions", "sum")
).reset_index()

print("\n----- Page Performance -----")
print(page_analysis.round(2))

# -----------------------------
# 6. Device Analysis
# -----------------------------

device_analysis = df.groupby("Device").agg(
    Sessions=("Session_ID", "nunique"),
    Average_Bounce_Rate=("Bounce_Rate", "mean"),
    Average_Session_Duration=("Session_Duration_Min", "mean"),
    Goal_Completions=("Goal_Completions", "sum")
).reset_index()

print("\n----- Device Analysis -----")
print(device_analysis.round(2))

# -----------------------------
# 7. Daily Traffic Trend
# -----------------------------

daily_traffic = df.groupby("Date").agg(
    Sessions=("Session_ID", "nunique"),
    Users=("User_ID", "nunique"),
    Goal_Completions=("Goal_Completions", "sum")
).reset_index()

print("\n----- Daily Traffic Trend -----")
print(daily_traffic.head())

# -----------------------------
# 8. Conversion Analysis
# -----------------------------

total_sessions = df["Session_ID"].nunique()

conversion_rate = (
    total_goal_completions / total_sessions
) * 100

print("\n----- Conversion Analysis -----")
print("Conversion Rate:", round(conversion_rate, 2), "%")

# -----------------------------
# 9. Save Analysis Results
# -----------------------------

traffic_source.to_csv(
    "../Dataset/Traffic_Source_Analysis.csv",
    index=False
)

page_analysis.to_csv(
    "../Dataset/Page_Performance_Analysis.csv",
    index=False
)

device_analysis.to_csv(
    "../Dataset/Device_Analysis.csv",
    index=False
)

daily_traffic.to_csv(
    "../Dataset/Daily_Traffic_Analysis.csv",
    index=False
)

# -----------------------------
# 10. Create Charts
# -----------------------------

import os

os.makedirs("../Report/Charts", exist_ok=True)

# Traffic Source Chart
plt.figure(figsize=(9, 5))
sns.barplot(
    data=traffic_source,
    x="Traffic_Source",
    y="Sessions"
)
plt.title("Sessions by Traffic Source")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("../Report/Charts/traffic_source_sessions.png")
plt.close()

# Page Performance Chart
plt.figure(figsize=(10, 5))
sns.barplot(
    data=page_analysis.sort_values(
        "Sessions", ascending=False
    ),
    x="Page",
    y="Sessions"
)
plt.title("Sessions by Website Page")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../Report/Charts/page_sessions.png")
plt.close()

# Bounce Rate by Traffic Source
plt.figure(figsize=(9, 5))
sns.barplot(
    data=traffic_source,
    x="Traffic_Source",
    y="Average_Bounce_Rate"
)
plt.title("Average Bounce Rate by Traffic Source")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("../Report/Charts/bounce_rate_by_source.png")
plt.close()

# Daily Traffic Trend
plt.figure(figsize=(12, 5))
plt.plot(
    daily_traffic["Date"],
    daily_traffic["Sessions"]
)
plt.title("Daily Website Sessions Trend")
plt.xlabel("Date")
plt.ylabel("Sessions")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../Report/Charts/daily_sessions_trend.png")
plt.close()

# Conversion by Traffic Source
plt.figure(figsize=(9, 5))
sns.barplot(
    data=traffic_source,
    x="Traffic_Source",
    y="Goal_Completions"
)
plt.title("Goal Completions by Traffic Source")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("../Report/Charts/conversions_by_source.png")
plt.close()

print("\nCharts created successfully!")
print("Analysis completed successfully!")