import os
from flask import Flask, render_template, request, url_for, redirect, jsonify, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json
from dotenv import load_dotenv


load_dotenv()
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
    db.init_app(app)

    from routes import register_routes
    register_routes(app, db)
    
    with app.app_context():
        db.create_all()


    return app