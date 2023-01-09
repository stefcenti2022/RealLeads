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
from wtforms import StringField

class MyListPrice(FlaskForm):
    list_price = StringField('List Price', render_kw={ 'readonly': True })

    @property
    def list_price(self):
        return self.list_price

    @list_price.setter
    def list_price(self, value):
        self.list_price = value