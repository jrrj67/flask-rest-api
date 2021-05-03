from flask import Flask

# Creating app
app = Flask(__name__)

# Importing environment config
app.config.from_object('config.DevelopmentConfig')

# Importing views
from app.views import views

