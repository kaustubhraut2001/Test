import asyncio
import aiohttp
from bs4 import BeautifulSoup
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()
db_connection_string = os.getenv('MONGO_URI')
db_Collection = os.getenv('COLLECTION')
db_client = os.getenv('CLIENT')


print(db_connection_string)

async def scrape_store_info(url):
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=60)) as session:
        async with session.get(url) as response:
            content = await response.text()

    soup = BeautifulSoup(content, 'html.parser')

    stores = []
    store_list = soup.find_all('div', class_='store-block')

    for store in store_list:
        name = store.find('h3').text.strip()
        address = store.find('p', class_='address').text.strip()
        city = store.find('p', class_='city').text.strip()
        pincode = store.find('p', class_='pincode').text.strip()

        store_info = {
            'name': name,
            'address': address,
            'city': city,
            'pincode': pincode
        }

        stores.append(store_info)

    return stores

async def insert_stores_into_database(stores):
    client = AsyncIOMotorClient(db_connection_string)
    db = client[db_client]
    collection = db[db_Collection]
    await collection.insert_many(stores)
    client.close()

async def main():
    url = 'https://www.shoppersstop.com/store-finder'
    stores = await scrape_store_info(url)
    await insert_stores_into_database(stores)

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
