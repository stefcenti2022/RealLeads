from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from ..models import SearchData

class SearchForm(FlaskForm):

    # The address field will have a dropdown menu for the user to select
    # from a list of home addresses that the machine language model found
    # in it's predictive algorithm.
    # 
    # The list of addresses will be added to the dropdown after the Form is 
    # created in app.py
    address = SelectField(label='Address', validate_choice=False)

    # Once an address is chosen the following fields will be populated with
    # the rest of the address data and the MLS number for the address selected.
    city = StringField(label='City', render_kw={'readonly': True})
    state = StringField(label='State', render_kw={'readonly': True})
    zipcode = StringField(label='Zip Code', render_kw={'readonly': True})
    mls_number = StringField(label='MLSNumber', render_kw={'readonly': True})

# View Functions: These functions allow the app to access data to be displayed on the Form
def view_listing_price(request, address):
    sd = SearchData(address)
    form = SearchForm(request.GET, obj=sd)

    # Read all home listing data 
    addresses = sd.read_all('Address')
    form.address.choices = addresses