from flask import Flask

# Importing environment config
from app.config import config

# Creating app
app = Flask(__name__)

# Importing views
from app.views import views

