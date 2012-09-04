from exampleapp.models import DBSession, User
from flask import Flask, request, abort

app = Flask("exampleapp")
log = app.logger

@app.teardown_request
def shutdown_session(exception=None):
    session = DBSession()
    
    if exception:
        session.rollback()
        log.error("Unhandled Execption:\n%s", traceback.format_exc())
    else:
        try:
            session.commit()
        except:
            log.error("Error committing transaction: %s", traceback.format_exc())
            session.rollback()
                
    DBSession.remove()

@app.route("/hello", methods=["GET"])
def hello_world():
    return "Hello World"
