# Project 2 - Ames Housing Data and Kaggle Challenge


## Problem Statement
Presently, one of my relatives is gaining interested in a real estate trading business. What she's currently doing is searching for second-hand houses/condominiums that worth renovating for resale. One of the problems she has is the valuation of the property since it is very subjective, and there are plenty of factors affecting its price.
Therefore, **this project aims to study significant factors affecting the property value (which add the most value to a property and which hurt the price most?) and finally build a model that accurately predicts the property price in a timely manner. So we do not miss an opportunity to get undervalued properties and maximize our profit!**

**List of model used in the project:**  
1. Multiple Linear Regression
1. Regularized Linear Regression in multiple variance
 - Ridge Regression
 - Lasso Regression
 - ElasticNet Regression

**Evaluation metrics:**  
For this occasion, **RMSE** (Square root of Mean Squared Error) will be used as an evaluation metrics

**Baseline performance:**  
The performance of our model will be compared against the baseline model that make an average of property price as a prediction in every time.

## About the dataset
The <a href = http://www.amstat.org/publications/jse/v19n3/decock.pdf > Ames Housing dataset </a>  was compiled by Dean De Cock for use in data science education. It's an incredible alternative for data scientists looking for a modernized and expanded version of the often cited Boston Housing dataset.

The dataset contains 2051 observation of 80 features, describing specific characteristics of residential property in Ames, Iowa sold between 2006 - 2010.  Of the 80 features, it can be separated into 4 main categories as follow
- Features of the house --> a string describing main features such as roof material, mansory type, electrical system  
- Area-Size related --> 1st floor and 2nd floor area, lot area, pool area, garage area  
- Location of the house, neighborhood...
- Surrounding Environmental Factor --> alley, landslope

<a href = https://github.com/Joeycooky/DSI_Project_2/blob/main/data_dict.md > See full data dictionary here </a>

## Executive Summary

![Overall](https://github.com/Joeycooky/DSI_Project_2/blob/main/images/coef_overall.png)

Among all models in our study, an ElasticNet regressor with polynomial has the best predictive performance (evaluated by RMSE). However, considering interpretability, the simpler version without polynomial transformation is much easier to interpret and be understood by non-technical user.
Although numerous factors impacted the property value, some of the factors worth mentioning are ...
- Although price tend to increase with the total area of the house, living area is the most expensive part of it.
- From the perspective of property reseller, while overall quality directly means high resell price, we could consider buying an average quality house and focus on renovation to boost its price.
- With a limited budget, focus on kitchen renovation and refurbishing external appearance by repainting.
- If there is no garage, don't waste your time building one. It won't add much value to the house.

for detailed analysis please go to ...
1. <a href = https://github.com/Joeycooky/DSI_Project_2/blob/main/Code/EDA.ipynb > Exploratory Data Analysis </a>
1. <a href = https://github.com/Joeycooky/DSI_Project_2/blob/main/Code/model_polyorder2.ipynb > Model, Prediction and Conclusion </a>
