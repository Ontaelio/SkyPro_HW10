import json

from models.persons import Person


def import_data(json_file: str = 'candidates.json'):
    """
    Get json data from the file provided
    :param json_file: filename, default is given
    :return: a list of dicts (or None if FNF)
    """

    try:
        with open(json_file, 'r', encoding='utf-8') as fin:
            staff = [Person(p) for p in json.load(fin)]
    except FileNotFoundError:
        staff = None

    return staff
