##
# The goal of this module is to take in an English language query, convert it to a Mongo Query,
# query the database, and return a list of companies
##
from pymongo import MongoClient # pymongo is the mongo client that python uses to connect to mongo db
import re
from textblob import TextBlob
 
# Database connection
client = MongoClient('mongodb://karan.rajpal:karan.rajpal@ds163397.mlab.com:63397/joby') # a mongo db hosting platform called mlab. free place to host mong db
db = client.joby    # Name of the database
companies_collection = db.Companies # Name of the collection
 
def handle_message(message):
    response = 'I don''t know right now'
    return response
 
 
def find_companies_by_location(location):
    location_regex = re.compile(location, re.IGNORECASE)
    companies = companies_collection.find({
        "$or": [
            {'location_region': location_regex},
            {'location_city': location_regex},
            {'location_country_code': location_regex}
        ]
    })
    # Potential improvement - Sort by company size to get better companies
    # Randomly choosing the first 5 companies
    companies = list(companies)
    if len(companies) > 5:
        companies = companies[0:5]
    return companies
 
def format_companies(companies):
    response = 'Here is a list of companies to consider'
    for i, company in enumerate(companies):
            response = response + '\n' +\
            str(i+1) + ') ' + company['name'] + '\n' +\
            'Description: ' + company['short_description'] + '\n' +\
            'Link: ' + company['linkedin_url'] + '\n'
    return response