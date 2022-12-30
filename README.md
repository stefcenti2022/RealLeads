# RealLeads

## Overview

The real estate industry has a significant impact on the American economy. There are several indicators that affect real estate sales such as location, property characteristics and the economy including the job market, economic cycle and interest rates etc. These indicators help us the determine current approximate value of the property.

## Goal

Whether you are a buyer, seller, agent or investor, everyone has two big questions:

- How much can I sell my home for?
- How fast can my house be sold?

In this project we will try to find answers for these questions using the data set below from 2019-2022 in New Castle, DE.

## Description of Data Source

We will be using:

- Multi Listing Service Data (MLS)
- Public Record (PD)
- Mortgage Data (MD)
- Census Data (CD)
- APIs

## Architecture

<img src="./static/images/architecture.png" alt="RealLeads Architecture Diagram" width="500"/>

## Software Used

## Machine Learning Model

### Supervised


The first stage of the data preprocessing involves merging multiple tables to create a machine learning ready data table. Each merge tage involves further data cleaning such as column dropping and disposing any rows that have NaN value.

The model that we will be using to predict list and sold price of a house is a random forest regressor model which is a regression model. This model has benefits such as retraining on random states to find the best tree to use and also has built in functions 
that helps find out what features have the strongest weight when determine the target variable.

##### How fast can my house be sold?



## Site Map

<img src="./static/images/site_map.png" alt="Site Map Diagram" width="500"/>

## Home Page Example

