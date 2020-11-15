from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def display_main_page():
    return render_template("index.html",
                                        pageTitle="Home")

@app.route("/CV")
def display_cv():
    return render_template("CV.html",
                                        pageTitle="CV")

@app.route("/PersonalPage")
def display_about():
    return render_template("PersonalPage.html",
                                        pageTitle="PersonalPage")

@app.route("/FavouriteGames")
def display_favourite_games():
    return render_template("FavouriteGames.html",
                                        pageTitle="Favourite games")

@app.route("/Interests")
def display_interests():
    return render_template("Interests.html",
                                        pageTitle="My Interests")

if __name__ == '__main__':
    app.run(debug=True)