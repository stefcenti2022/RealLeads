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

from flask import Flask, jsonify, request

#---------------------------------------------------------------------------
# Class Definition for Search Data Model
#---------------------------------------------------------------------------
class SearchData:
    def __init__(self, view_name, address=None):
        self._name = 'ml_samples'
        self._path = './Resources/'
        self._csvfile = self._path + self._name + '.csv'
        self._df = pd.read_csv(self._csvfile)
        self._view_name = view_name
        self._button_value = 'Receive Data'
        
        #results = self._df.loc[self._df['MLSNumber'] == 'DENC508522']

        self._results = json.loads(self._df.to_json(orient='records'))
        
        if address is None:
            # This returns the first record in the search list
            print("++++++++++++++++ address is None")
            self._data = self._results[0]
        else: 
            print("++++++++++++++++ address is " + address)
            # next((item for item in dicts if item["name"] == "Pam"), False)
            self._data = next((addr for addr in self._results if addr['Address'] == address), False)

        # Set attributes using data from the ml_samples CSV file using setter methods below
        self.addresses = self._df['Address']
        self.cities = self._df['City']
        self.states = self._df['State']
        self.zip_codes = self._df['Zip_Code']
        self.counties = self._df['County']
        self.mls_numbers = self._df['MLSNumber']

    def show_all(self):
        print('************** SELF *******************')
        print(self)
        print(self.button_value)
        print(self.view_name)
        print(self._data['MLSNumber'])
        print('************** SELF._RESULTS *******************')
        print(self._results)
        print('************** SELF.DATA *******************')
        print(self._data)
        print('************** SELF.ADDRESSES *******************')
        print(self.addresses)

    def search_data(self):
        return self._data
 
    @property
    def view_name(self):
        return self._view_name

    @view_name.setter
    def view_name(self, value):
        self._view_name = value

    @property
    def button_value(self):
        return self._button_value

    @button_value.setter
    def button_value(self, value):
        self._button_value = value

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

    def search_test(self, value):

        print("+++++++++++++++++ value = " + value)

        self.show_all()

    def read_all(self, key):
        return self._data[key]

