# Machine Learning Process
​
## Overview
​
RealLeads is a data analytics group that is working for determine trends and solve problems within the real estate market in New Castle County, Delaware. There are three questions that we explored using data analytics: 
1. Can we predict the listing price of a house? 
2. Can we predict the price the house would be sold for? 
3. Can we determine the date range the house will be sold on? 
Using machine learning, we can predict the answer to these questions, which will provide insight for home owners looking to sell their home. 
​
For the machine learning model, we created a structure that has an order to how we answer these questions. We first predict the listing price, then the sold price, followed by the date range. This is because each machine learning builds off of the previous in that there is required information from previous models used in the later models. We first train and predict the listing price. Next, we then use the original list price as well as the same columns as the listed price to determine the sold price. Lastly, we take both the original and sold prices to determine if a house will sell in less than or more than two months using the date range model.
​
## Preprocessing
​
The first step to creating machine learning models is to provide clean and accurate data to the model. If the data is not cleaned or is inacurate, then the machine learning model will perform poorly and provide incorrect information. We begin preprocessing by importing tables from a local database which contains a large quantity of information related to the New Castle County housing market such as listing prices, sold prices, days on market, number of bedrooms, and much more. Once the tables are imported, we begin to merge relevant tables together and drop any unnecessary columns that will not provide value to the machine learning model. Including invaluable columns in the machine learning model can break the model and/or provide very poor results. For example, if we include a column named *MLSNumber* in the machine learning model, it will not provide any insight to help the machine learning model predict prices or day on market. This is because each row contains a different MLSNumber as they are the unique identifiers that similar to an ID. After dropping and cleaning the data, we removed over 60 columns to only include relevant columns in the machine learning models.
​
## Testing Different Machine Learning Models Stage 1 (List Price)
​
Before applying our data to a machine learning model, we first have to split the data into training data and testing data. Eighty percent of the data is being used to train the model, while the remaining twenty percent is used to test the model. Next, we begin testing on multiple models. The below models are aiming to predict the suggested listing price of a house. For the listing price model, we used regression models. 
​
### RandomForestRegressor
​
RandomForestRegressor is the first model we used. This model provided the best score compared to other models. 
​
![RFR_SCORE.PNG](RealLeads%20Machine%20Learning%20Process%20fbae3acb038c462b9556e84aea4891cd/RFR_SCORE.png)
​
This model scored a 76% accuracy with a mean absolute error of 36000. Our goal was to attain a model that was in the range of 75-85% accuracy because this shows that the model is not overfitted to the training data and can handle any new data added into the dataset.
​
### RidgeRegression
​
The next model we tested was RidgeRegression. This was done to determine if we could get a better score than the 76% given by the RandomForestRegressor.
​
![RidgeRegression.PNG](RealLeads%20Machine%20Learning%20Process%20fbae3acb038c462b9556e84aea4891cd/RidgeRegression.png)
​
Unlike the RandomForestRegressor, the Ridge model performed poorly with an accuracy of 54% and a mean absolute error of 54000.
​
### Linear Regression
​
We then tried Linear Regression, which is a standard model that is commonly used to perform a basic prediction but after training it on the model, it performed better than the Ridge model but not as well as the RandomForest model.
​
![LinearRegression.PNG](RealLeads%20Machine%20Learning%20Process%20fbae3acb038c462b9556e84aea4891cd/LinearRegression.png)
​
The Linear Regression model performed with 59% accuracy and a mean absolute error of 50000.
​
### Lasso
​
Lasso is another type of machine learning model that we used to train the model, but it performed similarly to the Linear Regression Model.
​
![Lasso.PNG](RealLeads%20Machine%20Learning%20Process%20fbae3acb038c462b9556e84aea4891cd/Lasso.png)
​
The Lasso model performed with 59% accuracy and a mean absolute error of 50000.
​
### Elastic Net
​
![ElasticNet.PNG](RealLeads%20Machine%20Learning%20Process%20fbae3acb038c462b9556e84aea4891cd/ElasticNet.png)
​
The Elastic Net model performed with 58% accuracy and a mean absolute error of 51866.
​
### Bayesian Ridge
​
![BayesianRidge.PNG](RealLeads%20Machine%20Learning%20Process%20fbae3acb038c462b9556e84aea4891cd/BayesianRidge.png)
​
The Bayesian Ridge model performed with 58% accuracy and a mean absolute error of 50000.
​
## Machine Learning Stage 2 (List Price)
​
With RandomForestRegressor model being the best option, we decided to attempt one more method which is scaling our data using the StandardScaler method. StandardScaler is used to scale data to the point where the all numbers are in close range with each other. For example, house prices can be listed as 300,000 dollars, but the number of bedrooms are 3, which indicates a wide range of numerical values, although the data columns are not the same. Scaling tackles this issue by changing all the numbers to very small numbers to keep the data normalized, which improves machine learning model capabilities.
​
We applied the RandomForestRegressor to the scaled data, and resulted with similar scores as the unscaled model.
​
![rfrscaled.PNG](RealLeads%20Machine%20Learning%20Process%20fbae3acb038c462b9556e84aea4891cd/rfrscaled.png)
​
Though the scaled model performed marginally close to unscaled model, we decided to use this scaled model for the rest of the predictions to maintain consistency.
​
## Machine Learning Stage 3 (Sold Price)
​
The next step in the analysis was to predict the sold price of the house. We added the original list price to our existing data table to help determine the prediction for what price the house would be sold for. The reason we did not use the predicted list price, for this case, is because we wanted the model to use the existing data given to provide the best learning experience. Once the model learned from the exising data, in production, a home owner can then predict their listed price. Based on the list price prediction, we will then be able to predict the expected sold price of the house.
​
### RandomForestRegressor
​
We used the RandomForestRegressor again to predict the sold price  because of how well it performed on the previous prediction. In addition, the RandomForestRegressor has some useful built in functions that help visualize important correlations between the data. After training the model with our scaled data which included the original list price, it performed remarkably well.

