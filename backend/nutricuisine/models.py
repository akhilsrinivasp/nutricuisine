from nutricuisine.database import db, ma
from sqlalchemy.sql import func 

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    
    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = password
    
    def __repr__(self):
        return '<User %r>' % self.username
    
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'username', 'email', 'created_at', 'updated_at')
        
user_schema = UserSchema()
users_schema = UserSchema(many=True)

class Food(db.Model):
    __tablename__ = 'food'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    protein = db.Column(db.Integer, nullable=True)
    carbs = db.Column(db.Integer, nullable=True)
    fat = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
    
    def __repr__(self):
        return '<Food %r>' % self.name

class FoodSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'calories', 'protein', 'carbs', 'fat', 'created_at', 'updated_at')
        
food_schema = FoodSchema()
foods_schema = FoodSchema(many=True)

class ConsumedFood(db.Model):
    __tablename__ = 'consumed_food'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    food_id = db.Column(db.Integer, db.ForeignKey('food.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    
    def __init__(self, user_id, food_id, quantity):
        self.user_id = user_id
        self.food_id = food_id
        self.quantity = quantity
    
    def __repr__(self):
        return '<ConsumedFood %r>' % self.id 
