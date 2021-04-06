from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from app.admin import admin_bp
app = Flask(__name__)

app.register_blueprint(admin_bp)

api = Api(app)

response_regst = {
    "User": "user",
    "Token": "Token"
}

response_detect ={
    "detect": "detector",
    "Token": "Token"
}


class Register(Resource):
    def post(self):
        return jsonify(response_regst)

    def get(self):
        return "register Get"


class Detect(Resource):
    def post(self):
        return jsonify(response_detect)

    def get(self):
        return "Detect Get"


api.add_resource(Register, "/register")
api.add_resource(Detect, "/detect")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
