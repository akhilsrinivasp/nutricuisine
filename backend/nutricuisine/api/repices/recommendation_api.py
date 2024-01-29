from flask import Blueprint, request, jsonify
from nutricuisine.models import Food
from nutricuisine import db
from nutricuisine.api.repices.utils import get_recipe_recommendation

recommendation_blueprint = Blueprint('recommend', __name__, url_prefix='/recommend')

@recommendation_blueprint.route('/', methods=['POST'])
def recommend():
    if request.method == 'POST':
        ingredients = request.form.get('ingredients')
        recipe = get_recipe_recommendation(ingredients)
        food = Food.query.filter_by(name=recipe['title']).first()
        if not food:
            food = Food(
                name=recipe['title'],
                calories=recipe['calories'],
                protein=recipe['protein'],
                carbs=recipe['carbs'],
                fat=recipe['fat']
            )
            db.session.add(food)
            db.session.commit()
            food = Food.query.filter_by(name=recipe['title']).first()
        recipe['id'] = food.id
        return jsonify({'recipe': recipe})
    else:
        return jsonify({'error': 'Invalid request method'})
    
# example curl request: curl -X POST -F 'ingredients=chicken, rice, broccoli' http://
