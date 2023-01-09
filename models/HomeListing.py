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

from flask import Flask, jsonify

#---------------------------------------------------------------------------
# Class Definition for Sample Data Model
#---------------------------------------------------------------------------
class HomeListing:
    def __init__(self, address):
        self._name = 'ml_samples'
        self._path = './Resources/'
        self._csvfile = self._path + self._name + '.csv'
        self._df = pd.read_csv(self._csvfile)

        results = self._df.loc[self._df['Address'] == address]
        json_res = json.loads(results.to_json(orient='records'))
        self._data = json_res[0]

        # Set attributes using data from the ml_samples CSV file using setter methods below
        self.address = self._data['Address']
        self.city = self._data['City']
        self.state = self._data['State']
        self.zip_code = self._data['Zip_Code']
        self.county = self._data['County']
        self.mls_number = self._data['MLSNumber']
        self.sold_price = self._data['Sold_Price']
        self.orig_list_price = self._data['Orig_List_Price']
        self.days_on_market = self._data['Days_on_Market']
        self.settle_date = self._data['SettleDate']
        self.neighborhood = self._data['SubdivisionNeighborhood']
        self.school_district = self._data['SchoolDistrict']
        self.acres = self._data['Acres']
        self.ownership = self._data['Ownership']
        self.senior_community = self._data['Senior_Community_YN']
        self.condo_assoc = self._data['Condo/Coop_Assoc_YN']
        self.hoa = self._data['HOA_YN']
        self.association_fee = self._data['AssociationFee']
        self.association_fee_frequency = self._data['AssociationFeeFrequency']
        self.age = self._data['Age']
        self.interior_sq_ft = self._data['InteriorSqFt']
        self.bedrooms = self._data['Bedrooms']
        self.baths = self._data['Baths']
        self.baths_full = self._data['BathsFull']
        self.partial_baths = self._data['PartialBaths']
        self.garage_spaces = self._data['GarageSpaces']
        self.design = self._data['Design']
        self.style = self._data['Style']
        self.garage = self._data['Garage_YN']
        self.flooring = self._data['Flooring']
        self.hot_water = self._data['HotWater']
        self.water = self._data['Water']
        self.sewer = self._data['Sewer']
        self.basement = self._data['Basement_YN']
        self.basement_type = self._data['BasementType']
        self.exterior_material = self._data['ExteriorMaterial']
        self.main_roof = self._data['Main Roof']
        self.central_air = self._data['Central_Air_YN']
        self.cooling = self._data['Cooling']
        self.primary_heat = self._data['PrimaryHeat']
        self.pred_orig_list_price = self._data['Pred_Orig_List_Price']
        self.pred_sold_price = self._data['Pred_Sold_Price']
        self.predicted_dom = self._data['Predicted_DOM']

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

    @property
    def sold_price(self):
        return self._sold_price

    @sold_price.setter
    def sold_price(self, value):
        self._sold_price = value

    @property
    def orig_list_price(self):
        return self._orig_list_price

    @orig_list_price.setter
    def orig_list_price(self, value):
        self._orig_list_price = value
    
    @property
    def days_on_market(self):
        return self._days_on_market

    @days_on_market.setter
    def days_on_market(self, value):
        self._days_on_market = value

    @property
    def settle_date(self):
        return self._settle_date

    @settle_date.setter
    def settle_date(self, value):
        self._settle_date = value

    @property
    def neighborhood(self):
        return self._neighborhood

    @settle_date.setter
    def neighborhood(self, value):
        self._neighborhood = value

    @property
    def school_district(self):
        return self._school_district
    
    @school_district.setter
    def school_district(self, value):
        self._school_district = value

    @property
    def acres(self):
        return self._acres

    @acres.setter
    def acres(self, value):
        self._acres = value

    @property
    def ownership(self):
        return self._ownership    
    
    @ownership.setter
    def ownership(self, value):
        self._ownership = value

    @property
    def senior_community(self):
        return self._senior_community

    @senior_community.setter
    def senior_community(self, value):
        self._senior_community = value

    @property
    def condo_assoc(self):
        return self._condo_assoc

    @condo_assoc.setter
    def condo_assoc(self, value):
        self._condo_assoc = value
   
    @property
    def hoa(self):
        return self._hoa
   
    @hoa.setter
    def hoa(self, value):
        self._hoa = value
    
    @property
    def association_fee(self):
        return self._association_fee
    
    @association_fee.setter
    def association_fee(self, value):
        self._association_fee = value

    @property
    def association_fee_frequency(self):
        return self._association_fee_frequency

    @association_fee_frequency.setter
    def association_fee_frequency(self, value):
        self._association_fee_frequency = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @property
    def interior_sq_ft(self):
        return self._interior_sq_ft

    @interior_sq_ft.setter
    def interior_sq_ft(self, value):
        self._interior_sq_ft = value

    @property
    def bedrooms(self):
        return self._bedrooms

    @bedrooms.setter
    def bedrooms(self, value):
        self._bedrooms = value

    @property
    def baths(self):
        return self._baths

    @baths.setter
    def baths(self, value):
        self._baths = value
    
    @property
    def baths_full(self):
        return self._baths_full
    
    @baths_full.setter
    def baths_full(self, value):
        self._baths_full = value

    @property
    def partial_baths(self):
        return self._partial_baths
    
    @partial_baths.setter
    def partial_baths(self, value):
        self._partial_baths = value
    
    @property
    def garage_spaces(self):
        return self._garage_spaces
    
    @garage_spaces.setter
    def garage_spaces(self, value):
        self._garage_spaces = value

    @property
    def design(self):
        return self._design

    @design.setter
    def design(self, value):
        self._design = value

    @property
    def style(self):
        return self._style
    
    @style.setter
    def style(self, value):
        self._style = value
    
    @property
    def garage(self):
        return True if self._garage == "Y" else False
        
    @garage.setter
    def garage(self, value):
        self._garage = value
    
    @property
    def flooring(self):
        return self._flooring
    
    @flooring.setter
    def flooring(self, value):
        self._flooring = value

    @property
    def hot_water(self):
        return self._hot_water

    @hot_water.setter
    def hot_water(self, value):
        self._hot_water = value

    @property
    def water(self):
        return self._water

    @water.setter
    def water(self, value):
        self._water = value

    @property
    def sewer(self):
        return self._sewer

    @sewer.setter
    def sewer(self, value):
        self._sewer = value

    @property
    def basement(self):
        return self._basement

    @basement.setter
    def basement(self, value):
        self._basement = value

    @property
    def basement_type(self):
        return self._basement_type

    @basement_type.setter
    def basement_type(self, value):
        self._basement_type = value

    @property
    def exterior_material(self):
        return self._exterior_material
  
    @exterior_material.setter
    def exterior_material(self, value):
        self._exterior_material = value
  
    @property
    def main_roof(self):
        return self._main_roof
      
    @main_roof.setter
    def main_roof(self, value):
        self._main_roof = value
    
    @property
    def central_air(self):
        return True if self._central_air == "Y" else False
    
    @central_air.setter
    def central_air(self, value):
        self._central_air = value

    @property
    def cooling(self):
        return self._cooling

    @cooling.setter
    def cooling(self, value):
        self._cooling = value

    @property
    def primary_heat(self):
        return self._primary_heat

    @primary_heat.setter
    def primary_heat(self, value):
        self._primary_heat = value

    @property
    def pred_orig_list_price(self):
        return self._pred_orig_list_price
    
    @pred_orig_list_price.setter
    def pred_orig_list_price(self, value):
        self._pred_orig_list_price = value
    
    @property
    def pred_sold_price(self):
        return self._pred_sold_price
    
    @pred_sold_price.setter
    def pred_sold_price(self, value):
        self._pred_sold_price = value

    @property
    def predicted_dom(self):
        return self._predicted_dom

    @predicted_dom.setter
    def predicted_dom(self, value):
        self._predicted_dom = value

    # CRUD Methods.  For Create, use __init(path_to_csv)
    
    # Read Methods
    def read_all(self):
        return json.loads(self.df.to_json(orient='records'))
    
    def read(self, address):
        results = self.df.loc[self.df['Address'] == address]

        return json.loads(results.to_json(orient='records'))
