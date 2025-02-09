from flask import Flask, render_template, Response, jsonify, Blueprint
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
        
        return Response(
                json.dumps(allapi, indent=2),
                mimetype='application/json'
            )


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
        
            return Response(
                json.dumps(data.to_dict(), indent=2),
                mimetype='application/json'
            )

        else:
            castles = Castle.query.all()
            counts = Castle.query.count()
            resp = {
                'counts': counts, 
                'status': 'successful',
                'results': [castle.to_dict() for castle in castles]
            }
        
            
            return Response(
                json.dumps(resp, indent=2),
                mimetype='application/json'
            )


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
            
            return Response(
                json.dumps(data.to_dict(), indent=2),
                mimetype='application/json'
            )
        
        else:
            houses = House.query.all()
            counts = House.query.count()
            resp = {
                'counts': counts, 
                'status': 'successful',
                'results': [house.to_dict() for house in houses]
            }
            
            return Response(
                json.dumps(resp, indent=2),
                mimetype='application/json'
            )



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
            
            return Response(
                json.dumps(data.to_dict(), indent=2),
                mimetype='application/json'
            )
        

        else:
            characters = Character.query.all()
            counts = Character.query.count()
            resp = {
                'counts': counts, 
                'status': 'successful',
                'results': [character.to_dict() for character in characters]
            }
                        
            return Response(
                json.dumps(resp, indent=2),
                mimetype='application/json'
            )



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
            
            return Response(
                json.dumps(data.to_dict(), indent=2),
                mimetype='application/json'
            )
        
            
        else:
            episodes = Episode.query.all()
            counts = Episode.query.count()
            resp = {
                'counts': counts, 
                'status': 'successful',
                'results': [episode.to_dict() for episode in episodes]
            }
        
            return Response(
                json.dumps(resp, indent=2),
                mimetype='application/json'
            )



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
            
            return Response(
                json.dumps(data.to_dict(), indent=2),
                mimetype='application/json'
            )
        
        else:
            seasons = Season.query.all()
            counts = Season.query.count()
            resp = {
                'counts': counts, 
                'status': 'successful',
                'results': [season.to_dict() for season in seasons]
            }
            return Response(
                json.dumps(resp, indent=2),
                mimetype='application/json'
            )

