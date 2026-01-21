from contractor import get_contracts, create_contract_log
import finetune as ft
import utils


def get_help(args, game):
    return [
        "Commands:",
        "  help",
        "  look",
        "  contracts",
        "  gather brC",
        "  gather herbs",
        "",
        "Tip: Use PageUp/PageDown or mouse wheel to scroll",
        "the log."
    ]



def look(args, game):
    fire_intensity = game['fire intensity']

    if fire_intensity == "CALM":
        return ["You see the road to the Monastery"]
    elif fire_intensity == "CRACKLING":
        return ["Beyond the Monastery you see.."]
    else:
        return ["Beyond .. you see the Forsaken Shore"]

def show_contracts(args, game):
    if len(game['contracts']) == 0:
        game['contracts'] = get_contracts()
    log = create_contract_log(game['contracts'])
    return ["CONTRACTS:"] + log

def gather(args, game):
    resources = ['wood', 'herbs']
    if not args:
        return ["Gather what?",
                "wood/herbs"]

    resource = args[0]

    if resource not in resources:
        return ["You can't gather something like that"]

    if game['fire heat'] > ft.action_costs[resource]:
        game['fire heat'] -= ft.action_costs[resource]
        game['resources'][resource] += ft.to_gather[resource]
        utils.update_fire_intensity(game)
        return [f"Gathered {ft.to_gather[resource]} {resource}",
                'Time passes the fire weakens']
    else:
        return ["If you leave now fire will extinguish"]

def burn(args, game):
    fuels = ["branches", "skulls"]

    if not args:
        return ["Burn what?",
                "Usage: burn <resource>  OR  burn <amount> <resource>"]

    if len(args) == 1:
        amount = 1
        resource = args[0]

    elif len(args) == 2 and args[0].isdigit():
        amount = int(args[0])
        resource = args[1]

    else:
        return ["Nothing happens",
                "Usage: burn <resource> OR burn <amount> <resource>"]

    if resource not in fuels:
        return ["You can't burn something like that"]

    if amount <= 0:
        return ["Burn how many?"]

    if game["resources"][resource] < amount:
        return [f"Not enough {resource}"]

    game["resources"][resource] -= amount
    game["fire heat"] += ft.heat_gains[resource] * amount
    utils.update_fire_intensity(game)

    # message fixes: don't hardcode wood
    return [
        f"You burn {amount} {resource}.",
        "Fire thanks you for your service.",
        f"The fire is now {game['fire intensity']}."
    ]



COMMAND_MAP = {
    'help': get_help,
    'look': look,
    'contracts': show_contracts,
    'gather': gather,
    'burn' : burn,
}

def parse_command(command: str):
    cmdline = command.lower().strip()
    if not cmdline:
        return None, []

    parts = cmdline.split()
    return parts[0], parts[1:]   # args is a list of words

def dispatch_command(command, game):
    cmd, args = parse_command(command)
    if not cmd:
        return []  # show nothing if empty enter

    func = COMMAND_MAP.get(cmd)
    if not func:
        return [f"Unknown command: {cmd}"]

    return func(args, game)  # <-- CALL the function
