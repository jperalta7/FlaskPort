# 
# IMPORTS
# 
# you might have to import additional things you need

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
#
# SETUP/CONFIG
#
# change the classname to reflect the name of your table
# change the columns to reflect the columns you need
# each row of your data will be an instance of this class

app = Flask(__name__)

app.config["ENV"] = 'development'
app.config["SECRET_KEY"]=b'_5#y2L"F4Q8z\n\xec]/'

# change the following .db file name
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///WorldCultures-Project-JuanP.db'
# this line is to prevent SQLAlchemy from throwing a warning
# if you don't get one with out it, feel free to remove
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#
# DB SETUP
# 

# this set's up our db connection to our flask application
db = SQLAlchemy(app)

# this is our model (aka table)
class Countries(db.Model):
    __tablename__ = "Countries"
    CountryId = db.Column(db.Integer, primary_key=True) ##how to autoincrment on sqlalchemy
    CountryName = db.Column(db.String(255), nullable=False)
    CountryDescription = db.Column(db.Text, nullable=True)
    #column_3 = db.Column(db.DateTime, nullable=False)
    #column_4 = db.Column(db.Float, nullable=False)
    #column_5 = db.Column(db.Boolean, nullable=False)

class WorldCultures(db.Model):
    __tablename__ = "World Cultures"
    CountryGroupId = db.Column(db.Integer, primary_key=True)
    CultureCountryGroup = db.Column(db.String(255), nullable=False)
    CountryGroupURL = db.Column(db.String(255), nullable=False)
    #column_3 = db.Column(db.DateTime, nullable=False)
    #column_4 = db.Column(db.Float, nullable=False)
    #column_5 = db.Column(db.Boolean, nullable=False)

class CultureOfCountries(db.Model):
    __tablename__ = "Culture of Countries"
    CountryCultureID = db.Column(db.Integer, primary_key=True)
    CountryID = db.Column(db.Integer, nullable=True)
    CountryGroupURL = db.Column(db.String(255), nullable=True)
    CultureCountryName = db.Column(db.String(150), nullable = True)
    CultureCountryName = db.Column(db.String(150), nullable = True)                    
    FoodInDailyLife = db.Column(db.String (255), nullable = True)
    FoodCustomsAtCeremonialOccasions = db.Column(db.String (255), nullable = True)
    BasicEconomy = db.Column(db.String(255), nullable = True)
    LandTenureAndProperty = db.Column(db.String(255), nullable = True)
    CommercialActivities = db.Column(db.String(255), nullable = True)
    MajorIndustries = db.Column(db.String(255), nullable = True)
    Trade = db.Column(db.String(255), nullable = True)
    DivsionOfLabor = db.Column(db.String(255), nullable = True)
    #column_3 = db.Column(db.DateTime, nullable=False)
    #column_4 = db.Column(db.Float, nullable=False)
    #column_5 = db.Column(db.Boolean, nullable=False)
    
#
# VIEWS 
#

# set up your index view to show your "home" page
# it should include:
# links to any pages you have
# information about your data
# information about how to access your data
# you can choose to output data on this page
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# include other views that return html here:
@app.route('/other')
def other():
    return render_template('other.html')

# set up the following views to allow users to make
# GET requests to get your data in json
# POST requests to store/update some data
# DELETE requests to delete some data

# change this to return your data
@app.route('/api', methods=['GET'])
def get_data():
    table = DBTable.query.all()
    d = {row.column_1:row.column_2 for row in table}
    return jsonify(d)

# change this to allow users to add/update data
@app.route('/api', methods=['POST'])
def add_data():
    for k,v in request.args.items():
        pass
    return jsonify({})
        
# change this to allow the deletion of data
@app.route('/api', methods=['DELETE'])
def delete_data():
    for k,v in request.args.items():
        pass
    return jsonify({})

#
# CODE TO BE EXECUTED WHEN RAN AS SCRIPT
#

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
