#---------------------------------------------------------------------------
# Name: LatLng.py
#
# Description:
# Python class with methods for Creating, Reading, Updating and Deleting
# LatLng records.
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
# read(self): This method will return all Id objects from the LatLng DF in a JSON list.
#
# read(self, mls_number): Given an mls_number, this method will retrieve the 
# data from the LatLng DF with the coresponding mls_number and return a JSON list
# to be renedered by the appropriate View.
#
#---------

# Import dependencies
import pandas as pd
import json

from flask import Flask, jsonify

#---------------------------------------------------------------------------
# Class Definition for the LatLng Model
#---------------------------------------------------------------------------
class LatLng:
    def __init__(self, path):
        self.name = 'lat_lng_clean'
        self.csvfile = path + self.name + '.csv'
        self.df = pd.read_csv(self.csvfile)

    def read_all(self):
        return json.loads(self.df.to_json(orient='records'))
    
    def read(self, mls_number):
        results = self.df.loc[self.df['MLSNumber'] == mls_number]

        return json.loads(results.to_json(orient='records'))
    
#---------------------------------------------------------------------------
# Functions for accessing Id Table Data
def get_lat_lng_model(mls_number):
    model = LatLng('./Resources/data/')

    return model.read(mls_number)
