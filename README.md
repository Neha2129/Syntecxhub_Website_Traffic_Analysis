# Website Traffic Analysis

## 📌 Project Overview

Website Traffic Analysis is a data analytics project developed as part of the **Syntecxhub Data Analysis Internship**.

The project analyzes website traffic data to understand user behavior, traffic sources, engagement, page performance, and conversions. Python and SQL were used for data analysis, while Power BI was used to create an interactive dashboard.

---

## 🎯 Project Objectives

- Analyze website sessions, users, and bounce rate
- Identify major traffic sources
- Evaluate user engagement using session duration and pages per session
- Analyze goal completions and conversion rates
- Identify high-performing and low-performing pages
- Analyze traffic trends over time
- Compare user behavior across devices
- Create an interactive Power BI dashboard for business insights

---

## 🛠️ Tools & Technologies

- **Python**
  - Pandas
  - NumPy
  - Matplotlib
  - Seaborn
- **MySQL**
- **Power BI**
- **CSV**
- **GitHub**

---

## 📊 Dataset

The dataset contains **10,000 website session records**.

### Main Columns

| Column | Description |
|---|---|
| Session_ID | Unique session identifier |
| User_ID | Unique user identifier |
| Date | Session date |
| Traffic_Source | Source through which the user reached the website |
| Page | Website page visited |
| Device | Device used by the visitor |
| Country | Visitor's country |
| New_or_Returning | New or returning visitor |
| Session_Duration_Min | Duration of the session in minutes |
| Pages_Per_Session | Number of pages viewed per session |
| Bounce_Rate | Website bounce rate |
| Goal_Completions | Number of completed goals |
| Conversion_Rate | Conversion rate |

> **Note:** The dataset used in this project is a synthetic dataset created for analytics practice and internship project development.

---

## 🔍 Analysis Performed

### 1. Traffic Source Analysis

Analyzed different traffic sources, including:

- Organic Search
- Paid Search
- Referral
- Direct
- Social Media

Metrics analyzed include sessions, users, bounce rate, session duration, and goal completions.

### 2. User Engagement Analysis

Analyzed:

- Average session duration
- Average pages per session
- Bounce rate
- Device-wise engagement

### 3. Conversion Analysis

Analyzed:

- Goal completions
- Conversion rate
- Goal completions by traffic source
- Goal completion trends over time

### 4. Page Performance Analysis

Compared website pages based on:

- Total sessions
- Bounce rate
- Session duration
- Pages per session
- Goal completions

### 5. Time-Based Analysis

Analyzed daily website traffic and goal-completion trends.

---

## 📈 Power BI Dashboard

The interactive Power BI dashboard includes:

- Total Sessions KPI
- Total Users KPI
- Average Bounce Rate KPI
- Average Session Duration KPI
- Sessions by Traffic Source
- Goal Completions by Traffic Source
- Page Performance
- Daily Sessions Trend
- Average Session Duration by Device
- Average Pages per Session by Traffic Source
- Traffic Source Distribution
- Sessions by Traffic Source and Device
- New vs Returning Users
- Goal Completions Trend

### Interactive Filters

- Date Filter
- Traffic Source Filter
- Device Filter

These filters allow users to explore the website traffic data interactively.

---

## 📁 Project Structure

```text
Syntecxhub_Website_Traffic_Analysis
│
├── Dataset
│   ├── Website_Traffic_Analysis.csv
│   ├── Traffic_Source_Analysis.csv
│   ├── Page_Performance_Analysis.csv
│   ├── Device_Analysis.csv
│   └── Daily_Traffic_Analysis.csv
│
├── Python
│   └── website_traffic_analysis.py
│
├── SQL
│   └── website_traffic_analysis.sql
│
├── PowerBI
│   └── Website_Traffic_Analysis_Dashboard.pbix
│
└── README.md
