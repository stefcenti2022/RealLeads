#-----------------------------------------------------------------
# Name: leads_map.py
# 
# Description:
# This module has methods creating maps and returning the map as a
# JSON object that can be rendered by a Flask template.
#
# Method: get_map()
# Input: none
# Returns: 
#   mapJSON: an example map of North America
#   header: an optional header to be displayed with the map
# 
# For more information on how to create the figure below see this
# document that uses Mapbox Map Layers in Python:
#
# https://plotly.com/python/mapbox-layers/
#
# NOTE: to use a map style other than open-street-map an access token
# must be located in a local file named config.py. This file is
# not part of the package so it will need to be created during setup
# of the RealLeads application.
# 
from flask import render_template
import pandas as pd
import json
import plotly
import plotly.express as px

from ..models import LatLng
from .config import mapbox_token

px.set_mapbox_access_token(mapbox_token)

def get_map():
    us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")

    fig = px.scatter_mapbox(us_cities, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Population"],
                            color_discrete_sequence=["fuchsia"], zoom=3, height=300)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    mapJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header = "Map of North America"
    return mapJSON, header

# Given an MLS Number, this method will find the lat/lng data from the lat_lng_clean.csv file
# and display a map with a marker to that location on a map. 
def get_map(mls_number):
    lat_lng = LatLng.get_lat_lng_model(mls_number)

    fig = px.scatter_mapbox(lat_lng, lat="lat", lon="lng",
                            color_discrete_sequence=["blue"], 
                            zoom=18)

    #fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(mapbox_style="mapbox://styles/mapbox/satellite-streets-v12")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.update_traces(hovertemplate=f"MLS Number: {lat_lng[0]['MLSNumber']}<br>Address: {lat_lng[0]['address_new']}")

    mapJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header = "Map for MLS Number: " + mls_number
    return mapJSON, header

def get_string():
    test_data = "GET MAP CALLED AND RETURNED THIS STRING"
    return test_data