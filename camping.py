from recipes import RECIPES
import utils

def apply_heat_cost(game, amt):
    game['fire_heat'] -= amt
    game['fire_heat'] = utils.clamp(game['fire_heat'],0,30)


def check_for_ingredients(game, ingredients):
    for k, v in ingredients.items():
        if game['resources'].get(k, 0) < v:
            return False
    return True

def spend_ingredients(game, ingredients):
    for k, v in ingredients.items():
        game['resources'][k] -= v

def add_output(game, recipe):
    target = recipe.get('target', 'resources')
    for k, v in recipe['output'].items():
        game[target][k] = game[target].get(k, 0) + v





def create_item(game, item_id):
    recipe = RECIPES.get(item_id, None)

    if not recipe:
        return ["You can't craft that"]
    if game['fire_heat'] <= recipe['heat_cost']:
        return ["Fire is to weak"]
    if not check_for_ingredients(game, recipe['ingredients']):
        return ["You are missing something"]

    apply_heat_cost(game, recipe['heat_cost'])
    spend_ingredients(game, recipe['ingredients'])
    add_output(game, recipe)
    utils.update_fire_intensity(game)
    return [f"Fire gives you back {item_id}",
            f"Fire is now {game['fire_intensity']}"]

def create_paper(game):
    return create_item(game, 'paper')