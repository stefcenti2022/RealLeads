#---------------------------------------------------------------------------
# Name: app.py
#
# Description:
# Main application for the RealLeads app using Flask routes.
#
# Note: 
# The RealLeads application framework is based on the application 
# framework developed in this tutorial:
#
# https://flask.palletsprojects.com/en/2.2.x/tutorial/
#
#-------------

from flask import Flask, render_template, render_template_string, request, redirect, url_for
#from flask_pymongo import PyMongo
from .leads_map import leads_map
from .models import IdTable
import json

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
#app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
#mongo = PyMongo(app)

# Set Up App Routes
@app.route("/")
def home():
   return render_template("home.html")

@app.route("/extends_test")
def extends_test():
   return render_template("extends_test.html")

@app.route("/list_test")
def list_test():
   # This route tests sending a list to an app to be rendered in the body
   # of our app.  For now, the list is hard coded but could come from the DB
   # like we did in the Mission to Mars app but instead of using Mongo DB we 
   # will need to connect to our Postgresql DB.
   towns = ['Christiana', 'Greenville', 'Hockessin', 'Middletown', 'Newark', 'Wilimington']
   return render_template("list_test.html", towns=towns)

@app.route("/tableau_test/<story_id>")
def tableau_test(story_id):
   # This route tests embedding a tableau story into the body of our app.
   return render_template("tableau_test.html", story_id = story_id)

@app.route("/script_test")
def script_test():
   # This route tests calling a method in a python module to retrive data
   # to be embeded/rendered.
   map = leads_map.get_string()
   return render_template("script_test.html", map = map)

@app.route("/mapbox_test")
def mapbox_test():
   # This route tests calling javascript scripts to retrive render
   # a map using the mapbox API.
   map, header = leads_map.get_map()
   return render_template("mapbox_test.html", map = map, header = header)

@app.route("/mapbox_test_eq")
def mapbox_test_eq():
   # This route tests calling javascript scripts to retrive render
   # the earthquake map from challenge_logic.js.
   return render_template("mapbox_test_eq.html")


@app.route("/example")
def example():
   # This route tests calling a method in a python module to retrive data
   # to be embeded/rendered.
   return render_template("example.html")

@app.route("/YourHome")
def YourHome():
   # This route tests calling a method in a python module to retrive data
   # to be embeded/rendered.
   return render_template("YourHome.html")

@app.route("/MyListPrice")
def MyListPrice():
   # This route tests calling a method in a python module to retrive data
   # to be embeded/rendered.
   return render_template("MyListPrice.html")

@app.route("/ExpectedPrice")
def ExpectedPrice():

   # This route tests calling a method in a python module to retrive data
   # to be embeded/rendered.
   return render_template("ExpectedPrice.html")

# This route opens the DaysOnMarket page.
@app.route("/DaysOnMarket")
def DaysOnMarket():
   return render_template("DaysOnMarket.html")

# This route opens the MyAgent page.
@app.route("/MyAgent")
def MyAgent():
   return render_template("MyAgent.html")

# This route retrieves data from the machine language algorithms to
# display the map for a given MLS Number.
@app.route("/FindMap/<mls_number>")
def FindMap(mls_number):
   map, header = leads_map.get_map(mls_number)
   return render_template("FindMap.html", map = map, header = header)

# This route tests retrieving a record from the datbase using search
# criteria selected from a dropdown menu on the search form.
@app.route("/db_test/<mls_number>")
def db_test(mls_number):
   id_table_data = IdTable.get_id_table_model(mls_number)
   return render_template("db_test.html", id_table_data=id_table_data)

@app.route("/more_info/<mls_number>")
def more_info(mls_number):
   # This route tests calling javascript scripts to retrive render
   # a map using the mapbox API.
   map, header = leads_map.get_map(mls_number)
   return render_template("mapbox_test.html", map = map, header = header)

    
if __name__ == "__main__":
   app.run()