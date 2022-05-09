## Milestone 3

This project milestone allowed us to have users edit their ratings of movies and delete reviews at will. 

# Installation
1. Clone this repo by running: `git clone https://github.com/csc4350-sp22/milestone3-sthelluri1.git`
2. Use `cd milestone3-sthelluri1` to change into the directory.
3. To install requirements, go to the command line and execute: `pip3 install -r requirements.txt`
4. Create a `.env` file in the directory and add your keys for `TMDB_API_KEY`,  `DATABASE_URL`, and `session_key`. The last one does not have anything to do with APIs, so it is a random string.
5. We will reference getting APIs in a different part.
6. To run the app, run `npm run build` and then `python3 routes.py`.

# APIs:
1. Follow instructions at https://developers.themoviedb.org/3/getting-started/introduction to set up the TMDB account.
2. Sign up for Heroku account at https://devcenter.heroku.com/start and click **"sign up"**.

# How to get database key?
1. Create a directory.
2. Run `git init` and `heroku create` to start the app.
3. Run `heroku addons:create heroku-postgresql:hobby-dev` to add a database.
4. Run `heroku config` to get the database url.
5. Before copying the url, make sure to change `"postgres"` to `"postgresql"` in the link.

# Techinical issues
1. `Updating the scores in the app`: This was among the hardest problems I solved. I had to make sure that the number was updated in the database. Initially, I used old SQL workbench knowledge to create a cursor and execute queries. But I later realized that the problem was way simpler. All I had to do was fetch the data and update a specific field in it.
2. `Rendering contents on app.js`: This was another issue where I had to spend a lot of time. I did not have enough methods to process all the different fields in the output. I then created my methods and states to process it all. I also had problems with the bind function, which I fixed after looking at the documentations. I then added 2 buttons to handle saving and deleting separately.
3. `Deleting reviews based on name`: I initially took a wrong approach on this problem. I figured out that I had to use the db.session.delete(), but I was using the wrong query id. I was initally looking up the comments by the username, which caused ambiguity on which comments had to be deleted and which ones had to be kept. The app kept deleting all the comments. I later realized that every single review had a unique id, which it could be accessed by. I then quieried every review with the id and was able to delete the given rating.

# Hardest part and Most valuable learning
The hardest part about this project was the setup and restarting from project 2. I tried to build upon my own app, but the logic was far too complicated. I decided to use the sample solution with all working modules to build upon. I had to write logics for almost every major action, as I was not happy with certain pieces. Writing up the App.js was challenging, as we did not process whole forms of data there. I had to pass a list into the use state. I am also not very experienced with processing json data, so getting it to work was challenging. I finally processed jason data by taking it as pieces of a list of dictionaries.

The most valuable learning in this project journey was how to integrate front and back end using javascript. I am now a lot better with writing usestates and using useeffects. I can now write fulls tack applications. Style sheets have a weird syntax, but I learned the basic attributes and div in the htmls which need to be handled. I am normally one who is good with backend development, but now I know how to write html, css, and javascript code too. Learning this has added a new skill to my arsenal, and has opened up my opportunities to work. 
