from flask import Flask

# Creating app
app = Flask(__name__)

# Importing environment config
if app.config['ENV'] == 'production':
    app.config.from_object('config.ProductionConfig')
elif app.config['ENV'] == 'development':
    app.config.from_object('config.DevelopmentConfig')

# Importing views
from app.views import views

