from flask import Blueprint, jsonify, request
from nutricuisine.models import User, Food, ConsumedFood
from nutricuisine.models import foods_schema, food_schema
from nutricuisine import db
from flask_jwt_extended import jwt_required, get_jwt_identity

food_blueprint = Blueprint('food', __name__, url_prefix='/food')

@food_blueprint.route('/', methods=['GET', 'POST'])
def get_all_food():
    if request.method == 'POST':
        name = request.form.get('name')
        calories = request.form.get('calories')
        protein = request.form.get('protein')
        carbs = request.form.get('carbs')
        fat = request.form.get('fat')
        food = Food(name, calories, protein, carbs, fat)
        db.session.add(food)
        db.session.commit()
        return jsonify({'message': 'Food added successfully'})
    if request.method == 'GET':
        foods = Food.query.all()
        return jsonify({'foods': foods_schema.dump(foods)})

@food_blueprint.route('/<int:food_id>', methods=['GET'])
def get_food(food_id):
    food = Food.query.filter_by(id=food_id).first()
    if not food:
        return jsonify({'message': 'Food not found'})
    return jsonify({'food': food_schema.dump(food)})

