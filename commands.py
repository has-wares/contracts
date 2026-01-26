from contractor import get_contracts, create_contract_log
import finetune as ft
import utils
import camping
import expedition

def get_help(args, game):
    return [
        "Commands:",
        "  help",
        "  look",
        "  contracts",
        "  gather <item>",
        "  create <item>",
        "  burn <item>",
        "",
        "Tip: Use PageUp/PageDown or mouse wheel to scroll",
        "the log."
    ]



def look(args, game):
    camp = game['camp']
    fire_intensity = camp['fire_intensity']

    if fire_intensity == "FEEBLE":
        return ["Fire allows no vision"]
    elif fire_intensity == "CALM":
        if 'monastery' not in camp['seen']:
            camp['seen'].append('monastery')
            return ["Fire allows for a vision",
                    "Road to the Monastery is visible"]
        return ["You see the road to the Monastery"]
    elif fire_intensity == "CRACKLING":
        return ["Beyond the Monastery you see.."]
    else:
        return ["Beyond .. you see the Forsaken Shore"]

####may be removed####
def show_contracts(args, game):
    contracts = game['global']['contracts']

    if not contracts:
        contracts.extend(get_contracts())

    log = create_contract_log(contracts)
    return ["CONTRACTS:"] + log


def select_contract(args, game):

    if len(args) == 0:
        return ["Select which one?(1 2 r 3)"] + show_contracts(args,game)

    return ["Blabla"]
####may be removed####

def gather(args, game):
    camp = game['camp']
    resources = ['branches', 'herbs']
    if not args:
        return ["Gather what?",
                "wood/herbs"]

    resource = args[0]

    if resource not in resources:
        return ["You can't gather something like that"]

    if camp['fire_heat'] > ft.action_costs[resource]: # fire doesnt go 0 for now
        camp['fire_heat'] -= ft.action_costs[resource]
        camp['resources'][resource] += ft.to_gather[resource]
        camping.update_fire_intensity(camp)
        return [f"Gathered {ft.to_gather[resource]} {resource}",
                'Time passes fire weakens']
    else:
        return ["Fire does not allow venturing further"]

def burn(args, game):
    camp = game['camp']
    fuels = ["branches", "skulls"]
    singular_to_plural = {"branch": "branches", "skull": "skulls"}
    plural_to_singular = {v: k for k, v in singular_to_plural.items()}

    if not args:
        return [
            "Burn what?",
            "Usage: burn <resource>  OR  burn <amount> <resource>",
            "Examples: burn branch | burn 2 branches"
        ]


    if len(args) == 1:
        amount = 1
        raw = args[0].lower()
    elif len(args) == 2 and args[0].isdigit():
        amount = int(args[0])
        raw = args[1].lower()
    else:
        return ["Nothing happens.", "Usage: burn <resource> OR burn <amount> <resource>"]

    if amount <= 0:
        return ["Burn how many?"]


    resource = singular_to_plural.get(raw, raw)

    if resource not in fuels:
        return ["You can't burn something like that."]

    if camp["resources"].get(resource, 0) < amount:
        return [f"Not enough {resource}."]

    extra = []
    if raw in fuels and amount == 1:
        extra = ["(It's 'branch'. The fire doesn't care.)"]
    elif raw in singular_to_plural and amount != 1:  # "burn 5 branch"
        extra = ["(Plural. The fire can count, at least.)"]

    camp["resources"][resource] -= amount
    camp["fire_heat"] += ft.heat_gains[resource] * amount
    camping.update_fire_intensity(camp)

    shown = plural_to_singular[resource] if amount == 1 else resource

    return [
        f"You burn {amount} {shown}.",
        "Fire thanks you for your service.",
        f"The fire is now {camp['fire_intensity']}."
    ] + extra


def create(args, game):
    camp = game['camp']
    dispatch ={
        'paper' : camping.create_paper,
            }

    if not args:
        return ["Create what?",
                "Try paper.."]

    item_id = args[0]
    func = dispatch.get(item_id)
    if not func:
        return ["you can't create that"]
    return func(camp)

def embark(args,game):
    if game['mode'] != 'camp':
        return ["you cant embark from here"]
    return expedition.cmd_embark(args, game)

def abandon(args, game):
    if game['mode'] == 'camp':
        return ['you cant abandon the camp']

    return expedition.abandon(args, game)

def advance(args, game):
    return expedition.advance(args, game)

COMMAND_MAP = {
    'help': get_help,
    'look': look,
    'contracts': show_contracts,
    'gather': gather,
    'burn' : burn,
    'create': create,
    'select': select_contract,
    'embark': embark,
    'abandon': abandon,
    'advance' : advance,
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

    return func(args, game)