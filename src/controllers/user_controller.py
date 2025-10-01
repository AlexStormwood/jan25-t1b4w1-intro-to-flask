from flask import Blueprint, jsonify, request
from src.init import db
from src.models.user import User
from src.schemas import user_schema, users_schema

user_bp = Blueprint("users", __name__, url_prefix="/users")

@user_bp.route("/", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify(users_schema.dump(users)), 200

@user_bp.route("/all/alternative", methods=["GET"])
def get_users_alternative():
    db_statement = db.select(User)
    users_list = db.session.scalars(db_statement)
    
    if users_list:
        return jsonify(users_schema.dump(users_list)), 200
    else:
        return jsonify({"message":"No data found."}), 404


# Jumping ahead - dynamic routing and POSTing data is beyond the scope of this week!
@user_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify(user_schema.dump(user)), 200
    else:
        return jsonify({"message": "User not found."}), 404
    
@user_bp.route("/", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({"message": "No input data provided"}), 400
    
    errors = user_schema.validate(data, session=db.session)
    if errors:
        return jsonify(errors), 422
    
    new_user = User(
        username=data["username"],
        email=data["email"]
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify(user_schema.dump(new_user)), 201