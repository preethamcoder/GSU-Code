'''
@author: Preetham Thelluri
This is a flask app that interacts with The Movie Database and the wikipedia APIs.
It shows the genres, tagline, image, and the wikipedia page of the movie, along with the name.
'''
import random
import os
import requests
from flask import Flask, render_template
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

app = Flask(__name__)
API_KEY = os.getenv('API_KEY')

@app.route("/")
def index():
    '''This is the main function which hosts the webpage.'''
    my_movies = ['Fight Club', 'Jack Reacher: Never Go Back', 'John Wick', "The Tomorrow War", "Captain America: The Winter Soldier", "The Amazing Spiderman"]
    movie = random.choice(my_movies)
    url = f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&language=en-US&query={movie}&page=1&include_adult=false'
    wiki_result = get_wiki(movie)
    response = requests.get(url).json()
    gen_url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=en-US'
    genre_response = requests.get(gen_url).json()
    movie_id = response['results'][0]['id']
    tagline_url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US'
    tagline_resp = requests.get(tagline_url).json()
    tag_line = tagline_resp['tagline']
    gen_list = []
    genres = response['results'][0]['genre_ids']
    for each in genres:
        for gen in genre_response['genres']:
            if each == gen['id']:
                gen_list.append(gen['name'])
    res_genres = ', '.join(gen_list)
    img_path = response['results'][0]['poster_path']
    img_url = f'https://image.tmdb.org/t/p/w500{img_path}'
    return render_template("index.html", mov=movie, genres=res_genres, image_url=img_url, tagline=tag_line, wiki_res=wiki_result)

def get_wiki(movie_name):
    '''This function gets the link of the wikipedia page of the movie. If the movie does not have a Wikipedia page, a friendly error page is shown.'''
    wiki_url = "https://en.wikipedia.org/w/api.php"
    wiki_params = {
    "action": "query",
    "titles":movie_name,
    "format":"json",
    }
    output = requests.get(wiki_url, wiki_params)
    page_id= list(output.json()['query']['pages'])[0]
    if page_id != -1:
        return f"http://en.wikipedia.org/?curid={page_id}"
    return render_template("error.html")


if __name__ == '__main__':
    app.run(os.getenv("IP", "0.0.0.0"), port=int(os.getenv("PORT", "8080")), debug=True)
