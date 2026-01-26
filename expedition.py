import uiconfig
from areas import AREAS
import ui

def cmd_embark(args, game):
    if len(args) == 0:
        return ['Embark to where?']

    area_id = args[0] if len(args) == 1 else args[-1]

    if area_id not in AREAS:
        return [f"Unknown area: {area_id}"]

    if area_id not in game['camp']['seen']:
        return ['you cant go there']

    area = AREAS[area_id]
    game['mode'] = 'expedition'
    game['expedition'] = {"area_id": area_id, "depth": 0, "actions": 8,
                          "supplies": 6, "danger": area['base_danger'],
                          }

    return [area['intro']]

def abandon(args, game):
    game['mode'] = 'camp'
    game['expedition'] = {}
    return ['run chicken run']

def advance(args, game):
    expedition = game['expedition']
    area = AREAS[expedition['area_id']]
    expedition['actions'] -= 1
    expedition['depth'] += 1
    expedition['danger'] += 0.1

    if expedition['depth'] >= area['max_depth'] or expedition['actions'] <= 0:
        game['mode'] = 'camp'
        expedition.clear()
        return [area['outro'], "--- BACK TO CAMP ---"]

    return ['some random advance message']


def draw_expedition(screen, exp, font, r_lines, s_lines):
    screen.fill(uiconfig.BLACK)
    ui.draw_scrollable_text(screen, r_lines, s_lines, font, uiconfig.WHITE, ui.RESPONSE_BOX)
    return s_lines