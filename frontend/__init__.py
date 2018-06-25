# Get flask
from flask import Flask

# Create the app
app = Flask(__name__)
app.debug=True

# from frontend.models.sqlclient import SqlClient
# my_sqlclient = SqlClient()

import frontend.views

