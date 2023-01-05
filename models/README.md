# Models

This folder contains models as part of the Model/View/Controller (MVC)framework for accessing the RealLeads DB.

For demonstration purposes, the data will be read only and will be retrieved from CSV files stored in Resources/data.

For each table (i.e. CSV file) there is a python class representing the Model in the MVC framework.

## Files and Folders

- \_\_init\_\_.py: tells the RealLeads app that this is a flask module that can be included in other modules for accessing the database.

- IdTable.py: python class representing the model containing data from the id_table and a function for retrieving the data in JSON format to be rendered on a template.

- model_test.ipynb: This notebook can be used to test python code before using it in the flask code which is harder to debug.

## Future Enhancements

- Create models that retrieve data from the RealLeads SQL DB tables instead of CSV files.
- Add exception handling.
