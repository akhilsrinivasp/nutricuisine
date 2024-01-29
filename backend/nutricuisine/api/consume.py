from flask import Blueprint, jsonify, request
from nutricuisine.models import User, Food, ConsumedFood, food_schema
from nutricuisine import db
from flask_jwt_extended import jwt_required, get_jwt_identity

consume_blueprint = Blueprint('consume', __name__, url_prefix='/consume')

@consume_blueprint.route('/', methods=['GET', 'POST'])
@jwt_required()
def consume():
    # user_id, food_id, quantity
    username = get_jwt_identity()
    user = User.query.filter_by(username=username).first()
    user_id = user.id
    
    if request.method == 'POST':
        food_id = request.form.get('food_id')
        quantity = request.form.get('quantity')
        consumed_food = ConsumedFood(user_id, food_id, quantity)
        db.session.add(consumed_food)
        db.session.commit()
        return jsonify({'message': 'Food consumed successfully'})
    
    if request.method == 'GET':
        consumed_food = ConsumedFood.query.filter_by(user_id=user_id).all()
        # now get actual data from food table
        foods = []
        for food in consumed_food:
            food_id = food.food_id
            temp = Food.query.filter_by(id=food_id).first()
            temp = food_schema.dump(temp)
            temp['quantity'] = food.quantity
            temp["created_at"] = food.created_at
            temp["consume_id"] = food.id
            
            foods.append(temp)
        return jsonify({'foods': foods})
    
    
@consume_blueprint.route('/<int:consume_id>', methods=['DELETE'])
@jwt_required()
def delete_consumed_food(consume_id):
    if request.method == 'DELETE':
        username = get_jwt_identity()
        user = User.query.filter_by(username=username).first()
        user_id = user.id
        consumed_food = ConsumedFood.query.filter_by(user_id=user_id, id=consume_id).first()
        db.session.delete(consumed_food)
        db.session.commit()
        return jsonify({'message': 'Food deleted successfully'})
    

        
    