import requests
import json

flickr_api = "9660665549dbab8ae3fe23837693f4db"
#secret = "31cb6600b9855822"

def flickr_search(query):
    api_key = flickr_api
    url = 'https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=' + api_key
    search_input = query.replace(" ","+")
    final_url = url + "&text=" + search_input + "&format=json&nojsoncallback=1"
    r = requests.get(final_url)
    data = r.json()
    #json_obj = response.read()
    #data = json.load(json_obj)
    #for photo in data['photos']:
    #    print (data['photo']['id'])
    print (data)


flickr_search("Monterey")