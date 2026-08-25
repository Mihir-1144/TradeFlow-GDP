
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

