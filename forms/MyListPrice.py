#------------------
#
# Name: MyListPrice.py
#
# Description:
# This form contains the data to be diplayed in the body of the
# HomeWise base page when the user clicks on "My List Price".
#
#---------------------
from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from ..forms import SearchForm

# Does the SearchForm object have to be created here or is it only
# referenced in the tempate?
# 
# If created here, it would have no data from the search which
# would have been sent to the route when 'Recieve Data' is clicked.
#
# Somehow, the form that needs to be rendered must be known by the
# Search form so it may make sense to have it globally instantiated
# in this module to be accessed by this form, where route_name would
# be 'my_list_price' in this instance. Alternatively, and better
# would be for FlaskForm to take some similar type of argument so tell
# it which form it belongs to:
# 
# search_form = SearchForm(FlaskForm, route_name)
#
# The main content of the this form only contains some text and the 
# original predicted list price from the machine language analysis.
#

#search_form = SearchForm.SearchForm()
#search_form.content_name = 'list_price'

class MyListPrice(FlaskForm):

    name = HiddenField()

    list_price = StringField(label='List Price', render_kw={ 'readonly': True })
