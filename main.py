import requests
import random
from flask import Flask, render_template, jsonify, request
from functions import *
import re

app = Flask(__name__, template_folder='templates', static_folder='static')
AllOrigen = GetAllOrigen()
AllCharacters = GetAllCharacters()

@app.route('/')
def main_page_view():
    return render_template('home.html', all_origen=AllOrigen, all_characters_select=AllCharacters)

@app.route('/search/all')
def show_all_date_information():
    characters_information = GetAllCharacters()
    locations_information = GetAllLocations()

    return render_template('results_search_all.html', all_origen=AllOrigen, all_characters_select=AllCharacters, all_characters=characters_information, all_locations=locations_information)

@app.route('/search/q=<character_name>')
def show_characters_information_name_query(character_name):
    characters_information = LookForSomeCharacters_from_Querry(character_name)
    print(characters_information)
    return render_template('character_search.html', all_origen=AllOrigen, all_characters_select=AllCharacters, all_characters=characters_information)

@app.route('/character/<int:character_id>')
def show_character_location(character_id):
    Info_Character_Information = GetCharacterInformation(character_id)
    return render_template('results_character.html', all_origen=AllOrigen, all_characters_select=AllCharacters, info_character=Info_Character_Information)

@app.route('/location/<int:location_id>')
def show_location_status(location_id):
    Info_Location_Information = GetOneLocationInfo(location_id)
    return render_template('results_origen.html', all_origen=AllOrigen, all_characters_select=AllCharacters, info_location=Info_Location_Information)

if __name__ == '__main__':
    app.run(debug=False)