from flask import Flask

api = Flask(__name__)

@api.route('/')
def hello():
    response_body = {
        "name": "Rider Cogswell",
    }

    return response_body
