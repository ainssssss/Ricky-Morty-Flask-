import requests
import re
def GetAllOrigen():
    all_locations = []
    url_format = "https://rickandmortyapi.com/api/location/"
    for _ in range(1,126):
        url_format += str(_) + ","
    page = requests.get(url_format).json()
    for _ in range(1,10000):
        try:
            locations_id = page[_]['id']
            name = page[_]['name']
            character_info = {
                "locations_id":locations_id,
                "name":name,
            }
            all_locations.append(character_info)
        except:
            break
    return all_locations
def LookForSomeCharacters_from_Querry(characters_name):
    all_characters_list = []
    url_format = "https://rickandmortyapi.com/api/character/?name={}".format(characters_name)
    page = requests.get(url_format).json()
    for _ in range(0,10000):
        try:
            id_character = page['results'][_]['id']
            name = page['results'][_]['name']
            image = page['results'][_]['image']

            character_info = {
                "id":id_character,
                "name":name,
                "image":image,
            }
            all_characters_list.append(character_info)
        except:
            break

    query_search_results_characters = {
        "querry":characters_name,
        "characters_information":all_characters_list,
    }
    return query_search_results_characters
def GetAllCharacters():
    all_characters = []
    url_format = "https://rickandmortyapi.com/api/character/"
    for _ in range(1,826):
        url_format += str(_) + ","
    page = requests.get(url_format).json()
    for _ in range(0,10000):
        try:
            character_id = page[_]['id']
            name = page[_]['name']
            image = page[_]['image']
            character_info = {
                "character_id":character_id,
                "name":name,
                "image":image,
            }
            all_characters.append(character_info)
        except:
            break
    return all_characters
def GetAllLocations():
    all_locations = []
    url_format = "https://rickandmortyapi.com/api/location/"
    for _ in range(1,126):
        url_format += str(_) + ","
    page = requests.get(url_format).json()
    for _ in range(0,10000):
        try:
            name = page[_]['name']
            character_info = {
                "locations_id":_,
                "name":name,
            }
            all_locations.append(character_info)
        except:
            break
    return all_locations
def GetOneLocationInfo(location_id):
    residentes_list = []
    page = requests.get("https://rickandmortyapi.com/api/location/{}".format(str(location_id))).json()
    name = page['name']
    type = page['type']
    dimension = page['dimension']

    for _ in range(1,1000):
        try:
            resident_info = page['residents'][_]
            look_for_number = re.findall(r'\d+', resident_info)
            for _ in look_for_number:
                residentes_list.append(_)
        except:
            None
    url_characters_format = "https://rickandmortyapi.com/api/character/"
    for _ in residentes_list:
        url_characters_format += _ + ","
    page = requests.get(url_characters_format).json()
    residents_info = []


    for _ in range(1,1000):
        try:
            id_character = page[_]['id']
            name = page[_]['name']
            image = page[_]['image']
            character_information = {
                    "id_character": id_character,
                    "name": name,
                    "image": image,
            }
            residents_info.append(character_information)

        except:
            break

    location_information = {
                "id_location":location_id,
                "name": name,
                "type": type,
                "dimension": dimension,
                'residents_list':residents_info,
    }


    return location_information
def GetCharacterInformation(location_id):
    residentes_list = []
    page = requests.get("https://rickandmortyapi.com/api/character/{}".format(str(location_id))).json()
    character_name = page['name']
    status = page['status']
    image = page['image']
    species = page['species']
    type = page['type']
    gender = page['gender']
    origen = page['origin']['name']

    for _ in range(0,1000):
        try:
            resident_info = page['episode'][_]
            look_for_number = re.findall(r'\d+', resident_info)
            for _ in look_for_number:
                residentes_list.append(_)
        except:break

    url_characters_format = "https://rickandmortyapi.com/api/episode/"
    for _ in residentes_list:
        url_characters_format += _ + ","
    page = requests.get(url_characters_format).json()
    episode_info = []


    for _ in range(0,1000):
        try:
            id_character = page[_]['id']
            name = page[_]['name']
            character_information = {
                    "id_character": id_character,
                    "name": name,
            }
            episode_info.append(character_information)

        except:
            break

    location_information = {
                "id_character":location_id,
                "name": name,
                "character_name":character_name,
                "type": type,
                "status": status,
                "species": species,
                "type": type,
                "image":image,
                "gender": gender,
                "origen": origen,
                'episode_info':episode_info,
    }
    return location_information