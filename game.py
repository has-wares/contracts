def new_game():
    return {
        "mode": "camp",
        "contracts": [],
        "selected_contract": None,
        "encounter_index": 0,
        "fire_heat": 9,
        "fire_intensity": "CALM",
        "resources": {"branches": 0, "paper": 0, "salt": 0, "skulls": 0, "herbs": 0},
        'key_items': {'map': 0,},
        'seen': [],

        # later:
        # "player": create_player(),
        # "gold": 0,
        # "inventory": [],
    }
