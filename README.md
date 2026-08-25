
# TradeFlow-GDP

## Overview
This project investigates the economic relationship between Canada's exports to the 
United States and Canada's GDP, with a focus on manufacturing and wholesale trade. 
Using a PESTEL framework alongside advanced econometric modeling, the analysis 
identifies which trade sectors most significantly drive GDP performance and how 
external shocks (tariffs, policy shifts, supply chain disruptions) ripple through 
the economy over time.

## Data
- **Source**: Statistics Canada — Canadian international merchandise trade by industry
- **Period**: Monthly data, 2002–2024
- **Scope**: 26 variables covering imports/exports across agriculture, mining, 
  utilities, manufacturing, and wholesale trade (world & U.S.-specific), merged 
  with monthly GDP data

## Methodology
- Exploratory Data Analysis & STL decomposition
- Multiple Linear Regression (OLS) with robust diagnostics
- Lagged regression models
- ARIMAX / SARIMAX time-series forecasting
- Vector Autoregression (VAR) with Impulse Response Functions
- Granger causality testing
- Model validation: ADF stationarity tests, Shapiro-Wilk, Breusch-Pagan, VIF

## Key Findings
- Manufacturing trade (exports & imports) explains ~95% of GDP variance 
  (Adjusted R² = 0.947)
- Manufacturing exports and imports Granger-cause GDP — they carry real 
  predictive power
- Wholesale trade shows high volatility and weaker, less reliable GDP effects
- Trade impacts on GDP are lagged, supporting the use of forecasting models 
  in policy timing

## Strategic Implications
Findings support targeted industrial policy around manufacturing exports, 
supply chain resilience for wholesale trade, and the integration of predictive 
trade models into macroeconomic and environmental policy planning.

## Tools & Techniques
Python (pandas, statsmodels), OLS regression, ARIMAX/SARIMAX, VAR, Granger 
causality, time-series diagnostics

## Dashboards

Interactive Power BI dashboards were built to visualize trade and GDP trends 
across five key industry sectors.

### All Industries — Trade Fluctuations and GDP Trends
<img width="1100" height="722" alt="Screenshot 2026-08-25 140654" src="https://github.com/user-attachments/assets/05b0047d-59ed-4912-9413-0808b361a66e" />
Overview of total U.S. exports/imports across sectors, with export share by 
industry and a year-over-year comparison of total exports vs. GDP.

### Manufacturing — Trade Flow Shifts and Economic Impact
<img width="1087" height="724" alt="Screenshot 2026-08-25 140728" src="https://github.com/user-attachments/assets/60808211-e9fc-46cd-a3c2-a71677222817" />
Tracks manufacturing exports vs. imports and their tight correlation with GDP 
growth — the sector identified as the strongest GDP driver in the analysis.

### Wholesale Trade — Imports, Exports, and GDP Correlation
<img width="1087" height="721" alt="Screenshot 2026-08-25 140850" src="https://github.com/user-attachments/assets/89d85f35-805f-473f-84b3-c40235c59d9c" />
Shows wholesale trade balance and its volatile relationship with GDP, 
consistent with the study's finding of unpredictable wholesale trade effects.

### Agriculture — Trade Performance and Economic Influence
<img width="1088" height="721" alt="Screenshot 2026-08-25 140919" src="https://github.com/user-attachments/assets/8ae76629-799c-4e4c-a21a-71654df8d6ec" />
Visualizes agriculture, forestry, fishing, and hunting trade balance alongside 
its steady, positive relationship with GDP over time.

### Mining & Oil — Resource Trade and GDP Linkage
<img width="1084" height="715" alt="Screenshot 2026-08-25 140937" src="https://github.com/user-attachments/assets/6ab872a4-6702-475e-bc44-a6779b0a2845" />
Highlights mining, quarrying, and oil & gas extraction trade flows, showing a 
strong export surplus and rising correlation with GDP.

### Utilities Trade — Trade Trends and GDP Impact
<img width="1094" height="723" alt="Screenshot 2026-08-25 141014" src="https://github.com/user-attachments/assets/14aabf9f-8f87-4b2a-98b5-b5d88c8e9297" />
Displays utilities trade balance and its gradual alignment with GDP growth 
across the study period.

