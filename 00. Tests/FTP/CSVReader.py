import csv


def get_terminals() -> list:
    with open("terminals.csv") as file:
        terminals = csv.reader(file)
        result = list()
        for terminal in terminals:
            result.append(terminal)
        return [item for sublist in result for item in sublist]
