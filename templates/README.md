# Templates

## Name: templates

## Purpose

The purpose of this folder is to hold all html templates to be used by our Flask application.

## Files

- extends_test.html: This template demonstrates how the 'extends' functionality of flask works by extending the main or index html file. In our case, home.html is the main index file containing the header body and footer of our application where the header and footer will be consistent and the body will be used to render the various views for our app.

- footer.html: This template contains code for the footer of each page.

- home.html: This is the main page of our app. The header and footer are renderend here once and the body will be used to render a new template when a specific route that is traversed.

- list_test.html: Use this template as an example for rendering lists of data in the body of the main page.

- mapbox_test_eq: This template is in development to be used to test rendering of the map created for the mapping earthquake challenge. Once this code can be rendered correctly, it can be used as a basis for our leads_map function to show possible leads.

- mapbox_test.html: This is a working example of a map created in the leads_map module. It will render a map of North America with state capitals and info that the user can over over to see for comparison. It uses Plotly and javascript in a script tag to render the map.

- script_test.html: This uses the leads_map module to render a string in the body of the home page. It originally was to be used for testing rendering of a map but that functionality has been moved to the mapbox testing templates.

- tableau_test.html: This template is an example of how a tableau story can be embeded into our home page.
