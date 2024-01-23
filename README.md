OMARKO-GOT-API
==============

### A GAME OF THRONE API INSPIRED BY [SWAPI API](https://swapi-api.alx-tools.com/) 

### Introduction

This documentation will be your guide on how to use [OMARKO-GOT-API](https://omarko-got-api.onrender.com/home/). It will show you how to request for data and explain what the data you've gotten means. Enjoy!

### How To Use

To send your first request you can use the request tool in the [home page](https://omarko-got-api.onrender.com/home/) or you can send a get request using curl or any other way you see fit

```
curl "https://omarko-got-api.onrender.com/castles/119"
```

You will get this response back

```
{
            "religion": [
            "Old Gods of the Forest"
            ],
            "founder": [
            "Brandon Stark (the Builder)"
            ],
            "name": "Winterfell",
            "location": "The North",
            "type": "CastleRegional capital",
            "age": 8000,
            "castle_id": 119,
            "holders": [
            "House Stark",
            "House Bolton",
            "House Greyjoy"
            ]
}
```

### ROOT URL

The root URL for all the api served is

```
curl "https://omarko-got-api.onrender.com/api/"
```

### RESOURCES

Here is all the information on the API OMARKO-GOT-API gives you

### Root

You can get information about api from the root

#### Example

```
curl "https://omarko-got-api.onrender.com/api/"
```

#### Response

```
{
            "castles": "https://omarko-got-api.onrender.com/castles/",
            "houses": "https://omarko-got-api.onrender.com/houses/",
            "characters": "https://omarko-got-api.onrender.com/characters/",
            "seasons": "https://omarko-got-api.onrender.com/seasons/",
            "episodes": "https://omarko-got-api.onrender.com/episodes/"
}
```


#### Attributes

*   **castles** _string_ -- This is the URL for castle resources
*   **houses** _string_ -- This is the URL for house resources
*   **characters** _string_ -- This is the URL for character resources
*   **seasons** _string_ -- This is the URL for season resources
*   **episodes** _string_ -- This is the URL for episode resources

### Castles

The Castles endpoint responds with castles in the Game Of Thrones World

#### Endpoints

*   **/castles/** -- returns all castles data
*   **/castles/:id/** -- returns castle data with specific id

#### Example

```
curl "https://omarko-got-api.onrender.com/castle/119/"
```

#### Response

```
{
            "religion": [
            "Old Gods of the Forest"
            ],
            "founder": [
            "Brandon Stark (the Builder)"
            ],
            "name": "Winterfell",
            "location": "The North",
            "type": "CastleRegional capital",
            "age": 8000,
            "castle_id": 119,
            "holders": [
            "House Stark",
            "House Bolton",
            "House Greyjoy"
            ]
}
```


#### Attributes

*   **religion** _array_ -- An array of the religion of holder of castle
*   **founder** _array_ -- An array of founder of castle
*   **name** _string_ -- Name of castle
*   **location** _string_ -- Location of castle
*   **age** _int_ -- Age of castle
*   **castle\_id** _int_ -- Id used to fetch castle data
*   **holder** _array_ -- Array containing holders of castle

### Houses

The House endpoint responds with different houses in the Game Of Thrones World

#### Endpoints

*   **/houses/** -- returns all house data
*   **/houses/:id/** -- returns house data with specific id

#### Example

```
curl "https://omarko-got-api.onrender.com/houses/10/"
```

#### Response

```
{
            "titles": [
            "King in the North/King of Winter",
            "Lord of Winterfell",
            "Warden of the North",
            "King of the Trident"
            ],
            "overlords": [
            "House Baratheon of King's Landing",
            "House Bolton"
            ],
            "ancestralWeapon": [],
            "coatOfArms": "A running grey direwolf, on an ice-white field(Argent, a direwolf courant cendr\u00e9e)",
            "words": "Winter is Coming",
            "currentLord": "Queen Sansa Stark",
            "seat": "Winterfell",
            "region": "North",
            "founded": null,
            "founder": "Bran the Builder",
            "cadetBranch": "House Greystark",
            "heir": "Arya Stark",
            "isExtinct": false,
            "house_name": "House Stark",
            "house_id": 10
}
```

#### Attributes

*   **title** _array_ -- Array of house title
*   **overlords** _array_ -- Overlords of house
*   **ancestralWeapon** _array_ -- House ancestral weapon
*   **coatOfArms** _string_ -- Coat of arm of house
*   **word** _string_ -- Phrase use by house frequently
*   **currentLord** _string_ -- Current lord of house
*   **seat** _string_ -- House seat
*   **region** _string_ -- Region house if from
*   **founded** _int_ -- When house was founded
*   **founder** _string_ -- Founder of house
*   **cadetBranch** _string_ -- Branch of house
*   **heir** _string_ -- Heir of house
*   **isExtinct** _boolean_ -- True if house is extinct else False
*   **house\_name** _string_ -- Hous\_txte name
*   **house\_id** _int_ -- Id used to fetch house data

### Characters

The character endpoint responds with different characters in the Game Of Thrones World

#### Endpoints

*   **/characters/** -- returns all character data
*   **/characters/:id/** -- returns character data with specific id

#### Example

```
curl "https://omarko-got-api.onrender.com/characters/1857/"
```

#### Response

```
{
        "titles": [
        "Lord Commander of the Night's Watch"
        ],
        "spouse": [],
        "children": [],
        "name": "Jon Snow",
        "gender": "male",
        "culture": "Northmen",
        "house": "House Stark",
        "alive": true,
        "character_id": 1857
}
```

#### Attributes

*   **title** _array_ -- An array containing character's titles
*   **spouse** _array_ -- Spouse of character
*   **children** _array_ -- Children of character
*   **name** _string_ -- Name of character
*   **gender** _string_ -- Gender of character
*   **culture** _string_ -- Culture of character
*   **house** _string_ -- House character belongs to
*   **alive** _boolean_ -- True if character is alive or False if not
*   **character\_id** _int_ -- id used to fetch character data

### Season

The season endpoint responds with different seasons of the Game Of Thrones show

#### Endpoints

*   **/seasons/** -- returns all seasons data
*   **/seasons/:id/** -- returns season data with specific id

#### Example

```
curl "https://omarko-got-api.onrender.com/seasons/2/"
```

#### Response

```
{
            "season": 2,
            "episodes": 10,
            "premiere": "The North Remembers",
            "finale": "Valar Morghulis",
            "airDate": [
            "2012-04-1",
            "2011-06-3"
            ],
            "season_id": 2,
            "episodes_name": [
            "The North Remembers",
            "The Night Lands",
            "What Is Dead May Never Die",
            "Garden of Bones",
            "The Ghost of Harrenhal",
            "The Old Gods and the New",
            "A Man Without Honor",
            "The Prince of Winterfell",
            "Blackwater",
            "Valar Morghulis"
            ]
}
```

#### Attributes

*   **season** _int_ -- Season of Game of Thrones show
*   **episodes** _int_ -- Number of episodes in season
*   **premiere** _string_ -- Season premiere
*   **finale** _string_ -- Season finale
*   **airDate** _array_ --Array containing date aired and date ended
*   **season\_id** _int_ -- Id used to fetch data
*   **episodes\_name** _array_ -- Array containing names of episodes in season

### Episodes

The episode endpoint responds with different episodes of the Game Of Thrones show

#### Endpoints

*   **/episodes/** -- returns all episodes data
*   **/episodes/:id/** -- returns episode data with specific id

#### Example

```
curl "https://omarko-got-api.onrender.com/episodes/2/"
```

#### Response

```
{
            "characters": [
            "Viserys Targaryen",
            "Catelyn Stark",
            "Cersei Lannister",
            "Jaime Lannister",
            "Eddard Stark",
            "Robert Baratheon",
            "Jorah Mormont",
            "Daenerys Targaryen",
            ...
            ]
            "director": "Tim Van Patten",
            "airDate": "2011-04-24",
            "season": 1,
            "name": "The Kingsroad",
            "predecessor": "Winter Is Coming",
            "successor": "Lord Snow",
            "total_episodes": 2,
            "episode": 2,
            "episode_id": 2
}
```

#### Attributes

*   **characters** _array_ -- Array of characters in this episode
*   **director** _string_ -- Director of episode
*   **airDate** _string_ -- Date episode aired
*   **Season** _int_ -- Season episode belongs to
*   **name** _string_\-- Name of episode
*   **predecessor** _string_ -- Previous episode
*   **successor** _string_ -- Next episode
*   **total\_episodes** _int_ -- Total episode number in all seasons
*   **episode** _int_ -- Episode number in season it belongs to
*   **episode\_id** _int_ -- Episode Id used to fetch data
