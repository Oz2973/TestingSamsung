from flask import Flask, render_template

app = Flask(__name__)

# Sample recipes data
recipes_data = {
    1: {
        'name': 'Chocolate cake',
        'ingredients': '200g sugar, 200g butter, 4 eggs, 200g flour, 2 tbsp cocoa powder, 1 tsp baking powder, 1/2 tsp vanilla extract and 2 tbsp milk',
        'instructions': '1. heat oven to 180C. 2.mix in a bowl all ingredients listed above and mix until pale. 3.bake in the oven for 20m. 4. let cool for 10m and enjoy.',
        'photo': 'static/image/recipe1.jpg',
    },
    2: {
        'name': 'Rose pasta',
        'ingredients': '3 cloves garlic, 1tbsp oil, 400ml tomato sauce, 1/2cup of parmesan cheese, 1 cup heavy cream and salt and pepper for seasoning',
        'instructions': '1. cut garlic to small pieces. 2.heat oil and add the garlic cook for a minute and then stir. 3. add tomato sauce and stir well. 4.add parmesan cheese while stirring. 5. add the cream and stir. 6.add salt and pepper to taste. 7.stir for 5 more minutes and remove from heat. 8. bon appetite!',
    },
    3: {
        'name': 'Recipe 3',
        'ingredients': 'Ingredients for Recipe 3',
        'instructions': 'Instructions for Recipe 3',
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recipes')
def recipes():
    return render_template('recipes.html', recipes=recipes_data)


@app.route('/recipes/<int:recipe_id>')
def recipe_detail(recipe_id):
    recipe = recipes_data.get(recipe_id)
    if recipe:
        return render_template('recipe_detail.html', recipe=recipe)
    else:
        return "Recipe not found", 404

@app.route('/add')
def add_recipe():
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
