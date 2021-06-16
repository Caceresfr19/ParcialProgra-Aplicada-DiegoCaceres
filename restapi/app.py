from flask import Flask
from flask_restful import Api
from resources.user_resource import User

app = Flask(__name__)
api = Api(app)

api.add_resource(User, "/user/<int:id>")

if __name__ == "__main__":
    app.run(debug=True)
