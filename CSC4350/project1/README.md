# Movie Explorer

This is a web app that randomly picks a movie and displays its details - poster, movie name, movie tagline, movie genre(s), and a link to its Wikipedia page.

Technologies used: **Python (Flask), HTML, CSS, and Heroku**.

Libraries used: **_Flask, OS, Requests, and random_**. 

The TMDB (The Movie Database) API was used to get all information about the movie, except its Wikipedia page. Wikipedia API was used to extract the page id of the movie and finally render the Wikipedia page. 

# Copy the code onto your personal machine

1. Create a new repository with a name of your choice.
2. Clone **this** repository, using the command: `git clone https://github.com/csc4350-sp22/project1-sthelluri1.git`
3. Move to the cloned repository using `cd <repo-name>`.
4. Now, the connection must be made between the cloned and your personal repository. Use `git remote set-url origin https://www.github.com/<your-username>/<your-repo-name>.git`.
5. Execute `git push origin master` to push the local repository code to the remote one. 

# Sign up for accounts:
1. Follow instructions at https://developers.themoviedb.org/3/getting-started/introduction to set up the TMDB account.
2. Sign up for Heroku account at https://devcenter.heroku.com/start and click **"sign up"**.

# Install Requirements
1. `pip3 install -r requirements.txt`

# Setup

1. Create a `.env` file and add your TMDB API key to it, in this format: `API_KEY='<key>'`
2. On line 19, in `app.py`, change the list to include any movies you like.
3. No further chanegs are needed, as the port and host are already added as arguments to the app.run().

# Web-app - deployed version

In case you want a working sample, feel free to chek it out here: https://cryptic-reef-73946.herokuapp.com/
Reload the page to see different movies.

# Challenge encountered

1. `Deploying the app to Heroku`. I faced this issue after I was done with the local development. Initially, I refered to the Heroku documentation and used the commands to deploy the app. Consequently, I received the error: "Exited with error code 3." I researched about the error and realized that some key was missing in the app. I went to the Heroku app page and addded my TMDB API key as a config vars key.

2. `Extracting genres of the movie`. Initially, I struggled to find the genres from the base url, as it only provided ids of the genre(s). I searched the Genre extracter from TMDB and found an url that would output genres based on the id number. I tested it out with one value, and it worked. I then tried a lsit of values, which caused it to fail. Finally, I used a for loop to loop through genre values and made a list of genres. I joined them using the `', '.join(<list>)` call.

3. `Fetching tagline of the movie`. When I looked through the GET API of TMDB, I could not find anything called "tagline." I mistook it for "overview" and was confused for a while. Later, I queried Google with "tagline tmdb api." I came across a "movie id information" finder on the TMDB site. I extracted the movie id from the base url and then used it to find the tagline with the movie information api.

# Existing problems and possible modifications

1. `User input`. I would like to change the homepage to a "POST" request page, so that the user can query a movie of his/her choice. I will implement an HTML form to grab user input, and then I will pass the input through the movie finder api. I will then extract the first result in the "results" dictionary and process that information.

2. `CSS aesthetics`. Although my styling has been decent, I would like to improvise it with a background image and more radial/conical gradients. I currently have a linear gradient, but it can be better with more styles. I would also like to add some 3-D effects to images, and I will do that using the img tag styling in CSS. Using more different fonts in a **pattern** (unlike the current randomness), I would like to make the user experience better. 

3. `Trailer/Teaser provision`. I want my app to be able to provide the user with a sample trailer/teaser video to get a feel of the movie. I would do this using the YouTube search API, where I can have the program automatically search the movie and return results. I would embed this using the media and video CSS aspects. This would help the user to confirm if that was the movie he/she was looking for.

# Deploy to Heroku - if needed

1. Set up a Heroku account as mentioned in the **"Sign up for accounts"** section.
2. Download the Heroku CLI from this page: https://devcenter.heroku.com/articles/getting-started-with-python#set-up.
3. Use `heroku login` to sync the logs in your command line.
4. Clone your repository using `git clone <git repository.git>`
5. Change to the directory using `cd <git repository name>`.
6. Create a `requiremnts.txt` file with the libraries you need. Additionally, create a `Procfile` with `web: python app.py` if the files don't already exist in your repository.
7. Git add and commit all the files.
8. Create a heroku app using `heroku create`.
9. Push the code to heroku using `git push heroku master`. If an error occurs, fix it using `heroku buildpacks:set heroku/python`.
10. Add your API key to heroku under the "config vars" section on your app's page.
11. Execute `heroku open` to view your web-app!
