#---------------------------------------------------------------------------
# Name: Sample.py
#
# Description:
# Python class with methods for Creating, Reading, Updating and Deleting
# Sample records provided by the machine learning algorithms.
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
# read(self, mls_number): Given an mls_number, this method will retrieve the 
# instantiate a Sample object which will retrieve it's data using the coresponding 
# mls_number and return a JSON list to be renedered by the appropriate View.
#
#---------

# Import dependencies
import pandas as pd
import json

from flask import Flask, jsonify

#---------------------------------------------------------------------------
# Class Definition for Sample Data Model
#---------------------------------------------------------------------------
class Sample:
    def __init__(self, path):
        self.name = 'ml_samples'
        self.csvfile = path + self.name + '.csv'
        self.df = pd.read_csv(self.csvfile)

    def read_all(self):
        return json.loads(self.df.to_json(orient='records'))
    
    def read(self, mls_number):
        results = self.df.loc[self.df['MLSNumber'] == mls_number]

        return json.loads(results.to_json(orient='records'))
    
#---------------------------------------------------------------------------
# Functions for accessing Sample Data
def get_sample_model(mls_number):
    model = Sample('./Resources/')

    return model.read(mls_number)
