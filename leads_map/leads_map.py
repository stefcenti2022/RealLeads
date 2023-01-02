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
from flask import render_template
import pandas as pd
import json
import plotly
import plotly.express as px

def get_map():
    us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")

    fig = px.scatter_mapbox(us_cities, lat="lat", lon="lon", hover_name="City", hover_data=["State", "Population"],
                            color_discrete_sequence=["fuchsia"], zoom=3, height=300)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    mapJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header = "Map of North America"
    return mapJSON, header

def get_string():
    test_data = "GET MAP CALLED AND RETURNED THIS STRING"
    return test_data