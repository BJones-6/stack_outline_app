from flask import Flask

from config import Config
from .extensions import db




from sqlalchemy import event
from sqlalchemy.engine import Engine
import sqlite3


# 🔹 Enable foreign key enforcement for SQLite
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, sqlite3.Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()






def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from .routes import main

    app.register_blueprint(main)

    with app.app_context():
        db.create_all()

    return app
