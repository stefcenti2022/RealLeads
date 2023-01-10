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
#from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
#from flask_pymongo import PyMongo
from .leads_map import leads_map

from .models import SearchData as sd
from .models import SampleTable, HomeListing

from .forms import SearchForm as sf
from .forms import MyListPrice as lp

import os

csrf = CSRFProtect()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

csrf.init_app(app)

samples = SampleTable.SampleTable()

# Use flask_pymongo to set up mongo connection
#app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
#mongo = PyMongo(app)

# Set Up App Routes
@app.route("/")
def home():
   return render_template("home.html")

#----------------------------------------------------------------------
#  This is the base search form that will be included on all forms that
# require a search before rendering data
#----------------------------------------------------------------------
@app.route("/search", methods=['POST'])
def search():
   search_form = sf.SearchForm()

   # hard code for now. Still need a way to get the name of the
   # template to render as content.
   # This does not work at all and ends up in a recursive loop:
   #   name = search_form.content_name

   template = 'list_price' + '.html'

   # Add code for special processing here
   # if name == 'your_home':
   #    pass
   # elif name == 'list_price':
   #    content_form = lp.MyListPrice()
   # elif name == 'expected_price':
   #    pass
   # elif name == 'expected_dom':
   #    pass

   # # Add code for general processing here
   # if search_form.validate_on_submit():
   #    pass

   address = request.form.get('address')

   args=request.args
   if address:
      #data = sd.SearchData('search_test', address=args.get('address'))
      data = samples.read('Address', address)
      #form.address = data.address
      search_form.city = data.city
      search_form.state = data.state
      search_form.zipcode = data.zip_code
      search_form.mls_number = data.mls_number

   data = samples.read_all('Address')
   print('+++++++++++++ DATA +++++++++++=')
   print(data)
   search_form.address.choices = data

   ###return render_template(template, search_form=search_form, content_form=content_form )
   return redirect('/search_form.html', search_form=search_form, content_form=template)

#----------------------------------------------------------------------------
# **** CONTROL PANEL ROUTES ****
#
# These routes will be used by the control panel to render the corresponding
# template for the button clicked.
#----------------------------------------------------------------------
@app.route("/YourHome")
def YourHome():
   # This route tests calling a method in a python module to retrive data
   # to be embeded/rendered.
   return render_template("YourHome.html")

@app.route("/MyListPrice/<address>")
def MyListPrice(address):
   # This route creates a Sample record from the ml_samples data for a give mls_number
   # The predicted original list price is sent to the my_list_price view to populate
   # the List Price field.
   sample = HomeListing.HomeListing(address)
   return render_template("MyListPrice.html", sample=sample)

# New route for rendering the list price portion in the body below the new search
# form. This will also test having both WTF Forms on the same page.
@app.route("/list_price")
def list_price():
   # Render code for search form and for My List Price here.
   search_form = sf.SearchForm()
   content_form = lp.MyListPrice(name='list_price')

   if content_form.validate_on_submit():
      pass

   address = request.form.get('address')

   args=request.args
   if address:
      #data = sd.SearchData('search_test', address=args.get('address'))
      data = samples.read('Address', address)
      #form.address = data.address
      search_form.city = data.city
      search_form.state = data.state
      search_form.zipcode = data.zip_code
      search_form.mls_number = data.mls_number

   data = samples.read_all('Address')
   print('+++++++++++++ DATA +++++++++++')
   print(data)
   search_form.address.choices = data

   return render_template("list_price.html", search_form=search_form, content_form=content_form)

@app.route("/ExpectedPrice")
def ExpectedPrice():
   # This route tests calling a method in a python module to retrive data
   # to be embeded/rendered.
   return render_template("ExpectedPrice.html")

@app.route("/DaysOnMarket")
def DaysOnMarket():
   # This route tests calling a method in a python module to retrive data
   # to be embeded/rendered.
   return render_template("DaysOnMarket.html")

@app.route("/MyAgent")
def MyAgent():
   # This route tests calling a method in a python module to retrive data
   # to be embeded/rendered.
   return render_template("MyAgent.html")

@app.route("/more_info/<mls_number>")
def more_info(mls_number):
   # This route tests calling javascript scripts to retrive render
   # a map using the mapbox API.
   map, header = leads_map.get_map(mls_number)
   return render_template("more_info.html", map = map, header = header)

#-------------------------------------------
# **** SEARCH FORM ROUTES ****
#
# The following routes are used for searching based on selections
# made on the Search form rendered at the top of several of the 
# templates.
#---------------------------------------------
@app.route("/search_test/")
#@app.route("/search_test/?<search_str>")
def search_test(search_str=None):
   # This route is used for testing out ideas before changing other routes
   # that are currently working.  Once the app is tested and ready for demonstration
   # the button to access this route will be commented out of the base.html page.
   args=request.args
   if args:
      search = sd.SearchData('search_test', mls_number=args.get('mls_number'))
      search.search_test('1')
   else:
      search = sd.SearchData('search_test')
      search.search_test('2')
   return render_template("search_test.html", search=search)
   #id_table_data = IdTable.get_id_table_model(mls_number)
   #return render_template("db_test.html", id_table_data=id_table_data)

@app.route("/search1/", methods=['GET', 'POST'])
def search1():
   form = sf.SearchForm(request.form)

   address = request.form.get('address')

   args=request.args
   if address:
      #data = sd.SearchData('search_test', address=args.get('address'))
      data = samples.read('Address', address)
      #form.address = data.address
      form.city = data.city
      form.state = data.state
      form.zipcode = data.zip_code
      form.mls_number = data.mls_number

   data = samples.read_all('Address')
   print('+++++++++++++ DATA +++++++++++=')
   print(data)
   form.address.choices = data

   return render_template('search_form.html', form=form)

#-------------------------------------------
# **** OLD FORM ROUTES ****
#
# The following routes are used for proof of concept testing and will
# be removed after refactoring.
#---------------------------------------------
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


if __name__ == "__main__":
   app.run()