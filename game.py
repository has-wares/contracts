def new_game():
    return {
        "mode": "camp",
        "contracts": [],
        "selected_contract": None,
        "encounter_index": 0,
        "fire points": 15,
        "max fire points": 15,
        "fire heat": 9,
        "fire intensity": "CALM",
        "resources": {"wood": 0, "paper": 0, "salt": 0, "skulls": 0, "herbs": 0},

        # later:
        # "player": create_player(),
        # "gold": 0,
        # "inventory": [],
    }
