import random
from contracts import CONTRACTS


def get_contracts():
    contracts = []
    while len(contracts) < 3 and len(contracts) < len(CONTRACTS):
        contract = random.choice(CONTRACTS)
        if contract not in contracts:
            contracts.append(contract)
    return contracts


def create_contract_log(contracts):
    contract_log = []
    for i, c in enumerate(contracts, 1):
        contract_log.append(f"{i}) {c['title']} (Diff {c['difficulty']}) Reward {c['reward']['gold']} gold!")
    return contract_log


def choose_contract(contracts):
    choice = input('Choose a contract: 1, 2, 3 !\n').strip()
    if choice.isdigit():
        n = int(choice)
        index = n - 1
        if 1<= n <= len(contracts):
            return contracts[index]

    return "Invalid Choice. Type 1, 2 or 3!!"