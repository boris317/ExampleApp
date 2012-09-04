from sqlalchemy import engine_from_config

from exampleapp.models import init_db
from exampleapp.wsgi import app

def make_app(global_conf, **conf):
    init_db(engine_from_config(conf))            
    app.config.update(conf)
    return app
