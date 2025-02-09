from flask import Flask, render_template, request, jsonify, Blueprint
from fetch_req import  convert_to_int
from sqlalchemy.exc import OperationalError
from models.model import Season, Episode, Castle, Character, House
import json


def register_routes(app, db):

    res = [""]
    req_string = "https://omarko-got-api/"

    omarko = Blueprint("omarko", __name__)

    '''Route to Home Page'''


    @app.errorhandler(404)
    def page_not_found(error):
        return ('404 NOT FOUND', 404)


    @app.route("/home/", methods=['GET', 'POST'])
    @app.route("/", methods=['GET', 'POST'])
    def home():
        try:
            data = Castle.query.filter_by(castle_id=119).first()
        except OperationalError:
            db.session.rollback()  
            data = Castle.query.filter_by(castle_id=119).first()
    
        castle = json.dumps(data.to_dict(), indent=2)
        return render_template('home.html', html_res=castle)
        

    @app.route("/documentation/", methods=['GET', 'POST'])
    def documentation():
        return render_template('documentation.html')


    @app.route("/about/", methods=['GET', 'POST'])
    def about():
        return render_template('about.html')


    '''Route to api page'''


    @app.route("/api/", methods=['GET', 'POST'])
    def api(data=None, id=None):
        allapi = {
            "castles": "https://omarko-got-api/api/castles/",
            "characters": "https://omarko-got-api/api/characters/",
            "episodes": "https://omarko-got-api/api/episodes/",
            "houses": "https://omarko-got-api/api/houses/",
            "seasons": "https://omarko-got-api/api/seasons/"
        }
        return jsonify(allapi)


    '''Route to api data'''


    @app.route("/castles/", methods=['GET'])
    @app.route("/castles/<id>/", methods=['GET'])
    def castles(id=None):
        if id != None:
            id = convert_to_int(id)
            if id == 0:
                return ('404 NOT FOUND', 404)

            data = Castle.query.filter_by(castle_id=id).first()
            if data is None:
                return ('404 NOT FOUND', 404)
            castle = data.to_dict()
            return jsonify(castle)

        else:
            castles = Castle.query.all()
            counts = Castle.query.count()
            return jsonify({
                'counts': counts, 
                'status': 'successful',
                'results': [castle.to_dict() for castle in castles]
            })


    '''Route to houses data'''


    @app.route("/houses/", methods=['GET'])
    @app.route("/houses/<id>/", methods=['GET'])
    def houses(id=None):
        if id != None:
            id = convert_to_int(id)
            if id == 0:
                return ('404 NOT FOUND', 404)

            data = House.query.filter_by(house_id=id).first()
            if data is None:
                return ('404 NOT FOUND', 404)
            house = data.to_dict()
            return jsonify(house)
        
        else:
            houses = House.query.all()
            counts = House.query.count()
            return jsonify({
                'counts': counts, 
                'status': 'successful',
                'results': [house.to_dict() for house in houses]
            })



    @app.route("/characters/", methods=['GET'])
    @app.route("/characters/<id>/", methods=['GET'])
    def characters(id=None):
        if id != None:
            id = convert_to_int(id)
            if id == 0:
                return ('404 NOT FOUND', 404)

            data = Character.query.filter_by(character_id=id).first()
            if data is None:
                return ('404 NOT FOUND', 404)
            character = data.to_dict()
            return jsonify(character)
        

        else:
            characters = Character.query.all()
            counts = Character.query.count()
            return jsonify({
                'counts': counts, 
                'status': 'successful',
                'results': [character.to_dict() for character in characters]
            })



    @app.route("/episodes/", methods=['GET'])
    @app.route("/episodes/<id>/", methods=['GET'])
    def episodes(id=None):
        if id != None:
            id = convert_to_int(id)
            if id == 0:
                return ('404 NOT FOUND', 404)
            
            data = Episode.query.filter_by(episode_id=id).first()
            if data is None:
                return ('404 NOT FOUND', 404)
            episode = data.to_dict()
            return jsonify(episode)
        
            
        else:
            episodes = Episode.query.all()
            counts = Episode.query.count()
            return jsonify({
                'counts': counts, 
                'status': 'successful',
                'results': [episode.to_dict() for episode in episodes]
            })



    @app.route("/seasons/", methods=['GET'])
    @app.route("/seasons/<id>/", methods=['GET'])
    def seasons(id=None):
        if id != None:
            id = convert_to_int(id)
            if id == 0:
                return ('404 NOT FOUND', 404)

            data = Season.query.filter_by(season_id=id).first()
            if data is None:
                return ('404 NOT FOUND', 404)
            season = data.to_dict()
            return jsonify(season)
        
        else:
            seasons = Season.query.all()
            counts = Season.query.count()
            return jsonify({
                'counts': counts, 
                'status': 'successful',
                'results': [season.to_dict() for season in seasons]
            })


