def new_game():
    return {
        "mode": "camp",
        "contracts": [],
        "selected_contract": None,
        "fire_heat": 5,
        "fire_intensity": "FEEBLE",
        "fire_order": {"FEEBLE": 0, "CALM": 1, "CRACKLING": 2, "ROARING": 3},
        "resources": {"branches": 0, "paper": 0, "salt": 0, "skulls": 0, "herbs": 0},
        'key_items': {'map': 0,},
        'seen': [],

        # later:
        # "player": create_player(),
        # "gold": 0,
        # "inventory": [],
    }
