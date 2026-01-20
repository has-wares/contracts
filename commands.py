from contractor import get_contracts, create_contract_log

def get_help(args, game):
    return "Available Commands: help/look"

def look(args, game):
    return "You see the road to the Monastery"

def show_contracts(args, game):
    if len(game['contracts']) == 0:
        game['contracts'] = get_contracts()
    log = create_contract_log(game['contracts'])
    print("Generating contracts" if not game["contracts"] else "Reusing contracts")
    return "CONTRACTS:\n" + "\n".join(log)

COMMAND_MAP = {
    'help': get_help,
    'look': look,
    'contracts': show_contracts,
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
