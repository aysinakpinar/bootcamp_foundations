from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

def test_get_all_recipes(db_connection):
    db_connection.seed("seeds/recipes.sql")

    repository = RecipeRepository(db_connection)
    recipes = repository.all()
    assert recipes == [
        Recipe(1, 'Lasagna', 120, 5),
        Recipe(2, 'Mac & Cheese', 30, 4),
        Recipe(3, 'Shepperds Pie', 60, 3),
        Recipe(4, 'Dolma', 120, 5),
        Recipe(5, 'Chicken Ramen', 90, 4) 
    ]   

def test_find_all(db_connection):
    db_connection.seed("seeds/recipes.sql")

    repository = RecipeRepository(db_connection)
    assert repository.find('Mac & Cheese', "name") == Recipe(2, 'Mac & Cheese', 30, 4)
