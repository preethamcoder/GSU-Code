# Movie-Review App

This is a web app that allows the user to search and critique movies. A poster and a link to the Wikipedia page is provided too. 
Technologies used: **Python(Flask), HTML, CSS, Heroku, SQLAlchemy (database)**
The TMDB API was used to search the movie, Wikipedia API was used to get the Wikipedia page, and hashing was used for eccryption.

# Copy the code onto your personal machine

1. Create a new repository with a name of your choice.
2. Clone **this** repository, using the command: `git clone https://github.com/csc4350-sp22/project2-sthelluri1.git`
3. Move to the cloned repository using `cd <repo-name>`.
4. Now, the connection must be made between the cloned and your personal repository. Use `git remote set-url origin https://www.github.com/<your-username>/<your-repo-name>.git`.
5. Execute `git push origin master` to push the local repository code to the remote one. 

# Sign up for accounts:
1. Follow instructions at https://developers.themoviedb.org/3/getting-started/introduction to set up the TMDB account.
2. Sign up for Heroku account at https://devcenter.heroku.com/start and click **"sign up"**.

# Install Requirements
1. `pip3 install -r requirements.txt`

# Setup
1. Create a `.env` file and add your TMDB API key to it, in this format: `API_KEY='<key>'`. After that, make sure to add your database key in the form `database='<key>'`.
2. No further chanegs are needed, as the port and host are already added as arguments to the app.run().

# Web-app - deployed version
In case you want a working sample, feel free to chek it out here: https://secret-peak-47148.herokuapp.com/
Follow instructions on the site to see what the app can do.

# How to get database key?
1. Create a directory.
2. Run `git init` and `heroku create` to start the app.
3. Run `heroku addons:create heroku-postgresql:hobby-dev` to add a database.
4. Run `heroku config` to get the database url.
5. Before copying the url, make sure to change `"postgres"` to `"postgresql"` in the link.

# Technical issues
1. `Unable to render reviews page`: I was unable to render the reviews page after getting the list of movies to be chosen from. The images were not redirecting to the right place. I spent a lot of time debugging this, but did not realize that I misspelled the path in multiple places. I was able to fix this by creating another redirect function and fixing the spelling errors. The redirect function was able to create a custom url every time I needed it, reducing my effort. I did not need to add dynamic URLs.
2. `E10 on Heroku`: This was an error triggered by my own stupidity. I deleted my local version of the code after pushing it to github, which resulted in me losing my .env file. Due to that, I was not able to access the database's key, which caused an error in the app - as it did not know which database to talk to. In the end, I navigated through the "Data" section of my heroku profile and found both my databases (both milestones). I then extracted the key from there and pasted it in the config vars section.
3. `Extracting every movie`: I initially wanted to make something similar to milestone-1, but I was not able to get the randomizer to stay the the page after the review. When it did stay, it defeated the purpose of the randomizer. So, I decided to give the user the ability to search through the movies they wanted to reivew. Using the original link, I only got one movie. I used another search API to get a list of relavant movies. I extracted information through the dictionaries and used the 0th index to get page 1.

# Experience difference
Initially I thought I could just build over milestone-1. However, I realized the randomizer would not be used the way it is supposed to be. I decided to revamp my app completely, to make it user-friendly. It was challenging to revamp the design and find the new resources to use. I had to research and debug for hours together to get a functional app. A lesson learned is to implement bare-bones of the app before committing to an idea.

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
10. Add your keys to heroku under the "config vars" section on your app's page.
11. Execute `heroku open` to view your web-app!