![rfr_sold.PNG](RealLeads%20Machine%20Learning%20Process%20fbae3acb038c462b9556e84aea4891cd/rfr_sold.png)
​
The model had an accuracy of 86% and a mean absolute error of 25000.
​
## Machine Learning Stage 4 (Days On Market)
​
The next step in the analysis was to predict the days on market for the house sale. After attempting to find the days on market as a value, the accuracy was too low with the given data, so we decided to bucket days on market data. With trial and error, we found that bucketing into two groups, less than/more than 2 months provided an accurate prediction. We split the data into training data and testing data with an 80/20 split, and began testing on multiple classification models. Balanced Random Forest Classifier after dropping columns was the model that provided the most accuracy.
​
### Balanced Random Forest Classifier
​
The Balanced Random Forest Classifier model performed with 70% accuracy after dropping unncessary columns. Prior to dropping these columns, the accuracy was 63%
​
### Easy Ensemble Classifier
​
The Easy Ensemble Classifier model performed with 44% accuracy, and only 37% accuracy after dropping columns.
​
## Machine Learning Stage 5 (Unsupervised Learning K-Means)
​
This step was optional for the RealLeads team, but we were determined to find any correlation with all data points by clustering using unsupervised learning. We used a different data table than the supervised macine learning models in that  we included majority of columns for the unsupervised model. Once the data was cleaned, we used a method called the Principal Component Analysis (PCA), which performs a dimensionality reduction on our data table and normalizes the data points. The PCA had 3 components that it reduced the data to which then was used to determine the amount of clusters that would be optimal using the elbow curve method. The elbow curved method uses the K-Means model and goes through a range of clusters to find which number cluster is the best for the data. In this case, four clusters was the most optimal. 
​
After analyzing the clusters, it was difficult to indicate if there was any correlation with the data. The clusters were close together, but were separated appropiately. After looking at some visualizations to explain the data, we were unable to determine any strong correlations between the data.
​
## Results
​
Here are some snippets of the results of all the machine learning model stages:
​
![ListPriceImportanvce.PNG](RealLeads%20Machine%20Learning%20Process%20fbae3acb038c462b9556e84aea4891cd/ListPriceImportanvce.png)
​
This shows the what features that had the most significant impact on predicting the list price.
​
![ZipCodeTABLE_PRICE.PNG](RealLeads%20Machine%20Learning%20Process%20fbae3acb038c462b9556e84aea4891cd/ZipCodeTABLE_PRICE.png)
​
This is an overview of the average prices of houses based on zipcode. The table also shows the difference between the original prices of the houses and the predicted prices from the model to show the difference between them.
​
![orig_price_diff_pred_zipcode.png](RealLeads%20Machine%20Learning%20Process%20fbae3acb038c462b9556e84aea4891cd/orig_price_diff_pred_zipcode.png)
​
![sold_price_diff_pred_zipcode.png](RealLeads%20Machine%20Learning%20Process%20fbae3acb038c462b9556e84aea4891cd/sold_price_diff_pred_zipcode.png)
​
![overall_diff_orig_zipcode.png](RealLeads%20Machine%20Learning%20Process%20fbae3acb038c462b9556e84aea4891cd/overall_diff_orig_zipcode.png)
​
The above three graphs show the difference between the original prices and the predicited prices.

![Alt text](seaborn.png)

This visualization shows the correlation between features.

![Alt text](features.png)

This shows the what features that had the most significant impact on predicting the days on market.

​![Alt text](confusion_matrix.png)

This is a correlation matrix which shows that 72% of thw rows that were predicted as "less than 2 months" are actually "less than 2 months" and 67% of the rows that were predicted as "more than 2 months" are actually "more than 2 months".
​
![newplot.png](RealLeads%20Machine%20Learning%20Process%20fbae3acb038c462b9556e84aea4891cd/newplot.png)
​
This cluster graph shows all the datapoints in the data table and the appropiate classes they belong to.
​
![scatterheatmap.png](RealLeads%20Machine%20Learning%20Process%20fbae3acb038c462b9556e84aea4891cd/scatterheatmap.png)
​
This shows the sold price of houses, each PCA component and correlation.

### Final Files:
List Price:
Testing Jupyter Notebook: mlTestSupervised.ipynb
Unscaled Model Jupyter Notebook: Supervised_ML_Testing_Unscaled.ipynb
Scaled Model Jupyter Notebook: Supervised_ML_Tst_Stg2_Scaled.ipynb
Model File: RandomForestRegressor_Scal_model.sav

Sold Price:
Model Jupyter Notebook: SupervisedML_RFR_Stg3
Model File: RFR_Scaled_SoldPrice.sav

Days on Market:
Testing Jupyter Notebook: HowLongToSell_ML_Testing.ipynb
Model Jupyter Notebook: HowLongToSell_ML_BRF.ipynb
Model File: BRF_DOM.sav

Unsupervised: Unsupervised_learning_stg_1.ipynb