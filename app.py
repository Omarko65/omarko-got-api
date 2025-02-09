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
    app.config.update({
        "SQLALCHEMY_DATABASE_URI": os.getenv("DB_URI")+"?sslmode=require",
        "SQLALCHEMY_ENGINE_OPTIONS": {
            "pool_pre_ping": True,  # Check connections before use
            "pool_recycle": 300,    # Recycle connections every 5 minutes
            "pool_size": 10,        # Adjust based on your needs
            "max_overflow": 5,
        },
        "JSONIFY_PRETTYPRINT_REGULAR": True
    })
    db.init_app(app)

    from routes import register_routes
    register_routes(app, db)
    
    with app.app_context():
        db.create_all()


    return app