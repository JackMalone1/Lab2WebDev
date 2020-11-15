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


@app.route("/AssassinsCreed")
def display_assassins_creed():
    return render_template("AssassinsCreed.html",
                           pageTitle="Assassin's Creed")


def display_god_of_war():
    return render_template("GOW.html",
                           pageTitle="God of War")


def display_final_fantasy():
    return render_template("DFFOO.html",
                           pageTitle="Dissidia Final Fantasy Opera Omnia")


if __name__ == '__main__':
    app.run(debug=True)
