def new_game():
    return {
        "mode": "camp",

        'global' : {
            "contracts": [],
            "selected_contract": None,
            'inventory': {},
            'gold': 0,
            },


        'camp': {
            "fire_heat": 5,
            "fire_intensity": "FEEBLE",
            "fire_order": {"FEEBLE": 0, "CALM": 1, "CRACKLING": 2, "ROARING": 3},
            "resources": {"branches": 15, "paper": 0, "salt": 0, "skulls": 0, "herbs": 0},
            'key_items': {'map': 0,},
            'seen': [],
            },

        'expedition': {},


    }

def global_data(game):
    return game['global']

def mode_data(game):
    return game[game['mode']]