from flask import Flask, render_template, redirect, url_for
#from flask_pymongo import PyMongo
import get_map

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
#app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
#mongo = PyMongo(app)

# Set Up App Routes
@app.route("/")
def index():
   return render_template("index.html")

@app.route("/get_map")
def get_map():
   # mars = mongo.db.mars
    #mars_data = scraping.scrape_all()
    #mars.update_one({}, {"$set":mars_data}, upsert=True)
    return redirect('/', code=302)

if __name__ == "__main__":
    app.run()