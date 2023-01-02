# Module: leads_map

## Description:

This module contains python methods for rendering maps and testing the use of modules for structuring our Flask application.

## Files:

- `__init__.py`: this tells flask that this folder is a module and makes code in this folder available to be imported by other python files in this app.

- `leads_map.py`: contains the methods that other files can use to render different graphs and maps.

## Leads Map Methods:

- get_map()

  - Input: None
  - Returns: map_na, header where map_na is a map of North America to be rendered by the leads_map template and header is an optional header to go with the map.

- get_string()

  - Input: None
  - Returns: string, where is a misc string for testing a flask route by calling a function located in a python module designed for our app.
