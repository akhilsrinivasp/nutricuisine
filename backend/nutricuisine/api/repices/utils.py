import openai
import os
from dotenv import load_dotenv

load_dotenv()
    
def get_recipe_recommendation(ingredients):
    prompt = f"""I am an AI trained to provide cooking recipes based on ingredients. Here is an example format of how you can use me:

    Ingredients: chicken, rice, broccoli
    Recipe: One Pot Chicken and Broccoli Rice Bowl
            Servings: 4 
            Calories: 671 
            Protein: 48g 
            Carbs: 80g
            Fat: 17g

            Ingredients:
            - 2 tablespoons extra virgin olive oil
            - 1 pound boneless, skinless chicken breasts, cut into 1-inch cubes
            - 1 teaspoon Italian seasoning
            - Salt and freshly ground black pepper
            - 2 cloves garlic, minced
            - 2 tablespoons all-purpose flour
            - 1½ cups chicken broth
            - 1 head broccoli, cut into small florets (about 4 cups)
            - 2 cups white or brown rice, cooked according to package instructions

            Instructions:
            1. Heat the olive oil in a large skillet over medium-high heat. 
            2. Add the chicken, Italian seasoning, salt, and pepper and cook until the chicken is cooked through, about 8 minutes.
            3. Add the garlic and cook for another minute or until fragrant.
            4. Sprinkle the flour over the chicken and stir to coat.
            5. Add the chicken broth and stir to combine.
            6. Add the broccoli and stir to combine.
            7. Simmer until the sauce has thickened, about 5 minutes.
            8. Serve the chicken and broccoli over the cooked rice.

    Ingredients: {ingredients}
    Recipe:"""
    openai.api_key = os.getenv('OPENAI_API_KEY')

    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=600  # Adjust the number of tokens as needed
        )
        recipe = response.choices[0].text.strip()
        
        # find servings in recipe then take the number next to it
        servings = recipe.split('Servings:')[1].split('\n')[0].strip()
        # find calories in recipe then take the number next to it
        calories = recipe.split('Calories:')[1].split('\n')[0].strip()
        # find protein in recipe then take the number next to it
        protein = recipe.split('Protein:')[1].split('\n')[0].strip()[0:-1]
        # find carbs in recipe then take the number next to it
        carbs = recipe.split('Carbs:')[1].split('\n')[0].strip()[0:-1]
        # find fat in recipe then take the number next to it
        fat = recipe.split('Fat:')[1].split('\n')[0].strip()[0:-1]
        print(servings)
        title = recipe.split('\n')[0].strip()
        
        ingredients = recipe.split('Ingredients:')[1].split('Instructions:')[0].strip()
        ingredients = ingredients.split('\n')
        ingredients = list(filter(None, ingredients))
        ingredients = [ingredient.strip() for ingredient in ingredients]
        ingredients = [ingredient[2:] for ingredient in ingredients]
        
        instructions = recipe.split('Instructions:')[1].strip()
        instructions = instructions.split('\n')
        instructions = list(filter(None, instructions))
        instructions = [instruction.strip() for instruction in instructions]
        instructions = [instruction[2:] for instruction in instructions]
        
        # form json file 
        recipe = {
            "title": title,
            "servings": servings,
            "calories": calories,
            "protein": protein,
            "carbs": carbs,
            "fat": fat,
            "ingredients": ingredients,
            "instructions": instructions
        }
        return recipe
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # Example usage
    ingredients = "tomato, cheese, bread"

    recipe_suggestion = get_recipe_recommendation(ingredients)
    print(recipe_suggestion)
    
    


