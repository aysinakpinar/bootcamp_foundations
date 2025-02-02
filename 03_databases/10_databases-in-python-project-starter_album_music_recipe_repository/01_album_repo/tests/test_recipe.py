from lib.recipe import Recipe
def test_attributes_recipe():
    recipe = Recipe(1, 'Lasagna', 120, 5)
    assert recipe.id == 1
    assert recipe.name == 'Lasagna'
    assert recipe.cooking_time == 120
    assert recipe.rating == 5

def test_recipes_equal():
    recipe1 = Recipe(1, 'Lasagna', 120, 5)
    recipe2= Recipe(1, 'Lasagna', 120, 5)
    assert recipe1 == recipe2

def test_recipe_format():
    recipe = Recipe(1, 'Lasagna', 120, 5)
    assert str(recipe) == "Recipe(1, Lasagna, 120, 5)"