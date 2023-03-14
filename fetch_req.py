import json

'''conversion of id passed'''


def convert_to_int(id):
    try:
        int(id)
        return int(id)
    except (TypeError, ValueError):
        return (0)


'''Fetcher for castle request'''


def req_castle(id=None):
    if not id:
        with open('castles.json') as f:
            data = json.load(f)
        return (data)

    elif convert_to_int(id) != 0 and int(id) < 122:
        with open('castles.json') as f:
            data = json.load(f)
        for castle in data['results']:
            if castle['castle_id'] == int(id):
                return castle

    else:
        return (0)


'''Fetcher For House request'''


def req_house(id=None):
    if not id:
        with open('houses.json') as f:
            data = json.load(f)
        return (data)

    elif convert_to_int(id) != 0 and int(id) < 591:
        with open('houses.json') as f:
            data = json.load(f)
        for house in data['results']:
            if house['house_id'] == int(id):
                return house

    else:
        return (0)


'''Fetcher for character request'''


def req_character(id=None):
    if not id:
        with open('characters.json') as f:
            data = json.load(f)
        return (data)

    elif convert_to_int(id) != 0 and int(id) < 2049:
        with open('characters.json') as f:
            data = json.load(f)
        for character in data['results']:
            if character['character_id'] == int(id):
                return character

    else:
        return (0)


'''Fetcher for episode request'''


def req_episode(id=None):
    if not id:
        with open('episodes.json') as f:
            data = json.load(f)
        return (data)

    elif convert_to_int(id) != 0 and int(id) < 51:
        with open('episodes.json') as f:
            data = json.load(f)
        for episode in data['results']:
            if episode['episode_id'] == int(id):
                return episode

    else:
        return (0)


def req_season(id=None):
    if not id:
        with open('seasons.json') as f:
            data = json.load(f)
        return (data)

    elif convert_to_int(id) != 0 and int(id) < 6:
        with open('seasons.json') as f:
            data = json.load(f)
        for season in data['results']:
            if season['season_id'] == int(id):
                return season

    else:
        return (0)


def req_api():
    with open('api.json') as f:
        data = json.load(f)
    return data
