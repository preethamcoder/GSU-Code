from flask import Flask, render_template, jsonify, Blueprint
import random
app = Flask(__name__)

# set up a separate route to serve the index.html file generated
# by create-react-app/npm run build.
# By doing this, we make it so you can paste in all your old app routes
# from Milestone 2 without interfering with the functionality here.
bp = Blueprint(
    "bp",
    __name__,
    template_folder="./static/react",
)

# route for serving React page
@bp.route("/")
def index():
    # NB: DO NOT add an "index.html" file in your normal templates folder
    # Flask will stop serving this React page correctly
    return render_template("index.html")

@bp.route("/fun_fact", methods=["GET", "POST"])
def fact():
    says = ["The polar bear is black, not white!", "Glass is white, not colorless!", "You are less dumb, not intelligent!", "You aren't boring, you are just less interesting!"]
    ret = random.choice(says)
    return jsonify(ret)

app.register_blueprint(bp)
app.run()