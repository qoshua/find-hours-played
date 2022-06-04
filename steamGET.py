import requests
import json

appid = '' # App ID of the game you want to get the playtime of
key = '' # Steam Web API Key
steamid = '' # Steam Profile 64bit ID

# api-endpoint
steam_url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"
# defining a params dict for the parameters to be sent to the API
PARAMS = { 'key' : key, 'steamid' : steamid }


# sending get request and saving the response as response object
r = requests.get(url = steam_url, params = PARAMS)
# extracting data in json format
data = r.json()
data = data['response']['games']

def get_playtime(data):
    for i in data:
        if i['appid'] == int(appid):
            print(i['playtime_forever'])
            playtime_forever = i['playtime_forever']
            return playtime_forever

hours = get_playtime(data) / 60
print(hours)
print(int(hours))



