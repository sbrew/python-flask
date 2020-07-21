import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
            type=str,
            required=True,
            help="Username Field cannot be left blank"
        )
    parser.add_argument('password',
            type=str,
            required=True,
            help="Password Field cannot be left blank.. would you just leave your doors unlocked??"
        )z

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "That username is already in use"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."},201