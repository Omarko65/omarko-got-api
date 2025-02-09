import json

'''conversion of id passed'''


def convert_to_int(id):
    try:
        int(id)
        return int(id)
    except (TypeError, ValueError):
        return (0)


