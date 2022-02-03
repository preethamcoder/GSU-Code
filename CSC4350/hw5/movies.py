import requests
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

media = 'movie'
time = 'week'
API_KEY = os.getenv('API_KEY')

url = f'https://api.themoviedb.org/3/trending/{media}/{time}?api_key={API_KEY}'
response = requests.get(url).json()
print(f"Trending {media}s this {time} are: \n") 
for each in range(len(response['results'])):
	print(response['results'][each]['original_title'])
