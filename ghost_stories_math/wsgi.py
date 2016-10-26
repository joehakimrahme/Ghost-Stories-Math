import flask

from ghost_stories_math import Exorcism


def create_app():
    app = flask.Flask(__name__)

    @app.route("/")
    def index():
        return flask.render_template("index.html",
                                     dice=4,
                                     resistance=1,
                                     exorcism=None)

    @app.route("/exorcism")
    def exorcism():
        dice = int(flask.request.args.get("dice"))
        resistance = int(flask.request.args.get("resistance"))
        second_wind = flask.request.args.get("Second Wind") == "sw"
        nameless = flask.request.args.get("Nameless") == "nm"

        powers = []
        if second_wind:
            powers.append("Second Wind")
        if not nameless:
            powers.append("Wild White")
        exorcism = Exorcism(dice, powers)
        return flask.render_template("index.html",
                                     dice=dice,
                                     resistance=resistance,
                                     exorcism=exorcism)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
