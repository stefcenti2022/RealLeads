#---------------------------------------------------------------------------
# Name: HomeListing.py
#
# Description:
# Python class with methods for Creating, Reading, Updating and Deleting
# Sample home listing records provided by the machine learning algorithms.
#
# Note: for demonstration purposes, each model will be using CSV files and
# will only perform Read operations to start.
#
# Methods:
#
# __init__(self, name): given the name of the model, this method will initialize
# the name of the model and its coresponding CSV file name.
#
# open(self): This method will open the CSV file and read the data into a pandas
# DataFrame.
#
# read(self): This method will return all Id objects from the Sample DF in a JSON list.
#
# read(self, mls_number): Given an mls_number, this method will instantiate
# a HomeListing object which will retrieve it's data using the coresponding 
# mls_number and return a JSON list to be renedered by the appropriate View.
#
#---------

# Import dependencies
import pandas as pd
import json
from collections import namedtuple
from json import JSONEncoder

#from flask import Flask, jsonify

#---------------------------------------------------------------------------
# Class Definition for Sample Data Model
#---------------------------------------------------------------------------
class Sample:
    def __init__(self, row):
        print("+++++++++++++++++ ROW ++++++++++++")
        print(row)
        # Set attributes using data from the ml_samples CSV file using setter methods below
        self.address = row['Address']
        self.city = row['City']
        self.state = row['State']
        self.zip_code = row['Zip_Code']
        self.county = row['County']
        self.mls_number = row['MLSNumber']
        self.sold_price = row['Sold_Price']
        self.orig_list_price = row['Orig_List_Price']
        self.days_on_market = row['Days_on_Market']
        self.settle_date = row['SettleDate']
        self.neighborhood = row['SubdivisionNeighborhood']
        self.school_district = row['SchoolDistrict']
        self.acres = row['Acres']
        self.ownership = row['Ownership']
        self.senior_community = row['Senior_Community_YN']
        self.condo_assoc = row['Condo/Coop_Assoc_YN']
        self.hoa = row['HOA_YN']
        self.association_fee = row['AssociationFee']
        self.association_fee_frequency = row['AssociationFeeFrequency']
        self.age = row['Age']
        self.interior_sq_ft = row['InteriorSqFt']
        self.bedrooms = row['Bedrooms']
        self.baths = row['Baths']
        self.baths_full = row['BathsFull']
        self.partial_baths = row['PartialBaths']
        self.garage_spaces = row['GarageSpaces']
        self.design = row['Design']
        self.style = row['Style']
        self.garage = row['Garage_YN']
        self.flooring = row['Flooring']
        self.hot_water = row['HotWater']
        self.water = row['Water']
        self.sewer = row['Sewer']
        self.basement = row['Basement_YN']
        self.basement_type = row['BasementType']
        self.exterior_material = row['ExteriorMaterial']
        self.main_roof = row['Main Roof']
        self.central_air = row['Central_Air_YN']
        self.cooling = row['Cooling']
        self.primary_heat = row['PrimaryHeat']
        self.pred_orig_list_price = row['Pred_Orig_List_Price']
        self.pred_sold_price = row['Pred_Sold_Price']
        self.predicted_dom = row['Predicted_DOM']
    
class SampleTable:
    name = 'ml_samples'
    path = './Resources/'
    csvfile = path + name + '.csv'
    df = pd.read_csv(csvfile)
    cursor = 0
    json_data = json.loads(df.to_json(orient='records'))

    # CRUD Methods.  For Create, use __init(path_to_csv)
    
    # Read Methods

    # Returns the list of records as a json list
    def read_all(self):
        return self.json_data
    
    # Returns the data for a specific field as a list of strings
    def read_all(self, field_name):
        results = self.df[field_name]

        return json.loads(results.to_json(orient='records'))
    
    # Returns one row of the table as a python object
    def read(self, field_name, value):
        results = self.df.loc[self.df[field_name] == value]

        results = json.loads(results.to_json(orient='records'))
        sample = Sample(results[0])
        return sample

    def get_current(self):
        return self.data[self.cursor]

    def get_next(self):
        if self.cursor < len(self.data):
            self.cursor = self.cursor + 1

        return self.data[self.cursor]

    def get_prev(self):
        if self.cursor > 0:
            self.cursor = self.cursor - 1

        return self.data[self.cursor]
