import requests
import json
import random
from PIL import Image
import urllib.request

def flickr_search(query):
    flickr_api = "9660665549dbab8ae3fe23837693f4db"
    #initialize variables to be empty
    results = []
    data = ''
    url = ''
    search_input = ''
    one_picture = ''
    list_of_urls = []
    final_picture = ''
    final_url = ''
    really_final_url = ''
    really_really_final_url = ''

    api_key = flickr_api
    #building the url that will return the search results
    url = 'https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=' + api_key
    search_input = query.replace(" ","+")
    final_url = url + "&text=" + search_input + "&sort=relevance&format=json&nojsoncallback=1"
    r = requests.get(final_url)
    data = r.json()
    for photo in data['photos']['photo']:
        results.append(photo['id'])
        #results now has a list of picture IDs that was returned by the Flickr API
        #each ID is for a unique picture
    one_picture = random.choice(results)
    #picks a picture at random
    get_picture_url = 'https://api.flickr.com/services/rest/?method=flickr.photos.getSizes&api_key=' + flickr_api + '&photo_id=' + one_picture + '&format=json&nojsoncallback=1'
    #get_picture_url then creates the url using the ID
    #that was choosen at random
    r2 = requests.get(get_picture_url)
    final_picture = r2.json()
    for my_url in final_picture['sizes']['size']:
        list_of_urls.append(my_url['source'])
        #list_of_urls has a list of all the possible sizes (Large,Medium,Original,thumbnail...) we can get for the picture
    really_really_final_url = list_of_urls[3]
    #gets the last url which is for the Original size the picture was taken at
    #with urllib.request.urlopen(really_really_final_url) as url:
    #    with open('temp.jpg','wb') as f:
    #        f.write(url.read())
    #img = Image.open('temp.jpg')
    #img.show()
    #create an Image object with the picture and present it
    return really_really_final_url
    #also prints out the url for the picture we just presented