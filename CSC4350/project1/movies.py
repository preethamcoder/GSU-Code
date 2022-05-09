import requests
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

media = 'movie'
time = 'day'
API_KEY = os.getenv('API_KEY')
gen_url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=en-US'
url = f'https://api.themoviedb.org/3/trending/{media}/{time}?api_key={API_KEY}'
genre_response = requests.get(gen_url).json()
response = requests.get(url).json()
print(f"Trending {media}s this {time} are: \n") 
for each in range(len(response['results'])):
	print(response['results'][each]['original_title'])
	genres = response['results'][each]['genre_ids']
	img_path = response['results'][each]['poster_path']
	img_url = img_url = f'https://image.tmdb.org/t/p/w500{img_path}'
	id = response['results'][each]['id']
	tagline_url = f'https://api.themoviedb.org/3/movie/{id}?api_key={API_KEY}&language=en-US'
	tagline_resp = requests.get(tagline_url).json()
	tl = tagline_resp['tagline']
	gen_list = []
	for each in genres:
		for gen in genre_response['genres']:
			if each == gen['id']:
				gen_list.append(gen['name'])
	print(', '.join(gen_list))
	print(tl)
	print(img_url, end = '\n\n')
