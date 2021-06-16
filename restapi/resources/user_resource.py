from flask_restful import Resource, reqparse
from logic.user_logic import UserLogic


class User(Resource):
    def __init__(self):
        self.user_put_args = self.createParser()
        self.logic = UserLogic()

    def createParser(self):
        args = reqparse.RequestParser()
        args.add_argument("user_name", type=str, help="nombre de usuario")
        args.add_argument("user_email", type=str, help="email del usuario")
        args.add_argument("password", type=int, help="contraseña del usuario")
        return args

    def head(self, id):
        pass

    def get(self, id):
        result = self.logic.getUserById(id)
        if len(result) == 0:
            return {}
        else:
            return result[0], 200

    def post(self, id):
        result = self.logic.getUserById(id)
        if len(result) == 0:
            return {}
        else:
            return result[0], 200

    def put(self, id):
        user = self.user_put_args.parse_args()
        rows = self.logic.insertUser(user)
        return {"rowsAffefcted": rows}, 200

    def patch(self, id):
        user = self.user_put_args.parse_args()
        rows = self.logic.updateUser(id, user)
        return {"rowsAffefcted": rows}, 200

    def delete(self, id):
        rows = self.logic.deleteUser(id)
        return {"rowsAffefcted": rows}, 200
