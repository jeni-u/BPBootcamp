from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route('/new/recipe')
def newRecipe():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': session['user_id']
    }
    user = User.get_user_by_id(data)
    return render_template('addrecipe.html',user=user)


@app.route('/create/recipe', methods=['POST'])
def createRecipe():
    if 'user_id' not in session:
        return redirect('/')

    if not Recipe.validate_recipe(request.form):
        return redirect(request.referrer)

    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date': request.form['date'],
        'time_takes': request.form['time_takes'],
        'user_id': session['user_id']
    }

    Recipe.create(data)
    return redirect('/dashboard')



@app.route('/recipe/<int:id>')
def getRecipe(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'recipe_id': id,
        'id': session['user_id']
    }
    recipe = Recipe.get_recipe_by_id(data)
    loggedUser = User.get_user_by_id(data)
    return render_template('recipe.html', recipe=recipe, loggedUser=loggedUser)


@app.route('/edit/recipe/<int:id>')
def editRecipe(id):
    if 'user_id' not in session:
        return redirect('/')

    recipe = Recipe.get_recipe_by_id(id)
    if not recipe:
        return redirect('/')
    loggedUser = User.get_user_by_id({'id': session['user_id']})
    if recipe['user_id'] != loggedUser['id']:
        return redirect('/')

    return render_template('editRecipe.html', recipe=recipe, loggedUser=loggedUser)


@app.route('/update/recipe/<int:id>', methods=['POST'])
def updateRecipe(id):
    if 'user_id' not in session:
        return redirect('/')

    recipe = Recipe.get_recipe_by_id(id)
    if not recipe:
        return redirect('/')
    
    loggedUser = User.get_user_by_id({'id': session['user_id']})
    if not loggedUser:
        return redirect('/')

    if recipe['user_id'] != loggedUser['id']:
        return redirect('/')

    updateData = {
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date': request.form['date'],
        'time_takes': request.form.get('time_takes'),  # Use .get() to avoid KeyError if not present
        'id': id
    }
    
    if not Recipe.validate_recipe(updateData):
        return redirect(request.referrer)

    Recipe.update_recipe(updateData)
    return redirect('/dashboard')

    

@app.route('/delete/recipe/<int:id>')
def deleteRecipe(id):
    if 'user_id' not in session:
        return redirect('/')
    
    recipe = Recipe.get_recipe_by_id(id)
    if not recipe:
        return "Recipe not found", 404
    
    user_id = session['user_id']
    logged_user = User.get_user_by_id({'id': user_id})
    if not logged_user:
        return "User not found", 404
    
    if logged_user['id'] == recipe['user_id']:
        Recipe.delete_recipe({'recipe_id': id})
    
    return redirect(request.referrer)




@app.route('/view/recipe/<int:id>')
def show(id):
    if 'user_id' not in session:
        return redirect('/')
    data ={
        'id': session['user_id']
    }
    recipes = Recipe.get_recipe_by_id(id)
    loggedUser = User.get_user_by_id(data)
    return render_template("view.html", recipes=recipes, loggedUser=loggedUser)

