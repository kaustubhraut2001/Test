import googlemaps
from pymongo import MongoClient
from dotenv import load_dotenv


client = MongoClient('MONGO_URI')
db = client['CLIENT']
collection = db['COLLECTION']

api_key = 'GOOGLE_API'
gmaps = googlemaps.Client(api_key)

stores = collection.find()

for store in stores:
    address = store['address'] + ', ' + store['city'] + ', ' + store['pincode']
    geocode_result = gmaps.geocode(address)

    if geocode_result:
        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']

        if lat == store['latitude'] and lng == store['longitude']:
            print(f"Location for store '{store['name']}' matches.")
        else:
            print(f"Location for store '{store['name']}' does not match.")
    else:
        print(f"No location found for store '{store['name']}'.")

client.close()
