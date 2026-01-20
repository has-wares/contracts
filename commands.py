from contractor import get_contracts, create_contract_log
import finetune as ft

def get_help(args, game):
    return "Available Commands: help/look"

def look(args, game):
    return "You see the road to the Monastery"

def show_contracts(args, game):
    if len(game['contracts']) == 0:
        game['contracts'] = get_contracts()
    log = create_contract_log(game['contracts'])
    return "CONTRACTS:\n" + "\n".join(log)

def gather(args, game):
    resources = ['wood', 'herbs']
    if not args:
        return "Gather what?\nwood/herbs"

    resource = args[0]

    if resource not in resources:
        return "You can't gather something like that"

    if game['fire points'] >= ft.costs[resource]:
        game['fire points'] -= ft.costs[resource]
        game['resources'][resource] += ft.to_gather[resource]
        return f"Gathered {ft.to_gather[resource]} {resource}"
    else:
        return "Not enough fire points"



COMMAND_MAP = {
    'help': get_help,
    'look': look,
    'contracts': show_contracts,
    'gather': gather,
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
        return ""  # show nothing if empty enter

    func = COMMAND_MAP.get(cmd)
    if not func:
        return f"Unknown command: {cmd}"

    return func(args, game)  # <-- CALL the function
