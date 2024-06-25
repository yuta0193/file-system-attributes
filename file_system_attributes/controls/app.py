"""flask appの初期化を行い、flask appオブジェクトの実体を持つ"""
from flask import Flask
from controls.database import init_db
from controls.config import Config
import models.models

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_db(app)

    return app

app = create_app()
