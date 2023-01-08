#---------------------------------------------------------------------------
# Name: SearchData.py
#
# Description:
# Python class with data that can be used to search for available listings in
# the RealLeads DB.
#
# Note: for demonstration purposes, each model will be using CSV files and
# will only perform Read operations to start.
#
# Methods:
#
# __init__(self, name): given the name of the model, this method will initialize
# the name of the model and its coresponding CSV file name. This method will
# initially contain address info for MLSNumber = 'DENC508522'.
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
# Class Definition for Search Data Model
#---------------------------------------------------------------------------
class SearchData:
    def __init__(self):
        self._name = 'ml_samples'
        self._path = './Resources/'
        self._csvfile = self._path + self._name + '.csv'
        self._df = pd.read_csv(self._csvfile)

        results = self._df.loc[self._df['MLSNumber'] == 'DENC508522']
        
        self._results = json.loads(results.to_json(orient='records'))
        self._data = self._results[0]

        # Set attributes using data from the ml_samples CSV file using setter methods below
        self.address = self._data['Address']
        self.city = self._data['City']
        self.state = self._data['State']
        self.zip_code = self._data['Zip_Code']
        self.county = self._data['County']
        self.mls_number = self._data['MLSNumber']

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, value):
        self._zip_code = value

    @property
    def county(self):
        return self._county

    @county.setter
    def county(self, value):
        self._county = value
    
    @property
    def mls_number(self):
        return self._mls_number

    @mls_number.setter
    def mls_number(self, value):
        self._mls_number = value