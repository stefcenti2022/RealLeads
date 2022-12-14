from flask import Flask, render_template, request, redirect, url_for
#from flask_pymongo import PyMongo
import census_map

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
#app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
#mongo = PyMongo(app)

# Set Up App Routes
@app.route("/")
def index():
   return render_template("index.html")

@app.route("/home")
def home():
   return render_template("home.html")

@app.route("/about")
def about():
   sites = ['twitter', 'facebook', 'instagram', 'github']
   return render_template("about.html", sites=sites)

@app.route("/get_map")
def census_map():
   # For now, use townnames. These will most likely be zipcodes or some other unique identifier.
   # This data may come from the DB. If so, we will need to connect to the DB like we did
   # in the Mission to Mars app but instead of using Mongo DB we will need to connect to 
   # our Postgresql DB.
   towns = ['Christiana', 'Greenville', 'Hockessin', 'Middletown', 'Newark', 'Wilimington']
   return render_template("census_map.html", towns=towns)

@app.route("/tableau_story/<story_id>")
def tableau_story(story_id):
   return render_template("tableau_story.html", story_id = story_id)

if __name__ == "__main__":
    app.run()