from app import db
from sqlalchemy import JSON
import json

class Season(db.Model):
    __tablename__ = 'seasons'
    season_id = db.Column(db.Integer, primary_key=True)
    season = db.Column(db.Integer, nullable=False)
    episodes_name = db.Column(JSON)
    premiere = db.Column(db.String, nullable=False)
    finale = db.Column(db.String, nullable=False)
    airDate = db.Column(JSON)
    episodes = db.Column(JSON)

    def __repr__(self):
        allattributes = {'season': self.season, 'episodes_name': self.episodes_name, 'premiere': self.premiere, 'finale': self.finale, 'airDate': self.airDate, 'episodes': self.episodes}
        return json.dumps(allattributes, indent=4)

    def to_dict(self):
        return {'season': self.season, 'episodes_name': self.episodes_name, 'premiere': self.premiere, 'finale': self.finale, 'airDate': self.airDate, 'episodes': self.episodes}



class Episode(db.Model):
    __tablename__ = 'episodes'
    episode_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    episode = db.Column(db.Integer,nullable=False)
    season = db.Column(db.String, nullable=False)
    characters = db.Column(JSON)
    director = db.Column(db.String, nullable=False)
    airDate = db.Column(db.String, nullable=False)
    predecessor = db.Column(db.String)
    successor = db.Column(db.String)
    total_episode = db.Column(db.Integer)

    def __repr__(self):
        allattributes = {'episode_id': self.episode_id, 'name': self.name, 'episode': self.episode, 'season': self.season, 'characters': self.characters, 'director': self.director, 'airDate': self.airDate, 'predecessor': self.predecessor, 'successor': self.successor}
        return json.dumps(allattributes, indent=4)
    
    def to_dict(self):
        return {'episode_id': self.episode_id, 'name': self.name, 'episode': self.episode, 'season': self.season, 'characters': self.characters, 'director': self.director, 'airDate': self.airDate, 'predecessor': self.predecessor, 'successor': self.successor}
    

class Castle(db.Model):
    __tablename__ = 'castles'
    castle_id =  db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    castle_type = db.Column(db.String, nullable=False)
    religion = db.Column(JSON)
    founder = db.Column(JSON)
    holders = db.Column(JSON)

    def _repr__(self):
        allattributes = {'castle_id': self.castle_id, 'name': self.name, 'location': self.location, 'castle_type': self.castle_type, 'religion': self.religion, 'founder': self.founder, 'holders': self.holders}
        return json.dumps(allattributes, indent=4)

    def to_dict(self):
        return {'castle_id': self.castle_id, 'name': self.name, 'location': self.location, 'castle_type': self.castle_type, 'religion': self.religion, 'founder': self.founder, 'holders': self.holders}

class Character(db.Model):
    __tablename__ = 'characters'
    character_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    alive = db.Column(db.Boolean, default=True, nullable=False)
    titles = db.Column(JSON)
    spouse = db.Column(JSON)
    children = db.Column(JSON)
    father = db.Column(db.String)
    mother = db.Column(db.String)
    heir = db.Column(db.String)
    house = db.Column(db.String)
    placeOfBirth = db.Column(db.String)
    culture = db.Column(db.String)

    def __repr__(self):
        allattributes = {'character_id': self.character_id, 'name': self.name, 'gender': self.gender, 'alive': self.alive, 'titles': self.titles, 'spouse': self.spouse, 'children': self.children, 'father': self.father, 'mother': self.mother, 'heir': self.heir, 'house': self.house, 'placeOfBirth': self.placeOfBirth, 'culture': self.culture}
        return json.dumps(allattributes, indent=4)

    def to_dict(self):
        return {'character_id': self.character_id, 'name': self.name, 'gender': self.gender, 'alive': self.alive, 'titles': self.titles, 'spouse': self.spouse, 'children': self.children, 'father': self.father, 'mother': self.mother, 'heir': self.heir, 'house': self.house, 'placeOfBirth': self.placeOfBirth, 'culture': self.culture}

class House(db.Model):
    __tablename__ = 'houses'
    house_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    titles = db.Column(JSON)
    isExtinct = db.Column(db.Boolean, default=False, nullable=False)
    overlords = db.Column(JSON)
    heir = db.Column(db.String)
    coatOfArms = db.Column(db.String)
    words = db.Column(db.String)
    currentLord = db.Column(db.String)
    seat = db.Column(db.String)
    region = db.Column(db.String)
    founded = db.Column(db.String)
    founder = db.Column(db.String)

    def __repr__(self):
        allattributes = {'house_id': self.house_id, 'name': self.name, 'titles': self.titles, 'isExtinct': self.isExtinct, 'overlords': self.overlords, 'heir': self.heir, 'coatOfArms': self.coatOfArms, 'words': self.words, 'currentLord': self.currentLord, 'seat': self.seat, 'region': self.region, 'founded': self.founded, 'founder': self.founder}
        return json.dumps(allattributes, indent=4)
    
    def to_dict(self):
        return {'house_id': self.house_id, 'name': self.name, 'titles': self.titles, 'isExtinct': self.isExtinct, 'overlords': self.overlords, 'heir': self.heir, 'coatOfArms': self.coatOfArms, 'words': self.words, 'currentLord': self.currentLord, 'seat': self.seat, 'region': self.region, 'founded': self.founded, 'founder': self.founder}