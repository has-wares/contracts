from recipes import RECIPES
import utils
import ui
import uiconfig

def apply_heat_cost(game, amt):
    camp = game['camp']
    camp['fire_heat'] -= amt
    camp['fire_heat'] = utils.clamp(camp['fire_heat'],0,60)


def check_for_ingredients(game, ingredients):
    camp = game['camp']
    for k, v in ingredients.items():
        if camp['resources'].get(k, 0) < v:
            return False
    return True

def spend_ingredients(game, ingredients):
    camp = game['camp']
    for k, v in ingredients.items():
        camp['resources'][k] -= v

def add_output(game, recipe):
    camp = game['camp']
    target = recipe.get('target', 'resources')
    for k, v in recipe['output'].items():
        camp[target][k] = camp[target].get(k, 0) + v





def create_item(game, item_id):
    camp = game['camp']
    recipe = RECIPES.get(item_id, None)

    if not recipe:
        return ["You can't craft that"]
    if camp['fire_heat'] <= recipe['heat_cost']:
        return ["Fire is to weak"]
    if not check_for_ingredients(game, recipe['ingredients']):
        return ["You are missing something"]

    apply_heat_cost(game, recipe['heat_cost'])
    spend_ingredients(game, recipe['ingredients'])
    add_output(game, recipe)
    utils.update_fire_intensity(game)
    return [f"Fire gives you back {item_id}",
            f"Fire is now {camp['fire_intensity']}"]

def create_paper(game):
    camp = game['camp']
    level = camp['fire_order'][camp['fire_intensity']]

    if level < camp['fire_order']["CALM"]:
        return ["Fire is weak", "Fire Intensity required: CALM"]
    if level > camp['fire_order']['CALM']:
        return ["Fire is too wild", "paper turns to ash", "Fire Intensity required: CALM"]

    return create_item(game, "paper")


def draw_camp(screen, dt, fire, game, font, response_lines, scroll_lines):
    camp = game['camp']
    fire.update(dt, 8)
    screen.fill(uiconfig.BLACK)
    fire.draw_centered(screen, ui.BONFIRE_BOX.center)

    ui.draw_rect(screen, uiconfig.WHITE, ui.RESOURCE_BOX)
    ui.draw_text(screen, f"FIRE HEAT: {camp['fire_heat']}", font, uiconfig.WHITE, ui.FIRE_INFO_BOX)
    ui.draw_text(screen, f"FIRE: {camp['fire_intensity']}", font, uiconfig.WHITE, ui.FIRE_INFO_BOX, padding=740)
    ui.draw_multiline_text(screen, utils.format_resources(camp), font, uiconfig.WHITE, ui.RESOURCE_BOX)

    scroll_lines, max_scroll = ui.draw_scrollable_text(
        screen, response_lines, scroll_lines, font, uiconfig.WHITE, ui.RESPONSE_BOX
    )
    scroll_lines = max(0, min(scroll_lines, max_scroll))
    return scroll_lines